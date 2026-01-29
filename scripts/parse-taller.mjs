#!/usr/bin/env node
/**
 * parse-taller.mjs
 * 
 * Parsea un archivo Markdown de taller directo (sin frontmatter).
 * Extrae título del H1, área de la carpeta, preguntas del contenido.
 */

import { readFileSync } from 'fs';
import { basename, dirname } from 'path';

/**
 * Parsea un taller desde un archivo Markdown
 * @param {string} filePath - Ruta al archivo .md
 * @returns {Object} Taller estructurado
 */
export function parseTallerMarkdown(filePath) {
    let content = readFileSync(filePath, 'utf-8');
    const fileName = basename(filePath, '.md');
    const area = basename(dirname(filePath)); // Carpeta padre = área

    // Eliminar frontmatter si existe (para compatibilidad con ediprof)
    content = content.replace(/^---\n[\s\S]*?\n---\n/, '');

    // Extraer título del primer H1
    const titleMatch = content.match(/^#\s+(.+)$/m);
    const titulo = titleMatch ? titleMatch[1].trim() : fileName;

    // Extraer sección de Resumen (## Resumen...) si existe ANTES de la primera pregunta
    let resumen = null;
    const resumenMatch = content.match(/^##\s+Resumen[^\n]*\n([\s\S]*?)(?=\n##\s+\d+\.|\n---)/m);
    if (resumenMatch) {
        resumen = resumenMatch[0].trim();
    }

    // Dividir por bloques de contexto (separados por ---)
    // PERO también detectar bloques de contexto compartido sin separador
    // Ejemplo: "<!-- imprimible: ancho-completo -->\n\nRESPONDA LAS PREGUNTAS..."
    
    // Primero, normalizar: agregar --- antes de bloques de contexto compartido
    content = content.replace(
        /(<!-- imprimible: ancho-completo -->\s*\n+RESPONDA LAS PREGUNTAS)/g,
        '\n---\n\n$1'
    );

    const sections = content.split(/\n---\n/).filter(s => s.trim());

    const bloques = [];
    let currentBloque = null;
    let numeroGlobal = 0;
    let contextoCompartido = ''; // Para manejar contextos que aplican a múltiples preguntas

    for (const section of sections) {
        // Verificar si la sección comienza con una pregunta
        // Soportar ambos formatos: "## 1." (banco-saber) y "## Pregunta 1" (ediprof)
        let isQuestion = section.match(/^\s*##\s*(\d+\.|Pregunta\s+\d+)/m);

        // Verificar si hay un contexto compartido (texto antes de la primera pregunta)
        // Ejemplo: "RESPONDA LAS PREGUNTAS 9 A 11..."
        const contextBeforeQuestion = section.match(/([\s\S]*?)(?=\n##\s*(\d+\.|Pregunta\s+\d+))/);
        if (contextBeforeQuestion && contextBeforeQuestion[1].trim()) {
            contextoCompartido = contextBeforeQuestion[1].trim();
        }

        if (isQuestion) {
            // Si es pregunta, puede haber MÚLTIPLES preguntas en este bloque si no usaron separadores ---
            // Dividimos por "## numero." o "## Pregunta numero"

            const rawQuestions = section.split(/\n(?=##\s*(\d+\.|Pregunta\s+\d+))/);

            for (const qRaw of rawQuestions) {
                // Verificar que sea realmente una pregunta (puede haber basura al inicio si el split falló)
                if (qRaw.match(/^##\s*\d+\./) || qRaw.match(/^\s*##\s*\d+\./) || 
                    qRaw.match(/^##\s*Pregunta\s+\d+/) || qRaw.match(/^\s*##\s*Pregunta\s+\d+/)) {
                    numeroGlobal++;
                    // Importante: parsePregunta espera el texto crudo de esa pregunta
                    const pregunta = parsePregunta(qRaw, numeroGlobal);

                    // Si hay contexto compartido y es la primera pregunta del bloque, crear nuevo bloque
                    if (contextoCompartido && (!currentBloque || currentBloque.contexto !== contextoCompartido)) {
                        if (currentBloque && currentBloque.preguntas.length > 0) {
                            bloques.push(currentBloque);
                        }
                        currentBloque = { contexto: contextoCompartido, preguntas: [] };
                    }

                    if (!currentBloque) {
                        currentBloque = { contexto: '', preguntas: [] };
                    }
                    currentBloque.preguntas.push(pregunta);
                }
            }
            // Resetear contexto compartido después de procesar las preguntas
            contextoCompartido = '';

        } else {
            // Es un bloque de contexto puro (sin preguntas)
            if (currentBloque && currentBloque.preguntas.length > 0) {
                bloques.push(currentBloque);
            }
            currentBloque = {
                contexto: section.replace(/^#\s+.+\n/, '').trim(), // Quitar título principal
                preguntas: []
            };
            contextoCompartido = currentBloque.contexto;
        }
    }

    // Agregar último bloque
    if (currentBloque && currentBloque.preguntas.length > 0) {
        bloques.push(currentBloque);
    }

    // Detectar si es estructura de carpeta (taller.md dentro de carpeta)
    // o archivo suelto (old style)
    const tallerDir = fileName === 'taller' ? dirname(filePath) : dirname(filePath);
    const tallerId = fileName === 'taller' ? basename(dirname(filePath)) : fileName;

    return {
        id: tallerId,
        titulo,
        resumen,  // Nueva propiedad para contenido introductorio
        tallerDir, // Ruta a la carpeta del taller (para imágenes locales)
        meta: {
            area,
            unidad: tallerId,
            tiempo_sugerido: Math.max(10, numeroGlobal * 3)
        },
        bloques,
        totalItems: numeroGlobal
    };
}

/**
 * Parsea una sección de pregunta
 */
function parsePregunta(section, numeroGlobal) {
    const lines = section.split('\n');

    // Detectar si requiere ancho completo (ANTES de procesar)
    const fullWidth = section.includes('<!-- imprimible: ancho-completo -->');

    // Extraer metadatos del comentario HTML (si existe)
    // Formato: <!-- fuente: ICFES | año: 2020 | tema: clasificación -->
    const metadatos = {};
    const metaMatches = section.matchAll(/<!--\s*([\s\S]*?)\s*-->/g);
    for (const metaMatch of metaMatches) {
        const metaContent = metaMatch[1];
        // Parsear líneas tipo YAML: "fuente: valor"
        metaContent.split('\n').forEach(line => {
            const kvMatch = line.match(/^\s*([a-zA-Z_áéíóúñ]+)\s*:\s*(.+?)\s*$/);
            if (kvMatch) {
                metadatos[kvMatch[1].toLowerCase()] = kvMatch[2].trim();
            }
        });
    }

    // Extraer texto de la pregunta (después del ## número)
    let texto = '';
    let inOpciones = false;
    const opciones = {};
    let respuestaCorrecta = '';
    let explicacion = '';
    let retroalimentacion = '';  // NUEVO: contenido con marcadores ==resaltado== y ~~tachado~~

    // Buscar el texto después del encabezado
    // Soportar ambos formatos: "## 1." y "## Pregunta 1"
    const headerIndex = lines.findIndex(l => l.match(/^##\s*(\d+\.|Pregunta\s+\d+)/));
    let inComment = false; // Rastrear si estamos dentro de un comentario HTML
    let commentBuffer = ''; // Buffer para comentarios multi-línea

    for (let i = headerIndex + 1; i < lines.length; i++) {
        const line = lines[i];

        // Manejar comentarios HTML multi-línea
        if (line.includes('<!--')) {
            inComment = true;
            commentBuffer = line;
        }
        if (inComment) {
            if (!commentBuffer) commentBuffer = line;
            else if (line !== commentBuffer) commentBuffer += '\n' + line;
            
            if (line.includes('-->')) {
                inComment = false;
                commentBuffer = '';
            }
            continue; // Saltar toda la línea si estamos en comentario
        }

        // ¿Es opción?
        const opcionMatch = line.match(/^\s*-\s*([A-D])\.\s*(.+)$/);
        if (opcionMatch) {
            inOpciones = true;
            opciones[opcionMatch[1]] = opcionMatch[2].trim();
            continue;
        }

        // ¿Es inicio de respuesta?
        if (line.includes('<details>')) {
            // Buscar respuesta correcta
            const restContent = lines.slice(i).join('\n');
            const respMatch = restContent.match(/\*\*Respuesta:\s*([A-D])\*\*/);
            if (respMatch) {
                respuestaCorrecta = respMatch[1];
            }

            // Extraer retroalimentación (contenido entre </summary> y **Respuesta:**)
            // Esto es donde van los marcadores ==resaltado== y ~~tachado~~
            const retroMatch = restContent.match(/<\/summary>\s*\n+([\s\S]*?)(?=\n\*\*Respuesta:)/);
            if (retroMatch && retroMatch[1].trim()) {
                // Limpiar comentarios HTML de la retroalimentación
                retroalimentacion = retroMatch[1].trim()
                    .replace(/<!--\s*RETROALIMENTACIÓN CON MARCADORES\s*-->/g, '')
                    .trim();
            }

            // Extraer explicación (contenido después de **Respuesta: X**)
            const explMatch = restContent.match(/\*\*Respuesta:\s*[A-D]\*\*\s*\n+([\s\S]*?)<\/details>/);
            if (explMatch) {
                explicacion = explMatch[1].trim();
            }
            break;
        }

        // Es texto de la pregunta (mantener líneas vacías para Markdown/Tablas)
        if (!inOpciones) {
            texto += (texto ? '\n' : '') + line;
        }
    }

    // NO limpiar comentarios del texto - los necesitamos para el contexto
    // Solo limpiar comentarios que NO sean de metadatos o layout
    texto = texto.replace(/<!--\s*RETROALIMENTACIÓN CON MARCADORES\s*-->/g, '').trim();

    // Separar CONTEXTO y ENUNCIADO automáticamente
    // Regla: El último párrafo antes de las opciones = ENUNCIADO
    //        Todo lo anterior = CONTEXTO
    let contexto = '';
    let enunciado = texto;

    // Dividir por párrafos (doble salto de línea o línea vacía)
    const parrafos = texto.split(/\n\s*\n/).filter(p => p.trim());

    if (parrafos.length > 1) {
        // El último párrafo es el enunciado
        enunciado = parrafos[parrafos.length - 1].trim();
        // El resto es contexto
        contexto = parrafos.slice(0, -1).join('\n\n').trim();
    }

    return {
        numeroGlobal,
        texto: texto.trim(),       // Mantener para compatibilidad
        contexto,                   // Todo excepto último párrafo
        enunciado,                  // Último párrafo (la pregunta)
        opciones,
        respuestaCorrecta,
        explicacion,
        retroalimentacion,          // NUEVO: Versión con marcadores ==resaltado== y ~~tachado~~
        metadatos,
        fullWidth                   // NUEVO: Indicador explícito de ancho completo
    };
}

// CLI para testing
if (import.meta.url === `file://${process.argv[1]}`) {
    if (process.argv[2]) {
        const result = parseTallerMarkdown(process.argv[2]);
        console.log(JSON.stringify(result, null, 2));
    } else {
        console.log('Uso: node parse-taller.mjs <ruta-taller.md>');
    }
}

export default parseTallerMarkdown;

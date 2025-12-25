#!/usr/bin/env node
/**
 * preprocess-markdown.mjs
 * 
 * Preprocesa archivos Markdown/MDX para exportación a Word:
 * - Extrae imports de imágenes de Astro y los convierte a markdown
 * - Convierte componentes <Image> a sintaxis markdown
 * - Convierte rutas de imagen a absolutas
 * - Convierte SVG a PNG usando Playwright
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { resolve, dirname, basename } from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const PROJECT_ROOT = resolve(__dirname, '..');

function preprocessMarkdown(inputPath, outputPath, tempImagesDir, includeImages = true) {
    let content = readFileSync(inputPath, 'utf-8');

    // ===========================================
    // 1. EXTRAER IMPORTS DE IMÁGENES DE ASTRO
    // ===========================================
    // Buscar: import varName from '/public/images/...'
    const importMap = {};
    const importRegex = /import\s+(\w+)\s+from\s+['"]([^'"]+)['"]/g;
    let importMatch;

    while ((importMatch = importRegex.exec(content)) !== null) {
        const varName = importMatch[1];
        let importPath = importMatch[2];

        // Si es una ruta de imagen
        if (importPath.includes('/images/') || importPath.match(/\.(png|jpg|jpeg|gif|svg|webp)$/i)) {
            // Normalizar la ruta (quitar /public si existe al inicio)
            if (importPath.startsWith('/public/')) {
                importPath = importPath.substring(7); // Quitar '/public'
            }
            importMap[varName] = importPath;
            console.log(`📦 Import detectado: ${varName} → ${importPath}`);
        }
    }

    // Eliminar líneas de import
    content = content.split('\n')
        .filter(line => !line.trim().startsWith('import '))
        .join('\n');

    // ===========================================
    // 2. CONVERTIR COMPONENTES <Image> DE ASTRO
    // ===========================================
    // Buscar: <Image src={varName} alt="texto" ... />
    const imageComponentRegex = /<Image\s+[^>]*src=\{(\w+)\}[^>]*alt=["']([^"']+)["'][^>]*\/>/g;
    const imageComponentRegex2 = /<Image\s+[^>]*alt=["']([^"']+)["'][^>]*src=\{(\w+)\}[^>]*\/>/g;

    // Reemplazar <Image src={var} alt="..."/> con ![alt](path)
    content = content.replace(imageComponentRegex, (match, varName, altText) => {
        if (importMap[varName]) {
            return `![${altText}](${importMap[varName]})`;
        }
        return match; // Si no encontramos el import, dejar como está
    });

    content = content.replace(imageComponentRegex2, (match, altText, varName) => {
        if (importMap[varName]) {
            return `![${altText}](${importMap[varName]})`;
        }
        return match;
    });

    // También manejar <Image> sin las llaves (ruta directa)
    content = content.replace(/<Image[^>]*src=["']([^"']+)["'][^>]*alt=["']([^"']+)["'][^>]*\/>/g,
        (match, src, alt) => `![${alt}](${src})`);
    content = content.replace(/<Image[^>]*alt=["']([^"']+)["'][^>]*src=["']([^"']+)["'][^>]*\/>/g,
        (match, alt, src) => `![${alt}](${src})`);

    // ===========================================
    // 3. PROCESAR IMÁGENES HTML (<img src="...">)
    // ===========================================
    // Las imágenes dentro de <div><img src="..." alt="..."></div> no son detectadas
    // por el regex de markdown. Primero convertimos <img> a sintaxis markdown.
    const imgTagRegex = /<img\s+[^>]*src=["']([^"']+)["'][^>]*alt=["']([^"']+)["'][^>]*\/?>/gi;
    const imgTagRegex2 = /<img\s+[^>]*alt=["']([^"']+)["'][^>]*src=["']([^"']+)["'][^>]*\/?>/gi;
    
    // Convertir <img src="..." alt="..."> a ![alt](src)
    content = content.replace(imgTagRegex, (match, src, alt) => `![${alt}](${src})`);
    content = content.replace(imgTagRegex2, (match, alt, src) => `![${alt}](${src})`);
    
    // Limpiar divs contenedores vacíos que quedaron
    content = content.replace(/<div[^>]*>\s*(\!\[[^\]]*\]\([^)]+\))\s*<\/div>/gi, '\n$1\n');

    // ===========================================
    // 4. PROCESAR IMÁGENES MARKDOWN
    // ===========================================
    const imageRegex = /!\[([^\]]*)\]\(([^)]+)\)/g;
    let match;
    const replacements = [];
    const inputDir = dirname(inputPath);

    // Resetear el regex para buscar desde el inicio
    while ((match = imageRegex.exec(content)) !== null) {
        const fullMatch = match[0];
        const altText = match[1];
        let imagePath = match[2];
        let absPath = null;

        // Manejar rutas relativas con ../
        if (imagePath.includes('../')) {
            // Resolver ruta relativa desde el archivo de entrada
            const resolvedPath = resolve(inputDir, imagePath);
            // Normalizar: si contiene /public/, extraer la parte de /images/
            if (resolvedPath.includes('/public/')) {
                const publicIndex = resolvedPath.indexOf('/public/');
                imagePath = resolvedPath.substring(publicIndex + 7); // quitar /public
                absPath = resolve(PROJECT_ROOT, 'public', imagePath.startsWith('/') ? imagePath.substring(1) : imagePath);
            } else {
                absPath = resolvedPath;
                imagePath = '/' + basename(resolvedPath);
            }
        } else {
            // Normalizar ruta (quitar /public si existe)
            if (imagePath.startsWith('/public/')) {
                imagePath = imagePath.substring(7);
            }

            // Asegurar que empiece con /
            if (!imagePath.startsWith('/') && !imagePath.startsWith('http')) {
                imagePath = '/' + imagePath;
            }
        }

        // Solo procesar imágenes locales (no URLs)
        if (imagePath.startsWith('/images/') || imagePath.startsWith('images/') || absPath) {
            // Si no tenemos absPath de ruta relativa, calcularla
            if (!absPath) {
                const cleanPath = imagePath.startsWith('/') ? imagePath.substring(1) : imagePath;
                absPath = resolve(PROJECT_ROOT, 'public', cleanPath);
            }

            if (existsSync(absPath)) {
                if (includeImages) {
                    let finalPath = absPath;

                    // Convertir SVG a PNG
                    if (imagePath.endsWith('.svg')) {
                        const pngName = basename(imagePath, '.svg') + '.png';
                        const pngPath = resolve(tempImagesDir, pngName);

                        console.log(`🎨 Convirtiendo SVG: ${basename(imagePath)}`);
                        try {
                            execSync(`node "${__dirname}/svg-to-png.mjs" "${absPath}" "${pngPath}" 1.5`, {
                                stdio: 'pipe'
                            });
                            if (existsSync(pngPath)) {
                                finalPath = pngPath;
                                console.log(`✅ PNG creado: ${pngPath}`);
                            }
                        } catch (err) {
                            console.error(`⚠️ Error convirtiendo SVG: ${err.message}`);
                        }
                    }

                    replacements.push({
                        original: fullMatch,
                        replacement: `![${altText}](${finalPath})`
                    });
                } else {
                    // Modo sin imágenes: placeholder
                    const placeholder = `\n> **📷 IMAGEN**\n>\n> *${altText}*\n>\n> 🔗 Ver en la web\n`;
                    replacements.push({
                        original: fullMatch,
                        replacement: placeholder
                    });
                }
            } else {
                console.warn(`⚠️ Imagen no encontrada: ${absPath}`);
            }
        }
    }

    // Aplicar reemplazos
    for (const { original, replacement } of replacements) {
        content = content.replace(original, replacement);
    }

    // ===========================================
    // 5. CONVERTIR LISTAS DE DATOS A LINE BLOCKS
    // ===========================================
    // Las listas con `*   $latex$` se rompen en Word
    // Convertimos a LineBlock (| línea) que Pandoc preserva correctamente
    // Esto solo aplica a listas que siguen a "**Datos:**"
    
    // Buscar bloques de "Datos:" seguidos de listas con asterisco
    content = content.replace(
        /(\*\*Datos:\*\*)\n((?:\*   .+\n?)+)/g,
        (match, header, listBlock) => {
            // Convertir cada línea de lista a formato LineBlock
            const lines = listBlock
                .split('\n')
                .filter(line => line.trim())
                .map(line => {
                    // Quitar el asterisco y espacios iniciales
                    const content = line.replace(/^\*\s+/, '').trim();
                    return `| • ${content}`;
                })
                .join('\n');
            return `${header}\n\n${lines}`;
        }
    );
    
    // También convertir listas sueltas con asterisco (no solo después de Datos:)
    // Solo si están en contexto de solución (después de <summary>)
    content = content.replace(/^\*   /gm, '- ');
    
    // ===========================================
    // 6. ESCAPAR LISTAS ALFABÉTICAS PARA QUE SEAN TEXTO PLANO
    // ===========================================
    // Esto evita que Pandoc las convierta a listas de Word
    // que luego Google Docs no interpreta bien
    // Agregamos un caracter invisible (backslash) para romper el patrón de lista
    const lines = content.split('\n');

    content = lines.map(line => {
        // Detectar lista alfabética al inicio de línea: "a) ", "b) ", "A) ", "B) "
        // Agregamos un espacio después de la letra para que no sea lista
        const alphabeticMatch = line.match(/^(\s*)([a-zA-Z])(\)\s)/);

        if (alphabeticMatch) {
            const indent = alphabeticMatch[1];
            const letter = alphabeticMatch[2];
            const rest = line.substring(alphabeticMatch[0].length);
            // Usar texto con espacio no-breaking para evitar interpretación como lista
            return `${indent}**${letter})** ${rest}`;
        }
        return line;
    }).join('\n');

    writeFileSync(outputPath, content);
    console.log(`📝 Markdown procesado: ${outputPath}`);
    return outputPath;
}

// Uso desde línea de comandos
if (process.argv.length < 4) {
    console.log('Uso: node preprocess-markdown.mjs <input.md> <output.md> [temp_images_dir] [--no-images]');
    process.exit(1);
}

const inputPath = process.argv[2];
const outputPath = process.argv[3];
const tempImagesDir = process.argv[4] || '/tmp/docx_images';
const includeImages = !process.argv.includes('--no-images');

if (!existsSync(tempImagesDir)) {
    mkdirSync(tempImagesDir, { recursive: true });
}

preprocessMarkdown(inputPath, outputPath, tempImagesDir, includeImages);

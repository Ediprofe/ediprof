#!/usr/bin/env node
/**
 * Script para generar PDFs de talleres Saber
 * Genera 3 versiones: normal, imprimible y retroalimentación
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname, basename } from 'path';
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const PROJECT_ROOT = join(__dirname, '..');

const colors = {
    reset: '\x1b[0m',
    green: '\x1b[32m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    red: '\x1b[31m',
};

function log(msg, color = 'reset') {
    console.log(`${colors[color]}${msg}${colors.reset}`);
}

/**
 * Procesa markdown a HTML
 */
function processMarkdown(text, showAnswers = false) {
    if (!text) return '';
    
    let html = text
        // Imágenes (ahora desde CDN)
        .replace(/!\[([^\]]*)\]\((https?:\/\/[^)]+)\)/g, '<div class="img-container"><img src="$2" alt="$1"></div>')
        // Negritas
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        // Tablas
        .replace(/\|(.+)\|\s*\n\s*\|([-:| ]+)\|\s*\n\s*((?:\|.+\|\s*\n?)+)/g, (match, header, separator, body) => {
            const headers = header.split('|').map(s => s.trim()).filter(s => s);
            const rows = body.trim().split(/\r?\n/).map(row =>
                row.split('|').map(s => s.trim()).filter(s => s)
            );

            let t = '<table class="data-table"><thead><tr>';
            headers.forEach(h => t += `<th>${h}</th>`);
            t += '</tr></thead><tbody>';
            rows.forEach(r => {
                t += '<tr>';
                r.forEach(c => t += `<td>${c}</td>`);
                t += '</tr>';
            });
            t += '</tbody></table>';
            return t;
        })
        // Saltos de línea
        .split(/(<div.*?<\/div>|<table.*?<\/table>)/gs).map(part => {
            if (part.startsWith('<div') || part.startsWith('<table')) return part;
            return part
                .replace(/\r?\n\s*\r?\n/g, '<div class="paragraph-break"></div>')
                .replace(/\r?\n/g, '<br>');
        })
        .join('');

    // Eliminar respuestas si no se deben mostrar
    if (!showAnswers) {
        html = html.replace(/<details>[\s\S]*?<\/details>/g, '');
    }

    return html;
}

/**
 * Parsea el taller markdown
 */
function parseTaller(mdContent) {
    const lines = mdContent.split('\n');
    const taller = {
        titulo: '',
        area: '',
        unidad: '',
        preguntas: []
    };

    // Extraer frontmatter
    if (lines[0] === '---') {
        let i = 1;
        while (i < lines.length && lines[i] !== '---') {
            const match = lines[i].match(/^(\w+):\s*(.+)$/);
            if (match) {
                const [, key, value] = match;
                if (key === 'title') taller.titulo = value.replace(/['"]/g, '');
                if (key === 'area') taller.area = value.replace(/['"]/g, '');
                if (key === 'unidad') taller.unidad = value.replace(/['"]/g, '');
            }
            i++;
        }
    }

    // Extraer preguntas
    const content = mdContent.replace(/^---[\s\S]*?---\n/, '');
    const preguntaRegex = /## Pregunta (\d+)([\s\S]*?)(?=## Pregunta \d+|$)/g;
    let match;

    while ((match = preguntaRegex.exec(content)) !== null) {
        const [, numero, contenido] = match;
        
        // Extraer texto de la pregunta (antes de las opciones)
        const textoMatch = contenido.match(/^([\s\S]*?)(?=\n[A-D]\.\s)/);
        const texto = textoMatch ? textoMatch[1].trim() : '';

        // Extraer opciones
        const opciones = {};
        const opcionRegex = /([A-D])\.\s+([\s\S]*?)(?=\n[A-D]\.\s|\n<details>|$)/g;
        let opMatch;
        while ((opMatch = opcionRegex.exec(contenido)) !== null) {
            opciones[opMatch[1]] = opMatch[2].trim();
        }

        // Extraer respuesta
        const respuestaMatch = contenido.match(/<details>[\s\S]*?<summary>.*?Ver respuesta.*?<\/summary>([\s\S]*?)<\/details>/);
        const respuesta = respuestaMatch ? respuestaMatch[1].trim() : '';

        taller.preguntas.push({
            numero: parseInt(numero),
            texto,
            opciones,
            respuesta
        });
    }

    return taller;
}

/**
 * Genera HTML base para PDF
 */
function generateHTML(taller, tipo = 'normal') {
    const showAnswers = tipo === 'feedback';
    const twoColumns = tipo === 'imprimible';

    let content = '';

    taller.preguntas.forEach((pregunta, index) => {
        const shouldBreak = index > 0;

        content += `
            ${shouldBreak ? '<div class="page-break"></div>' : ''}
            <div class="pregunta-container">
                <div class="pregunta-num">Pregunta ${pregunta.numero}</div>
                <div class="pregunta-texto">${processMarkdown(pregunta.texto, showAnswers)}</div>
                
                <div class="opciones-grid ${twoColumns ? 'two-columns' : ''}">
                    ${Object.entries(pregunta.opciones).map(([letra, texto]) => `
                        <div class="opcion-item">
                            <span class="opcion-letra">${letra}</span>
                            <span class="opcion-texto">${processMarkdown(texto, showAnswers)}</span>
                        </div>
                    `).join('')}
                </div>

                ${showAnswers && pregunta.respuesta ? `
                    <div class="respuesta-container">
                        <div class="respuesta-titulo">✅ Respuesta y Explicación</div>
                        <div class="respuesta-body">${processMarkdown(pregunta.respuesta, true)}</div>
                    </div>
                ` : ''}
            </div>
        `;
    });

    return `<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>${taller.titulo}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
      onload="renderMathInElement(document.body, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ]
      });"></script>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700&family=Open+Sans:wght@400;600;700&display=swap');
        
        body { 
            font-family: 'Merriweather', serif; 
            font-size: ${twoColumns ? '10pt' : '12pt'}; 
            line-height: 1.6; 
            color: #111;
            margin: 0;
            padding: 0;
            background: white;
        }

        .page-break { page-break-before: always; }
        .paragraph-break { height: 8px; }
        
        .header-doc { 
            text-align: center; 
            border-bottom: 2px solid #000; 
            padding-bottom: 15px; 
            margin-bottom: 20px; 
        }
        .titulo-doc { 
            font-family: 'Open Sans', sans-serif; 
            font-size: 18pt; 
            font-weight: 700; 
            text-transform: uppercase; 
        }
        .sub-doc { 
            font-family: 'Open Sans', sans-serif; 
            font-size: 10pt; 
            text-transform: uppercase; 
            letter-spacing: 1px; 
            margin-top: 5px; 
        }

        .pregunta-container { 
            margin-bottom: 15px; 
            page-break-inside: avoid;
        }
        .pregunta-num { 
            font-family: 'Open Sans', sans-serif; 
            font-weight: 700; 
            font-size: 14pt; 
            color: #000; 
            margin-bottom: 5px; 
        }
        .pregunta-texto { 
            font-size: ${twoColumns ? '10pt' : '12pt'}; 
            margin-bottom: 10px; 
        }

        .opciones-grid { 
            display: flex; 
            flex-direction: column; 
            gap: ${twoColumns ? '8px' : '10px'}; 
            page-break-inside: avoid;
        }
        .opciones-grid.two-columns {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        .opcion-item { 
            display: flex; 
            gap: 15px; 
            padding: ${twoColumns ? '8px 12px' : '10px 15px'}; 
            border: 1px solid #eee; 
            border-radius: 4px; 
            page-break-inside: avoid;
        }
        .opcion-letra { 
            font-family: 'Open Sans', sans-serif; 
            font-weight: 700; 
            min-width: 25px; 
            color: #333; 
        }
        .opcion-texto { 
            font-family: 'Open Sans', sans-serif; 
            font-size: ${twoColumns ? '9pt' : '11pt'}; 
        }

        .respuesta-container {
            margin-top: 15px;
            padding: 15px;
            background-color: #f0fdf4;
            border-left: 4px solid #22c55e;
            border-radius: 4px;
        }
        .respuesta-titulo {
            font-family: 'Open Sans', sans-serif;
            font-weight: 700;
            font-size: 12pt;
            color: #15803d;
            margin-bottom: 10px;
        }
        .respuesta-body {
            font-size: 11pt;
        }

        .data-table { 
            width: 100%; 
            border-collapse: collapse; 
            margin: 10px 0; 
            font-family: 'Open Sans', sans-serif; 
            font-size: ${twoColumns ? '9pt' : '10pt'}; 
        }
        .data-table th { 
            background: #eee; 
            border: 1px solid #333; 
            padding: 8px; 
            font-weight: 700; 
            text-align: center; 
        }
        .data-table td { 
            border: 1px solid #333; 
            padding: 8px; 
            text-align: center; 
        }

        img { 
            max-width: 100%; 
            max-height: ${twoColumns ? '300px' : '400px'}; 
            object-fit: contain;
            height: auto; 
            display: block; 
            margin: 5px auto; 
        }
        .img-container { text-align: center; }
    </style>
</head>
<body>
    <div class="header-doc">
        <div class="titulo-doc">${taller.titulo}</div>
        <div class="sub-doc">${taller.area || 'Taller Saber'} • ${taller.unidad || 'Preparación ICFES'}</div>
    </div>

    ${content}
</body>
</html>`;
}

/**
 * Genera PDF usando Playwright
 */
async function generatePDF(html, outputPath, tipo) {
    const tempHtml = outputPath.replace('.pdf', '.html');
    writeFileSync(tempHtml, html);

    try {
        const browser = await chromium.launch();
        const page = await browser.newPage();

        await page.goto(`file://${tempHtml}`, { waitUntil: 'networkidle' });
        await page.waitForTimeout(3000); // Esperar KaTeX

        await page.pdf({
            path: outputPath,
            format: 'Letter',
            printBackground: true,
            margin: { top: '1.5cm', right: '1.5cm', bottom: '1.5cm', left: '1.5cm' }
        });

        await browser.close();
        
        // Limpiar HTML temporal
        try {
            const { unlinkSync } = await import('fs');
            unlinkSync(tempHtml);
        } catch (e) {}

        return true;
    } catch (error) {
        log(`❌ Error generando PDF: ${error.message}`, 'red');
        return false;
    }
}

/**
 * Main
 */
async function main() {
    const args = process.argv.slice(2);
    
    if (args.length < 2) {
        log('Uso: node export-saber-pdf.mjs <ruta-taller.md> <directorio-salida>', 'yellow');
        process.exit(1);
    }

    const tallerPath = args[0];
    const outputDir = args[1];

    if (!existsSync(tallerPath)) {
        log(`❌ No se encontró: ${tallerPath}`, 'red');
        process.exit(1);
    }

    if (!existsSync(outputDir)) {
        mkdirSync(outputDir, { recursive: true });
    }

    log('📝 Generando PDFs de taller Saber...', 'blue');
    console.log('');

    const mdContent = readFileSync(tallerPath, 'utf-8');
    const taller = parseTaller(mdContent);
    const baseName = basename(tallerPath, '.md');

    // 1. PDF Normal
    log('  📄 Generando PDF normal...', 'cyan');
    const normalHtml = generateHTML(taller, 'normal');
    const normalPath = join(outputDir, `${baseName}.pdf`);
    await generatePDF(normalHtml, normalPath, 'normal');
    log(`     ✓ ${normalPath}`, 'green');

    // 2. PDF Imprimible (2 columnas)
    log('  📄 Generando PDF imprimible...', 'cyan');
    const imprimibleHtml = generateHTML(taller, 'imprimible');
    const imprimiblePath = join(outputDir, `${baseName}_imprimible.pdf`);
    await generatePDF(imprimibleHtml, imprimiblePath, 'imprimible');
    log(`     ✓ ${imprimiblePath}`, 'green');

    // 3. PDF Retroalimentación
    log('  📄 Generando PDF retroalimentación...', 'cyan');
    const feedbackHtml = generateHTML(taller, 'feedback');
    const feedbackPath = join(outputDir, `${baseName}_retroalimentacion.pdf`);
    await generatePDF(feedbackHtml, feedbackPath, 'feedback');
    log(`     ✓ ${feedbackPath}`, 'green');

    console.log('');
    log('✅ ¡PDFs generados exitosamente!', 'green');
}

main().catch(err => {
    log(`❌ Error: ${err.message}`, 'red');
    process.exit(1);
});

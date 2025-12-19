/**
 * svg-to-png.mjs
 * Captura SVGs como PNG usando Playwright, recortando a los límites del contenido
 */

import { chromium } from 'playwright';
import { readFileSync, existsSync, mkdirSync } from 'fs';
import { dirname, resolve } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

async function svgToPng(svgPath, outputPath, scale = 1.5) {
    const absoluteSvgPath = resolve(svgPath);
    if (!existsSync(absoluteSvgPath)) {
        console.error(`❌ SVG no encontrado: ${absoluteSvgPath}`);
        process.exit(1);
    }

    const svgContent = readFileSync(absoluteSvgPath, 'utf-8');

    // Extraer dimensiones del viewBox
    const viewBoxMatch = svgContent.match(/viewBox=["']([^"']+)["']/);
    let width = 620;
    let height = 450;

    if (viewBoxMatch) {
        const parts = viewBoxMatch[1].split(/[\s,]+/).map(Number);
        if (parts.length >= 4) {
            width = parts[2];
            height = parts[3];
        }
    }

    // HTML que renderiza el SVG centrado con fondo blanco puro
    const html = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body {
            width: ${width}px;
            height: ${height}px;
            background: #ffffff;
            overflow: hidden;
        }
        #container {
            width: ${width}px;
            height: ${height}px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        svg {
            max-width: 100%;
            max-height: 100%;
            display: block;
        }
        /* Forzar fondo blanco en el SVG */
        svg rect[fill*="gradient"], 
        svg rect[fill*="#f8fafc"],
        svg rect[fill*="#e2e8f0"] {
            fill: #ffffff !important;
        }
    </style>
</head>
<body>
<div id="container">
${svgContent}
</div>
</body>
</html>
    `;

    const outputDir = dirname(outputPath);
    if (!existsSync(outputDir)) {
        mkdirSync(outputDir, { recursive: true });
    }

    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
        viewport: {
            width: Math.ceil(width * scale),
            height: Math.ceil(height * scale)
        },
        deviceScaleFactor: scale
    });

    const page = await context.newPage();
    await page.setContent(html, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    // Capturar la pantalla completa
    await page.screenshot({
        path: outputPath,
        type: 'png'
    });

    await browser.close();
    console.log(`✅ PNG: ${outputPath} (${Math.round(width * scale)}x${Math.round(height * scale)})`);
}

const args = process.argv.slice(2);
if (args.length < 2) {
    console.log('Uso: node svg-to-png.mjs <svg_path> <output_png_path> [scale]');
    process.exit(1);
}

svgToPng(args[0], args[1], parseFloat(args[2]) || 1.5).catch(err => {
    console.error('Error:', err);
    process.exit(1);
});

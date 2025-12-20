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

    // ==========================================================
    // CONFIGURACIÓN CENTRALIZADA DE FONDO PARA EXPORTACIÓN
    // ==========================================================
    // Los SVGs del proyecto usan un fondo gris degradado (#f8fafc → #e2e8f0)
    // que debe preservarse para que los títulos con texto blanco sean legibles.
    // NO forzar fondo blanco - el SVG ya tiene su propio fondo integrado.
    // ==========================================================

    const html = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body {
            /* Fondo transparente para no interferir con el SVG */
            background: transparent;
        }
        #svg-container {
            display: inline-block;
            /* El SVG tiene su propio fondo gris degradado integrado */
            background: transparent;
            width: ${width}px;
            height: ${height}px;
        }
        svg {
            display: block;
            width: ${width}px;
            height: ${height}px;
        }
        /* 
         * NOTA: NO forzar fondo blanco aquí.
         * Los SVGs de Ediprofe tienen fondo gris degradado que debe preservarse
         * para mantener la legibilidad del texto blanco en títulos.
         */
    </style>
</head>
<body>
<div id="svg-container">
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
            width: Math.ceil(width * scale) + 100,
            height: Math.ceil(height * scale) + 100
        },
        deviceScaleFactor: scale
    });

    const page = await context.newPage();
    await page.setContent(html, { waitUntil: 'load' });
    await page.waitForTimeout(500);

    // Capturar solo el contenedor del SVG (sin bordes extra)
    const container = await page.$('#svg-container');
    if (container) {
        const box = await container.boundingBox();
        await page.screenshot({
            path: outputPath,
            type: 'png',
            clip: {
                x: box.x,
                y: box.y,
                width: box.width,
                height: box.height
            }
        });
        console.log(`✅ PNG: ${outputPath} (${Math.round(box.width)}x${Math.round(box.height)})`);
    } else {
        // Fallback: captura completa
        await page.screenshot({
            path: outputPath,
            type: 'png'
        });
        console.log(`✅ PNG: ${outputPath} (${Math.round(width * scale)}x${Math.round(height * scale)})`);
    }

    await browser.close();
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

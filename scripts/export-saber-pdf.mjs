#!/usr/bin/env node
/**
 * scripts/export-saber-pdf.mjs
 * 
 * Genera PDFs de talleres Saber usando Renderizado Web Nativo.
 * Navega a la ruta /print-saber/... y usa Playwright para imprimir.
 */

import { mkdirSync, existsSync } from 'fs';
import { join, basename, relative } from 'path';
import { chromium } from 'playwright';

// Configuración
const BASE_URL = 'http://localhost:4321'; // URL del servidor de desarrollo
const CONTENT_DIR = 'src/content/saber';

const colors = {
    reset: '\x1b[0m',
    green: '\x1b[32m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    cyan: '\x1b[36m',
    red: '\x1b[31m',
};

function log(msg, color = 'reset') {
    console.log(`${colors[color]}${msg}${colors.reset}`);
}

/**
 * Convierte ruta de archivo a slug URL
 * Ejemplo: src/content/saber/quimica/01-materia/taller.mdx -> quimica/01-materia/taller
 */
function getSlugFromPath(filePath) {
    // Normalizar ruta absoluta a relativa si es necesario
    let relPath = filePath;
    if (filePath.startsWith('/')) {
        // Intentar encontrar la parte relativa después de 'src/content/saber'
        const marker = 'src/content/saber/';
        const idx = filePath.indexOf(marker);
        if (idx !== -1) {
            relPath = filePath.substring(idx + marker.length);
        }
    } else {
        // Es relativa, asegurar que no tenga el prefijo
        relPath = filePath.replace(/^src\/content\/saber\//, '');
    }

    // Quitar extensión
    const relPathNoExt = relPath.replace(/\.(md|mdx)$/, '');

    // Aplicar lógica cleanSlug: eliminar prefijos numéricos de cada segmento
    return relPathNoExt
        .split('/')
        .map(segment => segment.replace(/^\d+-/, ''))
        .join('/');
}

async function main() {
    const args = process.argv.slice(2);

    if (args.length < 2) {
        log('Uso: node export-saber-pdf.mjs <ruta-taller.mdx> <directorio-salida>', 'yellow');
        process.exit(1);
    }

    const tallerPath = args[0];
    const outputDir = args[1];
    const tallerSlug = getSlugFromPath(tallerPath);
    const fileName = basename(tallerPath).replace(/\.(md|mdx)$/, '');

    // Verificar si el servidor está corriendo (ping simple)
    try {
        const response = await fetch(BASE_URL);
        if (!response.ok) throw new Error();
    } catch (e) {
        log('❌ Error: El servidor de desarrollo (http://localhost:4321) no parece estar corriendo.', 'red');
        log('   Por favor ejecuta "npm run dev:all" en otra terminal antes de exportar.', 'yellow');
        process.exit(1);
    }

    if (!existsSync(outputDir)) {
        mkdirSync(outputDir, { recursive: true });
    }

    log(`📝 Generando PDFs para: ${tallerSlug}`, 'blue');
    console.log('');

    let browser;
    try {
        browser = await chromium.launch();
        const page = await browser.newPage();

        // 1. PDF Normal (1 columna, limpio)
        // URL: /print-saber/slug?mode=default
        const urlNormal = `${BASE_URL}/print-saber/${tallerSlug}?mode=default`;
        log(`  📄 Generando PDF Normal...`, 'cyan');
        await page.goto(urlNormal, { waitUntil: 'networkidle' });
        // Esperar renderizado de matemáticas y componentes
        await page.waitForTimeout(2000);

        await page.pdf({
            path: join(outputDir, `${fileName}_normal.pdf`),
            format: 'Letter',
            margin: { top: '0.6in', right: '0.6in', bottom: '0.6in', left: '0.6in' },
            printBackground: true
        });
        log(`     ✓ ${fileName}_normal.pdf`, 'green');

        // 2. PDF Imprimible (2 columnas, compacto)
        // URL: /print-saber/slug?mode=imprimible
        const urlImprimible = `${BASE_URL}/print-saber/${tallerSlug}?mode=imprimible`;
        log(`  📄 Generando PDF Imprimible (2 columnas)...`, 'cyan');
        await page.goto(urlImprimible, { waitUntil: 'networkidle' });
        await page.waitForTimeout(2000);

        await page.pdf({
            path: join(outputDir, `${fileName}_imprimible.pdf`),
            format: 'Letter',
            margin: { top: '1cm', right: '1cm', bottom: '1cm', left: '1cm' },
            printBackground: true
        });
        log(`     ✓ ${fileName}_imprimible.pdf`, 'green');

        // 3. PDF Retroalimentación (Con respuestas)
        // URL: /print-saber/slug?mode=feedback
        const urlFeedback = `${BASE_URL}/print-saber/${tallerSlug}?mode=feedback`;
        log(`  📄 Generando PDF Retroalimentación...`, 'cyan');
        await page.goto(urlFeedback, { waitUntil: 'networkidle' });
        await page.waitForTimeout(2000);

        await page.pdf({
            path: join(outputDir, `${fileName}_retroalimentacion.pdf`),
            format: 'Letter',
            margin: { top: '0.6in', right: '0.6in', bottom: '0.6in', left: '0.6in' },
            printBackground: true
        });
        log(`     ✓ ${fileName}_retroalimentacion.pdf`, 'green');

        console.log('');
        log('✅ ¡PDFs generados exitosamente con renderizado nativo!', 'green');

    } catch (error) {
        log(`❌ Error generando PDFs: ${error.message}`, 'red');
        console.error(error);
    } finally {
        if (browser) await browser.close();
    }
}

main().catch(console.error);

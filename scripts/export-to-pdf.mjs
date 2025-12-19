/**
 * export-to-pdf.mjs
 * 
 * Genera PDFs profesionales de las lecciones usando Playwright.
 * Usa las rutas /print/ y /print-tema/ que tienen estilos optimizados para impresión.
 * 
 * USO:
 *   # Una lección individual
 *   node scripts/export-to-pdf.mjs --lesson <url> --output <archivo.pdf>
 * 
 *   # Tema completo (un solo PDF combinado)
 *   node scripts/export-to-pdf.mjs --tema <url-tema> --output <archivo.pdf>
 * 
 * EJEMPLOS:
 *   node scripts/export-to-pdf.mjs \
 *     --lesson fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas \
 *     --output ~/Desktop/fisica-ramas.pdf
 * 
 *   node scripts/export-to-pdf.mjs \
 *     --tema fisica/introduccion-a-la-fisica/introduccion \
 *     --output ~/Desktop/guia-introduccion-fisica.pdf
 */

import { chromium } from 'playwright';
import { mkdirSync, existsSync } from 'fs';
import { dirname, resolve, basename } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Configuración
const BASE_URL = 'http://localhost:4321';

function parseArgs() {
    const args = process.argv.slice(2);
    const options = {
        lesson: null,
        tema: null,
        output: null
    };

    for (let i = 0; i < args.length; i++) {
        if (args[i] === '--lesson' && args[i + 1]) {
            options.lesson = args[i + 1].replace(/^\//, '');
            i++;
        } else if (args[i] === '--tema' && args[i + 1]) {
            options.tema = args[i + 1].replace(/^\//, '');
            i++;
        } else if (args[i] === '--output' && args[i + 1]) {
            options.output = args[i + 1];
            i++;
        }
    }

    return options;
}

async function generatePdf(page, url, outputPath, waitTime = 2000) {
    /**
     * Genera PDF de una página
     */
    console.log(`  🖨️  Capturando: ${url}`);

    await page.goto(`${BASE_URL}${url}`, { waitUntil: 'networkidle', timeout: 60000 });

    // Esperar que KaTeX renderice las fórmulas
    await page.waitForTimeout(waitTime);

    // Generar PDF
    await page.pdf({
        path: outputPath,
        format: 'Letter',
        margin: {
            top: '0.5in',
            bottom: '0.5in',
            left: '0.6in',
            right: '0.6in'
        },
        printBackground: true,
        displayHeaderFooter: false
    });
}

async function main() {
    const options = parseArgs();

    if (!options.lesson && !options.tema) {
        console.log(`
📄 export-to-pdf.mjs - Genera PDFs profesionales

USO:
  # Una lección individual
  node scripts/export-to-pdf.mjs --lesson <url> --output <archivo.pdf>

  # Tema completo (PDF combinado con portada e índice)
  node scripts/export-to-pdf.mjs --tema <url-tema> --output <archivo.pdf>

EJEMPLOS:
  node scripts/export-to-pdf.mjs \\
    --lesson fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas \\
    --output ~/Desktop/fisica-ramas.pdf

  node scripts/export-to-pdf.mjs \\
    --tema fisica/introduccion-a-la-fisica/introduccion \\
    --output ~/Desktop/guia-introduccion-fisica.pdf
`);
        process.exit(1);
    }

    console.log('━'.repeat(50));
    console.log('📚 Exportando a PDF profesional...');
    console.log('━'.repeat(50));

    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
        viewport: { width: 1200, height: 800 }
    });
    const page = await context.newPage();

    try {
        let outputPath;

        if (options.lesson) {
            // Generar una sola lección usando /print/
            outputPath = options.output
                ? resolve(options.output.replace('~', process.env.HOME))
                : resolve(process.env.HOME, 'Desktop', `${basename(options.lesson)}.pdf`);

            // Crear directorio si no existe
            const outputDir = dirname(outputPath);
            if (!existsSync(outputDir)) {
                mkdirSync(outputDir, { recursive: true });
            }

            await generatePdf(page, `/print/${options.lesson}`, outputPath);

        } else if (options.tema) {
            // Generar tema completo usando /print-tema/
            const temaName = options.tema.split('/').pop();
            outputPath = options.output
                ? resolve(options.output.replace('~', process.env.HOME))
                : resolve(process.env.HOME, 'Desktop', `guia-${temaName}.pdf`);

            // Crear directorio si no existe
            const outputDir = dirname(outputPath);
            if (!existsSync(outputDir)) {
                mkdirSync(outputDir, { recursive: true });
            }

            // Más tiempo de espera para páginas con múltiples lecciones
            await generatePdf(page, `/print-tema/${options.tema}`, outputPath, 4000);
        }

        console.log(`\n✅ PDF generado: ${outputPath}`);
        console.log('━'.repeat(50));

    } finally {
        await browser.close();
    }
}

main().catch(err => {
    console.error('❌ Error:', err);
    process.exit(1);
});

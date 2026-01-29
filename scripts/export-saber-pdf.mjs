#!/usr/bin/env node
/**
 * Script para generar PDFs de talleres Saber
 * Usa los scripts originales de banco-saber
 */

import { mkdirSync, existsSync } from 'fs';
import { join } from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
import { parseTallerMarkdown } from './parse-taller.mjs';
import { renderPDF } from './render-pdf.mjs';
import { renderPDFImprimible } from './render-pdf-imprimible.mjs';
import { renderPDFFeedback } from './render-pdf-feedback.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

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

    try {
        // Parsear el taller usando el parser original
        const taller = parseTallerMarkdown(tallerPath);

        // 1. PDF Normal
        log('  📄 Generando PDF normal...', 'cyan');
        const normalPath = await renderPDF(taller, outputDir);
        if (normalPath) {
            log(`     ✓ ${normalPath}`, 'green');
        }

        // 2. PDF Imprimible
        log('  📄 Generando PDF imprimible...', 'cyan');
        const imprimiblePath = await renderPDFImprimible(taller, outputDir);
        if (imprimiblePath) {
            log(`     ✓ ${imprimiblePath}`, 'green');
        }

        // 3. PDF Retroalimentación
        log('  📄 Generando PDF retroalimentación...', 'cyan');
        const feedbackPath = await renderPDFFeedback(taller, outputDir);
        if (feedbackPath) {
            log(`     ✓ ${feedbackPath}`, 'green');
        }

        console.log('');
        log('✅ ¡PDFs generados exitosamente!', 'green');
    } catch (error) {
        log(`❌ Error: ${error.message}`, 'red');
        console.error(error);
        process.exit(1);
    }
}

main().catch(err => {
    log(`❌ Error: ${err.message}`, 'red');
    console.error(err);
    process.exit(1);
});

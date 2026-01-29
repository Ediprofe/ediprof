#!/usr/bin/env node
/**
 * export-menu.js
 * 
 * Script interactivo para exportar lecciones a PDF o Word.
 * Simplifica el proceso con un menú guiado.
 * 
 * USO:
 *   npm run export
 *   o
 *   node scripts/export-menu.js
 */

import inquirer from 'inquirer';
import { readdirSync, existsSync, statSync, readFileSync, mkdirSync } from 'fs';
import { join, resolve, basename } from 'path';
import { execSync, spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const PROJECT_ROOT = resolve(__dirname, '..');
const CONTENT_DIR = join(PROJECT_ROOT, 'src', 'content');

// Colores para console
const colors = {
    reset: '\x1b[0m',
    green: '\x1b[32m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    cyan: '\x1b[36m',
    red: '\x1b[31m',
    bold: '\x1b[1m'
};

function log(msg, color = 'reset') {
    console.log(`${colors[color]}${msg}${colors.reset}`);
}

/**
 * Lee el nombre desde _meta.json o formatea el nombre de carpeta
 */
function getName(path) {
    const metaPath = join(path, '_meta.json');
    if (existsSync(metaPath)) {
        try {
            const meta = JSON.parse(readFileSync(metaPath, 'utf-8'));
            if (meta.name) return meta.name;
        } catch (e) { }
    }
    // Formatear: "01-nombre-largo" -> "Nombre Largo"
    return basename(path)
        .replace(/^\d+-/, '')
        .split('-')
        .map(w => w.charAt(0).toUpperCase() + w.slice(1))
        .join(' ');
}

/**
 * Obtiene título de una lección desde su contenido
 */
function getLessonTitle(filePath) {
    try {
        const content = readFileSync(filePath, 'utf-8');
        const match = content.match(/^#\s+(.+)$/m);
        if (match) return match[1];
    } catch (e) { }
    return basename(filePath, '.md').replace(/^\d+-/, '').replace(/-/g, ' ');
}

/**
 * Lista carpetas con prefijo numérico ordenadas
 */
function listFolders(dir) {
    if (!existsSync(dir)) return [];
    return readdirSync(dir)
        .filter(f => {
            const fullPath = join(dir, f);
            return statSync(fullPath).isDirectory() && !f.startsWith('.') && !f.startsWith('_');
        })
        .sort((a, b) => {
            const numA = parseInt(a.match(/^(\d+)/)?.[1] || '999');
            const numB = parseInt(b.match(/^(\d+)/)?.[1] || '999');
            return numA - numB;
        });
}

/**
 * Lista archivos .md/.mdx en un directorio
 */
function listLessons(dir) {
    if (!existsSync(dir)) return [];
    return readdirSync(dir)
        .filter(f => f.endsWith('.md') || f.endsWith('.mdx'))
        .filter(f => !f.startsWith('_'))
        .sort();
}

/**
 * Limpia prefijo numérico y normaliza
 */
function cleanSlug(name) {
    return name.replace(/^\d+-/, '').toLowerCase();
}

async function main() {
    console.clear();
    log('━'.repeat(50), 'cyan');
    log('📤 EXPORTAR LECCIONES', 'bold');
    log('━'.repeat(50), 'cyan');
    console.log();

    // 0. Elegir fuente
    const { source } = await inquirer.prompt([
        {
            type: 'rawlist',
            name: 'source',
            message: '¿Qué quieres exportar?',
            choices: [
                { name: '📚 Lecciones del contenido web', value: 'content' },
                { name: '📝 Talleres Saber (ICFES)', value: 'saber' },
                { name: '📋 Guías docentes institucionales', value: 'guias' }
            ]
        }
    ]);

    if (source === 'guias') {
        await exportGuiasDocentes();
        return;
    }

    if (source === 'saber') {
        await exportTalleresSaber();
        return;
    }

    // 1. Elegir formato
    const { format } = await inquirer.prompt([
        {
            type: 'rawlist',
            name: 'format',
            message: '¿En qué formato quieres exportar?',
            choices: [
                { name: '📄 PDF (requiere servidor corriendo)', value: 'pdf' },
                { name: '📝 Word (DOCX)', value: 'docx' }
            ]
        }
    ]);

    // 2. Elegir materia
    const materias = listFolders(CONTENT_DIR);
    const materiaChoices = materias.map(m => ({
        name: `${getMateriaIcon(m)} ${getName(join(CONTENT_DIR, m))}`,
        value: m
    }));

    const { materia } = await inquirer.prompt([
        {
            type: 'rawlist',
            name: 'materia',
            message: '¿De qué materia?',
            choices: materiaChoices
        }
    ]);

    // 3. Elegir unidad
    const unidadesDir = join(CONTENT_DIR, materia);
    const unidades = listFolders(unidadesDir);

    if (unidades.length === 0) {
        log('❌ No hay unidades en esta materia', 'red');
        process.exit(1);
    }

    const unidadChoices = unidades.map((u, i) => ({
        name: `${i + 1}. ${getName(join(unidadesDir, u))}`,
        value: u
    }));

    const { unidad } = await inquirer.prompt([
        {
            type: 'rawlist',
            name: 'unidad',
            message: '¿De qué unidad?',
            choices: unidadChoices
        }
    ]);

    // 4. Elegir alcance (unidad, tema o lecciones)
    const temasDir = join(unidadesDir, unidad);
    const temas = listFolders(temasDir);

    if (temas.length === 0) {
        log('❌ No hay temas en esta unidad', 'red');
        process.exit(1);
    }

    // Contar lecciones totales en la unidad
    let totalLeccionesUnidad = 0;
    for (const t of temas) {
        totalLeccionesUnidad += listLessons(join(temasDir, t)).length;
    }

    const { scopeLevel } = await inquirer.prompt([
        {
            type: 'rawlist',
            name: 'scopeLevel',
            message: '¿Qué quieres exportar?',
            choices: [
                { name: `📦 Toda la unidad (${temas.length} temas, ${totalLeccionesUnidad} lecciones)`, value: 'unidad' },
                { name: '📚 Un tema específico', value: 'tema' },
                { name: '📄 Lecciones específicas de un tema', value: 'lecciones' }
            ]
        }
    ]);

    let tema = null;
    let scope = scopeLevel;
    let selectedLessons = [];
    let leccionesDir = null;

    // Si no es unidad completa, elegir tema
    if (scopeLevel === 'tema' || scopeLevel === 'lecciones') {
        const temaChoices = temas.map((t, i) => ({
            name: `${i + 1}. ${getName(join(temasDir, t))}`,
            value: t
        }));

        const { selectedTema } = await inquirer.prompt([
            {
                type: 'rawlist',
                name: 'selectedTema',
                message: '¿De qué tema?',
                choices: temaChoices
            }
        ]);
        tema = selectedTema;
        leccionesDir = join(temasDir, tema);

        // Si quiere lecciones específicas, mostrar selector
        if (scopeLevel === 'lecciones') {
            const lecciones = listLessons(leccionesDir);

            if (lecciones.length === 0) {
                log('❌ No hay lecciones en este tema', 'red');
                process.exit(1);
            }

            const lessonChoices = lecciones.map(l => ({
                name: getLessonTitle(join(leccionesDir, l)),
                value: l
            }));

            const { lessons } = await inquirer.prompt([
                {
                    type: 'checkbox',
                    name: 'lessons',
                    message: 'Selecciona las lecciones (espacio para marcar, enter para confirmar):',
                    choices: lessonChoices,
                    validate: (answer) => answer.length > 0 ? true : 'Selecciona al menos una lección'
                }
            ]);
            selectedLessons = lessons;
            scope = 'seleccionar';
        } else {
            // Tema completo
            selectedLessons = listLessons(leccionesDir);
        }
    }

    // 5. Nombre del archivo de salida
    let defaultName;
    if (scopeLevel === 'unidad') {
        defaultName = `${getName(join(unidadesDir, unidad))}.${format === 'pdf' ? 'pdf' : 'docx'}`;
    } else if (scope === 'tema') {
        defaultName = `${getName(join(temasDir, tema))}.${format === 'pdf' ? 'pdf' : 'docx'}`;
    } else {
        defaultName = `exportacion.${format === 'pdf' ? 'pdf' : 'docx'}`;
    }

    const { outputName } = await inquirer.prompt([
        {
            type: 'input',
            name: 'outputName',
            message: 'Nombre del archivo de salida:',
            default: defaultName.replace(/\s+/g, '-')
        }
    ]);

    const outputPath = resolve(process.env.HOME, 'Desktop', outputName);

    // 7. Seleccionar plantilla (solo para Word)
    let templatePath = null;
    if (format === 'docx') {
        const templatesDir = join(PROJECT_ROOT, 'templates');
        const templates = existsSync(templatesDir)
            ? readdirSync(templatesDir).filter(f => f.endsWith('.docx'))
            : [];

        if (templates.length > 0) {
            const templateChoices = [
                { name: 'Sin plantilla (estilo por defecto)', value: null },
                ...templates.map(t => ({
                    name: t.replace('.docx', ''),
                    value: join(templatesDir, t)
                }))
            ];

            const { template } = await inquirer.prompt([
                {
                    type: 'rawlist',
                    name: 'template',
                    message: '¿Qué plantilla usar?',
                    choices: templateChoices
                }
            ]);
            templatePath = template;
        }
    }

    // 8. Ejecutar exportación
    console.log();
    log('━'.repeat(50), 'cyan');
    log(`📤 Exportando a ${format.toUpperCase()}...`, 'green');
    log('━'.repeat(50), 'cyan');
    console.log();

    try {
        if (format === 'pdf') {
            await exportToPdf(materia, unidad, tema, selectedLessons, scopeLevel, outputPath);
        } else {
            await exportToDocx(materia, unidad, tema, selectedLessons, outputPath, leccionesDir, templatePath, scopeLevel, temasDir);
        }

        console.log();
        log('━'.repeat(50), 'cyan');
        log(`✅ ¡Éxito! Archivo guardado en:`, 'green');
        log(`   ${outputPath}`, 'yellow');
        log('━'.repeat(50), 'cyan');

    } catch (error) {
        log(`❌ Error: ${error.message}`, 'red');
        process.exit(1);
    }
}

function getMateriaIcon(materia) {
    const icons = {
        matematicas: '🧮',
        fisica: '⚡',
        quimica: '🧪',
        ciencias: '🌿'
    };
    return icons[materia] || '📚';
}

async function exportToPdf(materia, unidad, tema, lessons, scope, outputPath) {
    const cleanMateria = cleanSlug(materia);
    const cleanUnidad = cleanSlug(unidad);
    const cleanTema = tema ? cleanSlug(tema) : null;

    if (scope === 'unidad') {
        // Exportar unidad completa
        const unidadUrl = `${cleanMateria}/${cleanUnidad}`;
        log(`📦 Generando PDF de toda la unidad...`, 'blue');

        const cmd = `node "${join(PROJECT_ROOT, 'scripts', 'export-to-pdf.mjs')}" --unidad ${unidadUrl} --output "${outputPath}"`;
        execSync(cmd, { stdio: 'inherit', cwd: PROJECT_ROOT });
    } else if (scope === 'tema') {
        // Exportar tema completo
        const temaUrl = `${cleanMateria}/${cleanUnidad}/${cleanTema}`;
        log(`📚 Generando PDF del tema completo...`, 'blue');

        const cmd = `node "${join(PROJECT_ROOT, 'scripts', 'export-to-pdf.mjs')}" --tema ${temaUrl} --output "${outputPath}"`;
        execSync(cmd, { stdio: 'inherit', cwd: PROJECT_ROOT });
    } else {
        // Para lecciones individuales, exportar la primera (o combinar manualmente)
        if (lessons.length === 1) {
            const lessonSlug = lessons[0].replace(/^\d+-/, '').replace(/\.mdx?$/, '');
            const lessonUrl = `${cleanMateria}/${cleanUnidad}/${cleanTema}/${lessonSlug}`;
            log(`📄 Generando PDF de: ${getLessonTitle(join(PROJECT_ROOT, 'src', 'content', materia, unidad, tema, lessons[0]))}`, 'blue');

            const cmd = `node "${join(PROJECT_ROOT, 'scripts', 'export-to-pdf.mjs')}" --lesson ${lessonUrl} --output "${outputPath}"`;
            execSync(cmd, { stdio: 'inherit', cwd: PROJECT_ROOT });
        } else {
            log(`⚠️  Para múltiples lecciones específicas en PDF, usa la opción "Todo el tema"`, 'yellow');
            log(`   O exporta cada lección por separado.`, 'yellow');
            throw new Error('PDF de múltiples lecciones específicas no soportado aún');
        }
    }
}

async function exportToDocx(materia, unidad, tema, lessons, outputPath, leccionesDir, templatePath, scopeLevel, temasDir) {
    let files = [];

    if (scopeLevel === 'unidad') {
        // Recolectar todas las lecciones de todos los temas de la unidad
        const temas = listFolders(temasDir);
        for (const t of temas) {
            const temaLeccionesDir = join(temasDir, t);
            const temaLecciones = listLessons(temaLeccionesDir);
            files.push(...temaLecciones.map(l => join(temaLeccionesDir, l)));
        }
        log(`📦 Generando Word de toda la unidad (${files.length} lecciones)...`, 'blue');
    } else {
        files = lessons.map(l => join(leccionesDir, l));
        log(`📝 Generando Word con ${files.length} lección(es)...`, 'blue');
    }

    if (templatePath) {
        log(`   📋 Usando plantilla: ${basename(templatePath)}`, 'cyan');
    }
    files.forEach(f => log(`   • ${getLessonTitle(f)}`, 'cyan'));
    console.log();

    let cmd = `bash "${join(PROJECT_ROOT, 'scripts', 'export-to-docx.sh')}" ${files.map(f => `"${f}"`).join(' ')} -o "${outputPath}"`;
    if (templatePath) {
        cmd += ` -t "${templatePath}"`;
    }
    execSync(cmd, { stdio: 'inherit', cwd: PROJECT_ROOT });
}

const GUIAS_DIR = join(PROJECT_ROOT, 'guias-docente');
const SABER_DIR = join(PROJECT_ROOT, 'src', 'content', 'saber');

/**
 * Lista archivos .md en guias-docente/ organizados por semestre
 */
function listGuiasDocentes() {
    if (!existsSync(GUIAS_DIR)) return [];

    const semestres = readdirSync(GUIAS_DIR)
        .filter(f => {
            const fullPath = join(GUIAS_DIR, f);
            return statSync(fullPath).isDirectory() && !f.startsWith('.') && f !== 'output';
        })
        .sort();

    const guias = [];
    for (const semestre of semestres) {
        const semestreDir = join(GUIAS_DIR, semestre);
        const files = readdirSync(semestreDir)
            .filter(f => f.endsWith('.md'))
            .sort();

        for (const file of files) {
            guias.push({
                semestre,
                file,
                path: join(semestreDir, file),
                title: getLessonTitle(join(semestreDir, file))
            });
        }
    }
    return guias;
}

async function exportGuiasDocentes() {
    log('━'.repeat(50), 'cyan');
    log('📋 EXPORTAR GUÍAS DOCENTES', 'bold');
    log('━'.repeat(50), 'cyan');
    console.log();

    const guias = listGuiasDocentes();

    if (guias.length === 0) {
        log('❌ No hay guías docentes en guias-docente/', 'red');
        log('   Usa el comando /guia para generar actividades.', 'yellow');
        process.exit(1);
    }

    // Agrupar por semestre
    const semestreGroups = {};
    for (const g of guias) {
        if (!semestreGroups[g.semestre]) semestreGroups[g.semestre] = [];
        semestreGroups[g.semestre].push(g);
    }

    // Crear choices con separadores por semestre
    const choices = [];
    for (const semestre of Object.keys(semestreGroups).sort()) {
        choices.push(new inquirer.Separator(`── ${semestre} ──`));
        for (const g of semestreGroups[semestre]) {
            choices.push({
                name: `${g.file.includes('bilingue') ? '🌍' : '🎯'} ${g.title}`,
                value: g.path
            });
        }
    }

    const { selectedGuias } = await inquirer.prompt([
        {
            type: 'checkbox',
            name: 'selectedGuias',
            message: 'Selecciona las guías a exportar (espacio para marcar):',
            choices,
            validate: answer => answer.length > 0 ? true : 'Selecciona al menos una guía'
        }
    ]);

    // Nombre del archivo de salida
    const defaultName = selectedGuias.length === 1
        ? `${basename(selectedGuias[0], '.md')}.docx`
        : 'guias-docentes.docx';

    const { outputName } = await inquirer.prompt([
        {
            type: 'input',
            name: 'outputName',
            message: 'Nombre del archivo de salida:',
            default: defaultName
        }
    ]);

    const outputPath = resolve(process.env.HOME, 'Desktop', outputName);

    // Usar plantilla bitacora.docx
    const templatePath = join(PROJECT_ROOT, 'templates', 'bitacora.docx');
    const useTemplate = existsSync(templatePath);

    console.log();
    log('━'.repeat(50), 'cyan');
    log('📤 Exportando guías docentes...', 'green');
    if (useTemplate) {
        log('   📋 Usando plantilla: bitacora.docx', 'cyan');
    }
    log('━'.repeat(50), 'cyan');
    console.log();

    let cmd = `bash "${join(PROJECT_ROOT, 'scripts', 'export-to-docx.sh')}" ${selectedGuias.map(f => `"${f}"`).join(' ')} -o "${outputPath}"`;
    if (useTemplate) {
        cmd += ` -t "${templatePath}"`;
    }

    try {
        execSync(cmd, { stdio: 'inherit', cwd: PROJECT_ROOT });

        console.log();
        log('━'.repeat(50), 'cyan');
        log('✅ ¡Éxito! Archivo guardado en:', 'green');
        log(`   ${outputPath}`, 'yellow');
        log('━'.repeat(50), 'cyan');
    } catch (error) {
        throw new Error(`Error al exportar: ${error.message}`);
    }
}

main().catch(err => {
    console.error('❌ Error:', err);
    process.exit(1);
});


/**
 * Lista talleres Saber disponibles
 */
function listTalleresSaber() {
    if (!existsSync(SABER_DIR)) return [];

    const talleres = [];
    const materias = listFolders(SABER_DIR);

    for (const materia of materias) {
        const materiaDir = join(SABER_DIR, materia);
        const unidades = listFolders(materiaDir);

        for (const unidad of unidades) {
            const unidadDir = join(materiaDir, unidad);
            const files = readdirSync(unidadDir)
                .filter(f => (f.endsWith('.md') || f.endsWith('.mdx')) && !f.startsWith('_'))
                .sort();

            for (const file of files) {
                talleres.push({
                    materia,
                    unidad,
                    file,
                    path: join(unidadDir, file),
                    title: getLessonTitle(join(unidadDir, file))
                });
            }
        }
    }
    return talleres;
}

/**
 * Exporta talleres Saber a PDF
 */
async function exportTalleresSaber() {
    log('━'.repeat(50), 'cyan');
    log('📝 EXPORTAR TALLERES SABER', 'bold');
    log('━'.repeat(50), 'cyan');
    console.log();

    const talleres = listTalleresSaber();

    if (talleres.length === 0) {
        log('❌ No hay talleres Saber en src/content/saber/', 'red');
        process.exit(1);
    }

    // Agrupar por materia
    const materiaGroups = {};
    for (const t of talleres) {
        if (!materiaGroups[t.materia]) materiaGroups[t.materia] = [];
        materiaGroups[t.materia].push(t);
    }

    // Crear choices con separadores por materia
    const choices = [];
    for (const materia of Object.keys(materiaGroups).sort()) {
        choices.push(new inquirer.Separator(`── ${getMateriaIcon(materia)} ${getName(join(SABER_DIR, materia))} ──`));
        for (const t of materiaGroups[materia]) {
            choices.push({
                name: `${t.title}`,
                value: t.path
            });
        }
    }

    const { selectedTaller } = await inquirer.prompt([
        {
            type: 'rawlist',
            name: 'selectedTaller',
            message: 'Selecciona el taller a exportar:',
            choices
        }
    ]);

    // Directorio de salida
    const outputDir = resolve(process.env.HOME, 'Desktop', 'talleres-saber');
    if (!existsSync(outputDir)) {
        mkdirSync(outputDir, { recursive: true });
    }

    console.log();
    log('━'.repeat(50), 'cyan');
    log('📤 Generando PDFs del taller Saber...', 'green');
    log('   Se generarán 3 versiones:', 'cyan');
    log('   • PDF normal (1 columna)', 'cyan');
    log('   • PDF imprimible (2 columnas)', 'cyan');
    log('   • PDF retroalimentación (con respuestas)', 'cyan');
    log('━'.repeat(50), 'cyan');
    console.log();

    try {
        const cmd = `node "${join(PROJECT_ROOT, 'scripts', 'export-saber-pdf.mjs')}" "${selectedTaller}" "${outputDir}"`;
        execSync(cmd, { stdio: 'inherit', cwd: PROJECT_ROOT });

        console.log();
        log('━'.repeat(50), 'cyan');
        log('✅ ¡Éxito! Archivos guardados en:', 'green');
        log(`   ${outputDir}`, 'yellow');
        log('━'.repeat(50), 'cyan');
    } catch (error) {
        throw new Error(`Error al exportar: ${error.message}`);
    }
}

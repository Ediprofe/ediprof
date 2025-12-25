#!/usr/bin/env node
/**
 * Script para optimizar imágenes PNG → WebP y subirlas a Cloudflare R2
 * 
 * Uso:
 *   npm run img                                  # Menú interactivo (recomendado)
 *   npm run img <archivo.png> --materia <materia>
 *   npm run img --list fisica                    # Lista imágenes de física
 *   npm run img --search velocidad               # Busca imágenes por nombre
 * 
 * El script:
 *   1. Genera un ID único de 4 caracteres
 *   2. Optimiza PNG → WebP (reduce ~80%)
 *   3. Sube a R2 en la estructura: img/{materia}/{id}-{nombre}.webp
 *   4. Copia el markdown al clipboard
 *   5. Actualiza el índice local
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import sharp from 'sharp';
import { select, confirm, search } from '@inquirer/prompts';

// Configuración
const CONFIG = {
  inboxDir: './inbox',
  indexFile: './images-index.json',
  r2Bucket: 'ediprofe',
  cdnDomain: 'cdn.ediprofe.com',  // Actualizar al dominio que configures
  materias: ['fisica', 'matematicas', 'quimica', 'ciencias'],
  webpQuality: 80
};

// Colores para terminal
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  red: '\x1b[31m',
  gray: '\x1b[90m'
};

function log(emoji, message, color = 'reset') {
  console.log(`${colors[color]}${emoji} ${message}${colors.reset}`);
}

// Genera ID único de 4 caracteres
function generateId() {
  const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
  let id = '';
  for (let i = 0; i < 4; i++) {
    id += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return id;
}

// Carga el índice de imágenes
function loadIndex() {
  if (fs.existsSync(CONFIG.indexFile)) {
    return JSON.parse(fs.readFileSync(CONFIG.indexFile, 'utf-8'));
  }
  return { images: [], lastUpdated: null };
}

// Guarda el índice
function saveIndex(index) {
  index.lastUpdated = new Date().toISOString();
  fs.writeFileSync(CONFIG.indexFile, JSON.stringify(index, null, 2));
}

// Busca imágenes similares en el índice
function findSimilar(index, name, materia) {
  const searchTerm = name.toLowerCase().replace(/\.(png|jpg|jpeg|webp)$/, '');
  return index.images.filter(img => 
    img.materia === materia && 
    img.name.toLowerCase().includes(searchTerm)
  );
}

// Copia texto al clipboard (macOS)
function copyToClipboard(text) {
  try {
    execSync(`echo "${text}" | pbcopy`);
    return true;
  } catch {
    return false;
  }
}

// Verifica que wrangler esté instalado y configurado
function checkWrangler() {
  try {
    execSync('wrangler --version', { stdio: 'pipe' });
    return true;
  } catch {
    return false;
  }
}

// Sube archivo a R2
function uploadToR2(localPath, r2Path) {
  try {
    execSync(`wrangler r2 object put ${CONFIG.r2Bucket}/${r2Path} --file="${localPath}" --remote`, {
      stdio: 'pipe'
    });
    return true;
  } catch (error) {
    console.error('Error subiendo a R2:', error.message);
    return false;
  }
}

// Optimiza imagen PNG → WebP (o mantiene original si WebP es más grande)
async function optimizeImage(inputPath, outputPath) {
  const inputStats = fs.statSync(inputPath);
  const inputSize = inputStats.size;
  const ext = path.extname(inputPath).toLowerCase();

  // Crear versión WebP temporal
  const tempWebp = outputPath + '.temp';
  await sharp(inputPath)
    .webp({ quality: CONFIG.webpQuality })
    .toFile(tempWebp);

  const webpStats = fs.statSync(tempWebp);
  const webpSize = webpStats.size;

  // Si WebP es más grande, mantener formato original optimizado
  if (webpSize >= inputSize && (ext === '.png' || ext === '.jpg' || ext === '.jpeg')) {
    fs.unlinkSync(tempWebp);
    
    // Optimizar en formato original
    const finalPath = outputPath.replace('.webp', ext);
    await sharp(inputPath)
      .png({ quality: CONFIG.webpQuality, compressionLevel: 9 })
      .toFile(finalPath);
    
    const finalStats = fs.statSync(finalPath);
    const reduction = Math.round((1 - finalStats.size / inputSize) * 100);
    
    return { 
      inputSize, 
      outputSize: finalStats.size, 
      reduction,
      finalPath,
      format: ext.slice(1),
      keptOriginalFormat: true
    };
  }

  // WebP es más pequeño, usarlo
  fs.renameSync(tempWebp, outputPath);
  const reduction = Math.round((1 - webpSize / inputSize) * 100);

  return { 
    inputSize, 
    outputSize: webpSize, 
    reduction,
    finalPath: outputPath,
    format: 'webp',
    keptOriginalFormat: false
  };
}

// Formatea bytes a KB/MB
function formatBytes(bytes) {
  if (bytes < 1024) return `${bytes}B`;
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)}KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)}MB`;
}

// Lista imágenes de una materia
function listImages(index, materia) {
  const images = index.images.filter(img => !materia || img.materia === materia);
  
  if (images.length === 0) {
    log('📭', `No hay imágenes${materia ? ` en ${materia}` : ''}`, 'yellow');
    return;
  }

  log('📚', `Imágenes${materia ? ` en ${materia}` : ''}: ${images.length}`, 'blue');
  console.log('');
  
  const grouped = {};
  images.forEach(img => {
    if (!grouped[img.materia]) grouped[img.materia] = [];
    grouped[img.materia].push(img);
  });

  Object.keys(grouped).sort().forEach(mat => {
    console.log(`${colors.yellow}${mat}/${colors.reset}`);
    grouped[mat].forEach(img => {
      console.log(`  ${colors.gray}${img.id}${colors.reset}-${img.name} ${colors.gray}(${img.size}, ${img.date})${colors.reset}`);
    });
  });
}

// Busca imágenes por nombre
function searchImages(index, query) {
  const results = index.images.filter(img => 
    img.name.toLowerCase().includes(query.toLowerCase()) ||
    img.id.includes(query.toLowerCase())
  );

  if (results.length === 0) {
    log('🔍', `No se encontraron imágenes con "${query}"`, 'yellow');
    return;
  }

  log('🔍', `Resultados para "${query}": ${results.length}`, 'blue');
  console.log('');
  
  results.forEach(img => {
    const url = `https://${CONFIG.cdnDomain}/img/${img.materia}/${img.id}-${img.name}`;
    console.log(`${colors.yellow}${img.materia}/${colors.reset}${img.id}-${img.name}`);
    console.log(`  ${colors.gray}${url}${colors.reset}`);
  });
}

// Proceso principal de subida
async function uploadImage(fileName, materia) {
  const inputPath = path.join(CONFIG.inboxDir, fileName);
  
  // Verificar que existe el archivo
  if (!fs.existsSync(inputPath)) {
    log('❌', `Archivo no encontrado: ${inputPath}`, 'red');
    log('💡', `Asegúrate de poner la imagen en la carpeta inbox/`, 'yellow');
    process.exit(1);
  }

  // Verificar materia válida
  if (!CONFIG.materias.includes(materia)) {
    log('❌', `Materia inválida: ${materia}`, 'red');
    log('💡', `Materias válidas: ${CONFIG.materias.join(', ')}`, 'yellow');
    process.exit(1);
  }

  // Cargar índice
  const index = loadIndex();
  
  // Verificar si ya existe una imagen similar
  const baseName = path.basename(fileName, path.extname(fileName));
  const similar = findSimilar(index, baseName, materia);
  
  if (similar.length > 0) {
    log('⚠️', `Ya existen imágenes similares:`, 'yellow');
    similar.forEach(img => {
      console.log(`   ${colors.gray}${img.id}-${img.name} (${img.date})${colors.reset}`);
    });
    console.log('');
    log('💡', 'Continuando con la subida (nuevo ID)...', 'gray');
    console.log('');
  }

  // Generar ID único
  let id;
  do {
    id = generateId();
  } while (index.images.some(img => img.id === id));

  // Preparar nombres de archivo
  const cleanName = baseName.toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Quitar acentos
    .replace(/[^a-z0-9-]/g, '-')  // Solo letras, números y guiones
    .replace(/-+/g, '-')          // Colapsar guiones múltiples
    .replace(/^-|-$/g, '');       // Quitar guiones al inicio/final
  
  const tempOutput = path.join(CONFIG.inboxDir, `temp-${id}.webp`);

  console.log('');
  log('📍', `Materia: ${materia}`, 'blue');
  log('🆔', `ID generado: ${id}`, 'blue');
  console.log('');

  // Optimizar imagen
  log('📦', 'Optimizando...', 'gray');
  let optimizeResult;
  try {
    optimizeResult = await optimizeImage(inputPath, tempOutput);
    const { inputSize, outputSize, reduction, format, keptOriginalFormat } = optimizeResult;
    if (keptOriginalFormat) {
      log('✓', `${formatBytes(inputSize)} → ${formatBytes(outputSize)} (${reduction >= 0 ? '-' : '+'}${Math.abs(reduction)}%) [mantiene ${format.toUpperCase()}]`, 'green');
    } else {
      log('✓', `${formatBytes(inputSize)} → ${formatBytes(outputSize)} (-${reduction}%) [WebP]`, 'green');
    }
  } catch (error) {
    log('❌', `Error optimizando: ${error.message}`, 'red');
    process.exit(1);
  }

  // Determinar nombre final y ruta
  const { finalPath, format } = optimizeResult;
  const finalName = `${cleanName}.${format}`;
  const r2FileName = `${id}-${finalName}`;
  const r2Path = `img/${materia}/${r2FileName}`;

  // Verificar wrangler
  if (!checkWrangler()) {
    log('⚠️', 'Wrangler no está instalado o configurado', 'yellow');
    log('💡', 'Instala con: npm install -g wrangler && wrangler login', 'yellow');
    console.log('');
    log('📁', `Imagen optimizada guardada en: ${finalPath}`, 'blue');
    log('📋', 'Cuando configures R2, sube manualmente con:', 'gray');
    console.log(`   wrangler r2 object put ${CONFIG.r2Bucket}/${r2Path} --file="${finalPath}" --remote`);
    
    // Igual guardar en índice como pendiente
    index.images.push({
      id,
      name: finalName,
      materia,
      date: new Date().toISOString().split('T')[0],
      size: formatBytes(fs.statSync(finalPath).size),
      status: 'pending',
      localPath: finalPath
    });
    saveIndex(index);
    return;
  }

  // Subir a R2
  log('☁️', 'Subiendo a R2...', 'gray');
  if (uploadToR2(finalPath, r2Path)) {
    log('✓', `Subido: ${r2Path}`, 'green');
  } else {
    log('❌', 'Error subiendo a R2', 'red');
    process.exit(1);
  }

  // Generar URL y markdown
  const url = `https://${CONFIG.cdnDomain}/${r2Path}`;
  const markdown = `![${cleanName}](${url})`;

  // Copiar al clipboard
  console.log('');
  if (copyToClipboard(markdown)) {
    log('📋', 'Copiado al clipboard:', 'green');
  } else {
    log('📋', 'Copia esto:', 'blue');
  }
  console.log('');
  console.log(`   ${colors.yellow}${markdown}${colors.reset}`);
  console.log('');

  // Actualizar índice
  index.images.push({
    id,
    name: finalName,
    materia,
    date: new Date().toISOString().split('T')[0],
    size: formatBytes(fs.statSync(finalPath).size),
    url,
    status: 'uploaded'
  });
  saveIndex(index);

  // Limpiar archivos temporales
  fs.unlinkSync(finalPath);
  
  // Preguntar si eliminar original
  log('🗑️', `¿Eliminar original? Ejecuta: rm "${inputPath}"`, 'gray');
  
  console.log('');
  log('✅', '¡Listo! Pega el markdown en tu archivo (Cmd+V)', 'green');
}

// Mostrar ayuda
function showHelp() {
  console.log(`
${colors.blue}📸 Upload to R2 - Sistema de imágenes para Ediprofe${colors.reset}

${colors.yellow}Uso:${colors.reset}
  npm run img <archivo.png> --materia <materia>
  
${colors.yellow}Ejemplos:${colors.reset}
  npm run img grafica-velocidad.png --materia fisica
  npm run img orbital-3d.png --materia quimica
  
${colors.yellow}Comandos:${colors.reset}
  npm run img --list [materia]      Lista todas las imágenes
  npm run img --search <término>    Busca por nombre o ID
  npm run img --help                Muestra esta ayuda

${colors.yellow}Materias válidas:${colors.reset}
  ${CONFIG.materias.join(', ')}

${colors.yellow}Flujo:${colors.reset}
  1. Guarda tu imagen PNG en la carpeta ${colors.blue}inbox/${colors.reset}
  2. Ejecuta el comando con la materia correspondiente
  3. Pega el markdown generado en tu archivo (Cmd+V)
`);
}

// Obtener archivos de imagen en inbox
function getInboxFiles() {
  const validExtensions = ['.png', '.jpg', '.jpeg', '.webp', '.gif'];
  
  if (!fs.existsSync(CONFIG.inboxDir)) {
    return [];
  }
  
  return fs.readdirSync(CONFIG.inboxDir)
    .filter(file => {
      const ext = path.extname(file).toLowerCase();
      return validExtensions.includes(ext) && !file.startsWith('temp-') && !file.startsWith('.');
    })
    .sort();
}

// Menú interactivo
async function interactiveMode() {
  console.log('');
  log('📸', 'Subir imagen a R2', 'blue');
  console.log('');
  
  // Obtener archivos del inbox
  const inboxFiles = getInboxFiles();
  
  if (inboxFiles.length === 0) {
    log('📭', 'No hay imágenes en la carpeta inbox/', 'yellow');
    log('💡', 'Copia una imagen a inbox/ y vuelve a ejecutar:', 'gray');
    console.log(`   cp ~/Downloads/mi-imagen.png inbox/`);
    console.log('');
    return;
  }
  
  // Preparar choices con tamaño
  const fileChoices = inboxFiles.map(file => {
    const stats = fs.statSync(path.join(CONFIG.inboxDir, file));
    const sizeKB = Math.round(stats.size / 1024);
    return {
      name: `${file} (${sizeKB}KB)`,
      value: file
    };
  });
  
  // Seleccionar archivo con búsqueda/filtrado
  const selectedFile = await search({
    message: 'Busca y selecciona la imagen (escribe para filtrar):',
    source: async (input) => {
      if (!input) return fileChoices;
      const lower = input.toLowerCase();
      return fileChoices.filter(c => c.name.toLowerCase().includes(lower));
    }
  });
  
  // Seleccionar materia con flechas
  const selectedMateria = await select({
    message: 'Selecciona la materia (↑↓ para navegar):',
    choices: [
      { name: '1. ⚡ Física', value: 'fisica' },
      { name: '2. 🧮 Matemáticas', value: 'matematicas' },
      { name: '3. 🧪 Química', value: 'quimica' },
      { name: '4. 🌿 Ciencias', value: 'ciencias' }
    ]
  });
  
  console.log('');
  
  // Subir la imagen
  await uploadImage(selectedFile, selectedMateria);
  
  // Preguntar si eliminar el original
  const deleteOriginal = await confirm({
    message: '¿Eliminar la imagen original del inbox?',
    default: true
  });
  
  if (deleteOriginal) {
    const originalPath = path.join(CONFIG.inboxDir, selectedFile);
    if (fs.existsSync(originalPath)) {
      fs.unlinkSync(originalPath);
      log('🗑️', 'Imagen original eliminada', 'gray');
    }
  }
  
  // Preguntar si subir otra
  const remainingFiles = getInboxFiles();
  if (remainingFiles.length > 0) {
    const uploadAnother = await confirm({
      message: `¿Subir otra imagen? (${remainingFiles.length} restantes)`,
      default: false
    });
    
    if (uploadAnother) {
      await interactiveMode();
    }
  }
}

// Main
async function main() {
  const args = process.argv.slice(2);
  
  // Si no hay argumentos, modo interactivo
  if (args.length === 0) {
    await interactiveMode();
    return;
  }
  
  if (args.includes('--help') || args.includes('-h')) {
    showHelp();
    return;
  }

  const index = loadIndex();

  // Comando --list
  if (args.includes('--list')) {
    const listIndex = args.indexOf('--list');
    const materia = args[listIndex + 1];
    listImages(index, CONFIG.materias.includes(materia) ? materia : null);
    return;
  }

  // Comando --search
  if (args.includes('--search')) {
    const searchIndex = args.indexOf('--search');
    const query = args[searchIndex + 1];
    if (!query) {
      log('❌', 'Debes especificar un término de búsqueda', 'red');
      return;
    }
    searchImages(index, query);
    return;
  }

  // Subir imagen (modo directo)
  const fileName = args[0];
  const materiaIndex = args.indexOf('--materia');
  
  if (materiaIndex === -1 || !args[materiaIndex + 1]) {
    // Sin materia, preguntar interactivamente
    const selectedMateria = await select({
      message: 'Selecciona la materia (↑↓ para navegar):',
      choices: [
        { name: '1. ⚡ Física', value: 'fisica' },
        { name: '2. 🧮 Matemáticas', value: 'matematicas' },
        { name: '3. 🧪 Química', value: 'quimica' },
        { name: '4. 🌿 Ciencias', value: 'ciencias' }
      ]
    });
    await uploadImage(fileName, selectedMateria);
    return;
  }

  const materia = args[materiaIndex + 1];
  await uploadImage(fileName, materia);
}

main().catch(console.error);

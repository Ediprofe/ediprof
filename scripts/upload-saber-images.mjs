#!/usr/bin/env node
/**
 * Script para subir imágenes de talleres Saber a R2
 * Estructura: img/saber/{area}/{nombre}.webp
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const CONFIG = {
  r2Bucket: 'ediprofe',
  cdnDomain: 'cdn.ediprofe.com',
  areas: ['quimica', 'ciencias', 'fisica', 'matematicas']
};

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

function checkWrangler() {
  try {
    execSync('wrangler --version', { stdio: 'pipe' });
    return true;
  } catch {
    return false;
  }
}

function uploadToR2(localPath, r2Path) {
  try {
    execSync(`wrangler r2 object put ${CONFIG.r2Bucket}/${r2Path} --file="${localPath}" --remote`, {
      stdio: 'pipe'
    });
    return true;
  } catch (error) {
    console.error('Error:', error.message);
    return false;
  }
}

async function main() {
  console.log('');
  log('📸', 'Subiendo imágenes de talleres Saber a R2', 'blue');
  console.log('');

  if (!checkWrangler()) {
    log('❌', 'Wrangler no está instalado o configurado', 'red');
    log('💡', 'Instala con: npm install -g wrangler && wrangler login', 'yellow');
    process.exit(1);
  }

  const results = {
    uploaded: [],
    failed: [],
    skipped: []
  };

  for (const area of CONFIG.areas) {
    const inboxDir = `inbox/saber-${area}`;
    
    if (!fs.existsSync(inboxDir)) {
      log('⏭️', `Carpeta ${inboxDir} no existe, saltando...`, 'gray');
      continue;
    }

    const files = fs.readdirSync(inboxDir).filter(f => f.endsWith('.webp'));
    
    if (files.length === 0) {
      log('📭', `No hay imágenes en ${inboxDir}`, 'gray');
      continue;
    }

    log('📁', `Procesando ${area}: ${files.length} imágenes`, 'blue');
    console.log('');

    for (const file of files) {
      const localPath = path.join(inboxDir, file);
      const r2Path = `img/saber/${area}/${file}`;
      const url = `https://${CONFIG.cdnDomain}/${r2Path}`;

      process.stdout.write(`  ${file}... `);

      if (uploadToR2(localPath, r2Path)) {
        console.log(`${colors.green}✓${colors.reset}`);
        results.uploaded.push({ file, area, url });
      } else {
        console.log(`${colors.red}✗${colors.reset}`);
        results.failed.push({ file, area });
      }
    }
    console.log('');
  }

  // Resumen
  console.log('');
  log('📊', 'Resumen:', 'blue');
  log('✅', `Subidas: ${results.uploaded.length}`, 'green');
  if (results.failed.length > 0) {
    log('❌', `Fallidas: ${results.failed.length}`, 'red');
  }
  
  // Generar archivo de mapeo
  if (results.uploaded.length > 0) {
    const mapping = {};
    results.uploaded.forEach(({ file, area, url }) => {
      const baseName = path.basename(file, '.webp');
      if (!mapping[area]) mapping[area] = {};
      mapping[area][baseName] = url;
    });

    fs.writeFileSync('saber-images-mapping.json', JSON.stringify(mapping, null, 2));
    log('📝', 'Mapeo guardado en: saber-images-mapping.json', 'blue');
  }

  console.log('');
  log('✅', '¡Listo!', 'green');
}

main().catch(console.error);

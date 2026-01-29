#!/usr/bin/env node
/**
 * Script para actualizar rutas de imágenes en talleres Saber
 * Convierte rutas locales a URLs de CDN
 */

import fs from 'fs';
import path from 'path';

const mapping = JSON.parse(fs.readFileSync('saber-images-mapping.json', 'utf-8'));

function updateImagePaths(content, area) {
  if (!mapping[area]) {
    console.log(`⚠️  No hay mapeo para ${area}`);
    return content;
  }

  let updated = content;
  let count = 0;

  // Patrón para encontrar imágenes: ![alt](ruta)
  const imageRegex = /!\[([^\]]*)\]\(([^)]+)\)/g;

  updated = content.replace(imageRegex, (match, alt, imagePath) => {
    // Extraer nombre del archivo sin extensión
    const fileName = path.basename(imagePath, path.extname(imagePath));
    
    // Buscar en el mapeo
    if (mapping[area][fileName]) {
      count++;
      return `![${alt}](${mapping[area][fileName]})`;
    }
    
    return match;
  });

  console.log(`  ✓ Actualizadas ${count} imágenes`);
  return updated;
}

function processFile(filePath, area) {
  console.log(`\n📄 Procesando: ${filePath}`);
  
  const content = fs.readFileSync(filePath, 'utf-8');
  const updated = updateImagePaths(content, area);
  
  if (content !== updated) {
    fs.writeFileSync(filePath, updated);
    console.log(`  ✅ Archivo actualizado`);
  } else {
    console.log(`  ⏭️  Sin cambios`);
  }
}

// Procesar talleres
console.log('\n📸 Actualizando rutas de imágenes en talleres Saber\n');

// Química
const quimicaTaller = 'src/content/saber/quimica/01-la-materia/taller.md';
if (fs.existsSync(quimicaTaller)) {
  processFile(quimicaTaller, 'quimica');
}

console.log('\n✅ ¡Listo!\n');

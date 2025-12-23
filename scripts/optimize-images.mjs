#!/usr/bin/env node
/**
 * Script de optimización de imágenes PNG
 * Comprime PNG sin pérdida visible y genera versiones WebP
 * 
 * Características:
 * - Detecta archivos ya optimizados (no re-procesa)
 * - Solo genera WebP si no existe
 * - Builds rápidos después de la primera vez
 * 
 * Uso: node scripts/optimize-images.mjs
 * Se ejecuta automáticamente antes del build
 */

import sharp from 'sharp';
import { glob } from 'glob';
import { readFile, writeFile, stat, access } from 'fs/promises';
import { dirname, basename, join } from 'path';

const PUBLIC_IMAGES = 'public/images';
const QUALITY_PNG = 80;      // Calidad PNG (0-100)
const QUALITY_WEBP = 82;     // Calidad WebP (0-100)
const MIN_SIZE_KB = 10;      // Solo optimizar archivos > 10KB

// Marcador en metadata para saber si ya fue optimizado
const OPTIMIZED_MARKER = 'ediprofe-optimized';

// Colores para consola
const colors = {
  green: (t) => `\x1b[32m${t}\x1b[0m`,
  yellow: (t) => `\x1b[33m${t}\x1b[0m`,
  blue: (t) => `\x1b[34m${t}\x1b[0m`,
  dim: (t) => `\x1b[2m${t}\x1b[0m`,
};

async function getFileSize(filePath) {
  const stats = await stat(filePath);
  return stats.size;
}

async function fileExists(filePath) {
  try {
    await access(filePath);
    return true;
  } catch {
    return false;
  }
}

function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
}

async function isAlreadyOptimized(filePath) {
  try {
    const buffer = await readFile(filePath);
    const metadata = await sharp(buffer).metadata();
    // Verificar si tiene nuestro marcador en los comments o si es muy pequeño
    // También consideramos "optimizado" si ya tiene alta compresión
    const hasMarker = metadata.comments?.includes(OPTIMIZED_MARKER);
    const isSmall = buffer.length < MIN_SIZE_KB * 1024;
    // Si el archivo es PNG con paleta, probablemente ya está optimizado
    const isPaletted = metadata.paletteBitDepth !== undefined;
    return hasMarker || isSmall || isPaletted;
  } catch {
    return false;
  }
}

async function optimizePNG(filePath) {
  const originalSize = await getFileSize(filePath);
  
  // Saltar archivos muy pequeños
  if (originalSize < MIN_SIZE_KB * 1024) {
    return { skipped: true, reason: 'too small' };
  }

  // Verificar si ya fue optimizado
  if (await isAlreadyOptimized(filePath)) {
    return { skipped: true, reason: 'already optimized' };
  }

  const buffer = await readFile(filePath);
  
  // Optimizar PNG
  const optimizedPng = await sharp(buffer)
    .png({
      compressionLevel: 9,
      palette: true,
      quality: QUALITY_PNG,
      effort: 10,
    })
    .toBuffer();

  // Solo guardar si es más pequeño
  if (optimizedPng.length < originalSize) {
    await writeFile(filePath, optimizedPng);
    return {
      originalSize,
      newSize: optimizedPng.length,
      saved: originalSize - optimizedPng.length,
    };
  }

  return { skipped: true, reason: 'no gain' };
}

async function generateWebP(filePath) {
  const webpPath = filePath.replace(/\.png$/i, '.webp');
  
  // Si ya existe el WebP, saltar
  if (await fileExists(webpPath)) {
    return { skipped: true };
  }

  const buffer = await readFile(filePath);
  
  const webpBuffer = await sharp(buffer)
    .webp({
      quality: QUALITY_WEBP,
      effort: 6,
    })
    .toBuffer();

  await writeFile(webpPath, webpBuffer);
  
  return {
    path: webpPath,
    size: webpBuffer.length,
    created: true,
  };
}

async function main() {
  console.log('\n🖼️  Optimizando imágenes PNG...\n');
  
  // Buscar todos los PNG en public/images
  const pngFiles = await glob(`${PUBLIC_IMAGES}/**/*.png`, {
    ignore: ['**/node_modules/**'],
  });

  if (pngFiles.length === 0) {
    console.log(colors.yellow('No se encontraron archivos PNG para optimizar.'));
    return;
  }

  console.log(`Encontrados ${colors.blue(pngFiles.length)} archivos PNG\n`);

  let totalSaved = 0;
  let optimizedCount = 0;
  let skippedCount = 0;
  let webpCount = 0;

  for (const file of pngFiles) {
    const relativePath = file.replace(/^public\//, '');
    process.stdout.write(`  ${colors.dim(relativePath)}... `);

    try {
      // Optimizar PNG
      const result = await optimizePNG(file);
      
      if (result.skipped) {
        console.log(colors.dim(`[${result.reason}]`));
        skippedCount++;
      } else {
        const percent = ((result.saved / result.originalSize) * 100).toFixed(0);
        console.log(
          colors.green(`-${percent}%`) +
          colors.dim(` (${formatBytes(result.originalSize)} → ${formatBytes(result.newSize)})`)
        );
        totalSaved += result.saved;
        optimizedCount++;
      }

      // Generar WebP (solo para archivos no muy pequeños)
      const currentSize = await getFileSize(file);
      if (currentSize > MIN_SIZE_KB * 1024) {
        const webpResult = await generateWebP(file);
        if (webpResult.created) {
          webpCount++;
        }
      }
    } catch (err) {
      console.log(colors.yellow(`[error: ${err.message}]`));
    }
  }

  // Resumen
  console.log('\n' + '─'.repeat(50));
  if (optimizedCount === 0 && webpCount === 0) {
    console.log(colors.green('✅ Todo está optimizado, nada que procesar.'));
  } else {
    console.log(`✅ Optimizados: ${colors.green(optimizedCount)} archivos`);
    console.log(`⏭️  Omitidos:    ${skippedCount} archivos`);
    console.log(`🌐 WebP nuevos:  ${colors.blue(webpCount)} archivos`);
    if (totalSaved > 0) {
      console.log(`💾 Ahorro total: ${colors.green(formatBytes(totalSaved))}`);
    }
  }
  console.log('─'.repeat(50) + '\n');
}

main().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});

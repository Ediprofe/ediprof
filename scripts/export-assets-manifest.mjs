#!/usr/bin/env node

/**
 * Genera un manifiesto canónico de assets desde images-index.json
 * para consumo por backend/app móvil.
 *
 * Uso:
 *   node scripts/export-assets-manifest.mjs
 *   node scripts/export-assets-manifest.mjs --output docs/new-features/assets-manifest.json
 */

import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { dirname, resolve } from 'path';

const DEFAULT_INDEX = 'images-index.json';
const DEFAULT_OUTPUT = '/tmp/ediprofe-assets-manifest.json';
const CDN_DOMAIN = 'cdn.ediprofe.com';

function parseArgs(argv) {
  const args = {
    index: DEFAULT_INDEX,
    output: DEFAULT_OUTPUT,
  };

  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (token === '--index' && argv[i + 1]) {
      args.index = argv[i + 1];
      i += 1;
    } else if (token === '--output' && argv[i + 1]) {
      args.output = argv[i + 1];
      i += 1;
    }
  }

  return args;
}

function buildCanonicalPath({ materia, id, name, type }) {
  return type === 'saber'
    ? `img/saber/${materia}/${id}-${name}`
    : `img/${materia}/${id}-${name}`;
}

function normalizeCdnUrl(url) {
  if (!url || typeof url !== 'string') return '';
  if (!url.startsWith('https://')) return '';
  return url.replace(`https://${CDN_DOMAIN}/images/`, `https://${CDN_DOMAIN}/img/`);
}

function toCanonical(entry) {
  const aliases = Array.isArray(entry.aliases) ? [...entry.aliases] : [];
  const normalizedUrl = normalizeCdnUrl(entry.canonicalUrl || entry.url);

  if ((entry.url || '').startsWith(`https://${CDN_DOMAIN}/images/`)) {
    aliases.push(entry.url);
  }

  let canonicalUrl = normalizedUrl;
  if (!canonicalUrl && entry.status === 'uploaded' && entry.id && entry.name && entry.materia) {
    canonicalUrl = `https://${CDN_DOMAIN}/${buildCanonicalPath({
      materia: entry.materia,
      id: entry.id,
      name: entry.name,
      type: entry.type,
    })}`;
  }

  const canonicalPath = canonicalUrl
    ? canonicalUrl.replace(`https://${CDN_DOMAIN}/`, '')
    : (entry.canonicalPath || '');

  return {
    id: entry.id,
    materia: entry.materia,
    name: entry.name,
    type: entry.type || 'lesson',
    status: entry.status || 'unknown',
    date: entry.date || null,
    size: entry.size || null,
    canonicalUrl,
    canonicalPath,
    aliases: [...new Set(aliases)].sort(),
  };
}

function main() {
  const { index, output } = parseArgs(process.argv.slice(2));
  const raw = JSON.parse(readFileSync(resolve(index), 'utf-8'));
  const images = Array.isArray(raw.images) ? raw.images : [];

  const assets = images.map(toCanonical);
  const uploadedAssets = assets.filter((a) => a.status === 'uploaded');
  const withoutCanonical = uploadedAssets.filter((a) => !a.canonicalUrl);

  const duplicates = new Map();
  uploadedAssets.forEach((asset) => {
    if (!asset.id) return;
    duplicates.set(asset.id, (duplicates.get(asset.id) || 0) + 1);
  });

  const duplicateIds = [...duplicates.entries()]
    .filter(([, count]) => count > 1)
    .map(([id]) => id)
    .sort();

  const manifest = {
    generatedAt: new Date().toISOString(),
    sourceIndex: index,
    cdnDomain: CDN_DOMAIN,
    totals: {
      entries: assets.length,
      uploaded: uploadedAssets.length,
      pending: assets.filter((a) => a.status === 'pending').length,
      withoutCanonical: withoutCanonical.length,
      duplicateIds: duplicateIds.length,
    },
    duplicateIds,
    assets,
  };

  const outputPath = resolve(output);
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(manifest, null, 2));

  console.log('📦 Assets manifest generado');
  console.log(`   Total entradas: ${manifest.totals.entries}`);
  console.log(`   Subidas:        ${manifest.totals.uploaded}`);
  console.log(`   Pendientes:     ${manifest.totals.pending}`);
  console.log(`   Sin canónica:   ${manifest.totals.withoutCanonical}`);
  console.log(`   IDs duplicados: ${manifest.totals.duplicateIds}`);
  console.log(`   Archivo:        ${output}`);
}

main();

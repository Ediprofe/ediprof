#!/usr/bin/env node

/**
 * Auditoría de referencias de assets en contenido Markdown/MDX.
 *
 * Objetivo:
 * - Detectar rutas legacy y mezcla de convenciones.
 * - Mantener modo no bloqueante por defecto.
 *
 * Uso:
 *   node scripts/assets-audit.mjs
 *   node scripts/assets-audit.mjs --strict
 *   node scripts/assets-audit.mjs --output docs/new-features/assets-audit-report.json
 */

import { readFileSync, mkdirSync, writeFileSync, existsSync } from 'fs';
import { dirname, resolve } from 'path';
import { globSync } from 'glob';

const DEFAULT_OUTPUT = '/tmp/ediprofe-assets-audit-report.json';
const CONTENT_GLOB = 'src/content/**/*.{md,mdx}';

function parseArgs(argv) {
  const args = {
    strict: false,
    output: DEFAULT_OUTPUT,
    baseline: null,
  };

  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (token === '--strict') {
      args.strict = true;
    } else if (token === '--output' && argv[i + 1]) {
      args.output = argv[i + 1];
      i += 1;
    } else if (token === '--baseline' && argv[i + 1]) {
      args.baseline = argv[i + 1];
      i += 1;
    }
  }

  return args;
}

function compareWithBaseline(categories, baselinePath) {
  const resolvedBaseline = resolve(baselinePath);
  if (!existsSync(resolvedBaseline)) {
    throw new Error(`No existe el baseline: ${baselinePath}`);
  }

  const raw = JSON.parse(readFileSync(resolvedBaseline, 'utf-8'));
  const baselineCategories = raw.categories || {};
  const regressions = [];

  for (const [category, maxAllowed] of Object.entries(baselineCategories)) {
    if (typeof maxAllowed !== 'number') continue;
    const current = categories[category] || 0;
    if (current > maxAllowed) {
      regressions.push({
        category,
        current,
        maxAllowed,
        delta: current - maxAllowed,
      });
    }
  }

  return {
    baselinePath: resolvedBaseline,
    regressions,
    trackedCategories: Object.keys(baselineCategories),
  };
}

function normalizeRef(rawRef) {
  if (!rawRef) return '';
  const trimmed = rawRef.trim();
  // Eliminar query/hash para clasificar rutas de forma estable.
  return trimmed.replace(/[?#].*$/, '');
}

function isAssetLike(ref) {
  if (!ref) return false;

  return (
    ref.startsWith('/images/') ||
    ref.startsWith('/ilustraciones/') ||
    ref.startsWith('/illustrations/') ||
    ref.startsWith('https://cdn.ediprofe.com/') ||
    /\.(png|jpg|jpeg|webp|svg|gif|avif)$/i.test(ref)
  );
}

function classifyRef(ref) {
  if (ref.startsWith('https://cdn.ediprofe.com/img/')) return 'canonical_cdn';
  if (ref.startsWith('https://cdn.ediprofe.com/images/')) return 'legacy_cdn_images';
  if (ref.startsWith('https://cdn.ediprofe.com/')) return 'cdn_other';
  if (ref.startsWith('/images/')) return 'local_images';
  if (ref.startsWith('/ilustraciones/')) return 'local_ilustraciones';
  if (ref.startsWith('/illustrations/')) return 'local_illustrations';
  if (ref.startsWith('http://') || ref.startsWith('https://')) return 'external_url';
  return 'relative_or_unknown';
}

function extractRefs(content) {
  const refs = [];

  // Markdown images/links
  const mdRefRegex = /!?\[[^\]]*\]\(([^)]+)\)/g;
  let match = null;
  while ((match = mdRefRegex.exec(content)) !== null) {
    const raw = match[1]?.trim() ?? '';
    const ref = normalizeRef(raw.split(/\s+"/)[0]);
    if (isAssetLike(ref)) refs.push(ref);
  }

  // HTML src/href
  const htmlRefRegex = /\b(?:src|href)\s*=\s*["']([^"']+)["']/g;
  while ((match = htmlRefRegex.exec(content)) !== null) {
    const ref = normalizeRef(match[1]);
    if (isAssetLike(ref)) refs.push(ref);
  }

  return refs;
}

function main() {
  const { strict, output, baseline } = parseArgs(process.argv.slice(2));
  const files = globSync(CONTENT_GLOB, { nodir: true }).sort();

  const categories = {
    canonical_cdn: 0,
    legacy_cdn_images: 0,
    cdn_other: 0,
    local_images: 0,
    local_ilustraciones: 0,
    local_illustrations: 0,
    external_url: 0,
    relative_or_unknown: 0,
  };

  const fileSummaries = [];
  const legacyRefs = new Set();
  let totalRefs = 0;

  for (const file of files) {
    const content = readFileSync(file, 'utf-8');
    const refs = extractRefs(content);
    if (refs.length === 0) continue;

    const perFile = {
      file,
      total: refs.length,
      categories: {},
      refs: [],
    };

    refs.forEach((ref) => {
      const type = classifyRef(ref);
      categories[type] += 1;
      totalRefs += 1;
      perFile.categories[type] = (perFile.categories[type] || 0) + 1;

      if (type !== 'canonical_cdn') {
        legacyRefs.add(ref);
      }

      perFile.refs.push({ ref, type });
    });

    fileSummaries.push(perFile);
  }

  const legacyCount =
    categories.legacy_cdn_images +
    categories.local_images +
    categories.local_ilustraciones +
    categories.local_illustrations +
    categories.cdn_other +
    categories.relative_or_unknown;

  const report = {
    generatedAt: new Date().toISOString(),
    strictMode: strict,
    scanned: {
      files: files.length,
      filesWithAssetRefs: fileSummaries.length,
      refs: totalRefs,
    },
    categories,
    summary: {
      canonicalRefs: categories.canonical_cdn,
      legacyOrNonCanonicalRefs: legacyCount,
      externalRefs: categories.external_url,
    },
    uniqueLegacyRefs: [...legacyRefs].sort(),
    files: fileSummaries,
  };

  const outputPath = resolve(output);
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(report, null, 2));

  console.log('📊 Auditoría de assets');
  console.log(`   Archivos escaneados: ${files.length}`);
  console.log(`   Archivos con refs:   ${fileSummaries.length}`);
  console.log(`   Refs totales:        ${totalRefs}`);
  console.log(`   Canonical CDN:       ${categories.canonical_cdn}`);
  console.log(`   Legacy/no canónico:  ${legacyCount}`);
  console.log(`   Externas:            ${categories.external_url}`);
  console.log(`   Reporte:             ${output}`);

  if (baseline) {
    try {
      const baselineResult = compareWithBaseline(categories, baseline);
      console.log(`   Baseline:            ${baselineResult.baselinePath}`);
      console.log(
        `   Categorías baseline: ${baselineResult.trackedCategories.join(', ') || '(ninguna)'}`
      );

      if (baselineResult.regressions.length > 0) {
        console.error('⚠️  Regresiones detectadas contra baseline:');
        baselineResult.regressions.forEach((regression) => {
          console.error(
            `   - ${regression.category}: actual=${regression.current}, máximo=${regression.maxAllowed}, +${regression.delta}`
          );
        });
        if (strict) {
          process.exit(1);
        }
      } else {
        console.log('✅ Sin regresiones contra baseline.');
      }
    } catch (error) {
      console.error(`❌ Error validando baseline: ${error.message}`);
      process.exit(1);
    }
    return;
  }

  if (strict && legacyCount > 0) {
    console.error('❌ Modo strict: se detectaron referencias legacy/no canónicas.');
    process.exit(1);
  }
}

main();

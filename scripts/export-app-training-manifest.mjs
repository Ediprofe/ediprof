#!/usr/bin/env node

/**
 * Exporta un manifiesto de app (entrenamiento) desde el content manifest.
 *
 * Uso:
 *   node scripts/export-app-training-manifest.mjs
 *   node scripts/export-app-training-manifest.mjs --content-manifest /tmp/ediprofe-content-manifest.json
 *   node scripts/export-app-training-manifest.mjs --overrides docs/new-features/samples/app-content-overrides.example.json
 *   node scripts/export-app-training-manifest.mjs --output /tmp/ediprofe-app-training-manifest.json
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { dirname, resolve } from 'path';

const DEFAULT_CONTENT_MANIFEST = '/tmp/ediprofe-content-manifest.json';
const DEFAULT_OVERRIDES = 'docs/new-features/samples/app-content-overrides.example.json';
const DEFAULT_OUTPUT = '/tmp/ediprofe-app-training-manifest.json';

function parseArgs(argv) {
  const args = {
    contentManifest: DEFAULT_CONTENT_MANIFEST,
    overrides: DEFAULT_OVERRIDES,
    output: DEFAULT_OUTPUT,
    includeDrafts: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === '--content-manifest' && argv[i + 1]) {
      args.contentManifest = argv[i + 1];
      i += 1;
    } else if (token === '--overrides' && argv[i + 1]) {
      args.overrides = argv[i + 1];
      i += 1;
    } else if (token === '--output' && argv[i + 1]) {
      args.output = argv[i + 1];
      i += 1;
    } else if (token === '--include-drafts') {
      args.includeDrafts = true;
    }
  }

  return args;
}

function readJsonOrNull(pathLike) {
  const fullPath = resolve(pathLike);
  if (!existsSync(fullPath)) return null;
  return JSON.parse(readFileSync(fullPath, 'utf-8'));
}

function buildOverridesMap(overridesDoc) {
  const map = new Map();
  if (!overridesDoc || !Array.isArray(overridesDoc.entries)) return map;

  overridesDoc.entries.forEach((entry) => {
    if (!entry || typeof entry.route !== 'string') return;
    map.set(entry.route, entry);
  });

  return map;
}

function pickPreviewAssets(assetRefs) {
  if (!Array.isArray(assetRefs)) return [];

  return assetRefs
    .filter((ref) => ref.startsWith('https://cdn.ediprofe.com/img/'))
    .slice(0, 4);
}

function inferSurface(entry, override) {
  if (override?.surface) return override.surface;
  if (entry.contentType === 'workshop') return 'app';
  return 'web';
}

function inferAccessTier(entry, override) {
  if (override?.access_tier) return override.access_tier;
  return entry.accessTier || 'free';
}

function inferAppModule(entry, override) {
  if (override?.app_module) return override.app_module;
  if (entry.contentType === 'workshop') return 'workshop';
  if (entry.route.includes('/resumen')) return 'tactical_summary';
  return 'theory_reference';
}

function defaultPractice(moduleName) {
  if (moduleName === 'workshop') {
    return {
      recommended_questions: 20,
      recommended_minutes: 35,
      difficulty_mix: { easy: 5, medium: 10, hard: 5 },
    };
  }

  if (moduleName === 'tactical_summary') {
    return {
      recommended_questions: 8,
      recommended_minutes: 15,
      difficulty_mix: { easy: 3, medium: 4, hard: 1 },
    };
  }

  return {
    recommended_questions: 5,
    recommended_minutes: 10,
    difficulty_mix: { easy: 3, medium: 2, hard: 0 },
  };
}

function buildCard(entry, override) {
  const defaultHeadline = entry.contentType === 'workshop'
    ? `Entrenamiento: ${entry.title}`
    : entry.title;

  const defaultSubtitle = entry.contentType === 'workshop'
    ? 'Practica cronometrada con retroalimentacion'
    : `${entry.area?.name || entry.collectionName} · ${entry.unidad?.name || 'Contenido base'}`;

  return {
    headline: override?.card?.headline || defaultHeadline,
    subtitle: override?.card?.subtitle || defaultSubtitle,
  };
}

function buildTacticalSummary(override) {
  if (!override?.tactical_summary) return null;

  return {
    key_points: Array.isArray(override.tactical_summary.key_points)
      ? override.tactical_summary.key_points
      : [],
    common_traps: Array.isArray(override.tactical_summary.common_traps)
      ? override.tactical_summary.common_traps
      : [],
    micro_plan: Array.isArray(override.tactical_summary.micro_plan)
      ? override.tactical_summary.micro_plan
      : [],
  };
}

function buildAppEntry(entry, override) {
  const moduleName = inferAppModule(entry, override);

  return {
    id: entry.id,
    route: entry.route,
    site_url: entry.siteUrl,
    collection: entry.collection,
    content_type: entry.contentType,
    module: moduleName,
    surface: inferSurface(entry, override),
    access_tier: inferAccessTier(entry, override),
    published: Boolean(entry.flags?.published),
    card: buildCard(entry, override),
    taxonomy: {
      area: entry.area,
      unidad: entry.unidad,
      tema: entry.tema,
    },
    tactical_summary: buildTacticalSummary(override),
    practice: override?.practice || defaultPractice(moduleName),
    assets: {
      preview: pickPreviewAssets(entry.assets?.refs || []),
      total_refs: entry.assets?.total || 0,
    },
  };
}

function buildTotals(appEntries) {
  const totals = {
    entries: appEntries.length,
    published: 0,
    free: 0,
    premium: 0,
    by_surface: {},
    by_module: {},
  };

  appEntries.forEach((entry) => {
    if (entry.published) totals.published += 1;
    if (entry.access_tier === 'premium') totals.premium += 1;
    else totals.free += 1;

    totals.by_surface[entry.surface] = (totals.by_surface[entry.surface] || 0) + 1;
    totals.by_module[entry.module] = (totals.by_module[entry.module] || 0) + 1;
  });

  return totals;
}

function main() {
  const { contentManifest, overrides, output, includeDrafts } = parseArgs(process.argv.slice(2));

  const manifest = readJsonOrNull(contentManifest);
  if (!manifest || !Array.isArray(manifest.entries)) {
    console.error(`No se pudo cargar content manifest: ${contentManifest}`);
    console.error('Primero ejecuta: npm run content:manifest');
    process.exit(1);
  }

  const overridesDoc = readJsonOrNull(overrides);
  const overridesMap = buildOverridesMap(overridesDoc);

  const baseEntries = includeDrafts
    ? manifest.entries
    : manifest.entries.filter((entry) => entry.flags?.published);

  const appEntries = baseEntries
    .map((entry) => {
      const override = overridesMap.get(entry.route);
      return buildAppEntry(entry, override);
    })
    .filter((entry) => entry.surface === 'app' || entry.surface === 'both');

  const appManifest = {
    generatedAt: new Date().toISOString(),
    contractVersion: 1,
    source: {
      contentManifest: resolve(contentManifest),
      overrides: existsSync(resolve(overrides)) ? resolve(overrides) : null,
      includeDrafts,
    },
    strategy: {
      principle: 'App de entrenamiento, no espejo de la web.',
      freeLayer: 'resumenes tacticos y diagnostico base',
      premiumLayer: 'talleres, simulacros y retroalimentacion avanzada',
    },
    totals: buildTotals(appEntries),
    entries: appEntries,
  };

  const outputPath = resolve(output);
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(appManifest, null, 2));

  console.log('App training manifest generated');
  console.log(`   Entries:     ${appManifest.totals.entries}`);
  console.log(`   Published:   ${appManifest.totals.published}`);
  console.log(`   Free:        ${appManifest.totals.free}`);
  console.log(`   Premium:     ${appManifest.totals.premium}`);
  console.log(`   Output:      ${output}`);
}

main();

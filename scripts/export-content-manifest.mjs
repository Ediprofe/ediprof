#!/usr/bin/env node

/**
 * Genera un manifiesto de contenido desde src/content para consumo de backend/app.
 *
 * Uso:
 *   node scripts/export-content-manifest.mjs
 *   node scripts/export-content-manifest.mjs --output /tmp/ediprofe-content-manifest.json
 *   node scripts/export-content-manifest.mjs --published-only
 */

import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { basename, dirname, extname, relative, resolve } from 'path';
import { globSync } from 'glob';

const DEFAULT_OUTPUT = '/tmp/ediprofe-content-manifest.json';
const CONTENT_GLOB = 'src/content/**/*.{md,mdx}';
const META_GLOB = 'src/content/**/_meta.json';
const SITE_URL = 'https://ediprofe.com';

const MATERIA_NAMES = {
  matematicas: 'Matematicas',
  fisica: 'Fisica',
  quimica: 'Quimica',
  ciencias: 'Ciencias',
  saber: 'Talleres Saber',
};

function parseArgs(argv) {
  const args = {
    output: DEFAULT_OUTPUT,
    publishedOnly: false,
  };

  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (token === '--output' && argv[i + 1]) {
      args.output = argv[i + 1];
      i += 1;
    } else if (token === '--published-only') {
      args.publishedOnly = true;
    }
  }

  return args;
}

function normalizePath(pathLike) {
  return pathLike.replace(/\\/g, '/');
}

function stripNumericPrefix(segment) {
  return segment.replace(/^\d+-/, '');
}

function cleanSlug(slug) {
  return slug
    .split('/')
    .map((segment) => stripNumericPrefix(segment))
    .join('/');
}

function cleanSlugLower(slug) {
  return slug
    .split('/')
    .map((segment) => stripNumericPrefix(segment).toLowerCase())
    .join('/');
}

function formatNameFromSlug(slug) {
  return stripNumericPrefix(slug)
    .split('-')
    .filter(Boolean)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function parseFrontmatter(raw) {
  if (!raw.startsWith('---\n')) {
    return { data: {}, content: raw };
  }

  const endIndex = raw.indexOf('\n---\n', 4);
  if (endIndex === -1) {
    return { data: {}, content: raw };
  }

  const block = raw.slice(4, endIndex);
  const content = raw.slice(endIndex + 5);
  const data = {};

  block.split('\n').forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;

    const separator = trimmed.indexOf(':');
    if (separator === -1) return;

    const key = trimmed.slice(0, separator).trim();
    const value = trimmed.slice(separator + 1).trim();

    if (!key) return;
    data[key] = parseScalar(value);
  });

  return { data, content };
}

function parseScalar(value) {
  if (value === 'true') return true;
  if (value === 'false') return false;
  if (/^-?\d+$/.test(value)) return Number.parseInt(value, 10);
  if (/^-?\d+\.\d+$/.test(value)) return Number.parseFloat(value);
  if (
    (value.startsWith('"') && value.endsWith('"')) ||
    (value.startsWith("'") && value.endsWith("'"))
  ) {
    return value.slice(1, -1);
  }
  return value;
}

function extractH1(content) {
  const match = content.match(/^#\s+(.+)$/m);
  if (!match) return null;

  return match[1]
    .replace(/\*\*/g, '')
    .replace(/`/g, '')
    .replace(/[\u{1F300}-\u{1FAFF}]/gu, '')
    .replace(/[\u{2600}-\u{27BF}]/gu, '')
    .trim();
}

function extractOrder(fileName) {
  const match = fileName.match(/^(\d+)-/);
  return match ? Number.parseInt(match[1], 10) : null;
}

function loadMetaMap() {
  const metaMap = {};
  const metaFiles = globSync(META_GLOB, { nodir: true }).sort();

  metaFiles.forEach((file) => {
    const raw = JSON.parse(readFileSync(file, 'utf-8'));
    const rel = normalizePath(relative('src/content', file));
    const keyRaw = rel.replace(/\/_meta\.json$/, '');
    const key = cleanSlugLower(keyRaw);
    metaMap[key] = raw;
  });

  return metaMap;
}

function getMetaEntry(metaMap, key) {
  return metaMap[key] || null;
}

function extractAssetRefs(content) {
  const refs = [];

  const markdownRegex = /!?\[[^\]]*\]\(([^)]+)\)/g;
  const htmlRegex = /\b(?:src|href)\s*=\s*["']([^"']+)["']/g;

  let match = null;
  while ((match = markdownRegex.exec(content)) !== null) {
    const rawRef = (match[1] || '').trim();
    const ref = rawRef.split(/\s+"/)[0].replace(/[?#].*$/, '');
    if (isAssetLike(ref)) refs.push(ref);
  }

  while ((match = htmlRegex.exec(content)) !== null) {
    const ref = (match[1] || '').trim().replace(/[?#].*$/, '');
    if (isAssetLike(ref)) refs.push(ref);
  }

  return [...new Set(refs)].sort();
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

function classifyAssetRef(ref) {
  if (ref.startsWith('https://cdn.ediprofe.com/img/')) return 'canonical_cdn';
  if (ref.startsWith('https://cdn.ediprofe.com/images/')) return 'legacy_cdn_images';
  if (ref.startsWith('https://cdn.ediprofe.com/')) return 'cdn_other';
  if (ref.startsWith('/images/')) return 'local_images';
  if (ref.startsWith('/ilustraciones/')) return 'local_ilustraciones';
  if (ref.startsWith('/illustrations/')) return 'local_illustrations';
  if (ref.startsWith('http://') || ref.startsWith('https://')) return 'external_url';
  return 'relative_or_unknown';
}

function getAccessTier(frontmatter, collection) {
  const raw = String(frontmatter.access_tier || frontmatter.access || frontmatter.tier || '').toLowerCase().trim();

  if (raw === 'premium' || raw === 'paid') return 'premium';
  if (raw === 'free' || raw === 'public') return 'free';

  return collection === 'saber' ? 'premium' : 'free';
}

function buildMetaChainKeys(collection, slugRaw) {
  const dir = dirname(slugRaw);
  if (dir === '.' || dir === '') {
    return [collection];
  }

  const segments = normalizePath(dir).split('/').filter(Boolean);
  const keys = [collection];

  for (let i = 0; i < segments.length; i++) {
    const prefix = segments.slice(0, i + 1).join('/');
    keys.push(`${collection}/${cleanSlugLower(prefix)}`);
  }

  return [...new Set(keys)];
}

function resolveTitle(frontmatter, content, fileStem, deepestMeta) {
  if (typeof frontmatter.title === 'string' && frontmatter.title.trim()) {
    return frontmatter.title.trim();
  }

  const h1 = extractH1(content);
  if (h1) return h1;

  if (deepestMeta?.name) return String(deepestMeta.name);

  return formatNameFromSlug(fileStem);
}

function buildEntry(file, metaMap) {
  const rel = normalizePath(relative('src/content', file));
  const parsed = rel.match(/^([^/]+)\/(.+)\.(md|mdx)$/);
  if (!parsed) return null;

  const [, collection, slugRaw, extension] = parsed;
  const slugClean = cleanSlug(slugRaw);
  const slugPartsRaw = slugRaw.split('/');
  const slugPartsClean = slugClean.split('/');
  const fileStem = basename(slugRaw);

  const rawFile = readFileSync(file, 'utf-8');
  const { data: frontmatter, content } = parseFrontmatter(rawFile);

  const metaChainKeys = buildMetaChainKeys(collection, slugRaw);
  const deepestMetaKey = metaChainKeys[metaChainKeys.length - 1];
  const deepestMeta = getMetaEntry(metaMap, deepestMetaKey);
  const metaDraftKeys = metaChainKeys.filter((key) => metaMap[key]?.draft === true);

  const title = resolveTitle(frontmatter, content, fileStem, deepestMeta);
  const order = extractOrder(fileStem);
  const accessTier = getAccessTier(frontmatter, collection);
  const contentType = collection === 'saber' ? 'workshop' : 'lesson';
  const route = collection === 'saber'
    ? `/saber/${slugClean}`
    : `/${collection}/${slugClean}`;

  const hasH1 = extractH1(content) !== null;
  const frontmatterDraft = frontmatter.draft === true;
  const published = !frontmatterDraft && metaDraftKeys.length === 0;

  const areaSlug = collection === 'saber'
    ? (slugPartsClean[0] || 'general').toLowerCase()
    : collection;

  const unidadRaw = collection === 'saber' ? slugPartsRaw[1] : slugPartsRaw[0];
  const temaRaw = collection === 'saber' ? slugPartsRaw[2] : slugPartsRaw[1];

  const unidadKey = unidadRaw
    ? `${collection}/${cleanSlugLower(collection === 'saber' ? `${slugPartsRaw[0]}/${unidadRaw}` : unidadRaw)}`
    : null;
  const temaKey = temaRaw && unidadRaw
    ? `${collection}/${cleanSlugLower(
        collection === 'saber'
          ? `${slugPartsRaw[0]}/${unidadRaw}/${temaRaw}`
          : `${unidadRaw}/${temaRaw}`
      )}`
    : null;

  const unidadMeta = unidadKey ? getMetaEntry(metaMap, unidadKey) : null;
  const temaMeta = temaKey ? getMetaEntry(metaMap, temaKey) : null;

  const assetRefs = extractAssetRefs(content);
  const assetTypeCounts = assetRefs.reduce((acc, ref) => {
    const type = classifyAssetRef(ref);
    acc[type] = (acc[type] || 0) + 1;
    return acc;
  }, {});

  return {
    id: `content:${collection}:${slugClean.toLowerCase()}`,
    collection,
    collectionName: MATERIA_NAMES[collection] || formatNameFromSlug(collection),
    contentType,
    accessTier,
    route,
    siteUrl: `${SITE_URL}${route}`,
    slug: {
      raw: slugRaw,
      clean: slugClean,
      segmentsRaw: slugPartsRaw,
      segmentsClean: slugPartsClean,
    },
    area: {
      slug: areaSlug,
      name: MATERIA_NAMES[areaSlug] || formatNameFromSlug(areaSlug),
    },
    unidad: unidadRaw
      ? {
          slugRaw: unidadRaw,
          slug: stripNumericPrefix(unidadRaw),
          name: unidadMeta?.name || formatNameFromSlug(unidadRaw),
          metaKey: unidadKey,
        }
      : null,
    tema: temaRaw
      ? {
          slugRaw: temaRaw,
          slug: stripNumericPrefix(temaRaw),
          name: temaMeta?.name || formatNameFromSlug(temaRaw),
          metaKey: temaKey,
        }
      : null,
    title,
    description:
      (typeof frontmatter.description === 'string' && frontmatter.description.trim())
        ? frontmatter.description.trim()
        : (typeof deepestMeta?.description === 'string' ? deepestMeta.description : null),
    order,
    file: {
      path: file,
      extension,
    },
    flags: {
      published,
      hasH1,
      draftByFrontmatter: frontmatterDraft,
      draftByMeta: metaDraftKeys.length > 0,
      draftMetaKeys: metaDraftKeys,
    },
    assets: {
      total: assetRefs.length,
      byType: assetTypeCounts,
      refs: assetRefs,
    },
  };
}

function buildTotals(entries) {
  const totals = {
    entries: entries.length,
    published: 0,
    draft: 0,
    free: 0,
    premium: 0,
    withAssets: 0,
    assetRefs: 0,
    byCollection: {},
  };

  entries.forEach((entry) => {
    if (entry.flags.published) totals.published += 1;
    else totals.draft += 1;

    if (entry.accessTier === 'premium') totals.premium += 1;
    else totals.free += 1;

    if (entry.assets.total > 0) totals.withAssets += 1;
    totals.assetRefs += entry.assets.total;

    if (!totals.byCollection[entry.collection]) {
      totals.byCollection[entry.collection] = {
        total: 0,
        published: 0,
        draft: 0,
        free: 0,
        premium: 0,
      };
    }

    const bucket = totals.byCollection[entry.collection];
    bucket.total += 1;
    if (entry.flags.published) bucket.published += 1;
    else bucket.draft += 1;
    if (entry.accessTier === 'premium') bucket.premium += 1;
    else bucket.free += 1;
  });

  return totals;
}

function main() {
  const { output, publishedOnly } = parseArgs(process.argv.slice(2));
  const metaMap = loadMetaMap();

  const files = globSync(CONTENT_GLOB, { nodir: true }).sort();
  const allEntries = files
    .map((file) => buildEntry(file, metaMap))
    .filter(Boolean)
    .sort((a, b) => a.route.localeCompare(b.route));

  const entries = publishedOnly ? allEntries.filter((entry) => entry.flags.published) : allEntries;
  const manifest = {
    generatedAt: new Date().toISOString(),
    contractVersion: 1,
    siteUrl: SITE_URL,
    source: {
      contentGlob: CONTENT_GLOB,
      metaGlob: META_GLOB,
      publishedOnly,
    },
    totals: buildTotals(entries),
    entries,
  };

  const outputPath = resolve(output);
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(manifest, null, 2));

  console.log('Content manifest generated');
  console.log(`   Entries:      ${manifest.totals.entries}`);
  console.log(`   Published:    ${manifest.totals.published}`);
  console.log(`   Draft:        ${manifest.totals.draft}`);
  console.log(`   Free:         ${manifest.totals.free}`);
  console.log(`   Premium:      ${manifest.totals.premium}`);
  console.log(`   With assets:  ${manifest.totals.withAssets}`);
  console.log(`   Asset refs:   ${manifest.totals.assetRefs}`);
  console.log(`   Output:       ${output}`);
}

main();

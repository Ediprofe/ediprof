#!/usr/bin/env node

/**
 * Exporta talleres Saber (MD/MDX) a un manifiesto JSON para backend/app.
 *
 * Uso:
 *   node scripts/export-workshops-manifest.mjs
 *   node scripts/export-workshops-manifest.mjs --output /tmp/ediprofe-workshops-manifest.json
 *   node scripts/export-workshops-manifest.mjs --content-manifest /tmp/ediprofe-content-manifest.json
 *   node scripts/export-workshops-manifest.mjs --published-only
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { dirname, relative, resolve } from 'path';
import { globSync } from 'glob';

const DEFAULT_OUTPUT = '/tmp/ediprofe-workshops-manifest.json';
const DEFAULT_CONTENT_MANIFEST = '/tmp/ediprofe-content-manifest.json';
const WORKSHOPS_GLOB = 'src/content/saber/**/taller.{md,mdx}';

function parseArgs(argv) {
  const args = {
    output: DEFAULT_OUTPUT,
    contentManifest: DEFAULT_CONTENT_MANIFEST,
    publishedOnly: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];

    if (token === '--output' && argv[i + 1]) {
      args.output = argv[i + 1];
      i += 1;
    } else if (token === '--content-manifest' && argv[i + 1]) {
      args.contentManifest = argv[i + 1];
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

function parseTagAttributes(raw = '') {
  const attrs = {};
  const regex = /(\w+)="([^"]*)"|(\w+)/g;
  let match = null;

  while ((match = regex.exec(raw)) !== null) {
    if (match[1]) {
      attrs[match[1]] = match[2];
    } else if (match[3]) {
      attrs[match[3]] = true;
    }
  }

  return attrs;
}

function stripHtmlTags(text) {
  return text
    .replace(/\/\*\{[\s\S]*?\}\*\//g, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractAssetRefs(content) {
  const refs = [];

  const mdRefRegex = /!?\[[^\]]*\]\(([^)]+)\)/g;
  const htmlRefRegex = /\b(?:src|href)\s*=\s*["']([^"']+)["']/g;

  let match = null;
  while ((match = mdRefRegex.exec(content)) !== null) {
    const raw = (match[1] || '').trim();
    const ref = raw.split(/\s+"/)[0].replace(/[?#].*$/, '');
    if (isAssetLike(ref)) refs.push(ref);
  }

  while ((match = htmlRefRegex.exec(content)) !== null) {
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

function extractTitle(content) {
  const match = content.match(/^#\s+(.+)$/m);
  if (!match) return null;

  return match[1]
    .replace(/\*\*/g, '')
    .replace(/`/g, '')
    .replace(/[\u{1F300}-\u{1FAFF}]/gu, '')
    .replace(/[\u{2600}-\u{27BF}]/gu, '')
    .trim();
}

function toWorkshopId(slugClean) {
  return `workshop:saber:${slugClean.replace(/\//g, ':')}`;
}

function splitQuestionSections(content) {
  const headingRegex = /^##\s+(\d+)\.?\s*$/gm;
  const matches = [];
  let match = null;

  while ((match = headingRegex.exec(content)) !== null) {
    matches.push({
      number: Number.parseInt(match[1], 10),
      start: match.index,
      end: headingRegex.lastIndex,
    });
  }

  if (matches.length === 0) return [];

  return matches.map((item, index) => {
    const nextStart = matches[index + 1]?.start ?? content.length;
    const body = content.slice(item.end, nextStart).trim();
    return {
      number: item.number,
      raw: body,
    };
  });
}

function parseOptions(optionsBody) {
  const optionRegex = /<Opcion([^>]*)>([\s\S]*?)<\/Opcion>/gi;
  const options = [];
  let match = null;

  while ((match = optionRegex.exec(optionsBody)) !== null) {
    const attrs = parseTagAttributes(match[1] || '');
    const optionId = String(attrs.letra || '').trim().toUpperCase();
    const isCorrect = attrs.correcta === true || attrs.correcta === 'true';
    const optionText = stripHtmlTags(match[2] || '');

    options.push({
      id: optionId || `OPT_${options.length + 1}`,
      text: optionText,
      is_correct: isCorrect,
    });
  }

  return options;
}

function parseQuestion(section) {
  const preguntaMatch = section.raw.match(/<Pregunta([^>]*)>([\s\S]*?)<\/Pregunta>/i);
  if (!preguntaMatch) {
    return null;
  }

  const attrs = parseTagAttributes(preguntaMatch[1] || '');
  const inner = (preguntaMatch[2] || '').trim();

  const optionsMatch = inner.match(/<Opciones>([\s\S]*?)<\/Opciones>/i);
  const detailsMatch = inner.match(/<details>([\s\S]*?)<\/details>/i);

  const optionsBody = optionsMatch ? optionsMatch[1] : '';
  const options = parseOptions(optionsBody);
  const correctOption = options.find((option) => option.is_correct);

  let stemMdx = inner;
  if (optionsMatch) stemMdx = stemMdx.replace(optionsMatch[0], '');
  if (detailsMatch) stemMdx = stemMdx.replace(detailsMatch[0], '');
  stemMdx = stemMdx.trim();

  let feedbackMdx = detailsMatch ? detailsMatch[1].trim() : '';
  feedbackMdx = feedbackMdx.replace(/<summary>[\s\S]*?<\/summary>/i, '').trim();

  const questionId = String(attrs.id || section.number).trim();
  const anioRaw = attrs.anio ? Number.parseInt(String(attrs.anio), 10) : null;

  return {
    id: questionId,
    order: section.number,
    meta: {
      fuente: attrs.fuente ?? null,
      anio: Number.isFinite(anioRaw) ? anioRaw : null,
      bloque: attrs.bloque ?? null,
      competencia: attrs.competencia ?? null,
      componente: attrs.componente ?? null,
      headerless: attrs.headerless === true,
    },
    stem_mdx: stemMdx,
    stem_assets: extractAssetRefs(stemMdx),
    options,
    correct_option_id: correctOption?.id ?? null,
    feedback_mdx: feedbackMdx,
    feedback_assets: extractAssetRefs(feedbackMdx),
  };
}

function loadContentManifestMap(pathLike) {
  const fullPath = resolve(pathLike);
  if (!existsSync(fullPath)) return new Map();

  const raw = JSON.parse(readFileSync(fullPath, 'utf-8'));
  const entries = Array.isArray(raw.entries) ? raw.entries : [];
  const map = new Map();

  entries.forEach((entry) => {
    if (!entry || typeof entry.route !== 'string') return;
    map.set(entry.route, entry);
  });

  return map;
}

function buildWorkshopEntry(filePath, contentEntryMap) {
  const rel = normalizePath(relative('src/content/saber', filePath));
  const parsed = rel.match(/^(.+)\.(md|mdx)$/);
  if (!parsed) return null;

  const rawSlug = parsed[1];
  const slugClean = cleanSlug(rawSlug);
  const route = `/saber/${slugClean}`;

  const rawFile = readFileSync(filePath, 'utf-8');
  const { data: frontmatter, content } = parseFrontmatter(rawFile);

  const sections = splitQuestionSections(content);
  const questions = sections
    .map(parseQuestion)
    .filter(Boolean)
    .sort((a, b) => a.order - b.order);

  if (questions.length === 0) {
    return null;
  }

  const contentEntry = contentEntryMap.get(route);

  const title =
    (typeof frontmatter.title === 'string' && frontmatter.title.trim())
      ? frontmatter.title.trim()
      : (contentEntry?.title || extractTitle(content) || 'Taller Saber');

  const areaSlug = contentEntry?.area?.slug || slugClean.split('/')[0] || 'general';
  const unidadSlug = contentEntry?.unidad?.slug || slugClean.split('/')[1] || null;

  const accessTier = contentEntry?.accessTier || 'premium';
  const isPublished = Boolean(contentEntry?.flags?.published ?? !(frontmatter.draft === true));

  const allAssets = [...new Set(questions.flatMap((q) => [...q.stem_assets, ...q.feedback_assets]))].sort();

  return {
    id: contentEntry?.id || toWorkshopId(slugClean),
    content_external_id: contentEntry?.id || null,
    route,
    title,
    area_slug: areaSlug,
    unidad_slug: unidadSlug,
    access_tier: accessTier,
    published: isPublished,
    stats: {
      total_questions: questions.length,
      total_assets: allAssets.length,
    },
    assets: allAssets,
    questions,
  };
}

function main() {
  const { output, contentManifest, publishedOnly } = parseArgs(process.argv.slice(2));
  const contentEntryMap = loadContentManifestMap(contentManifest);

  const files = globSync(WORKSHOPS_GLOB, { nodir: true }).sort();
  const workshops = files
    .map((filePath) => buildWorkshopEntry(filePath, contentEntryMap))
    .filter(Boolean)
    .filter((entry) => !publishedOnly || entry.published)
    .sort((a, b) => a.route.localeCompare(b.route));

  const totals = {
    workshops: workshops.length,
    published: workshops.filter((w) => w.published).length,
    draft: workshops.filter((w) => !w.published).length,
    questions: workshops.reduce((sum, w) => sum + w.stats.total_questions, 0),
    assets: workshops.reduce((sum, w) => sum + w.stats.total_assets, 0),
  };

  const manifest = {
    generatedAt: new Date().toISOString(),
    contractVersion: 1,
    source: {
      workshopsGlob: WORKSHOPS_GLOB,
      contentManifest: existsSync(resolve(contentManifest)) ? resolve(contentManifest) : null,
      publishedOnly,
    },
    totals,
    workshops,
  };

  const outputPath = resolve(output);
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(manifest, null, 2));

  console.log('Workshops manifest generated');
  console.log(`   Workshops: ${totals.workshops}`);
  console.log(`   Published: ${totals.published}`);
  console.log(`   Draft:     ${totals.draft}`);
  console.log(`   Questions: ${totals.questions}`);
  console.log(`   Output:    ${output}`);
}

main();

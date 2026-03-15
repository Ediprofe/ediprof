#!/usr/bin/env node

/**
 * Exporta talleres y simulacros (MD/MDX) a un manifiesto JSON para backend/app.
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
import {
  cleanInlineMarkdown,
} from '../src/scripts/workshops/inlineShared.js';
import {
  parseMdxCommentDirective,
  stripMdxComments,
} from '../src/scripts/workshops/directivesShared.js';
import {
  EXPLICIT_CONTEXT_REGEX,
  parseSupplementSections,
  parseTagAttributes,
  splitQuestionSections,
} from '../src/scripts/workshops/authoringContractShared.js';
import { renderPracticeFragmentHtml } from '../src/scripts/workshops/htmlShared.js';
import { buildBlocks } from '../src/scripts/workshops/blocksShared.js';

const DEFAULT_OUTPUT = '/tmp/ediprofe-workshops-manifest.json';
const DEFAULT_CONTENT_MANIFEST = '/tmp/ediprofe-content-manifest.json';
const CONTENT_SOURCES = [
  {
    glob: 'src/content/saber/**/taller.{md,mdx}',
    contentRoot: 'src/content/saber',
    routePrefix: '/saber',
    idPrefix: 'content:saber:',
    contentType: 'taller',
  },
  {
    glob: 'src/content/simulacros/**/taller.{md,mdx}',
    contentRoot: 'src/content/simulacros',
    routePrefix: '/simulacros',
    idPrefix: 'content:simulacros:',
    contentType: 'simulacro',
  },
];
const APP_PAYLOAD_VERSION = 1;

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

function stripHtmlTags(text) {
  return text
    .replace(/\/\*\{[\s\S]*?\}\*\//g, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function inferAssetType(ref) {
  if (/\.svg$/i.test(ref)) return 'svg';
  if (/\.(png|jpg|jpeg|webp|gif|avif)$/i.test(ref)) return 'image';
  if (/\.(pdf)$/i.test(ref)) return 'document';
  return 'asset';
}

function buildAssetRefs(refs = []) {
  return [...new Set(refs)]
    .map((src) => String(src || '').trim())
    .filter(Boolean)
    .sort()
    .map((src, index) => ({
      asset_id: `asset:${Buffer.from(src).toString('base64url').slice(0, 24)}:${index + 1}`,
      src,
      alt: null,
      caption: null,
      type: inferAssetType(src),
    }));
}

function isStructuralHtmlLine(line) {
  const normalized = String(line || '').trim();
  return /^<\/?(div|details|summary)\b[^>]*>$/i.test(normalized);
}

async function buildContextPayload(content, filePath) {
  const rawContext = String(content || '').trim();
  const contextMdx = stripMdxComments(rawContext)
    .split('\n')
    .map((line) => line.trimEnd())
    .filter((line) => line.trim() !== '---')
    .join('\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  if (!rawContext) {
    return {
      context_mdx: '',
      context_html: '',
      context_assets: [],
      context_blocks: [],
      context_nodes: [],
    };
  }

  const contextAssets = extractAssetRefs(rawContext);
  const contextNodes = buildBlocks(rawContext, contextAssets);

  return {
    context_mdx: contextMdx,
    context_html: await renderPracticeFragmentHtml(contextMdx, { filePath }),
    context_assets: contextAssets,
    context_blocks: contextNodes,
    context_nodes: contextNodes,
  };
}

function normalizeDetachedContext(rawContext) {
  const lines = String(rawContext || '').replace(/\r\n/g, '\n').split('\n');
  let isInsideComment = false;
  const kept = [];

  lines.forEach((raw) => {
    const line = raw.trim();

    if (isInsideComment) {
      if (line.includes('*/}')) {
        isInsideComment = false;
      }
      return;
    }

    if (line.startsWith('{/*')) {
      const directive = parseMdxCommentDirective(line);
      if (directive?.type === 'layout' && directive.layout === 'full-width') {
        kept.push(line);
      }
      if (!line.includes('*/}')) {
        isInsideComment = true;
      }
      return;
    }

    if (isStructuralHtmlLine(line)) return;
    if (line === '---') return;

    if (line === '') {
      kept.push('');
      return;
    }

    kept.push(raw.trimEnd());
  });

  return kept
    .join('\n')
    .replace(EXPLICIT_CONTEXT_REGEX, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

async function extractExplicitContexts(content, filePath) {
  const contexts = [];
  let match = null;
  let orderBase = 1;

  while ((match = EXPLICIT_CONTEXT_REGEX.exec(content)) !== null) {
    const attrs = parseTagAttributes(match[1] || '');
    const externalId = String(attrs.id || '').trim();
    if (!externalId) {
      throw new Error(
        `ContextoCompartido sin id en ${normalizePath(relative(process.cwd(), filePath))}`
      );
    }

    const rawContext = String(match[2] || '').trim();
    const payload = await buildContextPayload(rawContext, filePath);
    contexts.push({
      external_id: externalId,
      title: typeof attrs.title === 'string' ? attrs.title.trim() || null : null,
      order_base: orderBase,
      ...payload,
      metadata: {
        source: 'explicit',
      },
    });
    orderBase += 1;
  }

  return contexts;
}

function parseSharedContextRanges(contextMdx) {
  const ranges = [];
  const regex = /RESPONDA\s+LAS\s+PREGUNTAS\s+(\d+)\s+(?:A|Y|AL|-)\s+(\d+)/gi;
  let match = null;

  while ((match = regex.exec(contextMdx)) !== null) {
    const start = Number.parseInt(match[1], 10);
    const end = Number.parseInt(match[2], 10);

    if (!Number.isFinite(start) || !Number.isFinite(end)) continue;

    ranges.push({
      start: Math.min(start, end),
      end: Math.max(start, end),
    });
  }

  return ranges;
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

function toContentId(slugClean, source) {
  return `${source.idPrefix}${slugClean}`;
}

async function parseOptions(optionsBody, filePath) {
  const optionRegex = /<Opcion([^>]*)>([\s\S]*?)<\/Opcion>/gi;
  const options = [];
  let match = null;

  while ((match = optionRegex.exec(optionsBody)) !== null) {
    const attrs = parseTagAttributes(match[1] || '');
    const optionId = String(attrs.letra || '').trim().toUpperCase();
    const isCorrect = attrs.correcta === true || attrs.correcta === 'true';
    const rawOptionContent = String(match[2] || '').trim();
    const optionMdx = stripMdxComments(rawOptionContent).trim();
    const optionText = cleanInlineMarkdown(stripHtmlTags(rawOptionContent));
    const optionAssets = extractAssetRefs(rawOptionContent);
    const optionHtml = await renderPracticeFragmentHtml(optionMdx, { filePath });
    const optionNodes = buildBlocks(rawOptionContent, optionAssets);

    options.push({
      id: optionId || `OPT_${options.length + 1}`,
      text: optionText,
      text_html: optionHtml,
      text_assets: optionAssets,
      nodes_mobile: optionNodes,
      is_correct: isCorrect,
    });
  }

  return options;
}

async function parseQuestion(section, filePath) {
  const preguntaRegex = /<Pregunta([^>]*)>([\s\S]*?)<\/Pregunta>/i;
  const preguntaMatch = section.raw.match(preguntaRegex);
  if (!preguntaMatch) {
    return null;
  }

  const attrs = parseTagAttributes(preguntaMatch[1] || '');
  const inner = (preguntaMatch[2] || '').trim();
  const outerMatch = preguntaMatch[0] || '';
  const fullMatchIndex = preguntaMatch.index ?? 0;
  const leadingContext = section.raw.slice(0, fullMatchIndex).trim();
  const trailingContext = section.raw.slice(fullMatchIndex + outerMatch.length).trim();
  const detachedContext = normalizeDetachedContext(
    [leadingContext, trailingContext].filter(Boolean).join('\n\n')
  );

  const optionsMatch = inner.match(/<Opciones>([\s\S]*?)<\/Opciones>/i);
  const supplementSections = parseSupplementSections(inner);
  const answerDetails =
    supplementSections.find((entry) => entry.kind === 'feedback') ??
    supplementSections.find((entry) => entry.kind === 'details') ??
    null;
  const conceptDetails =
    supplementSections.find((entry) => entry.kind === 'concepts') ?? null;

  const optionsBody = optionsMatch ? optionsMatch[1] : '';
  const options = await parseOptions(optionsBody, filePath);
  const correctOption = options.find((option) => option.is_correct);

  let stemMdx = inner;
  if (optionsMatch) stemMdx = stemMdx.replace(optionsMatch[0], '');
  supplementSections.forEach((entry) => {
    stemMdx = stemMdx.replace(entry.raw, '');
  });
  const stemMdxRaw = stemMdx.trim();
  stemMdx = stripMdxComments(stemMdxRaw).trim();

  let feedbackMdx = answerDetails ? answerDetails.content.trim() : '';
  const feedbackMdxRaw = feedbackMdx;
  feedbackMdx = stripMdxComments(feedbackMdxRaw).trim();
  let conceptsMdx = conceptDetails ? conceptDetails.content.trim() : '';
  const conceptsMdxRaw = conceptsMdx;
  conceptsMdx = stripMdxComments(conceptsMdxRaw).trim();

  const stemAssets = extractAssetRefs(stemMdxRaw);
  const feedbackAssets = extractAssetRefs(feedbackMdxRaw);
  const conceptsAssets = extractAssetRefs(conceptsMdxRaw);
  const stemNodes = buildBlocks(stemMdxRaw, stemAssets);
  const feedbackNodes = buildBlocks(feedbackMdxRaw, feedbackAssets);
  const conceptsNodes = buildBlocks(conceptsMdxRaw, conceptsAssets);

  const questionId = String(attrs.id || section.number).trim();
  const anioRaw = attrs.anio ? Number.parseInt(String(attrs.anio), 10) : null;
  const contextRefs = String(attrs.context || attrs.contexto || '')
    .split(',')
    .map((value) => value.trim())
    .filter(Boolean);

  const [stemHtml, feedbackHtml, conceptsHtml] = await Promise.all([
    renderPracticeFragmentHtml(stemMdx, { filePath }),
    renderPracticeFragmentHtml(feedbackMdx, { filePath }),
    renderPracticeFragmentHtml(conceptsMdx, { filePath }),
  ]);

  return {
    id: questionId,
    order: section.number,
    order_base: section.number,
    meta: {
      fuente: attrs.fuente ?? null,
      anio: Number.isFinite(anioRaw) ? anioRaw : null,
      bloque: attrs.bloque ?? null,
      competencia: attrs.competencia ?? null,
      componente: attrs.componente ?? null,
      headerless: attrs.headerless === true,
    },
    stem_mdx: stemMdx,
    stem_html: stemHtml,
    stem_assets: stemAssets,
    stem_blocks: stemNodes,
    stem_nodes: stemNodes,
    options,
    correct_option_id: correctOption?.id ?? null,
    feedback_mdx: feedbackMdx,
    feedback_html: feedbackHtml,
    feedback_summary: answerDetails?.summary?.trim() || 'Respuesta',
    feedback_assets: feedbackAssets,
    feedback_blocks: feedbackNodes,
    feedback_nodes: feedbackNodes,
    concepts_mdx: conceptsMdx,
    concepts_html: conceptsHtml,
    concepts_summary: conceptDetails?.summary?.trim() || 'Conceptos relacionados',
    concepts_assets: conceptsAssets,
    concepts_blocks: conceptsNodes,
    concepts_nodes: conceptsNodes,
    app_payload_version: APP_PAYLOAD_VERSION,
    detached_context_mdx: detachedContext,
    context_refs: contextRefs,
  };
}

function assertUniqueExternalIds(entries, key, entityLabel, route) {
  const seen = new Set();

  entries.forEach((entry) => {
    const value = String(entry?.[key] || '').trim();
    if (!value) return;

    if (seen.has(value)) {
      throw new Error(`ID duplicado de ${entityLabel} "${value}" en ${route}`);
    }

    seen.add(value);
  });
}

function assertQuestionIntegrity(question, route) {
  const options = Array.isArray(question?.options) ? question.options : [];
  const correctCount = options.filter((option) => option?.is_correct === true).length;

  if (options.length < 2) {
    throw new Error(`La pregunta ${question?.id || '?'} en ${route} debe tener al menos 2 opciones`);
  }

  if (correctCount !== 1) {
    throw new Error(
      `La pregunta ${question?.id || '?'} en ${route} debe tener exactamente 1 opción correcta (actual: ${correctCount})`
    );
  }
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

async function buildWorkshopEntry(filePath, contentEntryMap, source) {
  const rel = normalizePath(relative(source.contentRoot, filePath));
  const parsed = rel.match(/^(.+)\.(md|mdx)$/);
  if (!parsed) return null;

  const rawSlug = parsed[1];
  const slugClean = cleanSlug(rawSlug);
  const route = `${source.routePrefix}/${slugClean}`;

  const rawFile = readFileSync(filePath, 'utf-8');
  const { data: frontmatter, content } = parseFrontmatter(rawFile);

  const sections = splitQuestionSections(content);
  const parsedQuestions = (await Promise.all(
    sections.map((section) => parseQuestion(section, filePath))
  )).filter(Boolean);
  const explicitContexts = await extractExplicitContexts(content, filePath);

  assertUniqueExternalIds(parsedQuestions, 'id', 'pregunta', route);
  assertUniqueExternalIds(explicitContexts, 'external_id', 'contexto', route);
  parsedQuestions.forEach((question) => assertQuestionIntegrity(question, route));

  if (parsedQuestions.length === 0) {
    return null;
  }

  const sharedContexts = [];
  const inlineContexts = [];

  for (const question of parsedQuestions) {
    const detached = String(question.detached_context_mdx || '').trim();
    if (!detached) continue;

    const ranges = parseSharedContextRanges(stripMdxComments(detached));
    if (ranges.length > 0) {
      const payload = await buildContextPayload(detached, filePath);
      ranges.forEach((range) => {
        sharedContexts.push({
          external_id: `legacy:${range.start}-${range.end}`,
          title: `Contexto compartido (${range.start}-${range.end})`,
          order_base: range.start,
          metadata: {
            source: 'legacy-range',
            range,
          },
          ...range,
          ...payload,
        });
      });
      continue;
    }

    inlineContexts.push({
      external_id: `inline:${question.id}`,
      title: null,
      order_base: question.order_base ?? question.order ?? 1,
      metadata: {
        source: 'inline-question-context',
        question_id: question.id,
      },
      ...(await buildContextPayload(detached, filePath)),
    });
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

  const contextEntries = [
    ...explicitContexts,
    ...sharedContexts,
    ...inlineContexts,
  ];
  const contextsById = new Map();

  contextEntries.forEach((context) => {
    const externalId = String(context.external_id || '').trim();
    if (!externalId) return;
    if (!contextsById.has(externalId)) {
      contextsById.set(externalId, {
        external_id: externalId,
        title: context.title ?? null,
        order_base: Number(context.order_base ?? 1) || 1,
        context_mdx: context.context_mdx ?? '',
        context_html: context.context_html ?? '',
        context_assets: Array.isArray(context.context_assets) ? context.context_assets : [],
        context_blocks: Array.isArray(context.context_blocks) ? context.context_blocks : [],
        context_nodes: Array.isArray(context.context_nodes) ? context.context_nodes : [],
        metadata: context.metadata ?? {},
      });
    }
  });

  const questions = [];
  const questionContextLinks = [];

  parsedQuestions.forEach((question) => {
    const explicitIds = Array.isArray(question.context_refs) ? question.context_refs : [];
    explicitIds.forEach((contextId) => {
      if (!contextsById.has(contextId)) {
        throw new Error(
          `La pregunta ${question.id} referencia el contexto "${contextId}" que no existe en ${route}`
        );
      }
    });

    const sharedIds = sharedContexts
      .filter((context) => question.order >= context.start && question.order <= context.end)
      .map((context) => context.external_id);
    const inlineId = contextsById.has(`inline:${question.id}`) ? [`inline:${question.id}`] : [];
    const contextIds = [...new Set([...explicitIds, ...sharedIds, ...inlineId])];
    const contextPayloads = contextIds
      .map((contextId) => contextsById.get(contextId))
      .filter(Boolean)
      .sort((a, b) => (a.order_base ?? 1) - (b.order_base ?? 1));

    contextPayloads.forEach((context, index) => {
      questionContextLinks.push({
        question_external_id: question.id,
        context_external_id: context.external_id,
        order_base: index + 1,
      });
    });

    const contextMdx = contextPayloads
      .map((context) => context.context_mdx)
      .filter(Boolean)
      .join('\n\n')
      .trim();
    const contextHtml = contextPayloads
      .map((context) => context.context_html)
      .filter(Boolean)
      .join('\n');
    const contextAssets = [...new Set(contextPayloads.flatMap((context) => context.context_assets || []))];
    const contextBlocks = contextPayloads.flatMap((context) => context.context_blocks || []);
    const contextNodes = contextPayloads.flatMap((context) => context.context_nodes || []);

    questions.push({
      ...question,
      order_base: Number(question.order_base ?? question.order ?? 1) || 1,
      source_slug: `${slugClean}#pregunta-${question.id}`,
      context_ids: contextIds,
      context_mdx: contextMdx,
      context_html: contextHtml,
      context_assets: contextAssets,
      context_blocks: contextBlocks,
      context_nodes: contextNodes,
    });
  });

  questions.forEach((question) => {
    delete question.detached_context_mdx;
    delete question.context_refs;
  });

  const allAssets = [
    ...new Set(
      questions.flatMap((q) => [
        ...(q.context_assets || []),
        ...(q.stem_assets || []),
        ...((Array.isArray(q.options) ? q.options : []).flatMap((option) => option?.text_assets || [])),
        ...(q.feedback_assets || []),
        ...(q.concepts_assets || []),
      ])
    ),
  ].sort();
  const assetRefs = buildAssetRefs(allAssets);
  const contexts = [...contextsById.values()].sort(
    (a, b) => (a.order_base ?? 1) - (b.order_base ?? 1)
  );

  const fallbackId = toContentId(slugClean, source);

  return {
    id: contentEntry?.id || fallbackId,
    content_external_id: contentEntry?.id || fallbackId,
    content_type: source.contentType,
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
    asset_refs: assetRefs,
    contexts,
    question_context_links: questionContextLinks,
    questions,
  };
}

async function main() {
  const { output, contentManifest, publishedOnly } = parseArgs(process.argv.slice(2));
  const contentEntryMap = loadContentManifestMap(contentManifest);

  const files = CONTENT_SOURCES.flatMap((source) =>
    globSync(source.glob, { nodir: true }).sort().map((filePath) => ({ filePath, source }))
  );
  const workshops = (await Promise.all(
    files.map(({ filePath, source }) => buildWorkshopEntry(filePath, contentEntryMap, source))
  ))
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
    appPayloadVersion: APP_PAYLOAD_VERSION,
    source: {
      workshopsGlobs: CONTENT_SOURCES.map((source) => source.glob),
      contentManifest: existsSync(resolve(contentManifest)) ? resolve(contentManifest) : null,
      publishedOnly,
    },
    totals,
    workshops,
  };

  const outputPath = resolve(output);
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(manifest, null, 2));

  console.log('Practice manifest generated');
  console.log(`   Entries:    ${totals.workshops}`);
  console.log(`   Published: ${totals.published}`);
  console.log(`   Draft:     ${totals.draft}`);
  console.log(`   Questions: ${totals.questions}`);
  console.log(`   Output:    ${output}`);
}

void main();

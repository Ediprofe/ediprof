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

function toSubscriptDigits(value) {
  const digits = {
    '0': '₀',
    '1': '₁',
    '2': '₂',
    '3': '₃',
    '4': '₄',
    '5': '₅',
    '6': '₆',
    '7': '₇',
    '8': '₈',
    '9': '₉',
  };

  return String(value || '')
    .split('')
    .map((char) => digits[char] ?? char)
    .join('');
}

function normalizeLatexInlineText(value) {
  return String(value || '')
    .replace(/\\([%$#&{}])/g, '$1')
    .replace(/\\_/g, '_')
    .replace(/\\+text\s*\{([^}]*)\}/g, '$1')
    .replace(/\\+rightarrow/g, '→')
    .replace(/\brightarrow\b/gi, '→')
    .replace(/\bightarrow\b/gi, '→')
    .replace(/\barrow\b/gi, '→')
    .replace(/\\+times/g, '×')
    .replace(/\\+cdot/g, '·')
    .replace(/([A-Za-z0-9\)])_\\?\{([0-9]+)\}/g, (_m, base, digits) => `${base}${toSubscriptDigits(digits)}`)
    .replace(/([A-Za-z0-9\)])_([0-9]+)/g, (_m, base, digits) => `${base}${toSubscriptDigits(digits)}`)
    .replace(/\\(?=\s)/g, '');
}

function cleanInlineMarkdown(value) {
  const markdownCleaned = String(value || '')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\$([^$]+)\$/g, '$1')
    .replace(/\\left|\\right/g, '')
    .replace(/\\,/g, ' ')
    .replace(/\\;/g, ' ')
    .replace(/\\:/g, ' ')
    .replace(/\\!/g, '');

  return normalizeLatexInlineText(markdownCleaned).replace(/\s+/g, ' ').trim();
}

function normalizeMathForDisplay(value) {
  return normalizeLatexInlineText(value)
    .replace(/\rightarrow/gi, '→')
    .replace(/\brightarrow\b/gi, '→')
    .replace(/\bightarrow\b/gi, '→')
    .replace(/\barrow\b/gi, '→')
    .replace(/\\left|\\right/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function parseInlineSegments(value) {
  const source = cleanInlineMarkdown(value);
  const pattern = /(==[\s\S]+?==|~~[\s\S]+?~~|\*\*[\s\S]+?\*\*)/g;

  const segments = [];
  let lastIndex = 0;
  let match = null;

  while ((match = pattern.exec(source)) !== null) {
    const token = match[0] || '';
    const index = match.index ?? 0;

    if (index > lastIndex) {
      const chunk = source.slice(lastIndex, index);
      if (chunk.trim() !== '') {
        segments.push({
          text: chunk,
          variant: 'plain',
        });
      }
    }

    if (token.startsWith('==')) {
      segments.push({
        text: token.slice(2, -2),
        variant: 'highlight',
      });
    } else if (token.startsWith('~~')) {
      segments.push({
        text: token.slice(2, -2),
        variant: 'strike',
      });
    } else if (token.startsWith('**')) {
      segments.push({
        text: token.slice(2, -2),
        variant: 'bold',
      });
    }

    lastIndex = index + token.length;
  }

  if (lastIndex < source.length) {
    const chunk = source.slice(lastIndex);
    if (chunk.trim() !== '') {
      segments.push({
        text: chunk,
        variant: 'plain',
      });
    }
  }

  if (segments.length === 0 && source.trim() !== '') {
    return [{
      text: source,
      variant: 'plain',
    }];
  }

  return segments;
}

function parseTableRow(line) {
  const raw = line.split('|').map((part) => part.trim());
  const body = raw
    .filter((part, idx) => !(idx === 0 && part === ''))
    .filter((part, idx, arr) => !(idx === arr.length - 1 && part === ''));

  return body.map(cleanInlineMarkdown);
}

function isTableSeparatorRow(line) {
  const normalized = line.replace(/\s/g, '');
  return /^\|?:?-+:?\|(:?-+:?\|)+$/.test(normalized);
}

function parseImageLine(line) {
  const match = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
  if (!match) return null;

  const alt = (match[1] || '').trim();
  const url = (match[2] || '').trim();
  if (!url) return null;

  return { alt, url };
}

function isUnorderedListLine(line) {
  return /^[-*]\s+/.test(String(line || '').trim());
}

function isOrderedListLine(line) {
  return /^\d+\.\s+/.test(String(line || '').trim());
}

function parseListItemText(line) {
  return String(line || '')
    .trim()
    .replace(/^[-*]\s+/, '')
    .replace(/^\d+\.\s+/, '')
    .trim();
}

function isStructuralHtmlLine(line) {
  const normalized = String(line || '').trim();
  return /^<\/?div\b[^>]*>$/i.test(normalized);
}

function buildContextPayload(content) {
  const contextMdx = String(content || '').trim();
  if (!contextMdx) {
    return {
      context_mdx: '',
      context_assets: [],
      context_blocks: [],
    };
  }

  const contextAssets = extractAssetRefs(contextMdx);

  return {
    context_mdx: contextMdx,
    context_assets: contextAssets,
    context_blocks: buildBlocks(contextMdx, contextAssets),
  };
}

function normalizeDetachedContext(rawContext) {
  const lines = String(rawContext || '').replace(/\r\n/g, '\n').split('\n');
  const kept = lines.filter((raw) => {
    const line = raw.trim();
    if (!line) return false;
    if (isStructuralHtmlLine(line)) return false;
    if (line === '---') return false;
    return true;
  });

  return kept.join('\n').trim();
}

function parseSharedContextRanges(contextMdx) {
  const ranges = [];
  const regex = /RESPONDA\s+LAS\s+PREGUNTAS\s+(\d+)\s+A\s+(\d+)/gi;
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

function buildBlocks(content, assetRefs = []) {
  const blocks = [];
  const lines = String(content || '').replace(/\r\n/g, '\n').split('\n');
  const renderedImages = new Set();
  let isInsideComment = false;

  let i = 0;
  while (i < lines.length) {
    const rawLine = lines[i] || '';
    const line = rawLine.trim();

    if (isInsideComment) {
      if (line.includes('*/}')) {
        isInsideComment = false;
      }
      i += 1;
      continue;
    }

    if (line === '') {
      i += 1;
      continue;
    }

    if (isStructuralHtmlLine(line)) {
      i += 1;
      continue;
    }

    if (line.includes('{/*')) {
      if (!line.includes('*/}')) {
        isInsideComment = true;
      }
      i += 1;
      continue;
    }

    const image = parseImageLine(line);
    if (image) {
      renderedImages.add(image.url);
      blocks.push({
        type: 'image',
        src: image.url,
        alt: image.alt,
      });
      i += 1;
      continue;
    }

    if (line === '$$') {
      const mathLines = [];
      i += 1;

      while (i < lines.length && (lines[i] || '').trim() !== '$$') {
        const value = (lines[i] || '').trim();
        if (value !== '') {
          mathLines.push(value);
        }
        i += 1;
      }

      blocks.push({
        type: 'equation',
        latex: normalizeMathForDisplay(cleanInlineMarkdown(mathLines.join('\n'))),
      });

      if (i < lines.length && (lines[i] || '').trim() === '$$') {
        i += 1;
      }

      continue;
    }

    if (line.includes('|')) {
      const tableLines = [];

      while (i < lines.length) {
        const candidate = (lines[i] || '').trim();
        if (!candidate.includes('|')) {
          break;
        }
        tableLines.push(candidate);
        i += 1;
      }

      const rows = tableLines
        .filter((row) => !isTableSeparatorRow(row))
        .map(parseTableRow)
        .filter((row) => row.length > 0);

      if (rows.length > 0) {
        blocks.push({
          type: 'table',
          rows,
        });
        continue;
      }
    }

    if (isUnorderedListLine(line) || isOrderedListLine(line)) {
      const ordered = isOrderedListLine(line);
      const items = [];

      while (i < lines.length) {
        const candidate = (lines[i] || '').trim();
        if (candidate === '') {
          break;
        }

        const sameKind = ordered ? isOrderedListLine(candidate) : isUnorderedListLine(candidate);
        if (!sameKind) {
          break;
        }

        const text = cleanInlineMarkdown(parseListItemText(candidate));
        if (text) {
          items.push({
            inlines: parseInlineSegments(text),
          });
        }

        i += 1;
      }

      if (items.length > 0) {
        blocks.push({
          type: 'list',
          ordered,
          items,
        });
        continue;
      }
    }

    const paragraphLines = [];
    while (i < lines.length) {
      const candidate = (lines[i] || '').trim();
      if (candidate === '' || candidate === '$$' || candidate.includes('|')) {
        break;
      }
      if (parseImageLine(candidate)) {
        break;
      }
      if (isStructuralHtmlLine(candidate)) {
        i += 1;
        continue;
      }
      if (isUnorderedListLine(candidate) || isOrderedListLine(candidate)) {
        break;
      }
      if (candidate.includes('{/*')) {
        break;
      }
      paragraphLines.push(candidate);
      i += 1;
    }

    const text = cleanInlineMarkdown(paragraphLines.join(' '));
    if (text) {
      blocks.push({
        type: 'paragraph',
        inlines: parseInlineSegments(text),
      });
    }
  }

  assetRefs.forEach((asset) => {
    if (!asset || renderedImages.has(asset)) return;
    renderedImages.add(asset);
    blocks.push({
      type: 'image',
      src: asset,
      alt: 'Imagen de apoyo',
    });
  });

  return blocks;
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
  return `content:saber:${slugClean}`;
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

  const stemAssets = extractAssetRefs(stemMdx);
  const feedbackAssets = extractAssetRefs(feedbackMdx);

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
    stem_assets: stemAssets,
    stem_blocks: buildBlocks(stemMdx, stemAssets),
    options,
    correct_option_id: correctOption?.id ?? null,
    feedback_mdx: feedbackMdx,
    feedback_assets: feedbackAssets,
    feedback_blocks: buildBlocks(feedbackMdx, feedbackAssets),
    app_payload_version: APP_PAYLOAD_VERSION,
    detached_context_mdx: detachedContext,
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
  const parsedQuestions = sections
    .map(parseQuestion)
    .filter(Boolean)
    .sort((a, b) => a.order - b.order);

  if (parsedQuestions.length === 0) {
    return null;
  }

  const sharedContexts = [];

  for (const question of parsedQuestions) {
    const detached = String(question.detached_context_mdx || '').trim();
    if (!detached) continue;

    const ranges = parseSharedContextRanges(detached);
    if (ranges.length > 0) {
      const payload = buildContextPayload(detached);
      ranges.forEach((range) => {
        sharedContexts.push({
          ...range,
          ...payload,
        });
      });
      continue;
    }

    Object.assign(question, buildContextPayload(detached));
  }

  const questions = parsedQuestions.map((question) => {
    const contextualMatches = sharedContexts.filter(
      (context) => question.order >= context.start && question.order <= context.end
    );

    if (contextualMatches.length === 0) {
      // internal field used during parsing only
      delete question.detached_context_mdx;
      return question;
    }

    const contextMdx = contextualMatches
      .map((context) => context.context_mdx)
      .filter(Boolean)
      .join('\n\n')
      .trim();

    const contextAssets = [...new Set(contextualMatches.flatMap((context) => context.context_assets || []))];
    const contextBlocks = contextualMatches.flatMap((context) => context.context_blocks || []);

    question.context_mdx = contextMdx;
    question.context_assets = contextAssets;
    question.context_blocks = contextBlocks;

    delete question.detached_context_mdx;
    return question;
  });

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

  const fallbackId = toWorkshopId(slugClean);

  return {
    id: contentEntry?.id || fallbackId,
    content_external_id: contentEntry?.id || fallbackId,
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
    appPayloadVersion: APP_PAYLOAD_VERSION,
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

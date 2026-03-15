import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkMdx from 'remark-mdx';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import { toString } from 'mdast-util-to-string';

import {
  cleanInlineMarkdown,
  normalizeMathForDisplay,
  parseInlineSegments,
} from './inlineShared.js';
import { parseMdxCommentDirective } from './directivesShared.js';

function normalizeSource(value = '') {
  return String(value || '').replace(/\r\n/g, '\n').trim();
}

function sliceNodeSource(source, node) {
  const start = node?.position?.start?.offset;
  const end = node?.position?.end?.offset;

  if (!Number.isInteger(start) || !Number.isInteger(end)) {
    return '';
  }

  return String(source || '').slice(start, end);
}

function withLayout(block, layout) {
  if (!block || !layout) return block;

  return {
    ...block,
    layout,
  };
}

function mergeSegments(segments = []) {
  const merged = [];

  segments.forEach((segment) => {
    if (!segment || !String(segment.text || '').trim()) return;

    const previous = merged[merged.length - 1];
    if (previous && previous.variant === segment.variant) {
      previous.text = `${previous.text}${segment.text}`;
      return;
    }

    merged.push({
      text: String(segment.text || ''),
      variant: segment.variant || 'plain',
    });
  });

  return merged;
}

function applyVariant(segments = [], variant = null) {
  if (!variant) return segments;

  return segments.map((segment) => ({
    ...segment,
    variant,
  }));
}

function buildInlineSegments(nodes = [], forcedVariant = null) {
  const segments = [];

  nodes.forEach((node) => {
    if (!node || typeof node !== 'object') return;

    if (node.type === 'text') {
      segments.push(...applyVariant(parseInlineSegments(node.value || ''), forcedVariant));
      return;
    }

    if (node.type === 'inlineMath') {
      segments.push({
        text: normalizeMathForDisplay(String(node.value || '')),
        variant: forcedVariant || 'plain',
      });
      return;
    }

    if (node.type === 'strong') {
      segments.push(...buildInlineSegments(node.children || [], forcedVariant || 'bold'));
      return;
    }

    if (node.type === 'emphasis') {
      segments.push(...buildInlineSegments(node.children || [], forcedVariant || 'italic'));
      return;
    }

    if (node.type === 'delete') {
      segments.push(...buildInlineSegments(node.children || [], forcedVariant || 'strike'));
      return;
    }

    if (node.type === 'link') {
      segments.push(...buildInlineSegments(node.children || [], forcedVariant));
      return;
    }

    if (node.type === 'break') {
      segments.push({
        text: ' ',
        variant: forcedVariant || 'plain',
      });
      return;
    }

    if (node.type === 'image') {
      segments.push({
        text: String(node.alt || 'imagen'),
        variant: forcedVariant || 'plain',
      });
      return;
    }

    const fallback = cleanInlineMarkdown(toString(node) || '');
    if (fallback) {
      segments.push(...applyVariant(parseInlineSegments(fallback), forcedVariant));
    }
  });

  return mergeSegments(segments);
}

function extractTableRows(node) {
  const rows = Array.isArray(node?.children) ? node.children : [];

  return rows
    .map((row) => {
      const cells = Array.isArray(row?.children) ? row.children : [];

      return cells
        .map((cell) => cleanInlineMarkdown(toString(cell) || ''))
        .filter((value) => value !== '');
    })
    .filter((row) => row.length > 0);
}

function extractListItems(node) {
  const items = Array.isArray(node?.children) ? node.children : [];

  return items
    .map((item) => {
      const paragraph = Array.isArray(item?.children)
        ? item.children.find((child) => child?.type === 'paragraph')
        : null;

      if (paragraph && Array.isArray(paragraph.children)) {
        return { inlines: buildInlineSegments(paragraph.children) };
      }

      const text = cleanInlineMarkdown(toString(item) || '');
      if (!text) return null;

      return { inlines: parseInlineSegments(text) };
    })
    .filter(Boolean);
}

function paragraphContainsOnlyImages(node) {
  const children = Array.isArray(node?.children) ? node.children : [];
  return children.length > 0 && children.every((child) => child?.type === 'image');
}

function paragraphContainsRawJsx(node) {
  const children = Array.isArray(node?.children) ? node.children : [];

  return children.some((child) =>
    ['mdxJsxTextElement', 'mdxJsxFlowElement', 'html'].includes(String(child?.type || ''))
  );
}

function layoutForRawHtml(raw, activeLayout) {
  if (/\b(span-all|full-width)\b/i.test(String(raw || ''))) {
    return 'full-width';
  }

  return activeLayout;
}

function buildBlocksFromAstTree(tree, source, assetRefs = []) {
  const blocks = [];
  const renderedImages = new Set();
  let activeLayout = null;

  const pushBlock = (block, layout = activeLayout) => {
    if (!block) return;

    const normalized = withLayout(block, layout);
    blocks.push(normalized);

    if (normalized.type === 'image' && normalized.src) {
      renderedImages.add(String(normalized.src));
    }
  };

  const children = Array.isArray(tree?.children) ? tree.children : [];

  children.forEach((node) => {
    if (!node || typeof node !== 'object') return;

    if (node.type === 'thematicBreak') {
      activeLayout = null;
      return;
    }

    if (node.type === 'mdxFlowExpression') {
      const raw = sliceNodeSource(source, node);
      const directive = parseMdxCommentDirective(raw);
      if (directive?.type === 'layout' && directive.layout === 'full-width') {
        activeLayout = 'full-width';
      }
      return;
    }

    if (node.type === 'heading') {
      const inlines = buildInlineSegments(node.children || []);
      if (inlines.length > 0) {
        pushBlock({
          type: 'heading',
          depth: Number(node.depth || 3),
          inlines,
        });
      }
      return;
    }

    if (node.type === 'math') {
      pushBlock({
        type: 'equation',
        latex: normalizeMathForDisplay(String(node.value || '')),
      });
      return;
    }

    if (node.type === 'table') {
      const rows = extractTableRows(node);
      if (rows.length > 0) {
        pushBlock({
          type: 'table',
          rows,
        });
      }
      return;
    }

    if (node.type === 'list') {
      const items = extractListItems(node);
      if (items.length > 0) {
        pushBlock({
          type: 'list',
          ordered: Boolean(node.ordered),
          items,
        });
      }
      return;
    }

    if (node.type === 'html' || node.type === 'mdxJsxFlowElement') {
      const raw = sliceNodeSource(source, node).trim();
      if (raw) {
        pushBlock(
          {
            type: 'html',
            html: raw,
          },
          layoutForRawHtml(raw, activeLayout),
        );
      }
      return;
    }

    if (node.type === 'paragraph') {
      const paragraphChildren = Array.isArray(node.children) ? node.children : [];

      if (
        paragraphChildren.length === 1 &&
        paragraphChildren[0]?.type === 'inlineMath'
      ) {
        pushBlock({
          type: 'equation',
          latex: normalizeMathForDisplay(String(paragraphChildren[0]?.value || '')),
        });
        return;
      }

      if (paragraphContainsOnlyImages(node)) {
        (node.children || []).forEach((child) => {
          if (child?.type !== 'image' || !child.url) return;

          pushBlock({
            type: 'image',
            src: String(child.url),
            alt: String(child.alt || ''),
          });
        });
        return;
      }

      if (paragraphContainsRawJsx(node)) {
        const raw = sliceNodeSource(source, node).trim();
        if (raw) {
          pushBlock(
            {
              type: 'html',
              html: raw,
            },
            layoutForRawHtml(raw, activeLayout),
          );
        }
        return;
      }

      const inlines = buildInlineSegments(node.children || []);
      if (inlines.length > 0) {
        pushBlock({
          type: 'paragraph',
          inlines,
        });
      }
      return;
    }

    const raw = sliceNodeSource(source, node).trim();
    if (raw) {
      pushBlock(
        {
          type: 'html',
          html: raw,
        },
        layoutForRawHtml(raw, activeLayout),
      );
      return;
    }

    const fallback = cleanInlineMarkdown(toString(node) || '');
    if (fallback) {
      pushBlock({
        type: 'paragraph',
        inlines: parseInlineSegments(fallback),
      });
    }
  });

  assetRefs.forEach((asset) => {
    const normalized = String(asset || '').trim();
    if (!normalized || renderedImages.has(normalized)) return;

    pushBlock({
      type: 'image',
      src: normalized,
      alt: 'Imagen de apoyo',
    }, null);
  });

  return blocks;
}

function buildBlocks(content, assetRefs = []) {
  const source = normalizeSource(content);

  if (!source) {
    return Array.isArray(assetRefs)
      ? assetRefs
          .map((asset) => String(asset || '').trim())
          .filter(Boolean)
          .map((asset) => ({
            type: 'image',
            src: asset,
            alt: 'Imagen de apoyo',
          }))
      : [];
  }

  const tree = unified()
    .use(remarkParse)
    .use(remarkMdx)
    .use(remarkGfm)
    .use(remarkMath, { singleDollarTextMath: true })
    .parse(source);

  return buildBlocksFromAstTree(tree, source, assetRefs);
}

export {
  buildBlocks,
};

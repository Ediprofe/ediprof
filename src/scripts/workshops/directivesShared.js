/**
 * Shared helpers for workshop authoring directives embedded in MDX comments.
 *
 * Current supported directives:
 * - `imprimible: ancho-completo` => mark following blocks as full-width until separator (`---`).
 */

const FULL_WIDTH_TOKENS = [
  'imprimible: ancho-completo',
  'imprimible: ancho completo',
  'print: full-width',
  'print:full-width',
  'full-width',
];

function normalizeDirectiveText(value) {
  return String(value || '')
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .trim();
}

function parseCommentBody(line) {
  const raw = String(line || '').trim();

  const mdxMatch = raw.match(/^\{\/\*\s*([\s\S]*?)\s*\*\/\}$/);
  if (mdxMatch?.[1]) {
    return mdxMatch[1].trim();
  }

  const htmlMatch = raw.match(/^<!--\s*([\s\S]*?)\s*-->$/);
  if (htmlMatch?.[1]) {
    return htmlMatch[1].trim();
  }

  return null;
}

function parseMdxCommentDirective(line) {
  const body = parseCommentBody(line);
  if (!body) return null;

  const normalized = normalizeDirectiveText(body);
  const isFullWidth = FULL_WIDTH_TOKENS.some((token) => normalized.includes(token));

  if (isFullWidth) {
    return {
      type: 'layout',
      layout: 'full-width',
      scope: 'until-separator',
      raw: body,
    };
  }

  return {
    type: 'comment',
    raw: body,
  };
}

function stripMdxComments(content) {
  return String(content || '')
    .replace(/\{\/\*[\s\S]*?\*\/\}/g, '')
    .replace(/<!--[\s\S]*?-->/g, '');
}

export {
  parseMdxCommentDirective,
  stripMdxComments,
};

/**
 * Shared inline normalization helpers for workshops.
 *
 * Single source of truth used by:
 * - Manifest export pipeline (Node scripts)
 * - Members web renderer (browser)
 */

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

function cleanInlineForRender(value) {
  return normalizeLatexInlineText(value);
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
    return [{ text: source, variant: 'plain' }];
  }

  return segments;
}

function parseTableRow(line) {
  const raw = String(line || '').split('|').map((part) => part.trim());
  const body = raw
    .filter((part, idx) => !(idx === 0 && part === ''))
    .filter((part, idx, arr) => !(idx === arr.length - 1 && part === ''));

  return body.map(cleanInlineMarkdown);
}

function isTableSeparatorRow(line) {
  const normalized = String(line || '').replace(/\s/g, '');
  return /^\|?:?-+:?\|(:?-+:?\|)+$/.test(normalized);
}

export {
  cleanInlineForRender,
  cleanInlineMarkdown,
  isTableSeparatorRow,
  normalizeLatexInlineText,
  normalizeMathForDisplay,
  parseInlineSegments,
  parseTableRow,
  toSubscriptDigits,
};

export type InlineVariant = 'plain' | 'highlight' | 'strike' | 'bold';

export type InlineSegment = {
  text: string;
  variant: InlineVariant;
};

function toSubscriptDigits(value: string): string {
  const digits: Record<string, string> = {
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

  return value
    .split('')
    .map((char) => digits[char] ?? char)
    .join('');
}

export function normalizeLatexInlineText(value: string): string {
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
    .replace(/([A-Za-z0-9\)])_\\?\{([0-9]+)\}/g, (_m, base: string, digits: string) => {
      return `${base}${toSubscriptDigits(digits)}`;
    })
    .replace(/([A-Za-z0-9\)])_([0-9]+)/g, (_m, base: string, digits: string) => {
      return `${base}${toSubscriptDigits(digits)}`;
    })
    .replace(/\\(?=\s)/g, '');
}

export function cleanInlineMarkdown(value: string): string {
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

export function cleanInlineForRender(value: string): string {
  return normalizeLatexInlineText(value);
}

export function normalizeMathForDisplay(value: string): string {
  return normalizeLatexInlineText(value)
    .replace(/\rightarrow/gi, '→')
    .replace(/\brightarrow\b/gi, '→')
    .replace(/\bightarrow\b/gi, '→')
    .replace(/\barrow\b/gi, '→')
    .replace(/\\left|\\right/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

export function parseInlineSegments(value: string): InlineSegment[] {
  const source = cleanInlineMarkdown(value);
  const pattern = /(==[\s\S]+?==|~~[\s\S]+?~~|\*\*[\s\S]+?\*\*)/g;

  const segments: InlineSegment[] = [];
  let lastIndex = 0;

  for (const match of source.matchAll(pattern)) {
    const token = match[0] ?? '';
    const index = match.index ?? 0;

    if (index > lastIndex) {
      segments.push({
        text: source.slice(lastIndex, index),
        variant: 'plain',
      });
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
    segments.push({
      text: source.slice(lastIndex),
      variant: 'plain',
    });
  }

  if (segments.length === 0) {
    return [{ text: source, variant: 'plain' }];
  }

  return segments;
}

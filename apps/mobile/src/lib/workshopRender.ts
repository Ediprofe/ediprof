export type InlineVariant = 'plain' | 'highlight' | 'strike' | 'bold';

export type InlineSegment = {
  text: string;
  variant: InlineVariant;
};

export type StemBlock =
  | { type: 'paragraph'; text?: string; inlines?: InlineSegment[] }
  | { type: 'math'; text: string }
  | { type: 'equation'; latex: string }
  | { type: 'table'; rows: string[][] }
  | { type: 'image'; alt?: string; url?: string; src?: string };

export function toSubscriptDigits(value: string): string {
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
  return value
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
  const markdownCleaned = value
    .replace(/__(.*?)__/g, '$1')
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
    // Defensive cleanup when an escaped LaTeX command is decoded incorrectly
    // (e.g. "\rightarrow" ending up as carriage-return + "ightarrow").
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

export function parseTableRow(line: string): string[] {
  const raw = line.split('|').map((part) => part.trim());
  const body = raw.filter((part, idx) => !(idx === 0 && part === '')).filter((part, idx, arr) => {
    if (idx === arr.length - 1 && part === '') {
      return false;
    }

    return true;
  });

  return body.map(cleanInlineMarkdown);
}

export function isTableSeparatorRow(line: string): boolean {
  const normalized = line.replace(/\s/g, '');
  return /^\|?:?-+:?\|(:?-+:?\|)+$/.test(normalized);
}

export function toBlocks(stem: string, stemAssets: string[] = []): StemBlock[] {
  const blocks: StemBlock[] = [];
  const lines = stem.replace(/\r\n/g, '\n').split('\n');
  const renderedImages = new Set<string>();

  let i = 0;
  let isInsideComment = false;

  while (i < lines.length) {
    const rawLine = lines[i] ?? '';
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

    if (line.includes('{/*')) {
      if (!line.includes('*/}')) {
        isInsideComment = true;
      }
      i += 1;
      continue;
    }

    const imageMatch = line.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
    if (imageMatch) {
      const alt = imageMatch[1]?.trim() ?? '';
      const url = imageMatch[2]?.trim() ?? '';
      if (url) {
        renderedImages.add(url);
        blocks.push({ type: 'image', alt, url });
      }
      i += 1;
      continue;
    }

    if (line === '$$') {
      const mathLines: string[] = [];
      i += 1;
      while (i < lines.length && (lines[i]?.trim() ?? '') !== '$$') {
        const value = lines[i]?.trim() ?? '';
        if (value) {
          mathLines.push(value);
        }
        i += 1;
      }

      blocks.push({
        type: 'math',
        text: normalizeMathForDisplay(cleanInlineMarkdown(mathLines.join('\n'))),
      });

      if (i < lines.length && (lines[i]?.trim() ?? '') === '$$') {
        i += 1;
      }

      continue;
    }

    if (line.includes('|')) {
      const tableLines: string[] = [];
      while (i < lines.length) {
        const candidate = lines[i]?.trim() ?? '';
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
        blocks.push({ type: 'table', rows });
        continue;
      }
    }

    const paragraphLines: string[] = [];
    while (i < lines.length) {
      const candidate = lines[i]?.trim() ?? '';
      if (candidate === '' || candidate === '$$' || candidate.includes('|')) {
        break;
      }
      if (candidate.match(/^!\[([^\]]*)\]\(([^)]+)\)$/)) {
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
      blocks.push({ type: 'paragraph', text });
    }
  }

  stemAssets.forEach((asset) => {
    if (!asset || renderedImages.has(asset)) {
      return;
    }

    renderedImages.add(asset);
    blocks.push({ type: 'image', alt: 'Imagen de apoyo', url: asset });
  });

  return blocks;
}

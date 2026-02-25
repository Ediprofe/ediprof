import { memo, useMemo } from 'react';
import { Image } from 'expo-image';
import { StyleSheet, Text, View } from 'react-native';
import type { WorkshopRichBlock } from '../types/api';

type InlineVariant = 'plain' | 'highlight' | 'strike' | 'bold';

type InlineSegment = {
  text: string;
  variant: InlineVariant;
};

type StemBlock =
  | { type: 'paragraph'; text?: string; inlines?: InlineSegment[] }
  | { type: 'math'; text: string }
  | { type: 'equation'; latex: string }
  | { type: 'table'; rows: string[][] }
  | { type: 'image'; alt?: string; url?: string; src?: string };

type Props = {
  stem: string;
  stemAssets?: string[];
  blocks?: WorkshopRichBlock[] | null;
};

function normalizeLatexInlineText(value: string): string {
  return value
    .replace(/\\([%$#&{}])/g, '$1')
    .replace(/\\_/g, '_')
    .replace(/\\text\s*\{([^}]*)\}/g, '$1')
    .replace(/\\rightarrow/g, '→')
    .replace(/\\times/g, '×')
    .replace(/\\cdot/g, '·')
    .replace(/([A-Za-z0-9\)])_\\?\{([0-9]+)\}/g, (_m, base: string, digits: string) => {
      return `${base}${toSubscriptDigits(digits)}`;
    })
    .replace(/([A-Za-z0-9\)])_([0-9]+)/g, (_m, base: string, digits: string) => {
      return `${base}${toSubscriptDigits(digits)}`;
    });
}

function cleanInlineMarkdown(value: string): string {
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

  return normalizeLatexInlineText(markdownCleaned).trim();
}

function cleanInlineForRender(value: string): string {
  return normalizeLatexInlineText(value);
}

function normalizeMathForDisplay(value: string): string {
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

function parseInlineSegments(value: string): InlineSegment[] {
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

function parseTableRow(line: string): string[] {
  const raw = line.split('|').map((part) => part.trim());
  const body = raw.filter((part, idx) => !(idx === 0 && part === '')).filter((part, idx, arr) => {
    if (idx === arr.length - 1 && part === '') {
      return false;
    }

    return true;
  });

  return body.map(cleanInlineMarkdown);
}

function isTableSeparatorRow(line: string): boolean {
  const normalized = line.replace(/\s/g, '');
  return /^\|?:?-+:?\|(:?-+:?\|)+$/.test(normalized);
}

function toBlocks(stem: string, stemAssets: string[] = []): StemBlock[] {
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

function QuestionStemImpl({ stem, stemAssets = [], blocks = null }: Props) {
  const blocksNormalized = useMemo<StemBlock[]>(() => {
    if (Array.isArray(blocks) && blocks.length > 0) {
      const mapped: StemBlock[] = blocks
        .map((block): StemBlock | null => {
          if (!block || typeof block !== 'object' || !('type' in block)) {
            return null;
          }

          if (block.type === 'paragraph') {
            return {
              type: 'paragraph',
              inlines: Array.isArray(block.inlines)
                ? block.inlines.filter((segment) => typeof segment?.text === 'string')
                : [],
            };
          }

          if (block.type === 'equation') {
            return {
              type: 'equation',
              latex: block.latex ?? '',
            };
          }

          if (block.type === 'table') {
            return {
              type: 'table',
              rows: Array.isArray(block.rows) ? block.rows : [],
            };
          }

          if (block.type === 'image') {
            return {
              type: 'image',
              src: block.src,
              alt: block.alt,
            };
          }

          return null;
        })
        .filter((block): block is StemBlock => block !== null);

      if (mapped.length > 0) {
        return mapped;
      }
    }

    return toBlocks(stem, stemAssets);
  }, [blocks, stem, stemAssets]);

  const renderInlineSegments = (
    segments: InlineSegment[],
    baseStyle: (typeof styles)['paragraph'] | (typeof styles)['cell'],
    keyPrefix: string,
  ) => {
    return segments.map((segment, idx) => {
      const segmentStyle =
        segment.variant === 'highlight'
          ? styles.inlineHighlight
          : segment.variant === 'strike'
            ? styles.inlineStrike
            : segment.variant === 'bold'
              ? styles.inlineBold
              : null;

      return (
        <Text key={`${keyPrefix}-${idx}`} style={[baseStyle, segmentStyle]}>
          {cleanInlineForRender(segment.text)}
        </Text>
      );
    });
  };

  return (
    <View style={styles.root}>
      {blocksNormalized.map((block, index) => {
        const key = `${block.type}-${index}`;

        if (block.type === 'paragraph') {
          const segments = block.inlines ?? parseInlineSegments(block.text ?? '');

          return (
            <Text key={key} style={styles.paragraph}>
              {renderInlineSegments(segments, styles.paragraph, key)}
            </Text>
          );
        }

        if (block.type === 'math' || block.type === 'equation') {
          const mathText =
            block.type === 'equation'
              ? normalizeMathForDisplay(cleanInlineMarkdown(block.latex))
              : block.text;

          return (
            <View key={key} style={styles.mathBox}>
              <Text style={styles.mathText}>{mathText}</Text>
            </View>
          );
        }

        if (block.type === 'image') {
          const src = block.url ?? block.src ?? '';
          if (!src) {
            return null;
          }

          return (
            <Image
              key={key}
              source={src}
              accessibilityLabel={block.alt}
              style={styles.image}
              contentFit="contain"
              transition={120}
            />
          );
        }

        const header = block.rows[0] ?? [];
        const body = block.rows.slice(1);

        return (
          <View key={key} style={styles.table}>
            <View style={styles.tableRow}>
              {header.map((cell, idx) => (
                <Text key={`h-${idx}`} style={[styles.cell, styles.headerCell]}>
                  {renderInlineSegments(parseInlineSegments(cell), styles.cell, `${key}-h-${idx}`)}
                </Text>
              ))}
            </View>
            {body.map((row, rowIndex) => (
              <View key={`r-${rowIndex}`} style={styles.tableRow}>
                {row.map((cell, idx) => (
                  <Text key={`c-${rowIndex}-${idx}`} style={styles.cell}>
                    {renderInlineSegments(parseInlineSegments(cell), styles.cell, `${key}-c-${rowIndex}-${idx}`)}
                  </Text>
                ))}
              </View>
            ))}
          </View>
        );
      })}
    </View>
  );
}

export const QuestionStem = memo(QuestionStemImpl);

const styles = StyleSheet.create({
  root: {
    gap: 10,
  },
  paragraph: {
    color: '#d4ddf7',
    fontSize: 12,
    lineHeight: 19,
  },
  mathBox: {
    borderWidth: 1,
    borderColor: '#304a80',
    borderRadius: 8,
    backgroundColor: '#081127',
    paddingHorizontal: 10,
    paddingVertical: 8,
  },
  mathText: {
    color: '#d8e6ff',
    fontSize: 14,
    lineHeight: 18,
    fontFamily: 'Courier',
    letterSpacing: 0.2,
  },
  table: {
    borderWidth: 1,
    borderColor: '#314a7e',
    borderRadius: 8,
    overflow: 'hidden',
    backgroundColor: '#0b142b',
  },
  tableRow: {
    flexDirection: 'row',
    borderTopWidth: 1,
    borderTopColor: '#23345d',
  },
  cell: {
    flex: 1,
    color: '#d7e1ff',
    fontSize: 11,
    lineHeight: 16,
    paddingHorizontal: 8,
    paddingVertical: 7,
    borderLeftWidth: 1,
    borderLeftColor: '#23345d',
  },
  headerCell: {
    color: '#f1f5ff',
    fontWeight: '700',
    backgroundColor: '#132244',
  },
  image: {
    width: '100%',
    height: 220,
    borderRadius: 8,
    backgroundColor: '#f4f7ff',
    borderWidth: 1,
    borderColor: '#2a3f6d',
  },
  inlineHighlight: {
    backgroundColor: 'rgba(255, 223, 128, 0.28)',
    color: '#fff2c4',
    fontWeight: '700',
  },
  inlineStrike: {
    textDecorationLine: 'line-through',
    textDecorationColor: '#c79aa1',
    color: '#b6a6bb',
  },
  inlineBold: {
    fontWeight: '800',
    color: '#f4f7ff',
  },
});

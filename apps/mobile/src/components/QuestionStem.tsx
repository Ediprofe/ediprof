import { memo, useMemo } from 'react';
import { Image } from 'expo-image';
import { StyleSheet, Text, View } from 'react-native';

type InlineVariant = 'plain' | 'highlight' | 'strike' | 'bold';

type InlineSegment = {
  text: string;
  variant: InlineVariant;
};

type StemBlock =
  | { type: 'paragraph'; text: string }
  | { type: 'math'; text: string }
  | { type: 'table'; rows: string[][] }
  | { type: 'image'; alt: string; url: string };

type Props = {
  stem: string;
  stemAssets?: string[];
};

function cleanInlineMarkdown(value: string): string {
  return value
    .replace(/__(.*?)__/g, '$1')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\\rightarrow/g, '→')
    .replace(/\\times/g, '×')
    .replace(/\\cdot/g, '·')
    .replace(/\$([^$]+)\$/g, '$1')
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

function normalizeMathForDisplay(value: string): string {
  return value
    .replace(/\\rightarrow/g, '→')
    .replace(/\\times/g, '×')
    .replace(/\\cdot/g, '·')
    .replace(/_\\?\{([0-9]+)\}/g, (_, digits: string) => toSubscriptDigits(digits))
    .replace(/_([0-9]+)/g, (_, digits: string) => toSubscriptDigits(digits))
    .replace(/\s+/g, ' ')
    .trim();
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

function QuestionStemImpl({ stem, stemAssets = [] }: Props) {
  const blocks = useMemo(() => toBlocks(stem, stemAssets), [stem, stemAssets]);

  const renderInlineText = (
    text: string,
    baseStyle: (typeof styles)['paragraph'] | (typeof styles)['cell'],
    keyPrefix: string,
  ) => {
    const segments = parseInlineSegments(text);

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
          {segment.text}
        </Text>
      );
    });
  };

  return (
    <View style={styles.root}>
      {blocks.map((block, index) => {
        const key = `${block.type}-${index}`;

        if (block.type === 'paragraph') {
          return (
            <Text key={key} style={styles.paragraph}>
              {renderInlineText(block.text, styles.paragraph, key)}
            </Text>
          );
        }

        if (block.type === 'math') {
          return (
            <View key={key} style={styles.mathBox}>
              <Text style={styles.mathText}>{block.text}</Text>
            </View>
          );
        }

        if (block.type === 'image') {
          return (
            <Image
              key={key}
              source={block.url}
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
                  {renderInlineText(cell, styles.cell, `${key}-h-${idx}`)}
                </Text>
              ))}
            </View>
            {body.map((row, rowIndex) => (
              <View key={`r-${rowIndex}`} style={styles.tableRow}>
                {row.map((cell, idx) => (
                  <Text key={`c-${rowIndex}-${idx}`} style={styles.cell}>
                    {renderInlineText(cell, styles.cell, `${key}-c-${rowIndex}-${idx}`)}
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

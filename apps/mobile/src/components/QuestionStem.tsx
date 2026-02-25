import { memo, useMemo } from 'react';
import { StyleSheet, Text, View } from 'react-native';

type StemBlock =
  | { type: 'paragraph'; text: string }
  | { type: 'math'; text: string }
  | { type: 'table'; rows: string[][] };

type Props = {
  stem: string;
};

function cleanInlineMarkdown(value: string): string {
  return value
    .replace(/\*\*(.*?)\*\*/g, '$1')
    .replace(/__(.*?)__/g, '$1')
    .replace(/\*(.*?)\*/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\\rightarrow/g, '→')
    .replace(/\\times/g, '×')
    .replace(/\\cdot/g, '·')
    .replace(/\$([^$]+)\$/g, '$1')
    .trim();
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

function toBlocks(stem: string): StemBlock[] {
  const blocks: StemBlock[] = [];
  const lines = stem.replace(/\r\n/g, '\n').split('\n');

  let i = 0;
  while (i < lines.length) {
    const line = lines[i]?.trim() ?? '';

    if (line === '') {
      i += 1;
      continue;
    }

    if (line.startsWith('{/*') || line.endsWith('*/}')) {
      i += 1;
      continue;
    }

    if (line.startsWith('![') && line.includes('](')) {
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
        text: cleanInlineMarkdown(mathLines.join('\n')),
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
      if (candidate.startsWith('![') && candidate.includes('](')) {
        i += 1;
        continue;
      }
      paragraphLines.push(candidate);
      i += 1;
    }

    const text = cleanInlineMarkdown(paragraphLines.join(' '));
    if (text) {
      blocks.push({ type: 'paragraph', text });
    }
  }

  return blocks;
}

function QuestionStemImpl({ stem }: Props) {
  const blocks = useMemo(() => toBlocks(stem), [stem]);

  return (
    <View style={styles.root}>
      {blocks.map((block, index) => {
        const key = `${block.type}-${index}`;

        if (block.type === 'paragraph') {
          return (
            <Text key={key} style={styles.paragraph}>
              {block.text}
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

        const header = block.rows[0] ?? [];
        const body = block.rows.slice(1);

        return (
          <View key={key} style={styles.table}>
            <View style={styles.tableRow}>
              {header.map((cell, idx) => (
                <Text key={`h-${idx}`} style={[styles.cell, styles.headerCell]}>
                  {cell}
                </Text>
              ))}
            </View>
            {body.map((row, rowIndex) => (
              <View key={`r-${rowIndex}`} style={styles.tableRow}>
                {row.map((cell, idx) => (
                  <Text key={`c-${rowIndex}-${idx}`} style={styles.cell}>
                    {cell}
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
    fontSize: 12,
    lineHeight: 18,
    fontFamily: 'Courier',
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
});

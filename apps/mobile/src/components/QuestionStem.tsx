import { memo, useMemo } from 'react';
import { Image } from 'expo-image';
import { StyleSheet, Text, View } from 'react-native';
import type { WorkshopRichBlock } from '../types/api';
import {
  cleanInlineForRender,
  cleanInlineMarkdown,
  normalizeMathForDisplay,
  parseInlineSegments,
  toBlocks,
} from '../lib/workshopRender';
import type { InlineSegment, StemBlock } from '../lib/workshopRender';

type Props = {
  stem: string;
  stemAssets?: string[];
  blocks?: WorkshopRichBlock[] | null;
};

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

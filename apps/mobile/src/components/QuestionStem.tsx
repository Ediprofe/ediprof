import { memo, useMemo } from 'react';
import { Image } from 'expo-image';
import { StyleSheet, Text, View } from 'react-native';
import type { TextStyle } from 'react-native';
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
  nodes?: WorkshopRichBlock[] | null;
  blocks?: WorkshopRichBlock[] | null;
  compact?: boolean;
};

function QuestionStemImpl({ stem, stemAssets = [], nodes = null, blocks = null, compact = false }: Props) {
  const blocksNormalized = useMemo<StemBlock[]>(() => {
    const sourceBlocks = Array.isArray(nodes) && nodes.length > 0
      ? nodes
      : (Array.isArray(blocks) && blocks.length > 0 ? blocks : null);

    if (sourceBlocks) {
      const mapped: StemBlock[] = sourceBlocks
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

          if (block.type === 'heading') {
            return {
              type: 'heading',
              depth: typeof block.depth === 'number' ? block.depth : 3,
              inlines: Array.isArray(block.inlines)
                ? block.inlines.filter((segment) => typeof segment?.text === 'string')
                : [],
            };
          }

          if (block.type === 'list') {
            return {
              type: 'list',
              ordered: Boolean(block.ordered),
              items: Array.isArray(block.items)
                ? block.items
                    .filter((item) => item && typeof item === 'object')
                    .map((item) => ({
                      inlines: Array.isArray(item.inlines)
                        ? item.inlines.filter((segment) => typeof segment?.text === 'string')
                        : [],
                    }))
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

          if (block.type === 'html') {
            return {
              type: 'html',
              html: block.html ?? '',
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
  }, [blocks, nodes, stem, stemAssets]);

  const renderInlineSegments = (
    segments: InlineSegment[],
    baseStyle: TextStyle,
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
              : segment.variant === 'italic'
                ? styles.inlineItalic
              : null;

      return (
        <Text key={`${keyPrefix}-${idx}`} style={[baseStyle, segmentStyle]}>
          {cleanInlineForRender(segment.text)}
        </Text>
      );
    });
  };

  return (
    <View style={[styles.root, compact ? styles.rootCompact : null]}>
      {blocksNormalized.map((block, index) => {
        const key = `${block.type}-${index}`;

        if (block.type === 'paragraph') {
          const segments = block.inlines ?? parseInlineSegments(block.text ?? '');

          return (
            <Text key={key} style={[styles.paragraph, compact ? styles.paragraphCompact : null]}>
              {renderInlineSegments(segments, compact ? styles.paragraphCompact : styles.paragraph, key)}
            </Text>
          );
        }

        if (block.type === 'heading') {
          const segments = block.inlines ?? [];
          const headingStyle =
            block.depth <= 2
              ? styles.headingLg
              : block.depth === 3
                ? styles.headingMd
                : styles.headingSm;

          return (
            <Text key={key} style={[headingStyle, compact ? styles.headingCompact : null]}>
              {renderInlineSegments(segments, headingStyle, key)}
            </Text>
          );
        }

        if (block.type === 'list') {
          return (
            <View key={key} style={styles.list}>
              {block.items.map((item, itemIndex) => {
                const marker = block.ordered ? `${itemIndex + 1}.` : '•';
                const segments = item.inlines ?? [];

                return (
                  <View key={`${key}-item-${itemIndex}`} style={styles.listItem}>
                    <Text style={[styles.listMarker, compact ? styles.paragraphCompact : null]}>{marker}</Text>
                    <Text style={[styles.paragraph, compact ? styles.paragraphCompact : null, styles.listItemText]}>
                      {renderInlineSegments(segments, compact ? styles.paragraphCompact : styles.paragraph, `${key}-item-${itemIndex}`)}
                    </Text>
                  </View>
                );
              })}
            </View>
          );
        }

        if (block.type === 'math' || block.type === 'equation') {
          const mathText =
            block.type === 'equation'
              ? normalizeMathForDisplay(cleanInlineMarkdown(block.latex))
              : block.text;

          return (
            <View key={key} style={[styles.mathBox, compact ? styles.mathBoxCompact : null]}>
              <Text style={[styles.mathText, compact ? styles.mathTextCompact : null]}>{mathText}</Text>
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
              style={[styles.image, compact ? styles.imageCompact : null]}
              contentFit="contain"
              transition={120}
            />
          );
        }

        if (block.type === 'html') {
          const plainText = cleanInlineForRender(
            block.html
              .replace(/<br\s*\/?>/gi, '\n')
              .replace(/<\/(p|div|li|h[1-6])>/gi, '\n')
              .replace(/<[^>]+>/g, ' ')
              .replace(/\s+\n/g, '\n')
              .replace(/\n{3,}/g, '\n\n')
              .trim()
          );

          if (!plainText) {
            return null;
          }

          return (
            <Text key={key} style={[styles.paragraph, compact ? styles.paragraphCompact : null]}>
              {plainText}
            </Text>
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
  rootCompact: {
    gap: 8,
  },
  paragraph: {
    color: '#d4ddf7',
    fontSize: 12,
    lineHeight: 19,
  },
  paragraphCompact: {
    fontSize: 11,
    lineHeight: 17,
  },
  headingLg: {
    color: '#f4f7ff',
    fontSize: 16,
    lineHeight: 22,
    fontWeight: '800',
  },
  headingMd: {
    color: '#eef4ff',
    fontSize: 14,
    lineHeight: 20,
    fontWeight: '800',
  },
  headingSm: {
    color: '#e4edff',
    fontSize: 13,
    lineHeight: 18,
    fontWeight: '700',
  },
  headingCompact: {
    fontSize: 12,
    lineHeight: 17,
  },
  list: {
    gap: 6,
  },
  listItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 8,
  },
  listMarker: {
    color: '#d4ddf7',
    fontSize: 12,
    lineHeight: 19,
    fontWeight: '700',
  },
  listItemText: {
    flex: 1,
  },
  mathBox: {
    borderWidth: 1,
    borderColor: '#304a80',
    borderRadius: 8,
    backgroundColor: '#081127',
    paddingHorizontal: 10,
    paddingVertical: 8,
  },
  mathBoxCompact: {
    paddingHorizontal: 8,
    paddingVertical: 6,
  },
  mathText: {
    color: '#d8e6ff',
    fontSize: 14,
    lineHeight: 18,
    fontFamily: 'Courier',
    letterSpacing: 0.2,
  },
  mathTextCompact: {
    fontSize: 12,
    lineHeight: 16,
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
  imageCompact: {
    height: 160,
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
  inlineItalic: {
    fontStyle: 'italic',
  },
});

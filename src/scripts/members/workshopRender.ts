import {
  cleanInlineForRender as cleanInlineForRenderShared,
  cleanInlineMarkdown as cleanInlineMarkdownShared,
  normalizeLatexInlineText as normalizeLatexInlineTextShared,
  normalizeMathForDisplay as normalizeMathForDisplayShared,
  parseInlineSegments as parseInlineSegmentsShared,
} from '../workshops/inlineShared.js';

export type InlineVariant = 'plain' | 'highlight' | 'strike' | 'bold';

export type InlineSegment = {
  text: string;
  variant: InlineVariant;
};

export function normalizeLatexInlineText(value: string): string {
  return normalizeLatexInlineTextShared(value);
}

export function cleanInlineMarkdown(value: string): string {
  return cleanInlineMarkdownShared(value);
}

export function cleanInlineForRender(value: string): string {
  return cleanInlineForRenderShared(value);
}

export function normalizeMathForDisplay(value: string): string {
  return normalizeMathForDisplayShared(value);
}

export function parseInlineSegments(value: string): InlineSegment[] {
  return parseInlineSegmentsShared(value) as InlineSegment[];
}

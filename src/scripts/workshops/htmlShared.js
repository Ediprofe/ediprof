import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import remarkBreaks from 'remark-breaks';
import remarkRehype from 'remark-rehype';
import rehypeRaw from 'rehype-raw';
import rehypeKatex from 'rehype-katex';
import rehypeStringify from 'rehype-stringify';
import rehypeExternalLinks from 'rehype-external-links';
import { youtubeAutoEmbed } from '../../plugins/youtube-auto-embed.js';
import tableWrapper from '../../plugins/table-wrapper.js';
import { remarkSaberMarcadores } from '../../plugins/remark-saber-marcadores.js';
import { rehypeSaberOpciones } from '../../plugins/rehype-saber-opciones.js';

function normalizeFragment(value = '') {
  return String(value || '').replace(/\r\n/g, '\n').trim();
}

export async function renderPracticeFragmentHtml(value = '', options = {}) {
  const source = normalizeFragment(value);
  if (!source) {
    return '';
  }

  const filePath = String(options.filePath || '');

  const processor = unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkMath, { singleDollarTextMath: true })
    .use(youtubeAutoEmbed)
    .use(remarkSaberMarcadores)
    .use(remarkBreaks)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .use(rehypeKatex, {
      strict: false,
      trust: true,
      output: 'htmlAndMathml',
      throwOnError: false,
      errorColor: '#cc0000',
      fleqn: false,
      minRuleThickness: 0.05,
      maxSize: 100,
      maxExpand: 1000,
      macros: {
        '\\R': '\\mathbb{R}',
        '\\N': '\\mathbb{N}',
        '\\Z': '\\mathbb{Z}',
        '\\Q': '\\mathbb{Q}',
        '\\C': '\\mathbb{C}',
        '\\sen': '\\text{sen}',
        '\\cos': '\\text{cos}',
      },
    })
    .use(rehypeSaberOpciones)
    .use(rehypeExternalLinks, {
      target: '_blank',
      rel: ['noopener', 'noreferrer'],
    })
    .use(tableWrapper)
    .use(rehypeStringify, { allowDangerousHtml: true });

  const result = await processor.process({
    value: source,
    path: filePath || undefined,
  });

  return String(result.value || '').trim();
}

export const QUESTION_HEADING_REGEX = /^##\s+(\d+)(?:\s+\([^)]+\))?\.?\s*$/gm;
export const EXPLICIT_CONTEXT_REGEX = /<ContextoCompartido([^>]*)>([\s\S]*?)<\/ContextoCompartido>/gi;

export function parseTagAttributes(raw = '') {
  const attrs = {};
  const regex = /([\w:-]+)="([^"]*)"|([\w:-]+)/g;
  let match = null;

  while ((match = regex.exec(raw)) !== null) {
    if (match[1]) {
      attrs[match[1]] = match[2];
    } else if (match[3]) {
      attrs[match[3]] = true;
    }
  }

  return attrs;
}

export function splitQuestionSections(content) {
  const regex = new RegExp(QUESTION_HEADING_REGEX.source, QUESTION_HEADING_REGEX.flags);
  const matches = [];
  let match = null;

  while ((match = regex.exec(content)) !== null) {
    matches.push({
      number: Number.parseInt(match[1], 10),
      start: match.index,
      end: regex.lastIndex,
    });
  }

  if (matches.length === 0) return [];

  return matches.map((item, index) => {
    const nextStart = matches[index + 1]?.start ?? content.length;

    return {
      number: item.number,
      raw: content.slice(item.end, nextStart).trim(),
    };
  });
}

function normalizeSummary(rawSummary, fallback) {
  const normalized = String(rawSummary || '').trim();
  return normalized || fallback;
}

function inferDetailsKind(attrs, summary) {
  const classNames = String(attrs.class || '')
    .split(/\s+/)
    .map((value) => value.trim().toLowerCase())
    .filter(Boolean);
  const normalizedSummary = String(summary || '').trim().toLowerCase();

  if (
    classNames.includes('conceptos-relacionados') ||
    /conceptos?\s+relacionados/.test(normalizedSummary)
  ) {
    return 'concepts';
  }

  if (/respuesta|soluci[oó]n/.test(normalizedSummary)) {
    return 'feedback';
  }

  return 'details';
}

function collectExplicitSections(inner, tagName, kind, fallbackSummary) {
  const regex = new RegExp(`<${tagName}([^>]*)>([\\s\\S]*?)<\\/${tagName}>`, 'gi');
  const sections = [];
  let match = null;

  while ((match = regex.exec(inner)) !== null) {
    const attrs = parseTagAttributes(match[1] || '');
    sections.push({
      kind,
      raw: String(match[0] || ''),
      summary: normalizeSummary(attrs.summary || attrs.titulo || attrs.title, fallbackSummary),
      content: String(match[2] || '').trim(),
      index: match.index ?? 0,
    });
  }

  return sections;
}

export function parseSupplementSections(inner) {
  const sections = [
    ...collectExplicitSections(inner, 'Respuesta', 'feedback', 'Respuesta'),
    ...collectExplicitSections(
      inner,
      'ConceptosRelacionados',
      'concepts',
      'Conceptos relacionados'
    ),
  ];

  const detailsRegex = /<details\b([^>]*)>([\s\S]*?)<\/details>/gi;
  let match = null;

  while ((match = detailsRegex.exec(inner)) !== null) {
    const attrs = parseTagAttributes(match[1] || '');
    const body = String(match[2] || '').trim();
    const summaryMatch = body.match(/<summary>([\s\S]*?)<\/summary>/i);
    const summary = normalizeSummary(
      String(summaryMatch?.[1] || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' '),
      'Respuesta'
    );
    const content = body.replace(/<summary>[\s\S]*?<\/summary>/i, '').trim();

    sections.push({
      kind: inferDetailsKind(attrs, summary),
      raw: String(match[0] || ''),
      summary,
      content,
      index: match.index ?? 0,
    });
  }

  return sections.sort((a, b) => a.index - b.index);
}

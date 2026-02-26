#!/usr/bin/env node

/**
 * Preflight de talleres Saber antes de exportar/sincronizar.
 *
 * Valida:
 * - Estructura base de preguntas (<Pregunta>, <Opciones>, <details>)
 * - Coherencia opciones/correcta
 * - IDs duplicados
 * - Rangos de contexto compartido
 * - Referencias de assets locales
 * - Fugas visibles de LaTeX en bloques ya parseados para app
 *
 * Uso:
 *   node scripts/workshops-preflight.mjs
 *   node scripts/workshops-preflight.mjs --strict-warnings
 */

import { existsSync, readFileSync, unlinkSync } from 'fs';
import { resolve } from 'path';
import { globSync } from 'glob';
import { spawnSync } from 'child_process';

const WORKSHOPS_GLOB = 'src/content/saber/**/taller.{md,mdx}';
const TEMP_MANIFEST = '/tmp/ediprofe-workshops-manifest.preflight.json';

function parseArgs(argv) {
  return {
    strictWarnings: argv.includes('--strict-warnings'),
  };
}

function normalizePath(pathLike) {
  return String(pathLike || '').replace(/\\/g, '/');
}

function parseFrontmatter(raw) {
  if (!raw.startsWith('---\n')) {
    return { data: {}, content: raw };
  }

  const endIndex = raw.indexOf('\n---\n', 4);
  if (endIndex === -1) {
    return { data: {}, content: raw };
  }

  const block = raw.slice(4, endIndex);
  const content = raw.slice(endIndex + 5);
  const data = {};

  block.split('\n').forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return;

    const separator = trimmed.indexOf(':');
    if (separator === -1) return;

    const key = trimmed.slice(0, separator).trim();
    const value = trimmed.slice(separator + 1).trim();

    if (!key) return;
    data[key] = value;
  });

  return { data, content };
}

function splitQuestionSections(content) {
  const headingRegex = /^##\s+(\d+)\.?\s*$/gm;
  const matches = [];
  let match = null;

  while ((match = headingRegex.exec(content)) !== null) {
    matches.push({
      number: Number.parseInt(match[1], 10),
      start: match.index,
      end: headingRegex.lastIndex,
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

function parseTagAttributes(raw = '') {
  const attrs = {};
  const regex = /(\w+)="([^"]*)"|(\w+)/g;
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

function parseOptions(optionsBody) {
  const optionRegex = /<Opcion([^>]*)>([\s\S]*?)<\/Opcion>/gi;
  const options = [];
  let match = null;

  while ((match = optionRegex.exec(optionsBody)) !== null) {
    const attrs = parseTagAttributes(match[1] || '');
    const optionId = String(attrs.letra || '').trim().toUpperCase();
    const isCorrect = attrs.correcta === true || attrs.correcta === 'true';
    const optionText = String(match[2] || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();

    options.push({
      id: optionId || `OPT_${options.length + 1}`,
      text: optionText,
      isCorrect,
    });
  }

  return options;
}

function parseSharedContextRanges(contextMdx) {
  const ranges = [];
  const regex = /RESPONDA\s+LAS\s+PREGUNTAS\s+(\d+)\s+A\s+(\d+)/gi;
  let match = null;

  while ((match = regex.exec(contextMdx)) !== null) {
    const start = Number.parseInt(match[1], 10);
    const end = Number.parseInt(match[2], 10);
    if (!Number.isFinite(start) || !Number.isFinite(end)) continue;

    ranges.push({
      start: Math.min(start, end),
      end: Math.max(start, end),
    });
  }

  return ranges;
}

function extractAssetRefs(content) {
  const refs = [];
  const mdRefRegex = /!?\[[^\]]*\]\(([^)]+)\)/g;
  const htmlRefRegex = /\b(?:src|href)\s*=\s*["']([^"']+)["']/g;

  let match = null;
  while ((match = mdRefRegex.exec(content)) !== null) {
    const raw = (match[1] || '').trim();
    const ref = raw.split(/\s+"/)[0].replace(/[?#].*$/, '');
    refs.push(ref);
  }

  while ((match = htmlRefRegex.exec(content)) !== null) {
    const ref = (match[1] || '').trim().replace(/[?#].*$/, '');
    refs.push(ref);
  }

  return [...new Set(refs.filter(Boolean))];
}

function validateAssetRef(ref) {
  if (ref.startsWith('https://cdn.ediprofe.com/')) {
    return { ok: true, kind: 'cdn' };
  }

  if (ref.startsWith('http://') || ref.startsWith('https://')) {
    return {
      ok: true,
      kind: 'external',
      warning: `asset externo no canónico: ${ref}`,
    };
  }

  if (ref.startsWith('/')) {
    const candidates = [
      resolve(`public${ref}`),
      resolve(`src${ref}`),
      resolve(ref.slice(1)),
    ];

    const exists = candidates.some((candidate) => existsSync(candidate));
    if (!exists) {
      return {
        ok: false,
        kind: 'local',
        error: `asset local no encontrado: ${ref}`,
      };
    }
    return { ok: true, kind: 'local' };
  }

  return {
    ok: true,
    kind: 'relative',
    warning: `asset relativo (revisar): ${ref}`,
  };
}

function hasStructuralWrappers(raw) {
  return /<\/?(div|span)\b[^>]*>/i.test(String(raw || ''));
}

function runManifestExport() {
  const cmd = spawnSync(
    process.execPath,
    [resolve('scripts/export-workshops-manifest.mjs'), '--output', TEMP_MANIFEST],
    { encoding: 'utf-8' }
  );

  if (cmd.status !== 0) {
    return {
      ok: false,
      message: cmd.stderr || cmd.stdout || 'Falló export-workshops-manifest.',
    };
  }

  if (!existsSync(TEMP_MANIFEST)) {
    return {
      ok: false,
      message: `No se generó manifiesto temporal: ${TEMP_MANIFEST}`,
    };
  }

  const json = JSON.parse(readFileSync(TEMP_MANIFEST, 'utf-8'));
  return { ok: true, json };
}

function findLatexLeakInText(text) {
  const source = String(text || '');
  return /\\(?:text|left|right|frac|sqrt|cdot|times|rightarrow|alpha|beta|gamma)\b/.test(source);
}

function validateManifestBlocks(manifest, collector) {
  const workshops = Array.isArray(manifest?.workshops) ? manifest.workshops : [];

  workshops.forEach((workshop) => {
    const route = workshop?.route || 'unknown-route';
    const questions = Array.isArray(workshop?.questions) ? workshop.questions : [];

    questions.forEach((question) => {
      const qRef = `${route}#Q${question?.order ?? '?'}`;
      const groups = [
        ['stem_blocks', question?.stem_blocks || []],
        ['feedback_blocks', question?.feedback_blocks || []],
        ['context_blocks', question?.context_blocks || []],
      ];

      groups.forEach(([label, blocks]) => {
        if (!Array.isArray(blocks)) return;

        blocks.forEach((block, idx) => {
          if (!block || typeof block !== 'object') return;

          if (block.type === 'paragraph') {
            const inlines = Array.isArray(block.inlines) ? block.inlines : [];
            inlines.forEach((inline) => {
              const text = String(inline?.text || '');
              if (findLatexLeakInText(text)) {
                collector.warnings.push(
                  `[${qRef}] ${label}[${idx}] contiene comandos LaTeX visibles: "${text.slice(0, 80)}"`
                );
              }
              if (/<\/?(div|span)\b/i.test(text)) {
                collector.errors.push(
                  `[${qRef}] ${label}[${idx}] contiene HTML estructural filtrado: "${text.slice(0, 80)}"`
                );
              }
            });
          }

          if (block.type === 'equation') {
            const latex = String(block.latex || '');
            if (/\barrow\b|\brightarrow\b|\bightarrow\b/i.test(latex)) {
              collector.errors.push(
                `[${qRef}] ${label}[${idx}] tiene flecha no normalizada ("arrow/rightarrow"): "${latex}"`
              );
            }
          }
        });
      });
    });
  });
}

function main() {
  const { strictWarnings } = parseArgs(process.argv.slice(2));
  const files = globSync(WORKSHOPS_GLOB, { nodir: true }).sort();

  if (files.length === 0) {
    console.log('No se encontraron talleres para validar.');
    process.exit(0);
  }

  const collector = {
    errors: [],
    warnings: [],
    files: files.length,
    questions: 0,
  };

  files.forEach((filePath) => {
    const rawFile = readFileSync(filePath, 'utf-8');
    const { content } = parseFrontmatter(rawFile);
    const sections = splitQuestionSections(content);
    const relPath = normalizePath(filePath);

    if (sections.length === 0) {
      collector.errors.push(`[${relPath}] no tiene secciones "## N."`);
      return;
    }

    const seenIds = new Set();
    const sharedRanges = [];
    let expectedNumber = 1;

    sections.forEach((section) => {
      collector.questions += 1;

      if (section.number !== expectedNumber) {
        collector.warnings.push(
          `[${relPath}] numeración no secuencial: se esperaba ${expectedNumber} y se encontró ${section.number}`
        );
      }
      expectedNumber = section.number + 1;

      const questionMatch = section.raw.match(/<Pregunta([^>]*)>([\s\S]*?)<\/Pregunta>/i);
      if (!questionMatch) {
        collector.errors.push(`[${relPath}#${section.number}] bloque <Pregunta> inválido o ausente`);
        return;
      }

      const attrs = parseTagAttributes(questionMatch[1] || '');
      const questionId = String(attrs.id || section.number).trim();
      if (!questionId) {
        collector.errors.push(`[${relPath}#${section.number}] id de pregunta vacío`);
      } else if (seenIds.has(questionId)) {
        collector.errors.push(`[${relPath}#${section.number}] id duplicado: "${questionId}"`);
      } else {
        seenIds.add(questionId);
      }

      const fullQuestion = questionMatch[0] || '';
      const inner = (questionMatch[2] || '').trim();
      const matchIndex = questionMatch.index ?? 0;
      const leading = section.raw.slice(0, matchIndex).trim();
      const trailing = section.raw.slice(matchIndex + fullQuestion.length).trim();
      const detachedContext = [leading, trailing].filter(Boolean).join('\n\n');

      if (hasStructuralWrappers(detachedContext)) {
        collector.warnings.push(
          `[${relPath}#${section.number}] contexto con <div>/<span>. Recomendado: contexto en markdown puro, sin wrappers HTML`
        );
      }

      const ranges = parseSharedContextRanges(detachedContext);
      sharedRanges.push(...ranges);

      const optionsMatch = inner.match(/<Opciones>([\s\S]*?)<\/Opciones>/i);
      if (!optionsMatch) {
        collector.errors.push(`[${relPath}#${section.number}] bloque <Opciones> ausente`);
      }

      const detailsMatch = inner.match(/<details>([\s\S]*?)<\/details>/i);
      if (!detailsMatch) {
        collector.errors.push(`[${relPath}#${section.number}] bloque <details> (retroalimentación) ausente`);
      }

      const options = parseOptions(optionsMatch ? optionsMatch[1] : '');
      if (options.length < 2) {
        collector.errors.push(`[${relPath}#${section.number}] debe tener al menos 2 opciones`);
      }

      const seenOptionIds = new Set();
      let correctCount = 0;
      options.forEach((option) => {
        if (!option.text) {
          collector.warnings.push(
            `[${relPath}#${section.number}] opción ${option.id} sin texto`
          );
        }

        if (seenOptionIds.has(option.id)) {
          collector.errors.push(
            `[${relPath}#${section.number}] opción duplicada: "${option.id}"`
          );
        } else {
          seenOptionIds.add(option.id);
        }

        if (option.isCorrect) {
          correctCount += 1;
        }
      });

      if (correctCount !== 1) {
        collector.errors.push(
          `[${relPath}#${section.number}] debe existir exactamente 1 opción correcta (actual: ${correctCount})`
        );
      }

      const assetRefs = extractAssetRefs(`${inner}\n${detachedContext}`);
      assetRefs.forEach((ref) => {
        const result = validateAssetRef(ref);
        if (!result.ok && result.error) {
          collector.errors.push(`[${relPath}#${section.number}] ${result.error}`);
        } else if (result.warning) {
          collector.warnings.push(`[${relPath}#${section.number}] ${result.warning}`);
        }
      });
    });

    sharedRanges.forEach((range) => {
      if (range.start < 1 || range.end > sections.length) {
        collector.errors.push(
          `[${relPath}] rango de contexto compartido fuera de límites: ${range.start}-${range.end} (preguntas disponibles: ${sections.length})`
        );
      }
    });
  });

  const manifestExport = runManifestExport();
  if (!manifestExport.ok) {
    collector.errors.push(`[manifest] ${manifestExport.message}`);
  } else {
    validateManifestBlocks(manifestExport.json, collector);
  }

  try {
    if (existsSync(TEMP_MANIFEST)) {
      unlinkSync(TEMP_MANIFEST);
    }
  } catch {
    // no-op
  }

  console.log('Workshop preflight summary');
  console.log(`  Files:     ${collector.files}`);
  console.log(`  Questions: ${collector.questions}`);
  console.log(`  Warnings:  ${collector.warnings.length}`);
  console.log(`  Errors:    ${collector.errors.length}`);

  if (collector.warnings.length > 0) {
    console.log('\nWarnings:');
    collector.warnings.forEach((warning) => console.log(`  - ${warning}`));
  }

  if (collector.errors.length > 0) {
    console.log('\nErrors:');
    collector.errors.forEach((error) => console.log(`  - ${error}`));
  }

  const shouldFail = collector.errors.length > 0 || (strictWarnings && collector.warnings.length > 0);
  process.exit(shouldFail ? 1 : 0);
}

main();

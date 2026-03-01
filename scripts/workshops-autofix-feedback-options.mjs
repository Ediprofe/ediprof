#!/usr/bin/env node

/**
 * Normaliza opciones A/B/C/D dentro de <details> de talleres Saber para que
 * se rendericen en líneas separadas en web/app/PDF.
 *
 * Regla aplicada:
 *   A. Texto...
 *   B. Texto...
 * -> 
 *   - A. Texto...
 *   - B. Texto...
 *
 * Uso:
 *   node scripts/workshops-autofix-feedback-options.mjs
 *   node scripts/workshops-autofix-feedback-options.mjs --check
 */

import { readFileSync, writeFileSync } from 'fs';
import { globSync } from 'glob';

const WORKSHOPS_GLOB = 'src/content/saber/**/taller.{md,mdx}';
const CHECK_ONLY = process.argv.includes('--check');

function normalizeDetailsBlock(detailsRaw) {
  const lines = detailsRaw.split('\n');
  let changed = 0;

  const normalized = lines.map((line) => {
    // Ya está en lista markdown: "  - A. ..."
    if (/^\s*-\s+[A-D]\.\s+/.test(line)) {
      return line;
    }

    // Opción compacta no-lista: "  A. ..."
    const match = line.match(/^(\s*)([A-D])\.\s+(.*)$/);
    if (!match) return line;

    const [, indent, letter, rest] = match;
    changed += 1;
    return `${indent}- ${letter}. ${rest}`;
  });

  return {
    content: normalized.join('\n'),
    changed,
  };
}

function normalizeFile(raw) {
  let changed = 0;
  const output = raw.replace(/<details>[\s\S]*?<\/details>/g, (detailsBlock) => {
    const normalized = normalizeDetailsBlock(detailsBlock);
    changed += normalized.changed;
    return normalized.content;
  });

  return { output, changed };
}

function main() {
  const files = globSync(WORKSHOPS_GLOB, { nodir: true }).sort();
  if (files.length === 0) {
    console.log('No se encontraron archivos de talleres.');
    process.exit(0);
  }

  let filesChanged = 0;
  let linesChanged = 0;

  files.forEach((filePath) => {
    const raw = readFileSync(filePath, 'utf-8');
    const { output, changed } = normalizeFile(raw);
    if (changed === 0) return;

    filesChanged += 1;
    linesChanged += changed;

    if (!CHECK_ONLY) {
      writeFileSync(filePath, output);
    }
  });

  console.log('Autofix feedback options summary');
  console.log(`  Files scanned:  ${files.length}`);
  console.log(`  Files changed:  ${filesChanged}`);
  console.log(`  Lines changed:  ${linesChanged}`);
  console.log(`  Mode:           ${CHECK_ONLY ? 'check' : 'write'}`);

  if (CHECK_ONLY && filesChanged > 0) {
    process.exit(1);
  }
}

main();

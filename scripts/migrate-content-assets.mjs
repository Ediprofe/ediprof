#!/usr/bin/env node

/**
 * Migra referencias legacy de assets en contenido Markdown/MDX.
 *
 * Reglas seguras por defecto:
 * - https://cdn.ediprofe.com/images/... -> https://cdn.ediprofe.com/img/...
 * - aliases definidos en images-index.json -> canonicalUrl
 *
 * Opcional:
 * - --include-local: también intenta convertir /images/... mapeados en el índice
 *
 * Uso:
 *   node scripts/migrate-content-assets.mjs
 *   node scripts/migrate-content-assets.mjs --write
 *   node scripts/migrate-content-assets.mjs --write --include-local
 */

import { readFileSync, writeFileSync } from 'fs';
import { globSync } from 'glob';

const CONTENT_GLOB = 'src/content/**/*.{md,mdx}';
const INDEX_FILE = 'images-index.json';
const LEGACY_PREFIX = 'https://cdn.ediprofe.com/images/';
const CANONICAL_PREFIX = 'https://cdn.ediprofe.com/img/';

function parseArgs(argv) {
  return {
    write: argv.includes('--write'),
    includeLocal: argv.includes('--include-local'),
  };
}

function addRule(rules, from, to) {
  if (!from || !to || from === to) return;
  rules.set(from, to);
}

function loadRewriteRules(includeLocal) {
  const index = JSON.parse(readFileSync(INDEX_FILE, 'utf-8'));
  const images = Array.isArray(index.images) ? index.images : [];
  const rules = new Map();

  images.forEach((entry) => {
    const canonicalUrl = entry.canonicalUrl || entry.url;
    if (!canonicalUrl) return;

    addRule(rules, entry.url, canonicalUrl);

    if (Array.isArray(entry.aliases)) {
      entry.aliases.forEach((alias) => addRule(rules, alias, canonicalUrl));
    }

    if (includeLocal && typeof entry.canonicalPath === 'string') {
      // Convierte /images/<...> cuando hay mapeo explícito en el índice.
      const localPath = '/' + entry.canonicalPath.replace(/^img\//, 'images/');
      addRule(rules, localPath, canonicalUrl);
    }
  });

  return rules;
}

function countOccurrences(text, value) {
  if (!value) return 0;
  return text.split(value).length - 1;
}

function applyLiteralRewrites(content, rules) {
  let next = content;
  let replacements = 0;

  for (const [from, to] of rules.entries()) {
    const occurrences = countOccurrences(next, from);
    if (occurrences === 0) continue;
    next = next.split(from).join(to);
    replacements += occurrences;
  }

  return { content: next, replacements };
}

function applyLegacyPrefixRewrite(content) {
  const regex = /https:\/\/cdn\.ediprofe\.com\/images\//g;
  const matches = content.match(regex);
  const count = matches ? matches.length : 0;
  if (count === 0) {
    return { content, replacements: 0 };
  }

  return {
    content: content.replace(regex, CANONICAL_PREFIX),
    replacements: count,
  };
}

function main() {
  const { write, includeLocal } = parseArgs(process.argv.slice(2));
  const files = globSync(CONTENT_GLOB, { nodir: true }).sort();
  const rules = loadRewriteRules(includeLocal);

  let touchedFiles = 0;
  let totalReplacements = 0;

  for (const file of files) {
    const original = readFileSync(file, 'utf-8');

    const literalPass = applyLiteralRewrites(original, rules);
    const prefixPass = applyLegacyPrefixRewrite(literalPass.content);

    const next = prefixPass.content;
    const replacements = literalPass.replacements + prefixPass.replacements;

    if (replacements === 0 || next === original) continue;

    touchedFiles += 1;
    totalReplacements += replacements;

    if (write) {
      writeFileSync(file, next, 'utf-8');
    }
  }

  console.log('🔁 Migración de assets en contenido');
  console.log(`   Archivos escaneados: ${files.length}`);
  console.log(`   Archivos con cambios: ${touchedFiles}`);
  console.log(`   Reemplazos aplicables: ${totalReplacements}`);
  console.log(`   Reglas cargadas: ${rules.size}`);
  console.log(`   Modo: ${write ? 'write' : 'dry-run'}`);
  console.log(`   Include local: ${includeLocal ? 'sí' : 'no'}`);

  if (!write && touchedFiles > 0) {
    console.log('💡 Ejecuta con --write para aplicar los cambios.');
  }
}

main();

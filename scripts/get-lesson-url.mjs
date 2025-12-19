#!/usr/bin/env node
/**
 * get-lesson-url.mjs
 * Genera la URL de una lección usando la lógica existente del proyecto
 * 
 * Uso: node scripts/get-lesson-url.mjs src/content/fisica/01-intro/.../01-leccion.md
 * Salida: fisica/introduccion/.../leccion
 */

import { cleanSlug } from '../src/utils/navigation-generator.js';

const filePath = process.argv[2];

if (!filePath) {
    console.error('Uso: node get-lesson-url.mjs <ruta-archivo-md>');
    process.exit(1);
}

// Extraer la parte relevante: todo después de src/content/ y antes de .md/.mdx
const match = filePath.match(/src\/content\/([^/]+)\/(.+?)\.mdx?$/);

if (!match) {
    console.error('Ruta no válida');
    process.exit(1);
}

const materia = match[1];
const lessonSlug = match[2];

// Usar cleanSlug del proyecto
const cleanedSlug = cleanSlug(lessonSlug);
const fullUrl = `${materia}/${cleanedSlug}`;

console.log(fullUrl);

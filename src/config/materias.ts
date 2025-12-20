/**
 * Configuración centralizada de materias
 * Este archivo contiene toda la información de configuración de las materias
 * para evitar duplicación de código en múltiples archivos.
 * 
 * IMPORTANTE: Si cambias colores aquí, también actualiza los gradientes de fondo
 * en los archivos CSS que tienen el comentario "SINCRONIZAR con src/config/materias.ts":
 * - src/styles/layouts/lesson.css
 * - src/styles/pages/materia.css
 * - src/styles/pages/capitulo.css
 * - src/styles/pages/tema.css
 */

export interface MateriaConfig {
  name: string;        // Nombre con tilde para mostrar
  icon: string;
  color: string;
  gradient: string;
  lightBg: string;
  lightSolid: string;  // Color light sólido para impresión (no rgba)
  dark: string;        // Color oscuro para títulos en impresión
  description: string;
}

// =========================================
// CONSTANTES DEL SITIO (URLs, redes sociales)
// =========================================
export const SITE_CONFIG = {
  url: 'https://ediprofe.com',
  name: 'Ediprofe',
  tagline: 'Educación de calidad para todos',
  social: {
    youtube: { url: 'https://www.youtube.com/PROFEEDI', handle: '@PROFEEDI' },
    tiktok: { url: 'https://www.tiktok.com/@EDIPROFE', handle: '@EDIPROFE' },
  }
} as const;

export const MATERIAS_SLUGS = ['matematicas', 'fisica', 'quimica', 'ciencias'] as const;
export type MateriaSlug = typeof MATERIAS_SLUGS[number];

export const materiaConfig: Record<MateriaSlug, MateriaConfig> = {
  matematicas: {
    name: 'Matemáticas',
    icon: '🧮',
    color: '#ef4444',
    gradient: 'linear-gradient(135deg, #ef4444, #dc2626)',
    lightBg: 'rgba(239, 68, 68, 0.1)',
    lightSolid: '#fee2e2',
    dark: '#991b1b',
    description: 'Álgebra, geometría, cálculo y más'
  },
  fisica: {
    name: 'Física',
    icon: '🚀',
    color: '#3b82f6',
    gradient: 'linear-gradient(135deg, #3b82f6, #2563eb)',
    lightBg: 'rgba(59, 130, 246, 0.1)',
    lightSolid: '#dbeafe',
    dark: '#1e40af',
    description: 'Mecánica, ondas, termodinámica'
  },
  quimica: {
    name: 'Química',
    icon: '🧪',
    color: '#ea580c',
    gradient: 'linear-gradient(135deg, #f97316, #ea580c)',
    lightBg: 'rgba(249, 115, 22, 0.1)',
    lightSolid: '#ffedd5',
    dark: '#c2410c',
    description: 'Química general y orgánica'
  },
  ciencias: {
    name: 'Ciencias',
    icon: '🌍',
    color: '#22c55e',
    gradient: 'linear-gradient(135deg, #22c55e, #16a34a)',
    lightBg: 'rgba(34, 197, 94, 0.1)',
    lightSolid: '#dcfce7',
    dark: '#166534',
    description: 'Biología y ciencias naturales'
  }
};

/**
 * Obtiene la configuración de una materia por su slug
 */
export function getMateriaConfig(slug: string): MateriaConfig {
  return materiaConfig[slug as MateriaSlug] || materiaConfig.fisica;
}

/**
 * Obtiene el icono de una materia
 */
export function getMateriaIcon(slug: string): string {
  return getMateriaConfig(slug).icon;
}

/**
 * Obtiene el color de una materia
 */
export function getMateriaColor(slug: string): string {
  return getMateriaConfig(slug).color;
}

/**
 * Obtiene el nombre con tilde de una materia
 */
export function getMateriaName(slug: string): string {
  return getMateriaConfig(slug).name;
}

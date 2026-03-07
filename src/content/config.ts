import { defineCollection, z } from 'astro:content';

const lessonsSchema = z.object({
  title: z.string().optional(),
  description: z.string().optional(),
  order: z.number().optional(),
  draft: z.boolean().optional().default(false),
});

// Schema específico para talleres ICFES (Saber)
const saberSchema = z.object({
  title: z.string().optional(),
  area: z.string().optional(),
  unidad: z.string().optional(),
  fuente: z.string().optional(),
  anio: z.union([z.string(), z.number()]).optional(),
  print_title: z.string().optional(),
  print_source: z.string().optional(),
  print_year: z.union([z.string(), z.number()]).optional(),
  total_preguntas: z.number().optional(),
  access: z.enum(['free', 'premium', 'public', 'paid']).optional(),
  tier: z.enum(['free', 'premium', 'public', 'paid']).optional(),
  access_tier: z.enum(['free', 'premium', 'public', 'paid']).optional(),
  draft: z.boolean().optional().default(true), // Por defecto en draft
});

const matematicasCollection = defineCollection({
  type: 'content',
  schema: lessonsSchema,
});

const fisicaCollection = defineCollection({
  type: 'content',
  schema: lessonsSchema,
});

const quimicaCollection = defineCollection({
  type: 'content',
  schema: lessonsSchema,
});

const cienciasCollection = defineCollection({
  type: 'content',
  schema: lessonsSchema,
});

const saberCollection = defineCollection({
  type: 'content',
  schema: saberSchema,
});

const simulacrosCollection = defineCollection({
  type: 'content',
  schema: saberSchema,
});

export const collections = {
  'matematicas': matematicasCollection,
  'fisica': fisicaCollection,
  'quimica': quimicaCollection,
  'ciencias': cienciasCollection,
  'saber': saberCollection,
  'simulacros': simulacrosCollection,
};

/**
 * Utilidad para cargar navegación contextual (colapsada por nivel)
 * Usada por CollapsibleSidebar y MobileMenu para evitar duplicación
 */

import { getCollection } from 'astro:content';
import { buildNavigationFromLessonsWithCollection, mergeNavigations, cleanSegment } from './navigation-generator.js';
import { allMeta } from './load-meta';

import { MATERIAS_SLUGS, type MateriaSlug } from '../config/materias';
export const MATERIAS_LIST = MATERIAS_SLUGS;
export type MateriaKey = MateriaSlug;

export interface MateriaStats {
  name: string;
  count: number;
}

export interface NavigationContext {
  navigation: Record<string, any>;
  materiaStats: Record<string, MateriaStats>;
  currentMateriaKey: string;
  currentUnidadSlug: string;
  currentBloqueSlug: string;
  isMateriaActive: (materiaKey: string) => boolean;
  isUnidadActive: (unidadKey: string) => boolean;
  isBloqueActive: (bloqueKey: string) => boolean;
}

/**
 * Carga la navegación contextual para una ruta dada.
 * Solo carga en detalle la materia actual, las demás solo muestran stats.
 */
export async function loadContextualNavigation(currentPath: string): Promise<NavigationContext> {
  // Parsear la ruta actual
  const pathParts = currentPath.split('/').filter(Boolean).map(part => decodeURIComponent(part));
  const currentMateriaKey = pathParts[0] || '';
  const currentUnidadSlug = pathParts[1] || '';
  const currentBloqueSlug = pathParts[2] || '';

  let navigation: Record<string, any> = {};
  let materiaStats: Record<string, MateriaStats> = {};

  // Cargar todas las materias pero solo expandir la actual
  for (const materiaKey of MATERIAS_LIST) {
    try {
      const collection = await getCollection(materiaKey);
      if (collection.length > 0) {
        const navData = buildNavigationFromLessonsWithCollection(collection, materiaKey, allMeta);
        
        // Solo cargar estructura completa de la materia actual
        if (materiaKey === currentMateriaKey) {
          navigation = mergeNavigations(navigation, navData);
        }
        
        // Guardar stats para todas las materias
        const materiaNav = navData[materiaKey];
        if (materiaNav) {
          const count = Object.values(materiaNav.unidades).reduce((acc: number, unidad: any) => {
            return acc + Object.values(unidad.bloques).reduce((acc2: number, bloque: any) => acc2 + bloque.lecciones.length, 0);
          }, 0);
          materiaStats[materiaKey] = { name: materiaNav.name, count };
        }
      }
    } catch (e) {
      // Silenciar errores de colecciones vacías
    }
  }

  // Funciones helper usando cleanSegment para comparar keys con prefijos vs slugs limpios
  const isMateriaActive = (materiaKey: string) => currentPath.startsWith(`/${materiaKey}`);
  const isUnidadActive = (unidadKey: string) => cleanSegment(unidadKey) === currentUnidadSlug;
  const isBloqueActive = (bloqueKey: string) => cleanSegment(bloqueKey) === currentBloqueSlug;

  return {
    navigation,
    materiaStats,
    currentMateriaKey,
    currentUnidadSlug,
    currentBloqueSlug,
    isMateriaActive,
    isUnidadActive,
    isBloqueActive,
  };
}

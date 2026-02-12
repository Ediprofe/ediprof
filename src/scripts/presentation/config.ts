/**
 * Configuración centralizada del Modo Presentación
 *
 * Todas las constantes, colores y configuraciones van aquí.
 * NUNCA hardcodear estos valores en otros archivos.
 */

// ============================================
// COLORES DE HERRAMIENTAS
// ============================================

export const TOOL_COLORS = {
  white: '#FFFFFF',
  yellow: '#FFD700',
  red: '#EF4444',
  blue: '#3B82F6',
  black: '#111111',
  neonGreen: '#00FF99',
} as const;

// Array ordenado para UI (dock) y atajos de teclado
export const COLOR_PALETTE = [
  { key: '1', hex: TOOL_COLORS.white, name: 'Blanco' },
  { key: '2', hex: TOOL_COLORS.yellow, name: 'Amarillo' },
  { key: '3', hex: TOOL_COLORS.red, name: 'Rojo' },
  { key: '4', hex: TOOL_COLORS.blue, name: 'Azul' },
  { key: '5', hex: TOOL_COLORS.black, name: 'Negro' },
  { key: '6', hex: TOOL_COLORS.neonGreen, name: 'Verde Neón' },
] as const;

// ============================================
// COLORES DE UI
// ============================================

export const UI_COLORS = {
  laser: '#FF0000',
  guide: '#06b6d4',
  laserButton: '#ef4444',
  penButton: '#eab308',
  arrowButton: '#10b981',
  rectButton: '#6366f1',
  selectButton: '#8b5cf6',
  highlighterButton: '#facc15',
  selection: 'rgba(59, 130, 246, 0.5)',
  selectionFill: 'rgba(59, 130, 246, 0.2)',
  primary: '#2563eb',
} as const;

// ============================================
// CONFIGURACIÓN DE TIEMPOS
// ============================================

export const TIMING = {
  /** Duración del efecto láser antes de desvanecerse (ms) */
  laserFadeDuration: 3000,
  /** Transición de opacidad del board (ms) */
  boardTransition: 300,
} as const;

// ============================================
// Z-INDEX (capas de UI)
// ============================================

export const Z_INDEX = {
  /** Board de fondo (pizarra blanca/negra) */
  board: 999999997,
  /** Canvas de dibujo */
  canvas: 999999998,
  /** Dock de herramientas (máximo permitido por navegadores) */
  dock: 2147483647,
} as const;

// ============================================
// ATAJOS DE TECLADO
// ============================================

export const KEYBOARD_SHORTCUTS = {
  tools: {
    'h': 'hand',
    'l': 'laser',
    'p': 'pen',
    'm': 'highlighter',
    's': 'select',
    'a': 'arrow',
    'r': 'rect',
    't': 'text',
    'g': 'guide',
  },
  boards: {
    'b': 'black',
    'w': 'white',
  },
  actions: {
    'escape': 'close',
    'c': 'clear',
  },
} as const;

// ============================================
// TAMAÑOS Y DIMENSIONES
// ============================================

export const SIZES = {
  /** Ancho de línea para trazos permanentes */
  strokeWidth: 4,
  /** Ancho de línea para resaltador */
  highlighterWidth: 24,
  /** Tamaño de la cabeza de flecha */
  arrowHeadLength: 15,
  /** Radio del arco de selección */
  selectionStrokeWidth: 2,
} as const;

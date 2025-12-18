"""
🎨 Colors - Paleta de colores unificada para todas las ilustraciones

IMPORTANTE: Este es el ÚNICO lugar donde se definen colores.
Todos los renderers deben importar de aquí.

Uso:
    from core.colors import COLORS
    # o
    from core import COLORS
"""

# ============================================================================
# PALETA DE COLORES ESTÁNDAR
# ============================================================================

COLORS = {
    # === FONDOS ===
    'background': '#f8fafc',
    'background_dark': '#1e293b',
    
    # === COLORES SEMÁNTICOS (usar estos para consistencia) ===
    'primary': '#3b82f6',        # Azul - figuras principales
    'secondary': '#22c55e',      # Verde - elementos secundarios
    'accent': '#ef4444',         # Rojo - puntos notables, destacados
    'highlight': '#f97316',      # Naranja - énfasis
    'purple': '#8b5cf6',         # Púrpura - diámetros, bisectrices
    'pink': '#ec4899',           # Rosa - tangentes, mediatrices
    'teal': '#14b8a6',           # Verde azulado - secantes
    'yellow': '#fbbf24',         # Amarillo - resaltados
    
    # === CIRCUNFERENCIAS ===
    'circle_stroke': '#3b82f6',
    'circle_fill': '#dbeafe',
    'radius': '#ef4444',
    'diameter': '#8b5cf6',
    'chord': '#22c55e',
    'arc': '#f97316',
    'sector_fill': '#dcfce7',
    'segment_fill': '#fef3c7',
    'tangent': '#ec4899',
    'secant': '#14b8a6',
    'crown': '#e0e7ff',
    
    # === TRIÁNGULOS ===
    'triangle_fill': '#f8fafc',
    'triangle_stroke': '#1e293b',
    'medianas': '#22c55e',
    'alturas': '#f97316',
    'bisectrices': '#8b5cf6',
    'mediatrices': '#ec4899',
    'punto_notable': '#ef4444',
    
    # === GEOMETRÍA ANALÍTICA ===
    'axis': '#64748b',           # Ejes coordenados
    'grid': '#e2e8f0',           # Cuadrícula
    'point': '#ef4444',          # Puntos
    'center': '#ef4444',         # Centro (alias de point)
    'segment': '#3b82f6',        # Segmentos
    'line': '#22c55e',           # Rectas
    'polygon_fill': '#dbeafe',   # Relleno de polígonos
    'polygon_stroke': '#3b82f6', # Borde de polígonos
    'auxiliary': '#94a3b8',      # Líneas auxiliares (punteadas)
    'formula_bg': '#fef3c7',     # Fondo de fórmulas
    
    # === TEXTO ===
    'text': '#1e293b',
    'text_light': '#64748b',
    'vertices': '#1e293b',
    
    # === ÁNGULOS ===
    'angle': '#f97316',
    'angle_fill': '#fed7aa',
    
    # === CÍRCULO UNITARIO (cuadrantes) ===
    'quadrant_I': '#22c55e',
    'quadrant_II': '#3b82f6',
    'quadrant_III': '#f97316',
    'quadrant_IV': '#ec4899',
    'cos_color': '#3b82f6',
    'sin_color': '#ef4444',
}


# Alias para compatibilidad con código existente
def get_color(name: str, default: str = '#000000') -> str:
    """Obtiene un color por nombre, con fallback."""
    return COLORS.get(name, default)

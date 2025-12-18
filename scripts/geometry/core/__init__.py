"""
📐 Core - Módulo base para renderizado de geometría

Contiene clases y utilidades compartidas por todos los renderers.

Uso:
    from core import COLORS, Point, SVGBuilder
    from core import escape_xml, point_on_circle
    from core import SIZE_SIMPLE, get_canvas_config
"""

# === Estructuras de datos ===
from .base import Point, ValidationResult

# === Colores (fuente única de verdad) ===
from .colors import COLORS, get_color

# === Tamaños de canvas ===
from .canvas import (
    SIZE_SIMPLE, SIZE_COMPOUND, SIZE_MULTIPLE, SIZE_HORIZONTAL, 
    SIZE_CARTESIAN, SIZE_SQUARE,
    CanvasSize, CANVAS_CONFIGS,
    get_canvas_config, get_canvas_dimensions
)

# === Primitivas y helpers ===
from .primitives import (
    escape_xml, escape_svg_text,
    point_on_circle, point_on_circle_svg, arc_path,
    format_number, format_coord, format_angle,
    distance, midpoint, lerp, clamp,
    svg_translate, svg_rotate, svg_scale
)

# === Builders ===
from .svg_builder import SVGBuilder
from .coordinate_system import CoordinateSystem


__all__ = [
    # Estructuras
    'Point', 'ValidationResult',
    
    # Colores
    'COLORS', 'get_color',
    
    # Canvas
    'SIZE_SIMPLE', 'SIZE_COMPOUND', 'SIZE_MULTIPLE', 'SIZE_HORIZONTAL',
    'SIZE_CARTESIAN', 'SIZE_SQUARE',
    'CanvasSize', 'CANVAS_CONFIGS',
    'get_canvas_config', 'get_canvas_dimensions',
    
    # Primitivas
    'escape_xml', 'escape_svg_text',
    'point_on_circle', 'point_on_circle_svg', 'arc_path',
    'format_number', 'format_coord', 'format_angle',
    'distance', 'midpoint', 'lerp', 'clamp',
    'svg_translate', 'svg_rotate', 'svg_scale',
    
    # Builders
    'SVGBuilder', 'CoordinateSystem',
]

"""
📐 Base - Clases y constantes fundamentales para geometría

Este módulo contiene las estructuras de datos básicas y la paleta de colores
que se comparten entre todos los renderers de geometría.
"""

import math
from dataclasses import dataclass, field
from typing import List, Tuple
from enum import Enum


# ============================================================================
# PALETA DE COLORES ESTÁNDAR
# ============================================================================

COLORS = {
    # Fondos
    'background': '#f8fafc',
    'background_dark': '#1e293b',
    
    # Elementos geométricos
    'primary': '#3b82f6',        # Azul - figuras principales
    'secondary': '#22c55e',      # Verde - elementos secundarios
    'accent': '#ef4444',         # Rojo - puntos notables, altura
    'highlight': '#f97316',      # Naranja - destacados
    
    # Circunferencias
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
    
    # Triángulos
    'triangle_fill': '#f8fafc',
    'triangle_stroke': '#1e293b',
    'medianas': '#22c55e',
    'alturas': '#f97316',
    'bisectrices': '#8b5cf6',
    'mediatrices': '#ec4899',
    'punto_notable': '#ef4444',
    
    # Geometría analítica
    'axis': '#64748b',           # Ejes coordenados
    'grid': '#e2e8f0',           # Cuadrícula
    'point': '#ef4444',          # Puntos
    'segment': '#3b82f6',        # Segmentos
    'line': '#22c55e',           # Rectas
    'polygon_fill': '#dbeafe',   # Relleno de polígonos
    'polygon_stroke': '#3b82f6', # Borde de polígonos
    'auxiliary': '#94a3b8',      # Líneas auxiliares (punteadas)
    'formula_bg': '#fef3c7',     # Fondo de fórmulas
    
    # Texto
    'text': '#1e293b',
    'text_light': '#64748b',
    'vertices': '#1e293b',
    
    # Ángulos
    'angle': '#f97316',
    'angle_fill': '#fed7aa',
}


# ============================================================================
# TAMAÑOS DE CANVAS
# ============================================================================

class CanvasSize(Enum):
    """Tamaños estándar de canvas."""
    SIMPLE = "simple"           # 500x400 - 1 concepto
    COMPOUND = "compound"       # 600x460 - 2-3 elementos
    MULTIPLE = "multiple"       # 750x450 - 4+ elementos
    HORIZONTAL = "horizontal"   # 750x420 - Operaciones lado a lado
    CARTESIAN = "cartesian"     # 600x500 - Plano cartesiano


CANVAS_CONFIGS = {
    CanvasSize.SIMPLE.value: {
        'width': 500,
        'height': 400,
        'padding': 40
    },
    CanvasSize.COMPOUND.value: {
        'width': 600,
        'height': 460,
        'padding': 40
    },
    CanvasSize.MULTIPLE.value: {
        'width': 750,
        'height': 450,
        'padding': 40
    },
    CanvasSize.HORIZONTAL.value: {
        'width': 750,
        'height': 420,
        'padding': 40
    },
    CanvasSize.CARTESIAN.value: {
        'width': 600,
        'height': 500,
        'padding': 50
    }
}


# ============================================================================
# ESTRUCTURAS DE DATOS
# ============================================================================

@dataclass
class Point:
    """Punto 2D con operaciones vectoriales."""
    x: float
    y: float
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)
    
    def length(self) -> float:
        """Longitud del vector desde el origen."""
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_to(self, other: 'Point') -> float:
        """Distancia a otro punto."""
        return (self - other).length()
    
    def normalize(self) -> 'Point':
        """Vector unitario en la misma dirección."""
        l = self.length()
        if l == 0:
            return Point(0, 0)
        return Point(self.x / l, self.y / l)
    
    def midpoint(self, other: 'Point') -> 'Point':
        """Punto medio entre este punto y otro."""
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)
    
    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)
    
    def rotate(self, angle_deg: float, center: 'Point' = None) -> 'Point':
        """Rota el punto alrededor de un centro."""
        if center is None:
            center = Point(0, 0)
        
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        # Trasladar al origen
        dx = self.x - center.x
        dy = self.y - center.y
        
        # Rotar
        new_x = dx * cos_a - dy * sin_a
        new_y = dx * sin_a + dy * cos_a
        
        # Trasladar de vuelta
        return Point(new_x + center.x, new_y + center.y)
    
    @classmethod
    def from_polar(cls, r: float, angle_deg: float, center: 'Point' = None) -> 'Point':
        """Crea un punto desde coordenadas polares."""
        if center is None:
            center = Point(0, 0)
        
        angle_rad = math.radians(angle_deg)
        x = center.x + r * math.cos(angle_rad)
        y = center.y + r * math.sin(angle_rad)
        return cls(x, y)


@dataclass
class ValidationResult:
    """Resultado de validación de una especificación."""
    valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    
    def add_error(self, msg: str):
        self.errors.append(msg)
        self.valid = False
    
    def add_warning(self, msg: str):
        self.warnings.append(msg)


# ============================================================================
# UTILIDADES
# ============================================================================

def escape_xml(text: str) -> str:
    """Escapa caracteres especiales para XML/SVG."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

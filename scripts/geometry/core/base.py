"""
📐 Base - Clases y estructuras de datos fundamentales para geometría

Este módulo contiene las estructuras de datos básicas.
Para colores, usar: from core.colors import COLORS
Para canvas, usar: from core.canvas import SIZE_SIMPLE, etc.

NOTA: COLORS y CanvasSize se re-exportan aquí para compatibilidad hacia atrás.
"""

import math
from dataclasses import dataclass, field
from typing import List, Tuple

# Re-exportar para compatibilidad hacia atrás
from .colors import COLORS
from .canvas import CanvasSize, CANVAS_CONFIGS


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
# UTILIDADES (re-exportadas de primitives para compatibilidad)
# ============================================================================

from .primitives import escape_xml

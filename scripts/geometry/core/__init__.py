"""
📐 Core - Módulo base para renderizado de geometría

Contiene clases y utilidades compartidas por todos los renderers.
"""

from .base import Point, COLORS, ValidationResult
from .svg_builder import SVGBuilder
from .coordinate_system import CoordinateSystem

__all__ = ['Point', 'COLORS', 'ValidationResult', 'SVGBuilder', 'CoordinateSystem']

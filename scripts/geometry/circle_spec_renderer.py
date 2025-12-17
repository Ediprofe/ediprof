#!/usr/bin/env python3
"""
📐 Circle Spec Renderer - Sistema de Geometría Exacta para Circunferencias

Motor de renderizado basado en especificaciones JSON con cálculos exactos usando SymPy.

Principio Fundamental:
    - La IA genera un spec JSON declarativo
    - SymPy calcula coordenadas exactas
    - El renderer genera SVG validado

Uso:
    python scripts/geometry/circle_spec_renderer.py --spec ARCHIVO.json --output ARCHIVO.svg
    python scripts/geometry/circle_spec_renderer.py --spec ARCHIVO.json --validate-only
    python scripts/geometry/circle_spec_renderer.py --batch specs/geometria/circulos/

Referencia: .agent/workflows/geometry-exact.md
"""

import argparse
import json
import math
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum

# ============================================================================
# SYMPY PARA CÁLCULOS EXACTOS
# ============================================================================

try:
    from sympy import Point as SymPoint, Circle as SymCircle, Line, Segment
    from sympy import sqrt, Rational, pi, cos, sin, atan2, N
    from sympy.geometry import Point2D
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False
    print("⚠️  SymPy no está instalado. Instalar con: pip install sympy")


# ============================================================================
# CONFIGURACIÓN CENTRALIZADA
# ============================================================================

class CanvasSize(Enum):
    """Tamaños estándar de canvas."""
    SIMPLE = "simple"           # 500x400 - 1 concepto
    COMPOUND = "compound"       # 600x460 - 2-3 elementos
    MULTIPLE = "multiple"       # 750x450 - 4+ elementos
    HORIZONTAL = "horizontal"   # 750x420 - Operaciones lado a lado


# Configuración de tamaños
CANVAS_CONFIGS = {
    CanvasSize.SIMPLE.value: {
        'width': 500,
        'height': 400,
        'circle_center': (250, 175),
        'circle_radius': 110,
        'title_y': 30,
        'legend_y': 305,
        'legend_height': 35,
        'padding': 40
    },
    CanvasSize.COMPOUND.value: {
        'width': 600,
        'height': 460,
        'circle_center': (300, 200),
        'circle_radius': 120,
        'title_y': 30,
        'legend_y': 385,
        'legend_height': 55,
        'padding': 40
    },
    CanvasSize.MULTIPLE.value: {
        'width': 750,
        'height': 450,
        'circle_center': (375, 200),
        'circle_radius': 100,
        'title_y': 28,
        'legend_y': 380,
        'legend_height': 50,
        'padding': 40
    },
    CanvasSize.HORIZONTAL.value: {
        'width': 750,
        'height': 420,
        'circle_center': (375, 190),
        'circle_radius': 85,
        'title_y': 28,
        'legend_y': 320,
        'legend_height': 85,
        'padding': 40
    }
}

# Paleta de colores estándar
COLORS = {
    'background': '#f8fafc',
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
    'angle': '#f97316',
    'point': '#1e293b',
    'center': '#ef4444',
    'text': '#1e293b',
    'auxiliary': '#94a3b8',
    'highlight': '#fbbf24',
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
    
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        l = self.length()
        if l == 0:
            return Point(0, 0)
        return Point(self.x / l, self.y / l)
    
    def to_tuple(self):
        return (self.x, self.y)
    
    @classmethod
    def from_sympy(cls, sym_point):
        """Convierte un punto SymPy a Point."""
        return cls(float(N(sym_point.x)), float(N(sym_point.y)))


@dataclass
class ValidationResult:
    """Resultado de validación."""
    valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


# ============================================================================
# CÁLCULOS GEOMÉTRICOS CON SYMPY
# ============================================================================

class CircleGeometry:
    """Cálculos geométricos exactos para circunferencias usando SymPy."""
    
    def __init__(self, center: Tuple[float, float], radius: float):
        self.center = SymPoint(center[0], center[1])
        self.radius = radius
        self.circle = SymCircle(self.center, radius)
    
    def point_on_circle(self, angle_deg: float) -> Point:
        """
        Calcula un punto en la circunferencia dado un ángulo.
        
        Args:
            angle_deg: Ángulo en grados (0° = derecha, 90° = arriba en coords matemáticas)
        
        Returns:
            Point en la circunferencia
        
        NOTA: En SVG, Y crece hacia abajo, por eso usamos -sin()
        """
        angle_rad = math.radians(angle_deg)
        x = float(self.center.x) + self.radius * math.cos(angle_rad)
        y = float(self.center.y) - self.radius * math.sin(angle_rad)  # Negativo para SVG
        return Point(x, y)
    
    def chord_from_angles(self, angle1: float, angle2: float) -> Tuple[Point, Point]:
        """Calcula los extremos de una cuerda dados dos ángulos."""
        p1 = self.point_on_circle(angle1)
        p2 = self.point_on_circle(angle2)
        return (p1, p2)
    
    def arc_path(self, start_deg: float, end_deg: float, large_arc: bool = None) -> str:
        """
        Genera el path SVG para un arco.
        
        Args:
            start_deg: Ángulo inicial en grados
            end_deg: Ángulo final en grados
            large_arc: Forzar arco grande/pequeño (None = automático)
        """
        start = self.point_on_circle(start_deg)
        end = self.point_on_circle(end_deg)
        
        # Determinar si es arco grande (>180°)
        arc_span = (end_deg - start_deg) % 360
        if large_arc is None:
            large_arc = 1 if arc_span > 180 else 0
        else:
            large_arc = 1 if large_arc else 0
        
        # sweep-flag: 0 para sentido antihorario visual en SVG
        sweep = 0
        
        return f"M {start.x:.2f} {start.y:.2f} A {self.radius} {self.radius} 0 {large_arc} {sweep} {end.x:.2f} {end.y:.2f}"
    
    def sector_path(self, start_deg: float, end_deg: float) -> str:
        """Genera el path SVG para un sector circular."""
        start = self.point_on_circle(start_deg)
        end = self.point_on_circle(end_deg)
        cx, cy = float(self.center.x), float(self.center.y)
        
        arc_span = (end_deg - start_deg) % 360
        large_arc = 1 if arc_span > 180 else 0
        
        return f"M {cx:.2f} {cy:.2f} L {start.x:.2f} {start.y:.2f} A {self.radius} {self.radius} 0 {large_arc} 0 {end.x:.2f} {end.y:.2f} Z"
    
    def segment_path(self, start_deg: float, end_deg: float) -> str:
        """Genera el path SVG para un segmento circular (arco + cuerda)."""
        start = self.point_on_circle(start_deg)
        end = self.point_on_circle(end_deg)
        
        arc_span = (end_deg - start_deg) % 360
        large_arc = 1 if arc_span > 180 else 0
        
        return f"M {start.x:.2f} {start.y:.2f} A {self.radius} {self.radius} 0 {large_arc} 0 {end.x:.2f} {end.y:.2f} Z"
    
    def tangent_point(self, external_point: Tuple[float, float]) -> List[Point]:
        """
        Calcula los puntos de tangencia desde un punto externo.
        
        Usa SymPy para cálculo exacto.
        """
        if not SYMPY_AVAILABLE:
            raise RuntimeError("SymPy requerido para cálculos de tangencia")
        
        P = SymPoint(external_point[0], external_point[1])
        
        # Distancia del punto externo al centro
        d = float(P.distance(self.center))
        
        if d <= self.radius:
            return []  # Punto interior o en la circunferencia
        
        # Ángulo del centro al punto externo
        dx = float(P.x - self.center.x)
        dy = float(P.y - self.center.y)
        angle_to_P = math.atan2(-dy, dx)  # Negativo por coordenadas SVG
        
        # Ángulo del triángulo rectángulo
        alpha = math.acos(self.radius / d)
        
        # Dos puntos de tangencia
        angle1 = angle_to_P + alpha
        angle2 = angle_to_P - alpha
        
        return [
            self.point_on_circle(math.degrees(angle1)),
            self.point_on_circle(math.degrees(angle2))
        ]
    
    def get_label_position(self, angle_deg: float, offset: float = 20, direction: str = "outward") -> Point:
        """
        Calcula la posición óptima para una etiqueta.
        
        Args:
            angle_deg: Ángulo del elemento
            offset: Distancia desde el elemento
            direction: "outward" (fuera del círculo) o "inward" (dentro)
        """
        point = self.point_on_circle(angle_deg)
        cx, cy = float(self.center.x), float(self.center.y)
        
        # Vector desde el centro hacia el punto
        dx = point.x - cx
        dy = point.y - cy
        length = math.sqrt(dx**2 + dy**2)
        
        if length == 0:
            return point
        
        # Normalizar y aplicar offset
        factor = offset / length
        if direction == "outward":
            return Point(point.x + dx * factor, point.y + dy * factor)
        else:
            return Point(point.x - dx * factor, point.y - dy * factor)


# ============================================================================
# VALIDACIÓN
# ============================================================================

class SpecValidator:
    """Validador de especificaciones CircleSpec."""
    
    REQUIRED_FIELDS = ['tipo', 'canvas']
    VALID_TIPOS = [
        'elemento-radio', 'elemento-diametro', 'elemento-cuerda', 
        'elemento-arco', 'elemento-sector', 'elemento-segmento',
        'elemento-corona', 'posiciones-punto', 'posiciones-circunferencias',
        'angulo-central', 'angulo-inscrito', 'angulo-exterior',
        'teorema', 'formula'
    ]
    
    @classmethod
    def validate(cls, spec: dict) -> ValidationResult:
        """Valida una especificación completa."""
        errors = []
        warnings = []
        
        # Campos requeridos
        for field in cls.REQUIRED_FIELDS:
            if field not in spec:
                errors.append(f"Campo requerido faltante: '{field}'")
        
        # Tipo válido
        tipo = spec.get('tipo', '')
        if tipo and tipo not in cls.VALID_TIPOS:
            warnings.append(f"Tipo '{tipo}' no está en la lista de tipos conocidos")
        
        # Validar canvas
        canvas = spec.get('canvas', {})
        if isinstance(canvas, str):
            if canvas not in CANVAS_CONFIGS:
                errors.append(f"Canvas preset '{canvas}' no existe. Usar: {list(CANVAS_CONFIGS.keys())}")
        elif isinstance(canvas, dict):
            if 'width' not in canvas or 'height' not in canvas:
                errors.append("Canvas debe tener 'width' y 'height'")
        
        # Validar circunferencia
        circ = spec.get('circunferencia', {})
        if circ:
            if 'centro' not in circ and 'radio' not in circ:
                warnings.append("Circunferencia sin centro/radio usará valores por defecto")
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    @classmethod
    def validate_bounds(cls, elements: List[dict], width: int, height: int, padding: int = 10) -> ValidationResult:
        """Valida que todos los elementos estén dentro del canvas."""
        errors = []
        warnings = []
        
        for elem in elements:
            x = elem.get('x', 0)
            y = elem.get('y', 0)
            
            if x < padding or x > width - padding:
                warnings.append(f"Elemento en x={x:.1f} cerca del borde horizontal")
            if y < padding or y > height - padding:
                warnings.append(f"Elemento en y={y:.1f} cerca del borde vertical")
            
            if x < 0 or x > width:
                errors.append(f"Elemento fuera del canvas: x={x:.1f}")
            if y < 0 or y > height:
                errors.append(f"Elemento fuera del canvas: y={y:.1f}")
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )


# ============================================================================
# UTILIDADES SVG
# ============================================================================

def escape_svg_text(text: str) -> str:
    """
    Escapa caracteres especiales XML para texto en SVG.
    
    CRÍTICO: Los caracteres <, >, & son inválidos en XML.
    """
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def svg_text(x: float, y: float, text: str, size: int = 12, weight: str = "normal", 
             color: str = None, anchor: str = "start") -> str:
    """Genera elemento de texto SVG con escape automático."""
    color = color or COLORS['text']
    safe_text = escape_svg_text(text)
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{color}">{safe_text}</text>'


def svg_circle(cx: float, cy: float, r: float, fill: str = "none", 
               stroke: str = None, stroke_width: float = 2, opacity: float = 1) -> str:
    """Genera elemento círculo SVG."""
    stroke = stroke or COLORS['circle_stroke']
    opacity_attr = f' fill-opacity="{opacity}"' if opacity < 1 else ''
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{opacity_attr}/>'


def svg_line(x1: float, y1: float, x2: float, y2: float, 
             stroke: str = None, stroke_width: float = 2, dashed: bool = False) -> str:
    """Genera elemento línea SVG."""
    stroke = stroke or COLORS['auxiliary']
    dash_attr = ' stroke-dasharray="4,3"' if dashed else ''
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{stroke_width}"{dash_attr}/>'


def svg_path(d: str, fill: str = "none", stroke: str = None, stroke_width: float = 2) -> str:
    """Genera elemento path SVG."""
    stroke = stroke or COLORS['arc']
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'


def svg_rect(x: float, y: float, width: float, height: float, 
             fill: str = "white", stroke: str = None, rx: float = 8) -> str:
    """Genera elemento rectángulo SVG."""
    stroke = stroke or COLORS['auxiliary']
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{width}" height="{height}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'


# ============================================================================
# RENDERER PRINCIPAL
# ============================================================================

class CircleSpecRenderer:
    """
    Renderizador de especificaciones CircleSpec.
    
    Flujo:
        1. Cargar spec JSON
        2. Validar spec
        3. Calcular geometría con SymPy
        4. Generar SVG
        5. Validar bounds
        6. Guardar archivo
    """
    
    def __init__(self, spec: dict):
        self.spec = spec
        self.errors = []
        self.warnings = []
        
        # Configurar canvas
        canvas = spec.get('canvas', 'simple')
        if isinstance(canvas, str):
            self.config = CANVAS_CONFIGS.get(canvas, CANVAS_CONFIGS['simple']).copy()
        else:
            self.config = {
                'width': canvas.get('width', 500),
                'height': canvas.get('height', 400),
                'padding': canvas.get('padding', 40)
            }
            # Calcular centro si no está especificado
            self.config['circle_center'] = (
                self.config['width'] // 2,
                self.config['height'] // 2 - 25
            )
            self.config['circle_radius'] = min(self.config['width'], self.config['height']) // 4
        
        # Sobrescribir con valores del spec si existen
        circ = spec.get('circunferencia', {})
        if 'centro' in circ:
            self.config['circle_center'] = tuple(circ['centro'])
        if 'radio' in circ:
            self.config['circle_radius'] = circ['radio']
        
        # Inicializar geometría
        self.geometry = CircleGeometry(
            self.config['circle_center'],
            self.config['circle_radius']
        )
        
        self.svg_elements = []
        self.label_positions = []  # Para detección de colisiones
    
    def render(self) -> str:
        """Renderiza la especificación a SVG."""
        self.svg_elements = []
        
        width = self.config['width']
        height = self.config['height']
        
        # Header SVG
        self.svg_elements.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'style="font-family: \'Inter\', \'Segoe UI\', system-ui, sans-serif;">'
        )
        
        # Fondo
        self.svg_elements.append(
            f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>'
        )
        
        # Título
        if 'titulo' in self.spec:
            self._render_title()
        
        # Renderizar según tipo
        tipo = self.spec.get('tipo', '')
        
        if tipo.startswith('elemento-'):
            self._render_elemento()
        elif tipo.startswith('posiciones-'):
            self._render_posiciones()
        elif tipo.startswith('angulo-'):
            self._render_angulo()
        elif tipo == 'teorema':
            self._render_teorema()
        elif tipo == 'formula':
            self._render_formula()
        else:
            # Renderizado genérico
            self._render_generic()
        
        # Footer SVG
        self.svg_elements.append('</svg>')
        
        return '\n'.join(self.svg_elements)
    
    def _render_title(self):
        """Renderiza el título."""
        title = self.spec.get('titulo', '')
        color = self.spec.get('titulo_color', COLORS['text'])
        y = self.config.get('title_y', 30)
        
        self.svg_elements.append(
            svg_text(self.config['width'] / 2, y, title, 18, "bold", color, "middle")
        )
    
    def _render_elemento(self):
        """Renderiza un elemento de la circunferencia (radio, cuerda, arco, etc.)."""
        tipo = self.spec.get('tipo', '')
        elemento = self.spec.get('elemento', {})
        
        cx, cy = self.config['circle_center']
        r = self.config['circle_radius']
        
        # Circunferencia base
        self.svg_elements.append(
            svg_circle(cx, cy, r, "none", COLORS['circle_stroke'])
        )
        
        # Centro
        self.svg_elements.append(
            svg_circle(cx, cy, 3, COLORS['center'], COLORS['center'])
        )
        self.svg_elements.append(
            svg_text(cx + 8, cy + 5, "O", 11, "normal", COLORS['auxiliary'])
        )
        
        # Renderizar elemento específico
        if tipo == 'elemento-radio':
            self._render_radio(elemento)
        elif tipo == 'elemento-diametro':
            self._render_diametro(elemento)
        elif tipo == 'elemento-cuerda':
            self._render_cuerda(elemento)
        elif tipo == 'elemento-arco':
            self._render_arco(elemento)
        elif tipo == 'elemento-sector':
            self._render_sector(elemento)
        elif tipo == 'elemento-segmento':
            self._render_segmento(elemento)
        
        # Leyenda
        if 'leyenda' in self.spec:
            self._render_leyenda()
    
    def _render_radio(self, config: dict):
        """Renderiza un radio."""
        angulo = config.get('angulo', 45)
        color = config.get('color', COLORS['radius'])
        etiqueta = config.get('etiqueta', 'r')
        
        cx, cy = self.config['circle_center']
        punto = self.geometry.point_on_circle(angulo)
        
        # Línea del radio
        self.svg_elements.append(
            svg_line(cx, cy, punto.x, punto.y, color, 3)
        )
        
        # Punto en la circunferencia
        self.svg_elements.append(
            svg_circle(punto.x, punto.y, 4, color, color)
        )
        
        # Etiqueta del radio (en el punto medio)
        mid = Point((cx + punto.x) / 2, (cy + punto.y) / 2)
        label_pos = self.geometry.get_label_position(angulo, -15, "inward")
        self.svg_elements.append(
            svg_text(label_pos.x, label_pos.y, etiqueta, 14, "bold", color, "middle")
        )
    
    def _render_diametro(self, config: dict):
        """Renderiza un diámetro."""
        angulo = config.get('angulo', 30)
        color = config.get('color', COLORS['diameter'])
        
        p1 = self.geometry.point_on_circle(angulo)
        p2 = self.geometry.point_on_circle(angulo + 180)
        
        # Línea del diámetro
        self.svg_elements.append(
            svg_line(p1.x, p1.y, p2.x, p2.y, color, 3)
        )
        
        # Puntos extremos
        self.svg_elements.append(svg_circle(p1.x, p1.y, 4, color, color))
        self.svg_elements.append(svg_circle(p2.x, p2.y, 4, color, color))
        
        # Etiquetas
        label1 = self.geometry.get_label_position(angulo, 15)
        label2 = self.geometry.get_label_position(angulo + 180, 15)
        self.svg_elements.append(svg_text(label1.x, label1.y, "A", 14, "bold", color))
        self.svg_elements.append(svg_text(label2.x, label2.y, "B", 14, "bold", color))
    
    def _render_cuerda(self, config: dict):
        """Renderiza una cuerda."""
        angulo1 = config.get('angulo1', 120)
        angulo2 = config.get('angulo2', 30)
        color = config.get('color', COLORS['chord'])
        
        p1 = self.geometry.point_on_circle(angulo1)
        p2 = self.geometry.point_on_circle(angulo2)
        cx, cy = self.config['circle_center']
        
        # Línea de la cuerda
        self.svg_elements.append(
            svg_line(p1.x, p1.y, p2.x, p2.y, color, 4)
        )
        
        # Puntos extremos
        self.svg_elements.append(svg_circle(p1.x, p1.y, 5, color, color))
        self.svg_elements.append(svg_circle(p2.x, p2.y, 5, color, color))
        
        # Etiquetas
        label1 = self.geometry.get_label_position(angulo1, 15)
        label2 = self.geometry.get_label_position(angulo2, 15)
        self.svg_elements.append(svg_text(label1.x - 10, label1.y - 5, "A", 14, "bold", color))
        self.svg_elements.append(svg_text(label2.x + 5, label2.y - 5, "B", 14, "bold", color))
        
        # Distancia al centro (línea auxiliar)
        mid = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
        self.svg_elements.append(
            svg_line(cx, cy, mid.x, mid.y, COLORS['auxiliary'], 1.5, dashed=True)
        )
        self.svg_elements.append(
            svg_text(mid.x + 15, mid.y + 15, "d", 11, "normal", COLORS['auxiliary'])
        )
    
    def _render_arco(self, config: dict):
        """Renderiza un arco (o arcos mayor/menor)."""
        angulo1 = config.get('angulo1', 120)
        angulo2 = config.get('angulo2', 30)
        mostrar_ambos = config.get('mostrar_ambos', True)
        
        if mostrar_ambos:
            # Arco menor
            path_menor = self.geometry.arc_path(angulo1, angulo2)
            self.svg_elements.append(
                svg_path(path_menor, "none", COLORS['arc'], 5)
            )
            
            # Arco mayor
            path_mayor = self.geometry.arc_path(angulo2, angulo1)
            self.svg_elements.append(
                svg_path(path_mayor, "none", COLORS['auxiliary'], 3)
            )
        else:
            path = self.geometry.arc_path(angulo1, angulo2)
            self.svg_elements.append(
                svg_path(path, "none", config.get('color', COLORS['arc']), 4)
            )
    
    def _render_sector(self, config: dict):
        """Renderiza un sector circular."""
        angulo1 = config.get('angulo1', 90)
        angulo2 = config.get('angulo2', 30)
        color = config.get('color', COLORS['chord'])
        fill = config.get('fill', COLORS['sector_fill'])
        
        cx, cy = self.config['circle_center']
        p1 = self.geometry.point_on_circle(angulo1)
        p2 = self.geometry.point_on_circle(angulo2)
        
        # Sector (path cerrado)
        path = self.geometry.sector_path(angulo1, angulo2)
        self.svg_elements.append(
            f'<path d="{path}" fill="{fill}" stroke="{color}" stroke-width="2"/>'
        )
        
        # Radios
        self.svg_elements.append(svg_line(cx, cy, p1.x, p1.y, color, 2))
        self.svg_elements.append(svg_line(cx, cy, p2.x, p2.y, color, 2))
        
        # Puntos
        self.svg_elements.append(svg_circle(p1.x, p1.y, 4, color, color))
        self.svg_elements.append(svg_circle(p2.x, p2.y, 4, color, color))
    
    def _render_segmento(self, config: dict):
        """Renderiza un segmento circular."""
        angulo1 = config.get('angulo1', 120)
        angulo2 = config.get('angulo2', 60)
        color = config.get('color', COLORS['chord'])
        fill = config.get('fill', COLORS['segment_fill'])
        
        p1 = self.geometry.point_on_circle(angulo1)
        p2 = self.geometry.point_on_circle(angulo2)
        
        # Segmento (arco + cuerda)
        path = self.geometry.segment_path(angulo1, angulo2)
        self.svg_elements.append(
            f'<path d="{path}" fill="{fill}" stroke="{color}" stroke-width="2"/>'
        )
        
        # Cuerda
        self.svg_elements.append(svg_line(p1.x, p1.y, p2.x, p2.y, color, 2))
    
    def _render_leyenda(self):
        """Renderiza la caja de leyenda."""
        leyenda = self.spec.get('leyenda', {})
        texto = leyenda.get('texto', '')
        color = leyenda.get('color', COLORS['chord'])
        bg_color = leyenda.get('bg_color', COLORS['sector_fill'])
        
        width = self.config['width']
        y = self.config.get('legend_y', 305)
        box_width = min(320, width - 80)
        box_height = self.config.get('legend_height', 35)
        x = (width - box_width) / 2
        
        # Caja
        self.svg_elements.append(
            svg_rect(x, y, box_width, box_height, bg_color, color)
        )
        
        # Texto
        self.svg_elements.append(
            svg_text(width / 2, y + box_height / 2 + 4, texto, 12, "normal", COLORS['text'], "middle")
        )
    
    def _render_posiciones(self):
        """Renderiza posiciones de puntos o circunferencias."""
        tipo = self.spec.get('tipo', '')
        
        if tipo == 'posiciones-punto':
            self._render_posiciones_punto()
        elif tipo == 'posiciones-circunferencias':
            self._render_posiciones_circunferencias()
    
    def _render_posiciones_punto(self):
        """Renderiza las tres posiciones de un punto respecto a la circunferencia."""
        posiciones = self.spec.get('posiciones', [
            {'tipo': 'interior', 'etiqueta': 'Interior', 'formula': 'd < r'},
            {'tipo': 'sobre', 'etiqueta': 'Sobre la circ.', 'formula': 'd = r'},
            {'tipo': 'exterior', 'etiqueta': 'Exterior', 'formula': 'd > r'}
        ])
        
        width = self.config['width']
        n = len(posiciones)
        spacing = width / (n + 1)
        
        for i, pos in enumerate(posiciones):
            cx = spacing * (i + 1)
            cy = 190
            r = 70
            
            # Color según tipo
            colors = {
                'interior': COLORS['chord'],
                'sobre': COLORS['circle_stroke'],
                'exterior': COLORS['tangent']
            }
            color = colors.get(pos['tipo'], COLORS['chord'])
            
            # Circunferencia
            self.svg_elements.append(
                svg_circle(cx, cy, r, COLORS['circle_fill'], COLORS['circle_stroke'], 2, 0.3)
            )
            self.svg_elements.append(svg_circle(cx, cy, 3, COLORS['center'], COLORS['center']))
            
            # Punto P según posición
            if pos['tipo'] == 'interior':
                px, py = cx + 25, cy - 15
            elif pos['tipo'] == 'sobre':
                geom = CircleGeometry((cx, cy), r)
                p = geom.point_on_circle(50)
                px, py = p.x, p.y
            else:  # exterior
                px, py = cx + r + 20, cy - 20
            
            self.svg_elements.append(svg_circle(px, py, 6, color, color))
            self.svg_elements.append(svg_text(px + 10, py - 8, "P", 12, "bold", color))
            
            # Línea de distancia
            self.svg_elements.append(
                svg_line(cx, cy, px, py, COLORS['auxiliary'], 1.5, dashed=True)
            )
            
            # Etiquetas
            self.svg_elements.append(
                svg_text(cx, cy + r + 35, pos['etiqueta'], 13, "bold", color, "middle")
            )
            self.svg_elements.append(
                svg_text(cx, cy + r + 55, pos['formula'], 11, "normal", COLORS['text'], "middle")
            )
    
    def _render_posiciones_circunferencias(self):
        """Renderiza posiciones relativas entre dos circunferencias."""
        # Implementación similar a generate_circle_positions en circle_renderer.py
        # pero basada en spec JSON
        pass
    
    def _render_angulo(self):
        """Renderiza un ángulo en la circunferencia."""
        # Implementar según tipo de ángulo
        pass
    
    def _render_teorema(self):
        """Renderiza un teorema con demostración visual."""
        pass
    
    def _render_formula(self):
        """Renderiza una fórmula con componentes visuales."""
        pass
    
    def _render_generic(self):
        """Renderizado genérico basado en elementos del spec."""
        elementos = self.spec.get('elementos', [])
        
        for elem in elementos:
            tipo = elem.get('tipo', '')
            
            if tipo == 'circunferencia':
                cx = elem.get('cx', self.config['circle_center'][0])
                cy = elem.get('cy', self.config['circle_center'][1])
                r = elem.get('r', self.config['circle_radius'])
                self.svg_elements.append(
                    svg_circle(cx, cy, r, elem.get('fill', 'none'), 
                              elem.get('stroke', COLORS['circle_stroke']))
                )
            
            elif tipo == 'punto':
                x, y = elem.get('x', 0), elem.get('y', 0)
                self.svg_elements.append(
                    svg_circle(x, y, elem.get('r', 4), 
                              elem.get('color', COLORS['point']))
                )
            
            elif tipo == 'linea':
                self.svg_elements.append(
                    svg_line(elem['x1'], elem['y1'], elem['x2'], elem['y2'],
                            elem.get('color', COLORS['auxiliary']),
                            elem.get('width', 2),
                            elem.get('dashed', False))
                )
            
            elif tipo == 'texto':
                self.svg_elements.append(
                    svg_text(elem['x'], elem['y'], elem['texto'],
                            elem.get('size', 12), elem.get('weight', 'normal'),
                            elem.get('color', COLORS['text']),
                            elem.get('anchor', 'start'))
                )
    
    def save(self, output_path: str):
        """Guarda el SVG en un archivo."""
        svg_content = self.render()
        
        # Validar bounds antes de guardar
        # (implementar validación de elementos)
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        return output_path


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='CircleSpec Renderer - Genera SVGs de circunferencias desde specs JSON'
    )
    parser.add_argument('--spec', type=str, help='Archivo JSON con la especificación')
    parser.add_argument('--output', type=str, help='Archivo SVG de salida')
    parser.add_argument('--validate-only', action='store_true', help='Solo validar sin generar')
    parser.add_argument('--batch', type=str, help='Directorio con specs para procesar en lote')
    
    args = parser.parse_args()
    
    if args.batch:
        # Procesar directorio
        batch_dir = Path(args.batch)
        if not batch_dir.exists():
            print(f"❌ Directorio no existe: {args.batch}")
            sys.exit(1)
        
        specs = list(batch_dir.glob('*.json'))
        print(f"📁 Procesando {len(specs)} specs en {args.batch}")
        
        for spec_path in specs:
            output_path = spec_path.with_suffix('.svg')
            try:
                with open(spec_path, 'r', encoding='utf-8') as f:
                    spec = json.load(f)
                
                renderer = CircleSpecRenderer(spec)
                renderer.save(str(output_path))
                print(f"  ✅ {spec_path.name} → {output_path.name}")
            except Exception as e:
                print(f"  ❌ {spec_path.name}: {e}")
        
        return
    
    if not args.spec:
        parser.print_help()
        sys.exit(1)
    
    # Cargar spec
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"❌ Archivo no existe: {args.spec}")
        sys.exit(1)
    
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    
    # Validar
    validation = SpecValidator.validate(spec)
    
    if validation.warnings:
        for w in validation.warnings:
            print(f"⚠️  {w}")
    
    if not validation.valid:
        for e in validation.errors:
            print(f"❌ {e}")
        sys.exit(1)
    
    if args.validate_only:
        print("✅ Spec válido")
        sys.exit(0)
    
    # Renderizar
    output_path = args.output or str(spec_path.with_suffix('.svg'))
    
    renderer = CircleSpecRenderer(spec)
    renderer.save(output_path)
    
    print(f"✅ SVG generado: {output_path}")


if __name__ == '__main__':
    main()

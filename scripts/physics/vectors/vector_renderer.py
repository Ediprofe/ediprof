#!/usr/bin/env python3
"""
📐 Vector Renderer - Renderizador para Ilustraciones de Vectores (Física)

Genera SVGs para:
- Elementos de un vector (magnitud, dirección, sentido)
- Vectores en el plano cartesiano
- Componentes de un vector
- Suma de vectores (triángulo, paralelogramo)
- Escalado de vectores

Uso:
    python3 scripts/physics/vectors/vector_renderer.py --type <tipo> --output <archivo.svg>
"""

import math
import sys
from pathlib import Path

# Agregar el directorio de scripts al path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'geometry'))

from core.colors import COLORS
from core.svg_builder import SVGBuilder
from core.base import Point
from core.coordinate_system import CoordinateSystem


# ============================================================================
# CONFIGURACIÓN
# ============================================================================

SIZE_VECTOR = (600, 450)


# ============================================================================
# FUNCIÓN 1: ELEMENTOS DE UN VECTOR
# ============================================================================

def render_elementos_vector(output_path: str, title: str = "Elementos de un Vector"):
    """
    Renderiza un vector mostrando sus tres elementos:
    - Magnitud (longitud de la flecha)
    - Dirección (ángulo θ)
    - Sentido (punta de la flecha)
    """
    width, height = SIZE_VECTOR
    
    cs = CoordinateSystem(
        svg_width=width,
        svg_height=height,
        x_range=(-1, 8),
        y_range=(-1, 6),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    
    # Fondo
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Ejes
    origin = cs.to_svg(Point(0, 0))
    x_end = cs.to_svg(Point(7, 0))
    y_end = cs.to_svg(Point(0, 5))
    
    svg.arrow(Point(origin.x - 20, origin.y), x_end, stroke=COLORS['axis'], stroke_width=2)
    svg.arrow(Point(origin.x, origin.y + 20), y_end, stroke=COLORS['axis'], stroke_width=2)
    
    # Etiquetas de ejes
    svg.text("x", Point(x_end.x + 15, x_end.y), font_size=16, font_weight="bold", fill=COLORS['text'])
    svg.text("y", Point(y_end.x, y_end.y - 15), font_size=16, font_weight="bold", fill=COLORS['text'])
    
    # Vector principal: de (1, 1) a (6, 4)
    p_origin = cs.to_svg(Point(1, 1))
    p_end = cs.to_svg(Point(6, 4))
    
    # Dibujar vector con flecha
    svg.arrow(p_origin, p_end, stroke=COLORS['primary'], stroke_width=4)
    
    # Punto de origen
    svg.point(p_origin, radius=5, fill=COLORS['secondary'])
    svg.text("Origen", Point(p_origin.x - 40, p_origin.y + 5), font_size=12, fill=COLORS['secondary'], anchor="end")
    
    # Punto extremo
    svg.point(p_end, radius=5, fill=COLORS['primary'])
    svg.text("Extremo", Point(p_end.x + 10, p_end.y - 10), font_size=12, fill=COLORS['primary'], anchor="start")
    
    # Etiqueta de magnitud
    mid = Point((p_origin.x + p_end.x) / 2, (p_origin.y + p_end.y) / 2)
    svg.text("Magnitud", Point(mid.x - 10, mid.y - 25), font_size=14, font_weight="bold", fill=COLORS['primary'])
    
    # Línea horizontal para mostrar el ángulo
    p_horiz = cs.to_svg(Point(4, 1))
    svg.line(p_origin, p_horiz, stroke=COLORS['axis'], stroke_width=1, dashed=True)
    
    # Arco del ángulo
    angle = math.atan2(4 - 1, 6 - 1)
    arc_radius = 40
    arc_end_x = p_origin.x + arc_radius * math.cos(angle)
    arc_end_y = p_origin.y - arc_radius * math.sin(angle)
    
    svg.path(f"M {p_origin.x + arc_radius} {p_origin.y} A {arc_radius} {arc_radius} 0 0 0 {arc_end_x} {arc_end_y}",
             stroke=COLORS['accent'], stroke_width=2)
    
    svg.text("θ", Point(p_origin.x + arc_radius + 10, p_origin.y - 10), font_size=16, font_weight="bold", fill=COLORS['accent'])
    svg.text("(Dirección)", Point(p_origin.x + arc_radius + 55, p_origin.y - 5), font_size=11, fill=COLORS['accent'])
    
    # Etiqueta de sentido
    svg.text("Sentido", Point(p_end.x - 50, p_end.y - 45), font_size=12, font_weight="bold", fill=COLORS['secondary'])
    svg.text("(hacia aquí)", Point(p_end.x - 50, p_end.y - 30), font_size=10, fill=COLORS['secondary'])
    svg.arrow(Point(p_end.x - 30, p_end.y - 25), Point(p_end.x - 5, p_end.y - 5),
              stroke=COLORS['secondary'], stroke_width=2)
    
    # Título
    svg.text(title, Point(width / 2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# FUNCIÓN 2: VECTOR EN EL PLANO CARTESIANO
# ============================================================================

def render_vector_plano(output_path: str, vector: tuple = (4, 3), title: str = "Vector en el Plano Cartesiano"):
    """Renderiza un vector desde el origen hasta un punto P(x, y)."""
    width, height = SIZE_VECTOR
    vx, vy = vector
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, max(6, vx + 2)), y_range=(-1, max(5, vy + 2)),
        padding=50
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Cuadrícula
    for i in range(int(cs.x_min), int(cs.x_max) + 1):
        p1 = cs.to_svg(Point(i, cs.y_min))
        p2 = cs.to_svg(Point(i, cs.y_max))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    for j in range(int(cs.y_min), int(cs.y_max) + 1):
        p1 = cs.to_svg(Point(cs.x_min, j))
        p2 = cs.to_svg(Point(cs.x_max, j))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    
    # Ejes
    origin = cs.to_svg(Point(0, 0))
    x_end = cs.to_svg(Point(cs.x_max - 0.3, 0))
    y_end = cs.to_svg(Point(0, cs.y_max - 0.3))
    
    svg.arrow(Point(origin.x - 20, origin.y), x_end, stroke=COLORS['axis'], stroke_width=2)
    svg.arrow(Point(origin.x, origin.y + 20), y_end, stroke=COLORS['axis'], stroke_width=2)
    svg.text("x", Point(x_end.x + 15, x_end.y), font_size=16, font_weight="bold", fill=COLORS['text'])
    svg.text("y", Point(y_end.x, y_end.y - 15), font_size=16, font_weight="bold", fill=COLORS['text'])
    
    # Punto P y Vector A
    p_point = cs.to_svg(Point(vx, vy))
    svg.arrow(origin, p_point, stroke=COLORS['primary'], stroke_width=4)
    
    svg.point(origin, radius=4, fill=COLORS['secondary'])
    svg.text("O", Point(origin.x - 15, origin.y + 15), font_size=14, font_weight="bold", fill=COLORS['secondary'])
    
    svg.point(p_point, radius=5, fill=COLORS['primary'])
    svg.text(f"P({vx},{vy})", Point(p_point.x + 10, p_point.y - 10), font_size=13, font_weight="bold", fill=COLORS['primary'], anchor="start")
    
    mid = Point((origin.x + p_point.x) / 2, (origin.y + p_point.y) / 2)
    svg.text("A", Point(mid.x - 25, mid.y - 15), font_size=20, font_weight="bold", fill=COLORS['primary'])
    
    svg.text(title, Point(width / 2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# FUNCIÓN 3: COMPONENTES DE UN VECTOR
# ============================================================================

def render_componentes_vector(output_path: str, vector: tuple = (4, 3), title: str = "Componentes de un Vector"):
    """Renderiza un vector con sus componentes Ax y Ay."""
    width, height = SIZE_VECTOR
    vx, vy = vector
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, max(6, vx + 2)), y_range=(-1, max(5, vy + 2)),
        padding=50
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Cuadrícula
    for i in range(int(cs.x_min), int(cs.x_max) + 1):
        p1 = cs.to_svg(Point(i, cs.y_min))
        p2 = cs.to_svg(Point(i, cs.y_max))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    for j in range(int(cs.y_min), int(cs.y_max) + 1):
        p1 = cs.to_svg(Point(cs.x_min, j))
        p2 = cs.to_svg(Point(cs.x_max, j))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    
    # Ejes
    origin = cs.to_svg(Point(0, 0))
    x_end = cs.to_svg(Point(cs.x_max - 0.3, 0))
    y_end = cs.to_svg(Point(0, cs.y_max - 0.3))
    
    svg.arrow(Point(origin.x - 20, origin.y), x_end, stroke=COLORS['axis'], stroke_width=2)
    svg.arrow(Point(origin.x, origin.y + 20), y_end, stroke=COLORS['axis'], stroke_width=2)
    svg.text("x", Point(x_end.x + 15, x_end.y), font_size=16, font_weight="bold", fill=COLORS['text'])
    svg.text("y", Point(y_end.x, y_end.y - 15), font_size=16, font_weight="bold", fill=COLORS['text'])
    
    # Puntos
    p_point = cs.to_svg(Point(vx, vy))
    p_x = cs.to_svg(Point(vx, 0))
    
    # Componente X
    svg.arrow(origin, p_x, stroke=COLORS['accent'], stroke_width=3)
    svg.text(f"Ax = {vx}", Point((p_x.x + origin.x) / 2, origin.y + 25), font_size=13, font_weight="bold", fill=COLORS['accent'])
    
    # Componente Y
    svg.arrow(p_x, p_point, stroke=COLORS['secondary'], stroke_width=3)
    svg.text(f"Ay = {vy}", Point(p_x.x + 20, (p_x.y + p_point.y) / 2), font_size=13, font_weight="bold", fill=COLORS['secondary'], anchor="start")
    
    # Vector A principal
    svg.arrow(origin, p_point, stroke=COLORS['primary'], stroke_width=4)
    
    svg.point(p_point, radius=5, fill=COLORS['primary'])
    svg.text(f"P({vx},{vy})", Point(p_point.x + 10, p_point.y - 10), font_size=12, fill=COLORS['primary'], anchor="start")
    
    mid = Point((origin.x + p_point.x) / 2, (origin.y + p_point.y) / 2)
    svg.text("A", Point(mid.x - 25, mid.y - 15), font_size=20, font_weight="bold", fill=COLORS['primary'])
    
    # Líneas punteadas
    svg.line(p_point, Point(p_point.x, origin.y), stroke=COLORS['secondary'], stroke_width=1, dashed=True)
    svg.line(p_point, Point(origin.x, p_point.y), stroke=COLORS['secondary'], stroke_width=1, dashed=True)
    
    # Ángulo
    angle = math.atan2(vy, vx)
    arc_radius = 35
    arc_end_x = origin.x + arc_radius * math.cos(angle)
    arc_end_y = origin.y - arc_radius * math.sin(angle)
    svg.path(f"M {origin.x + arc_radius} {origin.y} A {arc_radius} {arc_radius} 0 0 0 {arc_end_x} {arc_end_y}",
             stroke=COLORS['accent'], stroke_width=2)
    svg.text("θ", Point(origin.x + arc_radius + 10, origin.y - 10), font_size=14, font_weight="bold", fill=COLORS['accent'])
    
    svg.text(title, Point(width / 2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# FUNCIÓN 4: SUMA DE VECTORES EN LÍNEA
# ============================================================================

def render_suma_linea(output_path: str, a_mag: float = 3, b_mag: float = 2, mismo_sentido: bool = True,
                      title: str = "Suma de Vectores Colineales"):
    """Renderiza suma de vectores en la misma línea."""
    width, height = 600, 250
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    scale = 50
    start_x = 80
    y_top = 80
    y_bottom = 180
    
    if mismo_sentido:
        svg.arrow(Point(start_x, y_top), Point(start_x + a_mag * scale, y_top), stroke=COLORS['primary'], stroke_width=4)
        svg.text(f"A = {a_mag}", Point(start_x + a_mag * scale / 2, y_top - 15), font_size=14, font_weight="bold", fill=COLORS['primary'])
        
        svg.arrow(Point(start_x + a_mag * scale, y_top), Point(start_x + (a_mag + b_mag) * scale, y_top), stroke=COLORS['accent'], stroke_width=4)
        svg.text(f"B = {b_mag}", Point(start_x + a_mag * scale + b_mag * scale / 2, y_top - 15), font_size=14, font_weight="bold", fill=COLORS['accent'])
        
        r_mag = a_mag + b_mag
        svg.arrow(Point(start_x, y_bottom), Point(start_x + r_mag * scale, y_bottom), stroke=COLORS['secondary'], stroke_width=4)
        svg.text(f"R = {a_mag} + {b_mag} = {r_mag}", Point(start_x + r_mag * scale / 2, y_bottom + 25), font_size=14, font_weight="bold", fill=COLORS['secondary'])
    else:
        svg.arrow(Point(start_x, y_top), Point(start_x + a_mag * scale, y_top), stroke=COLORS['primary'], stroke_width=4)
        svg.text(f"A = {a_mag}", Point(start_x + a_mag * scale / 2, y_top - 15), font_size=14, font_weight="bold", fill=COLORS['primary'])
        
        svg.arrow(Point(start_x + a_mag * scale, y_top), Point(start_x + (a_mag - b_mag) * scale, y_top), stroke=COLORS['accent'], stroke_width=4)
        svg.text(f"B = {b_mag}", Point(start_x + a_mag * scale - b_mag * scale / 2, y_top - 15), font_size=14, font_weight="bold", fill=COLORS['accent'])
        
        r_mag = a_mag - b_mag
        svg.arrow(Point(start_x, y_bottom), Point(start_x + r_mag * scale, y_bottom), stroke=COLORS['secondary'], stroke_width=4)
        svg.text(f"R = {a_mag} - {b_mag} = {r_mag}", Point(start_x + r_mag * scale / 2, y_bottom + 25), font_size=14, font_weight="bold", fill=COLORS['secondary'])
    
    svg.text(title, Point(width / 2, 30), font_size=18, font_weight="bold", fill=COLORS['text'])
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# FUNCIÓN 5: SUMA DE VECTORES - MÉTODO DEL TRIÁNGULO
# ============================================================================

def render_suma_triangulo(output_path: str, vec_a: tuple = (4, 1.5), vec_b: tuple = (2, 3),
                          title: str = "Método del Triángulo"):
    """Renderiza suma de vectores usando el método del triángulo (punta a cola)."""
    width, height = SIZE_VECTOR
    ax, ay = vec_a
    bx, by = vec_b
    rx, ry = ax + bx, ay + by
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, max(8, rx + 1)), y_range=(-1, max(6, ry + 1)),
        padding=50
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Cuadrícula
    for i in range(int(cs.x_min), int(cs.x_max) + 1):
        p1 = cs.to_svg(Point(i, cs.y_min))
        p2 = cs.to_svg(Point(i, cs.y_max))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    for j in range(int(cs.y_min), int(cs.y_max) + 1):
        p1 = cs.to_svg(Point(cs.x_min, j))
        p2 = cs.to_svg(Point(cs.x_max, j))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    
    # Ejes
    origin = cs.to_svg(Point(0, 0))
    x_end = cs.to_svg(Point(cs.x_max - 0.5, 0))
    y_end = cs.to_svg(Point(0, cs.y_max - 0.5))
    svg.arrow(Point(origin.x - 20, origin.y), x_end, stroke=COLORS['axis'], stroke_width=2)
    svg.arrow(Point(origin.x, origin.y + 20), y_end, stroke=COLORS['axis'], stroke_width=2)
    
    # Puntos
    p_a = cs.to_svg(Point(ax, ay))
    p_r = cs.to_svg(Point(rx, ry))
    
    # Vector A
    svg.arrow(origin, p_a, stroke=COLORS['primary'], stroke_width=4)
    svg.text("① A", Point((origin.x + p_a.x) / 2 - 20, (origin.y + p_a.y) / 2 - 15), font_size=14, font_weight="bold", fill=COLORS['primary'])
    
    # Vector B (punta a cola)
    svg.arrow(p_a, p_r, stroke=COLORS['accent'], stroke_width=4)
    svg.text("② B", Point((p_a.x + p_r.x) / 2 + 10, (p_a.y + p_r.y) / 2 - 10), font_size=14, font_weight="bold", fill=COLORS['accent'])
    
    # Vector R (resultante)
    svg.arrow(origin, p_r, stroke=COLORS['secondary'], stroke_width=4)
    svg.text("③ R = A + B", Point((origin.x + p_r.x) / 2 - 30, (origin.y + p_r.y) / 2 + 10), font_size=13, font_weight="bold", fill=COLORS['secondary'])
    
    svg.point(origin, radius=4, fill=COLORS['secondary'])
    svg.text("O", Point(origin.x - 15, origin.y + 15), font_size=12, fill=COLORS['secondary'])
    
    svg.text(title, Point(width / 2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# FUNCIÓN 6: SUMA DE VECTORES - MÉTODO DEL PARALELOGRAMO
# ============================================================================

def render_suma_paralelogramo(output_path: str, vec_a: tuple = (5, 1), vec_b: tuple = (2, 4),
                               title: str = "Método del Paralelogramo"):
    """Renderiza suma de vectores usando el método del paralelogramo."""
    width, height = SIZE_VECTOR
    ax, ay = vec_a
    bx, by = vec_b
    rx, ry = ax + bx, ay + by
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, max(8, rx + 1)), y_range=(-1, max(6, ry + 1)),
        padding=50
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Cuadrícula
    for i in range(int(cs.x_min), int(cs.x_max) + 1):
        p1 = cs.to_svg(Point(i, cs.y_min))
        p2 = cs.to_svg(Point(i, cs.y_max))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    for j in range(int(cs.y_min), int(cs.y_max) + 1):
        p1 = cs.to_svg(Point(cs.x_min, j))
        p2 = cs.to_svg(Point(cs.x_max, j))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    
    # Ejes
    origin = cs.to_svg(Point(0, 0))
    x_end = cs.to_svg(Point(cs.x_max - 0.5, 0))
    y_end = cs.to_svg(Point(0, cs.y_max - 0.5))
    svg.arrow(Point(origin.x - 20, origin.y), x_end, stroke=COLORS['axis'], stroke_width=2)
    svg.arrow(Point(origin.x, origin.y + 20), y_end, stroke=COLORS['axis'], stroke_width=2)
    
    # Puntos
    p_a = cs.to_svg(Point(ax, ay))
    p_b = cs.to_svg(Point(bx, by))
    p_r = cs.to_svg(Point(rx, ry))
    
    # Lados del paralelogramo
    svg.line(p_a, p_r, stroke=COLORS['secondary'], stroke_width=2, dashed=True)
    svg.line(p_b, p_r, stroke=COLORS['secondary'], stroke_width=2, dashed=True)
    
    # Vectores
    svg.arrow(origin, p_a, stroke=COLORS['primary'], stroke_width=4)
    svg.text("A", Point((origin.x + p_a.x) / 2, (origin.y + p_a.y) / 2 + 20), font_size=16, font_weight="bold", fill=COLORS['primary'])
    
    svg.arrow(origin, p_b, stroke=COLORS['accent'], stroke_width=4)
    svg.text("B", Point((origin.x + p_b.x) / 2 - 25, (origin.y + p_b.y) / 2), font_size=16, font_weight="bold", fill=COLORS['accent'])
    
    svg.arrow(origin, p_r, stroke=COLORS['secondary'], stroke_width=4)
    svg.text("R", Point((origin.x + p_r.x) / 2 + 10, (origin.y + p_r.y) / 2 - 10), font_size=16, font_weight="bold", fill=COLORS['secondary'])
    
    svg.point(origin, radius=4, fill=COLORS['secondary'])
    svg.text("O", Point(origin.x - 15, origin.y + 15), font_size=12, fill=COLORS['secondary'])
    
    svg.text(title, Point(width / 2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# FUNCIÓN 7: ESCALADO DE VECTORES
# ============================================================================

def render_escalado_vector(output_path: str, vector: tuple = (3, 2), title: str = "Multiplicación por Escalar"):
    """Renderiza un vector A y sus múltiplos: 2A, 0.5A, -A."""
    width, height = SIZE_VECTOR
    vx, vy = vector
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-7, 8), y_range=(-5, 6),
        padding=50
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Cuadrícula
    for i in range(int(cs.x_min), int(cs.x_max) + 1):
        p1 = cs.to_svg(Point(i, cs.y_min))
        p2 = cs.to_svg(Point(i, cs.y_max))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    for j in range(int(cs.y_min), int(cs.y_max) + 1):
        p1 = cs.to_svg(Point(cs.x_min, j))
        p2 = cs.to_svg(Point(cs.x_max, j))
        svg.line(p1, p2, stroke=COLORS['grid'], stroke_width=1)
    
    # Ejes
    origin = cs.to_svg(Point(0, 0))
    x_start = cs.to_svg(Point(cs.x_min + 0.5, 0))
    x_end = cs.to_svg(Point(cs.x_max - 0.5, 0))
    y_start = cs.to_svg(Point(0, cs.y_min + 0.5))
    y_end = cs.to_svg(Point(0, cs.y_max - 0.5))
    
    svg.arrow(x_start, x_end, stroke=COLORS['axis'], stroke_width=2)
    svg.arrow(y_start, y_end, stroke=COLORS['axis'], stroke_width=2)
    svg.text("x", Point(x_end.x + 10, x_end.y), font_size=14, font_weight="bold", fill=COLORS['text'])
    svg.text("y", Point(y_end.x, y_end.y - 10), font_size=14, font_weight="bold", fill=COLORS['text'])
    
    # Vector A
    p_a = cs.to_svg(Point(vx, vy))
    svg.arrow(origin, p_a, stroke=COLORS['primary'], stroke_width=4)
    svg.text("A", Point(p_a.x + 10, p_a.y - 5), font_size=14, font_weight="bold", fill=COLORS['primary'], anchor="start")
    
    # Vector 2A
    p_2a = cs.to_svg(Point(2*vx, 2*vy))
    svg.arrow(origin, p_2a, stroke=COLORS['secondary'], stroke_width=3)
    svg.text("2A", Point(p_2a.x + 10, p_2a.y - 5), font_size=13, font_weight="bold", fill=COLORS['secondary'], anchor="start")
    
    # Vector 0.5A
    p_half = cs.to_svg(Point(0.5*vx, 0.5*vy))
    svg.arrow(origin, p_half, stroke=COLORS['accent'], stroke_width=3)
    svg.text("0.5A", Point(p_half.x + 5, p_half.y - 15), font_size=12, font_weight="bold", fill=COLORS['accent'], anchor="start")
    
    # Vector -A
    p_neg = cs.to_svg(Point(-vx, -vy))
    svg.arrow(origin, p_neg, stroke=COLORS['accent'], stroke_width=3)
    svg.text("-A", Point(p_neg.x - 25, p_neg.y + 15), font_size=13, font_weight="bold", fill=COLORS['accent'])
    
    svg.point(origin, radius=4, fill=COLORS['secondary'])
    svg.text("O", Point(origin.x - 15, origin.y + 15), font_size=12, fill=COLORS['secondary'])
    
    svg.text(title, Point(width / 2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")


# ============================================================================
# CLI
# ============================================================================

RENDER_FUNCTIONS = {
    'elementos-vector': render_elementos_vector,
    'vector-plano': render_vector_plano,
    'componentes-vector': render_componentes_vector,
    'suma-linea-mismo': lambda out, **kw: render_suma_linea(out, mismo_sentido=True, title="Suma: Mismo Sentido"),
    'suma-linea-opuesto': lambda out, **kw: render_suma_linea(out, mismo_sentido=False, title="Suma: Sentidos Opuestos"),
    'suma-triangulo': render_suma_triangulo,
    'suma-paralelogramo': render_suma_paralelogramo,
    'escalado-vector': render_escalado_vector,
}


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generador de SVGs para vectores de física')
    parser.add_argument('--type', '-t', choices=list(RENDER_FUNCTIONS.keys()), help='Tipo de ilustración')
    parser.add_argument('--output', '-o', required=True, help='Ruta de salida del SVG')
    parser.add_argument('--all', action='store_true', help='Generar todos los tipos')
    
    args = parser.parse_args()
    
    if args.all:
        base_path = Path(args.output)
        base_path.mkdir(parents=True, exist_ok=True)
        for tipo, func in RENDER_FUNCTIONS.items():
            output = base_path / f"{tipo}.svg"
            func(str(output))
        print(f"\n🎉 ¡Todos los SVGs generados en {base_path}!")
    elif args.type:
        RENDER_FUNCTIONS[args.type](args.output)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

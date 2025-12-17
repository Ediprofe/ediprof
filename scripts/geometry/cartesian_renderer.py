#!/usr/bin/env python3
"""
📐 Cartesian Renderer - Renderizador para Geometría Analítica

Genera SVGs para ilustraciones del plano cartesiano:
- Puntos con coordenadas
- Segmentos y distancias
- Punto medio
- División de segmentos
- Polígonos y áreas

Uso:
    python scripts/geometry/cartesian_renderer.py --spec ARCHIVO.json --output ARCHIVO.svg
    python scripts/geometry/cartesian_renderer.py --type plano-basico --output plano.svg

Referencia: .agent/workflows/cartesian-spec.md
"""

import argparse
import json
import math
import sys
from pathlib import Path

# Importar módulo core
sys.path.insert(0, str(Path(__file__).parent))
from core.base import Point, COLORS, ValidationResult
from core.svg_builder import SVGBuilder
from core.coordinate_system import CoordinateSystem


# ============================================================================
# TIPOS DE ILUSTRACIÓN PREDEFINIDOS
# ============================================================================

def render_plano_basico(output_path: str, title: str = "El Plano Cartesiano"):
    """
    Renderiza un plano cartesiano básico con los 4 cuadrantes.
    Para: 01-introduccion-plano-cartesiano.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(-6, 6), y_range=(-5, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    
    # Fondo
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    
    # Título
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    # Cuadrícula y ejes
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Etiquetas de cuadrantes
    cuadrantes = [
        (Point(3, 3), "I", "(+, +)"),
        (Point(-3, 3), "II", "(−, +)"),
        (Point(-3, -3), "III", "(−, −)"),
        (Point(3, -3), "IV", "(+, −)")
    ]
    
    for pos, num, signos in cuadrantes:
        svg_pos = coord.to_svg(pos)
        builder.text(f"Cuadrante {num}", svg_pos, font_size=14, 
                     font_weight='bold', fill=COLORS['primary'])
        builder.text(signos, Point(svg_pos.x, svg_pos.y + 18), 
                     font_size=12, fill=COLORS['text_light'])
    
    # Puntos de ejemplo
    ejemplos = [
        (Point(4, 3), "P", COLORS['point']),
        (Point(-3, 2), "Q", COLORS['secondary']),
        (Point(-2, -4), "R", COLORS['highlight']),
        (Point(5, -2), "S", COLORS['accent'])
    ]
    
    for p, label, color in ejemplos:
        coord.draw_point(builder, p, label=label, show_coords=True, color=color)
    
    # Leyenda
    builder.rect(400, 420, 180, 70, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text("Puntos de ejemplo:", Point(490, 438), font_size=11, 
                 font_weight='bold', fill=COLORS['text'])
    
    y_leg = 455
    for i, (p, label, color) in enumerate(ejemplos[:2]):
        x_str = str(int(p.x)) if p.x == int(p.x) else f'{p.x}'
        y_str = str(int(p.y)) if p.y == int(p.y) else f'{p.y}'
        builder.point(Point(420, y_leg + i*15), radius=4, fill=color)
        builder.text(f"{label}({x_str}, {y_str})", Point(435, y_leg + i*15), 
                     font_size=10, fill=color, anchor='start')
    
    for i, (p, label, color) in enumerate(ejemplos[2:]):
        x_str = str(int(p.x)) if p.x == int(p.x) else f'{p.x}'
        y_str = str(int(p.y)) if p.y == int(p.y) else f'{p.y}'
        builder.point(Point(510, y_leg + i*15), radius=4, fill=color)
        builder.text(f"{label}({x_str}, {y_str})", Point(525, y_leg + i*15), 
                     font_size=10, fill=color, anchor='start')
    
    builder.save(output_path)
    return True


def render_distancia(output_path: str, 
                     p1: tuple = (1, 2), p2: tuple = (4, 6),
                     title: str = "Distancia entre dos puntos"):
    """
    Renderiza la fórmula de distancia con triángulo rectángulo.
    Para: 02-distancia-entre-dos-puntos.md
    """
    # Determinar rango basado en los puntos
    x_min = min(p1[0], p2[0]) - 2
    x_max = max(p1[0], p2[0]) + 2
    y_min = min(p1[1], p2[1]) - 2
    y_max = max(p1[1], p2[1]) + 2
    
    # Ajustar para incluir el origen si está cerca
    x_min = min(x_min, -1)
    y_min = min(y_min, -1)
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(x_min, x_max), y_range=(y_min, y_max),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    # Cuadrícula y ejes
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Puntos
    P1 = Point(p1[0], p1[1])
    P2 = Point(p2[0], p2[1])
    
    # Triángulo rectángulo auxiliar
    coord.draw_right_triangle(builder, P1, P2, color=COLORS['auxiliary'], fill='#fef3c7')
    coord.draw_distance_labels(builder, P1, P2, 
                               dx_label=f'Δx = {abs(p2[0]-p1[0])}',
                               dy_label=f'Δy = {abs(p2[1]-p1[1])}')
    
    # Segmento (hipotenusa)
    coord.draw_segment(builder, P1, P2, color=COLORS['accent'], width=2.5, label='d')
    
    # Puntos
    coord.draw_point(builder, P1, label='P₁', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, P2, label='P₂', show_coords=True, color=COLORS['secondary'],
                     label_offset=(-60, -10))
    
    # Fórmula
    dx = abs(p2[0] - p1[0])
    dy = abs(p2[1] - p1[1])
    d = math.sqrt(dx**2 + dy**2)
    d_str = str(int(d)) if d == int(d) else f'√{dx**2 + dy**2}'
    
    formula = f'd = √(Δx² + Δy²) = √({dx}² + {dy}²) = {d_str}'
    builder.formula_box(formula, Point(300, 450), font_size=13)
    
    builder.save(output_path)
    return True


def render_punto_medio(output_path: str,
                       p1: tuple = (2, 1), p2: tuple = (6, 5),
                       title: str = "Punto medio de un segmento"):
    """
    Renderiza el punto medio de un segmento.
    Para: 03-punto-medio.md
    """
    x_min = min(p1[0], p2[0]) - 2
    x_max = max(p1[0], p2[0]) + 2
    y_min = min(p1[1], p2[1]) - 2
    y_max = max(p1[1], p2[1]) + 2
    
    x_min = min(x_min, -1)
    y_min = min(y_min, -1)
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(x_min, x_max), y_range=(y_min, y_max),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    P1 = Point(p1[0], p1[1])
    P2 = Point(p2[0], p2[1])
    M = P1.midpoint(P2)
    
    # Segmento
    coord.draw_segment(builder, P1, P2, color=COLORS['primary'], width=2)
    
    # Puntos
    coord.draw_point(builder, P1, label='A', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, P2, label='B', show_coords=True, color=COLORS['primary'],
                     label_offset=(-50, -10))
    coord.draw_point(builder, M, label='M', show_coords=True, color=COLORS['accent'],
                     radius=6, label_offset=(10, -15))
    
    # Marcas de igualdad en los segmentos
    svg_p1 = coord.to_svg(P1)
    svg_m = coord.to_svg(M)
    svg_p2 = coord.to_svg(P2)
    
    # Líneas de marca (indicando que AM = MB)
    mid1 = svg_p1.midpoint(svg_m)
    mid2 = svg_m.midpoint(svg_p2)
    
    # Perpendicular al segmento para las marcas
    dx = svg_p2.x - svg_p1.x
    dy = svg_p2.y - svg_p1.y
    length = math.sqrt(dx**2 + dy**2)
    nx, ny = -dy/length * 8, dx/length * 8
    
    builder.line(Point(mid1.x - nx, mid1.y - ny), 
                 Point(mid1.x + nx, mid1.y + ny),
                 stroke=COLORS['secondary'], stroke_width=2)
    builder.line(Point(mid2.x - nx, mid2.y - ny), 
                 Point(mid2.x + nx, mid2.y + ny),
                 stroke=COLORS['secondary'], stroke_width=2)
    
    # Fórmula
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2
    mx_str = str(int(mx)) if mx == int(mx) else f'{mx:.1f}'
    my_str = str(int(my)) if my == int(my) else f'{my:.1f}'
    
    formula = f'M = (({p1[0]}+{p2[0]})/2, ({p1[1]}+{p2[1]})/2) = ({mx_str}, {my_str})'
    builder.formula_box(formula, Point(300, 450), font_size=12)
    
    builder.save(output_path)
    return True


def render_division_segmento(output_path: str,
                             p1: tuple = (1, 2), p2: tuple = (7, 8),
                             m: int = 1, n: int = 2,
                             title: str = "División de un segmento"):
    """
    Renderiza la división de un segmento en razón m:n.
    Para: 04-division-segmento-razon.md
    """
    x_min = min(p1[0], p2[0]) - 2
    x_max = max(p1[0], p2[0]) + 2
    y_min = min(p1[1], p2[1]) - 2
    y_max = max(p1[1], p2[1]) + 2
    
    x_min = min(x_min, -1)
    y_min = min(y_min, -1)
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(x_min, x_max), y_range=(y_min, y_max),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(f'{title} en razón {m}:{n}', Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    P1 = Point(p1[0], p1[1])
    P2 = Point(p2[0], p2[1])
    
    # Punto P que divide en razón m:n
    px = (m * p2[0] + n * p1[0]) / (m + n)
    py = (m * p2[1] + n * p1[1]) / (m + n)
    P = Point(px, py)
    
    # Segmento completo
    coord.draw_segment(builder, P1, P2, color=COLORS['primary'], width=2)
    
    # Segmentos parciales con colores diferentes
    svg_p1 = coord.to_svg(P1)
    svg_p = coord.to_svg(P)
    svg_p2 = coord.to_svg(P2)
    
    # Etiquetas de razón
    mid1 = svg_p1.midpoint(svg_p)
    mid2 = svg_p.midpoint(svg_p2)
    
    builder.text(f'{m}', Point(mid1.x, mid1.y - 15), font_size=14, 
                 font_weight='bold', fill=COLORS['secondary'])
    builder.text(f'{n}', Point(mid2.x, mid2.y - 15), font_size=14, 
                 font_weight='bold', fill=COLORS['highlight'])
    
    # Puntos
    coord.draw_point(builder, P1, label='A', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, P2, label='B', show_coords=True, color=COLORS['primary'],
                     label_offset=(-50, -10))
    coord.draw_point(builder, P, label='P', show_coords=True, color=COLORS['accent'],
                     radius=6, label_offset=(10, -15))
    
    # Fórmula
    px_str = str(int(px)) if px == int(px) else f'{px:.1f}'
    py_str = str(int(py)) if py == int(py) else f'{py:.1f}'
    
    formula = f'P divide AB en razón {m}:{n} → P({px_str}, {py_str})'
    builder.formula_box(formula, Point(300, 450), font_size=12)
    
    builder.save(output_path)
    return True


def render_area_triangulo(output_path: str,
                          vertices: list = [(1, 1), (5, 1), (3, 5)],
                          title: str = "Área de un triángulo"):
    """
    Renderiza un triángulo con su área.
    Para: 05-area-triangulos-poligonos.md
    """
    xs = [v[0] for v in vertices]
    ys = [v[1] for v in vertices]
    
    x_min = min(xs) - 2
    x_max = max(xs) + 2
    y_min = min(ys) - 2
    y_max = max(ys) + 2
    
    x_min = min(x_min, -1)
    y_min = min(y_min, -1)
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(x_min, x_max), y_range=(y_min, y_max),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Triángulo
    points = [Point(v[0], v[1]) for v in vertices]
    coord.draw_polygon(builder, points, fill='#dbeafe', stroke=COLORS['primary'])
    
    # Vértices
    labels = ['A', 'B', 'C']
    offsets = [(10, 10), (10, 10), (0, -15)]
    
    for i, (v, label, offset) in enumerate(zip(vertices, labels, offsets)):
        coord.draw_point(builder, Point(v[0], v[1]), label=label, 
                         show_coords=True, color=COLORS['primary'],
                         label_offset=offset)
    
    # Calcular área usando fórmula del determinante
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    
    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
    area_str = str(int(area)) if area == int(area) else f'{area:.1f}'
    
    # Mostrar área en el centro del triángulo
    cx = sum(xs) / 3
    cy = sum(ys) / 3
    svg_center = coord.to_svg(Point(cx, cy))
    
    builder.text(f'Área = {area_str}', svg_center, font_size=14, 
                 font_weight='bold', fill=COLORS['accent'])
    
    # Fórmula
    formula = f'A = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)| = {area_str}'
    builder.formula_box(formula, Point(300, 470), font_size=12)
    
    builder.save(output_path)
    return True


# ============================================================================
# PENDIENTE E INCLINACIÓN
# ============================================================================

def render_tipos_pendiente(output_path: str, title: str = "Tipos de Pendiente"):
    """
    Renderiza 3 rectas: positiva, negativa y horizontal.
    Para: 01-concepto-pendiente.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-5, 5), y_range=(-6, 8),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta positiva (m = 2): y = 2x
    p1_pos = Point(-3, -6)
    p2_pos = Point(3, 6)
    coord.draw_segment(builder, p1_pos, p2_pos, color='#22c55e', width=2.5)
    svg_label_pos = coord.to_svg(Point(2.5, 5))
    builder.text('m = 2 (↗)', Point(svg_label_pos.x + 10, svg_label_pos.y), 
                 font_size=12, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Recta negativa (m = -1.5): y = -1.5x
    p1_neg = Point(-4, 6)
    p2_neg = Point(4, -6)
    coord.draw_segment(builder, p1_neg, p2_neg, color='#ef4444', width=2.5)
    svg_label_neg = coord.to_svg(Point(3, -4.5))
    builder.text('m = -1.5 (↘)', Point(svg_label_neg.x + 10, svg_label_neg.y), 
                 font_size=12, font_weight='bold', fill='#ef4444', anchor='start')
    
    # Recta horizontal (m = 0): y = 2
    p1_hor = Point(-4, 2)
    p2_hor = Point(4, 2)
    coord.draw_segment(builder, p1_hor, p2_hor, color='#3b82f6', width=2.5)
    svg_label_hor = coord.to_svg(Point(3.5, 2))
    builder.text('m = 0 (→)', Point(svg_label_hor.x + 10, svg_label_hor.y - 15), 
                 font_size=12, font_weight='bold', fill='#3b82f6', anchor='start')
    
    # Leyenda
    builder.rect(420, 400, 160, 65, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text('Leyenda:', Point(500, 415), font_size=11, font_weight='bold')
    builder.line(Point(430, 430), Point(460, 430), stroke='#22c55e', stroke_width=3)
    builder.text('Positiva (sube)', Point(470, 430), font_size=10, fill='#22c55e', anchor='start')
    builder.line(Point(430, 445), Point(460, 445), stroke='#ef4444', stroke_width=3)
    builder.text('Negativa (baja)', Point(470, 445), font_size=10, fill='#ef4444', anchor='start')
    builder.line(Point(430, 460), Point(460, 460), stroke='#3b82f6', stroke_width=3)
    builder.text('Horizontal', Point(470, 460), font_size=10, fill='#3b82f6', anchor='start')
    
    builder.save(output_path)
    return True


def render_concepto_pendiente(output_path: str, title: str = "Concepto de Pendiente: m = Δy/Δx"):
    """
    Renderiza una recta con el triángulo Δx, Δy marcado.
    Para: 01-concepto-pendiente.md (segunda ilustración)
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-1, 5), y_range=(-1, 9),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta y = 2x
    coord.draw_segment(builder, Point(-0.5, -1), Point(4.5, 9), color='#3b82f6', width=2.5)
    
    # Puntos sobre la recta
    P1 = Point(1, 2)
    P2 = Point(2, 4)
    P3 = Point(3, 6)
    
    # Triángulo auxiliar entre P1 y P2
    coord.draw_right_triangle(builder, P1, P2, color='#94a3b8', fill='#fef3c7')
    
    # Etiquetas Δx y Δy
    svg_p1 = coord.to_svg(P1)
    svg_p2 = coord.to_svg(P2)
    svg_aux = coord.to_svg(Point(2, 2))
    
    mid_x = svg_p1.midpoint(svg_aux)
    mid_y = svg_aux.midpoint(svg_p2)
    
    builder.text('Δx = 1', Point(mid_x.x, mid_x.y + 20), 
                 font_size=13, font_weight='bold', fill='#22c55e')
    builder.text('Δy = 2', Point(mid_y.x + 20, mid_y.y), 
                 font_size=13, font_weight='bold', fill='#f97316')
    
    # Puntos
    coord.draw_point(builder, P1, label='', color='#ef4444', radius=6)
    coord.draw_point(builder, P2, label='', color='#ef4444', radius=6)
    coord.draw_point(builder, P3, label='', color='#ef4444', radius=6)
    
    # Etiquetas de puntos
    builder.text('(1, 2)', Point(coord.to_svg(P1).x - 10, coord.to_svg(P1).y - 15), 
                 font_size=11, font_weight='bold', fill='#1e293b')
    builder.text('(2, 4)', Point(coord.to_svg(P2).x + 10, coord.to_svg(P2).y - 10), 
                 font_size=11, font_weight='bold', fill='#1e293b')
    builder.text('(3, 6)', Point(coord.to_svg(P3).x + 10, coord.to_svg(P3).y - 10), 
                 font_size=11, font_weight='bold', fill='#1e293b')
    
    # Fórmula
    builder.formula_box('m = Δy/Δx = 2/1 = 2', Point(300, 450), font_size=14)
    
    builder.save(output_path)
    return True


def render_pendiente_absoluto(output_path: str, title: str = "Comparación por Valor Absoluto"):
    """
    Renderiza 3 rectas con diferentes valores absolutos de pendiente.
    Para: 01-concepto-pendiente.md (tercera ilustración)
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-4, 4), y_range=(-5, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta suave (m = 0.3)
    coord.draw_segment(builder, Point(-4, -1.2), Point(4, 1.2), color='#22c55e', width=2.5)
    svg_l1 = coord.to_svg(Point(3, 0.9))
    builder.text('|m| = 0.3 (suave)', Point(svg_l1.x + 5, svg_l1.y - 10), 
                 font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Recta 45° (m = 1)
    coord.draw_segment(builder, Point(-4, -4), Point(4, 4), color='#f59e0b', width=2.5)
    svg_l2 = coord.to_svg(Point(3.5, 3.5))
    builder.text('|m| = 1 (45°)', Point(svg_l2.x + 5, svg_l2.y - 10), 
                 font_size=11, font_weight='bold', fill='#f59e0b', anchor='start')
    
    # Recta empinada (m = 3)
    coord.draw_segment(builder, Point(-1.5, -4.5), Point(1.5, 4.5), color='#ef4444', width=2.5)
    svg_l3 = coord.to_svg(Point(1.2, 3.6))
    builder.text('|m| = 3 (empinada)', Point(svg_l3.x + 5, svg_l3.y - 10), 
                 font_size=11, font_weight='bold', fill='#ef4444', anchor='start')
    
    # Leyenda
    builder.rect(20, 400, 200, 65, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text('Mayor |m| = más empinada', Point(120, 420), font_size=11, font_weight='bold')
    builder.line(Point(30, 440), Point(60, 440), stroke='#22c55e', stroke_width=3)
    builder.text('Suave', Point(70, 440), font_size=10, fill='#22c55e', anchor='start')
    builder.line(Point(110, 440), Point(140, 440), stroke='#f59e0b', stroke_width=3)
    builder.text('45°', Point(150, 440), font_size=10, fill='#f59e0b', anchor='start')
    builder.line(Point(30, 455), Point(60, 455), stroke='#ef4444', stroke_width=3)
    builder.text('Empinada', Point(70, 455), font_size=10, fill='#ef4444', anchor='start')
    
    builder.save(output_path)
    return True


def render_rectas_especiales(output_path: str, title: str = "Rectas Horizontales y Verticales"):
    """
    Renderiza rectas horizontales (m=0) y verticales (m indefinida).
    Para: 01-concepto-pendiente.md (cuarta ilustración)
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-5, 5), y_range=(-4, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Rectas horizontales
    coord.draw_segment(builder, Point(-5, 3), Point(5, 3), color='#3b82f6', width=2.5)
    svg_h1 = coord.to_svg(Point(4, 3))
    builder.text('y = 3 (m = 0)', Point(svg_h1.x, svg_h1.y - 12), 
                 font_size=10, font_weight='bold', fill='#3b82f6')
    
    coord.draw_segment(builder, Point(-5, -2), Point(5, -2), color='#f59e0b', width=2.5)
    svg_h2 = coord.to_svg(Point(4, -2))
    builder.text('y = -2 (m = 0)', Point(svg_h2.x, svg_h2.y + 18), 
                 font_size=10, font_weight='bold', fill='#f59e0b')
    
    # Rectas verticales
    coord.draw_segment(builder, Point(2, -4), Point(2, 5), color='#ef4444', width=2.5)
    svg_v1 = coord.to_svg(Point(2, 4.5))
    builder.text('x = 2', Point(svg_v1.x + 10, svg_v1.y), 
                 font_size=10, font_weight='bold', fill='#ef4444')
    
    coord.draw_segment(builder, Point(-3, -4), Point(-3, 5), color='#a855f7', width=2.5)
    svg_v2 = coord.to_svg(Point(-3, 4.5))
    builder.text('x = -3', Point(svg_v2.x - 40, svg_v2.y), 
                 font_size=10, font_weight='bold', fill='#a855f7')
    
    # Leyenda
    builder.rect(400, 390, 180, 75, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text('Casos especiales:', Point(490, 405), font_size=11, font_weight='bold')
    builder.text('Horizontales: m = 0', Point(415, 425), font_size=10, fill='#3b82f6', anchor='start')
    builder.text('Verticales: m indefinida', Point(415, 445), font_size=10, fill='#ef4444', anchor='start')
    builder.text('(no se puede dividir ÷ 0)', Point(415, 460), font_size=9, fill='#64748b', anchor='start')
    
    builder.save(output_path)
    return True


def render_calculo_pendiente(output_path: str, 
                              p1: tuple = (1, 2), p2: tuple = (4, 5),
                              title: str = "Cálculo de la Pendiente"):
    """
    Renderiza dos puntos con Δx y Δy marcados.
    Para: 02-calculo-pendiente.md
    """
    x_min = min(p1[0], p2[0]) - 2
    x_max = max(p1[0], p2[0]) + 3
    y_min = min(p1[1], p2[1]) - 2
    y_max = max(p1[1], p2[1]) + 2
    
    x_min = min(x_min, -1)
    y_min = min(y_min, -1)
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(x_min, x_max), y_range=(y_min, y_max),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    P1 = Point(p1[0], p1[1])
    P2 = Point(p2[0], p2[1])
    P3 = Point(p2[0], p1[1])  # Punto auxiliar
    
    # Triángulo auxiliar
    coord.draw_right_triangle(builder, P1, P2, color=COLORS['auxiliary'], fill='#fef3c7')
    
    # Recta principal
    coord.draw_segment(builder, P1, P2, color=COLORS['primary'], width=2.5)
    
    # Etiquetas Δx y Δy
    svg_p1 = coord.to_svg(P1)
    svg_p2 = coord.to_svg(P2)
    svg_p3 = coord.to_svg(P3)
    
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    mid_x = svg_p1.midpoint(svg_p3)
    mid_y = svg_p3.midpoint(svg_p2)
    
    builder.text(f'Δx = {dx}', Point(mid_x.x, mid_x.y + 18), 
                 font_size=12, font_weight='bold', fill=COLORS['secondary'])
    builder.text(f'Δy = {dy}', Point(mid_y.x + 18, mid_y.y), 
                 font_size=12, font_weight='bold', fill=COLORS['accent'])
    
    # Puntos
    coord.draw_point(builder, P1, label='P₁', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, P2, label='P₂', show_coords=True, color=COLORS['primary'],
                     label_offset=(-60, -10))
    
    # Fórmula
    m = dy / dx if dx != 0 else 'indefinida'
    if isinstance(m, float):
        m_str = str(int(m)) if m == int(m) else f'{m:.2f}'
    else:
        m_str = m
    
    formula = f'm = Δy/Δx = {dy}/{dx} = {m_str}'
    builder.formula_box(formula, Point(300, 450), font_size=13)
    
    builder.save(output_path)
    return True


def render_angulo_inclinacion(output_path: str, 
                               pendiente: float = 1,
                               title: str = "Ángulo de Inclinación"):
    """
    Renderiza una recta con su ángulo θ respecto al eje X.
    Para: 03-angulo-inclinacion.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-4, 6), y_range=(-2, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta y = mx (pasa por el origen)
    x1, x2 = -2, 5
    y1 = pendiente * x1
    y2 = pendiente * x2
    
    P1 = Point(x1, y1)
    P2 = Point(x2, y2)
    
    coord.draw_segment(builder, P1, P2, color=COLORS['primary'], width=2.5)
    
    # Arco del ángulo
    import math
    angle_rad = math.atan(pendiente)
    angle_deg = math.degrees(angle_rad)
    
    origin_svg = coord.to_svg(Point(0, 0))
    arc_radius = 40
    
    # Dibujar arco
    end_x = origin_svg.x + arc_radius * math.cos(angle_rad)
    end_y = origin_svg.y - arc_radius * math.sin(angle_rad)  # Negativo porque SVG Y invertido
    
    # Path del arco
    large_arc = 0 if angle_deg <= 180 else 1
    sweep = 0  # Antihorario en SVG
    arc_path = f'M {origin_svg.x + arc_radius} {origin_svg.y} A {arc_radius} {arc_radius} 0 {large_arc} {sweep} {end_x} {end_y}'
    builder.path(arc_path, fill='none', stroke=COLORS['highlight'], stroke_width=2)
    
    # Etiqueta θ
    label_angle = angle_rad / 2
    label_x = origin_svg.x + (arc_radius + 15) * math.cos(label_angle)
    label_y = origin_svg.y - (arc_radius + 15) * math.sin(label_angle)
    builder.text('θ', Point(label_x, label_y), font_size=16, font_weight='bold', fill=COLORS['highlight'])
    
    # Etiqueta de la recta
    svg_label = coord.to_svg(Point(4, pendiente * 4))
    builder.text(f'm = {pendiente}', Point(svg_label.x + 10, svg_label.y - 10), 
                 font_size=12, font_weight='bold', fill=COLORS['primary'], anchor='start')
    
    # Fórmula
    angle_str = f'{angle_deg:.1f}°' if angle_deg != int(angle_deg) else f'{int(angle_deg)}°'
    formula = f'm = tan(θ)  →  θ = arctan({pendiente}) = {angle_str}'
    builder.formula_box(formula, Point(300, 450), font_size=12)
    
    builder.save(output_path)
    return True


def render_paralelas_perpendiculares(output_path: str, 
                                      title: str = "Rectas Paralelas y Perpendiculares"):
    """
    Renderiza dos pares de rectas: paralelas y perpendiculares.
    Para: 04-rectas-paralelas-perpendiculares.md
    """
    coord = CoordinateSystem(
        svg_width=650, svg_height=480,
        x_range=(-5, 7), y_range=(-4, 6),
        padding=50
    )
    
    builder = SVGBuilder(650, 480)
    builder.rect(0, 0, 650, 480, fill='#ffffff')
    builder.text(title, Point(325, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Rectas paralelas (m = 1)
    # L1: y = x + 2
    coord.draw_segment(builder, Point(-4, -2), Point(3, 5), color='#22c55e', width=2.5)
    svg_l1 = coord.to_svg(Point(2, 4))
    builder.text('L₁: m = 1', Point(svg_l1.x + 5, svg_l1.y - 10), 
                 font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # L2: y = x - 2
    coord.draw_segment(builder, Point(-2, -4), Point(6, 4), color='#22c55e', width=2.5)
    svg_l2 = coord.to_svg(Point(5, 3))
    builder.text('L₂: m = 1', Point(svg_l2.x + 5, svg_l2.y + 15), 
                 font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Símbolo paralelas
    svg_mid = coord.to_svg(Point(0, 1))
    builder.text('∥', Point(svg_mid.x - 30, svg_mid.y), font_size=20, fill='#22c55e')
    
    # Rectas perpendiculares
    # L3: y = 2x - 3
    coord.draw_segment(builder, Point(-1, -5), Point(4, 5), color='#ef4444', width=2.5)
    svg_l3 = coord.to_svg(Point(3.5, 4))
    builder.text('L₃: m = 2', Point(svg_l3.x + 5, svg_l3.y - 5), 
                 font_size=11, font_weight='bold', fill='#ef4444', anchor='start')
    
    # L4: y = -0.5x + 1 (perpendicular a L3)
    coord.draw_segment(builder, Point(-4, 3), Point(6, -2), color='#3b82f6', width=2.5)
    svg_l4 = coord.to_svg(Point(5, -1.5))
    builder.text('L₄: m = -½', Point(svg_l4.x + 5, svg_l4.y + 15), 
                 font_size=11, font_weight='bold', fill='#3b82f6', anchor='start')
    
    # Símbolo perpendicular
    svg_perp = coord.to_svg(Point(1.5, -0.5))
    builder.text('⊥', Point(svg_perp.x + 20, svg_perp.y - 10), font_size=18, fill='#ef4444')
    
    # Leyenda
    builder.rect(480, 380, 150, 85, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text('Condiciones:', Point(555, 395), font_size=11, font_weight='bold')
    builder.text('Paralelas:', Point(495, 415), font_size=10, fill='#22c55e', anchor='start')
    builder.text('m₁ = m₂', Point(560, 415), font_size=10, fill='#1e293b', anchor='start')
    builder.text('Perpendic.:', Point(495, 435), font_size=10, fill='#ef4444', anchor='start')
    builder.text('m₁·m₂ = -1', Point(560, 435), font_size=10, fill='#1e293b', anchor='start')
    builder.text('2 × (-½) = -1 ✓', Point(520, 455), font_size=10, fill='#64748b')
    
    builder.save(output_path)
    return True


def render_angulo_entre_rectas(output_path: str,
                                m1: float = 2, m2: float = 0.5,
                                title: str = "Ángulo entre dos rectas"):
    """
    Renderiza dos rectas con el ángulo φ entre ellas.
    Para: 05-angulo-entre-dos-rectas.md
    """
    import math
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-3, 6), y_range=(-2, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Punto de intersección (calculado para y = m1*x y y = m2*x + 1)
    # Intersección: m1*x = m2*x + 1 => x = 1/(m1-m2)
    if m1 != m2:
        x_int = 1 / (m1 - m2)
        y_int = m1 * x_int
    else:
        x_int, y_int = 0, 0
    
    # Recta 1: y = m1 * x
    x1_start, x1_end = -1, 3
    coord.draw_segment(builder, 
                       Point(x1_start, m1 * x1_start), 
                       Point(x1_end, m1 * x1_end), 
                       color='#3b82f6', width=2.5)
    svg_l1 = coord.to_svg(Point(2.5, m1 * 2.5))
    builder.text(f'L₁: m₁ = {m1}', Point(svg_l1.x + 5, svg_l1.y - 10), 
                 font_size=11, font_weight='bold', fill='#3b82f6', anchor='start')
    
    # Recta 2: y = m2 * x + 1
    x2_start, x2_end = -2, 5
    coord.draw_segment(builder, 
                       Point(x2_start, m2 * x2_start + 1), 
                       Point(x2_end, m2 * x2_end + 1), 
                       color='#22c55e', width=2.5)
    svg_l2 = coord.to_svg(Point(4, m2 * 4 + 1))
    builder.text(f'L₂: m₂ = {m2}', Point(svg_l2.x + 5, svg_l2.y + 15), 
                 font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Punto de intersección
    coord.draw_point(builder, Point(x_int, y_int), label='', color=COLORS['accent'], radius=4)
    
    # Arco del ángulo
    angle1 = math.atan(m1)
    angle2 = math.atan(m2)
    
    int_svg = coord.to_svg(Point(x_int, y_int))
    arc_radius = 35
    
    # Calcular ángulo entre las rectas
    tan_phi = abs((m2 - m1) / (1 + m1 * m2)) if (1 + m1 * m2) != 0 else float('inf')
    phi = math.atan(tan_phi)
    phi_deg = math.degrees(phi)
    
    # Dibujar arco entre las dos rectas
    start_angle = min(angle1, angle2)
    end_angle = max(angle1, angle2)
    
    start_x = int_svg.x + arc_radius * math.cos(start_angle)
    start_y = int_svg.y - arc_radius * math.sin(start_angle)
    end_x = int_svg.x + arc_radius * math.cos(end_angle)
    end_y = int_svg.y - arc_radius * math.sin(end_angle)
    
    arc_path = f'M {start_x} {start_y} A {arc_radius} {arc_radius} 0 0 0 {end_x} {end_y}'
    builder.path(arc_path, fill='none', stroke=COLORS['highlight'], stroke_width=2.5)
    
    # Etiqueta φ
    mid_angle = (start_angle + end_angle) / 2
    label_x = int_svg.x + (arc_radius + 15) * math.cos(mid_angle)
    label_y = int_svg.y - (arc_radius + 15) * math.sin(mid_angle)
    builder.text('φ', Point(label_x, label_y), font_size=16, font_weight='bold', fill=COLORS['highlight'])
    
    # Fórmula
    phi_str = f'{phi_deg:.2f}°'
    formula = f'tan(φ) = |({m2}-{m1})/(1+{m1}·{m2})| → φ ≈ {phi_str}'
    builder.formula_box(formula, Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


# ============================================================================
# LUGAR GEOMÉTRICO
# ============================================================================

def render_lugar_circunferencia(output_path: str, 
                                 centro: tuple = (0, 0), radio: float = 5,
                                 title: str = "Lugar Geométrico: Circunferencia"):
    """
    Renderiza una circunferencia como lugar geométrico.
    Para: 01-concepto-lugar-geometrico.md
    """
    import math
    
    cx, cy = centro
    coord = CoordinateSystem(
        svg_width=600, svg_height=520,
        x_range=(cx - radio - 2, cx + radio + 2), 
        y_range=(cy - radio - 2, cy + radio + 2),
        padding=50
    )
    
    builder = SVGBuilder(600, 520)
    builder.rect(0, 0, 600, 520, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Circunferencia
    centro_svg = coord.to_svg(Point(cx, cy))
    radio_svg = abs(coord.to_svg(Point(cx + radio, cy)).x - centro_svg.x)
    builder.circle(centro_svg, radio_svg, fill='none', stroke=COLORS['primary'], stroke_width=2.5)
    
    # Centro
    coord.draw_point(builder, Point(cx, cy), label='C', color=COLORS['accent'], radius=5)
    
    # Algunos puntos sobre la circunferencia
    angles = [0, 45, 90, 135, 225, 315]
    for i, angle in enumerate(angles):
        rad = math.radians(angle)
        px = cx + radio * math.cos(rad)
        py = cy + radio * math.sin(rad)
        coord.draw_point(builder, Point(px, py), label=f'P{i+1}', color=COLORS['point'], radius=4)
    
    # Radio (línea desde centro a un punto)
    p_radio = Point(cx + radio * math.cos(math.radians(45)), 
                    cy + radio * math.sin(math.radians(45)))
    svg_centro = coord.to_svg(Point(cx, cy))
    svg_p = coord.to_svg(p_radio)
    builder.line(svg_centro, svg_p, stroke=COLORS['secondary'], stroke_width=2)
    
    # Etiqueta del radio
    mid_radio = svg_centro.midpoint(svg_p)
    builder.text(f'r = {int(radio)}', Point(mid_radio.x + 10, mid_radio.y - 10), 
                 font_size=12, font_weight='bold', fill=COLORS['secondary'])
    
    # Fórmula
    formula = f'Todos los puntos a distancia {int(radio)} del centro → x² + y² = {int(radio**2)}'
    builder.formula_box(formula, Point(300, 490), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_tabulacion(output_path: str, title: str = "Gráfica por Tabulación: y = x² - 4"):
    """
    Renderiza una parábola con puntos tabulados.
    Para: 02-ecuacion-grafica.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(-4, 4), y_range=(-5, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Dibujar la parábola como segmentos
    import math
    points = []
    for x in [i * 0.2 for i in range(-15, 16)]:
        y = x**2 - 4
        if -5 <= y <= 6:
            points.append(Point(x, y))
    
    # Dibujar curva
    for i in range(len(points) - 1):
        svg_p1 = coord.to_svg(points[i])
        svg_p2 = coord.to_svg(points[i + 1])
        builder.line(svg_p1, svg_p2, stroke=COLORS['primary'], stroke_width=2.5)
    
    # Puntos tabulados
    tabla = [(-3, 5), (-2, 0), (-1, -3), (0, -4), (1, -3), (2, 0), (3, 5)]
    for x, y in tabla:
        coord.draw_point(builder, Point(x, y), label='', color=COLORS['point'], radius=5)
        svg_p = coord.to_svg(Point(x, y))
        builder.text(f'({x},{y})', Point(svg_p.x + 8, svg_p.y - 8), 
                     font_size=9, fill=COLORS['text'])
    
    # Vértice destacado
    coord.draw_point(builder, Point(0, -4), label='V', color=COLORS['accent'], radius=6)
    
    # Interceptos X
    builder.text('Interceptos X', Point(coord.to_svg(Point(-2, 0)).x - 50, coord.to_svg(Point(-2, 0)).y - 15), 
                 font_size=10, fill=COLORS['secondary'])
    builder.text('Interceptos X', Point(coord.to_svg(Point(2, 0)).x + 10, coord.to_svg(Point(2, 0)).y - 15), 
                 font_size=10, fill=COLORS['secondary'])
    
    # Fórmula
    builder.formula_box('y = x² - 4  |  Vértice: (0, -4)', Point(300, 470), font_size=12)
    
    builder.save(output_path)
    return True


def render_analisis_curva(output_path: str, title: str = "Análisis de Curva: Interceptos y Simetría"):
    """
    Renderiza una curva con sus características marcadas.
    Para: 03-analisis-curvas.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(-1, 5), y_range=(-2, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Parábola y = x² - 4x + 3 = (x-1)(x-3)
    points = []
    for x in [i * 0.1 for i in range(-5, 55)]:
        y = x**2 - 4*x + 3
        if -2 <= y <= 5:
            points.append(Point(x, y))
    
    for i in range(len(points) - 1):
        svg_p1 = coord.to_svg(points[i])
        svg_p2 = coord.to_svg(points[i + 1])
        builder.line(svg_p1, svg_p2, stroke=COLORS['primary'], stroke_width=2.5)
    
    # Intercepto Y
    coord.draw_point(builder, Point(0, 3), label='', color='#22c55e', radius=6)
    svg_iy = coord.to_svg(Point(0, 3))
    builder.text('Int. Y: (0, 3)', Point(svg_iy.x + 10, svg_iy.y - 5), 
                 font_size=10, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Interceptos X
    coord.draw_point(builder, Point(1, 0), label='', color='#ef4444', radius=6)
    coord.draw_point(builder, Point(3, 0), label='', color='#ef4444', radius=6)
    svg_ix1 = coord.to_svg(Point(1, 0))
    svg_ix2 = coord.to_svg(Point(3, 0))
    builder.text('(1, 0)', Point(svg_ix1.x, svg_ix1.y + 18), 
                 font_size=10, font_weight='bold', fill='#ef4444')
    builder.text('(3, 0)', Point(svg_ix2.x, svg_ix2.y + 18), 
                 font_size=10, font_weight='bold', fill='#ef4444')
    
    # Vértice
    coord.draw_point(builder, Point(2, -1), label='V', color=COLORS['accent'], radius=6)
    svg_v = coord.to_svg(Point(2, -1))
    builder.text('Vértice (2, -1)', Point(svg_v.x + 10, svg_v.y + 5), 
                 font_size=10, font_weight='bold', fill=COLORS['accent'], anchor='start')
    
    # Eje de simetría
    svg_eje_top = coord.to_svg(Point(2, 5))
    svg_eje_bot = coord.to_svg(Point(2, -2))
    builder.line(svg_eje_top, svg_eje_bot, stroke='#a855f7', stroke_width=1.5, dashed=True)
    builder.text('x = 2', Point(svg_eje_top.x + 10, svg_eje_top.y + 15), 
                 font_size=10, fill='#a855f7')
    
    # Fórmula
    builder.formula_box('y = x² - 4x + 3 = (x-1)(x-3)', Point(300, 470), font_size=12)
    
    builder.save(output_path)
    return True


def render_mediatriz(output_path: str, 
                     a: tuple = (1, 1), b: tuple = (5, 5),
                     title: str = "Lugar Geométrico: Mediatriz"):
    """
    Renderiza la mediatriz entre dos puntos.
    Para: 04-construccion-ecuaciones.md
    """
    import math
    
    ax, ay = a
    bx, by = b
    
    # Punto medio
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(-1, 7), y_range=(-1, 7),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Segmento AB
    coord.draw_segment(builder, Point(ax, ay), Point(bx, by), color=COLORS['auxiliary'], width=2)
    
    # Mediatriz (perpendicular al segmento AB pasando por M)
    # Pendiente de AB
    if bx != ax:
        m_ab = (by - ay) / (bx - ax)
        if m_ab != 0:
            m_med = -1 / m_ab  # Pendiente perpendicular
        else:
            m_med = float('inf')
    else:
        m_med = 0  # Si AB es vertical, mediatriz es horizontal
    
    # Dibujar mediatriz
    if m_med != float('inf'):
        x1_med, x2_med = -1, 7
        y1_med = my + m_med * (x1_med - mx)
        y2_med = my + m_med * (x2_med - mx)
        coord.draw_segment(builder, Point(x1_med, y1_med), Point(x2_med, y2_med), 
                          color=COLORS['primary'], width=2.5)
    else:
        coord.draw_segment(builder, Point(mx, -1), Point(mx, 7), 
                          color=COLORS['primary'], width=2.5)
    
    # Puntos A y B
    coord.draw_point(builder, Point(ax, ay), label='A', show_coords=True, color='#ef4444')
    coord.draw_point(builder, Point(bx, by), label='B', show_coords=True, color='#ef4444',
                     label_offset=(-50, -10))
    
    # Punto medio M
    coord.draw_point(builder, Point(mx, my), label='M', color=COLORS['accent'], radius=5)
    
    # Un punto P sobre la mediatriz
    px = 1
    py = my + m_med * (px - mx) if m_med != float('inf') else my
    coord.draw_point(builder, Point(px, py), label='P', color=COLORS['secondary'], radius=5)
    
    # Líneas PA y PB (mostrando equidistancia)
    svg_p = coord.to_svg(Point(px, py))
    svg_a = coord.to_svg(Point(ax, ay))
    svg_b = coord.to_svg(Point(bx, by))
    builder.line(svg_p, svg_a, stroke='#22c55e', stroke_width=1.5, dashed=True)
    builder.line(svg_p, svg_b, stroke='#22c55e', stroke_width=1.5, dashed=True)
    
    # Distancias
    da = math.sqrt((px - ax)**2 + (py - ay)**2)
    db = math.sqrt((px - bx)**2 + (py - by)**2)
    
    # Fórmula
    formula = f'd(P,A) = d(P,B) → Mediatriz de AB'
    builder.formula_box(formula, Point(300, 470), font_size=12)
    
    builder.save(output_path)
    return True


# ============================================================================
# LÍNEA RECTA
# ============================================================================

def render_ecuacion_general(output_path: str, title: str = "Ecuación General: Ax + By + C = 0"):
    """
    Renderiza una recta con sus interceptos.
    Para: 01-ecuacion-general-recta.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-2, 6), y_range=(-1, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=14, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta 2x + 3y - 6 = 0 → intercepto X: 3, intercepto Y: 2
    coord.draw_segment(builder, Point(-0.5, 2.33), Point(5, -1.33), color=COLORS['primary'], width=2.5)
    
    # Interceptos
    coord.draw_point(builder, Point(3, 0), label='', color='#ef4444', radius=6)
    coord.draw_point(builder, Point(0, 2), label='', color='#22c55e', radius=6)
    
    svg_ix = coord.to_svg(Point(3, 0))
    svg_iy = coord.to_svg(Point(0, 2))
    
    builder.text('Int. X: (3, 0)', Point(svg_ix.x + 10, svg_ix.y + 18), 
                 font_size=10, font_weight='bold', fill='#ef4444', anchor='start')
    builder.text('Int. Y: (0, 2)', Point(svg_iy.x + 10, svg_iy.y - 5), 
                 font_size=10, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Etiqueta de la recta
    svg_label = coord.to_svg(Point(4, 0.67))
    builder.text('2x + 3y - 6 = 0', Point(svg_label.x, svg_label.y - 15), 
                 font_size=11, font_weight='bold', fill=COLORS['primary'])
    
    builder.formula_box('m = -A/B = -2/3  |  Int. X = -C/A  |  Int. Y = -C/B', Point(300, 450), font_size=10)
    
    builder.save(output_path)
    return True


def render_punto_pendiente(output_path: str, title: str = "Forma Punto-Pendiente"):
    """
    Renderiza una recta pasando por un punto con pendiente dada.
    Para: 02-forma-punto-pendiente.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-1, 7), y_range=(-1, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Punto conocido y pendiente m = 2/3
    p1 = Point(2, 1)
    m = 2/3
    
    # Recta: y - 1 = (2/3)(x - 2)
    x1, x2 = -0.5, 6.5
    y1 = 1 + m * (x1 - 2)
    y2 = 1 + m * (x2 - 2)
    
    coord.draw_segment(builder, Point(x1, y1), Point(x2, y2), color=COLORS['primary'], width=2.5)
    
    # Punto conocido
    coord.draw_point(builder, p1, label='P₁', show_coords=True, color=COLORS['accent'], radius=6)
    
    # Triángulo de pendiente
    p2 = Point(5, 3)
    coord.draw_right_triangle(builder, p1, p2, color=COLORS['auxiliary'], fill='#fef3c7')
    
    svg_p1 = coord.to_svg(p1)
    svg_p2 = coord.to_svg(p2)
    svg_aux = coord.to_svg(Point(5, 1))
    
    builder.text('Δx = 3', Point(svg_p1.midpoint(svg_aux).x, svg_p1.midpoint(svg_aux).y + 18), 
                 font_size=11, font_weight='bold', fill='#22c55e')
    builder.text('Δy = 2', Point(svg_aux.midpoint(svg_p2).x + 15, svg_aux.midpoint(svg_p2).y), 
                 font_size=11, font_weight='bold', fill='#f97316')
    
    builder.formula_box('y - y₁ = m(x - x₁)  →  y - 1 = ⅔(x - 2)', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_pendiente_ordenada(output_path: str, title: str = "Forma Pendiente-Ordenada: y = mx + b"):
    """
    Renderiza una recta mostrando m y b.
    Para: 03-forma-pendiente-ordenada.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-2, 5), y_range=(-1, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # y = x + 1 (m=1, b=1)
    coord.draw_segment(builder, Point(-1.5, -0.5), Point(4, 5), color=COLORS['primary'], width=2.5)
    
    # Intercepto Y (b)
    coord.draw_point(builder, Point(0, 1), label='b', color='#22c55e', radius=6)
    svg_b = coord.to_svg(Point(0, 1))
    builder.text('b = 1', Point(svg_b.x + 15, svg_b.y), font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Triángulo de pendiente
    coord.draw_right_triangle(builder, Point(1, 2), Point(2, 3), color=COLORS['auxiliary'], fill='#fef3c7')
    svg_m = coord.to_svg(Point(2, 2.5))
    builder.text('m = 1', Point(svg_m.x + 10, svg_m.y), font_size=11, font_weight='bold', fill='#f97316', anchor='start')
    
    builder.formula_box('y = mx + b  →  y = 1·x + 1  →  y = x + 1', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_recta_dos_puntos(output_path: str, title: str = "Recta por Dos Puntos"):
    """
    Renderiza una recta pasando por dos puntos.
    Para: 04-recta-dos-puntos.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-1, 7), y_range=(-1, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    p1 = Point(1, 1)
    p2 = Point(5, 4)
    
    # Extender la recta
    m = (4 - 1) / (5 - 1)
    x1, x2 = -0.5, 6.5
    y1 = 1 + m * (x1 - 1)
    y2 = 1 + m * (x2 - 1)
    
    coord.draw_segment(builder, Point(x1, y1), Point(x2, y2), color=COLORS['primary'], width=2.5)
    
    # Puntos
    coord.draw_point(builder, p1, label='P₁', show_coords=True, color=COLORS['accent'], radius=6)
    coord.draw_point(builder, p2, label='P₂', show_coords=True, color=COLORS['secondary'], radius=6,
                     label_offset=(-60, -10))
    
    builder.formula_box('(y - y₁)/(y₂ - y₁) = (x - x₁)/(x₂ - x₁)', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_forma_simetrica(output_path: str, title: str = "Forma Simétrica: x/a + y/b = 1"):
    """
    Renderiza una recta con interceptos a y b.
    Para: 05-forma-simetrica.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-1, 6), y_range=(-1, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # x/4 + y/3 = 1 → interceptos (4,0) y (0,3)
    # La recta pasa exactamente por (0,3) y (4,0)
    # Extendemos: cuando x=-1, y = 3*(1 - (-1)/4) = 3*1.25 = 3.75
    # cuando x=5, y = 3*(1 - 5/4) = 3*(-0.25) = -0.75
    coord.draw_segment(builder, Point(0, 3), Point(4, 0), color=COLORS['primary'], width=2.5)
    
    # Interceptos
    coord.draw_point(builder, Point(4, 0), label='', color='#ef4444', radius=6)
    coord.draw_point(builder, Point(0, 3), label='', color='#22c55e', radius=6)
    
    svg_a = coord.to_svg(Point(4, 0))
    svg_b = coord.to_svg(Point(0, 3))
    
    builder.text('a = 4', Point(svg_a.x, svg_a.y + 20), font_size=12, font_weight='bold', fill='#ef4444')
    builder.text('b = 3', Point(svg_b.x + 15, svg_b.y), font_size=12, font_weight='bold', fill='#22c55e', anchor='start')
    
    builder.formula_box('x/a + y/b = 1  →  x/4 + y/3 = 1', Point(300, 450), font_size=12)
    
    builder.save(output_path)
    return True


def render_forma_normal(output_path: str, title: str = "Forma Normal de la Recta"):
    """
    Renderiza una recta con distancia p y ángulo ω.
    Para: 06-forma-normal.md
    """
    import math
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-1, 6), y_range=(-1, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta con p=2, ω=45°
    omega = math.radians(45)
    p = 2
    
    # La recta: x·cos(ω) + y·sin(ω) = p
    # Puntos en la recta
    x1, x2 = -0.5, 5
    y1 = (p - x1 * math.cos(omega)) / math.sin(omega)
    y2 = (p - x2 * math.cos(omega)) / math.sin(omega)
    
    coord.draw_segment(builder, Point(x1, y1), Point(x2, y2), color=COLORS['primary'], width=2.5)
    
    # Perpendicular desde origen
    px = p * math.cos(omega)
    py = p * math.sin(omega)
    
    svg_o = coord.to_svg(Point(0, 0))
    svg_p = coord.to_svg(Point(px, py))
    builder.line(svg_o, svg_p, stroke=COLORS['accent'], stroke_width=2)
    
    # Punto pie de perpendicular
    coord.draw_point(builder, Point(px, py), label='', color=COLORS['accent'], radius=5)
    
    # Etiqueta p
    mid_p = svg_o.midpoint(svg_p)
    builder.text('p', Point(mid_p.x - 15, mid_p.y), font_size=14, font_weight='bold', fill=COLORS['accent'])
    
    # Arco del ángulo ω
    arc_radius = 30
    end_x = svg_o.x + arc_radius * math.cos(omega)
    end_y = svg_o.y - arc_radius * math.sin(omega)
    arc_path = f'M {svg_o.x + arc_radius} {svg_o.y} A {arc_radius} {arc_radius} 0 0 0 {end_x} {end_y}'
    builder.path(arc_path, fill='none', stroke=COLORS['highlight'], stroke_width=2)
    builder.text('ω', Point(svg_o.x + 40, svg_o.y - 15), font_size=14, font_weight='bold', fill=COLORS['highlight'])
    
    builder.formula_box('x·cos(ω) + y·sin(ω) = p', Point(300, 450), font_size=12)
    
    builder.save(output_path)
    return True


def render_distancia_punto_recta(output_path: str, title: str = "Distancia de Punto a Recta"):
    """
    Renderiza un punto con su perpendicular a una recta.
    Para: 07-distancia-punto-recta.md
    """
    import math
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-1, 7), y_range=(-1, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta: x + y - 2 = 0 (pasa por (2,0) y (0,2))
    coord.draw_segment(builder, Point(-0.5, 2.5), Point(6, -4), color=COLORS['primary'], width=2.5)
    
    # Punto P(4, 3)
    P = Point(4, 3)
    coord.draw_point(builder, P, label='P', show_coords=True, color=COLORS['accent'], radius=6)
    
    # Pie de la perpendicular: proyección de P sobre la recta
    # Para x + y - 2 = 0, el pie es ((x0+2-y0)/2, (y0+2-x0)/2)
    pie_x = (4 + 2 - 3) / 2
    pie_y = (3 + 2 - 4) / 2
    pie = Point(pie_x + 0.5, pie_y + 0.5)  # Ajuste visual
    
    # Perpendicular
    svg_p = coord.to_svg(P)
    svg_pie = coord.to_svg(pie)
    builder.line(svg_p, svg_pie, stroke=COLORS['secondary'], stroke_width=2, dashed=True)
    
    # Etiqueta d
    mid_d = svg_p.midpoint(svg_pie)
    builder.text('d', Point(mid_d.x + 10, mid_d.y), font_size=14, font_weight='bold', fill=COLORS['secondary'])
    
    # Marca de ángulo recto
    builder.text('⊥', Point(svg_pie.x + 10, svg_pie.y - 10), font_size=12, fill=COLORS['auxiliary'])
    
    builder.formula_box('d = |Ax₀ + By₀ + C| / √(A² + B²)', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_familias_rectas(output_path: str, title: str = "Familia de Rectas (Haz)"):
    """
    Renderiza un haz de rectas por un punto.
    Para: 08-familias-de-rectas.md
    """
    import math
    
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-3, 5), y_range=(-2, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Punto común
    centro = Point(1, 2)
    
    # Varias rectas pasando por el punto
    pendientes = [-2, -1, -0.5, 0, 0.5, 1, 2]
    colores = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#06b6d4', '#3b82f6', '#8b5cf6']
    
    for m, color in zip(pendientes, colores):
        x1, x2 = -2.5, 4.5
        y1 = 2 + m * (x1 - 1)
        y2 = 2 + m * (x2 - 1)
        coord.draw_segment(builder, Point(x1, y1), Point(x2, y2), color=color, width=1.5)
    
    # Punto común destacado
    coord.draw_point(builder, centro, label='P₀', show_coords=True, color='#1e293b', radius=7)
    
    builder.formula_box('Todas pasan por P₀(1, 2) con diferentes pendientes', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_rectas_notables(output_path: str, title: str = "Rectas Notables del Triángulo"):
    """
    Renderiza un triángulo con medianas.
    Para: 09-rectas-notables-triangulo.md
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(-1, 7), y_range=(-1, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Triángulo
    A = Point(1, 1)
    B = Point(6, 1)
    C = Point(3, 5)
    
    coord.draw_polygon(builder, [A, B, C], fill='#dbeafe', stroke=COLORS['primary'])
    
    # Puntos medios
    M_ab = A.midpoint(B)
    M_bc = B.midpoint(C)
    M_ca = C.midpoint(A)
    
    # Medianas
    coord.draw_segment(builder, A, M_bc, color='#ef4444', width=1.5)
    coord.draw_segment(builder, B, M_ca, color='#22c55e', width=1.5)
    coord.draw_segment(builder, C, M_ab, color='#3b82f6', width=1.5)
    
    # Baricentro
    G = Point((A.x + B.x + C.x) / 3, (A.y + B.y + C.y) / 3)
    coord.draw_point(builder, G, label='G', color=COLORS['accent'], radius=5)
    
    # Vértices
    coord.draw_point(builder, A, label='A', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, B, label='B', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, C, label='C', show_coords=True, color=COLORS['primary'], label_offset=(0, -15))
    
    builder.formula_box('Medianas: unen vértice con punto medio opuesto | G = baricentro', Point(300, 470), font_size=10)
    
    builder.save(output_path)
    return True


# ============================================================================
# ILUSTRACIONES ADICIONALES LÍNEA RECTA
# ============================================================================

def render_rectas_horizontales_verticales(output_path: str, title: str = "Rectas Horizontales y Verticales"):
    """Rectas especiales para lección 01."""
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-5, 5), y_range=(-4, 4),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Rectas horizontales
    coord.draw_segment(builder, Point(-5, 2), Point(5, 2), color='#3b82f6', width=2.5)
    coord.draw_segment(builder, Point(-5, -1), Point(5, -1), color='#22c55e', width=2.5)
    
    svg_h1 = coord.to_svg(Point(4, 2))
    svg_h2 = coord.to_svg(Point(4, -1))
    builder.text('y = 2 (A=0)', Point(svg_h1.x, svg_h1.y - 12), font_size=10, font_weight='bold', fill='#3b82f6')
    builder.text('y = -1 (A=0)', Point(svg_h2.x, svg_h2.y + 15), font_size=10, font_weight='bold', fill='#22c55e')
    
    # Rectas verticales
    coord.draw_segment(builder, Point(3, -4), Point(3, 4), color='#ef4444', width=2.5)
    coord.draw_segment(builder, Point(-2, -4), Point(-2, 4), color='#f97316', width=2.5)
    
    svg_v1 = coord.to_svg(Point(3, 3.5))
    svg_v2 = coord.to_svg(Point(-2, 3.5))
    builder.text('x = 3 (B=0)', Point(svg_v1.x + 8, svg_v1.y), font_size=10, font_weight='bold', fill='#ef4444', anchor='start')
    builder.text('x = -2 (B=0)', Point(svg_v2.x - 60, svg_v2.y), font_size=10, font_weight='bold', fill='#f97316')
    
    # Leyenda
    builder.rect(420, 390, 160, 75, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text('En Ax + By + C = 0:', Point(500, 408), font_size=10, font_weight='bold')
    builder.text('A = 0 → Horizontal', Point(435, 428), font_size=10, fill='#3b82f6', anchor='start')
    builder.text('B = 0 → Vertical', Point(435, 448), font_size=10, fill='#ef4444', anchor='start')
    
    builder.save(output_path)
    return True


def render_paralela_perpendicular_punto(output_path: str, title: str = "Paralela y Perpendicular por un Punto"):
    """Para lección 02."""
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-2, 7), y_range=(-2, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=14, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Recta original L: y = x (m = 1)
    coord.draw_segment(builder, Point(-1, -1), Point(6, 6), color='#64748b', width=2)
    svg_l = coord.to_svg(Point(5, 5))
    builder.text('L: m = 1', Point(svg_l.x + 5, svg_l.y - 10), font_size=10, fill='#64748b', anchor='start')
    
    # Punto P
    P = Point(2, 4)
    coord.draw_point(builder, P, label='P', show_coords=True, color=COLORS['accent'], radius=6)
    
    # Paralela por P: y - 4 = 1(x - 2) → y = x + 2
    coord.draw_segment(builder, Point(-1, 1), Point(4, 6), color='#22c55e', width=2.5)
    svg_par = coord.to_svg(Point(3.5, 5.5))
    builder.text('Paralela: m = 1', Point(svg_par.x - 80, svg_par.y - 10), font_size=10, font_weight='bold', fill='#22c55e')
    
    # Perpendicular por P: y - 4 = -1(x - 2) → y = -x + 6
    coord.draw_segment(builder, Point(0, 6), Point(6, 0), color='#ef4444', width=2.5)
    svg_perp = coord.to_svg(Point(5, 1))
    builder.text('Perpendicular: m = -1', Point(svg_perp.x - 10, svg_perp.y + 18), font_size=10, font_weight='bold', fill='#ef4444')
    
    # Símbolo perpendicular
    svg_int = coord.to_svg(Point(3, 3))
    builder.text('⊥', Point(svg_int.x + 10, svg_int.y - 10), font_size=14, fill='#ef4444')
    
    builder.formula_box('Paralela: m₁ = m  |  Perpendicular: m₂ = -1/m', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_graficar_pendiente_ordenada(output_path: str, title: str = "Graficar con Pendiente-Ordenada"):
    """Para lección 03."""
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-2, 6), y_range=(-2, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # y = (2/3)x + 1
    m = 2/3
    b = 1
    coord.draw_segment(builder, Point(-1.5, b + m*(-1.5)), Point(5.5, b + m*5.5), color=COLORS['primary'], width=2.5)
    
    # Paso 1: Marcar b en eje Y
    coord.draw_point(builder, Point(0, 1), label='', color='#22c55e', radius=7)
    svg_b = coord.to_svg(Point(0, 1))
    builder.text('① b = 1', Point(svg_b.x + 15, svg_b.y), font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Paso 2: Desde b, usar pendiente (avanzar 3, subir 2)
    coord.draw_right_triangle(builder, Point(0, 1), Point(3, 3), color='#f97316', fill='#fef3c7')
    
    svg_dx = coord.to_svg(Point(1.5, 1))
    svg_dy = coord.to_svg(Point(3, 2))
    builder.text('② Δx=3', Point(svg_dx.x, svg_dx.y + 18), font_size=10, font_weight='bold', fill='#f97316')
    builder.text('Δy=2', Point(svg_dy.x + 12, svg_dy.y), font_size=10, font_weight='bold', fill='#f97316')
    
    # Segundo punto
    coord.draw_point(builder, Point(3, 3), label='', color='#ef4444', radius=6)
    svg_p2 = coord.to_svg(Point(3, 3))
    builder.text('③ (3, 3)', Point(svg_p2.x + 10, svg_p2.y - 10), font_size=10, font_weight='bold', fill='#ef4444', anchor='start')
    
    builder.formula_box('y = ⅔x + 1  |  m = ⅔ = Δy/Δx  |  b = 1', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_rectas_paralelas_familia(output_path: str, title: str = "Familia de Rectas Paralelas"):
    """Para lección 08."""
    coord = CoordinateSystem(
        svg_width=600, svg_height=480,
        x_range=(-4, 4), y_range=(-4, 5),
        padding=50
    )
    
    builder = SVGBuilder(600, 480)
    builder.rect(0, 0, 600, 480, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Familia y = x + k con diferentes k
    ks = [-3, -1.5, 0, 1.5, 3]
    colores = ['#ef4444', '#f97316', '#22c55e', '#3b82f6', '#8b5cf6']
    
    for k, color in zip(ks, colores):
        x1, x2 = -3.5, 3.5
        y1 = x1 + k
        y2 = x2 + k
        coord.draw_segment(builder, Point(x1, y1), Point(x2, y2), color=color, width=2)
        
        # Etiqueta
        svg_label = coord.to_svg(Point(3, 3 + k))
        if -4 < 3 + k < 5:
            builder.text(f'k={k}', Point(svg_label.x + 5, svg_label.y), font_size=9, fill=color, anchor='start')
    
    builder.formula_box('y = x + k  |  Misma pendiente m = 1, diferente k', Point(300, 450), font_size=11)
    
    builder.save(output_path)
    return True


def render_alturas_ortocentro(output_path: str, title: str = "Alturas y Ortocentro"):
    """Para lección 09. Calculado con SymPy."""
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(-1, 7), y_range=(-1, 6),
        padding=50
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(title, Point(300, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Triángulo A(1,1), B(6,1), C(3,5)
    A = Point(1, 1)
    B = Point(6, 1)
    C = Point(3, 5)
    
    coord.draw_polygon(builder, [A, B, C], fill='#dbeafe', stroke=COLORS['primary'])
    
    # Alturas calculadas exactamente con SymPy
    # Altura desde A a BC: pie en (4.2, 3.4)
    coord.draw_segment(builder, A, Point(4.2, 3.4), color='#ef4444', width=1.5)
    # Altura desde B a AC: pie en (2, 3)
    coord.draw_segment(builder, B, Point(2, 3), color='#22c55e', width=1.5)
    # Altura desde C a AB: pie en (3, 1)
    coord.draw_segment(builder, C, Point(3, 1), color='#3b82f6', width=1.5)
    
    # Ortocentro H(3, 2.5)
    H = Point(3, 2.5)
    coord.draw_point(builder, H, label='H', color=COLORS['accent'], radius=5)
    
    # Vértices
    coord.draw_point(builder, A, label='A', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, B, label='B', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, C, label='C', show_coords=True, color=COLORS['primary'], label_offset=(0, -15))
    
    # Símbolos perpendicular en los pies
    svg_pie_c = coord.to_svg(Point(3, 1))
    builder.text('⊥', Point(svg_pie_c.x + 8, svg_pie_c.y - 8), font_size=10, fill='#3b82f6')
    
    builder.formula_box('Alturas: perpendiculares desde vértice al lado opuesto | H = ortocentro', Point(300, 470), font_size=10)
    
    builder.save(output_path)
    return True


def render_mediatrices_circuncentro(output_path: str, title: str = "Mediatrices y Circuncentro"):
    """Para lección 09. Calculado con SymPy.
    
    IMPORTANTE: Para dibujar un círculo correctamente, las escalas X y Y deben ser iguales.
    """
    import math
    
    # Para escala uniforme: usar mismo rango en ambos ejes
    # Rango X: 8 unidades (-1 a 7)
    # Rango Y: 8 unidades (-1.5 a 6.5) para que scale_x == scale_y
    
    svg_width = 600
    svg_height = 600  # Cuadrado para escala uniforme
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-1, 7), y_range=(-1.5, 6.5),  # 8 unidades en ambos ejes
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=1, show_labels=True)
    
    # Triángulo A(1,1), B(6,1), C(3,5)
    A = Point(1, 1)
    B = Point(6, 1)
    C = Point(3, 5)
    
    coord.draw_polygon(builder, [A, B, C], fill='#dbeafe', stroke=COLORS['primary'])
    
    # Puntos medios calculados
    M_ab = Point(3.5, 1)   # Punto medio AB
    M_bc = Point(4.5, 3)   # Punto medio BC
    M_ca = Point(2, 3)     # Punto medio CA
    
    # Circuncentro O(3.5, 2.25) calculado con SymPy
    O = Point(3.5, 2.25)
    
    # Radio circunscrito exacto = 2.7950849718747373
    r = 2.7950849718747373
    
    # Dibujar circunferencia - usar la escala uniforme
    svg_o = coord.to_svg(O)
    # Con escala uniforme, podemos usar cualquier eje para el radio
    svg_r = r * coord.scale_x  # scale_x == scale_y cuando es uniforme
    builder.circle(svg_o, svg_r, fill='none', stroke='#a855f7', stroke_width=1.5)
    
    # Mediatrices (pasan por punto medio, perpendiculares al lado)
    # Todas deben extenderse uniformemente más allá de la circunferencia
    
    # Mediatriz de AB: vertical x = 3.5 (desde y=-1 hasta y=6)
    coord.draw_segment(builder, Point(3.5, -1), Point(3.5, 6), color='#ef4444', width=1.5)
    
    # Mediatriz de BC: pasa por (4.5, 3) con pendiente 3/4
    # Extender desde x=0.5 hasta x=7 (fuera de la circunferencia en ambos lados)
    # y - 3 = (3/4)(x - 4.5) → y = 0.75x + (-3.375 + 3) = 0.75x - 0.375
    coord.draw_segment(builder, Point(0.5, 0), Point(7, 4.875), color='#22c55e', width=1.5)
    
    # Mediatriz de CA: pasa por (2, 3) con pendiente -1/2
    # y - 3 = (-1/2)(x - 2) → y = -0.5x + 4
    # Extender desde x=-1 hasta x=7
    coord.draw_segment(builder, Point(-1, 4.5), Point(7, 0.5), color='#3b82f6', width=1.5)
    
    # Puntos medios
    coord.draw_point(builder, M_ab, label='', color='#64748b', radius=4)
    coord.draw_point(builder, M_bc, label='', color='#64748b', radius=4)
    coord.draw_point(builder, M_ca, label='', color='#64748b', radius=4)
    
    # Circuncentro
    coord.draw_point(builder, O, label='O', color=COLORS['accent'], radius=5)
    
    # Vértices
    coord.draw_point(builder, A, label='A', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, B, label='B', show_coords=True, color=COLORS['primary'])
    coord.draw_point(builder, C, label='C', show_coords=True, color=COLORS['primary'], label_offset=(0, -15))
    
    builder.formula_box('Circunferencia circunscrita pasa por A, B, C | O = circuncentro', Point(svg_width/2, svg_height - 30), font_size=10)
    
    builder.save(output_path)
    return True


# ============================================================================
# CIRCUNFERENCIA - ILUSTRACIONES
# ============================================================================

def render_elementos_circunferencia(output_path: str, title: str = "Elementos de la Circunferencia"):
    """Lección 01: Definición - muestra centro, radio, diámetro, cuerda."""
    import math
    
    # Escala uniforme para círculo perfecto
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-6, 6), y_range=(-6, 6),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Circunferencia con centro C(1, 1) y radio 4
    C = Point(1, 1)
    r = 4
    
    # Dibujar circunferencia
    svg_c = coord.to_svg(C)
    svg_r = r * coord.scale_x
    builder.circle(svg_c, svg_r, fill='#dbeafe', fill_opacity=0.3, stroke=COLORS['primary'], stroke_width=2)
    
    # Radio: desde centro a punto (1+4, 1) = (5, 1)
    P_radio = Point(5, 1)
    coord.draw_segment(builder, C, P_radio, color=COLORS['accent'], width=2)
    # Etiqueta radio
    svg_mid_r = coord.to_svg(Point(3, 1))
    builder.text('r = 4', Point(svg_mid_r.x, svg_mid_r.y - 10), font_size=11, fill=COLORS['accent'], font_weight='bold')
    
    # Diámetro: de (-3, 1) a (5, 1)
    P_diam1 = Point(-3, 1)
    P_diam2 = Point(5, 1)
    coord.draw_segment(builder, P_diam1, P_diam2, color='#22c55e', width=2, dashed=True)
    svg_diam = coord.to_svg(Point(1, 1.5))
    builder.text('d = 2r = 8', Point(svg_diam.x, svg_diam.y - 25), font_size=10, fill='#22c55e')
    
    # Cuerda: de (1-4*cos(60°), 1+4*sin(60°)) a (1+4*cos(60°), 1+4*sin(60°))
    # Usando ángulo 60° = π/3
    angle = math.pi / 3
    P_cuerda1 = Point(1 - 4*math.cos(angle), 1 + 4*math.sin(angle))
    P_cuerda2 = Point(1 + 4*math.cos(angle), 1 + 4*math.sin(angle))
    coord.draw_segment(builder, P_cuerda1, P_cuerda2, color='#a855f7', width=2)
    svg_cuerda = coord.to_svg(Point(1, 1 + 4*math.sin(angle) + 0.3))
    builder.text('cuerda', Point(svg_cuerda.x, svg_cuerda.y - 10), font_size=10, fill='#a855f7')
    
    # Centro
    coord.draw_point(builder, C, label='C', show_coords=True, color=COLORS['accent'], radius=5)
    
    # Puntos en la circunferencia
    coord.draw_point(builder, P_radio, label='P', color=COLORS['primary'], radius=4)
    coord.draw_point(builder, P_diam1, label='', color='#22c55e', radius=4)
    coord.draw_point(builder, P_cuerda1, label='', color='#a855f7', radius=4)
    coord.draw_point(builder, P_cuerda2, label='', color='#a855f7', radius=4)
    
    builder.formula_box('Centro C(h,k) | Radio r | Diámetro d=2r | Cuerda', Point(svg_width/2, svg_height - 30), font_size=10)
    
    builder.save(output_path)
    return True


def render_ecuacion_ordinaria_circ(output_path: str, title: str = "Ecuación Ordinaria"):
    """Lección 02: Ecuación ordinaria (x-h)² + (y-k)² = r²."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-2, 10), y_range=(-2, 10),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Circunferencia: centro (3, 4), radio 3
    C = Point(3, 4)
    r = 3
    
    svg_c = coord.to_svg(C)
    svg_r = r * coord.scale_x
    builder.circle(svg_c, svg_r, fill='#dbeafe', fill_opacity=0.3, stroke=COLORS['primary'], stroke_width=2)
    
    # Punto P(x,y) genérico en la circunferencia (en ángulo 45°)
    angle = math.pi / 4
    P = Point(3 + 3*math.cos(angle), 4 + 3*math.sin(angle))
    
    # Radio desde C a P
    coord.draw_segment(builder, C, P, color=COLORS['accent'], width=2)
    
    # Líneas punteadas para mostrar (x-h) y (y-k)
    coord.draw_segment(builder, C, Point(P.x, C.y), color='#64748b', width=1, dashed=True)
    coord.draw_segment(builder, Point(P.x, C.y), P, color='#64748b', width=1, dashed=True)
    
    # Etiquetas
    svg_xh = coord.to_svg(Point((C.x + P.x)/2, C.y - 0.3))
    builder.text('x - h', Point(svg_xh.x, svg_xh.y + 15), font_size=10, fill='#64748b')
    
    svg_yk = coord.to_svg(Point(P.x + 0.3, (C.y + P.y)/2))
    builder.text('y - k', Point(svg_yk.x + 10, svg_yk.y), font_size=10, fill='#64748b')
    
    svg_r_label = coord.to_svg(Point((C.x + P.x)/2 - 0.3, (C.y + P.y)/2 + 0.3))
    builder.text('r', Point(svg_r_label.x - 10, svg_r_label.y), font_size=12, fill=COLORS['accent'], font_weight='bold')
    
    # Puntos
    coord.draw_point(builder, C, label='C(h, k)', color=COLORS['accent'], radius=5, label_offset=(-40, 15))
    coord.draw_point(builder, P, label='P(x, y)', color=COLORS['primary'], radius=4, label_offset=(10, -10))
    
    builder.formula_box('(x - h)² + (y - k)² = r²  |  C(3, 4), r = 3', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_posiciones_recta_circ(output_path: str, title: str = "Posiciones Recta-Circunferencia"):
    """Lección 05: Posiciones relativas - exterior, tangente, secante."""
    import math
    
    svg_width = 700
    svg_height = 280
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 20), font_size=14, font_weight='bold')
    
    # Tres mini-diagramas
    configs = [
        {'cx': 100, 'label': 'Exterior (d > r)', 'line_y': 180, 'color': '#ef4444'},
        {'cx': 350, 'label': 'Tangente (d = r)', 'line_y': 130, 'color': '#22c55e'},
        {'cx': 600, 'label': 'Secante (d < r)', 'line_y': 100, 'color': '#3b82f6'},
    ]
    
    for cfg in configs:
        cx, cy, r = cfg['cx'], 130, 50
        
        # Circunferencia
        builder.circle(Point(cx, cy), r, fill='#dbeafe', fill_opacity=0.3, stroke=COLORS['primary'], stroke_width=2)
        
        # Centro
        builder.circle(Point(cx, cy), 4, fill=COLORS['accent'])
        
        # Recta horizontal
        builder.line(Point(cx - 80, cfg['line_y']), Point(cx + 80, cfg['line_y']), 
                    stroke=cfg['color'], stroke_width=2)
        
        # Distancia d (línea punteada vertical)
        builder.line(Point(cx, cy), Point(cx, cfg['line_y']), 
                    stroke='#64748b', stroke_width=1, dashed=True)
        builder.text('d', Point(cx + 8, (cy + cfg['line_y'])/2), font_size=10, fill='#64748b')
        
        # Etiqueta
        builder.text(cfg['label'], Point(cx, 250), font_size=11, fill=cfg['color'], font_weight='bold')
    
    builder.save(output_path)
    return True


def render_posiciones_dos_circ(output_path: str, title: str = "Posiciones entre Circunferencias"):
    """Lección 05: Posiciones relativas entre dos circunferencias."""
    import math
    
    svg_width = 700
    svg_height = 300
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 20), font_size=14, font_weight='bold')
    
    # Cuatro configuraciones
    configs = [
        {'cx1': 60, 'cx2': 150, 'r1': 30, 'r2': 25, 'label': 'Externas'},
        {'cx1': 250, 'cx2': 305, 'r1': 30, 'r2': 25, 'label': 'Tang. Ext.'},
        {'cx1': 420, 'cx2': 450, 'r1': 40, 'r2': 25, 'label': 'Secantes'},
        {'cx1': 590, 'cx2': 600, 'r1': 50, 'r2': 20, 'label': 'Internas'},
    ]
    
    cy = 140
    colors = ['#3b82f6', '#22c55e']
    
    for cfg in configs:
        # Circunferencia 1
        builder.circle(Point(cfg['cx1'], cy), cfg['r1'], fill='#dbeafe', fill_opacity=0.3, 
                      stroke=colors[0], stroke_width=2)
        builder.circle(Point(cfg['cx1'], cy), 3, fill=colors[0])
        
        # Circunferencia 2
        builder.circle(Point(cfg['cx2'], cy), cfg['r2'], fill='#dcfce7', fill_opacity=0.3, 
                      stroke=colors[1], stroke_width=2)
        builder.circle(Point(cfg['cx2'], cy), 3, fill=colors[1])
        
        # Etiqueta
        mid_x = (cfg['cx1'] + cfg['cx2']) / 2
        builder.text(cfg['label'], Point(mid_x, 250), font_size=10, font_weight='bold')
    
    builder.save(output_path)
    return True


def render_circunferencias_concentricas(output_path: str, title: str = "Circunferencias Concéntricas"):
    """Lección 06: Familia de circunferencias concéntricas."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-6, 6), y_range=(-6, 6),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Centro común
    C = Point(0, 0)
    svg_c = coord.to_svg(C)
    
    # Familia de circunferencias con radios 1, 2, 3, 4, 5
    colors = ['#fecaca', '#fed7aa', '#fef08a', '#bbf7d0', '#bfdbfe']
    radii = [1, 2, 3, 4, 5]
    
    for i, r in enumerate(reversed(radii)):  # Dibujar de mayor a menor
        svg_r = r * coord.scale_x
        color_idx = len(radii) - 1 - i
        builder.circle(svg_c, svg_r, fill=colors[color_idx], fill_opacity=0.4, 
                      stroke=COLORS['primary'], stroke_width=1.5)
    
    # Centro
    coord.draw_point(builder, C, label='C(0, 0)', color=COLORS['accent'], radius=5)
    
    # Etiquetas de radios
    for r in radii:
        svg_label = coord.to_svg(Point(r + 0.2, 0.3))
        builder.text(f'r={r}', Point(svg_label.x, svg_label.y), font_size=9, fill='#64748b')
    
    builder.formula_box('x² + y² = r²  |  Mismo centro, diferentes radios', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_tangente_circunferencia(output_path: str, title: str = "Recta Tangente"):
    """Lección 07: Tangente a la circunferencia desde un punto.
    
    Calculado con SymPy:
    - Circunferencia: x² + y² = 16 (centro origen, radio 4)
    - Punto de tangencia: P(3, √7) ≈ (3, 2.6458)
    - Verificación: 9 + 7 = 16 ✓
    - Tangente: 3x + √7·y = 16
    - Distancia centro-recta = 16/√16 = 4 = r ✓
    """
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-6, 6), y_range=(-6, 6),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Circunferencia x² + y² = 16, centro (0,0), radio 4
    C = Point(0, 0)
    r = 4
    
    svg_c = coord.to_svg(C)
    svg_r = r * coord.scale_x
    builder.circle(svg_c, svg_r, fill='#dbeafe', fill_opacity=0.3, stroke=COLORS['primary'], stroke_width=2)
    
    # Punto de tangencia P(3, √7) calculado con SymPy
    # 3² + (√7)² = 9 + 7 = 16 ✓
    sqrt7 = math.sqrt(7)  # ≈ 2.6458
    P = Point(3, sqrt7)
    
    # Radio al punto de tangencia
    coord.draw_segment(builder, C, P, color=COLORS['accent'], width=2)
    
    # Tangente: 3x + √7·y = 16
    # Despejando: y = (16 - 3x) / √7
    # Puntos calculados con SymPy:
    # x = -2: y ≈ 8.3152
    # x = 6: y ≈ -0.7559
    y_at_minus2 = (16 - 3*(-2)) / sqrt7  # ≈ 8.3152
    y_at_6 = (16 - 3*6) / sqrt7  # ≈ -0.7559
    coord.draw_segment(builder, Point(-2, y_at_minus2), Point(6, y_at_6), color='#22c55e', width=2)
    
    # Símbolo de perpendicular
    svg_p = coord.to_svg(P)
    builder.text('⊥', Point(svg_p.x + 15, svg_p.y - 5), font_size=12, fill='#22c55e')
    
    # Puntos
    coord.draw_point(builder, C, label='C(0, 0)', color=COLORS['accent'], radius=5)
    coord.draw_point(builder, P, label='P(3, √7)', color=COLORS['primary'], radius=4, label_offset=(10, -10))
    
    # Etiqueta tangente
    svg_tang = coord.to_svg(Point(4.5, 0.5))
    builder.text('3x + √7y = 16', Point(svg_tang.x, svg_tang.y), font_size=10, fill='#22c55e', font_weight='bold')
    
    builder.formula_box('Tangente ⊥ radio | Ecuación: x₀x + y₀y = r²', Point(svg_width/2, svg_height - 30), font_size=10)
    
    builder.save(output_path)
    return True


def render_circ_por_punto_fijo(output_path: str, title: str = "Circunferencias por un Punto Fijo"):
    """Familia de circunferencias que pasan por el origen con centro en eje X."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-4, 8), y_range=(-4, 8),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Familia: circunferencias que pasan por origen con centro en eje X
    # Centro (h, 0), radio = h, ecuación: (x-h)² + y² = h²
    colors = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#3b82f6']
    h_values = [1, 2, 3, 4, 5]
    
    for i, h in enumerate(h_values):
        center = Point(h, 0)
        svg_c = coord.to_svg(center)
        svg_r = h * coord.scale_x
        builder.circle(svg_c, svg_r, fill='none', stroke=colors[i], stroke_width=1.5)
        # Centro pequeño
        builder.circle(svg_c, 3, fill=colors[i])
    
    # Punto fijo (origen)
    coord.draw_point(builder, Point(0, 0), label='O (punto fijo)', color=COLORS['accent'], radius=6, label_offset=(10, 15))
    
    builder.formula_box('(x - h)² + y² = h²  |  Todas pasan por el origen', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_circ_tangentes_recta(output_path: str, title: str = "Circunferencias Tangentes al Eje X"):
    """Familia de circunferencias tangentes al eje X en un punto."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-2, 10), y_range=(-2, 10),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Familia: tangentes al eje X en (3, 0)
    # Centro (3, k), radio = |k|
    colors = ['#3b82f6', '#22c55e', '#eab308', '#f97316']
    k_values = [1, 2, 3, 4]
    
    for i, k in enumerate(k_values):
        center = Point(3, k)
        svg_c = coord.to_svg(center)
        svg_r = k * coord.scale_x
        builder.circle(svg_c, svg_r, fill='none', stroke=colors[i], stroke_width=1.5, fill_opacity=0.1)
        # Centro
        builder.circle(svg_c, 3, fill=colors[i])
    
    # Punto de tangencia
    coord.draw_point(builder, Point(3, 0), label='(3, 0)', color=COLORS['accent'], radius=5, label_offset=(10, 15))
    
    # Línea vertical x = 3 (lugar de centros)
    coord.draw_segment(builder, Point(3, 0.5), Point(3, 8), color='#64748b', width=1, dashed=True)
    svg_label = coord.to_svg(Point(3.3, 7))
    builder.text('x = 3', Point(svg_label.x, svg_label.y), font_size=10, fill='#64748b')
    
    builder.formula_box('(x - 3)² + (y - k)² = k²  |  Tangentes en (3, 0)', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_haz_circunferencias(output_path: str, title: str = "Haz de Circunferencias"):
    """Haz de circunferencias que pasan por dos puntos de intersección."""
    import math
    from sympy import sqrt, Rational, symbols, solve, Eq
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-4, 6), y_range=(-4, 6),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # C1: x² + y² = 4 (centro origen, radio 2)
    # C2: x² + y² - 2x - 2y = 0 → (x-1)² + (y-1)² = 2 (centro (1,1), radio √2)
    
    # C1
    svg_c1 = coord.to_svg(Point(0, 0))
    svg_r1 = 2 * coord.scale_x
    builder.circle(svg_c1, svg_r1, fill='none', stroke='#3b82f6', stroke_width=2)
    
    # C2
    svg_c2 = coord.to_svg(Point(1, 1))
    svg_r2 = math.sqrt(2) * coord.scale_x
    builder.circle(svg_c2, svg_r2, fill='none', stroke='#22c55e', stroke_width=2)
    
    # Puntos de intersección (calculados con SymPy)
    # x² + y² = 4 y x² + y² - 2x - 2y = 0
    # Restando: 2x + 2y = 4 → x + y = 2
    # Sustituyendo y = 2 - x en x² + y² = 4:
    # x² + (2-x)² = 4 → 2x² - 4x = 0 → x(x-2) = 0
    # x = 0 → y = 2, x = 2 → y = 0
    P1 = Point(0, 2)
    P2 = Point(2, 0)
    
    coord.draw_point(builder, P1, label='P₁', color=COLORS['accent'], radius=5)
    coord.draw_point(builder, P2, label='P₂', color=COLORS['accent'], radius=5)
    
    # Miembro del haz con λ = 0.5
    # (1+0.5)(x²+y²) - 2(0.5)x - 2(0.5)y - 4 = 0
    # 1.5(x²+y²) - x - y - 4 = 0
    # Centro: (1/3, 1/3), radio calculado
    svg_c3 = coord.to_svg(Point(1/3, 1/3))
    # Radio: sqrt((1/3)² + (1/3)² + 4/1.5) ≈ 1.76
    svg_r3 = 1.76 * coord.scale_x
    builder.circle(svg_c3, svg_r3, fill='none', stroke='#a855f7', stroke_width=1.5, fill_opacity=0.1)
    
    # Etiquetas
    svg_label1 = coord.to_svg(Point(-1.5, 1.5))
    builder.text('C₁', Point(svg_label1.x, svg_label1.y), font_size=11, fill='#3b82f6', font_weight='bold')
    svg_label2 = coord.to_svg(Point(2, 2))
    builder.text('C₂', Point(svg_label2.x, svg_label2.y), font_size=11, fill='#22c55e', font_weight='bold')
    
    # Centros
    coord.draw_point(builder, Point(0, 0), label='', color='#3b82f6', radius=3)
    coord.draw_point(builder, Point(1, 1), label='', color='#22c55e', radius=3)
    
    builder.formula_box('C₁ + λC₂ = 0  |  Todas pasan por P₁ y P₂', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_eje_radical(output_path: str, title: str = "Eje Radical"):
    """Eje radical de dos circunferencias."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-2, 8), y_range=(-2, 8),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # C1: centro (2, 3), radio 2
    # C2: centro (5, 3), radio 2.5
    C1 = Point(2, 3)
    r1 = 2
    C2 = Point(5, 3)
    r2 = 2.5
    
    svg_c1 = coord.to_svg(C1)
    svg_r1 = r1 * coord.scale_x
    builder.circle(svg_c1, svg_r1, fill='#dbeafe', fill_opacity=0.3, stroke='#3b82f6', stroke_width=2)
    
    svg_c2 = coord.to_svg(C2)
    svg_r2 = r2 * coord.scale_x
    builder.circle(svg_c2, svg_r2, fill='#dcfce7', fill_opacity=0.3, stroke='#22c55e', stroke_width=2)
    
    # Eje radical: recta perpendicular a la línea de centros
    # Para estas circunferencias, el eje radical es vertical en x ≈ 3.375
    # Calculado: (r1² - r2² + d²) / (2d) donde d = 3
    # x = 2 + (4 - 6.25 + 9) / 6 = 2 + 6.75/6 = 2 + 1.125 = 3.125
    x_radical = 3.125
    coord.draw_segment(builder, Point(x_radical, -1), Point(x_radical, 7), color='#ef4444', width=2)
    
    # Etiqueta
    svg_label = coord.to_svg(Point(x_radical + 0.3, 6))
    builder.text('Eje radical', Point(svg_label.x, svg_label.y), font_size=10, fill='#ef4444', font_weight='bold')
    
    # Centros
    coord.draw_point(builder, C1, label='C₁', color='#3b82f6', radius=4)
    coord.draw_point(builder, C2, label='C₂', color='#22c55e', radius=4)
    
    # Línea entre centros
    coord.draw_segment(builder, C1, C2, color='#64748b', width=1, dashed=True)
    
    builder.formula_box('C₁ - C₂ = 0  |  Puntos con igual potencia', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_circ_ortogonales(output_path: str, title: str = "Circunferencias Ortogonales"):
    """Dos circunferencias que se cortan en ángulo recto."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-4, 8), y_range=(-4, 8),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Para ortogonalidad: d² = r1² + r2²
    # C1: centro (0, 0), radio 3
    # C2: centro (5, 0), radio 4
    # d = 5, d² = 25, r1² + r2² = 9 + 16 = 25 ✓
    C1 = Point(0, 0)
    r1 = 3
    C2 = Point(5, 0)
    r2 = 4
    
    svg_c1 = coord.to_svg(C1)
    svg_r1 = r1 * coord.scale_x
    builder.circle(svg_c1, svg_r1, fill='#dbeafe', fill_opacity=0.3, stroke='#3b82f6', stroke_width=2)
    
    svg_c2 = coord.to_svg(C2)
    svg_r2 = r2 * coord.scale_x
    builder.circle(svg_c2, svg_r2, fill='#dcfce7', fill_opacity=0.3, stroke='#22c55e', stroke_width=2)
    
    # Punto de intersección (calculado)
    # x² + y² = 9 y (x-5)² + y² = 16
    # x² + y² = 9, x² - 10x + 25 + y² = 16
    # Restando: 10x - 25 = -7 → x = 1.8
    # y² = 9 - 3.24 = 5.76 → y = 2.4
    P = Point(1.8, 2.4)
    coord.draw_point(builder, P, label='P', color=COLORS['accent'], radius=5)
    
    # Radios al punto de intersección
    coord.draw_segment(builder, C1, P, color='#3b82f6', width=1.5)
    coord.draw_segment(builder, C2, P, color='#22c55e', width=1.5)
    
    # Símbolo de ángulo recto
    svg_p = coord.to_svg(P)
    builder.text('90°', Point(svg_p.x + 10, svg_p.y - 10), font_size=10, fill=COLORS['accent'], font_weight='bold')
    
    # Centros
    coord.draw_point(builder, C1, label='C₁', color='#3b82f6', radius=4)
    coord.draw_point(builder, C2, label='C₂', color='#22c55e', radius=4)
    
    builder.formula_box('d² = r₁² + r₂²  |  Se cortan en ángulo recto', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


# ============================================================================
# PARÁBOLA - ILUSTRACIONES (SymPy)
# ============================================================================

def render_elementos_parabola(output_path: str, title: str = "Elementos de la Parábola"):
    """Lección 01: Definición - muestra foco, directriz, vértice, eje, lado recto.
    
    Calculado con SymPy:
    - Parábola: x² = 8y (p = 2)
    - Vértice: (0, 0)
    - Foco: (0, 2)
    - Directriz: y = -2
    - Lado recto: 8 (extremos en (-4, 2) y (4, 2))
    """
    from sympy import sqrt, Rational, symbols
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-8, 8), y_range=(-4, 10),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Parábola x² = 8y, p = 2
    p = 2
    
    # Dibujar parábola: y = x²/8
    parabola_points = []
    for x_val in range(-7, 8):
        x = x_val
        y = (x**2) / 8
        if y <= 10:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    # Dibujar como polilínea
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{p.x:.2f},{p.y:.2f}' for p in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Vértice V(0, 0)
    V = Point(0, 0)
    coord.draw_point(builder, V, label='V(0, 0)', color=COLORS['accent'], radius=5, label_offset=(10, 15), show_coords=False)
    
    # Foco F(0, p) = F(0, 2)
    F = Point(0, p)
    coord.draw_point(builder, F, label='F(0, 2)', color='#ef4444', radius=5, label_offset=(10, -10), show_coords=False)
    
    # Directriz y = -p = -2
    coord.draw_segment(builder, Point(-7, -p), Point(7, -p), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(5, -p))
    builder.text('directriz: y = -2', Point(svg_dir.x, svg_dir.y + 15), font_size=10, fill='#22c55e')
    
    # Eje (eje Y)
    coord.draw_segment(builder, Point(0, -3), Point(0, 9), color='#64748b', width=1, dashed=True)
    
    # Lado recto: extremos (-4, 2) y (4, 2)
    LR1 = Point(-4, p)
    LR2 = Point(4, p)
    coord.draw_segment(builder, LR1, LR2, color='#a855f7', width=2)
    coord.draw_point(builder, LR1, label='', color='#a855f7', radius=4)
    coord.draw_point(builder, LR2, label='', color='#a855f7', radius=4)
    svg_lr = coord.to_svg(Point(0, p + 0.5))
    builder.text('LR = 4p = 8', Point(svg_lr.x, svg_lr.y - 15), font_size=10, fill='#a855f7')
    
    # Distancia d(P, F) = d(P, ℓ) para un punto P
    P_ejemplo = Point(4, 2)
    # Distancia a directriz
    coord.draw_segment(builder, P_ejemplo, Point(4, -p), color='#64748b', width=1, dashed=True)
    
    builder.formula_box('x² = 4py | d(P, F) = d(P, directriz)', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_vertical_arriba(output_path: str, title: str = "Parábola Vertical (Abre Arriba)"):
    """Lección 02: x² = 4py con p > 0.
    
    SymPy: x² = 12y → p = 3
    """
    from sympy import Rational
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-10, 10), y_range=(-4, 14),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # x² = 12y → p = 3
    p = 3
    
    # Dibujar parábola: y = x²/12
    parabola_points = []
    for x_val in range(-90, 91):
        x = x_val / 10
        y = (x**2) / 12
        if -4 <= y <= 14:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Elementos
    V = Point(0, 0)
    F = Point(0, p)
    
    coord.draw_point(builder, V, label='V(0, 0)', color=COLORS['accent'], radius=5, show_coords=False)
    coord.draw_point(builder, F, label='F(0, 3)', color='#ef4444', radius=5, label_offset=(10, 0), show_coords=False)
    
    # Directriz
    coord.draw_segment(builder, Point(-9, -p), Point(9, -p), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(6, -p))
    builder.text('y = -3', Point(svg_dir.x, svg_dir.y + 15), font_size=10, fill='#22c55e')
    
    # Lado recto
    coord.draw_segment(builder, Point(-6, p), Point(6, p), color='#a855f7', width=1.5)
    
    builder.formula_box('x² = 12y | p = 3 | Abre hacia arriba', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_vertical_abajo(output_path: str, title: str = "Parábola Vertical (Abre Abajo)"):
    """Lección 02: x² = -4py con p > 0.
    
    SymPy: x² = -12y → p = 3
    """
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-10, 10), y_range=(-14, 4),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # x² = -12y → p = 3, abre abajo
    p = 3
    
    # Dibujar parábola: y = -x²/12
    parabola_points = []
    for x_val in range(-90, 91):
        x = x_val / 10
        y = -(x**2) / 12
        if -14 <= y <= 4:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Elementos
    V = Point(0, 0)
    F = Point(0, -p)
    
    coord.draw_point(builder, V, label='V(0, 0)', color=COLORS['accent'], radius=5, show_coords=False)
    coord.draw_point(builder, F, label='F(0, -3)', color='#ef4444', radius=5, label_offset=(10, 0), show_coords=False)
    
    # Directriz y = p = 3
    coord.draw_segment(builder, Point(-9, p), Point(9, p), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(6, p))
    builder.text('y = 3', Point(svg_dir.x, svg_dir.y - 10), font_size=10, fill='#22c55e')
    
    # Lado recto
    coord.draw_segment(builder, Point(-6, -p), Point(6, -p), color='#a855f7', width=1.5)
    
    builder.formula_box('x² = -12y | p = 3 | Abre hacia abajo', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_horizontal_derecha(output_path: str, title: str = "Parábola Horizontal (Abre Derecha)"):
    """Lección 03: y² = 4px con p > 0.
    
    SymPy: y² = 8x → p = 2
    """
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-4, 10), y_range=(-8, 8),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # y² = 8x → p = 2
    p = 2
    
    # Dibujar parábola: x = y²/8
    parabola_points_upper = []
    parabola_points_lower = []
    for y_val in range(0, 71):
        y = y_val / 10
        x = (y**2) / 8
        if x <= 10:
            parabola_points_upper.append(coord.to_svg(Point(x, y)))
            parabola_points_lower.append(coord.to_svg(Point(x, -y)))
    
    # Combinar (de abajo hacia arriba)
    parabola_points = list(reversed(parabola_points_lower)) + parabola_points_upper
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Elementos
    V = Point(0, 0)
    F = Point(p, 0)
    
    coord.draw_point(builder, V, label='V(0, 0)', color=COLORS['accent'], radius=5, show_coords=False)
    coord.draw_point(builder, F, label='F(2, 0)', color='#ef4444', radius=5, label_offset=(0, -15), show_coords=False)
    
    # Directriz x = -p = -2
    coord.draw_segment(builder, Point(-p, -7), Point(-p, 7), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(-p, 5))
    builder.text('x = -2', Point(svg_dir.x - 30, svg_dir.y), font_size=10, fill='#22c55e')
    
    # Lado recto
    coord.draw_segment(builder, Point(p, -4), Point(p, 4), color='#a855f7', width=1.5)
    
    builder.formula_box('y² = 8x | p = 2 | Abre hacia la derecha', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_horizontal_izquierda(output_path: str, title: str = "Parábola Horizontal (Abre Izquierda)"):
    """Lección 03: y² = -4px con p > 0.
    
    SymPy: y² = -8x → p = 2
    """
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-10, 4), y_range=(-8, 8),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # y² = -8x → p = 2, abre izquierda
    p = 2
    
    # Dibujar parábola: x = -y²/8
    parabola_points_upper = []
    parabola_points_lower = []
    for y_val in range(0, 71):
        y = y_val / 10
        x = -(y**2) / 8
        if x >= -10:
            parabola_points_upper.append(coord.to_svg(Point(x, y)))
            parabola_points_lower.append(coord.to_svg(Point(x, -y)))
    
    parabola_points = list(reversed(parabola_points_lower)) + parabola_points_upper
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Elementos
    V = Point(0, 0)
    F = Point(-p, 0)
    
    coord.draw_point(builder, V, label='V(0, 0)', color=COLORS['accent'], radius=5, show_coords=False)
    coord.draw_point(builder, F, label='F(-2, 0)', color='#ef4444', radius=5, label_offset=(0, -15), show_coords=False)
    
    # Directriz x = p = 2
    coord.draw_segment(builder, Point(p, -7), Point(p, 7), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(p, 5))
    builder.text('x = 2', Point(svg_dir.x + 5, svg_dir.y), font_size=10, fill='#22c55e')
    
    # Lado recto
    coord.draw_segment(builder, Point(-p, -4), Point(-p, 4), color='#a855f7', width=1.5)
    
    builder.formula_box('y² = -8x | p = 2 | Abre hacia la izquierda', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_trasladada(output_path: str, title: str = "Parábola Trasladada"):
    """Lección 04: (x-h)² = 4p(y-k).
    
    SymPy: (x-2)² = 8(y+1) → V(2, -1), p = 2
    """
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-6, 10), y_range=(-4, 10),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # (x-2)² = 8(y+1) → V(2, -1), p = 2
    h, k = 2, -1
    p = 2
    
    # Dibujar parábola: y = (x-h)²/8 + k
    parabola_points = []
    for x_val in range(-50, 90):
        x = x_val / 10
        y = ((x - h)**2) / 8 + k
        if -4 <= y <= 10:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Elementos
    V = Point(h, k)
    F = Point(h, k + p)
    
    coord.draw_point(builder, V, label='V(2, -1)', color=COLORS['accent'], radius=5, label_offset=(10, 15), show_coords=False)
    coord.draw_point(builder, F, label='F(2, 1)', color='#ef4444', radius=5, label_offset=(10, -10), show_coords=False)
    
    # Directriz y = k - p = -3
    coord.draw_segment(builder, Point(-5, k - p), Point(9, k - p), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(6, k - p))
    builder.text('y = -3', Point(svg_dir.x, svg_dir.y + 15), font_size=10, fill='#22c55e')
    
    # Eje x = h = 2
    coord.draw_segment(builder, Point(h, k - 2), Point(h, 8), color='#64748b', width=1, dashed=True)
    
    builder.formula_box('(x - 2)² = 8(y + 1) | V(2, -1), F(2, 1)', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_cuatro_orientaciones_parabola(output_path: str, title: str = "Las Cuatro Orientaciones"):
    """Lección 01: Muestra las 4 orientaciones de la parábola."""
    import math
    
    svg_width = 700
    svg_height = 350
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 20), font_size=14, font_weight='bold')
    
    # 4 mini-diagramas
    configs = [
        {'cx': 90, 'cy': 170, 'dir': 'arriba', 'eq': 'x² = 4py'},
        {'cx': 265, 'cy': 170, 'dir': 'abajo', 'eq': 'x² = -4py'},
        {'cx': 440, 'cy': 170, 'dir': 'derecha', 'eq': 'y² = 4px'},
        {'cx': 615, 'cy': 170, 'dir': 'izquierda', 'eq': 'y² = -4px'},
    ]
    
    for cfg in configs:
        cx, cy = cfg['cx'], cfg['cy']
        
        # Ejes pequeños
        builder.line(Point(cx - 50, cy), Point(cx + 50, cy), stroke='#94a3b8', stroke_width=1)
        builder.line(Point(cx, cy - 60), Point(cx, cy + 60), stroke='#94a3b8', stroke_width=1)
        
        # Parábola simplificada
        points = []
        if cfg['dir'] == 'arriba':
            for t in range(-30, 31):
                x = t
                y = -(t**2) / 30
                points.append(Point(cx + x, cy + y))
        elif cfg['dir'] == 'abajo':
            for t in range(-30, 31):
                x = t
                y = (t**2) / 30
                points.append(Point(cx + x, cy + y))
        elif cfg['dir'] == 'derecha':
            for t in range(-30, 31):
                y = t
                x = (t**2) / 30
                points.append(Point(cx + x, cy + y))
        elif cfg['dir'] == 'izquierda':
            for t in range(-30, 31):
                y = t
                x = -(t**2) / 30
                points.append(Point(cx + x, cy + y))
        
        points_str = ' '.join(f'{p.x:.1f},{p.y:.1f}' for p in points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2"/>'
        )
        
        # Foco (punto rojo)
        if cfg['dir'] == 'arriba':
            builder.circle(Point(cx, cy - 15), 4, fill='#ef4444')
        elif cfg['dir'] == 'abajo':
            builder.circle(Point(cx, cy + 15), 4, fill='#ef4444')
        elif cfg['dir'] == 'derecha':
            builder.circle(Point(cx + 15, cy), 4, fill='#ef4444')
        elif cfg['dir'] == 'izquierda':
            builder.circle(Point(cx - 15, cy), 4, fill='#ef4444')
        
        # Vértice
        builder.circle(Point(cx, cy), 4, fill=COLORS['accent'])
        
        # Etiquetas
        builder.text(cfg['eq'], Point(cx, cy + 85), font_size=10, font_weight='bold')
        builder.text(cfg['dir'], Point(cx, cy + 100), font_size=9, fill='#64748b')
    
    builder.save(output_path)
    return True


def render_tangente_parabola(output_path: str, title: str = "Tangente a la Parábola"):
    """Lección 07: Tangente a x² = 8y en (4, 2).
    
    SymPy:
    - Parábola: x² = 8y → p = 2
    - Punto: P(4, 2) → verificar: 16 = 8(2) = 16 ✓
    - Tangente: x₀x = 2p(y + y₀) → 4x = 4(y + 2) → x = y + 2
    """
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-6, 10), y_range=(-4, 10),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=2)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Parábola x² = 8y, p = 2
    p = 2
    
    # Dibujar parábola
    parabola_points = []
    for x_val in range(-70, 90):
        x = x_val / 10
        y = (x**2) / 8
        if -4 <= y <= 10:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Punto de tangencia P(4, 2)
    P = Point(4, 2)
    coord.draw_point(builder, P, label='P(4, 2)', color=COLORS['accent'], radius=5, label_offset=(10, -10), show_coords=False)
    
    # Tangente: x = y + 2 → y = x - 2
    # Puntos: (-2, -4) a (8, 6)
    coord.draw_segment(builder, Point(-2, -4), Point(8, 6), color='#22c55e', width=2)
    
    # Etiqueta tangente
    svg_tang = coord.to_svg(Point(6, 4.5))
    builder.text('x = y + 2', Point(svg_tang.x, svg_tang.y - 10), font_size=10, fill='#22c55e', font_weight='bold')
    
    # Foco
    F = Point(0, p)
    coord.draw_point(builder, F, label='F', color='#ef4444', radius=4)
    
    # Vértice
    V = Point(0, 0)
    coord.draw_point(builder, V, label='V', color='#64748b', radius=4)
    
    builder.formula_box('x² = 8y | Tangente en P(4,2): x₀x = 2p(y + y₀)', Point(svg_width/2, svg_height - 30), font_size=10)
    
    builder.save(output_path)
    return True


# ============================================================================
# CONSTRUCCIÓN DE PARÁBOLAS - 4 CASOS (SymPy)
# ============================================================================

def render_construccion_caso1_vertice_foco(output_path: str, title: str = "Caso 1: Vértice y Foco"):
    """Construcción: V(2, 3) y F(2, 5) → (x-2)² = 8(y-3).
    
    SymPy:
    - p = |5 - 3| = 2
    - Foco arriba → abre arriba → (x-h)² = 4p(y-k)
    - 4p = 8
    """
    from sympy import Rational, sqrt, Abs
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-4, 8), y_range=(-1, 11),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Datos con SymPy
    h, k = 2, 3  # Vértice
    f_y = 5      # Foco y-coord
    p = Rational(f_y - k)  # p = 2
    coef_4p = 4 * p  # 4p = 8
    
    # Parábola: (x-2)² = 8(y-3) → y = (x-2)²/8 + 3
    parabola_points = []
    for x_val in range(-30, 70):
        x = x_val / 10
        y = ((x - h)**2) / float(coef_4p) + k
        if -1 <= y <= 11:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Vértice V(2, 3)
    V = Point(h, k)
    coord.draw_point(builder, V, label='V(2, 3)', color=COLORS['accent'], radius=5, label_offset=(-50, 10), show_coords=False)
    
    # Foco F(2, 5)
    F = Point(h, f_y)
    coord.draw_point(builder, F, label='F(2, 5)', color='#ef4444', radius=5, label_offset=(10, -10), show_coords=False)
    
    # Directriz y = k - p = 1
    dir_y = k - int(p)
    coord.draw_segment(builder, Point(-3, dir_y), Point(7, dir_y), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(5, dir_y))
    builder.text('y = 1', Point(svg_dir.x, svg_dir.y + 15), font_size=10, fill='#22c55e')
    
    # Distancia p entre V y F
    coord.draw_segment(builder, V, F, color='#a855f7', width=1.5, dashed=True)
    svg_mid = coord.to_svg(Point(h + 0.5, (k + f_y) / 2))
    builder.text('p = 2', Point(svg_mid.x + 10, svg_mid.y), font_size=10, fill='#a855f7', font_weight='bold')
    
    builder.formula_box('(x - 2)² = 8(y - 3) | p = 2, 4p = 8', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_construccion_caso2_vertice_directriz(output_path: str, title: str = "Caso 2: Vértice y Directriz"):
    """Construcción: V(0, 2) y directriz y = 5 → x² = -12(y-2).
    
    SymPy:
    - Directriz arriba del vértice → abre abajo
    - p = |5 - 2| = 3
    - Ecuación: x² = -4p(y - k) = -12(y - 2)
    """
    from sympy import Rational
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-8, 8), y_range=(-6, 8),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Datos con SymPy
    h, k = 0, 2      # Vértice
    dir_y = 5        # Directriz
    p = Rational(abs(dir_y - k))  # p = 3
    coef_4p = -4 * p  # -12 (negativo porque abre abajo)
    
    # Parábola: x² = -12(y-2) → y = -x²/12 + 2
    parabola_points = []
    for x_val in range(-80, 81):
        x = x_val / 10
        y = -(x**2) / 12 + k
        if -6 <= y <= 8:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Vértice V(0, 2)
    V = Point(h, k)
    coord.draw_point(builder, V, label='V(0, 2)', color=COLORS['accent'], radius=5, label_offset=(10, 10), show_coords=False)
    
    # Foco F(0, -1) = (0, k - p)
    f_y = k - int(p)
    F = Point(h, f_y)
    coord.draw_point(builder, F, label='F(0, -1)', color='#ef4444', radius=5, label_offset=(10, 10), show_coords=False)
    
    # Directriz y = 5
    coord.draw_segment(builder, Point(-7, dir_y), Point(7, dir_y), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(5, dir_y))
    builder.text('y = 5 (directriz)', Point(svg_dir.x, svg_dir.y - 10), font_size=10, fill='#22c55e')
    
    # Distancia p entre V y directriz
    coord.draw_segment(builder, V, Point(h, dir_y), color='#a855f7', width=1.5, dashed=True)
    svg_mid = coord.to_svg(Point(h + 0.5, (k + dir_y) / 2))
    builder.text('p = 3', Point(svg_mid.x + 10, svg_mid.y), font_size=10, fill='#a855f7', font_weight='bold')
    
    builder.formula_box('x² = -12(y - 2) | p = 3, abre abajo', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_construccion_caso3_foco_directriz(output_path: str, title: str = "Caso 3: Foco y Directriz"):
    """Construcción: F(3, 4) y directriz y = -2 → (x-3)² = 12(y-1).
    
    SymPy:
    - Vértice = punto medio entre foco y directriz
    - V = (3, (4 + (-2))/2) = (3, 1)
    - p = |4 - 1| = 3
    - Ecuación: (x - 3)² = 12(y - 1)
    """
    from sympy import Rational
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-4, 10), y_range=(-4, 10),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Datos con SymPy
    f_x, f_y = 3, 4   # Foco
    dir_y = -2        # Directriz
    
    # Vértice = punto medio
    h = f_x
    k = Rational(f_y + dir_y, 2)  # k = (4 + (-2))/2 = 1
    p = Rational(f_y - int(k))    # p = 4 - 1 = 3
    coef_4p = 4 * p  # 12
    
    # Parábola: (x-3)² = 12(y-1) → y = (x-3)²/12 + 1
    parabola_points = []
    for x_val in range(-30, 90):
        x = x_val / 10
        y = ((x - h)**2) / float(coef_4p) + float(k)
        if -4 <= y <= 10:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Foco F(3, 4)
    F = Point(f_x, f_y)
    coord.draw_point(builder, F, label='F(3, 4)', color='#ef4444', radius=5, label_offset=(10, -10), show_coords=False)
    
    # Vértice V(3, 1)
    V = Point(h, int(k))
    coord.draw_point(builder, V, label='V(3, 1)', color=COLORS['accent'], radius=5, label_offset=(10, 10), show_coords=False)
    
    # Directriz y = -2
    coord.draw_segment(builder, Point(-3, dir_y), Point(9, dir_y), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(6, dir_y))
    builder.text('y = -2 (directriz)', Point(svg_dir.x, svg_dir.y + 15), font_size=10, fill='#22c55e')
    
    # Línea punteada F → directriz (mostrando punto medio = V)
    coord.draw_segment(builder, F, Point(f_x, dir_y), color='#a855f7', width=1.5, dashed=True)
    svg_mid = coord.to_svg(Point(f_x - 0.5, (f_y + dir_y) / 2))
    builder.text('V = punto medio', Point(svg_mid.x - 80, svg_mid.y), font_size=9, fill='#a855f7')
    
    builder.formula_box('(x - 3)² = 12(y - 1) | V = punto medio, p = 3', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_construccion_caso4_vertice_punto(output_path: str, title: str = "Caso 4: Vértice y Punto"):
    """Construcción: V(1, 2), pasa por P(3, 6) → (x-1)² = (y-2).
    
    SymPy:
    - (x - 1)² = 4p(y - 2)
    - Sustituir P(3, 6): (3-1)² = 4p(6-2)
    - 4 = 16p → p = 1/4
    - 4p = 1
    - Ecuación: (x - 1)² = (y - 2)
    """
    from sympy import Rational, symbols, solve
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-3, 7), y_range=(-1, 9),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Datos con SymPy
    h, k = 1, 2      # Vértice
    px, py = 3, 6    # Punto conocido
    
    # Calcular p: (px - h)² = 4p(py - k)
    p_sym = symbols('p')
    ecuacion = (px - h)**2 - 4*p_sym*(py - k)
    p_val = solve(ecuacion, p_sym)[0]  # p = 1/4
    coef_4p = 4 * p_val  # 4p = 1
    
    # Parábola: (x-1)² = (y-2) → y = (x-1)² + 2
    parabola_points = []
    for x_val in range(-25, 55):
        x = x_val / 10
        y = (x - h)**2 + k
        if -1 <= y <= 9:
            parabola_points.append(coord.to_svg(Point(x, y)))
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )
    
    # Vértice V(1, 2)
    V = Point(h, k)
    coord.draw_point(builder, V, label='V(1, 2)', color=COLORS['accent'], radius=5, label_offset=(-50, 10), show_coords=False)
    
    # Punto P(3, 6)
    P = Point(px, py)
    coord.draw_point(builder, P, label='P(3, 6)', color='#22c55e', radius=5, label_offset=(10, -10), show_coords=False)
    
    # Foco F(1, 2 + p) = F(1, 2.25)
    f_y = k + float(p_val)
    F = Point(h, f_y)
    coord.draw_point(builder, F, label='F(1, 2.25)', color='#ef4444', radius=4, label_offset=(10, 0), show_coords=False)
    
    # Mostrar cálculo
    svg_calc = coord.to_svg(Point(-2, 7))
    builder.text('(3-1)² = 4p(6-2)', Point(svg_calc.x, svg_calc.y), font_size=9, fill='#64748b')
    builder.text('4 = 16p → p = ¼', Point(svg_calc.x, svg_calc.y + 15), font_size=9, fill='#64748b')
    
    builder.formula_box('(x - 1)² = (y - 2) | p = ¼, 4p = 1', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_interior_exterior_circ(output_path: str, title: str = "Interior, Exterior y Frontera"):
    """Lección 01: Clasificación de puntos respecto a la circunferencia."""
    import math
    
    svg_width = 600
    svg_height = 600
    padding = 50
    
    coord = CoordinateSystem(
        svg_width=svg_width, svg_height=svg_height,
        x_range=(-6, 6), y_range=(-6, 6),
        padding=padding
    )
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 25), font_size=15, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    coord.draw_ticks(builder, step=2, show_labels=True)
    
    # Circunferencia x² + y² = 16 (centro origen, radio 4)
    C = Point(0, 0)
    r = 4
    
    svg_c = coord.to_svg(C)
    svg_r = r * coord.scale_x
    builder.circle(svg_c, svg_r, fill='#dbeafe', fill_opacity=0.2, stroke=COLORS['primary'], stroke_width=2)
    
    # Punto interior: (1, 1) → 1 + 1 = 2 < 16
    P_int = Point(1, 1)
    coord.draw_point(builder, P_int, label='Interior', color='#22c55e', radius=5, label_offset=(10, 15))
    
    # Punto sobre la circunferencia: (0, 4) → 0 + 16 = 16
    P_sobre = Point(0, 4)
    coord.draw_point(builder, P_sobre, label='Sobre', color=COLORS['primary'], radius=5, label_offset=(10, -10))
    
    # Punto exterior: (4, 3) → 16 + 9 = 25 > 16
    P_ext = Point(4, 3)
    coord.draw_point(builder, P_ext, label='Exterior', color='#ef4444', radius=5, label_offset=(10, 0))
    
    # Centro
    coord.draw_point(builder, C, label='C', color=COLORS['accent'], radius=4)
    
    builder.formula_box('Interior: d < r | Sobre: d = r | Exterior: d > r', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


# ============================================================================
# RENDERIZADO DESDE SPEC JSON
# ============================================================================

def render_from_spec(spec: dict, output_path: str) -> bool:
    """Renderiza desde una especificación JSON."""
    tipo = spec.get('tipo', 'custom')
    
    if tipo == 'plano-basico':
        return render_plano_basico(output_path, spec.get('titulo', 'El Plano Cartesiano'))
    
    elif tipo == 'distancia':
        return render_distancia(
            output_path,
            p1=tuple(spec.get('p1', [1, 2])),
            p2=tuple(spec.get('p2', [4, 6])),
            title=spec.get('titulo', 'Distancia entre dos puntos')
        )
    
    elif tipo == 'punto-medio':
        return render_punto_medio(
            output_path,
            p1=tuple(spec.get('p1', [2, 1])),
            p2=tuple(spec.get('p2', [6, 5])),
            title=spec.get('titulo', 'Punto medio de un segmento')
        )
    
    elif tipo == 'division-segmento':
        return render_division_segmento(
            output_path,
            p1=tuple(spec.get('p1', [1, 2])),
            p2=tuple(spec.get('p2', [7, 8])),
            m=spec.get('m', 1),
            n=spec.get('n', 2),
            title=spec.get('titulo', 'División de un segmento')
        )
    
    elif tipo == 'area-triangulo':
        return render_area_triangulo(
            output_path,
            vertices=spec.get('vertices', [[1, 1], [5, 1], [3, 5]]),
            title=spec.get('titulo', 'Área de un triángulo')
        )
    
    else:
        print(f"❌ Tipo desconocido: {tipo}")
        return False


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Cartesian Renderer - SVGs para Geometría Analítica'
    )
    parser.add_argument('--spec', help='Archivo JSON de especificación')
    parser.add_argument('--type', choices=[
        'plano-basico', 'distancia', 'punto-medio', 
        'division-segmento', 'area-triangulo',
        'tipos-pendiente', 'calculo-pendiente', 'angulo-inclinacion',
        'paralelas-perpendiculares', 'angulo-entre-rectas'
    ], help='Tipo de ilustración predefinida')
    parser.add_argument('--output', required=True, help='Archivo SVG de salida')
    parser.add_argument('--title', help='Título personalizado')
    
    args = parser.parse_args()
    
    if args.spec:
        # Renderizar desde spec
        spec_path = Path(args.spec)
        if not spec_path.exists():
            print(f"❌ Error: No se encuentra {spec_path}")
            sys.exit(1)
        
        with open(spec_path) as f:
            spec = json.load(f)
        
        success = render_from_spec(spec, args.output)
    
    elif args.type:
        # Renderizar tipo predefinido
        title = args.title or args.type.replace('-', ' ').title()
        
        if args.type == 'plano-basico':
            success = render_plano_basico(args.output, title)
        elif args.type == 'distancia':
            success = render_distancia(args.output, title=title)
        elif args.type == 'punto-medio':
            success = render_punto_medio(args.output, title=title)
        elif args.type == 'division-segmento':
            success = render_division_segmento(args.output, title=title)
        elif args.type == 'area-triangulo':
            success = render_area_triangulo(args.output, title=title)
        elif args.type == 'tipos-pendiente':
            success = render_tipos_pendiente(args.output, title=title)
        elif args.type == 'calculo-pendiente':
            success = render_calculo_pendiente(args.output, title=title)
        elif args.type == 'angulo-inclinacion':
            success = render_angulo_inclinacion(args.output, title=title)
        elif args.type == 'paralelas-perpendiculares':
            success = render_paralelas_perpendiculares(args.output, title=title)
        elif args.type == 'angulo-entre-rectas':
            success = render_angulo_entre_rectas(args.output, title=title)
        else:
            print(f"❌ Tipo no implementado: {args.type}")
            sys.exit(1)
    
    else:
        print("❌ Error: Especifica --spec o --type")
        sys.exit(1)
    
    if success:
        print(f"✅ SVG generado: {args.output}")
    else:
        print("❌ Error al generar SVG")
        sys.exit(1)


if __name__ == '__main__':
    main()

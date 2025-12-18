"""
📍 Points - Funciones de renderizado para puntos y segmentos

Incluye:
- Plano cartesiano básico
- Distancia entre puntos
- Punto medio
- División de segmentos
- Área de triángulos/polígonos
"""

import math
import sys
from pathlib import Path

# Importar desde core
sys.path.insert(0, str(Path(__file__).parent.parent))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


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

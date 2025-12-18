"""
📏 Lines - Funciones de renderizado para ecuaciones de rectas

Incluye:
- Ecuación general
- Forma punto-pendiente
- Forma pendiente-ordenada
- Recta por dos puntos
- Forma simétrica
- Forma normal
- Distancia punto-recta
- Familias de rectas
"""

import math
import sys
from pathlib import Path

# Importar desde core
sys.path.insert(0, str(Path(__file__).parent.parent))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


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
    
    # Pie de la perpendicular
    pie_x = (4 + 2 - 3) / 2
    pie_y = (3 + 2 - 4) / 2
    pie = Point(pie_x + 0.5, pie_y + 0.5)
    
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

"""
📐 Slopes - Funciones de renderizado para pendientes e inclinación

Incluye:
- Tipos de pendiente (positiva, negativa, cero)
- Concepto de pendiente (Δy/Δx)
- Comparación por valor absoluto
- Rectas horizontales y verticales
- Cálculo de pendiente
- Ángulo de inclinación
- Rectas paralelas y perpendiculares
"""

import math
import sys
from pathlib import Path

# Importar desde core
sys.path.insert(0, str(Path(__file__).parent.parent))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


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
    coord.draw_segment(builder, Point(-4, -2), Point(4, 6), color='#3b82f6', width=2.5)
    svg_l1 = coord.to_svg(Point(3, 5))
    builder.text('L₁: m = 1', Point(svg_l1.x + 5, svg_l1.y - 10), 
                 font_size=11, font_weight='bold', fill='#3b82f6', anchor='start')
    
    # L2: y = x - 2
    coord.draw_segment(builder, Point(-2, -4), Point(6, 4), color='#22c55e', width=2.5)
    svg_l2 = coord.to_svg(Point(5, 3))
    builder.text('L₂: m = 1', Point(svg_l2.x + 5, svg_l2.y + 15), 
                 font_size=11, font_weight='bold', fill='#22c55e', anchor='start')
    
    # Rectas perpendiculares
    # L3: y = 2x - 3
    coord.draw_segment(builder, Point(-1, -5), Point(3, 3), color='#ef4444', width=2.5)
    svg_l3 = coord.to_svg(Point(2.5, 2))
    builder.text('L₃: m = 2', Point(svg_l3.x + 5, svg_l3.y - 10), 
                 font_size=11, font_weight='bold', fill='#ef4444', anchor='start')
    
    # L4: y = -0.5x + 1 (perpendicular a L3)
    coord.draw_segment(builder, Point(-4, 3), Point(6, -2), color='#a855f7', width=2.5)
    svg_l4 = coord.to_svg(Point(-3, 2.5))
    builder.text('L₄: m = -½', Point(svg_l4.x - 60, svg_l4.y - 10), 
                 font_size=11, font_weight='bold', fill='#a855f7', anchor='start')
    
    # Leyenda
    builder.rect(480, 380, 150, 85, fill='#f8fafc', stroke='#e2e8f0', rx=8)
    builder.text('Relaciones:', Point(555, 395), font_size=11, font_weight='bold')
    builder.text('Paralelas:', Point(490, 415), font_size=10, fill='#1e293b', anchor='start')
    builder.text('m₁ = m₂', Point(490, 430), font_size=10, fill='#64748b', anchor='start')
    builder.text('Perpendiculares:', Point(490, 450), font_size=10, fill='#1e293b', anchor='start')
    builder.text('m₁ · m₂ = -1', Point(490, 465), font_size=10, fill='#64748b', anchor='start')
    
    builder.save(output_path)
    return True

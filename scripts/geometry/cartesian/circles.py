"""
⭕ Circles - Funciones de renderizado para circunferencias en el plano cartesiano

Incluye:
- Elementos de la circunferencia
- Ecuación ordinaria
- Posiciones recta-circunferencia
- Posiciones entre circunferencias
- Circunferencias concéntricas
- Tangentes
"""

import math
import sys
from pathlib import Path

# Importar desde core
sys.path.insert(0, str(Path(__file__).parent.parent))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


def render_elementos_circunferencia(output_path: str, title: str = "Elementos de la Circunferencia"):
    """Lección 01: Definición - muestra centro, radio, diámetro, cuerda."""
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
    svg_mid_r = coord.to_svg(Point(3, 1))
    builder.text('r = 4', Point(svg_mid_r.x, svg_mid_r.y - 10), font_size=11, fill=COLORS['accent'], font_weight='bold')
    
    # Diámetro: de (-3, 1) a (5, 1)
    P_diam1 = Point(-3, 1)
    P_diam2 = Point(5, 1)
    coord.draw_segment(builder, P_diam1, P_diam2, color='#22c55e', width=2, dashed=True)
    svg_diam = coord.to_svg(Point(1, 1.5))
    builder.text('d = 2r = 8', Point(svg_diam.x, svg_diam.y - 25), font_size=10, fill='#22c55e')
    
    # Cuerda
    angle = math.pi / 3
    P_cuerda1 = Point(1 - 4*math.cos(angle), 1 + 4*math.sin(angle))
    P_cuerda2 = Point(1 + 4*math.cos(angle), 1 + 4*math.sin(angle))
    coord.draw_segment(builder, P_cuerda1, P_cuerda2, color='#a855f7', width=2)
    svg_cuerda = coord.to_svg(Point(1, 1 + 4*math.sin(angle) + 0.3))
    builder.text('cuerda', Point(svg_cuerda.x, svg_cuerda.y - 10), font_size=10, fill='#a855f7')
    
    # Centro y puntos
    coord.draw_point(builder, C, label='C', show_coords=True, color=COLORS['accent'], radius=5)
    coord.draw_point(builder, P_radio, label='P', color=COLORS['primary'], radius=4)
    coord.draw_point(builder, P_diam1, label='', color='#22c55e', radius=4)
    coord.draw_point(builder, P_cuerda1, label='', color='#a855f7', radius=4)
    coord.draw_point(builder, P_cuerda2, label='', color='#a855f7', radius=4)
    
    builder.formula_box('Centro C(h,k) | Radio r | Diámetro d=2r | Cuerda', Point(svg_width/2, svg_height - 30), font_size=10)
    
    builder.save(output_path)
    return True


def render_ecuacion_ordinaria_circ(output_path: str, title: str = "Ecuación Ordinaria"):
    """Lección 02: Ecuación ordinaria (x-h)² + (y-k)² = r²."""
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
    
    for i, r in enumerate(reversed(radii)):
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
    """Lección 07: Tangente a la circunferencia desde un punto."""
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
    
    # Circunferencia: x² + y² = 16 (centro origen, radio 4)
    C = Point(0, 0)
    r = 4
    
    svg_c = coord.to_svg(C)
    svg_r = r * coord.scale_x
    builder.circle(svg_c, svg_r, fill='#dbeafe', fill_opacity=0.3, stroke=COLORS['primary'], stroke_width=2)
    
    # Punto de tangencia P(3, √7) ≈ (3, 2.6458)
    sqrt7 = math.sqrt(7)
    P = Point(3, sqrt7)
    
    # Radio al punto de tangencia
    coord.draw_segment(builder, C, P, color=COLORS['accent'], width=2)
    
    # Tangente: 3x + √7·y = 16
    # Puntos en la tangente
    x1, x2 = -1, 6
    y1 = (16 - 3*x1) / sqrt7
    y2 = (16 - 3*x2) / sqrt7
    coord.draw_segment(builder, Point(x1, y1), Point(x2, y2), color='#22c55e', width=2)
    
    # Marca de perpendicularidad
    svg_p = coord.to_svg(P)
    builder.text('⊥', Point(svg_p.x + 15, svg_p.y - 5), font_size=14, fill='#64748b')
    
    # Puntos
    coord.draw_point(builder, C, label='C', color=COLORS['accent'], radius=5)
    coord.draw_point(builder, P, label='P', show_coords=False, color='#22c55e', radius=5)
    
    builder.formula_box('Tangente ⊥ Radio en punto de tangencia', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True

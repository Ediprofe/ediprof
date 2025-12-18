"""
📈 Parabolas - Funciones de renderizado para parábolas

Incluye:
- Elementos de la parábola (foco, directriz, vértice, eje, lado recto)
- Parábola vertical (arriba/abajo)
- Parábola horizontal (derecha/izquierda)
- Parábola trasladada
- Cuatro orientaciones
"""

import math
import sys
from pathlib import Path

# Importar desde core
sys.path.insert(0, str(Path(__file__).parent.parent))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


def _draw_parabola_vertical(builder, coord, p: float, opens_up: bool = True, x_range: tuple = (-9, 9)):
    """Helper para dibujar parábola vertical y = ±x²/(4p)."""
    sign = 1 if opens_up else -1
    parabola_points = []
    for x_val in range(x_range[0] * 10, x_range[1] * 10 + 1):
        x = x_val / 10
        y = sign * (x**2) / (4 * p)
        svg_pt = coord.to_svg(Point(x, y))
        if 0 <= svg_pt.y <= coord.svg_height:
            parabola_points.append(svg_pt)
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )


def _draw_parabola_horizontal(builder, coord, p: float, opens_right: bool = True, y_range: tuple = (-7, 7)):
    """Helper para dibujar parábola horizontal x = ±y²/(4p)."""
    sign = 1 if opens_right else -1
    parabola_points_upper = []
    parabola_points_lower = []
    
    for y_val in range(0, abs(y_range[1]) * 10 + 1):
        y = y_val / 10
        x = sign * (y**2) / (4 * p)
        svg_upper = coord.to_svg(Point(x, y))
        svg_lower = coord.to_svg(Point(x, -y))
        if 0 <= svg_upper.x <= coord.svg_width:
            parabola_points_upper.append(svg_upper)
            parabola_points_lower.append(svg_lower)
    
    parabola_points = list(reversed(parabola_points_lower)) + parabola_points_upper
    
    if len(parabola_points) > 1:
        points_str = ' '.join(f'{pt.x:.2f},{pt.y:.2f}' for pt in parabola_points)
        builder.elements.append(
            f'<polyline points="{points_str}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2.5"/>'
        )


def render_elementos_parabola(output_path: str, title: str = "Elementos de la Parábola"):
    """Lección 01: Definición - muestra foco, directriz, vértice, eje, lado recto."""
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
    _draw_parabola_vertical(builder, coord, p, opens_up=True, x_range=(-7, 7))
    
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
    coord.draw_segment(builder, P_ejemplo, Point(4, -p), color='#64748b', width=1, dashed=True)
    
    builder.formula_box('x² = 4py | d(P, F) = d(P, directriz)', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_parabola_vertical_arriba(output_path: str, title: str = "Parábola Vertical (Abre Arriba)"):
    """Lección 02: x² = 4py con p > 0."""
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
    _draw_parabola_vertical(builder, coord, p, opens_up=True)
    
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
    """Lección 02: x² = -4py con p > 0."""
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
    _draw_parabola_vertical(builder, coord, p, opens_up=False)
    
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
    """Lección 03: y² = 4px con p > 0."""
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
    _draw_parabola_horizontal(builder, coord, p, opens_right=True)
    
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
    """Lección 03: y² = -4px con p > 0."""
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
    _draw_parabola_horizontal(builder, coord, p, opens_right=False)
    
    # Elementos
    V = Point(0, 0)
    F = Point(-p, 0)
    
    coord.draw_point(builder, V, label='V(0, 0)', color=COLORS['accent'], radius=5, show_coords=False)
    coord.draw_point(builder, F, label='F(-2, 0)', color='#ef4444', radius=5, label_offset=(0, -15), show_coords=False)
    
    # Directriz x = p = 2
    coord.draw_segment(builder, Point(p, -7), Point(p, 7), color='#22c55e', width=2)
    svg_dir = coord.to_svg(Point(p, 5))
    builder.text('x = 2', Point(svg_dir.x + 10, svg_dir.y), font_size=10, fill='#22c55e')
    
    # Lado recto
    coord.draw_segment(builder, Point(-p, -4), Point(-p, 4), color='#a855f7', width=1.5)
    
    builder.formula_box('y² = -8x | p = 2 | Abre hacia la izquierda', Point(svg_width/2, svg_height - 30), font_size=11)
    
    builder.save(output_path)
    return True


def render_cuatro_orientaciones_parabola(output_path: str, title: str = "Las Cuatro Orientaciones"):
    """Muestra las 4 orientaciones de parábolas en un solo gráfico."""
    svg_width = 700
    svg_height = 350
    
    builder = SVGBuilder(svg_width, svg_height)
    builder.rect(0, 0, svg_width, svg_height, fill='#ffffff')
    builder.text(title, Point(svg_width/2, 20), font_size=14, font_weight='bold')
    
    # Cuatro mini-diagramas
    configs = [
        {'cx': 100, 'label': 'x² = 4py\n(arriba)', 'dir': 'up'},
        {'cx': 275, 'label': 'x² = -4py\n(abajo)', 'dir': 'down'},
        {'cx': 450, 'label': 'y² = 4px\n(derecha)', 'dir': 'right'},
        {'cx': 625, 'label': 'y² = -4px\n(izquierda)', 'dir': 'left'},
    ]
    
    cy = 170
    r = 60  # Tamaño del mini-diagrama
    
    for cfg in configs:
        cx = cfg['cx']
        
        # Ejes mini
        builder.line(Point(cx - r, cy), Point(cx + r, cy), stroke='#94a3b8', stroke_width=1)
        builder.line(Point(cx, cy - r), Point(cx, cy + r), stroke='#94a3b8', stroke_width=1)
        
        # Parábola simplificada
        points = []
        if cfg['dir'] == 'up':
            for t in range(-5, 6):
                x = cx + t * 10
                y = cy - (t**2) * 2
                points.append(f'{x},{y}')
        elif cfg['dir'] == 'down':
            for t in range(-5, 6):
                x = cx + t * 10
                y = cy + (t**2) * 2
                points.append(f'{x},{y}')
        elif cfg['dir'] == 'right':
            for t in range(-5, 6):
                y = cy + t * 10
                x = cx + (t**2) * 2
                points.append(f'{x},{y}')
        elif cfg['dir'] == 'left':
            for t in range(-5, 6):
                y = cy + t * 10
                x = cx - (t**2) * 2
                points.append(f'{x},{y}')
        
        builder.elements.append(
            f'<polyline points="{" ".join(points)}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2"/>'
        )
        
        # Vértice
        builder.circle(Point(cx, cy), 4, fill=COLORS['accent'])
        
        # Foco (punto rojo)
        fx, fy = cx, cy
        if cfg['dir'] == 'up': fy = cy - 20
        elif cfg['dir'] == 'down': fy = cy + 20
        elif cfg['dir'] == 'right': fx = cx + 20
        elif cfg['dir'] == 'left': fx = cx - 20
        builder.circle(Point(fx, fy), 3, fill='#ef4444')
        
        # Etiqueta
        lines = cfg['label'].split('\n')
        builder.text(lines[0], Point(cx, cy + r + 20), font_size=10, font_weight='bold')
        builder.text(lines[1], Point(cx, cy + r + 35), font_size=9, fill='#64748b')
    
    builder.save(output_path)
    return True

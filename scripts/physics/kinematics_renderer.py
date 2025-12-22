#!/usr/bin/env python3
"""
🏎️ Kinematics Renderer - Renderizador para Cinemática
Genera SVGs para ilustraciones de posición, marcos de referencia y movimiento.
"""

import sys
from pathlib import Path

# Importar módulo core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))

from core.base import Point, COLORS
from core.svg_builder import SVGBuilder
from core.coordinate_system import CoordinateSystem

def render_posicion_2d(output_path: str, p: tuple = (5, 3), 
                       title: str = "Posición en 2D",
                       label_p: str = "P",
                       show_r_vector: bool = True,
                       show_coord_labels: bool = True):
    """
    Renderiza un punto P en un sistema de coordenadas 2D.
    Muestra las proyecciones a los ejes y opcionalmente el vector posición r.
    """
    width, height = 600, 450
    
    # Determinar rango
    max_x = max(6, p[0] + 2)
    max_y = max(4, p[1] + 2)
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, max_x), y_range=(-1, max_y),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text(title, Point(width/2, 25), font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Ejes
    cs.draw_grid(svg, step=1)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=1, show_labels=True)
    
    origin = cs.to_svg(Point(0, 0))
    point_p = cs.to_svg(Point(p[0], p[1]))
    
    # Proyecciones
    proj_x = cs.to_svg(Point(p[0], 0))
    proj_y = cs.to_svg(Point(0, p[1]))
    
    svg.line(point_p, proj_x, stroke=COLORS['auxiliary'], stroke_width=1, dashed=True)
    svg.line(point_p, proj_y, stroke=COLORS['auxiliary'], stroke_width=1, dashed=True)
    
    # Vector posición r
    if show_r_vector:
        svg.arrow(origin, point_p, stroke=COLORS['secondary'], stroke_width=2)
        mid_r = Point((origin.x + point_p.x)/2, (origin.y + point_p.y)/2)
        svg.text("r", Point(mid_r.x - 10, mid_r.y - 10), font_size=14, 
                 font_weight="bold", fill=COLORS['secondary'])
    
    # Punto P
    cs.draw_point(svg, Point(p[0], p[1]), label=label_p, show_coords=False, color=COLORS['primary'])
    
    # Etiquetas de coordenadas
    if show_coord_labels:
        svg.text(f"x = {p[0]}", Point(proj_x.x, proj_x.y + 20), font_size=12, fill=COLORS['text'])
        svg.text(f"y = {p[1]}", Point(proj_y.x - 25, proj_y.y), font_size=12, fill=COLORS['text'])
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_marcos_referencia(output_path: str):
    """
    Renderiza dos marcos de referencia y un punto P.
    """
    width, height = 700, 500
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, 10), y_range=(-1, 7),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Ejes
    cs.draw_grid(svg, step=1)
    
    # Ejes principales (O1) - Usando el sistema estándar para que se vea "numerado" y "didáctico"
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=1, show_labels=True)
    
    # Título (después del grid para que quede arriba)
    svg.text("El origen puede estar en cualquier punto", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    o1_pos = Point(0, 0)
    o1_svg = cs.to_svg(o1_pos)
    
    # Ejes secundarios (O2) en (6, 1) - Rojo
    o2_real = Point(6, 1)
    o2_svg = cs.to_svg(o2_real)
    
    x_end_2 = cs.to_svg(Point(9, 1))
    y_end_2 = cs.to_svg(Point(6, 4))
    
    svg.arrow(o2_svg, x_end_2, stroke=COLORS['accent'], stroke_width=2)
    svg.arrow(o2_svg, y_end_2, stroke=COLORS['accent'], stroke_width=2)
    
    svg.text("x₂", Point(x_end_2.x, x_end_2.y + 20), fill=COLORS['accent'], font_weight="bold")
    svg.text("y₂", Point(y_end_2.x - 20, y_end_2.y), fill=COLORS['accent'], font_weight="bold")
    
    # Punto P en (7, 5)
    p_real = Point(7, 5)
    p_svg = cs.to_svg(p_real)
    
    # Vectores posición
    # Desde O1
    svg.arrow(o1_svg, p_svg, stroke=COLORS['primary'], stroke_width=1.5)
    
    # Desde O2
    svg.arrow(o2_svg, p_svg, stroke=COLORS['accent'], stroke_width=1.5)
    
    # Puntos
    cs.draw_point(svg, o1_pos, label="O₁(0, 0)", show_coords=False, color=COLORS['primary'], label_offset=(-10, 20))
    # O2 en azul (primary) porque su posición es relativa a O1
    cs.draw_point(svg, o2_real, label="O₂(6, 1)", show_coords=False, color=COLORS['primary'], label_offset=(-10, 25))
    cs.draw_point(svg, p_real, label="P(7, 5)", show_coords=False, color=COLORS['secondary'], label_offset=(10, -10))
    
    # Etiquetas de coordenadas
    # Posicionar texto donde no estorbe (ej: x=1.5, y=6.5)
    pos_text_1 = cs.to_svg(Point(1.5, 6.5))
    pos_text_2 = cs.to_svg(Point(1.5, 6.0))
    
    coord_text_1 = f"Respecto a O₁: ({p_real.x}, {p_real.y})"
    coord_text_2 = f"Respecto a O₂: ({p_real.x - o2_real.x}, {p_real.y - o2_real.y})"
    
    svg.text(coord_text_1, pos_text_1, fill=COLORS['primary'], font_size=14, font_weight="bold")
    svg.text(coord_text_2, pos_text_2, fill=COLORS['accent'], font_size=14, font_weight="bold")
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_posicion_1d(output_path: str, 
                       origin_label: str,
                       points: list, 
                       x_range: tuple,
                       title: str = "Posición en 1D"):
    """
    Renderiza una línea de números 1D con puntos.
    points: lista de tuplas (coordenada, etiqueta, color)
    """
    width, height = 600, 180
    
    # Calcular coordenadas x SVG
    padding = 40
    draw_width = width - 2 * padding
    x_min, x_max = x_range
    scale = draw_width / (x_max - x_min)
    
    def get_x(val):
        return padding + (val - x_min) * scale
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text(title, Point(width/2, 25), font_size=16, font_weight="bold", fill=COLORS['text'])
    
    # Eje
    y_axis = height / 2
    svg.line(Point(padding, y_axis), Point(width - padding, y_axis), 
             stroke=COLORS['axis'], stroke_width=2)
    
    # Flecha eje
    svg.arrow(Point(width - padding - 10, y_axis), Point(width - padding, y_axis),
              stroke=COLORS['axis'], stroke_width=2)
    
    # Marcas y etiquetas
    step = 5 if (x_max - x_min) <= 40 else 10
    start_tick = (int(x_min / step) + (1 if x_min % step != 0 else 0)) * step
    if start_tick < x_min: start_tick += step
    
    for val in range(int(x_min), int(x_max) + 1):
        if val % step == 0:
            x_pos = get_x(val)
            svg.line(Point(x_pos, y_axis - 5), Point(x_pos, y_axis + 5), 
                     stroke=COLORS['axis'], stroke_width=1)
            svg.text(str(val), Point(x_pos, y_axis + 20), 
                     font_size=10, fill=COLORS['text_light'])
            
    # Puntos de interés
    for pos, label, color in points:
        x_pos = get_x(pos)
        
        # Punto
        svg.circle(Point(x_pos, y_axis), 5, fill=color)
        
        # Etiqueta nombre (arriba)
        svg.text(label, Point(x_pos, y_axis - 15), 
                 font_size=12, font_weight="bold", fill=color)
        
        # Etiqueta valor (abajo, más destacado)
        sign = "+" if pos > 0 else ""
        val_text = f"x={sign}{pos}"
        if pos == 0: val_text = "x=0"
        
        svg.text(val_text, Point(x_pos, y_axis + 35), 
                 font_size=12, font_weight="bold", fill=color)

    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_plaza_ana(output_path: str):
    """
    Renderiza el ejemplo 4 (Plaza) con origen en Ana.
    """
    width, height = 600, 450
    
    # Rango para Ana(0,0), Beto(3,4), Carlos(6,0)
    # x: -1 a 8, y: -1 a 6
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, 8), y_range=(-1, 6),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Ejes
    cs.draw_grid(svg, step=1)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=1, show_labels=True)
    
    # Puntos
    p_ana = (0, 0)
    p_beto = (3, 4)
    p_carlos = (6, 0)
    
    svg_ana = cs.to_svg(Point(*p_ana))
    svg_beto = cs.to_svg(Point(*p_beto))
    svg_carlos = cs.to_svg(Point(*p_carlos))
    
    # Vectores desde Ana
    svg.arrow(svg_ana, svg_beto, stroke=COLORS['primary'], stroke_width=2)
    svg.arrow(svg_ana, svg_carlos, stroke=COLORS['secondary'], stroke_width=2)
    
    # Dibujar puntos
    cs.draw_point(svg, Point(*p_ana), label="Ana", color=COLORS['accent'], show_coords=True)
    cs.draw_point(svg, Point(*p_beto), label="Beto", color=COLORS['primary'], show_coords=True)
    cs.draw_point(svg, Point(*p_carlos), label="Carlos", color=COLORS['secondary'], show_coords=True)
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_plaza_carlos(output_path: str):
    """
    Renderiza el ejemplo 4 (Plaza) con origen en Carlos.
    """
    width, height = 600, 450
    
    # Rango para Carlos(0,0), Ana(-6,0), Beto(-3,4)
    # x: -7 a 2, y: -1 a 6
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-7, 2), y_range=(-1, 6),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Ejes
    cs.draw_grid(svg, step=1)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=1, show_labels=True)
    
    # Puntos
    p_carlos = (0, 0)
    p_ana = (-6, 0)
    p_beto = (-3, 4)
    
    svg_carlos = cs.to_svg(Point(*p_carlos))
    svg_ana = cs.to_svg(Point(*p_ana))
    svg_beto = cs.to_svg(Point(*p_beto))
    
    # Vectores desde Carlos
    svg.arrow(svg_carlos, svg_ana, stroke=COLORS['accent'], stroke_width=2)
    svg.arrow(svg_carlos, svg_beto, stroke=COLORS['primary'], stroke_width=2)
    
    # Dibujar puntos
    cs.draw_point(svg, Point(*p_carlos), label="Carlos", color=COLORS['secondary'], show_coords=True)
    cs.draw_point(svg, Point(*p_ana), label="Ana", color=COLORS['accent'], show_coords=True)
    cs.draw_point(svg, Point(*p_beto), label="Beto", color=COLORS['primary'], show_coords=True)
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Renderizador de Cinemática")
    parser.add_argument("--type", required=True, help="Tipo de ilustración")
    parser.add_argument("--output", required=True, help="Ruta de salida")
    
    args = parser.parse_args()
    
    if args.type == "posicion_2d":
        render_posicion_2d(args.output, show_coord_labels=False)
    elif args.type == "marcos_referencia":
        render_marcos_referencia(args.output)
    elif args.type == "posicion_1d_rectoria":
        render_posicion_1d(args.output, "Rectoría", [
            (0, "Rectoría", COLORS['secondary']),
            (20, "Salón A", COLORS['primary']),
            (30, "Salón B", COLORS['accent'])
        ], (-5, 35))
    elif args.type == "posicion_1d_salon_a":
        render_posicion_1d(args.output, "Salón A", [
            (-20, "Rectoría", COLORS['secondary']),
            (0, "Salón A", COLORS['primary']),
            (10, "Salón B", COLORS['accent'])
        ], (-25, 15))
    elif args.type == "posicion_1d_salon_b":
        render_posicion_1d(args.output, "Salón B", [
            (-30, "Rectoría", COLORS['secondary']),
            (-10, "Salón A", COLORS['primary']),
            (0, "Salón B", COLORS['accent'])
        ], (-35, 5))
    elif args.type == "atletas_origen_2":
        render_posicion_1d(args.output, "Atleta 2", [
            (-15, "Atleta 1", COLORS['secondary']),
            (0, "Atleta 2", COLORS['primary']),
            (15, "Atleta 3", COLORS['accent'])
        ], (-20, 20))
    elif args.type == "atletas_origen_1":
        render_posicion_1d(args.output, "Atleta 1", [
            (0, "Atleta 1", COLORS['secondary']),
            (15, "Atleta 2", COLORS['primary']),
            (30, "Atleta 3", COLORS['accent'])
        ], (-5, 35))
    elif args.type == "dron_posicion":
        render_posicion_2d(args.output, p=(4, 3), title="Posición del Dron", label_p="Dron", show_coord_labels=False)
    elif args.type == "plaza_ana":
        render_plaza_ana(args.output)
    elif args.type == "plaza_carlos":
        render_plaza_carlos(args.output)
    else:
        print(f"Tipo desconocido: {args.type}")

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

def render_tenista(output_path: str):
    """
    Renderiza el ejemplo del tenista (1D horizontal).
    0 -> 12 -> 6
    """
    width, height = 600, 250
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-2, 14), y_range=(-2, 4),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Movimiento del Tenista", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Eje X
    cs.draw_grid(svg, step=1)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=2, show_labels=True)
    
    # Puntos clave
    p_start = Point(0, 0)
    p_net = Point(12, 0)
    p_end = Point(6, 0)
    
    svg_start = cs.to_svg(p_start)
    svg_net = cs.to_svg(p_net)
    svg_end = cs.to_svg(p_end)
    
    # Trayectoria 1: 0 -> 12 (arriba del eje)
    y_offset_1 = -30 # En SVG y crece hacia abajo, así que negativo es arriba visualmente? No, to_svg invierte Y.
    # CoordinateSystem.to_svg: svg_y = padding + (y_max - p.y) * scale_y
    # Si p.y aumenta, svg_y disminuye (sube).
    # Queremos dibujar flechas desplazadas verticalmente para que no se solapen.
    
    # Usaremos coordenadas matemáticas para los puntos de las flechas y luego convertimos
    p_start_arrow1 = Point(0, 0.5)
    p_net_arrow1 = Point(12, 0.5)
    
    svg_start_arrow1 = cs.to_svg(p_start_arrow1)
    svg_net_arrow1 = cs.to_svg(p_net_arrow1)
    
    svg.arrow(svg_start_arrow1, svg_net_arrow1, stroke=COLORS['primary'], stroke_width=3)
    svg.text("1. Avanza 12m", Point((svg_start_arrow1.x + svg_net_arrow1.x)/2, svg_start_arrow1.y - 15),
             font_size=12, fill=COLORS['primary'], font_weight="bold")
    
    # Trayectoria 2: 12 -> 6 (más arriba)
    p_net_arrow2 = Point(12, 1.5)
    p_end_arrow2 = Point(6, 1.5)
    
    svg_net_arrow2 = cs.to_svg(p_net_arrow2)
    svg_end_arrow2 = cs.to_svg(p_end_arrow2)
    
    svg.arrow(svg_net_arrow2, svg_end_arrow2, stroke=COLORS['accent'], stroke_width=3)
    svg.text("2. Retrocede 6m", Point((svg_net_arrow2.x + svg_end_arrow2.x)/2, svg_net_arrow2.y - 15),
             font_size=12, fill=COLORS['accent'], font_weight="bold")
    
    # Puntos en el eje
    cs.draw_point(svg, p_start, label="Inicio (0)", color=COLORS['secondary'], show_coords=False, label_offset=(-10, -20))
    cs.draw_point(svg, p_net, label="Red (12)", color=COLORS['primary'], show_coords=False, label_offset=(-10, -20))
    cs.draw_point(svg, p_end, label="Fin (6)", color=COLORS['accent'], show_coords=False, label_offset=(-10, -20))
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_ascensor(output_path: str):
    """
    Renderiza el ejemplo del ascensor (1D vertical).
    0 -> 20 -> -4
    """
    width, height = 350, 600
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-4, 6), y_range=(-10, 25),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Movimiento del Ascensor", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Eje Y (dibujamos grid solo horizontal)
    cs.draw_grid(svg, step=5)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=5, show_labels=True)
    
    # Trayectoria 1: 0 -> 20 (desplazada a la derecha)
    p_start = Point(1, 0)
    p_top = Point(1, 20)
    
    svg_start = cs.to_svg(p_start)
    svg_top = cs.to_svg(p_top)
    
    svg.arrow(svg_start, svg_top, stroke=COLORS['primary'], stroke_width=3)
    svg.text("1. Sube 20m", Point(svg_start.x + 40, (svg_start.y + svg_top.y)/2),
             font_size=12, fill=COLORS['primary'], font_weight="bold", anchor="start")
    
    # Trayectoria 2: 20 -> -4 (desplazada más a la derecha)
    p_top_2 = Point(2.5, 20)
    p_end = Point(2.5, -4)
    
    svg_top_2 = cs.to_svg(p_top_2)
    svg_end = cs.to_svg(p_end)
    
    svg.arrow(svg_top_2, svg_end, stroke=COLORS['accent'], stroke_width=3)
    svg.text("2. Baja 24m", Point(svg_top_2.x + 10, (svg_top_2.y + svg_end.y)/2),
             font_size=12, fill=COLORS['accent'], font_weight="bold", anchor="start")
    
    # Puntos clave en el eje
    cs.draw_point(svg, Point(0, 0), label="Inicio (0)", color=COLORS['secondary'], show_coords=False, label_offset=(-60, 5))
    cs.draw_point(svg, Point(0, 20), label="Piso 20", color=COLORS['primary'], show_coords=False, label_offset=(-60, 5))
    cs.draw_point(svg, Point(0, -4), label="Sótano (-4)", color=COLORS['accent'], show_coords=False, label_offset=(-70, 5))
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_vuelta_manzana(output_path: str):
    """
    Renderiza trayectoria circular.
    """
    width, height = 500, 500
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Vuelta a la Manzana", Point(width/2, 30), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    center = Point(width/2, height/2)
    radius = 150
    
    # Círculo trayectoria
    svg.circle(center, radius, stroke=COLORS['primary'], stroke_width=3, fill="none", dashed=True)
    
    # Flecha indicando dirección (curva aproximada o simple flecha tangente)
    # Dibujamos un arco o flechas en el círculo
    top_point = Point(center.x, center.y - radius)
    right_point = Point(center.x + radius, center.y)
    
    # Flecha curva (simulada con path)
    # Move to top, arc to right
    path_d = f"M {center.x} {center.y - radius} A {radius} {radius} 0 0 1 {center.x + radius} {center.y}"
    # Esto es SVG path manual, SVGBuilder necesita soporte para 'path' o 'arc'
    # Como SVGBuilder es básico, usaremos líneas o 'arrow' rectas cortas para indicar dirección
    
    svg.arrow(Point(center.x - 20, center.y - radius), Point(center.x + 20, center.y - radius), 
              stroke=COLORS['primary'], stroke_width=3)
    
    # Texto
    svg.text("400 m recorridos", Point(center.x, center.y - radius - 20), 
             font_size=14, fill=COLORS['primary'], font_weight="bold")
    
    # Punto Inicio/Fin
    start_point = Point(center.x + radius, center.y)
    svg.circle(start_point, 6, fill=COLORS['success'])
    svg.text("Inicio / Fin", Point(start_point.x + 15, start_point.y), 
             font_size=14, fill=COLORS['success'], font_weight="bold", anchor="start")
    
    # Etiqueta central
    svg.text("Desplazamiento = 0", Point(center.x, center.y), 
             font_size=16, fill=COLORS['danger'], font_weight="bold")
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_caminata_2d(output_path: str):
    """
    Renderiza caminata 2D: 30m Norte, 40m Este.
    """
    width, height = 600, 500
    
    # Rango: x(0-50), y(0-40)
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-10, 60), y_range=(-10, 50),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Caminata en 2D", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Ejes
    cs.draw_grid(svg, step=10)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=10, show_labels=True)
    
    # Puntos
    p_start = Point(0, 0)
    p_mid = Point(0, 30)
    p_end = Point(40, 30)
    
    svg_start = cs.to_svg(p_start)
    svg_mid = cs.to_svg(p_mid)
    svg_end = cs.to_svg(p_end)
    
    # Vectores trayectoria
    svg.arrow(svg_start, svg_mid, stroke=COLORS['primary'], stroke_width=3)
    svg.text("30m N", Point(svg_start.x - 30, (svg_start.y + svg_mid.y)/2), 
             font_size=12, fill=COLORS['primary'], font_weight="bold")
    
    svg.arrow(svg_mid, svg_end, stroke=COLORS['primary'], stroke_width=3)
    svg.text("40m E", Point((svg_mid.x + svg_end.x)/2, svg_mid.y - 15), 
             font_size=12, fill=COLORS['primary'], font_weight="bold")
    
    # Vector desplazamiento
    svg.arrow(svg_start, svg_end, stroke=COLORS['success'], stroke_width=3, dashed=True)
    mid_disp = Point((svg_start.x + svg_end.x)/2, (svg_start.y + svg_end.y)/2)
    svg.text("Δx = 50m", Point(mid_disp.x + 10, mid_disp.y + 20), 
             font_size=14, fill=COLORS['success'], font_weight="bold")
    
    # Puntos
    cs.draw_point(svg, p_start, label="Inicio", color=COLORS['secondary'], show_coords=True, label_offset=(-20, 20))
    cs.draw_point(svg, p_end, label="Fin", color=COLORS['danger'], show_coords=True, label_offset=(10, -10))
    
    # Triángulo rectángulo auxiliar (para Pitágoras)
    # Ya está implícito con los ejes, pero podemos resaltarlo si queremos
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_atleta_100m(output_path: str):
    """
    Renderiza carrera de 100m.
    """
    width, height = 600, 200
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-10, 110), y_range=(-1, 2),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Carrera de 100 metros", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Eje X
    cs.draw_grid(svg, step=10)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=10, show_labels=True)
    
    # Puntos
    p_start = Point(0, 0)
    p_end = Point(100, 0)
    
    svg_start = cs.to_svg(p_start)
    svg_end = cs.to_svg(p_end)
    
    # Flecha trayectoria
    p_arrow_start = Point(0, 0.5)
    p_arrow_end = Point(100, 0.5)
    
    svg_arrow_start = cs.to_svg(p_arrow_start)
    svg_arrow_end = cs.to_svg(p_arrow_end)
    
    svg.arrow(svg_arrow_start, svg_arrow_end, stroke=COLORS['primary'], stroke_width=3)
    svg.text("d = 100 m", Point((svg_arrow_start.x + svg_arrow_end.x)/2, svg_arrow_start.y - 15),
             font_size=12, fill=COLORS['primary'], font_weight="bold")
    
    # Puntos
    cs.draw_point(svg, p_start, label="Salida", color=COLORS['success'], show_coords=True, label_offset=(-10, -20))
    cs.draw_point(svg, p_end, label="Meta", color=COLORS['danger'], show_coords=True, label_offset=(-10, -20))
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_caminata_ida_vuelta(output_path: str):
    """
    Renderiza caminata ida (60m) y vuelta (20m).
    """
    width, height = 600, 250
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-10, 70), y_range=(-2, 4),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Caminata de Ida y Vuelta", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Eje X
    cs.draw_grid(svg, step=10)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=10, show_labels=True)
    
    # Puntos
    p_start = Point(0, 0)
    p_turn = Point(60, 0)
    p_end = Point(40, 0)
    
    # Trayectoria 1: Ida (0 -> 60)
    p_arrow1_start = Point(0, 0.5)
    p_arrow1_end = Point(60, 0.5)
    svg_arrow1_start = cs.to_svg(p_arrow1_start)
    svg_arrow1_end = cs.to_svg(p_arrow1_end)
    
    svg.arrow(svg_arrow1_start, svg_arrow1_end, stroke=COLORS['primary'], stroke_width=3)
    svg.text("1. Ida: 60m (Este)", Point((svg_arrow1_start.x + svg_arrow1_end.x)/2, svg_arrow1_start.y - 15),
             font_size=12, fill=COLORS['primary'], font_weight="bold")
    
    # Trayectoria 2: Vuelta (60 -> 40)
    p_arrow2_start = Point(60, 1.5)
    p_arrow2_end = Point(40, 1.5)
    svg_arrow2_start = cs.to_svg(p_arrow2_start)
    svg_arrow2_end = cs.to_svg(p_arrow2_end)
    
    svg.arrow(svg_arrow2_start, svg_arrow2_end, stroke=COLORS['danger'], stroke_width=3)
    svg.text("2. Vuelta: 20m (Oeste)", Point((svg_arrow2_start.x + svg_arrow2_end.x)/2, svg_arrow2_start.y - 15),
             font_size=12, fill=COLORS['danger'], font_weight="bold")
    
    # Puntos
    cs.draw_point(svg, p_start, label="Inicio", color=COLORS['success'], show_coords=True, label_offset=(-10, -20))
    cs.draw_point(svg, p_turn, label="Giro", color=COLORS['primary'], show_coords=True, label_offset=(-10, -20))
    cs.draw_point(svg, p_end, label="Fin", color=COLORS['danger'], show_coords=True, label_offset=(-10, -20))
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_velodromo(output_path: str):
    """
    Renderiza vuelta al velódromo (500m).
    """
    width, height = 500, 500
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Vuelta al Velódromo", Point(width/2, 30), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    center = Point(width/2, height/2)
    radius = 150
    
    # Círculo trayectoria
    svg.circle(center, radius, stroke=COLORS['primary'], stroke_width=3, fill="none", dashed=True)
    
    # Flechas indicando dirección
    svg.arrow(Point(center.x - 20, center.y - radius), Point(center.x + 20, center.y - radius), 
              stroke=COLORS['primary'], stroke_width=3)
    svg.arrow(Point(center.x + 20, center.y + radius), Point(center.x - 20, center.y + radius), 
              stroke=COLORS['primary'], stroke_width=3)
    
    # Texto
    svg.text("d = 500 m", Point(center.x, center.y - radius - 20), 
             font_size=14, fill=COLORS['primary'], font_weight="bold")
    
    # Punto Inicio/Fin
    start_point = Point(center.x + radius, center.y)
    svg.circle(start_point, 6, fill=COLORS['success'])
    svg.text("Inicio / Fin", Point(start_point.x + 15, start_point.y), 
             font_size=14, fill=COLORS['success'], font_weight="bold", anchor="start")
    
    # Etiqueta central
    svg.text("Desplazamiento = 0", Point(center.x, center.y), 
             font_size=16, fill=COLORS['danger'], font_weight="bold")
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_robot_L(output_path: str):
    """
    Renderiza movimiento en L del robot (3m N, 4m E).
    """
    width, height = 600, 500
    
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, 6), y_range=(-1, 5),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Movimiento del Robot", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Ejes
    cs.draw_grid(svg, step=1)
    cs.draw_axes(svg, show_arrows=True)
    cs.draw_ticks(svg, step=1, show_labels=True)
    
    # Puntos
    p_start = Point(0, 0)
    p_mid = Point(0, 3)
    p_end = Point(4, 3)
    
    svg_start = cs.to_svg(p_start)
    svg_mid = cs.to_svg(p_mid)
    svg_end = cs.to_svg(p_end)
    
    # Vectores trayectoria
    # 1. Norte (0,0) -> (0,3)
    svg.arrow(svg_start, svg_mid, stroke=COLORS['primary'], stroke_width=3)
    svg.text("3m N", Point(svg_start.x - 20, (svg_start.y + svg_mid.y)/2), 
             font_size=12, fill=COLORS['primary'], font_weight="bold", anchor="end")
    
    # 2. Este (0,3) -> (4,3)
    svg.arrow(svg_mid, svg_end, stroke=COLORS['primary'], stroke_width=3)
    svg.text("4m E", Point((svg_mid.x + svg_end.x)/2, svg_mid.y - 15), 
             font_size=12, fill=COLORS['primary'], font_weight="bold")
    
    # Vector desplazamiento
    svg.arrow(svg_start, svg_end, stroke=COLORS['success'], stroke_width=3, dashed=True)
    mid_disp = Point((svg_start.x + svg_end.x)/2, (svg_start.y + svg_end.y)/2)
    svg.text("Δx = 5m", Point(mid_disp.x + 10, mid_disp.y + 20), 
             font_size=14, fill=COLORS['success'], font_weight="bold")
    
    # Puntos
    cs.draw_point(svg, p_start, label="Inicio", color=COLORS['secondary'], show_coords=True, label_offset=(-10, 20))
    cs.draw_point(svg, p_end, label="Fin", color=COLORS['danger'], show_coords=True, label_offset=(10, -10))
    
    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_mru_posicion_tiempo(output_path: str):
    """
    Renderiza gráfico Posición vs Tiempo para MRU (robot).
    t: 0, 1, 2, 3
    x: 0, 4, 8, 12
    """
    width, height = 600, 400
    
    # Rango t (0-4), x (0-14)
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-0.5, 4.5), y_range=(-2, 14),
        padding=50
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Posición del robot vs Tiempo", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Ejes
    cs.draw_grid(svg, step=1)
    
    # Eje X - Tiempo
    x_axis_end = cs.to_svg(Point(4.5, 0))
    y_axis_end = cs.to_svg(Point(0, 14))
    
    cs.draw_axes(svg, show_arrows=True)
    
    # Etiquetas ejes
    svg.text("Tiempo (s)", Point(x_axis_end.x - 40, x_axis_end.y + 35), 
             font_size=14, font_weight="bold", fill=COLORS['text'])
    svg.text("Posición (m)", Point(y_axis_end.x, y_axis_end.y - 20), 
             font_size=14, font_weight="bold", fill=COLORS['text'])
    
    # Ticks customizados
    # X: 0, 1, 2, 3, 4
    for t in range(5):
        pt = cs.to_svg(Point(t, 0))
        svg.line(Point(pt.x, pt.y-5), Point(pt.x, pt.y+5), stroke=COLORS['axis'], stroke_width=1)
        svg.text(str(t), Point(pt.x, pt.y+20), font_size=12, fill=COLORS['text_light'])
        
    # Y: 0, 2, 4, 6, 8, 10, 12, 14
    for x in range(0, 15, 2):
        if x == 0: continue
        pt = cs.to_svg(Point(0, x))
        svg.line(Point(pt.x-5, pt.y), Point(pt.x+5, pt.y), stroke=COLORS['axis'], stroke_width=1)
        svg.text(str(x), Point(pt.x-20, pt.y+5), font_size=12, fill=COLORS['text_light'], anchor="end")

    # Datos
    points = [
        (0, 0),
        (1, 4),
        (2, 8),
        (3, 12)
    ]
    
    # Línea
    svg_points = [cs.to_svg(Point(t, x)) for t, x in points]
    for i in range(len(svg_points) - 1):
        svg.line(svg_points[i], svg_points[i+1], stroke=COLORS['primary'], stroke_width=3)
        
    # Puntos
    for i, (t, x) in enumerate(points):
        pt = svg_points[i]
        cs.draw_point(svg, Point(t, x), color=COLORS['primary'], show_coords=False)
        # Etiqueta valor
        svg.text(f"{x}m", Point(pt.x, pt.y - 15), font_size=12, fill=COLORS['primary'], font_weight="bold")

    svg.save(output_path)
    print(f"✅ SVG generado: {output_path}")

def render_mrua_moto(output_path: str):
    """
    Renderiza mapa de movimiento para MRUA (a=2 m/s^2).
    t=0 (0m), t=1 (1m), t=2 (4m), t=3 (9m)
    """
    width, height = 700, 250
    
    # Rango x: 0 a 10m.
    cs = CoordinateSystem(
        svg_width=width, svg_height=height,
        x_range=(-1, 11), y_range=(-1, 4),
        padding=40
    )
    
    svg = SVGBuilder(width, height)
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    svg.text("Mapa de Movimiento (a = 2 m/s²)", Point(width/2, 25), 
             font_size=18, font_weight="bold", fill=COLORS['text'])
    
    # Eje X (Suelo)
    # Usamos coordinate system para dibujar el eje
    start_line = cs.to_svg(Point(0, 0))
    end_line = cs.to_svg(Point(10, 0))
    # Extendemos un poco visualmente
    svg.line(Point(40, start_line.y), Point(width-40, start_line.y), stroke=COLORS['axis'], stroke_width=1)
    
    # Datos
    # t, x, v
    data = [
        (0, 0, 0),
        (1, 1, 2),
        (2, 4, 4),
        (3, 9, 6)
    ]
    
    # Dibujar cada instante
    for t, x, v in data:
        # Posición en SVG
        pt = cs.to_svg(Point(x, 0))
        
        # Dibujar Moto (Punto)
        cs.draw_point(svg, Point(x, 0), color=COLORS['primary'], show_coords=False)
        
        # Etiqueta Tiempo (Arriba)
        svg.text(f"t={t}s", Point(pt.x, pt.y - 40), font_size=12, fill=COLORS['text_light'], font_weight="bold")
        
        # Etiqueta Posición (Abajo del eje)
        svg.text(f"x={x}m", Point(pt.x, pt.y + 25), font_size=12, fill=COLORS['text_light'])
        
        # Vector Velocidad (Verde) - Escala visual
        if v > 0:
            v_len = v * 0.5 # Factor de escala
            # Calculamos punto final en unidades SVG directamente para controlar longitud visual
            # 1 unidad de coord system = scale_x pixeles
            scale_x = cs.scale_x
            pixel_len = v_len * scale_x
            
            arrow_y_offset = -15 
            p_start = Point(pt.x, pt.y + arrow_y_offset)
            p_end = Point(pt.x + pixel_len, pt.y + arrow_y_offset)
            
            svg.arrow(p_start, p_end, stroke=COLORS['success'], stroke_width=3)
            svg.text(f"v={v}", Point((p_start.x + p_end.x)/2, p_start.y - 10), 
                     font_size=10, fill=COLORS['success'], font_weight="bold")
            
        # Vector Aceleración (Naranja) - Constante
        # Dibujar debajo de la posición
        a_len = 2 * 0.5
        scale_x = cs.scale_x
        pixel_len_a = a_len * scale_x
        
        arrow_y_offset_a = 45
        p_start_a = Point(pt.x, pt.y + arrow_y_offset_a)
        p_end_a = Point(pt.x + pixel_len_a, pt.y + arrow_y_offset_a)
        
        svg.arrow(p_start_a, p_end_a, stroke=COLORS['danger'], stroke_width=2)
        svg.text("a=2", Point((p_start_a.x + p_end_a.x)/2, p_start_a.y + 15), 
                 font_size=10, fill=COLORS['danger'], font_weight="bold")

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
    elif args.type == "tenista":
        render_tenista(args.output)
    elif args.type == "ascensor":
        render_ascensor(args.output)
    elif args.type == "vuelta_manzana":
        render_vuelta_manzana(args.output)
    elif args.type == "caminata_2d":
        render_caminata_2d(args.output)
    elif args.type == "atleta_100m":
        render_atleta_100m(args.output)
    elif args.type == "caminata_ida_vuelta":
        render_caminata_ida_vuelta(args.output)
    elif args.type == "velodromo":
        render_velodromo(args.output)
    elif args.type == "robot_L":
        render_robot_L(args.output)
    elif args.type == "mru_posicion_tiempo":
        render_mru_posicion_tiempo(args.output)
    elif args.type == "mrua_moto":
        render_mrua_moto(args.output)
    else:
        print(f"Tipo desconocido: {args.type}")

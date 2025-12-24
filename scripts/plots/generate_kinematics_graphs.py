import sys
import os
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.geometry.core.plotter import MathPlotter
from scripts.geometry.core.colors import COLORS
from scripts.geometry.core.base import Point

OUTPUT_DIR = "public/images/fisica/cinematica/graficas"

def save_plot(plot, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    plot.save(path)

def generate_reposo():
    print("Generating Reposo...")
    # x vs t: x=4
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 8), title="x vs t", grid_step=2, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: 4, color='primary', width=3)
    save_plot(p, "reposo-x.svg")

    # v vs t: v=0
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-2, 4), title="v vs t", x_label="t (s)", y_label="v (m/s)")
    p.plot(lambda t: 0, color='secondary', width=3)
    save_plot(p, "reposo-v.svg")

    # a vs t: a=0
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-2, 2), title="a vs t", x_label="t (s)", y_label="a (m/s²)")
    p.plot(lambda t: 0, color='accent', width=3)
    save_plot(p, "reposo-a.svg")

def generate_mru_adelante():
    print("Generating MRU Adelante...")
    # x vs t: x = 4t
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 18), title="x vs t", grid_step=4, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: 4*t, color='primary', width=3)
    save_plot(p, "mru-adelante-x.svg")

    # v vs t: v=4
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 6), title="v vs t", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    p.plot(lambda t: 4, color='secondary', width=3)
    save_plot(p, "mru-adelante-v.svg")

    # a vs t: a=0
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-2, 2), title="a vs t", x_label="t (s)", y_label="a (m/s²)")
    p.plot(lambda t: 0, color='accent', width=3)
    save_plot(p, "mru-adelante-a.svg")

def generate_mru_atras():
    print("Generating MRU Atras...")
    # x vs t: x = 16 - 4t
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 18), title="x vs t", grid_step=4, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: 16 - 4*t, color='primary', width=3)
    save_plot(p, "mru-atras-x.svg")

    # v vs t: v=-4
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-6, 2), title="v vs t", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    p.plot(lambda t: -4, color='secondary', width=3)
    save_plot(p, "mru-atras-v.svg")

    # a vs t: a=0
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-2, 2), title="a vs t", x_label="t (s)", y_label="a (m/s²)")
    p.plot(lambda t: 0, color='accent', width=3)
    save_plot(p, "mru-atras-a.svg")

def generate_mrua_acelera():
    print("Generating MRUA Acelera...")
    # x vs t: x = t^2
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 18), title="x vs t", grid_step=4, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: t**2, color='primary', width=3)
    save_plot(p, "mrua-acelera-x.svg")

    # v vs t: v = 2t
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 10), title="v vs t", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    p.plot(lambda t: 2*t, color='secondary', width=3)
    save_plot(p, "mrua-acelera-v.svg")

    # a vs t: a = 2
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 4), title="a vs t", grid_step=1, x_label="t (s)", y_label="a (m/s²)")
    p.plot(lambda t: 2, color='accent', width=3)
    save_plot(p, "mrua-acelera-a.svg")

def generate_mrua_frena():
    print("Generating MRUA Frena...")
    # x vs t: x = 8t - t^2 (starts at 0, v0=8, a=-2) -> v = 8 - 2t. At t=4, v=0. x(4) = 32-16=16.
    # Original data: [[0, 0], [1, 7], [2, 12], [3, 15], [4, 16]]
    # Formula: x = 8t - t^2 fits perfectly: 0, 7, 12, 15, 16.
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 18), title="x vs t", grid_step=4, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: 8*t - t**2, color='primary', width=3)
    save_plot(p, "mrua-frena-x.svg")

    # v vs t: v = 8 - 2t
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 10), title="v vs t", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    p.plot(lambda t: 8 - 2*t, color='secondary', width=3)
    save_plot(p, "mrua-frena-v.svg")

    # a vs t: a=-2
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-4, 1), title="a vs t", x_label="t (s)", y_label="a (m/s²)")
    p.plot(lambda t: -2, color='accent', width=3)
    save_plot(p, "mrua-frena-a.svg")

def generate_ejercicio_1():
    print("Generating Ejercicio 1...")
    # Ciclista: Piecewise linear
    # (0,0)->(5,5)->(10,5)->(15,10)->(20,10)
    p = MathPlotter(width=600, height=300, x_range=(0, 22), y_range=(0, 12), title="Ejercicio 1: El ciclista", x_label="t (s)", y_label="x (m)")
    
    points = [Point(0,0), Point(5,5), Point(10,5), Point(15,10), Point(20,10)]
    svg_points = [p.coord.to_svg(pt) for pt in points]
    
    p.builder.polyline(svg_points, stroke=COLORS['primary'], stroke_width=3)
    
    # Add points
    for pt in points:
        p.scatter(pt.x, pt.y, color='primary')
        
    save_plot(p, "ejercicio-1-ciclista.svg")

def generate_ejercicio_2():
    print("Generating Ejercicio 2...")
    # Carrera de autos
    # Auto A: v=8 (constante)
    # Auto B: v=4t (linear from 0 to 16 in 4s)
    # grid_step=2 to reduce tick density
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 18), title="Ejercicio 2: Carrera de autos", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    
    # Auto A Area
    # Rect (0,0) to (4,8)
    pts_a = [Point(0,0), Point(4,0), Point(4,8), Point(0,8)]
    svg_pts_a = [p.coord.to_svg(pt) for pt in pts_a]
    p.builder.polygon(svg_pts_a, fill=COLORS['primary'], stroke='none')
    # Add opacity manually to the last element
    p.builder.elements[-1] = p.builder.elements[-1].replace('fill-opacity="1"', 'fill-opacity="0.2"').replace('/>', ' fill-opacity="0.2"/>')

    # Auto B Area
    # Triangle (0,0), (4,0), (4,16)
    pts_b = [Point(0,0), Point(4,0), Point(4,16)]
    svg_pts_b = [p.coord.to_svg(pt) for pt in pts_b]
    p.builder.polygon(svg_pts_b, fill=COLORS['secondary'], stroke='none')
    p.builder.elements[-1] = p.builder.elements[-1].replace('fill-opacity="1"', 'fill-opacity="0.2"').replace('/>', ' fill-opacity="0.2"/>')

    # Lines
    p.plot(lambda t: 8, label="Auto A", color='primary', width=3)
    p.plot(lambda t: 4*t, label="Auto B", color='secondary', width=3)
    
    # Move legend to top-left (x=80, y=60) to avoid covering the graph on the right
    p.add_legend(x=80, y=60)
    save_plot(p, "ejercicio-2-carrera.svg")

def generate_ejercicio_3():
    print("Generating Ejercicio 3...")
    # Tren frenando
    # v goes from 20 to 0 in 10s. v = 20 - 2t
    # grid_step=5 to reduce tick density
    p = MathPlotter(width=600, height=300, x_range=(0, 11), y_range=(0, 25), title="Ejercicio 3: Tren frenando", grid_step=5, x_label="t (s)", y_label="v (m/s)")
    
    # Area
    pts = [Point(0,0), Point(10,0), Point(0,20)]
    svg_pts = [p.coord.to_svg(pt) for pt in pts]
    p.builder.polygon(svg_pts, fill=COLORS['secondary'], stroke='none')
    p.builder.elements[-1] = p.builder.elements[-1].replace('/>', ' fill-opacity="0.2"/>')
    
    p.plot(lambda t: 20 - 2*t, color='secondary', width=3)
    
    save_plot(p, "ejercicio-3-tren.svg")

def generate_ejercicio_4():
    print("Generating Ejercicio 4...")
    # Pelota lanzada
    # v = 20 - 10t. t=0->20, t=2->0, t=4->-20
    # grid_step=5 to reduce tick density
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(-25, 25), title="Ejercicio 4: Pelota lanzada", grid_step=5, x_label="t (s)", y_label="v (m/s)")
    
    p.plot(lambda t: 20 - 10*t, color='purple', width=3)
    
    # Points
    for t in [0, 1, 2, 3, 4]:
        v = 20 - 10*t
        p.scatter(t, v, color='purple')
        
    save_plot(p, "ejercicio-4-pelota.svg")

def generate_ejercicio_5():
    print("Generating Ejercicio 5...")
    # Comparacion
    # A: (0,0)->(4,8) => v=2
    # B: (0,0)->(4,16) => v=4
    # C: (0,0)->(4,24) => v=6
    # grid_step=5 to reduce tick density
    p = MathPlotter(width=600, height=300, x_range=(0, 4.5), y_range=(0, 26), title="Ejercicio 5: Comparación", grid_step=5, x_label="t (s)", y_label="x (m)")
    
    p.plot(lambda t: 2*t, label="Objeto A", color='primary', width=3)
    p.plot(lambda t: 4*t, label="Objeto B", color='secondary', width=3)
    p.plot(lambda t: 6*t, label="Objeto C", color='accent', width=3)
    
    # Move legend to top-left (x=80, y=60)
    p.add_legend(x=80, y=60)
    save_plot(p, "ejercicio-5-comparacion.svg")

def generate_ejercicio_6():
    print("Generating Ejercicio 6...")
    # Velocidad negativa
    # x starts at 12, goes to 0 in 6s. v = -2.
    p = MathPlotter(width=600, height=300, x_range=(0, 7), y_range=(0, 14), title="Ejercicio 6: Regreso a casa", grid_step=2, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: 12 - 2*t, color='primary', width=3)
    save_plot(p, "ejercicio-6-regreso.svg")

def generate_ejercicio_7():
    print("Generating Ejercicio 7...")
    # Desplazamiento ida y vuelta
    # v-t: 0-3s v=4, 3-6s v=-4
    p = MathPlotter(width=600, height=300, x_range=(0, 7), y_range=(-6, 6), title="Ejercicio 7: Ida y vuelta", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    
    # Area 1 (Positive)
    pts1 = [Point(0,0), Point(3,0), Point(3,4), Point(0,4)]
    svg_pts1 = [p.coord.to_svg(pt) for pt in pts1]
    p.builder.polygon(svg_pts1, fill=COLORS['primary'], stroke='none')
    p.builder.elements[-1] = p.builder.elements[-1].replace('/>', ' fill-opacity="0.2"/>')

    # Area 2 (Negative)
    pts2 = [Point(3,0), Point(6,0), Point(6,-4), Point(3,-4)]
    svg_pts2 = [p.coord.to_svg(pt) for pt in pts2]
    p.builder.polygon(svg_pts2, fill=COLORS['secondary'], stroke='none')
    p.builder.elements[-1] = p.builder.elements[-1].replace('/>', ' fill-opacity="0.2"/>')

    # Lines
    p.plot(lambda t: 4 if t < 3 else -4, color='text', width=3) # Simplified drawing
    # Better to draw segments
    p1 = [Point(0,4), Point(3,4)]
    p2 = [Point(3,-4), Point(6,-4)]
    p3 = [Point(3,4), Point(3,-4)] # Vertical connector
    
    p.builder.polyline([p.coord.to_svg(pt) for pt in p1], stroke=COLORS['primary'], stroke_width=3)
    p.builder.polyline([p.coord.to_svg(pt) for pt in p2], stroke=COLORS['secondary'], stroke_width=3)
    
    # Use line for dashed segment
    p3_start = p.coord.to_svg(Point(3,4))
    p3_end = p.coord.to_svg(Point(3,-4))
    p.builder.line(p3_start, p3_end, stroke=COLORS['text'], stroke_width=1, dashed=True)

    save_plot(p, "ejercicio-7-ida-vuelta.svg")

def generate_ejercicio_8():
    print("Generating Ejercicio 8...")
    # Aceleracion desde v-t
    # v goes 0->10 in 5s.
    p = MathPlotter(width=600, height=300, x_range=(0, 6), y_range=(0, 12), title="Ejercicio 8: Despegue", grid_step=2, x_label="t (s)", y_label="v (m/s)")
    p.plot(lambda t: 2*t, color='accent', width=3)
    save_plot(p, "ejercicio-8-despegue.svg")

def generate_ejercicio_9():
    print("Generating Ejercicio 9...")
    # Encuentro
    # A: x = 2t
    # B: x = 12 - t
    # Meet at 2t = 12-t => 3t=12 => t=4. x=8.
    p = MathPlotter(width=600, height=300, x_range=(0, 6), y_range=(0, 14), title="Ejercicio 9: El encuentro", grid_step=2, x_label="t (s)", y_label="x (m)")
    p.plot(lambda t: 2*t, label="Corredor A", color='primary', width=3)
    p.plot(lambda t: 12 - t, label="Corredor B", color='secondary', width=3)
    p.add_legend(x=80, y=60)
    save_plot(p, "ejercicio-9-encuentro.svg")

def generate_ejercicio_10():
    print("Generating Ejercicio 10...")
    # Interpretacion a-t
    # a = 3 constant.
    p = MathPlotter(width=600, height=300, x_range=(0, 5), y_range=(0, 5), title="Ejercicio 10: Aceleración constante", grid_step=1, x_label="t (s)", y_label="a (m/s²)")
    p.plot(lambda t: 3, color='accent', width=3)
    save_plot(p, "ejercicio-10-aceleracion.svg")

if __name__ == "__main__":
    generate_reposo()
    generate_mru_adelante()
    generate_mru_atras()
    generate_mrua_acelera()
    generate_mrua_frena()
    generate_ejercicio_1()
    generate_ejercicio_2()
    generate_ejercicio_3()
    generate_ejercicio_4()
    generate_ejercicio_5()
    generate_ejercicio_6()
    generate_ejercicio_7()
    generate_ejercicio_8()
    generate_ejercicio_9()
    generate_ejercicio_10()

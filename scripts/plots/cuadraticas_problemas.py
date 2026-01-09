
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter
from scripts.geometry.core.base import Point, COLORS

OUTPUT_DIR = "public/images/matematicas/algebra/funciones-ecuaciones-cuadraticas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_ex1_rectangle():
    """Ejemplo 1: Rectángulo 8x12. Área 96."""
    # Using MathPlotter primarily for the coordinate and saving system, 
    # but we will draw geometry manually or semi-manually.
    plot = MathPlotter(
        width=500, height=400,
        x_range=(-2, 14), y_range=(-2, 10),
        title="El Rectángulo",
        show_grid=False, show_axes=False
    )
    
    # Draw Rectangle (0,0) to (12, 8)
    # Math coordinates
    p1 = Point(0, 0)
    p2 = Point(12, 0)
    p3 = Point(12, 8)
    p4 = Point(0, 8)
    
    # To SVG
    svg_p1 = plot.coord.to_svg(p1)
    svg_p3 = plot.coord.to_svg(p3)
    
    width = svg_p3.x - svg_p1.x
    height = svg_p1.y - svg_p3.y 
    
    # Use builder rect
    plot.builder.rect(svg_p1.x, svg_p3.y, width, height, fill=COLORS['primary'], fill_opacity=0.1, stroke=COLORS['primary'], stroke_width=3)
    
    # Labels
    # Base
    plot.builder.text("Largo = x + 4", Point(svg_p1.x + width/2, svg_p1.y + 20), font_size=14, font_weight='bold')
    # Height
    plot.builder.text("Ancho = x", Point(svg_p1.x - 40, svg_p3.y + height/2), font_size=14, font_weight='bold')
    # Area
    plot.builder.text("Área = 96 m²", Point(svg_p1.x + width/2, svg_p3.y + height/2), font_size=16, font_weight='bold', fill=COLORS['text'])
    
    plot.save(f"{OUTPUT_DIR}/problemas_ex1_rectangulo.svg")

def plot_ex2_rocket():
    """Ejemplo 2: Cohete h(t) = -5t^2 + 30t"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-0.5, 7), y_range=(-5, 50),
        title="Trayectoria del Cohete",
        x_label="Tiempo (s)", y_label="Altura (m)",
        grid_step_x=1, grid_step_y=5
    )
    
    func = lambda t: -5*t**2 + 30*t
    plot.plot(func, label="h(t) = -5t² + 30t", color="accent")
    
    # Vertex (3, 45)
    plot.scatter(3, 45, label="Máx (3s, 45m)", color="highlight")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/problemas_ex2_cohete.svg")

def plot_ex3_numbers():
    """Ejemplo 3: n(n+1) = 156. Intersection method."""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 15), y_range=(0, 200),
        title="Producto Números Consecutivos",
        x_label="Número n", y_label="Producto",
        grid_step_x=1, grid_step_y=20
    )
    
    # Curve n(n+1)
    plot.plot(lambda x: x*(x+1), label="Producto n(n+1)", color="primary")
    
    # Target 156
    plot.plot(lambda x: 156, label="Objetivo = 156", color="secondary", dashed=True)
    
    # Intersection
    plot.scatter(12, 156, label="Solución n=12", color="accent")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/problemas_ex3_numeros.svg")

def plot_ex4_frame():
    """Ejemplo 4: Marco de foto. Visual geometry."""
    plot = MathPlotter(
        width=500, height=400,
        x_range=(-10, 10), y_range=(-10, 10),
        title="El Marco de la Foto",
        show_grid=False, show_axes=False
    )
    
    # Inner Photo: 10x15. Centered at origin.
    # Dimensions: width=10, height=15.
    # Coordinates: x from -5 to 5, y from -7.5 to 7.5
    
    # Outer Frame: adds x=2 on each side.
    # Dimensions: 14x19.
    # Coordinates: x from -7 to 7, y from -9.5 to 9.5
    
    # Draw Outer
    p_out_top_left = plot.coord.to_svg(Point(-7, 9.5))
    p_out_bottom_right = plot.coord.to_svg(Point(7, -9.5))
    w_out = p_out_bottom_right.x - p_out_top_left.x
    h_out = p_out_bottom_right.y - p_out_top_left.y
    plot.builder.rect(p_out_top_left.x, p_out_top_left.y, w_out, h_out, fill=COLORS['secondary'], fill_opacity=0.1, stroke=COLORS['secondary'])
    
    # Draw Inner
    p_in_top_left = plot.coord.to_svg(Point(-5, 7.5))
    p_in_bottom_right = plot.coord.to_svg(Point(5, -7.5))
    w_in = p_in_bottom_right.x - p_in_top_left.x
    h_in = p_in_bottom_right.y - p_in_top_left.y
    plot.builder.rect(p_in_top_left.x, p_in_top_left.y, w_in, h_in, fill=COLORS['primary'], fill_opacity=0.1, stroke=COLORS['primary'])
    
    # Labels
    plot.builder.text("Foto", Point(plot.width/2, plot.height/2 - 10), font_weight='bold')
    plot.builder.text("10 x 15", Point(plot.width/2, plot.height/2 + 10))
    plot.builder.text("Marco (x)", Point(plot.width/2, p_out_top_left.y + 15), font_size=12)

    # Dimension arrows (Manual approximation)
    # Arrow for width x on the right side
    # From x=5 to x=7 at y=0
    start = plot.coord.to_svg(Point(5, 0))
    end = plot.coord.to_svg(Point(7, 0))
    plot.builder.line(start, end, stroke=COLORS['text'], stroke_width=2)
    # plot.builder.text("x", Point((start.x+end.x)/2, start.y - 10), font_size=12)

    plot.save(f"{OUTPUT_DIR}/problemas_ex4_marco.svg")

def plot_ex5_freefall():
    """Ejemplo 5: Caída libre h(t) = 80 - 5t^2"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-0.5, 5), y_range=(-10, 110),
        title="Caída Libre",
        x_label="Tiempo (s)", y_label="Altura (m)",
        grid_step_x=1, grid_step_y=10
    )
    
    func = lambda t: 80 - 5*t**2
    plot.plot(func, label="h(t) = 80 - 5t²", color="secondary")
    
    plot.scatter(0, 80, label="Inicio (80m)", color="accent")
    plot.scatter(4, 0, label="Suelo (4s)", color="highlight")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/problemas_ex5_caida.svg")

if __name__ == "__main__":
    plot_ex1_rectangle()
    plot_ex2_rocket()
    plot_ex3_numbers()
    plot_ex4_frame()
    plot_ex5_freefall()


import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter
from scripts.geometry.core.base import Point, COLORS

OUTPUT_DIR = "public/images/matematicas/algebra/funciones-ecuaciones-cuadraticas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_intro_a_positive():
    """Concavidad Positiva (a > 0)"""
    plot = MathPlotter(
        width=400, height=300,
        x_range=(-2, 2), y_range=(-1, 5),
        title="a > 0 (Abre hacia arriba)"
    )
    # y = x^2
    plot.plot(lambda x: x**2, label="f(x) = x²", color="primary")
    plot.save(f"{OUTPUT_DIR}/intro_a_positive.svg")

def plot_intro_a_negative():
    """Concavidad Negativa (a < 0)"""
    plot = MathPlotter(
        width=400, height=300,
        x_range=(-2, 2), y_range=(-5, 1),
        title="a < 0 (Abre hacia abajo)"
    )
    # y = -x^2
    plot.plot(lambda x: -x**2, label="f(x) = -x²", color="secondary")
    plot.save(f"{OUTPUT_DIR}/intro_a_negative.svg")

def plot_vertex_concept():
    """Concepto de vertice visual"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-1, 6),
        title="El Vértice (h, k)"
    )
    
    # Parabola with vertex at (2, 1) -> y = (x-2)^2 + 1 = x^2 - 4x + 5
    plot.plot(lambda x: (x-2)**2 + 1, label="f(x)", color="primary")
    
    # Mark Vertex
    plot.scatter(2, 1, label="Vértice (2, 1)", color="accent")
    
    # Axis of symmetry: Vertical line at x=2
    # Get endpoints in math coordinates
    p_start_math = Point(2, -1)
    p_end_math = Point(2, 6)
    
    # Convert to SVG coordinates
    p_start_svg = plot.coord.to_svg(p_start_math)
    p_end_svg = plot.coord.to_svg(p_end_math)
    
    # Draw line manually
    plot.builder.line(p_start_svg, p_end_svg, stroke=COLORS['secondary'], stroke_width=2, dashed=True)
    
    # Add manual legend entry for the axis since we drew it manually
    plot.legend_items.append({
        'label': 'Eje de Simetría',
        'color': COLORS['secondary'],
        'dashed': True
    })
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/vertex_concept.svg")

def plot_width_comparison():
    """Comparison of widths based on |a|"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-4, 4), y_range=(0, 10),
        title="Efecto de |a| en la Apertura"
    )
    
    # a = 1 (Standard)
    plot.plot(lambda x: x**2, label="a = 1 (Normal)", color="primary", width=2)
    
    # a = 4 (Narrow)
    plot.plot(lambda x: 4*x**2, label="a = 4 (Estrecha)", color="accent", width=2)
    
    # a = 0.2 (Wide)
    plot.plot(lambda x: 0.2*x**2, label="a = 0.2 (Ancha)", color="secondary", width=2)
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/width_comparison.svg")

def plot_ex1_basic():
    """Ejemplo 1: x^2 - 4x + 3 -> Vertex (2, -1)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-2, 4),
        title="Ejemplo 1: x² - 4x + 3"
    )
    plot.plot(lambda x: x**2 - 4*x + 3, label="f(x) = x² - 4x + 3", color="primary")
    plot.scatter(2, -1, label="V (2, -1)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_ex1.svg")

def plot_ex2_downward():
    """Ejemplo 2: -2x^2 + 8x - 6 -> Vertex (2, 2)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-4, 3),
        title="Ejemplo 2: -2x² + 8x - 6"
    )
    plot.plot(lambda x: -2*x**2 + 8*x - 6, label="g(x)", color="secondary")
    plot.scatter(2, 2, label="V (2, 2)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_ex2.svg")

def plot_ex3_incomplete():
    """Ejemplo 3: 3x^2 + 6x -> Vertex (-1, -3)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-4, 2), y_range=(-4, 5),
        title="Ejemplo 3: 3x² + 6x"
    )
    plot.plot(lambda x: 3*x**2 + 6*x, label="h(x)", color="primary")
    plot.scatter(-1, -3, label="V (-1, -3)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_ex3.svg")

def plot_ex4_eval():
    """Ejemplo 4: x^2 - 5x + 6 evaluated at 3 -> (3, 0)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 5), y_range=(-1, 4),
        title="Ejemplo 4: Evaluar en x=3"
    )
    plot.plot(lambda x: x**2 - 5*x + 6, label="f(x) = x² - 5x + 6", color="primary")
    plot.scatter(3, 0, label="f(3) = 0", color="highlight")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_ex4.svg")

def plot_ex5_intercept():
    """Ejemplo 5: -x^2 + 4x + 10 -> Intercept (0, 10). Need appropriate range."""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(0, 15),
        title="Ejemplo 5: Intercepto Y"
    )
    plot.plot(lambda x: -x**2 + 4*x + 10, label="f(x) = -x² + 4x + 10", color="secondary")
    plot.scatter(0, 10, label="Corte Y (0, 10)", color="highlight")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_ex5.svg")

if __name__ == "__main__":
    plot_intro_a_positive()
    plot_intro_a_negative()
    plot_vertex_concept()
    plot_width_comparison()
    plot_ex1_basic()
    plot_ex2_downward()
    plot_ex3_incomplete()
    plot_ex4_eval()
    plot_ex5_intercept()


import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter
from scripts.geometry.core.base import Point, COLORS

OUTPUT_DIR = "public/images/matematicas/algebra/funciones-ecuaciones-cuadraticas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_treasure_map():
    """Conceptual Map: Generic parabola showing Vertex, Roots, Y-Intercept, Axis"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-3, 6),
        title="El Mapa del Tesoro"
    )
    
    # Function: y = (x-2)^2 - 2 = x^2 - 4x + 2
    # Roots: 2 +/- sqrt(2) approx 0.59 and 3.41
    # Vertex: (2, -2)
    # Y-Int: (0, 2)
    func = lambda x: (x-2)**2 - 2
    
    plot.plot(func, label="Parábola", color="primary")
    
    # 1. Vertex
    plot.scatter(2, -2, label="Vértice", color="accent")
    
    # 2. Roots
    x1 = 2 - 2**0.5
    x2 = 2 + 2**0.5
    plot.scatter(x1, 0, label="Raíz", color="secondary")
    plot.scatter(x2, 0, label="Raíz", color="secondary")
    
    # 3. Y-Intercept
    plot.scatter(0, 2, label="Corte Y", color="highlight")
    
    # 4. Axis of Symmetry (manual line)
    p_start = plot.coord.to_svg(Point(2, -3))
    p_end = plot.coord.to_svg(Point(2, 6))
    plot.builder.line(p_start, p_end, stroke=COLORS['text_light'], stroke_width=2, dashed=True)
    
    # Legend manually for axis
    plot.legend_items.append({
        'label': 'Eje de Simetría',
        'color': COLORS['text_light'],
        'dashed': True
    })
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/grafica_mapa_tesoro.svg")

def plot_ex1_complete():
    """Ej 1: x^2 - 4x + 3 -> V(2, -1), Roots (1, 3), Y-int (0, 3)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-2, 5),
        title="Ejemplo 1: x² - 4x + 3"
    )
    func = lambda x: x**2 - 4*x + 3
    plot.plot(func, label="f(x)", color="primary")
    
    plot.scatter(2, -1, label="Vértice (2, -1)", color="accent")
    plot.scatter(1, 0, label="(1, 0)", color="secondary")
    plot.scatter(3, 0, label="(3, 0)", color="secondary")
    plot.scatter(0, 3, label="(0, 3)", color="highlight")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/grafica_ex1.svg")

def plot_ex2_inverted():
    """Ej 2: -x^2 + 2x + 3 -> V(1, 4), Roots (-1, 3), Y-int (0, 3)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-3, 5), y_range=(-5, 6),
        title="Ejemplo 2: -x² + 2x + 3"
    )
    func = lambda x: -x**2 + 2*x + 3
    plot.plot(func, label="g(x)", color="secondary")
    
    plot.scatter(1, 4, label="Vértice (1, 4)", color="accent")
    plot.scatter(-1, 0, label="(-1, 0)", color="primary")
    plot.scatter(3, 0, label="(3, 0)", color="primary")
    plot.scatter(0, 3, label="(0, 3)", color="highlight")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/grafica_ex2.svg")

def plot_ex3_no_roots():
    """Ej 3: x^2 + 2x + 2 -> V(-1, 1), No roots, Y-int (0, 2)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-4, 2), y_range=(0, 6),
        title="Ejemplo 3: x² + 2x + 2"
    )
    func = lambda x: x**2 + 2*x + 2
    plot.plot(func, label="h(x)", color="primary")
    
    plot.scatter(-1, 1, label="Vértice (-1, 1)", color="accent")
    plot.scatter(0, 2, label="(0, 2)", color="highlight")
    # Symmetric point to y-int: (-2, 2)
    plot.scatter(-2, 2, label="Simétrico", color="grey")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/grafica_ex3.svg")

def plot_ex4_vertex_form():
    """Ej 4: 2(x-1)^2 - 3 -> V(1, -3), Narrower"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 4), y_range=(-4, 6),
        title="Ejemplo 4: 2(x-1)² - 3"
    )
    func = lambda x: 2*(x-1)**2 - 3
    plot.plot(func, label="k(x)", color="accent")
    
    plot.scatter(1, -3, label="Vértice (1, -3)", color="highlight")
    plot.scatter(0, -1, label="(0, -1)", color="secondary")
    plot.scatter(2, -1, label="(2, -1)", color="secondary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/grafica_ex4.svg")

if __name__ == "__main__":
    plot_treasure_map()
    plot_ex1_complete()
    plot_ex2_inverted()
    plot_ex3_no_roots()
    plot_ex4_vertex_form()

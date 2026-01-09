
import sys
import os
import math

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter
from scripts.geometry.core.base import COLORS

OUTPUT_DIR = "public/images/matematicas/algebra/funciones-ecuaciones-cuadraticas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_concept_2_cuts():
    """Concept: 2 solutions"""
    plot = MathPlotter(
        width=400, height=300,
        x_range=(-2, 4), y_range=(-2, 4),
        title="2 Soluciones Reales"
    )
    # Roots at 0 and 2 => x(x-2) = x^2 - 2x
    plot.plot(lambda x: x**2 - 2*x, label="Corta en 2 puntos", color="primary")
    plot.scatter(0, 0, color="accent")
    plot.scatter(2, 0, color="accent")
    plot.save(f"{OUTPUT_DIR}/resolucion_concept_2.svg")

def plot_concept_1_cut():
    """Concept: 1 solution"""
    plot = MathPlotter(
        width=400, height=300,
        x_range=(-1, 3), y_range=(-1, 4),
        title="1 Solución Real"
    )
    # Touch at 1 => (x-1)^2 = x^2 - 2x + 1
    plot.plot(lambda x: (x-1)**2, label="Toca en 1 punto", color="secondary")
    plot.scatter(1, 0, color="accent")
    plot.save(f"{OUTPUT_DIR}/resolucion_concept_1.svg")

def plot_concept_0_cuts():
    """Concept: 0 solutions"""
    plot = MathPlotter(
        width=400, height=300,
        x_range=(-2, 2), y_range=(-1, 5),
        title="0 Soluciones Reales"
    )
    # Above axis => x^2 + 1
    plot.plot(lambda x: x**2 + 1, label="No toca el eje X", color="highlight")
    plot.save(f"{OUTPUT_DIR}/resolucion_concept_0.svg")

def plot_ex1_trinomio():
    """Ej 1: x^2 - 5x + 6 = 0 => x=2, x=3"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 5), y_range=(-1, 4),
        title="Ejemplo 1: x² - 5x + 6 = 0"
    )
    plot.plot(lambda x: x**2 - 5*x + 6, label="f(x)", color="primary")
    plot.scatter(2, 0, label="x=2", color="accent")
    plot.scatter(3, 0, label="x=3", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex1.svg")

def plot_ex2_diff_squares():
    """Ej 2: x^2 - 9 = 0 => x=3, x=-3"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-5, 5), y_range=(-10, 10),
        title="Ejemplo 2: x² - 9 = 0"
    )
    plot.plot(lambda x: x**2 - 9, label="f(x)", color="secondary")
    plot.scatter(3, 0, label="x=3", color="accent")
    plot.scatter(-3, 0, label="x=-3", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex2.svg")

def plot_ex3_no_factor():
    """Ej 3: 2x^2 + 5x - 3 = 0 => x=0.5, x=-3"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-4, 2), y_range=(-8, 5),
        title="Ejemplo 3: 2x² + 5x - 3 = 0"
    )
    plot.plot(lambda x: 2*x**2 + 5*x - 3, label="f(x)", color="primary")
    plot.scatter(0.5, 0, label="x=0.5", color="accent")
    plot.scatter(-3, 0, label="x=-3", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex3.svg")

def plot_ex4_non_exact():
    """Ej 4: x^2 - 4x + 1 = 0 => x~0.27, x~3.73"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-4, 5),
        title="Ejemplo 4: Raíces no exactas"
    )
    plot.plot(lambda x: x**2 - 4*x + 1, label="f(x)", color="secondary")
    x1 = 2 - math.sqrt(3) # ~0.268
    x2 = 2 + math.sqrt(3) # ~3.732
    plot.scatter(x1, 0, label=f"x≈{x1:.2f}", color="accent")
    plot.scatter(x2, 0, label=f"x≈{x2:.2f}", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex4.svg")

def plot_ex5_unique():
    """Ej 5: x^2 - 6x + 9 = 0 => x=3"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 6), y_range=(-1, 5),
        title="Ejemplo 5: Solución Única"
    )
    plot.plot(lambda x: x**2 - 6*x + 9, label="(x-3)²", color="primary")
    plot.scatter(3, 0, label="x=3", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex5.svg")

def plot_ex6_no_solution():
    """Ej 6: x^2 + x + 1 = 0 => No real roots"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-3, 2), y_range=(-1, 5),
        title="Ejemplo 6: Sin Solución"
    )
    plot.plot(lambda x: x**2 + x + 1, label="x² + x + 1", color="highlight")
    # No scatter points
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex6.svg")

def plot_ex7_complete_square():
    """Ej 7: x^2 + 6x + 5 = 0 => x=-1, x=-5"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-7, 1), y_range=(-5, 5),
        title="Ejemplo 7: x² + 6x + 5 = 0"
    )
    plot.plot(lambda x: x**2 + 6*x + 5, label="f(x)", color="secondary")
    plot.scatter(-1, 0, label="x=-1", color="accent")
    plot.scatter(-5, 0, label="x=-5", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/resolucion_ex7.svg")

if __name__ == "__main__":
    plot_concept_2_cuts()
    plot_concept_1_cut()
    plot_concept_0_cuts()
    plot_ex1_trinomio()
    plot_ex2_diff_squares()
    plot_ex3_no_factor()
    plot_ex4_non_exact()
    plot_ex5_unique()
    plot_ex6_no_solution()
    plot_ex7_complete_square()

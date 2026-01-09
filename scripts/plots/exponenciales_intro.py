
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter
from scripts.geometry.core.base import COLORS

OUTPUT_DIR = "public/images/matematicas/algebra/funciones-exponenciales-logaritmicas"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_intro_growth():
    """Formula General: Crecimiento (b > 1)"""
    plot = MathPlotter(
        width=500, height=350,
        x_range=(-2, 4), y_range=(-1, 10),
        title="Crecimiento Exponencial (b > 1)",
        grid_step_y=2
    )
    # y = 2^x
    plot.plot(lambda x: 2**x, label="f(x) = a · 2ˣ", color="primary")
    plot.scatter(0, 1, label="Inicio (a)", color="accent")
    
    # Asymptote hint arrow or text? 
    # Just standard plot is usually enough, but let's highlight y-intercept
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_growth.svg")

def plot_intro_decay():
    """Formula General: Decaimiento (0 < b < 1)"""
    plot = MathPlotter(
        width=500, height=350,
        x_range=(-2, 4), y_range=(-1, 10),
        title="Decaimiento Exponencial (0 < b < 1)",
        grid_step_y=2
    )
    # y = (0.5)^x
    plot.plot(lambda x: 0.5**x, label="f(x) = a · (0.5)ˣ", color="secondary")
    plot.scatter(0, 1, label="Inicio (a)", color="accent")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/intro_decay.svg")

def plot_example1_bacteria():
    """Ejemplo 1: Bacterias 100 * 3^t"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1.5, 4.5), y_range=(-500, 9000),  # More space on left
        title="Cultivo de Bacterias",
        x_label="Horas (t)", y_label="Bacterias",
        grid_step_x=1, grid_step_y=2000
    )
    
    func = lambda t: 100 * 3**t
    plot.plot(func, label="B(t) = 100 · 3ᵗ", color="primary")
    plot.scatter(0, 100, label="Inicio (100)", color="accent")
    plot.scatter(4, 8100, label="4h (8100)", color="highlight")
    
    # Move legend to top-left to avoid blocking the graph at top-right
    plot.add_legend(x=80, y=80)
    plot.save(f"{OUTPUT_DIR}/example1_bacteria.svg")

def plot_example2_car():
    """Ejemplo 2: Auto 20M * 0.9^t"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 11), y_range=(-2, 24), # Start X at -2 to free Y-axis
        title="Depreciación del Auto (Millones)",
        x_label="Años", y_label="Valor (Millones)",
        grid_step_x=1, grid_step_y=5
    )
    
    func = lambda x: 20 * 0.9**x
    plot.plot(func, label="V(t) = 20 · 0.9ᵗ", color="secondary")
    
    # Manually placing text for "Nuevo" to avoid axis overlap if needed, 
    # but increasing x_range to -2 should help standard label placement.
    plot.scatter(0, 20, label="Nuevo (20M)", color="accent")
    
    plot.scatter(5, 11.81, label="5 años (~11.8M)", color="primary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/example2_car.svg")

def plot_example3_check():
    """Ejemplo 3: 500 * 1.05^x (Crecimiento Lento)"""
    plot = MathPlotter(
        width=500, height=350,
        x_range=(0, 20), y_range=(400, 1500),
        title="¿Crece o Decrece?",
        x_label="Tiempo", y_label="Valor",
        grid_step_x=5, grid_step_y=200
    )
    
    func = lambda x: 500 * 1.05**x
    plot.plot(func, label="f(x) = 500 · 1.05ˣ", color="primary")
    plot.scatter(0, 500, label="500", color="highlight")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/example3_growth_check.svg")

def plot_example5_basic():
    """Ejemplo 5: y = 2^x"""
    plot = MathPlotter(
        width=500, height=500,
        x_range=(-3, 4), y_range=(-1, 10),
        title="Gráfica Básica: y = 2ˣ",
        grid_step_x=1, grid_step_y=1
    )
    
    func = lambda x: 2**x
    plot.plot(func, label="y = 2ˣ", color="primary")
    
    # Points mentioned in lesson
    # (0,1), (1,2), (2,4), (-1, 0.5)
    plot.scatter(0, 1, label="(0, 1)", color="accent")
    plot.scatter(1, 2, label="(1, 2)", color="secondary")
    plot.scatter(2, 4, label="(2, 4)", color="secondary")
    plot.scatter(-1, 0.5, label="(-1, 0.5)", color="highlight")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/example5_basic_graph.svg")

if __name__ == "__main__":
    plot_intro_growth()
    plot_intro_decay()
    plot_example1_bacteria()
    plot_example2_car()
    plot_example3_check()
    # plot_example4_paper() # Removed per user request
    plot_example5_basic()

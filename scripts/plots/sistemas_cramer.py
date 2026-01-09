
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/matematicas/algebra/sistemas-ecuaciones-lineales"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_ex1_directo():
    """Ejemplo 1: 2x + 3y = 7, x - y = 1 -> Sol (2, 1)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-2, 6),
        title="Ejemplo 1: Solución (2, 1)"
    )
    
    # 2x + 3y = 7 => 3y = 7 - 2x => y = (7 - 2x)/3
    plot.plot(lambda x: (7 - 2*x)/3, label="2x + 3y = 7")
    
    # x - y = 1 => y = x - 1
    plot.plot(lambda x: x - 1, label="x - y = 1", color="secondary")
    
    plot.scatter(2, 1, label="(2, 1)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/cramer_ex1.svg")

def plot_ex2_grandes():
    """Ejemplo 2: 3x + 2y = 12, 5x - 3y = 1 -> Sol (2, 3)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-2, 6),
        title="Ejemplo 2: Solución (2, 3)"
    )
    
    # 3x + 2y = 12 => 2y = 12 - 3x => y = 6 - 1.5x
    plot.plot(lambda x: 6 - 1.5*x, label="3x + 2y = 12")
    
    # 5x - 3y = 1 => 3y = 5x - 1 => y = (5x - 1)/3
    plot.plot(lambda x: (5*x - 1)/3, label="5x - 3y = 1", color="secondary")
    
    plot.scatter(2, 3, label="(2, 3)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/cramer_ex2.svg")

def plot_ex3_imposible():
    """Ejemplo 3: 2x + 4y = 6, x + 2y = 5 -> Paralelas"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-2, 6),
        title="Ejemplo 3: Incompatible (Det = 0)"
    )
    
    # 2x + 4y = 6 => 4y = 6 - 2x => y = 1.5 - 0.5x
    plot.plot(lambda x: 1.5 - 0.5*x, label="2x + 4y = 6")
    
    # x + 2y = 5 => 2y = 5 - x => y = 2.5 - 0.5x
    plot.plot(lambda x: 2.5 - 0.5*x, label="x + 2y = 5", color="secondary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/cramer_ex3.svg")

def plot_ex4_indeterminado():
    """Ejemplo 4: x + y = 2, 2x + 2y = 4 -> Coincidentes"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-2, 4),
        title="Ejemplo 4: Indeterminado (Det = 0)"
    )
    
    # x + y = 2 => y = 2 - x
    plot.plot(lambda x: 2 - x, label="x + y = 2", width=4)
    
    # 2x + 2y = 4 => 2y = 4 - 2x => y = 2 - x
    plot.plot(lambda x: 2 - x, label="2x + 2y = 4", color="secondary", width=2, dashed=True)
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/cramer_ex4.svg")

if __name__ == "__main__":
    plot_ex1_directo()
    plot_ex2_grandes()
    plot_ex3_imposible()
    plot_ex4_indeterminado()

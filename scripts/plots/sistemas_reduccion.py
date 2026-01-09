
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/matematicas/algebra/sistemas-ecuaciones-lineales"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_ex1_perfecto():
    """Ejemplo 1: x + y = 7, x - y = 3 -> Sol (5, 2)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 8), y_range=(0, 8),
        title="Ejemplo 1: Solución (5, 2)"
    )
    
    # x + y = 7 => y = 7 - x
    plot.plot(lambda x: 7 - x, label="x + y = 7")
    
    # x - y = 3 => y = x - 3
    plot.plot(lambda x: x - 3, label="x - y = 3", color="secondary")
    
    plot.scatter(5, 2, label="(5, 2)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/reduccion_ex1.svg")

def plot_ex2_multiplicar_uno():
    """Ejemplo 2: x + 3y = 7, 2x - y = 7 -> Sol (4, 1)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 8), y_range=(-2, 4),
        title="Ejemplo 2: Solución (4, 1)"
    )
    
    # x + 3y = 7 => 3y = 7 - x => y = (7 - x)/3
    plot.plot(lambda x: (7 - x)/3, label="x + 3y = 7")
    
    # 2x - y = 7 => y = 2x - 7
    plot.plot(lambda x: 2*x - 7, label="2x - y = 7", color="secondary")
    
    plot.scatter(4, 1, label="(4, 1)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/reduccion_ex2.svg")

def plot_ex3_mcm():
    """Ejemplo 3: 3x + 4y = 25, 2x - 3y = 6 -> Sol (99/17 ~ 5.82, 32/17 ~ 1.88)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 10), y_range=(-2, 8),
        title="Ejemplo 3: Solución (5.82, 1.88)"
    )
    
    # 3x + 4y = 25 => y = (25 - 3x)/4
    plot.plot(lambda x: (25 - 3*x)/4, label="3x + 4y = 25")
    
    # 2x - 3y = 6 => 3y = 2x - 6 => y = (2x - 6)/3
    plot.plot(lambda x: (2*x - 6)/3, label="2x - 3y = 6", color="secondary")
    
    # 99/17 approx 5.823, 32/17 approx 1.882
    sln_x = 99/17
    sln_y = 32/17
    
    plot.scatter(sln_x, sln_y, label=f"({sln_x:.2f}, {sln_y:.2f})", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/reduccion_ex3.svg")

def plot_ex4_signos_iguales():
    """Ejemplo 4: 5x + y = 10, 2x + y = 4 -> Sol (2, 0)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 4), y_range=(-4, 12),
        title="Ejemplo 4: Solución (2, 0)"
    )
    
    # 5x + y = 10 => y = 10 - 5x
    plot.plot(lambda x: 10 - 5*x, label="5x + y = 10")
    
    # 2x + y = 4 => y = 4 - 2x
    plot.plot(lambda x: 4 - 2*x, label="2x + y = 4", color="secondary")
    
    plot.scatter(2, 0, label="(2, 0)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/reduccion_ex4.svg")

def plot_ex5_incompatible():
    """Ejemplo 5: 2x - y = 4, -4x + 2y = 8 -> Paralelas"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-4, 8),
        title="Ejemplo 5: Incompatible"
    )
    
    # 2x - y = 4 => y = 2x - 4
    plot.plot(lambda x: 2*x - 4, label="2x - y = 4")
    
    # -4x + 2y = 8 => 2y = 4x + 8 => y = 2x + 4
    plot.plot(lambda x: 2*x + 4, label="-4x + 2y = 8", color="secondary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/reduccion_ex5.svg")

if __name__ == "__main__":
    plot_ex1_perfecto()
    plot_ex2_multiplicar_uno()
    plot_ex3_mcm()
    plot_ex4_signos_iguales()
    plot_ex5_incompatible()

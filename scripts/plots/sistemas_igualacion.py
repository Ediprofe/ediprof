
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/matematicas/algebra/sistemas-ecuaciones-lineales"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_ex1_sencillo():
    """Ejemplo 1: x + y = 10, x - y = 2 -> Sol (6, 4)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 10), y_range=(0, 10),
        title="Ejemplo 1: Solución (6, 4)"
    )
    
    # x + y = 10 => y = 10 - x
    plot.plot(lambda x: 10 - x, label="x + y = 10")
    
    # x - y = 2 => y = x - 2
    plot.plot(lambda x: x - 2, label="x - y = 2", color="secondary")
    
    plot.scatter(6, 4, label="(6, 4)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/igualacion_ex1.svg")

def plot_ex2_despeje_y():
    """Ejemplo 2: 2x + y = 11, 3x - y = 4 -> Sol (3, 5)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 6), y_range=(0, 10),
        title="Ejemplo 2: Solución (3, 5)"
    )
    
    # 2x + y = 11 => y = 11 - 2x
    plot.plot(lambda x: 11 - 2*x, label="2x + y = 11")
    
    # 3x - y = 4 => y = 3x - 4
    plot.plot(lambda x: 3*x - 4, label="3x - y = 4", color="secondary")
    
    plot.scatter(3, 5, label="(3, 5)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/igualacion_ex2.svg")

def plot_ex3_fracciones():
    """Ejemplo 3: 2x + 3y = 13, 4x - y = 5 -> Sol (2, 3)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 6), y_range=(-1, 6),
        title="Ejemplo 3: Solución (2, 3)"
    )
    
    # 2x + 3y = 13 => y = (13 - 2x)/3
    plot.plot(lambda x: (13 - 2*x)/3, label="2x + 3y = 13")
    
    # 4x - y = 5 => y = 4x - 5
    plot.plot(lambda x: 4*x - 5, label="4x - y = 5", color="secondary")
    
    plot.scatter(2, 3, label="(2, 3)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/igualacion_ex3.svg")

def plot_ex4_fracciones_ambos():
    """Ejemplo 4: 5x - 3y = 7, 2x + 3y = 14 -> Sol (3, 8/3 ~ 2.66)"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(0, 6), y_range=(0, 6),
        title="Ejemplo 4: Solución (3, 2.67)"
    )
    
    # 5x - 3y = 7 => y = (5x - 7)/3
    plot.plot(lambda x: (5*x - 7)/3, label="5x - 3y = 7")
    
    # 2x + 3y = 14 => y = (14 - 2x)/3
    plot.plot(lambda x: (14 - 2*x)/3, label="2x + 3y = 14", color="secondary")
    
    plot.scatter(3, 8/3, label="(3, 8/3)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/igualacion_ex4.svg")

def plot_ex5_imposible():
    """Ejemplo 5: x + y = 3, x + y = 7 -> Paralelas"""
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-2, 8),
        title="Ejemplo 5: Incompatible (Paralelas)"
    )
    
    # x + y = 3 => y = 3 - x
    plot.plot(lambda x: 3 - x, label="x + y = 3")
    
    # x + y = 7 => y = 7 - x
    plot.plot(lambda x: 7 - x, label="x + y = 7", color="secondary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/igualacion_ex5.svg")

if __name__ == "__main__":
    plot_ex1_sencillo()
    plot_ex2_despeje_y()
    plot_ex3_fracciones()
    plot_ex4_fracciones_ambos()
    plot_ex5_imposible()

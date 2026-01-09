
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/matematicas/algebra/sistemas-ecuaciones-lineales"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_ex1_ideal():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 8), y_range=(-2, 8),
        title="Ejemplo 1: Solución (4, 3)"
    )
    
    # x + y = 7 => y = 7 - x
    plot.plot(lambda x: 7 - x, label="x + y = 7")
    
    # 2x - y = 5 => y = 2x - 5
    plot.plot(lambda x: 2*x - 5, label="2x - y = 5", color="secondary")
    
    plot.scatter(4, 3, label="(4, 3)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sustitucion_ex1.svg")

def plot_ex2_despeje_x():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 6), y_range=(-1, 6),
        title="Ejemplo 2: Solución (2.8, 1.8)"
    )
    
    # 3x + 2y = 12 => y = (12 - 3x)/2 = 6 - 1.5x
    plot.plot(lambda x: 6 - 1.5*x, label="3x + 2y = 12")
    
    # x - y = 1 => y = x - 1
    plot.plot(lambda x: x - 1, label="x - y = 1", color="secondary")
    
    plot.scatter(2.8, 1.8, label="(2.8, 1.8)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sustitucion_ex2.svg")

def plot_ex3_variable_despejada():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 5), y_range=(-2, 4),
        title="Ejemplo 3: Solución (2, 1)"
    )
    
    # 5x - 2y = 8 => 2y = 5x - 8 => y = 2.5x - 4
    plot.plot(lambda x: 2.5*x - 4, label="5x - 2y = 8")
    
    # x = 3y - 1 => 3y = x + 1 => y = x/3 + 1/3
    plot.plot(lambda x: x/3 + 1/3, label="x = 3y - 1", color="secondary")
    
    plot.scatter(2, 1, label="(2, 1)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sustitucion_ex3.svg")

def plot_ex4_fracciones():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(2, 10), y_range=(-2, 6),
        title="Ejemplo 4: Solución (7, 1.5)"
    )
    
    # x/2 + y = 5 => y = 5 - 0.5x
    plot.plot(lambda x: 5 - 0.5*x, label="x/2 + y = 5")
    
    # x - 2y = 4 => 2y = x - 4 => y = 0.5x - 2
    plot.plot(lambda x: 0.5*x - 2, label="x - 2y = 4", color="secondary")
    
    plot.scatter(7, 1.5, label="(7, 1.5)", color="accent")
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sustitucion_ex4.svg")

def plot_ex5_incompatible():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-1, 6), y_range=(-2, 6),
        title="Ejemplo 5: Incompatible (Paralelas)"
    )
    
    # x + y = 3 => y = 3 - x
    plot.plot(lambda x: 3 - x, label="x + y = 3")
    
    # 2x + 2y = 8 => 2y = 8 - 2x => y = 4 - x
    plot.plot(lambda x: 4 - x, label="2x + 2y = 8", color="secondary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sustitucion_ex5.svg")

def plot_ex6_indeterminado():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 8), y_range=(-4, 4),
        title="Ejemplo 6: Indeterminado (Coincidentes)"
    )
    
    # x - 2y = 4 => 2y = x - 4 => y = 0.5x - 2
    plot.plot(lambda x: 0.5*x - 2, label="x - 2y = 4", width=4)
    
    # 3x - 6y = 12 => 6y = 3x - 12 => y = 0.5x - 2
    plot.plot(lambda x: 0.5*x - 2, label="3x - 6y = 12", color="secondary", width=2, dashed=True)
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sustitucion_ex6.svg")

if __name__ == "__main__":
    plot_ex1_ideal()
    plot_ex2_despeje_x()
    plot_ex3_variable_despejada()
    plot_ex4_fracciones()
    plot_ex5_incompatible()
    plot_ex6_indeterminado()

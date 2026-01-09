
import sys
import os

# Add project root to path to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/matematicas/algebra/sistemas-ecuaciones-lineales"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_compatible_determinado():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-2, 6),
        title="1. Sistema Compatible Determinado"
    )
    
    # L1: x + y = 4  => y = 4 - x
    plot.plot(lambda x: 4 - x, label="x + y = 4", color="primary")
    
    # L2: -x + y = 0 => y = x
    plot.plot(lambda x: x, label="-x + y = 0", color="secondary")
    
    # Intersection (2, 2)
    plot.scatter(2, 2, label="Solución única (2, 2)", color="accent")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sistema_determinado.svg")

def plot_incompatible():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-4, 6), y_range=(-4, 6),
        title="2. Sistema Incompatible"
    )
    
    # L1: y = 0.5x + 2
    plot.plot(lambda x: 0.5*x + 2, label="x - 2y = -4", color="primary")
    
    # L2: y = 0.5x - 1
    plot.plot(lambda x: 0.5*x - 1, label="x - 2y = 2", color="secondary")
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sistema_incompatible.svg")

def plot_indeterminado():
    plot = MathPlotter(
        width=600, height=400,
        x_range=(-2, 6), y_range=(-2, 6),
        title="3. Compatible Indeterminado"
    )
    
    # L1: x + y = 3 => y = 3 - x
    plot.plot(lambda x: 3 - x, label="x + y = 3", color="primary", width=5)
    
    # L2: 2x + 2y = 6 (Same line)
    # Draw dashed on top to show they are the same
    plot.plot(lambda x: 3 - x, label="2x + 2y = 6", color="secondary", width=2, dashed=True)
    
    plot.add_legend()
    plot.save(f"{OUTPUT_DIR}/sistema_indeterminado.svg")

if __name__ == "__main__":
    plot_compatible_determinado()
    plot_incompatible()
    plot_indeterminado()

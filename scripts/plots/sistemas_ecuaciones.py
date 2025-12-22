#!/usr/bin/env python3
"""
Generación de gráficos para sistemas de ecuaciones usando MathPlotter.
Versión limpia y mantenible.
"""

import sys
from pathlib import Path

# Setup path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

from geometry.core.plotter import MathPlotter

OUTPUT_DIR = PROJECT_ROOT / 'public' / 'images' / 'matematicas' / 'algebra' / 'sistemas-ecuaciones'

def generar_graficos():
    print("🎨 Generando gráficos con MathPlotter...")

    # Ejemplo 1: Sistema Básico
    (MathPlotter(title="Ejemplo 1: x+y=4, x-y=2", x_range=(-1, 6), y_range=(-3, 6))
        .plot(lambda x: -x + 4, label="y = -x + 4", color="primary")
        .plot(lambda x: x - 2,  label="y = x - 2",  color="secondary")
        .scatter(3, 1, label="(3, 1)", color="accent")
        .add_legend()
        .save(OUTPUT_DIR / "ejemplo1-sistema.svg"))

    # Ejemplo 2: Intersección en (2,2)
    (MathPlotter(title="Ejemplo 2: 2x+y=6, x-y=0", x_range=(-1, 5), y_range=(-1, 7))
        .plot(lambda x: -2*x + 6, label="y = -2x + 6", color="primary")
        .plot(lambda x: x,        label="y = x",        color="secondary")
        .scatter(2, 2, label="(2, 2)", color="accent")
        .add_legend()
        .save(OUTPUT_DIR / "ejemplo2-sistema.svg"))

    # Ejemplo 3: Intersección en (2,3)
    (MathPlotter(title="Ejemplo 3: y=2x-1, y=-x+5", x_range=(-1, 6), y_range=(-2, 7))
        .plot(lambda x: 2*x - 1, label="y = 2x - 1", color="primary")
        .plot(lambda x: -x + 5,  label="y = -x + 5", color="secondary")
        .scatter(2, 3, label="(2, 3)", color="accent")
        .add_legend()
        .save(OUTPUT_DIR / "ejemplo3-sistema.svg"))

    # Ejemplo 4: Paralelas (Incompatible)
    (MathPlotter(title="Ejemplo 4: Incompatible (paralelas)", x_range=(-2, 5), y_range=(-5, 10))
        .plot(lambda x: 2*x + 1, label="y = 2x + 1", color="accent")
        .plot(lambda x: 2*x - 3, label="y = 2x - 3", color="highlight", dashed=True)
        .add_legend()
        .save(OUTPUT_DIR / "ejemplo4-incompatible.svg"))

    # Ejemplo 5: Coincidentes (Indeterminado)
    (MathPlotter(title="Ejemplo 5: Indeterminado (coincidentes)", x_range=(-1, 5), y_range=(-1, 5))
        .plot(lambda x: -x + 3, label="x + y = 3",     color="secondary", width=5)
        .plot(lambda x: -x + 3, label="2x + 2y = 6",   color="primary",   width=2, dashed=True)
        .add_legend()
        .save(OUTPUT_DIR / "ejemplo5-indeterminado.svg"))

if __name__ == "__main__":
    generar_graficos()

#!/usr/bin/env python3
"""
DISTRIBUTION EXAMPLES RENDERER
Genera 6 ilustraciones individuales para los ejemplos de distribución electrónica:
H, He, Li, C, Ne, Na.
"""

import math
import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def get_electron_coords(cx, cy, r, count):
    coords = []
    angle_step = (2 * math.pi) / count if count > 0 else 0
    start_angle = -math.pi / 2
    for i in range(count):
        angle = start_angle + i * angle_step
        coords.append(Point(cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return coords

def render_example_atom(name, symbol, z, distribution):
    width, height = 450, 400
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Info del Elemento (Arriba)
    builder.text(f"{name} ({symbol})", Point(width / 2, 40), 
                font_size=22, font_weight="bold", anchor="middle")
    builder.text(f"Z = {z}", Point(width / 2, 65), 
                font_size=16, font_weight="bold", fill=COLORS['text_light'], anchor="middle")
    
    # Centro
    cx, cy = width / 2, height / 2 + 25
    center = Point(cx, cy)
    
    orbit_color = "#334155" # Slate 700
    base_r = 50
    step = 40
    
    # 1. Dibujar Órbitas y Electrones según la distribución
    for i, count in enumerate(distribution):
        r = base_r + i * step
        # Órbita sólida
        builder.circle(center, r, fill="none", stroke=orbit_color, stroke_width=2)
        
        # Etiqueta n
        builder.text(f"n={i+1}", Point(cx, cy - r - 6), 
                    font_size=10, font_weight="bold", fill=orbit_color, anchor="middle")
        
        # Electrones
        e_positions = get_electron_coords(cx, cy, r, count)
        for pos in e_positions:
            builder.circle(pos, 6, fill=COLORS['primary'], stroke="white", stroke_width=1)
            builder.text("-", Point(pos.x, pos.y + 1.5), font_size=10, 
                        font_weight="bold", fill="white", anchor="middle")

    # 2. Núcleo
    builder.circle(center, 22, fill=COLORS['accent'], stroke=COLORS['white'], stroke_width=2)
    builder.text(f"{z}+", Point(cx, cy + 6), font_size=18, font_weight="bold", fill="white", anchor="middle")

    # 3. Texto de Distribución (Abajo)
    dist_str = ", ".join(map(str, distribution))
    builder.text(f"Distribución: {dist_str}", Point(width / 2, height - 25), 
                font_size=14, font_weight="bold", fill=COLORS['primary'], anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/configuracion-electronica/ejemplos")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    examples = [
        {"name": "Hidrógeno", "symbol": "H",  "z": 1,  "dist": [1]},
        {"name": "Helio",     "symbol": "He", "z": 2,  "dist": [2]},
        {"name": "Litio",     "symbol": "Li", "z": 3,  "dist": [2, 1]},
        {"name": "Carbono",   "symbol": "C",  "z": 6,  "dist": [2, 4]},
        {"name": "Neón",      "symbol": "Ne", "z": 10, "dist": [2, 8]},
        {"name": "Sodio",     "symbol": "Na", "z": 11, "dist": [2, 8, 1]},
    ]
    
    for ex in examples:
        filename = f"{ex['symbol'].lower()}-distribucion.svg"
        (output_dir / filename).write_text(
            render_example_atom(ex['name'], ex['symbol'], ex['z'], ex['dist']), 
            encoding="utf-8"
        )
        print(f"✅ {filename} generado")

if __name__ == "__main__":
    main()

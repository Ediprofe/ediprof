#!/usr/bin/env python3
"""
ENERGY VS DISTANCE RENDERER - FINAL VERSION
Corrección de altura para evitar solapamiento de texto inferior.
"""

import math
import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def get_electron_coords(cx, cy, r, count):
    """Genera coordenadas para distribuir 'count' electrones uniformemente."""
    coords = []
    angle_step = (2 * math.pi) / count
    start_angle = -math.pi / 2
    for i in range(count):
        angle = start_angle + i * angle_step
        coords.append(Point(cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return coords

def render_energy_vs_distance():
    # Aumentamos la altura para dar espacio al texto inferior
    width, height = 800, 560
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Energía y Atracción en el Átomo", Point(width / 2, 45), 
                font_size=26, font_weight="bold", anchor="middle")
    
    # Centro del átomo (Centrado verticalmente con ligero ajuste)
    cx, cy = width / 2, 280
    center = Point(cx, cy)
    
    # Configuración representativa
    shells_config = [
        {"r": 60,  "n": "1", "e": 2},
        {"r": 105, "n": "2", "e": 8},
        {"r": 150, "n": "3", "e": 8},
        {"r": 195, "n": "4", "e": 1},
    ]
    
    orbit_color = "#334155" 
    
    # 1. Dibujar Órbitas y Electrones
    for shell in shells_config:
        builder.circle(center, shell['r'], fill="none", stroke=orbit_color, stroke_width=2.5)
        
        # Etiqueta de nivel n=X
        builder.text(f"n = {shell['n']}", Point(cx, cy - shell['r'] - 8), 
                    font_size=12, font_weight="bold", fill=orbit_color, anchor="middle")
        
        e_positions = get_electron_coords(cx, cy, shell['r'], shell['e'])
        for pos in e_positions:
            builder.circle(pos, 7, fill=COLORS['primary'], stroke=COLORS['white'], stroke_width=1.5)
            builder.text("-", Point(pos.x, pos.y + 2), font_size=12, font_weight="bold", 
                        fill=COLORS['white'], anchor="middle")

    # 2. Núcleo
    builder.circle(center, 30, fill=COLORS['accent'], stroke=COLORS['white'], stroke_width=3)
    builder.text("+", Point(cx, cy + 8), font_size=32, font_weight="bold", 
                fill=COLORS['white'], anchor="middle")
    builder.text("NÚCLEO", Point(cx, cy + 50), font_size=12, font_weight="bold", 
                fill=COLORS['text'], anchor="middle")

    # 3. Flechas de Tendencia Laterales
    y_min, y_max = cy - 195, cy + 195
    
    # ATRACCIÓN (Izquierda)
    attr_x = 80
    builder.arrow(Point(attr_x, y_max), Point(attr_x, cy + 55), stroke=COLORS['teal'], stroke_width=6)
    builder.arrow(Point(attr_x, y_min), Point(attr_x, cy - 55), stroke=COLORS['teal'], stroke_width=6)
    builder.text("ATRACCIÓN", Point(attr_x, cy - 15), font_size=16, font_weight="900", fill=COLORS['teal'], anchor="middle")
    builder.text("AL NÚCLEO", Point(attr_x, cy + 15), font_size=16, font_weight="900", fill=COLORS['teal'], anchor="middle")

    # ENERGÍA (Derecha)
    ener_x = width - 80
    builder.arrow(Point(ener_x, cy - 55), Point(ener_x, y_min), stroke=COLORS['highlight'], stroke_width=6)
    builder.arrow(Point(ener_x, cy + 55), Point(ener_x, y_max), stroke=COLORS['highlight'], stroke_width=6)
    builder.text("MAYOR", Point(ener_x, cy - 15), font_size=16, font_weight="900", fill=COLORS['highlight'], anchor="middle")
    builder.text("ENERGÍA", Point(ener_x, cy + 15), font_size=16, font_weight="900", fill=COLORS['highlight'], anchor="middle")

    # 4. Etiquetas de pie de página (Conceptuales) - Movidas hacia abajo para evitar solapamiento
    builder.text("Electrones cercanos: Máxima atracción, mínima energía", 
                Point(width / 2, height - 45), font_size=12, fill=COLORS['text_light'], anchor="middle")
    builder.text("Electrones lejanos: Mínima atracción, máxima energía", 
                Point(width / 2, height - 25), font_size=12, fill=COLORS['text_light'], anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/configuracion-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = "energia-vs-distancia.svg"
    (output_dir / filename).write_text(render_energy_vs_distance(), encoding="utf-8")
    print(f"✅ {filename} generado (Altura corregida: 560px)")

if __name__ == "__main__":
    main()

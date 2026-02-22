#!/usr/bin/env python3
"""
ORBITAL CONCEPT RENDERER
Ilustra el concepto de orbital como una zona de probabilidad para máximo 2 electrones.
"""

import math
import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_orbital_concept():
    width, height = 600, 380
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Concepto de Orbital", Point(width / 2, 40), 
                font_size=24, font_weight="bold", anchor="middle")
    
    # Centro
    cx, cy = 200, 220
    center = Point(cx, cy)
    
    # 1. Zona de Probabilidad (Orbital s)
    # Dibujamos varios círculos con opacidades bajas para dar efecto de "nube"
    nube_color = COLORS['primary']
    for r in range(40, 90, 10):
        opacity = (100 - r) / 100 * 0.2
        builder.circle(center, r, fill=nube_color, fill_opacity=opacity, stroke="none")
    
    # 2. Núcleo (Pequeño)
    builder.circle(center, 12, fill=COLORS['accent'], stroke=COLORS['white'], stroke_width=2)
    builder.text("+", Point(cx, cy + 5), font_size=18, font_weight="bold", fill="white", anchor="middle")
    builder.text("Núcleo", Point(cx, cy + 30), font_size=11, font_weight="bold", fill=COLORS['text'], anchor="middle")

    # 3. Electrones (Límite máximo de 2)
    e1_pos = Point(cx + 40, cy - 30)
    e2_pos = Point(cx - 50, cy + 20)
    
    for pos in [e1_pos, e2_pos]:
        builder.circle(pos, 8, fill=COLORS['primary'], stroke="white", stroke_width=1.5)
        builder.text("-", Point(pos.x, pos.y + 2), font_size=12, font_weight="bold", fill="white", anchor="middle")

    # 4. Explicación Visual (Flechas y Etiquetas)
    # Flecha hacia la nube
    builder.arrow(Point(cx + 120, cy - 100), Point(cx + 60, cy - 50), 
                stroke=COLORS['text_light'], stroke_width=2)
    builder.text("Zona de Probabilidad", Point(cx + 125, cy - 110), 
                font_size=14, font_weight="bold", fill=COLORS['text'], anchor="start")
    
    # Flecha hacia los electrones
    builder.arrow(Point(400, 280), Point(cx + 48, cy - 25), 
                stroke=COLORS['text_light'], stroke_width=2)
    builder.rect(400, 280, 160, 50, fill="white", stroke=COLORS['primary'], rx=8)
    builder.text("Capacidad Máxima:", Point(480, 305), font_size=14, font_weight="bold", 
                fill=COLORS['primary'], anchor="middle")
    builder.text("2 Electrones", Point(480, 322), font_size=14, font_weight="bold", 
                fill=COLORS['primary'], anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/config-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = "concepto-orbital.svg"
    (output_dir / filename).write_text(render_orbital_concept(), encoding="utf-8")
    print(f"✅ {filename} generado")

if __name__ == "__main__":
    main()

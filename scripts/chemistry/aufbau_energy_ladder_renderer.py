#!/usr/bin/env python3
"""
AUFBAU ENERGY LADDER RENDERER
Ilustra el Principio de Aufbau como una escalera de energía.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_aufbau_ladder():
    width, height = 600, 480
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Principio de Aufbau", Point(width / 2, 40), 
                font_size=24, font_weight="bold", anchor="middle")
    
    # Eje de Energía (Vertical)
    ax_x = 70
    builder.arrow(Point(ax_x, 420), Point(ax_x, 80), stroke=COLORS['text'], stroke_width=3)
    builder.text("ENERGÍA", Point(ax_x - 15, 250), font_size=16, font_weight="bold", 
                fill=COLORS['text'], anchor="middle") # Se asume lectura vertical por posición

    # Peldaños (Subniveles)
    steps = [
        {"y": 380, "label": "1s", "status": "Lleno", "e": 2},
        {"y": 320, "label": "2s", "status": "Lleno", "e": 2},
        {"y": 260, "label": "2p", "status": "Llenándose", "e": 4},
        {"y": 200, "label": "3s", "status": "Vacío", "e": 0},
    ]
    
    step_x_start = 140
    step_width = 250
    
    for step in steps:
        # Línea de energía
        color = COLORS['primary'] if step['status'] != "Vacío" else COLORS['grid']
        builder.line(Point(step_x_start, step['y']), Point(step_x_start + step_width, step['y']), 
                    stroke=color, stroke_width=4)
        
        # Etiqueta subnivel
        builder.text(step['label'], Point(step_x_start - 30, step['y'] + 6), 
                    font_size=18, font_weight="bold", fill=COLORS['text'], anchor="middle")
        
        # Electrones (bolitas)
        for i in range(step['e']):
            ex = step_x_start + 30 + i * 35
            ey = step['y'] - 12
            e_color = COLORS['primary'] if step['status'] == "Lleno" else COLORS['highlight']
            builder.circle(Point(ex, ey), 8, fill=e_color, stroke="white", stroke_width=1)
            builder.text("-", Point(ex, ey + 2), font_size=10, font_weight="bold", fill="white", anchor="middle")

    # Flecha de flujo (Llenado)
    builder.arrow(Point(width - 100, 400), Point(width - 100, 150), 
                stroke=COLORS['highlight'], stroke_width=4, dashed=True)
    builder.text("Orden de", Point(width - 90, 260), font_size=14, font_weight="bold", 
                fill=COLORS['highlight'], anchor="start")
    builder.text("Llenado", Point(width - 90, 280), font_size=14, font_weight="bold", 
                fill=COLORS['highlight'], anchor="start")

    # Notas didácticas
    builder.rect(320, 360, 250, 80, fill="white", stroke=COLORS['grid'], rx=8)
    builder.text("1. Los niveles bajos", Point(335, 385), font_size=12, fill=COLORS['text'], anchor="start")
    builder.text("se ocupan primero.", Point(335, 400), font_size=12, fill=COLORS['text'], anchor="start")
    builder.text("2. Luego se 'construye'", Point(335, 420), font_size=12, fill=COLORS['text'], anchor="start")
    builder.text("hacia arriba.", Point(335, 435), font_size=12, fill=COLORS['text'], anchor="start")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/config-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = "aufbau-escalera.svg"
    (output_dir / filename).write_text(render_aufbau_ladder(), encoding="utf-8")
    print(f"✅ {filename} generado")

if __name__ == "__main__":
    main()

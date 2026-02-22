#!/usr/bin/env python3
"""
AUFBAU PRINCIPLE RENDERER
Ilustra el llenado de electrones desde los niveles de menor energía hacia los de mayor energía.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_aufbau_principle():
    width, height = 600, 450
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Principio de Aufbau", Point(width / 2, 40), 
                font_size=24, font_weight="bold", anchor="middle")
    
    # Eje de Energía (Vertical, a la izquierda)
    ax_x = 80
    ax_y_bottom = 380
    ax_y_top = 80
    builder.arrow(Point(ax_x, ax_y_bottom), Point(ax_x, ax_y_top), stroke=COLORS['text'], stroke_width=3)
    builder.text("ENERGÍA", Point(ax_x - 40, (ax_y_bottom + ax_y_top)/2), 
                font_size=16, font_weight="bold", fill=COLORS['text'], 
                anchor="middle") # Nota: Sin rotación en la API, pero el contexto es claro

    # Peldaños de la escalera (Niveles de energía)
    levels = [
        {"y": 350, "label": "1s", "electrons": 2, "full": True},
        {"y": 300, "label": "2s", "electrons": 2, "full": True},
        {"y": 250, "label": "2p", "electrons": 6, "full": True},
        {"y": 200, "label": "3s", "electrons": 2, "full": True},
        {"y": 150, "label": "3p", "electrons": 3, "full": False}, # Llenándose
    ]
    
    step_width = 300
    step_start_x = 150
    
    for level in levels:
        # Dibujar peldaño (Línea horizontal gruesa)
        builder.line(Point(step_start_x, level['y']), Point(step_start_x + step_width, level['y']), 
                    stroke=COLORS['grid'], stroke_width=3)
        
        # Etiqueta del subnivel
        builder.text(level['label'], Point(step_start_x - 30, level['y'] + 5), 
                    font_size=16, font_weight="bold", fill=COLORS['primary'], anchor="end")
        
        # Electrones representados como bolitas
        e_spacing = 25
        for i in range(level['electrons']):
            e_x = step_start_x + 20 + i * e_spacing
            e_y = level['y'] - 10
            color = COLORS['primary'] if level['full'] else COLORS['highlight']
            builder.circle(Point(e_x, e_y), 8, fill=color, stroke="white", stroke_width=1)
            builder.text("-", Point(e_x, e_y + 2), font_size=10, font_weight="bold", fill="white", anchor="middle")

    # Flecha de llenado (Animación visual)
    builder.arrow(Point(step_start_x + step_width + 30, 360), Point(step_start_x + step_width + 30, 140), 
                stroke=COLORS['highlight'], stroke_width=4, dashed=True)
    builder.text("Orden de llenado", Point(step_start_x + step_width + 40, 250), 
                font_size=14, font_weight="bold", fill=COLORS['highlight'], anchor="start")
    
    # Cuadro explicativo
    builder.rect(380, 280, 200, 120, fill="white", stroke=COLORS['grid'], stroke_width=1, rx=8)
    builder.text("Llenado progresivo:", Point(395, 305), font_size=14, font_weight="bold", anchor="start")
    builder.text("1. Niveles bajos primero", Point(395, 330), font_size=12, fill=COLORS['text_light'], anchor="start")
    builder.text("2. Construcción (Aufbau)", Point(395, 350), font_size=12, fill=COLORS['text_light'], anchor="start")
    builder.text("3. Hacia mayor energía", Point(395, 370), font_size=12, fill=COLORS['text_light'], anchor="start")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/configuracion-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = "aufbau-principio.svg"
    (output_dir / filename).write_text(render_aufbau_principle(), encoding="utf-8")
    print(f"✅ {filename} generado exitosamente")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
AUFBAU PROGRESSIVE RENDERER
Ilustra el llenado progresivo de orbitales como bloques apilados.
Muestra claramente la cantidad de orbitales por subnivel (s=1, p=3, d=5, f=7).
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_aufbau_progressive():
    width, height = 800, 650
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Llenado Progresivo de Orbitales", Point(width / 2, 40), 
                font_size=26, font_weight="bold", anchor="middle")
    builder.text("Orden de energía creciente (Principio de Aufbau)", Point(width / 2, 65), 
                font_size=14, fill=COLORS['text_light'], anchor="middle")
    
    # Configuración de subniveles en orden de llenado
    sublevels = [
        {"name": "1s", "orbitals": 1, "color": COLORS['primary']},
        {"name": "2s", "orbitals": 1, "color": COLORS['primary']},
        {"name": "2p", "orbitals": 3, "color": COLORS['purple']},
        {"name": "3s", "orbitals": 1, "color": COLORS['primary']},
        {"name": "3p", "orbitals": 3, "color": COLORS['purple']},
        {"name": "4s", "orbitals": 1, "color": COLORS['primary']},
        {"name": "3d", "orbitals": 5, "color": COLORS['teal']},
        {"name": "4p", "orbitals": 3, "color": COLORS['purple']},
        {"name": "5s", "orbitals": 1, "color": COLORS['primary']},
    ]
    
    box_size = 35
    gap_y = 15
    start_y = height - 80
    center_x = 350
    
    # Eje de energía
    builder.arrow(Point(80, start_y + 40), Point(80, 100), stroke=COLORS['text'], stroke_width=3)
    builder.text("MAYOR ENERGÍA", Point(70, 100), font_size=12, font_weight="bold", anchor="start")
    
    for i, sub in enumerate(sublevels):
        y = start_y - i * (box_size + gap_y)
        
        # Etiqueta del subnivel
        builder.text(sub['name'], Point(center_x - 60, y + box_size/2 + 5), 
                    font_size=18, font_weight="bold", fill=COLORS['text'], anchor="end")
        
        # Dibujar los orbitales (cajitas)
        row_width = sub['orbitals'] * box_size
        row_start_x = center_x
        
        for j in range(sub['orbitals']):
            bx = row_start_x + j * box_size
            builder.rect(bx, y, box_size, box_size, fill=sub['color'], fill_opacity=0.2, 
                        stroke=sub['color'], stroke_width=2, rx=4)
            
            # Electrones (opcional, uno o dos en los primeros niveles)
            if i < 4: # Llenamos los primeros como ejemplo
                # e1 (flecha arriba)
                builder.line(Point(bx + box_size*0.35, y + box_size*0.8), 
                            Point(bx + box_size*0.35, y + box_size*0.2), 
                            stroke=sub['color'], stroke_width=2)
                builder.path(f"M {bx + box_size*0.2} {y + box_size*0.4} L {bx + box_size*0.35} {y + box_size*0.2} L {bx + box_size*0.5} {y + box_size*0.4}", 
                            stroke=sub['color'], stroke_width=2)
                
                # e2 (flecha abajo)
                builder.line(Point(bx + box_size*0.65, y + box_size*0.2), 
                            Point(bx + box_size*0.65, y + box_size*0.8), 
                            stroke=sub['color'], stroke_width=2)
                builder.path(f"M {bx + box_size*0.5} {y + box_size*0.6} L {bx + box_size*0.65} {y + box_size*0.8} L {bx + box_size*0.8} {y + box_size*0.6}", 
                            stroke=sub['color'], stroke_width=2)

    # Leyenda de tipos de orbitales
    legend_x = 600
    legend_y = 150
    builder.rect(legend_x, legend_y, 160, 180, fill="white", stroke=COLORS['grid'], rx=8)
    builder.text("Orbitales por Tipo", Point(legend_x + 80, legend_y + 25), 
                font_size=14, font_weight="bold", anchor="middle")
    
    types = [("s", 1, COLORS['primary']), ("p", 3, COLORS['purple']), ("d", 5, COLORS['teal']), ("f", 7, COLORS['highlight'])]
    for k, (t, n, c) in enumerate(types):
        ly = legend_y + 55 + k * 30
        builder.rect(legend_x + 15, ly - 10, 15, 15, fill=c, rx=2)
        builder.text(f"Tipo {t}: {n} orbital", Point(legend_x + 40, ly + 2), 
                    font_size=12, fill=COLORS['text'], anchor="start")

    # Nota sobre capacidad
    builder.rect(legend_x, 350, 160, 80, fill="#eff6ff", stroke=COLORS['primary'], rx=8)
    builder.text("CAPACIDAD", Point(legend_x + 80, 375), font_size=12, font_weight="bold", fill=COLORS['primary'], anchor="middle")
    builder.text("Cada cajita =", Point(legend_x + 80, 395), font_size=11, fill=COLORS['primary'], anchor="middle")
    builder.text("MÁX 2 e⁻", Point(legend_x + 80, 415), font_size=14, font_weight="bold", fill=COLORS['primary'], anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/config-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = "aufbau-progresivo.svg"
    (output_dir / filename).write_text(render_aufbau_progressive(), encoding="utf-8")
    print(f"✅ {filename} generado")

if __name__ == "__main__":
    main()

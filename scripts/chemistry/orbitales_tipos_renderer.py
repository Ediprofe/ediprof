#!/usr/bin/env python3
"""
ORBITALES TIPOS RENDERER
Ilustra las formas de los orbitales s, p, d, f de manera esquemática.
"""

import math
import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_orbital_types():
    width, height = 800, 300
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Tipos de Orbitales", Point(width / 2, 35), 
                font_size=24, font_weight="bold", anchor="middle")
    
    # Posiciones horizontales
    x_positions = [100, 300, 500, 700]
    y_center = 170
    
    types = [
        {"name": "s", "shape": "Esférica", "color": COLORS['primary']},
        {"name": "p", "shape": "Mancuerna", "color": COLORS['purple']},
        {"name": "d", "shape": "Trébol", "color": COLORS['teal']},
        {"name": "f", "shape": "Compleja", "color": COLORS['highlight']},
    ]
    
    for i, t in enumerate(types):
        cx = x_positions[i]
        
        # Etiqueta de tipo
        builder.text(f"Orbital '{t['name']}'", Point(cx, 80), 
                    font_size=18, font_weight="bold", fill=t['color'], anchor="middle")
        
        # Forma esquemática
        if t['name'] == 's':
            # Esfera
            builder.circle(Point(cx, y_center), 40, fill=t['color'], fill_opacity=0.6, stroke=t['color'], stroke_width=2)
            # Efecto 3D simple
            builder.circle(Point(cx - 10, y_center - 10), 10, fill="white", fill_opacity=0.4)
            
        elif t['name'] == 'p':
            # Mancuerna (Dos lóbulos)
            builder.circle(Point(cx, y_center - 30), 25, fill=t['color'], fill_opacity=0.6, stroke=t['color'], stroke_width=1.5)
            builder.circle(Point(cx, y_center + 30), 25, fill=t['color'], fill_opacity=0.6, stroke=t['color'], stroke_width=1.5)
            # Centro del átomo (Nucleo pequeño)
            builder.circle(Point(cx, y_center), 5, fill=COLORS['accent'])
            
        elif t['name'] == 'd':
            # Trébol (Cuatro lóbulos)
            angles = [math.pi/4, 3*math.pi/4, 5*math.pi/4, 7*math.pi/4]
            for angle in angles:
                lx = cx + 35 * math.cos(angle)
                ly = y_center + 35 * math.sin(angle)
                builder.circle(Point(lx, ly), 22, fill=t['color'], fill_opacity=0.5, stroke=t['color'], stroke_width=1)
            # Nucleo
            builder.circle(Point(cx, y_center), 5, fill=COLORS['accent'])
            
        elif t['name'] == 'f':
            # Compleja (Varios lóbulos y anillos esquemáticos)
            # 6 lóbulos pequeños
            for j in range(6):
                angle = j * (2 * math.pi / 6)
                lx = cx + 38 * math.cos(angle)
                ly = y_center + 38 * math.sin(angle)
                builder.circle(Point(lx, ly), 16, fill=t['color'], fill_opacity=0.4, stroke=t['color'], stroke_width=1)
            # Anillo central
            builder.circle(Point(cx, y_center), 18, fill="none", stroke=t['color'], stroke_width=4, fill_opacity=0.2)
            # Nucleo
            builder.circle(Point(cx, y_center), 5, fill=COLORS['accent'])
            
        # Descripción
        builder.text(t['shape'], Point(cx, height - 40), 
                    font_size=14, font_weight="bold", fill=COLORS['text_light'], anchor="middle")
        builder.text("Máx 2 e⁻", Point(cx, height - 20), 
                    font_size=12, fill=COLORS['text_light'], anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/configuracion-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = "orbitales-tipos.svg"
    (output_dir / filename).write_text(render_orbital_types(), encoding="utf-8")
    print(f"✅ {filename} generado exitosamente")

if __name__ == "__main__":
    main()

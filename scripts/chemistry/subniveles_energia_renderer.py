#!/usr/bin/env python3
"""
SUBNIVELES ENERGIA RENDERER
Ilustra la notación de un subnivel (nivel + tipo de orbital).
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_sublevel_notation():
    width, height = 600, 350
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Notación de un Subnivel", Point(width / 2, 45), 
                font_size=24, font_weight="bold", anchor="middle")
    
    # Ejemplo central: 3d
    cx, cy = width / 2, 160
    
    # Notación: 3d
    builder.text("3", Point(cx - 30, cy), font_size=100, font_weight="bold", fill=COLORS['primary'], anchor="middle")
    builder.text("d", Point(cx + 35, cy), font_size=100, font_weight="bold", fill=COLORS['purple'], anchor="middle")
    
    # Flechas y Explicación para el 3 (Nivel)
    l_x, l_y = cx - 35, cy + 60
    builder.arrow(Point(l_x, l_y + 100), Point(l_x, l_y), stroke=COLORS['primary'], stroke_width=3)
    builder.rect(l_x - 90, l_y + 100, 180, 45, fill="white", stroke=COLORS['primary'], rx=8)
    builder.text("Nivel de Energía", Point(l_x, l_y + 120), font_size=16, font_weight="bold", fill=COLORS['primary'], anchor="middle")
    builder.text("(Capa o Periodo)", Point(l_x, l_y + 138), font_size=12, fill=COLORS['text_light'], anchor="middle")
    
    # Flechas y Explicación para la d (Orbital)
    o_x, o_y = cx + 40, cy + 60
    builder.arrow(Point(o_x, o_y + 100), Point(o_x, o_y), stroke=COLORS['purple'], stroke_width=3)
    builder.rect(o_x - 90, o_y + 100, 180, 45, fill="white", stroke=COLORS['purple'], rx=8)
    builder.text("Tipo de Orbital", Point(o_x, o_y + 120), font_size=16, font_weight="bold", fill=COLORS['purple'], anchor="middle")
    builder.text("(s, p, d o f)", Point(o_x, o_y + 138), font_size=12, fill=COLORS['text_light'], anchor="middle")

    # Pequeño resumen lateral
    builder.rect(480, 40, 100, 100, fill="#fef3c7", stroke="#f59e0b", rx=8)
    builder.text("Ejemplo", Point(530, 65), font_size=12, font_weight="bold", fill="#92400e", anchor="middle")
    builder.text("3d", Point(530, 95), font_size=30, font_weight="bold", fill="#92400e", anchor="middle")
    builder.text("Nivel 3, Orbital d", Point(530, 125), font_size=10, fill="#92400e", anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/configuracion-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = "subniveles-notacion.svg"
    (output_dir / filename).write_text(render_sublevel_notation(), encoding="utf-8")
    print(f"✅ {filename} generado exitosamente")

if __name__ == "__main__":
    main()

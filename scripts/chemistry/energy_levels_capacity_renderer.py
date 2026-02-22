#!/usr/bin/env python3
"""
ENERGY LEVELS CAPACITY RENDERER - IMPROVED VERSION
Ilustra la capacidad máxima de electrones por nivel usando la fórmula 2n².
Incluye electrones con colores coordinados y diseño sin solapamientos.
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

def render_energy_levels_capacity():
    # Aumentamos dimensiones para evitar solapamientos
    width, height = 800, 560
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Capacidad Máxima de Electrones", Point(width / 2, 45), 
                font_size=26, font_weight="bold", anchor="middle")
    
    # Centro para el diagrama (lado izquierdo)
    cx, cy = 250, 280
    center = Point(cx, cy)
    
    levels = [
        {"n": 1, "r": 55,  "cap": 2,  "color": COLORS['primary']},
        {"n": 2, "r": 95,  "cap": 8,  "color": COLORS['purple']},
        {"n": 3, "r": 135, "cap": 18, "color": COLORS['teal']},
        {"n": 4, "r": 175, "cap": 32, "color": COLORS['highlight']},
    ]
    
    # 1. Dibujar Niveles y Electrones coordinados por color
    orbit_color = "#334155" # Slate 700 (Oscuro sólido)
    for level in levels:
        # Órbita sólida
        builder.circle(center, level['r'], fill="none", stroke=orbit_color, stroke_width=2)
        builder.text(f"n={level['n']}", Point(cx, cy - level['r'] - 8), 
                    font_size=11, font_weight="bold", fill=orbit_color, anchor="middle")
        
        # Electrones con el color correspondiente a la tabla
        e_positions = get_electron_coords(cx, cy, level['r'], level['cap'])
        # Para el nivel 4 (32 e-) los hacemos un poco más pequeños
        e_radius = 5 if level['cap'] > 18 else 6
        
        for pos in e_positions:
            builder.circle(pos, e_radius, fill=level['color'], stroke="white", stroke_width=1)
            # Solo ponemos el signo '-' si hay espacio (niveles 1-3)
            if level['cap'] <= 18:
                builder.text("-", Point(pos.x, pos.y + 1.5), font_size=e_radius*1.5, 
                            font_weight="bold", fill="white", anchor="middle")

    # Núcleo
    builder.circle(center, 25, fill=COLORS['accent'], stroke=COLORS['white'], stroke_width=2)
    builder.text("+", Point(cx, cy + 8), font_size=28, font_weight="bold", fill="white", anchor="middle")

    # 2. Tabla de capacidades (Lado derecho)
    table_x = 480
    table_y = 120
    row_h = 65
    
    # Encabezado de la tabla
    builder.rect(table_x, table_y - 35, 270, 35, fill="#1e293b", rx=6)
    builder.text("Nivel", Point(table_x + 45, table_y - 12), font_size=14, font_weight="bold", fill="white", anchor="middle")
    builder.text("Fórmula 2n²", Point(table_x + 135, table_y - 12), font_size=14, font_weight="bold", fill="white", anchor="middle")
    builder.text("Capacidad", Point(table_x + 225, table_y - 12), font_size=14, font_weight="bold", fill="white", anchor="middle")

    for i, level in enumerate(levels):
        y = table_y + i * row_h
        fill = "white" if i % 2 == 0 else "#f8fafc"
        builder.rect(table_x, y, 270, row_h, fill=fill, stroke=COLORS['grid'], stroke_width=1)
        
        builder.text(str(level['n']), Point(table_x + 45, y + row_h/2), font_size=16, font_weight="bold", fill=COLORS['text'], anchor="middle")
        builder.text(f"2({level['n']}²)", Point(table_x + 135, y + row_h/2), font_size=16, fill=COLORS['text_light'], anchor="middle")
        
        # Círculo destacado que coincide con los electrones
        cap_x = table_x + 225
        cap_y = y + row_h/2
        builder.circle(Point(cap_x, cap_y), 20, fill=level['color'], stroke="white", stroke_width=2)
        builder.text(str(level['cap']), Point(cap_x, cap_y + 5), font_size=15, font_weight="bold", fill="white", anchor="middle")

    # 3. Cuadro de la fórmula universal (Bajado para evitar solapamiento)
    formula_x, formula_y = width / 2, height - 50
    builder.rect(formula_x - 180, formula_y - 25, 360, 50, fill="#fef3c7", stroke="#f59e0b", stroke_width=1.5, rx=10)
    builder.text("Capacidad Máxima = 2n²", Point(formula_x, formula_y + 6), 
                font_size=20, font_weight="bold", fill="#92400e", anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/configuracion-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    filename = "capacidad-niveles.svg"
    (output_dir / filename).write_text(render_energy_levels_capacity(), encoding="utf-8")
    print(f"✅ {filename} actualizado exitosamente (colores coordinados y sin solapamientos)")

if __name__ == "__main__":
    main()

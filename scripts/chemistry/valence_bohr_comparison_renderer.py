#!/usr/bin/env python3
"""
VALENCE BOHR COMPARISON RENDERER
- Ilustración 3: Modelos atómicos comparativos resaltando los electrones de valencia y su relación con el grupo.
- Compara Sodio (IA) y Fósforo (VA).
"""

import sys
import math
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def polar_to_cartesian(r, theta, cx, cy):
    return Point(cx + r * math.cos(theta), cy + r * math.sin(theta))

def draw_bohr_atom(builder, cx, cy, name, symbol, group, config, shells, highlight_color):
    # 1. Título y Grupo
    builder.text(f"{name} ({symbol})", Point(cx, cy - 160), font_size=20, font_weight="bold", fill="#1e293b", anchor="middle")
    builder.text(f"Grupo {group}", Point(cx, cy - 135), font_size=18, font_weight="900", fill=highlight_color, anchor="middle")
    builder.text(config, Point(cx, cy + 150), font_size=16, font_family="monospace", fill="#64748b", anchor="middle")

    # 2. Órbitas
    base_r = 40
    step = 25
    for i, count in enumerate(shells):
        r = base_r + i * step
        is_last = (i == len(shells) - 1)
        stroke = highlight_color if is_last else "#e2e8f0"
        width = 2.5 if is_last else 1.5
        builder.circle(Point(cx, cy), r, fill="none", stroke=stroke, stroke_width=width, fill_opacity=1.0 if is_last else 0.5)
        
        # Electrones
        angle_step = (2 * math.pi) / count
        for e in range(count):
            theta = -math.pi/2 + e * angle_step
            pos = polar_to_cartesian(r, theta, cx, cy)
            
            e_fill = highlight_color if is_last else "#94a3b8"
            builder.circle(Point(pos.x, pos.y), 4, fill=e_fill, stroke="white", stroke_width=0.8)
            builder.text("-", Point(pos.x, pos.y + 1.5), font_size=7, font_weight="bold", fill="white", anchor="middle")

    # 3. Núcleo
    builder.circle(Point(cx, cy), 18, fill="#f8fafc", stroke="#64748b", stroke_width=1.5)
    builder.text(symbol, Point(cx, cy + 4), font_size=12, font_weight="bold", fill="#1e293b", anchor="middle")

def main():
    width, height = 900, 400
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título general
    builder.text("Relación Grupo - Capa de Valencia", Point(width/2, 40), font_size=24, font_weight="bold", fill=COLORS['text'], anchor="middle")

    # 1. Sodio (IA) - Izquierda
    draw_bohr_atom(builder, 250, 200, "Sodio", "Na", "IA", "1s² 2s² 2p⁶ 3s¹", [2, 8, 1], "#fbbf24")
    
    # 2. Fósforo (VA) - Derecha
    draw_bohr_atom(builder, 650, 200, "Fósforo", "P", "VA", "[Ne] 3s² 3p³", [2, 8, 5], "#3b82f6")

    # Flechas explicativas o notas
    builder.text("1 electrón de valencia", Point(250, 360), font_size=14, font_weight="bold", fill="#b45309", anchor="middle")
    builder.text("5 electrones de valencia", Point(650, 360), font_size=14, font_weight="bold", fill="#1d4ed8", anchor="middle")

    output_path = Path("public/images/quimica/config-electronica/bloques/ejemplos-valencia-bohr.svg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(builder.build(), encoding="utf-8")
    print(f"✅ {output_path.name} generado")

if __name__ == "__main__":
    main()

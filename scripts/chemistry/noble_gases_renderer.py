#!/usr/bin/env python3
"""
VALENCE EXAMPLES DETAIL RENDERER - V12 (NOBLE GASES SPECIAL)
- Genera 2 imágenes por gas noble.
- Distribución COMPLETA (sin abreviar capas internas).
- Mismo estilo visual que los ejemplos representativos.
"""

import sys
import math
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

ROMAN_A = {
    1: "IA", 2: "IIA",
    13: "IIIA", 14: "IVA", 15: "VA", 16: "VIA", 17: "VIIA", 18: "VIIIA"
}

TERMS = {
    1: "s¹", 2: "s²",
    13: "p¹", 14: "p²", 15: "p³", 16: "p⁴", 17: "p⁵", 18: "p⁶"
}

def draw_full_periodic_table(builder, start_x, start_y, target_z, target_color):
    box = 40
    gap = 4
    for c in range(1, 19):
        tx = start_x + (c-1)*box + (box-gap)/2
        is_transition = 3 <= c <= 12
        modern_color = "#cbd5e1" if is_transition else "#64748b"
        roman_color = "#cbd5e1" if is_transition else "#1e293b"
        term = TERMS.get(c, "")
        if term:
            builder.text(term, Point(tx, start_y - 45), font_size=12, font_weight="900", fill="#3b82f6" if c > 2 else "#f59e0b")
        roman = ROMAN_A.get(c, "")
        if roman:
            builder.text(roman, Point(tx, start_y - 28), font_size=11, font_weight="900", fill=roman_color)
        builder.text(str(c), Point(tx, start_y - 12), font_size=10, font_weight="bold", fill=modern_color)

    for r in range(1, 8):
        ty = start_y + (r-1)*box + (box-gap)/2
        builder.text(str(r), Point(start_x - 25, ty + 5), font_size=14, font_weight="900", fill="#64748b")

    # Mapeo de Z para Gases Nobles
    coords = {
        2: (1, 18), 10: (2, 18), 18: (3, 18), 
        36: (4, 18), 54: (5, 18), 86: (6, 18)
    }
    target_pos = coords.get(target_z)

    for r in range(1, 8):
        for c in range(1, 19):
            exists = True
            if r == 1 and 1 < c < 18: exists = False
            if (r == 2 or r == 3) and 2 < c < 13: exists = False
            if not exists: continue
            is_target = target_pos == (r, c)
            is_transition = 3 <= c <= 12
            x, y = start_x + (c-1)*box, start_y + (r-1)*box
            
            fill = target_color if is_target else "#f8fafc"
            stroke = target_color if is_target else "#cbd5e1"
            width = 4 if is_target else 1
            op = 1.0 if not is_transition else 0.3
            builder.rect(x, y, box-gap, box-gap, fill=fill, stroke=stroke, stroke_width=width, rx=6, fill_opacity=op)

def render_position_image(name, symbol, z, color, filename):
    width, height = 850, 480
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(f"Ubicación: {name} ({symbol})", Point(width/2, 45), font_size=30, font_weight="900", fill="#1e293b")
    draw_full_periodic_table(builder, 60, 135, z, color)
    output_path = Path("public/images/quimica/config-electronica/bloques/gases-nobles") / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(builder.build(), encoding="utf-8")

def render_distribution_image(name, symbol, z, shells, config, color, filename):
    num_shells = len(shells)
    width, height = 850, 850 if num_shells >= 5 else 750
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(f"Gas Noble: {name} ({symbol})", Point(width/2, 50), font_size=32, font_weight="900", fill="#1e293b")
    
    cx, cy = width/2, 420
    base_r = 60
    step = 45 if num_shells < 5 else 38
    
    for i, count in enumerate(shells):
        r = base_r + i * step
        is_last = (i == num_shells - 1)
        stroke = color if is_last else "#e2e8f0"
        builder.circle(Point(cx, cy), r, fill="none", stroke=stroke, stroke_width=4 if is_last else 1.5, fill_opacity=1.0 if is_last else 0.3)
        
        angle_step = (2 * math.pi) / count
        for e in range(count):
            theta = -math.pi/2 + e * angle_step
            pos = Point(cx + r * math.cos(theta), cy + r * math.sin(theta))
            e_color = color if is_last else "#94a3b8"
            builder.circle(Point(pos.x, pos.y), 6, fill=e_color, stroke="white", stroke_width=1.2)
            builder.text("-", Point(pos.x, pos.y + 2), font_size=11, font_weight="900", fill="white")

    builder.circle(Point(cx, cy), 35, fill="#f1f5f9", stroke="#1e293b", stroke_width=3)
    builder.text(symbol, Point(cx, cy - 2), font_size=22, font_weight="900", fill="#1e293b")
    builder.text(f"Z={z}", Point(cx, cy + 18), font_size=14, font_weight="bold", fill="#64748b")

    # Configuración COMPLETA (Sin abreviar para gases nobles)
    config_y = height - 60
    builder.rect(width/2 - 350, config_y - 25, 700, 50, fill="#f1f5f9", rx=25)
    builder.text(f"Configuración: {config}", Point(width/2, config_y + 8), font_size=18, font_family="monospace", font_weight="bold", fill="#334155")

    output_path = Path("public/images/quimica/config-electronica/bloques/gases-nobles") / filename
    output_path.write_text(builder.build(), encoding="utf-8")

def main():
    # Gases Nobles (VIIIA)
    nobles = [
        ("Helio", "He", 2, [2], "1s²", "#3b82f6"),
        ("Neón", "Ne", 10, [2, 8], "1s² 2s² 2p⁶", "#3b82f6"),
        ("Argón", "Ar", 18, [2, 8, 8], "1s² 2s² 2p⁶ 3s² 3p⁶", "#3b82f6"),
        ("Kriptón", "Kr", 36, [2, 8, 18, 8], "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶", "#3b82f6"),
        ("Xenón", "Xe", 54, [2, 8, 18, 18, 8], "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶", "#3b82f6"),
        ("Radón", "Rn", 86, [2, 8, 18, 32, 18, 8], "1s² ... 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶", "#3b82f6")
    ]
    
    for ex in nobles:
        slug = ex[1].lower()
        render_position_image(ex[0], ex[1], ex[2], ex[5], f"noble-{slug}-pos.svg")
        render_distribution_image(ex[0], ex[1], ex[2], ex[3], ex[4], ex[5], f"noble-{slug}-dist.svg")
        print(f"✅ Gas Noble {ex[1]} generado")

if __name__ == "__main__":
    main()

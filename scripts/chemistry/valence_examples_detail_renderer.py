#!/usr/bin/env python3
"""
VALENCE EXAMPLES DETAIL RENDERER - V11 (REORDERED LABELS)
- Etiquetas: 1. Terminación (Top), 2. Romano (Mid), 3. Moderno (Bottom).
- Bloque central atenuado (0.3).
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
    """Dibuja una tabla periódica con etiquetas reordenadas."""
    box = 40
    gap = 4
    
    # 1. Triple Notación de Grupos (Arriba - Reordenada)
    for c in range(1, 19):
        tx = start_x + (c-1)*box + (box-gap)/2
        is_transition = 3 <= c <= 12
        
        # Color de texto atenuado para transición
        modern_color = "#cbd5e1" if is_transition else "#64748b"
        roman_color = "#cbd5e1" if is_transition else "#1e293b"
        
        # FILA 1: Terminación (ARRIBA DEL TODO)
        term = TERMS.get(c, "")
        if term:
            builder.text(term, Point(tx, start_y - 45), font_size=12, font_weight="900", fill="#3b82f6" if c > 2 else "#f59e0b")
        
        # FILA 2: Notación Romana (CENTRO)
        roman = ROMAN_A.get(c, "")
        if roman:
            builder.text(roman, Point(tx, start_y - 28), font_size=11, font_weight="900", fill=roman_color)
        
        # FILA 3: Notación Moderna (BASE)
        builder.text(str(c), Point(tx, start_y - 12), font_size=10, font_weight="bold", fill=modern_color)

    # 2. Etiquetas de Periodo
    for r in range(1, 8):
        ty = start_y + (r-1)*box + (box-gap)/2
        builder.text(str(r), Point(start_x - 25, ty + 5), font_size=14, font_weight="900", fill="#64748b")

    # Coordenadas exactas
    coords = {
        10: (2, 18), 18: (3, 18), 19: (4, 1), 34: (4, 16),
        38: (5, 2), 53: (5, 17), 54: (5, 18), 55: (6, 1),
        56: (6, 2), 83: (6, 15)
    }
    target_pos = coords.get(target_z)

    # 3. Celdas
    for r in range(1, 8):
        for c in range(1, 19):
            exists = True
            if r == 1 and 1 < c < 18: exists = False
            if (r == 2 or r == 3) and 2 < c < 13: exists = False
            if not exists: continue
            
            is_target = target_pos == (r, c)
            is_transition = 3 <= c <= 12
            
            x, y = start_x + (c-1)*box, start_y + (r-1)*box
            
            if is_target:
                fill = target_color
                stroke = target_color
                width = 4
                op = 1.0
            elif is_transition:
                fill = "#f1f5f9"
                stroke = "#e2e8f0"
                width = 0.8
                op = 0.3
            else:
                fill = "#f8fafc"
                stroke = "#cbd5e1"
                width = 1
                op = 1.0
            
            builder.rect(x, y, box-gap, box-gap, fill=fill, stroke=stroke, stroke_width=width, rx=6, fill_opacity=op)

def render_position_image(name, symbol, z, group_rom, period, color, filename):
    width, height = 850, 480
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(f"Ubicación: {name} ({symbol})", Point(width/2, 45), font_size=30, font_weight="900", fill="#1e293b")
    draw_full_periodic_table(builder, 60, 135, z, color) # Bajamos un poco la tabla para las 3 filas de texto
    output_path = Path("public/images/quimica/config-electronica/bloques/ejemplos") / filename
    output_path.write_text(builder.build(), encoding="utf-8")

def render_distribution_image(name, symbol, z, shells, config, color, filename):
    num_shells = len(shells)
    width, height = 800, 750 if num_shells < 5 else 820
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(f"Distribución Electrónica: {name} ({symbol})", Point(width/2, 50), font_size=32, font_weight="900", fill="#1e293b")
    cx, cy = width/2, 400 if num_shells < 5 else 420
    base_r = 60
    step = 40 if num_shells < 6 else 36
    for i, count in enumerate(shells):
        r = base_r + i * step
        is_last = (i == num_shells - 1)
        stroke = color if is_last else "#e2e8f0"
        builder.circle(Point(cx, cy), r, fill="none", stroke=stroke, stroke_width=4 if is_last else 1.5, fill_opacity=1.0 if is_last else 0.2)
        angle_step = (2 * math.pi) / count
        for e in range(count):
            theta = -math.pi/2 + e * angle_step
            pos = Point(cx + r * math.cos(theta), cy + r * math.sin(theta))
            e_color = color if is_last else "#94a3b8"
            builder.circle(Point(pos.x, pos.y), 6, fill=e_color, stroke="white", stroke_width=1.2)
            builder.text("-", Point(pos.x, pos.y + 2), font_size=11, font_weight="900", fill="white")
    builder.circle(Point(cx, cy), 32, fill="#f1f5f9", stroke="#1e293b", stroke_width=3)
    builder.text(symbol, Point(cx, cy - 2), font_size=20, font_weight="900", fill="#1e293b")
    builder.text(f"Z={z}", Point(cx, cy + 16), font_size=12, font_weight="bold", fill="#64748b")
    config_y = height - 60
    builder.rect(width/2 - 300, config_y - 25, 600, 50, fill="#f1f5f9", rx=25)
    builder.text(f"Configuración: {config}", Point(width/2, config_y + 8), font_size=22, font_family="monospace", font_weight="bold", fill="#334155")
    output_path = Path("public/images/quimica/config-electronica/bloques/ejemplos") / filename
    output_path.write_text(builder.build(), encoding="utf-8")

def main():
    examples = [
        ("Neón", "Ne", 10, "VIIIA", 2, [2, 8], "1s² 2s² 2p⁶", "#3b82f6"),
        ("Argón", "Ar", 18, "VIIIA", 3, [2, 8, 8], "[Ne] 3s² 3p⁶", "#3b82f6"),
        ("Potasio", "K", 19, "IA", 4, [2, 8, 8, 1], "[Ar] 4s¹", "#f59e0b"),
        ("Selenio", "Se", 34, "VIA", 4, [2, 8, 18, 6], "[Ar] 4s² 3d¹⁰ 4p⁴", "#ef4444"),
        ("Estroncio", "Sr", 38, "IIA", 5, [2, 8, 18, 8, 2], "[Kr] 5s²", "#10b981"),
        ("Yodo", "I", 53, "VIIA", 5, [2, 8, 18, 18, 7], "[Kr] 5s² 4d¹⁰ 5p⁵", "#06b6d4"),
        ("Xenón", "Xe", 54, "VIIIA", 5, [2, 8, 18, 18, 8], "[Kr] 5s² 4d¹⁰ 5p⁶", "#3b82f6"),
        ("Cesio", "Cs", 55, "IA", 6, [2, 8, 18, 18, 8, 1], "[Xe] 6s¹", "#f59e0b"),
        ("Bario", "Ba", 56, "IIA", 6, [2, 8, 18, 18, 8, 2], "[Xe] 6s²", "#10b981"),
        ("Bismuto", "Bi", 83, "VA", 6, [2, 8, 18, 32, 18, 5], "[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p³", "#8b5cf6")
    ]
    for ex in examples:
        slug = ex[1].lower()
        render_position_image(ex[0], ex[1], ex[2], ex[3], ex[4], ex[7], f"valencia-{slug}-pos.svg")
        render_distribution_image(ex[0], ex[1], ex[2], ex[5], ex[6], ex[7], f"valencia-{slug}-dist.svg")
        print(f"✅ Ejemplo {ex[1]} actualizado (Etiquetas reordenadas)")

if __name__ == "__main__":
    main()

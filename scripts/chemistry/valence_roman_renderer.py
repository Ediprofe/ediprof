#!/usr/bin/env python3
"""
VALENCE ROMAN RENDERER - V2
- Inserta un salto visual entre el grupo 2 y 13.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def draw_roman_rule(builder, canvas_width, canvas_height):
    start_y = 100
    row_height = 80
    box_w = 85
    gap = 12
    jump_w = 100 # Espacio para el salto
    
    groups = [
        {"mod": "1", "rom": "IA", "e": "1"},
        {"mod": "2", "rom": "IIA", "e": "2"},
        {"jump": True}, # Marcador de salto
        {"mod": "13", "rom": "IIIA", "e": "3"},
        {"mod": "14", "rom": "IVA", "e": "4"},
        {"mod": "15", "rom": "VA", "e": "5"},
        {"mod": "16", "rom": "VIA", "e": "6"},
        {"mod": "17", "rom": "VIIA", "e": "7"},
        {"mod": "18", "rom": "VIIIA", "e": "8"}
    ]
    
    total_w = (len(groups)-1) * (box_w + gap) + jump_w - gap
    start_x = (canvas_width - total_w) / 2 + 40
    
    # Etiquetas de Fila
    label_x = start_x - 120
    builder.text("Grupo Moderno", Point(label_x, start_y + 30), font_size=15, font_weight="bold", fill="#64748b", anchor="start")
    builder.text("Grupo Romano", Point(label_x, start_y + row_height + 40), font_size=15, font_weight="900", fill="#1e293b", anchor="start")
    builder.text("e- de Valencia", Point(label_x, start_y + 2*row_height + 40), font_size=15, font_weight="bold", fill="#3b82f6", anchor="start")

    current_x = start_x
    for g in groups:
        if g.get("jump"):
            # Dibujar salto visual
            jx = current_x + jump_w/2
            builder.text("...", Point(jx, start_y + 30), font_size=30, fill="#cbd5e1")
            builder.rect(current_x + 10, start_y + row_height + 10, jump_w - 20, 60, fill="#f1f5f9", stroke="#cbd5e1", dashed=True, rx=8)
            builder.text("Transición", Point(jx, start_y + row_height + 35), font_size=12, font_weight="bold", fill="#94a3b8")
            builder.text("(Bloque d)", Point(jx, start_y + row_height + 50), font_size=11, fill="#94a3b8")
            current_x += jump_w + gap
            continue

        cx = current_x + box_w/2
        
        # Fila 1: Moderno
        builder.rect(current_x, start_y, box_w, 60, fill="#f8fafc", stroke="#cbd5e1", rx=8)
        if int(g["mod"]) > 10:
            builder.text("1", Point(cx - 10, start_y + 40), font_size=28, font_weight="bold", fill="#94a3b8", anchor="middle")
            builder.line(Point(cx - 18, start_y + 45), Point(cx - 2, start_y + 25), stroke="#ef4444", stroke_width=2.5)
            builder.text(g["mod"][1], Point(cx + 10, start_y + 40), font_size=28, font_weight="bold", fill="#3b82f6", anchor="middle")
        else:
            builder.text(g["mod"], Point(cx, start_y + 40), font_size=28, font_weight="bold", fill="#3b82f6", anchor="middle")
            
        # Fila 2: Romano
        builder.rect(current_x, start_y + row_height + 10, box_w, 60, fill="#eff6ff", stroke="#3b82f6", stroke_width=2, rx=8)
        builder.text(g["rom"], Point(cx, start_y + row_height + 50), font_size=22, font_weight="900", fill="#1e293b", anchor="middle")
        
        # Conexión
        builder.arrow(Point(cx, start_y + row_height + 80), Point(cx, start_y + 2*row_height + 10), stroke="#3b82f6", stroke_width=2)
        
        # Fila 3: Valencia
        builder.circle(Point(cx, start_y + 2*row_height + 40), 22, fill="#3b82f6", stroke="#1d4ed8")
        builder.text(g["e"], Point(cx, start_y + 2*row_height + 48), font_size=22, font_weight="900", fill="white", anchor="middle")
        
        current_x += box_w + gap

def main():
    width, height = 1150, 450
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text("El Secreto de la Familia A: Romano = Electrones de Valencia", Point(width/2, 45), font_size=28, font_weight="bold", fill=COLORS['text'], anchor="middle")
    draw_roman_rule(builder, width, height)
    
    output_path = Path("public/images/quimica/config-electronica/bloques/codigo-romano-valencia.svg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(builder.build(), encoding="utf-8")
    print(f"✅ {output_path.name} actualizado")

if __name__ == "__main__":
    main()

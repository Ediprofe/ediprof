#!/usr/bin/env python3
"""
PERIODIC FAMILIES RENDERER - PREMIUM V4 (CENTERED & LARGE)
- Centrado automático y tamaño de caja aumentado.
- Símbolos y triple notación.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

BLOCK_COLORS = {
    's': '#fef3c7', 's_stroke': '#f59e0b',
    'p': '#e0f2fe', 'p_stroke': '#0ea5e9',
    'd': '#fee2e2', 'd_stroke': '#ef4444',
    'neutral': '#f8fafc', 'neutral_stroke': '#cbd5e1'
}

SYMBOLS = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
]

ROMAN_A = {1: "IA", 2: "IIA", 13: "IIIA", 14: "IVA", 15: "VA", 16: "VIA", 17: "VIIA", 18: "VIIIA"}
TERMS = {1: "s¹", 2: "s²", 13: "p¹", 14: "p²", 15: "p³", 16: "p⁴", 17: "p⁵", 18: "p⁶"}

def get_block(r, c):
    if c <= 2: return 's'
    if c >= 13: return 'p'
    if r == 1 and c == 18: return 's'
    return 'd'

def draw_centered_family_bridge(builder, canvas_width, start_y):
    box = 52 # Aumentado de 45 a 52
    gap = 4
    table_width = 18 * box + 17 * gap
    start_x = (canvas_width - table_width) / 2 + 10 # Margen extra para periodo
    
    # 1. TRIPLE NOTACIÓN (Arriba)
    for c in range(1, 19):
        tx = start_x + (c-1)*box + (box-gap)/2
        is_transition = 3 <= c <= 12
        
        modern_color = "#cbd5e1" if is_transition else "#64748b"
        roman_color = "#cbd5e1" if is_transition else "#1e293b"
        
        # Terminación
        term = TERMS.get(c, "")
        if term:
            builder.text(term, Point(tx, start_y - 55), font_size=14, font_weight="900", fill="#3b82f6" if c > 2 else "#f59e0b")
        # Romano
        roman = ROMAN_A.get(c, "")
        if roman:
            builder.text(roman, Point(tx, start_y - 35), font_size=12, font_weight="900", fill=roman_color)
        # Moderno
        builder.text(str(c), Point(tx, start_y - 15), font_size=11, font_weight="bold", fill=modern_color)

    # 2. TABLA CON SÍMBOLOS
    for r_idx, row in enumerate(SYMBOLS):
        r = r_idx + 1
        builder.text(str(r), Point(start_x - 25, start_y + r_idx*box + box/2 + 4), font_size=18, font_weight="900", fill="#94a3b8")
        
        for c_idx, symbol in enumerate(row):
            c = c_idx + 1
            if not symbol: continue
            
            b_type = get_block(r, c)
            is_transition = b_type == 'd'
            
            x, y = start_x + c_idx*box, start_y + r_idx*box
            fill = BLOCK_COLORS[b_type]
            stroke = BLOCK_COLORS[b_type+'_stroke'] if not is_transition else "#e2e8f0"
            op = 1.0 if not is_transition else 0.25
            
            builder.rect(x, y, box-gap, box-gap, fill=fill, stroke=stroke, stroke_width=2 if not is_transition else 0.8, rx=8, fill_opacity=op)
            
            sym_color = "#1e293b" if not is_transition else "#cbd5e1"
            builder.text(symbol, Point(x + (box-gap)/2, y + (box-gap)/2 + 6), font_size=16, font_weight="900", fill=sym_color)

    # 3. LEYENDA (Inferior)
    legend_y = start_y + 7*box + 60
    active_blocks = [('Bloque s (Familia IA e IIA)', 's'), ('Bloque p (Familia IIIA a VIIIA)', 'p')]
    item_w = 320
    total_legend_w = len(active_blocks) * item_w
    start_lx = (canvas_width - total_legend_w) / 2
    
    for i, (label, key) in enumerate(active_blocks):
        lx = start_lx + i * item_w
        builder.rect(lx, legend_y, 25, 25, fill=BLOCK_COLORS[key], stroke=BLOCK_COLORS[key+'_stroke'], stroke_width=2, rx=6)
        builder.text(label, Point(lx + 35, legend_y + 16), font_size=18, font_weight="bold", fill="#1e293b", anchor="start")

def main():
    width, height = 1100, 650
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text("Elementos Representativos (Familia A)", Point(width/2, 50), font_size=36, font_weight="900", fill="#1e293b")
    
    draw_centered_family_bridge(builder, width, 140)
    
    output_path = Path("public/images/quimica/config-electronica/bloques/puente-nomenclatura-tradicional.svg")
    output_path.write_text(builder.build(), encoding="utf-8")
    print(f"✅ {output_path.name} corregido (Centrado y Grande)")

if __name__ == "__main__":
    main()

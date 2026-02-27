#!/usr/bin/env python3
"""
TABLE BLOCKS PREMIUM RENDERER - V2
- Incluye leyendas descriptivas para los bloques.
- tabla-bloques-completa.svg
- tabla-bloques-representativos.svg
- tabla-bloques-transicion.svg
- tabla-maestra-bloques.svg
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

BLOCK_COLORS = {
    's': '#fef3c7', # Amarillo pastel
    's_stroke': '#f59e0b',
    'p': '#e0f2fe', # Azul pastel
    'p_stroke': '#0ea5e9',
    'd': '#fee2e2', # Rojo pastel
    'd_stroke': '#ef4444',
    'f': '#f0fdf4', # Verde pastel
    'f_stroke': '#22c55e',
    'neutral': '#f8fafc',
    'neutral_stroke': '#cbd5e1'
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

SYMBOLS_F = [
    ["Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
    ["Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]
]

def get_block(r, c):
    if c <= 2: return 's'
    if c >= 13: return 'p'
    if r == 1 and c == 18: return 's'
    return 'd'

def draw_blocks_table(builder, start_x, start_y, highlights=None, show_f=True):
    box = 42
    gap = 4
    
    # 1. Tabla Principal
    for r_idx, row in enumerate(SYMBOLS):
        r = r_idx + 1
        builder.text(str(r), Point(start_x - 20, start_y + r_idx*box + box/2), font_size=14, font_weight="bold", fill="#94a3b8")
        for c_idx, symbol in enumerate(row):
            c = c_idx + 1
            if not symbol: continue
            
            b_type = get_block(r, c)
            is_high = highlights is None or b_type in highlights
            
            x, y = start_x + c_idx*box, start_y + r_idx*box
            fill = BLOCK_COLORS[b_type] if is_high else BLOCK_COLORS['neutral']
            stroke = BLOCK_COLORS[b_type+'_stroke'] if is_high else BLOCK_COLORS['neutral_stroke']
            op = 1.0 if is_high else 0.2
            
            builder.rect(x, y, box-gap, box-gap, fill=fill, stroke=stroke, stroke_width=2 if is_high else 0.5, rx=6, fill_opacity=op)
            if is_high:
                builder.text(symbol, Point(x + (box-gap)/2, y + (box-gap)/2 + 5), font_size=12, font_weight="900", fill="#1e293b")

    # 2. Bloque F
    last_y = start_y + 7*box
    if show_f:
        f_start_x = start_x + 2*box
        f_start_y = start_y + 7*box + 40
        is_high_f = highlights is None or 'f' in highlights
        
        for r_idx, row in enumerate(SYMBOLS_F):
            for c_idx, symbol in enumerate(row):
                x, y = f_start_x + c_idx*box, f_start_y + r_idx*box
                fill = BLOCK_COLORS['f'] if is_high_f else BLOCK_COLORS['neutral']
                stroke = BLOCK_COLORS['f_stroke'] if is_high_f else BLOCK_COLORS['neutral_stroke']
                op = 1.0 if is_high_f else 0.2
                
                builder.rect(x, y, box-gap, box-gap, fill=fill, stroke=stroke, stroke_width=2 if is_high_f else 0.5, rx=6, fill_opacity=op)
                if is_high_f:
                    builder.text(symbol, Point(x + (box-gap)/2, y + (box-gap)/2 + 5), font_size=12, font_weight="900", fill="#1e293b")
        last_y = f_start_y + 2*box

    # 3. Leyenda (Inferior)
    legend_y = last_y + 40
    blocks = [
        ('Bloque s', 's'),
        ('Bloque p', 'p'),
        ('Bloque d', 'd'),
        ('Bloque f', 'f')
    ]
    
    # Filtrar leyenda según highlights si no es la completa
    if highlights:
        active_blocks = [b for b in blocks if b[1] in highlights]
    else:
        active_blocks = blocks
        
    item_w = 160
    total_legend_w = len(active_blocks) * item_w
    start_lx = (900 - total_legend_w) / 2
    
    for i, (label, key) in enumerate(active_blocks):
        lx = start_lx + i * item_w
        builder.rect(lx, legend_y, 20, 20, fill=BLOCK_COLORS[key], stroke=BLOCK_COLORS[key+'_stroke'], stroke_width=2, rx=4)
        builder.text(label, Point(lx + 28, legend_y + 12), font_size=16, font_weight="bold", fill="#1e293b", anchor="start")

def render_block_image(title, highlights, filename, show_f=True):
    # Ajustar altura según si hay leyenda y bloque f
    height = 750 if show_f else 550
    width = 900
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(title, Point(width/2, 45), font_size=28, font_weight="900", fill="#1e293b")
    draw_blocks_table(builder, 60, 100, highlights, show_f)
    
    out_dir = Path("public/images/quimica/config-electronica/bloques")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / filename).write_text(builder.build(), encoding="utf-8")
    print(f"✅ {filename} generado con leyenda")

def main():
    render_block_image("Los 4 Bloques de la Tabla Periódica", None, "tabla-bloques-completa.svg")
    render_block_image("Elementos Representativos (Bloques s y p)", ['s', 'p'], "tabla-bloques-representativos.svg", show_f=False)
    render_block_image("Elementos de Transición (Bloques d y f)", ['d', 'f'], "tabla-bloques-transicion.svg")
    render_block_image("Guía Maestra de Bloques Electrónicos", None, "tabla-maestra-bloques.svg")

if __name__ == "__main__":
    main()

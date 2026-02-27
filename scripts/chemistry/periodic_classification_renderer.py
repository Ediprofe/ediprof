#!/usr/bin/env python3
"""
PERIODIC TABLE CLASSIFICATION RENDERER - V2
- Incluye símbolos de los elementos.
- Estilo panorámico Premium.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

CLASS_COLORS = {
    'metal': '#e0f2fe',      # Azul muy claro
    'metal_stroke': '#0ea5e9',
    'metalloid': '#fef3c7',  # Amarillo/Dorado claro
    'metalloid_stroke': '#f59e0b',
    'nonmetal': '#dcfce7',   # Verde claro
    'nonmetal_stroke': '#22c55e',
    'text': '#1e293b'
}

# Símbolos por filas (1-7)
SYMBOLS = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
]

def get_element_type(r, c):
    if r == 1 and c == 1: return 'nonmetal' # H
    if c >= 17: return 'nonmetal' # Halógenos y Nobles
    if r == 2 and c >= 14: return 'nonmetal'
    if r == 3 and c >= 15: return 'nonmetal'
    if r == 4 and c >= 16: return 'nonmetal'
    
    metalloids = [(2, 13), (3, 14), (4, 14), (4, 15), (5, 15), (5, 16), (6, 16)]
    if (r, c) in metalloids: return 'metalloid'
    
    return 'metal'

def draw_classification_table(builder, start_x, start_y):
    box = 48
    gap = 4
    
    for r_idx, row in enumerate(SYMBOLS):
        r = r_idx + 1
        builder.text(str(r), Point(start_x - 25, start_y + r_idx*box + box/2), font_size=16, font_weight="900", fill="#94a3b8")
        
        for c_idx, symbol in enumerate(row):
            c = c_idx + 1
            if not symbol and not ( (r==1 and (c==1 or c==18)) or (r in [2,3] and (c<=2 or c>=13)) or r>=4 ):
                continue
            if not symbol: continue # Salto de huecos
            
            el_type = get_element_type(r, c)
            x, y = start_x + c_idx*box, start_y + r_idx*box
            
            builder.rect(x, y, box-gap, box-gap, fill=CLASS_COLORS[el_type], stroke=CLASS_COLORS[el_type + '_stroke'], stroke_width=1.5, rx=8)
            
            # Símbolo
            builder.text(symbol, Point(x + (box-gap)/2, y + (box-gap)/2 + 5), font_size=14, font_weight="900", fill=CLASS_COLORS['text'])

    legend_y = start_y + 7*box + 50
    classes = [('Metales', 'metal'), ('Metaloides', 'metalloid'), ('No Metales', 'nonmetal')]
    item_w = 200
    start_lx = (1000 - len(classes)*item_w)/2 + 50
    for i, (label, key) in enumerate(classes):
        lx = start_lx + i * item_w
        builder.rect(lx, legend_y, 25, 25, fill=CLASS_COLORS[key], stroke=CLASS_COLORS[key+'_stroke'], stroke_width=2, rx=6)
        builder.text(label, Point(lx + 35, legend_y + 15), font_size=18, font_weight="bold", fill=CLASS_COLORS['text'], anchor="start")

def main():
    width, height = 1000, 600
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text("Clasificación General de los Elementos", Point(width/2, 50), font_size=32, font_weight="900", fill="#1e293b")
    draw_classification_table(builder, 60, 120)
    output_path = Path("public/images/quimica/config-electronica/bloques/clasificacion-metales-no-metales.svg")
    output_path.write_text(builder.build(), encoding="utf-8")
    print(f"✅ {output_path.name} actualizado con símbolos")

if __name__ == "__main__":
    main()

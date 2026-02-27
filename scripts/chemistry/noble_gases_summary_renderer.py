#!/usr/bin/env python3
"""
NOBLE GASES SUMMARY RENDERER - V3 (FULL WIDTH & OCTET FOCUS)
- Tabla periódica ocupando todo el ancho.
- Tarjeta de "Regla del Octeto" en la parte inferior.
- Símbolos y triple notación integrados.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

BLOCK_COLORS = {
    's': '#fef3c7', # Amarillo pastel
    'p': '#e0f2fe', # Azul pastel
    'd': '#fee2e2', # Rojo pastel
    'noble': '#2563eb', # Azul intenso
    'stroke_noble': '#1e3a8a'
}

def draw_wide_periodic_table(builder, start_x, start_y):
    box = 48 # Aumentado para ocupar más ancho
    gap = 4
    
    # 1. Triple Notación de Grupos (Solo representativos para no saturar)
    groups_to_label = {1: "IA", 2: "IIA", 13: "IIIA", 14: "IVA", 15: "VA", 16: "VIA", 17: "VIIA", 18: "VIIIA"}
    for c, label in groups_to_label.items():
        tx = start_x + (c-1)*box + (box-gap)/2
        
        # Terminación (Arriba)
        term = "s¹" if c==1 else "s²" if c==2 else f"p{c-12}⁶" if c==18 else f"p{c-12}"
        if c == 18: term = "p⁶"
        elif c > 12: term = f"p{c-12}"
        
        builder.text(term, Point(tx, start_y - 55), font_size=14, font_weight="900", fill="#2563eb" if c==18 else "#64748b")
        builder.text(label, Point(tx, start_y - 35), font_size=12, font_weight="900", fill="#1e293b")
        builder.text(str(c), Point(tx, start_y - 15), font_size=10, font_weight="bold", fill="#94a3b8")

    # 2. Celdas
    noble_symbols = {1: "He", 2: "Ne", 3: "Ar", 4: "Kr", 5: "Xe", 6: "Rn"}
    
    for r in range(1, 8):
        # Etiqueta de periodo
        builder.text(str(r), Point(start_x - 25, start_y + (r-1)*box + box/2), font_size=16, font_weight="900", fill="#94a3b8")
        
        for c in range(1, 19):
            exists = True
            if r == 1 and 1 < c < 18: exists = False
            if (r == 2 or r == 3) and 2 < c < 13: exists = False
            if not exists: continue
            
            is_noble = (c == 18)
            x, y = start_x + (c-1)*box, start_y + (r-1)*box
            
            if is_noble:
                fill = BLOCK_COLORS['noble']
                stroke = BLOCK_COLORS['stroke_noble']
                width = 3.5
            else:
                if c <= 2: b_type = 's'
                elif 3 <= c <= 12: b_type = 'd'
                else: b_type = 'p'
                fill = BLOCK_COLORS[b_type]
                stroke = "#cbd5e1"
                width = 0.8
            
            builder.rect(x, y, box-gap, box-gap, fill=fill, stroke=stroke, stroke_width=width, rx=8, fill_opacity=1.0 if is_noble else 0.4)
            
            if is_noble and r in noble_symbols:
                builder.text(noble_symbols[r], Point(x + (box-gap)/2, y + (box-gap)/2 + 5), 
                            font_size=16, font_weight="900", fill="white")

def main():
    width, height = 1000, 650 # Más alto para la tarjeta inferior
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título Principal
    builder.text("Gases Nobles: El Modelo de Estabilidad", Point(width/2, 45), font_size=32, font_weight="900", fill="#1e293b")
    
    # Tabla Periódica
    draw_wide_periodic_table(builder, 55, 130)
    
    # 3. Tarjeta Inferior: REGLA DEL OCTETO (Centrada)
    card_w, card_h = 600, 100
    card_x = (width - card_w) / 2
    card_y = 510
    
    builder.rect(card_x, card_y, card_w, card_h, fill="#eff6ff", stroke="#2563eb", stroke_width=2.5, rx=15)
    
    builder.text("REGLA DEL OCTETO", Point(width/2, card_y + 35), font_size=28, font_weight="900", fill="#2563eb")
    builder.text("Los átomos buscan tener 8 electrones en su capa de valencia para ser estables.", 
                Point(width/2, card_y + 70), font_size=16, font_weight="bold", fill="#1e40af")

    output_path = Path("public/images/quimica/config-electronica/bloques/gases-nobles-meta-estabilidad.svg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(builder.build(), encoding="utf-8")
    print(f"✅ {output_path.name} actualizado (V3 - Octeto Focus)")

if __name__ == "__main__":
    main()

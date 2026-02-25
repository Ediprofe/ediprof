#!/usr/bin/env python3
"""
TABLE BLOCKS RENDERER - V6.5 (CENTRE & POLISH)
- Centrado horizontal automático de la tabla.
- Ejes de filas dinámicos: n para representativos, (n-1)d y (n-2)f para transición.
- Altura de canvas dinámica según contenido.
- Etiquetas d1-d10 y f1-f14 pegadas a los bloques.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

BLOCK_COLORS = {
    's': '#fbbf24',
    'p': '#3b82f6',
    'd': '#ef4444',
    'f': '#84cc16',
    'neutral': '#f1f5f9',
    'stroke_neutral': '#cbd5e1',
    'label_dark': '#1e293b'
}

def get_sup(n):
    sups = {'1':'¹', '2':'²', '3':'³', '4':'⁴', '5':'⁵', '6':'⁶', '7':'⁷', '8':'⁸', '9':'⁹', '0':'⁰'}
    return "".join(sups.get(c, c) for c in str(n))

def draw_table_v6(builder, box_size, gap, canvas_width, highlight_types=None, show_logic=None, show_block_names=False):
    # Calcular ancho total de la tabla (18 columnas) para centrar
    table_width = 18 * box_size + 17 * gap
    # start_x centrado, pero considerando que hay etiquetas a la izquierda (~30px)
    start_x = (canvas_width - table_width) / 2 + 10 
    start_y = 140
    
    # --- 1. CABECERAS (X-AXIS) ---
    def draw_term(label, col_idx, color, y_offset=0):
        tx = start_x + col_idx * (box_size + gap) + box_size/2
        base = label[0]
        sup = get_sup(label[1:])
        ty = start_y - 20 + y_offset
        builder.text(base, Point(tx - 3, ty), font_size=18, font_weight="bold", fill=color, anchor="end")
        builder.text(sup, Point(tx - 1, ty - 7), font_size=14, font_weight="900", fill=color, anchor="start")

    # Mostrar términos s1, s2, p1-p6
    if show_logic in ['rep', 'master', 'none']:
        color_s = BLOCK_COLORS['s'] if (highlight_types is None or 's' in highlight_types) else BLOCK_COLORS['stroke_neutral']
        color_p = BLOCK_COLORS['p'] if (highlight_types is None or 'p' in highlight_types) else BLOCK_COLORS['stroke_neutral']
        for c in [1, 2]: draw_term(f"s{c}", c-1, color_s)
        for c in range(1, 7): draw_term(f"p{c}", c+11, color_p)
    
    # Mostrar términos d1-d10
    if show_logic in ['trans', 'master', 'none']:
        color_d = BLOCK_COLORS['d'] if (highlight_types is None or 'd' in highlight_types) else BLOCK_COLORS['stroke_neutral']
        y_off = 3 * (box_size + gap) if show_logic == 'trans' else 0
        for c in range(1, 11): draw_term(f"d{c}", c+1, color_d, y_offset=y_off)

    # --- 2. CELDAS Y NIVELES (Y-AXIS) ---
    for r in range(1, 8):
        ly = start_y + (r-1)*(box_size+gap) + box_size/2 + 4
        
        # Lógica de etiquetas de fila (izquierda)
        if show_logic == 'trans':
            if r >= 4:
                builder.text(f"{r-1}d", Point(start_x - 15, ly), font_size=18, font_weight="900", fill=BLOCK_COLORS['d'], anchor="end")
        elif show_logic in ['rep', 'master', 'none']:
            builder.text(str(r), Point(start_x - 25, ly), font_size=18, font_weight="bold", fill="#64748b", anchor="end")

        # Dibujar celdas
        for c in range(1, 19):
            exists = True
            if r == 1 and 1 < c < 18: exists = False
            if (r == 2 or r == 3) and 2 < c < 13: exists = False
            if not exists: continue

            b_type = 's'
            if c <= 2: b_type = 's'
            elif 3 <= c <= 12: b_type = 'd'
            elif 13 <= c <= 18: b_type = 'p'
            if r == 1 and c == 18: b_type = 's'

            is_high = highlight_types is None or b_type in highlight_types
            x, y = start_x + (c-1) * (box_size + gap), start_y + (r-1) * (box_size + gap)
            
            fill_color = BLOCK_COLORS[b_type] if is_high else BLOCK_COLORS['neutral']
            stroke_color = "black" if is_high else BLOCK_COLORS['stroke_neutral']
            
            builder.rect(x, y, box_size, box_size, fill=fill_color, stroke=stroke_color, stroke_width=1.2, rx=4)

    # --- 3. BLOQUE F ---
    show_f = show_logic in ['trans', 'master', 'none']
    if show_f:
        f_y = start_y + 7 * (box_size + gap) + 70
        is_high_f = highlight_types is None or 'f' in highlight_types
        
        # Centrar bloque f respecto a la tabla principal (14 cols vs 18 cols)
        f_start_x = start_x + 2 * (box_size + gap)
        
        for r in range(1, 3):
            f_level = "4f" if r == 1 else "5f"
            builder.text(f_level, Point(f_start_x - 15, f_y + (r-1)*(box_size+gap) + box_size/2 + 4), 
                        font_size=18, font_weight="900", fill=BLOCK_COLORS['f'] if is_high_f else BLOCK_COLORS['stroke_neutral'], anchor="end")
            
            for c in range(1, 15):
                x, y = f_start_x + (c-1) * (box_size + gap), f_y + (r-1) * (box_size + gap)
                
                fill_color = BLOCK_COLORS['f'] if is_high_f else BLOCK_COLORS['neutral']
                stroke_color = "black" if is_high_f else BLOCK_COLORS['stroke_neutral']
                
                builder.rect(x, y, box_size, box_size, fill=fill_color, stroke=stroke_color, stroke_width=1.2, rx=4)
                
                if r == 1:
                    tx = x + box_size/2
                    color_f_text = BLOCK_COLORS['f'] if is_high_f else BLOCK_COLORS['stroke_neutral']
                    builder.text("f", Point(tx - 3, f_y - 15), font_size=14, font_weight="bold", fill=color_f_text, anchor="end")
                    builder.text(get_sup(c), Point(tx - 1, f_y - 22), font_size=11, font_weight="900", fill=color_f_text, anchor="start")

    # --- 4. NOMBRES DE BLOQUE ---
    if show_block_names:
        builder.text("BLOQUE s", Point(start_x + box_size, start_y - 45), font_size=20, font_weight="900", fill=BLOCK_COLORS['s'])
        builder.text("BLOQUE p", Point(start_x + 15.5*(box_size+gap), start_y - 45), font_size=20, font_weight="900", fill=BLOCK_COLORS['p'])
        builder.text("BLOQUE d", Point(start_x + 7.5*(box_size+gap), start_y + 1.5*(box_size+gap)), font_size=20, font_weight="900", fill=BLOCK_COLORS['d'])
        if show_f:
            builder.text("BLOQUE f (Transición Interna)", Point(canvas_width/2, f_y + 2.5*(box_size+gap) + 25), 
                        font_size=20, font_weight="900", fill=BLOCK_COLORS['f'], anchor="middle")

def render_v6(title, highlight, logic, filename, show_names=False):
    has_f = logic in ['trans', 'master', 'none']
    width, height = 1050, 850 if has_f else 550
    
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(title, Point(width/2, 45), font_size=32, font_weight="bold", fill=COLORS['text'])
    
    draw_table_v6(builder, 38, 4, width, highlight, logic, show_names)
    
    output_dir = Path("public/images/quimica/config-electronica/bloques")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / filename).write_text(builder.build(), encoding="utf-8")
    print(f"✅ {filename} generado (V6.5)")

def main():
    render_v6("Los 4 Bloques de la Tabla Periódica", None, 'none', "tabla-bloques-completa.svg", show_names=True)
    render_v6("Bloques s y p (Representativos)", ['s', 'p'], 'rep', "tabla-bloques-representativos.svg")
    render_v6("Bloques d y f (Transición)", ['d', 'f'], 'trans', "tabla-bloques-transicion.svg")
    render_v6("Guía Maestra de Configuraciones", None, 'master', "tabla-maestra-bloques.svg")

if __name__ == "__main__":
    main()

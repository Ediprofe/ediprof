#!/usr/bin/env python3
"""
GAS NOBLE RENDERER - V10 (EDICIÓN MAGISTRAL - LÁSER FRIENDLY)
- Fuentes masivas para legibilidad con puntero láser.
- Mapa de tabla periódica expandido.
- Proceso de procedimiento con máxima claridad.
"""

import math
import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

GN_COLORS = {
    'gas_noble': '#f59e0b',
    'gn_light': '#fef3c7',
    'electron_ext': '#3b82f6',
    'gain': '#22c55e',
    'loss': '#ef4444',
    'arrow': '#94a3b8',
    'table_bg': '#ffffff',
    'label': '#64748b',
    'highlight_ion': '#dcfce7',
    'loss_bg': '#fee2e2'
}

def get_col_x_factor(col):
    if col == 'd': return 2.5
    if isinstance(col, int):
        if col <= 2: return col - 1
        if col >= 13: return (col - 13) + 4.0
    return 2.5

def render_map(data):
    width, height = 1000, 380
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    builder.text(f"Ubicación: {data['name']} ({data['symbol']})", Point(width/2, 45), font_size=32, font_weight="bold", fill=COLORS['text'])
    
    box_size, gap = 52, 8 # Aumentado significativamente
    total_table_width = 9.5 * (box_size + gap)
    start_x = (width - total_table_width) / 2 + 30
    pos = Point(start_x, 130)
    el_pos, gn_pos = data['table_pos'], data['gn_table_pos']
    terminations = {1: 's¹', 2: 's²', 13: 'p¹', 14: 'p²', 15: 'p³', 16: 'p⁴', 17: 'p⁵', 18: 'p⁶'}
    
    for col in [1, 2, 13, 14, 15, 16, 17, 18]:
        lx = pos.x + get_col_x_factor(col) * (box_size + gap) + box_size/2
        builder.text(terminations[col], Point(lx, pos.y - 20), font_size=16, font_weight="900", fill=GN_COLORS['label'])
    
    display_cols = [1, 2, 'd', 13, 14, 15, 16, 17, 18]
    for r in range(1, 6):
        builder.text(f"n={r}", Point(pos.x - 25, pos.y + (r-1)*(box_size+gap) + box_size/2), font_size=12, font_weight="bold", fill=GN_COLORS['label'], anchor="end")
        for c in display_cols:
            if r == 1 and c != 1 and c != 18: continue
            if (r == 2 or r == 3) and c == 'd': continue
            x, y = pos.x + get_col_x_factor(c) * (box_size + gap), pos.y + (r-1) * (box_size + gap)
            is_gn, is_el = (c == 18), (r == el_pos[0] and c == el_pos[1]) or (c == 'd' and 2 < el_pos[1] < 13 and r == el_pos[0])
            fill = GN_COLORS['gn_light'] if is_gn else (COLORS['fill_blue_light'] if is_el else "#fff")
            stroke = GN_COLORS['gas_noble'] if is_gn else (COLORS['primary'] if is_el else COLORS['grid'])
            builder.rect(x, y, box_size, box_size, fill=fill, stroke=stroke, stroke_width=2, rx=5)
            if is_el: builder.text(data['symbol'], Point(x + box_size/2, y + box_size/2 + 6), font_size=22, font_weight="bold")
            elif is_gn:
                gn_names = {1: 'He', 2: 'Ne', 3: 'Ar', 4: 'Kr', 5: 'Xe'}
                builder.text(gn_names.get(r, ''), Point(x + box_size/2, y + box_size/2 + 6), font_size=18, font_weight="bold", fill=GN_COLORS['gas_noble'])
    
    p_el_x = pos.x + get_col_x_factor(el_pos[1]) * (box_size + gap) + box_size/2
    p_el_y = pos.y + (el_pos[0]-1) * (box_size + gap) + box_size/2
    p_gn_x = pos.x + get_col_x_factor(gn_pos[1]) * (box_size + gap) + box_size/2
    p_gn_y = pos.y + (gn_pos[0]-1) * (box_size + gap) + box_size/2
    path = f"M {p_el_x} {p_el_y} Q {(p_el_x + p_gn_x)/2} {min(p_el_y, p_gn_y)-70} {p_gn_x} {p_gn_y}"
    builder.path(path, stroke=GN_COLORS['gas_noble'], stroke_width=4, fill="none")
    builder.circle(Point(p_gn_x, p_gn_y), 6, fill=GN_COLORS['gas_noble'])
    return builder.build()

def render_process(data):
    width, height = 1000, 520
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    sym, charge = data['symbol'], data.get('charge', "")
    el_id = f"{sym}{charge}"
    builder.text(f"Transformación: {data['name']}", Point(width/2, 45), font_size=32, font_weight="bold", fill=COLORS['text'])
    
    px, py, box_w, box_h = 40, 100, 920, 380
    builder.rect(px, py, box_w, box_h, fill="#fff", stroke=COLORS['grid'], rx=15)
    
    gn_sym = data['gn_symbol']
    if not data.get('is_ion'):
        c_int, c_ext = data['config_internal'], data['config_external']
        gn_full = data.get('gn_config_full', c_int)
        steps = [
            {"label": "A) Configuración completa", "val": f"{el_id} =", "parts": [(c_int, GN_COLORS['gas_noble'], True), (c_ext, COLORS['text'], False)]},
            {"label": f"B) Equivalencia de [{gn_sym}]", "val": f"[{gn_sym}] =", "parts": [(gn_full, GN_COLORS['gas_noble'], False)]},
            {"label": "C) Notación Abreviada", "val": f"{el_id} =", "parts": [(f"[{gn_sym}]", GN_COLORS['gas_noble'], True), (c_ext, COLORS['text'], False)], "is_final": True}
        ]
    else:
        c_neutra, c_ion = data['config_neutral_full'], data['config_ion_full']
        change_text, parts_i = data['change_text'], c_ion.split(' ')
        change_color = GN_COLORS['loss'] if 'Pierde' in change_text else GN_COLORS['gain']
        change_bg = GN_COLORS['loss_bg'] if 'Pierde' in change_text else GN_COLORS['highlight_ion']
        steps = [
            {"label": "A) Átomo Neutro", "val": f"{sym} =", "parts": [(c_neutra, COLORS['text'], False)]},
            {"label": f"B) {change_text}", "val": f"{el_id} =", "parts": [(" ".join(parts_i[:-1]), COLORS['text'], False), (parts_i[-1], change_color, True, change_bg)]},
            {"label": "C) Identidad Gas Noble", "val": f"{el_id} =", "parts": [(c_ion, change_color, False), ("=", COLORS['text_light'], False), (f"[{gn_sym}]", GN_COLORS['gas_noble'], True)]},
            {"label": "D) Resultado final", "val": f"{el_id} =", "parts": [(f"[{gn_sym}]", GN_COLORS['gas_noble'], True)], "is_final": True}
        ]
    
    curr_y, step_gap = py + 70, 80 if data.get('is_ion') else 110
    for i, step in enumerate(steps):
        builder.text(step['label'], Point(px + 30, curr_y), font_size=16, font_weight="bold", fill=COLORS['text_light'], anchor="start")
        config_x = px + 280
        builder.text(step['val'], Point(config_x, curr_y), font_size=28, font_weight="bold", fill=COLORS['text'], anchor="end")
        
        current_part_x = config_x + 20
        for p_data in step['parts']:
            val, color, is_boxed, *bg = p_data
            txt_size, font_w = (42 if step.get('is_final') else 32), ("900" if is_boxed else "bold")
            tw = len(val) * (txt_size * 0.6)
            if is_boxed:
                builder.rect(current_part_x - 8, curr_y - txt_size*0.85, tw + 16, txt_size*1.4, fill=bg[0] if bg else GN_COLORS['gn_light'], stroke=color, stroke_width=2.5, rx=8)
            builder.text(val, Point(current_part_x + tw/2, curr_y), font_size=txt_size, font_weight=font_w, fill=color)
            current_part_x += tw + 30
        if i < len(steps)-1: builder.arrow(Point(px + 230, curr_y + 15), Point(px + 230, curr_y + step_gap - 25), stroke=GN_COLORS['arrow'], stroke_width=2)
        curr_y += step_gap
    return builder.build()

def main():
    output_dir = Path("public/images/quimica/config-electronica/ejercicios")
    output_dir.mkdir(parents=True, exist_ok=True)
    exercises = [
        {"name": "Oxígeno", "symbol": "O", "z_real": 8, "table_pos": (2, 16), "gn_symbol": "He", "gn_z": 2, "gn_table_pos": (1, 18), "config_internal": "1s²", "config_external": "2s² 2p⁴", "filename": "o-gas-noble"},
        {"name": "Aluminio", "symbol": "Al", "z_real": 13, "table_pos": (3, 13), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_internal": "1s² 2s² 2p⁶", "config_external": "3s² 3p¹", "filename": "al-gas-noble"},
        {"name": "Azufre", "symbol": "S", "z_real": 16, "table_pos": (3, 16), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_internal": "1s² 2s² 2p⁶", "config_external": "3s² 3p⁴", "filename": "s-gas-noble"},
        {"name": "Hierro", "symbol": "Fe", "z_real": 26, "table_pos": (4, 8), "gn_symbol": "Ar", "gn_z": 18, "gn_table_pos": (3, 18), "config_internal": "1s²... 3p⁶", "config_external": "4s² 3d⁶", "filename": "fe-gas-noble"},
        {"name": "Rubidio", "symbol": "Rb", "z_real": 37, "table_pos": (5, 1), "gn_symbol": "Kr", "gn_z": 36, "gn_table_pos": (4, 18), "config_internal": "1s²... 4p⁶", "config_external": "5s¹", "filename": "rb-gas-noble"},
        {"name": "Fluoruro", "symbol": "F", "z_real": 9, "is_ion": True, "charge": "⁻", "change_text": "Gana 1e⁻", "table_pos": (2, 17), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_neutral_full": "1s² 2s² 2p⁵", "config_ion_full": "1s² 2s² 2p⁶", "filename": "f-ion-gas-noble"},
        {"name": "Sulfuro", "symbol": "S", "z_real": 16, "is_ion": True, "charge": "²⁻", "change_text": "Gana 2e⁻", "table_pos": (3, 16), "gn_symbol": "Ar", "gn_z": 18, "gn_table_pos": (3, 18), "config_neutral_full": "1s² 2s² 2p⁶ 3s² 3p⁴", "config_ion_full": "1s² 2s² 2p⁶ 3s² 3p⁶", "filename": "s-ion-gas-noble"},
        {"name": "Nitruro", "symbol": "N", "z_real": 7, "is_ion": True, "charge": "³⁻", "change_text": "Gana 3e⁻", "table_pos": (2, 15), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_neutral_full": "1s² 2s² 2p³", "config_ion_full": "1s² 2s² 2p⁶", "filename": "n-ion-gas-noble"},
        {"name": "Sodio", "symbol": "Na", "z_real": 11, "is_ion": True, "charge": "⁺", "change_text": "Pierde 1e⁻", "table_pos": (3, 1), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_neutral_full": "1s² 2s² 2p⁶ 3s¹", "config_ion_full": "1s² 2s² 2p⁶", "filename": "na-ion-gas-noble"},
        {"name": "Calcio", "symbol": "Ca", "z_real": 20, "is_ion": True, "charge": "²⁺", "change_text": "Pierde 2e⁻", "table_pos": (4, 2), "gn_symbol": "Ar", "gn_z": 18, "gn_table_pos": (3, 18), "config_neutral_full": "1s²... 3p⁶ 4s²", "config_ion_full": "1s²... 3p⁶", "filename": "ca-ion-gas-noble"},
        # PRÁCTICA
        {"name": "Carbono", "symbol": "C", "z_real": 6, "table_pos": (2, 14), "gn_symbol": "He", "gn_z": 2, "gn_table_pos": (1, 18), "config_internal": "1s²", "config_external": "2s² 2p²", "filename": "c-gas-noble-prac"},
        {"name": "Fósforo", "symbol": "P", "z_real": 15, "table_pos": (3, 15), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_internal": "1s²... 2p⁶", "config_external": "3s² 3p³", "filename": "p-gas-noble-prac"},
        {"name": "Cloro", "symbol": "Cl", "z_real": 17, "table_pos": (3, 17), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_internal": "1s²... 2p⁶", "config_external": "3s² 3p⁵", "filename": "cl-gas-noble-prac"},
        {"name": "Escandio", "symbol": "Sc", "z_real": 21, "table_pos": (4, 3), "gn_symbol": "Ar", "gn_z": 18, "gn_table_pos": (3, 18), "config_internal": "1s²... 3p⁶", "config_external": "4s² 3d¹", "filename": "sc-gas-noble-prac"},
        {"name": "Estroncio", "symbol": "Sr", "z_real": 38, "table_pos": (5, 2), "gn_symbol": "Kr", "gn_z": 36, "gn_table_pos": (4, 18), "config_internal": "1s²... 4p⁶", "config_external": "5s²", "filename": "sr-gas-noble-prac"},
        {"name": "Bromuro", "symbol": "Br", "z_real": 35, "is_ion": True, "charge": "⁻", "change_text": "Gana 1e⁻", "table_pos": (4, 17), "gn_symbol": "Kr", "gn_z": 36, "gn_table_pos": (4, 18), "config_neutral_full": "1s²... 4p⁵", "config_ion_full": "1s²... 4p⁶", "filename": "br-ion-gas-noble-prac"},
        {"name": "Aluminio", "symbol": "Al", "z_real": 13, "is_ion": True, "charge": "³⁺", "change_text": "Pierde 3e⁻", "table_pos": (3, 13), "gn_symbol": "Ne", "gn_z": 10, "gn_table_pos": (2, 18), "config_neutral_full": "1s²... 3p¹", "config_ion_full": "1s² 2s² 2p⁶", "filename": "al-ion-gas-noble-prac"},
        {"name": "Zinc", "symbol": "Zn", "z_real": 30, "table_pos": (4, 12), "gn_symbol": "Ar", "gn_z": 18, "gn_table_pos": (3, 18), "config_internal": "1s²... 3p⁶", "config_external": "4s² 3d¹⁰", "filename": "zn-gas-noble-prac"},
        {"name": "Litio", "symbol": "Li", "z_real": 3, "is_ion": True, "charge": "⁺", "change_text": "Pierde 1e⁻", "table_pos": (2, 1), "gn_symbol": "He", "gn_z": 2, "gn_table_pos": (1, 18), "config_neutral_full": "1s² 2s¹", "config_ion_full": "1s²", "filename": "li-ion-gas-noble-prac"},
        {"name": "Cobre", "symbol": "Cu", "z_real": 29, "table_pos": (4, 11), "gn_symbol": "Ar", "gn_z": 18, "gn_table_pos": (3, 18), "config_internal": "1s²... 3p⁶", "config_external": "4s¹ 3d¹⁰", "filename": "cu-gas-noble-prac"}
    ]
    for ex in exercises:
        (output_dir / f"{ex['filename']}-map.svg").write_text(render_map(ex), encoding="utf-8")
        (output_dir / f"{ex['filename']}-proc.svg").write_text(render_process(ex), encoding="utf-8")
        print(f"✅ Set Dual Magistral generado para {ex['name']}")

if __name__ == "__main__":
    main()

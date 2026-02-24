#!/usr/bin/env python3
"""
CONFIGURACION EJEMPLOS RENDERER - V4 (COHERENCIA VISUAL TOTAL)
- Superíndices reales para iones.
- Electrones coloreados según su subnivel (s, p, d, f).
- Layout profesional y didáctico.
"""

import math
import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

# Colores de orbitales (fuente única de verdad para toda la imagen)
ORBITAL_COLORS = {
    's': '#fbbf24', # Amarillo
    'p': '#3b82f6', # Azul
    'd': '#ef4444', # Rojo
    'f': '#84cc16'  # Verde
}

def get_electron_coords(cx, cy, r, count):
    coords = []
    if count <= 0: return coords
    start_angle = -math.pi / 2
    angle_step = (2 * math.pi) / count
    for i in range(count):
        angle = start_angle + i * angle_step
        coords.append(Point(cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return coords

def draw_large_moeller(builder, start_point, active_sublevels):
    box_size = 36
    gap = 8
    sublevel_types = ['s', 'p', 'd', 'f']
    max_n = 5
    pos_map = {}
    
    for n in range(1, max_n + 1):
        for t_idx, t in enumerate(sublevel_types):
            if (n == 1 and t_idx > 0) or (n == 2 and t_idx > 1) or (n == 3 and t_idx > 2):
                continue
            
            label = f"{n}{t}"
            is_active = label in active_sublevels
            x = start_point.x + t_idx * (box_size + gap)
            y = start_point.y + (n-1) * (box_size + gap)
            
            color = ORBITAL_COLORS[t]
            opacity = 1.0 if is_active else 0.15
            
            stroke = "black" if is_active else "none"
            builder.rect(x, y, box_size, box_size, fill=color, fill_opacity=opacity, 
                        stroke=stroke, stroke_width=1.5, rx=4)
            
            text_color = "black" if is_active else "#94a3b8"
            builder.text(label, Point(x + box_size/2, y + box_size/2 + 5), 
                        font_size=16, font_weight="900", fill=text_color, anchor="middle")
            pos_map[label] = Point(x + box_size/2, y + box_size/2)

    diagonals = [
        ['1s'], ['2s'], ['2p', '3s'], ['3p', '4s'], ['3d', '4p', '5s'],
    ]
    
    for diag in diagonals:
        diag_active = any(item in active_sublevels for item in diag)
        arrow_color = COLORS['primary'] if diag_active else "#cbd5e1"
        available = [item for item in diag if item in pos_map]
        if not available: continue
        first = pos_map[available[0]]
        last = pos_map[available[-1]]
        p_start = Point(first.x + box_size*0.7, first.y - box_size*0.7)
        p_end = Point(last.x - box_size*0.7, last.y + box_size*0.7)
        
        if diag_active:
            builder.arrow(p_start, p_end, stroke=arrow_color, stroke_width=2.5)
        else:
            builder.line(p_start, p_end, stroke=arrow_color, stroke_width=1, dashed=True)

def render_config_atom(data):
    width, height = 850, 580
    builder = SVGBuilder(width, height)
    
    name = data['name']
    symbol = data['symbol']
    z = data['z']
    electrons_total = data.get('electrons_total', z)
    # detailed_distribution: list of list of (sublevel_type, count) per level
    # e.g. [ [('s', 2)], [('s', 2), ('p', 6)] ]
    detailed_dist = data['detailed_distribution']
    config = data['config']
    active_sublevels = data['active_sublevels']
    is_ion = data.get('is_ion', False)
    charge = data.get('charge', "")

    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    nucleus_color = COLORS['secondary'] if not is_ion else COLORS['purple']
    grad_id = f"grad-nucleus-{symbol.lower()}-{z}"
    builder.defs.append(f"""
        <radialGradient id="{grad_id}" cx="30%" cy="30%" r="70%">
            <stop offset="0%" stop-color="white" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="{nucleus_color}" stop-opacity="0.2"/>
        </radialGradient>
    """)

    # 1. Título con superíndice real
    title_y = 50
    if is_ion and charge:
        # Dibujar partes por separado para control total
        # Estimamos anchos
        main_text = f"{name} ({symbol}"
        builder.text(main_text, Point(width/2 - 15, title_y), font_size=32, font_weight="bold", fill=COLORS['text'], anchor="end")
        # Superíndice
        builder.text(charge, Point(width/2 - 12, title_y - 12), font_size=20, font_weight="bold", fill=COLORS['text'], anchor="start")
        # Cierre paréntesis
        builder.text(")", Point(width/2 + 5, title_y), font_size=32, font_weight="bold", fill=COLORS['text'], anchor="start")
    else:
        builder.text(f"{name} ({symbol})", Point(width/2, title_y), font_size=32, font_weight="bold", fill=COLORS['text'], anchor="middle")
    
    builder.text(f"Z = {z} | {electrons_total} electrones", 
                Point(width/2, 85), font_size=18, font_weight="bold", fill=COLORS['text_light'], anchor="middle")

    # 2. Bohr Model (Izquierda)
    cx, cy = 250, height / 2 + 10
    center = Point(cx, cy)
    
    num_levels = len(detailed_dist)
    base_r = 60
    step = 45
    if num_levels > 3:
        step = 35
        base_r = 55
    
    orbit_color = "#e2e8f0"
    for i, level_sublevels in enumerate(detailed_dist):
        r = base_r + i * step
        builder.circle(center, r, fill="none", stroke=orbit_color, stroke_width=2)
        
        # Recolectar todos los electrones de este nivel para distribuirlos uniformemente
        level_electrons = []
        for s_type, count in level_sublevels:
            level_electrons.extend([s_type] * count)
        
        total_in_level = len(level_electrons)
        e_positions = get_electron_coords(cx, cy, r, total_in_level)
        
        for pos, s_type in zip(e_positions, level_electrons):
            e_color = ORBITAL_COLORS[s_type]
            # Glow con el color del subnivel
            builder.circle(pos, 8, fill=e_color, fill_opacity=0.3)
            # Cuerpo
            builder.circle(pos, 6, fill=e_color, stroke="white", stroke_width=1.5)
            # Signo menos
            builder.text("-", Point(pos.x, pos.y + 1), font_size=12, 
                        font_weight="bold", fill="white", anchor="middle")

    # 3. Núcleo con superíndice real
    nucleus_radius = 32
    builder.circle(center, nucleus_radius, fill=f"url(#{grad_id})", stroke=nucleus_color, stroke_width=2.5)
    
    if charge:
        # Símbolo un poco movido a la izquierda para dejar espacio al superíndice
        builder.text(symbol, Point(cx - 5, cy + 10), font_size=24, font_weight="900", fill=nucleus_color, anchor="middle")
        builder.text(charge, Point(cx + 8, cy - 8), font_size=14, font_weight="bold", fill=nucleus_color, anchor="start")
    else:
        builder.text(symbol, Point(cx, cy + 10), font_size=24, font_weight="900", fill=nucleus_color, anchor="middle")

    # 4. Large Moeller (Derecha)
    moeller_start = Point(530, 160)
    builder.text("Regla de las Diagonales", Point(530 + 80, 140), 
                font_size=18, font_weight="bold", fill=COLORS['text_light'], anchor="middle")
    draw_large_moeller(builder, moeller_start, active_sublevels)

    # 5. Configuración (Abajo)
    builder.formula_box(config, Point(width / 2, height - 45), 
                       font_size=24, bg_color="#eff6ff", text_color=COLORS['primary'], padding=12)

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/config-electronica/ejercicios")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    exercises = [
        # EJERCICIOS RESUELTOS (YA EN EL TEXTO)
        {"name": "Hidrógeno", "symbol": "H", "z": 1, "detailed_distribution": [[('s', 1)]], "config": "1s¹", "active_sublevels": ["1s"], "filename": "h-configuracion.svg"},
        {"name": "Oxígeno", "symbol": "O", "z": 8, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 4)]], "config": "1s² 2s² 2p⁴", "active_sublevels": ["1s", "2s", "2p"], "filename": "o-configuracion.svg"},
        {"name": "Aluminio", "symbol": "Al", "z": 13, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 1)]], "config": "1s² 2s² 2p⁶ 3s² 3p¹", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "al-configuracion.svg"},
        {"name": "Azufre", "symbol": "S", "z": 16, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 4)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁴", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "s-configuracion.svg"},
        {"name": "Hierro", "symbol": "Fe", "z": 26, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6), ('d', 6)], [('s', 2)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶", "active_sublevels": ["1s", "2s", "2p", "3s", "3p", "4s", "3d"], "filename": "fe-configuracion.svg"},
        {"name": "Ion Sodio", "symbol": "Na", "z": 11, "electrons_total": 10, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶", "is_ion": True, "charge": "+", "active_sublevels": ["1s", "2s", "2p"], "filename": "na-ion-configuracion.svg"},
        {"name": "Ion Calcio", "symbol": "Ca", "z": 20, "electrons_total": 18, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶", "is_ion": True, "charge": "2+", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "ca-ion-configuracion.svg"},
        {"name": "Ion Sulfuro", "symbol": "S", "z": 16, "electrons_total": 18, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶", "is_ion": True, "charge": "2-", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "s-ion-configuracion.svg"},
        {"name": "Ion Nitruro", "symbol": "N", "z": 7, "electrons_total": 10, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶", "is_ion": True, "charge": "3-", "active_sublevels": ["1s", "2s", "2p"], "filename": "n-ion-configuracion.svg"},
        {"name": "Ion Fluoruro", "symbol": "F", "z": 9, "electrons_total": 10, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶", "is_ion": True, "charge": "-", "active_sublevels": ["1s", "2s", "2p"], "filename": "f-ion-configuracion.svg"},
        
        # EJERCICIOS DE PRÁCTICA (PARA LA SECCIÓN FINAL)
        {"name": "Carbono", "symbol": "C", "z": 6, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 2)]], "config": "1s² 2s² 2p²", "active_sublevels": ["1s", "2s", "2p"], "filename": "c-configuracion.svg"},
        {"name": "Magnesio", "symbol": "Mg", "z": 12, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2)]], "config": "1s² 2s² 2p⁶ 3s²", "active_sublevels": ["1s", "2s", "2p", "3s"], "filename": "mg-configuracion.svg"},
        {"name": "Fósforo", "symbol": "P", "z": 15, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 3)]], "config": "1s² 2s² 2p⁶ 3s² 3p³", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "p-configuracion.svg"},
        {"name": "Cloro", "symbol": "Cl", "z": 17, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 5)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁵", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "cl-configuracion.svg"},
        {"name": "Argón", "symbol": "Ar", "z": 18, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "ar-configuracion.svg"},
        {"name": "Potasio", "symbol": "K", "z": 19, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6)], [('s', 1)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", "active_sublevels": ["1s", "2s", "2p", "3s", "3p", "4s"], "filename": "k-configuracion.svg"},
        {"name": "Calcio", "symbol": "Ca", "z": 20, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6)], [('s', 2)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", "active_sublevels": ["1s", "2s", "2p", "3s", "3p", "4s"], "filename": "ca-configuracion.svg"},
        {"name": "Ion Litio", "symbol": "Li", "z": 3, "electrons_total": 2, "detailed_distribution": [[('s', 2)]], "config": "1s²", "is_ion": True, "charge": "+", "active_sublevels": ["1s"], "filename": "li-ion-configuracion.svg"},
        {"name": "Ion Óxido", "symbol": "O", "z": 8, "electrons_total": 10, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶", "is_ion": True, "charge": "2-", "active_sublevels": ["1s", "2s", "2p"], "filename": "o-ion-configuracion.svg"},
        {"name": "Ion Potasio", "symbol": "K", "z": 19, "electrons_total": 18, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶", "is_ion": True, "charge": "+", "active_sublevels": ["1s", "2s", "2p", "3s", "3p"], "filename": "k-ion-configuracion.svg"},
        {"name": "Cobre", "symbol": "Cu", "z": 29, "detailed_distribution": [[('s', 2)], [('s', 2), ('p', 6)], [('s', 2), ('p', 6), ('d', 10)], [('s', 1)]], "config": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰", "active_sublevels": ["1s", "2s", "2p", "3s", "3p", "4s", "3d"], "filename": "cu-configuracion.svg"}
    ]
    
    for ex in exercises:
        svg_content = render_config_atom(ex)
        (output_dir / ex['filename']).write_text(svg_content, encoding="utf-8")
        print(f"✅ {ex['filename']} generado")

if __name__ == "__main__":
    main()

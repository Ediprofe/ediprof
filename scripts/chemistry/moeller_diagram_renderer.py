#!/usr/bin/env python3
"""
MOELLER DIAGRAM RENDERER - REDESIGNED VERSION
Genera un diagrama de Moeller basado en la referencia de cuadrados de colores.
Colores: s=amarillo, p=azul, d=rojo, f=verde.
"""

import sys
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / "geometry"))

from core import COLORS, SVGBuilder, Point

def render_moeller_diagram():
    width, height = 650, 750
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'], rx=12)
    
    # Título
    builder.text("Diagrama de Moeller", Point(width / 2, 45), 
                font_size=28, font_weight="bold", anchor="middle")
    builder.text("(Regla de las Diagonales)", Point(width / 2, 75), 
                font_size=16, fill=COLORS['text_light'], anchor="middle")
    
    # Configuración de colores (según referencia)
    ref_colors = {
        's': '#fbbf24', # Amarillo
        'p': '#3b82f6', # Azul
        'd': '#ef4444', # Rojo
        'f': '#84cc16'  # Verde manzana
    }
    
    # Layout
    start_x = 100
    start_y = 130
    box_size = 70
    gap = 15
    
    orbital_types = ['s', 'p', 'd', 'f']
    orbitals_per_level = [1, 2, 3, 4, 4, 4, 4] # s, p, d, f
    
    sublevel_pos = {}
    
    # 1. Dibujar Cuadrados
    for n in range(1, 8): # Niveles 1-7
        for t_idx, t in enumerate(orbital_types):
            if t_idx < orbitals_per_level[n-1]:
                cx = start_x + t_idx * (box_size + gap)
                cy = start_y + (n-1) * (box_size + gap)
                
                # Cuadrado de color
                builder.rect(cx, cy, box_size, box_size, fill=ref_colors[t], stroke="none", rx=0)
                
                # Texto (ej: 1s) - Grande y Negro
                builder.text(f"{n}{t}", Point(cx + box_size/2, cy + box_size/2 + 8), 
                            font_size=32, font_weight="900", fill="black", anchor="middle")
                
                # Almacenar centro para las flechas
                sublevel_pos[(n, t)] = Point(cx + box_size/2, cy + box_size/2)

    # 2. Dibujar Flechas Diagonales (Estilo referencia)
    diagonals = [
        [(1, 's')],
        [(2, 's')],
        [(2, 'p'), (3, 's')],
        [(3, 'p'), (4, 's')],
        [(3, 'd'), (4, 'p'), (5, 's')],
        [(4, 'd'), (5, 'p'), (6, 's')],
        [(4, 'f'), (5, 'd'), (6, 'p'), (7, 's')],
        [(5, 'f'), (6, 'd'), (7, 'p')],
        [(6, 'f'), (7, 'd')],
        [(7, 'f')]
    ]
    
    arrow_color = "#94a3b8" # Gris suave para las flechas de guía
    
    for diag in diagonals:
        first = sublevel_pos[diag[0]]
        last = sublevel_pos[diag[-1]]
        
        # Offset para que la flecha empiece fuera del cuadro superior-derecha
        # y termine fuera del cuadro inferior-izquierda
        offset = box_size * 0.8
        
        # En este diagrama, las diagonales van de derecha-arriba a izquierda-abajo
        # Calculamos la dirección unitaria de la diagonal (siempre es la misma pendiente)
        
        p_start = Point(first.x + offset, first.y - offset)
        p_end = Point(last.x - offset, last.y + offset)
        
        builder.arrow(p_start, p_end, stroke=arrow_color, stroke_width=3)

    # 3. Orden de Llenado (Footer)
    builder.rect(50, 700, 550, 35, fill="#1e293b", rx=6)
    builder.text("Orden: 1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s ...", 
                Point(width/2, 723), font_size=14, font_weight="bold", fill="white", anchor="middle")

    return builder.build()

def main():
    output_dir = Path("public/images/quimica/config-electronica")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = "diagrama-moeller.svg"
    (output_dir / filename).write_text(render_moeller_diagram(), encoding="utf-8")
    print(f"✅ {filename} actualizado con nuevo diseño de referencia")

if __name__ == "__main__":
    main()

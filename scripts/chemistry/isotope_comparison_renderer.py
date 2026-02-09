
"""
⚖️ Isotope Comparison Renderer - Genera comparativa visual entre dos isótopos
"""

import json
import argparse
import sys
import math
from pathlib import Path

# Importar core y el renderer de átomos existente
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))
sys.path.insert(0, str(Path(__file__).parent))

from core import COLORS
from core.primitives import escape_xml
from atom_renderer import pack_nucleus, distribute_electrons, polar_to_cartesian

def render_comparison(spec: Path, output: Path):
    # Dummies for C-12 and C-13/14 based on the request "Carbono"
    # We will hardcode the comparison logic for now to ensure it looks exactly as requested (Analogy)
    
    width = 800
    height = 700
    
    colors = COLORS
    
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="{colors["background"]}" rx="12"/>')
    
    # Título Principal
    svg_parts.append(f'<text x="{width/2}" y="40" font-family="Inter, sans-serif" font-size="24" font-weight="bold" fill="{colors["text"]}" text-anchor="middle">Isótopos: "Gemelos" con Diferente Peso</text>')
    
    # Coordenada Y de los átomos (Bajamos un poco para dar espacio arriba si crecen)
    cy = 280
    
    # --- Átomo 1: Carbono-12 (El delgado) ---
    cx1 = 200
    draw_atom_group(svg_parts, cx1, cy, protons=6, neutrons=6, title="Carbono-12", subtitle="El 'Gemelo' Ligero", highlight_extras=False)
    
    # --- Átomo 2: Carbono-14 (El que comió más) ---
    cx2 = 600
    draw_atom_group(svg_parts, cx2, cy, protons=6, neutrons=8, title="Carbono-14", subtitle="El 'Gemelo' Pesado", highlight_extras=True)
    
    # --- Elementos de la Analogía ---
    
    # 1. Flecha de igualdad en Z
    # Bajamos la flecha visualmente debajo de los átomos que ahora son más grandes
    arrow_y = cy + 180
    svg_parts.append(f'<path d="M {cx1} {arrow_y} L {cx2} {arrow_y}" stroke="{colors["text_light"]}" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrow)"/>')
    svg_parts.append(f'<text x="{width/2}" y="{arrow_y-5}" font-family="Inter, sans-serif" font-size="14" fill="{colors["primary"]}" font-weight="bold" text-anchor="middle">Mismo Z (6 Protones)</text>')
    svg_parts.append(f'<text x="{width/2}" y="{arrow_y+15}" font-family="Inter, sans-serif" font-size="12" fill="{colors["text_light"]}" text-anchor="middle">(Mismo ADN / Identidad)</text>')

    # 2. Balanza esquemática (Visualizando el peso)
    
    # Pivote (Bajamos pivote)
    piv_x, piv_y = width/2, 550
    svg_parts.append(f'<path d="M {piv_x} {piv_y} L {piv_x-20} {piv_y+40} L {piv_x+20} {piv_y+40} Z" fill="{colors["text"]}"/>')
    
    # Barra inclinada
    angle = 10 * (math.pi / 180) # 10 grados de inclinación
    bar_len = 250
    y_drop = math.sin(angle) * bar_len
    x_span = math.cos(angle) * bar_len
    
    left_x, left_y = piv_x - x_span, piv_y - y_drop
    right_x, right_y = piv_x + x_span, piv_y + y_drop
    
    svg_parts.append(f'<line x1="{left_x}" y1="{left_y}" x2="{right_x}" y2="{right_y}" stroke="{colors["text"]}" stroke-width="6" stroke-linecap="round"/>')
    
    # Platos
    svg_parts.append(f'<line x1="{left_x}" y1="{left_y}" x2="{left_x}" y2="{left_y+30}" stroke="{colors["text_light"]}" stroke-width="2"/>')
    svg_parts.append(f'<ellipse cx="{left_x}" cy="{left_y+35}" rx="30" ry="10" fill="{colors["fill_blue_light"]}" stroke="{colors["primary"]}" stroke-width="2"/>')
    
    svg_parts.append(f'<line x1="{right_x}" y1="{right_y}" x2="{right_x}" y2="{right_y+30}" stroke="{colors["text_light"]}" stroke-width="2"/>')
    svg_parts.append(f'<ellipse cx="{right_x}" cy="{right_y+35}" rx="30" ry="10" fill="{colors["fill_red_light"]}" stroke="{colors["accent"]}" stroke-width="2"/>')
    
    # Etiquetas de peso
    svg_parts.append(f'<text x="{left_x}" y="{left_y+60}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{colors["primary"]}" text-anchor="middle">Masa = 12</text>')
    svg_parts.append(f'<text x="{right_x}" y="{right_y+60}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{colors["accent"]}" text-anchor="middle">Masa = 14</text>')
    
    # Annotación "Comió más"
    svg_parts.append(f'<text x="{right_x + 60}" y="{right_y}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{colors["accent"]}" text-anchor="start">¡Comió más!</text>')
    svg_parts.append(f'<text x="{right_x + 60}" y="{right_y+15}" font-family="Inter, sans-serif" font-size="12" fill="{colors["text_light"]}" text-anchor="start">(+2 Neutrones)</text>')
    
    svg_parts.append('</svg>')
    
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(svg_parts), encoding='utf-8')
    print(f"✅ Comparación generada: {output}")

def draw_atom_group(svg_parts, cx, cy, protons, neutrons, title, subtitle, highlight_extras=False):
    colors = COLORS
    
    # Títulos - Subimos más para dar espacio a órbitas grandes
    svg_parts.append(f'<text x="{cx}" y="{cy-160}" font-family="Inter, sans-serif" font-size="18" font-weight="bold" fill="{colors["text"]}" text-anchor="middle">{title}</text>')
    svg_parts.append(f'<text x="{cx}" y="{cy-140}" font-family="Inter, sans-serif" font-size="12" fill="{colors["text_light"]}" text-anchor="middle">{subtitle}</text>')

    # Órbitas (Aumentadas aún más para separar del núcleo)
    # Antes 80 y 110 -> Ahora 100 y 130
    radius_1 = 100
    radius_2 = 130
    
    # Órbitas (Estilo más notorio)
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius_1}" fill="none" stroke="{colors["grid"]}" stroke-width="2.5" stroke-dasharray="0" opacity="0.8"/>')
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius_2}" fill="none" stroke="{colors["grid"]}" stroke-width="2.5" stroke-dasharray="0" opacity="0.8"/>')
    
    # Electrones (6)
    # Inner 2 (radius 100)
    svg_parts.append(f'<circle cx="{cx}" cy="{cy-radius_1}" r="6" fill="{colors["primary"]}" stroke="white" stroke-width="1.5"/>')
    svg_parts.append(f'<circle cx="{cx}" cy="{cy+radius_1}" r="6" fill="{colors["primary"]}" stroke="white" stroke-width="1.5"/>')
    # Outer 4 (radius 130)
    for angle in [45, 135, 225, 315]:
        rad = angle * (math.pi / 180)
        ex = cx + radius_2 * math.cos(rad)
        ey = cy + radius_2 * math.sin(rad)
        svg_parts.append(f'<circle cx="{ex}" cy="{ey}" r="6" fill="{colors["primary"]}" stroke="white" stroke-width="1.5"/>')
        
    # Núcleo (Fondo distintivo que encierra a todos)
    nucleons = pack_nucleus(protons, neutrons, particle_radius=8)
    
    # Calcular radio necesario para cubrir todas las partículas
    max_dist = 0
    if nucleons:
        max_dist = max(math.sqrt(p['x']**2 + p['y']**2) for p in nucleons)
    
    # Radio del fondo = distancia más lejana + radio de partícula + padding
    nucleus_bg_radius = max_dist + 8 + 6 
    
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{nucleus_bg_radius}" fill="#fdf4ff" stroke="{colors["purple"]}" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.8"/>')
        
    # Núcleo
    nucleons = pack_nucleus(protons, neutrons, particle_radius=8)
    
    # Si highlight_extras es True, coloreamos los últimos (neutrones extra) de forma distinta
    extra_count = 2 if highlight_extras else 0
    # The last ones packed logic in pack_nucleus might not place them nicely at the edge, but let's try.
    # Actually pack_nucleus mixes them. Let's just draw them.
    
    # Identificar cuáles son los neutrones "extra" para resaltarlos.
    # El C-14 tiene 8 neutrones. El C-12 tiene 6. Los 2 extra los pintaremos de "Comida" (Highlight).
    
    neutron_indices = [i for i, p in enumerate(nucleons) if p['type'] != 'p']
    extra_neutron_indices = neutron_indices[-extra_count:] if extra_count > 0 else []
    
    svg_parts.append(f'<g transform="translate({cx},{cy})">')
    for i, p in enumerate(nucleons):
        r = 8
        is_extra = i in extra_neutron_indices
        
        if p['type'] == 'p':
            fill = colors['accent']
            label = "+"
        else:
            if is_extra:
                fill = colors['highlight'] # Naranja para la "Comida" extra
                label = ""
            else:
                fill = colors['text_light']
                label = ""
                
        svg_parts.append(f'<circle cx="{p["x"]}" cy="{p["y"]}" r="{r}" fill="{fill}" stroke="white" stroke-width="1"/>')
        
        if label:
            svg_parts.append(f'<text x="{p["x"]}" y="{p["y"]+2.5}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">{label}</text>')
            
    svg_parts.append('</g>')
    
    # Si hay extras, ya los hemos coloreado en el bucle anterior.
    # El usuario pidió quitar la etiqueta y flecha explicativa.
    pass

if __name__ == '__main__':
    render_comparison(Path("dummy"), Path("public/images/quimica/isotopos/comparacion-gemelos.svg"))

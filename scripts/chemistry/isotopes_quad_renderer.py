
"""
⚛️ Isotopes Quad Renderer - Genera comparativa de 4 átomos (isótopos) side-by-side
"""

import math
import sys
from pathlib import Path

# Agregar paths para importar core y atom_renderer
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))
sys.path.insert(0, str(Path(__file__).parent))

from core import COLORS
from core.primitives import escape_xml
from atom_renderer import pack_nucleus, distribute_electrons

def render_quad_isotopes(output_path: Path):
    width = 1000
    height = 450
    
    # Configuración de los 4 átomos
    atoms_data = [
        {"id": "1", "p": 5, "n": 5, "e": 5},
        {"id": "2", "p": 5, "n": 6, "e": 5},
        {"id": "3", "p": 6, "n": 6, "e": 6},
        {"id": "4", "p": 6, "n": 7, "e": 6},
    ]
    
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    
    # Fondo
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>')
    
    # Espaciado
    margin_x = 100
    spacing_x = (width - 2 * margin_x) / 3
    cy = 200
    
    # Colores específicos para coincidir con la imagen y leyenda
    color_proton = "#ffffff"
    color_neutron = "#94a3b8" # Gris (auxiliary)
    color_electron = "#1e293b" # Oscuro (text)
    color_stroke = "#1e293b"
    
    for i, data in enumerate(atoms_data):
        cx = margin_x + i * spacing_x
        
        # Etiqueta de número de átomo
        svg_parts.append(f'<text x="{cx}" y="40" font-family="Inter, sans-serif" font-size="22" font-weight="bold" fill="{color_electron}" text-anchor="middle">{data["id"]}</text>')
        
        # Dibujar Órbitas
        orbit_radii = [65, 95]
        for r in orbit_radii:
            svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["grid"]}" stroke-width="1.5"/>')
        
        # Dibujar Electrones
        shells = distribute_electrons(data["e"])
        for s_idx, shell in enumerate(shells):
            r = orbit_radii[s_idx]
            count = shell['count']
            angle_step = (2 * math.pi) / count
            start_angle = -math.pi / 2
            
            for e_idx in range(count):
                theta = start_angle + e_idx * angle_step
                ex = cx + r * math.cos(theta)
                ey = cy + r * math.sin(theta)
                svg_parts.append(f'<circle cx="{ex}" cy="{ey}" r="4.5" fill="{color_electron}" stroke="white" stroke-width="0.5"/>')
        
        # Dibujar Núcleo
        # Fondo del núcleo (sutil)
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="35" fill="white" fill-opacity="0.3" stroke="{COLORS["grid"]}" stroke-dasharray="3,2"/>')
        
        nucleons = pack_nucleus(data["p"], data["n"], particle_radius=6)
        # Dibujar nucleones con sombra para efecto 3D simple (orden: atrás hacia adelante)
        # pack_nucleus ya da un orden de espiral que funciona bien
        for p in nucleons:
            fill = color_proton if p['type'] == 'p' else color_neutron
            svg_parts.append(f'<circle cx="{cx + p["x"]}" cy="{cy + p["y"]}" r="6.5" fill="{fill}" stroke="{color_stroke}" stroke-width="0.8"/>')

    # Leyenda (Abajo)
    legend_y = 380
    legend_items = [
        {"label": "Protones", "color": color_proton},
        {"label": "Neutrones", "color": color_neutron},
        {"label": "Electrones", "color": color_electron},
    ]
    
    legend_start_x = width / 2 - 150
    for i, item in enumerate(legend_items):
        lx = legend_start_x + i * 120
        svg_parts.append(f'<circle cx="{lx}" cy="{legend_y}" r="8" fill="{item["color"]}" stroke="{color_stroke}" stroke-width="1"/>')
        svg_parts.append(f'<text x="{lx + 15}" y="{legend_y + 6}" font-family="Inter, sans-serif" font-size="16" fill="{COLORS["text"]}" text-anchor="start">{item["label"]}</text>')

    svg_parts.append('</svg>')
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(svg_parts), encoding='utf-8')
    print(f"✅ Ilustración de isótopos generada: {output_path}")

if __name__ == '__main__':
    render_quad_isotopes(Path("public/images/saber/quimica/modelos-atomicos-isotopos.svg"))

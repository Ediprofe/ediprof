
#!/usr/bin/env python3
"""
Renderizador para la Masa de Partículas (uma)
Comparación visual tipo Balanza y Tabla Visual.
"""
import argparse
import sys
import math
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))

from core import COLORS
from core.primitives import escape_xml

def render_particle_mass(output: Path):
    width = 750
    height = 600
    
    colors = COLORS
    
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="{colors["background"]}" rx="12"/>')
    
    # Título
    svg_parts.append(f'<text x="{width/2}" y="50" font-family="Inter, sans-serif" font-size="28" font-weight="900" fill="{colors["text"]}" text-anchor="middle">Peso Atómico: Los Pesados vs. Los Ligeros</text>')
    
    # Layout de 3 Columnas
    col_width = width / 3
    base_y = 100
    
    # --- Columna 1: Protón ---
    cx1 = col_width * 0.5
    draw_particle_card(svg_parts, cx1, base_y, 'p', "Protón", "1 uma", "Fundamental", colors['accent'])
    
    # --- Columna 2: Neutrón ---
    cx2 = col_width * 1.5
    draw_particle_card(svg_parts, cx2, base_y, 'n', "Neutrón", "1 uma", "Fundamental", '#64748b') # Slate
    
    # --- Columna 3: Electrón ---
    cx3 = col_width * 2.5
    draw_particle_card(svg_parts, cx3, base_y, 'e', "Electrón", "~0 uma", "Despreciable", colors['primary'])
    
    # --- Parte Inferior: La Balanza Analogía ---
    draw_balance_scale(svg_parts, width/2, 420, width)
    
    svg_parts.append('</svg>')
    
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(svg_parts), encoding='utf-8')
    print(f"✅ Ilustración de Masas generada: {output}")

def draw_particle_card(svg_parts, cx, y, p_type, name, mass, role, color):
    # Caja de fondo sutil
    box_w = 220
    box_h = 240
    box_x = cx - box_w/2
    
    svg_parts.append(f'<rect x="{box_x}" y="{y}" width="{box_w}" height="{box_h}" rx="16" fill="white" stroke="{COLORS["grid"]}" stroke-width="1"/>')
    
    # Título
    svg_parts.append(f'<text x="{cx}" y="{y+40}" font-family="Inter, sans-serif" font-size="22" font-weight="bold" fill="{color}" text-anchor="middle">{name}</text>')
    
    # Ilustración de la partícula
    # Si es electrón es pequeñito. Si es P/N es grande.
    center_y = y + 100
    if p_type == 'e':
        r = 6
        svg_parts.append(f'<circle cx="{cx}" cy="{center_y}" r="{r}" fill="{color}" stroke="white" stroke-width="1.5"/>')
        svg_parts.append(f'<path d="M {cx-2} {center_y} L {cx+2} {center_y}" stroke="white" stroke-width="1.5" stroke-linecap="round"/>')
        # Símbolo de "pluma" o aire alrededor para denotar ligereza
        # Unas lines de movimiento/flotación
        svg_parts.append(f'<path d="M {cx-15} {center_y+10} Q {cx} {center_y+20} {cx+15} {center_y+5}" fill="none" stroke="{COLORS["text_light"]}" stroke-width="1" stroke-dasharray="2,2"/>')
    else:
        r = 35
        svg_parts.append(f'<circle cx="{cx}" cy="{center_y}" r="{r}" fill="{color}" stroke="white" stroke-width="2"/>')
        label = "+" if p_type == 'p' else ""
        if label:
            svg_parts.append(f'<text x="{cx}" y="{center_y+10}" font-family="Inter, sans-serif" font-size="30" font-weight="bold" fill="white" text-anchor="middle">{label}</text>')
        
        # Símbolo de "pesa" abajo
        # Un iconito simple de pesa
        # Rectangulo gris
        wd = 40
        ht = 15
        svg_parts.append(f'<rect x="{cx-wd/2}" y="{center_y+45}" width="{wd}" height="{ht}" fill="#94a3b8" rx="2"/>')
        svg_parts.append(f'<rect x="{cx-5}" y="{center_y+45-5}" width="10" height="5" fill="#94a3b8"/>')

    # Masa (Grande)
    svg_parts.append(f'<text x="{cx}" y="{y+180}" font-family="Inter, sans-serif" font-size="28" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">{mass}</text>')
    
    # Rol (Pequeño)
    svg_parts.append(f'<text x="{cx}" y="{y+210}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["text_light"]}" text-anchor="middle">{role}</text>')

def draw_balance_scale(svg_parts, cx, cy, width):
    # Dibujar una balanza abajo.
    # Izquierda: 1 Protón. Derecha: 1 Electrón
    # El lado del protón está hundido (pesado). El lado del electrón está arriba.
    
    piv_x = cx
    piv_y = cy
    
    # Base triangular
    svg_parts.append(f'<path d="M {piv_x} {piv_y} L {piv_x-15} {piv_y+30} L {piv_x+15} {piv_y+30} Z" fill="{COLORS["text"]}"/>')
    svg_parts.append(f'<line x1="{piv_x}" y1="{piv_y+30}" x2="{piv_x}" y2="{piv_y+50}" stroke="{COLORS["text"]}" stroke-width="2"/>') # soporte
    svg_parts.append(f'<line x1="{piv_x-40}" y1="{piv_y+50}" x2="{piv_x+40}" y2="{piv_y+50}" stroke="{COLORS["text"]}" stroke-width="2"/>') # base suelo
    
    # Barra Inclinada (Izquierda abajo)
    angle = 15 * (math.pi / 180)
    bar_len = 200
    dx = bar_len * math.cos(angle)
    dy = bar_len * math.sin(angle)
    
    left_x, left_y = piv_x - dx, piv_y + dy # Abajo
    right_x, right_y = piv_x + dx, piv_y - dy # Arriba
    
    svg_parts.append(f'<line x1="{left_x}" y1="{left_y}" x2="{right_x}" y2="{right_y}" stroke="{COLORS["text"]}" stroke-width="4" stroke-linecap="round"/>')
    
    # Platos y Cadenas
    def draw_plate(px, py, content_type):
        # Cadena
        svg_parts.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+40}" stroke="{COLORS["text_light"]}" stroke-width="1.5"/>')
        # Plato
        plat_y = py + 40
        svg_parts.append(f'<path d="M {px-25} {plat_y} Q {px} {plat_y+15} {px+25} {plat_y}" fill="none" stroke="{COLORS["text"]}" stroke-width="2"/>')
        
        # Contenido
        item_y = plat_y - 5 
        if content_type == 'p':
            # Protón
            svg_parts.append(f'<circle cx="{px}" cy="{item_y-10}" r="12" fill="{COLORS["accent"]}" stroke="white" stroke-width="1"/>')
            svg_parts.append(f'<text x="{px}" y="{item_y-6}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="white" text-anchor="middle">+</text>')
            # Etiqueta "Pesado"
            svg_parts.append(f'<text x="{px-35}" y="{item_y+10}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{COLORS["accent"]}" text-anchor="end">1 uma</text>')
        else:
            # Electrón
            svg_parts.append(f'<circle cx="{px}" cy="{item_y-5}" r="3" fill="{COLORS["primary"]}" stroke="white" stroke-width="1"/>')
            # Etiqueta "Ligero"
            svg_parts.append(f'<text x="{px+35}" y="{item_y+10}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{COLORS["primary"]}" text-anchor="start">~0 uma</text>')

    draw_plate(left_x, left_y, 'p') # Protón abajo
    draw_plate(right_x, right_y, 'e') # Electrón arriba
    
    # Texto Explicativo Arriba de la balanza
    # svg_parts.append(f'<text x="{cx}" y="{cy-40}" font-family="Inter, sans-serif" font-size="14" fill="{COLORS["text_light"]}" text-anchor="middle">El núcleo aporta casi toda la masa</text>')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    
    render_particle_mass(Path(args.output))

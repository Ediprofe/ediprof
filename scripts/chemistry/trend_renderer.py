#!/usr/bin/env python3
"""
📊 Trend Renderer - Genera SVGs de tendencias periódicas

Uso:
    python3 scripts/chemistry/trend_renderer.py \
        --type radio_atomico \
        --output public/images/quimica/tendencias/radio-atomico.svg

Tipos disponibles:
- radio_atomico: Radio atómico (↓ horizontal, ↑ vertical)
- energia_ionizacion: EI (↑ horizontal, ↓ vertical)
- afinidad_electronica: AE (↑ horizontal, ↓ vertical)
- electronegatividad: EN (↑ horizontal, ↓ vertical)
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))

from core import COLORS
from core.primitives import escape_xml


TRENDS = {
    'radio_atomico': {
        'title': 'Tendencia del Radio Atómico',
        'h_arrow': 'left',  # Disminuye hacia la derecha
        'v_arrow': 'down',  # Aumenta hacia abajo
        'h_label': 'Radio atómico DISMINUYE →',
        'v_label': '↓ Radio AUMENTA',
        'min_label': 'Pequeño (He)',
        'max_label': 'Grande (Cs)',
        'min_pos': (18, 1),
        'max_pos': (1, 4),
        'color_min': '#dcfce7',
        'color_max': '#166534'
    },
    'energia_ionizacion': {
        'title': 'Tendencia de la Energía de Ionización',
        'h_arrow': 'right',  # Aumenta hacia la derecha
        'v_arrow': 'up',     # Disminuye hacia abajo
        'h_label': 'EI AUMENTA →',
        'v_label': '↓ EI DISMINUYE',
        'min_label': 'Baja EI (Cs)',
        'max_label': 'Alta EI (He)',
        'min_pos': (1, 4),
        'max_pos': (18, 1),
        'color_min': '#fef2f2',
        'color_max': '#991b1b'
    },
    'afinidad_electronica': {
        'title': 'Tendencia de la Afinidad Electrónica',
        'h_arrow': 'right',
        'v_arrow': 'up',
        'h_label': 'AE más negativa →',
        'v_label': '↓ AE menos negativa',
        'min_label': 'Baja AE (Cs)',
        'max_label': 'Alta AE (Cl)',
        'min_pos': (1, 4),
        'max_pos': (17, 3),
        'color_min': '#f0fdf4',
        'color_max': '#0d9488'
    },
    'electronegatividad': {
        'title': 'Tendencia de la Electronegatividad',
        'h_arrow': 'right',
        'v_arrow': 'up',
        'h_label': 'EN AUMENTA →',
        'v_label': '↓ EN DISMINUYE',
        'min_label': 'Baja EN (Cs = 0.7)',
        'max_label': 'Alta EN (F = 4.0)',
        'min_pos': (1, 4),
        'max_pos': (17, 2),
        'color_min': '#eff6ff',
        'color_max': '#1d4ed8'
    }
}


def render_trend(trend_type: str) -> str:
    """Genera el SVG de tendencia periódica."""
    trend = TRENDS[trend_type]
    
    # Dimensiones
    padding = 50
    cell_w = 28
    cell_h = 28
    gap = 2
    cols = 18
    rows = 4
    
    width = padding * 2 + cols * (cell_w + gap) - gap
    height = padding * 2 + rows * (cell_h + gap) - gap + 40  # Extra para flechas
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    svg.append(f'  <rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>')
    
    # Título
    svg.append(f'  <text x="{width/2}" y="18" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(trend["title"])}</text>')
    
    # Etiqueta flecha horizontal (arriba)
    svg.append(f'  <text x="{width/2}" y="{padding - 5}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["accent"]}" text-anchor="middle">{escape_xml(trend["h_label"])}</text>')
    
    # Flecha horizontal
    arrow_y = padding - 15
    svg.append(f'  <line x1="{padding + 50}" y1="{arrow_y}" x2="{width - padding - 50}" y2="{arrow_y}" stroke="{COLORS["accent"]}" stroke-width="2"/>')
    svg.append(f'  <polygon points="{width - padding - 50},{arrow_y} {width - padding - 60},{arrow_y - 5} {width - padding - 60},{arrow_y + 5}" fill="{COLORS["accent"]}"/>')
    
    # Etiqueta flecha vertical (izquierda)
    v_label_x = padding - 25
    v_label_y = padding + rows * (cell_h + gap) / 2
    svg.append(f'  <text x="{v_label_x}" y="{v_label_y}" font-family="Inter, sans-serif" font-size="9" fill="{COLORS["secondary"]}" text-anchor="middle" transform="rotate(-90, {v_label_x}, {v_label_y})">{escape_xml(trend["v_label"])}</text>')
    
    # Flecha vertical
    arrow_x = padding - 10
    svg.append(f'  <line x1="{arrow_x}" y1="{padding + 20}" x2="{arrow_x}" y2="{padding + rows * (cell_h + gap) - 30}" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
    svg.append(f'  <polygon points="{arrow_x},{padding + rows * (cell_h + gap) - 30} {arrow_x - 5},{padding + rows * (cell_h + gap) - 40} {arrow_x + 5},{padding + rows * (cell_h + gap) - 40}" fill="{COLORS["secondary"]}"/>')
    
    # Dibujar cuadrícula simplificada con gradiente de color
    for period in range(1, rows + 1):
        for group in range(1, cols + 1):
            # Calcular intensidad de color basada en posición
            # Para radio atómico: más grande abajo-izquierda, más pequeño arriba-derecha
            if trend['h_arrow'] == 'left' and trend['v_arrow'] == 'down':
                intensity = ((group - 1) / (cols - 1) + (1 - (period - 1) / (rows - 1))) / 2
            else:
                intensity = ((1 - (group - 1) / (cols - 1)) + (period - 1) / (rows - 1)) / 2
            
            # Interpolación de color simple
            r1, g1, b1 = int(trend['color_min'][1:3], 16), int(trend['color_min'][3:5], 16), int(trend['color_min'][5:7], 16)
            r2, g2, b2 = int(trend['color_max'][1:3], 16), int(trend['color_max'][3:5], 16), int(trend['color_max'][5:7], 16)
            r = int(r1 + (r2 - r1) * intensity)
            g = int(g1 + (g2 - g1) * intensity)
            b = int(b1 + (b2 - b1) * intensity)
            fill_color = f'#{r:02x}{g:02x}{b:02x}'
            
            x = padding + (group - 1) * (cell_w + gap)
            y = padding + (period - 1) * (cell_h + gap)
            
            # Solo dibujar donde hay elementos (simplificado: grupos principales)
            skip = False
            if period == 1 and group not in [1, 18]:
                skip = True
            if period in [2, 3] and group in range(3, 13):
                skip = True
            
            if not skip:
                svg.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill_color}" stroke="#94a3b8" stroke-width="0.5" rx="3"/>')
    
    # Etiquetas de extremos
    min_x = padding + (trend['min_pos'][0] - 1) * (cell_w + gap) + cell_w / 2
    min_y = padding + rows * (cell_h + gap) + 15
    max_x = padding + (trend['max_pos'][0] - 1) * (cell_w + gap) + cell_w / 2
    max_y = padding - 25
    
    svg.append(f'  <text x="{padding + 10}" y="{height - 10}" font-family="Inter, sans-serif" font-size="8" fill="{COLORS["secondary"]}">{escape_xml(trend["max_label"])}</text>')
    svg.append(f'  <text x="{width - padding - 10}" y="{height - 10}" font-family="Inter, sans-serif" font-size="8" fill="{COLORS["accent"]}" text-anchor="end">{escape_xml(trend["min_label"])}</text>')
    
    svg.append('</svg>')
    return '\n'.join(svg)


def main():
    parser = argparse.ArgumentParser(description='Genera SVG de tendencias periódicas')
    parser.add_argument('--type', required=True, choices=list(TRENDS.keys()), help='Tipo de tendencia')
    parser.add_argument('--output', required=True, help='Ruta de salida para el SVG')
    args = parser.parse_args()
    
    svg_content = render_trend(args.type)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg_content, encoding='utf-8')
    
    print(f"✅ SVG generado: {args.output}")


if __name__ == '__main__':
    main()

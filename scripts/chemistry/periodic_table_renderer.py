#!/usr/bin/env python3
"""
📊 Periodic Table Renderer - Genera tabla periódica SVG desde spec JSON

Uso:
    python3 scripts/chemistry/periodic_table_renderer.py \
        --spec specs/quimica/elementos/tabla-periodica-simple.json \
        --output public/images/quimica/tabla-periodica-simple.svg

Soporta:
- Tabla simple (períodos 1-4)
- Tabla completa (118 elementos con lantánidos y actínidos)

Este renderer sigue los principios del proyecto:
- Spec-First: La IA genera el JSON, Python renderiza
- DRY: Usa colores del módulo core
- Modular: Archivos pequeños y enfocados
"""

import json
import argparse
import sys
from pathlib import Path

# Agregar el directorio de scripts al path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))

from core import COLORS
from core.primitives import escape_xml


def load_spec(spec_path: str) -> dict:
    """Carga y valida el spec JSON."""
    with open(spec_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_periodic_table(spec: dict) -> str:
    """Genera el SVG de la tabla periódica desde el spec."""
    layout = spec['layout']
    elements = spec['elements']
    categories = spec['categories']
    
    cell_w = layout['cell_width']
    cell_h = layout['cell_height']
    gap = layout['gap']
    padding = layout['padding']
    lanthanide_gap = layout.get('lanthanide_gap', 15)
    
    # Detectar si hay lantánidos/actínidos
    has_series = any(e.get('series') for e in elements)
    
    # Calcular dimensiones del canvas
    total_width = padding * 2 + layout['columns'] * (cell_w + gap) - gap
    
    # Altura base: 7 períodos + título + leyenda
    main_rows = layout['rows']
    extra_height = 30  # Título
    
    if has_series:
        # Añadir espacio para 2 filas de series (lantánidos + actínidos) + gap
        series_height = lanthanide_gap + 2 * (cell_h + gap)
        legend_height = 50
    else:
        series_height = 0
        legend_height = 80
    
    total_height = padding * 2 + main_rows * (cell_h + gap) - gap + extra_height + series_height + legend_height
    
    # Iniciar SVG
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width} {total_height}">')
    
    # Fondo
    svg_parts.append(f'  <rect width="{total_width}" height="{total_height}" fill="{COLORS["background"]}"/>')
    
    # Título
    title = spec.get('title', 'Tabla Periódica')
    svg_parts.append(f'  <text x="{total_width/2}" y="14" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(title)}</text>')
    
    # Offset vertical para el contenido (después del título)
    title_offset = 18
    
    # Etiquetas de grupos (1-18)
    for g in range(1, 19):
        x = padding + (g - 1) * (cell_w + gap) + cell_w / 2
        svg_parts.append(f'  <text x="{x}" y="{padding + title_offset - 2}" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="middle">{g}</text>')
    
    # Renderizar elementos principales (no series)
    for elem in elements:
        if elem.get('series'):
            continue  # Los renderizamos después
            
        group = elem['group']
        period = elem['period']
        symbol = elem['symbol']
        z = elem['Z']
        cat = elem['category']
        
        cat_info = categories[cat]
        fill_color = cat_info['fill']
        stroke_color = cat_info['color']
        
        # Calcular posición
        x = padding + (group - 1) * (cell_w + gap)
        y = padding + title_offset + (period - 1) * (cell_h + gap)
        
        # Celda del elemento
        svg_parts.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="1" rx="3"/>')
        
        # Número atómico (pequeño, arriba izquierda)
        svg_parts.append(f'  <text x="{x + 3}" y="{y + 8}" font-family="Inter, sans-serif" font-size="6" fill="{COLORS["text_light"]}">{z}</text>')
        
        # Símbolo (grande, centrado)
        font_size = 10 if len(symbol) <= 2 else 8
        svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h/2 + 3}" font-family="Inter, sans-serif" font-size="{font_size}" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(symbol)}</text>')
    
    # Renderizar series (lantánidos y actínidos) debajo de la tabla principal
    if has_series:
        main_table_bottom = padding + title_offset + main_rows * (cell_h + gap)
        series_start_y = main_table_bottom + lanthanide_gap
        
        # Marcador de series en la tabla principal (grupo 3)
        for period, series_name, label in [(6, 'lanthanide', '57-71'), (7, 'actinide', '89-103')]:
            x = padding + 2 * (cell_w + gap)  # Grupo 3
            y = padding + title_offset + (period - 1) * (cell_h + gap)
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2" rx="3"/>')
            svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h/2 + 2}" font-family="Inter, sans-serif" font-size="6" fill="{COLORS["text_light"]}" text-anchor="middle">{label}</text>')
        
        # Renderizar elementos de series
        for elem in elements:
            if not elem.get('series'):
                continue
            
            series = elem['series']
            pos = elem['series_pos']
            symbol = elem['symbol']
            z = elem['Z']
            cat = elem['category']
            
            cat_info = categories[cat]
            fill_color = cat_info['fill']
            stroke_color = cat_info['color']
            
            # Posición en la fila de series
            x = padding + 2 * (cell_w + gap) + (pos - 1) * (cell_w + gap)  # Empieza en grupo 3
            
            if series == 'lanthanide':
                y = series_start_y
            else:  # actinide
                y = series_start_y + cell_h + gap
            
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="1" rx="3"/>')
            svg_parts.append(f'  <text x="{x + 3}" y="{y + 8}" font-family="Inter, sans-serif" font-size="6" fill="{COLORS["text_light"]}">{z}</text>')
            font_size = 10 if len(symbol) <= 2 else 8
            svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h/2 + 3}" font-family="Inter, sans-serif" font-size="{font_size}" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(symbol)}</text>')
        
        # Etiquetas de series
        label_x = padding
        svg_parts.append(f'  <text x="{label_x + cell_w}" y="{series_start_y + cell_h/2 + 2}" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="end">Lantánidos</text>')
        svg_parts.append(f'  <text x="{label_x + cell_w}" y="{series_start_y + cell_h + gap + cell_h/2 + 2}" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="end">Actínidos</text>')
        
        legend_y = series_start_y + 2 * (cell_h + gap) + 10
    else:
        legend_y = padding + title_offset + main_rows * (cell_h + gap) + 15
    
    # Leyenda
    svg_parts.append(f'  <text x="{total_width/2}" y="{legend_y}" font-family="Inter, sans-serif" font-size="8" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">Categorías</text>')
    
    # Mostrar categorías usadas en la leyenda
    used_categories = []
    seen = set()
    for e in elements:
        cat = e['category']
        if cat not in seen:
            seen.add(cat)
            used_categories.append(cat)
    
    cols = 5
    legend_item_width = (total_width - 2 * padding) / cols
    
    for i, cat_key in enumerate(used_categories):
        cat = categories[cat_key]
        col = i % cols
        row = i // cols
        lx = padding + col * legend_item_width
        ly = legend_y + 12 + row * 14
        
        svg_parts.append(f'  <rect x="{lx}" y="{ly - 6}" width="8" height="8" fill="{cat["fill"]}" stroke="{cat["color"]}" stroke-width="0.5" rx="1"/>')
        svg_parts.append(f'  <text x="{lx + 11}" y="{ly + 1}" font-family="Inter, sans-serif" font-size="6" fill="{COLORS["text"]}">{escape_xml(cat["name"])}</text>')
    
    svg_parts.append('</svg>')
    
    return '\n'.join(svg_parts)


def main():
    parser = argparse.ArgumentParser(description='Genera SVG de tabla periódica desde spec JSON')
    parser.add_argument('--spec', required=True, help='Ruta al archivo spec JSON')
    parser.add_argument('--output', required=True, help='Ruta de salida para el SVG')
    args = parser.parse_args()
    
    # Cargar spec
    spec = load_spec(args.spec)
    
    # Generar SVG
    svg_content = render_periodic_table(spec)
    
    # Guardar
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg_content, encoding='utf-8')
    
    print(f"✅ SVG generado: {args.output}")


if __name__ == '__main__':
    main()

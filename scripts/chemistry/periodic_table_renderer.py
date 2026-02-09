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
    
    # Mapeo de notación moderna a antigua
    old_notation = {
        1: 'IA', 2: 'IIA',
        13: 'IIIA', 14: 'IVA', 15: 'VA', 16: 'VIA', 17: 'VIIA', 18: 'VIIIA',
        3: 'IIIB', 4: 'IVB', 5: 'VB', 6: 'VIB', 7: 'VIIB', 8: 'VIIIB', 9: 'VIIIB', 10: 'VIIIB', 11: 'IB', 12: 'IIB'
    }
    
    # Etiquetas de grupos (1-18) con notación antigua
    for g in range(1, 19):
        x = padding + (g - 1) * (cell_w + gap) + cell_w / 2
        # Número del grupo
        svg_parts.append(f'  <text x="{x}" y="{padding + title_offset - 9}\" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="middle">{g}</text>')
        # Notación antigua (si existe)
        if g in old_notation:
            old_label = old_notation[g]
            svg_parts.append(f'  <text x="{x}" y="{padding + title_offset - 2}\" font-family="Inter, sans-serif" font-size="5.5" fill="{COLORS["text_light"]}" text-anchor="middle">({old_label})</text>')
    
    # Etiquetas de periodos (1-7) en el lado izquierdo
    for p in range(1, main_rows + 1):
        y = padding + title_offset + (p - 1) * (cell_h + gap) + cell_h / 2
        svg_parts.append(f'  <text x="{padding - 8}" y="{y + 3}" font-family="Inter, sans-serif" font-size="9" font-weight="bold" fill="{COLORS["primary"]}" text-anchor="end">{p}</text>')
    
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
        svg_parts.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="1.5" rx="4"/>')
        
        element_name = elem.get('name')
        atomic_mass = elem.get('mass')
        
        # Número atómico
        svg_parts.append(f'  <text x="{x + 4}" y="{y + 10}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="{COLORS["text_light"]}">{z}</text>')
        
        if atomic_mass:
            # Masa atómica (arriba derecha)
            svg_parts.append(f'  <text x="{x + cell_w - 4}" y="{y + 10}" font-family="Inter, sans-serif" font-size="6.5" fill="{COLORS["text_light"]}" text-anchor="end">{atomic_mass}</text>')

        if element_name:
            # Layout con Nombre
            # Símbolo
            font_size_sym = 14 if len(symbol) <= 2 else 12
            svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h * 0.45}" font-family="Inter, sans-serif" font-size="{font_size_sym}" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(symbol)}</text>')
            
            # Nombre (ajustar tamaño si es muy largo)
            font_size_name = 6.5
            if len(element_name) > 10: font_size_name = 5.5
            svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h * 0.82}" font-family="Inter, sans-serif" font-size="{font_size_name}" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(element_name)}</text>')
        else:
            # Layout Original (Solo Símbolo)
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
            
            element_name = elem.get('name')
            atomic_mass = elem.get('mass')
            
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="1.5" rx="4"/>')
            svg_parts.append(f'  <text x="{x + 4}" y="{y + 10}" font-family="Inter, sans-serif" font-size="7" font-weight="bold" fill="{COLORS["text_light"]}">{z}</text>')
            
            if atomic_mass:
                svg_parts.append(f'  <text x="{x + cell_w - 4}" y="{y + 10}" font-family="Inter, sans-serif" font-size="6.5" fill="{COLORS["text_light"]}" text-anchor="end">{atomic_mass}</text>')
            
            if element_name:
                font_size_sym = 14 if len(symbol) <= 2 else 12
                svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h * 0.45}" font-family="Inter, sans-serif" font-size="{font_size_sym}" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(symbol)}</text>')
                
                font_size_name = 6.5
                if len(element_name) > 10: font_size_name = 5.5
                svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h * 0.82}" font-family="Inter, sans-serif" font-size="{font_size_name}" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(element_name)}</text>')
            else:
                font_size = 10 if len(symbol) <= 2 else 8
                svg_parts.append(f'  <text x="{x + cell_w/2}" y="{y + cell_h/2 + 3}" font-family="Inter, sans-serif" font-size="{font_size}" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(symbol)}</text>')
        
        # Etiquetas de series
        label_x = padding
        svg_parts.append(f'  <text x="{label_x + cell_w}" y="{series_start_y + cell_h/2 + 2}" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="end">Lantánidos</text>')
        svg_parts.append(f'  <text x="{label_x + cell_w}" y="{series_start_y + cell_h + gap + cell_h/2 + 2}" font-family="Inter, sans-serif" font-size="7" fill="{COLORS["text_light"]}" text-anchor="end">Actínidos</text>')
        
        legend_y = series_start_y + 2 * (cell_h + gap) + 20
    else:
        legend_y = padding + title_offset + main_rows * (cell_h + gap) + 20
    
    # Leyenda Estilizada y Grande
    legend_title_y = legend_y
    svg_parts.append(f'  <text x="{total_width/2}" y="{legend_title_y}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">Categorías</text>')
    
    # Mostrar categorías usadas en la leyenda
    used_categories = []
    seen = set()
    for e in elements:
        cat = e['category']
        if cat not in seen:
            seen.add(cat)
            used_categories.append(cat)
    
    # Grid de leyenda centrada y grande
    num_cats = len(used_categories)
    legend_item_width = 100
    legend_total_width = num_cats * legend_item_width
    start_x = (total_width - legend_total_width) / 2
    
    for i, cat_key in enumerate(used_categories):
        cat = categories[cat_key]
        lx = start_x + i * legend_item_width + 10
        ly = legend_title_y + 25
        
        # Cuadro de color grande
        svg_parts.append(f'  <rect x="{lx}" y="{ly - 10}" width="20" height="20" fill="{cat["fill"]}" stroke="{cat["color"]}" stroke-width="2" rx="4"/>')
        # Texto grande
        svg_parts.append(f'  <text x="{lx + 30}" y="{ly + 5}" font-family="Inter, sans-serif" font-size="12" font-weight="500" fill="{COLORS["text"]}">{escape_xml(cat["name"])}</text>')
    
    # Añadir extra padding al final
    svg_parts[-1] = svg_parts[-1].replace('</svg>', '') # Remove closing tag from previous append if exists (it's built in list)
    # Actually just set total_height correctly at the start, but we can't easily change it now without re-calculating.
    # The initial calculation included legend_height. Let's trust it fits or is close enough.
    
    svg_parts.append('</svg>')
    
    # Re-calculate height to fit the new larger legend
    final_height = legend_y + 60
    svg_parts[0] = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width} {final_height}">'
    svg_parts[1] = f'  <rect width="{total_width}" height="{final_height}" fill="{COLORS["background"]}"/>'

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

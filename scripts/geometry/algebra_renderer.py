#!/usr/bin/env python3
"""
🧮 Algebra Renderer - Ilustraciones para álgebra y productos notables

Genera SVGs educativos de:
- Cuadrado de un binomio (representación geométrica)
- Diferencia de cuadrados
- Cubo de un binomio
"""

import argparse
import json
import sys
from pathlib import Path

# Importar paleta de colores y utilidades centralizadas
sys.path.insert(0, str(Path(__file__).parent))
from core.colors import COLORS
from core.base import Point
from core.svg_builder import SVGBuilder

def generate_square_sum(spec) -> str:
    """
    Genera la representación geométrica de (a+b)^2 = a^2 + 2ab + b^2.
    """
    data = spec.get('data', {})
    a_label = data.get('a_label', 'a')
    b_label = data.get('b_label', 'b')
    ab_label = data.get('ab_label', f'{a_label}{b_label}') # Permite personalización como "3x"
    a2_label = data.get('a2_label', f'{a_label}²')
    b2_label = data.get('b2_label', f'{b_label}²')
    
    a_val = data.get('a_val', 220)
    b_val = data.get('b_val', 100)
    
    # Canvas y márgenes
    margin = 50
    title_height = 40
    width = a_val + b_val + margin * 2 + 30
    height = a_val + b_val + margin * 2 + title_height + 20
    
    builder = SVGBuilder(width, height)
    
    # Fondo blanco
    builder.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    title = spec.get('metadata', {}).get('title', f'({a_label} + {b_label})²')
    builder.text(title, Point(width/2, 25), font_size=20, font_weight='bold')
    
    # Coordenadas base para el cuadrado
    start_x = margin
    start_y = margin + title_height
    
    # Colores con opacidad
    color_a2 = COLORS['primary']
    color_ab = COLORS['secondary']
    color_b2 = COLORS['success'] if 'success' in COLORS else '#22c55e'
    
    # 1. Cuadrado a^2 (Top-Left)
    builder.rect(start_x, start_y, a_val, a_val, 
                fill=color_a2, stroke=COLORS['text'], stroke_width=2)
    builder.text(a2_label, Point(start_x + a_val/2, start_y + a_val/2), 
                font_size=24, font_weight='bold', fill='white')
    
    # 2. Rectángulo ab (Top-Right)
    builder.rect(start_x + a_val, start_y, b_val, a_val, 
                fill=color_ab, stroke=COLORS['text'], stroke_width=2)
    builder.text(ab_label, Point(start_x + a_val + b_val/2, start_y + a_val/2), 
                font_size=18, font_weight='bold', fill='white')
    
    # 3. Rectángulo ab (Bottom-Left)
    builder.rect(start_x, start_y + a_val, a_val, b_val, 
                fill=color_ab, stroke=COLORS['text'], stroke_width=2)
    builder.text(ab_label, Point(start_x + a_val/2, start_y + a_val + b_val/2), 
                font_size=18, font_weight='bold', fill='white')
    
    # 4. Cuadrado b^2 (Bottom-Right)
    builder.rect(start_x + a_val, start_y + a_val, b_val, b_val, 
                fill=color_b2, stroke=COLORS['text'], stroke_width=2)
    builder.text(b2_label, Point(start_x + a_val + b_val/2, start_y + a_val + b_val/2), 
                font_size=18, font_weight='bold', fill='white')
    
    # ETIQUETAS DE LADOS
    # Lado superior
    builder.text(a_label, Point(start_x + a_val/2, start_y - 15), font_size=18, font_weight='bold')
    builder.text(b_label, Point(start_x + a_val + b_val/2, start_y - 15), font_size=18, font_weight='bold')
    
    # Lado izquierdo
    builder.text(a_label, Point(start_x - 15, start_y + a_val/2), font_size=18, font_weight='bold', anchor='end')
    builder.text(b_label, Point(start_x - 15, start_y + a_val + b_val/2), font_size=18, font_weight='bold', anchor='end')
    
    # Llaves (brackets) de (a+b) x (a+b)
    # Horizontal abajo
    builder.line(Point(start_x, start_y + a_val + b_val + 10), 
                 Point(start_x + a_val + b_val, start_y + a_val + b_val + 10),
                 stroke=COLORS['text'], stroke_width=1)
    builder.text(f'{a_label} + {b_label}', Point(start_x + (a_val+b_val)/2, start_y + a_val + b_val + 30), 
                font_size=18, font_weight='bold')
    
    # Vertical derecha
    builder.line(Point(start_x + a_val + b_val + 15, start_y), 
                 Point(start_x + a_val + b_val + 15, start_y + a_val + b_val),
                 stroke=COLORS['text'], stroke_width=1)
    builder.text(f'{a_label} + {b_label}', Point(start_x + a_val + b_val + 25, start_y + (a_val+b_val)/2), 
                font_size=18, font_weight='bold', anchor='start')
    
    return builder.build()

def generate_square_diff(spec) -> str:
    """
    Genera la representación geométrica de (a-b)^2 = a^2 - 2ab + b^2.
    """
    data = spec.get('data', {})
    a_label = data.get('a_label', 'a')
    b_label = data.get('b_label', 'b')
    a_minus_b_label = f'{a_label} - {b_label}'
    
    a_val = data.get('a_val', 300)
    b_val = data.get('b_val', 80)
    diff_val = a_val - b_val
    
    # Canvas y márgenes
    margin = 50
    title_height = 40
    width = a_val + margin * 2 + 50
    height = a_val + margin * 2 + title_height + 20
    
    builder = SVGBuilder(width, height)
    
    # Fondo blanco
    builder.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    title = spec.get('metadata', {}).get('title', f'({a_label} - {b_label})²')
    builder.text(title, Point(width/2, 25), font_size=20, font_weight='bold')
    
    # Coordenadas base
    start_x = margin
    start_y = margin + title_height
    
    # Colores
    color_diff2 = COLORS['primary']
    color_sub = COLORS['secondary']
    color_b2 = COLORS['success'] if 'success' in COLORS else '#22c55e'
    
    # 1. Cuadrado total a^2 (fondo opaco/dashed)
    builder.rect(start_x, start_y, a_val, a_val, 
                fill='none', stroke=COLORS['text'], stroke_width=1, dashed=True)
    
    # 2. Área central highlight (a-b)^2
    builder.rect(start_x, start_y, diff_val, diff_val, 
                fill=color_diff2, stroke=COLORS['text'], stroke_width=2)
    builder.text(f'({a_minus_b_label})²', Point(start_x + diff_val/2, start_y + diff_val/2), 
                font_size=22, font_weight='bold', fill='white')
    
    # 3. Rectángulos que se restan
    # Rectángulo derecha: (a-b) * b
    builder.rect(start_x + diff_val, start_y, b_val, diff_val, 
                fill=color_sub, fill_opacity=0.3, stroke=COLORS['text'], stroke_width=1)
    builder.text(f'{b_label}({a_minus_b_label})', Point(start_x + diff_val + b_val/2, start_y + diff_val/2), 
                font_size=12, font_weight='bold', fill=COLORS['text'])

    # Rectángulo abajo: b * (a-b)
    builder.rect(start_x, start_y + diff_val, diff_val, b_val, 
                fill=color_sub, fill_opacity=0.3, stroke=COLORS['text'], stroke_width=1)
    builder.text(f'{b_label}({a_minus_b_label})', Point(start_x + diff_val/2, start_y + diff_val + b_val/2), 
                font_size=12, font_weight='bold', fill=COLORS['text'])

    # Cuadrado abajo derecha: b^2 (que se suma después de restar 2ab)
    builder.rect(start_x + diff_val, start_y + diff_val, b_val, b_val, 
                fill=color_b2, fill_opacity=0.6, stroke=COLORS['text'], stroke_width=2)
    builder.text(f'{b_label}²', Point(start_x + diff_val + b_val/2, start_y + diff_val + b_val/2), 
                font_size=16, font_weight='bold', fill='white')

    # ETIQUETAS EXTERNAS (Medida a)
    # Superior
    builder.line(Point(start_x, start_y - 15), Point(start_x + a_val, start_y - 15), 
                 stroke=COLORS['text'], stroke_width=1)
    builder.text(a_label, Point(start_x + a_val/2, start_y - 25), font_size=18, font_weight='bold')

    # Izquierda
    builder.line(Point(start_x - 15, start_y), Point(start_x - 15, start_y + a_val), 
                 stroke=COLORS['text'], stroke_width=1)
    builder.text(a_label, Point(start_x - 30, start_y + a_val/2), font_size=18, font_weight='bold')

    # ETIQUETAS INTERNAS (Cotas inferiores)
    builder.text(a_minus_b_label, Point(start_x + diff_val/2, start_y + a_val + 20), font_size=16)
    builder.text(b_label, Point(start_x + diff_val + b_val/2, start_y + a_val + 20), font_size=16)
    
    return builder.build()

GENERATORS = {
    'square_sum': generate_square_sum,
    'square_diff': generate_square_diff,
}

def main():
    parser = argparse.ArgumentParser(description='Algebra Renderer')
    parser.add_argument('--spec', required=True, help='Archivo JSON de especificación')
    parser.add_argument('--output', required=True, help='Archivo SVG de salida')
    
    args = parser.parse_args()
    
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"❌ Error: No se encuentra el archivo {spec_path}")
        return 1
        
    with open(spec_path) as f:
        spec = json.load(f)
        
    type_ = spec.get('type', 'square_sum')
    generator = GENERATORS.get(type_)
    
    if not generator:
        print(f"❌ Tipo desconocido: {type_}")
        return 1
        
    svg_content = generator(spec)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg_content)
    
    print(f"✅ SVG generado: {args.output}")
    return 0

if __name__ == '__main__':
    exit(main())

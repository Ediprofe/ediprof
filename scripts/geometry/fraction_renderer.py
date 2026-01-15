#!/usr/bin/env python3
"""
📐 Renderer para Fracciones - v2.0 (SVGBuilder)

Genera modelos visuales de fracciones usando SVGBuilder siguiendo
los patrones establecidos en circle_renderer.py.

Tipos disponibles:
    definition     - Diagrama de numerador/denominador
    pie            - Gráfico circular (tipo pizza)
    grid           - Cuadrícula de celdas
    compound       - Múltiples unidades para fracciones impropias

Uso:
    python3 scripts/geometry/fraction_renderer.py --mode pie --num 3 --den 8 --output path.svg
"""

import argparse
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from core.svg_builder import SVGBuilder
from core.base import Point
from core.colors import COLORS
from core.canvas import SIZE_SIMPLE, SIZE_HORIZONTAL
from core.primitives import point_on_circle_svg

# ============================================================================
# COLORES ESPECÍFICOS PARA FRACCIONES
# ============================================================================

COLOR_TAKEN = COLORS['secondary']      # Verde - partes tomadas
COLOR_EMPTY = '#f1f5f9'                # Gris muy claro - partes vacías
COLOR_BORDER = COLORS['text_light']    # Bordes entre secciones
COLOR_LABEL = COLORS['text']           # Texto de etiquetas


def sector_path(cx: float, cy: float, r: float, start_deg: float, end_deg: float) -> str:
    """
    Genera path SVG para un sector circular (porción de pizza).
    SECTOR = Centro → Punto1 → Arco → Punto2 → Centro
    
    Basado en circle_renderer.py sector_path()
    """
    start = point_on_circle_svg(cx, cy, r, start_deg)
    end = point_on_circle_svg(cx, cy, r, end_deg)
    
    arc_span = abs(end_deg - start_deg)
    large_arc = 1 if arc_span > 180 else 0
    sweep = 1  # Sentido horario para que el arco curve hacia afuera
    
    return f"M {cx} {cy} L {start[0]:.2f} {start[1]:.2f} A {r} {r} 0 {large_arc} {sweep} {end[0]:.2f} {end[1]:.2f} Z"



# ============================================================================
# GENERADORES
# ============================================================================

def generate_definition(output_path: str):
    """Genera diagrama explicativo de numerador/denominador."""
    width, height = SIZE_SIMPLE
    svg = SVGBuilder(width, height)
    
    # Fondo
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    cx, cy = width / 2 - 50, height / 2
    
    # Línea de fracción
    svg.line(Point(cx - 40, cy), Point(cx + 40, cy), 
             stroke=COLORS['text'], stroke_width=4)
    
    # Letras a y b
    svg.text("a", Point(cx, cy - 25), font_size=48, font_weight='bold', 
             fill=COLORS['primary'])
    svg.text("b", Point(cx, cy + 45), font_size=48, font_weight='bold', 
             fill=COLOR_TAKEN)
    
    # Etiquetas explicativas
    svg.text("Numerador", Point(cx + 130, cy - 30), font_size=18, 
             font_weight='bold', fill=COLORS['primary'], anchor='start')
    svg.text("(Partes que tomamos)", Point(cx + 130, cy - 10), font_size=14, 
             fill=COLORS['text_light'], anchor='start')
    
    svg.text("Denominador", Point(cx + 130, cy + 35), font_size=18, 
             font_weight='bold', fill=COLOR_TAKEN, anchor='start')
    svg.text("(Total de partes iguales)", Point(cx + 130, cy + 55), font_size=14, 
             fill=COLORS['text_light'], anchor='start')
    
    # Flechas simples (líneas)
    svg.line(Point(cx + 50, cy - 25), Point(cx + 120, cy - 25), 
             stroke=COLORS['text_light'], stroke_width=2)
    svg.line(Point(cx + 50, cy + 35), Point(cx + 120, cy + 35), 
             stroke=COLORS['text_light'], stroke_width=2)
    
    svg.save(output_path)
    print(f"✅ Generated {output_path}")


def generate_mixed_definition(output_path: str):
    """Genera diagrama explicativo de la estructura de un número mixto."""
    width, height = SIZE_SIMPLE
    svg = SVGBuilder(width, height)
    
    # Fondo
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    cx, cy = width / 2, height / 2
    
    # Entero Grande (A)
    svg.text("A", Point(cx - 60, cy + 20), font_size=80, font_weight='bold', 
             fill=COLORS['primary'])
    
    # Fracción (b/c)
    svg.text("b", Point(cx + 40, cy - 10), font_size=48, font_weight='bold', 
             fill=COLOR_TAKEN)
    svg.line(Point(cx + 10, cy + 5), Point(cx + 70, cy + 5), 
             stroke=COLORS['text'], stroke_width=4)
    svg.text("c", Point(cx + 40, cy + 60), font_size=48, font_weight='bold', 
             fill=COLOR_BORDER)
    
    # Etiquetas
    svg.text("Parte Entera", Point(cx - 70, cy - 60), font_size=18, 
             font_weight='bold', fill=COLORS['primary'], anchor='middle')
    svg.line(Point(cx - 70, cy - 50), Point(cx - 70, cy - 20), 
             stroke=COLORS['text_light'], stroke_width=2)
    
    svg.text("Fracción Propia", Point(cx + 70, cy - 60), font_size=18, 
             font_weight='bold', fill=COLOR_TAKEN, anchor='middle')
    svg.line(Point(cx + 70, cy - 50), Point(cx + 70, cy - 20), 
             stroke=COLORS['text_light'], stroke_width=2)
    
    svg.save(output_path)
    print(f"✅ Generated {output_path}")


def generate_pie(num: int, den: int, output_path: str):
    """
    Genera gráfico circular tipo pizza.
    
    Los primeros 'num' sectores se colorean en verde,
    los restantes en gris claro.
    """
    width, height = SIZE_SIMPLE
    svg = SVGBuilder(width, height)
    
    # Fondo
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    cx, cy = width / 2 - 60, height / 2
    r = 100
    
    if den == 0:
        svg.save(output_path)
        return
    
    angle_step = 360 / den
    
    # Dibujar todos los sectores
    for i in range(den):
        # Ángulos: empezamos desde arriba (90°) y vamos en sentido horario
        start_angle = 90 - (i * angle_step)
        end_angle = 90 - ((i + 1) * angle_step)
        
        # Color según si está "tomado" o "vacío"
        fill_color = COLOR_TAKEN if i < num else COLOR_EMPTY
        
        # Path del sector
        path_d = sector_path(cx, cy, r, start_angle, end_angle)
        svg.path(path_d, fill=fill_color, stroke=COLOR_BORDER, stroke_width=2)
    
    # Borde exterior del círculo completo para acabado limpio
    svg.circle(Point(cx, cy), r, fill='none', stroke=COLORS['text_light'], stroke_width=2)
    
    # Etiqueta de la fracción a la derecha
    svg.text(f"{num}/{den}", Point(width - 80, height / 2), 
             font_size=56, font_weight='bold', fill=COLOR_LABEL)
    
    svg.save(output_path)
    print(f"✅ Generated {output_path}")


def generate_grid(num: int, den: int, output_path: str):
    """
    Genera cuadrícula de celdas para representar fracciones.
    
    Útil para fracciones como 7/12 (grupo de estudiantes).
    """
    width, height = SIZE_SIMPLE
    svg = SVGBuilder(width, height)
    
    # Fondo
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    if den == 0:
        svg.save(output_path)
        return
    
    # Calcular layout de la cuadrícula (lo más cuadrado posible)
    cols = math.ceil(math.sqrt(den))
    rows = math.ceil(den / cols)
    
    # Tamaño de cada celda
    grid_width = 280
    grid_height = 200
    cell_w = grid_width / cols
    cell_h = grid_height / rows
    
    # Posición inicial (centrado)
    start_x = (width - grid_width) / 2
    start_y = (height - grid_height) / 2 + 20
    
    # Título
    svg.text(f"Representación de {num}/{den}", Point(width / 2, 40), 
             font_size=20, font_weight='bold', fill=COLOR_LABEL)
    
    # Dibujar celdas
    count = 0
    for row in range(rows):
        for col in range(cols):
            if count >= den:
                break
            
            x = start_x + col * cell_w + 2
            y = start_y + row * cell_h + 2
            w = cell_w - 4
            h = cell_h - 4
            
            fill_color = COLOR_TAKEN if count < num else COLOR_EMPTY
            
            svg.rect(x, y, w, h, fill=fill_color, 
                     stroke=COLOR_BORDER, stroke_width=1, rx=6)
            
            count += 1
    
    svg.save(output_path)
    print(f"✅ Generated {output_path}")


def generate_compound(num: int, den: int, output_path: str):
    """
    Genera múltiples círculos para fracciones impropias/mixtas.
    
    Organiza las unidades en filas para evitar que se salgan del canvas
    cuando hay muchos enteros (ej: 10 1/10).
    """
    width, height = SIZE_HORIZONTAL
    svg = SVGBuilder(width, height)
    
    # Fondo
    svg.rect(0, 0, width, height, fill=COLORS['background'])
    
    if den == 0:
        svg.save(output_path)
        return
    
    # Número de unidades necesarias
    units_needed = math.ceil(num / den)
    
    # Configuración de layout
    r = 50 if units_needed > 5 else 60  # Reducir un poco si hay muchos
    gap_x = 20
    gap_y = 30
    
    # Determinar cuántas columnas caben
    max_cols = math.floor((width - 40) / (2 * r + gap_x))
    cols = min(units_needed, max_cols)
    rows = math.ceil(units_needed / cols)
    
    # Centrado
    total_w = cols * (2 * r) + (cols - 1) * gap_x
    total_h = rows * (2 * r) + (rows - 1) * gap_y
    
    start_x = (width - total_w) / 2 + r
    start_y = (height - total_h) / 2 + r - 10 # Un poco hacia arriba para dejar espacio al texto abajo
    
    remaining = num
    angle_step = 360 / den
    
    for i in range(units_needed):
        row = i // cols
        col = i % cols
        
        cx = start_x + col * (2 * r + gap_x)
        cy = start_y + row * (2 * r + gap_y)
        
        parts_in_this_unit = min(remaining, den)
        
        # Dibujar sectores de esta unidad
        for j in range(den):
            # Empezamos desde arriba (90°) y vamos en sentido anti-horario para ser consistentes
            # o sentido horario (sweep=1 en sector_path). Usamos 90 - ... para sentido horario.
            start_angle = 90 - (j * angle_step)
            end_angle = 90 - ((j + 1) * angle_step)
            
            fill_color = COLOR_TAKEN if j < parts_in_this_unit else COLOR_EMPTY
            
            path_d = sector_path(cx, cy, r, start_angle, end_angle)
            svg.path(path_d, fill=fill_color, stroke=COLOR_BORDER, stroke_width=2)
        
        # Borde exterior
        svg.circle(Point(cx, cy), r, fill='none', 
                   stroke=COLORS['text_light'], stroke_width=2)
        
        remaining -= parts_in_this_unit
    
    # Etiqueta de la fracción (solo una vez abajo)
    label = f"{num // den} {num % den}/{den}" if num % den != 0 else f"{num // den}"
    if num // den == 0: label = f"{num}/{den}"
    
    # Mostramos tanto la forma mixta como la impropia para claridad
    full_label = f"{num // den} {num % den}/{den}" if num % den != 0 else f"{num // den}"
    if num // den > 0 and num % den != 0:
        full_label = f"{num // den} \u2423 {num % den}/{den} = {num}/{den}"
    else:
        full_label = f"{num}/{den}"

    svg.text(full_label, Point(width / 2, height - 25), 
             font_size=32, font_weight='bold', fill=COLOR_LABEL)
    
    svg.save(output_path)
    print(f"✅ Generated {output_path}")


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="Fraction Renderer v2.0")
    parser.add_argument("--mode", required=True, 
                        choices=['definition', 'mixed_definition', 'pie', 'grid', 'compound'],
                        help="Tipo de ilustración")
    parser.add_argument("--num", type=int, default=1, 
                        help="Numerador")
    parser.add_argument("--den", type=int, default=1, 
                        help="Denominador")
    parser.add_argument("--output", required=True, 
                        help="Ruta del archivo SVG de salida")
    
    args = parser.parse_args()
    
    if args.mode == 'definition':
        generate_definition(args.output)
    elif args.mode == 'mixed_definition':
        generate_mixed_definition(args.output)
    elif args.mode == 'pie':
        generate_pie(args.num, args.den, args.output)
    elif args.mode == 'grid':
        generate_grid(args.num, args.den, args.output)
    elif args.mode == 'compound':
        generate_compound(args.num, args.den, args.output)


if __name__ == "__main__":
    main()

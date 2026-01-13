#!/usr/bin/env python3
"""
📐 TEMPLATE: Renderer Base

⚠️ INSTRUCCIONES OBLIGATORIAS:
   1. Copiar este archivo para crear un nuevo renderer
   2. Renombrar a [tema]_renderer.py
   3. NUNCA definir constantes como width=600, height=300
   4. SIEMPRE importar de core/

Este template garantiza que cualquier renderer nuevo:
- Use la paleta de colores estándar
- Use tamaños de canvas consistentes
- Use layouts predefinidos
- NO tenga hardcoding

Uso:
    python scripts/geometry/nuevo_renderer.py --mode MODO --output ruta.svg
"""

import argparse
import sys
from pathlib import Path

# ============================================================================
# IMPORTACIONES OBLIGATORIAS DE CORE
# ============================================================================

sys.path.insert(0, str(Path(__file__).parent))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.layouts import side_by_side, centered_single, get_title_position, get_symbol_position
from core.triangle_primitives import (
    draw_triangle, draw_angle_arc, draw_tick_marks,
    draw_label, draw_comparison_symbol, transform_points
)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def generate_svg(mode: str, output_path: str):
    """
    Genera una ilustración SVG.
    
    Args:
        mode: Tipo de ilustración a generar
        output_path: Ruta del archivo SVG de salida
    """
    # -------------------------------------------------------------------------
    # PASO 1: Obtener configuración del canvas (NUNCA hardcodear)
    # -------------------------------------------------------------------------
    # Opciones: 'simple', 'compound', 'horizontal', 'cartesian', 'square'
    config = get_canvas_config('horizontal')  # ← Cambiar según necesidad
    width = config['width']
    height = config['height']
    
    # -------------------------------------------------------------------------
    # PASO 2: Inicializar el SVG
    # -------------------------------------------------------------------------
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>')
    
    # -------------------------------------------------------------------------
    # PASO 3: Definir la figura base (ejemplo: triángulo)
    # -------------------------------------------------------------------------
    # Puntos en coordenadas locales (origen en 0,0)
    base_triangle = [(0, 0), (100, 0), (50, -80)]
    figure_w, figure_h = 100, 80
    
    # -------------------------------------------------------------------------
    # PASO 4: Calcular layout
    # -------------------------------------------------------------------------
    if mode == 'comparacion':
        # Dos figuras lado a lado
        off1, off2 = side_by_side('horizontal', figure_w, figure_h, gap=100)
        
        T1 = transform_points(base_triangle, scale=1.0, offset=off1)
        T2 = transform_points(base_triangle, scale=1.0, offset=off2)
        
        # Dibujar triángulos
        parts.append(draw_triangle(T1, stroke=COLORS['primary']))
        parts.append(draw_triangle(T2, stroke=COLORS['medianas']))
        
        # Símbolo de comparación
        sym_pos = get_symbol_position(off1, off2, figure_w, 'horizontal')
        parts.append(draw_comparison_symbol(sym_pos[0], sym_pos[1], "≅"))
        
    elif mode == 'simple':
        # Una figura centrada
        off = centered_single('compound', figure_w, figure_h)
        
        T = transform_points(base_triangle, scale=1.5, offset=off)
        parts.append(draw_triangle(T, stroke=COLORS['primary']))
        
        # Etiquetas de vértices
        parts.append(draw_label(T[0][0] - 15, T[0][1] + 15, "A"))
        parts.append(draw_label(T[1][0] + 15, T[1][1] + 15, "B"))
        parts.append(draw_label(T[2][0], T[2][1] - 15, "C"))
    
    # -------------------------------------------------------------------------
    # PASO 5: Agregar título
    # -------------------------------------------------------------------------
    title_pos = get_title_position('horizontal')
    parts.append(draw_label(title_pos[0], title_pos[1], "Título de la Ilustración", size=18))
    
    # -------------------------------------------------------------------------
    # PASO 6: Cerrar y guardar
    # -------------------------------------------------------------------------
    parts.append('</svg>')
    
    with open(output_path, 'w') as f:
        f.write("\n".join(parts))
    
    print(f"✅ Generated {output_path}")


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Template Renderer")
    parser.add_argument("--mode", required=True, help="Tipo de ilustración")
    parser.add_argument("--output", required=True, help="Ruta del SVG de salida")
    args = parser.parse_args()
    
    generate_svg(args.mode, args.output)

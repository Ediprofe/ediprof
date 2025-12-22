#!/usr/bin/env python3
"""
📐 Render Vectores Sentido - Ilustraciones de vectores con misma dirección y diferente sentido

Genera tres planos cartesianos que muestran pares de vectores con:
1. Dirección vertical: uno hacia arriba, otro hacia abajo
2. Dirección horizontal: uno hacia la derecha, otro hacia la izquierda  
3. Dirección diagonal (45°): uno a 45°, otro a 225°

Uso:
    python3 scripts/geometry/render_vectores_sentido.py
"""

import sys
import os
import math

# Agregar el directorio scripts/geometry al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.base import Point
from core.colors import COLORS
from core.svg_builder import SVGBuilder
from core.coordinate_system import CoordinateSystem


def render_vectores_verticales(output_path: str) -> None:
    """
    Renderiza dos vectores verticales: uno hacia arriba, otro hacia abajo.
    Misma dirección (vertical), diferente sentido.
    """
    # Configuración del sistema de coordenadas
    cs = CoordinateSystem(
        svg_width=400,
        svg_height=400,
        x_range=(-4, 4),
        y_range=(-4, 4),
        padding=40
    )
    
    builder = SVGBuilder(400, 400)
    
    # Fondo
    builder.rect(0, 0, 400, 400, fill=COLORS['background'], rx=12)
    
    # Cuadrícula, ejes y marcas
    cs.draw_grid(builder)
    cs.draw_axes(builder)
    cs.draw_ticks(builder)
    
    # Vector hacia arriba (positivo) - desde origen hasta (0, 3)
    start_up = cs.to_svg(Point(0, 0))
    end_up = cs.to_svg(Point(0, 3))
    builder.arrow(start_up, end_up, stroke=COLORS['primary'], stroke_width=3, head_size=12)
    
    # Etiqueta v₁
    label_up_pos = Point(end_up.x + 15, end_up.y + 5)
    builder.text('v₁', label_up_pos, font_size=16, fill=COLORS['primary'], font_weight='bold')
    
    # Vector hacia abajo (negativo) - desde origen hasta (0, -3)
    # Desplazado horizontalmente para que se vea claramente
    start_down = cs.to_svg(Point(0, 0))
    end_down = cs.to_svg(Point(0, -3))
    builder.arrow(start_down, end_down, stroke=COLORS['accent'], stroke_width=3, head_size=12)
    
    # Etiqueta v₂
    label_down_pos = Point(end_down.x + 15, end_down.y - 5)
    builder.text('v₂', label_down_pos, font_size=16, fill=COLORS['accent'], font_weight='bold')
    
    # Línea punteada que muestra la "línea de acción"
    line_start = cs.to_svg(Point(0, -3.8))
    line_end = cs.to_svg(Point(0, 3.8))
    # Ya está representada por el eje Y, pero podríamos agregar énfasis
    
    # Título descriptivo
    builder.text('Dirección: Vertical', Point(200, 25), 
                 font_size=14, fill=COLORS['text'], font_weight='bold')
    builder.text('Sentidos opuestos', Point(200, 385), 
                 font_size=12, fill=COLORS['text_light'])
    
    # Guardar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    builder.save(output_path)
    print(f"✓ Generado: {output_path}")


def render_vectores_horizontales(output_path: str) -> None:
    """
    Renderiza dos vectores horizontales: uno hacia la derecha, otro hacia la izquierda.
    Misma dirección (horizontal), diferente sentido.
    """
    cs = CoordinateSystem(
        svg_width=400,
        svg_height=400,
        x_range=(-4, 4),
        y_range=(-4, 4),
        padding=40
    )
    
    builder = SVGBuilder(400, 400)
    
    # Fondo
    builder.rect(0, 0, 400, 400, fill=COLORS['background'], rx=12)
    
    # Cuadrícula, ejes y marcas
    cs.draw_grid(builder)
    cs.draw_axes(builder)
    cs.draw_ticks(builder)
    
    # Vector hacia la derecha - desde origen hasta (3, 0)
    start_right = cs.to_svg(Point(0, 0))
    end_right = cs.to_svg(Point(3, 0))
    builder.arrow(start_right, end_right, stroke=COLORS['primary'], stroke_width=3, head_size=12)
    
    # Etiqueta v₁
    label_right_pos = Point(end_right.x + 5, end_right.y - 15)
    builder.text('v₁', label_right_pos, font_size=16, fill=COLORS['primary'], font_weight='bold')
    
    # Vector hacia la izquierda - desde origen hasta (-3, 0)
    start_left = cs.to_svg(Point(0, 0))
    end_left = cs.to_svg(Point(-3, 0))
    builder.arrow(start_left, end_left, stroke=COLORS['accent'], stroke_width=3, head_size=12)
    
    # Etiqueta v₂
    label_left_pos = Point(end_left.x - 5, end_left.y - 15)
    builder.text('v₂', label_left_pos, font_size=16, fill=COLORS['accent'], font_weight='bold')
    
    # Título descriptivo
    builder.text('Dirección: Horizontal', Point(200, 25), 
                 font_size=14, fill=COLORS['text'], font_weight='bold')
    builder.text('Sentidos opuestos', Point(200, 385), 
                 font_size=12, fill=COLORS['text_light'])
    
    # Guardar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    builder.save(output_path)
    print(f"✓ Generado: {output_path}")


def render_vectores_diagonales(output_path: str) -> None:
    """
    Renderiza dos vectores diagonales: uno a 45°, otro a 225°.
    Misma dirección (diagonal noreste-suroeste), diferente sentido.
    """
    cs = CoordinateSystem(
        svg_width=400,
        svg_height=400,
        x_range=(-4, 4),
        y_range=(-4, 4),
        padding=40
    )
    
    builder = SVGBuilder(400, 400)
    
    # Fondo
    builder.rect(0, 0, 400, 400, fill=COLORS['background'], rx=12)
    
    # Cuadrícula, ejes y marcas
    cs.draw_grid(builder)
    cs.draw_axes(builder)
    cs.draw_ticks(builder)
    
    # Calcular puntos para vectores de magnitud 3 a 45° y 225°
    magnitude = 2.5
    
    # Vector a 45° (primer cuadrante)
    angle_45 = math.radians(45)
    end_x_45 = magnitude * math.cos(angle_45)
    end_y_45 = magnitude * math.sin(angle_45)
    
    start_45 = cs.to_svg(Point(0, 0))
    end_45 = cs.to_svg(Point(end_x_45, end_y_45))
    builder.arrow(start_45, end_45, stroke=COLORS['primary'], stroke_width=3, head_size=12)
    
    # Etiqueta v₁ con ángulo
    label_45_pos = Point(end_45.x + 10, end_45.y - 10)
    builder.text('v₁ (45°)', label_45_pos, font_size=14, fill=COLORS['primary'], font_weight='bold')
    
    # Vector a 225° (tercer cuadrante)
    angle_225 = math.radians(225)
    end_x_225 = magnitude * math.cos(angle_225)
    end_y_225 = magnitude * math.sin(angle_225)
    
    start_225 = cs.to_svg(Point(0, 0))
    end_225 = cs.to_svg(Point(end_x_225, end_y_225))
    builder.arrow(start_225, end_225, stroke=COLORS['accent'], stroke_width=3, head_size=12)
    
    # Etiqueta v₂ con ángulo
    label_225_pos = Point(end_225.x - 35, end_225.y + 15)
    builder.text('v₂ (225°)', label_225_pos, font_size=14, fill=COLORS['accent'], font_weight='bold')
    
    # Dibujar la línea de acción (punteada) que muestra que están en la misma dirección
    # Extender un poco más allá de los vectores
    diag_start = cs.to_svg(Point(-3.2, -3.2))
    diag_end = cs.to_svg(Point(3.2, 3.2))
    builder.line(diag_start, diag_end, stroke=COLORS['auxiliary'], stroke_width=1, dashed=True)
    
    # Título descriptivo
    builder.text('Dirección: Diagonal (45°)', Point(200, 25), 
                 font_size=14, fill=COLORS['text'], font_weight='bold')
    builder.text('Sentidos opuestos', Point(200, 385), 
                 font_size=12, fill=COLORS['text_light'])
    
    # Guardar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    builder.save(output_path)
    print(f"✓ Generado: {output_path}")


def main():
    """Genera todas las ilustraciones de vectores con diferentes sentidos."""
    base_path = "public/images/fisica/vectores"
    
    print("🔄 Generando ilustraciones de vectores con mismo dirección y diferente sentido...")
    print()
    
    # 1. Vectores verticales
    render_vectores_verticales(f"{base_path}/sentido-vertical.svg")
    
    # 2. Vectores horizontales
    render_vectores_horizontales(f"{base_path}/sentido-horizontal.svg")
    
    # 3. Vectores diagonales
    render_vectores_diagonales(f"{base_path}/sentido-diagonal.svg")
    
    print()
    print("✅ Todas las ilustraciones generadas correctamente.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Pie Chart Renderer - Ilustración de la definición de Radián
Muestra cómo radios caben en media vuelta (PI) o vuelta completa (2PI).
"""

import argparse
import math
from pathlib import Path

def get_sector_path(cx, cy, start_rad, end_rad, r, fill_color, stroke_color="white"):
    # Y invertido en SVG, ángulos en sentido antihorario estándar matemático
    # SVG y crece hacia abajo, así que para ir "arriba" (ángulos positivos) restamos en sin
    # Corrección: En SVG, ángulos positivos con cos/sin usuales van horario si no invertimos Y.
    # Aquí usaremos: x = cx + r*cos(-angle), y = cy + r*sin(-angle) para simular coords cartesianas visuales
    x1 = cx + r * math.cos(-start_rad)
    y1 = cy + r * math.sin(-start_rad)
    x2 = cx + r * math.cos(-end_rad)
    y2 = cy + r * math.sin(-end_rad)
    
    # Large arc flag
    large_arc = 1 if (end_rad - start_rad) > math.pi else 0
    
    path = f"M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large_arc} 0 {x2:.1f} {y2:.1f} Z"
    return f'<path d="{path}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2" opacity="0.9"/>'

def draw_arc_stroke(cx, cy, start_rad, end_rad, r, color):
    x1 = cx + r * math.cos(-start_rad)
    y1 = cy + r * math.sin(-start_rad)
    x2 = cx + r * math.cos(-end_rad)
    y2 = cy + r * math.sin(-end_rad)
    large_arc = 1 if (end_rad - start_rad) > math.pi else 0
    path = f"M {x1:.1f} {y1:.1f} A {r} {r} 0 {large_arc} 0 {x2:.1f} {y2:.1f}"
    return f'<path d="{path}" fill="none" stroke="{color}" stroke-width="4"/>'

def draw_label(cx, cy, radius, angle_rad, text, r_offset=30, color="#fff"):
    lx = cx + (radius - r_offset) * math.cos(-angle_rad)
    ly = cy + (radius - r_offset) * math.sin(-angle_rad)
    return f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold" fill="{color}">{text}</text>'

def generate_half_turn_viz(width=600, height=400) -> str:
    cx, cy = width / 2, height - 60
    radius = 250
    
    color_rad1 = "#3b82f6"
    color_rad2 = "#8b5cf6"
    color_rad3 = "#ec4899"
    color_rest = "#ef4444"

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<text x="{cx}" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e293b">1 Media Vuelta (180°)</text>',
        f'<text x="{cx}" y="65" text-anchor="middle" font-size="14" fill="#64748b">3 radios + 0.14... = 3.14... = π</text>',
    ]

    # Sectores con texto "1 Rad"
    svg_parts.append(get_sector_path(cx, cy, 0, 1, radius, color_rad1))
    svg_parts.append(draw_label(cx, cy, radius, 0.5, "1 Rad", 60, "white"))
    
    svg_parts.append(get_sector_path(cx, cy, 1, 2, radius, color_rad2))
    svg_parts.append(draw_label(cx, cy, radius, 1.5, "1 Rad", 60, "white"))
    
    svg_parts.append(get_sector_path(cx, cy, 2, 3, radius, color_rad3))
    svg_parts.append(draw_label(cx, cy, radius, 2.5, "1 Rad", 60, "white"))

    # Pedacito resto (3 a pi)
    svg_parts.append(get_sector_path(cx, cy, 3, math.pi, radius + 15, color_rest))
    
    # Etiqueta con línea indicadora para "0.1416..."
    rest_angle = 3 + (math.pi - 3)/2
    
    # Punto dentro del sector (destino de la flecha)
    tx = cx + (radius - 20) * math.cos(-rest_angle)
    ty = cy + (radius - 20) * math.sin(-rest_angle)
    
    # Posición del texto (FORCE SAFE COORDINATES)
    # El sector está a la izquierda (cerca de x=50). Ponemos el texto arriba y a la derecha del sector.
    lx = cx - radius + 10 # x approx 60
    ly = cy - 40          # y un poco arriba de la línea base
    
    svg_parts.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="start" font-size="14" font-weight="bold" fill="{color_rest}">≈ 0.1416...</text>')
    svg_parts.append(f'<line x1="{lx + 10:.1f}" y1="{ly + 5:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="{color_rest}" stroke-width="2"/>')
    svg_parts.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="2" fill="{color_rest}"/>') # Punto final de flecha

    # Arcos de borde (strokes) para resaltar la medida de 1 radio
    svg_parts.append(draw_arc_stroke(cx, cy, 0, 1, radius, "#1d4ed8"))
    svg_parts.append(draw_arc_stroke(cx, cy, 1, 2, radius, "#6d28d9"))
    svg_parts.append(draw_arc_stroke(cx, cy, 2, 3, radius, "#be185d"))

    # Eje base y etiquetas de extremos
    svg_parts.append(f'<line x1="{cx - radius - 20}" y1="{cy}" x2="{cx + radius + 20}" y2="{cy}" stroke="#64748b" stroke-width="2"/>')
    svg_parts.append(f'<text x="{cx + radius + 10}" y="{cy}" font-size="12" fill="#64748b">0</text>')
    
    # Etiqueta de TOTAL PI (alejada para no confundir con el pedacito)
    svg_parts.append(f'<text x="{cx - radius - 25}" y="{cy}" text-anchor="end" font-size="14" font-weight="bold" fill="#64748b">Total = π</text>')
    
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#1e293b"/>')
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def generate_full_turn_viz(width=600, height=600) -> str:
    cx, cy = width / 2, height / 2 + 20
    radius = 200
    
    colors = ["#3b82f6", "#8b5cf6", "#ec4899", "#f59e0b", "#10b981", "#06b6d4"]
    color_rest = "#ef4444"

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<text x="{cx}" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e293b">1 Vuelta Completa</text>',
        f'<text x="{cx}" y="55" text-anchor="middle" font-size="14" fill="#64748b">360° = 2π radianes ≈ 6.28 radios</text>',
    ]

    # Sectores enteros 1 a 6
    for i in range(6):
        svg_parts.append(get_sector_path(cx, cy, i, i+1, radius, colors[i]))
        svg_parts.append(draw_label(cx, cy, radius, i + 0.5, f"{i+1}", 40))
        # Stroke del arco para resaltar
        # svg_parts.append(draw_arc_stroke(cx, cy, i, i+1, radius, "rgba(255,255,255,0.5)"))

    # Resto (6 a 2pi)
    svg_parts.append(get_sector_path(cx, cy, 6, 2*math.pi, radius + 15, color_rest))
    
    # Etiqueta del resto
    rest_angle = 6 + (2*math.pi - 6)/2
    rx = cx + (radius + 50) * math.cos(-rest_angle)
    ry = cy + (radius + 50) * math.sin(-rest_angle)
    svg_parts.append(f'<text x="{rx:.1f}" y="{ry:.1f}" text-anchor="start" font-size="14" font-weight="bold" fill="{color_rest}">0.28...</text>')

    # Eje horizontal referencia
    svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + radius + 30}" y2="{cy}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>')
    svg_parts.append(f'<text x="{cx + radius + 35}" y="{cy}" dominant-baseline="middle" font-size="14" fill="#64748b">0 / 2π</text>')
    
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#1e293b"/>')
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def main():
    parser = argparse.ArgumentParser(description='Radian Viz Renderer')
    parser.add_argument('--output', required=True, help='Archivo SVG de salida')
    parser.add_argument('--mode', choices=['half', 'full'], default='half', help='half (PI) o full (2PI)')
    args = parser.parse_args()
    
    if args.mode == 'full':
        svg_content = generate_full_turn_viz()
    else:
        svg_content = generate_half_turn_viz()
        
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg_content)
    print(f"✅ SVG generado: {args.output}")

if __name__ == '__main__':
    main()

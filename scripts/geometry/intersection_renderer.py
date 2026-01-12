#!/usr/bin/env python3
"""
Intersection Renderer
Generates an SVG illustration for intersecting lines with specific angles and custom labels.
"""

import math
import argparse
from pathlib import Path

# Color Palette
COLOR_LINE = "#64748b" # Slate 500
COLOR_ANGLE_ACUTE = "#f97316" # Orange 500
COLOR_ANGLE_OBTUSE = "#3b82f6" # Blue 500
COLOR_TEXT = "#1e293b" # Slate 800
COLOR_BG = "white"

def get_coord(cx, cy, r, angle_deg):
    rad = math.radians(angle_deg)
    return cx + r * math.cos(rad), cy - r * math.sin(rad)

def draw_arc(cx, cy, r, start_deg, end_deg, color):
    sx, sy = get_coord(cx, cy, r, start_deg)
    ex, ey = get_coord(cx, cy, r, end_deg)
    diff = end_deg - start_deg
    large_arc = 1 if diff > 180 else 0
    return f'<path d="M {cx} {cy} L {sx:.2f} {sy:.2f} A {r} {r} 0 {large_arc} 0 {ex:.2f} {ey:.2f} Z" fill="{color}" fill-opacity="0.2" stroke="none" />' \
           f'<path d="M {sx:.2f} {sy:.2f} A {r} {r} 0 {large_arc} 0 {ex:.2f} {ey:.2f}" fill="none" stroke="{color}" stroke-width="2" />'

def generate_svg(width=600, height=300, mode="cross", labels=None):
    cx, cy = width / 2, height / 2
    length = 120
    
    # Base angles for lines (representing obtuse 100 / acute 80 situation generally, or 36/144)
    if mode == "adyacentes_x_4x":
        # 36 deg and 144 deg
        # Let's rotate so base line is horizontal
        # Line 1: 0 to 180
        # Line 2: 36 deg
        angle_line1 = 0
        angle_line2 = 36 # Acute angle
        
        # We need adjacent angles on a straight line.
        # Angle 1 forms x (Acute). Angle 2 forms 4x (Obtuse).
        # We'll draw adjacent angles on top side.
        
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
            f'<rect width="{width}" height="{height}" fill="{COLOR_BG}" rx="12"/>',
        ]
        
        r_arc = 50
        
        # Line 1 (Horizontal)
        svg_parts.append(f'<line x1="{cx-length}" y1="{cy}" x2="{cx+length}" y2="{cy}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        # Line 2 (Ray at 36 deg)
        l2x, l2y = get_coord(cx, cy, length, 36)
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{l2x:.2f}" y2="{l2y:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        # Angle X (0 to 36)
        svg_parts.append(draw_arc(cx, cy, r_arc+20, 0, 36, COLOR_ANGLE_ACUTE))
        lx, ly = get_coord(cx, cy, r_arc + 40, 18)
        svg_parts.append(f'<text x="{lx:.2f}" y="{ly:.2f}" text-anchor="start" dominant-baseline="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">{labels[0]}</text>')
        
        # Angle 4X (36 to 180)
        svg_parts.append(draw_arc(cx, cy, r_arc, 36, 180, COLOR_ANGLE_OBTUSE))
        lx2, ly2 = get_coord(cx, cy, r_arc + 30, 108)
        svg_parts.append(f'<text x="{lx2:.2f}" y="{ly2:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">{labels[1]}</text>')
        
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLOR_TEXT}"/>')
        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    elif mode == "opuestos_eq":
        # Example: 100 deg (obtuse) are the opposite ones.
        # We'll draw X shape.
        # Line 1: -10 to 170
        # Line 2: 10 to 190. 
        # Wait, for 100 deg vertical angle:
        # Angles from vertical?
        # Let's say angles are Left and Right (Obtuse 100).
        # Top/Bottom are Acute (80).
        
        # Let's use 50 and 130 deg lines for symmetry (Up is 80, Right is 100).
        # We label the Obtuse angles (Left and Right).
        
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
            f'<rect width="{width}" height="{height}" fill="{COLOR_BG}" rx="12"/>',
        ]
        
        # Lines
        x1, y1 = get_coord(cx, cy, length, 50)
        x2, y2 = get_coord(cx, cy, length, 230)
        svg_parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        x3, y3 = get_coord(cx, cy, length, 130)
        x4, y4 = get_coord(cx, cy, length, 310)
        svg_parts.append(f'<line x1="{x3:.2f}" y1="{y3:.2f}" x2="{x4:.2f}" y2="{y4:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')

        r_arc = 50
        
        # Opuesto 1 (Right): 310 (-50) to 50? No, 310 to 410 (50+360)? 
        # Actually range is between line ends: 130 and 230 is Left. 310 and 50 is Right.
        # Wait lines are 50/230 and 130/310.
        # Angle between 310 and 50 (passing 0) is 100 deg.
        
        # Right Angle (3x + 10)
        svg_parts.append(draw_arc(cx, cy, r_arc, 310, 410, COLOR_ANGLE_OBTUSE))
        lx, ly = get_coord(cx, cy, r_arc + 40, 0) # 0 is center of this arc
        svg_parts.append(f'<text x="{lx:.2f}" y="{ly:.2f}" text-anchor="start" dominant-baseline="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">{labels[0]}</text>')
        
        # Left Angle (4x - 20)
        svg_parts.append(draw_arc(cx, cy, r_arc, 130, 230, COLOR_ANGLE_OBTUSE))
        lx2, ly2 = get_coord(cx, cy, r_arc + 40, 180)
        svg_parts.append(f'<text x="{lx2:.2f}" y="{ly2:.2f}" text-anchor="end" dominant-baseline="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">{labels[1]}</text>')
        
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLOR_TEXT}"/>')
        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)
        
    elif mode == "opuestos_simple":
        # Example 1: Top/Bottom 120 deg
        # Lines at 30 and 150 deg (Bisector 90)
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
            f'<rect width="{width}" height="{height}" fill="{COLOR_BG}" rx="12"/>',
        ]
        
        # Lines
        x1, y1 = get_coord(cx, cy, length, 30)
        x2, y2 = get_coord(cx, cy, length, 210)
        svg_parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        x3, y3 = get_coord(cx, cy, length, 150)
        x4, y4 = get_coord(cx, cy, length, 330)
        svg_parts.append(f'<line x1="{x3:.2f}" y1="{y3:.2f}" x2="{x4:.2f}" y2="{y4:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        r_arc = 50
        # Top (120) - 30 to 150
        svg_parts.append(draw_arc(cx, cy, r_arc, 30, 150, COLOR_ANGLE_OBTUSE))
        lx, ly = get_coord(cx, cy, r_arc + 40, 90)
        svg_parts.append(f'<text x="{lx:.2f}" y="{ly:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">{labels[0]}</text>')
        
        # Bottom (?) - 210 to 330
        svg_parts.append(draw_arc(cx, cy, r_arc, 210, 330, COLOR_ANGLE_OBTUSE))
        lx2, ly2 = get_coord(cx, cy, r_arc + 40, 270)
        svg_parts.append(f'<text x="{lx2:.2f}" y="{ly2+15:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">{labels[1]}</text>')
        
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLOR_TEXT}"/>')
        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    elif mode == "adyacentes_simple":
        # Example 2: 30 deg and ?
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
            f'<rect width="{width}" height="{height}" fill="{COLOR_BG}" rx="12"/>',
        ]
        
        # Horizontal Line
        svg_parts.append(f'<line x1="{cx-length}" y1="{cy}" x2="{cx+length}" y2="{cy}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        # Ray at 30 deg
        lx, ly = get_coord(cx, cy, length, 30)
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{lx:.2f}" y2="{ly:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        r_arc = 60
        # Angle 30
        svg_parts.append(draw_arc(cx, cy, r_arc+20, 0, 30, COLOR_ANGLE_ACUTE))
        txt_x, txt_y = get_coord(cx, cy, r_arc + 50, 15)
        # Manually adjust label pos slightly for 30 deg
        svg_parts.append(f'<text x="{txt_x:.2f}" y="{txt_y+5:.2f}" text-anchor="start" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">{labels[0]}</text>')
        
        # Angle ? (30 to 180)
        svg_parts.append(draw_arc(cx, cy, r_arc, 30, 180, COLOR_ANGLE_OBTUSE))
        txt2_x, txt2_y = get_coord(cx, cy, r_arc + 40, 105)
        svg_parts.append(f'<text x="{txt2_x:.2f}" y="{txt2_y:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">{labels[1]}</text>')
        
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLOR_TEXT}"/>')
        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    elif mode == "tijeras":
        # Example 6: 45 deg scissors
        # Lines at -22.5 (337.5) and 22.5
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
            f'<rect width="{width}" height="{height}" fill="{COLOR_BG}" rx="12"/>',
        ]
        
        # Lines
        x1, y1 = get_coord(cx, cy, length, 22.5)
        x2, y2 = get_coord(cx, cy, length, 202.5)
        svg_parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        x3, y3 = get_coord(cx, cy, length, -22.5) # 337.5
        x4, y4 = get_coord(cx, cy, length, 157.5)
        svg_parts.append(f'<line x1="{x3:.2f}" y1="{y3:.2f}" x2="{x4:.2f}" y2="{y4:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        r_arc = 50
        # Right (Hojas)
        svg_parts.append(draw_arc(cx, cy, r_arc, 337.5, 382.5, COLOR_ANGLE_ACUTE)) # 382.5 = 22.5 + 360
        lx, ly = get_coord(cx, cy, r_arc + 60, 0)
        svg_parts.append(f'<text x="{lx:.2f}" y="{ly-10:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">Hojas</text>')
        svg_parts.append(f'<text x="{lx:.2f}" y="{ly+10:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">{labels[0]}</text>')
        
        # Left (Mangos)
        svg_parts.append(draw_arc(cx, cy, r_arc, 157.5, 202.5, COLOR_ANGLE_ACUTE))
        lx2, ly2 = get_coord(cx, cy, r_arc + 60, 180)
        svg_parts.append(f'<text x="{lx2:.2f}" y="{ly2-10:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">Mangos</text>')
        svg_parts.append(f'<text x="{lx2:.2f}" y="{ly2+10:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">{labels[1]}</text>')
        
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLOR_TEXT}"/>')
        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)
    
    else:
        # Default Cross (Example 3) - North 80 deg / East 100 deg
        # Lines at 50-230 and 130-310
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
            f'<rect width="{width}" height="{height}" fill="{COLOR_BG}" rx="12"/>',
            # f'<text x="{cx}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLOR_TEXT}">Cruce de Rectas</text>'
        ]

        # Draw Angles (Sectors)
        r_arc = 50
        # North (80 deg) -> from 50 to 130
        svg_parts.append(draw_arc(cx, cy, r_arc, 50, 130, COLOR_ANGLE_ACUTE))
        # South (80 deg) -> from 230 to 310
        svg_parts.append(draw_arc(cx, cy, r_arc, 230, 310, COLOR_ANGLE_ACUTE))
        
        # West (100 deg) -> from 130 to 230
        svg_parts.append(draw_arc(cx, cy, r_arc, 130, 230, COLOR_ANGLE_OBTUSE))
        # East (100 deg) -> from 310 to 410 (50)
        svg_parts.append(draw_arc(cx, cy, r_arc, 310, 410, COLOR_ANGLE_OBTUSE))
        
        # Draw Lines
        # Line 1: 50 deg to 230 deg
        x1, y1 = get_coord(cx, cy, length, 50)
        x2, y2 = get_coord(cx, cy, length, 230)
        svg_parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')

        # Line 2: 130 deg to 310 deg
        x3, y3 = get_coord(cx, cy, length, 130)
        x4, y4 = get_coord(cx, cy, length, 310)
        svg_parts.append(f'<line x1="{x3:.2f}" y1="{y3:.2f}" x2="{x4:.2f}" y2="{y4:.2f}" stroke="{COLOR_LINE}" stroke-width="3" stroke-linecap="round"/>')
        
        # Build Labels
        # North Label
        nx, ny = get_coord(cx, cy, r_arc + 40, 90)
        svg_parts.append(f'<text x="{nx:.2f}" y="{ny:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">Norte (80°)</text>')
        
        # South Label
        sx, sy = get_coord(cx, cy, r_arc + 40, 270)
        svg_parts.append(f'<text x="{sx:.2f}" y="{sy+15:.2f}" text-anchor="middle" font-weight="bold" fill="{COLOR_ANGLE_ACUTE}">Sur (80°)</text>')
        
        # West Label
        wx, wy = get_coord(cx, cy, r_arc + 50, 180)
        svg_parts.append(f'<text x="{wx:.2f}" y="{wy+5:.2f}" text-anchor="end" dominant-baseline="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">Oeste (100°)</text>')
        
        # East Label
        ex, ey = get_coord(cx, cy, r_arc + 50, 0)
        svg_parts.append(f'<text x="{ex:.2f}" y="{ey+5:.2f}" text-anchor="start" dominant-baseline="middle" font-weight="bold" fill="{COLOR_ANGLE_OBTUSE}">Este (100°)</text>')

        # Center Dot
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLOR_TEXT}"/>')

        svg_parts.append('</svg>')
        return '\n'.join(svg_parts) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode', default='cross')
    parser.add_argument('--labels', nargs='+', default=[])
    args = parser.parse_args()
    
    # Re-use logic for previous example 3 if needed, otherwise use new generate_svg
    if args.mode == 'cross':
        # Quick re-implementation of Ex 3 logic inside generic structure if desired, 
        # but for now let's focus on 4 and 5.
        pass
    
    svg = generate_svg(mode=args.mode, labels=args.labels)
    
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(svg)
    print(f"✅ Generated {args.output}")


import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.triangle_primitives import draw_label

# --- Configuration & Helpers ---
CANVAS_NAME = 'compound' # Standard 600x460
FONT_SIZE_LABEL = 20
FONT_SIZE_TITLE = 22

def draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color='none', stroke_width=3, fill_opacity=0.1):
    path_d = f"M {points[0][0]} {points[0][1]} L {points[1][0]} {points[1][1]} L {points[2][0]} {points[2][1]} L {points[3][0]} {points[3][1]} Z"
    parts.append(f'<path d="{path_d}" fill="{fill_color}" fill-opacity="{fill_opacity}" stroke="{stroke_color}" stroke-width="{stroke_width}" stroke-linejoin="round"/>')

def draw_tick_mark(parts, p1, p2, count=1, color=COLORS['text']):
    mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    perp_angle = angle + math.pi/2
    
    size = 12
    gap = 5
    
    start_offset = - (count - 1) * gap / 2
    for i in range(count):
        off = start_offset + i * gap
        cx = mid[0] + off * math.cos(angle)
        cy = mid[1] + off * math.sin(angle)
        
        x1 = cx + (size/2) * math.cos(perp_angle)
        y1 = cy + (size/2) * math.sin(perp_angle)
        x2 = cx - (size/2) * math.cos(perp_angle)
        y2 = cy - (size/2) * math.sin(perp_angle)
        
        parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="2"/>')

def draw_parallelogram_scene(parts, width, height, mode):
    cx, cy = width / 2, height / 2

    if mode == 'lados_opuestos_iguales':
        title = "Propiedad: Lados Opuestos Iguales"
        w, h, shift = 300, 160, 60
        # A, B, C, D (counter-clockwise from bottom-left)
        pA = (cx - w/2 - shift/2, cy + h/2)
        pB = (cx + w/2 - shift/2, cy + h/2)
        pC = (cx + w/2 + shift/2, cy - h/2)
        pD = (cx - w/2 + shift/2, cy - h/2)
        points = [pA, pB, pC, pD]
        
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'], fill_opacity=0.05)
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-25, pA[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+25, pB[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+25, pC[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-25, pD[1]-15, "D", COLORS['vertices'], weight='bold'))
        
        # Tick marks for opposite sides
        # AB (bottom) and DC (top)
        draw_tick_mark(parts, pA, pB, count=1, color=COLORS['text'])
        draw_tick_mark(parts, pD, pC, count=1, color=COLORS['text'])
        
        # BC (right) and AD (left)
        draw_tick_mark(parts, pB, pC, count=2, color=COLORS['text'])
        draw_tick_mark(parts, pA, pD, count=2, color=COLORS['text'])
        
        # Footer Label
        parts.append(draw_label(cx, cy + h/2 + 60, "AB = CD  y  BC = AD", COLORS['text'], size=20, weight='bold'))
        return title

    return "Parallelogram"

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    
    parts = []
    # Background
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    
    title = draw_parallelogram_scene(parts, width, height, mode)
    
    # Title
    if title:
        parts.append(draw_label(width/2, 35, title, COLORS["vertices"], size=FONT_SIZE_TITLE, weight="bold"))
    
    parts.append('</svg>')
    
    # Write
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write("\n".join(parts))
    print(f"✅ Generated {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    generate_svg(args.mode, args.output)

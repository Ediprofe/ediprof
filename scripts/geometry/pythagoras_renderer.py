
import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.triangle_primitives import draw_triangle, draw_label, draw_angle_arc

# --- Configuration & Helpers ---
CANVAS_NAME = 'compound' # Standard 600x460
FONT_SIZE_LABEL = 20
FONT_SIZE_TITLE = 22

def draw_pythagoras_scene(parts, width, height, mode='concept_sides'):
    cx, cy = width / 2, height / 2

    # --- 1. Concept: Sides Identification ---
    if mode == 'concept_sides':
        title = "Identificando los Lados"
        
        # Right Triangle
        a = 150 # cateto height
        b = 200 # cateto base
        
        C = (cx - 80, cy + 60) # Right angle vertex
        A = (cx - 80, cy + 60 - a) # Top vertex
        B = (cx - 80 + b, cy + 60) # Right vertex
        
        parts.append(draw_triangle([A, B, C], stroke=COLORS["primary"], stroke_width=3, fill=COLORS["primary"], fill_opacity=0.05))
        
        # Right Angle Mark
        parts.append(f'<rect x="{C[0]}" y="{C[1]-20}" width="20" height="20" fill="none" stroke="{COLORS["text"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{C[0]+10}" cy="{C[1]-10}" r="2" fill="{COLORS["text"]}"/>')

        # Labels
        # Hipotenusa (c) - Slanted label
        mid_c = ((A[0]+B[0])/2, (A[1]+B[1])/2)
        parts.append(draw_label(mid_c[0]+20, mid_c[1]-20, "Hipotenusa (c)", COLORS["danger"], weight="bold"))
        
        # Cateto a (vertical)
        mid_a = ((A[0]+C[0])/2, (A[1]+C[1])/2)
        parts.append(draw_label(mid_a[0]-50, mid_a[1], "Cateto (a)", COLORS["text"]))
        
        # Cateto b (horizontal)
        mid_b = ((C[0]+B[0])/2, (C[1]+B[1])/2)
        parts.append(draw_label(mid_b[0], mid_b[1]+30, "Cateto (b)", COLORS["text"]))
        
        return title

    # --- 2. Concept: Squares Formula ---
    elif mode == 'concept_squares':
        title = "La Fórmula Clave"
        
        # Centered Triangle 3-4-5 scaled
        scale = 36 # Reduced scale slightly
        a = 3 * scale
        b = 4 * scale
        
        # Shift down to avoid cutting off top
        offset_y = 60
        
        C = (cx - 20, cy + offset_y)
        A = (cx - 20, cy + offset_y - a)
        B = (cx - 20 + b, cy + offset_y)
        
        parts.append(draw_triangle([A, B, C], stroke=COLORS["text"], stroke_width=2, fill=COLORS["text"], fill_opacity=0.05))
        
        # Square on a (left)
        parts.append(f'<rect x="{C[0]-a}" y="{C[1]-a}" width="{a}" height="{a}" fill="{COLORS["primary"]}" fill-opacity="0.2" stroke="{COLORS["primary"]}" stroke-width="2"/>')
        parts.append(draw_label(C[0]-a/2, C[1]-a/2, "a²", COLORS["primary"], size=24, weight="bold"))
        
        # Square on b (bottom)
        parts.append(f'<rect x="{C[0]}" y="{C[1]}" width="{b}" height="{b}" fill="{COLORS["secondary"]}" fill-opacity="0.2" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
        parts.append(draw_label(C[0]+b/2, C[1]+b/2, "b²", COLORS["secondary"], size=24, weight="bold"))
        
        # Square on c (diagonal) - This requires rotation or path
       
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        
        # Rotated -90deg: (dy, -dx) since in SVG y increases downwards, so "up" is negative y.
        # Vector AB = (b, a).
        # Perpendicular "upwards" and "leftwards" relative to AB direction?
        # A is top-left, B is bot-right. Diagonal goes down-right.
        # We want square to be top-right.
        # Normal vector nP should be (dy, -dx) = (a, -b).
        # Wait. A=(x, y-a), B=(x+b, y). 
        # Dx = b, Dy = a.
        # (dy, -dx) = (a, -b).
        # A is approx (280, 230). B is approx (420, 330).
        # A + (a, -b) -> x increases, y decreases (up-right). Correct.
        
        nP = (dy, -dx) 
        
        A_sq = (A[0] + nP[0], A[1] + nP[1])
        B_sq = (B[0] + nP[0], B[1] + nP[1])
        
        path_sq = f"M {A[0]} {A[1]} L {B[0]} {B[1]} L {B_sq[0]} {B_sq[1]} L {A_sq[0]} {A_sq[1]} Z"
        parts.append(f'<path d="{path_sq}" fill="{COLORS["danger"]}" fill-opacity="0.2" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        center_sq = ((A[0]+B_sq[0])/2, (A[1]+B_sq[1])/2)
        parts.append(draw_label(center_sq[0], center_sq[1], "c²", COLORS["danger"], size=24, weight="bold"))
        
        return title

    # --- 3. Example 1: Finding Hypotenuse (3-4-x) ---
    elif mode == 'example_3_4_5':
        title = "Hallando la Hipotenusa"
        
        scale = 50
        a, b = 3*scale, 4*scale
        
        C = (cx - b/2, cy + a/2)
        A = (cx - b/2, cy - a/2)
        B = (cx + b/2, cy + a/2)
        
        parts.append(draw_triangle([A, B, C], stroke=COLORS["primary"], stroke_width=3))
        
        parts.append(draw_label((A[0]+C[0])/2 - 20, (A[1]+C[1])/2, "3", COLORS["text"]))
        parts.append(draw_label((C[0]+B[0])/2, (C[1]+B[1])/2 + 25, "4", COLORS["text"]))
        parts.append(draw_label((A[0]+B[0])/2 + 20, (A[1]+B[1])/2 - 20, "?", COLORS["danger"], size=26, weight="bold"))

        return title

    # --- 4. Example 2: Ladder ---
    elif mode == 'example_ladder':
        title = "Problema de la Escalera"
        
        ground_y = cy + 100
        wall_x = cx - 80
        
        parts.append(f'<line x1="{wall_x}" y1="{ground_y+20}" x2="{width-50}" y2="{ground_y+20}" stroke="{COLORS["grid"]}" stroke-width="2"/>') # Ground
        parts.append(f'<line x1="{wall_x}" y1="{ground_y+20}" x2="{wall_x}" y2="50" stroke="{COLORS["text"]}" stroke-width="4"/>') # Wall
        
        base_dist = 120 # Represents 6m
        ladder_len = 200 # Represents 10m (20 px per m)
        
        # Calculate height: sqrt(200^2 - 120^2) = sqrt(40000 - 14400) = sqrt(25600) = 160
        height_px = 160
        
        base_pt = (wall_x + base_dist, ground_y + 20)
        top_pt = (wall_x, ground_y + 20 - height_px)
        
        # Ladder
        parts.append(f'<line x1="{base_pt[0]}" y1="{base_pt[1]}" x2="{top_pt[0]}" y2="{top_pt[1]}" stroke="{COLORS["secondary"]}" stroke-width="8" stroke-linecap="round"/>')
        
        # Dashed height
        # parts.append(f'<line x1="{wall_x}" y1="{base_pt[1]}" x2="{wall_x}" y2="{top_pt[1]}" stroke="{COLORS["danger"]}" stroke-width="3" stroke-dasharray="4,4"/>')
        
        parts.append(draw_label(wall_x - 30, (base_pt[1]+top_pt[1])/2, "h = ?", COLORS["danger"], weight="bold"))
        parts.append(draw_label((wall_x+base_pt[0])/2, base_pt[1]+30, "6 m", COLORS["text"]))
        parts.append(draw_label((wall_x+base_pt[0])/2 + 20, (base_pt[1]+top_pt[1])/2 - 20, "10 m", COLORS["secondary"], weight="bold"))

        return title

    # --- 5. Example 3: TV ---
    elif mode == 'example_tv':
        title = "Diagonal del TV"
        
        # Rectangular TV
        w_tv = 240 # prop 4
        h_tv = 180 # prop 3
        
        tv_x = cx - w_tv/2
        tv_y = cy - h_tv/2
        
        parts.append(f'<rect x="{tv_x}" y="{tv_y}" width="{w_tv}" height="{h_tv}" fill="#111" stroke="#333" stroke-width="5" rx="8"/>')
        parts.append(f'<rect x="{tv_x+10}" y="{tv_y+10}" width="{w_tv-20}" height="{h_tv-20}" fill="#222" stroke="none"/>') # Screen area
        
        # Diagonal
        parts.append(f'<line x1="{tv_x+10}" y1="{tv_y+h_tv-10}" x2="{tv_x+w_tv-10}" y2="{tv_y+10}" stroke="{COLORS["danger"]}" stroke-width="3" stroke-dasharray="6,6"/>')
        
        # Labels
        parts.append(draw_label(cx, tv_y + h_tv + 30, 'Ancho = 40"', COLORS["text"]))
        parts.append(draw_label(tv_x - 40, cy, 'h = ?', COLORS["primary"], weight="bold"))
        parts.append(draw_label(cx, cy, '50"', COLORS["danger"], size=24, weight="bold"))

        return title

    # --- 6. Summary: Add vs Sub ---
    elif mode == 'summary_visual':
        # title = "Resumen: ¿Sumar o Restar?"
        title = ""
        
        # Split screen
        # Left: Finding c (Sum)
        cx_l = width * 0.25
        cy_l = height / 2 + 20
        
        scale = 35
        pA = (cx_l - 1.5*scale, cy_l + 2*scale) # Bottom Left
        pB = (cx_l + 1.5*scale, cy_l + 2*scale) # Bottom right (actually right angle is here?) No.
        # Let's make right angle at bottom-left for simplicity
        pC = (cx_l - 1.5*scale, cy_l - 2*scale) # Top Left
        
        # Sum case: Know legs, find Hyp
        parts.append(draw_triangle([pA, pB, pC], stroke=COLORS["text_light"], stroke_width=2))
        parts.append(f'<rect x="{pA[0]}" y="{pA[1]-15}" width="15" height="15" fill="none" stroke="{COLORS["text_light"]}"/>')
        
        parts.append(draw_label(pA[0]-15, (pA[1]+pC[1])/2, "a", COLORS["text_light"], size=14))
        parts.append(draw_label((pA[0]+pB[0])/2, pA[1]+15, "b", COLORS["text_light"], size=14))
        parts.append(draw_label((pC[0]+pB[0])/2+10, (pC[1]+pB[1])/2-10, "?", COLORS["danger"], size=20, weight="bold"))
        
        parts.append(draw_label(cx_l, cy_l + 90, "Buscar Hipotenusa", COLORS["text"], size=16, weight="bold"))
        parts.append(f'<path d="M {cx_l-10} {cy_l+115} L {cx_l+10} {cy_l+115} M {cx_l} {cy_l+105} L {cx_l} {cy_l+125}" stroke="{COLORS["primary"]}" stroke-width="4"/>') # Plus Sign
        parts.append(draw_label(cx_l, cy_l + 145, "SUMAR", COLORS["primary"], weight="bold"))


        # Right: Finding leg (Sub)
        cx_r = width * 0.75
        
        pAr = (cx_r - 1.5*scale, cy_l + 2*scale)
        pBr = (cx_r + 1.5*scale, cy_l + 2*scale)
        pCr = (cx_r - 1.5*scale, cy_l - 2*scale)
        
        parts.append(draw_triangle([pAr, pBr, pCr], stroke=COLORS["text_light"], stroke_width=2))
        parts.append(f'<rect x="{pAr[0]}" y="{pAr[1]-15}" width="15" height="15" fill="none" stroke="{COLORS["text_light"]}"/>')

        parts.append(draw_label(pAr[0]-15, (pAr[1]+pCr[1])/2, "?", COLORS["danger"], size=20, weight="bold"))
        parts.append(draw_label((pAr[0]+pBr[0])/2, pAr[1]+15, "b", COLORS["text_light"], size=14))
        parts.append(draw_label((pCr[0]+pBr[0])/2+10, (pCr[1]+pBr[1])/2-10, "c", COLORS["text_light"], size=14))
        
        parts.append(draw_label(cx_r, cy_l + 90, "Buscar Cateto", COLORS["text"], size=16, weight="bold"))
        parts.append(f'<line x1="{cx_r-10}" y1="{cy_l+115}" x2="{cx_r+10}" y2="{cy_l+115}" stroke="{COLORS["danger"]}" stroke-width="4"/>') # Minus Sign
        parts.append(draw_label(cx_r, cy_l + 145, "RESTAR", COLORS["danger"], weight="bold"))
        
        # Divider
        parts.append(f'<line x1="{width/2}" y1="80" x2="{width/2}" y2="{height-40}" stroke="{COLORS["grid"]}" stroke-dasharray="4"/>')

        return title

    return "Pythagoras Scene"

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    
    parts = []
    # Background
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    
    title = draw_pythagoras_scene(parts, width, height, mode)
    
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

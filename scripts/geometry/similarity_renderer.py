
import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.layouts import side_by_side, side_by_side_asymmetric, get_title_position
from core.triangle_primitives import draw_triangle, draw_angle_arc, draw_label, transform_points

def generate_svg_main(mode, output_path):
    # Use standardized Compound canvas (600x460) for comparison scenes by default
    config_name = 'compound'
    canvas_cfg = get_canvas_config(config_name)
    width = canvas_cfg['width']
    height = canvas_cfg['height']
    
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>')

    # --- Styling Constants ---
    FONT_SIZE_TITLE = 22
    
    # Common colors
    C_SIDE1 = COLORS['primary']
    C_SIDE2 = COLORS['medianas']
    C_SIDE3 = COLORS['danger']
    C_ANG1 = COLORS['purple']
    C_ANG2 = COLORS['highlight']
    C_ANG3 = COLORS['cyan']

    scene_title = ""

    if mode == 'concept':
        scene_title = "Misma forma, distinto tamaño"
        raw = [(0,0), (80,0), (30,-80)]
        
        off1, off2 = side_by_side_asymmetric(config_name, 80*1.3, 80*1.3, 80*2.2, 80*2.2, gap=80)
        
        T1 = transform_points(raw, 1.3, off1)
        T2 = transform_points(raw, 2.2, off2)
        
        parts.append(draw_triangle(T1, stroke_colors=[C_SIDE1, C_SIDE2, C_SIDE3]))
        parts.append(draw_triangle(T2, stroke_colors=[C_SIDE1, C_SIDE2, C_SIDE3]))
        
        for T, r in [(T1, 30), (T2, 45)]:
            parts.append(draw_angle_arc(T[0], T[1], T[2], color=C_ANG1, radius=r))
            parts.append(draw_angle_arc(T[1], T[2], T[0], color=C_ANG2, radius=r))
            parts.append(draw_angle_arc(T[2], T[0], T[1], color=C_ANG3, radius=r))

    elif mode == 'criterion_aa':
        scene_title = "Criterio AA: Dos ángulos iguales"
        raw = [(0,0), (80,0), (25,-90)]
        off1, off2 = side_by_side_asymmetric(config_name, 80*1.3, 90*1.3, 80*2.0, 90*2.0, gap=100)
        
        T1 = transform_points(raw, 1.3, off1)
        T2 = transform_points(raw, 2.0, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['auxiliary']))
        parts.append(draw_triangle(T2, stroke=COLORS['auxiliary']))
        
        for T, r in [(T1, 30), (T2, 45)]:
            parts.append(draw_angle_arc(T[0], T[1], T[2], color=C_ANG1, radius=r))
            parts.append(draw_angle_arc(T[1], T[2], T[0], color=C_ANG2, radius=r))

    elif mode == 'criterion_lll_sim':
        scene_title = "Criterio LLL: Lados Proporcionales"
        raw = [(0,0), (90,0), (30,-70)]
        off1, off2 = side_by_side_asymmetric(config_name, 90*1.3, 70*1.3, 90*2.0, 70*2.0, gap=100)
        
        T1 = transform_points(raw, 1.3, off1)
        T2 = transform_points(raw, 2.0, off2)
        
        parts.append(draw_triangle(T1, stroke_colors=[C_SIDE1, C_SIDE2, C_SIDE3]))
        parts.append(draw_triangle(T2, stroke_colors=[C_SIDE1, C_SIDE2, C_SIDE3]))
        
        m1 = ((T1[0][0]+T1[1][0])/2, T1[0][1] + 25)
        m2 = ((T2[0][0]+T2[1][0])/2, T2[0][1] + 25)
        
        parts.append(draw_label(m1[0], m1[1], "a", C_SIDE1, size=20))
        parts.append(draw_label(m2[0], m2[1], "k·a", C_SIDE1, size=20))

    elif mode == 'criterion_lal_sim':
        scene_title = "LAL: Lados Prop. y Ángulo Igual"
        raw = [(0,0), (80,0), (20,-85)]
        off1, off2 = side_by_side_asymmetric(config_name, 80*1.3, 85*1.3, 80*2.0, 85*2.0, gap=100)
        
        T1 = transform_points(raw, 1.3, off1)
        T2 = transform_points(raw, 2.0, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['auxiliary']))
        parts.append(draw_triangle(T2, stroke=COLORS['auxiliary']))
        
        parts.append(f'<line x1="{T1[0][0]:.2f}" y1="{T1[0][1]:.2f}" x2="{T1[1][0]:.2f}" y2="{T1[1][1]:.2f}" stroke="{C_SIDE1}" stroke-width="5"/>')
        parts.append(f'<line x1="{T2[0][0]:.2f}" y1="{T2[0][1]:.2f}" x2="{T2[1][0]:.2f}" y2="{T2[1][1]:.2f}" stroke="{C_SIDE1}" stroke-width="5"/>')
        
        parts.append(f'<line x1="{T1[2][0]:.2f}" y1="{T1[2][1]:.2f}" x2="{T1[0][0]:.2f}" y2="{T1[0][1]:.2f}" stroke="{C_SIDE3}" stroke-width="5"/>')
        parts.append(f'<line x1="{T2[2][0]:.2f}" y1="{T2[2][1]:.2f}" x2="{T2[0][0]:.2f}" y2="{T2[0][1]:.2f}" stroke="{C_SIDE3}" stroke-width="5"/>')
        
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], color=C_ANG1, radius=30, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], color=C_ANG1, radius=45, fill_opacity=0.4))

    elif mode == 'example_ratio':
        scene_title = "Ejemplo: Razón de semejanza k=3"
        UNIT = 22
        raw = [(0,0), (3*UNIT,0), (0,-4*UNIT)]
        w1, h1 = 3*UNIT, 4*UNIT
        w2, h2 = 9*UNIT, 12*UNIT
        
        off1, off2 = side_by_side_asymmetric(config_name, w1, h1, w2, h2, gap=100)
        
        T1 = transform_points(raw, 1.0, off1)
        T2 = transform_points(raw, 3.0, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['primary']))
        parts.append(draw_triangle(T2, stroke=COLORS['primary']))
        
        parts.append(draw_label((T1[0][0]+T1[1][0])/2, T1[0][1]+25, "3", COLORS['text'], size=20))
        parts.append(draw_label(T1[0][0]-20, (T1[0][1]+T1[2][1])/2, "4", COLORS['text'], size=20))
        parts.append(draw_label(T1[1][0]+20, (T1[1][1]+T1[2][1])/2 -5, "5", COLORS['text'], size=20))

        parts.append(draw_label((T2[0][0]+T2[1][0])/2, T2[0][1]+30, "9", COLORS['text'], size=20))
        parts.append(draw_label(T2[0][0]-25, (T2[0][1]+T2[2][1])/2, "12", COLORS['text'], size=20))
        parts.append(draw_label(T2[1][0]+30, (T2[1][1]+T2[2][1])/2 -5, "15", COLORS['text'], size=20))
        
        mid_x = (off1[0] + w1 + off2[0]) / 2
        arrow_y = height/2 - 20 
        
        parts.append(f'<path d="M {mid_x-40} {arrow_y} L {mid_x+40} {arrow_y}" stroke="{COLORS["highlight"]}" stroke-width="3" marker-end="url(#arrow)"/>')
        parts.append(f'<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="3" orient="auto"><path d="M0,0 L0,6 L10,3 z" fill="{COLORS["highlight"]}" /></marker></defs>')
        parts.append(draw_label(mid_x, arrow_y - 25, "k = 3", color=COLORS["highlight"], size=24, weight="bold"))

    elif mode == 'example_find_side':
        scene_title = "Hallar x con proporciones"
        UNIT = 35
        raw = [(0,0), (4*UNIT,0), (1.5*UNIT,-3.5*UNIT)]
        k_factor = 2.0
        w1, h1 = 4*UNIT, 3.5*UNIT
        w2, h2 = 8*UNIT, 7.0*UNIT
        
        # Note: logic swapped in example_find_side in original: T1 was big (T2 in list), T2 was small.
        # Original: T1=1.0, T2=k. BUT T2 was drawn using T2 transform(raw, 1.0)??
        # Checked original: T1 = transform(raw, 1.0), T2 = transform(raw, k).
        # T1 drawn second (medianas).
        
        off1, off2 = side_by_side_asymmetric(config_name, w1, h1, w2, h2, gap=60)
        
        T1 = transform_points(raw, 1.0, off1) 
        T2 = transform_points(raw, k_factor, off2) 
        
        parts.append(draw_triangle(T2, stroke=COLORS['primary'])) 
        parts.append(draw_triangle(T1, stroke=COLORS['medianas'])) 
        
        parts.append(draw_label(T2[0][0]-15, T2[0][1]+10, "A", COLORS["vertices"], size=18, weight="bold"))
        parts.append(draw_label(T2[1][0]+15, T2[1][1]+10, "B", COLORS["vertices"], size=18, weight="bold"))
        parts.append(draw_label(T2[2][0], T2[2][1]-25, "C", COLORS["vertices"], size=18, weight="bold"))

        parts.append(draw_label(T1[0][0]-15, T1[0][1]+10, "D", COLORS["vertices"], size=18, weight="bold"))
        parts.append(draw_label(T1[1][0]+15, T1[1][1]+10, "E", COLORS["vertices"], size=18, weight="bold"))
        parts.append(draw_label(T1[2][0], T1[2][1]-25, "F", COLORS["vertices"], size=18, weight="bold"))
        
        parts.append(draw_label((T2[0][0]+T2[1][0])/2, T2[0][1]+30, "AB = 8", COLORS['primary'], size=20))
        mid_bc = ((T2[1][0]+T2[2][0])/2, (T2[1][1]+T2[2][1])/2)
        parts.append(draw_label(mid_bc[0]+25, mid_bc[1], "x", COLORS['danger'], size=30, weight="bold"))
        
        parts.append(draw_label((T1[0][0]+T1[1][0])/2, T1[0][1]+30, "DE = 4", COLORS['medianas'], size=20))
        mid_ef = ((T1[1][0]+T1[2][0])/2, (T1[1][1]+T1[2][1])/2)
        parts.append(draw_label(mid_ef[0]+35, mid_ef[1], "EF = 6", COLORS['medianas'], size=20))

    elif mode == 'area_ratio':
        scene_title = "Razón de Áreas = k²"
        UNIT = 24
        raw = [(0,0), (3*UNIT,0), (0,-4*UNIT)]
        k = 2.0
        
        w1, h1 = 3*UNIT, 4*UNIT
        w2, h2 = 6*UNIT, 8*UNIT
        
        # Centering calculations
        gap = 160
        off1, off2 = side_by_side_asymmetric(config_name, w1, h1, w2, h2, gap=gap)
        
        T1 = transform_points(raw, 1.0, off1)
        T2 = transform_points(raw, k, off2)
        
        # Right angle markers (Corrected to vertex 0)
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], color=COLORS['text'], radius=15, is_right_angle=True))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], color=COLORS['text'], radius=20, is_right_angle=True))

        # Triangles with fill
        parts.append(draw_triangle(T1, stroke=COLORS['primary'], fill=COLORS['primary'], stroke_width=2, fill_opacity=0.15))
        parts.append(draw_triangle(T2, stroke=COLORS['medianas'], fill=COLORS['medianas'], stroke_width=2, fill_opacity=0.15))
        
        # Labels T1
        parts.append(draw_label((T1[0][0]+T1[1][0])/2, T1[0][1]+25, "b = 3", COLORS['text'], size=18))
        parts.append(draw_label(T1[0][0]-30, (T1[0][1]+T1[2][1])/2, "h = 4", COLORS['text'], size=18))
        # Centroid Area Label
        c1x = (T1[0][0] + T1[1][0] + T1[2][0]) / 3
        c1y = (T1[0][1] + T1[1][1] + T1[2][1]) / 3
        parts.append(draw_label(c1x + 5, c1y + 5, "A=6", COLORS['primary'], size=20, weight="bold"))
        
        # Labels T2
        parts.append(draw_label((T2[0][0]+T2[1][0])/2, T2[0][1]+25, "b = 6", COLORS['text'], size=18))
        parts.append(draw_label(T2[0][0]-35, (T2[0][1]+T2[2][1])/2, "h = 8", COLORS['text'], size=18))
        
        c2x = (T2[0][0] + T2[1][0] + T2[2][0]) / 3
        c2y = (T2[0][1] + T2[1][1] + T2[2][1]) / 3
        parts.append(draw_label(c2x + 10, c2y + 10, "A=24", COLORS['medianas'], size=24, weight="bold"))

        # Center graphic (Arrow and k)
        mx = off1[0] + w1 + gap/2
        my = height / 2 - 20
        
        # Elegant arrow
        arrow_w = 60
        parts.append(f'<defs><marker id="arrow_area" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{COLORS["highlight"]}" /></marker></defs>')
        parts.append(f'<line x1="{mx - arrow_w/2}" y1="{my}" x2="{mx + arrow_w/2}" y2="{my}" stroke="{COLORS["highlight"]}" stroke-width="3" marker-end="url(#arrow_area)"/>')
        
        parts.append(draw_label(mx, my - 25, "k = 2", COLORS['highlight'], size=22, weight='bold'))
        
        # Explanation text (more spacious)
        parts.append(draw_label(mx, my + 35, "Área × k²", COLORS['text'], size=18))
        parts.append(draw_label(mx, my + 60, "6 · 2² = 24", COLORS['danger'], size=20, weight='bold'))

    # Title
    tpos = get_title_position(config_name)
    parts.append(draw_label(tpos[0], tpos[1], scene_title, color=COLORS["vertices"], size=FONT_SIZE_TITLE, weight="bold"))
    
    parts.append('</svg>')
    
    with open(output_path, 'w') as f:
        f.write("\n".join(parts))
    print(f"✅ Generated {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    generate_svg_main(args.mode, args.output)


import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.layouts import side_by_side
from core.triangle_primitives import draw_triangle, draw_label, draw_angle_arc

# --- Configuration & Helpers ---
CANVAS_NAME = 'compound' # Standard 600x460
FONT_SIZE_LABEL = 20
FONT_SIZE_TITLE = 22

def get_intersection(p1, v1, p2, v2):
    """
    Returns intersection of line P1+t*V1 and P2+u*V2.
    Points are (x,y) tuples. Vectors are (dx,dy).
    """
    x1, y1 = p1
    dx1, dy1 = v1
    x2, y2 = p2
    dx2, dy2 = v2
    
    # Solve: x1 + t*dx1 = x2 + u*dx2
    #        y1 + t*dy1 = y2 + u*dy2
    
    # t*dx1 - u*dx2 = x2 - x1
    # t*dy1 - u*dy2 = y2 - y1
    
    det = dx1 * (-dy2) - (-dx2) * dy1
    if abs(det) < 1e-9: return None # Parallel
    
    rhs_x = x2 - x1
    rhs_y = y2 - y1
    
    t = (rhs_x * (-dy2) - (-dx2) * rhs_y) / det
    
    return (x1 + t * dx1, y1 + t * dy1)

def draw_thales_lines(parts, width, height, mode='concept'):
    """
    Draws the relevant composition for Thales Theorem with parallel lines.
    """
    cx, cy = width / 2, height / 2
    
    # --- 1. General Concept (3 parallels, 2 transversals) ---
    if mode == 'general_concept':
        scene_title = "Teorema General de Tales"
        
        spacing = 80
        y_lines = [cy - spacing, cy, cy + spacing]
        
        t1_p = (cx - 100, cy - spacing - 50) 
        t1_v = (60, 200) 
        
        t2_p = (cx + 100, cy - spacing - 50)
        t2_v = (-40, 200) 
        
        ps_left = []
        ps_right = []
        
        for i, y in enumerate(y_lines):
            # Draw Parallel Line
            parts.append(f'<line x1="50" y1="{y}" x2="{width-50}" y2="{y}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
            parts.append(f'<text x="{width-40}" y="{y+5}" fill="{COLORS["medianas"]}" font-size="16">L{i+1}</text>')
            
            # Intersect T1
            i1 = get_intersection(t1_p, t1_v, (0,y), (1,0))
            ps_left.append(i1)
            
            # Intersect T2
            i2 = get_intersection(t2_p, t2_v, (0,y), (1,0))
            ps_right.append(i2)
            
        # Draw Transversals
        def extend(p1, p2, factor=0.2):
            dx, dy = p2[0]-p1[0], p2[1]-p1[1]
            return (p1[0]-dx*factor, p1[1]-dy*factor), (p2[0]+dx*factor, p2[1]+dy*factor)
            
        l1_start, l1_end = extend(ps_left[0], ps_left[-1], 0.4)
        l2_start, l2_end = extend(ps_right[0], ps_right[-1], 0.4)
        
        parts.append(f'<line x1="{l1_start[0]:.2f}" y1="{l1_start[1]:.2f}" x2="{l1_end[0]:.2f}" y2="{l1_end[1]:.2f}" stroke="{COLORS["primary"]}" stroke-width="3"/>')
        parts.append(f'<line x1="{l2_start[0]:.2f}" y1="{l2_start[1]:.2f}" x2="{l2_end[0]:.2f}" y2="{l2_end[1]:.2f}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        
        # Labels for Segments
        parts.append(draw_label((ps_left[0][0]+ps_left[1][0])/2 - 15, (ps_left[0][1]+ps_left[1][1])/2, "A", COLORS["text"]))
        parts.append(draw_label((ps_left[1][0]+ps_left[2][0])/2 - 15, (ps_left[1][1]+ps_left[2][1])/2, "B", COLORS["text"]))
        
        parts.append(draw_label((ps_right[0][0]+ps_right[1][0])/2 + 15, (ps_right[0][1]+ps_right[1][1])/2, "A'", COLORS["text"]))
        parts.append(draw_label((ps_right[1][0]+ps_right[2][0])/2 + 15, (ps_right[1][1]+ps_right[2][1])/2, "B'", COLORS["text"]))

        # Equation
        eq_y = height - 40
        parts.append(f'<rect x="{cx-100}" y="{eq_y-25}" width="200" height="50" rx="8" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        parts.append(f'<text x="{cx}" y="{eq_y+8}" font-family="KaTeX_Main, Times, serif" font-size="24" fill="{COLORS["text"]}" text-anchor="middle">A/B = A\'/B\'</text>')

        return scene_title

    # --- 2. Example 1: Shelves (Repisa) ---
    elif mode == 'example_shelves':
        scene_title = "Ejemplo: Estantes"
        
        spacing_unit = 25
        h1 = 2 * spacing_unit
        h2 = 3.2 * spacing_unit
        
        y_start = cy - (h1+h2)/2
        y1 = y_start
        y2 = y_start + h1
        y3 = y_start + h1 + h2
        ys = [y1, y2, y3]
        
        for y in ys:
            parts.append(f'<line x1="100" y1="{y}" x2="{width-100}" y2="{y}" stroke="{COLORS["text_light"]}" stroke-width="4" stroke-linecap="round"/>')
            
        lx = cx - 120
        rx = cx + 120
        
        p1_top = (lx - 30, y1 - 20)
        p1_bot = (lx + 30, y3 + 20)
        parts.append(f'<line x1="{p1_top[0]}" y1="{p1_top[1]}" x2="{p1_bot[0]}" y2="{p1_bot[1]}" stroke="{COLORS["primary"]}" stroke-width="6"/>')

        p2_top = (rx + 40, y1 - 20)
        p2_bot = (rx - 20, y3 + 20)
        parts.append(f'<line x1="{p2_top[0]}" y1="{p2_top[1]}" x2="{p2_bot[0]}" y2="{p2_bot[1]}" stroke="{COLORS["danger"]}" stroke-width="6"/>')

        def get_seg_mid(p_start, p_end, y_val_a, y_val_b):
            def get_x(y):
                ratio = (y - p_start[1]) / (p_end[1] - p_start[1])
                return p_start[0] + ratio * (p_end[0] - p_start[0])
            x_a = get_x(y_val_a)
            x_b = get_x(y_val_b)
            return ((x_a+x_b)/2, (y_val_a+y_val_b)/2)

        m1 = get_seg_mid(p1_top, p1_bot, y1, y2)
        m2 = get_seg_mid(p1_top, p1_bot, y2, y3)
        parts.append(draw_label(m1[0]-35, m1[1], "50", COLORS['text'], weight='bold'))
        parts.append(draw_label(m2[0]-35, m2[1], "80", COLORS['text'], weight='bold'))
        
        m3 = get_seg_mid(p2_top, p2_bot, y1, y2)
        m4 = get_seg_mid(p2_top, p2_bot, y2, y3)
        parts.append(draw_label(m3[0]+35, m3[1], "60", COLORS['text'], weight='bold'))
        parts.append(draw_label(m4[0]+35, m4[1], "x", COLORS['danger'], size=24, weight='bold'))
        
        return scene_title

    # --- 3. Geometric Problems (Triangles) ---
    elif mode in ['triangle_concept', 'example_triangle_numeric', 'example_reciprocal', 'example_base_trap']:
        if mode == 'triangle_concept':
            scene_title = "Tales en un Triángulo"
            labels = {'AD': 'AD', 'DB': 'DB', 'AE': 'AE', 'EC': 'EC', 'DE': 'DE', 'BC': 'BC'}
            vals = None
            is_reciprocal = False
        elif mode == 'example_reciprocal':
            scene_title = "¿Son Paralelas?"
            labels = {'AD': '3', 'DB': '6', 'AE': '4', 'EC': '8', 'DE': '?', 'BC': ''}
            vals = {'AD': 3, 'DB': 6}
            is_reciprocal = True
        elif mode == 'example_base_trap':
            scene_title = "¡Cuidado con la Base!"
            # AD=2, DB=3. Bases 4 and x.
            labels = {'AD': '2', 'DB': '3', 'AE': '', 'EC': '', 'DE': '4', 'BC': 'x'}
            vals = {'AD': 2, 'DB': 3}
            is_reciprocal = False
        else:
            scene_title = "Ejemplo: Triángulo"
            labels = {'AD': '4', 'DB': '6', 'AE': '8', 'EC': 'x', 'DE': '', 'BC': ''}
            vals = {'AD': 4, 'DB': 6}
            is_reciprocal = False

        A = (cx, 110)
        
        split_ratio = 0.4 if vals is None else (vals['AD'] / (vals['AD'] + vals['DB']))
        
        total_h = 300 
        half_base = 180
        
        B = (cx - half_base, A[1] + total_h)
        C = (cx + half_base, A[1] + total_h)
        
        D = (A[0] + (B[0]-A[0])*split_ratio, A[1] + (B[1]-A[1])*split_ratio)
        E = (A[0] + (C[0]-A[0])*split_ratio, A[1] + (C[1]-A[1])*split_ratio)
        
        parts.append(draw_triangle([A, B, C], stroke=COLORS["primary"], stroke_width=3))
        
        # Parallel Line
        stroke_line = COLORS["highlight"]
        dash_line = ""
        if is_reciprocal:
            stroke_line = COLORS["accent"] # Red for "Is it?" question
            dash_line = 'stroke-dasharray="8,8"'
        elif mode == 'example_base_trap':
            stroke_line = COLORS["danger"]
            
        parts.append(f'<line x1="{D[0]:.2f}" y1="{D[1]:.2f}" x2="{E[0]:.2f}" y2="{E[1]:.2f}" stroke="{stroke_line}" stroke-width="4" {dash_line}/>')
        
        parts.append(draw_label(A[0], A[1]-20, "A", COLORS["vertices"]))
        parts.append(draw_label(B[0]-20, B[1], "B", COLORS["vertices"]))
        parts.append(draw_label(C[0]+20, C[1], "C", COLORS["vertices"]))
        parts.append(draw_label(D[0]-25, D[1], "D", COLORS["vertices"]))
        parts.append(draw_label(E[0]+25, E[1], "E", COLORS["vertices"]))
        
        parts.append(draw_label((A[0]+D[0])/2 - 15, (A[1]+D[1])/2, labels['AD'], COLORS["text_light"]))
        parts.append(draw_label((D[0]+B[0])/2 - 15, (D[1]+B[1])/2, labels['DB'], COLORS["text_light"]))
        
        if labels['AE']:
            parts.append(draw_label((A[0]+E[0])/2 + 15, (A[1]+E[1])/2, labels['AE'], COLORS["text_light"]))
        if labels['EC']:
            col_ec = COLORS['danger'] if mode == 'example_triangle_numeric' else COLORS["text_light"]
            parts.append(draw_label((E[0]+C[0])/2 + 15, (E[1]+C[1])/2, labels['EC'], col_ec, weight='bold'))
            
        # Base Labels
        if labels['DE']:
             mid_de = ((D[0]+E[0])/2, (D[1]+E[1])/2)
             parts.append(draw_label(mid_de[0], mid_de[1]-15, labels['DE'], COLORS["danger"], weight="bold"))
        if labels['BC']:
            # mid_bc is width/2, B[1]
             mid_bc = (cx, B[1])
             parts.append(draw_label(mid_bc[0], mid_bc[1]+15, labels['BC'], COLORS["danger"], weight="bold"))

        if not is_reciprocal and mode != 'example_base_trap':
            parts.append(f'<defs><marker id="arrow_par" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{COLORS["highlight"]}" /></marker></defs>')
            mid_de = ((D[0]+E[0])/2, (D[1]+E[1])/2)
            mid_bc = ((B[0]+C[0])/2, (B[1]+C[1])/2)
            parts.append(f'<line x1="{mid_de[0]-5}" y1="{mid_de[1]}" x2="{mid_de[0]+5}" y2="{mid_de[1]}" stroke="{COLORS["highlight"]}" marker-end="url(#arrow_par)"/>')
            parts.append(f'<line x1="{mid_bc[0]-5}" y1="{mid_bc[1]}" x2="{mid_bc[0]+5}" y2="{mid_bc[1]}" stroke="{COLORS["highlight"]}" marker-end="url(#arrow_par)"/>')
        
        if mode == 'example_base_trap':
             off = 40
             bx = B[0] - off
             ax = A[0] - off * 1.5 
             parts.append(f'<path d="M {A[0]-50} {A[1]} L {A[0]-60} {A[1]} L {B[0]-60} {B[1]} L {B[0]-50} {B[1]}" fill="none" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
             mid_brack = ((A[0]-60 + B[0]-60)/2, (A[1]+B[1])/2)
             parts.append(draw_label(mid_brack[0]-15, mid_brack[1], "Total = 5", COLORS["secondary"], weight="bold"))

        elif is_reciprocal:
            mid_de = ((D[0]+E[0])/2, (D[1]+E[1])/2)
            parts.append(draw_label(mid_de[0], mid_de[1]-15, "?", COLORS["accent"], size=24, weight="bold"))

        return scene_title

    # --- 4. Shadows (Pyramids) ---
    elif mode == 'example_shadows':
        scene_title = "Semejanza por Sombras"
        ground_y = height - 60
        parts.append(f'<line x1="20" y1="{ground_y}" x2="{width-20}" y2="{ground_y}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        
        s_cx = 100 
        s_h = 80   
        s_w = s_h * (2 / 1.5) 
        
        stick_top = (s_cx, ground_y - s_h)
        stick_base = (s_cx, ground_y)
        stick_shadow_end = (s_cx + s_w, ground_y)
        
        p_cx = 380 
        p_h = 160  
        p_w = p_h * (2 / 1.5) 
        
        pyr_top = (p_cx, ground_y - p_h)
        pyr_base_center = (p_cx, ground_y)
        pyr_shadow_end = (p_cx + p_w, ground_y)
        
        parts.append(draw_triangle([stick_top, stick_base, stick_shadow_end], stroke=COLORS["primary"], fill=COLORS["primary"], fill_opacity=0.1))
        parts.append(f'<line x1="{stick_top[0]}" y1="{stick_top[1]}" x2="{stick_base[0]}" y2="{stick_base[1]}" stroke="{COLORS["text"]}" stroke-width="4"/>') 
        
        pyr_left = (p_cx - 50, ground_y)
        pyr_right = (p_cx + 50, ground_y)
        parts.append(f'<path d="M {pyr_left[0]} {pyr_left[1]} L {pyr_top[0]} {pyr_top[1]} L {pyr_right[0]} {pyr_right[1]} Z" fill="none" stroke="{COLORS["text"]}" stroke-width="2"/>')
        
        parts.append(draw_triangle([pyr_top, pyr_base_center, pyr_shadow_end], stroke=COLORS["secondary"], fill=COLORS["secondary"], fill_opacity=0.1))
        parts.append(f'<line x1="{pyr_top[0]}" y1="{pyr_top[1]}" x2="{pyr_base_center[0]}" y2="{pyr_base_center[1]}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="4,4"/>') 
        
        parts.append(f'<line x1="{stick_top[0]}" y1="{stick_top[1]}" x2="{stick_shadow_end[0]}" y2="{stick_shadow_end[1]}" stroke="{COLORS["yellow_dark"]}" stroke-width="2" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{pyr_top[0]}" y1="{pyr_top[1]}" x2="{pyr_shadow_end[0]}" y2="{pyr_shadow_end[1]}" stroke="{COLORS["yellow_dark"]}" stroke-width="2" stroke-dasharray="2,2"/>')
        
        parts.append(draw_label(s_cx - 20, ground_y - s_h/2, "1.5", COLORS["text"]))
        parts.append(draw_label(s_cx + s_w/2, ground_y + 20, "2 m", COLORS["text"]))
        
        parts.append(draw_label(p_cx - 15, ground_y - p_h/2, "H=?", COLORS["danger"], weight='bold'))
        parts.append(draw_label(p_cx + p_w/2, ground_y + 20, "180 m", COLORS["text"]))
        
        parts.append(f'<circle cx="50" cy="50" r="20" fill="{COLORS["yellow_dark"]}" />')
        
        return scene_title
    
    # --- 5. Division of Segment ---
    elif mode == 'example_segment_division':
        scene_title = "División de un Segmento"
        
        start_x = 100
        end_x = 400
        line_y = cy + 100
        
        A = (start_x, line_y)
        B = (end_x, line_y)
        
        ray_len = 350
        angle_rad = math.radians(35)
        AX_end = (start_x + ray_len * math.cos(angle_rad), line_y - ray_len * math.sin(angle_rad))
        
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{COLORS["primary"]}" stroke-width="4"/>')
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{AX_end[0]:.2f}" y2="{AX_end[1]:.2f}" stroke="{COLORS["auxiliary"]}" stroke-width="2"/>')
        
        num_parts = 3
        step = ray_len / (num_parts + 0.5) 
        
        pts_ray = []
        for i in range(1, num_parts+1):
            dist = step * i
            px = start_x + dist * math.cos(angle_rad)
            py = line_y - dist * math.sin(angle_rad)
            pts_ray.append((px, py))
            
            parts.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="4" fill="{COLORS["accent"]}" />')
            parts.append(draw_label(px-10, py-10, f"P{i}", COLORS["text_light"], size=16))
            
        last_p = pts_ray[-1]
        parts.append(f'<line x1="{last_p[0]:.2f}" y1="{last_p[1]:.2f}" x2="{B[0]}" y2="{B[1]}" stroke="{COLORS["highlight"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        
        total_ray = step * num_parts
        total_line = end_x - start_x
        
        pts_line = []
        for i, p_ray in enumerate(pts_ray[:-1]): # Exclude last
            ratio = (i+1) / num_parts
            bx = start_x + total_line * ratio
            by = line_y
            pts_line.append((bx, by))
            
            parts.append(f'<line x1="{p_ray[0]:.2f}" y1="{p_ray[1]:.2f}" x2="{bx:.2f}" y2="{by:.2f}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="4,4"/>')
            parts.append(f'<circle cx="{bx:.2f}" cy="{by:.2f}" r="3" fill="{COLORS["primary"]}" />')
            
        parts.append(draw_label(A[0]-20, A[1], "A", COLORS["vertices"]))
        parts.append(draw_label(B[0]+20, B[1], "B", COLORS["vertices"]))
        
        parts.append(f'<text x="{cx}" y="{height-30}" text-anchor="middle" fill="{COLORS["text_light"]}">Paralelas dividen AB en partes iguales</text>')
        
        return scene_title

    # --- 6. Visual Summary ---
    elif mode == 'summary_visual':
        scene_title = "" # No title, it's a summary graphic
        
        # 3 Panels: General Parallel, Triangle Thales, Triangle Similarity
        
        # Panel 1: General
        w_panel = width / 3
        cx1 = w_panel/2
        cy1 = height/2 - 10
        
        parts.append(f'<text x="{cx1}" y="30" text-anchor="middle" font-family="KaTeX_Main, Times, serif" font-weight="bold" fill="{COLORS["text"]}">Teorema General</text>')
        
        # Box for formula
        parts.append(f'<rect x="{cx1-60}" y="{height-50}" width="120" height="30" rx="4" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(f'<text x="{cx1}" y="{height-30}" text-anchor="middle" font-family="KaTeX_Main, Times, serif" font-size="16" fill="{COLORS["text"]}"><tspan font-style="italic">a</tspan>/<tspan font-style="italic">b</tspan> = <tspan font-style="italic">c</tspan>/<tspan font-style="italic">d</tspan></text>')
        
        # Lines L1, L2, L3
        for i in [-1, 0, 1]:
            y = cy1 + i * 35
            parts.append(f'<line x1="{cx1-50}" y1="{y}" x2="{cx1+50}" y2="{y}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
            
        # Transversals
        parts.append(f'<line x1="{cx1-30}" y1="{cy1-50}" x2="{cx1-15}" y2="{cy1+50}" stroke="{COLORS["text"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{cx1+15}" y1="{cy1-50}" x2="{cx1+30}" y2="{cy1+50}" stroke="{COLORS["text"]}" stroke-width="2"/>')
        
        # Labels a, b, c, d
        parts.append(draw_label(cx1-35, cy1-18, "a", COLORS["primary"], size=14, weight="normal"))
        parts.append(draw_label(cx1-30, cy1+18, "b", COLORS["primary"], size=14, weight="normal"))
        parts.append(draw_label(cx1+35, cy1-18, "c", COLORS["secondary"], size=14, weight="normal"))
        parts.append(draw_label(cx1+40, cy1+18, "d", COLORS["secondary"], size=14, weight="normal"))


        # Panel 2: Thales Triangle (Sides)
        cx2 = width/2
        cy2 = height/2 - 10
        parts.append(f'<text x="{cx2}" y="30" text-anchor="middle" font-family="KaTeX_Main, Times, serif" font-weight="bold" fill="{COLORS["text"]}">Lados (Cortes)</text>')
        
        # Triangle
        top_y = cy2 - 50
        bot_y = cy2 + 50
        A = (cx2, top_y)
        B = (cx2 - 50, bot_y)
        C = (cx2 + 50, bot_y)
        
        # Cut
        mid_y = (top_y + bot_y) / 2
        D = ((A[0]+B[0])/2, mid_y)
        E = ((A[0]+C[0])/2, mid_y)
        
        parts.append(draw_triangle([A, B, C], stroke=COLORS["text"], stroke_width=2))
        parts.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="{E[0]}" y2="{E[1]}" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
        
        # Labels AD, DB...
        parts.append(draw_label(A[0], A[1]-10, "A", COLORS["vertices"], size=12))
        parts.append(draw_label(B[0]-10, B[1]+5, "B", COLORS["vertices"], size=12))
        parts.append(draw_label(C[0]+10, C[1]+5, "C", COLORS["vertices"], size=12))
        parts.append(draw_label(D[0]-12, D[1], "D", COLORS["vertices"], size=12))
        parts.append(draw_label(E[0]+12, E[1], "E", COLORS["vertices"], size=12))
        
        # Formula Box
        parts.append(f'<rect x="{cx2-75}" y="{height-50}" width="150" height="30" rx="4" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        # Correct Formula: AD/DB = AE/EC
        parts.append(f'<text x="{cx2}" y="{height-30}" text-anchor="middle" font-family="KaTeX_Main, Times, serif" font-size="14" fill="{COLORS["text"]}">AD/DB = AE/EC</text>')


        # Panel 3: Similarity (Bases)
        cx3 = width - w_panel/2
        cy3 = height/2 - 10
        parts.append(f'<text x="{cx3}" y="30" text-anchor="middle" font-family="KaTeX_Main, Times, serif" font-weight="bold" fill="{COLORS["danger"]}">Bases (Semejanza)</text>')
        
        # Similar Triangles separated implicitly or explicitly? 
        # Let's show the standard triangle with base emphasis
        A3 = (cx3, top_y)
        B3 = (cx3 - 50, bot_y)
        C3 = (cx3 + 50, bot_y)
        D3 = ((A3[0]+B3[0])/2, mid_y)
        E3 = ((A3[0]+C3[0])/2, mid_y)
        
        parts.append(draw_triangle([A3, B3, C3], stroke=COLORS["text"], stroke_width=2))
        parts.append(f'<line x1="{D3[0]}" y1="{D3[1]}" x2="{E3[0]}" y2="{E3[1]}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        parts.append(f'<line x1="{B3[0]}" y1="{B3[1]}" x2="{C3[0]}" y2="{C3[1]}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        
        parts.append(draw_label(A3[0], A3[1]-10, "A", COLORS["vertices"], size=12))
        parts.append(draw_label(B3[0]-10, B3[1]+5, "B", COLORS["vertices"], size=12))
        parts.append(draw_label(C3[0]+10, C3[1]+5, "C", COLORS["vertices"], size=12))
        parts.append(draw_label(D3[0]-12, D3[1], "D", COLORS["vertices"], size=12))
        parts.append(draw_label(E3[0]+12, E3[1], "E", COLORS["vertices"], size=12))
        
        # Formula Box
        parts.append(f'<rect x="{cx3-75}" y="{height-50}" width="150" height="30" rx="4" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        # Correct Formula: AD/AB = DE/BC
        parts.append(f'<text x="{cx3}" y="{height-30}" text-anchor="middle" font-family="KaTeX_Main, Times, serif" font-size="14" fill="{COLORS["text"]}">AD/AB = DE/BC</text>')
        
        # Dividers
        parts.append(f'<line x1="{width/3}" y1="50" x2="{width/3}" y2="{height-20}" stroke="{COLORS["grid"]}" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{2*width/3}" y1="50" x2="{2*width/3}" y2="{height-20}" stroke="{COLORS["grid"]}" stroke-dasharray="4"/>')

        return scene_title


    return scene_title

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    if mode == 'summary_visual':
        height = 250 # Custom smaller height for footer
    
    parts = []
    # Background
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>')
    
    title = draw_thales_lines(parts, width, height, mode)
    
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

#!/usr/bin/env python3
"""
Intersection Renderer - Updated for Parallels and Secants
Generates SVG illustrations for parallel lines intersected by a secant, 
supporting various angle highlights and "Z", "F", "C" patterns.
"""

import math
import argparse
from pathlib import Path
from core.colors import COLORS

# Canvas Configuration
WIDTH = 600
HEIGHT = 400
CX, CY = WIDTH / 2, HEIGHT / 2

def get_coord(cx, cy, r, angle_deg):
    rad = math.radians(angle_deg) # standard math angle (CCW from East) -> SVG y is inverted so -sin
    return cx + r * math.cos(rad), cy - r * math.sin(rad)

def draw_arc(cx, cy, r, start_deg, end_deg, color, fill_opacity=0.2):
    diff = end_deg - start_deg
    while diff < 0: diff += 360
    large_arc = 1 if diff > 180 else 0
    
    sx, sy = get_coord(cx, cy, r, start_deg)
    ex, ey = get_coord(cx, cy, r, end_deg)
    
    return f'<path d="M {cx} {cy} L {sx:.2f} {sy:.2f} A {r} {r} 0 {large_arc} 0 {ex:.2f} {ey:.2f} Z" fill="{color}" fill-opacity="{fill_opacity}" stroke="none" />' \
           f'<path d="M {sx:.2f} {sy:.2f} A {r} {r} 0 {large_arc} 0 {ex:.2f} {ey:.2f}" fill="none" stroke="{color}" stroke-width="2" />'

def draw_parallel_system(width, height, angle_secant=60, highlights=None, labels=None, pattern=None, line_spacing=100, angle_colors=None, slant_top=0, slant_bot=0, arrows=None):
    """
    Generates SVG for two parallel (or nearly parallel) lines cut by a secant.
    angle_secant: Angle of the transversal line relative to horizontal.
    highlights: list of angle indices (1-8) to color.
    labels: dict of {index: text}.
    pattern: 'Z', 'F', 'C' or None.
    line_spacing: vertical distance at center.
    angle_colors: dict {index: color}.
    slant_top: angle of top line (0 is horizontal).
    slant_bot: angle of bottom line.
    arrows: list of tuples (from_idx, to_idx) to draw connecting arrows.
    """
    if highlights is None: highlights = []
    if labels is None: labels = {}
    if angle_colors is None: angle_colors = {}
    if arrows is None: arrows = []
    
    cx, cy = width / 2, height / 2
    
    # Configuration
    line_length = 400
    secant_length = 420
    
    # Center Y of lines
    y_top_c = cy - line_spacing / 2
    y_bot_c = cy + line_spacing / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>',
    ]

    # --- Helper to get line end points with slant ---
    def get_line_ends(yc, slant):
        # SVG y increases down. Math y increases up.
        # tan(slant) = dy / dx in math.
        # dy_svg = -dy_math
        # dy_svg = -tan(slant) * dx
        rad = math.radians(slant)
        dy = -math.tan(rad) * (line_length / 2)
        return (cx - line_length/2, yc - dy), (cx + line_length/2, yc + dy)

    # --- Calculate Intersection Points ---
    # Intersection of Secant (through cx,cy with angle_secant) and Lines.
    # Secant Line: P(t) = (cx, cy) + t * (cos(a), -sin(a))
    # Top Line: P(u) = (cx, y_top_c) + u * (cos(slant_top), -sin(slant_top)) ?
    # Let's solve generally.
    # Secant: -sin(a)*x - cos(a)*y + C = 0 ?
    # Line through (x0, y0) with angle theta: sin(theta)(x-x0) + cos(theta)(y-y0) = 0 (Normal vector is (sin, cos)?)
    # Direction vector v = (cos t, -sin t). Normal n = (sin t, cos t).
    # n . (P - P0) = 0
    # sin(a)*(x - cx) + cos(a)*(y - cy) = 0  <-- Check: if a=0 (horiz), sin=0, gives y=cy. Correct (inverted Y).
    
    def intersect_lines(p1, ang1, p2, ang2):
        # Returns intersection of line through p1 w/ ang1 and line through p2 w/ ang2
        # Equation 1: sin(a1)(x - x1) + cos(a1)(y - y1) = 0
        # Equation 2: sin(a2)(x - x2) + cos(a2)(y - y2) = 0
        # A1*x + B1*y = C1
        # A2*x + B2*y = C2
        
        r1, r2 = math.radians(ang1), math.radians(ang2)
        A1, B1 = math.sin(r1), math.cos(r1)
        C1 = A1*p1[0] + B1*p1[1]
        
        A2, B2 = math.sin(r2), math.cos(r2)
        C2 = A2*p2[0] + B2*p2[1]
        
        det = A1*B2 - A2*B1
        if abs(det) < 1e-9: return (0,0) # Parallel
        
        x = (B2*C1 - B1*C2) / det
        y = (A1*C2 - A2*C1) / det
        return (x, y)

    pt_top = intersect_lines((cx, cy), angle_secant, (cx, y_top_c), slant_top)
    pt_bot = intersect_lines((cx, cy), angle_secant, (cx, y_bot_c), slant_bot)

    # --- Draw Pattern Highlights (Z, F, C) ---
    if pattern:
        pat_color = COLORS['highlight']
        pat_width = 8
        pat_opacity = 0.3
        lx_end = cx + line_length/2
        lx_start = cx - line_length/2
        
        if pattern == 'Z':
            # Path Top-Left -> Top-Int -> Bot-Int -> Bot-Right
            # Assuming standard Z involves acute angles for 3 and 6?
            # Start: point on top line far left? or just from int?
            p1 = (cx - line_length/2, y_top_c - math.tan(math.radians(slant_top)) * (-line_length/2) ) # approx
            # Let's just use simple horizontal approximation for Z visual if slants are 0 usually
            # Use computed intersection points
            path_d = f"M {lx_start} {pt_top[1]} L {pt_top[0]} {pt_top[1]} L {pt_bot[0]} {pt_bot[1]} L {lx_end} {pt_bot[1]}"
            svg_parts.append(f'<path d="{path_d}" stroke="{pat_color}" stroke-width="{pat_width}" stroke-opacity="{pat_opacity}" fill="none"/>')
            
        elif pattern == 'F':
            # F shape
            path_d = f"M {pt_bot[0]} {pt_bot[1]+40} L {pt_top[0]} {pt_top[1]-40} M {pt_top[0]} {pt_top[1]} L {lx_end} {pt_top[1]} M {pt_bot[0]} {pt_bot[1]} L {lx_end} {pt_bot[1]}"
            svg_parts.append(f'<path d="{path_d}" stroke="{pat_color}" stroke-width="{pat_width}" stroke-opacity="{pat_opacity}" fill="none"/>')
            
        elif pattern == 'C':
            # C shape
            path_d = f"M {lx_end} {pt_top[1]} L {pt_top[0]} {pt_top[1]} L {pt_bot[0]} {pt_bot[1]} L {lx_end} {pt_bot[1]}"
            svg_parts.append(f'<path d="{path_d}" stroke="{pat_color}" stroke-width="{pat_width}" stroke-opacity="{pat_opacity}" fill="none"/>')

    # --- Draw Lines ---
    t1, t2 = get_line_ends(y_top_c, slant_top)
    b1, b2 = get_line_ends(y_bot_c, slant_bot)
    
    svg_parts.append(f'<line x1="{t1[0]:.2f}" y1="{t1[1]:.2f}" x2="{t2[0]:.2f}" y2="{t2[1]:.2f}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linecap="round"/>')
    svg_parts.append(f'<line x1="{b1[0]:.2f}" y1="{b1[1]:.2f}" x2="{b2[0]:.2f}" y2="{b2[1]:.2f}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linecap="round"/>')
    
    # Arrows on lines
    arrow_offset = 15
    svg_parts.append(f'<path d="M {t2[0]-arrow_offset} {t2[1]-6} L {t2[0]} {t2[1]} L {t2[0]-arrow_offset} {t2[1]+6}" fill="none" stroke="{COLORS["line"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    svg_parts.append(f'<path d="M {b2[0]-arrow_offset} {b2[1]-6} L {b2[0]} {b2[1]} L {b2[0]-arrow_offset} {b2[1]+6}" fill="none" stroke="{COLORS["line"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')

    # --- Draw Secant ---
    rad = math.radians(angle_secant)
    dx_sec = (secant_length/2) * math.cos(rad)
    dy_sec = (secant_length/2) * math.sin(rad)
    s_x1, s_y1 = cx - dx_sec, cy + dy_sec 
    s_x2, s_y2 = cx + dx_sec, cy - dy_sec
    svg_parts.append(f'<line x1="{s_x1:.2f}" y1="{s_y1:.2f}" x2="{s_x2:.2f}" y2="{s_y2:.2f}" stroke="{COLORS["secant"]}" stroke-width="3" stroke-linecap="round"/>')
    
    # --- Angles ---
    r_arc = 40
    
    def draw_highlighted_angle(idx, center_pt, label=None, custom_color=None):
        col = custom_color
        if not col: col = angle_colors.get(idx)
        if not col: col = COLORS['angle'] if idx in highlights else COLORS['text_light']
        
        is_highlighted = (idx in highlights) or (idx in angle_colors) or (custom_color is not None)
        fill_op = 0.4 if is_highlighted else 0.0
        
        # Ranges depend on slant! For simplicity, assume slant is small enough that relative order is same.
        # But we must add slant to the 0/180 bounds.
        # Top-Left (1): secant to 180+slant. 
        # Secant angle is fixed globally. 
        # Line angle is `slant`. Left direction is `180+slant`.
        # Region 1: Ray `angle_secant` to Ray `180+slant_top`.
        
        if idx <= 4:
            base_angle = slant_top
        else:
            base_angle = slant_bot
            
        # Rays involved: 
        # R_secant_up: angle_secant
        # R_secant_down: 180 + angle_secant
        # R_line_right: base_angle
        # R_line_left: 180 + base_angle
        
        # 1 (Top-Left): R_secant_up to R_line_left
        # 2 (Top-Right): R_line_right to R_secant_up
        # 3 (Bot-Left): R_line_left to R_secant_down
        # 4 (Bot-Right): R_secant_down to R_line_right
        
        if idx in [1, 5]:
            start, end = angle_secant, 180+base_angle
        elif idx in [2, 6]:
            start, end = base_angle, angle_secant 
        elif idx in [3, 7]:
            start, end = 180+base_angle, 180+angle_secant
        elif idx in [4, 8]:
            start, end = 180+angle_secant, 360+base_angle # normalize
            
        # Draw
        svg_parts.append(draw_arc(center_pt[0], center_pt[1], r_arc, start, end, col, fill_opacity=fill_op))
        
        if label:
            lbl_ang = (start + end)/2
            lr = r_arc + 20
            lx, ly = get_coord(center_pt[0], center_pt[1], lr, lbl_ang)
            anchor = "middle"
            if 0 <= lbl_ang%360 < 45 or 315 < lbl_ang%360 <= 360: anchor = "start"
            elif 135 < lbl_ang%360 < 225: anchor = "end"
            svg_parts.append(f'<text x="{lx:.2f}" y="{ly:.2f}" text-anchor="{anchor}" dominant-baseline="middle" font-weight="bold" fill="{COLORS["text"]}">{label}</text>')
            
            return lx, ly # Return label position for arrows
        return None, None

    all_indices = set(highlights) | set(labels.keys()) | set(angle_colors.keys())
    # Add arrow sources/targets
    for s, t in arrows:
        all_indices.add(s)
        all_indices.add(t)
        
    lbl_positions = {}
    
    for idx in all_indices:
        is_top = idx <= 4
        center_pt = pt_top if is_top else pt_bot
        lbl = labels.get(idx, "")
        lx, ly = draw_highlighted_angle(idx, center_pt, label=lbl)
        if lx: lbl_positions[idx] = (lx, ly)
        
    # Draw Arrows Connecting Labels
    for s, t in arrows:
        if s in lbl_positions and t in lbl_positions:
            sx, sy = lbl_positions[s]
            tx, ty = lbl_positions[t]
            # Draw curved arrow
            mx, my = (sx+tx)/2 + 20, (sy+ty)/2
            svg_parts.append(f'<path d="M {sx} {sy+10} Q {mx} {my} {tx} {ty-10}" fill="none" stroke="{COLORS["accent"]}" stroke-width="2" marker-end="url(#arrowhead)"/>')
            
    # Defs for marker
    svg_parts.insert(2, '<defs><marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="'+COLORS["accent"]+'"/></marker></defs>')

    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def draw_zigzag(width, height, angle_peaks_left):
    """
    Draws 'M' property (ZigZag).
    angle_peaks_left: list of angles [top_peak, bot_peak] pointing left.
    The center angle pointing right is sum.
    """
    cx, cy = width/2, height/2
    
    line_spacing = 150
    y_top = cy - line_spacing/2
    y_bot = cy + line_spacing/2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>',
    ]
    
    # Parallels
    svg_parts.append(f'<line x1="50" y1="{y_top}" x2="{width-50}" y2="{y_top}" stroke="{COLORS["line"]}" stroke-width="3"/>')
    svg_parts.append(f'<line x1="50" y1="{y_bot}" x2="{width-50}" y2="{y_bot}" stroke="{COLORS["line"]}" stroke-width="3"/>')
    svg_parts.append(f'<path d="M {width-65} {y_top-6} L {width-50} {y_top} L {width-65} {y_top+6}" fill="none" stroke="{COLORS["line"]}" stroke-width="3"/>')
    svg_parts.append(f'<path d="M {width-65} {y_bot-6} L {width-50} {y_bot} L {width-65} {y_bot+6}" fill="none" stroke="{COLORS["line"]}" stroke-width="3"/>')
    
    # ZigZag "M"
    # Vertex at center left? Center right?
    # Angle sum property: Left pointing angles = Right pointing angles.
    # Scenario: 
    #   \ a
    #    \______ x
    #    / 
    #   / b
    #
    # Top segment comes down with angle `a` relative to horizontal.
    # Bottom segment goes up with angle `b`.
    
    ang_a = angle_peaks_left[0]
    ang_b = angle_peaks_left[1]
    
    # Vertex position
    vx, vy = cx + 50, cy # Vertex pointing right
    
    # Calculate start points on lines
    # Top point: 
    # slope = tan(ang_a).
    # dy = vy - y_top.
    # dx = dy / tan(ang_a).
    # x_top = vx - dx. 
    dx_top = (vy - y_top) / math.tan(math.radians(ang_a))
    x_top = vx - dx_top
    
    # Bot point:
    # slope = tan(ang_b)
    # y_bot - vy = dy_bot
    dx_bot = (y_bot - vy) / math.tan(math.radians(ang_b))
    x_bot = vx - dx_bot
    
    # Draw ZigZag Lines
    svg_parts.append(f'<polyline points="{x_top},{y_top} {vx},{vy} {x_bot},{y_bot}" fill="none" stroke="{COLORS["secant"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    
    # Draw Angles
    r = 40
    # Top Angle (a) - Alternate interior at top
    # Ray 1: 0 (Horizontal right). Ray 2: Down-Right (angle a).
    # Actually, angle `a` is usually interior acute.
    # Angle at top line: between Line (Right, 0) and Seg (Down-Right, -a in math, +a in svg).
    svg_parts.append(draw_arc(x_top, y_top, r, 0, ang_a+5, COLORS['angle'], 0.4)) # +5 for visual
    svg_parts.append(f'<text x="{x_top+40}" y="{y_top+15}" font-weight="bold" fill="{COLORS["text"]}">{ang_a}°</text>')
    
    # Bot Angle (b)
    # Ray 1: 0 (Horizontal). Seg is Up-Right. Math angle b. SVG -b.
    # We want angle between Horizontal and Seg.
    # SVG arc from 360-b to 360/0?
    svg_parts.append(draw_arc(x_bot, y_bot, r, 360-ang_b, 360, COLORS['angle'], 0.4))
    svg_parts.append(f'<text x="{x_bot+40}" y="{y_bot-15}" font-weight="bold" fill="{COLORS["text"]}">{ang_b}°</text>')
    
    # Middle Angle (x) - Pointing Right.
    # It is the reflex angle? No, internal angle `x = a + b`.
    # Between Seg Top (coming in) and Seg Bot (going out).
    # Math angles:
    # Top Seg coming in: 180 - a.
    # Bot Seg going out: 180 + b.
    # Angle x is between them. range: 180-a to 180+b.
    # Size = a+b.
    svg_parts.append(draw_arc(vx, vy, r, 180-ang_a, 180+ang_b, COLORS['primary'], 0.4))
    svg_parts.append(f'<text x="{vx-30}" y="{vy}" dominant-baseline="middle" text-anchor="end" font-weight="bold" fill="{COLORS["primary"]}">x</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def generate_resumen_zfc(width, height):
    """
    Generates a visual summary infographic showing all 3 angle types.
    Layout: 3 rows, each with: Letter | Mini-Diagram | Property
    """
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>',
    ]
    
    row_height = height / 3
    
    # Helper to draw mini parallel system
    def draw_mini(cx, cy, scale, pattern_letter, highlight_pair, angle_color):
        mini_parts = []
        ls = 25 * scale  # line spacing
        ll = 80 * scale  # line length
        sa = 60  # secant angle
        
        y_t = cy - ls/2
        y_b = cy + ls/2
        
        # Lines
        mini_parts.append(f'<line x1="{cx-ll/2}" y1="{y_t}" x2="{cx+ll/2}" y2="{y_t}" stroke="{COLORS["line"]}" stroke-width="2"/>')
        mini_parts.append(f'<line x1="{cx-ll/2}" y1="{y_b}" x2="{cx+ll/2}" y2="{y_b}" stroke="{COLORS["line"]}" stroke-width="2"/>')
        
        # Secant
        rad = math.radians(sa)
        dx = (ll*0.7) * math.cos(rad)
        dy = (ll*0.7) * math.sin(rad)
        mini_parts.append(f'<line x1="{cx-dx}" y1="{cy+dy}" x2="{cx+dx}" y2="{cy-dy}" stroke="{COLORS["secant"]}" stroke-width="2"/>')
        
        # Intersection points
        x_off = (ls/2) / math.tan(rad)
        pt_t = (cx + x_off, y_t)
        pt_b = (cx - x_off, y_b)
        
        # Angle arcs
        r = 12 * scale
        if pattern_letter == 'Z':
            # Alternos: 3 and 6
            mini_parts.append(draw_arc(pt_t[0], pt_t[1], r, 180, 180+sa, angle_color, 0.5))
            mini_parts.append(draw_arc(pt_b[0], pt_b[1], r, 0, sa, angle_color, 0.5))
        elif pattern_letter == 'F':
            # Correspondientes: 2 and 6
            mini_parts.append(draw_arc(pt_t[0], pt_t[1], r, 0, sa, angle_color, 0.5))
            mini_parts.append(draw_arc(pt_b[0], pt_b[1], r, 0, sa, angle_color, 0.5))
        elif pattern_letter == 'C':
            # Conjugados: 4 and 6
            mini_parts.append(draw_arc(pt_t[0], pt_t[1], r, 180+sa, 360, angle_color, 0.5))
            mini_parts.append(draw_arc(pt_b[0], pt_b[1], r, 0, sa, angle_color, 0.5))
            
        return ''.join(mini_parts)
    
    # Row data: (y_center, letter, name, property, color)
    rows = [
        (row_height * 0.5, 'Z', 'Alternos Internos', 'Iguales (a = b)', COLORS['angle']),
        (row_height * 1.5, 'F', 'Correspondientes', 'Iguales (a = b)', COLORS['primary']),
        (row_height * 2.5, 'C', 'Conjugados', 'Suman 180° (a + b = 180)', COLORS['secondary']),
    ]
    
    col_letter = 60
    col_diagram = width / 2
    col_property = width - 80
    
    for yc, letter, name, prop, color in rows:
        # Letter (big, colored)
        svg_parts.append(f'<text x="{col_letter}" y="{yc}" font-size="48" font-weight="bold" fill="{color}" text-anchor="middle" dominant-baseline="middle">{letter}</text>')
        
        # Mini diagram
        svg_parts.append(draw_mini(col_diagram, yc, 1.2, letter, None, color))
        
        # Name + Property
        svg_parts.append(f'<text x="{col_property}" y="{yc-12}" font-size="14" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{name}</text>')
        svg_parts.append(f'<text x="{col_property}" y="{yc+12}" font-size="12" fill="{COLORS["text_light"]}" text-anchor="middle">{prop}</text>')
        
        # Divider line (except last)
        if letter != 'C':
            svg_parts.append(f'<line x1="20" y1="{yc + row_height/2}" x2="{width-20}" y2="{yc + row_height/2}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="4"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def generate_svg_main(mode, output_path):
    width, height = WIDTH, HEIGHT
    
    # 1. Correspondientes ("El Ascensor")
    if mode == "concept_ascensor":
        svg = draw_parallel_system(width, height, angle_secant=65,
                                   highlights=[6, 2], # Same position (Right side)
                                   labels={6: "Sube", 2: "Aquí"},
                                   arrows=[(6, 2)], # Arrow from 6 to 2
                                   pattern='F')

    # 2. Alternos ("El Cruce")
    elif mode == "concept_cruce":
        svg = draw_parallel_system(width, height, angle_secant=65,
                                   highlights=[3, 6], # Alternos Internos
                                   labels={3: "1", 6: "1"},
                                   arrows=[(3, 6)],
                                   pattern='Z')

    # 3. Principio de Suma (Conjugados)
    elif mode == "concept_suma":
        svg = draw_parallel_system(width, height, angle_secant=110,
                                   highlights=[4, 6], # Same side internal
                                   labels={4: "a", 6: "b"},
                                   pattern='C')

    # Ex 1: Correspondientes Básicos (110 deg)
    elif mode == "ex1":
        # 110 deg is Obtuse.
        # Top right (2) is Obtuse if angle_secant > 90? No, if secant leans left.
        # Let's use secant=110. Then Top-Left (1) is Acute (70). Top-Right (2) is Obtuse (110).
        # Bot-Right (6) is 110.
        svg = draw_parallel_system(width, height, angle_secant=110,
                                   highlights=[2, 6],
                                   labels={2: "110°", 6: "?"},
                                   angle_colors={2: COLORS['primary']})
                                   
    # Ex 2: Alternos Ecuation (2x, 80)
    elif mode == "ex2":
        # 80 is Acute.
        # Alternos Internos Acute: 3 and 6 (if secant < 90).
        svg = draw_parallel_system(width, height, angle_secant=80,
                                   highlights=[3, 6],
                                   labels={3: "2x", 6: "80°"},
                                   pattern='Z')

    # Ex 3: Conjugados (x, x+20) -> 80, 100
    elif mode == "ex3":
        # Sum 180. One 80 (acute), one 100 (obtuse).
        # Conjugados Internos: 4 (Obtuse) and 6 (Acute).
        svg = draw_parallel_system(width, height, angle_secant=80,
                                   highlights=[4, 6],
                                   labels={4: "x+20", 6: "x"},
                                   pattern='C')

    # Ex 4: Alternos Externos (150)
    elif mode == "ex4":
        # 150 Obtuse. Secant leaning left (120 deg) -> Top-Right is 120 (Obtuse).
        # Or just standard secant=60, Top-Left (1) is 120 (Obtuse).
        # Let's use secant=30 (flatter). Top-Left is 150.
        # Alterno Externo to 1 is 8 (Bot-Right).
        svg = draw_parallel_system(width, height, angle_secant=30,
                                   highlights=[1, 8],
                                   labels={1: "150°", 8: "?"})
                                   
    # Ex 5: No Paralelas (70 vs 71)
    elif mode == "ex5_noparallel":
        # Correspondientes are different.
        # Slant top line by 1 deg?
        svg = draw_parallel_system(width, height, angle_secant=70,
                                   highlights=[2, 6],
                                   labels={2: "71°", 6: "70°"},
                                   slant_top=2, # subtle slant
                                   slant_bot=0)

    # Ex 6: ZigZag
    elif mode == "ex6_zigzag":
        svg = draw_zigzag(width, height, [30, 40])

    # Ex 7: Ecuación Compleja Correspondientes (5x-20, 3x+40) -> 130
    elif mode == "ex7":
        # Result 130 (Obtuse).
        svg = draw_parallel_system(width, height, angle_secant=130, # Leaning left
                                   highlights=[2, 6], # Top-Right, Bot-Right (Obtuse)
                                   labels={2: "5x - 20", 6: "3x + 40"},
                                   angle_colors={2: COLORS['primary'], 6: COLORS['primary']})

    # Resumen Visual Z-F-C
    elif mode == "resumen_zfc":
        svg = generate_resumen_zfc(width, height + 100)

    else:
        svg = f'<svg><text>Unknown mode {mode}</text></svg>'
        
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(svg)
    print(f"✅ Generated {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode', required=True)
    args = parser.parse_args()
    
    generate_svg_main(args.mode, args.output)

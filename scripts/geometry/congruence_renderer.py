
import argparse
import sys
import math
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS

def generate_svg_main(mode, output_path):
    # COMPACT CANVAS: Reduced height to minimize whitespace
    width = 600
    height = 350  # Reduced from 460
    
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>')

    STROKE_WIDTH = 2.5
    FONT_SIZE_LABEL = 18
    FONT_SIZE_TITLE = 20
    FONT_FAMILY = "sans-serif"
    TITLE_Y = height - 25  # Reserve 25px for title at bottom
    
    def draw_triangle(pts, stroke=COLORS["line"], fill="none", stroke_width=STROKE_WIDTH, stroke_colors=None):
        if stroke_colors:
            path = ""
            for i in range(3):
                p_start = pts[i]
                p_end = pts[(i+1)%3]
                color = stroke_colors[i]
                path += f'<line x1="{p_start[0]:.2f}" y1="{p_start[1]:.2f}" x2="{p_end[0]:.2f}" y2="{p_end[1]:.2f}" stroke="{color}" stroke-width="{stroke_width+1}" stroke-linecap="round"/>'
            return path
        else:
            path = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} L {pts[1][0]:.2f} {pts[1][1]:.2f} L {pts[2][0]:.2f} {pts[2][1]:.2f} Z"
            return f'<path d="{path}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linejoin="round"/>'

    def draw_tick_mark(p1, p2, count=1, color=COLORS["text"]):
        mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        dx, dy = p2[0]-p1[0], p2[1]-p1[1]
        length = math.hypot(dx, dy)
        if length < 1e-6: return ""
        ux, uy = dx/length, dy/length
        nx, ny = -uy, ux
        diag_x = ux*0.5 + nx*0.8
        diag_y = uy*0.5 + ny*0.8
        spacing = 6
        start = -((count-1)*spacing)/2
        svg = ""
        for i in range(count):
            off = start + i*spacing
            cx, cy = mx + ux*off, my + uy*off
            x1, y1 = cx - diag_x*8, cy - diag_y*8
            x2, y2 = cx + diag_x*8, cy + diag_y*8
            svg += f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="2"/>'
        return svg

    def draw_angle_arc(center, p1, p2, count=1, radius=25, color=COLORS["line"], fill_opacity=0.2):
        ang1 = math.atan2(p1[1]-center[1], p1[0]-center[0])
        ang2 = math.atan2(p2[1]-center[1], p2[0]-center[0])
        diff = ang2 - ang1
        while diff < 0: diff += 2*math.pi
        while diff > 2*math.pi: diff -= 2*math.pi
        if diff > math.pi:
            ang1, ang2 = ang2, ang1
            diff = 2*math.pi - diff
        sx = center[0] + radius * math.cos(ang1)
        sy = center[1] + radius * math.sin(ang1)
        ex = center[0] + radius * math.cos(ang2)
        ey = center[1] + radius * math.sin(ang2)
        sector_path = f"M {center[0]:.2f} {center[1]:.2f} L {sx:.2f} {sy:.2f} A {radius} {radius} 0 0 1 {ex:.2f} {ey:.2f} Z"
        svg = f'<path d="{sector_path}" fill="{color}" fill-opacity="{fill_opacity}" stroke="none"/>'
        gap = 5
        for i in range(count):
            r = radius - i*gap 
            sx_r = center[0] + r * math.cos(ang1)
            sy_r = center[1] + r * math.sin(ang1)
            ex_r = center[0] + r * math.cos(ang2)
            ey_r = center[1] + r * math.sin(ang2)
            svg += f'<path d="M {sx_r:.2f} {sy_r:.2f} A {r} {r} 0 0 1 {ex_r:.2f} {ey_r:.2f}" fill="none" stroke="{color}" stroke-width="2"/>'
        return svg

    def draw_label(x, y, text, color=COLORS["text"], size=FONT_SIZE_LABEL, weight="bold"):
        return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT_FAMILY}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="middle" dominant-baseline="middle">{text}</text>'

    def transform(pts, scale=1.0, offset=(0,0)):
        return [ (p[0]*scale + offset[0], p[1]*scale + offset[1]) for p in pts ]

    # TIGHT CENTERING: Shapes fill available vertical space (height - title area)
    available_height = height - 60  # 25 for title, 35 for top margin
    
    def get_centered_offsets(w, h, gap=80):
        total_w = w*2 + gap
        start_x = (width - total_w) / 2
        # Vertical: Center in available area (top 35px margin, bottom 25px title)
        center_y = 35 + available_height / 2
        base_y = center_y + h / 2  # Bottom of shape
        off1 = (start_x, base_y)
        off2 = (start_x + w + gap, base_y)
        return off1, off2

    def draw_congruence_symbol(x, y, size=40):
        return draw_label(x, y, "≅", size=size, weight="bold")

    C_PAIR1 = COLORS['primary']
    C_PAIR2 = COLORS['medianas']
    C_PAIR3 = COLORS['danger']
    
    # Standard Shape - Reduced base size for compact canvas
    base_raw = [(0,0), (120,0), (40,-95)]
    w_std, h_std = 120, 95

    if mode == 'definition':
        scale = 1.2
        w, h = w_std*scale, h_std*scale
        off1, off2 = get_centered_offsets(w, h, gap=100)
        T1 = transform(base_raw, scale, off1)
        T2 = transform(base_raw, scale, off2)
        
        parts.append(draw_triangle(T1, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        parts.append(draw_triangle(T2, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T1[1], T1[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T1[2], T1[0], 3, C_PAIR3))
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[1], T2[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T2[2], T2[0], 3, C_PAIR3))
        
        for T in [T1, T2]:
            parts.append(draw_angle_arc(T[0], T[1], T[2], 1, color=C_PAIR3, radius=28))
            parts.append(draw_angle_arc(T[1], T[2], T[0], 2, color=C_PAIR1, radius=28))
            parts.append(draw_angle_arc(T[2], T[0], T[1], 3, color=C_PAIR2, radius=28))
            
        for pt, txt in zip(T1, ["A","B","C"]):
            dy = 22 if txt in ["A","B"] else -22
            dx = -12 if txt=="A" else (12 if txt=="B" else 0)
            parts.append(draw_label(pt[0]+dx, pt[1]+dy, txt, COLORS['vertices']))
        for pt, txt in zip(T2, ["D","E","F"]):
            dy = 22 if txt in ["D","E"] else -22
            dx = -12 if txt=="D" else (12 if txt=="E" else 0)
            parts.append(draw_label(pt[0]+dx, pt[1]+dy, txt, COLORS['vertices']))

        cx = (off1[0] + w + off2[0]) / 2 + 10
        parts.append(draw_congruence_symbol(cx, 35 + available_height/2, size=45))
        parts.append(draw_label(width/2, TITLE_Y, "Partes Correspondientes", weight="bold"))

    elif mode == 'criterion_lll':
        scale = 1.2
        w, h = w_std*scale, h_std*scale
        off1, off2 = get_centered_offsets(w, h, gap=100)
        T1 = transform(base_raw, scale, off1)
        T2 = transform(base_raw, scale, off2)
        
        parts.append(draw_triangle(T1, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        parts.append(draw_triangle(T2, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T1[1], T1[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T1[2], T1[0], 3, C_PAIR3))
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[1], T2[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T2[2], T2[0], 3, C_PAIR3))
        
        cx = (off1[0] + w + off2[0]) / 2 + 30
        parts.append(draw_congruence_symbol(cx, 35 + available_height/2, size=45))
        parts.append(draw_label(width/2, TITLE_Y, "Criterio LLL: Lados Iguales", weight="bold"))

    elif mode == 'criterion_lal':
        scale = 1.2
        w, h = w_std*scale, h_std*scale
        off1, off2 = get_centered_offsets(w, h, gap=100)
        T1 = transform(base_raw, scale, off1)
        T2 = transform(base_raw, scale, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['auxiliary']))
        parts.append(draw_triangle(T2, stroke=COLORS['auxiliary']))
        
        parts.append(f'<line x1="{T1[0][0]:.2f}" y1="{T1[0][1]:.2f}" x2="{T1[1][0]:.2f}" y2="{T1[1][1]:.2f}" stroke="{C_PAIR1}" stroke-width="5"/>')
        parts.append(f'<line x1="{T2[0][0]:.2f}" y1="{T2[0][1]:.2f}" x2="{T2[1][0]:.2f}" y2="{T2[1][1]:.2f}" stroke="{C_PAIR1}" stroke-width="5"/>')
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        
        parts.append(f'<line x1="{T1[2][0]:.2f}" y1="{T1[2][1]:.2f}" x2="{T1[0][0]:.2f}" y2="{T1[0][1]:.2f}" stroke="{C_PAIR3}" stroke-width="5"/>')
        parts.append(f'<line x1="{T2[2][0]:.2f}" y1="{T2[2][1]:.2f}" x2="{T2[0][0]:.2f}" y2="{T2[0][1]:.2f}" stroke="{C_PAIR3}" stroke-width="5"/>')
        parts.append(draw_tick_mark(T1[2], T1[0], 2, C_PAIR3))
        parts.append(draw_tick_mark(T2[2], T2[0], 2, C_PAIR3))
        
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, color=C_PAIR2, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, color=C_PAIR2, fill_opacity=0.4))
        
        cx = (off1[0] + w + off2[0]) / 2 + 30
        parts.append(draw_congruence_symbol(cx, 35 + available_height/2, size=45))
        parts.append(draw_label(width/2, TITLE_Y, "Criterio LAL: Lado-Ángulo-Lado", weight="bold"))

    elif mode == 'criterion_ala':
        scale = 1.2
        w, h = w_std*scale, h_std*scale
        off1, off2 = get_centered_offsets(w, h, gap=100)
        T1 = transform(base_raw, scale, off1)
        T2 = transform(base_raw, scale, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['auxiliary']))
        parts.append(draw_triangle(T2, stroke=COLORS['auxiliary']))
        
        parts.append(f'<line x1="{T1[0][0]:.2f}" y1="{T1[0][1]:.2f}" x2="{T1[1][0]:.2f}" y2="{T1[1][1]:.2f}" stroke="{C_PAIR1}" stroke-width="5"/>')
        parts.append(f'<line x1="{T2[0][0]:.2f}" y1="{T2[0][1]:.2f}" x2="{T2[1][0]:.2f}" y2="{T2[1][1]:.2f}" stroke="{C_PAIR1}" stroke-width="5"/>')
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, color=C_PAIR2, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, color=C_PAIR2, fill_opacity=0.4))
        parts.append(draw_angle_arc(T1[1], T1[0], T1[2], 2, color=C_PAIR3, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[1], T2[0], T2[2], 2, color=C_PAIR3, fill_opacity=0.4))
        
        cx = (off1[0] + w + off2[0]) / 2 + 30
        parts.append(draw_congruence_symbol(cx, 35 + available_height/2, size=45))
        parts.append(draw_label(width/2, TITLE_Y, "Criterio ALA: Ángulo-Lado-Ángulo", weight="bold"))

    elif mode == 'example_lll_345':
        UNIT = 35
        raw_345 = [(0,0), (3*UNIT,0), (0,-4*UNIT)]
        w, h = 3*UNIT, 4*UNIT
        off1, off2 = get_centered_offsets(w, h, gap=120)
        T1 = transform(raw_345, 1.0, off1)
        T2 = transform(raw_345, 1.0, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['primary']))
        parts.append(draw_triangle(T2, stroke=COLORS['primary']))
        
        for T in [T1, T2]:
            parts.append(draw_label((T[0][0]+T[1][0])/2, T[0][1]+22, "3", color=COLORS['primary']))
            parts.append(draw_label(T[0][0]-18, (T[0][1]+T[2][1])/2, "4", color=COLORS['primary']))
            parts.append(draw_label((T[1][0]+T[2][0])/2+20, (T[1][1]+T[2][1])/2-8, "5", color=COLORS['primary']))
        
        cx = (off1[0] + w + off2[0]) / 2 + 10
        parts.append(draw_congruence_symbol(cx, 35 + available_height/2 - 20, size=45))
        parts.append(draw_label(width/2, TITLE_Y, "Lados iguales → Congruentes", weight="bold"))

    elif mode == 'example_lal_5740':
        # FIXED: Reduced scale to fit within canvas
        scale = 25  # Reduced from 35
        rad = math.radians(40)
        pA = (0,0)
        pB = (7*scale, 0) 
        pC = (5*scale*math.cos(rad), -5*scale*math.sin(rad)) 
        
        raw_lal = [pA, pB, pC]
        w, h = 7*scale, 5*scale*math.sin(rad)
        
        off1, off2 = get_centered_offsets(w, h, gap=80)  # Reduced gap
        T1 = transform(raw_lal, 1.0, off1)
        T2 = transform(raw_lal, 1.0, off2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['line']))
        parts.append(draw_triangle(T2, stroke=COLORS['line']))
        
        for T in [T1, T2]:
            parts.append(draw_label((T[0][0]+T[1][0])/2, T[0][1]+22, "7", color=COLORS['primary']))
            parts.append(draw_label((T[0][0]+T[2][0])/2-20, (T[0][1]+T[2][1])/2-8, "5", color=COLORS['primary']))
            parts.append(draw_angle_arc(T[0], T[1], T[2], 1, radius=30, color=COLORS['danger']))
            parts.append(draw_label(T[0][0]+50, T[0][1]-15, "40°", size=16, color=COLORS['danger']))

        cx = (off1[0] + w + off2[0]) / 2 + 10
        parts.append(draw_congruence_symbol(cx, 35 + available_height/2 - 15, size=45))
        parts.append(draw_label(width/2, TITLE_Y, "LAL → Congruentes", weight="bold"))

    elif mode == 'example_ambiguous':
        # SSA AMBIGUOUS CASE: Two different triangles with SAME L-L-A data
        # Given: Angle A = 30°, Side AC = 8 (adjacent), Side BC = 6 (opposite to A)
        # 
        # Construction:
        # - A at origin (0,0)
        # - C at 30° from x-axis, distance 8: C = (8*cos30, -8*sin30)
        # - B is on x-axis at distance 6 from C
        # - Two solutions: B1 and B2
        
        scale = 16
        rad30 = math.radians(30)
        
        # Point C (same for both triangles)
        Cx = 8 * scale * math.cos(rad30)  # ~6.93 * scale
        Cy = -8 * scale * math.sin(rad30) # -4 * scale (up in SVG)
        
        # B on x-axis (y=0) at distance 6*scale from C
        # (Bx - Cx)^2 + Cy^2 = (6*scale)^2
        # Bx = Cx ± sqrt((6*scale)^2 - Cy^2)
        dist_BC = 6 * scale
        delta = math.sqrt(dist_BC**2 - Cy**2)  # sqrt(36 - 16) * scale = ~4.47 * scale
        
        B1x = Cx + delta  # Wider triangle
        B2x = Cx - delta  # Narrower triangle
        
        # Triangle 1 (wide base)
        T1_raw = [(0, 0), (B1x, 0), (Cx, Cy)]
        # Triangle 2 (narrow base)
        T2_raw = [(0, 0), (B2x, 0), (Cx, Cy)]
        
        w1 = B1x
        w2 = max(B2x, Cx)  # Ensure positive width
        h = abs(Cy)
        
        # Layout: Both triangles side by side
        gap = 70
        total_w = w1 + gap + w2
        start_x = (width - total_w) / 2
        center_y = 35 + available_height / 2
        base_y = center_y + h / 2
        
        off1 = (start_x, base_y)
        off2 = (start_x + w1 + gap, base_y)
        
        T1 = transform(T1_raw, 1.0, off1)
        T2 = transform(T2_raw, 1.0, off2)
        
        # Draw both triangles
        parts.append(draw_triangle(T1, stroke=COLORS['primary']))
        parts.append(draw_triangle(T2, stroke=COLORS['medianas']))
        
        # Labels for Triangle 1
        # Side AC = 8
        parts.append(draw_label((T1[0][0]+T1[2][0])/2 - 15, (T1[0][1]+T1[2][1])/2 - 5, "8", color=COLORS['primary']))
        # Side BC = 6
        parts.append(draw_label((T1[1][0]+T1[2][0])/2 + 15, (T1[1][1]+T1[2][1])/2 - 5, "6", color=COLORS['primary']))
        # Angle A = 30°
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, radius=30, color=COLORS['danger']))
        parts.append(draw_label(T1[0][0] + 45, T1[0][1] - 12, "30°", size=14, color=COLORS['danger']))
        
        # Labels for Triangle 2
        # Side AC = 8
        parts.append(draw_label((T2[0][0]+T2[2][0])/2 - 15, (T2[0][1]+T2[2][1])/2 - 5, "8", color=COLORS['medianas']))
        # Side BC = 6
        parts.append(draw_label((T2[1][0]+T2[2][0])/2 + 15, (T2[1][1]+T2[2][1])/2 - 5, "6", color=COLORS['medianas']))
        # Angle A = 30°
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, radius=30, color=COLORS['danger']))
        parts.append(draw_label(T2[0][0] + 45, T2[0][1] - 12, "30°", size=14, color=COLORS['danger']))
        
        # NOT EQUAL symbol between triangles
        cx = (off1[0] + w1 + off2[0]) / 2 + 10
        parts.append(draw_label(cx, center_y, "≠", size=50, weight="bold", color="red"))
        
        parts.append(draw_label(width/2, TITLE_Y, "Mismos datos (6, 8, 30°), triángulos distintos", weight="bold", color="red", size=16))

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

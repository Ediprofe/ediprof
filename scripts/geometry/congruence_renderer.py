
import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS

def generate_svg_main(mode, output_path):
    width = 600
    height = 300
    parts = []
    
    # Background
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>')
    # Optional debug border
    # parts.append(f'<rect width="{width}" height="{height}" fill="none" stroke="red"/>')

    # --- Helpers ---
    def draw_triangle(pts, stroke=COLORS["line"], fill="none", stroke_width=2, stroke_colors=None):
        # stroke_colors: list of 3 colors for sides [p0-p1, p1-p2, p2-p0]
        if stroke_colors:
            # Draw individual lines
            path = ""
            for i in range(3):
                p_start = pts[i]
                p_end = pts[(i+1)%3]
                color = stroke_colors[i]
                path += f'<line x1="{p_start[0]}" y1="{p_start[1]}" x2="{p_end[0]}" y2="{p_end[1]}" stroke="{color}" stroke-width="{stroke_width+1}" stroke-linecap="round"/>'
            return path
        else:
            path = f"M {pts[0][0]} {pts[0][1]} L {pts[1][0]} {pts[1][1]} L {pts[2][0]} {pts[2][1]} Z"
            return f'<path d="{path}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linejoin="round"/>'

    def draw_tick_mark(p1, p2, count=1, color=COLORS["text"]):
        # Diagonal slash mark on segment
        mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
        dx, dy = p2[0]-p1[0], p2[1]-p1[1]
        length = math.hypot(dx, dy)
        if length < 1e-6: return ""
        
        # Unit vector along line
        ux, uy = dx/length, dy/length
        # Normal vector
        nx, ny = -uy, ux
        
        # Diagonal direction (mix of tangent and normal)
        # 45 degreesish
        diag_x = ux*0.5 + nx*0.8
        diag_y = uy*0.5 + ny*0.8
        
        spacing = 5
        start = -((count-1)*spacing)/2
        svg = ""
        for i in range(count):
            off = start + i*spacing
            cx, cy = mx + ux*off, my + uy*off
            
            # Draw diagonal slash len ~10
            x1, y1 = cx - diag_x*6, cy - diag_y*6
            x2, y2 = cx + diag_x*6, cy + diag_y*6
            
            svg += f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="2"/>'
        return svg

    def draw_angle_arc(center, p1, p2, count=1, radius=25, color=COLORS["line"], fill_opacity=0.2):
        # Draw arc with fill
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
        
        # Filled sector
        sector_path = f"M {center[0]} {center[1]} L {sx:.2f} {sy:.2f} A {radius} {radius} 0 0 1 {ex:.2f} {ey:.2f} Z"
        
        svg = f'<path d="{sector_path}" fill="{color}" fill-opacity="{fill_opacity}" stroke="none"/>'
        
        # Arcs/Strokes
        gap = 5
        for i in range(count):
            r = radius - i*gap # Go inwards for multiple arcs
            sx_r = center[0] + r * math.cos(ang1)
            sy_r = center[1] + r * math.sin(ang1)
            ex_r = center[0] + r * math.cos(ang2)
            ey_r = center[1] + r * math.sin(ang2)
            svg += f'<path d="M {sx_r:.2f} {sy_r:.2f} A {r} {r} 0 0 1 {ex_r:.2f} {ey_r:.2f}" fill="none" stroke="{color}" stroke-width="2"/>'
            
        return svg

    def draw_label(x, y, text, color=COLORS["text"], size=16, weight="normal"):
        return f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="middle">{text}</text>'

    # --- Geometry Setup ---
    # Colors for pairs
    C_PAIR1 = COLORS['primary']      # Blue
    C_PAIR2 = COLORS['medianas']     # Teal/Green
    C_PAIR3 = COLORS['danger']       # Red/Orange
    C_NEUTRAL = COLORS['line']       # Gray/Dark
    
    # ... (rest of geometry setup same as before)
    def transform(pts, dx, dy):
        return [(p[0]+dx, p[1]+dy) for p in pts]
        
    base_tri = [(20, 180), (180, 180), (70, 50)] # Slightly nicer shape
    
    if mode == 'definition':
        offset1 = (40, 50)
        offset2 = (340, 50)
        T1 = transform(base_tri, *offset1)
        T2 = transform(base_tri, *offset2)
        
        # Draw sides with COLORS
        # Side 0-1 (Bottom): Pair 1
        # Side 1-2 (Right): Pair 2
        # Side 2-0 (Left): Pair 3
        # Use simple stroke drawing for colored sides
        
        parts.append(draw_triangle(T1, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        parts.append(draw_triangle(T2, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        
        # Marks (Diagonal ticks matching color)
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T1[1], T1[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T1[2], T1[0], 3, C_PAIR3))
        
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[1], T2[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T2[2], T2[0], 3, C_PAIR3))
        
        # Angles with COLORS (use same as adjacent side or distinctive?)
        # Let's use the colors but purely for angles now.
        # Angle 0 (Left): Pair 1 color
        # Angle 1 (Right): Pair 2 color
        # Angle 2 (Top): Pair 3 color
        # Actually better to use separate colors if confusing, but let's stick to pairs.
        
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, color=C_PAIR3)) # A
        parts.append(draw_angle_arc(T1[1], T1[0], T1[2], 2, color=C_PAIR1)) # B
        parts.append(draw_angle_arc(T1[2], T1[0], T1[1], 3, color=C_PAIR2)) # C
        
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, color=C_PAIR3))
        parts.append(draw_angle_arc(T2[1], T2[0], T2[2], 2, color=C_PAIR1))
        parts.append(draw_angle_arc(T2[2], T2[0], T2[1], 3, color=C_PAIR2))
        
        parts.append(draw_label(300, 280, "Partes Correspondientes (Color)", weight="bold"))

    elif mode == 'criterion_lll':
        offset1 = (40, 50)
        offset2 = (340, 50)
        T1 = transform(base_tri, *offset1)
        T2 = transform(base_tri, *offset2)
        
        # Color the sides only!
        parts.append(draw_triangle(T1, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        parts.append(draw_triangle(T2, stroke_colors=[C_PAIR1, C_PAIR2, C_PAIR3]))
        
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T1[1], T1[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T1[2], T1[0], 3, C_PAIR3))
        
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[1], T2[2], 2, C_PAIR2))
        parts.append(draw_tick_mark(T2[2], T2[0], 3, C_PAIR3))
        
        parts.append(draw_label(300, 280, "Lado-Lado-Lado (Colores)", weight="bold"))

    elif mode == 'criterion_lal':
        offset1 = (40, 50)
        offset2 = (340, 50)
        T1 = transform(base_tri, *offset1)
        T2 = transform(base_tri, *offset2)
        
        # Sides 0-1 and 2-0 defined. Angle 0 defined.
        # Draw full triangle neutral, overwrite colored parts
        parts.append(draw_triangle(T1, stroke=COLORS['auxiliary']))
        parts.append(draw_triangle(T2, stroke=COLORS['auxiliary']))
        
        # Colored Side 1 (Bottom)
        parts.append(f'<line x1="{T1[0][0]}" y1="{T1[0][1]}" x2="{T1[1][0]}" y2="{T1[1][1]}" stroke="{C_PAIR1}" stroke-width="4"/>')
        parts.append(f'<line x1="{T2[0][0]}" y1="{T2[0][1]}" x2="{T2[1][0]}" y2="{T2[1][1]}" stroke="{C_PAIR1}" stroke-width="4"/>')
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        
        # Colored Side 2 (Left)
        parts.append(f'<line x1="{T1[2][0]}" y1="{T1[2][1]}" x2="{T1[0][0]}" y2="{T1[0][1]}" stroke="{C_PAIR2}" stroke-width="4"/>')
        parts.append(f'<line x1="{T2[2][0]}" y1="{T2[2][1]}" x2="{T2[0][0]}" y2="{T2[0][1]}" stroke="{C_PAIR2}" stroke-width="4"/>')
        parts.append(draw_tick_mark(T1[2], T1[0], 2, C_PAIR2))
        parts.append(draw_tick_mark(T2[2], T2[0], 2, C_PAIR2))
        
        # Angle between (at 0)
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, color=C_PAIR3, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, color=C_PAIR3, fill_opacity=0.4))
        
        parts.append(draw_label(300, 280, "Lado-Ángulo(Color)-Lado", weight="bold"))

    elif mode == 'criterion_ala':
        offset1 = (40, 50)
        offset2 = (340, 50)
        T1 = transform(base_tri, *offset1)
        T2 = transform(base_tri, *offset2)
        
        parts.append(draw_triangle(T1, stroke=COLORS['auxiliary']))
        parts.append(draw_triangle(T2, stroke=COLORS['auxiliary']))
        
        # Side between (Bottom)
        parts.append(f'<line x1="{T1[0][0]}" y1="{T1[0][1]}" x2="{T1[1][0]}" y2="{T1[1][1]}" stroke="{C_PAIR1}" stroke-width="4"/>')
        parts.append(f'<line x1="{T2[0][0]}" y1="{T2[0][1]}" x2="{T2[1][0]}" y2="{T2[1][1]}" stroke="{C_PAIR1}" stroke-width="4"/>')
        parts.append(draw_tick_mark(T1[0], T1[1], 1, C_PAIR1))
        parts.append(draw_tick_mark(T2[0], T2[1], 1, C_PAIR1))
        
        # Angle Left (0)
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, color=C_PAIR2, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, color=C_PAIR2, fill_opacity=0.4))
        
        # Angle Right (1)
        parts.append(draw_angle_arc(T1[1], T1[0], T1[2], 2, color=C_PAIR3, fill_opacity=0.4))
        parts.append(draw_angle_arc(T2[1], T2[0], T2[2], 2, color=C_PAIR3, fill_opacity=0.4))
        
        parts.append(draw_label(300, 280, "Ángulo-Lado-Ángulo", weight="bold"))

    elif mode == 'example_lll_345':
        # Draw a 3-4-5 triangle scaled (Right triangle)
        # 3*40=120, 4*40=160, 5*40=200
        scale = 30
        tri_345 = [(0, 4*scale), (3*scale, 4*scale), (0, 0)] # A=(0,120), B=(90,120), C=(0,0) -> AB=90(3), AC=120(4), BC=150(5). Wait.
        # coords: A(0,0), B(3,0), C(0,4)? Dist(AB)=3, Dist(AC)=4, Dist(BC)=5. 
        # Correct coords: (0, 4), (3, 4), (0, 0)? No.
        # A=(0,H), B=(W, H), C=(0, 0).
        # AB length = W. AC length = H. BC length = sqrt(W^2+H^2).
        # We want sides 3, 4, 5. So W=3, H=4 -> Hyp=5.
        
        base_345 = [(20, 150), (20+3*scale, 150), (20, 150-4*scale)] # Right angle at bottom left
        
        offset1 = (40, 50)
        offset2 = (340, 50)
        
        T1 = transform(base_345, *offset1)
        T2 = transform(base_345, *offset2)
        
        parts.append(draw_triangle(T1))
        parts.append(draw_triangle(T2))
        
        # Labels for sides
        # T1
        parts.append(draw_label((T1[0][0]+T1[1][0])/2, T1[0][1]+20, "3", color=COLORS['primary']))
        parts.append(draw_label(T1[0][0]-15, (T1[0][1]+T1[2][1])/2, "4", color=COLORS['primary']))
        parts.append(draw_label((T1[1][0]+T1[2][0])/2+10, (T1[1][1]+T1[2][1])/2, "5", color=COLORS['primary']))
        
        # T2
        parts.append(draw_label((T2[0][0]+T2[1][0])/2, T2[0][1]+20, "3", color=COLORS['primary']))
        parts.append(draw_label(T2[0][0]-15, (T2[0][1]+T2[2][1])/2, "4", color=COLORS['primary']))
        parts.append(draw_label((T2[1][0]+T2[2][0])/2+10, (T2[1][1]+T2[2][1])/2, "5", color=COLORS['primary']))
        
        parts.append(draw_label(300, 280, "Lados idénticos → Congruentes", weight="bold"))

    elif mode == 'example_lal_5740':
        # Side 5, Side 7, Angle 40
        # Draw base side 7, angle 40, side 5.
        scale = 20
        # A at origin. B at (7, 0). C at (5*cos40, -5*sin40)
        rad = math.radians(40)
        pA = (0, 0)
        pB = (7*scale, 0)
        pC = (5*scale*math.cos(rad), -5*scale*math.sin(rad))
        
        base_tri = [pA, pB, pC] # Note: y is negative going up in normal coords, but in SVG y+ is down. 
        # So for SVG angle going "up" visually, y needs to be negative? No, SVG y=0 is top.
        # Let's map to screen coords.
        # We want A at bottom-left. B to right. C up-right.
        
        # Manual adjustment for SVG placement
        # Local coords
        base_local = [ (20, 180), (20+7*scale, 180), (20+5*scale*math.cos(rad), 180-5*scale*math.sin(rad)) ]
        
        offset1 = (40, 20)
        offset2 = (340, 20)
        
        T1 = transform(base_local, *offset1)
        T2 = transform(base_local, *offset2)
        
        parts.append(draw_triangle(T1))
        parts.append(draw_triangle(T2))
        
        # Labels: Side 7 (Bottom), Side 5 (Left-slope), Angle 40 (Left)
        # T1
        parts.append(draw_label((T1[0][0]+T1[1][0])/2, T1[0][1]+20, "7", color=COLORS['primary']))
        parts.append(draw_label((T1[0][0]+T1[2][0])/2-15, (T1[0][1]+T1[2][1])/2, "5", color=COLORS['primary']))
        parts.append(draw_angle_arc(T1[0], T1[1], T1[2], 1, radius=25))
        parts.append(draw_label(T1[0][0]+40, T1[0][1]-10, "40°", size=12, color=COLORS['danger']))
        
        # T2
        parts.append(draw_label((T2[0][0]+T2[1][0])/2, T2[0][1]+20, "7", color=COLORS['primary']))
        parts.append(draw_label((T2[0][0]+T2[2][0])/2-15, (T2[0][1]+T2[2][1])/2, "5", color=COLORS['primary']))
        parts.append(draw_angle_arc(T2[0], T2[1], T2[2], 1, radius=25))
        parts.append(draw_label(T2[0][0]+40, T2[0][1]-10, "40°", size=12, color=COLORS['danger']))
        
        parts.append(draw_label(300, 280, "Lado-Ángulo-Lado coincide", weight="bold"))

    elif mode == 'example_ambiguous':
        # Side a=6, Side b=8, Angle B=30 (Opposite to b=8) -> Unique because 8>6.
        # User text: "Lados 6 y 8, ángulo opuesto al lado 8 es 30°"
        # Wait, if angle given is opposite to 8, then we have (Side 6, Side 8, Angle 30 opposite to 8).
        # Adjacent side to 30 is 6? 
        # Let's draw: Point A. Line AB length 6. Angle at A? No.
        # Let's say Angle given is at vertex B relative to side c=6?
        # A common ambiguous case config: Side b, Side a, Angle A.
        # User says: "Lados 6 y 8, ángulo opuesto al lado 8".
        # So we have pair (Lado=8, Angle=30) and other Lado=6.
        # This is SSA where Side(Opposite) > Side(Adjacent). 8 > 6.
        # This is NOT ambiguous geometrically (1 solution), but PEDAGOGICALLY it illustrates "Angle not inclusive".
        
        # Layout: 
        # Draw Side 6 horizontal? Or Side 8?
        # Typically draw "Angle side" horizontal.
        # Let's draw the "Unknown side" horizontal.
        # Vertex C (where angle 30 is NOT). Vertex B (where angle 30 is?).
        # Let's assume Angle is alpha=30. Adjacent side is 6. Opposite side is 8.
        # Draw ray from Origin at 30 degrees.
        # Draw horizontal line.
        # Wait, usually we draw horizontal side = 6 (Adjacent). 
        # Angle 30 at left.
        # Then opposite side 8 swings from geometrical top. 
        # But if Adj=6, Opp=8... 8 is longer than 6. It hits way out.
        
        # Visual setup:
        # A at left. Side c=6 along 30 deg? Or flat?
        # Let's put c=6 flat. A=(0,0), B=(6,0). Angle at A?
        # If angle at A is 30, then opposite side 'a' would be... ?
        # Text: "ángulo opuesto al lado 8 es 30".
        # So angle is 30. Opposite side is 8. Other side is 6.
        # So Angle 30 is opposite to 8.
        # Adjacent side is 6.
        
        scale = 25
        # Draw Angle 30 at Vertex A.
        # Side AC = 6 (Adjacent).
        # Side CB = 8 (Opposite).
        
        # A at origin. C on horizontal? Or C at 30 deg?
        # Let's put AC on horizontal for clarity.
        # A=(0,0), C=(6*scale, 0).
        # Angle at A is NOT 30. Angle at A is opposite to... wait.
        # Angle opposite to 8 is 30.
        # If Opp=8, Adj=6.
        # Let Angle be at vertex B?
        # Let's construct:
        # Vertex V1. Side len 6 to V2.
        # Angle 30 is NOT at V1 (that would make 6 adj). It IS at V1!
        # Yes: we have Side 6, Side 8. Angle opposite to 8 is 30.
        # So at vertex V_alpha, we have side 6. From end of 6, side 8 goes to meet the ray from V_alpha?
        # No. Side 8 is OPPOSITE to 30.
        # So we have Angle 30. One defining arm has length "unknown". The other arm is determined by close of triangle.
        # But we know one side IS 6. Is 6 adjacent or opposite?
        # 6 is the OTHER side. So 6 is adjacent to the 30 deg angle?
        # Yes. If 6 was opposite, the angle opposite 6 would be unknown.
        # So Setup:
        # Angle alpha = 30.
        # Adjacent Side = 6.
        # Opposite Side = 8.
        
        # Let's draw:
        # Vertex A. Ray R1 horizontal. Ray R2 at 30 deg.
        # Put Side 6 on R1? Or R2?
        # Put Side 6 on R2 (fixed leg). B is at dist 6 from A.
        # From B, swing radius 8.
        # Where does it hit R1?
        # It hits R1 at C1.
        
        rad30 = math.radians(30)
        pA = (0, 0)
        # B on 30 deg ray, len 6.
        pB = (6*scale*math.cos(rad30), -6*scale*math.sin(rad30)) # SVG y-up is negative
        
        # Now find C on horizontal (y=0) such that dist(B, C) = 8
        # (x_c - x_b)^2 + (0 - y_b)^2 = 8^2
        # (x_c - x_b)^2 = 64 - y_b^2
        y_b_val = -pB[1]/scale
        # y_b for calculation is 6*sin30 = 3.
        # 64 - 3^2 = 64 - 9 = 55.
        # x_c - x_b = +/- sqrt(55). sqrt(55) ~ 7.4.
        # x_b = 6*cos30 ~ 5.2.
        # C1 = 5.2 + 7.4 = 12.6.
        # C2 = 5.2 - 7.4 = -2.2. (Negative, so normally discarded if ray starts at A)
        
        # So there is only 1 geometric triangle!
        # But we want to illustrate "Ambiguity" or "Non-congruence criterion".
        # Show the setup:
        # Drawn Side 6.
        # Drawn Angle 30.
        # Drawn Side 8 connecting them.
        # Label elements. Mark Angle with color. Mark Sides.
        # Add visual "Warning": The angle is NOT between the sides.
        
        # Local offset transform
        def to_screen(pt): return (pt[0]+250, pt[1]+200) # Centered
        
        pC_calc = (pB[0] + math.sqrt((8*scale)**2 - pB[1]**2), 0)
        
        T_amb = [pA, pB, pC_calc]
        
        # Shift to screen
        T_screen = [(p[0]+150, p[1]+220) for p in T_amb] # A at 150,220
        
        # Draw
        parts.append(draw_triangle(T_screen))
        
        # Marks
        # Side 6 (AB)
        parts.append(draw_label((T_screen[0][0]+T_screen[1][0])/2-10, (T_screen[0][1]+T_screen[1][1])/2-10, "6", color=COLORS['primary']))
        # Side 8 (BC)
        parts.append(draw_label((T_screen[1][0]+T_screen[2][0])/2+10, (T_screen[1][1]+T_screen[2][1])/2-10, "8", color=COLORS['primary']))
        # Angle 30 at A
        parts.append(draw_angle_arc(T_screen[0], T_screen[2], T_screen[1], 1, radius=40))
        parts.append(draw_label(T_screen[0][0]+50, T_screen[0][1]-10, "30°", color=COLORS['danger']))
        
        # Visual indicator that Angle is not included
        # Draw explicit arrow pointing to "included angle" (at B) with "?"
        inc_ang_loc = T_screen[1]
        parts.append(draw_label(inc_ang_loc[0]+10, inc_ang_loc[1]-20, "?", color="red", size=24, weight="bold"))
        parts.append(draw_label(300, 280, "¿Ángulo en medio? NO -> LAL falla", color="red", weight="bold"))

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

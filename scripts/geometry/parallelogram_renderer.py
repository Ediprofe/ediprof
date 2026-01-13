
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

def draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color='none', stroke_width=3, fill_opacity=0.1):
    path_d = f"M {points[0][0]} {points[0][1]} L {points[1][0]} {points[1][1]} L {points[2][0]} {points[2][1]} L {points[3][0]} {points[3][1]} Z"
    parts.append(f'<path d="{path_d}" fill="{fill_color}" fill-opacity="{fill_opacity}" stroke="{stroke_color}" stroke-width="{stroke_width}"/>')

def draw_parallel_mark(parts, p1, p2, count=1, color=COLORS['text']):
    # Draw arrows on the segment p1-p2
    mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    
    size = 10
    gap = 5
    
    # Arrow head shape
    def draw_arrow(cx, cy):
        # Rotate arrow points
        # Simple chevron >
        # Tip at cx,cy. Back points rotated.
        # Actually let's put the center of the mark at cx,cy
        # Tip: (cx + size/2, cy) rotated
        tip_x = cx + (size/2) * math.cos(angle)
        tip_y = cy + (size/2) * math.sin(angle)
        
        # Base: (cx - size/2, cy)
        base_x = cx - (size/2) * math.cos(angle)
        base_y = cy - (size/2) * math.sin(angle)
        
        # Wings
        wing_angle = math.pi * 3/4 # 135 deg
        w1_x = tip_x + size * math.cos(angle + wing_angle)
        w1_y = tip_y + size * math.sin(angle + wing_angle)
        
        w2_x = tip_x + size * math.cos(angle - wing_angle)
        w2_y = tip_y + size * math.sin(angle - wing_angle)
        
        parts.append(f'<polyline points="{w1_x:.2f},{w1_y:.2f} {tip_x:.2f},{tip_y:.2f} {w2_x:.2f},{w2_y:.2f}" fill="none" stroke="{color}" stroke-width="2"/>')

    # Draw multiple arrows centered
    start_offset = - (count - 1) * gap / 2
    for i in range(count):
        off = start_offset + i * gap
        # Move center along the line
        mcx = mid[0] + off * math.cos(angle)
        mcy = mid[1] + off * math.sin(angle)
        draw_arrow(mcx, mcy)

def draw_tick_mark(parts, p1, p2, count=1, color=COLORS['text']):
    mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    angle = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    perp_angle = angle + math.pi/2
    
    size = 10
    gap = 4
    
    start_offset = - (count - 1) * gap / 2
    for i in range(count):
        off = start_offset + i * gap
        # Center of this tick
        cx = mid[0] + off * math.cos(angle)
        cy = mid[1] + off * math.sin(angle)
        
        # Line perp
        x1 = cx + (size/2) * math.cos(perp_angle)
        y1 = cy + (size/2) * math.sin(perp_angle)
        x2 = cx - (size/2) * math.cos(perp_angle)
        y2 = cy - (size/2) * math.sin(perp_angle)
        
        parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="2"/>')

def draw_parallelogram_scene(parts, width, height, mode='concept_definition'):
    cx, cy = width / 2, height / 2
    
    # Standard Parallelogram Geometry
    # Base b=200, height h=120, lean=60
    b = 200
    h = 140
    lean = 50
    
    # Centered
    # Top-Left (A), Top-Right (B)
    # Bot-Right (C), Bot-Left (D)
    # Wait, usually A bottom-left counter-clockwise
    # Let's do A bottom-left
    
    # A = (cx - b/2 - lean/2, cy + h/2)
    # B = (cx + b/2 - lean/2, cy + h/2)
    # C = (cx + b/2 + lean/2, cy - h/2)
    # D = (cx - b/2 + lean/2, cy - h/2)
    
    # Standard: A=bottom-left, B=bottom-right, C=top-right, D=top-left
    # A (x, y)
    # B (x+b, y)
    # C (x+b+lean, y-h)
    # D (x+lean, y-h)
    
    # Centering
    total_w = b + lean
    start_x = cx - total_w/2
    start_y = cy + h/2 - 20 # bit up
    
    A = (start_x, start_y)
    B = (start_x + b, start_y)
    C = (start_x + b + lean, start_y - h)
    D = (start_x + lean, start_y - h)
    
    points = [A, B, C, D]
    
    # --- 1. Concept: Definition ---
    if mode == 'concept_definition':
        title = "Definición de Paralelogramo"
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Parallel marks
        # AB || DC ( > )
        draw_parallel_mark(parts, A, B, 1, COLORS['text'])
        draw_parallel_mark(parts, D, C, 1, COLORS['text'])
        
        # AD || BC ( >> )
        # Note: D->A direction or A->D. Let's start from bottom. A->D is up.
        draw_parallel_mark(parts, A, D, 2, COLORS['text'])
        draw_parallel_mark(parts, B, C, 2, COLORS['text'])
        
        # Labels for vertices to match text
        parts.append(draw_label(A[0]-25, A[1], "A", COLORS['vertices']))
        parts.append(draw_label(B[0]+25, B[1], "B", COLORS['vertices']))
        parts.append(draw_label(C[0]+25, C[1], "C", COLORS['vertices']))
        parts.append(draw_label(D[0]-25, D[1], "D", COLORS['vertices']))
        
        parts.append(draw_label(cx, cy + h/2 + 40, "Dos pares de lados paralelos", COLORS['text'], size=18))
        return title

    # --- 2. Concept: Properties ---
    elif mode == 'concept_properties':
        title = "Propiedades: Lados y Ángulos"
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Equal Sides
        draw_tick_mark(parts, A, B, 1, COLORS['secondary'])
        draw_tick_mark(parts, C, D, 1, COLORS['secondary']) # Top
        
        draw_tick_mark(parts, A, D, 2, COLORS['secondary'])
        draw_tick_mark(parts, B, C, 2, COLORS['secondary'])
        
        # Equal Angles
        # A and C are acute here? No, A and C are opposite.
        # A is bottom-left. D top-left (leaned). A is obtuse? No.
        # Check coords.
        # A(start_x, start_y). D(start_x+lean, start_y-h).
        # Vector AD = (lean, -h). Leans right. So A is Acute?
        # A (0,0) -> D(lean, -h). Angle is < 90. Yes acute.
        # B (b, 0) -> C(b+lean, -h). Angle at B is obtuse (180 - A).
        
        parts.append(draw_angle_arc(A, B, D, radius=30, color=COLORS['danger']))
        parts.append(draw_label(A[0]+30, A[1]-15, "α", COLORS['text']))
        
        parts.append(draw_angle_arc(C, D, B, radius=30, color=COLORS['danger'])) # Opposite to A
        parts.append(draw_label(C[0]-30, C[1]+15, "α", COLORS['text']))
        
        parts.append(draw_angle_arc(B, C, A, radius=30, color=COLORS['success'], marks=2))
        parts.append(draw_label(B[0]-25, B[1]-15, "β", COLORS['text']))
        
        parts.append(draw_angle_arc(D, A, C, radius=30, color=COLORS['success'], marks=2))
        parts.append(draw_label(D[0]+25, D[1]+15, "β", COLORS['text']))
        
        parts.append(draw_label(cx, cy+h/2+40, "Lados Opuestos Iguales | Ángulos Opuestos Iguales", COLORS['text_light'], size=16))
        return title

    # --- 2.5 Concept: Consecutive Angles ---
    elif mode == 'concept_consecutive_angles':
        title = "Ángulos Consecutivos (Suplementarios)"
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Mark Angle A (alpha)
        parts.append(draw_angle_arc(A, B, D, radius=40, color=COLORS['danger']))
        parts.append(draw_label(A[0]+40, A[1]-15, "α", COLORS['text']))
        
        # Mark Angle B (beta) - consecutive to A
        parts.append(draw_angle_arc(B, C, A, radius=40, color=COLORS['success'], marks=2))
        parts.append(draw_label(B[0]-35, B[1]-15, "β", COLORS['text']))
        
        # Formula Box (Higher to avoid overlap)
        parts.append(f'<rect x="{cx-80}" y="{cy-80}" width="160" height="60" rx="6" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, cy-50, "α + β = 180°", COLORS['text'], size=22, weight='bold'))
        
        # Visual proof hint: Extend line AB to right
        E = (B[0] + 80, B[1])
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{E[0]}" y2="{E[1]}" stroke="{COLORS["text_light"]}" stroke-dasharray="4,4"/>')
        
        # Angle CBE is alpha (corresponding angles if AD || BC... wait AD || BC. AB intersects. 
        # Line AB is transversal? No.
        # AD || BC. Transversal is AB. Interior consecutive angles sum to 180.
        # Visual correspondence: Extend AB. Angle at B outside is...
        # If AB || DC. Transversal BC. Angle C + Angle B = 180.
        # Let's stick to the formula and clean highlights.
        
        return title

    # --- 3. Concept: Diagonals ---
    elif mode == 'concept_diagonals':
        title = "Las Diagonales se Bisecan"
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Draw Diagonals
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        
        # Intersection
        mid_x = (A[0] + C[0]) / 2
        mid_y = (A[1] + C[1]) / 2
        M = (mid_x, mid_y)
        
        parts.append(draw_label(M[0], M[1]-15, "M", COLORS['text']))
        
        # Tick marks on diagonal segments
        # AM = MC
        draw_tick_mark(parts, A, M, 3, COLORS['medianas'])
        draw_tick_mark(parts, M, C, 3, COLORS['medianas'])
        
        # DM = MB
        draw_tick_mark(parts, D, M, 1, COLORS['medianas']) # vertical tick geometry
        draw_tick_mark(parts, M, B, 1, COLORS['medianas'])
        
        return title

        return title

    # --- 3.5 Concept: Perimeter ---
    elif mode == 'concept_perimeter':
        title = "Perímetro = Suma de Lados"
        # Only contour
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'], stroke_width=4)
        
        # Labels for sides
        # Bottom b
        parts.append(draw_label((A[0]+B[0])/2, A[1]+25, "b", COLORS['text'], weight='bold', size=24))
        # Top b
        parts.append(draw_label((D[0]+C[0])/2, D[1]-25, "b", COLORS['text'], weight='bold', size=24))
        
        # Left a
        parts.append(draw_label((A[0]+D[0])/2 - 25, (A[1]+D[1])/2, "a", COLORS['text'], weight='bold', size=24))
        # Right a
        parts.append(draw_label((B[0]+C[0])/2 + 25, (B[1]+C[1])/2, "a", COLORS['text'], weight='bold', size=24))
        
        # Formula
        parts.append(f'<rect x="{cx-90}" y="{cy-30}" width="180" height="60" rx="6" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, cy+5, "P = 2a + 2b", COLORS['text'], size=24, weight='bold'))
        
        return title

    # --- 4. Concept: Area ---
    elif mode == 'concept_area':
        title = "Área = Base × Altura"
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Height Line (Perpendicular from D to base AB extended or intersect)
        # Vertical line from D down to y of AB
        H_point = (D[0], A[1]) # Same x as D, same y as A/B
        
        # Dashed projection
        parts.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="{H_point[0]}" y2="{H_point[1]}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        
        # Right angle mark at H
        ra_size=15
        parts.append(f'<path d="M {H_point[0]} {H_point[1]-ra_size} L {H_point[0]+ra_size} {H_point[1]-ra_size} L {H_point[0]+ra_size} {H_point[1]}" fill="none" stroke="{COLORS["danger"]}"/>')
        
        # Labels
        parts.append(draw_label((A[0]+B[0])/2, A[1]+20, "Base (b)", COLORS['text'], weight='bold'))
        parts.append(draw_label(D[0]-15, (D[1]+H_point[1])/2, "h", COLORS['danger'], weight='bold'))
        
        # Contrast with slanted side
        parts.append(draw_label((B[0]+C[0])/2 + 10, (B[1]+C[1])/2, "lado", COLORS['text_light'], size=14))
        
        return title

    # --- 5. Example 1: Angles ---
    elif mode == 'example_angles':
        title = "Cálculo de Ángulos"
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Known A = 60
        parts.append(draw_angle_arc(A, B, D, radius=30, color=COLORS['secondary']))
        parts.append(draw_label(A[0]+25, A[1]-15, "60°", COLORS['text'], weight='bold'))
        
        # Result C = 60
        parts.append(draw_label(C[0]-25, C[1]+15, "60°", COLORS['success'], weight='bold'))
        
        # Result B = 120
        parts.append(draw_label(B[0]-25, B[1]-15, "120°", COLORS['success'], weight='bold'))
        
        # Result D = 120
        parts.append(draw_label(D[0]+25, D[1]+15, "120°", COLORS['success'], weight='bold'))
        
        # Reasoning text
        parts.append(draw_label(cx, cy+h/2+40, "Opuestos iguales, Consecutivos suman 180°", COLORS['text_light'], size=16))
        
        return title

    # --- 6. Example 2: Area ---
    elif mode == 'example_area':
        title = "Ejemplo de Área"
        
        # Custom smaller dimensions for scale? Or just label standard.
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Labels: Base=10, Height=4, Side=5
        parts.append(draw_label((A[0]+B[0])/2, A[1]+20, "10 cm", COLORS['text'], weight='bold'))
        
        # Height
        H_point = (D[0], A[1])
        parts.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="{H_point[0]}" y2="{H_point[1]}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        parts.append(draw_label(D[0]-15, (D[1]+H_point[1])/2, "4 cm", COLORS['danger'], weight='bold'))
        
        # Slanted Side (Label on right BC)
        parts.append(draw_label((B[0]+C[0])/2 + 25, (B[1]+C[1])/2, "5 cm", COLORS['text_light']))
        
        # Formula
        parts.append(f'<rect x="{cx-70}" y="{cy-30}" width="140" height="60" rx="6" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, cy, "A = 10 × 4", COLORS['text']))
        parts.append(draw_label(cx, cy+20, "A = 40", COLORS['text'], weight='bold'))
        
        return title

    # --- 7. Summary ---
    elif mode == 'summary_all':
        title = ""
        # 4 Panels? Or one big diagram with everything?
        # A single rich diagram usually works best for constraints
        
        # Let's do a panel split 2x2 roughly? No, 600x460 is tight.
        # Let's do a central large parallelogram with all features annotated in different colors.
        
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # 1. Parallels
        draw_parallel_mark(parts, A, B, 1, COLORS['primary'])
        draw_parallel_mark(parts, D, C, 1, COLORS['primary'])
        
        # 2. Sides Equal
        # (Use ticks on the other pair to avoid clutter)
        draw_tick_mark(parts, A, D, 2, COLORS['secondary'])
        draw_tick_mark(parts, B, C, 2, COLORS['secondary'])
        
        # 3. Diagonals bisect
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>')
        
        # 4. Angles
        parts.append(draw_angle_arc(A, B, D, radius=25, color=COLORS['text'], fill_opacity=0))
        parts.append(draw_angle_arc(C, D, B, radius=25, color=COLORS['text'], fill_opacity=0))
        
        # Legend/List below
        sy = points[0][1] + 40
        gap = 25
        x_leg = cx - 200 # Shift left for start anchor
        
        def draw_text_left(x, y, text, color):
            return (f'<text x="{x}" y="{y}" font-family="Inter, sans-serif" font-size="16" fill="{color}" '
                    f'text-anchor="start" dominant-baseline="middle">{text}</text>')
        
        parts.append(draw_text_left(x_leg, sy, "1. Lados opuestos paralelos e iguales", COLORS['text']))
        parts.append(draw_text_left(x_leg, sy+gap, "2. Ángulos opuestos iguales", COLORS['text']))
        parts.append(draw_text_left(x_leg, sy+gap*2, "3. Diagonales se bisecan", COLORS['text']))
        parts.append(draw_text_left(x_leg, sy+gap*3, "4. Área = Base × Altura (Perpendicular)", COLORS['text']))
        
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


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

def draw_quadrilateral_scene(parts, width, height, mode='concept_elements'):
    cx, cy = width / 2, height / 2

    # --- 1. Concept: Elements ---
    if mode == 'concept_elements':
        title = "Elementos de un Cuadrilátero"
        
        # Generic Convex Quadrilateral
        A = (cx - 150, cy - 80)
        B = (cx + 100, cy - 100)
        C = (cx + 160, cy + 80)
        D = (cx - 120, cy + 120)
        
        points = [A, B, C, D]
        draw_quad(parts, points, stroke_color=COLORS["primary"], fill_color=COLORS["primary"])
        
        # Diagonal AC
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        # Diagonal BD
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        
        # Labels
        parts.append(draw_label(A[0]-20, A[1]-10, "A", COLORS["vertices"]))
        parts.append(draw_label(B[0]+20, B[1]-10, "B", COLORS["vertices"]))
        parts.append(draw_label(C[0]+20, C[1]+10, "C", COLORS["vertices"]))
        parts.append(draw_label(D[0]-20, D[1]+10, "D", COLORS["vertices"]))
        
        # Angle arcs (approximate)
        parts.append(draw_angle_arc(A, D, B, marks=1, radius=30, color=COLORS["secondary"]))
        parts.append(draw_angle_arc(B, A, C, marks=1, radius=30, color=COLORS["secondary"]))
        parts.append(draw_angle_arc(C, B, D, marks=1, radius=30, color=COLORS["secondary"]))
        parts.append(draw_angle_arc(D, C, A, marks=1, radius=30, color=COLORS["secondary"]))
        
        # Greek labels (inward)
        # Simple inward offset logic: towards centroid roughly
        centroid = ((A[0]+B[0]+C[0]+D[0])/4, (A[1]+B[1]+C[1]+D[1])/4)
        def lerp(p1, p2, t): return (p1[0] + (p2[0]-p1[0])*t, p1[1] + (p2[1]-p1[1])*t)
        
        la = lerp(A, centroid, 0.25)
        lb = lerp(B, centroid, 0.25)
        lc = lerp(C, centroid, 0.25)
        ld = lerp(D, centroid, 0.25)
        
        parts.append(draw_label(la[0], la[1], "α", COLORS["text"], size=16, font_family="KaTeX_Main"))
        parts.append(draw_label(lb[0], lb[1], "β", COLORS["text"], size=16, font_family="KaTeX_Main"))
        parts.append(draw_label(lc[0], lc[1], "γ", COLORS["text"], size=16, font_family="KaTeX_Main"))
        parts.append(draw_label(ld[0], ld[1], "δ", COLORS["text"], size=16, font_family="KaTeX_Main"))
        
        parts.append(draw_label(cx, cy+160, "Lados, Vértices, Ángulos y Diagonales", COLORS["text_light"], size=16, weight="normal"))
        
        return title

    # --- 2. Concept: Sum of Angles ---
    elif mode == 'concept_sum_angles':
        title = "Suma de Ángulos (360°)"
        
        A = (cx - 150, cy - 60)
        B = (cx + 120, cy - 80)
        C = (cx + 80, cy + 100)
        D = (cx - 100, cy + 120)
        
        # Diagonal BD divides into 2 triangles
        # Triangle ABD
        parts.append(draw_triangle([A, B, D], stroke=COLORS["primary"], fill=COLORS["primary"], fill_opacity=0.05))
        # Triangle BCD
        parts.append(draw_triangle([B, C, D], stroke=COLORS["secondary"], fill=COLORS["secondary"], fill_opacity=0.05))
        
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        
        # Labels
        centroid_abd = ((A[0]+B[0]+D[0])/3, (A[1]+B[1]+D[1])/3)
        centroid_bcd = ((B[0]+C[0]+D[0])/3, (B[1]+C[1]+D[1])/3)
        
        parts.append(draw_label(centroid_abd[0], centroid_abd[1], "180°", COLORS["primary"], weight="bold"))
        parts.append(draw_label(centroid_bcd[0], centroid_bcd[1], "180°", COLORS["secondary"], weight="bold"))
        
        # Sum text
        parts.append(f'<rect x="{cx-80}" y="{height-60}" width="160" height="40" rx="4" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, height-40, "Total = 360°", COLORS["text"], size=20, weight="bold"))

        return title

    # --- 3. Classification: Convex ---
    elif mode == 'type_convex':
        title = "Cuadrilátero Convexo"
        
        A = (cx - 120, cy - 80)
        B = (cx + 120, cy - 60)
        C = (cx + 80, cy + 80)
        D = (cx - 100, cy + 100)
        
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS["success"], fill_color=COLORS["success"])
        
        # Diagonals BOTH inside
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        
        parts.append(draw_label(cx, height-40, "Diagonales Internas", COLORS["success"], weight="bold"))

        return title

    # --- 4. Classification: Concave ---
    elif mode == 'type_concave':
        title = "Cuadrilátero Cóncavo"
        
        # Boomerang shape
        A = (cx - 140, cy - 50)
        B = (cx + 140, cy - 50)
        C = (cx, cy + 150) # Bottom tip
        D = (cx, cy + 20)  # Re-entrant vertex
        
        # Vertices order around perimeter: A -> D -> B -> C -> A
        points = [A, D, B, C]
        draw_quad(parts, points, stroke_color=COLORS["danger"], fill_color=COLORS["danger"])
        
        # Diagonal AB (External)
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        parts.append(draw_label((A[0]+B[0])/2, A[1]-15, "Diagonal Externa", COLORS["text"], size=14))
        
        # Reflex Angle at D
        radius = 25
        angA = math.atan2(A[1]-D[1], A[0]-D[0])
        angB = math.atan2(B[1]-D[1], B[0]-D[0])
        
        sx = D[0] + radius * math.cos(angA)
        sy = D[1] + radius * math.sin(angA)
        ex = D[0] + radius * math.cos(angB)
        ey = D[1] + radius * math.sin(angB)
        
        # SWEEP 0 for reflex (CCW from A to B via bottom)
        parts.append(f'<path d="M {sx:.2f} {sy:.2f} A {radius} {radius} 0 1 0 {ex:.2f} {ey:.2f}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        parts.append(draw_label(D[0], D[1]+45, "&gt; 180°", COLORS["danger"], weight="bold"))

        return title

    # --- 5. Example 1: Find Angle ---
    elif mode == 'example_find_angle':
        title = "Hallar Ángulo Desconocido"
        
        # Need sum 360. A=100, B=80, C=70, D=110.
        # Construct roughly accurate shape
        # A at top-left
        A = (cx - 100, cy - 100)
        # D is 110 deg from A?
        # Let's just place points to look approximate
        B = (cx + 100, cy - 80)
        C = (cx + 120, cy + 80)
        D = (cx - 80, cy + 100)
        
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS["text"])
        
        parts.append(draw_angle_arc(D, A, B, radius=25, color=COLORS["secondary"]))
        parts.append(draw_label(A[0]+15, A[1]+25, "100°", COLORS["text"]))
        
        parts.append(draw_angle_arc(A, B, C, radius=25, color=COLORS["secondary"]))
        parts.append(draw_label(B[0]-15, B[1]+25, "80°", COLORS["text"]))
        
        parts.append(draw_angle_arc(B, C, D, radius=25, color=COLORS["secondary"]))
        parts.append(draw_label(C[0]-25, C[1]-15, "70°", COLORS["text"]))
        
        parts.append(draw_label(D[0]+20, D[1]-20, "D=?", COLORS["danger"], size=24, weight="bold"))

        return title

    # --- 6. Example 2: Concave Check ---
    elif mode == 'example_concave_check':
        title = "¿Convexo o Cóncavo?"
        
        # 40, 30, 50, 240
        # Re-entrant shape
        A = (cx - 100, cy - 80)
        B = (cx, cy) # Re-entrant 240 deg
        C = (cx + 100, cy - 80)
        D = (cx, cy + 100)
        # Order A->B->C->D
        
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS["text"], fill_color="none")
        
        # Explain Reflex B
        radius = 25
        # Adjacent vertices to B are A and C
        angA = math.atan2(A[1]-B[1], A[0]-B[0]) #( -80, -100 )
        angC = math.atan2(C[1]-B[1], C[0]-B[0]) #( -80, 100 )
        
        sx = B[0] + radius * math.cos(angA)
        sy = B[1] + radius * math.sin(angA)
        ex = B[0] + radius * math.cos(angC)
        ey = B[1] + radius * math.sin(angC)
        
        # Sweep 0 (CCW) covers the bottom (reflex) side.
        parts.append(f'<path d="M {sx:.2f} {sy:.2f} A {radius} {radius} 0 1 0 {ex:.2f} {ey:.2f}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        parts.append(draw_label(B[0], B[1]+40, "240°", COLORS["danger"], weight="bold"))
        
        # Other angles quiet
        parts.append(draw_label(A[0], A[1]-20, "40°", COLORS["text_light"]))
        parts.append(draw_label(C[0], C[1]-20, "50°", COLORS["text_light"]))
        parts.append(draw_label(D[0], D[1]+20, "30°", COLORS["text_light"]))

        return title

    # --- 7. Summary ---
    elif mode == 'summary_types':
        scene_title = ""
        
        # Side by side comparison
        w_panel = width / 2
        
        # Left: Convex
        cx1 = w_panel / 2
        cy1 = height / 2
        parts.append(draw_label(cx1, 40, "CONVEXO", COLORS["success"], weight="bold"))
        
        A1 = (cx1 - 60, cy1 - 40)
        B1 = (cx1 + 60, cy1 - 40)
        C1 = (cx1 + 60, cy1 + 40)
        D1 = (cx1 - 60, cy1 + 40)
        draw_quad(parts, [A1, B1, C1, D1], stroke_color=COLORS["success"])
        # Diagonals
        parts.append(f'<line x1="{A1[0]}" y1="{A1[1]}" x2="{C1[0]}" y2="{C1[1]}" stroke="{COLORS["text_light"]}" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{B1[0]}" y1="{B1[1]}" x2="{D1[0]}" y2="{D1[1]}" stroke="{COLORS["text_light"]}" stroke-dasharray="2,2"/>')
        parts.append(draw_label(cx1, cy1 + 70, "Ángulos &lt; 180°", COLORS["text"], size=14))
        parts.append(draw_label(cx1, cy1 + 90, "Diagonales dentro", COLORS["text"], size=14))

        # Right: Concave
        cx2 = width - w_panel / 2
        cy2 = height / 2
        parts.append(draw_label(cx2, 40, "CÓNCAVO", COLORS["danger"], weight="bold"))
        
        A2 = (cx2 - 60, cy2 - 40)
        B2 = (cx2, cy2 ) # Inner
        C2 = (cx2 + 60, cy2 - 40)
        D2 = (cx2, cy2 + 60)
        draw_quad(parts, [A2, B2, C2, D2], stroke_color=COLORS["danger"])
        
        # Visuals: External Diagonal
        parts.append(f'<line x1="{A2[0]}" y1="{A2[1]}" x2="{C2[0]}" y2="{C2[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="2,2"/>')
        
        # Visuals: Reflex Angle at B2
        radius = 20
        # A2 is (-60, -40) relative to B2. Angle = atan2(-40, -60) = -146 deg
        # C2 is (60, -40) relative to B2. Angle = atan2(-40, 60) = -33 deg
        # We want arc from C2 side to A2 side via bottom (reflex)
        # Or A2 to C2 via bottom? 
        # A2(-146) -> C2(-33). Direct is small. 
        # A2 -> C2 large arc (sweep 1? no y is down). 
        # Let's calculate precise angles.
        angA = math.atan2(A2[1]-B2[1], A2[0]-B2[0])
        angC = math.atan2(C2[1]-B2[1], C2[0]-B2[0])
        
        sx = B2[0] + radius * math.cos(angA)
        sy = B2[1] + radius * math.sin(angA)
        ex = B2[0] + radius * math.cos(angC)
        ey = B2[1] + radius * math.sin(angC)
        
        # CCW (Sweep 0) covers the bottom reflex part
        parts.append(f'<path d="M {sx:.2f} {sy:.2f} A {radius} {radius} 0 1 0 {ex:.2f} {ey:.2f}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        parts.append(draw_label(cx2, cy2 + 70, "Un ángulo &gt; 180°", COLORS["text"], size=14))
        parts.append(draw_label(cx2, cy2 + 90, "Diagonal fuera", COLORS["text"], size=14))
        
        # Divider
        parts.append(f'<line x1="{width/2}" y1="60" x2="{width/2}" y2="{height-40}" stroke="{COLORS["grid"]}" stroke-dasharray="4"/>')

        return scene_title

    return "Quadrilateral Scene"

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    
    parts = []
    # Background
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    
    title = draw_quadrilateral_scene(parts, width, height, mode)
    
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

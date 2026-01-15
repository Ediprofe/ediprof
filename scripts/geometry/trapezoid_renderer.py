
import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.triangle_primitives import draw_triangle, draw_label, draw_angle_arc, draw_tick_marks

# --- Configuration ---
CANVAS_NAME = 'compound' # 600x460
FONT_SIZE_LABEL = 20
FONT_SIZE_TITLE = 22

def draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color='none', stroke_width=3, fill_opacity=0.1):
    path_d = f"M {points[0][0]:.2f} {points[0][1]:.2f} "
    for i in range(1, len(points)):
        path_d += f"L {points[i][0]:.2f} {points[i][1]:.2f} "
    path_d += "Z"
    parts.append(f'<path d="{path_d}" fill="{fill_color}" fill-opacity="{fill_opacity}" stroke="{stroke_color}" stroke-width="{stroke_width}" stroke-linejoin="round"/>')

def draw_right_angle(parts, p, v1, v2, size=15, color=COLORS['danger']):
    a1 = math.atan2(v1[1]-p[1], v1[0]-p[0])
    a2 = math.atan2(v2[1]-p[1], v2[0]-p[0])
    p1 = (p[0] + size * math.cos(a1), p[1] + size * math.sin(a1))
    p2 = (p[0] + size * math.cos(a2), p[1] + size * math.sin(a2))
    p12 = (p1[0] + size * math.cos(a2), p1[1] + size * math.sin(a2))
    parts.append(f'<path d="M {p1[0]:.2f} {p1[1]:.2f} L {p12[0]:.2f} {p12[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f}" fill="none" stroke="{color}" stroke-width="2"/>')

def draw_dimension(parts, p1, p2, offset_val, label, color=COLORS['text'], horizontal=True, label_offset=None):
    """Draw a dimension line with label outside the figure."""
    if horizontal:
        y = p1[1] + offset_val
        parts.append(f'<line x1="{p1[0]}" y1="{y}" x2="{p2[0]}" y2="{y}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{p1[0]}" y1="{y-5}" x2="{p1[0]}" y2="{y+5}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{p2[0]}" y1="{y-5}" x2="{p2[0]}" y2="{y+5}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p1[0]}" y2="{y}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{p2[0]}" y1="{p2[1]}" x2="{p2[0]}" y2="{y}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        lbl_off = label_offset if label_offset else 20
        parts.append(draw_label((p1[0]+p2[0])/2, y + lbl_off, label, color, size=14, weight='bold'))
    else:
        x = p1[0] + offset_val
        parts.append(f'<line x1="{x}" y1="{p1[1]}" x2="{x}" y2="{p2[1]}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{x-5}" y1="{p1[1]}" x2="{x+5}" y2="{p1[1]}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{x-5}" y1="{p2[1]}" x2="{x+5}" y2="{p2[1]}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{x}" y2="{p1[1]}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{p2[0]}" y1="{p2[1]}" x2="{x}" y2="{p2[1]}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        lbl_off = label_offset if label_offset else 20
        mid_y = (p1[1] + p2[1]) / 2
        parts.append(f'<text x="{x + lbl_off}" y="{mid_y}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{color}" text-anchor="middle" dominant-baseline="middle" transform="rotate(-90 {x + lbl_off} {mid_y})">{label}</text>')

def draw_trapezoid_base_scenes(parts, width, height, mode):
    cx, cy = width / 2, height / 2

    if mode == 'anatomia':
        title = "Anatomía del Trapecio"
        B, b, h = 300, 160, 150
        offset_top = (B - b) / 2 + 30 # slight shift for generic look
        
        pA = (cx - B/2, cy + h/2)
        pB = (cx + B/2, cy + h/2)
        pC = (cx + B/2 - (B-b-offset_top), cy - h/2)
        pD = (cx - B/2 + offset_top, cy - h/2)
        points = [pA, pB, pC, pD]

        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        # Height line
        parts.append(f'<line x1="{pD[0]}" y1="{pD[1]}" x2="{pD[0]}" y2="{pA[1]}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        draw_right_angle(parts, (pD[0], pA[1]), pD, pA)
        
        # Labels using draw_dimension
        draw_dimension(parts, pA, pB, 40, "Base Mayor (B)", horizontal=True)
        draw_dimension(parts, pD, pC, -40, "Base Menor (b)", horizontal=True)
        
        parts.append(draw_label(pD[0] - 15, (pD[1]+pA[1])/2, "h", COLORS['danger'], weight='bold'))
        parts.append(draw_label((pA[0]+pD[0])/2 - 50, (pA[1]+pD[1])/2, "Lado Lateral", COLORS['text_light'], size=14))
        
        return title

    elif mode == 'tipos':
        # Panel comparison
        title = "Tipos de Trapecios"
        w_panel = width / 3
        h = 100
        y_pos = cy + 20
        
        # 1. Isosceles
        c1 = w_panel / 2
        B1, b1 = 120, 60
        pts1 = [(c1-B1/2, y_pos+h/2), (c1+B1/2, y_pos+h/2), (c1+b1/2, y_pos-h/2), (c1-b1/2, y_pos-h/2)]
        draw_quad(parts, pts1, stroke_color=COLORS['success'])
        parts.append(draw_label(c1, y_pos - h/2 - 30, "ISÓSCELES", COLORS['success'], size=16, weight='bold'))
        parts.append(draw_tick_marks(pts1[0], pts1[3], count=1, color=COLORS['success']))
        parts.append(draw_tick_marks(pts1[1], pts1[2], count=1, color=COLORS['success']))

        # 2. Rectangle
        c2 = width / 2
        B2, b2 = 120, 70
        pts2 = [(c2-B2/2, y_pos+h/2), (c2+B2/2, y_pos+h/2), (c2+B2/2-(B2-b2), y_pos-h/2), (c2-B2/2, y_pos-h/2)]
        draw_quad(parts, pts2, stroke_color=COLORS['primary'])
        parts.append(draw_label(c2, y_pos - h/2 - 30, "RECTÁNGULO", COLORS['primary'], size=16, weight='bold'))
        draw_right_angle(parts, pts2[0], pts2[1], pts2[3], size=12)
        draw_right_angle(parts, pts2[3], pts2[0], pts2[2], size=12)

        # 3. Scalene
        c3 = width - w_panel / 2
        B3, b3 = 120, 50
        pts3 = [(c3-B3/2, y_pos+h/2), (c3+B3/2, y_pos+h/2), (c3+B3/2-10, y_pos-h/2), (c3-B3/2+40, y_pos-h/2)]
        draw_quad(parts, pts3, stroke_color=COLORS['highlight'])
        parts.append(draw_label(c3, y_pos - h/2 - 30, "ESCALENO", COLORS['highlight'], size=16, weight='bold'))

        return title

    elif mode == 'base_media':
        title = "Base Media o Mediana"
        B, b, h = 320, 140, 160
        pA = (cx - B/2, cy + h/2)
        pB = (cx + B/2, cy + h/2)
        pC = (cx + b/2 + 40, cy - h/2)
        pD = (cx - b/2 + 40, cy - h/2)
        
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        # Midpoints
        M1 = ((pA[0]+pD[0])/2, (pA[1]+pD[1])/2)
        M2 = ((pB[0]+pC[0])/2, (pB[1]+pC[1])/2)
        
        # Circles at midpoints
        parts.append(f'<circle cx="{M1[0]}" cy="{M1[1]}" r="4" fill="{COLORS["secondary"]}"/>')
        parts.append(f'<circle cx="{M2[0]}" cy="{M2[1]}" r="4" fill="{COLORS["secondary"]}"/>')
        
        parts.append(f'<line x1="{M1[0]}" y1="{M1[1]}" x2="{M2[0]}" y2="{M2[1]}" stroke="{COLORS["secondary"]}" stroke-width="4"/>')
        
        # Labels for points
        parts.append(draw_label(M1[0]-15, M1[1]-15, "M", COLORS['secondary'], weight='bold'))
        parts.append(draw_label(M2[0]+15, M2[1]-15, "N", COLORS['secondary'], weight='bold'))
        
        # Context labels
        parts.append(draw_label(cx + 40, (M1[1]+M2[1])/2 - 15, "Base Media (m)", COLORS['secondary'], weight='bold'))
        
        # Dimensions
        draw_dimension(parts, pA, pB, 40, "B", horizontal=True)
        draw_dimension(parts, pD, pC, -40, "b", horizontal=True)
        
        # Tick marks to show midpoints (more visible)
        parts.append(draw_tick_marks(pA, M1, count=1, color=COLORS['secondary']))
        parts.append(draw_tick_marks(M1, pD, count=1, color=COLORS['secondary']))
        parts.append(draw_tick_marks(pB, M2, count=2, color=COLORS['secondary']))
        parts.append(draw_tick_marks(M2, pC, count=2, color=COLORS['secondary']))
        
        # Formula box
        parts.append(f'<rect x="{cx-70}" y="{cy+110}" width="140" height="50" rx="8" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, cy+135, "m = (B + b) / 2", COLORS['text'], size=18, weight='bold'))

        return title

    elif mode == 'ejemplo_area':
        title = "Ejemplo: Cálculo de Área"
        # B=10, b=6, h=4 -> Scale up x30
        s = 30
        B_val, b_val, h_val = 10*s, 6*s, 4*s
        pA = (cx - B_val/2, cy + h_val/2)
        pB = (cx + B_val/2, cy + h_val/2)
        pC = (cx + b_val/2, cy - h_val/2)
        pD = (cx - b_val/2, cy - h_val/2)
        
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'], fill_color=COLORS['primary'], fill_opacity=0.05)
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        # Dimensions
        draw_dimension(parts, pA, pB, 40, "B = 10", horizontal=True)
        draw_dimension(parts, pD, pC, -40, "b = 6", horizontal=True)
        
        # Height
        h_x = pD[0]
        parts.append(f'<line x1="{h_x}" y1="{pD[1]}" x2="{h_x}" y2="{pA[1]}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        parts.append(draw_label(h_x - 30, (pD[1]+pA[1])/2, "h = 4", COLORS['danger'], weight='bold'))
        
        # Calculation text
        parts.append(draw_label(cx, pA[1] + 90, "Área = [(10 + 6) / 2] × 4 = 32", COLORS['success'], size=20, weight='bold'))

        return title

    elif mode == 'ejercicio_isosceles_pitagoras':
        title = "Ejercicio: Perímetro y Pitágoras"
        # B=10, b=4, h=4 -> Scale x40
        s = 40
        B_v, b_v, h_v = 10*s, 4*s, 4*s
        A = (cx - B_v/2, cy + h_v/2)
        B_pt = (cx + B_v/2, cy + h_v/2)
        C = (cx + b_v/2, cy - h_v/2)
        D = (cx - b_v/2, cy - h_v/2)
        
        draw_quad(parts, [A, B_pt, C, D], stroke_color=COLORS['text'])
        
        # Show breakdown
        H1 = (D[0], A[1])
        H2 = (C[0], A[1])
        parts.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="{H1[0]}" y2="{H1[1]}" stroke="{COLORS["danger"]}" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{H2[0]}" y2="{H2[1]}" stroke="{COLORS["danger"]}" stroke-dasharray="2,2"/>')
        
        # Highlight right triangle
        parts.append(draw_triangle([A, H1, D], fill=COLORS['fill_orange_light'], fill_opacity=0.4, stroke=COLORS['highlight']))
        
        # Labels
        parts.append(draw_label(cx, D[1] - 20, "b = 4", COLORS['text']))
        parts.append(draw_label(cx, A[1] + 25, "B = 10", COLORS['text']))
        
        # Parts of B
        parts.append(draw_label((A[0]+H1[0])/2, A[1] + 15, "3", COLORS['highlight'], size=14, weight='bold'))
        parts.append(draw_label(cx, A[1] + 15, "4", COLORS['text'], size=14))
        parts.append(draw_label((H2[0]+B_pt[0])/2, A[1] + 15, "3", COLORS['highlight'], size=14, weight='bold'))
        
        # Height and Hypotenuse
        parts.append(draw_label(D[0] - 15, (D[1]+H1[1])/2, "4", COLORS['danger'], weight='bold'))
        parts.append(draw_label((A[0]+D[0])/2 - 20, (A[1]+D[1])/2, "L = 5", COLORS['success'], weight='bold'))
        
        parts.append(draw_label(cx, cy + h_v/2 + 60, "√(3² + 4²) = 5", COLORS['success'], size=18, weight='bold'))

        return title

    elif mode == 'tipo_isosceles':
        title = "Trapecio Isósceles"
        B, b, h = 280, 140, 140
        pts = [(cx-B/2, cy+h/2), (cx+B/2, cy+h/2), (cx+b/2, cy-h/2), (cx-b/2, cy-h/2)]
        draw_quad(parts, pts, stroke_color=COLORS['success'], fill_color=COLORS['success'], fill_opacity=0.05)
        
        # Vertex Labels
        parts.append(draw_label(pts[0][0]-20, pts[0][1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[1][0]+20, pts[1][1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[2][0]+20, pts[2][1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[3][0]-20, pts[3][1]-20, "D", COLORS['vertices'], weight='bold'))

        # Proper symmetry marks
        parts.append(draw_tick_marks(pts[0], pts[3], count=1, color=COLORS['success']))
        parts.append(draw_tick_marks(pts[1], pts[2], count=1, color=COLORS['success']))
        
        # Base angles
        parts.append(draw_angle_arc(pts[0], pts[1], pts[3], radius=30, color=COLORS['success']))
        parts.append(draw_angle_arc(pts[1], pts[0], pts[2], radius=30, color=COLORS['success']))
        
        parts.append(draw_label(cx, cy + h/2 + 70, "Lados laterales y ángulos basales iguales", COLORS['text_light'], size=16))
        return title

    elif mode == 'tipo_rectangulo':
        title = "Trapecio Rectángulo"
        B, b, h = 280, 160, 140
        pts = [(cx-B/2, cy+h/2), (cx+B/2, cy+h/2), (cx+B/2-(B-b), cy-h/2), (cx-B/2, cy-h/2)]
        draw_quad(parts, pts, stroke_color=COLORS['primary'], fill_color=COLORS['primary'], fill_opacity=0.05)
        
        # Vertex Labels
        parts.append(draw_label(pts[0][0]-20, pts[0][1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[1][0]+20, pts[1][1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[2][0]+20, pts[2][1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[3][0]-20, pts[3][1]-20, "D", COLORS['vertices'], weight='bold'))

        # Right angles
        draw_right_angle(parts, pts[0], pts[1], pts[3])
        draw_right_angle(parts, pts[3], pts[0], pts[2])
        
        parts.append(draw_label(cx, cy + h/2 + 70, "Dos ángulos rectos (90°)", COLORS['text_light'], size=16))
        return title

    elif mode == 'tipo_escaleno':
        title = "Trapecio Escaleno"
        B, b, h = 280, 150, 140
        pts = [(cx-120, cy+h/2), (cx+160, cy+h/2), (cx+110, cy-h/2), (cx-50, cy-h/2)]
        draw_quad(parts, pts, stroke_color=COLORS['highlight'], fill_color=COLORS['highlight'], fill_opacity=0.05)
        
        # Vertex Labels
        parts.append(draw_label(pts[0][0]-20, pts[0][1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[1][0]+20, pts[1][1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[2][0]+20, pts[2][1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pts[3][0]-20, pts[3][1]-20, "D", COLORS['vertices'], weight='bold'))

        parts.append(draw_label(cx, cy + h/2 + 70, "Lados y ángulos todos diferentes", COLORS['text_light'], size=16))
        return title

        parts.append(draw_label(cx, cy + h/2 + 50, "x + 50° = 180°", COLORS['text_light'], weight='bold'))
        
        return title

    elif mode == 'ejemplo_angulos_rectangulo':
        title = "Ejemplo: Ángulos en Trapecio Rectángulo"
        B, b, h = 280, 150, 160
        pA = (cx - B/2, cy + h/2)
        pB = (cx + B/2, cy + h/2)
        pC = (cx + B/2 - (B-b), cy - h/2)
        pD = (cx - B/2, cy - h/2)
        pts = [pA, pB, pC, pD]
        
        draw_quad(parts, pts, stroke_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        # Right angles at A and D
        draw_right_angle(parts, pA, pB, pD)
        draw_right_angle(parts, pD, pA, pC)
        
        # Acute angle at B (50 deg)
        parts.append(draw_angle_arc(pB, pA, pC, radius=40, color=COLORS['angle']))
        parts.append(draw_label(pB[0]-60, pB[1]-20, "50°", COLORS['text']))
        
        # Obtuse angle at C (x)
        parts.append(draw_angle_arc(pC, pB, pD, radius=40, color=COLORS['accent'], marks=1))
        parts.append(draw_label(pC[0]-35, pC[1]+35, "x = ?", COLORS['accent'], size=20, weight='bold'))
        
        parts.append(draw_label(cx, cy + h/2 + 70, "x + 50° = 180°", COLORS['text_light'], weight='bold'))
        
        return title

    elif mode == 'ejemplo_escaleno_identificacion':
        title = "Ejemplo: Trapecio Escaleno"
        pA = (cx - 100, cy + 75)
        pB = (cx + 250, cy + 75)
        pC = (cx + 40, cy - 75)
        pD = (cx - 60, cy - 75)
        pts = [pA, pB, pC, pD]
        
        draw_quad(parts, pts, stroke_color=COLORS['highlight'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        # Labels for sides using rotation for slanted sides
        mid_L1 = ((pA[0]+pD[0])/2, (pA[1]+pD[1])/2)
        parts.append(draw_label(mid_L1[0]-40, mid_L1[1], "L₁ = 5", COLORS['text']))
        
        mid_L2 = ((pB[0]+pC[0])/2, (pB[1]+pC[1])/2)
        parts.append(draw_label(mid_L2[0]+40, mid_L2[1], "L₂ = 8", COLORS['text']))
        
        # Base labels (centered between A and B)
        label_cx = (pA[0] + pB[0]) / 2
        draw_dimension(parts, pA, pB, 40, "Base Mayor", horizontal=True)
        
        # Different angles
        parts.append(draw_angle_arc(pA, pB, pD, radius=30, color=COLORS['angle']))
        parts.append(draw_angle_arc(pB, pA, pC, radius=40, color=COLORS['accent'], marks=1))
        
        # Conclusion text centered under figure
        parts.append(draw_label(label_cx, pA[1] + 90, "L₁ ≠ L₂ ⟹ Ángulos Basales Diferentes", COLORS['highlight'], weight='bold', size=16))
        
        return title

    elif mode == 'ejemplo_perimetro_isosceles_calculo':
        title = "Ejemplo 2: Perímetro de Trapecio Isósceles"
        s = 15 # scale
        B_val, b_val, h_val = 20, 10, 12
        pA = (cx - (B_val*s)/2, cy + (h_val*s)/2)
        pB = (cx - (b_val*s)/2, cy - (h_val*s)/2)
        pC = (cx + (b_val*s)/2, cy - (h_val*s)/2)
        pD = (cx + (B_val*s)/2, cy + (h_val*s)/2)
        
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Internal triangles for Pythagoras
        pE = (pB[0], pA[1]) # Projection of B on base AD
        parts.append(draw_triangle([pA, pB, pE], stroke=COLORS['secondary'], fill=COLORS['secondary'], fill_opacity=0.2))
        draw_right_angle(parts, pE, pA, pB)
        
        # Labels
        parts.append(draw_label(pA[0]-20, pA[1]+15, "A", COLORS['vertices']))
        parts.append(draw_label(pB[0], pB[1]-15, "B", COLORS['vertices']))
        parts.append(draw_label(pC[0], pC[1]-15, "C", COLORS['vertices']))
        parts.append(draw_label(pD[0]+20, pD[1]+15, "D", COLORS['vertices']))
        
        # Dimensions
        draw_dimension(parts, pA, pD, 35, "Base Mayor (B) = 20", horizontal=True)
        draw_dimension(parts, pB, pC, -35, "Base Menor (b) = 10", horizontal=True)
        # Height on the triangle side
        draw_dimension(parts, pE, pB, -35, "h = 12", horizontal=False)
        
        # Calculated parts
        parts.append(draw_label((pA[0]+pE[0])/2, pA[1]+20, "base=5", COLORS['secondary'], weight='bold'))
        parts.append(draw_label((pA[0]+pB[0])/2 - 30, (pA[1]+pB[1])/2 - 10, "L=13", COLORS['danger'], weight='bold'))
        
        # Pythagorean annotation
        parts.append(draw_label(cx, cy + (h_val*s)/2 + 80, "L = √(12² + 5²) = 13", COLORS['danger'], size=18, weight='bold'))
        
        return title

    return "Trapezoid"

def draw_trapezoid_extra_scenes(parts, cx, cy, h, mode):
    if mode == 'trapecio_angulos_conjugados':
        title = "Ángulos Conjugados (Entre Paralelas)"
        B, b, h_v = 300, 150, 150
        pA = (cx - B/2, cy + h_v/2)
        pB = (cx + B/2, cy + h_v/2)
        pC = (cx + B/2 - 40, cy - h_v/2)
        pD = (cx - B/2 + 80, cy - h_v/2)
        pts = [pA, pB, pC, pD]
        draw_quad(parts, pts, stroke_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        parts.append(draw_angle_arc(pA, pB, pD, radius=35, color=COLORS['angle']))
        parts.append(draw_label(pA[0]+35, pA[1]-20, "α", COLORS['text'], size=18))
        parts.append(draw_angle_arc(pD, pC, pA, radius=35, color=COLORS['angle']))
        parts.append(draw_label(pD[0]+15, pD[1]+35, "δ", COLORS['text'], size=18))
        
        parts.append(f'<line x1="{pA[0]-40}" y1="{pA[1]}" x2="{pB[0]+40}" y2="{pB[1]}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
        parts.append(f'<line x1="{pD[0]-40}" y1="{pD[1]}" x2="{pC[0]+40}" y2="{pC[1]}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
        
        parts.append(draw_label(cx, pA[1] + 60, "α + δ = 180°", COLORS['text'], weight='bold', size=20))
        return title

    elif mode == 'trapecio_area_formula':
        title = "Fórmula del Área del Trapecio"
        B, b, h_v = 300, 160, 150
        pA = (cx - B/2, cy + h_v/2)
        pB = (cx + B/2, cy + h_v/2)
        pC = (cx + b/2, cy - h_v/2)
        pD = (cx - b/2, cy - h_v/2)
        
        # Draw quad with fill
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'], fill_color=COLORS['primary'], fill_opacity=0.1)
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        draw_dimension(parts, pA, pB, 40, "Base Mayor (B)", horizontal=True)
        draw_dimension(parts, pD, pC, -40, "Base Menor (b)", horizontal=True)

        parts.append(f'<line x1="{pD[0]}" y1="{pD[1]}" x2="{pD[0]}" y2="{pA[1]}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        parts.append(draw_label(pD[0] - 20, (pD[1]+pA[1])/2, "h", COLORS['danger'], weight='bold'))
        
        # Formula box moved OUTSIDE (bottom)
        box_y = pA[1] + 80
        parts.append(f'<rect x="{cx - 110}" y="{box_y}" width="220" height="50" rx="10" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, box_y + 25, "Área = [(B+b)/2] · h", COLORS['text'], weight='bold', size=18))
        return title

    elif mode == 'ejemplo_base_media':
        title = "Ejemplo: Cálculo de Base Media"
        B_val, b_val = 25, 15
        s = 10
        B, b, h_v = B_val*s, b_val*s, 140
        pA = (cx - B/2, cy + h_v/2)
        pB = (cx + B/2, cy + h_v/2)
        pC = (cx + b/2, cy - h_v/2)
        pD = (cx - b/2, cy - h_v/2)
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'])
        
        M1 = ((pA[0]+pD[0])/2, (pA[1]+pD[1])/2)
        M2 = ((pB[0]+pC[0])/2, (pB[1]+pC[1])/2)
        
        # Circles and line
        parts.append(f'<circle cx="{M1[0]}" cy="{M1[1]}" r="4" fill="{COLORS["secondary"]}"/>')
        parts.append(f'<circle cx="{M2[0]}" cy="{M2[1]}" r="4" fill="{COLORS["secondary"]}"/>')
        parts.append(f'<line x1="{M1[0]}" y1="{M1[1]}" x2="{M2[0]}" y2="{M2[1]}" stroke="{COLORS["secondary"]}" stroke-width="4"/>')
        
        # Tick marks
        parts.append(draw_tick_marks(pA, M1, count=1, color=COLORS['secondary']))
        parts.append(draw_tick_marks(M1, pD, count=1, color=COLORS['secondary']))
        parts.append(draw_tick_marks(pB, M2, count=2, color=COLORS['secondary']))
        parts.append(draw_tick_marks(M2, pC, count=2, color=COLORS['secondary']))
        
        parts.append(draw_label(cx, pA[1]+25, "B = 25", COLORS['text'], weight='bold'))
        parts.append(draw_label(cx, pD[1]-20, "b = 15", COLORS['text'], weight='bold'))
        parts.append(draw_label(cx, (M1[1]+M2[1])/2 - 15, "m = (25+15)/2 = 20", COLORS['secondary'], weight='bold'))
        return title

    elif mode == 'ejemplo_isosceles_angulos':
        title = "Ejemplo: Ángulos en Trapecio Isósceles"
        B, b, h_v = 280, 140, 140
        pA = (cx - B/2, cy + h_v/2)
        pB = (cx + B/2, cy + h_v/2)
        pC = (cx + b/2, cy - h_v/2)
        pD = (cx - b/2, cy - h_v/2)
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['success'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        parts.append(draw_angle_arc(pA, pB, pD, radius=35, color=COLORS['angle']))
        parts.append(draw_label(pA[0]+45, pA[1]-20, "75°", COLORS['text']))
        parts.append(draw_angle_arc(pB, pA, pC, radius=35, color=COLORS['accent']))
        parts.append(draw_label(pB[0]-45, pB[1]-20, "75°", COLORS['accent'], weight='bold'))
        return title

    elif mode == 'ejemplo_angulos_conjugados':
        title = "Ejemplo: Ángulos Conjugados"
        B, b, h_v = 280, 160, 140
        pA = (cx - B/2, cy + h_v/2)
        pB = (cx + B/2, cy + h_v/2)
        pC = (cx + 80, cy - h_v/2)
        pD = (cx - 60, cy - h_v/2)
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]+20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]-20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]-20, "D", COLORS['vertices'], weight='bold'))

        parts.append(draw_angle_arc(pA, pB, pD, radius=35, color=COLORS['angle']))
        parts.append(draw_label(pA[0]+45, pA[1]-20, "110°", COLORS['text']))
        parts.append(draw_angle_arc(pD, pC, pA, radius=35, color=COLORS['accent']))
        parts.append(draw_label(pD[0]+25, pD[1]+35, "x = 70°", COLORS['accent'], weight='bold'))
        return title
    return None

def draw_trapezoid_scene(parts, width, height, mode):
    cx, cy = width / 2, height / 2
    extra = draw_trapezoid_extra_scenes(parts, cx, cy, 150, mode)
    if extra: return extra
    return draw_trapezoid_base_scenes(parts, width, height, mode)

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    title = draw_trapezoid_scene(parts, width, height, mode)
    if title:
        parts.append(draw_label(width/2, 35, title, COLORS["vertices"], size=FONT_SIZE_TITLE, weight="bold"))
    parts.append('</svg>')
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

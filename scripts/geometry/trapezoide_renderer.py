
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
    # Unit vectors
    def unit(v_p, p_p):
        d = math.hypot(v_p[0]-p_p[0], v_p[1]-p_p[1])
        if d == 0: return (0,0)
        return ((v_p[0]-p_p[0])/d, (v_p[1]-p_p[1])/d)
    
    u1 = unit(v1, p)
    u2 = unit(v2, p)
    
    p1 = (p[0] + size * u1[0], p[1] + size * u1[1])
    p2 = (p[0] + size * u2[0], p[1] + size * u2[1])
    p12 = (p1[0] + size * u2[0], p1[1] + size * u2[1])
    
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

def draw_trapezoide_scene(parts, width, height, mode):
    cx, cy = width / 2, height / 2
    # Adjust vertical center for vertical-heavy modes
    if 'deltoide' in mode or 'cometa' in mode or 'triangulacion' in mode:
        cy -= 50

    if mode == 'definicion_irregular':
        title = "Trapezoide (Sin lados paralelos)"
        # Random looking points
        pA = (cx - 140, cy - 80)
        pB = (cx + 120, cy - 100)
        pC = (cx + 160, cy + 90)
        pD = (cx - 100, cy + 130)
        points = [pA, pB, pC, pD]
        
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-25, pA[1]-10, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+25, pB[1]-10, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+25, pC[1]+20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-25, pD[1]+20, "D", COLORS['vertices'], weight='bold'))
        
        parts.append(draw_label(cx, cy + 160, "Ningún par de lados paralelos", COLORS['text_light'], size=18))
        return title

    elif mode == 'deltoide_anatomia':
        title = "El Deltoide (Cometa)"
        h_top, h_bot, w = 80, 180, 120
        pA = (cx, cy - h_top)
        pB = (cx + w, cy)
        pC = (cx, cy + h_bot)
        pD = (cx - w, cy)
        points = [pA, pB, pC, pD]
        
        draw_quad(parts, points, stroke_color=COLORS['secondary'], fill_color=COLORS['secondary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0], pA[1]-30, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+30, pB[1], "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0], pC[1]+30, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-30, pD[1], "D", COLORS['vertices'], weight='bold'))

        # Diagonals
        parts.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        parts.append(f'<line x1="{pB[0]}" y1="{pB[1]}" x2="{pD[0]}" y2="{pD[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        
        # Right angle mark in center
        draw_right_angle(parts, (cx, cy), pB, pA)
        
        # Equality marks
        parts.append(draw_tick_marks(pA, pB, count=1, color=COLORS['secondary']))
        parts.append(draw_tick_marks(pA, pD, count=1, color=COLORS['secondary']))
        parts.append(draw_tick_marks(pB, pC, count=2, color=COLORS['secondary']))
        parts.append(draw_tick_marks(pD, pC, count=2, color=COLORS['secondary']))
        
        parts.append(draw_label(cx + 60, cy - 15, "d", COLORS['medianas'], weight='bold'))
        parts.append(draw_label(cx - 15, cy + 60, "D", COLORS['medianas'], weight='bold'))
        
        return title

    elif mode == 'deltoide_area_formula':
        title = "Fórmula del Área (Deltoide)"
        h_top, h_bot, w = 60, 140, 100
        pA = (cx, cy - h_top)
        pB = (cx + w, cy)
        pC = (cx, cy + h_bot)
        pD = (cx - w, cy)
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['secondary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0], pA[1]-25, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+25, pB[1], "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0], pC[1]+25, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-25, pD[1], "D", COLORS['vertices'], weight='bold'))

        # Diagonals
        parts.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="{COLORS["medianas"]}" stroke-width="3"/>')
        parts.append(f'<line x1="{pB[0]}" y1="{pB[1]}" x2="{pD[0]}" y2="{pD[1]}" stroke="{COLORS["medianas"]}" stroke-width="3"/>')
        
        # Center mark
        parts.append(f'<rect x="{cx}" y="{cy-15}" width="15" height="15" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        # Labels using dimensions
        draw_dimension(parts, pB, pD, h_bot + 20, "Diagonal Menor (d)", horizontal=True)
        draw_dimension(parts, pA, pC, w + 30, "Diagonal Mayor (D)", horizontal=False)

        # Formula box
        parts.append(f'<rect x="{cx-90}" y="{cy+h_bot+70}" width="180" height="50" rx="8" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, cy+h_bot+95, "Área = (D · d) / 2", COLORS['text'], size=18, weight='bold'))
        
        return title

    elif mode == 'metodo_triangulacion':
        title = "Área por Triangulación"
        pA = (cx - 150, cy - 60)
        pB = (cx + 100, cy - 90)
        pC = (cx + 140, cy + 80)
        pD = (cx - 120, cy + 110)
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]-10, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1]-10, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]+20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1]+20, "D", COLORS['vertices'], weight='bold'))

        # Division diagonal AC
        parts.append(draw_triangle([pA, pB, pC], fill=COLORS['fill_blue_light'], fill_opacity=0.3, stroke=COLORS['primary']))
        parts.append(draw_triangle([pA, pC, pD], fill=COLORS['fill_green_light'], fill_opacity=0.3, stroke=COLORS['secondary']))
        
        parts.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="{COLORS["text"]}" stroke-width="3" stroke-dasharray="6,3"/>')
        
        parts.append(draw_label((pA[0]+pB[0]+pC[0])/3, (pA[1]+pB[1]+pC[1])/3, "Área 1", COLORS['primary'], weight='bold'))
        parts.append(draw_label((pA[0]+pC[0]+pD[0])/3, (pA[1]+pC[1]+pD[1])/3, "Área 2", COLORS['secondary'], weight='bold'))
        
        parts.append(draw_label(cx, cy + 160, "Área Total = Área 1 + Área 2", COLORS['text'], size=20, weight='bold'))
        return title

    elif mode == 'ejemplo_cometa':
        title = "Ejemplo: Área de la Cometa"
        scale = 4
        h_top, h_bot, w = 15*scale, 45*scale, 20*scale
        
        pA = (cx, cy - h_top)
        pB = (cx + w, cy)
        pC = (cx, cy + h_bot)
        pD = (cx - w, cy)
        
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['secondary'], fill_color=COLORS['secondary'], fill_opacity=0.1)
        
        # Vertex Labels
        parts.append(draw_label(pA[0], pA[1]-20, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+20, pB[1], "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0], pC[1]+20, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-20, pD[1], "D", COLORS['vertices'], weight='bold'))

        # Diagonals
        parts.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        parts.append(f'<line x1="{pB[0]}" y1="{pB[1]}" x2="{pD[0]}" y2="{pD[1]}" stroke="{COLORS["text"]}" stroke-width="2" stroke-dasharray="4,4"/>')
        
        draw_dimension(parts, pB, pD, h_bot + 20, "d = 40", horizontal=True)
        draw_dimension(parts, pA, pC, w + 30, "D = 60", horizontal=False)

        parts.append(draw_label(cx, cy + h_bot + 90, "A = (60 × 40) / 2 = 1200", COLORS['success'], size=22, weight='bold'))
        return title

    elif mode == 'ejercicio_area_diagonal':
        title = "Ejercicio: Triangulación"
        s = 35
        diag_len = 10 * s
        h1, h2 = 3 * s, 4 * s
        
        pA = (cx - diag_len/2, cy)
        pC = (cx + diag_len/2, cy)
        pB = (cx - 1*s, cy - h1)
        pD = (cx + 2*s, cy + h2)
        
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-20, pA[1]+10, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0], pB[1]-20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+20, pC[1]+10, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0], pD[1]+20, "D", COLORS['vertices'], weight='bold'))

        # Diagonal AC
        parts.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="{COLORS["text"]}" stroke-width="3"/>')
        parts.append(draw_label(cx, cy + 20, "Diagonal = 10", COLORS['text'], weight='bold'))
        
        # Height 1 (to B)
        parts.append(f'<line x1="{pB[0]}" y1="{pB[1]}" x2="{pB[0]}" y2="{cy}" stroke="{COLORS["danger"]}" stroke-dasharray="3,3"/>')
        draw_right_angle(parts, (pB[0], cy), pB, pC, size=12)
        parts.append(draw_label(pB[0] - 30, (pB[1]+cy)/2, "h₁=3", COLORS['danger'], weight='bold'))
        
        # Height 2 (to D)
        parts.append(f'<line x1="{pD[0]}" y1="{pD[1]}" x2="{pD[0]}" y2="{cy}" stroke="{COLORS["danger"]}" stroke-dasharray="3,3"/>')
        draw_right_angle(parts, (pD[0], cy), pD, pA, size=12)
        parts.append(draw_label(pD[0] + 30, (pD[1]+cy)/2, "h₂=4", COLORS['danger'], weight='bold'))
        
        parts.append(draw_label(cx, cy + h2 + 60, "A = (10 × 3)/2 + (10 × 4)/2 = 35", COLORS['success'], size=20, weight='bold'))
        
        return title

    elif mode == 'ejemplo_triangulacion':
        title = "Ejemplo: Área por Triangulación"
        s = 30
        diag_len = 10 * s
        pA = (cx - diag_len/2, cy)
        pC = (cx + diag_len/2, cy)
        # heights 3 and 4
        pB = (cx - 0.5*s, cy - 3*s)
        pD = (cx + 1.5*s, cy + 4*s)
        
        # Draw background triangles
        parts.append(draw_triangle([pA, pB, pC], fill=COLORS['fill_blue_light'], fill_opacity=0.2, stroke=COLORS['primary']))
        parts.append(draw_triangle([pA, pC, pD], fill=COLORS['fill_green_light'], fill_opacity=0.2, stroke=COLORS['secondary']))
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-25, pA[1], "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0], pB[1]-20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+25, pC[1], "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0], pD[1]+20, "D", COLORS['vertices'], weight='bold'))

        # Diagonal AC (Base)
        parts.append(f'<line x1="{pA[0]}" y1="{pA[1]}" x2="{pC[0]}" y2="{pC[1]}" stroke="{COLORS["text"]}" stroke-width="3"/>')
        parts.append(draw_label(cx, cy + 20, "d = 10", COLORS['text'], weight='bold'))
        
        # Height 1 (to B)
        parts.append(f'<line x1="{pB[0]}" y1="{pB[1]}" x2="{pB[0]}" y2="{cy}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="3,3"/>')
        draw_right_angle(parts, (pB[0], cy), pB, pC, size=15)
        parts.append(draw_label(pB[0] - 25, (pB[1]+cy)/2, "h₁ = 3", COLORS['danger'], weight='bold'))
        
        # Height 2 (to D)
        parts.append(f'<line x1="{pD[0]}" y1="{pD[1]}" x2="{pD[0]}" y2="{cy}" stroke="{COLORS["danger"]}" stroke-width="2" stroke-dasharray="3,3"/>')
        draw_right_angle(parts, (pD[0], cy), pD, pA, size=15)
        parts.append(draw_label(pD[0] + 35, (pD[1]+cy)/2, "h₂ = 4", COLORS['danger'], weight='bold'))
        
        return title

    elif mode == 'ejemplo_angulos':
        title = "Ejemplo: Ángulos en el Trapezoide"
        pA = (cx - 100, cy - 80)
        pB = (cx + 100, cy - 80)
        pC = (cx + 140, cy + 100)
        pD = (cx - 110, cy + 100)
        
        draw_quad(parts, [pA, pB, pC, pD], stroke_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(pA[0]-25, pA[1]-10, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pB[0]+25, pB[1]-10, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pC[0]+25, pC[1]+10, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(pD[0]-25, pD[1]+10, "D", COLORS['vertices'], weight='bold'))

        # Angle arcs
        parts.append(draw_angle_arc(pA, pD, pB, radius=30, color=COLORS['angle']))
        parts.append(draw_label(pA[0]+25, pA[1]+30, "100°", COLORS['text']))
        
        parts.append(draw_angle_arc(pB, pA, pC, radius=30, color=COLORS['angle']))
        parts.append(draw_label(pB[0]-25, pB[1]+30, "80°", COLORS['text']))
        
        parts.append(draw_angle_arc(pC, pB, pD, radius=30, color=COLORS['angle']))
        parts.append(draw_label(pC[0]-35, pC[1]-20, "70°", COLORS['text']))
        
        # The unknown one
        parts.append(draw_angle_arc(pD, pC, pA, radius=35, color=COLORS['accent'], marks=1))
        parts.append(draw_label(pD[0]+35, pD[1]-25, "x = ?", COLORS['accent'], size=24, weight='bold'))
        
        parts.append(draw_label(cx, cy + 160, "Suma Total = 360°", COLORS['text_light'], weight='bold'))
        
        return title

    return "Trapezoide"

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    title = draw_trapezoide_scene(parts, width, height, mode)
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

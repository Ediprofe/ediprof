
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

def draw_right_angle(parts, p, v1, v2, size=15, color=COLORS['danger']):
    # p is vertex, v1/v2 are directions
    a1 = math.atan2(v1[1]-p[1], v1[0]-p[0])
    a2 = math.atan2(v2[1]-p[1], v2[0]-p[0])
    
    p1 = (p[0] + size * math.cos(a1), p[1] + size * math.sin(a1))
    p2 = (p[0] + size * math.cos(a2), p[1] + size * math.sin(a2))
    p12 = (p1[0] + size * math.cos(a2), p1[1] + size * math.sin(a2))
    
    
    parts.append(f'<path d="M {p1[0]:.2f} {p1[1]:.2f} L {p12[0]:.2f} {p12[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f}" fill="none" stroke="{color}" stroke-width="2"/>')

def draw_dimension(parts, p1, p2, offset_val, label, color=COLORS['text'], horizontal=True, label_offset=None):
    """Draw a dimension line with label outside the figure.
    
    For vertical dimensions, the label is rotated 90° for better readability
    and to avoid edge overflow issues.
    """
    if horizontal:
        y = p1[1] + offset_val
        # Main line
        parts.append(f'<line x1="{p1[0]}" y1="{y}" x2="{p2[0]}" y2="{y}" stroke="{color}" stroke-width="1.5"/>')
        # Ticks
        parts.append(f'<line x1="{p1[0]}" y1="{y-5}" x2="{p1[0]}" y2="{y+5}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{p2[0]}" y1="{y-5}" x2="{p2[0]}" y2="{y+5}" stroke="{color}" stroke-width="1.5"/>')
        # Extension lines (dashed)
        parts.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p1[0]}" y2="{y}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{p2[0]}" y1="{p2[1]}" x2="{p2[0]}" y2="{y}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        # Label (below dimension line, horizontal)
        lbl_off = label_offset if label_offset else 20
        parts.append(draw_label((p1[0]+p2[0])/2, y + lbl_off, label, color, size=14, weight='bold'))
    else:
        x = p1[0] + offset_val
        # Main line
        parts.append(f'<line x1="{x}" y1="{p1[1]}" x2="{x}" y2="{p2[1]}" stroke="{color}" stroke-width="1.5"/>')
        # Ticks
        parts.append(f'<line x1="{x-5}" y1="{p1[1]}" x2="{x+5}" y2="{p1[1]}" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<line x1="{x-5}" y1="{p2[1]}" x2="{x+5}" y2="{p2[1]}" stroke="{color}" stroke-width="1.5"/>')
        # Extension lines (dashed)
        parts.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{x}" y2="{p1[1]}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{p2[0]}" y1="{p2[1]}" x2="{x}" y2="{p2[1]}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="2,2"/>')
        # Label (ROTATED 90° for vertical alignment)
        lbl_off = label_offset if label_offset else 20
        mid_y = (p1[1] + p2[1]) / 2
        parts.append(f'<text x="{x + lbl_off}" y="{mid_y}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{color}" text-anchor="middle" dominant-baseline="middle" transform="rotate(-90 {x + lbl_off} {mid_y})">{label}</text>')

def draw_special_quad_scene(parts, width, height, mode):
    cx, cy = width / 2, height / 2

    if mode == 'rectangulo_propiedades':
        title = "Propiedades del Rectángulo"
        w, h = 300, 180
        # Vertices (counter-clockwise from Bottom-Left)
        A = (cx - w/2, cy + h/2)
        B = (cx + w/2, cy + h/2)
        C = (cx + w/2, cy - h/2)
        D = (cx - w/2, cy - h/2)
        points = [A, B, C, D]
        
        draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Vertex Labels
        parts.append(draw_label(A[0]-25, A[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0]+25, B[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+25, C[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0]-25, D[1]-15, "D", COLORS['vertices'], weight='bold'))
        
        # 4 Right angles
        draw_right_angle(parts, A, B, D)
        draw_right_angle(parts, B, C, A)
        draw_right_angle(parts, C, D, B)
        draw_right_angle(parts, D, A, C)
        
        # Diagonals
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        
        # Equal diagonal segments AM = MB = MC = MD
        mid = (cx, cy)
        def draw_tick(p1, p2):
            mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
            ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0]) + math.pi/2
            s = 8
            parts.append(f'<line x1="{mx + s*math.cos(ang):.2f}" y1="{my + s*math.sin(ang):.2f}" x2="{mx - s*math.cos(ang):.2f}" y2="{my - s*math.sin(ang):.2f}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
            
        draw_tick(A, mid)
        draw_tick(mid, C)
        draw_tick(B, mid)
        draw_tick(mid, D)
        
        # Footer Label
        parts.append(draw_label(cx, cy + h/2 + 60, "Diagonales Iguales: AC = BD", COLORS['text'], size=20, weight='bold'))
        return title

    elif mode == 'rectangulo_diagonal_formula':
        title = "Fórmula de la Diagonal (Rectángulo)"
        w, h = 300, 180
        A = (cx - w/2, cy + h/2)
        B = (cx + w/2, cy + h/2)
        C = (cx + w/2, cy - h/2)
        D = (cx - w/2, cy - h/2)
        
        draw_quad(parts, [D, C, B, A], stroke_color=COLORS['primary'])
        draw_right_angle(parts, A, B, D)
        
        # Diagonal
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        
        # Vertex Labels
        parts.append(draw_label(A[0]-25, A[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0]+25, B[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+25, C[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0]-25, D[1]-15, "D", COLORS['vertices'], weight='bold'))
        # Labels
        parts.append(draw_label(cx, A[1] + 25, "base (b)", COLORS['text']))
        parts.append(draw_label(cx + w/2 + 45, cy, "altura (h)", COLORS['text']))
        parts.append(draw_label(cx - 20, cy - 10, "d = √(b² + h²)", COLORS['danger'], weight='bold'))
        
        return title

    elif mode == 'rombo_propiedades':
        title = "Propiedades del Rombo"
        dw, dh = 300, 180 # Diagonals
        # Vertices (Clockwise from Left)
        A = (cx - dw/2, cy)
        B = (cx, cy - dh/2) # Top
        C = (cx + dw/2, cy)
        D = (cx, cy + dh/2) # Bottom
        points = [A, B, C, D]
        
        draw_quad(parts, points, stroke_color=COLORS['secondary'], fill_color=COLORS['secondary'])
        
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1], "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0], B[1]-20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+20, C[1], "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0], D[1]+25, "D", COLORS['vertices'], weight='bold'))
        
        # Equal sides marks
        def draw_side_tick(p1, p2):
            mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
            ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0]) + math.pi/2
            s = 8
            parts.append(f'<line x1="{mx + s*math.cos(ang):.2f}" y1="{my + s*math.sin(ang):.2f}" x2="{mx - s*math.cos(ang):.2f}" y2="{my - s*math.sin(ang):.2f}" stroke="{COLORS["text"]}" stroke-width="2"/>')

        for i in range(4):
            draw_side_tick(points[i], points[(i+1)%4])
            
        # Diagonals
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        
        # Center right angle
        parts.append(f'<path d="M {cx} {cy-15} L {cx+15} {cy-15} L {cx+15} {cy}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        # Footer Label
        parts.append(draw_label(cx, cy + dh/2 + 50, "Lados Iguales (AB=BC=CD=DA) y Diagonales ⊥", COLORS['text'], size=18, weight='bold'))
        return title

    elif mode == 'rombo_area_formula':
        title = "Fórmula del Área del Rombo"
        dw, dh = 300, 180
        A = (cx - dw/2, cy)
        B = (cx, cy + dh/2)
        C = (cx + dw/2, cy)
        D = (cx, cy - dh/2)
        
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['secondary'])
        
        # Diagonals as dashed lines inside
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
        
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1], "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0], B[1]+20, "B", COLORS['vertices'], weight='bold')) # Bottom
        parts.append(draw_label(C[0]+20, C[1], "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0], D[1]-20, "D", COLORS['vertices'], weight='bold')) # Top

        # Right angle
        parts.append(f'<path d="M {cx} {cy-15} L {cx+15} {cy-15} L {cx+15} {cy}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        # Dimensions outside
        draw_dimension(parts, A, C, dh/2 + 30, "Diagonal Mayor (D)", horizontal=True)
        draw_dimension(parts, D, B, dw/2 + 30, "Diagonal Menor (d)", horizontal=False)
        
        # Formula box
        parts.append(f'<rect x="{cx-90}" y="{cy+dh/2+70}" width="180" height="50" rx="8" fill="{COLORS["formula_bg"]}" stroke="{COLORS["grid"]}"/>')
        parts.append(draw_label(cx, cy+dh/2+95, "Área = (D · d) / 2", COLORS['text'], size=18, weight='bold'))
        
        return title

    elif mode == 'cuadrado_perfeccion':
        title = "El Cuadrado: Perfección"
        s = 200
        # Vertices (Counter-clockwise from Bottom-Left)
        A = (cx - s/2, cy + s/2)
        B = (cx + s/2, cy + s/2)
        C = (cx + s/2, cy - s/2)
        D = (cx - s/2, cy - s/2)
        points = [A, B, C, D]
        
        draw_quad(parts, points, stroke_color=COLORS['success'], fill_color=COLORS['success'])
        
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0]+20, B[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+20, C[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0]-20, D[1]-15, "D", COLORS['vertices'], weight='bold'))

        # Right angles
        for p, v1, v2 in [(A, B, D), (B, C, A), (C, D, B), (D, A, C)]:
            draw_right_angle(parts, p, v1, v2)
            
        # Side ticks
        def draw_side_tick(p1, p2):
            mx, my = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
            ang = math.atan2(p2[1]-p1[1], p2[0]-p1[0]) + math.pi/2
            s_tick = 8
            parts.append(f'<line x1="{mx + s_tick*math.cos(ang):.2f}" y1="{my + s_tick*math.sin(ang):.2f}" x2="{mx - s_tick*math.cos(ang):.2f}" y2="{my - s_tick*math.sin(ang):.2f}" stroke="{COLORS["text"]}" stroke-width="2"/>')

        for i in range(4):
            draw_side_tick(points[i], points[(i+1)%4])

        # Diagonals
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-dasharray="5,5"/>')
        # Center right angle
        parts.append(f'<path d="M {cx} {cy-15} L {cx+15} {cy-15} L {cx+15} {cy}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        
        # Footer Label
        parts.append(draw_label(cx, cy + s/2 + 55, "Rectángulo + Rombo: Perfección", COLORS['text'], size=20, weight='bold'))
        return title

    elif mode == 'cuadrado_diagonal_formula':
        title = "Diagonal del Cuadrado"
        s = 200
        A = (cx - s/2, cy + s/2)
        B = (cx + s/2, cy + s/2)
        C = (cx + s/2, cy - s/2)
        D = (cx - s/2, cy - s/2)
        
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['success'])
        draw_right_angle(parts, A, B, D)
        
        # Diagonal
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0]+20, B[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+20, C[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0]-20, D[1]-15, "D", COLORS['vertices'], weight='bold'))
        # Labels
        parts.append(draw_label(cx, A[1] + 25, "lado (l)", COLORS['text']))
        parts.append(draw_label(cx + s/2 + 35, cy, "lado (l)", COLORS['text']))
        parts.append(draw_label(cx - 20, cy - 20, "d = l√2", COLORS['danger'], size=22, weight='bold'))
        
        return title

    elif mode == 'ejemplo_rectangulo_verificacion':
        title = "Ejemplo 1: Verificación de Rectángulo"
        w, h = 300, 180
        A = (cx - w/2, cy + h/2)
        B = (cx + w/2, cy + h/2)
        C = (cx + w/2, cy - h/2)
        D = (cx - w/2, cy - h/2)
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        # Diagonals labeled 10cm
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        parts.append(draw_label(cx - 60, cy - 30, "10 cm", COLORS['medianas'], weight='bold'))
        parts.append(draw_label(cx + 60, cy - 30, "10 cm", COLORS['medianas'], weight='bold'))
        parts.append(draw_label(cx, cy + h/2 + 40, "Diagonales Iguales = Rectángulo", COLORS['text'], size=18, weight='bold'))
        return title

    elif mode == 'ejemplo_rombo_perimetro':
        title = "Ejemplo 3: Perímetro del Rombo"
        dw, dh = 240, 240
        A = (cx - dw/2, cy)
        B = (cx, cy - dh/2)
        C = (cx + dw/2, cy)
        D = (cx, cy + dh/2)
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['secondary'], fill_color=COLORS['secondary'])
        # Side labels 5cm
        parts.append(draw_label((A[0]+B[0])/2 - 20, (A[1]+B[1])/2 - 10, "5", COLORS['text'], weight='bold'))
        parts.append(draw_label((B[0]+C[0])/2 + 20, (B[1]+C[1])/2 - 10, "5", COLORS['text'], weight='bold'))
        parts.append(draw_label((C[0]+D[0])/2 + 20, (C[1]+D[1])/2 + 20, "5", COLORS['text'], weight='bold'))
        parts.append(draw_label((D[0]+A[0])/2 - 20, (D[1]+A[1])/2 + 20, "5", COLORS['text'], weight='bold'))
        parts.append(draw_label(cx, cy + dh/2 + 40, "Perímetro = 5 × 4 = 20", COLORS['text'], size=18, weight='bold'))
        return title

    elif mode == 'ejemplo_cuadrado_simetria':
        title = "Ejemplo 5: Simetría del Cuadrado"
        s = 200
        A = (cx - s/2, cy + s/2)
        B = (cx + s/2, cy + s/2)
        C = (cx + s/2, cy - s/2)
        D = (cx - s/2, cy - s/2)
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['success'], fill_color=COLORS['success'])
        # Diagonals with right angle
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        parts.append(f'<path d="M {cx} {cy-15} L {cx+15} {cy-15} L {cx+15} {cy}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        parts.append(draw_label(cx, cy + s/2 + 40, "Diagonales Iguales y Perpendiculares", COLORS['text'], size=18, weight='bold'))
        return title

    elif mode == 'ejemplo_diagonal_cuadrado':
        title = "Ejemplo 6: Diagonal de Cuadrado L=5"
        s = 200 # side = 5
        A = (cx - s/2, cy + s/2)
        B = (cx + s/2, cy + s/2)
        C = (cx + s/2, cy - s/2)
        D = (cx - s/2, cy - s/2)
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['success'], fill_color=COLORS['success'], fill_opacity=0.1)
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0]+20, B[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+20, C[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0]-20, D[1]-15, "D", COLORS['vertices'], weight='bold'))
        # Diagonal
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        # Labels
        parts.append(draw_label(cx, A[1] + 25, "l = 5", COLORS['text'], weight='bold'))
        parts.append(draw_label(cx - 15, cy - 15, "d = 5√2 ≈ 7.07", COLORS['danger'], weight='bold'))
        return title

    elif mode == 'ejemplo_puerta':
        title = "Ejemplo 2: Diagonal de la Puerta"
        scale = 80
        w, h = 1 * scale, 2 * scale
        # Bottom-Left at A
        A = (cx - w/2, cy + h/2)
        B = (cx + w/2, cy + h/2)
        C = (cx + w/2, cy - h/2)
        D = (cx - w/2, cy - h/2)
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['primary'])
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1]+15, "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0]+20, B[1]+15, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+20, C[1]-15, "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0]-20, D[1]-15, "D", COLORS['vertices'], weight='bold'))
        draw_right_angle(parts, A, B, D)
        # Diagonal
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["danger"]}" stroke-width="3"/>')
        # Labels
        parts.append(draw_label(cx, cy + h/2 + 25, "ancho = 1 m", COLORS['text']))
        parts.append(draw_label(cx + w/2 + 55, cy, "alto = 2 m", COLORS['text']))
        parts.append(draw_label(cx - 20, cy - 10, "d = √5 ≈ 2.24", COLORS['danger'], weight='bold'))
        return title

    elif mode == 'ejemplo_area_rombo':
        title = "Ejemplo 4: Área del Rombo (D=10, d=6)"
        dw, dh = 300, 180
        A = (cx - dw/2, cy)
        B = (cx, cy - dh/2) # Top
        C = (cx + dw/2, cy)
        D = (cx, cy + dh/2) # Bottom
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['secondary'], fill_color=COLORS['secondary'], fill_opacity=0.2)
        # Diagonals dashed
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["text"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["text"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
        # Vertex Labels
        parts.append(draw_label(A[0]-20, A[1], "A", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(B[0], B[1]-20, "B", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(C[0]+20, C[1], "C", COLORS['vertices'], weight='bold'))
        parts.append(draw_label(D[0], D[1]+25, "D", COLORS['vertices'], weight='bold'))
        
        # Dimensions outside
        draw_dimension(parts, A, C, dh/2 + 25, "D = 10", horizontal=True)
        draw_dimension(parts, B, D, dw/2 + 25, "d = 6", horizontal=False)
        
        # Result at bottom
        parts.append(draw_label(cx, cy + dh/2 + 75, "Área = (10 × 6) / 2 = 30", COLORS['success'], size=20, weight='bold'))
        return title

    elif mode == 'ejercicio_rombo_pitagoras':
        title = "Ejercicio: Lado del Rombo"
        dw, dh = 320, 240 # Diagonales 8 y 6 (escaladas)
        scale = 40
        # Vertices
        A = (cx - 4*scale, cy)
        B = (cx, cy - 3*scale)
        C = (cx + 4*scale, cy)
        D = (cx, cy + 3*scale)
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['text'])
        M = (cx, cy)
        parts.append(draw_triangle([A, M, D], stroke=COLORS['danger'], fill=COLORS['danger'], fill_opacity=0.2))
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["grid"]}" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["grid"]}" stroke-dasharray="2,2"/>')
        parts.append(f'<path d="M {cx-15} {cy} L {cx-15} {cy+15} L {cx} {cy+15}" fill="none" stroke="{COLORS["danger"]}" stroke-width="2"/>')
        parts.append(draw_label((A[0]+M[0])/2, cy - 20, "D/2 = 4", COLORS['text'], weight='bold'))
        parts.append(draw_label(cx + 45, (M[1]+D[1])/2, "d/2 = 3", COLORS['text'], weight='bold'))
        parts.append(draw_label((A[0]+D[0])/2 - 30, (A[1]+D[1])/2 + 25, "Lado = ?", COLORS['danger'], weight='bold'))
        parts.append(draw_label(cx, cy + dh/2 + 40, "Side = √(3² + 4²) = 5", COLORS['danger'], size=20, weight='bold'))
        return title

    elif mode == 'ejemplo_identificacion_rectangulo':
        title = "Ejemplo: Identificación (Rectángulo)"
        w, h = 320, 160
        A = (cx - w/2, cy + h/2)
        B = (cx + w/2, cy + h/2)
        C = (cx + w/2, cy - h/2)
        D = (cx - w/2, cy - h/2)
        
        draw_quad(parts, [A, B, C, D], stroke_color=COLORS['primary'], fill_color=COLORS['primary'])
        
        # Diagonals
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["danger"]}" stroke-width="2.5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["danger"]}" stroke-width="2.5"/>')
        
        # Labels for logic nodes in example
        parts.append(draw_label(cx, cy - 20, "Diagonales Iguales", COLORS['danger'], weight='bold'))
        parts.append(draw_label(cx, cy + h/2 + 25, "Lados desiguales (b > h)", COLORS['text']))
        parts.append(draw_label(cx, cy + h/2 + 60, "¡Es un Rectángulo!", COLORS['success'], size=20, weight='bold'))
        
        return title

    return "Special Parallelogram"

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    
    parts = []
    # Background
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    
    title = draw_special_quad_scene(parts, width, height, mode)
    
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

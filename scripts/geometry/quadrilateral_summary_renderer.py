
import argparse
import sys
import math
import os

# Add script directory to python path to access core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.colors import COLORS
from core.canvas import get_canvas_config
from core.triangle_primitives import draw_triangle, draw_label

# --- Configuration ---
CANVAS_NAME = 'compound' # Standard 600x460
FONT_SIZE_LABEL = 14
FONT_SIZE_TITLE = 22

def draw_quad(parts, points, stroke_color=COLORS['primary'], fill_color='none', stroke_width=2, fill_opacity=0.1):
    path_d = f"M {points[0][0]} {points[0][1]} L {points[1][0]} {points[1][1]} L {points[2][0]} {points[2][1]} L {points[3][0]} {points[3][1]} Z"
    parts.append(f'<path d="{path_d}" fill="{fill_color}" fill-opacity="{fill_opacity}" stroke="{stroke_color}" stroke-width="{stroke_width}"/>')

def draw_right_angle(parts, p, v1, v2, size=10, color=COLORS['danger']):
    a1 = math.atan2(v1[1]-p[1], v1[0]-p[0])
    a2 = math.atan2(v2[1]-p[1], v2[0]-p[0])
    p1 = (p[0] + size * math.cos(a1), p[1] + size * math.sin(a1))
    p2 = (p[0] + size * math.cos(a2), p[1] + size * math.sin(a2))
    p12 = (p1[0] + size * math.cos(a2), p1[1] + size * math.sin(a2))
    parts.append(f'<path d="M {p1[0]:.2f} {p1[1]:.2f} L {p12[0]:.2f} {p12[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f}" fill="none" stroke="{color}" stroke-width="1.5"/>')

def draw_summary_scene(parts, width, height, mode):
    cx, cy = width / 2, height / 2

    if mode == 'jerarquia_arbol':
        title = "Clasificación de Cuadriláteros"
        
        # Nodes levels
        y0, y1, y2, y3 = 80, 180, 280, 380
        
        # Root
        parts.append(f'<rect x="{cx-80}" y="{y0-20}" width="160" height="40" rx="8" fill="{COLORS["formula_bg"]}" stroke="{COLORS["text"]}"/>')
        parts.append(draw_label(cx, y0, "CUADRILÁTERO", COLORS["text"], weight="bold"))
        
        # Main branches
        x_teide, x_trape, x_paral = cx - 180, cx, cx + 180
        
        # Lines from root
        parts.append(f'<line x1="{cx}" y1="{y0+20}" x2="{x_teide}" y2="{y1-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{cx}" y1="{y0+20}" x2="{x_trape}" y2="{y1-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{cx}" y1="{y0+20}" x2="{x_paral}" y2="{y1-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        
        # Level 1 Nodes
        nodes1 = [
            (x_teide, "Trapezoide", "0 pares paralelos"),
            (x_trape, "Trapecio", "1 par paralelo"),
            (x_paral, "Paralelogramo", "2 pares paralelos")
        ]
        
        for x, name, desc in nodes1:
            parts.append(f'<rect x="{x-70}" y="{y1-20}" width="140" height="40" rx="4" fill="white" stroke="{COLORS["primary"]}" stroke-width="2"/>')
            parts.append(draw_label(x, y1, name, COLORS["primary"], weight="bold"))
            parts.append(draw_label(x, y1+35, desc, COLORS["text_light"], size=12))

        # Level 2 (under Paralelogramo)
        x_rect, x_rombo = x_paral - 70, x_paral + 70
        parts.append(f'<line x1="{x_paral}" y1="{y1+20}" x2="{x_rect}" y2="{y2-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{x_paral}" y1="{y1+20}" x2="{x_rombo}" y2="{y2-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        
        parts.append(f'<rect x="{x_rect-55}" y="{y2-20}" width="110" height="40" rx="4" fill="white" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
        parts.append(draw_label(x_rect, y2, "Rectángulo", COLORS["secondary"], weight="bold"))
        
        parts.append(f'<rect x="{x_rombo-55}" y="{y2-20}" width="110" height="40" rx="4" fill="white" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
        parts.append(draw_label(x_rombo, y2, "Rombo", COLORS["secondary"], weight="bold"))
        
        # Level 3 (Cuadrado)
        x_cuad = x_paral
        parts.append(f'<line x1="{x_rect}" y1="{y2+20}" x2="{x_cuad}" y2="{y3-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{x_rombo}" y1="{y2+20}" x2="{x_cuad}" y2="{y3-20}" stroke="{COLORS["grid"]}" stroke-width="2"/>')
        
        parts.append(f'<rect x="{x_cuad-60}" y="{y3-20}" width="120" height="40" rx="4" fill="white" stroke="{COLORS["success"]}" stroke-width="2"/>')
        parts.append(draw_label(x_cuad, y3, "CUADRADO", COLORS["success"], weight="bold"))
        parts.append(draw_label(x_cuad, y3+35, "¡Lo tiene TODO!", COLORS["success"], size=12, weight="bold"))

        return title

    elif mode == 'mapa_areas':
        title = "Mapa de Referencia: Áreas"
        
        # 3x2 Grid positions
        cols = [width*0.2, width*0.5, width*0.8]
        rows = [140, 310]
        
        # 1. Cuadrado
        p1 = (cols[0], rows[0])
        s = 50
        pts = [(p1[0]-s/2, p1[1]+s/2), (p1[0]+s/2, p1[1]+s/2), (p1[0]+s/2, p1[1]-s/2), (p1[0]-s/2, p1[1]-s/2)]
        draw_quad(parts, pts, stroke_color=COLORS['success'])
        parts.append(draw_label(p1[0], p1[1]+s/2+15, "l", COLORS['text']))
        parts.append(draw_label(p1[0], p1[1]+s/2+45, "A = l²", COLORS['success'], weight='bold'))
        parts.append(draw_label(p1[0], p1[1]-s/2-25, "Cuadrado", COLORS['vertices'], size=14, weight='bold'))

        # 2. Rectángulo 
        p2 = (cols[1], rows[0])
        w, h = 80, 50
        pts = [(p2[0]-w/2, p2[1]+h/2), (p2[0]+w/2, p2[1]+h/2), (p2[0]+w/2, p2[1]-h/2), (p2[0]-w/2, p2[1]-h/2)]
        draw_quad(parts, pts, stroke_color=COLORS['primary'])
        parts.append(draw_label(p2[0], p2[1]+h/2+15, "b", COLORS['text']))
        parts.append(draw_label(p2[0]+w/2+15, p2[1], "h", COLORS['text']))
        parts.append(draw_label(p2[0], p2[1]+h/2+45, "A = b · h", COLORS['primary'], weight='bold'))
        parts.append(draw_label(p2[0], p2[1]-h/2-25, "Rectángulo", COLORS['vertices'], size=14, weight='bold'))

        # 3. Rombo
        p3 = (cols[2], rows[0])
        dw, dh = 80, 50
        pts = [(p3[0]-dw/2, p3[1]), (p3[0], p3[1]-dh/2), (p3[0]+dw/2, p3[1]), (p3[0], p3[1]+dh/2)]
        draw_quad(parts, pts, stroke_color=COLORS['secondary'])
        parts.append(f'<line x1="{p3[0]-dw/2}" y1="{p3[1]}" x2="{p3[0]+dw/2}" y2="{p3[1]}" stroke="{COLORS["medianas"]}" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{p3[0]}" y1="{p3[1]-dh/2}" x2="{p3[0]}" y2="{p3[1]+dh/2}" stroke="{COLORS["medianas"]}" stroke-dasharray="2,2"/>')
        parts.append(draw_label(p3[0], p3[1]+dh/2+45, "A = (D · d) / 2", COLORS['secondary'], weight='bold'))
        parts.append(draw_label(p3[0], p3[1]-dh/2-25, "Rombo", COLORS['vertices'], size=14, weight='bold'))

        # 4. Paralelogramo
        p4 = (cols[0], rows[1])
        w, h, off = 80, 50, 20
        pts = [(p4[0]-w/2-off, p4[1]+h/2), (p4[0]+w/2-off, p4[1]+h/2), (p4[0]+w/2+off, p4[1]-h/2), (p4[0]-w/2+off, p4[1]-h/2)]
        draw_quad(parts, pts, stroke_color=COLORS['primary'])
        parts.append(draw_label(p4[0], p4[1]+h/2+15, "b", COLORS['text']))
        # Height line
        parts.append(f'<line x1="{p4[0]-w/2+off}" y1="{p4[1]-h/2}" x2="{p4[0]-w/2+off}" y2="{p4[1]+h/2}" stroke="{COLORS["danger"]}" stroke-dasharray="2,2"/>')
        parts.append(draw_label(p4[0]-w/2+off-15, p4[1], "h", COLORS['danger']))
        parts.append(draw_label(p4[0], p4[1]+h/2+45, "A = b · h", COLORS['primary'], weight='bold'))
        parts.append(draw_label(p4[0], p4[1]-h/2-25, "Paralelogramo", COLORS['vertices'], size=14, weight='bold'))

        # 5. Trapecio
        p5 = (cols[1], rows[1])
        B, b, h = 90, 50, 50
        pts = [(p5[0]-B/2, p5[1]+h/2), (p5[0]+B/2, p5[1]+h/2), (p5[0]+b/2, p5[1]-h/2), (p5[0]-b/2, p5[1]-h/2)]
        draw_quad(parts, pts, stroke_color=COLORS['secondary'])
        parts.append(draw_label(p5[0], p5[1]+h/2+15, "B", COLORS['text']))
        parts.append(draw_label(p5[0], p5[1]-h/2-15, "b", COLORS['text']))
        parts.append(f'<line x1="{p5[0]-b/2}" y1="{p5[1]-h/2}" x2="{p5[0]-b/2}" y2="{p5[1]+h/2}" stroke="{COLORS["danger"]}" stroke-dasharray="2,2"/>')
        parts.append(draw_label(p5[0]-b/2-15, p5[1], "h", COLORS['danger']))
        parts.append(draw_label(p5[0], p5[1]+h/2+45, "A = (B+b)/2 · h", COLORS['secondary'], weight='bold', size=12))
        parts.append(draw_label(p5[0], p5[1]-h/2-35, "Trapecio", COLORS['vertices'], size=14, weight='bold'))

        # 6. Deltoide
        p6 = (cols[2], rows[1])
        dw, dh = 60, 90
        pts = [(p6[0]-dw/2, p6[1]-10), (p6[0], p6[1]-dh/2), (p6[0]+dw/2, p6[1]-10), (p6[0], p6[1]+dh/2)]
        draw_quad(parts, pts, stroke_color=COLORS['primary'])
        parts.append(f'<line x1="{p6[0]-dw/2}" y1="{p6[1]-10}" x2="{p6[0]+dw/2}" y2="{p6[1]-10}" stroke="{COLORS["medianas"]}" stroke-dasharray="2,2"/>')
        parts.append(f'<line x1="{p6[0]}" y1="{p6[1]-dh/2}" x2="{p6[0]}" y2="{p6[1]+dh/2}" stroke="{COLORS["medianas"]}" stroke-dasharray="2,2"/>')
        parts.append(draw_label(p6[0], p6[1]+dh/2+45, "A = (D · d) / 2", COLORS['primary'], weight='bold'))
        parts.append(draw_label(p6[0], p6[1]-dh/2-25, "Deltoide", COLORS['vertices'], size=14, weight='bold'))

        return title

    return "Summary Scene"

def generate_svg(mode, output_path):
    canvas_cfg = get_canvas_config(CANVAS_NAME)
    width, height = canvas_cfg['width'], canvas_cfg['height']
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="font-family: Inter, system-ui, sans-serif;">')
    parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" />')
    title = draw_summary_scene(parts, width, height, mode)
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

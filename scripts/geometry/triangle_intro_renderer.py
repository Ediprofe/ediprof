#!/usr/bin/env python3
"""
Triangle Intro Renderer
Generates introductory illustrations for "Definición de Triángulo".
"""

import math
import argparse
import html
from pathlib import Path
from core.colors import COLORS

# Canvas Configuration
WIDTH = 600
HEIGHT = 400
CX, CY = WIDTH / 2, HEIGHT / 2

def get_coord(cx, cy, r, angle_deg):
    rad = math.radians(angle_deg)
    return cx + r * math.cos(rad), cy - r * math.sin(rad)

def draw_point(x, y, label=None, color=COLORS['text'], label_offset=(0, -20)):
    svg = f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="{color}"/>'
    if label:
        svg += f'<text x="{x+label_offset[0]:.2f}" y="{y+label_offset[1]:.2f}" text-anchor="middle" font-weight="bold" fill="{color}">{html.escape(label)}</text>'
    return svg

def draw_segment(p1, p2, color=COLORS['line'], width=2, label=None, label_offset=(0, -10)):
    svg = f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
    if label:
        # Midpoint
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        svg += f'<text x="{mx+label_offset[0]:.2f}" y="{my+label_offset[1]:.2f}" text-anchor="middle" dominant-baseline="middle" font-weight="bold" font-style="italic" fill="{color}">{html.escape(label)}</text>'
    return svg

def draw_angle_arc(p_center, p_from, p_to, radius=30, color=COLORS['angle'], label=None):
    # Calculate angles
    dx1, dy1 = p_from[0] - p_center[0], -(p_from[1] - p_center[1]) # SVG y inverted
    dx2, dy2 = p_to[0] - p_center[0], -(p_to[1] - p_center[1])
    
    ang1 = math.degrees(math.atan2(dy1, dx1))
    ang2 = math.degrees(math.atan2(dy2, dx2))
    
    # Normalize
    diff = ang2 - ang1
    while diff < 0: diff += 360
    
    # We want the interior angle. For a triangle, usually it's < 180.
    # If diff > 180, swap.
    if diff > 180:
        ang1, ang2 = ang2, ang1
        diff = 360 - diff
        
    start_angle = ang1
    end_angle = ang1 + diff
    
    # Draw arc
    # SVG Arc path
    # M start_x start_y A r r 0 large_arc sweep end_x end_y
    # Y is inverted. 
    # math angle + -> svg angle -
    # But let's use get_coord which handles it.
    
    sx, sy = get_coord(p_center[0], p_center[1], radius, start_angle)
    ex, ey = get_coord(p_center[0], p_center[1], radius, end_angle)
    
    large_arc = 1 if diff > 180 else 0
    sweep_flag = 0 # CCW in math is CW in SVG? Let's assume 0 for standard counter-clockwise visual in math.
    
    # Wait, get_coord: y = cy - r sin(a).
    # If a increases, sin(a) increases, y decreases (goes up). 
    # So 0->90 is "Upward". This is CCW visually on standard XY.
    
    svg = f'<path d="M {p_center[0]} {p_center[1]} L {sx:.2f} {sy:.2f} A {radius} {radius} 0 {large_arc} 0 {ex:.2f} {ey:.2f} Z" fill="{color}" fill-opacity="0.2" stroke="none"/>'
    svg += f'<path d="M {sx:.2f} {sy:.2f} A {radius} {radius} 0 {large_arc} 0 {ex:.2f} {ey:.2f}" fill="none" stroke="{color}" stroke-width="2"/>'
    
    if label:
        mid_ang = start_angle + diff/2
        lx, ly = get_coord(p_center[0], p_center[1], radius + 20, mid_ang)
        svg += f'<text x="{lx:.2f}" y="{ly:.2f}" text-anchor="middle" dominant-baseline="middle" font-weight="bold" fill="{color}">{html.escape(label)}</text>'
        
    return svg

def draw_tick_marks(p1, p2, count=1, length=10, gap=4, color=COLORS['line']):
    svg = ""
    # Midpoint
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    
    # Vector
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    l = math.hypot(dx, dy)
    if l == 0: return ""
    
    # Unit vector
    ux, uy = dx/l, dy/l
    
    # Normal vector
    nx, ny = -uy, ux # 90 deg rotation
    
    # Draw ticks
    # Offsets along the line for multiple ticks
    # If count is odd: 0, +/- 1*gap...
    # If count is even: +/- 0.5*gap, +/- 1.5*gap...
    
    offsets = []
    if count % 2 == 1:
        offsets.append(0)
        for i in range(1, (count+1)//2):
            offsets.append(i * gap)
            offsets.append(-i * gap)
    else:
        for i in range(count // 2):
            offsets.append((i + 0.5) * gap)
            offsets.append(-(i + 0.5) * gap)
            
    for off in offsets:
        # Center of this tick
        tx, ty = mx + ux * off, my + uy * off
        
        # Endpoints of tick
        t1x, t1y = tx + nx * (length/2), ty + ny * (length/2)
        t2x, t2y = tx - nx * (length/2), ty - ny * (length/2)
        
        svg += f'<line x1="{t1x:.2f}" y1="{t1y:.2f}" x2="{t2x:.2f}" y2="{t2y:.2f}" stroke="{color}" stroke-width="2" stroke-linecap="round"/>'
        
    return svg

def generate_svg_main(mode, output_path):
    svg_content = ""
    scale = 1.0
    
    # Common styles
    style_bg = f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS["background"]}" rx="12"/>'
    
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" style="font-family: Inter, system-ui, sans-serif;">', style_bg]

    if mode == 'definition':
        A, B, C = (300, 100), (150, 350), (450, 350)
        parts.append(draw_segment(A, B))
        parts.append(draw_segment(B, C))
        parts.append(draw_segment(C, A))
        parts.append(draw_point(A[0], A[1], "A"))
        parts.append(draw_point(B[0], B[1], "B", label_offset=(-15, 10)))
        parts.append(draw_point(C[0], C[1], "C", label_offset=(15, 10)))
        
    elif mode == 'collinear_vs_non_collinear':
        parts.append(f'<text x="50" y="40" font-weight="bold" fill="{COLORS["text_light"]}">1. Colineales (No forman triángulo)</text>')
        y_line = 100
        parts.append(draw_segment((100, y_line), (500, y_line), color=COLORS['grid'], width=1))
        parts.append(draw_segment((150, y_line), (300, y_line), color=COLORS['line'], width=3))
        parts.append(draw_segment((300, y_line), (450, y_line), color=COLORS['line'], width=3))
        parts.append(draw_point(150, y_line, "A", label_offset=(0, -15)))
        parts.append(draw_point(300, y_line, "B", label_offset=(0, -15)))
        parts.append(draw_point(450, y_line, "C", label_offset=(0, -15)))
        
        parts.append(f'<text x="50" y="200" font-weight="bold" fill="{COLORS["text_light"]}">2. No Colineales (Forman triángulo)</text>')
        A2, B2, C2 = (300, 250), (150, 350), (450, 350)
        parts.append(draw_segment(A2, B2))
        parts.append(draw_segment(B2, C2))
        parts.append(draw_segment(C2, A2))
        parts.append(draw_point(A2[0], A2[1], "A"))
        parts.append(draw_point(B2[0], B2[1], "B", label_offset=(-15, 10)))
        parts.append(draw_point(C2[0], C2[1], "C", label_offset=(15, 10)))
        
    elif mode == 'elements':
        A, B, C = (300, 100), (150, 350), (450, 350)
        parts.append(draw_angle_arc(A, C, B, label="α"))
        parts.append(draw_angle_arc(B, A, C, label="β"))
        parts.append(draw_angle_arc(C, B, A, label="γ"))
        parts.append(draw_segment(B, C, label="a", label_offset=(0, 20)))
        parts.append(draw_segment(C, A, label="b", label_offset=(20, 0)))
        parts.append(draw_segment(A, B, label="c", label_offset=(-20, 0)))
        parts.append(draw_point(A[0], A[1], "A"))
        parts.append(draw_point(B[0], B[1], "B", label_offset=(-15, 10)))
        parts.append(draw_point(C[0], C[1], "C", label_offset=(15, 10)))
        
    elif mode == 'ex1_opposite_sides':
        P, Q, R = (300, 80), (100, 320), (500, 320)
        cP, cQ, cR = COLORS['primary'], COLORS['secondary'], COLORS['highlight']
        
        parts.append(draw_segment(Q, R, color=cP, width=4, label="p (opuesto a P)", label_offset=(0, 25)))
        parts.append(draw_segment(P, R, color=cQ, width=4, label="q", label_offset=(30, 0)))
        parts.append(draw_segment(P, Q, color=cR, width=4, label="r", label_offset=(-30, 0)))
        
        parts.append(draw_angle_arc(P, R, Q, radius=40, color=cP, label="P"))
        parts.append(draw_angle_arc(Q, P, R, radius=40, color=cQ, label="Q"))
        parts.append(draw_angle_arc(R, Q, P, radius=40, color=cR, label="R"))

    elif mode == 'ex2_existence_fail':
        unit = 50
        base_len = 8 * unit
        start_x = (WIDTH - base_len)/2
        y = 300
        p_start, p_end = (start_x, y), (start_x + base_len, y)
        
        parts.append(draw_segment(p_start, p_end, width=4, label="c = 8", label_offset=(0, 25)))
        
        arm3_len = 3 * unit
        ang = 20
        end3 = get_coord(p_start[0], p_start[1], arm3_len, ang)
        parts.append(draw_segment(p_start, end3, color=COLORS['secondary'], width=4))
        parts.append(f'<text x="{end3[0]-20}" y="{end3[1]-10}" fill="{COLORS["secondary"]}" font-weight="bold">a=3</text>')
        
        arm4_len = 4 * unit
        end4 = get_coord(p_end[0], p_end[1], arm4_len, 180-ang)
        parts.append(draw_segment(p_end, end4, color=COLORS['highlight'], width=4))
        parts.append(f'<text x="{end4[0]+10}" y="{end4[1]-10}" fill="{COLORS["highlight"]}" font-weight="bold">b=4</text>')
        
        parts.append(draw_segment(end3, end4, color=COLORS['text_light'], width=1, label="¡No llegan!"))
        parts.append(f'<path d="M {p_start[0]} {p_start[1]} L {end3[0]} {end3[1]} A {arm3_len} {arm3_len} 0 0 0 {p_start[0]+arm3_len} {p_start[1]}" fill="none" stroke="{COLORS["secondary"]}" stroke-dasharray="4"/>')
        parts.append(f'<path d="M {p_end[0]} {p_end[1]} L {end4[0]} {end4[1]} A {arm4_len} {arm4_len} 0 0 1 {p_end[0]-arm4_len} {p_end[1]}" fill="none" stroke="{COLORS["highlight"]}" stroke-dasharray="4"/>')

    elif mode == 'ex3_missing_side':
        scale = 40
        b_len = 7 * scale
        s_len = 5 * scale
        cy, cx = 300, WIDTH/2
        h = math.sqrt(s_len**2 - (b_len/2)**2)
        p1, p2, p3 = (cx - b_len/2, cy), (cx + b_len/2, cy), (cx, cy - h)
        
        parts.append(draw_segment(p1, p2, label="7", label_offset=(0, 20)))
        parts.append(draw_segment(p1, p3, label="5", label_offset=(-20, 0)))
        parts.append(draw_segment(p2, p3, label="x", label_offset=(20, 0), color=COLORS['primary']))
        parts.append(f'<text x="{cx}" y="50" text-anchor="middle" font-size="14" fill="{COLORS["text_light"]}">Condición: 5 + x > 7  →  x > 2</text>')
    
    # ---------------- NEW MODES FOR CLASSIFICATION ----------------

    elif mode == 'equilateral':
        # 3 Sides equal, 3 angles 60
        s = 250
        h = s * math.sqrt(3)/2
        cx, cy = WIDTH/2, 350
        # Vertices
        A = (cx, cy - h)
        B = (cx - s/2, cy)
        C = (cx + s/2, cy)
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Tick marks (1 count)
        parts.append(draw_tick_marks(A, B, count=1, color=COLORS['primary']))
        parts.append(draw_tick_marks(B, C, count=1, color=COLORS['primary']))
        parts.append(draw_tick_marks(C, A, count=1, color=COLORS['primary']))
        
        # Angles (60)
        parts.append(draw_angle_arc(A, C, B, radius=40, label="60°", color=COLORS['angle']))
        parts.append(draw_angle_arc(B, A, C, radius=40, label="60°", color=COLORS['angle']))
        parts.append(draw_angle_arc(C, B, A, radius=40, label="60°", color=COLORS['angle']))

    elif mode == 'isosceles':
        # 2 Sides equal (legs), Base different
        # Let legs be long, base narrow-ish
        w_base = 160
        h = 300
        cx, cy = WIDTH/2, 380
        
        A = (cx, cy - h)
        B = (cx - w_base/2, cy)
        C = (cx + w_base/2, cy)
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Tick marks (2 counts for legs)
        parts.append(draw_tick_marks(A, B, count=2, color=COLORS['primary']))
        parts.append(draw_tick_marks(C, A, count=2, color=COLORS['primary']))
        # Base has 1 or no ticks? Using 1 tick represents 'diferent from 2'. 
        # But commonly we just mark the equal ones.
        
        # Angles (Base angles equal)
        # Calculate angle at B
        # tan(B) = h / (w/2)
        ang = math.degrees(math.atan2(h, w_base/2))
        ang_str = f"{ang:.0f}°"
        
        parts.append(draw_angle_arc(B, A, C, radius=40, label="α", color=COLORS['angle']))
        parts.append(draw_angle_arc(C, B, A, radius=40, label="α", color=COLORS['angle']))
        parts.append(draw_angle_arc(A, C, B, radius=40, label="β", color=COLORS['text_light']))

    elif mode == 'scalene':
        # 3 Different sides
        A = (200, 50)
        B = (100, 350)
        C = (550, 350)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Ticks: 1, 2, 3
        parts.append(draw_tick_marks(A, B, count=1, color=COLORS['primary']))
        parts.append(draw_tick_marks(B, C, count=2, color=COLORS['secondary']))
        parts.append(draw_tick_marks(C, A, count=3, color=COLORS['highlight']))
        
        # Angles: alpha, beta, gamma
        parts.append(draw_angle_arc(A, C, B, radius=30, label="α", color=COLORS['text']))
        parts.append(draw_angle_arc(B, A, C, radius=40, label="β", color=COLORS['text']))
        parts.append(draw_angle_arc(C, B, A, radius=50, label="γ", color=COLORS['text']))
        
    elif mode == 'sides_angles_relation':
        # 3 Mini triangles side by side
        # Equilateral
        cx1 = WIDTH * 0.2
        cy = 250
        s1 = 80
        h1 = s1 * math.sqrt(3)/2
        A1, B1, C1 = (cx1, cy-h1), (cx1-s1/2, cy), (cx1+s1/2, cy)
        
        parts.append(draw_segment(A1, B1, width=2)); parts.append(draw_segment(B1, C1, width=2)); parts.append(draw_segment(C1, A1, width=2))
        parts.append(draw_tick_marks(A1, B1, 1, 6, 2)); parts.append(draw_tick_marks(B1, C1, 1, 6, 2)); parts.append(draw_tick_marks(C1, A1, 1, 6, 2))
        parts.append(f'<text x="{cx1}" y="{cy+30}" text-anchor="middle" font-size="12" font-weight="bold">3 Lados = 3 Ángulos</text>')
        
        # Isosceles
        cx2 = WIDTH * 0.5
        w2, h2 = 60, 100
        A2, B2, C2 = (cx2, cy-h2), (cx2-w2/2, cy), (cx2+w2/2, cy)
        parts.append(draw_segment(A2, B2, width=2)); parts.append(draw_segment(B2, C2, width=2)); parts.append(draw_segment(C2, A2, width=2))
        parts.append(draw_tick_marks(A2, B2, 2, 6, 2)); parts.append(draw_tick_marks(C2, A2, 2, 6, 2))
        parts.append(f'<text x="{cx2}" y="{cy+30}" text-anchor="middle" font-size="12" font-weight="bold">2 Lados = 2 Ángulos</text>')
        
        # Scalene
        cx3 = WIDTH * 0.8
        A3, B3, C3 = (cx3-20, cy-90), (cx3-50, cy), (cx3+50, cy)
        parts.append(draw_segment(A3, B3, width=2)); parts.append(draw_segment(B3, C3, width=2)); parts.append(draw_segment(C3, A3, width=2))
        parts.append(draw_tick_marks(A3, B3, 1, 6, 2)); parts.append(draw_tick_marks(B3, C3, 2, 6, 2)); parts.append(draw_tick_marks(C3, A3, 3, 6, 2))
        parts.append(f'<text x="{cx3}" y="{cy+30}" text-anchor="middle" font-size="12" font-weight="bold">0 Lados = 0 Ángulos</text>')

    elif mode == 'ex1_identification':
        # 8, 8, 5 Isosceles
        # Scale: 1 unit = 30px
        # Base 5 = 150px. Sides 8 = 240px.
        scale = 30
        w = 5 * scale
        leg = 8 * scale
        h = math.sqrt(leg**2 - (w/2)**2)
        cx, cy = WIDTH/2, 350
        
        A, B, C = (cx, cy-h), (cx-w/2, cy), (cx+w/2, cy)
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4"/>')
        
        parts.append(draw_segment(A, B, label="8 cm", label_offset=(-20, 0), width=4, color=COLORS["primary"]))
        parts.append(draw_segment(C, A, label="8 cm", label_offset=(20, 0), width=4, color=COLORS["primary"]))
        parts.append(draw_segment(B, C, label="5 cm", label_offset=(0, 20), width=4))
        
        parts.append(f'<text x="{cx}" y="50" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">¿Qué tipo es?</text>')

    elif mode == 'ex2_perimeter':
        # Equilateral with P=15. Calculate side = 5.
        s = 200 # Visual size
        h = s * math.sqrt(3)/2
        cx, cy = WIDTH/2, 320
        A, B, C = (cx, cy-h), (cx-s/2, cy), (cx+s/2, cy)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4"/>')
        
        # Center label
        centroid_y = cy - h/3
        parts.append(f'<text x="{cx}" y="{centroid_y}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["primary"]}">Perímetro = 15</text>')
        parts.append(f'<text x="{cx}" y="{centroid_y+20}" text-anchor="middle" font-size="12" fill="{COLORS["text_light"]}">3 lados iguales</text>')
        
        parts.append(draw_segment(A, B, label="x = 5", label_offset=(-25, 0), width=3))
        parts.append(draw_segment(B, C, label="x = 5", label_offset=(0, 20), width=3))
        parts.append(draw_segment(C, A, label="x = 5", label_offset=(25, 0), width=3))

    elif mode == 'ex3_scalene':
        # 3, 4, 5 Sides
        scale = 60
        A = (150, 50) # Right angle top? 3-4-5 is right triangle.
        # Let's verify coordinates for 3-4-5 right triangle.
        # B at origin. C at (4,0). A at (0,3).
        # B=(150, 350). C=(150+240, 350) -> (390, 350). A=(150, 350-180) -> (150, 170).
        B = (200, 350)
        C = (200 + 4*scale, 350) # +240 = 440
        A = (200, 350 - 3*scale) # -180 = 170
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4"/>')
        
        parts.append(draw_segment(A, B, label="3 m", label_offset=(-20, 0), width=4, color=COLORS['text']))
        parts.append(draw_segment(B, C, label="4 m", label_offset=(0, 20), width=4, color=COLORS['text']))
        parts.append(draw_segment(C, A, label="5 m", label_offset=(20, 0), width=4, color=COLORS['text']))
        
        parts.append(f'<text x="{320}" y="100" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["secondary"]}">Todos diferentes</text>')

    # ---------------- CLASSIFICATION BY ANGLES ----------------

    elif mode == 'acutangle':
        # All angles < 90
        # Generic triangle
        A = (300, 100)
        B = (150, 350)
        C = (450, 350)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        parts.append(draw_angle_arc(A, C, B, radius=40, label="< 90°", color=COLORS['success']))
        parts.append(draw_angle_arc(B, A, C, radius=40, label="< 90°", color=COLORS['success']))
        parts.append(draw_angle_arc(C, B, A, radius=40, label="< 90°", color=COLORS['success']))
        
        parts.append(f'<text x="{300}" y="{380}" text-anchor="middle" font-weight="bold" fill="{COLORS["success"]}">Todos Agudos</text>')

    elif mode == 'rectangle':
        # One right angle
        scale = 1.2
        offset_x = 50
        B = (150 + offset_x, 350) # Bottom-Left (Right Angle)
        C = (150 + offset_x + 300*scale, 350) # Bottom-Right
        A = (150 + offset_x, 350 - 200*scale) # Top-Left
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Right angle mark
        size = 20
        parts.append(f'<rect x="{B[0]}" y="{B[1]-size}" width="{size}" height="{size}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
        parts.append(f'<text x="{B[0]+35}" y="{B[1]-10}" font-weight="bold" fill="{COLORS["angle"]}">90°</text>')
        
        # Labels
        parts.append(f'<text x="{B[0]-25}" y="{B[1]-100}" text-anchor="end" font-style="italic" fill="{COLORS["text_light"]}">Cateto</text>')
        parts.append(f'<text x="{B[0]+150}" y="{B[1]+25}" text-anchor="middle" font-style="italic" fill="{COLORS["text_light"]}">Cateto</text>')
        parts.append(f'<text x="{C[0]-100}" y="{A[1]+80}" text-anchor="start" font-weight="bold" fill="{COLORS["primary"]}">Hipotenusa</text>')

    elif mode == 'obtusangle':
        # One angle > 90
        B = (250, 350) # Vertex with obtuse angle
        C = (550, 350) # Right vertex
        # A needs to be to the left of B to make B obtuse
        A = (50, 150)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        parts.append(draw_angle_arc(B, C, A, radius=30, label="> 90°", color=COLORS['highlight']))
        parts.append(f'<text x="{300}" y="{380}" text-anchor="middle" font-weight="bold" fill="{COLORS["highlight"]}">1 Obtuso</text>')

    elif mode == 'logic_geometry':
        # Why not 2 right angles?
        # Draw a base line, and two perpendiculars going up parallel
        p1 = (150, 300)
        p2 = (450, 300)
        
        # Base
        parts.append(draw_segment(p1, p2, width=4))
        
        # Perpendiculars
        h = 150
        top1 = (p1[0], p1[1]-h)
        top2 = (p2[0], p2[1]-h)
        
        parts.append(draw_segment(p1, top1, color=COLORS['angle'], width=3))
        parts.append(draw_segment(p2, top2, color=COLORS['angle'], width=3))
        
        # Right angle marks
        s = 25
        parts.append(f'<rect x="{p1[0]}" y="{p1[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
        parts.append(f'<rect x="{p2[0]-s}" y="{p2[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
        
        parts.append(f'<text x="{p1[0]-40}" y="{p1[1]-h/2}" font-size="24" fill="{COLORS["angle"]}">90°</text>')
        parts.append(f'<text x="{p2[0]+10}" y="{p2[1]-h/2}" font-size="24" fill="{COLORS["angle"]}">90°</text>')
        
        # "Parallel - Never meet" annotation
        parts.append(f'<text x="{WIDTH/2}" y="{100}" text-anchor="middle" font-size="18" fill="{COLORS["primary"]}" font-weight="bold">¡Nunca se juntan!</text>')
        parts.append(f'<text x="{WIDTH/2}" y="{130}" text-anchor="middle" font-size="14" fill="{COLORS["text_light"]}">Suman 180°... ya no queda para el 3er ángulo.</text>')

    elif mode == 'ex1_quick_id':
        # 40, 60, 80 triangle
        # Acutangle
        A = (300, 80)
        B = (150, 350)
        C = (450, 350)
        # Not accurate angles but illustrative
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        parts.append(draw_angle_arc(A, C, B, label="80°", color=COLORS['text']))
        parts.append(draw_angle_arc(B, A, C, label="60°", color=COLORS['text']))
        parts.append(draw_angle_arc(C, B, A, label="40°", color=COLORS['text']))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" fill="{COLORS["success"]}" font-weight="bold">Todos &lt; 90° → Acutángulo</text>')

    elif mode == 'ex2_intruder':
        # 110, 35, 35
        # Obtuse Isosceles
        B = (300, 100) # Top obtuse angle
        # 110 deg
        # Base angles 35
        # Let's project legs.
        leg_len = 200
        angle_rad = math.radians(110/2)
        dx = leg_len * math.sin(angle_rad)
        dy = leg_len * math.cos(angle_rad)
        
        A = (300 - dx, 100 + dy)
        C = (300 + dx, 100 + dy)
        
        # Center vertically
        # Shift down
        shift_y = 50
        A = (A[0], A[1]+shift_y)
        B = (B[0], B[1]+shift_y)
        C = (C[0], C[1]+shift_y)

        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        parts.append(draw_angle_arc(B, C, A, radius=30, label="110°", color=COLORS['highlight']))
        parts.append(draw_angle_arc(A, B, C, radius=40, label="35°", color=COLORS['text_light']))
        parts.append(draw_angle_arc(C, A, B, radius=40, label="35°", color=COLORS['text_light']))

        parts.append(f'<text x="{300}" y="{350}" text-anchor="middle" font-size="16" fill="{COLORS["highlight"]}" font-weight="bold">¡Hay un intruso &gt; 90°!</text>')

    elif mode == 'ex3_double_class':
        # Isosceles + Right Angle (5, 5, 90)
        cx, cy = 300, 350
        s = 200
        # Right angle at bottom center? Let's do standard orientation.
        B = (150, 300) # Corner
        C = (150 + s, 300)
        A = (150, 300 - s)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Right angle mark
        size=25
        parts.append(f'<rect x="{B[0]}" y="{B[1]-size}" width="{size}" height="{size}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2"/>')
        parts.append(f'<text x="{B[0]+40}" y="{B[1]-10}" fill="{COLORS["primary"]}" font-weight="bold">90°</text>')
        
        # Sides labels
        parts.append(draw_segment(A, B, label="5 cm", label_offset=(-30, 0), color=COLORS['secondary'], width=4))
        parts.append(draw_segment(B, C, label="5 cm", label_offset=(0, 25), color=COLORS['secondary'], width=4))
        
        # Double Classification Text
        parts.append(f'<text x="{400}" y="{150}" text-anchor="middle" font-weight="bold" fill="{COLORS["primary"]}">1. Rectángulo (90°)</text>')
        parts.append(f'<text x="{400}" y="{180}" text-anchor="middle" font-weight="bold" fill="{COLORS["secondary"]}">2. Isósceles (Lados =)</text>')

    # ---------------- ANGLES PROPERTIES (INTERNAL/EXTERNAL) ----------------

    elif mode == 'internal_angles_sum':
        # Triangle with angles A, B, C labeled and equation A+B+C=180
        A = (300, 50)
        B = (100, 350)
        C = (500, 350)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Angles
        parts.append(draw_angle_arc(A, C, B, radius=40, label="A", color=COLORS['primary']))
        parts.append(draw_angle_arc(B, A, C, radius=40, label="B", color=COLORS['secondary']))
        parts.append(draw_angle_arc(C, B, A, radius=40, label="C", color=COLORS['highlight']))
        
        # Equation Text
        parts.append(f'<text x="{WIDTH/2}" y="{390}" text-anchor="middle" font-size="20" font-weight="bold" fill="{COLORS["text"]}">A + B + C = 180°</text>')
        
        # Unfolded visualization (optional/simplified)
        # Maybe show a straight line with semicircles A, B, C? 
        # Let's keep it simple for now, just the theorem statement visualization.
        
    elif mode == 'external_angles_sum':
        # Triangle with sides extended to show exterior angles
        # Shrink triangle a bit to have space for extensions
        scale = 0.7
        A = (300, 150)
        B = (200, 300)
        C = (400, 300)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Extensions
        ext_len = 100
        # Extend CA beyond A
        # Vector CA = A - C = (-100, -150)
        # Norm = sqrt(100^2 + 150^2) approx 180
        # extension
        parts.append(draw_segment(A, (A[0]-60, A[1]-90), color=COLORS['grid'], width=2)) # reduced manually
        # Extend AB beyond B
        parts.append(draw_segment(B, (B[0]-60, B[1]+90), color=COLORS['grid'], width=2))
        # Extend BC beyond C
        parts.append(draw_segment(C, (C[0]+120, C[1]), color=COLORS['grid'], width=2))
        
        # Exterior Angles
        # Ext A (Supplement of A)
        parts.append(draw_angle_arc(A, (A[0]-60, A[1]-90), C, radius=30, label="Ext A", color=COLORS['primary']))
        # Ext B
        parts.append(draw_angle_arc(B, (B[0]-60, B[1]+90), A, radius=30, label="Ext B", color=COLORS['secondary']))
        # Ext C
        parts.append(draw_angle_arc(C, (C[0]+120, C[1]), B, radius=30, label="Ext C", color=COLORS['highlight']))
        
        parts.append(f'<text x="{WIDTH/2}" y="{50}" text-anchor="middle" font-size="20" font-weight="bold" fill="{COLORS["text"]}">Suman 360° (Una vuelta)</text>')

    elif mode == 'exterior_angle_theorem':
        # Visualizing Ext = Int + Int
        A = (150, 50)
        B = (150, 350)
        C = (450, 350) # Right triangle for simplicity? No, let's do generic.
        # Shift A left
        A = (200, 100)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Extend BC for exterior angle
        ext_C = (550, 350)
        parts.append(draw_segment(C, ext_C, color=COLORS['grid'], width=3))
        
        # Internal Angles
        parts.append(draw_angle_arc(A, C, B, radius=40, label="α", color=COLORS['primary']))
        parts.append(draw_angle_arc(B, A, C, radius=40, label="β", color=COLORS['secondary']))
        
        # Exterior Angle
        # From A to ext_C centered at C
        # Note: draw_angle_arc goes CCW from p_from to p_to.
        # Vector CA angle is approx 135 deg? Vector C-ext is 0 deg.
        # We want angle from ext line to CA line. So p_from = ext_C, p_to = A.
        parts.append(draw_angle_arc(C, ext_C, A, radius=50, label="α + β", color=COLORS['highlight']))
        
        parts.append(f'<text x="{300}" y="{380}" text-anchor="middle" font-weight="bold" fill="{COLORS["highlight"]}">Exterior = α + β</text>')

    elif mode == 'ex1_missing_angle':
        # 40, 80, x
        A = (250, 50)
        B = (100, 350)
        C = (500, 350)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        parts.append(draw_angle_arc(A, C, B, label="40°", color=COLORS['text']))
        parts.append(draw_angle_arc(B, A, C, label="80°", color=COLORS['text']))
        parts.append(draw_angle_arc(C, B, A, label="x = ?", color=COLORS['primary']))
        
        parts.append(f'<text x="{WIDTH/2}" y="{380}" text-anchor="middle" font-size="16" fill="{COLORS["primary"]}">180 - (40+80) = 60°</text>')

    elif mode == 'ex2_right_triangle':
        # Right triangle, one acute 30, solve other
        offset=50
        B = (150+offset, 350) # Right angle
        C = (450+offset, 350) 
        A = (150+offset, 150) # Short leg vertical?
        # Make a 30-60-90 approx
        # tan 30 = 1/sqrt(3) = 0.577. 
        # Base = 300. Height = 300 * tan(30) = 173.
        A = (150+offset, 350 - 173)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Right angle
        s=20
        parts.append(f'<rect x="{B[0]}" y="{B[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
        
        # Acute 30 at C
        parts.append(draw_angle_arc(C, B, A, radius=60, label="30°", color=COLORS['text']))
        
        # Unknown x at A
        parts.append(draw_angle_arc(A, C, B, radius=40, label="x", color=COLORS['primary']))
        
        parts.append(f'<text x="{150}" y="{100}" text-anchor="middle" font-size="16" fill="{COLORS["primary"]}">x = 90 - 30 = 60°</text>')

    elif mode == 'ex3_using_exterior':
        # Ext = 120. Int Opp = 70. Find other Int Opp.
        # Let C have ext 120. A is 70. B is x.
        C = (400, 300)
        B = (150, 300)
        # Line from B through C extends.
        ext_pt = (550, 300)
        
        # Angle C needs to be 60 internal (supp of 120).
        # Angle A needs to be 50? (120 = 70 + 50)
        # C is at (400,300). B at (150,300). Base length 250.
        # C angle is 60.
        # A_x = C_x - d * cos(60)
        # A_y = C_y - d * sin(60)
        # Also angle B needs to be the unknown x=50.
        # Intersection calculation... or just approx for visual.
        
        # Visual approx:
        A = (300, 100) # Just a point up top
        
        # Draw extended base
        parts.append(draw_segment(B, ext_pt, color=COLORS['grid'], width=2))
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Labels
        # Ext angle at C
        parts.append(draw_angle_arc(C, ext_pt, A, radius=40, label="120°", color=COLORS['highlight']))
        
        # Int A
        parts.append(draw_angle_arc(A, C, B, radius=40, label="70°", color=COLORS['text']))
        
        # Int B (unknown)
        parts.append(draw_angle_arc(B, A, C, radius=40, label="x", color=COLORS['primary']))
        
        parts.append(f'<text x="{WIDTH/2}" y="{380}" text-anchor="middle" font-size="16" fill="{COLORS["primary"]}">120 = 70 + x  →  x = 50°</text>')

    # ---------------- RECTAS NOTABLES (LINES ONLY) ----------------

    elif mode == 'median':
        # Median from A to midpoint of BC
        A = (300, 50)
        B = (100, 350)
        C = (500, 350)
        
        mid_BC = ((B[0]+C[0])/2, (B[1]+C[1])/2)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Draw Median
        parts.append(draw_segment(A, mid_BC, color=COLORS['primary'], width=4))
        parts.append(draw_point(mid_BC[0], mid_BC[1], label="M (Punto Medio)", color=COLORS['primary'], label_offset=(0, 20)))
        
        # Ticks on BC to show BM = MC
        parts.append(draw_tick_marks(B, mid_BC, count=2, color=COLORS['text']))
        parts.append(draw_tick_marks(mid_BC, C, count=2, color=COLORS['text']))
        
        parts.append(f'<text x="{300}" y="{30}" text-anchor="middle" font-size="24" font-weight="bold" fill="{COLORS["primary"]}">Mediana</text>')

    elif mode == 'altitude':
        # Altitude from A to BC (perpendicular)
        A = (200, 50)
        B = (100, 350)
        C = (500, 350)
        
        # Project A onto BC. Since BC is horizontal, it is (A[0], B[1])
        H = (200, 350)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Draw Altitude
        parts.append(draw_segment(A, H, color=COLORS['highlight'], width=4))
        
        # Right angle mark
        s=25
        parts.append(f'<rect x="{H[0]}" y="{H[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{H[0]+s/2}" cy="{H[1]-s/2}" r="2" fill="{COLORS["highlight"]}"/>')
        
        parts.append(f'<text x="{H[0]}" y="{H[1]+30}" text-anchor="middle" font-weight="bold" fill="{COLORS["highlight"]}">90°</text>')
        parts.append(f'<text x="{200}" y="{30}" text-anchor="middle" font-size="24" font-weight="bold" fill="{COLORS["highlight"]}">Altura</text>')

    elif mode == 'bisector':
        # Angle bisector of A
        # Let's use an isosceles for easy bisector calc, or calculate properly.
        # A at top center (300, 50).
        A = (300, 50)
        B = (100, 350)
        C = (400, 350) # Not isosceles, so bisector != median
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Calculate bisector direction
        # Vector AB
        vAB = (B[0]-A[0], B[1]-A[1])
        lenAB = math.hypot(vAB[0], vAB[1])
        uAB = (vAB[0]/lenAB, vAB[1]/lenAB)
        
        # Vector AC
        vAC = (C[0]-A[0], C[1]-A[1])
        lenAC = math.hypot(vAC[0], vAC[1])
        uAC = (vAC[0]/lenAC, vAC[1]/lenAC)
        
        # Bisector vector = uAB + uAC
        vBis = (uAB[0]+uAC[0], uAB[1]+uAC[1])
        lenBis = math.hypot(vBis[0], vBis[1])
        uBis = (vBis[0]/lenBis, vBis[1]/lenBis)
        
        # Find intersection with BC (y=350)
        # Line: P(t) = A + t * uBis
        # Py(t) = Ay + t * uBis_y = 350
        # t = (350 - Ay) / uBis_y
        t = (350 - A[1]) / uBis[1]
        D = (A[0] + t * uBis[0], 350)
        
        # Draw Bisector
        parts.append(draw_segment(A, D, color=COLORS['secondary'], width=4))
        
        # Angle marks
        # We need two small arcs with marks
        parts.append(draw_angle_arc(A, D, B, radius=50, label="α", color=COLORS['secondary']))
        parts.append(draw_angle_arc(A, C, D, radius=60, label="α", color=COLORS['secondary'])) # Slightly larger radius to separate
        
        parts.append(f'<text x="{300}" y="{30}" text-anchor="middle" font-size="24" font-weight="bold" fill="{COLORS["secondary"]}">Bisectriz</text>')

    elif mode == 'perpendicular_bisector':
        # Mediatriz of BC
        # Does NOT have to pass through A.
        # Let's make a scalene triangle where A is clearly offset.
        A = (200, 80)
        B = (100, 350)
        C = (500, 350)
        
        mid_BC = ((B[0]+C[0])/2, (B[1]+C[1])/2) # (300, 350)
        
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="4" stroke-linejoin="round"/>')
        
        # Draw Perpendicular Bisector (Vertical line at 300)
        top_P = (300, 50)
        bot_P = (300, 380)
        parts.append(draw_segment(top_P, bot_P, color=COLORS['success'], width=4))
        
        # Mark 90 deg
        s = 25
        H = mid_BC
        parts.append(f'<rect x="{H[0]}" y="{H[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["success"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{H[0]+s/2}" cy="{H[1]-s/2}" r="2" fill="{COLORS["success"]}"/>')
        
        # Ticks for Equality (BM = MC)
        parts.append(draw_tick_marks(B, mid_BC, count=3, color=COLORS['text']))
        parts.append(draw_tick_marks(mid_BC, C, count=3, color=COLORS['text']))
        
        # Note
        parts.append(f'<text x="{300}" y="{30}" text-anchor="middle" font-size="24" font-weight="bold" fill="{COLORS["success"]}">Mediatriz</text>')
        parts.append(f'<text x="{450}" y="{150}" text-anchor="middle" font-size="14" fill="{COLORS["text_light"]}">¡No toca el vértice A!</text>')
        parts.append(draw_segment(A, (300, 80), color=COLORS['text_light'], width=1, label="Desvío", label_offset=(0, -5)))

    elif mode == 'summary_lines':
        # 2x2 Grid Summary
        # Q1: Mediana | Q2: Altura
        # Q3: Bisectriz | Q4: Mediatriz
        
        # Quadrant centers
        cx1, cy1 = WIDTH * 0.25, HEIGHT * 0.25
        cx2, cy2 = WIDTH * 0.75, HEIGHT * 0.25
        cx3, cy3 = WIDTH * 0.25, HEIGHT * 0.75
        cx4, cy4 = WIDTH * 0.75, HEIGHT * 0.75
        
        # Mini triangle standard size
        w, h = 120, 100
        
        # Helper to draw mini triangle at center (cx, cy)
        def draw_mini_tri(cx, cy, type):
            svg = ""
            # Base bottom y = cy + h/2. Top y = cy - h/2
            A = (cx, cy - h/2)
            B = (cx - w/2, cy + h/2)
            C = (cx + w/2, cy + h/2)
            
            # Special adjustments for types
            if type == "alt":
                # Make A offset so altitude is clear
                A = (cx - 20, cy - h/2)
            elif type == "med_perp":
                A = (cx - 30, cy - h/2) # Offset A to show missed vertex
            
            svg += f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="2" stroke-linejoin="round"/>'
            
            mid = ((B[0]+C[0])/2, (B[1]+C[1])/2)
            
            if type == "med":
                # Mediana: Vert -> Mid + Ticks
                svg += f'<line x1="{A[0]}" y1="{A[1]}" x2="{mid[0]}" y2="{mid[1]}" stroke="{COLORS["primary"]}" stroke-width="3"/>'
                svg += draw_tick_marks(B, mid, 1, 6, 2, COLORS['primary'])
                svg += draw_tick_marks(mid, C, 1, 6, 2, COLORS['primary'])
                svg += f'<text x="{cx}" y="{cy + h/2 + 20}" text-anchor="middle" font-weight="bold" font-size="14" fill="{COLORS["primary"]}">Mediana</text>'
                svg += f'<text x="{cx}" y="{cy + h/2 + 35}" text-anchor="middle" font-size="10" fill="{COLORS["text_light"]}">Parte el Lado</text>'

            elif type == "alt":
                # Altura: Vert -> Perp
                H = (A[0], B[1])
                svg += f'<line x1="{A[0]}" y1="{A[1]}" x2="{H[0]}" y2="{H[1]}" stroke="{COLORS["highlight"]}" stroke-width="3"/>'
                # Square
                s = 10
                svg += f'<rect x="{H[0]}" y="{H[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="1.5"/>'
                svg += f'<text x="{cx}" y="{cy + h/2 + 20}" text-anchor="middle" font-weight="bold" font-size="14" fill="{COLORS["highlight"]}">Altura</text>'
                svg += f'<text x="{cx}" y="{cy + h/2 + 35}" text-anchor="middle" font-size="10" fill="{COLORS["text_light"]}">Cae a 90°</text>'

            elif type == "bis":
                # Bisectriz: Vert -> Angle split
                # Just draw visual split
                D = (cx, cy + h/2)
                svg += f'<line x1="{A[0]}" y1="{A[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{COLORS["secondary"]}" stroke-width="3"/>'
                # Arcs
                rad = 20
                svg += f'<path d="M {A[0]-rad*0.3} {A[1]+rad} A {rad} {rad} 0 0 1 {A[0]+rad*0.3} {A[1]+rad}" fill="none" stroke="{COLORS["secondary"]}" stroke-width="1.5"/>'
                svg += f'<text x="{cx}" y="{cy + h/2 + 20}" text-anchor="middle" font-weight="bold" font-size="14" fill="{COLORS["secondary"]}">Bisectriz</text>'
                svg += f'<text x="{cx}" y="{cy + h/2 + 35}" text-anchor="middle" font-size="10" fill="{COLORS["text_light"]}">Parte el Ángulo</text>'

            elif type == "med_perp":
                # Mediatriz: Mid -> Up (90) + Ticks + No Vert
                top = (mid[0], cy - h/2 - 10)
                bot = (mid[0], cy + h/2 + 10)
                svg += f'<line x1="{top[0]}" y1="{top[1]}" x2="{bot[0]}" y2="{bot[1]}" stroke="{COLORS["success"]}" stroke-width="3"/>'
                # Square
                s = 10
                svg += f'<rect x="{mid[0]}" y="{mid[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["success"]}" stroke-width="1.5"/>'
                # Ticks
                svg += draw_tick_marks(B, mid, 2, 6, 2, COLORS['success'])
                svg += draw_tick_marks(mid, C, 2, 6, 2, COLORS['success'])
                svg += f'<text x="{cx}" y="{cy + h/2 + 20}" text-anchor="middle" font-weight="bold" font-size="14" fill="{COLORS["success"]}">Mediatriz</text>'
                svg += f'<text x="{cx}" y="{cy + h/2 + 35}" text-anchor="middle" font-size="10" fill="{COLORS["text_light"]}">90° en medio</text>'

            return svg

        parts.append(draw_mini_tri(cx1, cy1, "med"))
        parts.append(draw_mini_tri(cx2, cy1, "alt"))
        parts.append(draw_mini_tri(cx3, cy3, "bis"))
        parts.append(draw_mini_tri(cx4, cy3, "med_perp"))
        
        # Dividers
        parts.append(f'<line x1="{WIDTH/2}" y1="20" x2="{WIDTH/2}" y2="{HEIGHT-20}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="4"/>')
        parts.append(f'<line x1="20" y1="{HEIGHT/2}" x2="{WIDTH-20}" y2="{HEIGHT/2}" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="4"/>')

    elif mode == 'perpendicular_bisector_equidistance':
        # Illustration of the property: Any point on Mediatriz is equidistant from endpoints
        
        # Base segment BC
        B = (150, 350)
        C = (450, 350)
        mid_BC = ((B[0]+C[0])/2, (B[1]+C[1])/2) # (300, 350)
        
        # Mediatriz line (Vertical)
        top_line = (300, 70)
        bot_line = (300, 380)
        
        # 1. Draw Base BC (Black, strong)
        parts.append(draw_segment(B, C, width=4, color=COLORS['text']))
        
        # 2. Label B and C at their positions
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-20, 20)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(20, 20)))
        
        # 3. Draw Mediatriz (Green, dashed)
        parts.append(f'<line x1="{top_line[0]}" y1="{top_line[1]}" x2="{bot_line[0]}" y2="{bot_line[1]}" stroke="{COLORS["success"]}" stroke-width="3" stroke-dasharray="8"/>')
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-weight="bold" fill="{COLORS["success"]}">Mediatriz</text>')
        
        # 4. Pick a point P on the mediatriz - MAKE IT VERY VISIBLE
        P = (300, 140)
        # Highlight ring around P
        parts.append(f'<circle cx="{P[0]}" cy="{P[1]}" r="16" fill="{COLORS["success"]}" fill-opacity="0.2" stroke="{COLORS["success"]}" stroke-width="2"/>')
        # Point P itself
        parts.append(f'<circle cx="{P[0]}" cy="{P[1]}" r="8" fill="{COLORS["success"]}"/>')
        # Label P to the side
        parts.append(f'<text x="{P[0]+30}" y="{P[1]+5}" font-weight="bold" font-size="16" fill="{COLORS["success"]}">P</text>')
        
        # 5. Draw connection segments PB and PC (Blue)
        parts.append(draw_segment(P, B, color=COLORS['primary'], width=3))
        parts.append(draw_segment(P, C, color=COLORS['primary'], width=3))
        
        # 6. Right angle mark
        s = 20
        H = mid_BC
        parts.append(f'<rect x="{H[0]}" y="{H[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["text"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{H[0]+s/2}" cy="{H[1]-s/2}" r="2" fill="{COLORS["text"]}"/>')

        # 7. Ticks on PB and PC to show equality
        parts.append(draw_tick_marks(P, B, count=2, color=COLORS['primary']))
        parts.append(draw_tick_marks(P, C, count=2, color=COLORS['primary']))
        
        # Title and explanation
        parts.append(f'<text x="{300}" y="{35}" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Propiedad de la Mediatriz</text>')
        parts.append(f'<text x="{300}" y="{55}" text-anchor="middle" font-size="14" fill="{COLORS["text_light"]}">Cualquier punto P sobre ella está a igual distancia de B y C</text>')

    # ---------------- PUNTOS NOTABLES ----------------
    
    # Helper functions for exact calculations
    def line_intersection(p1, p2, p3, p4):
        """Calculate intersection of line p1-p2 with line p3-p4"""
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if abs(denom) < 1e-10:
            return None  # Lines are parallel
        
        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
        
        px = x1 + t*(x2-x1)
        py = y1 + t*(y2-y1)
        return (px, py)
    
    def perpendicular_foot(P, A, B):
        """Calculate foot of perpendicular from P to line AB"""
        ax, ay = A
        bx, by = B
        px, py = P
        
        dx, dy = bx - ax, by - ay
        len_sq = dx*dx + dy*dy
        if len_sq < 1e-10:
            return A
        
        t = ((px - ax)*dx + (py - ay)*dy) / len_sq
        return (ax + t*dx, ay + t*dy)
    
    def perpendicular_point(P, A, B, dist=100):
        """Get a point on the perpendicular to AB through P"""
        ax, ay = A
        bx, by = B
        dx, dy = bx - ax, by - ay
        length = math.hypot(dx, dy)
        if length < 1e-10:
            return (P[0], P[1] + dist)
        # Normal vector
        nx, ny = -dy/length, dx/length
        return (P[0] + nx*dist, P[1] + ny*dist)

    if mode == 'barycenter':
        # Triangle with 3 medians intersecting at G (Barycenter)
        A = (300, 50)
        B = (100, 350)
        C = (500, 350)
        
        # Midpoints
        M_a = ((B[0]+C[0])/2, (B[1]+C[1])/2)
        M_b = ((A[0]+C[0])/2, (A[1]+C[1])/2)
        M_c = ((A[0]+B[0])/2, (A[1]+B[1])/2)
        
        # Barycenter G (exact formula)
        G = ((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3)
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # Medians (green)
        parts.append(draw_segment(A, M_a, color=COLORS['success'], width=2))
        parts.append(draw_segment(B, M_b, color=COLORS['success'], width=2))
        parts.append(draw_segment(C, M_c, color=COLORS['success'], width=2))
        
        # Midpoint markers
        parts.append(draw_point(M_a[0], M_a[1], color=COLORS['success']))
        parts.append(draw_point(M_b[0], M_b[1], color=COLORS['success']))
        parts.append(draw_point(M_c[0], M_c[1], color=COLORS['success']))
        
        # Barycenter G
        parts.append(f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="8" fill="{COLORS["highlight"]}"/>')
        parts.append(f'<text x="{G[0]+15:.2f}" y="{G[1]+5:.2f}" font-weight="bold" font-size="18" fill="{COLORS["highlight"]}">G</text>')
        
        # Labels
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Baricentro (Medianas)</text>')

    elif mode == 'orthocenter_acute':
        # Acute triangle with altitudes intersecting at H INSIDE
        # Use a clearly acute triangle
        A = (300, 60)
        B = (120, 340)
        C = (480, 340)
        
        # Calculate feet of altitudes
        H_a = perpendicular_foot(A, B, C)
        H_b = perpendicular_foot(B, A, C)
        H_c = perpendicular_foot(C, A, B)
        
        # Calculate orthocenter (intersection of two altitudes)
        # Altitude from A: line through A perpendicular to BC
        A_perp = perpendicular_point(A, B, C)
        # Altitude from B: line through B perpendicular to AC
        B_perp = perpendicular_point(B, A, C)
        
        H = line_intersection(A, H_a, B, H_b)
        if H is None:
            H = (300, 200)  # Fallback
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # Altitudes (orange)
        parts.append(draw_segment(A, H_a, color=COLORS['highlight'], width=2))
        parts.append(draw_segment(B, H_b, color=COLORS['highlight'], width=2))
        parts.append(draw_segment(C, H_c, color=COLORS['highlight'], width=2))
        
        # Right angle marks at feet
        for foot, side_start, side_end in [(H_a, B, C), (H_b, A, C), (H_c, A, B)]:
            # Draw right angle symbol
            dx, dy = side_end[0] - side_start[0], side_end[1] - side_start[1]
            length = math.hypot(dx, dy)
            if length > 0:
                ux, uy = dx/length, dy/length
                nx, ny = -uy, ux
                s = 12
                p1 = (foot[0] + ux*s, foot[1] + uy*s)
                p2 = (foot[0] + ux*s + nx*s, foot[1] + uy*s + ny*s)
                p3 = (foot[0] + nx*s, foot[1] + ny*s)
                parts.append(f'<path d="M {p1[0]:.2f} {p1[1]:.2f} L {p2[0]:.2f} {p2[1]:.2f} L {p3[0]:.2f} {p3[1]:.2f}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="1.5"/>')
        
        # Orthocenter H
        parts.append(f'<circle cx="{H[0]:.2f}" cy="{H[1]:.2f}" r="8" fill="{COLORS["highlight"]}"/>')
        parts.append(f'<text x="{H[0]+15:.2f}" y="{H[1]+5:.2f}" font-weight="bold" font-size="18" fill="{COLORS["highlight"]}">H</text>')
        
        # Labels
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Ortocentro DENTRO (Acutángulo)</text>')

    elif mode == 'orthocenter_right':
        # Right triangle with H at the right angle vertex
        B = (150, 340)  # Right angle vertex
        A = (150, 80)   # Top
        C = (500, 340)  # Right
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # Right angle mark at B
        s = 25
        parts.append(f'<rect x="{B[0]}" y="{B[1]-s}" width="{s}" height="{s}" fill="none" stroke="{COLORS["text"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{B[0]+s/2}" cy="{B[1]-s/2}" r="2" fill="{COLORS["text"]}"/>')
        
        # Altitudes (the legs are altitudes, plus one more)
        parts.append(draw_segment(A, B, color=COLORS['highlight'], width=3))
        parts.append(draw_segment(C, B, color=COLORS['highlight'], width=3))
        
        # Altitude from B to AC
        H_b = perpendicular_foot(B, A, C)
        parts.append(draw_segment(B, H_b, color=COLORS['highlight'], width=2))
        
        # Orthocenter H = B
        parts.append(f'<circle cx="{B[0]}" cy="{B[1]}" r="12" fill="{COLORS["highlight"]}" fill-opacity="0.3" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
        parts.append(f'<text x="{B[0]-50}" y="{B[1]+5}" font-weight="bold" font-size="16" fill="{COLORS["highlight"]}">H = B</text>')
        
        # Labels
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(-15, -15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Ortocentro EN VÉRTICE (Rectángulo)</text>')

    elif mode == 'orthocenter_obtuse':
        # Obtuse triangle with H OUTSIDE - using SymPy for exact calculation
        # ENHANCED with pedagogical elements
        from core.triangle_geometry import TriangleGeometry
        
        tri = TriangleGeometry((180, 250), (100, 350), (500, 350))
        A, B, C = tri.vertices
        H = tri.orthocenter
        feet = tri.altitude_feet
        H_a, H_b, H_c = feet['H_a'], feet['H_b'], feet['H_c']
        
        # === 1. EXTENDED SIDE LINES (dashed gray) to show where altitudes land ===
        # Extend BC beyond both ends
        parts.append(f'<line x1="{B[0]-60}" y1="{B[1]}" x2="{C[0]+50}" y2="{C[1]}" stroke="{COLORS["grid"]}" stroke-width="1.5" stroke-dasharray="6"/>')
        
        # Extend AC beyond A (upward)
        dx_ac = C[0] - A[0]
        dy_ac = C[1] - A[1]
        len_ac = math.hypot(dx_ac, dy_ac)
        ext_a_up = (A[0] - dx_ac/len_ac*80, A[1] - dy_ac/len_ac*80)
        parts.append(f'<line x1="{ext_a_up[0]:.2f}" y1="{ext_a_up[1]:.2f}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["grid"]}" stroke-width="1.5" stroke-dasharray="6"/>')
        
        # Extend AB beyond A (upward)
        dx_ab = B[0] - A[0]
        dy_ab = B[1] - A[1]
        len_ab = math.hypot(dx_ab, dy_ab)
        ext_a_up2 = (A[0] - dx_ab/len_ab*80, A[1] - dy_ab/len_ab*80)
        parts.append(f'<line x1="{ext_a_up2[0]:.2f}" y1="{ext_a_up2[1]:.2f}" x2="{B[0]}" y2="{B[1]}" stroke="{COLORS["grid"]}" stroke-width="1.5" stroke-dasharray="6"/>')
        
        # === 2. TRIANGLE (solid) ===
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # === 3. ALTITUDES - ALL THREE MUST EXTEND TO H ===
        
        # Altitude from A to BC (lands at H_a on BC, then extends UP to H)
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{H_a[0]:.2f}" y2="{H_a[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="2.5"/>')
        # Extension from A upward to H (dashed)
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{H[0]:.2f}" y2="{H[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="2" stroke-dasharray="8"/>')
        
        # Altitude from B to AC (lands at H_b, then extends to H)
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{H_b[0]:.2f}" y2="{H_b[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="2.5"/>')
        # Extension from H_b to H (dashed)
        parts.append(f'<line x1="{H_b[0]:.2f}" y1="{H_b[1]:.2f}" x2="{H[0]:.2f}" y2="{H[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="2" stroke-dasharray="8"/>')
        
        # Altitude from C to AB (lands at H_c, then extends to H)
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{H_c[0]:.2f}" y2="{H_c[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="2.5"/>')
        # Extension from H_c to H (dashed)
        parts.append(f'<line x1="{H_c[0]:.2f}" y1="{H_c[1]:.2f}" x2="{H[0]:.2f}" y2="{H[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="2" stroke-dasharray="8"/>')
        
        # === 4. RIGHT ANGLE MARKS at feet ===
        def draw_right_angle_mark(foot, p1, p2, size=12):
            """Draw right angle mark at foot on line p1-p2"""
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            length = math.hypot(dx, dy)
            if length < 1e-6:
                return ""
            ux, uy = dx/length, dy/length
            nx, ny = -uy, ux
            sq1 = (foot[0] + ux*size, foot[1] + uy*size)
            sq2 = (foot[0] + ux*size + nx*size, foot[1] + uy*size + ny*size)
            sq3 = (foot[0] + nx*size, foot[1] + ny*size)
            return f'<path d="M {sq1[0]:.2f} {sq1[1]:.2f} L {sq2[0]:.2f} {sq2[1]:.2f} L {sq3[0]:.2f} {sq3[1]:.2f}" fill="none" stroke="{COLORS["alturas"]}" stroke-width="1.5"/>'
        
        parts.append(draw_right_angle_mark(H_a, B, C, 12))
        parts.append(draw_right_angle_mark(H_b, A, C, 10))
        parts.append(draw_right_angle_mark(H_c, A, B, 10))
        
        # === 5. ORTHOCENTER H with "FUERA" label ===
        parts.append(f'<circle cx="{H[0]:.2f}" cy="{H[1]:.2f}" r="16" fill="{COLORS["punto_notable"]}" fill-opacity="0.15" stroke="{COLORS["punto_notable"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{H[0]:.2f}" cy="{H[1]:.2f}" r="8" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{H[0]+25:.2f}" y="{H[1]+5:.2f}" font-weight="bold" font-size="18" fill="{COLORS["punto_notable"]}">H</text>')
        parts.append(f'<text x="{H[0]+25:.2f}" y="{H[1]+22:.2f}" font-size="12" font-style="italic" fill="{COLORS["punto_notable"]}">(fuera)</text>')
        
        # === 6. VERTEX LABELS ===
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(5, -20)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-20, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        # === 7. TITLE ===
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Ortocentro FUERA (Triángulo Obtusángulo)</text>')

    elif mode == 'incenter':
        # Triangle with bisectors and inscribed circle
        A = (300, 50)
        B = (100, 350)
        C = (500, 350)
        
        # Side lengths
        a = math.hypot(C[0]-B[0], C[1]-B[1])
        b = math.hypot(A[0]-C[0], A[1]-C[1])
        c = math.hypot(B[0]-A[0], B[1]-A[1])
        
        # Incenter (exact formula)
        Ix = (a*A[0] + b*B[0] + c*C[0]) / (a+b+c)
        Iy = (a*A[1] + b*B[1] + c*C[1]) / (a+b+c)
        I = (Ix, Iy)
        
        # Inradius (exact formula)
        s = (a+b+c)/2
        area = abs((B[0]-A[0])*(C[1]-A[1]) - (C[0]-A[0])*(B[1]-A[1])) / 2
        r = area / s
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # Bisectors (purple)
        parts.append(draw_segment(A, I, color=COLORS['secondary'], width=2))
        parts.append(draw_segment(B, I, color=COLORS['secondary'], width=2))
        parts.append(draw_segment(C, I, color=COLORS['secondary'], width=2))
        
        # Inscribed circle
        parts.append(f'<circle cx="{I[0]:.2f}" cy="{I[1]:.2f}" r="{r:.2f}" fill="{COLORS["secondary"]}" fill-opacity="0.1" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
        
        # Incenter I
        parts.append(f'<circle cx="{I[0]:.2f}" cy="{I[1]:.2f}" r="8" fill="{COLORS["secondary"]}"/>')
        parts.append(f'<text x="{I[0]+15:.2f}" y="{I[1]-10:.2f}" font-weight="bold" font-size="18" fill="{COLORS["secondary"]}">I</text>')
        
        # Labels
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Incentro (Bisectrices) + Círculo Inscrito</text>')

    elif mode == 'circumcenter':
        # Triangle with perpendicular bisectors and circumscribed circle
        # Using SymPy for exact calculations
        from core.triangle_geometry import TriangleGeometry
        
        # Triangle adjusted and centered vertically in the 600x400 canvas
        # New coordinates: moved up to center the circle (O.y ≈ 200)
        tri = TriangleGeometry((300, 51), (160, 251), (440, 251))
        A, B, C = tri.vertices
        O = tri.circumcenter
        R = tri.circumradius
        mids = tri.midpoints
        M_a, M_b, M_c = mids['M_a'], mids['M_b'], mids['M_c']
        
        # === 1. Circumscribed circle ===
        # Centered at O(300, 200), R=149 -> y_min=51, y_max=349 (Centered!)
        parts.append(f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="{R:.2f}" fill="{COLORS["mediatrices"]}" fill-opacity="0.08" stroke="{COLORS["mediatrices"]}" stroke-width="2.5"/>')
        
        # === 2. Triangle ===
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # === 3. Perpendicular Bisectors (from O to midpoints) ===
        parts.append(draw_segment(O, M_a, color=COLORS['mediatrices'], width=2))
        parts.append(draw_segment(O, M_b, color=COLORS['mediatrices'], width=2))
        parts.append(draw_segment(O, M_c, color=COLORS['mediatrices'], width=2))
        
        # === 4. Right angle marks at midpoints ===
        def draw_right_angle_mark(mid, p1, p2, size=10):
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            length = math.hypot(dx, dy)
            if length < 1e-6:
                return ""
            ux, uy = dx/length, dy/length
            nx, ny = -uy, ux
            sq1 = (mid[0] + ux*size, mid[1] + uy*size)
            sq2 = (mid[0] + ux*size + nx*size, mid[1] + uy*size + ny*size)
            sq3 = (mid[0] + nx*size, mid[1] + ny*size)
            return f'<path d="M {sq1[0]:.2f} {sq1[1]:.2f} L {sq2[0]:.2f} {sq2[1]:.2f} L {sq3[0]:.2f} {sq3[1]:.2f}" fill="none" stroke="{COLORS["mediatrices"]}" stroke-width="1.5"/>'
        
        parts.append(draw_right_angle_mark(M_a, B, C, 10))
        parts.append(draw_right_angle_mark(M_b, A, C, 10))
        parts.append(draw_right_angle_mark(M_c, A, B, 10))
        
        # === 5. Midpoint markers ===
        parts.append(f'<circle cx="{M_a[0]}" cy="{M_a[1]}" r="4" fill="{COLORS["mediatrices"]}"/>')
        parts.append(f'<circle cx="{M_b[0]}" cy="{M_b[1]}" r="4" fill="{COLORS["mediatrices"]}"/>')
        parts.append(f'<circle cx="{M_c[0]}" cy="{M_c[1]}" r="4" fill="{COLORS["mediatrices"]}"/>')
        
        # === 6. Circumcenter O ===
        parts.append(f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="10" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{O[0]+15:.2f}" y="{O[1]+5:.2f}" font-weight="bold" font-size="18" fill="{COLORS["punto_notable"]}">O</text>')
        
        # === 7. Vertex Labels ===
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        # === 8. Title ===
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Circuncentro (Mediatrices) + Círculo Circunscrito</text>')

    elif mode == 'euler_line':
        # Triangle showing Euler Line with all three constructions
        # Medianas → G, Alturas → H, Mediatrices → O
        # Using SymPy for exact calculations
        from core.triangle_geometry import TriangleGeometry
        
        # Use a clearly scalene triangle for visible separation of points
        tri = TriangleGeometry((300, 60), (100, 340), (500, 340))
        A, B, C = tri.vertices
        
        # Get all notable points from SymPy
        mids = tri.midpoints
        M_a, M_b, M_c = mids['M_a'], mids['M_b'], mids['M_c']
        G = tri.barycenter
        H = tri.orthocenter
        O = tri.circumcenter
        feet = tri.altitude_feet
        H_a, H_b, H_c = feet['H_a'], feet['H_b'], feet['H_c']
        
        # === Draw constructions ===
        
        # Triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # 1. Medianas (green, dashed) → G
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{M_a[0]}" y2="{M_a[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{M_b[0]}" y2="{M_b[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{M_c[0]}" y2="{M_c[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        
        # 2. Alturas (orange, dashed) → H
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{H_a[0]:.2f}" y2="{H_a[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{H_b[0]:.2f}" y2="{H_b[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{H_c[0]:.2f}" y2="{H_c[1]:.2f}" stroke="{COLORS["alturas"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        
        # 3. Mediatrices (pink, dashed) → O
        # Draw from O to each midpoint
        parts.append(f'<line x1="{O[0]:.2f}" y1="{O[1]:.2f}" x2="{M_a[0]}" y2="{M_a[1]}" stroke="{COLORS["mediatrices"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{O[0]:.2f}" y1="{O[1]:.2f}" x2="{M_b[0]}" y2="{M_b[1]}" stroke="{COLORS["mediatrices"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{O[0]:.2f}" y1="{O[1]:.2f}" x2="{M_c[0]}" y2="{M_c[1]}" stroke="{COLORS["mediatrices"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        
        # === Euler Line (cyan, solid, prominent) ===
        euler_dx = H[0] - O[0]
        euler_dy = H[1] - O[1]
        euler_len = math.hypot(euler_dx, euler_dy)
        if euler_len > 0:
            euler_ux = euler_dx / euler_len
            euler_uy = euler_dy / euler_len
            # Extend beyond both ends for visibility
            line_start = (O[0] - euler_ux*100, O[1] - euler_uy*100)
            line_end = (H[0] + euler_ux*100, H[1] + euler_uy*100)
            parts.append(f'<line x1="{line_start[0]:.2f}" y1="{line_start[1]:.2f}" x2="{line_end[0]:.2f}" y2="{line_end[1]:.2f}" stroke="{COLORS["euler_line"]}" stroke-width="4"/>')
        
        # === Notable Points ===
        # O - Circumcenter (pink/mediatrices color)
        parts.append(f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="10" fill="{COLORS["mediatrices"]}"/>')
        parts.append(f'<text x="{O[0]+15:.2f}" y="{O[1]+5:.2f}" font-weight="bold" font-size="16" fill="{COLORS["mediatrices"]}">O</text>')
        
        # G - Barycenter (green/medianas color)
        parts.append(f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="10" fill="{COLORS["medianas"]}"/>')
        parts.append(f'<text x="{G[0]+15:.2f}" y="{G[1]+5:.2f}" font-weight="bold" font-size="16" fill="{COLORS["medianas"]}">G</text>')
        
        # H - Orthocenter (orange/alturas color)
        parts.append(f'<circle cx="{H[0]:.2f}" cy="{H[1]:.2f}" r="10" fill="{COLORS["alturas"]}"/>')
        parts.append(f'<text x="{H[0]+15:.2f}" y="{H[1]+5:.2f}" font-weight="bold" font-size="16" fill="{COLORS["alturas"]}">H</text>')
        
        # Vertex Labels
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["euler_line"]}">Recta de Euler: O, G, H alineados</text>')

    elif mode == 'barycenter_ratio':
        # Barycenter with 2:1 ratio illustration
        # Using SymPy for exact calculations
        from core.triangle_geometry import TriangleGeometry
        
        tri = TriangleGeometry((300, 60), (100, 340), (500, 340))
        A, B, C = tri.vertices
        G = tri.barycenter
        mids = tri.midpoints
        M_a = mids['M_a']  # Midpoint of BC (opposite to A)
        
        # === 1. Triangle ===
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # === 2. Just one median (A to M_a) to focus on the ratio ===
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{M_a[0]}" y2="{M_a[1]}" stroke="{COLORS["medianas"]}" stroke-width="3"/>')
        
        # === 3. Mark the two parts with different visual emphasis ===
        # Long part: A to G (2 parts)
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{G[0]:.2f}" y2="{G[1]:.2f}" stroke="{COLORS["primary"]}" stroke-width="5"/>')
        # Short part: G to M_a (1 part)
        parts.append(f'<line x1="{G[0]:.2f}" y1="{G[1]:.2f}" x2="{M_a[0]}" y2="{M_a[1]}" stroke="{COLORS["danger"]}" stroke-width="5"/>')
        
        # === 4. Labels for the parts ===
        # Calculate midpoints of each segment for labels
        mid_AG = ((A[0] + G[0])/2, (A[1] + G[1])/2)
        mid_GM = ((G[0] + M_a[0])/2, (G[1] + M_a[1])/2)
        
        # Label "2" for long part
        parts.append(f'<text x="{mid_AG[0]-25:.2f}" y="{mid_AG[1]:.2f}" font-size="20" font-weight="bold" fill="{COLORS["primary"]}">2</text>')
        # Label "1" for short part
        parts.append(f'<text x="{mid_GM[0]-20:.2f}" y="{mid_GM[1]:.2f}" font-size="20" font-weight="bold" fill="{COLORS["danger"]}">1</text>')
        
        # === 5. Points with labels ===
        # Barycenter G
        parts.append(f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="10" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{G[0]+15:.2f}" y="{G[1]+5:.2f}" font-weight="bold" font-size="18" fill="{COLORS["punto_notable"]}">G</text>')
        
        # Midpoint M
        parts.append(f'<circle cx="{M_a[0]}" cy="{M_a[1]}" r="6" fill="{COLORS["medianas"]}"/>')
        parts.append(f'<text x="{M_a[0]+12:.2f}" y="{M_a[1]+18:.2f}" font-weight="bold" font-size="16" fill="{COLORS["medianas"]}">M</text>')
        
        # === 6. Vertex labels ===
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        # === 7. Title ===
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Propiedad 2:1 del Baricentro</text>')

    elif mode == 'barycenter_ratio_all':
        # Shows the 2:1 property for ALL three medians
        from core.triangle_geometry import TriangleGeometry
        tri = TriangleGeometry((300, 50), (100, 350), (500, 350))
        A, B, C = tri.vertices
        G = tri.barycenter
        mids = tri.midpoints
        
        # Draw background triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # Helper to draw labeled median part with UNIFORM color scheme (Blue/Red)
        def draw_median_parts(V, M, offset_l, offset_s):
             # Draw thin guide line
             parts.append(f'<line x1="{V[0]}" y1="{V[1]}" x2="{M[0]}" y2="{M[1]}" stroke="{COLORS["medianas"]}" stroke-width="2" stroke-opacity="0.3"/>')
             
             # Highlight segments
             # Long (V-G) -> BLUE (Primary)
             parts.append(f'<line x1="{V[0]}" y1="{V[1]}" x2="{G[0]:.2f}" y2="{G[1]:.2f}" stroke="{COLORS["primary"]}" stroke-width="4"/>')
             # Short (G-M) -> RED (Danger)
             parts.append(f'<line x1="{G[0]:.2f}" y1="{G[1]:.2f}" x2="{M[0]}" y2="{M[1]}" stroke="{COLORS["danger"]}" stroke-width="4"/>')
             
             # Labels "2" and "1"
             mid_VG = ((V[0] + G[0])/2, (V[1] + G[1])/2)
             mid_GM = ((G[0] + M[0])/2, (G[1] + M[1])/2)
             
             # White background circles for readability
             parts.append(f'<circle cx="{mid_VG[0]+offset_l[0]:.2f}" cy="{mid_VG[1]+offset_l[1]-5:.2f}" r="8" fill="{COLORS["background"]}" fill-opacity="0.8"/>')
             parts.append(f'<text x="{mid_VG[0]+offset_l[0]:.2f}" y="{mid_VG[1]+offset_l[1]:.2f}" font-size="16" font-weight="bold" fill="{COLORS["primary"]}" text-anchor="middle">2</text>')
             
             parts.append(f'<circle cx="{mid_GM[0]+offset_s[0]:.2f}" cy="{mid_GM[1]+offset_s[1]-5:.2f}" r="8" fill="{COLORS["background"]}" fill-opacity="0.8"/>')
             parts.append(f'<text x="{mid_GM[0]+offset_s[0]:.2f}" y="{mid_GM[1]+offset_s[1]:.2f}" font-size="16" font-weight="bold" fill="{COLORS["danger"]}" text-anchor="middle">1</text>')

        # Draw for all 3 medians using the SAME logic
        draw_median_parts(A, mids['M_a'], (15, 5), (15, 5)) 
        draw_median_parts(B, mids['M_b'], (-10, -10), (0, 20)) 
        draw_median_parts(C, mids['M_c'], (10, -10), (-10, 20))
        
        # Draw G
        parts.append(f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="8" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{G[0]+12:.2f}" y="{G[1]-10:.2f}" font-weight="bold" font-size="16" fill="{COLORS["punto_notable"]}">G</text>')
        
        # Vertices
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Proporción 2:1 en todas las medianas</text>')

    elif mode == 'barycenter_areas':
        # Shows that medians divide the triangle into 6 equal areas
        # Using a Scalene Triangle to demonstrate generality
        from core.triangle_geometry import TriangleGeometry
        tri = TriangleGeometry((220, 50), (80, 320), (520, 280))
        A, B, C = tri.vertices
        G = tri.barycenter
        mids = tri.midpoints
        
        # Draw background triangle
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # Draw 3 Medians
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{mids["M_a"][0]}" y2="{mids["M_a"][1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{mids["M_b"][0]}" y2="{mids["M_b"][1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{mids["M_c"][0]}" y2="{mids["M_c"][1]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        
        # Mark the 6 areas
        # We need the centroid of each of the 6 small triangles to place the label
        # The 6 triangles are: GM_aC, GM_aB, GM_bA, GM_bC, GM_cA, GM_cB
        # Actually easier involves vertices: G-B-Ma, G-C-Ma, etc.
        
        def get_centroid(p1, p2, p3):
            return ((p1[0]+p2[0]+p3[0])/3, (p1[1]+p2[1]+p3[1])/3)
            
        # List of 6 triangles represented by their vertices (besides G)
        # Tri 1: G, B, M_a
        c1 = get_centroid(G, B, mids['M_a'])
        # Tri 2: G, C, M_a
        c2 = get_centroid(G, C, mids['M_a'])
        # Tri 3: G, C, M_b
        c3 = get_centroid(G, C, mids['M_b'])
        # Tri 4: G, A, M_b
        c4 = get_centroid(G, A, mids['M_b'])
        # Tri 5: G, A, M_c
        c5 = get_centroid(G, A, mids['M_c'])
        # Tri 6: G, B, M_c
        c6 = get_centroid(G, B, mids['M_c'])
        
        areas_centers = [c1, c2, c3, c4, c5, c6]
        
        for i, center in enumerate(areas_centers):
            parts.append(f'<text x="{center[0]:.2f}" y="{center[1]+5:.2f}" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["text"]}" font-style="italic">S</text>')
            
        # Draw G
        parts.append(f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="8" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{G[0]+12:.2f}" y="{G[1]-10:.2f}" font-weight="bold" font-size="16" fill="{COLORS["punto_notable"]}">G</text>')
        
        # Title
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">6 Áreas Iguales (S)</text>')

    elif mode == 'incenter_equidistant':
        # Incenter showing equal distance to all three sides
        # Using SymPy for exact calculations
        from core.triangle_geometry import TriangleGeometry
        
        tri = TriangleGeometry((300, 60), (100, 340), (500, 340))
        A, B, C = tri.vertices
        I = tri.incenter
        r = abs(tri.inradius)
        
        # Calculate perpendicular feet from I to each side
        from sympy import Point, Line
        I_point = Point(I[0], I[1])
        
        # Feet of perpendiculars from I to each side
        line_BC = Line(Point(B[0], B[1]), Point(C[0], C[1]))
        line_AC = Line(Point(A[0], A[1]), Point(C[0], C[1]))
        line_AB = Line(Point(A[0], A[1]), Point(B[0], B[1]))
        
        foot_BC = line_BC.projection(I_point)
        foot_AC = line_AC.projection(I_point)
        foot_AB = line_AB.projection(I_point)
        
        P1 = (float(foot_BC.x), float(foot_BC.y))
        P2 = (float(foot_AC.x), float(foot_AC.y))
        P3 = (float(foot_AB.x), float(foot_AB.y))
        
        print(f"DEBUG: Incenter I={I}, Inradius r={r}")
        
        # === 1. Triangle ===
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # === 1.5 Bisectors (The lines that define the Incenter) ===
        # Draw from Vertices to Incenter (Bisector segments)
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{I[0]:.2f}" y2="{I[1]:.2f}" stroke="{COLORS["bisectrices"]}" stroke-width="2.5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{I[0]:.2f}" y2="{I[1]:.2f}" stroke="{COLORS["bisectrices"]}" stroke-width="2.5"/>')
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{I[0]:.2f}" y2="{I[1]:.2f}" stroke="{COLORS["bisectrices"]}" stroke-width="2.5"/>')
        
        # (Inscribed circle moved to end)
        
        # === 3. Perpendicular lines from I to each side (radii to tangent points) ===
        # These show the "distance" property (radius)
        parts.append(f'<line x1="{I[0]:.2f}" y1="{I[1]:.2f}" x2="{P1[0]:.2f}" y2="{P1[1]:.2f}" stroke="{COLORS["danger"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{I[0]:.2f}" y1="{I[1]:.2f}" x2="{P2[0]:.2f}" y2="{P2[1]:.2f}" stroke="{COLORS["danger"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        parts.append(f'<line x1="{I[0]:.2f}" y1="{I[1]:.2f}" x2="{P3[0]:.2f}" y2="{P3[1]:.2f}" stroke="{COLORS["danger"]}" stroke-width="1.5" stroke-dasharray="4"/>')
        
        # === 4. Right angle marks at feet ===
        def draw_right_angle(foot, p1, p2, size=10):
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            length = math.hypot(dx, dy)
            if length < 1e-6:
                return ""
            ux, uy = dx/length, dy/length
            nx, ny = -uy, ux
            sq1 = (foot[0] + ux*size, foot[1] + uy*size)
            sq2 = (foot[0] + ux*size + nx*size, foot[1] + uy*size + ny*size)
            sq3 = (foot[0] + nx*size, foot[1] + ny*size)
            return f'<path d="M {sq1[0]:.2f} {sq1[1]:.2f} L {sq2[0]:.2f} {sq2[1]:.2f} L {sq3[0]:.2f} {sq3[1]:.2f}" fill="none" stroke="{COLORS["danger"]}" stroke-width="1.5"/>'
        
        parts.append(draw_right_angle(P1, B, C, 8))
        parts.append(draw_right_angle(P2, A, C, 8))
        parts.append(draw_right_angle(P3, A, B, 8))
        
        # === 5. Tangent point markers ===
        parts.append(f'<circle cx="{P1[0]:.2f}" cy="{P1[1]:.2f}" r="5" fill="{COLORS["danger"]}"/>')
        parts.append(f'<circle cx="{P2[0]:.2f}" cy="{P2[1]:.2f}" r="5" fill="{COLORS["danger"]}"/>')
        parts.append(f'<circle cx="{P3[0]:.2f}" cy="{P3[1]:.2f}" r="5" fill="{COLORS["danger"]}"/>')
        
        # === 6. Label "5" for each radius (Example) ===
        parts.append(f'<text x="{(I[0]+P1[0])/2+10:.2f}" y="{(I[1]+P1[1])/2:.2f}" font-size="16" font-weight="bold" fill="{COLORS["danger"]}">5</text>')
        parts.append(f'<text x="{(I[0]+P2[0])/2-20:.2f}" y="{(I[1]+P2[1])/2:.2f}" font-size="16" font-weight="bold" fill="{COLORS["danger"]}">5</text>')
        parts.append(f'<text x="{(I[0]+P3[0])/2-20:.2f}" y="{(I[1]+P3[1])/2-5:.2f}" font-size="16" font-weight="bold" fill="{COLORS["danger"]}">5</text>')
        
        # === 7. Incenter I ===
        parts.append(f'<circle cx="{I[0]:.2f}" cy="{I[1]:.2f}" r="10" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{I[0]+15:.2f}" y="{I[1]-10:.2f}" font-weight="bold" font-size="18" fill="{COLORS["punto_notable"]}">I</text>')
        
        # === 8. Vertex labels ===
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        # === 8. Inscribed circle (Moved to END to ensure visibility) ===
        # Increased opacity and stroke width
        parts.append(f'<circle cx="{I[0]:.2f}" cy="{I[1]:.2f}" r="{r:.2f}" fill="{COLORS["bisectrices"]}" fill-opacity="0.25" stroke="{COLORS["bisectrices"]}" stroke-width="3"/>')

        # === 9. Title ===
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Incentro: Equidistante de los 3 lados</text>')

    elif mode == 'summary_all_points':
        # 2x2 Grid Summary of all 4 points
        # RADICAL FIX: Titles at TOP, Smaller Geometry
        
        from core.triangle_geometry import TriangleGeometry
        
        # Much more compact base triangle to ensure circumcircle fits
        # Verified: With offset (300, 200), circle bottom at y=361 (38px margin)
        # A(150, 50), B(100, 130), C(200, 130) -> Height 80, Width 100
        base_tri_coords = [(150, 50), (100, 130), (200, 130)]
        
        def draw_mini_diagram(offset_x, offset_y, type_str, title, subtitle, color_theme):
            # Title at TOP of the cell
            svg_content = f'<text x="{offset_x+150}" y="{offset_y+30}" text-anchor="middle" font-size="14" font-weight="bold" fill="{color_theme}">{title}</text>'
            # Subtitle (Description)
            svg_content += f'<text x="{offset_x+150}" y="{offset_y+50}" text-anchor="middle" font-size="12" font-style="italic" fill="{COLORS["text"]}">{subtitle}</text>'
            
            # Create geometry for this specific offset
            t_verts = [(p[0]+offset_x, p[1]+offset_y) for p in base_tri_coords]
            tri = TriangleGeometry(t_verts[0], t_verts[1], t_verts[2])
            A, B, C = tri.vertices
            
            svg_content += ""
            
            # Draw Triangle
            svg_content += f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="2" stroke-linejoin="round"/>'
            
            # Specific Construction
            if type_str == 'medians':
                mids = tri.midpoints
                G = tri.barycenter
                svg_content += f'<line x1="{A[0]}" y1="{A[1]}" x2="{mids["M_a"][0]}" y2="{mids["M_a"][1]}" stroke="{color_theme}" stroke-width="1.5"/>'
                svg_content += f'<line x1="{B[0]}" y1="{B[1]}" x2="{mids["M_b"][0]}" y2="{mids["M_b"][1]}" stroke="{color_theme}" stroke-width="1.5"/>'
                svg_content += f'<line x1="{C[0]}" y1="{C[1]}" x2="{mids["M_c"][0]}" y2="{mids["M_c"][1]}" stroke="{color_theme}" stroke-width="1.5"/>'
                svg_content += f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="5" fill="{COLORS["punto_notable"]}"/>'
                svg_content += f'<text x="{G[0]+12:.2f}" y="{G[1]+5:.2f}" font-weight="bold" font-size="14" fill="{COLORS["punto_notable"]}">G</text>'

            elif type_str == 'altitudes':
                feet = tri.altitude_feet
                H = tri.orthocenter
                svg_content += f'<line x1="{A[0]}" y1="{A[1]}" x2="{feet["H_a"][0]:.2f}" y2="{feet["H_a"][1]:.2f}" stroke="{color_theme}" stroke-width="1.5"/>'
                svg_content += f'<line x1="{B[0]}" y1="{B[1]}" x2="{feet["H_b"][0]:.2f}" y2="{feet["H_b"][1]:.2f}" stroke="{color_theme}" stroke-width="1.5"/>'
                svg_content += f'<line x1="{C[0]}" y1="{C[1]}" x2="{feet["H_c"][0]:.2f}" y2="{feet["H_c"][1]:.2f}" stroke="{color_theme}" stroke-width="1.5"/>'
                svg_content += f'<circle cx="{H[0]:.2f}" cy="{H[1]:.2f}" r="5" fill="{COLORS["punto_notable"]}"/>'
                svg_content += f'<text x="{H[0]+12:.2f}" y="{H[1]+5:.2f}" font-weight="bold" font-size="14" fill="{COLORS["punto_notable"]}">H</text>'
                
            elif type_str == 'bisectors':
                I = tri.incenter
                svg_content += draw_segment(A, I, color=color_theme, width=1.5)
                svg_content += draw_segment(B, I, color=color_theme, width=1.5)
                svg_content += draw_segment(C, I, color=color_theme, width=1.5)
                svg_content += f'<circle cx="{I[0]:.2f}" cy="{I[1]:.2f}" r="{tri.inradius:.2f}" fill="{color_theme}" fill-opacity="0.1" stroke="{color_theme}" stroke-width="1"/>'
                svg_content += f'<circle cx="{I[0]:.2f}" cy="{I[1]:.2f}" r="5" fill="{COLORS["punto_notable"]}"/>'
                svg_content += f'<text x="{I[0]+12:.2f}" y="{I[1]+5:.2f}" font-weight="bold" font-size="14" fill="{COLORS["punto_notable"]}">I</text>'

            elif type_str == 'perpendicular_bisectors':
                O = tri.circumcenter
                mids = tri.midpoints
                svg_content += draw_segment(O, mids["M_a"], color=color_theme, width=1.5)
                svg_content += draw_segment(O, mids["M_b"], color=color_theme, width=1.5)
                svg_content += draw_segment(O, mids["M_c"], color=color_theme, width=1.5)
                # Ensure circumcircle doesn't get cut off. Reduced triangle size helps this.
                svg_content += f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="{tri.circumradius:.2f}" fill="{color_theme}" fill-opacity="0.1" stroke="{color_theme}" stroke-width="1"/>'
                svg_content += f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="5" fill="{COLORS["punto_notable"]}"/>'
                svg_content += f'<text x="{O[0]+12:.2f}" y="{O[1]+10:.2f}" font-weight="bold" font-size="14" fill="{COLORS["punto_notable"]}">O</text>'
            
            return svg_content
        
        # Top Left: Baricentro
        parts.append(draw_mini_diagram(0, 0, 'medians', 'Baricentro (Medianas)', 'Vértice → Punto Medio', COLORS['medianas']))
        
        # Top Right: Ortocentro
        parts.append(draw_mini_diagram(300, 0, 'altitudes', 'Ortocentro (Alturas)', '90° desde el Vértice', COLORS['alturas']))
        
        # Bottom Left: Incentro
        parts.append(draw_mini_diagram(0, 200, 'bisectors', 'Incentro (Bisectrices)', 'Divide ángulo en dos partes iguales', COLORS['bisectrices']))
        
        # Bottom Right: Circuncentro
        parts.append(draw_mini_diagram(300, 200, 'perpendicular_bisectors', 'Circuncentro (Mediatrices)', 'Perpendicular en punto medio', COLORS['mediatrices']))
        
        # Grid separator lines
        parts.append(f'<line x1="300" y1="20" x2="300" y2="380" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="4"/>')
        parts.append(f'<line x1="20" y1="200" x2="580" y2="200" stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="4"/>')

    elif mode == 'circumcenter_right':
        # Special case: Right triangle -> Circumcenter on hypotenuse midpoint
        from core.triangle_geometry import TriangleGeometry
        
        # Right triangle A=(100, 100), B=(100, 300), C=(400, 300)
        # Right angle at B
        tri = TriangleGeometry((100, 100), (100, 300), (400, 300))
        A, B, C = tri.vertices
        O = tri.circumcenter
        R = tri.circumradius
        mids = tri.midpoints
        
        # === 1. Triangle ===
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["background"]}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linejoin="round"/>')
        
        # === 2. Right Angle Mark at B ===
        parts.append(f'<rect x="{B[0]}" y="{B[1]-20}" width="20" height="20" fill="none" stroke="{COLORS["text"]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{B[0]+8}" cy="{B[1]-8}" r="2" fill="{COLORS["text"]}"/>')

        # === 3. Perpendicular Bisectors (Mediatrices) ===
        # Use full lines or segments from midpoints to O
        parts.append(f'<line x1="{mids["M_a"][0]:.2f}" y1="{mids["M_a"][1]:.2f}" x2="{O[0]:.2f}" y2="{O[1]:.2f}" stroke="{COLORS["mediatrices"]}" stroke-width="2" stroke-dasharray="6"/>') # From side BC
        parts.append(f'<line x1="{mids["M_c"][0]:.2f}" y1="{mids["M_c"][1]:.2f}" x2="{O[0]:.2f}" y2="{O[1]:.2f}" stroke="{COLORS["mediatrices"]}" stroke-width="2" stroke-dasharray="6"/>') # From side AB
        
        # Hypotenuse bisector is just a perpendicular line through O
        # AC vector dx=300, dy=200 -> slope 2/3. Perp slope -1.5. Direction (2, -3)
        # Draw a segment of length 140 centered at O
        # Vector (20, -30) scaled
        dx, dy = 100, -150  # Direction vector roughly perpendicular to AC (300, 200) -> dot product 300*100 + 200*-150 = 30000 - 30000 = 0.
        # Start and End points relative to O
        parts.append(f'<line x1="{O[0]-dx/2:.2f}" y1="{O[1]-dy/2:.2f}" x2="{O[0]+dx/2:.2f}" y2="{O[1]+dy/2:.2f}" stroke="{COLORS["mediatrices"]}" stroke-width="2" stroke-dasharray="6"/>')
        
        # Mark right angle at hypotenuse mediatriz
        # A bit tricky to align, let's skip the tiny square on the diagonal mediatriz to avoid clutter, 
        # as the dashed line itself clearly indicates the geometry.
        
        # === 4. Circumscribed Circle ===
        parts.append(f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="{R:.2f}" fill="{COLORS["mediatrices"]}" fill-opacity="0.1" stroke="{COLORS["mediatrices"]}" stroke-width="2"/>')
        
        # === 5. Midpoints Markers ===
        parts.append(f'<circle cx="{mids["M_a"][0]:.2f}" cy="{mids["M_a"][1]:.2f}" r="4" fill="{COLORS["mediatrices"]}"/>') # Bottom
        parts.append(f'<circle cx="{mids["M_c"][0]:.2f}" cy="{mids["M_c"][1]:.2f}" r="4" fill="{COLORS["mediatrices"]}"/>') # Left
        
        # === 6. Circumcenter O ===
        parts.append(f'<circle cx="{O[0]:.2f}" cy="{O[1]:.2f}" r="8" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{O[0]+15:.2f}" y="{O[1]-15:.2f}" font-weight="bold" font-size="18" fill="{COLORS["punto_notable"]}">O</text>')
        
        # === 7. Vertices ===
        parts.append(draw_point(A[0], A[1], label="A", color=COLORS['text'], label_offset=(0, -15)))
        parts.append(draw_point(B[0], B[1], label="B", color=COLORS['text'], label_offset=(-15, 15)))
        parts.append(draw_point(C[0], C[1], label="C", color=COLORS['text'], label_offset=(15, 15)))
        
        # === 8. Title ===
        parts.append(f'<text x="{300}" y="{390}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Circuncentro en el punto medio de la hipotenusa</text>')

    elif mode == 'barycenter_coordinates':
        # Cartesian plane with triangle and barycenter formula visualization
        # Canvas: 600x400, Origin at (80, 320), Scale: 60 px per unit
        
        origin_x, origin_y = 80, 320
        scale = 50  # pixels per unit
        
        # Helper functions
        def to_canvas(x, y):
            return (origin_x + x * scale, origin_y - y * scale)
        
        # Triangle vertices with nice integer coordinates
        # A(1, 5), B(2, 1), C(7, 3)
        A_coord = (1, 5)
        B_coord = (2, 1)
        C_coord = (7, 3)
        
        # Calculate barycenter G = ((x1+x2+x3)/3, (y1+y2+y3)/3)
        G_x = (A_coord[0] + B_coord[0] + C_coord[0]) / 3  # (1+2+7)/3 = 10/3 ≈ 3.33
        G_y = (A_coord[1] + B_coord[1] + C_coord[1]) / 3  # (5+1+3)/3 = 9/3 = 3
        G_coord = (G_x, G_y)
        
        A = to_canvas(*A_coord)
        B = to_canvas(*B_coord)
        C = to_canvas(*C_coord)
        G = to_canvas(*G_coord)
        
        # === 1. GRID ===
        # Vertical lines (x = 0 to 9)
        for i in range(10):
            x = origin_x + i * scale
            opacity = "0.3" if i > 0 else "1"
            width = "1" if i > 0 else "2"
            parts.append(f'<line x1="{x}" y1="40" x2="{x}" y2="{origin_y+20}" stroke="{COLORS["grid"]}" stroke-width="{width}" stroke-opacity="{opacity}"/>')
            if i > 0:
                parts.append(f'<text x="{x}" y="{origin_y+35}" text-anchor="middle" font-size="12" fill="{COLORS["text"]}">{i}</text>')
        
        # Horizontal lines (y = 0 to 6)
        for i in range(7):
            y = origin_y - i * scale
            opacity = "0.3" if i > 0 else "1"
            width = "1" if i > 0 else "2"
            parts.append(f'<line x1="{origin_x-20}" y1="{y}" x2="580" y2="{y}" stroke="{COLORS["grid"]}" stroke-width="{width}" stroke-opacity="{opacity}"/>')
            if i > 0:
                parts.append(f'<text x="{origin_x-30}" y="{y+4}" text-anchor="middle" font-size="12" fill="{COLORS["text"]}">{i}</text>')
        
        # Axis labels
        parts.append(f'<text x="570" y="{origin_y+35}" font-size="14" font-weight="bold" fill="{COLORS["text"]}">x</text>')
        parts.append(f'<text x="{origin_x-30}" y="50" font-size="14" font-weight="bold" fill="{COLORS["text"]}">y</text>')
        
        # Origin label
        parts.append(f'<text x="{origin_x-20}" y="{origin_y+35}" font-size="12" fill="{COLORS["text"]}">0</text>')
        
        # === 2. TRIANGLE ===
        parts.append(f'<path d="M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z" fill="{COLORS["medianas"]}" fill-opacity="0.1" stroke="{COLORS["line"]}" stroke-width="2.5" stroke-linejoin="round"/>')
        
        # === 3. MEDIANS (dashed, leading to G) ===
        M_a = to_canvas((B_coord[0]+C_coord[0])/2, (B_coord[1]+C_coord[1])/2)
        M_b = to_canvas((A_coord[0]+C_coord[0])/2, (A_coord[1]+C_coord[1])/2)
        M_c = to_canvas((A_coord[0]+B_coord[0])/2, (A_coord[1]+B_coord[1])/2)
        
        parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{M_a[0]}" y2="{M_a[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="5"/>')
        parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{M_b[0]}" y2="{M_b[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="5"/>')
        parts.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{M_c[0]}" y2="{M_c[1]}" stroke="{COLORS["medianas"]}" stroke-width="1.5" stroke-dasharray="5"/>')
        
        # === 4. VERTICES with coordinate labels ===
        # A
        parts.append(f'<circle cx="{A[0]}" cy="{A[1]}" r="6" fill="{COLORS["primary"]}"/>')
        parts.append(f'<text x="{A[0]-5}" y="{A[1]-15}" font-weight="bold" font-size="14" fill="{COLORS["primary"]}">A({A_coord[0]}, {A_coord[1]})</text>')
        
        # B
        parts.append(f'<circle cx="{B[0]}" cy="{B[1]}" r="6" fill="{COLORS["primary"]}"/>')
        parts.append(f'<text x="{B[0]-45}" y="{B[1]+20}" font-weight="bold" font-size="14" fill="{COLORS["primary"]}">B({B_coord[0]}, {B_coord[1]})</text>')
        
        # C
        parts.append(f'<circle cx="{C[0]}" cy="{C[1]}" r="6" fill="{COLORS["primary"]}"/>')
        parts.append(f'<text x="{C[0]+10}" y="{C[1]+20}" font-weight="bold" font-size="14" fill="{COLORS["primary"]}">C({C_coord[0]}, {C_coord[1]})</text>')
        
        # === 5. BARYCENTER G with calculation ===
        parts.append(f'<circle cx="{G[0]:.2f}" cy="{G[1]:.2f}" r="10" fill="{COLORS["punto_notable"]}"/>')
        parts.append(f'<text x="{G[0]+15:.2f}" y="{G[1]-10:.2f}" font-weight="bold" font-size="16" fill="{COLORS["punto_notable"]}">G</text>')
        
        # === 6. CALCULATION BOX (formula with values) ===
        box_x, box_y = 350, 40
        # Background box
        parts.append(f'<rect x="{box_x}" y="{box_y}" width="230" height="90" rx="8" fill="{COLORS["background"]}" stroke="{COLORS["medianas"]}" stroke-width="2"/>')
        
        # Formula lines
        parts.append(f'<text x="{box_x+115}" y="{box_y+25}" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["medianas"]}">Cálculo del Baricentro</text>')
        parts.append(f'<text x="{box_x+10}" y="{box_y+50}" font-size="12" fill="{COLORS["text"]}">x = (1 + 2 + 7) / 3 = 10/3 ≈ 3.33</text>')
        parts.append(f'<text x="{box_x+10}" y="{box_y+75}" font-size="12" fill="{COLORS["text"]}">y = (5 + 1 + 3) / 3 = 9/3 = 3</text>')
        
        # Result
        parts.append(f'<text x="{G[0]+15:.2f}" y="{G[1]+20:.2f}" font-size="12" fill="{COLORS["punto_notable"]}">({G_x:.2f}, {G_y:.0f})</text>')

    parts.append('</svg>')
    
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text('\n'.join(parts))
    print(f"✅ Generated {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode', required=True)
    args = parser.parse_args()
    
    generate_svg_main(args.mode, args.output)

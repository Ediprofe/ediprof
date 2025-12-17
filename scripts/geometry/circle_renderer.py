#!/usr/bin/env python3
"""
⭕ Circle Renderer - Ilustraciones de Circunferencia y Círculo (v2.0)

REGLAS DE RIGUROSIDAD:
1. TODAS las coordenadas se calculan matemáticamente
2. TODO el texto debe ser 100% visible (no cortado)
3. Sector ≠ Segmento (verificación visual obligatoria)
4. Cada concepto = 1 ilustración separada

Tipos disponibles:
    # === BÁSICOS ===
    basic              - Circunferencia con centro y radio
    
    # === ELEMENTOS (uno por concepto) ===
    element_radius     - Solo el radio
    element_diameter   - Solo el diámetro
    element_chord      - Solo la cuerda
    element_arc        - Solo el arco
    element_sector     - Solo el sector circular (2 radios + arco)
    element_segment    - Solo el segmento circular (cuerda + arco)
    element_crown      - Corona circular
    
    # === POSICIONES ===
    point_positions    - Punto interior/sobre/exterior
    tangent_secant     - Recta tangente y secante
    circle_positions   - Posiciones entre dos circunferencias
    
    # === ÁNGULOS (uno por tipo) ===
    angle_central      - Ángulo central
    angle_inscribed    - Ángulo inscrito
    angle_semi_inscribed - Ángulo semi-inscrito
    angle_interior     - Ángulo interior
    angle_exterior     - Ángulo exterior
    
    # === TEOREMAS ===
    theorem_inscribed  - Teorema: inscrito = ½ central
    theorem_tales      - Teorema de Tales (semicircunferencia)
    
    # === FÓRMULAS ===
    formula_length     - Longitud L = 2πr
    formula_area       - Área A = πr²
    formula_sector_area - Área del sector
    formula_segment_area - Área del segmento
"""

import argparse
import math
from pathlib import Path

# ==============================================================================
# ESTÁNDARES DE TAMAÑO (Documentado en CLAUDE.md)
# ==============================================================================
# Todos los SVGs del mismo tema deben tener tamaños consistentes.

SIZE_SIMPLE = (500, 400)       # 1 concepto: radio, diámetro, cuerda, arco, ángulo
SIZE_COMPOUND = (600, 460)     # 2-3 elementos: sector+triángulo, teoremas (altura aumentada para leyendas)
SIZE_MULTIPLE = (750, 450)     # 4+ elementos: posiciones, comparaciones
SIZE_HORIZONTAL = (750, 420)   # Operaciones A - B = C, lado a lado (más espacio)

# Paleta de colores
COLORS = {
    'background': '#f8fafc',
    'circle_stroke': '#3b82f6',
    'circle_fill': '#dbeafe',
    'radius': '#ef4444',
    'diameter': '#8b5cf6',
    'chord': '#22c55e',
    'arc': '#f97316',
    'sector_fill': '#fef3c7',
    'segment_fill': '#dcfce7',
    'tangent': '#ec4899',
    'secant': '#14b8a6',
    'angle': '#f97316',
    'point': '#1e293b',
    'center': '#ef4444',
    'text': '#1e293b',
    'auxiliary': '#94a3b8',
    'highlight': '#fbbf24',
    'crown': '#e0e7ff',
}


def escape_svg_text(text):
    """
    ⚠️ CRÍTICO: Escapar caracteres especiales XML para texto en SVG.
    
    Los caracteres <, >, & son inválidos en XML y causan errores de parsing.
    SIEMPRE usar esta función para texto que contenga símbolos matemáticos.
    
    Ejemplos:
        "d < r"  → "d &lt; r"
        "d > R"  → "d &gt; R"
        "A & B"  → "A &amp; B"
    """
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def point_on_circle(cx, cy, r, angle_deg):
    """Calcula punto en la circunferencia dado ángulo en grados.
    NOTA: En SVG, Y crece hacia abajo, por eso usamos -sin()
    """
    angle_rad = math.radians(angle_deg)
    return (cx + r * math.cos(angle_rad), cy - r * math.sin(angle_rad))


def arc_path(cx, cy, r, start_deg, end_deg):
    """Genera path SVG para un arco."""
    start = point_on_circle(cx, cy, r, start_deg)
    end = point_on_circle(cx, cy, r, end_deg)
    
    # Determinar si es arco grande (>180°)
    arc_span = (end_deg - start_deg) % 360
    large_arc = 1 if arc_span > 180 else 0
    
    # sweep-flag: 0 para sentido antihorario en coordenadas matemáticas
    # Pero en SVG (Y invertido), queremos 0 para ir de start a end en sentido horario visual
    sweep = 0
    
    return f"M {start[0]:.2f} {start[1]:.2f} A {r} {r} 0 {large_arc} {sweep} {end[0]:.2f} {end[1]:.2f}"


def get_angle_arc_svg(vertex, point1, point2, radius=30):
    """
    🎯 FUNCIÓN CORRECTA para generar arcos de ángulos.
    
    Genera el path SVG para un arco de ángulo usando las POSICIONES REALES
    de los puntos, no ángulos abstractos.
    
    Args:
        vertex: (x, y) - El vértice del ángulo
        point1: (x, y) - Primer punto que define un lado
        point2: (x, y) - Segundo punto que define el otro lado
        radius: Radio del arco en pixels (default 30)
    
    Returns:
        dict con:
            - 'path': string SVG del path
            - 'label_pos': (x, y) posición óptima para la etiqueta
            - 'valid': bool indicando si el ángulo es válido
    """
    vx, vy = vertex
    
    # Calcular ángulos REALES de los lados respecto al vértice
    # En SVG, Y crece hacia abajo, así que usamos atan2 directamente
    angle1 = math.atan2(point1[1] - vy, point1[0] - vx)
    angle2 = math.atan2(point2[1] - vy, point2[0] - vx)
    
    # Normalizar ángulos a [0, 2π]
    if angle1 < 0:
        angle1 += 2 * math.pi
    if angle2 < 0:
        angle2 += 2 * math.pi
    
    # Determinar el camino más corto entre los ángulos
    # (queremos el ángulo menor, no el reflejo)
    diff = angle2 - angle1
    if diff < 0:
        diff += 2 * math.pi
    
    if diff > math.pi:
        # Ir en la otra dirección (camino más corto)
        angle1, angle2 = angle2, angle1
        diff = 2 * math.pi - diff
    
    # Puntos de inicio y fin del arco
    start_x = vx + radius * math.cos(angle1)
    start_y = vy + radius * math.sin(angle1)
    end_x = vx + radius * math.cos(angle2)
    end_y = vy + radius * math.sin(angle2)
    
    # ¿El arco es mayor a 180°?
    large_arc = 1 if diff > math.pi else 0
    
    # sweep-flag: 1 para ir en sentido horario (en coordenadas SVG)
    sweep = 1
    
    # Path SVG
    path = f"M {start_x:.2f} {start_y:.2f} A {radius} {radius} 0 {large_arc} {sweep} {end_x:.2f} {end_y:.2f}"
    
    # Posición de la etiqueta (en la bisectriz, un poco más lejos)
    bisector_angle = (angle1 + angle2) / 2
    if abs(angle2 - angle1) > math.pi:
        bisector_angle += math.pi  # Ajustar si cruzamos 0/2π
    
    label_radius = radius + 15
    label_x = vx + label_radius * math.cos(bisector_angle)
    label_y = vy + label_radius * math.sin(bisector_angle)
    
    return {
        'path': path,
        'label_pos': (label_x, label_y),
        'valid': True
    }


def sector_path(cx, cy, r, start_deg, end_deg):
    """Genera path SVG para un sector circular (porción de pizza).
    SECTOR = Centro → Punto1 → Arco → Punto2 → Centro
    """
    start = point_on_circle(cx, cy, r, start_deg)
    end = point_on_circle(cx, cy, r, end_deg)
    
    arc_span = (end_deg - start_deg) % 360
    large_arc = 1 if arc_span > 180 else 0
    sweep = 0
    
    return f"M {cx} {cy} L {start[0]:.2f} {start[1]:.2f} A {r} {r} 0 {large_arc} {sweep} {end[0]:.2f} {end[1]:.2f} Z"


def segment_path(cx, cy, r, start_deg, end_deg):
    """Genera path SVG para un segmento circular (región entre cuerda y arco).
    SEGMENTO = Punto1 → Arco → Punto2 → Línea recta de vuelta (cuerda)
    """
    start = point_on_circle(cx, cy, r, start_deg)
    end = point_on_circle(cx, cy, r, end_deg)
    
    arc_span = (end_deg - start_deg) % 360
    large_arc = 1 if arc_span > 180 else 0
    sweep = 0
    
    return f"M {start[0]:.2f} {start[1]:.2f} A {r} {r} 0 {large_arc} {sweep} {end[0]:.2f} {end[1]:.2f} Z"


def angle_arc_path(cx, cy, r, start_deg, end_deg):
    """Genera arco pequeño para indicar ángulo."""
    return arc_path(cx, cy, r, start_deg, end_deg)


def svg_header(width, height):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" 
style="font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;">
<rect width="{width}" height="{height}" fill="{COLORS['background']}"/>'''


def svg_footer():
    return '</svg>'


def text_element(x, y, text, size=12, weight="normal", color=None, anchor="start"):
    """
    Genera elemento de texto SVG con escape automático de caracteres XML.
    
    ⚠️ AUTOMÁTICO: Los caracteres <, >, & se escapan automáticamente.
    No es necesario escapar manualmente en el código que llama a esta función.
    """
    color = color or COLORS['text']
    safe_text = escape_svg_text(str(text))
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{color}">{safe_text}</text>'


def label_box(x, y, width, height, text, bg_color=None, border_color=None, text_color=None):
    """
    Genera caja con etiqueta y escape automático de caracteres XML.
    """
    bg = bg_color or "white"
    border = border_color or COLORS['auxiliary']
    txt_color = text_color or COLORS['text']
    safe_text = escape_svg_text(str(text))
    return f'''<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" fill="{bg}" stroke="{border}"/>
<text x="{x + width/2}" y="{y + height/2 + 4}" text-anchor="middle" font-size="12" fill="{txt_color}">{safe_text}</text>'''


# ============================================================================
# GENERADORES: BÁSICOS
# ============================================================================

def generate_basic(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Circunferencia básica con centro y radio."""
    cx, cy, r = 225, 200, 120
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Circunferencia", 18, "bold", COLORS["text"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{COLORS["circle_fill"]}" fill-opacity="0.3" stroke="{COLORS["circle_stroke"]}" stroke-width="3"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx - 18, cy + 5, "O", 14, "bold", COLORS["center"]))
    
    # Radio
    px, py = point_on_circle(cx, cy, r, 35)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.2f}" y2="{py:.2f}" stroke="{COLORS["radius"]}" stroke-width="3"/>')
    svg.append(text_element((cx + px)/2 + 8, (cy + py)/2 - 8, "r", 14, "bold", COLORS["radius"]))
    
    # Punto en la circunferencia
    svg.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(text_element(px + 10, py, "P", 14, "bold", COLORS["point"]))
    
    # Definición
    svg.append(label_box(50, 350, 350, 35, "Puntos equidistantes del centro O a distancia r"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


# ============================================================================
# GENERADORES: ELEMENTOS INDIVIDUALES
# ============================================================================

def generate_element_radius(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Radio: segmento del centro a la circunferencia."""
    cx, cy, r = 250, 175, 110  # CENTRADO: cx = width/2
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Radio", 18, "bold", COLORS["radius"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx - 18, cy + 5, "O", 14, "bold", COLORS["center"]))
    
    # Radio (resaltado)
    px, py = point_on_circle(cx, cy, r, 40)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.2f}" y2="{py:.2f}" stroke="{COLORS["radius"]}" stroke-width="4"/>')
    svg.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="5" fill="{COLORS["radius"]}"/>')
    svg.append(text_element((cx + px)/2 + 12, (cy + py)/2 - 8, "r", 16, "bold", COLORS["radius"]))
    
    # Definición (centrada)
    svg.append(label_box(100, 305, 300, 35, "Segmento del centro a la circunferencia", COLORS["sector_fill"], COLORS["radius"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_element_diameter(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Diámetro: segmento que pasa por el centro con extremos en la circunferencia."""
    cx, cy, r = 250, 175, 110  # CENTRADO: cx = width/2
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Diámetro", 18, "bold", COLORS["diameter"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx + 8, cy - 8, "O", 12, "bold", COLORS["center"]))
    
    # Diámetro (resaltado)
    p1 = point_on_circle(cx, cy, r, 150)
    p2 = point_on_circle(cx, cy, r, -30)
    svg.append(f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" stroke="{COLORS["diameter"]}" stroke-width="4"/>')
    svg.append(f'<circle cx="{p1[0]:.2f}" cy="{p1[1]:.2f}" r="5" fill="{COLORS["diameter"]}"/>')
    svg.append(f'<circle cx="{p2[0]:.2f}" cy="{p2[1]:.2f}" r="5" fill="{COLORS["diameter"]}"/>')
    svg.append(text_element(p1[0] - 15, p1[1] - 8, "A", 14, "bold", COLORS["diameter"]))
    svg.append(text_element(p2[0] + 8, p2[1] + 5, "B", 14, "bold", COLORS["diameter"]))
    svg.append(text_element(cx, cy + 25, "d = 2r", 14, "bold", COLORS["diameter"], "middle"))
    
    # Definición (centrada)
    svg.append(label_box(90, 305, 320, 35, "Pasa por el centro. Es la cuerda más larga.", COLORS["crown"], COLORS["diameter"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_element_chord(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Cuerda: segmento con extremos en la circunferencia."""
    cx, cy, r = 250, 175, 110  # CENTRADO: cx = width/2
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Cuerda", 18, "bold", COLORS["chord"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx + 8, cy + 5, "O", 11, "normal", COLORS["auxiliary"]))
    
    # Cuerda (resaltada)
    c1 = point_on_circle(cx, cy, r, 130)
    c2 = point_on_circle(cx, cy, r, 20)
    svg.append(f'<line x1="{c1[0]:.2f}" y1="{c1[1]:.2f}" x2="{c2[0]:.2f}" y2="{c2[1]:.2f}" stroke="{COLORS["chord"]}" stroke-width="4"/>')
    svg.append(f'<circle cx="{c1[0]:.2f}" cy="{c1[1]:.2f}" r="5" fill="{COLORS["chord"]}"/>')
    svg.append(f'<circle cx="{c2[0]:.2f}" cy="{c2[1]:.2f}" r="5" fill="{COLORS["chord"]}"/>')
    svg.append(text_element(c1[0] - 18, c1[1] - 5, "A", 14, "bold", COLORS["chord"]))
    svg.append(text_element(c2[0] + 8, c2[1] - 5, "B", 14, "bold", COLORS["chord"]))
    
    # Distancia al centro (punteada)
    mid_x, mid_y = (c1[0] + c2[0])/2, (c1[1] + c2[1])/2
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{mid_x:.2f}" y2="{mid_y:.2f}" stroke="{COLORS["auxiliary"]}" stroke-width="1.5" stroke-dasharray="4,3"/>')
    svg.append(text_element(mid_x + 5, mid_y + 15, "d", 11, "normal", COLORS["auxiliary"]))
    
    # Definición (centrada)
    svg.append(label_box(90, 305, 320, 35, "Extremos en la circunferencia (no pasa por O)", COLORS["segment_fill"], COLORS["chord"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_element_arc(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Arco: porción de la circunferencia."""
    cx, cy, r = 250, 175, 110  # CENTRADO: cx = width/2
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Arco", 18, "bold", COLORS["arc"], "middle"))
    
    # Circunferencia base (tenue)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["auxiliary"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["center"]}"/>')
    
    # Arco menor (resaltado)
    arc_minor = arc_path(cx, cy, r, 20, 140)
    svg.append(f'<path d="{arc_minor}" fill="none" stroke="{COLORS["arc"]}" stroke-width="5"/>')
    
    # Puntos A y B
    pa = point_on_circle(cx, cy, r, 140)
    pb = point_on_circle(cx, cy, r, 20)
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="5" fill="{COLORS["arc"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="5" fill="{COLORS["arc"]}"/>')
    svg.append(text_element(pa[0] - 18, pa[1] - 5, "A", 14, "bold", COLORS["arc"]))
    svg.append(text_element(pb[0] + 8, pb[1] - 5, "B", 14, "bold", COLORS["arc"]))
    
    # Etiqueta del arco
    arc_mid = point_on_circle(cx, cy, r + 20, 80)
    svg.append(text_element(arc_mid[0], arc_mid[1], "⌢AB", 14, "bold", COLORS["arc"], "middle"))
    
    # Leyenda
    # Leyendas centradas
    svg.append(f'<rect x="100" y="305" width="130" height="28" rx="6" fill="{COLORS["sector_fill"]}" stroke="{COLORS["arc"]}"/>')
    svg.append(text_element(165, 323, "Arco menor", 11, "normal", COLORS["text"], "middle"))
    
    svg.append(f'<rect x="270" y="305" width="130" height="28" rx="6" fill="{COLORS["background"]}" stroke="{COLORS["auxiliary"]}"/>')
    svg.append(text_element(335, 323, "Arco mayor", 11, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_element_sector(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Sector circular: región entre dos radios y un arco (rebanada de pizza)."""
    cx, cy, r = 250, 175, 110  # CENTRADO: cx = width/2
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Sector Circular", 18, "bold", COLORS["arc"], "middle"))
    
    # Circunferencia base (tenue)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["auxiliary"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
    
    # SECTOR: región entre 2 radios y arco
    sector = sector_path(cx, cy, r, 20, 100)
    svg.append(f'<path d="{sector}" fill="{COLORS["sector_fill"]}" stroke="{COLORS["arc"]}" stroke-width="3"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx - 18, cy + 5, "O", 14, "bold", COLORS["center"]))
    
    # Puntos en la circunferencia
    pa = point_on_circle(cx, cy, r, 100)
    pb = point_on_circle(cx, cy, r, 20)
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="4" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="4" fill="{COLORS["point"]}"/>')
    svg.append(text_element(pa[0] - 5, pa[1] - 12, "A", 12, "bold", COLORS["point"]))
    svg.append(text_element(pb[0] + 8, pb[1], "B", 12, "bold", COLORS["point"]))
    
    # Ángulo central
    angle_arc = angle_arc_path(cx, cy, 30, 20, 100)
    svg.append(f'<path d="{angle_arc}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
    svg.append(text_element(cx + 40, cy - 25, "θ", 14, "bold", COLORS["angle"]))
    
    # Anotaciones
    svg.append(text_element(cx + 30, cy - 50, "Arco", 11, "normal", COLORS["arc"]))
    svg.append(text_element(cx - 50, cy - 40, "Radio", 11, "normal", COLORS["radius"]))
    
    # Definición (centrada)
    svg.append(label_box(80, 320, 340, 50, "Limitado por 2 RADIOS + ARCO", COLORS["sector_fill"], COLORS["arc"]))
    svg.append(text_element(width/2, 355, '(Como una "rebanada de pizza")', 10, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_element_segment(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Segmento circular: región entre una cuerda y su arco."""
    cx, cy, r = 250, 175, 110  # CENTRADO: cx = width/2
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Segmento Circular", 18, "bold", COLORS["chord"], "middle"))
    
    # Circunferencia base (tenue)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["auxiliary"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
    
    # SEGMENTO: región entre cuerda y arco (NO incluye el centro)
    segment = segment_path(cx, cy, r, 30, 150)
    svg.append(f'<path d="{segment}" fill="{COLORS["segment_fill"]}" stroke="{COLORS["chord"]}" stroke-width="3"/>')
    
    # Cuerda (línea recta que cierra el segmento)
    ca = point_on_circle(cx, cy, r, 150)
    cb = point_on_circle(cx, cy, r, 30)
    svg.append(f'<line x1="{ca[0]:.2f}" y1="{ca[1]:.2f}" x2="{cb[0]:.2f}" y2="{cb[1]:.2f}" stroke="{COLORS["chord"]}" stroke-width="3"/>')
    
    # Centro (solo referencia)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["auxiliary"]}"/>')
    svg.append(text_element(cx + 8, cy + 5, "O", 10, "normal", COLORS["auxiliary"]))
    
    # Puntos
    svg.append(f'<circle cx="{ca[0]:.2f}" cy="{ca[1]:.2f}" r="4" fill="{COLORS["chord"]}"/>')
    svg.append(f'<circle cx="{cb[0]:.2f}" cy="{cb[1]:.2f}" r="4" fill="{COLORS["chord"]}"/>')
    svg.append(text_element(ca[0] - 18, ca[1], "A", 12, "bold", COLORS["chord"]))
    svg.append(text_element(cb[0] + 8, cb[1], "B", 12, "bold", COLORS["chord"]))
    
    # Anotaciones
    arc_mid = point_on_circle(cx, cy, r + 15, 90)
    svg.append(text_element(arc_mid[0], arc_mid[1] - 5, "Arco", 11, "normal", COLORS["arc"]))
    
    chord_mid_x = (ca[0] + cb[0])/2
    chord_mid_y = (ca[1] + cb[1])/2
    svg.append(text_element(chord_mid_x, chord_mid_y + 20, "Cuerda", 11, "normal", COLORS["chord"]))
    
    # Definición (centrada)
    svg.append(label_box(80, 320, 340, 50, "Limitado por CUERDA + ARCO", COLORS["segment_fill"], COLORS["chord"]))
    svg.append(text_element(width/2, 355, '(NO incluye el centro)', 10, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_element_crown(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Corona circular: región entre dos circunferencias concéntricas."""
    cx, cy = 250, 175  # CENTRADO: cx = width/2
    R, r = 110, 60  # Radio mayor y menor
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Corona Circular", 18, "bold", COLORS["circle_stroke"], "middle"))
    
    # Corona (usando clip path)
    svg.append(f'''<defs>
      <clipPath id="corona-clip">
        <circle cx="{cx}" cy="{cy}" r="{R}"/>
      </clipPath>
    </defs>''')
    
    # Círculo grande relleno
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{COLORS["crown"]}" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # "Agujero" en el centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{COLORS["background"]}" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx + 8, cy + 5, "O", 12, "bold", COLORS["center"]))
    
    # Radios R y r
    pR = point_on_circle(cx, cy, R, 30)
    pr = point_on_circle(cx, cy, r, 30)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pR[0]:.2f}" y2="{pR[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2"/>')
    svg.append(text_element((cx + pR[0])/2 + 10, (cy + pR[1])/2 - 10, "R", 14, "bold", COLORS["radius"]))
    
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pr[0]:.2f}" y2="{pr[1]:.2f}" stroke="{COLORS["diameter"]}" stroke-width="2"/>')
    svg.append(text_element((cx + pr[0])/2 - 15, (cy + pr[1])/2 + 5, "r", 14, "bold", COLORS["diameter"]))
    
    # Fórmula (centrada)
    svg.append(label_box(100, 310, 300, 55, "", COLORS["crown"], COLORS["circle_stroke"]))
    svg.append(text_element(250, 332, "Área = π(R² - r²)", 14, "bold", COLORS["text"], "middle"))
    svg.append(text_element(250, 352, "Dos circunferencias concéntricas", 11, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


# ============================================================================
# GENERADORES: POSICIONES
# ============================================================================

def generate_point_positions(width=SIZE_HORIZONTAL[0], height=SIZE_HORIZONTAL[1]):
    """
    Posiciones de un punto respecto a la circunferencia.
    
    NOTA: Usa SIZE_HORIZONTAL (750x420) para distribución equidistante.
    """
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 28, "Posiciones de un Punto", 18, "bold", COLORS["text"], "middle"))
    
    # Distribución equidistante en 750px: 150, 375, 600 (con margen para el punto exterior)
    circle_y = 190
    r = 70  # Radio reducido para dar más margen
    
    # Los caracteres < y > se escapan AUTOMÁTICAMENTE en text_element()
    positions = [
        (150, circle_y, "Interior", "d < r", "interior", COLORS["chord"]),
        (375, circle_y, "Sobre la circ.", "d = r", "sobre", COLORS["circle_stroke"]),
        (600, circle_y, "Exterior", "d > r", "exterior", COLORS["tangent"]),
    ]
    
    for cx, cy, label, formula, pos_type, color in positions:
        # Circunferencia
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{COLORS["circle_fill"]}" fill-opacity="0.3" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["center"]}"/>')
        
        # Punto P según posición
        if pos_type == "interior":
            px, py = cx + 25, cy - 15
        elif pos_type == "sobre":
            px, py = point_on_circle(cx, cy, r, 50)
        else:  # exterior - hacia la izquierda para no salirse del viewBox
            px, py = cx + r + 20, cy - 20
        
        # Ajustar etiqueta P para que no se salga del viewBox
        label_offset_x = 10 if px + 25 < width else -20
        
        svg.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="6" fill="{color}"/>')
        svg.append(text_element(px + label_offset_x, py - 8, "P", 12, "bold", color))
        
        # Distancia d
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.2f}" y2="{py:.2f}" stroke="{COLORS["auxiliary"]}" stroke-width="1.5" stroke-dasharray="4,3"/>')
        
        # Etiquetas (dentro del viewBox con margen)
        svg.append(text_element(cx, cy + r + 35, label, 13, "bold", color, "middle"))
        svg.append(text_element(cx, cy + r + 55, formula, 11, "normal", COLORS["text"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_tangent_secant(width=SIZE_HORIZONTAL[0], height=SIZE_HORIZONTAL[1]):
    """Recta tangente y secante."""
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 28, "Tangente y Secante", 18, "bold", COLORS["text"], "middle"))
    
    # === TANGENTE (izquierda) ===
    cx1, cy1, r1 = 170, 190, 90
    svg.append(f'<circle cx="{cx1}" cy="{cy1}" r="{r1}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    svg.append(f'<circle cx="{cx1}" cy="{cy1}" r="3" fill="{COLORS["center"]}"/>')
    
    # Punto de tangencia (arriba)
    pt = point_on_circle(cx1, cy1, r1, 90)
    svg.append(f'<circle cx="{pt[0]:.2f}" cy="{pt[1]:.2f}" r="5" fill="{COLORS["tangent"]}"/>')
    svg.append(text_element(pt[0] + 10, pt[1] - 5, "T", 12, "bold", COLORS["tangent"]))
    
    # Recta tangente (horizontal en T)
    svg.append(f'<line x1="{cx1 - 120}" y1="{pt[1]:.2f}" x2="{cx1 + 120}" y2="{pt[1]:.2f}" stroke="{COLORS["tangent"]}" stroke-width="3"/>')
    
    # Radio perpendicular
    svg.append(f'<line x1="{cx1}" y1="{cy1}" x2="{pt[0]:.2f}" y2="{pt[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2" stroke-dasharray="5,3"/>')
    
    # Símbolo de ángulo recto
    svg.append(f'<rect x="{pt[0] - 8:.2f}" y="{pt[1]:.2f}" width="8" height="8" fill="none" stroke="{COLORS["text"]}" stroke-width="1.5"/>')
    
    # Etiquetas DENTRO del viewBox
    svg.append(f'<rect x="{cx1 - 60}" y="310" width="120" height="55" rx="8" fill="white" stroke="{COLORS["tangent"]}" stroke-width="2"/>')
    svg.append(text_element(cx1, 330, "TANGENTE", 13, "bold", COLORS["tangent"], "middle"))
    svg.append(text_element(cx1, 348, "Toca en 1 punto", 10, "normal", COLORS["text"], "middle"))
    svg.append(text_element(cx1, 360, "⊥ al radio", 10, "normal", COLORS["text"], "middle"))
    
    # === SECANTE (derecha) ===
    cx2, cy2, r2 = 480, 190, 90
    svg.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r2}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    svg.append(f'<circle cx="{cx2}" cy="{cy2}" r="3" fill="{COLORS["center"]}"/>')
    
    # Puntos de intersección
    ps1 = point_on_circle(cx2, cy2, r2, 145)
    ps2 = point_on_circle(cx2, cy2, r2, 35)
    
    svg.append(f'<circle cx="{ps1[0]:.2f}" cy="{ps1[1]:.2f}" r="5" fill="{COLORS["secant"]}"/>')
    svg.append(f'<circle cx="{ps2[0]:.2f}" cy="{ps2[1]:.2f}" r="5" fill="{COLORS["secant"]}"/>')
    svg.append(text_element(ps1[0] - 15, ps1[1] - 8, "A", 12, "bold", COLORS["secant"]))
    svg.append(text_element(ps2[0] + 8, ps2[1] - 8, "B", 12, "bold", COLORS["secant"]))
    
    # Recta secante (extendida)
    dx, dy = ps2[0] - ps1[0], ps2[1] - ps1[1]
    svg.append(f'<line x1="{ps1[0] - dx*0.25:.2f}" y1="{ps1[1] - dy*0.25:.2f}" x2="{ps2[0] + dx*0.25:.2f}" y2="{ps2[1] + dy*0.25:.2f}" stroke="{COLORS["secant"]}" stroke-width="3"/>')
    
    # Etiquetas
    svg.append(f'<rect x="{cx2 - 60}" y="310" width="120" height="55" rx="8" fill="white" stroke="{COLORS["secant"]}" stroke-width="2"/>')
    svg.append(text_element(cx2, 330, "SECANTE", 13, "bold", COLORS["secant"], "middle"))
    svg.append(text_element(cx2, 348, "Corta en 2 puntos", 10, "normal", COLORS["text"], "middle"))
    svg.append(text_element(cx2, 360, "Cuerda AB interior", 10, "normal", COLORS["text"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_circle_positions(width=SIZE_MULTIPLE[0], height=SIZE_MULTIPLE[1]):
    """Posiciones relativas entre dos circunferencias."""
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 28, "Posiciones entre Circunferencias", 18, "bold", COLORS["text"], "middle"))
    
    # Fila 1 - Los caracteres < y > se escapan AUTOMÁTICAMENTE en text_element()
    positions_row1 = [
        (125, 140, 50, 35, 95, "Exteriores", "d > R + r", COLORS["chord"]),
        (375, 140, 50, 35, 50, "Tang. Ext.", "d = R + r", COLORS["angle"]),
        (625, 140, 55, 40, 30, "Secantes", "|R-r| < d < R+r", COLORS["secant"]),
    ]
    
    # Fila 2
    positions_row2 = [
        (200, 340, 60, 35, 25, "Tang. Int.", "d = R - r", COLORS["tangent"]),
        (500, 340, 65, 35, 0, "Concéntricas", "d = 0", COLORS["diameter"]),
    ]
    
    for cx, cy, r1, r2, offset, label, formula, color in positions_row1 + positions_row2:
        # Circunferencia grande
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="{COLORS["circle_fill"]}" fill-opacity="0.3" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["center"]}"/>')
        
        # Circunferencia pequeña
        cx2 = cx + offset
        svg.append(f'<circle cx="{cx2}" cy="{cy}" r="{r2}" fill="{COLORS["sector_fill"]}" fill-opacity="0.5" stroke="{color}" stroke-width="2"/>')
        if offset != 0:
            svg.append(f'<circle cx="{cx2}" cy="{cy}" r="3" fill="{color}"/>')
        
        # Etiquetas
        svg.append(text_element(cx, cy + 80, label, 12, "bold", color, "middle"))
        svg.append(text_element(cx, cy + 96, formula, 10, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


# ============================================================================
# GENERADORES: ÁNGULOS
# ============================================================================

def generate_angle_central(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Ángulo central: vértice en el centro."""
    cx, cy, r = 225, 200, 120
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Ángulo Central", 18, "bold", COLORS["angle"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Puntos A y B (ARRIBA para que el ángulo sea visible)
    angle_a, angle_b = 130, 40
    pa = point_on_circle(cx, cy, r, angle_a)
    pb = point_on_circle(cx, cy, r, angle_b)
    
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(text_element(pa[0] - 18, pa[1] - 8, "A", 14, "bold", COLORS["point"]))
    svg.append(text_element(pb[0] + 10, pb[1], "B", 14, "bold", COLORS["point"]))
    
    # Radios OA y OB
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pa[0]:.2f}" y2="{pa[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2.5"/>')
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2.5"/>')
    
    # Centro (vértice)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx - 20, cy + 20, "O", 14, "bold", COLORS["center"]))
    
    # Arco del ángulo θ - USANDO LA FUNCIÓN CORRECTA
    arc_data = get_angle_arc_svg(
        vertex=(cx, cy),
        point1=pa,
        point2=pb,
        radius=35
    )
    svg.append(f'<path d="{arc_data["path"]}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    svg.append(text_element(arc_data["label_pos"][0], arc_data["label_pos"][1], "θ", 16, "bold", COLORS["angle"]))
    
    # Arco AB resaltado
    arc_ab = arc_path(cx, cy, r, angle_b, angle_a)
    svg.append(f'<path d="{arc_ab}" fill="none" stroke="{COLORS["arc"]}" stroke-width="5"/>')
    
    # Fórmula
    svg.append(label_box(100, 350, 250, 40, "θ = arco AB", "white", COLORS["angle"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_angle_inscribed(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Ángulo inscrito: vértice en la circunferencia."""
    cx, cy, r = 225, 200, 120
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Ángulo Inscrito", 18, "bold", COLORS["angle"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Puntos A, B, P (P es el vértice en la circunferencia)
    angle_a, angle_b, angle_p = 150, 30, 250
    pa = point_on_circle(cx, cy, r, angle_a)
    pb = point_on_circle(cx, cy, r, angle_b)
    pp = point_on_circle(cx, cy, r, angle_p)
    
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pp[0]:.2f}" cy="{pp[1]:.2f}" r="7" fill="{COLORS["angle"]}"/>')
    
    svg.append(text_element(pa[0] - 18, pa[1] - 8, "A", 14, "bold", COLORS["point"]))
    svg.append(text_element(pb[0] + 10, pb[1], "B", 14, "bold", COLORS["point"]))
    svg.append(text_element(pp[0] - 5, pp[1] + 22, "P", 14, "bold", COLORS["angle"]))
    
    # Lados PA y PB
    svg.append(f'<line x1="{pp[0]:.2f}" y1="{pp[1]:.2f}" x2="{pa[0]:.2f}" y2="{pa[1]:.2f}" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    svg.append(f'<line x1="{pp[0]:.2f}" y1="{pp[1]:.2f}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    
    # Centro (referencia)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["auxiliary"]}"/>')
    
    # Arco AB resaltado
    arc_ab = arc_path(cx, cy, r, angle_b, angle_a)
    svg.append(f'<path d="{arc_ab}" fill="none" stroke="{COLORS["arc"]}" stroke-width="5"/>')
    
    # Arco del ángulo en P - USANDO LA FUNCIÓN CORRECTA
    arc_data = get_angle_arc_svg(
        vertex=pp,
        point1=pa,
        point2=pb,
        radius=28
    )
    svg.append(f'<path d="{arc_data["path"]}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    svg.append(text_element(arc_data["label_pos"][0], arc_data["label_pos"][1], "α", 14, "bold", COLORS["angle"]))
    
    # Fórmula
    svg.append(label_box(100, 350, 250, 40, "α = arco AB / 2", "white", COLORS["angle"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_angle_semi_inscribed(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Ángulo semi-inscrito: un lado es tangente."""
    cx, cy, r = 225, 200, 110
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Ángulo Semi-inscrito", 18, "bold", COLORS["angle"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Punto T (vértice, en la circunferencia) - a la izquierda
    pt = point_on_circle(cx, cy, r, 180)
    svg.append(f'<circle cx="{pt[0]:.2f}" cy="{pt[1]:.2f}" r="6" fill="{COLORS["angle"]}"/>')
    svg.append(text_element(pt[0] - 20, pt[1] + 5, "T", 14, "bold", COLORS["angle"]))
    
    # Punto B (otro extremo del arco) - arriba a la derecha
    pb = point_on_circle(cx, cy, r, 60)
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(text_element(pb[0] + 10, pb[1] - 5, "B", 14, "bold", COLORS["point"]))
    
    # Cuerda TB
    svg.append(f'<line x1="{pt[0]:.2f}" y1="{pt[1]:.2f}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["chord"]}" stroke-width="2.5"/>')
    
    # Tangente en T (vertical) - punto ficticio arriba de T
    tangent_point = (pt[0], pt[1] - 100)  # La tangente va hacia arriba
    svg.append(f'<line x1="{pt[0]:.2f}" y1="{pt[1] - 100:.2f}" x2="{pt[0]:.2f}" y2="{pt[1] + 100:.2f}" stroke="{COLORS["tangent"]}" stroke-width="2.5"/>')
    svg.append(text_element(pt[0] - 50, pt[1] - 85, "tangente", 11, "normal", COLORS["tangent"]))
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["auxiliary"]}"/>')
    
    # Arco TB (en la circunferencia)
    arc_tb = arc_path(cx, cy, r, 60, 180)
    svg.append(f'<path d="{arc_tb}" fill="none" stroke="{COLORS["arc"]}" stroke-width="4"/>')
    
    # Arco del ángulo en T - USANDO LA FUNCIÓN CORRECTA
    # El ángulo está entre la tangente (hacia arriba) y la cuerda TB
    arc_data = get_angle_arc_svg(
        vertex=pt,
        point1=tangent_point,  # Dirección de la tangente (arriba)
        point2=pb,              # Dirección de la cuerda
        radius=30
    )
    svg.append(f'<path d="{arc_data["path"]}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    svg.append(text_element(arc_data["label_pos"][0], arc_data["label_pos"][1], "α", 14, "bold", COLORS["angle"]))
    
    # Fórmula
    svg.append(label_box(100, 350, 250, 40, "α = arco TB / 2", "white", COLORS["angle"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_angle_interior(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Ángulo interior: vértice dentro de la circunferencia."""
    cx, cy, r = 225, 200, 110
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Ángulo Interior", 18, "bold", COLORS["angle"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Dos cuerdas que se cruzan dentro
    # Cuerda AC (diagonal de arriba-izquierda a abajo-derecha)
    pa = point_on_circle(cx, cy, r, 140)
    pc = point_on_circle(cx, cy, r, -20)
    # Cuerda BD (diagonal de arriba-derecha a abajo-izquierda)
    pb = point_on_circle(cx, cy, r, 70)
    pd = point_on_circle(cx, cy, r, 220)
    
    # Calcular intersección REAL de las dos cuerdas
    # Línea 1: A-C, Línea 2: B-D
    # Usando fórmula de intersección de líneas
    def line_intersection(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if abs(denom) < 1e-10:
            return None
        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
        px = x1 + t*(x2-x1)
        py = y1 + t*(y2-y1)
        return (px, py)
    
    intersection = line_intersection(pa, pc, pb, pd)
    if intersection:
        px, py = intersection
    else:
        px, py = cx, cy  # Fallback al centro
    
    svg.append(f'<line x1="{pa[0]:.2f}" y1="{pa[1]:.2f}" x2="{pc[0]:.2f}" y2="{pc[1]:.2f}" stroke="{COLORS["chord"]}" stroke-width="2"/>')
    svg.append(f'<line x1="{pb[0]:.2f}" y1="{pb[1]:.2f}" x2="{pd[0]:.2f}" y2="{pd[1]:.2f}" stroke="{COLORS["secant"]}" stroke-width="2"/>')
    
    # Puntos en la circunferencia
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="4" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="4" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pc[0]:.2f}" cy="{pc[1]:.2f}" r="4" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pd[0]:.2f}" cy="{pd[1]:.2f}" r="4" fill="{COLORS["point"]}"/>')
    
    svg.append(text_element(pa[0] - 18, pa[1] - 5, "A", 12, "bold", COLORS["point"]))
    svg.append(text_element(pb[0] + 5, pb[1] - 12, "B", 12, "bold", COLORS["point"]))
    svg.append(text_element(pc[0] + 10, pc[1] + 5, "C", 12, "bold", COLORS["point"]))
    svg.append(text_element(pd[0] - 18, pd[1] + 5, "D", 12, "bold", COLORS["point"]))
    
    # Arcos opuestos resaltados
    arc1 = arc_path(cx, cy, r, 70, 140)
    arc2 = arc_path(cx, cy, r, 220, 340)
    svg.append(f'<path d="{arc1}" fill="none" stroke="{COLORS["arc"]}" stroke-width="4"/>')
    svg.append(f'<path d="{arc2}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="4"/>')
    
    # Centro (referencia)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["auxiliary"]}"/>')
    
    # ⭐ ARCO DEL ÁNGULO α EN P - CRÍTICO: ESTO FALTABA
    # El ángulo está entre las direcciones hacia A y hacia B desde P
    arc_data = get_angle_arc_svg(
        vertex=(px, py),
        point1=pa,  # Dirección hacia A
        point2=pb,  # Dirección hacia B
        radius=25
    )
    svg.append(f'<path d="{arc_data["path"]}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    svg.append(text_element(arc_data["label_pos"][0], arc_data["label_pos"][1], "α", 14, "bold", COLORS["angle"]))
    
    # Vértice P (dibujado después del arco para que esté encima)
    svg.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="6" fill="{COLORS["angle"]}"/>')
    svg.append(text_element(px + 12, py + 5, "P", 14, "bold", COLORS["angle"]))
    
    # Fórmula
    svg.append(label_box(75, 340, 300, 50, "", "white", COLORS["angle"]))
    svg.append(text_element(225, 360, "α = (arco₁ + arco₂) / 2", 13, "bold", COLORS["text"], "middle"))
    svg.append(text_element(225, 378, "Semisuma de arcos opuestos", 10, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_angle_exterior(width=SIZE_COMPOUND[0], height=SIZE_COMPOUND[1]):
    """
    Ángulo exterior: vértice fuera de la circunferencia.
    
    PEDAGOGÍA:
    - El ángulo α está EN EL VÉRTICE P (fuera de la circunferencia)
    - El arco MAYOR es el que va "por fuera" (el más largo entre A y C)
    - El arco MENOR es el que va "por dentro" (el más corto entre A y C)
    - La fórmula es: α = (mayor - menor) / 2
    """
    cx, cy, r = 300, 220, 110
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Ángulo Exterior", 18, "bold", COLORS["angle"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Puntos en la circunferencia
    # A arriba-izquierda, C abajo-derecha
    angle_A = 130
    angle_C = -30
    pA = point_on_circle(cx, cy, r, angle_A)
    pC = point_on_circle(cx, cy, r, angle_C)
    
    # Vértice P (fuera, a la izquierda)
    px, py = 110, 220
    
    # Líneas PA y PC (las dos secantes)
    svg.append(f'<line x1="{px}" y1="{py}" x2="{pA[0]:.2f}" y2="{pA[1]:.2f}" stroke="{COLORS["chord"]}" stroke-width="2.5"/>')
    svg.append(f'<line x1="{px}" y1="{py}" x2="{pC[0]:.2f}" y2="{pC[1]:.2f}" stroke="{COLORS["secant"]}" stroke-width="2.5"/>')
    
    # Puntos A y C
    svg.append(f'<circle cx="{pA[0]:.2f}" cy="{pA[1]:.2f}" r="5" fill="{COLORS["chord"]}"/>')
    svg.append(f'<circle cx="{pC[0]:.2f}" cy="{pC[1]:.2f}" r="5" fill="{COLORS["secant"]}"/>')
    svg.append(text_element(pA[0] - 5, pA[1] - 15, "A", 14, "bold", COLORS["chord"]))
    svg.append(text_element(pC[0] + 10, pC[1] + 5, "C", 14, "bold", COLORS["secant"]))
    
    # ARCO MAYOR: de C a A pasando por abajo (el arco largo)
    # En grados: de -30° a 130° pasando por 270° (abajo)
    arc_mayor = arc_path(cx, cy, r, angle_C, angle_A)
    svg.append(f'<path d="{arc_mayor}" fill="none" stroke="{COLORS["arc"]}" stroke-width="5"/>')
    
    # ARCO MENOR: de A a C por arriba (el arco corto)
    # En grados: de 130° a 330° (=-30°) pasando por 0° (derecha)
    arc_menor = arc_path(cx, cy, r, angle_A, 360 + angle_C)
    svg.append(f'<path d="{arc_menor}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="5"/>')
    
    # Centro (referencia)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["auxiliary"]}"/>')
    
    # ⭐ ARCO DEL ÁNGULO α EN P (EL ÁNGULO QUE QUEREMOS MEDIR)
    arc_data = get_angle_arc_svg(
        vertex=(px, py),
        point1=pA,
        point2=pC,
        radius=35
    )
    svg.append(f'<path d="{arc_data["path"]}" fill="none" stroke="{COLORS["angle"]}" stroke-width="3"/>')
    svg.append(text_element(arc_data["label_pos"][0], arc_data["label_pos"][1], "α", 16, "bold", COLORS["angle"]))
    
    # Vértice P
    svg.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{COLORS["angle"]}"/>')
    svg.append(text_element(px - 25, py + 5, "P", 14, "bold", COLORS["angle"]))
    
    # === ETIQUETAS CLARAS ===
    # Etiqueta ARCO MAYOR (naranja)
    mayor_label_pos = point_on_circle(cx, cy, r + 25, -80)
    svg.append(f'<rect x="{mayor_label_pos[0] - 45}" y="{mayor_label_pos[1] - 12}" width="90" height="24" rx="4" fill="{COLORS["arc"]}" fill-opacity="0.2" stroke="{COLORS["arc"]}"/>')
    svg.append(text_element(mayor_label_pos[0], mayor_label_pos[1] + 5, "ARCO MAYOR", 10, "bold", COLORS["arc"], "middle"))
    
    # Etiqueta ARCO MENOR (amarillo)
    menor_label_pos = point_on_circle(cx, cy, r + 25, 50)
    svg.append(f'<rect x="{menor_label_pos[0] - 45}" y="{menor_label_pos[1] - 12}" width="90" height="24" rx="4" fill="{COLORS["highlight"]}" fill-opacity="0.3" stroke="{COLORS["highlight"]}"/>')
    svg.append(text_element(menor_label_pos[0], menor_label_pos[1] + 5, "ARCO MENOR", 10, "bold", COLORS["highlight"], "middle"))
    
    # Fórmula destacada (ajustada para caber en viewBox 600x460)
    svg.append(label_box(150, 385, 300, 55, "", "white", COLORS["angle"]))
    svg.append(text_element(300, 405, "α = (MAYOR - MENOR) / 2", 14, "bold", COLORS["text"], "middle"))
    svg.append(text_element(300, 425, "El ángulo es la SEMIDIFERENCIA de los arcos", 10, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


# ============================================================================
# GENERADORES: TEOREMAS
# ============================================================================

def generate_theorem_inscribed(width=SIZE_COMPOUND[0], height=SIZE_COMPOUND[1]):
    """
    Teorema: ángulo inscrito = ½ ángulo central.
    
    PEDAGOGÍA:
    - Mostrar AMBOS ángulos: θ (central) y α (inscrito)
    - El arco de α debe ser visible en P
    - La relación α = θ/2 debe ser evidente
    """
    cx, cy, r = 300, 230, 130
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Teorema del Ángulo Inscrito", 18, "bold", COLORS["text"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Puntos A, B (arriba)
    angle_a, angle_b = 145, 35
    pa = point_on_circle(cx, cy, r, angle_a)
    pb = point_on_circle(cx, cy, r, angle_b)
    
    # Punto P (inscrito, abajo)
    pp = point_on_circle(cx, cy, r, 255)
    
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="5" fill="{COLORS["point"]}"/>')
    
    svg.append(text_element(pa[0] - 18, pa[1] - 8, "A", 14, "bold", COLORS["point"]))
    svg.append(text_element(pb[0] + 10, pb[1] - 5, "B", 14, "bold", COLORS["point"]))
    
    # Ángulo central (OA, OB) - radios
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pa[0]:.2f}" y2="{pa[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2.5"/>')
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2.5"/>')
    
    # Ángulo inscrito (PA, PB) - cuerdas
    svg.append(f'<line x1="{pp[0]:.2f}" y1="{pp[1]:.2f}" x2="{pa[0]:.2f}" y2="{pa[1]:.2f}" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    svg.append(f'<line x1="{pp[0]:.2f}" y1="{pp[1]:.2f}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["angle"]}" stroke-width="2.5"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx + 10, cy + 5, "O", 12, "bold", COLORS["center"]))
    
    # ⭐ ARCO DEL ÁNGULO CENTRAL θ
    arc_central = get_angle_arc_svg(
        vertex=(cx, cy),
        point1=pa,
        point2=pb,
        radius=35
    )
    svg.append(f'<path d="{arc_central["path"]}" fill="none" stroke="{COLORS["radius"]}" stroke-width="3"/>')
    svg.append(text_element(arc_central["label_pos"][0], arc_central["label_pos"][1], "θ", 18, "bold", COLORS["radius"]))
    
    # ⭐ ARCO DEL ÁNGULO INSCRITO α (EN P)
    arc_inscribed = get_angle_arc_svg(
        vertex=pp,
        point1=pa,
        point2=pb,
        radius=30
    )
    svg.append(f'<path d="{arc_inscribed["path"]}" fill="none" stroke="{COLORS["angle"]}" stroke-width="3"/>')
    svg.append(text_element(arc_inscribed["label_pos"][0], arc_inscribed["label_pos"][1], "α", 18, "bold", COLORS["angle"]))
    
    # Punto P (vértice inscrito)
    svg.append(f'<circle cx="{pp[0]:.2f}" cy="{pp[1]:.2f}" r="6" fill="{COLORS["angle"]}"/>')
    svg.append(text_element(pp[0] - 5, pp[1] + 22, "P", 14, "bold", COLORS["angle"]))
    
    # Cajas de fórmulas con colores claros
    svg.append(f'<rect x="30" y="55" width="120" height="70" rx="8" fill="white" stroke="{COLORS["radius"]}" stroke-width="2"/>')
    svg.append(text_element(90, 80, "CENTRAL", 11, "bold", COLORS["radius"], "middle"))
    svg.append(text_element(90, 100, "θ = arco AB", 12, "normal", COLORS["text"], "middle"))
    svg.append(text_element(90, 118, "(vértice en O)", 9, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(f'<rect x="450" y="55" width="120" height="70" rx="8" fill="white" stroke="{COLORS["angle"]}" stroke-width="2"/>')
    svg.append(text_element(510, 80, "INSCRITO", 11, "bold", COLORS["angle"], "middle"))
    svg.append(text_element(510, 100, "α = θ / 2", 12, "normal", COLORS["text"], "middle"))
    svg.append(text_element(510, 118, "(vértice en P)", 9, "normal", COLORS["auxiliary"], "middle"))
    
    # Teorema destacado (ajustado para caber en viewBox 600x460)
    svg.append(f'<rect x="150" y="395" width="300" height="50" rx="10" fill="{COLORS["highlight"]}" fill-opacity="0.3" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
    svg.append(text_element(width/2, 418, "INSCRITO = ½ CENTRAL", 15, "bold", COLORS["text"], "middle"))
    svg.append(text_element(width/2, 438, "α = θ / 2", 12, "normal", COLORS["auxiliary"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_theorem_tales(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Teorema de Tales: inscrito en semicircunferencia = 90°."""
    cx, cy, r = 225, 200, 110
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Teorema de Tales", 18, "bold", COLORS["diameter"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    
    # Diámetro AB
    pa = point_on_circle(cx, cy, r, 180)
    pb = point_on_circle(cx, cy, r, 0)
    svg.append(f'<line x1="{pa[0]:.2f}" y1="{pa[1]:.2f}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["diameter"]}" stroke-width="3"/>')
    
    svg.append(f'<circle cx="{pa[0]:.2f}" cy="{pa[1]:.2f}" r="5" fill="{COLORS["diameter"]}"/>')
    svg.append(f'<circle cx="{pb[0]:.2f}" cy="{pb[1]:.2f}" r="5" fill="{COLORS["diameter"]}"/>')
    svg.append(text_element(pa[0] - 18, pa[1] + 5, "A", 14, "bold", COLORS["diameter"]))
    svg.append(text_element(pb[0] + 10, pb[1] + 5, "B", 14, "bold", COLORS["diameter"]))
    
    # Punto P (inscrito en la semicircunferencia)
    pp = point_on_circle(cx, cy, r, 70)
    svg.append(f'<circle cx="{pp[0]:.2f}" cy="{pp[1]:.2f}" r="6" fill="{COLORS["angle"]}"/>')
    svg.append(text_element(pp[0] + 5, pp[1] - 15, "P", 14, "bold", COLORS["angle"]))
    
    # Lados PA y PB
    svg.append(f'<line x1="{pp[0]:.2f}" y1="{pp[1]:.2f}" x2="{pa[0]:.2f}" y2="{pa[1]:.2f}" stroke="{COLORS["angle"]}" stroke-width="2"/>')
    svg.append(f'<line x1="{pp[0]:.2f}" y1="{pp[1]:.2f}" x2="{pb[0]:.2f}" y2="{pb[1]:.2f}" stroke="{COLORS["angle"]}" stroke-width="2"/>')
    
    # Símbolo de ángulo recto en P
    svg.append(f'<rect x="{pp[0] - 5:.2f}" y="{pp[1] + 3:.2f}" width="10" height="10" fill="none" stroke="{COLORS["angle"]}" stroke-width="1.5" transform="rotate(-20, {pp[0]}, {pp[1]})"/>')
    svg.append(text_element(pp[0] + 20, pp[1] + 20, "90°", 14, "bold", COLORS["angle"]))
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx + 8, cy + 15, "O", 11, "normal", COLORS["center"]))
    
    # Fórmula
    svg.append(label_box(75, 345, 300, 45, "", COLORS["crown"], COLORS["diameter"]))
    svg.append(text_element(225, 362, "Inscrito en semicircunferencia", 11, "normal", COLORS["auxiliary"], "middle"))
    svg.append(text_element(225, 380, "= 90° (ángulo recto)", 13, "bold", COLORS["text"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


# ============================================================================
# GENERADORES: FÓRMULAS
# ============================================================================

def generate_formula_length(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Fórmula de longitud de circunferencia."""
    cx, cy, r = 180, 190, 100
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Longitud de la Circunferencia", 18, "bold", COLORS["text"], "middle"))
    
    # Circunferencia
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["circle_stroke"]}" stroke-width="3"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx - 15, cy + 5, "O", 12, "bold", COLORS["center"]))
    
    # Radio
    pr = point_on_circle(cx, cy, r, 0)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pr[0]:.2f}" y2="{pr[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2.5"/>')
    svg.append(text_element((cx + pr[0])/2, cy - 10, "r", 14, "bold", COLORS["radius"], "middle"))
    
    # Fórmulas
    svg.append(f'<rect x="320" y="100" width="160" height="150" rx="12" fill="white" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    svg.append(text_element(400, 128, "FÓRMULAS", 13, "bold", COLORS["text"], "middle"))
    
    svg.append(text_element(400, 165, "L = 2πr", 20, "bold", COLORS["circle_stroke"], "middle"))
    svg.append(text_element(400, 195, "o también", 11, "normal", COLORS["auxiliary"], "middle"))
    svg.append(text_element(400, 220, "L = πd", 18, "bold", COLORS["circle_stroke"], "middle"))
    svg.append(text_element(400, 242, "(d = 2r)", 10, "normal", COLORS["auxiliary"], "middle"))
    
    # Nota
    svg.append(label_box(50, 330, 400, 35, "Es el \"perímetro\" de la circunferencia", COLORS["sector_fill"], COLORS["auxiliary"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_formula_area(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Fórmula de área del círculo."""
    cx, cy, r = 180, 190, 100
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Área del Círculo", 18, "bold", COLORS["text"], "middle"))
    
    # Círculo relleno
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{COLORS["circle_fill"]}" stroke="{COLORS["circle_stroke"]}" stroke-width="3"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx - 15, cy + 5, "O", 12, "bold", COLORS["center"]))
    
    # Radio
    pr = point_on_circle(cx, cy, r, 40)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{pr[0]:.2f}" y2="{pr[1]:.2f}" stroke="{COLORS["radius"]}" stroke-width="2.5"/>')
    svg.append(text_element((cx + pr[0])/2 + 10, (cy + pr[1])/2 - 8, "r", 14, "bold", COLORS["radius"]))
    
    # Fórmula
    svg.append(f'<rect x="320" y="120" width="160" height="120" rx="12" fill="white" stroke="{COLORS["circle_stroke"]}" stroke-width="2"/>')
    svg.append(text_element(400, 148, "FÓRMULA", 13, "bold", COLORS["text"], "middle"))
    
    svg.append(text_element(400, 195, "A = πr²", 24, "bold", COLORS["circle_stroke"], "middle"))
    svg.append(text_element(400, 225, "π ≈ 3.14159...", 10, "normal", COLORS["auxiliary"], "middle"))
    
    # Nota
    svg.append(label_box(50, 330, 400, 35, "El círculo es la región interior", COLORS["segment_fill"], COLORS["auxiliary"]))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_formula_sector_area(width=SIZE_SIMPLE[0], height=SIZE_SIMPLE[1]):
    """Fórmula del área del sector circular."""
    cx, cy, r = 180, 180, 100
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Área del Sector", 18, "bold", COLORS["arc"], "middle"))
    
    # Circunferencia base (tenue)
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["auxiliary"]}" stroke-width="1.5" stroke-dasharray="4,4"/>')
    
    # Sector
    sector = sector_path(cx, cy, r, 20, 110)
    svg.append(f'<path d="{sector}" fill="{COLORS["sector_fill"]}" stroke="{COLORS["arc"]}" stroke-width="2.5"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLORS["center"]}"/>')
    
    # Ángulo
    arc_angle = angle_arc_path(cx, cy, 30, 20, 110)
    svg.append(f'<path d="{arc_angle}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
    svg.append(text_element(cx + 40, cy - 25, "θ", 14, "bold", COLORS["angle"]))
    
    # Radio
    svg.append(text_element(cx + 50, cy + 30, "r", 14, "bold", COLORS["radius"]))
    
    # Fórmulas
    svg.append(f'<rect x="280" y="100" width="150" height="140" rx="10" fill="white" stroke="{COLORS["arc"]}" stroke-width="2"/>')
    svg.append(text_element(355, 125, "FÓRMULAS", 12, "bold", COLORS["text"], "middle"))
    
    svg.append(text_element(355, 160, "θ en grados:", 10, "normal", COLORS["auxiliary"], "middle"))
    svg.append(text_element(355, 182, "A = (θ/360)·πr²", 13, "bold", COLORS["text"], "middle"))
    
    svg.append(text_element(355, 210, "θ en radianes:", 10, "normal", COLORS["auxiliary"], "middle"))
    svg.append(text_element(355, 232, "A = ½r²θ", 13, "bold", COLORS["text"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


def generate_formula_segment_area(width=SIZE_HORIZONTAL[0], height=SIZE_HORIZONTAL[1]):
    """
    Fórmula del área del segmento circular.
    
    PEDAGOGÍA:
    - Mostrar claramente: SEGMENTO = SECTOR - TRIÁNGULO
    - Dibujar el triángulo (formado por los dos radios y la cuerda)
    - El segmento es la "media luna" entre cuerda y arco
    
    NOTA: Usa SIZE_HORIZONTAL (750x420) para mejor distribución
    """
    
    svg = [svg_header(width, height)]
    svg.append(text_element(width/2, 30, "Área del Segmento Circular", 18, "bold", COLORS["chord"], "middle"))
    
    # Distribución horizontal: 3 círculos equidistantes en 750px
    # Posiciones: 140, 375, 610 (separación de ~235px)
    circle_y = 185  # Centro vertical de los círculos
    r = 85  # Radio ligeramente mayor para mejor visibilidad
    angle_start, angle_end = 30, 150
    
    # === LADO IZQUIERDO: SECTOR completo ===
    cx1 = 140
    
    # Sector (área amarilla)
    sector = sector_path(cx1, circle_y, r, angle_start, angle_end)
    svg.append(f'<path d="{sector}" fill="{COLORS["sector_fill"]}" stroke="{COLORS["arc"]}" stroke-width="2"/>')
    
    # Centro
    svg.append(f'<circle cx="{cx1}" cy="{circle_y}" r="4" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx1 - 12, circle_y + 5, "O", 11, "bold", COLORS["center"]))
    
    # Puntos
    pA1 = point_on_circle(cx1, circle_y, r, angle_end)
    pB1 = point_on_circle(cx1, circle_y, r, angle_start)
    svg.append(f'<circle cx="{pA1[0]:.1f}" cy="{pA1[1]:.1f}" r="3" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pB1[0]:.1f}" cy="{pB1[1]:.1f}" r="3" fill="{COLORS["point"]}"/>')
    
    svg.append(text_element(cx1, circle_y + r + 25, "SECTOR", 12, "bold", COLORS["arc"], "middle"))
    
    # === SÍMBOLO MENOS ===
    svg.append(text_element(245, circle_y + 5, "−", 32, "bold", COLORS["text"]))
    
    # === CENTRO: TRIÁNGULO ===
    cx2 = 375
    
    # Circunferencia tenue
    svg.append(f'<circle cx="{cx2}" cy="{circle_y}" r="{r}" fill="none" stroke="{COLORS["auxiliary"]}" stroke-width="1" stroke-dasharray="4,4"/>')
    
    # Triángulo (formado por O, A, B)
    pA2 = point_on_circle(cx2, circle_y, r, angle_end)
    pB2 = point_on_circle(cx2, circle_y, r, angle_start)
    
    svg.append(f'<polygon points="{cx2},{circle_y} {pA2[0]:.1f},{pA2[1]:.1f} {pB2[0]:.1f},{pB2[1]:.1f}" fill="{COLORS["radius"]}" fill-opacity="0.2" stroke="{COLORS["radius"]}" stroke-width="2"/>')
    
    # Centro y puntos
    svg.append(f'<circle cx="{cx2}" cy="{circle_y}" r="4" fill="{COLORS["center"]}"/>')
    svg.append(text_element(cx2 - 12, circle_y + 5, "O", 11, "bold", COLORS["center"]))
    svg.append(f'<circle cx="{pA2[0]:.1f}" cy="{pA2[1]:.1f}" r="3" fill="{COLORS["point"]}"/>')
    svg.append(f'<circle cx="{pB2[0]:.1f}" cy="{pB2[1]:.1f}" r="3" fill="{COLORS["point"]}"/>')
    svg.append(text_element(pA2[0] - 15, pA2[1] - 5, "A", 11, "bold", COLORS["point"]))
    svg.append(text_element(pB2[0] + 8, pB2[1] - 5, "B", 11, "bold", COLORS["point"]))
    
    svg.append(text_element(cx2, circle_y + r + 25, "TRIÁNGULO OAB", 12, "bold", COLORS["radius"], "middle"))
    
    # === SÍMBOLO IGUAL ===
    svg.append(text_element(480, circle_y + 5, "=", 32, "bold", COLORS["text"]))
    
    # === LADO DERECHO: SEGMENTO (resultado) ===
    cx3 = 610
    
    # Circunferencia tenue
    svg.append(f'<circle cx="{cx3}" cy="{circle_y}" r="{r}" fill="none" stroke="{COLORS["auxiliary"]}" stroke-width="1" stroke-dasharray="4,4"/>')
    
    # Segmento (solo el área verde entre cuerda y arco)
    segment = segment_path(cx3, circle_y, r, angle_start, angle_end)
    svg.append(f'<path d="{segment}" fill="{COLORS["segment_fill"]}" stroke="{COLORS["chord"]}" stroke-width="3"/>')
    
    # Cuerda
    pA3 = point_on_circle(cx3, circle_y, r, angle_end)
    pB3 = point_on_circle(cx3, circle_y, r, angle_start)
    svg.append(f'<line x1="{pA3[0]:.1f}" y1="{pA3[1]:.1f}" x2="{pB3[0]:.1f}" y2="{pB3[1]:.1f}" stroke="{COLORS["chord"]}" stroke-width="2"/>')
    
    # Centro (referencia)
    svg.append(f'<circle cx="{cx3}" cy="{circle_y}" r="3" fill="{COLORS["auxiliary"]}"/>')
    
    svg.append(text_element(cx3, circle_y + r + 25, "SEGMENTO", 12, "bold", COLORS["chord"], "middle"))
    
    # === FÓRMULA DESTACADA (ajustada para viewBox 750x420) ===
    svg.append(f'<rect x="125" y="320" width="500" height="85" rx="12" fill="white" stroke="{COLORS["chord"]}" stroke-width="2"/>')
    svg.append(text_element(375, 348, "A(SEGMENTO) = A(SECTOR) − A(TRIÁNGULO)", 15, "bold", COLORS["text"], "middle"))
    svg.append(text_element(375, 373, "El TRIÁNGULO está formado por los 2 radios (OA, OB) y la cuerda (AB)", 11, "normal", COLORS["auxiliary"], "middle"))
    svg.append(text_element(375, 395, "A(△) = ½ · r² · sin(θ)", 12, "normal", COLORS["text"], "middle"))
    
    svg.append(svg_footer())
    return '\n'.join(svg)


# ============================================================================
# DISPATCHER
# ============================================================================

GENERATORS = {
    # Básicos
    'basic': generate_basic,
    
    # Elementos individuales
    'element_radius': generate_element_radius,
    'element_diameter': generate_element_diameter,
    'element_chord': generate_element_chord,
    'element_arc': generate_element_arc,
    'element_sector': generate_element_sector,
    'element_segment': generate_element_segment,
    'element_crown': generate_element_crown,
    
    # Posiciones
    'point_positions': generate_point_positions,
    'tangent_secant': generate_tangent_secant,
    'circle_positions': generate_circle_positions,
    
    # Ángulos
    'angle_central': generate_angle_central,
    'angle_inscribed': generate_angle_inscribed,
    'angle_semi_inscribed': generate_angle_semi_inscribed,
    'angle_interior': generate_angle_interior,
    'angle_exterior': generate_angle_exterior,
    
    # Teoremas
    'theorem_inscribed': generate_theorem_inscribed,
    'theorem_tales': generate_theorem_tales,
    
    # Fórmulas
    'formula_length': generate_formula_length,
    'formula_area': generate_formula_area,
    'formula_sector_area': generate_formula_sector_area,
    'formula_segment_area': generate_formula_segment_area,
    
    # Compatibilidad con nombres anteriores
    'elements': lambda: generate_element_radius(),  # Deprecated
    'central_angle': generate_angle_central,
    'inscribed_angle': generate_angle_inscribed,
    'inscribed_theorem': generate_theorem_inscribed,
    'length_formula': generate_formula_length,
    'area_formula': generate_formula_area,
}


def main():
    parser = argparse.ArgumentParser(description='Circle Renderer v2.0 - Ilustraciones de Circunferencia y Círculo')
    parser.add_argument('--type', choices=list(GENERATORS.keys()), required=True,
                       help='Tipo de ilustración a generar')
    parser.add_argument('--output', required=True, help='Archivo SVG de salida')
    
    args = parser.parse_args()
    
    generator = GENERATORS.get(args.type)
    if not generator:
        print(f"❌ Tipo desconocido: {args.type}")
        return 1
    
    svg_content = generator()
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg_content)
    
    print(f"✅ SVG generado: {args.output}")
    return 0


if __name__ == '__main__':
    exit(main())

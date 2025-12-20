#!/usr/bin/env python3
"""
📐 Oblique Triangle Renderer - Ilustraciones para triángulos oblicuángulos

Genera SVGs educativos de:
- Triángulos acutángulos y obtusángulos
- Ley de Senos
- Ley de Cosenos
- Casos de resolución (ALA, LAL, LLL, LLA)
- Aplicaciones (navegación, distancia)

Uso:
    python scripts/geometry/oblique_triangle_renderer.py --type TYPE --output archivo.svg
"""

import argparse
import math
import sys
from pathlib import Path

# Importar paleta de colores centralizada
sys.path.insert(0, str(Path(__file__).parent))
from core.colors import COLORS as BASE_COLORS

# Paleta de colores (basada en core.colors)
COLORS = {
    'background': BASE_COLORS['background'],
    'text': BASE_COLORS['text'],
    'side_a': BASE_COLORS['accent'],     # Rojo
    'side_b': BASE_COLORS['primary'],    # Azul  
    'side_c': BASE_COLORS['secondary'],  # Verde
    'angle_A': BASE_COLORS['accent'],    # Rojo (opuesto a 'a')
    'angle_B': BASE_COLORS['primary'],   # Azul (opuesto a 'b')
    'angle_C': BASE_COLORS['secondary'], # Verde (opuesto a 'c')
    'vertex': BASE_COLORS['text'],
    'auxiliary': BASE_COLORS['auxiliary'],
    'highlight': BASE_COLORS['highlight'],
    'box_bg': BASE_COLORS['grid'],
    'box_border': '#e2e8f0',
}


def draw_triangle(cx, cy, vertices, svg_parts, labels=None, colors=None, show_angles=True, angle_radius=25):
    """Dibuja un triángulo con vértices, lados y ángulos etiquetados."""
    A, B, C = vertices
    
    # Triángulo
    svg_parts.append(f'<polygon points="{A[0]:.1f},{A[1]:.1f} {B[0]:.1f},{B[1]:.1f} {C[0]:.1f},{C[1]:.1f}" '
                    f'fill="{COLORS["box_bg"]}" stroke="{COLORS["vertex"]}" stroke-width="3" stroke-linejoin="round"/>')
    
    # Vértices
    for v in [A, B, C]:
        svg_parts.append(f'<circle cx="{v[0]:.1f}" cy="{v[1]:.1f}" r="5" fill="{COLORS["vertex"]}"/>')
    
    if labels:
        # Etiquetas de vértices
        offsets = [(-15, -10), (15, -10), (0, 25)]
        for i, (v, label, offset) in enumerate(zip([A, B, C], ['A', 'B', 'C'], offsets)):
            svg_parts.append(f'<text x="{v[0] + offset[0]:.1f}" y="{v[1] + offset[1]:.1f}" '
                           f'text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["vertex"]}">{label}</text>')
        
        # Etiquetas de lados
        mid_a = ((B[0] + C[0])/2, (B[1] + C[1])/2)
        mid_b = ((A[0] + C[0])/2, (A[1] + C[1])/2)
        mid_c = ((A[0] + B[0])/2, (A[1] + B[1])/2)
        
        svg_parts.append(f'<text x="{mid_a[0] + 15:.1f}" y="{mid_a[1]:.1f}" font-size="16" font-weight="bold" fill="{COLORS["side_a"]}">a</text>')
        svg_parts.append(f'<text x="{mid_b[0] - 15:.1f}" y="{mid_b[1]:.1f}" font-size="16" font-weight="bold" fill="{COLORS["side_b"]}">b</text>')
        svg_parts.append(f'<text x="{mid_c[0]:.1f}" y="{mid_c[1] + 20:.1f}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["side_c"]}">c</text>')


def generate_types_comparison(width=700, height=400) -> str:
    """Genera comparación de triángulo acutángulo vs obtusángulo."""
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Tipos de Triángulos Oblicuángulos</text>',
        '',
    ]
    
    # Triángulo acutángulo (izquierda)
    svg_parts.append('<!-- Triángulo Acutángulo -->')
    svg_parts.append(f'<text x="175" y="70" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["side_b"]}">ACUTÁNGULO</text>')
    svg_parts.append(f'<text x="175" y="88" text-anchor="middle" font-size="11" fill="{COLORS["auxiliary"]}">Todos los ángulos &lt; 90°</text>')
    
    # Coordenadas del acutángulo
    A1 = (80, 320)
    B1 = (270, 320)
    C1 = (175, 130)
    
    svg_parts.append(f'<polygon points="{A1[0]},{A1[1]} {B1[0]},{B1[1]} {C1[0]},{C1[1]}" '
                    f'fill="{COLORS["side_b"]}" fill-opacity="0.15" stroke="{COLORS["side_b"]}" stroke-width="3" stroke-linejoin="round"/>')
    
    for v, label in [(A1, 'A'), (B1, 'B'), (C1, 'C')]:
        svg_parts.append(f'<circle cx="{v[0]}" cy="{v[1]}" r="5" fill="{COLORS["vertex"]}"/>')
    
    svg_parts.append(f'<text x="{A1[0] - 15}" y="{A1[1] + 5}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">65°</text>')
    svg_parts.append(f'<text x="{B1[0] + 10}" y="{B1[1] + 5}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">55°</text>')
    svg_parts.append(f'<text x="{C1[0]}" y="{C1[1] - 15}" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["text"]}">60°</text>')
    
    svg_parts.append(f'<text x="175" y="360" text-anchor="middle" font-size="11" fill="{COLORS["auxiliary"]}">65° + 55° + 60° = 180°</text>')
    
    # Triángulo obtusángulo (derecha)
    svg_parts.append('<!-- Triángulo Obtusángulo -->')
    svg_parts.append(f'<text x="525" y="70" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["side_a"]}">OBTUSÁNGULO</text>')
    svg_parts.append(f'<text x="525" y="88" text-anchor="middle" font-size="11" fill="{COLORS["auxiliary"]}">Un ángulo &gt; 90°</text>')
    
    # Coordenadas del obtusángulo
    A2 = (380, 320)
    B2 = (670, 320)
    C2 = (420, 150)
    
    svg_parts.append(f'<polygon points="{A2[0]},{A2[1]} {B2[0]},{B2[1]} {C2[0]},{C2[1]}" '
                    f'fill="{COLORS["side_a"]}" fill-opacity="0.15" stroke="{COLORS["side_a"]}" stroke-width="3" stroke-linejoin="round"/>')
    
    for v in [A2, B2, C2]:
        svg_parts.append(f'<circle cx="{v[0]}" cy="{v[1]}" r="5" fill="{COLORS["vertex"]}"/>')
    
    svg_parts.append(f'<text x="{A2[0] + 25}" y="{A2[1] - 25}" font-size="13" font-weight="bold" fill="{COLORS["side_a"]}">110°</text>')
    svg_parts.append(f'<text x="{B2[0] - 10}" y="{B2[1] + 5}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">30°</text>')
    svg_parts.append(f'<text x="{C2[0] - 20}" y="{C2[1] + 5}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">40°</text>')
    
    svg_parts.append(f'<text x="525" y="360" text-anchor="middle" font-size="11" fill="{COLORS["auxiliary"]}">110° + 30° + 40° = 180°</text>')
    
    # Línea divisoria
    svg_parts.append(f'<line x1="{width/2}" y1="60" x2="{width/2}" y2="380" stroke="{COLORS["auxiliary"]}" stroke-width="1" stroke-dasharray="5,3"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_law_of_sines(width=650, height=450) -> str:
    """Genera ilustración de la Ley de Senos."""
    cx = width / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{cx}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Ley de Senos</text>',
        '',
    ]
    
    # Triángulo
    A = (100, 350)
    B = (400, 350)
    C = (250, 120)
    
    svg_parts.append(f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" '
                    f'fill="{COLORS["box_bg"]}" stroke="{COLORS["vertex"]}" stroke-width="3" stroke-linejoin="round"/>')
    
    # Vértices
    for v, label, offset in [(A, 'A', (-20, 15)), (B, 'B', (15, 15)), (C, 'C', (0, -15))]:
        svg_parts.append(f'<circle cx="{v[0]}" cy="{v[1]}" r="6" fill="{COLORS["vertex"]}"/>')
        svg_parts.append(f'<text x="{v[0] + offset[0]}" y="{v[1] + offset[1]}" font-size="16" font-weight="bold" fill="{COLORS["vertex"]}">{label}</text>')
    
    # Lados con colores
    # Lado a (opuesto a A) = BC
    svg_parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["side_a"]}" stroke-width="4"/>')
    svg_parts.append(f'<text x="{(B[0]+C[0])/2 + 20}" y="{(B[1]+C[1])/2}" font-size="18" font-weight="bold" fill="{COLORS["side_a"]}">a</text>')
    
    # Lado b (opuesto a B) = AC
    svg_parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["side_b"]}" stroke-width="4"/>')
    svg_parts.append(f'<text x="{(A[0]+C[0])/2 - 25}" y="{(A[1]+C[1])/2}" font-size="18" font-weight="bold" fill="{COLORS["side_b"]}">b</text>')
    
    # Lado c (opuesto a C) = AB
    svg_parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{COLORS["side_c"]}" stroke-width="4"/>')
    svg_parts.append(f'<text x="{(A[0]+B[0])/2}" y="{(A[1]+B[1])/2 + 25}" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["side_c"]}">c</text>')
    
    # Fórmula principal
    svg_parts.append(f'<rect x="450" y="80" width="180" height="120" rx="10" fill="white" stroke="{COLORS["box_border"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="540" y="110" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["text"]}">LEY DE SENOS</text>')
    svg_parts.append(f'<text x="540" y="145" text-anchor="middle" font-size="14" fill="{COLORS["side_a"]}">a/sin A</text>')
    svg_parts.append(f'<text x="540" y="165" text-anchor="middle" font-size="14" fill="{COLORS["text"]}">=</text>')
    svg_parts.append(f'<text x="490" y="185" text-anchor="middle" font-size="14" fill="{COLORS["side_b"]}">b/sin B</text>')
    svg_parts.append(f'<text x="540" y="185" text-anchor="middle" font-size="14" fill="{COLORS["text"]}">=</text>')
    svg_parts.append(f'<text x="590" y="185" text-anchor="middle" font-size="14" fill="{COLORS["side_c"]}">c/sin C</text>')
    
    # Explicación
    svg_parts.append(f'<rect x="450" y="220" width="180" height="80" rx="8" fill="{COLORS["box_bg"]}" stroke="{COLORS["box_border"]}"/>')
    svg_parts.append(f'<text x="460" y="245" font-size="10" fill="{COLORS["text"]}">💡 Cada lado dividido</text>')
    svg_parts.append(f'<text x="460" y="262" font-size="10" fill="{COLORS["text"]}">por el seno de su ángulo</text>')
    svg_parts.append(f'<text x="460" y="279" font-size="10" fill="{COLORS["text"]}">opuesto es constante.</text>')
    
    # Casos de uso
    svg_parts.append(f'<rect x="40" y="380" width="570" height="55" rx="8" fill="white" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="55" y="405" font-size="11" font-weight="bold" fill="{COLORS["highlight"]}">📋 USAR CUANDO:</text>')
    svg_parts.append(f'<text x="200" y="405" font-size="11" fill="{COLORS["text"]}">Caso ALA (2 ángulos + 1 lado)</text>')
    svg_parts.append(f'<text x="430" y="405" font-size="11" fill="{COLORS["text"]}">Caso LLA (con cuidado: caso ambiguo)</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_law_of_cosines(width=650, height=450) -> str:
    """Genera ilustración de la Ley de Cosenos."""
    cx = width / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{cx}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Ley de Cosenos</text>',
        f'<text x="{cx}" y="50" text-anchor="middle" font-size="11" fill="{COLORS["auxiliary"]}">Generalización del Teorema de Pitágoras</text>',
        '',
    ]
    
    # Triángulo (caso LAL: conocemos b, c y ángulo A)
    A = (80, 330)
    B = (350, 330)
    C = (200, 100)
    
    svg_parts.append(f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" '
                    f'fill="{COLORS["box_bg"]}" stroke="{COLORS["vertex"]}" stroke-width="3" stroke-linejoin="round"/>')
    
    # Vértices
    for v, label, offset in [(A, 'A', (-20, 15)), (B, 'B', (15, 15)), (C, 'C', (0, -15))]:
        svg_parts.append(f'<circle cx="{v[0]}" cy="{v[1]}" r="6" fill="{COLORS["vertex"]}"/>')
        svg_parts.append(f'<text x="{v[0] + offset[0]}" y="{v[1] + offset[1]}" font-size="16" font-weight="bold" fill="{COLORS["vertex"]}">{label}</text>')
    
    # Lado a (opuesto a A, lo que buscamos) = BC - punteado
    svg_parts.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["side_a"]}" stroke-width="4" stroke-dasharray="8,4"/>')
    svg_parts.append(f'<text x="{(B[0]+C[0])/2 + 20}" y="{(B[1]+C[1])/2}" font-size="18" font-weight="bold" fill="{COLORS["side_a"]}">a = ?</text>')
    
    # Lado b (conocido) = AC
    svg_parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{COLORS["side_b"]}" stroke-width="4"/>')
    svg_parts.append(f'<text x="{(A[0]+C[0])/2 - 25}" y="{(A[1]+C[1])/2}" font-size="18" font-weight="bold" fill="{COLORS["side_b"]}">b</text>')
    
    # Lado c (conocido) = AB
    svg_parts.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{COLORS["side_c"]}" stroke-width="4"/>')
    svg_parts.append(f'<text x="{(A[0]+B[0])/2}" y="{(A[1]+B[1])/2 + 25}" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["side_c"]}">c</text>')
    
    # Arco del ángulo A (conocido)
    svg_parts.append(f'<path d="M {A[0] + 40} {A[1]} A 40 40 0 0 0 {A[0] + 25} {A[1] - 30}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="3"/>')
    svg_parts.append(f'<text x="{A[0] + 55}" y="{A[1] - 15}" font-size="14" font-weight="bold" fill="{COLORS["highlight"]}">A</text>')
    
    # Fórmula principal
    svg_parts.append(f'<rect x="400" y="70" width="230" height="100" rx="10" fill="white" stroke="{COLORS["side_a"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="515" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["text"]}">LEY DE COSENOS</text>')
    svg_parts.append(f'<text x="515" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["side_a"]}">a² = b² + c² - 2bc·cos A</text>')
    svg_parts.append(f'<text x="515" y="155" text-anchor="middle" font-size="10" fill="{COLORS["auxiliary"]}">Si A = 90°, cos A = 0 → Pitágoras</text>')
    
    # Todas las formas
    svg_parts.append(f'<rect x="400" y="185" width="230" height="90" rx="8" fill="{COLORS["box_bg"]}" stroke="{COLORS["box_border"]}"/>')
    svg_parts.append(f'<text x="515" y="208" text-anchor="middle" font-size="10" font-weight="bold" fill="{COLORS["text"]}">LAS 3 FORMAS:</text>')
    svg_parts.append(f'<text x="410" y="228" font-size="11" fill="{COLORS["side_a"]}">a² = b² + c² - 2bc·cos A</text>')
    svg_parts.append(f'<text x="410" y="248" font-size="11" fill="{COLORS["side_b"]}">b² = a² + c² - 2ac·cos B</text>')
    svg_parts.append(f'<text x="410" y="268" font-size="11" fill="{COLORS["side_c"]}">c² = a² + b² - 2ab·cos C</text>')
    
    # Casos de uso
    svg_parts.append(f'<rect x="40" y="380" width="570" height="55" rx="8" fill="white" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="55" y="405" font-size="11" font-weight="bold" fill="{COLORS["highlight"]}">📋 USAR CUANDO:</text>')
    svg_parts.append(f'<text x="200" y="405" font-size="11" fill="{COLORS["text"]}">Caso LAL (2 lados + ángulo entre ellos)</text>')
    svg_parts.append(f'<text x="450" y="405" font-size="11" fill="{COLORS["text"]}">Caso LLL (3 lados → encontrar ángulos)</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_cases_summary(width=750, height=500) -> str:
    """Genera resumen de los 4 casos de resolución."""
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Los 4 Casos de Resolución de Triángulos</text>',
        '',
    ]
    
    cases = [
        # (x, y, nombre, color, datos, herramienta, descripcion)
        (30, 60, "ALA", COLORS["side_b"], "2 ángulos + 1 lado", "Ley de Senos", "Siempre solución única"),
        (390, 60, "LAL", COLORS["side_c"], "2 lados + ángulo entre ellos", "Ley de Cosenos", "Siempre solución única"),
        (30, 280, "LLL", COLORS["highlight"], "3 lados", "Ley de Cosenos", "Siempre solución única"),
        (390, 280, "LLA", COLORS["side_a"], "2 lados + ángulo opuesto", "Ley de Senos", "⚠️ CASO AMBIGUO"),
    ]
    
    for x, y, nombre, color, datos, herramienta, descripcion in cases:
        # Caja del caso
        svg_parts.append(f'<rect x="{x}" y="{y}" width="330" height="190" rx="12" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-width="2"/>')
        
        # Nombre del caso
        svg_parts.append(f'<text x="{x + 165}" y="{y + 30}" text-anchor="middle" font-size="22" font-weight="bold" fill="{color}">{nombre}</text>')
        
        # Línea separadora
        svg_parts.append(f'<line x1="{x + 20}" y1="{y + 45}" x2="{x + 310}" y2="{y + 45}" stroke="{color}" stroke-width="1" opacity="0.5"/>')
        
        # Mini triángulo ilustrativo
        tri_cx = x + 80
        tri_cy = y + 110
        
        if nombre == "ALA":
            # Mostrar 2 ángulos conocidos
            svg_parts.append(f'<polygon points="{tri_cx - 40},{tri_cy + 40} {tri_cx + 50},{tri_cy + 40} {tri_cx},{tri_cy - 30}" '
                           f'fill="white" stroke="{color}" stroke-width="2"/>')
            svg_parts.append(f'<text x="{tri_cx - 25}" y="{tri_cy + 35}" font-size="10" fill="{color}">A✓</text>')
            svg_parts.append(f'<text x="{tri_cx + 35}" y="{tri_cy + 35}" font-size="10" fill="{color}">B✓</text>')
            svg_parts.append(f'<text x="{tri_cx}" y="{tri_cy + 55}" text-anchor="middle" font-size="10" fill="{color}">c✓</text>')
        elif nombre == "LAL":
            svg_parts.append(f'<polygon points="{tri_cx - 40},{tri_cy + 40} {tri_cx + 50},{tri_cy + 40} {tri_cx},{tri_cy - 30}" '
                           f'fill="white" stroke="{color}" stroke-width="2"/>')
            svg_parts.append(f'<text x="{tri_cx - 30}" y="{tri_cy + 10}" font-size="10" fill="{color}">b✓</text>')
            svg_parts.append(f'<text x="{tri_cx - 25}" y="{tri_cy + 35}" font-size="10" fill="{color}">A✓</text>')
            svg_parts.append(f'<text x="{tri_cx}" y="{tri_cy + 55}" text-anchor="middle" font-size="10" fill="{color}">c✓</text>')
        elif nombre == "LLL":
            svg_parts.append(f'<polygon points="{tri_cx - 40},{tri_cy + 40} {tri_cx + 50},{tri_cy + 40} {tri_cx},{tri_cy - 30}" '
                           f'fill="white" stroke="{color}" stroke-width="2"/>')
            svg_parts.append(f'<text x="{tri_cx + 30}" y="{tri_cy + 10}" font-size="10" fill="{color}">a✓</text>')
            svg_parts.append(f'<text x="{tri_cx - 30}" y="{tri_cy + 10}" font-size="10" fill="{color}">b✓</text>')
            svg_parts.append(f'<text x="{tri_cx}" y="{tri_cy + 55}" text-anchor="middle" font-size="10" fill="{color}">c✓</text>')
        else:  # LLA
            svg_parts.append(f'<polygon points="{tri_cx - 40},{tri_cy + 40} {tri_cx + 50},{tri_cy + 40} {tri_cx},{tri_cy - 30}" '
                           f'fill="white" stroke="{color}" stroke-width="2"/>')
            svg_parts.append(f'<text x="{tri_cx + 30}" y="{tri_cy + 10}" font-size="10" fill="{color}">a✓</text>')
            svg_parts.append(f'<text x="{tri_cx - 30}" y="{tri_cy + 10}" font-size="10" fill="{color}">b✓</text>')
            svg_parts.append(f'<text x="{tri_cx - 25}" y="{tri_cy + 35}" font-size="10" fill="{color}">A✓</text>')
        
        # Info del caso
        svg_parts.append(f'<text x="{x + 170}" y="{y + 80}" font-size="11" fill="{COLORS["text"]}">📊 {datos}</text>')
        svg_parts.append(f'<text x="{x + 170}" y="{y + 100}" font-size="11" fill="{COLORS["text"]}">🔧 {herramienta}</text>')
        
        # Descripción
        svg_parts.append(f'<rect x="{x + 150}" y="{y + 115}" width="160" height="30" rx="6" fill="white" stroke="{COLORS["box_border"]}"/>')
        svg_parts.append(f'<text x="{x + 230}" y="{y + 135}" text-anchor="middle" font-size="10" fill="{COLORS["text"]}">{descripcion}</text>')
        
        # Número de soluciones
        if nombre == "LLA":
            svg_parts.append(f'<text x="{x + 165}" y="{y + 170}" text-anchor="middle" font-size="9" fill="{COLORS["side_a"]}">0, 1 o 2 soluciones</text>')
    
    # Nota al pie
    svg_parts.append(f'<text x="{width/2}" y="485" text-anchor="middle" font-size="10" fill="{COLORS["auxiliary"]}">💡 Siempre necesitas al menos 3 datos incluyendo al menos 1 lado para resolver un triángulo</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_navigation_app(width=650, height=450) -> str:
    """Genera ilustración de aplicación de navegación."""
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Aplicación: Navegación</text>',
        f'<text x="{width/2}" y="50" text-anchor="middle" font-size="11" fill="{COLORS["auxiliary"]}">Calcular distancia entre dos barcos</text>',
        '',
    ]
    
    # Puerto (origen)
    puerto = (150, 350)
    svg_parts.append(f'<circle cx="{puerto[0]}" cy="{puerto[1]}" r="10" fill="{COLORS["vertex"]}"/>')
    svg_parts.append(f'<text x="{puerto[0]}" y="{puerto[1] + 25}" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["vertex"]}">Puerto</text>')
    
    # Barco 1 (norte)
    barco1 = (150, 120)
    svg_parts.append(f'<circle cx="{barco1[0]}" cy="{barco1[1]}" r="8" fill="{COLORS["side_b"]}"/>')
    svg_parts.append(f'<text x="{barco1[0] - 40}" y="{barco1[1] + 5}" font-size="11" font-weight="bold" fill="{COLORS["side_b"]}">Barco 1</text>')
    
    # Barco 2 (N60°E)
    barco2 = (450, 200)
    svg_parts.append(f'<circle cx="{barco2[0]}" cy="{barco2[1]}" r="8" fill="{COLORS["side_c"]}"/>')
    svg_parts.append(f'<text x="{barco2[0] + 15}" y="{barco2[1] + 5}" font-size="11" font-weight="bold" fill="{COLORS["side_c"]}">Barco 2</text>')
    
    # Trayectoria Barco 1 (norte)
    svg_parts.append(f'<line x1="{puerto[0]}" y1="{puerto[1]}" x2="{barco1[0]}" y2="{barco1[1]}" stroke="{COLORS["side_b"]}" stroke-width="3"/>')
    svg_parts.append(f'<text x="{puerto[0] - 30}" y="{(puerto[1] + barco1[1])/2}" font-size="12" font-weight="bold" fill="{COLORS["side_b"]}">80 km</text>')
    
    # Trayectoria Barco 2 (N60°E)
    svg_parts.append(f'<line x1="{puerto[0]}" y1="{puerto[1]}" x2="{barco2[0]}" y2="{barco2[1]}" stroke="{COLORS["side_c"]}" stroke-width="3"/>')
    svg_parts.append(f'<text x="{(puerto[0] + barco2[0])/2 - 10}" y="{(puerto[1] + barco2[1])/2 + 20}" font-size="12" font-weight="bold" fill="{COLORS["side_c"]}">60 km</text>')
    
    # Distancia entre barcos (lo que buscamos)
    svg_parts.append(f'<line x1="{barco1[0]}" y1="{barco1[1]}" x2="{barco2[0]}" y2="{barco2[1]}" stroke="{COLORS["side_a"]}" stroke-width="3" stroke-dasharray="8,4"/>')
    svg_parts.append(f'<text x="{(barco1[0] + barco2[0])/2 + 10}" y="{(barco1[1] + barco2[1])/2 - 10}" font-size="14" font-weight="bold" fill="{COLORS["side_a"]}">d = ?</text>')
    
    # Ángulo
    svg_parts.append(f'<path d="M {puerto[0]} {puerto[1] - 50} A 50 50 0 0 1 {puerto[0] + 43} {puerto[1] - 25}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="{puerto[0] + 35}" y="{puerto[1] - 50}" font-size="12" font-weight="bold" fill="{COLORS["highlight"]}">60°</text>')
    
    # Norte indicador
    svg_parts.append(f'<line x1="{puerto[0]}" y1="{puerto[1] - 20}" x2="{puerto[0]}" y2="{puerto[1] - 70}" stroke="{COLORS["auxiliary"]}" stroke-width="1" stroke-dasharray="3,2"/>')
    svg_parts.append(f'<text x="{puerto[0]}" y="{puerto[1] - 75}" text-anchor="middle" font-size="10" fill="{COLORS["auxiliary"]}">N</text>')
    
    # Solución
    svg_parts.append(f'<rect x="470" y="280" width="160" height="140" rx="10" fill="white" stroke="{COLORS["box_border"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="550" y="305" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["text"]}">📐 SOLUCIÓN (LAL)</text>')
    svg_parts.append(f'<text x="480" y="330" font-size="10" fill="{COLORS["text"]}">d² = 80² + 60²</text>')
    svg_parts.append(f'<text x="480" y="350" font-size="10" fill="{COLORS["text"]}">    - 2(80)(60)cos 60°</text>')
    svg_parts.append(f'<text x="480" y="375" font-size="10" fill="{COLORS["text"]}">d² = 6400 + 3600 - 4800</text>')
    svg_parts.append(f'<text x="480" y="395" font-size="10" fill="{COLORS["text"]}">d² = 5200</text>')
    svg_parts.append(f'<text x="550" y="415" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["side_a"]}">d ≈ 72.1 km</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


# Diccionario de generadores
GENERATORS = {
    'types': generate_types_comparison,
    'sines': generate_law_of_sines,
    'cosines': generate_law_of_cosines,
    'cases': generate_cases_summary,
    'navigation': generate_navigation_app,
}


def main():
    parser = argparse.ArgumentParser(description='Oblique Triangle Renderer')
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


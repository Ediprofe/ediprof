#!/usr/bin/env python3
"""
🔵 Unit Circle Renderer - Ilustraciones del círculo unitario

Genera SVGs educativos del círculo unitario con:
- Ejes coordenados
- Puntos clave (0°, 30°, 45°, 60°, 90°, etc.)
- Cuadrantes con signos
- Ángulos y sus valores

Uso:
    python scripts/geometry/unit_circle_renderer.py --type basic --output archivo.svg
    python scripts/geometry/unit_circle_renderer.py --type quadrants --output archivo.svg
"""

import argparse
import math
from pathlib import Path
from typing import List, Tuple

# Importar desde core unificado
from core import COLORS, format_angle

# Constantes
PI = math.pi


def format_angle_label(degrees: float) -> str:
    """Formatea un ángulo en grados para mostrar."""
    return format_angle(degrees)

def generate_basic_unit_circle(width=600, height=500) -> str:
    """Genera el círculo unitario básico con ejes y puntos cuadrantales."""
    cx, cy = width / 2, height / 2 + 20
    radius = min(width, height) / 2 - 80
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">El Círculo Unitario</text>',
        f'<text x="{width/2}" y="50" text-anchor="middle" font-size="12" fill="#64748b">Radio = 1, Centro en el origen</text>',
        '',
        '<!-- Cuadrícula -->',
        f'<line x1="{cx - radius - 20}" y1="{cy}" x2="{cx + radius + 20}" y2="{cy}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 20}" x2="{cx}" y2="{cy + radius + 20}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        '',
        '<!-- Flechas de ejes -->',
        f'<polygon points="{cx + radius + 20},{cy} {cx + radius + 10},{cy - 5} {cx + radius + 10},{cy + 5}" fill="{COLORS["axis"]}"/>',
        f'<polygon points="{cx},{cy - radius - 20} {cx - 5},{cy - radius - 10} {cx + 5},{cy - radius - 10}" fill="{COLORS["axis"]}"/>',
        '',
        '<!-- Etiquetas de ejes -->',
        f'<text x="{cx + radius + 35}" y="{cy + 5}" font-size="14" font-weight="bold" fill="{COLORS["text"]}">x</text>',
        f'<text x="{cx + 8}" y="{cy - radius - 30}" font-size="14" font-weight="bold" fill="{COLORS["text"]}">y</text>',
        '',
        '<!-- Círculo unitario -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{COLORS["circle"]}" stroke-width="3"/>',
    ]
    
    # Puntos cuadrantales
    quadrantal_points = [
        (0, 1, 0, "(1, 0)", "right"),
        (90, 0, 1, "(0, 1)", "top"),
        (180, -1, 0, "(-1, 0)", "left"),
        (270, 0, -1, "(0, -1)", "bottom"),
    ]
    
    svg_parts.append('')
    svg_parts.append('<!-- Puntos cuadrantales -->')
    
    for angle_deg, cos_val, sin_val, label, pos in quadrantal_points:
        px = cx + cos_val * radius
        py = cy - sin_val * radius  # Invertido porque Y crece hacia abajo en SVG
        
        # Punto
        svg_parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="8" fill="{COLORS["point"]}" stroke="white" stroke-width="2"/>')
        
        # Etiqueta
        if pos == "right":
            svg_parts.append(f'<text x="{px + 15}" y="{py + 5}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">{label}</text>')
            svg_parts.append(f'<text x="{px + 15}" y="{py + 20}" font-size="11" fill="#64748b">{format_angle_label(angle_deg)}</text>')
        elif pos == "top":
            svg_parts.append(f'<text x="{px}" y="{py - 15}" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["text"]}">{label}</text>')
            svg_parts.append(f'<text x="{px}" y="{py - 30}" text-anchor="middle" font-size="11" fill="#64748b">{format_angle_label(angle_deg)}</text>')
        elif pos == "left":
            svg_parts.append(f'<text x="{px - 15}" y="{py + 5}" text-anchor="end" font-size="13" font-weight="bold" fill="{COLORS["text"]}">{label}</text>')
            svg_parts.append(f'<text x="{px - 15}" y="{py + 20}" text-anchor="end" font-size="11" fill="#64748b">{format_angle_label(angle_deg)}</text>')
        elif pos == "bottom":
            svg_parts.append(f'<text x="{px}" y="{py + 25}" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["text"]}">{label}</text>')
            svg_parts.append(f'<text x="{px}" y="{py + 40}" text-anchor="middle" font-size="11" fill="#64748b">{format_angle_label(angle_deg)}</text>')
    
    # Etiquetas de cuadrantes
    svg_parts.append('')
    svg_parts.append('<!-- Etiquetas de cuadrantes -->')
    quadrant_labels = [
        (cx + radius/2, cy - radius/2, "I", COLORS["quadrant_I"]),
        (cx - radius/2, cy - radius/2, "II", COLORS["quadrant_II"]),
        (cx - radius/2, cy + radius/2, "III", COLORS["quadrant_III"]),
        (cx + radius/2, cy + radius/2, "IV", COLORS["quadrant_IV"]),
    ]
    
    for x, y, label, color in quadrant_labels:
        svg_parts.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="24" font-weight="bold" fill="{color}" opacity="0.6">{label}</text>')
    
    # Leyenda
    svg_parts.append('')
    svg_parts.append('<!-- Leyenda -->')
    svg_parts.append(f'<rect x="20" y="{height - 70}" width="180" height="55" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>')
    svg_parts.append(f'<text x="30" y="{height - 50}" font-size="11" font-weight="bold" fill="{COLORS["text"]}">En el círculo unitario:</text>')
    svg_parts.append(f'<text x="30" y="{height - 33}" font-size="11" fill="{COLORS["cos_color"]}">• x = cos(θ)</text>')
    svg_parts.append(f'<text x="30" y="{height - 18}" font-size="11" fill="{COLORS["sin_color"]}">• y = sin(θ)</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_point_on_circle(width=600, height=500) -> str:
    """Genera ilustración del punto P = (cos θ, sin θ) en el círculo."""
    cx, cy = width / 2, height / 2 + 20
    radius = min(width, height) / 2 - 80
    
    # Ángulo de ejemplo (45°)
    theta = PI / 4
    px = cx + math.cos(theta) * radius
    py = cy - math.sin(theta) * radius
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">El Punto P = (cos θ, sin θ)</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 20}" y1="{cy}" x2="{cx + radius + 20}" y2="{cy}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 20}" x2="{cx}" y2="{cy + radius + 20}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{COLORS["circle"]}" stroke-width="2" stroke-dasharray="5,3"/>',
        '',
        '<!-- Radio al punto P -->',
        f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{COLORS["angle"]}" stroke-width="3"/>',
        '',
        '<!-- Proyecciones -->',
        f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{px:.1f}" y2="{cy}" stroke="{COLORS["sin_color"]}" stroke-width="2" stroke-dasharray="5,3"/>',
        f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{cy}" stroke="{COLORS["cos_color"]}" stroke-width="2" stroke-dasharray="5,3"/>',
        '',
        '<!-- Punto P -->',
        f'<circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{COLORS["point"]}" stroke="white" stroke-width="2"/>',
        '',
        '<!-- Arco del ángulo -->',
        f'<path d="M {cx + 40} {cy} A 40 40 0 0 0 {cx + 40 * math.cos(theta):.1f} {cy - 40 * math.sin(theta):.1f}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>',
        '',
        '<!-- Etiquetas -->',
        f'<text x="{px + 15:.1f}" y="{py - 10:.1f}" font-size="14" font-weight="bold" fill="{COLORS["point"]}">P = (cos θ, sin θ)</text>',
        f'<text x="{cx + 55}" y="{cy - 10}" font-size="13" font-weight="bold" fill="{COLORS["angle"]}">θ</text>',
        '',
        '<!-- Etiquetas de proyecciones -->',
        f'<text x="{(cx + px)/2:.1f}" y="{cy + 20}" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["cos_color"]}">cos θ = x</text>',
        f'<text x="{px + 15:.1f}" y="{(cy + py)/2:.1f}" font-size="12" font-weight="bold" fill="{COLORS["sin_color"]}">sin θ = y</text>',
        '',
        '<!-- Radio = 1 -->',
        f'<text x="{(cx + px)/2 - 20:.1f}" y="{(cy + py)/2 - 15:.1f}" font-size="11" fill="{COLORS["angle"]}">r = 1</text>',
        '',
        '<!-- Cuadro explicativo -->',
        f'<rect x="20" y="{height - 90}" width="200" height="75" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>',
        f'<text x="30" y="{height - 70}" font-size="11" font-weight="bold" fill="{COLORS["text"]}">En el círculo unitario (r = 1):</text>',
        f'<text x="30" y="{height - 52}" font-size="11" fill="{COLORS["text"]}">cos θ = x/1 = x</text>',
        f'<text x="30" y="{height - 37}" font-size="11" fill="{COLORS["text"]}">sin θ = y/1 = y</text>',
        f'<text x="30" y="{height - 20}" font-size="11" fill="#64748b">∴ P = (x, y) = (cos θ, sin θ)</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


def generate_quadrant_signs(width=600, height=500) -> str:
    """Genera ilustración de los signos en cada cuadrante (ASTC)."""
    cx, cy = width / 2, height / 2 + 20
    radius = min(width, height) / 2 - 100
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Signos en los Cuadrantes</text>',
        f'<text x="{width/2}" y="50" text-anchor="middle" font-size="12" fill="#64748b">Mnemotecnia: "Todos Saben Tomar Café"</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 30}" y1="{cy}" x2="{cx + radius + 30}" y2="{cy}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 30}" x2="{cx}" y2="{cy + radius + 30}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,3"/>',
    ]
    
    # Cuadrantes con información
    quadrants = [
        # (x, y, numeral, color, titulo, positivas)
        (cx + radius/2, cy - radius/2, "I", COLORS["quadrant_I"], "TODOS", "sin +, cos +, tan +"),
        (cx - radius/2, cy - radius/2, "II", COLORS["quadrant_II"], "SENO", "sin +"),
        (cx - radius/2, cy + radius/2, "III", COLORS["quadrant_III"], "TANGENTE", "tan +"),
        (cx + radius/2, cy + radius/2, "IV", COLORS["quadrant_IV"], "COSENO", "cos +"),
    ]
    
    for x, y, numeral, color, titulo, positivas in quadrants:
        # Fondo del cuadrante
        svg_parts.append(f'<rect x="{x - 55}" y="{y - 35}" width="110" height="70" rx="8" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="2"/>')
        # Numeral
        svg_parts.append(f'<text x="{x}" y="{y - 15}" text-anchor="middle" font-size="20" font-weight="bold" fill="{color}">{numeral}</text>')
        # Título
        svg_parts.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-size="11" font-weight="bold" fill="{color}">{titulo}</text>')
        # Funciones positivas
        svg_parts.append(f'<text x="{x}" y="{y + 22}" text-anchor="middle" font-size="10" fill="{COLORS["text"]}">{positivas}</text>')
    
    # Leyenda
    svg_parts.append('')
    svg_parts.append('<!-- Leyenda -->')
    svg_parts.append(f'<rect x="{width - 220}" y="{height - 100}" width="200" height="85" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>')
    svg_parts.append(f'<text x="{width - 210}" y="{height - 80}" font-size="11" font-weight="bold" fill="{COLORS["text"]}">ASTC - Funciones Positivas:</text>')
    svg_parts.append(f'<text x="{width - 210}" y="{height - 62}" font-size="10" fill="{COLORS["quadrant_I"]}">I: All (Todas)</text>')
    svg_parts.append(f'<text x="{width - 210}" y="{height - 47}" font-size="10" fill="{COLORS["quadrant_II"]}">II: Sin (Seno)</text>')
    svg_parts.append(f'<text x="{width - 210}" y="{height - 32}" font-size="10" fill="{COLORS["quadrant_III"]}">III: Tan (Tangente)</text>')
    svg_parts.append(f'<text x="{width - 210}" y="{height - 17}" font-size="10" fill="{COLORS["quadrant_IV"]}">IV: Cos (Coseno)</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_reference_angles(width=650, height=500) -> str:
    """Genera ilustración de ángulos de referencia en cada cuadrante."""
    cx, cy = width / 2, height / 2 + 10
    radius = 130
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Ángulos de Referencia</text>',
        f'<text x="{width/2}" y="48" text-anchor="middle" font-size="11" fill="#64748b">El ángulo agudo formado con el eje X</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 30}" y1="{cy}" x2="{cx + radius + 30}" y2="{cy}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 30}" x2="{cx}" y2="{cy + radius + 30}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#cbd5e1" stroke-width="1"/>',
    ]
    
    # Ejemplos de ángulos de referencia
    examples = [
        # (ángulo, color, cuadrante, fórmula)
        (150, COLORS["quadrant_II"], "II", "α = 180° - 150° = 30°"),
        (225, COLORS["quadrant_III"], "III", "α = 225° - 180° = 45°"),
        (300, COLORS["quadrant_IV"], "IV", "α = 360° - 300° = 60°"),
    ]
    
    for i, (angle_deg, color, quadrant, formula) in enumerate(examples):
        angle_rad = math.radians(angle_deg)
        ref_angle = abs(angle_deg - 180) if 90 < angle_deg <= 270 else (360 - angle_deg if angle_deg > 270 else angle_deg)
        if angle_deg > 180 and angle_deg <= 270:
            ref_angle = angle_deg - 180
        
        px = cx + math.cos(angle_rad) * radius
        py = cy - math.sin(angle_rad) * radius
        
        # Radio al punto
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{color}" stroke-width="2"/>')
        
        # Punto
        svg_parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{color}"/>')
        
        # Proyección al eje X
        proj_x = px
        svg_parts.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{proj_x:.1f}" y2="{cy}" stroke="{color}" stroke-width="1" stroke-dasharray="4,2"/>')
        
        # Arco del ángulo de referencia (simplificado)
        if angle_deg == 150:
            svg_parts.append(f'<path d="M {cx - 30} {cy} A 30 30 0 0 0 {cx + 30 * math.cos(angle_rad):.1f} {cy - 30 * math.sin(angle_rad):.1f}" fill="none" stroke="{COLORS["angle"]}" stroke-width="2"/>')
        
        # Etiqueta
        svg_parts.append(f'<text x="{px + (15 if px > cx else -15):.1f}" y="{py + (-15 if py < cy else 20):.1f}" text-anchor="{"start" if px > cx else "end"}" font-size="12" font-weight="bold" fill="{color}">{angle_deg}°</text>')
    
    # Cuadro de fórmulas
    svg_parts.append('')
    svg_parts.append('<!-- Fórmulas -->')
    svg_parts.append(f'<rect x="15" y="{height - 130}" width="180" height="115" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>')
    svg_parts.append(f'<text x="25" y="{height - 110}" font-size="11" font-weight="bold" fill="{COLORS["text"]}">Fórmulas por cuadrante:</text>')
    svg_parts.append(f'<text x="25" y="{height - 92}" font-size="10" fill="{COLORS["quadrant_I"]}">I: α = θ</text>')
    svg_parts.append(f'<text x="25" y="{height - 77}" font-size="10" fill="{COLORS["quadrant_II"]}">II: α = 180° - θ</text>')
    svg_parts.append(f'<text x="25" y="{height - 62}" font-size="10" fill="{COLORS["quadrant_III"]}">III: α = θ - 180°</text>')
    svg_parts.append(f'<text x="25" y="{height - 47}" font-size="10" fill="{COLORS["quadrant_IV"]}">IV: α = 360° - θ</text>')
    svg_parts.append(f'<text x="25" y="{height - 27}" font-size="10" fill="#64748b">α = ángulo de referencia</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_negative_angles(width=600, height=450) -> str:
    """Genera ilustración de ángulos negativos vs positivos."""
    cx, cy = width / 2, height / 2 + 10
    radius = 120
    
    theta_pos = 45  # Ángulo positivo de ejemplo
    theta_rad = math.radians(theta_pos)
    
    # Puntos
    p_pos = (cx + math.cos(theta_rad) * radius, cy - math.sin(theta_rad) * radius)
    p_neg = (cx + math.cos(-theta_rad) * radius, cy - math.sin(-theta_rad) * radius)
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Ángulos Negativos</text>',
        f'<text x="{width/2}" y="46" text-anchor="middle" font-size="11" fill="#64748b">θ y -θ son simétricos respecto al eje X</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 30}" y1="{cy}" x2="{cx + radius + 30}" y2="{cy}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 30}" x2="{cx}" y2="{cy + radius + 30}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#cbd5e1" stroke-width="1"/>',
        '',
        '<!-- Eje de simetría (eje X resaltado) -->',
        f'<line x1="{cx - radius - 10}" y1="{cy}" x2="{cx + radius + 10}" y2="{cy}" stroke="{COLORS["cos_color"]}" stroke-width="3"/>',
        '',
        '<!-- Radio positivo -->',
        f'<line x1="{cx}" y1="{cy}" x2="{p_pos[0]:.1f}" y2="{p_pos[1]:.1f}" stroke="{COLORS["quadrant_I"]}" stroke-width="3"/>',
        '',
        '<!-- Radio negativo -->',
        f'<line x1="{cx}" y1="{cy}" x2="{p_neg[0]:.1f}" y2="{p_neg[1]:.1f}" stroke="{COLORS["quadrant_IV"]}" stroke-width="3"/>',
        '',
        '<!-- Puntos -->',
        f'<circle cx="{p_pos[0]:.1f}" cy="{p_pos[1]:.1f}" r="8" fill="{COLORS["quadrant_I"]}" stroke="white" stroke-width="2"/>',
        f'<circle cx="{p_neg[0]:.1f}" cy="{p_neg[1]:.1f}" r="8" fill="{COLORS["quadrant_IV"]}" stroke="white" stroke-width="2"/>',
        '',
        '<!-- Línea de simetría punteada -->',
        f'<line x1="{p_pos[0]:.1f}" y1="{p_pos[1]:.1f}" x2="{p_neg[0]:.1f}" y2="{p_neg[1]:.1f}" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,2"/>',
        '',
        '<!-- Etiquetas de puntos -->',
        f'<text x="{p_pos[0] + 15:.1f}" y="{p_pos[1] - 5:.1f}" font-size="12" font-weight="bold" fill="{COLORS["quadrant_I"]}">θ = +45°</text>',
        f'<text x="{p_pos[0] + 15:.1f}" y="{p_pos[1] + 12:.1f}" font-size="10" fill="#64748b">(cos 45°, sin 45°)</text>',
        '',
        f'<text x="{p_neg[0] + 15:.1f}" y="{p_neg[1] + 15:.1f}" font-size="12" font-weight="bold" fill="{COLORS["quadrant_IV"]}">θ = -45°</text>',
        f'<text x="{p_neg[0] + 15:.1f}" y="{p_neg[1] + 30:.1f}" font-size="10" fill="#64748b">(cos 45°, -sin 45°)</text>',
        '',
        '<!-- Flechas de dirección -->',
        f'<text x="{cx + 50}" y="{cy - 50}" font-size="11" fill="{COLORS["quadrant_I"]}">↺ Antihorario (+)</text>',
        f'<text x="{cx + 50}" y="{cy + 60}" font-size="11" fill="{COLORS["quadrant_IV"]}">↻ Horario (-)</text>',
        '',
        '<!-- Cuadro de propiedades -->',
        f'<rect x="15" y="{height - 95}" width="200" height="80" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>',
        f'<text x="25" y="{height - 75}" font-size="11" font-weight="bold" fill="{COLORS["text"]}">Propiedades de paridad:</text>',
        f'<text x="25" y="{height - 57}" font-size="10" fill="{COLORS["cos_color"]}">cos(-θ) = cos(θ)  ← Par</text>',
        f'<text x="25" y="{height - 42}" font-size="10" fill="{COLORS["sin_color"]}">sin(-θ) = -sin(θ) ← Impar</text>',
        f'<text x="25" y="{height - 27}" font-size="10" fill="{COLORS["angle"]}">tan(-θ) = -tan(θ) ← Impar</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


def generate_quadrantal_angles(width=650, height=500) -> str:
    """Genera ilustración de los ángulos cuadrantales (0°, 90°, 180°, 270°)."""
    cx, cy = width / 2, height / 2 + 20
    radius = 130
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Ángulos Cuadrantales</text>',
        f'<text x="{width/2}" y="46" text-anchor="middle" font-size="11" fill="#64748b">Múltiplos de 90° (sobre los ejes)</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 40}" y1="{cy}" x2="{cx + radius + 40}" y2="{cy}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 40}" x2="{cx}" y2="{cy + radius + 40}" stroke="{COLORS["axis"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{COLORS["circle"]}" stroke-width="2"/>',
    ]
    
    # Ángulos cuadrantales
    quadrantal = [
        (0, cx + radius, cy, "0° / 360°", "(1, 0)", "right", "sin=0, cos=1"),
        (90, cx, cy - radius, "90°", "(0, 1)", "top", "sin=1, cos=0"),
        (180, cx - radius, cy, "180°", "(-1, 0)", "left", "sin=0, cos=-1"),
        (270, cx, cy + radius, "270°", "(0, -1)", "bottom", "sin=-1, cos=0"),
    ]
    
    colors = [COLORS["quadrant_I"], COLORS["quadrant_II"], COLORS["quadrant_III"], COLORS["quadrant_IV"]]
    
    for i, (angle, px, py, angle_label, coord_label, pos, values) in enumerate(quadrantal):
        color = colors[i % 4]
        
        # Punto
        svg_parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{color}" stroke="white" stroke-width="2"/>')
        
        # Etiquetas según posición
        if pos == "right":
            svg_parts.append(f'<text x="{px + 20}" y="{py - 10}" font-size="13" font-weight="bold" fill="{color}">{angle_label}</text>')
            svg_parts.append(f'<text x="{px + 20}" y="{py + 7}" font-size="11" fill="{COLORS["text"]}">{coord_label}</text>')
            svg_parts.append(f'<text x="{px + 20}" y="{py + 22}" font-size="9" fill="#64748b">{values}</text>')
        elif pos == "top":
            svg_parts.append(f'<text x="{px}" y="{py - 25}" text-anchor="middle" font-size="13" font-weight="bold" fill="{color}">{angle_label}</text>')
            svg_parts.append(f'<text x="{px}" y="{py - 45}" text-anchor="middle" font-size="11" fill="{COLORS["text"]}">{coord_label}</text>')
            svg_parts.append(f'<text x="{px}" y="{py - 60}" text-anchor="middle" font-size="9" fill="#64748b">{values}</text>')
        elif pos == "left":
            svg_parts.append(f'<text x="{px - 20}" y="{py - 10}" text-anchor="end" font-size="13" font-weight="bold" fill="{color}">{angle_label}</text>')
            svg_parts.append(f'<text x="{px - 20}" y="{py + 7}" text-anchor="end" font-size="11" fill="{COLORS["text"]}">{coord_label}</text>')
            svg_parts.append(f'<text x="{px - 20}" y="{py + 22}" text-anchor="end" font-size="9" fill="#64748b">{values}</text>')
        elif pos == "bottom":
            svg_parts.append(f'<text x="{px}" y="{py + 30}" text-anchor="middle" font-size="13" font-weight="bold" fill="{color}">{angle_label}</text>')
            svg_parts.append(f'<text x="{px}" y="{py + 45}" text-anchor="middle" font-size="11" fill="{COLORS["text"]}">{coord_label}</text>')
            svg_parts.append(f'<text x="{px}" y="{py + 60}" text-anchor="middle" font-size="9" fill="#64748b">{values}</text>')
    
    # Centro
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{COLORS["axis"]}"/>')
    svg_parts.append(f'<text x="{cx + 10}" y="{cy + 20}" font-size="10" fill="#64748b">(0, 0)</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_cofunctions(width=600, height=450) -> str:
    """Genera ilustración de cofunciones en un triángulo rectángulo."""
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Cofunciones</text>',
        f'<text x="{width/2}" y="46" text-anchor="middle" font-size="11" fill="#64748b">sin θ = cos(90° - θ) porque comparten el mismo cateto</text>',
        '',
        '<!-- Triángulo -->',
        '<polygon points="100,350 450,350 450,120" fill="#f1f5f9" stroke="#1e293b" stroke-width="3" stroke-linejoin="round"/>',
        '',
        '<!-- Ángulo recto -->',
        '<path d="M 430 350 L 430 330 L 450 330" fill="none" stroke="#64748b" stroke-width="2"/>',
        '',
        '<!-- Arco del ángulo θ -->',
        '<path d="M 150 350 A 50 50 0 0 0 140 310" fill="none" stroke="{}" stroke-width="3"/>'.format(COLORS["angle"]),
        f'<text x="165" y="325" font-size="16" font-weight="bold" fill="{COLORS["angle"]}">θ</text>',
        '',
        '<!-- Arco del ángulo 90-θ -->',
        '<path d="M 450 170 A 50 50 0 0 0 410 155" fill="none" stroke="{}" stroke-width="3"/>'.format(COLORS["quadrant_II"]),
        f'<text x="415" y="180" font-size="14" font-weight="bold" fill="{COLORS["quadrant_II"]}">90°-θ</text>',
        '',
        '<!-- Etiquetas de lados -->',
        '<!-- Hipotenusa -->',
        f'<text x="250" y="220" font-size="14" font-weight="bold" fill="{COLORS["circle"]}" transform="rotate(-33, 250, 220)">Hipotenusa (H)</text>',
        '',
        '<!-- Cateto opuesto a θ = adyacente a (90-θ) -->',
        f'<rect x="455" y="200" width="110" height="40" rx="4" fill="{COLORS["sin_color"]}" fill-opacity="0.15"/>',
        f'<text x="510" y="215" text-anchor="middle" font-size="11" fill="{COLORS["sin_color"]}">Opuesto a θ</text>',
        f'<text x="510" y="232" text-anchor="middle" font-size="10" fill="{COLORS["quadrant_II"]}">= Adyacente a (90°-θ)</text>',
        '',
        '<!-- Cateto adyacente a θ = opuesto a (90-θ) -->',
        f'<rect x="220" y="355" width="110" height="40" rx="4" fill="{COLORS["cos_color"]}" fill-opacity="0.15"/>',
        f'<text x="275" y="372" text-anchor="middle" font-size="11" fill="{COLORS["cos_color"]}">Adyacente a θ</text>',
        f'<text x="275" y="389" text-anchor="middle" font-size="10" fill="{COLORS["quadrant_II"]}">= Opuesto a (90°-θ)</text>',
        '',
        '<!-- Vértices -->',
        '<circle cx="100" cy="350" r="5" fill="#1e293b"/>',
        '<circle cx="450" cy="350" r="5" fill="#1e293b"/>',
        '<circle cx="450" cy="120" r="5" fill="#1e293b"/>',
        '',
        '<!-- Cuadro de identidades -->',
        f'<rect x="30" y="70" width="180" height="100" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>',
        f'<text x="40" y="92" font-size="11" font-weight="bold" fill="{COLORS["text"]}">Identidades de Cofunciones:</text>',
        f'<text x="40" y="112" font-size="10" fill="{COLORS["sin_color"]}">sin θ = cos(90° - θ)</text>',
        f'<text x="40" y="130" font-size="10" fill="{COLORS["cos_color"]}">cos θ = sin(90° - θ)</text>',
        f'<text x="40" y="148" font-size="10" fill="{COLORS["angle"]}">tan θ = cot(90° - θ)</text>',
        f'<text x="40" y="163" font-size="9" fill="#64748b">"co" viene de "complemento"</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


# Diccionario de generadores
GENERATORS = {
    'basic': generate_basic_unit_circle,
    'point': generate_point_on_circle,
    'quadrants': generate_quadrant_signs,
    'reference': generate_reference_angles,
    'negative': generate_negative_angles,
    'quadrantal': generate_quadrantal_angles,
    'cofunctions': generate_cofunctions,
}


def main():
    parser = argparse.ArgumentParser(description='Unit Circle Renderer')
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



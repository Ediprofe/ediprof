#!/usr/bin/env python3
"""
📐 Identity Renderer - Ilustraciones para identidades trigonométricas

Genera SVGs educativos de:
- Mapas de identidades fundamentales
- Identidad pitagórica en círculo unitario
- Resúmenes visuales de fórmulas
- Estrategias de demostración
- Soluciones de ecuaciones

Uso:
    python scripts/geometry/identity_renderer.py --type map --output archivo.svg
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
    'primary': BASE_COLORS['primary'],
    'secondary': BASE_COLORS['accent'],
    'tertiary': BASE_COLORS['secondary'],
    'quaternary': BASE_COLORS['purple'],
    'accent': BASE_COLORS['highlight'],
    'muted': BASE_COLORS['auxiliary'],
    'box_bg': BASE_COLORS['grid'],
    'box_border': '#e2e8f0',
}


def generate_identity_map(width=700, height=550) -> str:
    """Genera mapa conceptual de identidades fundamentales."""
    cx = width / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{cx}" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="{COLORS["text"]}">Mapa de Identidades Fundamentales</text>',
        '',
    ]
    
    # Identidades Recíprocas (arriba izquierda)
    svg_parts.append('<!-- Identidades Recíprocas -->')
    svg_parts.append(f'<rect x="30" y="60" width="200" height="140" rx="12" fill="{COLORS["primary"]}" fill-opacity="0.1" stroke="{COLORS["primary"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="130" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["primary"]}">📎 RECÍPROCAS</text>')
    svg_parts.append(f'<text x="130" y="115" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">csc θ = 1/sin θ</text>')
    svg_parts.append(f'<text x="130" y="140" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">sec θ = 1/cos θ</text>')
    svg_parts.append(f'<text x="130" y="165" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">cot θ = 1/tan θ</text>')
    svg_parts.append(f'<text x="130" y="188" text-anchor="middle" font-size="10" fill="{COLORS["muted"]}">"Volteamos la fracción"</text>')
    
    # Identidades de Cociente (arriba derecha)
    svg_parts.append('<!-- Identidades de Cociente -->')
    svg_parts.append(f'<rect x="470" y="60" width="200" height="140" rx="12" fill="{COLORS["tertiary"]}" fill-opacity="0.1" stroke="{COLORS["tertiary"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="570" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["tertiary"]}">➗ COCIENTE</text>')
    svg_parts.append(f'<text x="570" y="120" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">tan θ = sin θ / cos θ</text>')
    svg_parts.append(f'<text x="570" y="155" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">cot θ = cos θ / sin θ</text>')
    svg_parts.append(f'<text x="570" y="188" text-anchor="middle" font-size="10" fill="{COLORS["muted"]}">"Una dividida por otra"</text>')
    
    # Centro: Las 6 funciones
    svg_parts.append('<!-- Centro: 6 funciones -->')
    svg_parts.append(f'<circle cx="{cx}" cy="200" r="80" fill="white" stroke="{COLORS["text"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="{cx}" y="170" text-anchor="middle" font-size="11" fill="{COLORS["primary"]}">sin θ    cos θ</text>')
    svg_parts.append(f'<text x="{cx}" y="190" text-anchor="middle" font-size="11" fill="{COLORS["tertiary"]}">tan θ    cot θ</text>')
    svg_parts.append(f'<text x="{cx}" y="210" text-anchor="middle" font-size="11" fill="{COLORS["secondary"]}">sec θ    csc θ</text>')
    svg_parts.append(f'<text x="{cx}" y="235" text-anchor="middle" font-size="10" font-weight="bold" fill="{COLORS["muted"]}">6 FUNCIONES</text>')
    
    # Flechas conectando
    svg_parts.append('<!-- Flechas -->')
    svg_parts.append(f'<line x1="230" y1="130" x2="270" y2="170" stroke="{COLORS["primary"]}" stroke-width="2" marker-end="url(#arrow)"/>')
    svg_parts.append(f'<line x1="470" y1="130" x2="430" y2="170" stroke="{COLORS["tertiary"]}" stroke-width="2" marker-end="url(#arrow)"/>')
    
    # Identidades Pitagóricas (abajo centro)
    svg_parts.append('<!-- Identidades Pitagóricas -->')
    svg_parts.append(f'<rect x="150" y="310" width="400" height="180" rx="12" fill="{COLORS["secondary"]}" fill-opacity="0.1" stroke="{COLORS["secondary"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="{cx}" y="340" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["secondary"]}">📐 PITAGÓRICAS (las más importantes)</text>')
    
    # Las 3 identidades pitagóricas
    svg_parts.append(f'<rect x="170" y="360" width="160" height="50" rx="8" fill="white" stroke="{COLORS["box_border"]}"/>')
    svg_parts.append(f'<text x="250" y="390" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["secondary"]}">sin²θ + cos²θ = 1</text>')
    
    svg_parts.append(f'<rect x="350" y="360" width="180" height="50" rx="8" fill="white" stroke="{COLORS["box_border"]}"/>')
    svg_parts.append(f'<text x="440" y="390" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">1 + tan²θ = sec²θ</text>')
    
    svg_parts.append(f'<rect x="260" y="420" width="180" height="50" rx="8" fill="white" stroke="{COLORS["box_border"]}"/>')
    svg_parts.append(f'<text x="350" y="450" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">1 + cot²θ = csc²θ</text>')
    
    # Nota al pie
    svg_parts.append(f'<text x="{cx}" y="510" text-anchor="middle" font-size="11" fill="{COLORS["muted"]}">💡 Las pitagóricas se derivan del teorema de Pitágoras en el círculo unitario</text>')
    
    # Definición de flecha
    svg_parts.append('''<defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#64748b"/>
    </marker>
  </defs>''')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_pythagorean_circle(width=600, height=500) -> str:
    """Genera ilustración de identidad pitagórica en círculo unitario."""
    cx, cy = width / 2, height / 2 + 30
    radius = 150
    
    # Ángulo de ejemplo
    theta = math.pi / 4
    px = cx + math.cos(theta) * radius
    py = cy - math.sin(theta) * radius
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Identidad Pitagórica: sin²θ + cos²θ = 1</text>',
        f'<text x="{width/2}" y="50" text-anchor="middle" font-size="12" fill="{COLORS["muted"]}">El punto (cos θ, sin θ) está sobre el círculo x² + y² = 1</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 30}" y1="{cy}" x2="{cx + radius + 30}" y2="{cy}" stroke="{COLORS["text"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 30}" x2="{cx}" y2="{cy + radius + 30}" stroke="{COLORS["text"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo unitario -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{COLORS["primary"]}" stroke-width="3"/>',
        '',
        '<!-- Triángulo rectángulo -->',
        f'<polygon points="{cx},{cy} {px:.1f},{cy} {px:.1f},{py:.1f}" fill="{COLORS["quaternary"]}" fill-opacity="0.2" stroke="{COLORS["quaternary"]}" stroke-width="2"/>',
        '',
        '<!-- Radio (hipotenusa) -->',
        f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{COLORS["secondary"]}" stroke-width="4"/>',
        '',
        '<!-- Cateto horizontal (cos θ) -->',
        f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{cy}" stroke="{COLORS["primary"]}" stroke-width="3"/>',
        '',
        '<!-- Cateto vertical (sin θ) -->',
        f'<line x1="{px:.1f}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{COLORS["tertiary"]}" stroke-width="3"/>',
        '',
        '<!-- Punto P -->',
        f'<circle cx="{px:.1f}" cy="{py:.1f}" r="8" fill="{COLORS["secondary"]}" stroke="white" stroke-width="2"/>',
        '',
        '<!-- Símbolo de ángulo recto -->',
        f'<path d="M {px - 15:.1f} {cy} L {px - 15:.1f} {cy - 15} L {px:.1f} {cy - 15}" fill="none" stroke="{COLORS["muted"]}" stroke-width="2"/>',
        '',
        '<!-- Etiquetas -->',
        f'<text x="{(cx + px)/2:.1f}" y="{cy + 25}" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["primary"]}">cos θ</text>',
        f'<text x="{px + 30:.1f}" y="{(cy + py)/2:.1f}" font-size="16" font-weight="bold" fill="{COLORS["tertiary"]}">sin θ</text>',
        f'<text x="{(cx + px)/2 - 30:.1f}" y="{(cy + py)/2 - 10:.1f}" font-size="14" font-weight="bold" fill="{COLORS["secondary"]}">r = 1</text>',
        f'<text x="{px + 15:.1f}" y="{py - 15:.1f}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">P = (cos θ, sin θ)</text>',
        '',
        '<!-- Cuadro de Pitágoras -->',
        f'<rect x="30" y="{height - 100}" width="250" height="85" rx="10" fill="white" stroke="{COLORS["secondary"]}" stroke-width="2"/>',
        f'<text x="45" y="{height - 75}" font-size="12" font-weight="bold" fill="{COLORS["secondary"]}">Teorema de Pitágoras:</text>',
        f'<text x="45" y="{height - 55}" font-size="12" fill="{COLORS["text"]}">cateto² + cateto² = hipotenusa²</text>',
        f'<text x="45" y="{height - 35}" font-size="14" font-weight="bold" fill="{COLORS["quaternary"]}">cos²θ + sin²θ = 1²</text>',
        '',
        '<!-- Ecuación del círculo -->',
        f'<rect x="{width - 200}" y="{height - 100}" width="180" height="85" rx="10" fill="white" stroke="{COLORS["primary"]}" stroke-width="2"/>',
        f'<text x="{width - 190}" y="{height - 75}" font-size="12" font-weight="bold" fill="{COLORS["primary"]}">Ecuación del círculo:</text>',
        f'<text x="{width - 190}" y="{height - 55}" font-size="12" fill="{COLORS["text"]}">x² + y² = r²</text>',
        f'<text x="{width - 190}" y="{height - 35}" font-size="14" font-weight="bold" fill="{COLORS["quaternary"]}">cos²θ + sin²θ = 1</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


def generate_double_angle_formulas(width=700, height=450) -> str:
    """Genera resumen visual de fórmulas de ángulo doble."""
    cx = width / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{cx}" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="{COLORS["text"]}">Identidades del Ángulo Doble</text>',
        f'<text x="{cx}" y="52" text-anchor="middle" font-size="12" fill="{COLORS["muted"]}">De θ a 2θ: "Duplicamos el ángulo"</text>',
        '',
        '<!-- Seno del ángulo doble -->',
        f'<rect x="40" y="75" width="200" height="90" rx="12" fill="{COLORS["primary"]}" fill-opacity="0.15" stroke="{COLORS["primary"]}" stroke-width="2"/>',
        f'<text x="140" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["primary"]}">SENO</text>',
        f'<text x="140" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">sin 2θ = 2 sin θ cos θ</text>',
        f'<text x="140" y="155" text-anchor="middle" font-size="10" fill="{COLORS["muted"]}">Una sola forma</text>',
        '',
        '<!-- Coseno del ángulo doble -->',
        f'<rect x="260" y="75" width="400" height="160" rx="12" fill="{COLORS["secondary"]}" fill-opacity="0.15" stroke="{COLORS["secondary"]}" stroke-width="2"/>',
        f'<text x="460" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["secondary"]}">COSENO (3 formas equivalentes)</text>',
        '',
        f'<rect x="280" y="115" width="160" height="35" rx="6" fill="white" stroke="{COLORS["box_border"]}"/>',
        f'<text x="360" y="138" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">cos²θ - sin²θ</text>',
        '',
        f'<rect x="280" y="160" width="160" height="35" rx="6" fill="white" stroke="{COLORS["box_border"]}"/>',
        f'<text x="360" y="183" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">2cos²θ - 1</text>',
        '',
        f'<rect x="280" y="205" width="160" height="35" rx="6" fill="white" stroke="{COLORS["box_border"]}"/>',
        f'<text x="360" y="228" text-anchor="middle" font-size="13" fill="{COLORS["text"]}">1 - 2sin²θ</text>',
        '',
        f'<text x="545" y="145" font-size="28" fill="{COLORS["secondary"]}">⎫</text>',
        f'<text x="545" y="175" font-size="28" fill="{COLORS["secondary"]}">⎬</text>',
        f'<text x="545" y="205" font-size="28" fill="{COLORS["secondary"]}">⎭</text>',
        f'<text x="575" y="178" font-size="12" fill="{COLORS["text"]}">cos 2θ</text>',
        '',
        '<!-- Tangente del ángulo doble -->',
        f'<rect x="40" y="180" width="200" height="90" rx="12" fill="{COLORS["tertiary"]}" fill-opacity="0.15" stroke="{COLORS["tertiary"]}" stroke-width="2"/>',
        f'<text x="140" y="205" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["tertiary"]}">TANGENTE</text>',
        f'<text x="140" y="235" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["text"]}">tan 2θ = 2tan θ</text>',
        f'<text x="140" y="255" text-anchor="middle" font-size="14" font-weight="bold" fill="{COLORS["text"]}">        1 - tan²θ</text>',
        f'<line x1="80" y1="240" x2="200" y2="240" stroke="{COLORS["text"]}" stroke-width="2"/>',
        '',
        '<!-- Fórmulas derivadas -->',
        f'<rect x="100" y="295" width="500" height="90" rx="12" fill="{COLORS["quaternary"]}" fill-opacity="0.15" stroke="{COLORS["quaternary"]}" stroke-width="2"/>',
        f'<text x="{cx}" y="320" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["quaternary"]}">💡 FÓRMULAS DE REDUCCIÓN DE POTENCIA (derivadas del coseno doble)</text>',
        '',
        f'<text x="200" y="355" text-anchor="middle" font-size="14" fill="{COLORS["text"]}">sin²θ = (1 - cos 2θ) / 2</text>',
        f'<text x="500" y="355" text-anchor="middle" font-size="14" fill="{COLORS["text"]}">cos²θ = (1 + cos 2θ) / 2</text>',
        '',
        '<!-- Tip -->',
        f'<text x="{cx}" y="420" text-anchor="middle" font-size="11" fill="{COLORS["muted"]}">🎯 Tip: Para sin 2θ, siempre es 2·sin·cos. Para cos 2θ, elige la forma según lo que tengas.</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


def generate_half_angle_formulas(width=650, height=400) -> str:
    """Genera resumen visual de fórmulas de ángulo mitad."""
    cx = width / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{cx}" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Identidades del Ángulo Mitad</text>',
        f'<text x="{cx}" y="48" text-anchor="middle" font-size="11" fill="{COLORS["muted"]}">De θ a θ/2: "Dividimos el ángulo a la mitad"</text>',
        '',
        '<!-- Seno mitad -->',
        f'<rect x="30" y="70" width="190" height="100" rx="10" fill="{COLORS["primary"]}" fill-opacity="0.15" stroke="{COLORS["primary"]}" stroke-width="2"/>',
        f'<text x="125" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["primary"]}">SENO</text>',
        f'<text x="125" y="125" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["text"]}">sin(θ/2) = ±√[(1-cos θ)/2]</text>',
        f'<text x="125" y="158" text-anchor="middle" font-size="10" fill="{COLORS["secondary"]}">⚠️ El signo depende del cuadrante</text>',
        '',
        '<!-- Coseno mitad -->',
        f'<rect x="230" y="70" width="190" height="100" rx="10" fill="{COLORS["tertiary"]}" fill-opacity="0.15" stroke="{COLORS["tertiary"]}" stroke-width="2"/>',
        f'<text x="325" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["tertiary"]}">COSENO</text>',
        f'<text x="325" y="125" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["text"]}">cos(θ/2) = ±√[(1+cos θ)/2]</text>',
        f'<text x="325" y="158" text-anchor="middle" font-size="10" fill="{COLORS["secondary"]}">⚠️ El signo depende del cuadrante</text>',
        '',
        '<!-- Tangente mitad -->',
        f'<rect x="430" y="70" width="190" height="100" rx="10" fill="{COLORS["quaternary"]}" fill-opacity="0.15" stroke="{COLORS["quaternary"]}" stroke-width="2"/>',
        f'<text x="525" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["quaternary"]}">TANGENTE (sin radicales)</text>',
        f'<text x="525" y="122" text-anchor="middle" font-size="12" fill="{COLORS["text"]}">tan(θ/2) = sin θ / (1+cos θ)</text>',
        f'<text x="525" y="148" text-anchor="middle" font-size="12" fill="{COLORS["text"]}">tan(θ/2) = (1-cos θ) / sin θ</text>',
        '',
        '<!-- Tabla de signos -->',
        f'<rect x="100" y="190" width="450" height="130" rx="10" fill="white" stroke="{COLORS["box_border"]}" stroke-width="2"/>',
        f'<text x="{cx}" y="215" text-anchor="middle" font-size="13" font-weight="bold" fill="{COLORS["text"]}">📋 Determinación del signo según el cuadrante de θ/2</text>',
        '',
        # Headers
        f'<text x="180" y="245" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["muted"]}">Cuadrante</text>',
        f'<text x="280" y="245" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["primary"]}">sin</text>',
        f'<text x="360" y="245" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["tertiary"]}">cos</text>',
        f'<text x="440" y="245" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["quaternary"]}">tan</text>',
        '',
        # Línea separadora
        f'<line x1="120" y1="252" x2="530" y2="252" stroke="{COLORS["box_border"]}" stroke-width="1"/>',
        '',
        # Fila I
        f'<text x="180" y="272" text-anchor="middle" font-size="11" fill="{COLORS["text"]}">I (0° - 90°)</text>',
        f'<text x="280" y="272" text-anchor="middle" font-size="12" fill="{COLORS["tertiary"]}">+</text>',
        f'<text x="360" y="272" text-anchor="middle" font-size="12" fill="{COLORS["tertiary"]}">+</text>',
        f'<text x="440" y="272" text-anchor="middle" font-size="12" fill="{COLORS["tertiary"]}">+</text>',
        '',
        # Fila II
        f'<text x="180" y="292" text-anchor="middle" font-size="11" fill="{COLORS["text"]}">II (90° - 180°)</text>',
        f'<text x="280" y="292" text-anchor="middle" font-size="12" fill="{COLORS["tertiary"]}">+</text>',
        f'<text x="360" y="292" text-anchor="middle" font-size="12" fill="{COLORS["secondary"]}">−</text>',
        f'<text x="440" y="292" text-anchor="middle" font-size="12" fill="{COLORS["secondary"]}">−</text>',
        '',
        # Fila III y IV
        f'<text x="180" y="312" text-anchor="middle" font-size="11" fill="{COLORS["text"]}">III y IV</text>',
        f'<text x="360" y="312" text-anchor="middle" font-size="10" fill="{COLORS["muted"]}">seguir regla ASTC</text>',
        '',
        '<!-- Tip -->',
        f'<text x="{cx}" y="365" text-anchor="middle" font-size="11" fill="{COLORS["muted"]}">💡 Primero encuentra θ/2, luego determina su cuadrante para elegir el signo correcto</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


def generate_proof_strategies(width=650, height=450) -> str:
    """Genera diagrama de estrategias para demostrar identidades."""
    cx = width / 2
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{cx}" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Estrategias para Demostrar Identidades</text>',
        '',
        '<!-- Estrategia 1 -->',
        f'<rect x="30" y="55" width="590" height="80" rx="10" fill="{COLORS["primary"]}" fill-opacity="0.15" stroke="{COLORS["primary"]}" stroke-width="2"/>',
        f'<text x="50" y="80" font-size="14" font-weight="bold" fill="{COLORS["primary"]}">1️⃣ CONVERTIR TODO A SIN Y COS</text>',
        f'<text x="50" y="102" font-size="12" fill="{COLORS["text"]}">Reemplaza tan, cot, sec, csc usando las identidades de cociente y recíprocas.</text>',
        f'<text x="50" y="122" font-size="11" fill="{COLORS["muted"]}">Ejemplo: tan θ → sin θ / cos θ, sec θ → 1/cos θ</text>',
        '',
        '<!-- Estrategia 2 -->',
        f'<rect x="30" y="145" width="590" height="80" rx="10" fill="{COLORS["tertiary"]}" fill-opacity="0.15" stroke="{COLORS["tertiary"]}" stroke-width="2"/>',
        f'<text x="50" y="170" font-size="14" font-weight="bold" fill="{COLORS["tertiary"]}">2️⃣ BUSCAR DENOMINADOR COMÚN</text>',
        f'<text x="50" y="192" font-size="12" fill="{COLORS["text"]}">Si hay fracciones, combínalas con denominador común y simplifica.</text>',
        f'<text x="50" y="212" font-size="11" fill="{COLORS["muted"]}">Ejemplo: sin/cos + cos/sin → (sin² + cos²)/(sin·cos) = 1/(sin·cos)</text>',
        '',
        '<!-- Estrategia 3 -->',
        f'<rect x="30" y="235" width="590" height="80" rx="10" fill="{COLORS["secondary"]}" fill-opacity="0.15" stroke="{COLORS["secondary"]}" stroke-width="2"/>',
        f'<text x="50" y="260" font-size="14" font-weight="bold" fill="{COLORS["secondary"]}">3️⃣ MULTIPLICAR POR CONJUGADO</text>',
        f'<text x="50" y="282" font-size="12" fill="{COLORS["text"]}">Si hay (1 ± sin θ) o (1 ± cos θ), multiplica arriba y abajo por el conjugado.</text>',
        f'<text x="50" y="302" font-size="11" fill="{COLORS["muted"]}">Ejemplo: (1 - sin θ) × (1 + sin θ) = 1 - sin²θ = cos²θ</text>',
        '',
        '<!-- Estrategia 4 -->',
        f'<rect x="30" y="325" width="590" height="80" rx="10" fill="{COLORS["quaternary"]}" fill-opacity="0.15" stroke="{COLORS["quaternary"]}" stroke-width="2"/>',
        f'<text x="50" y="350" font-size="14" font-weight="bold" fill="{COLORS["quaternary"]}">4️⃣ USAR IDENTIDADES PITAGÓRICAS</text>',
        f'<text x="50" y="372" font-size="12" fill="{COLORS["text"]}">Sustituye sin²θ + cos²θ = 1, o despeja según necesites.</text>',
        f'<text x="50" y="392" font-size="11" fill="{COLORS["muted"]}">sin²θ = 1 - cos²θ, tan²θ = sec²θ - 1, etc.</text>',
        '',
        '<!-- Regla importante -->',
        f'<text x="{cx}" y="430" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["secondary"]}">⚠️ REGLA DE ORO: Trabaja UN SOLO LADO a la vez. Nunca cruces el signo "="</text>',
        '',
        '</svg>'
    ]
    
    return '\n'.join(svg_parts)


def generate_equation_solutions(width=650, height=500) -> str:
    """Genera ilustración de soluciones de ecuaciones en círculo unitario."""
    cx, cy = width / 2, height / 2 + 40
    radius = 130
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="font-family: Inter, system-ui, sans-serif;">',
        f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}"/>',
        '',
        '<!-- Título -->',
        f'<text x="{width/2}" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="{COLORS["text"]}">Soluciones de sin θ = 0.5</text>',
        f'<text x="{width/2}" y="48" text-anchor="middle" font-size="12" fill="{COLORS["muted"]}">¿En qué ángulos el seno vale 0.5?</text>',
        '',
        '<!-- Ejes -->',
        f'<line x1="{cx - radius - 30}" y1="{cy}" x2="{cx + radius + 30}" y2="{cy}" stroke="{COLORS["text"]}" stroke-width="2"/>',
        f'<line x1="{cx}" y1="{cy - radius - 30}" x2="{cx}" y2="{cy + radius + 30}" stroke="{COLORS["text"]}" stroke-width="2"/>',
        '',
        '<!-- Círculo unitario -->',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2"/>',
        '',
        '<!-- Línea y = 0.5 -->',
        f'<line x1="{cx - radius - 20}" y1="{cy - radius * 0.5}" x2="{cx + radius + 20}" y2="{cy - radius * 0.5}" stroke="{COLORS["secondary"]}" stroke-width="2" stroke-dasharray="8,4"/>',
        f'<text x="{cx + radius + 25}" y="{cy - radius * 0.5 + 5}" font-size="12" font-weight="bold" fill="{COLORS["secondary"]}">y = 0.5</text>',
        '',
    ]
    
    # Puntos de intersección
    # θ = 30° y θ = 150°
    angles = [(30, "30°", "QI"), (150, "150°", "QII")]
    
    for angle_deg, label, quadrant in angles:
        angle_rad = math.radians(angle_deg)
        px = cx + math.cos(angle_rad) * radius
        py = cy - math.sin(angle_rad) * radius
        
        color = COLORS["tertiary"] if quadrant == "QI" else COLORS["quaternary"]
        
        # Radio al punto
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}" stroke="{color}" stroke-width="2"/>')
        
        # Punto
        svg_parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{color}" stroke="white" stroke-width="2"/>')
        
        # Etiqueta
        offset_x = 20 if px > cx else -20
        anchor = "start" if px > cx else "end"
        svg_parts.append(f'<text x="{px + offset_x:.1f}" y="{py - 10:.1f}" text-anchor="{anchor}" font-size="14" font-weight="bold" fill="{color}">θ = {label}</text>')
        svg_parts.append(f'<text x="{px + offset_x:.1f}" y="{py + 8:.1f}" text-anchor="{anchor}" font-size="11" fill="{COLORS["muted"]}">{quadrant}</text>')
    
    # Cuadro de método
    svg_parts.append('')
    svg_parts.append('<!-- Método -->')
    svg_parts.append(f'<rect x="30" y="{height - 140}" width="280" height="125" rx="10" fill="white" stroke="{COLORS["box_border"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="45" y="{height - 115}" font-size="12" font-weight="bold" fill="{COLORS["text"]}">📋 Método:</text>')
    svg_parts.append(f'<text x="45" y="{height - 93}" font-size="11" fill="{COLORS["text"]}">1. Ángulo de referencia: arcsin(0.5) = 30°</text>')
    svg_parts.append(f'<text x="45" y="{height - 73}" font-size="11" fill="{COLORS["text"]}">2. Seno positivo → QI y QII</text>')
    svg_parts.append(f'<text x="45" y="{height - 53}" font-size="11" fill="{COLORS["tertiary"]}">3. QI: θ = 30°</text>')
    svg_parts.append(f'<text x="45" y="{height - 33}" font-size="11" fill="{COLORS["quaternary"]}">4. QII: θ = 180° - 30° = 150°</text>')
    
    # Solución general
    svg_parts.append(f'<rect x="340" y="{height - 140}" width="280" height="125" rx="10" fill="{COLORS["accent"]}" fill-opacity="0.15" stroke="{COLORS["accent"]}" stroke-width="2"/>')
    svg_parts.append(f'<text x="355" y="{height - 115}" font-size="12" font-weight="bold" fill="{COLORS["accent"]}">✅ Soluciones:</text>')
    svg_parts.append(f'<text x="355" y="{height - 90}" font-size="12" fill="{COLORS["text"]}">Principales [0°, 360°):</text>')
    svg_parts.append(f'<text x="355" y="{height - 70}" font-size="13" font-weight="bold" fill="{COLORS["text"]}">θ = 30° y θ = 150°</text>')
    svg_parts.append(f'<text x="355" y="{height - 45}" font-size="12" fill="{COLORS["text"]}">Generales:</text>')
    svg_parts.append(f'<text x="355" y="{height - 25}" font-size="11" fill="{COLORS["text"]}">θ = 30° + k·360° , θ = 150° + k·360°</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


# Diccionario de generadores
GENERATORS = {
    'map': generate_identity_map,
    'pythagorean': generate_pythagorean_circle,
    'double': generate_double_angle_formulas,
    'half': generate_half_angle_formulas,
    'proof': generate_proof_strategies,
    'equations': generate_equation_solutions,
}


def main():
    parser = argparse.ArgumentParser(description='Identity Renderer')
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


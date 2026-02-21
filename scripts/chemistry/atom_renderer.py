
#!/usr/bin/env python3
"""
⚛️ Atom Structure Renderer - Genera diagramas atómicos (Bohr) desde spec JSON

Uso:
    python3 scripts/chemistry/atom_renderer.py \
        --spec specs/quimica/isotopos/h-1.json \
        --output public/images/quimica/isotopos/h-1.svg

Soporta:
- Núcleo con protones y neutrones (empaquetado simple)
- Capas de electrones (modelo de Bohr)
- Etiquetas personalizables
"""

import json
import argparse
import sys
import math
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))

from core import COLORS  # type: ignore
from core.primitives import escape_xml  # type: ignore

def load_spec(spec_path: str) -> dict:
    with open(spec_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def polar_to_cartesian(r, theta, cx, cy):
    return {
        'x': cx + r * math.cos(theta),
        'y': cy + r * math.sin(theta)
    }

def pack_nucleus(protons: int, neutrons: int, particle_radius: float) -> list:
    """
    Genera posiciones (x, y, tipo) para partículas en el núcleo.
    Usa un algoritmo de espiral phyllotaxis para empaquetado uniforme.
    """
    particles = []
    total_particles = protons + neutrons
    
    # Lista mezclada: p, n, p, n... para distribuir carga
    # Aunque en realidad p y n se agrupan, para visualización esto es claro
    pool = ['p'] * protons + ['n'] * neutrons
    # Mezclamos simple: si hay de ambos, alternamos
    mixed_pool = []
    while pool:
        if not mixed_pool:
            mixed_pool.append(pool.pop(0))
            continue
        
        last = mixed_pool[-1]
        # Intentar tomar uno diferente
        found = False
        for i, p in enumerate(pool):
            if p != last:
                mixed_pool.append(pool.pop(i))
                found = True
                break
        if not found:
            mixed_pool.append(pool.pop(0))
            
    # Phyllotaxis layout
    c = particle_radius * 2.2 # Espaciado
    golden_angle = 137.508 * (math.pi / 180)
    
    for i, p_type in enumerate(mixed_pool):
        if i == 0:
            x, y = 0, 0
        else:
            r = c * math.sqrt(i)
            theta = i * golden_angle
            x = r * math.cos(theta)
            y = r * math.sin(theta)
        
        particles.append({'type': p_type, 'x': x, 'y': y})
        
    return particles

def distribute_electrons(count: int) -> list:
    """Retorna lista de radios y ángulos para e- según configuración electrónica básica (2, 8, 8...)"""
    shells = []
    remaining = count
    shell_capacity = [2, 8, 8, 18, 18, 32, 32]
    
    current_shell = 1
    for cap in shell_capacity:
        if remaining <= 0:
            break
        
        take = min(remaining, cap)
        shells.append({'n': current_shell, 'count': take})
        remaining -= take
        current_shell += 1
        
    return shells

def render_atom(spec: dict) -> str:
    layout = spec.get('layout', {})
    
    # Layout Side-by-Side: Card (Left) | Atom (Right)
    width = 600
    
    # Atom Center (Right side)
    cx = 400 
    
    # Vertical Center (pushed down for title space as before)
    cy = 320 
    
    protons = spec['protons']
    neutrons = spec['neutrons']
    electrons = spec['electrons']
    
    mass_number = protons + neutrons
    
    nucleons = pack_nucleus(protons, neutrons, layout.get('particle_radius', 8))
    shells = distribute_electrons(electrons)
    
    # Calculamos radio máximo para ajustar altura dinámica
    base_orbit_radius = layout.get('orbit_base_radius', 100) 
    orbit_step = layout.get('orbit_step', 35)
    num_shells = len(distribute_electrons(electrons))
    max_r = base_orbit_radius
    if num_shells > 1:
        max_r += (num_shells - 1) * orbit_step
    if num_shells == 0: 
        max_r = base_orbit_radius * 0.5 

    # Ajuste dinámico de altura
    legend_gap = 50
    legend_y = cy + max_r + legend_gap
    new_height = int(legend_y + 50) 
    
    height = new_height
    
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    
    # Fondo
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>')
    
    # 4. Tarjeta de Tabla Periódica (Ahora a la Izquierda, centrada con el átomo)
    element_info = spec.get('element_info')
    if element_info:
        card_w, card_h = 80, 95
        card_x = 60 # Margen izquierdo
        # Centrar verticalmente respecto al átomo (cy)
        card_y = cy - card_h / 2
        
        draw_element_card(svg_parts, card_x, card_y, element_info)
        
        # Opcional: una línea conectora sutil o simplemente proximidad
    
    # Títulos y Etiquetas (Centrados sobre el ÁTOMO, usando cx)
    title = spec.get('title', '')
    if title:
        svg_parts.append(f'<text x="{cx}" y="50" font-family="Inter, sans-serif" font-size="24" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(title)}</text>')
    
    sub = spec.get('subtitle', '')
    if sub:
        svg_parts.append(f'<text x="{cx}" y="80" font-family="Inter, sans-serif" font-size="14" fill="{COLORS["text_light"]}" text-anchor="middle">{escape_xml(sub)}</text>')

    # Abundancia (Badge)
    abundance = spec.get('abundance', '')
    if abundance:
        # Dibujar Badge centrado debajo del subtítulo
        badge_y = 100
        text_width = len(abundance) * 7 + 38 # Estimación simple
        badge_w = max(110, text_width)
        badge_h = 24
        badge_x = cx - badge_w/2
        
        # Rectángulo redondeado (Pill)
        svg_parts.append(f'<rect x="{badge_x}" y="{badge_y}" width="{badge_w}" height="{badge_h}" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>')
        # Texto "Abundancia: X%"
        svg_parts.append(f'<text x="{cx}" y="{badge_y + 16}" font-family="Inter, sans-serif" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">Abundancia: {escape_xml(abundance)}</text>')

    # 1. Dibujar Órbitas (Shells) - ESTILO MEJORADO
    # Aumentar radio base de 80 a 90 para separar más
    base_r_default = 130 if abundance else 90
    base_orbit_radius = layout.get('orbit_base_radius', base_r_default) 
    orbit_step = layout.get('orbit_step', 35)
    
    electron_positions = []
    
    for i, shell in enumerate(shells):
        r = base_orbit_radius + i * orbit_step
        # Dibujar círculo de la órbita (Sólido, translúcido, más grueso)
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["grid"]}" stroke-width="2.5" stroke-dasharray="0" opacity="0.8"/>')
        
        # Calcular posiciones de electrones
        count = shell['count']
        angle_step = (2 * math.pi) / count
        start_angle = -math.pi / 2 # Empezar arriba
        
        for e in range(count):
            theta = start_angle + e * angle_step
            pos = polar_to_cartesian(r, theta, cx, cy)
            electron_positions.append(pos)
            
    # 2. Dibujar Núcleo
    # Centrar el grupo de nucleones
    
    # Calcular radio del fondo del núcleo dinámicamente
    max_dist = 0
    if nucleons:
        max_dist = max(math.sqrt(p['x']**2 + p['y']**2) for p in nucleons)
    
    # Radio del fondo = distancia más lejana + radio de partícula + padding
    # Si solo hay 1 partícula (H), max_dist es 0.
    particle_r = layout.get('particle_radius', 8)
    nucleus_bg_radius = max_dist + particle_r + 6 
    
    if nucleus_bg_radius < particle_r + 4: nucleus_bg_radius = particle_r + 8 # Mínimo
    
    svg_parts.append(f'<g transform="translate({cx},{cy})">')
    
    # Fondo del núcleo
    svg_parts.append(f'<circle cx="0" cy="0" r="{nucleus_bg_radius}" fill="#fdf4ff" stroke="{COLORS["purple"]}" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.8"/>')
    
    for p in nucleons:
        fill = COLORS['accent'] if p['type'] == 'p' else COLORS['text_light']
        stroke = COLORS['white']
        r = layout.get('particle_radius', 8)
        
        svg_parts.append(f'<circle cx="{p["x"]}" cy="{p["y"]}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        
        # Texto p+ o n
        label = "+" if p['type'] == 'p' else "" # n0 es muy largo a veces
        if label:
            svg_parts.append(f'<text x="{p["x"]}" y="{p["y"]+2.5}" font-family="Inter, sans-serif" font-size="{r*1.2}" font-weight="bold" fill="white" text-anchor="middle">{label}</text>')
            
    svg_parts.append('</g>')
    
    # 3. Dibujar Electrones
    e_radius = layout.get('electron_radius', 4)
    for pos in electron_positions:
        svg_parts.append(f'<circle cx="{pos["x"]}" cy="{pos["y"]}" r="{e_radius}" fill="{COLORS["primary"]}" stroke="white" stroke-width="1"/>')
        svg_parts.append(f'<text x="{pos["x"]}" y="{pos["y"]+1.5}" font-family="Inter, sans-serif" font-size="{e_radius*1.8}" font-weight="bold" fill="white" text-anchor="middle">-</text>')

    # 4. Tarjeta de Tabla Periódica (Ahora dibujada arriba)
    pass

    # 5. Leyenda (Abajo, Centrada)
    # legend_y ya fue calculado arriba dinámicamente
    pass
    
    # Definir items de leyenda
    legend_items = [
        {'label': 'Protón', 'symbol': '+', 'color': COLORS['accent']},
        {'label': 'Neutrón', 'symbol': '',  'color': COLORS['text_light']}, # Sin símbolo texto, solo color
        {'label': 'Electrón', 'symbol': '-', 'color': COLORS['primary']}
    ]
    
    # Calcular ancho total para centrar
    item_width = 90
    total_legend_width = len(legend_items) * item_width
    start_x = (width - total_legend_width) / 2
    
    for i, item in enumerate(legend_items):
        lx = start_x + i * item_width + item_width/2
        
        # Círculo
        r = 6
        svg_parts.append(f'<circle cx="{lx - 15}" cy="{legend_y}" r="{r}" fill="{item["color"]}" stroke="white" stroke-width="1"/>')
        
        # Símbolo dentro del círculo (si hay)
        if item['symbol']:
            font_size = 7
            y_offset = 1.5
            svg_parts.append(f'<text x="{lx - 15}" y="{legend_y + y_offset}" font-family="Inter, sans-serif" font-size="{font_size}" font-weight="bold" fill="white" text-anchor="middle">{item["symbol"]}</text>')
            
        # Texto etiqueta
        svg_parts.append(f'<text x="{lx}" y="{legend_y + 4}" font-family="Inter, sans-serif" font-size="12" fill="{COLORS["text_light"]}" text-anchor="start">{item["label"]}</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def draw_element_card(svg_parts: list, x: float, y: float, info: dict):
    """Dibuja una tarjeta estilo tabla periódica."""
    w, h = 80, 95
    
    # Colores (Estilo "Blue" por defecto, o basado en categoría si se pasara)
    fill = '#eff6ff'  # Blue 50
    stroke = COLORS['primary'] # Blue 500
    text_dark = COLORS['text']
    text_light = COLORS['text_light']
    
    # Sombra suave (opcional)
    # svg_parts.append(f'<rect x="{x+2}" y="{y+2}" width="{w}" height="{h}" rx="6" fill="#000000" opacity="0.1"/>')

    # Tarjeta Rect
    svg_parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    
    # Z (Arriba Izquierda)
    z = info.get("z", "")
    svg_parts.append(f'<text x="{x + 8}" y="{y + 20}" font-family="Inter, sans-serif" font-size="12" font-weight="bold" fill="{text_dark}">{z}</text>')
    
    # Masa (Arriba Derecha)
    mass = info.get("mass", "")
    svg_parts.append(f'<text x="{x + w - 8}" y="{y + 20}" font-family="Inter, sans-serif" font-size="10" fill="{text_light}" text-anchor="end">{mass}</text>')
    
    # Símbolo (Centro)
    symbol = info.get("symbol", "")
    # Ajustar tamaño según longitud
    sym_size = 32 if len(symbol) <= 2 else 24
    svg_parts.append(f'<text x="{x + w/2}" y="{y + h * 0.55}" font-family="Inter, sans-serif" font-size="{sym_size}" font-weight="800" fill="{text_dark}" text-anchor="middle">{symbol}</text>')
    
    # Nombre (Abajo)
    name = info.get("name", "")
    svg_parts.append(f'<text x="{x + w/2}" y="{y + h - 12}" font-family="Inter, sans-serif" font-size="10" fill="{text_dark}" text-anchor="middle">{name}</text>')

def main():
    parser = argparse.ArgumentParser(description='Genera diagrama atómico SVG')
    parser.add_argument('--spec', required=True, help='Spec JSON')
    parser.add_argument('--output', required=True, help='Output SVG')
    args = parser.parse_args()
    
    spec = load_spec(args.spec)
    svg = render_atom(spec)
    
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding='utf-8')
    print(f"✅ Átomo generado: {args.output}")

if __name__ == '__main__':
    main()

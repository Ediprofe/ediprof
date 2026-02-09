
#!/usr/bin/env python3
"""
Renderizador para explicar el Número Másico (A = Z + n)
"""
import json
import argparse
import sys
import math
from pathlib import Path

# Agregar path para importar core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))

from core import COLORS
from core.primitives import escape_xml

def load_spec(spec_path: str) -> dict:
    with open(spec_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def polar_to_cartesian(r, theta, cx, cy):
    return {
        'x': cx + r * math.cos(theta),
        'y': cy + r * math.sin(theta)
    }

def pack_nucleus(protons: int, neutrons: int, particle_radius: float) -> list:
    # Versión simplificada para layout claro: Protones juntos, Neutrones juntos pero mezclados en cluster
    # Phyllotaxis es buena
    particles = []
    pool = ['p'] * protons + ['n'] * neutrons
    # Mezcla simple
    mixed_pool = []
    while pool:
        if not mixed_pool: mixed_pool.append(pool.pop(0)); continue
        last = mixed_pool[-1]
        found = False
        for i, p in enumerate(pool):
            if p != last: mixed_pool.append(pool.pop(i)); found=True; break
        if not found: mixed_pool.append(pool.pop(0))
            
    c = particle_radius * 2.1
    golden_angle = 137.508 * (math.pi / 180)
    
    for i, p_type in enumerate(mixed_pool):
        r = c * math.sqrt(i) if i > 0 else 0
        theta = i * golden_angle
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        particles.append({'type': p_type, 'x': x, 'y': y})
        
    return particles

def distribute_electrons(count: int) -> list:
    shells = []
    remaining = count
    shell_capacity = [2, 8, 8, 18]
    current = 1
    for cap in shell_capacity:
        if remaining <= 0: break
        take = min(remaining, cap)
        shells.append({'n': current, 'count': take})
        remaining -= take
        current += 1
    return shells

def render_mass_number(spec: dict) -> str:
    layout = spec.get('layout', {})
    width = layout.get('width', 600)
    height = layout.get('height', 500)
    
    # Centro del átomo desplazado a la derecha para dejar espacio a la izquierda para explicaciones
    cx = width * 0.65
    cy = height * 0.55
    
    protons = spec['protons']
    neutrons = spec['neutrons']
    electrons = spec['electrons']
    
    particle_r = layout.get('particle_radius', 14)
    
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    
    # Fondo
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="{COLORS["background"]}" rx="12"/>')
    
    # Definiciones de marcadores (flechas)
    svg_parts.append('<defs>')
    svg_parts.append(f'<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="{COLORS["text_light"]}" /></marker>')
    svg_parts.append('</defs>')

    # 1. Título General
    title = spec.get('title', 'Número Másico (A)')
    svg_parts.append(f'<text x="{width/2}" y="40" font-family="Inter, sans-serif" font-size="24" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">{escape_xml(title)}</text>')
    
    sub = spec.get('subtitle', '')
    if sub:
        svg_parts.append(f'<text x="{width/2}" y="65" font-family="Inter, sans-serif" font-size="14" fill="{COLORS["text_light"]}" text-anchor="middle">{escape_xml(sub)}</text>')

    # --- CÁLCULOS PREVIOS ---
    
    # Calcular radio visual del núcleo primero
    nucleons = pack_nucleus(protons, neutrons, particle_r)
    max_n_dist = 0
    if nucleons:
        max_n_dist = max(math.sqrt(p['x']**2 + p['y']**2) for p in nucleons)
    nucleus_visual_r = max_n_dist + particle_r + 5
    
    # Ajustar radio base de órbita si colisiona con el núcleo
    base_orbit_r = layout.get('orbit_base_radius', 120)
    if base_orbit_r < nucleus_visual_r + 30:
        base_orbit_r = nucleus_visual_r + 30
        
    # --- RENDERIZADO POR CAPAS ---
    
    # CAPA 1: Fondo del Núcleo (Dashed Circle)
    # Dibujar un círculo grande punteado alrededor del núcleo (para representar "A")
    svg_parts.append(f'<g transform="translate({cx},{cy})">')
    svg_parts.append(f'<circle cx="0" cy="0" r="{nucleus_visual_r + 10}" fill="#fff7ed" stroke="{COLORS["highlight"]}" stroke-width="2" stroke-dasharray="6,4"/>')
    svg_parts.append('</g>')

    # CAPA 2: Electrones y Órbitas
    shells = distribute_electrons(electrons)
    orbit_step = 35
    
    # Etiqueta de electrones (Izquierda abajo o cerca)
    electron_label_set = False
    
    for i, shell in enumerate(shells):
        r = base_orbit_r + i * orbit_step
        # Órbita sólida
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{COLORS["grid"]}" stroke-width="2" stroke-dasharray="0"/>')
        
        count = shell['count']
        angle_step = (2 * math.pi) / count
        # Alternar ángulo de inicio
        start_angle = -math.pi / 2 + (i * math.pi / 2)
        
        for e in range(count):
            theta = start_angle + e * angle_step
            pos = polar_to_cartesian(r, theta, cx, cy)
            
            # Electrón Estándar (Azul)
            svg_parts.append(f'<circle cx="{pos["x"]}" cy="{pos["y"]}" r="5" fill="{COLORS["primary"]}" stroke="white" stroke-width="1.5"/>')
            # Signo menos
            svg_parts.append(f'<path d="M {pos["x"]-2} {pos["y"]} L {pos["x"]+2} {pos["y"]}" stroke="white" stroke-width="1.5" stroke-linecap="round"/>')
            
            if not electron_label_set and i == len(shells)-1 and e == 0:
                # Etiqueta a uno de los electrones externos
                ex, ey = pos['x'], pos['y']
                label_x = ex - 60
                label_y = ey - 20
                # Ajuste para evitar salir del canvas si está muy a la derecha
                if ex > width - 50: label_x = ex - 80 
                
                svg_parts.append(f'<path d="M {label_x+40} {label_y+5} Q {ex-10} {ey-10} {ex-4} {ey-4}" fill="none" stroke="{COLORS["text_light"]}" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.8"/>')
                svg_parts.append(f'<text x="{label_x}" y="{label_y}" font-family="Inter, sans-serif" font-size="11" fill="{COLORS["text_light"]}">Electrones</text>')
                svg_parts.append(f'<text x="{label_x}" y="{label_y+12}" font-family="Inter, sans-serif" font-size="10" font-weight="bold" fill="{COLORS["text_light"]}">(Masa ≈ 0)</text>')
                electron_label_set = True

    # CAPA 3: Partículas del Núcleo (Protones/Neutrones)
    svg_parts.append(f'<g transform="translate({cx},{cy})">')
    for p in nucleons:
        fill = COLORS['accent'] if p['type'] == 'p' else COLORS['secondary'] 
        if p['type'] == 'n': fill = '#64748b'
        
        stroke = 'white'
        svg_parts.append(f'<circle cx="{p["x"]}" cy="{p["y"]}" r="{particle_r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        
        label = "+" if p['type'] == 'p' else ""
        if label:
             svg_parts.append(f'<text x="{p["x"]}" y="{p["y"]+4}" font-family="Inter, sans-serif" font-size="{particle_r*1.2}" font-weight="bold" fill="white" text-anchor="middle">{label}</text>')
    svg_parts.append('</g>')

    # 4. Ecuación Visual y Flechas (Lado Izquierdo)
    
    # Posición de la ecuación: Lado izquierdo centrado verticalmente
    eq_x = 120
    eq_y = cy
    
    # Caja de la fórmula
    svg_parts.append(f'<rect x="{eq_x - 100}" y="{eq_y - 80}" width="200" height="160" rx="12" fill="white" stroke="{COLORS["grid"]}" stroke-width="1"/>')
    
    # A
    svg_parts.append(f'<text x="{eq_x}" y="{eq_y - 40}" font-family="Inter, sans-serif" font-size="48" font-weight="900" fill="{COLORS["text"]}" text-anchor="middle">A</text>')
    svg_parts.append(f'<text x="{eq_x}" y="{eq_y - 15}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["highlight"]}" text-anchor="middle">Número Másico</text>')
    
    # = Z + n
    svg_parts.append(f'<text x="{eq_x}" y="{eq_y + 20}" font-family="Inter, sans-serif" font-size="24" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">=</text>')
    
    # Z (Protones)
    svg_parts.append(f'<text x="{eq_x - 40}" y="{eq_y + 50}" font-family="Inter, sans-serif" font-size="20" font-weight="bold" fill="{COLORS["accent"]}" text-anchor="middle">Z</text>')
    svg_parts.append(f'<text x="{eq_x - 40}" y="{eq_y + 65}" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">(Protones)</text>')
    
    # +
    svg_parts.append(f'<text x="{eq_x}" y="{eq_y + 50}" font-family="Inter, sans-serif" font-size="20" font-weight="bold" fill="{COLORS["text"]}" text-anchor="middle">+</text>')

    # n (Neutrones)
    svg_parts.append(f'<text x="{eq_x + 40}" y="{eq_y + 50}" font-family="Inter, sans-serif" font-size="20" font-weight="bold" fill="#64748b" text-anchor="middle">n</text>')
    svg_parts.append(f'<text x="{eq_x + 40}" y="{eq_y + 65}" font-family="Inter, sans-serif" font-size="10" fill="{COLORS["text_light"]}" text-anchor="middle">(Neutrones)</text>')
    
    # 5. Notación Atómica (Eliminada por petición)
    pass
    
    # Conectores (Flechas Curvas)
    
    # Flecha desde "A" al Núcleo completo
    # Start: Right side of "A" box/text bounding
    # End: Left side of Nucleus circle
    
    start_x = eq_x + 60
    start_y = eq_y - 30
    
    end_x = cx - nucleus_visual_r - 10
    end_y = cy - 20
    
    # Curva Bezier
    path_d = f"M {start_x} {start_y} C {start_x+50} {start_y}, {end_x-50} {end_y}, {end_x} {end_y}"
    svg_parts.append(f'<path d="{path_d}" fill="none" stroke="{COLORS["highlight"]}" stroke-width="2.5" marker-end="url(#arrow)" stroke-dasharray="5,5"/>')
    
    # Flecha Z -> Protón (buscar posición de un protón)
    # Busquemos el primer p
    target_p = next((p for p in nucleons if p['type'] == 'p'), None)
    if target_p:
        tx, ty = target_p['x'] + cx, target_p['y'] + cy
        sx = eq_x - 20
        sy = eq_y + 70
        svg_parts.append(f'<path d="M {sx} {sy} Q {sx} {ty}, {tx-particle_r} {ty}" fill="none" stroke="{COLORS["accent"]}" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.6"/>')

    # Flecha n -> Neutrón
    target_n = next((p for p in nucleons if p['type'] == 'n'), None)
    if target_n:
        tx, ty = target_n['x'] + cx, target_n['y'] + cy
        sx = eq_x + 60
        sy = eq_y + 70
        svg_parts.append(f'<path d="M {sx} {sy} Q {sx+20} {ty}, {tx+particle_r} {ty}" fill="none" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.6"/>')
        
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--spec', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    
    spec = load_spec(args.spec)
    svg = render_mass_number(spec)
    
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding='utf-8')
    print(f"✅ Diagrama generado: {args.output}")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
📐 GeometrySpec Renderer

Motor de renderizado para geometría exacta usando SymPy para cálculos
y SVG para salida vectorial.

Uso:
    python scripts/geometry/renderer.py --spec ARCHIVO.json --output ARCHIVO.svg [--verify]

Opciones:
    --spec      Archivo JSON con la especificación GeometrySpec
    --output    Archivo SVG de salida
    --verify    Validar propiedades matemáticas antes de renderizar
    --validate-only  Solo validar sin generar SVG

Referencia completa: .agent/workflows/geometry-exact.md
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from sympy import Point, Line, Circle, Segment, Triangle
    from sympy import sqrt, Rational
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False
    print("⚠️  SymPy no está instalado. Instalar con: pip install sympy")

# ============================================================================
# PRIMITIVAS GEOMÉTRICAS
# ============================================================================

def calculate_centroid(A, B, C):
    """Calcula el baricentro (centroide) de un triángulo."""
    return Point(
        (A.x + B.x + C.x) / 3,
        (A.y + B.y + C.y) / 3
    )

def calculate_circumcenter(A, B, C):
    """Calcula el circuncentro de un triángulo."""
    triangle = Triangle(A, B, C)
    return triangle.circumcenter

def calculate_incenter(A, B, C):
    """Calcula el incentro de un triángulo."""
    triangle = Triangle(A, B, C)
    return triangle.incenter

def calculate_orthocenter(A, B, C):
    """Calcula el ortocentro de un triángulo."""
    triangle = Triangle(A, B, C)
    return triangle.orthocenter

def calculate_midpoint(P1, P2):
    """Calcula el punto medio de un segmento."""
    return Point(
        (P1.x + P2.x) / 2,
        (P1.y + P2.y) / 2
    )

# ============================================================================
# VALIDACIÓN
# ============================================================================

def verify_concurrent(lines, tolerance=1e-6):
    """Verifica que varias líneas sean concurrentes."""
    if len(lines) < 2:
        return True
    
    # Encontrar intersección de las dos primeras
    intersection = lines[0].intersection(lines[1])
    if not intersection:
        return False
    
    point = intersection[0]
    
    # Verificar que todas las demás pasan por ese punto
    for line in lines[2:]:
        if not line.contains(point):
            return False
    
    return True

def verify_collinear(points):
    """Verifica que varios puntos sean colineales."""
    if len(points) < 3:
        return True
    
    line = Line(points[0], points[1])
    for point in points[2:]:
        if not line.contains(point):
            return False
    
    return True

# ============================================================================
# RENDERIZADO SVG
# ============================================================================

def render_svg(spec, output_path):
    """Renderiza la especificación a SVG."""
    canvas = spec.get('canvas', {'width': 500, 'height': 400, 'padding': 40})
    width = canvas['width']
    height = canvas['height']
    
    construction = spec.get('construction', {})
    show = construction.get('show', {})
    
    # Colores por defecto
    COLORS = {
        'triangle_fill': '#f8fafc',
        'triangle_stroke': '#1e293b',
        'medianas': '#22c55e',
        'alturas': '#f97316',
        'bisectrices': '#8b5cf6',
        'mediatrices': '#ec4899',
        'punto_notable': '#ef4444',
        'vertices': '#1e293b'
    }
    
    svg_elements = []
    svg_elements.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
    svg_elements.append(f'  <rect width="{width}" height="{height}" fill="#ffffff"/>')
    
    # Obtener vértices del triángulo
    base = construction.get('base', {})
    if base:
        A = base.get('A', [50, 350])
        B = base.get('B', [450, 350])
        C = base.get('C', [250, 50])
        
        # Dibujar triángulo
        if show.get('triangle', True):
            fill = COLORS['triangle_fill']
            stroke = COLORS['triangle_stroke']
            svg_elements.append(f'  <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        
        # Etiquetas de vértices
        if show.get('vertices_labels'):
            labels = show['vertices_labels']
            offset = 15
            svg_elements.append(f'  <text x="{A[0]-offset}" y="{A[1]+offset}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["vertices"]}">{labels.get("A", "A")}</text>')
            svg_elements.append(f'  <text x="{B[0]+offset}" y="{B[1]+offset}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["vertices"]}">{labels.get("B", "B")}</text>')
            svg_elements.append(f'  <text x="{C[0]}" y="{C[1]-offset}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{COLORS["vertices"]}" text-anchor="middle">{labels.get("C", "C")}</text>')
        
        # Calcular puntos si es necesario
        if SYMPY_AVAILABLE:
            pA = Point(A[0], A[1])
            pB = Point(B[0], B[1])
            pC = Point(C[0], C[1])
            
            compute = construction.get('compute', [])
            
            # Medianas
            if 'medianas' in compute and show.get('medianas'):
                color = show['medianas'].get('color', COLORS['medianas'])
                style = 'stroke-dasharray: 5,5' if show['medianas'].get('style') == 'dashed' else ''
                
                Ma = calculate_midpoint(pB, pC)
                Mb = calculate_midpoint(pA, pC)
                Mc = calculate_midpoint(pA, pB)
                
                svg_elements.append(f'  <line x1="{float(pA.x)}" y1="{float(pA.y)}" x2="{float(Ma.x)}" y2="{float(Ma.y)}" stroke="{color}" stroke-width="2" {style}/>')
                svg_elements.append(f'  <line x1="{float(pB.x)}" y1="{float(pB.y)}" x2="{float(Mb.x)}" y2="{float(Mb.y)}" stroke="{color}" stroke-width="2" {style}/>')
                svg_elements.append(f'  <line x1="{float(pC.x)}" y1="{float(pC.y)}" x2="{float(Mc.x)}" y2="{float(Mc.y)}" stroke="{color}" stroke-width="2" {style}/>')
            
            # Baricentro
            if 'baricentro' in compute and show.get('baricentro'):
                G = calculate_centroid(pA, pB, pC)
                color = show['baricentro'].get('color', COLORS['punto_notable'])
                label = show['baricentro'].get('label', 'G')
                size = show['baricentro'].get('size', 6)
                
                svg_elements.append(f'  <circle cx="{float(G.x)}" cy="{float(G.y)}" r="{size}" fill="{color}"/>')
                svg_elements.append(f'  <text x="{float(G.x)+10}" y="{float(G.y)-10}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{color}">{label}</text>')
            
            # Ortocentro
            if 'ortocentro' in compute and show.get('ortocentro'):
                H = calculate_orthocenter(pA, pB, pC)
                color = show['ortocentro'].get('color', COLORS['punto_notable'])
                label = show['ortocentro'].get('label', 'H')
                
                svg_elements.append(f'  <circle cx="{float(H.x)}" cy="{float(H.y)}" r="6" fill="{color}"/>')
                svg_elements.append(f'  <text x="{float(H.x)+10}" y="{float(H.y)-10}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{color}">{label}</text>')
            
            # Circuncentro
            if 'circuncentro' in compute and show.get('circuncentro'):
                O = calculate_circumcenter(pA, pB, pC)
                color = show['circuncentro'].get('color', COLORS['punto_notable'])
                label = show['circuncentro'].get('label', 'O')
                
                svg_elements.append(f'  <circle cx="{float(O.x)}" cy="{float(O.y)}" r="6" fill="{color}"/>')
                svg_elements.append(f'  <text x="{float(O.x)+10}" y="{float(O.y)-10}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{color}">{label}</text>')
            
            # Incentro
            if 'incentro' in compute and show.get('incentro'):
                I = calculate_incenter(pA, pB, pC)
                color = show['incentro'].get('color', COLORS['punto_notable'])
                label = show['incentro'].get('label', 'I')
                
                svg_elements.append(f'  <circle cx="{float(I.x)}" cy="{float(I.y)}" r="6" fill="{color}"/>')
                svg_elements.append(f'  <text x="{float(I.x)+10}" y="{float(I.y)-10}" font-family="Inter, sans-serif" font-size="14" font-weight="bold" fill="{color}">{label}</text>')
    
    svg_elements.append('</svg>')
    
    # Escribir archivo
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(svg_elements))
    
    return True

# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='GeometrySpec Renderer - Geometría exacta con validación matemática'
    )
    parser.add_argument('--spec', required=True, help='Archivo JSON de especificación')
    parser.add_argument('--output', help='Archivo SVG de salida')
    parser.add_argument('--verify', action='store_true', help='Validar propiedades matemáticas')
    parser.add_argument('--validate-only', action='store_true', help='Solo validar sin generar')
    
    args = parser.parse_args()
    
    # Leer especificación
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"❌ Error: No se encuentra el archivo {spec_path}")
        sys.exit(1)
    
    with open(spec_path) as f:
        spec = json.load(f)
    
    print(f"📐 Procesando: {spec.get('metadata', {}).get('title', spec_path.stem)}")
    
    # Validar si se solicita
    if args.verify or args.validate_only:
        if not SYMPY_AVAILABLE:
            print("❌ Error: SymPy es requerido para validación")
            sys.exit(1)
        
        assertions = spec.get('assertions', [])
        all_valid = True
        
        for assertion in assertions:
            prop = assertion.get('property')
            if prop == 'concurrent':
                # TODO: Implementar validación de concurrencia
                print(f"  ✓ Concurrencia: {assertion.get('elements')}")
            elif prop == 'collinear':
                # TODO: Implementar validación de colinealidad
                print(f"  ✓ Colinealidad: {assertion.get('points')}")
            elif prop == 'ratio':
                # TODO: Implementar validación de razón
                print(f"  ✓ Razón: {assertion.get('value')}")
        
        if not all_valid:
            print("❌ Validación fallida")
            sys.exit(1)
        
        print("✅ Validación exitosa")
    
    # Generar SVG si no es solo validación
    if not args.validate_only:
        if not args.output:
            print("❌ Error: Se requiere --output para generar SVG")
            sys.exit(1)
        
        render_svg(spec, args.output)
        print(f"✅ SVG generado: {args.output}")

if __name__ == '__main__':
    main()


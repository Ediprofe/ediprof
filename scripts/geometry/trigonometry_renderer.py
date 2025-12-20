#!/usr/bin/env python3
"""
📐 Trigonometry Renderer - Triángulos con etiquetas automáticas

Genera SVGs de triángulos rectángulos con:
- Posicionamiento automático de etiquetas (calculado matemáticamente)
- Símbolos de ángulo recto
- Arcos de ángulos
- Cuadros informativos

Uso:
    python scripts/geometry/trigonometry_renderer.py --spec ARCHIVO.json --output ARCHIVO.svg
    python scripts/geometry/trigonometry_renderer.py --batch specs/geometria/trigonometria/

Referencia: .agent/workflows/geometry-exact.md
"""

import argparse
import json
import math
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional

# Importar paleta de colores centralizada
sys.path.insert(0, str(Path(__file__).parent))
from core.colors import COLORS as BASE_COLORS

# ============================================================================
# ESTRUCTURAS DE DATOS
# ============================================================================

@dataclass
class Point:
    x: float
    y: float
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        l = self.length()
        if l == 0:
            return Point(0, 0)
        return Point(self.x / l, self.y / l)
    
    def perpendicular(self):
        """Retorna vector perpendicular (rotación 90° antihorario)"""
        return Point(-self.y, self.x)

@dataclass 
class LabelConfig:
    text: str
    color: str = "#1e293b"
    font_size: int = 14
    font_weight: str = "bold"
    background: str = "#ffffff"
    padding: int = 4
    border_radius: int = 4

# ============================================================================
# CÁLCULOS GEOMÉTRICOS
# ============================================================================

def midpoint(p1: Point, p2: Point) -> Point:
    """Calcula el punto medio de un segmento."""
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

def distance(p1: Point, p2: Point) -> float:
    """Calcula la distancia entre dos puntos."""
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def angle_between_points(center: Point, p1: Point, p2: Point) -> float:
    """Calcula el ángulo en radianes entre dos vectores desde center."""
    v1 = p1 - center
    v2 = p2 - center
    dot = v1.x * v2.x + v1.y * v2.y
    cross = v1.x * v2.y - v1.y * v2.x
    return math.atan2(cross, dot)

def get_label_position_for_side(p1: Point, p2: Point, centroid: Point, offset: float = 25) -> Point:
    """
    Calcula la posición óptima para una etiqueta de lado.
    La etiqueta se coloca perpendicular al lado, hacia el exterior del triángulo.
    """
    mid = midpoint(p1, p2)
    
    # Vector del lado
    side_vec = p2 - p1
    
    # Vector perpendicular (hacia afuera del triángulo)
    perp = side_vec.perpendicular().normalize()
    
    # Determinar dirección correcta (opuesta al centroide)
    to_centroid = centroid - mid
    if perp.x * to_centroid.x + perp.y * to_centroid.y > 0:
        perp = Point(-perp.x, -perp.y)
    
    return mid + perp * offset

def get_angle_arc_path(vertex: Point, p1: Point, p2: Point, radius: float = 25) -> str:
    """Genera el path SVG para un arco de ángulo."""
    # Vectores desde el vértice
    v1 = (p1 - vertex).normalize()
    v2 = (p2 - vertex).normalize()
    
    # Puntos del arco
    start = vertex + v1 * radius
    end = vertex + v2 * radius
    
    # Determinar si es arco mayor o menor
    angle = abs(angle_between_points(vertex, p1, p2))
    large_arc = 1 if angle > math.pi else 0
    sweep = 1 if angle_between_points(vertex, p1, p2) > 0 else 0
    
    return f"M {start.x:.1f} {start.y:.1f} A {radius} {radius} 0 {large_arc} {sweep} {end.x:.1f} {end.y:.1f}"

def get_right_angle_symbol(vertex: Point, p1: Point, p2: Point, size: float = 15) -> str:
    """Genera el path SVG para el símbolo de ángulo recto."""
    v1 = (p1 - vertex).normalize()
    v2 = (p2 - vertex).normalize()
    
    corner1 = vertex + v1 * size
    corner2 = vertex + v1 * size + v2 * size
    corner3 = vertex + v2 * size
    
    return f"M {corner1.x:.1f} {corner1.y:.1f} L {corner2.x:.1f} {corner2.y:.1f} L {corner3.x:.1f} {corner3.y:.1f}"

# ============================================================================
# RENDERIZADO SVG
# ============================================================================

class TrigonometryRenderer:
    """Renderizador de triángulos para trigonometría."""
    
    # Paleta de colores (basada en core.colors + alias específicos)
    COLORS = {
        'hipotenusa': BASE_COLORS['primary'],       # Azul
        'opuesto': BASE_COLORS['accent'],           # Rojo
        'adyacente': BASE_COLORS['secondary'],      # Verde
        'angulo': BASE_COLORS['purple'],            # Violeta
        'angulo_recto': BASE_COLORS['text_light'],  # Gris
        'triangulo_fill': BASE_COLORS['background'],# Fondo claro
        'triangulo_stroke': BASE_COLORS['text'],   # Borde oscuro
        'text': BASE_COLORS['text'],               # Texto
        'background': '#ffffff',                    # Fondo etiqueta
        'info_bg': BASE_COLORS['grid'],            # Fondo cuadro info
        'info_border': '#e2e8f0'                   # Borde cuadro info
    }
    
    def __init__(self, spec: dict):
        self.spec = spec
        self.width = spec.get('canvas', {}).get('width', 600)
        self.height = spec.get('canvas', {}).get('height', 400)
        self.padding = spec.get('canvas', {}).get('padding', 50)
        
        # Extraer vértices
        vertices = spec.get('vertices', {})
        self.A = Point(vertices.get('A', [50, 300])[0], vertices.get('A', [50, 300])[1])
        self.B = Point(vertices.get('B', [250, 300])[0], vertices.get('B', [250, 300])[1])
        self.C = Point(vertices.get('C', [250, 100])[0], vertices.get('C', [250, 100])[1])
        
        # Calcular centroide para posicionamiento de etiquetas
        self.centroid = Point(
            (self.A.x + self.B.x + self.C.x) / 3,
            (self.A.y + self.B.y + self.C.y) / 3
        )
        
        self.svg_elements = []
    
    def render(self) -> str:
        """Renderiza el triángulo completo a SVG."""
        self.svg_elements = []
        
        # Inicio del SVG
        self.svg_elements.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'style="font-family: Inter, system-ui, sans-serif;">'
        )
        
        # Definiciones (filtros, gradientes)
        self._add_definitions()
        
        # Fondo
        self.svg_elements.append(
            f'<rect width="{self.width}" height="{self.height}" fill="{self.COLORS["background"]}"/>'
        )
        
        # Título si existe
        if 'titulo' in self.spec:
            self._render_title()
        
        # Triángulo
        self._render_triangle()
        
        # Ángulos
        self._render_angles()
        
        # Etiquetas de lados
        self._render_side_labels()
        
        # Cuadro de información
        if 'info_box' in self.spec:
            self._render_info_box()
        
        # Cierre del SVG
        self.svg_elements.append('</svg>')
        
        return '\n'.join(self.svg_elements)
    
    def _add_definitions(self):
        """Agrega definiciones SVG (filtros, etc.)."""
        self.svg_elements.append('''  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.15"/>
    </filter>
  </defs>''')
    
    def _render_title(self):
        """Renderiza el título del gráfico."""
        title = self.spec.get('titulo', '')
        self.svg_elements.append(
            f'  <text x="{self.width/2}" y="25" text-anchor="middle" '
            f'font-size="16" font-weight="bold" fill="{self.COLORS["text"]}">{title}</text>'
        )
    
    def _render_triangle(self):
        """Renderiza el triángulo base."""
        fill = self.COLORS['triangulo_fill']
        stroke = self.COLORS['triangulo_stroke']
        
        self.svg_elements.append(
            f'  <polygon points="{self.A.x:.1f},{self.A.y:.1f} '
            f'{self.B.x:.1f},{self.B.y:.1f} {self.C.x:.1f},{self.C.y:.1f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="3" stroke-linejoin="round"/>'
        )
        
        # Vértices como círculos
        for point in [self.A, self.B, self.C]:
            self.svg_elements.append(
                f'  <circle cx="{point.x:.1f}" cy="{point.y:.1f}" r="5" fill="{stroke}"/>'
            )
    
    def _render_angles(self):
        """Renderiza los ángulos (arcos y símbolos de ángulo recto)."""
        angulos = self.spec.get('angulos', {})
        
        for vertex_name, config in angulos.items():
            vertex = getattr(self, vertex_name, None)
            if not vertex:
                continue
            
            # Obtener los otros dos vértices
            other_vertices = [v for v in ['A', 'B', 'C'] if v != vertex_name]
            p1 = getattr(self, other_vertices[0])
            p2 = getattr(self, other_vertices[1])
            
            if config.get('tipo') == 'recto':
                # Símbolo de ángulo recto
                path = get_right_angle_symbol(vertex, p1, p2, size=18)
                self.svg_elements.append(
                    f'  <path d="{path}" fill="none" stroke="{self.COLORS["angulo_recto"]}" '
                    f'stroke-width="2"/>'
                )
            else:
                # Arco de ángulo
                color = config.get('color', self.COLORS['angulo'])
                radius = config.get('radio', 30)
                path = get_angle_arc_path(vertex, p1, p2, radius)
                self.svg_elements.append(
                    f'  <path d="{path}" fill="none" stroke="{color}" stroke-width="2"/>'
                )
            
            # Etiqueta del ángulo
            if 'etiqueta' in config:
                self._render_angle_label(vertex, p1, p2, config)
    
    def _render_angle_label(self, vertex: Point, p1: Point, p2: Point, config: dict):
        """Renderiza la etiqueta de un ángulo."""
        label = config.get('etiqueta', '')
        color = config.get('color', self.COLORS['angulo'])
        offset = config.get('offset_etiqueta', 45)
        
        # Calcular posición de la etiqueta (bisectriz del ángulo)
        v1 = (p1 - vertex).normalize()
        v2 = (p2 - vertex).normalize()
        bisector = Point((v1.x + v2.x) / 2, (v1.y + v2.y) / 2).normalize()
        
        label_pos = vertex + bisector * offset
        
        self.svg_elements.append(
            f'  <text x="{label_pos.x:.1f}" y="{label_pos.y:.1f}" '
            f'text-anchor="middle" dominant-baseline="middle" '
            f'font-size="18" font-weight="bold" fill="{color}">{label}</text>'
        )
    
    def _render_side_labels(self):
        """Renderiza las etiquetas de los lados con posicionamiento automático."""
        lados = self.spec.get('lados', {})
        offset = self.spec.get('offset_etiquetas', 28)
        
        # Mapeo de lados a vértices
        side_vertices = {
            'AB': (self.A, self.B),
            'BC': (self.B, self.C),
            'AC': (self.A, self.C),
            'BA': (self.B, self.A),
            'CB': (self.C, self.B),
            'CA': (self.C, self.A)
        }
        
        for side_name, config in lados.items():
            if side_name not in side_vertices:
                continue
            
            p1, p2 = side_vertices[side_name]
            text = config.get('texto', side_name)
            color = config.get('color', self.COLORS['text'])
            
            # Calcular posición automática
            label_pos = get_label_position_for_side(p1, p2, self.centroid, offset)
            
            # Estimar ancho del texto para el fondo
            text_width = len(text) * 8 + 16
            text_height = 24
            
            # Fondo de la etiqueta
            self.svg_elements.append(
                f'  <rect x="{label_pos.x - text_width/2:.1f}" y="{label_pos.y - text_height/2:.1f}" '
                f'width="{text_width}" height="{text_height}" rx="4" ry="4" '
                f'fill="{self.COLORS["background"]}" filter="url(#shadow)"/>'
            )
            
            # Texto de la etiqueta
            self.svg_elements.append(
                f'  <text x="{label_pos.x:.1f}" y="{label_pos.y:.1f}" '
                f'text-anchor="middle" dominant-baseline="middle" '
                f'font-size="13" font-weight="bold" fill="{color}">{text}</text>'
            )
    
    def _render_info_box(self):
        """Renderiza un cuadro de información con razones trigonométricas."""
        info = self.spec.get('info_box', {})
        x = info.get('x', self.width - 180)
        y = info.get('y', 60)
        width = info.get('width', 170)
        
        lines = info.get('lineas', [])
        titulo = info.get('titulo', '')
        
        # Calcular altura
        height = 35 + len(lines) * 22
        
        # Fondo del cuadro
        self.svg_elements.append(
            f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" ry="8" '
            f'fill="{self.COLORS["info_bg"]}" stroke="{self.COLORS["info_border"]}" stroke-width="1"/>'
        )
        
        # Título del cuadro
        if titulo:
            self.svg_elements.append(
                f'  <text x="{x + width/2}" y="{y + 18}" text-anchor="middle" '
                f'font-size="11" font-weight="bold" fill="#475569">{titulo}</text>'
            )
        
        # Líneas de información
        for i, line in enumerate(lines):
            text = line.get('texto', '')
            color = line.get('color', self.COLORS['text'])
            self.svg_elements.append(
                f'  <text x="{x + 10}" y="{y + 38 + i * 22}" '
                f'font-size="12" fill="{color}">{text}</text>'
            )

def render_spec(spec: dict, output_path: str) -> bool:
    """Renderiza una especificación a archivo SVG."""
    renderer = TrigonometryRenderer(spec)
    svg_content = renderer.render()
    
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(svg_content)
    
    return True

def process_batch(specs_dir: str, output_dir: str):
    """Procesa todos los specs en un directorio."""
    specs_path = Path(specs_dir)
    output_path = Path(output_dir)
    
    if not specs_path.exists():
        print(f"❌ Directorio no encontrado: {specs_path}")
        return
    
    json_files = list(specs_path.glob("*.json"))
    print(f"📁 Encontrados {len(json_files)} archivos JSON")
    
    for json_file in json_files:
        try:
            with open(json_file) as f:
                spec = json.load(f)
            
            output_file = output_path / f"{json_file.stem}.svg"
            render_spec(spec, str(output_file))
            print(f"  ✅ {json_file.name} → {output_file.name}")
        except Exception as e:
            print(f"  ❌ {json_file.name}: {e}")

# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Trigonometry Renderer - Triángulos con etiquetas automáticas'
    )
    parser.add_argument('--spec', help='Archivo JSON de especificación')
    parser.add_argument('--output', help='Archivo SVG de salida')
    parser.add_argument('--batch', help='Directorio con múltiples specs')
    parser.add_argument('--output-dir', default='public/images/geometria/trigonometria',
                       help='Directorio de salida para batch')
    
    args = parser.parse_args()
    
    if args.batch:
        process_batch(args.batch, args.output_dir)
    elif args.spec:
        if not args.output:
            print("❌ Error: Se requiere --output para generar SVG")
            sys.exit(1)
        
        spec_path = Path(args.spec)
        if not spec_path.exists():
            print(f"❌ Error: No se encuentra {spec_path}")
            sys.exit(1)
        
        with open(spec_path) as f:
            spec = json.load(f)
        
        render_spec(spec, args.output)
        print(f"✅ SVG generado: {args.output}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()


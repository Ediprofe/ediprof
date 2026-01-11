"""
📐 Angle Renderer v2.0 - Motor AUTO-CENTRADO para ilustraciones de ángulos

PRINCIPIO FUNDAMENTAL:
  - Los specs definen QUÉ dibujar (ángulo, etiquetas, arcos)
  - El renderer calcula DÓNDE dibujarlo automáticamente
  - El viewBox se ajusta al contenido (CERO espacio en blanco innecesario)

CÓMO FUNCIONA:
  1. Renderiza todo relativo al origen (0, 0) como vértice
  2. Calcula el bounding box del contenido real
  3. Agrega padding mínimo (20px)
  4. Ajusta el viewBox para eliminar espacio en blanco

USO:
    python3 scripts/geometry/angle_renderer.py \\
        --spec specs/geometria/angulos/ejemplo.json \\
        --output public/images/.../ejemplo.svg

PARA AGENTES IA:
  - NO especificar coordenadas absolutas en los specs
  - Solo definir: tipo, ángulos, etiquetas, colores
  - El renderer hace el resto automáticamente
"""

import sys
import os
import json
import math
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.svg_builder import SVGBuilder
from scripts.geometry.core.base import Point
from scripts.geometry.core.colors import COLORS


# =============================================================================
# CONFIGURACIÓN GLOBAL
# =============================================================================

PADDING = 25  # Padding mínimo alrededor del contenido
DEFAULT_RAY_LENGTH = 80  # Longitud estándar de rayos
DEFAULT_ARC_RADIUS = 30  # Radio estándar de arcos
FONT_SIZE_LABEL = 14  # Tamaño de fuente para etiquetas
FONT_SIZE_TITLE = 16  # Tamaño de fuente para títulos


# =============================================================================
# CLASE PARA CALCULAR BOUNDING BOX
# =============================================================================

class BoundingBox:
    """Calcula y acumula el bounding box de elementos."""
    
    def __init__(self):
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
    
    def add_point(self, x: float, y: float):
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)
    
    def add_text(self, x: float, y: float, text: str, font_size: int = 14):
        """Estima el bounding box de texto."""
        width = len(text) * font_size * 0.6
        height = font_size * 1.2
        self.add_point(x - width/2, y - height/2)
        self.add_point(x + width/2, y + height/2)
    
    def get_dimensions(self, padding: float = PADDING):
        width = self.max_x - self.min_x + padding * 2
        height = self.max_y - self.min_y + padding * 2
        return width, height, self.min_x - padding, self.min_y - padding


# =============================================================================
# UTILIDADES TRIGONOMÉTRICAS
# =============================================================================

def polar_to_cartesian(cx: float, cy: float, radius: float, angle_deg: float) -> Point:
    """Convierte coordenadas polares a cartesianas (Y invertido para SVG)."""
    angle_rad = math.radians(angle_deg)
    x = cx + radius * math.cos(angle_rad)
    y = cy - radius * math.sin(angle_rad)
    return Point(x, y)


def get_arc_path(center: Point, radius: float, start_deg: float, end_deg: float) -> str:
    """Genera el path SVG para un arco circular."""
    start = polar_to_cartesian(center.x, center.y, radius, start_deg)
    end = polar_to_cartesian(center.x, center.y, radius, end_deg)
    
    sweep_flag = 0 if end_deg > start_deg else 1
    large_arc_flag = 1 if abs(end_deg - start_deg) >= 180 else 0
    
    return f"M {start.x:.2f} {start.y:.2f} A {radius:.2f} {radius:.2f} 0 {large_arc_flag} {sweep_flag} {end.x:.2f} {end.y:.2f}"


# =============================================================================
# RENDERIZADOR PRINCIPAL (AUTO-CENTRADO)
# =============================================================================

def render_angle_auto(spec: dict) -> tuple:
    """
    Renderiza un ángulo y retorna (elementos_svg, bounding_box).
    Todo se dibuja relativo al origen (0, 0) como vértice.
    """
    construction = spec.get('construction', {})
    spec_type = construction.get('type', 'angle_basic')
    
    elements = []
    defs = []
    bbox = BoundingBox()
    
    # El vértice siempre está en (0, 0)
    vertex = Point(0, 0)
    
    if spec_type == 'angle_basic':
        _render_basic(construction, vertex, elements, defs, bbox)
    elif spec_type == 'angle_rotation':
        _render_rotation(construction, vertex, elements, defs, bbox)
    elif spec_type == 'angle_comparison':
        _render_comparison(construction, elements, defs, bbox)
    elif spec_type == 'angle_special':
        _render_special(construction, vertex, elements, defs, bbox)
    elif spec_type == 'angle_notation':
        _render_notation(construction, vertex, elements, defs, bbox)
    
    return elements, defs, bbox


def _add_arrow_marker(defs: list, color: str, size: int = 10) -> str:
    """Agrega un marcador de flecha a defs y retorna su ID."""
    marker_id = f"arrow-{color.replace('#', '')}-{size}"
    marker_def = f'''
    <marker id="{marker_id}" markerWidth="{size}" markerHeight="{size}" 
            refX="{size * 0.9}" refY="{size/2}" orient="auto"
            markerUnits="userSpaceOnUse">
        <polygon points="0,0 {size},{size/2} 0,{size}" fill="{color}"/>
    </marker>'''
    
    if not any(marker_id in d for d in defs):
        defs.append(marker_def)
    
    return marker_id


def _render_basic(construction: dict, vertex: Point, elements: list, defs: list, bbox: BoundingBox):
    """Renderiza un ángulo básico con vértice, lados y arco."""
    rays = construction.get('rays', [])
    arc_config = construction.get('arc', {})
    vertex_config = construction.get('vertex', {})
    
    ray_length = construction.get('ray_length', DEFAULT_RAY_LENGTH)
    arc_radius = arc_config.get('radius', DEFAULT_ARC_RADIUS)
    arc_color = arc_config.get('color', COLORS['primary'])
    
    # Vértice
    bbox.add_point(vertex.x, vertex.y)
    elements.append(f'<circle cx="{vertex.x:.2f}" cy="{vertex.y:.2f}" r="4" fill="{COLORS["text"]}"/>')
    
    if vertex_config.get('label'):
        label_pos = Point(vertex.x - 15, vertex.y + 15)
        elements.append(
            f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="{FONT_SIZE_TITLE}" font-weight="bold" '
            f'fill="{COLORS["text"]}" text-anchor="middle">{vertex_config["label"]}</text>'
        )
        bbox.add_text(label_pos.x, label_pos.y, vertex_config['label'], FONT_SIZE_TITLE)
    
    # Rayos
    angles = []
    for ray in rays:
        angle_deg = ray.get('angle_deg', 0)
        length = ray.get('length', ray_length)
        color = ray.get('color', COLORS['text_light'])
        label = ray.get('label', '')
        
        angles.append(angle_deg)
        end = polar_to_cartesian(vertex.x, vertex.y, length, angle_deg)
        bbox.add_point(end.x, end.y)
        
        marker_id = _add_arrow_marker(defs, color)
        elements.append(
            f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
            f'x2="{end.x:.2f}" y2="{end.y:.2f}" '
            f'stroke="{color}" stroke-width="2" marker-end="url(#{marker_id})"/>'
        )
        
        if label:
            label_pos = polar_to_cartesian(vertex.x, vertex.y, length + 18, angle_deg)
            elements.append(
                f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
                f'font-family="Inter, sans-serif" font-size="{FONT_SIZE_LABEL}" font-weight="bold" '
                f'fill="{COLORS["text"]}" text-anchor="middle">{label}</text>'
            )
            bbox.add_text(label_pos.x, label_pos.y, label, FONT_SIZE_LABEL)
    
    # Arco
    if len(angles) >= 2 and arc_config.get('show', True):
        start_angle = min(angles)
        end_angle = max(angles)
        arc_path = get_arc_path(vertex, arc_radius, start_angle, end_angle)
        elements.append(f'<path d="{arc_path}" fill="none" stroke="{arc_color}" stroke-width="2"/>')
        
        # Etiqueta del arco
        if arc_config.get('label'):
            mid_angle = (start_angle + end_angle) / 2
            label_pos = polar_to_cartesian(vertex.x, vertex.y, arc_radius + 15, mid_angle)
            elements.append(
                f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
                f'font-family="Inter, sans-serif" font-size="16" font-weight="bold" '
                f'fill="{arc_color}" text-anchor="middle">{arc_config["label"]}</text>'
            )
            bbox.add_text(label_pos.x, label_pos.y, arc_config['label'], 16)
    
    # Etiquetas personalizadas
    for label_cfg in construction.get('custom_labels', []):
        text = label_cfg.get('text', '')
        # Posición relativa al vértice
        rel_angle = label_cfg.get('angle', 20)
        rel_dist = label_cfg.get('distance', 45)
        pos = polar_to_cartesian(vertex.x, vertex.y, rel_dist, rel_angle)
        color = label_cfg.get('color', COLORS['primary'])
        elements.append(
            f'<text x="{pos.x:.2f}" y="{pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="{FONT_SIZE_TITLE}" font-weight="bold" '
            f'fill="{color}" text-anchor="middle">{text}</text>'
        )
        bbox.add_text(pos.x, pos.y, text, FONT_SIZE_TITLE)


def _render_rotation(construction: dict, vertex: Point, elements: list, defs: list, bbox: BoundingBox):
    """Renderiza un ángulo mostrando el giro (lado inicial → terminal)."""
    angle_deg = construction.get('angle_deg', 45)
    direction = construction.get('direction', 'ccw')
    
    ray_length = construction.get('ray_length', DEFAULT_RAY_LENGTH)
    arc_radius = construction.get('arc_radius', DEFAULT_ARC_RADIUS)
    
    if direction != 'ccw':
        angle_deg = -abs(angle_deg)
    
    terminal_color = COLORS['success'] if direction == 'ccw' else COLORS['accent']
    sign = "+" if direction == 'ccw' else "−"
    
    bbox.add_point(vertex.x, vertex.y)
    
    # Lado inicial
    initial_end = polar_to_cartesian(vertex.x, vertex.y, ray_length, 0)
    bbox.add_point(initial_end.x, initial_end.y)
    
    marker_id = _add_arrow_marker(defs, COLORS['text_light'])
    elements.append(
        f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
        f'x2="{initial_end.x:.2f}" y2="{initial_end.y:.2f}" '
        f'stroke="{COLORS["text_light"]}" stroke-width="2" marker-end="url(#{marker_id})"/>'
    )
    
    if construction.get('show_initial_label', True):
        label_pos = Point(vertex.x + ray_length/2, vertex.y + 18)
        elements.append(
            f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="11" '
            f'fill="{COLORS["text_light"]}" text-anchor="middle">Lado Inicial</text>'
        )
        bbox.add_text(label_pos.x, label_pos.y, "Lado Inicial", 11)
    
    # Lado terminal
    terminal_end = polar_to_cartesian(vertex.x, vertex.y, ray_length, angle_deg)
    bbox.add_point(terminal_end.x, terminal_end.y)
    
    marker_id = _add_arrow_marker(defs, terminal_color)
    elements.append(
        f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
        f'x2="{terminal_end.x:.2f}" y2="{terminal_end.y:.2f}" '
        f'stroke="{terminal_color}" stroke-width="3" marker-end="url(#{marker_id})"/>'
    )
    
    if construction.get('show_terminal_label', True):
        label_pos = polar_to_cartesian(vertex.x, vertex.y, ray_length + 25, angle_deg)
        elements.append(
            f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="12" font-weight="bold" '
            f'fill="{terminal_color}" text-anchor="middle">Lado Terminal</text>'
        )
        bbox.add_text(label_pos.x, label_pos.y, "Lado Terminal", 12)
    
    # Arco con flecha
    arc_marker_id = f"arc-arrow-{terminal_color.replace('#', '')}"
    arc_marker = f'''
    <marker id="{arc_marker_id}" markerWidth="8" markerHeight="8" 
            refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse">
        <polygon points="0,0 8,4 0,8" fill="{terminal_color}"/>
    </marker>'''
    if not any(arc_marker_id in d for d in defs):
        defs.append(arc_marker)
    
    arc_path = get_arc_path(vertex, arc_radius, 0, angle_deg)
    elements.append(f'<path d="{arc_path}" fill="none" stroke="{terminal_color}" stroke-width="2" marker-end="url(#{arc_marker_id})"/>')
    
    # Signo
    if construction.get('show_sign', True):
        mid_angle = angle_deg / 2
        sign_pos = polar_to_cartesian(vertex.x, vertex.y, arc_radius + 18, mid_angle)
        elements.append(
            f'<text x="{sign_pos.x:.2f}" y="{sign_pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="20" font-weight="bold" '
            f'fill="{terminal_color}" text-anchor="middle">{sign}</text>'
        )
        bbox.add_text(sign_pos.x, sign_pos.y, sign, 20)


def _render_comparison(construction: dict, elements: list, defs: list, bbox: BoundingBox):
    """Renderiza comparación de ángulos lado a lado."""
    angles_config = construction.get('angles', [])
    num = len(angles_config)
    if num == 0:
        return
    
    # Espaciado horizontal entre ángulos
    spacing = 180
    total_width = spacing * (num - 1)
    start_x = -total_width / 2
    
    for i, cfg in enumerate(angles_config):
        center_x = start_x + i * spacing
        vertex = Point(center_x, 40)
        
        title = cfg.get('title', '')
        if title:
            title_pos = Point(center_x, -50)
            elements.append(
                f'<text x="{title_pos.x:.2f}" y="{title_pos.y:.2f}" '
                f'font-family="Inter, sans-serif" font-size="14" font-weight="bold" '
                f'fill="{cfg.get("color", COLORS["primary"])}" text-anchor="middle">{title}</text>'
            )
            bbox.add_text(title_pos.x, title_pos.y, title, 14)
        
        # Renderizar el ángulo directamente en su posición (NO string replacement)
        ray_length = cfg.get('ray_length', 70)
        arc_radius = cfg.get('arc_radius', 25)
        color = cfg.get('color', COLORS['primary'])
        angle_deg = cfg.get('angle_deg', 45)
        
        # Vértice
        elements.append(f'<circle cx="{vertex.x:.2f}" cy="{vertex.y:.2f}" r="4" fill="{COLORS["text"]}"/>')
        bbox.add_point(vertex.x, vertex.y)
        
        # Rayo inicial (horizontal)
        end1 = polar_to_cartesian(vertex.x, vertex.y, ray_length, 0)
        marker_id = _add_arrow_marker(defs, COLORS['text_light'])
        elements.append(
            f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
            f'x2="{end1.x:.2f}" y2="{end1.y:.2f}" '
            f'stroke="{COLORS["text_light"]}" stroke-width="2" marker-end="url(#{marker_id})"/>'
        )
        bbox.add_point(end1.x, end1.y)
        
        # Rayo terminal (en ángulo)
        end2 = polar_to_cartesian(vertex.x, vertex.y, ray_length, angle_deg)
        marker_id = _add_arrow_marker(defs, color)
        elements.append(
            f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
            f'x2="{end2.x:.2f}" y2="{end2.y:.2f}" '
            f'stroke="{color}" stroke-width="2" marker-end="url(#{marker_id})"/>'
        )
        bbox.add_point(end2.x, end2.y)
        
        # Arco
        arc_path = get_arc_path(vertex, arc_radius, 0, angle_deg)
        elements.append(f'<path d="{arc_path}" fill="none" stroke="{color}" stroke-width="2"/>')
    
    # Mensaje inferior
    if construction.get('message'):
        msg = construction['message']
        msg_pos = Point(0, 100)
        elements.append(
            f'<text x="{msg_pos.x:.2f}" y="{msg_pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="13" '
            f'fill="{COLORS["text_light"]}" text-anchor="middle">{msg}</text>'
        )
        bbox.add_text(msg_pos.x, msg_pos.y, msg, 13)
    
    # Divisor vertical
    if num > 1:
        for i in range(1, num):
            div_x = start_x + i * spacing - spacing/2
            elements.append(
                f'<line x1="{div_x:.2f}" y1="{-60:.2f}" x2="{div_x:.2f}" y2="{90:.2f}" '
                f'stroke="{COLORS["grid"]}" stroke-width="1" stroke-dasharray="4,4"/>'
            )



def _render_special(construction: dict, vertex: Point, elements: list, defs: list, bbox: BoundingBox):
    """Renderiza ángulos especiales (0°, 90°, 180°, 360°)."""
    value = construction.get('value', 0)
    ray_length = construction.get('ray_length', DEFAULT_RAY_LENGTH)
    label = construction.get('label', '')
    
    bbox.add_point(vertex.x, vertex.y)
    
    if value == 0:
        end = polar_to_cartesian(vertex.x, vertex.y, ray_length, 0)
        bbox.add_point(end.x, end.y)
        
        marker_id = _add_arrow_marker(defs, COLORS['primary'])
        elements.append(
            f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
            f'x2="{end.x:.2f}" y2="{end.y:.2f}" '
            f'stroke="{COLORS["primary"]}" stroke-width="3" marker-end="url(#{marker_id})"/>'
        )
        
        # Etiqueta 0°
        label_pos = Point(vertex.x + ray_length/2, vertex.y - 20)
        elements.append(
            f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="18" font-weight="bold" '
            f'fill="{COLORS["primary"]}" text-anchor="middle">0°</text>'
        )
        bbox.add_text(label_pos.x, label_pos.y, "0°", 18)
        
        if label:
            desc_pos = Point(vertex.x + ray_length/2, vertex.y + 30)
            elements.append(
                f'<text x="{desc_pos.x:.2f}" y="{desc_pos.y:.2f}" '
                f'font-family="Inter, sans-serif" font-size="12" '
                f'fill="{COLORS["text_light"]}" text-anchor="middle">{label}</text>'
            )
            bbox.add_text(desc_pos.x, desc_pos.y, label, 12)


def _render_notation(construction: dict, vertex: Point, elements: list, defs: list, bbox: BoundingBox):
    """Renderiza un ángulo mostrando diferentes notaciones."""
    rays = construction.get('rays', [{'angle_deg': -20, 'label': 'X'}, {'angle_deg': 50, 'label': 'Z'}])
    vertex_label = construction.get('vertex_label', 'Y')
    notations = construction.get('notations', ['∠XYZ', '∠ZYX', '∠Y'])
    ray_length = construction.get('ray_length', 80)
    
    bbox.add_point(vertex.x, vertex.y)
    
    # Vértice con etiqueta
    elements.append(f'<circle cx="{vertex.x:.2f}" cy="{vertex.y:.2f}" r="4" fill="{COLORS["text"]}"/>')
    label_pos = Point(vertex.x - 18, vertex.y + 8)
    elements.append(
        f'<text x="{label_pos.x:.2f}" y="{label_pos.y:.2f}" '
        f'font-family="Inter, sans-serif" font-size="{FONT_SIZE_TITLE}" font-weight="bold" '
        f'fill="{COLORS["text"]}" text-anchor="middle">{vertex_label}</text>'
    )
    bbox.add_text(label_pos.x, label_pos.y, vertex_label, FONT_SIZE_TITLE)
    
    # Rayos
    angles = []
    for ray in rays:
        angle_deg = ray.get('angle_deg', 0)
        angles.append(angle_deg)
        end = polar_to_cartesian(vertex.x, vertex.y, ray_length, angle_deg)
        bbox.add_point(end.x, end.y)
        
        marker_id = _add_arrow_marker(defs, COLORS['text_light'])
        elements.append(
            f'<line x1="{vertex.x:.2f}" y1="{vertex.y:.2f}" '
            f'x2="{end.x:.2f}" y2="{end.y:.2f}" '
            f'stroke="{COLORS["text_light"]}" stroke-width="2" marker-end="url(#{marker_id})"/>'
        )
        
        if ray.get('label'):
            lbl_pos = polar_to_cartesian(vertex.x, vertex.y, ray_length + 15, angle_deg)
            elements.append(
                f'<text x="{lbl_pos.x:.2f}" y="{lbl_pos.y:.2f}" '
                f'font-family="Inter, sans-serif" font-size="{FONT_SIZE_LABEL}" font-weight="bold" '
                f'fill="{COLORS["text"]}" text-anchor="middle">{ray["label"]}</text>'
            )
            bbox.add_text(lbl_pos.x, lbl_pos.y, ray['label'], FONT_SIZE_LABEL)
    
    # Arco
    if len(angles) >= 2:
        arc_path = get_arc_path(vertex, 30, min(angles), max(angles))
        elements.append(f'<path d="{arc_path}" fill="none" stroke="{COLORS["primary"]}" stroke-width="2"/>')
    
    # Notaciones debajo
    y_offset = 60
    for i, notation in enumerate(notations):
        pos = Point(vertex.x, vertex.y + y_offset + i * 22)
        elements.append(
            f'<text x="{pos.x:.2f}" y="{pos.y:.2f}" '
            f'font-family="Inter, sans-serif" font-size="16" font-weight="bold" '
            f'fill="{COLORS["primary"]}" text-anchor="middle">{notation}</text>'
        )
        bbox.add_text(pos.x, pos.y, notation, 16)


# =============================================================================
# GENERADOR DE SVG CON AUTO-VIEWBOX
# =============================================================================

# =============================================================================
# TAMAÑOS DE CANVAS - ADAPTATIVO CON ASPECT RATIO CONTROLADO
# =============================================================================

# Límites para proporciones razonables
MIN_WIDTH = 200
MIN_HEIGHT = 100
MIN_ASPECT_RATIO = 2.0  # Width debe ser >= 2x Height para evitar imágenes muy altas
CANVAS_PADDING = 30  # Padding alrededor del contenido


def render_spec(spec: dict, output_path: str):
    """
    Renderiza un spec JSON a SVG con canvas adaptativo.
    
    ESTRATEGIA:
    1. Renderiza contenido relativo al origen
    2. Calcula bounding box del contenido real
    3. Canvas = contenido + padding (con mínimos)
    4. Aplica aspect ratio mínimo 2:1 (evita SVGs muy altos)
    """
    
    # Renderizar contenido (relativo al origen)
    elements, defs, bbox = render_angle_auto(spec)
    
    # Calcular dimensiones del contenido
    content_w, content_h, content_min_x, content_min_y = bbox.get_dimensions(0)
    
    # Canvas adaptativo con límites
    canvas_w = max(content_w + CANVAS_PADDING * 2, MIN_WIDTH)
    canvas_h = max(content_h + CANVAS_PADDING * 2, MIN_HEIGHT)
    
    # Aplicar aspect ratio mínimo (width >= height * 2)
    # Si el canvas es más alto que ancho/2, expandir el ancho
    if canvas_w < canvas_h * MIN_ASPECT_RATIO:
        canvas_w = canvas_h * MIN_ASPECT_RATIO
    
    # Calcular centro del contenido
    content_center_x = content_min_x + content_w / 2
    content_center_y = content_min_y + content_h / 2
    
    # Centro del canvas
    canvas_center_x = canvas_w / 2
    canvas_center_y = canvas_h / 2
    
    # Calcular traslación para centrar
    translate_x = canvas_center_x - content_center_x
    translate_y = canvas_center_y - content_center_y
    
    # Construir SVG con transform
    defs_str = '\n'.join(defs) if defs else ''
    elements_str = '\n    '.join(elements)
    transform = f'translate({translate_x:.2f}, {translate_y:.2f})'
    
    # SVG solo con viewBox (CSS del sitio controla max-height: 280px)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas_w:.0f} {canvas_h:.0f}">
  <defs>{defs_str}</defs>
  <rect x="0" y="0" width="{canvas_w:.0f}" height="{canvas_h:.0f}" fill="white"/>
  <g transform="{transform}">
    {elements_str}
  </g>
</svg>'''
    
    # Guardar
    from pathlib import Path
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(svg)
    
    print(f"✅ SVG generado: {output_path} ({canvas_w:.0f}x{canvas_h:.0f}px)")
    return True


def main():
    parser = argparse.ArgumentParser(description='Renderiza AngleSpec a SVG (auto-centrado)')
    parser.add_argument('--spec', type=str, help='Ruta al archivo JSON spec')
    parser.add_argument('--output', type=str, help='Ruta de salida del SVG')
    parser.add_argument('--spec-dir', type=str, help='Directorio con specs')
    parser.add_argument('--output-dir', type=str, help='Directorio de salida')
    
    args = parser.parse_args()
    
    if args.spec and args.output:
        with open(args.spec, 'r', encoding='utf-8') as f:
            spec = json.load(f)
        render_spec(spec, args.output)
    
    elif args.spec_dir and args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        for filename in os.listdir(args.spec_dir):
            if filename.endswith('.json'):
                spec_path = os.path.join(args.spec_dir, filename)
                output_name = filename.replace('.json', '.svg')
                output_path = os.path.join(args.output_dir, output_name)
                
                with open(spec_path, 'r', encoding='utf-8') as f:
                    spec = json.load(f)
                render_spec(spec, output_path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

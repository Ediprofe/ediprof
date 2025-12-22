"""
📐 SVG Builder - Primitivas para construcción de SVGs

Este módulo proporciona una API fluida para construir SVGs de geometría.
"""

from typing import List, Tuple, Optional
from .base import Point
from .colors import COLORS
from .primitives import escape_xml


class SVGBuilder:
    """Constructor de SVGs con API fluida."""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.elements: List[str] = []
        self.defs: List[str] = []
    
    # ========================================================================
    # PRIMITIVAS BÁSICAS
    # ========================================================================
    
    def line(self, p1: Point, p2: Point, 
             stroke: str = COLORS['primary'], 
             stroke_width: float = 2,
             dashed: bool = False,
             marker_end: str = None) -> 'SVGBuilder':
        """Dibuja una línea entre dos puntos."""
        style = f'stroke-dasharray="5,5"' if dashed else ''
        marker = f'marker-end="url(#{marker_end})"' if marker_end else ''
        self.elements.append(
            f'<line x1="{p1.x:.2f}" y1="{p1.y:.2f}" '
            f'x2="{p2.x:.2f}" y2="{p2.y:.2f}" '
            f'stroke="{stroke}" stroke-width="{stroke_width}" '
            f'{style} {marker}/>'
        )
        return self
    
    def circle(self, center: Point, radius: float,
               fill: str = 'none',
               stroke: str = COLORS['primary'],
               stroke_width: float = 2,
               fill_opacity: float = 1.0) -> 'SVGBuilder':
        """Dibuja un círculo."""
        opacity_attr = f'fill-opacity="{fill_opacity}"' if fill_opacity < 1.0 else ''
        self.elements.append(
            f'<circle cx="{center.x:.2f}" cy="{center.y:.2f}" r="{radius:.2f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" {opacity_attr}/>'
        )
        return self
    
    def point(self, p: Point, radius: float = 5,
              fill: str = COLORS['point'],
              stroke: str = None,
              stroke_width: float = 0) -> 'SVGBuilder':
        """Dibuja un punto (círculo pequeño relleno)."""
        stroke_attr = f'stroke="{stroke}" stroke-width="{stroke_width}"' if stroke else ''
        self.elements.append(
            f'<circle cx="{p.x:.2f}" cy="{p.y:.2f}" r="{radius}" '
            f'fill="{fill}" {stroke_attr}/>'
        )
        return self
    
    def polygon(self, points: List[Point],
                fill: str = COLORS['polygon_fill'],
                stroke: str = COLORS['polygon_stroke'],
                stroke_width: float = 2) -> 'SVGBuilder':
        """Dibuja un polígono."""
        points_str = ' '.join(f'{p.x:.2f},{p.y:.2f}' for p in points)
        self.elements.append(
            f'<polygon points="{points_str}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        )
        return self
    
    def polyline(self, points: List[Point],
                 stroke: str = COLORS['primary'],
                 stroke_width: float = 2,
                 fill: str = 'none') -> 'SVGBuilder':
        """Dibuja una polilínea (línea que conecta varios puntos)."""
        points_str = ' '.join(f'{p.x:.2f},{p.y:.2f}' for p in points)
        self.elements.append(
            f'<polyline points="{points_str}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        )
        return self
    
    def rect(self, x: float, y: float, width: float, height: float,
             fill: str = COLORS['background'],
             stroke: str = 'none',
             stroke_width: float = 0,
             rx: float = 0) -> 'SVGBuilder':
        """Dibuja un rectángulo."""
        self.elements.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{width:.2f}" height="{height:.2f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" rx="{rx}"/>'
        )
        return self
    
    def path(self, d: str,
             fill: str = 'none',
             stroke: str = COLORS['primary'],
             stroke_width: float = 2) -> 'SVGBuilder':
        """Dibuja un path SVG."""
        self.elements.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        )
        return self
    
    # ========================================================================
    # TEXTO Y ETIQUETAS
    # ========================================================================
    
    def text(self, content: str, pos: Point,
             font_size: int = 14,
             font_weight: str = 'normal',
             fill: str = COLORS['text'],
             anchor: str = 'middle',
             baseline: str = 'middle',
             font_family: str = 'Inter, sans-serif') -> 'SVGBuilder':
        """Dibuja texto."""
        escaped = escape_xml(content)
        self.elements.append(
            f'<text x="{pos.x:.2f}" y="{pos.y:.2f}" '
            f'font-family="{font_family}" font-size="{font_size}" '
            f'font-weight="{font_weight}" fill="{fill}" '
            f'text-anchor="{anchor}" dominant-baseline="{baseline}">'
            f'{escaped}</text>'
        )
        return self
    
    def label(self, content: str, pos: Point,
              font_size: int = 12,
              fill: str = COLORS['text'],
              bg_color: str = None,
              padding: float = 4) -> 'SVGBuilder':
        """Dibuja una etiqueta con fondo opcional."""
        if bg_color:
            # Estimar ancho del texto
            text_width = len(content) * font_size * 0.6
            text_height = font_size * 1.2
            self.rect(
                pos.x - text_width/2 - padding,
                pos.y - text_height/2 - padding,
                text_width + padding*2,
                text_height + padding*2,
                fill=bg_color,
                rx=4
            )
        self.text(content, pos, font_size=font_size, fill=fill, font_weight='bold')
        return self
    
    def point_label(self, name: str, pos: Point, coords: Tuple[float, float] = None,
                    offset: Tuple[float, float] = (10, -10),
                    show_coords: bool = True,
                    font_size: int = 12,
                    fill: str = COLORS['text']) -> 'SVGBuilder':
        """Etiqueta un punto con nombre y coordenadas opcionales."""
        label_pos = Point(pos.x + offset[0], pos.y + offset[1])
        
        if show_coords and coords:
            text = f'{name}({coords[0]}, {coords[1]})'
        else:
            text = name
        
        self.text(text, label_pos, font_size=font_size, fill=fill, 
                  font_weight='bold', anchor='start')
        return self
    
    def formula_box(self, formula: str, pos: Point,
                    font_size: int = 14,
                    bg_color: str = COLORS['formula_bg'],
                    text_color: str = COLORS['text'],
                    padding: float = 8) -> 'SVGBuilder':
        """Dibuja una fórmula en un recuadro destacado."""
        text_width = len(formula) * font_size * 0.55
        text_height = font_size * 1.4
        
        self.rect(
            pos.x - text_width/2 - padding,
            pos.y - text_height/2 - padding,
            text_width + padding*2,
            text_height + padding*2,
            fill=bg_color,
            stroke=COLORS['highlight'],
            stroke_width=1,
            rx=6
        )
        self.text(formula, pos, font_size=font_size, fill=text_color, font_weight='bold')
        return self
    
    # ========================================================================
    # ELEMENTOS ESPECIALES
    # ========================================================================
    
    def arrow(self, start: Point, end: Point,
              stroke: str = COLORS['primary'],
              stroke_width: float = 2,
              head_size: float = None) -> 'SVGBuilder':
        """Dibuja una flecha con punta triangular escalada al grosor de línea."""
        # Escalar head_size automáticamente si no se especifica
        if head_size is None:
            head_size = max(10, stroke_width * 3)
        
        # ID único para el marcador basado en color y tamaño
        marker_id = f'arrow-{stroke.replace("#", "")}-{int(head_size)}'
        
        # Marcador con userSpaceOnUse para mejor renderizado
        marker_def = f'''
        <marker id="{marker_id}" markerWidth="{head_size}" markerHeight="{head_size}" 
                refX="{head_size * 0.9}" refY="{head_size / 2}" orient="auto"
                markerUnits="userSpaceOnUse">
            <polygon points="0,0 {head_size},{head_size/2} 0,{head_size}" fill="{stroke}"/>
        </marker>'''
        
        if marker_id not in [d for d in self.defs if marker_id in d]:
            self.defs.append(marker_def)
        
        self.line(start, end, stroke=stroke, stroke_width=stroke_width, marker_end=marker_id)
        return self
    
    def right_angle_mark(self, vertex: Point, p1: Point, p2: Point,
                         size: float = 15,
                         stroke: str = COLORS['auxiliary']) -> 'SVGBuilder':
        """Dibuja el símbolo de ángulo recto."""
        # Vectores unitarios hacia p1 y p2
        v1 = (p1 - vertex).normalize() * size
        v2 = (p2 - vertex).normalize() * size
        
        # Puntos del cuadradito
        corner1 = vertex + v1
        corner2 = vertex + v1 + v2
        corner3 = vertex + v2
        
        self.polyline([corner1, corner2, corner3], stroke=stroke, stroke_width=1.5)
        return self
    
    def brace(self, start: Point, end: Point,
              label: str = None,
              side: str = 'bottom',
              stroke: str = COLORS['auxiliary']) -> 'SVGBuilder':
        """Dibuja una llave con etiqueta opcional."""
        # Simplificado: línea con etiqueta
        mid = start.midpoint(end)
        offset = 15 if side == 'bottom' else -15
        
        self.line(start, end, stroke=stroke, stroke_width=1)
        
        if label:
            label_pos = Point(mid.x, mid.y + offset)
            self.text(label, label_pos, font_size=12, fill=stroke)
        
        return self
    
    # ========================================================================
    # CONSTRUCCIÓN FINAL
    # ========================================================================
    
    def build(self) -> str:
        """Genera el SVG final."""
        defs_str = '\n'.join(self.defs) if self.defs else ''
        elements_str = '\n  '.join(self.elements)
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}">
  <defs>{defs_str}</defs>
  {elements_str}
</svg>'''
        return svg
    
    def save(self, path: str):
        """Guarda el SVG en un archivo."""
        from pathlib import Path
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(self.build())

"""
📐 Coordinate System - Sistema de coordenadas cartesianas para SVG

Este módulo maneja la transformación entre coordenadas matemáticas
y coordenadas SVG, además de dibujar ejes, cuadrículas y etiquetas.
"""

import math
from typing import Tuple, List, Optional
from .base import Point, COLORS
from .svg_builder import SVGBuilder


class CoordinateSystem:
    """
    Sistema de coordenadas cartesianas.
    
    Maneja la transformación entre:
    - Coordenadas matemáticas: Y crece hacia arriba, origen en centro
    - Coordenadas SVG: Y crece hacia abajo, origen en esquina superior izquierda
    """
    
    def __init__(self, 
                 svg_width: int = 600,
                 svg_height: int = 500,
                 x_range: Tuple[float, float] = (-6, 6),
                 y_range: Tuple[float, float] = (-5, 5),
                 padding: int = 50):
        """
        Inicializa el sistema de coordenadas.
        
        Args:
            svg_width: Ancho del SVG en píxeles
            svg_height: Alto del SVG en píxeles
            x_range: Rango del eje X (min, max)
            y_range: Rango del eje Y (min, max)
            padding: Espacio alrededor del área de dibujo
        """
        self.svg_width = svg_width
        self.svg_height = svg_height
        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.padding = padding
        
        # Área de dibujo efectiva
        self.plot_width = svg_width - 2 * padding
        self.plot_height = svg_height - 2 * padding
        
        # Escala (píxeles por unidad)
        self.scale_x = self.plot_width / (self.x_max - self.x_min)
        self.scale_y = self.plot_height / (self.y_max - self.y_min)
        
        # Origen en coordenadas SVG
        self.origin_svg = self.to_svg(Point(0, 0))
    
    def to_svg(self, p: Point) -> Point:
        """Convierte coordenadas matemáticas a coordenadas SVG."""
        svg_x = self.padding + (p.x - self.x_min) * self.scale_x
        svg_y = self.padding + (self.y_max - p.y) * self.scale_y  # Invertir Y
        return Point(svg_x, svg_y)
    
    def to_math(self, p: Point) -> Point:
        """Convierte coordenadas SVG a coordenadas matemáticas."""
        math_x = (p.x - self.padding) / self.scale_x + self.x_min
        math_y = self.y_max - (p.y - self.padding) / self.scale_y
        return Point(math_x, math_y)
    
    def draw_axes(self, builder: SVGBuilder,
                  show_arrows: bool = True,
                  axis_color: str = COLORS['axis'],
                  axis_width: float = 2) -> SVGBuilder:
        """Dibuja los ejes X e Y."""
        # Eje X
        x_start = self.to_svg(Point(self.x_min, 0))
        x_end = self.to_svg(Point(self.x_max, 0))
        
        # Eje Y
        y_start = self.to_svg(Point(0, self.y_min))
        y_end = self.to_svg(Point(0, self.y_max))
        
        if show_arrows:
            builder.arrow(x_start, x_end, stroke=axis_color, stroke_width=axis_width)
            builder.arrow(y_start, y_end, stroke=axis_color, stroke_width=axis_width)
        else:
            builder.line(x_start, x_end, stroke=axis_color, stroke_width=axis_width)
            builder.line(y_start, y_end, stroke=axis_color, stroke_width=axis_width)
        
        # Etiquetas de ejes
        builder.text('x', Point(x_end.x - 5, x_end.y + 20), 
                     font_size=14, font_weight='bold', fill=axis_color)
        builder.text('y', Point(y_end.x - 20, y_end.y + 10), 
                     font_size=14, font_weight='bold', fill=axis_color)
        
        return builder
    
    def draw_grid(self, builder: SVGBuilder,
                  step: float = 1,
                  grid_color: str = COLORS['grid'],
                  grid_width: float = 0.5,
                  custom_x_ticks: List[float] = None) -> SVGBuilder:
        """Dibuja la cuadrícula."""
        
        # Líneas verticales (X)
        if custom_x_ticks:
            x_values = custom_x_ticks
        else:
            x_values = []
            x = math.ceil(self.x_min / step) * step
            while x <= self.x_max:
                x_values.append(x)
                x += step
                
        for x in x_values:
            if x != 0:  # No dibujar sobre el eje Y
                p1 = self.to_svg(Point(x, self.y_min))
                p2 = self.to_svg(Point(x, self.y_max))
                builder.line(p1, p2, stroke=grid_color, stroke_width=grid_width)
        
        # Líneas horizontales (Y)
        y = math.ceil(self.y_min / step) * step
        while y <= self.y_max:
            if y != 0:  # No dibujar sobre el eje X
                p1 = self.to_svg(Point(self.x_min, y))
                p2 = self.to_svg(Point(self.x_max, y))
                builder.line(p1, p2, stroke=grid_color, stroke_width=grid_width)
            y += step
        
        return builder
    
    def draw_ticks(self, builder: SVGBuilder,
                   step: float = 1,
                   tick_size: float = 5,
                   show_labels: bool = True,
                   tick_color: str = COLORS['axis'],
                   label_color: str = COLORS['text_light'],
                   custom_x_ticks: List[float] = None) -> SVGBuilder:
        """Dibuja las marcas y etiquetas en los ejes."""
        origin = self.origin_svg
        
        # Marcas en eje X
        if custom_x_ticks:
            x_values = custom_x_ticks
        else:
            x_values = []
            x = math.ceil(self.x_min / step) * step
            while x <= self.x_max:
                x_values.append(x)
                x += step
                
        for x in x_values:
            if x != 0 or custom_x_ticks:
                p = self.to_svg(Point(x, 0))
                builder.line(
                    Point(p.x, origin.y - tick_size),
                    Point(p.x, origin.y + tick_size),
                    stroke=tick_color, stroke_width=1
                )
                if show_labels:
                    label = str(int(x)) if x == int(x) else f'{x:.1f}'
                    builder.text(label, Point(p.x, origin.y + 18),
                                 font_size=11, fill=label_color)
        
        # Marcas en eje Y
        y = math.ceil(self.y_min / step) * step
        while y <= self.y_max:
            if y != 0:
                p = self.to_svg(Point(0, y))
                builder.line(
                    Point(origin.x - tick_size, p.y),
                    Point(origin.x + tick_size, p.y),
                    stroke=tick_color, stroke_width=1
                )
                if show_labels:
                    label = str(int(y)) if y == int(y) else f'{y:.1f}'
                    builder.text(label, Point(origin.x - 15, p.y),
                                 font_size=11, fill=label_color, anchor='end')
            y += step
        
        # Etiqueta del origen
        if show_labels:
            builder.text('O', Point(origin.x - 12, origin.y + 15),
                         font_size=11, fill=label_color)
        
        return builder
    
    def draw_point(self, builder: SVGBuilder,
                   p: Point,
                   label: str = None,
                   show_coords: bool = True,
                   color: str = COLORS['point'],
                   radius: float = 5,
                   label_offset: Tuple[float, float] = (10, -10)) -> SVGBuilder:
        """Dibuja un punto con etiqueta opcional."""
        svg_p = self.to_svg(p)
        builder.point(svg_p, radius=radius, fill=color)
        
        if label:
            label_pos = Point(svg_p.x + label_offset[0], svg_p.y + label_offset[1])
            if show_coords:
                # Formatear coordenadas
                x_str = str(int(p.x)) if p.x == int(p.x) else f'{p.x:.1f}'
                y_str = str(int(p.y)) if p.y == int(p.y) else f'{p.y:.1f}'
                text = f'{label}({x_str}, {y_str})'
            else:
                text = label
            
            builder.text(text, label_pos, font_size=12, fill=color, 
                         font_weight='bold', anchor='start')
        
        return builder
    
    def draw_segment(self, builder: SVGBuilder,
                     p1: Point, p2: Point,
                     color: str = COLORS['segment'],
                     width: float = 2,
                     dashed: bool = False,
                     label: str = None) -> SVGBuilder:
        """Dibuja un segmento entre dos puntos."""
        svg_p1 = self.to_svg(p1)
        svg_p2 = self.to_svg(p2)
        builder.line(svg_p1, svg_p2, stroke=color, stroke_width=width, dashed=dashed)
        
        if label:
            mid = svg_p1.midpoint(svg_p2)
            builder.text(label, Point(mid.x, mid.y - 10), 
                         font_size=12, fill=color, font_weight='bold')
        
        return builder
    
    def draw_polygon(self, builder: SVGBuilder,
                     vertices: List[Point],
                     fill: str = COLORS['polygon_fill'],
                     stroke: str = COLORS['polygon_stroke'],
                     stroke_width: float = 2) -> SVGBuilder:
        """Dibuja un polígono."""
        svg_vertices = [self.to_svg(v) for v in vertices]
        builder.polygon(svg_vertices, fill=fill, stroke=stroke, stroke_width=stroke_width)
        return builder
    
    def draw_right_triangle(self, builder: SVGBuilder,
                            p1: Point, p2: Point,
                            color: str = COLORS['auxiliary'],
                            fill: str = 'none') -> SVGBuilder:
        """
        Dibuja un triángulo rectángulo auxiliar entre dos puntos.
        Útil para mostrar la fórmula de distancia.
        """
        # El tercer vértice está en (x2, y1) o (x1, y2)
        p3 = Point(p2.x, p1.y)
        
        svg_p1 = self.to_svg(p1)
        svg_p2 = self.to_svg(p2)
        svg_p3 = self.to_svg(p3)
        
        # Dibujar triángulo
        if fill != 'none':
            builder.polygon([svg_p1, svg_p3, svg_p2], fill=fill, stroke='none')
        
        # Catetos (punteados)
        builder.line(svg_p1, svg_p3, stroke=color, stroke_width=1.5, dashed=True)
        builder.line(svg_p3, svg_p2, stroke=color, stroke_width=1.5, dashed=True)
        
        # Marca de ángulo recto
        builder.right_angle_mark(svg_p3, svg_p1, svg_p2, size=12, stroke=color)
        
        return builder
    
    def draw_distance_labels(self, builder: SVGBuilder,
                             p1: Point, p2: Point,
                             dx_label: str = 'Δx',
                             dy_label: str = 'Δy',
                             color: str = COLORS['auxiliary']) -> SVGBuilder:
        """Dibuja las etiquetas de distancia horizontal y vertical."""
        p3 = Point(p2.x, p1.y)
        
        svg_p1 = self.to_svg(p1)
        svg_p3 = self.to_svg(p3)
        svg_p2 = self.to_svg(p2)
        
        # Etiqueta Δx (debajo del cateto horizontal)
        mid_x = svg_p1.midpoint(svg_p3)
        builder.text(dx_label, Point(mid_x.x, mid_x.y + 15), 
                     font_size=12, fill=color, font_weight='bold')
        
        # Etiqueta Δy (a la derecha del cateto vertical)
        mid_y = svg_p3.midpoint(svg_p2)
        builder.text(dy_label, Point(mid_y.x + 15, mid_y.y), 
                     font_size=12, fill=color, font_weight='bold')
        
        return builder

    def draw_function(self, builder: SVGBuilder,
                      func: callable,
                      x_range: Tuple[float, float] = None,
                      samples: int = 100,
                      color: str = COLORS['primary'],
                      width: float = 2.5,
                      dashed: bool = False) -> SVGBuilder:
        """Dibuja una función y = f(x)."""
        if x_range is None:
            x_range = (self.x_min, self.x_max)
        
        x_start, x_end = x_range
        step = (x_end - x_start) / (samples - 1)
        
        points = []
        for i in range(samples):
            x = x_start + i * step
            try:
                y = func(x)
                # Verificar si el punto está dentro del rango Y visible (con un margen generoso)
                if self.y_min - 5 <= y <= self.y_max + 5:
                    points.append(self.to_svg(Point(x, y)))
                else:
                    # Si salimos del rango, dibujamos lo acumulado y cortamos
                    if len(points) >= 2:
                        self._draw_polyline_segment(builder, points, color, width, dashed)
                    points = []
            except (ValueError, ZeroDivisionError, OverflowError):
                if len(points) >= 2:
                    self._draw_polyline_segment(builder, points, color, width, dashed)
                points = []
        
        if len(points) >= 2:
            self._draw_polyline_segment(builder, points, color, width, dashed)
            
        return builder

    def _draw_polyline_segment(self, builder: SVGBuilder, points: List[Point], 
                               color: str, width: float, dashed: bool):
        """Helper para dibujar un segmento de polilínea."""
        style = 'stroke-dasharray="6,4"' if dashed else ''
        points_str = ' '.join(f'{p.x:.2f},{p.y:.2f}' for p in points)
        builder.elements.append(
            f'<polyline points="{points_str}" '
            f'fill="none" stroke="{color}" stroke-width="{width}" '
            f'{style} stroke-linecap="round" stroke-linejoin="round"/>'
        )

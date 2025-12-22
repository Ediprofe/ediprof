"""
📈 MathPlotter - Tu propia "librería" de gráficos matemáticos.

Esta clase encapsula toda la complejidad de SVGBuilder y CoordinateSystem
para ofrecer una interfaz sencilla (tipo Matplotlib) pero con el diseño
exacto de Ediprofe.

Uso:
    plot = MathPlotter(title="Mi Gráfico")
    plot.add_function(lambda x: x**2, label="f(x)=x²")
    plot.add_point(2, 4, label="(2,4)")
    plot.save("output.svg")
"""

from typing import Tuple, Callable, Optional, List
from pathlib import Path
from .base import Point, COLORS
from .svg_builder import SVGBuilder
from .coordinate_system import CoordinateSystem

class MathPlotter:
    def __init__(self, 
                 width: int = 600, 
                 height: int = 500, 
                 x_range: Tuple[float, float] = (-6, 6),
                 y_range: Tuple[float, float] = (-5, 5),
                 title: str = None,
                 show_grid: bool = True,
                 show_axes: bool = True,
                 grid_step: float = 1,
                 custom_x_ticks: List[float] = None):
        
        self.width = width
        self.height = height
        self.coord = CoordinateSystem(width, height, x_range, y_range, padding=60)
        self.builder = SVGBuilder(width, height)
        self.legend_items = []
        
        # 1. Fondo limpio
        self.builder.rect(0, 0, width, height, fill='white')
        
        # 2. Título
        if title:
            self.builder.text(title, Point(width/2, 30), 
                            font_size=16, font_weight='bold', fill=COLORS['text'])
            
        # 3. Grid y Ejes (Configurables)
        if show_grid:
            self.coord.draw_grid(self.builder, step=grid_step, custom_x_ticks=custom_x_ticks)
        
        if show_axes:
            self.coord.draw_axes(self.builder, show_arrows=True)
            # Los ticks numéricos solo si es un gráfico matemático estándar
            if show_grid: 
                self.coord.draw_ticks(self.builder, step=grid_step, custom_x_ticks=custom_x_ticks)

    def plot(self, 
             func: Callable[[float], float], 
             label: str = None, 
             color: str = 'primary',
             width: float = 3,
             dashed: bool = False) -> 'MathPlotter':
        """Dibuja una función matemática."""
        
        # Resolver color si es nombre de clave
        color_hex = COLORS.get(color, color)
        
        self.coord.draw_function(
            self.builder, 
            func, 
            color=color_hex, 
            width=width, 
            dashed=dashed
        )
        
        if label:
            self.legend_items.append({
                'label': label,
                'color': color_hex,
                'dashed': dashed
            })
            
        return self

    def scatter(self, x: float, y: float, label: str = None, color: str = 'accent') -> 'MathPlotter':
        """Dibuja un punto destacado (tipo intersección)."""
        color_hex = COLORS.get(color, color)
        p = Point(x, y)
        svg_p = self.coord.to_svg(p)
        
        # Halo blanco
        self.builder.point(svg_p, radius=9, fill='white')
        # Punto real
        self.builder.point(svg_p, radius=5, fill=color_hex, stroke='white', stroke_width=2)
        
        if label:
            # Tooltip estilo "Ediprofe"
            text_width = len(label) * 7 + 16
            rect_x = svg_p.x - text_width/2
            rect_y = svg_p.y - 38
            
            # Sombra (simulada con gris)
            # self.builder.rect(rect_x + 2, rect_y + 2, text_width, 26, 
            #                 fill='#000000', fill_opacity=0.1, rx=6)
            # Caja
            self.builder.rect(rect_x, rect_y, text_width, 26, 
                            fill='white', stroke=color_hex, stroke_width=1.5, rx=6)
            # Texto
            self.builder.text(label, Point(svg_p.x, rect_y + 17), 
                            font_size=12, fill=color_hex, font_weight='bold')
            
        return self

    def bar(self, categories: List[str], values: List[float], color: str = 'primary', width: float = 0.6) -> 'MathPlotter':
        """Dibuja un gráfico de barras vertical."""
        color_hex = COLORS.get(color, color)
        
        for i, (cat, val) in enumerate(zip(categories, values)):
            # Usamos x = i + 1 para las posiciones
            x_center = i + 1
            
            # Coordenadas SVG
            # Top-Left del rectángulo (en coordenadas matemáticas, y=val)
            p_top = self.coord.to_svg(Point(x_center - width/2, val))
            # Bottom-Right del rectángulo (en coordenadas matemáticas, y=0)
            p_bottom = self.coord.to_svg(Point(x_center + width/2, 0))
            
            rect_w = p_bottom.x - p_top.x
            rect_h = p_bottom.y - p_top.y
            
            # Barra
            self.builder.rect(p_top.x, p_top.y, rect_w, rect_h, 
                            fill=color_hex, stroke='none', rx=4) # rx=4 para bordes redondeados suaves
            
            # Etiqueta Categoría (Eje X)
            p_label = self.coord.to_svg(Point(x_center, 0))
            self.builder.text(cat, Point(p_label.x, p_label.y + 25), 
                            font_size=12, fill=COLORS['text'], font_weight='bold')
            
            # Etiqueta Valor (Encima de la barra)
            self.builder.text(str(val), Point(p_top.x + rect_w/2, p_top.y - 8), 
                            font_size=11, fill=COLORS['text_light'])
                            
        return self

    def histogram(self, 
                  intervals: List[Tuple[float, float]], 
                  frequencies: List[float], 
                  color: str = 'primary',
                  edge_color: str = 'white',
                  show_values: bool = False) -> 'MathPlotter':
        """Dibuja un histograma basado en intervalos y frecuencias."""
        color_hex = COLORS.get(color, color)
        edge_hex = COLORS.get(edge_color, edge_color)
        
        for (start, end), freq in zip(intervals, frequencies):
            # Coordenadas SVG
            # Top-Left del rectángulo (en coordenadas matemáticas: x=start, y=freq)
            p_top = self.coord.to_svg(Point(start, freq))
            # Bottom-Right del rectángulo (en coordenadas matemáticas: x=end, y=0)
            p_bottom = self.coord.to_svg(Point(end, 0))
            
            rect_w = p_bottom.x - p_top.x
            rect_h = p_bottom.y - p_top.y
            
            self.builder.rect(p_top.x, p_top.y, rect_w, rect_h, 
                            fill=color_hex, stroke=edge_hex, stroke_width=1)
            
            if show_values:
                # Texto con la frecuencia encima de la barra
                center_x = p_top.x + rect_w / 2
                self.builder.text(str(freq), Point(center_x, p_top.y - 8),
                                font_size=12, fill=COLORS['text'], font_weight='bold')
                            
        return self

    def add_legend(self) -> 'MathPlotter':
        """Dibuja la leyenda automáticamente basada en los plots."""
        if not self.legend_items:
            return self
            
        # Configuración de la caja
        item_height = 20
        padding = 15
        box_width = 160
        box_height = padding * 2 + len(self.legend_items) * item_height
        
        x = self.width - box_width - 20
        y = 60
        
        # Fondo semitransparente (simulado con blanco sólido por ahora)
        self.builder.rect(x, y, box_width, box_height, 
                        fill='white', stroke=COLORS['grid'], rx=8)
        
        for i, item in enumerate(self.legend_items):
            item_y = y + padding + i * item_height + 5
            
            # Línea de muestra
            self.builder.line(
                Point(x + 15, item_y), 
                Point(x + 45, item_y),
                stroke=item['color'],
                stroke_width=3,
                dashed=item['dashed']
            )
            
            # Texto
            self.builder.text(
                item['label'], 
                Point(x + 55, item_y + 4), 
                font_size=11, 
                anchor='start',
                fill=COLORS['text']
            )
            
        return self

    def save(self, filepath: str):
        """Guarda el archivo SVG."""
        self.builder.save(filepath)
        print(f"✅ Gráfico guardado: {filepath}")

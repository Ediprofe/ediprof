
import svgwrite
from sympy import Point, Line, Triangle, Segment, Circle
from sympy.geometry import intersection
import os
import sys
import math
from pathlib import Path

# Importar paleta de colores centralizada
sys.path.insert(0, str(Path(__file__).parent))
from core.colors import COLORS as BASE_COLORS

class GeometryPlotter:
    def __init__(self, filename, width=500, height=400, padding=40):
        self.filename = filename
        self.width = width
        self.height = height
        self.dwg = svgwrite.Drawing(filename, size=(width, height))
        # No grid - Clean background
        self.dwg.add(self.dwg.rect(insert=(0,0), size=('100%','100%'), fill=BASE_COLORS['background']))
        
        # DEFINICIÓN DE ESTILOS (basado en core.colors)
        self.colors = {
            'vertex': BASE_COLORS['text'],
            'side': BASE_COLORS['triangle_stroke'],
            'median': BASE_COLORS['medianas'],
            'altitude': BASE_COLORS['alturas'],
            'bisector': BASE_COLORS['bisectrices'],
            'bisector_perp': BASE_COLORS['mediatrices'],
            'point_main': BASE_COLORS['punto_notable'],
            'aux': BASE_COLORS['auxiliary'],
            'fill': BASE_COLORS['grid']
        }

        self.styles = {
            'point': {'r': 4.5, 'fill': BASE_COLORS['text'], 'stroke': 'white', 'stroke_width': 2},
            'highlight_point': {'r': 7, 'fill': self.colors['point_main'], 'stroke': 'white', 'stroke_width': 2.5},
            'midpoint': {'r': 3.5, 'fill': 'white', 'stroke': self.colors['aux'], 'stroke_width': 2},
            
            'triangle_fill': {'fill': 'white', 'stroke': self.colors['side'], 'stroke_width': 3, 'stroke_linejoin': 'round', 'stroke_linecap': 'round'},
            
            'median_line': {'stroke': self.colors['median'], 'stroke_width': 2.5, 'stroke_dasharray': '5,4'},
            'altitude_line': {'stroke': self.colors['altitude'], 'stroke_width': 2.5, 'stroke_dasharray': '5,4'},
            'bisector_line': {'stroke': self.colors['bisector'], 'stroke_width': 2.5, 'stroke_dasharray': '5,4'},
            'mediator_line': {'stroke': self.colors['bisector_perp'], 'stroke_width': 2.5}, 
            'euler_line': {'stroke': BASE_COLORS['auxiliary'], 'stroke_width': 4, 'stroke_opacity': 0.4},
            
            'circle_main': {'fill': 'none', 'stroke': BASE_COLORS['primary'], 'stroke_width': 2.5},
            'circle_fill': {'fill': BASE_COLORS['primary'], 'fill_opacity': 0.08},
            
            'text': {'font_family': 'Arial, Helvetica, sans-serif', 'font_size': 16, 'fill': BASE_COLORS['text'], 'font_weight': 'bold'}, 
            'text_sub': {'font_family': 'Arial, Helvetica, sans-serif', 'font_size': 13, 'fill': BASE_COLORS['text_light'], 'font_weight': 'normal'}
        }
        
    def to_svg(self, p):
        return (float(p.x), float(p.y))

    def line(self, p1, p2, **style):
        self.dwg.add(self.dwg.line(start=self.to_svg(p1), end=self.to_svg(p2), **style))

    def right_angle_mark(self, vertex, p1, p2, size=15):
        # Dibuja un cuadradito de ángulo recto en 'vertex' alineado con p1 y p2
        # (Idealmente calcular vectores, aquí haremos algo simple si es ortogonal a ejes)
        # Para generalizar: Vector v1 = norm(p1-vertex), v2 = norm(p2-vertex)
        # Mark = vertex + v1*size + v2*size
        
        # Sympy geometry
        v = Point(float(vertex.x), float(vertex.y))
        a = Point(float(p1.x), float(p1.y))
        b = Point(float(p2.x), float(p2.y))
        
        vec1 = a - v
        vec2 = b - v
        
        # Normalize
        len1 = math.sqrt(float(vec1.x)**2 + float(vec1.y)**2)
        len2 = math.sqrt(float(vec2.x)**2 + float(vec2.y)**2)
        
        if len1 == 0 or len2 == 0: return

        u1 = Point(vec1.x/len1, vec1.y/len1)
        u2 = Point(vec2.x/len2, vec2.y/len2)
        
        p_a = v + u1 * size
        p_b = v + u2 * size
        p_corner = v + u1 * size + u2 * size
        
        path_data = f"M {float(p_a.x)},{float(p_a.y)} L {float(p_corner.x)},{float(p_corner.y)} L {float(p_b.x)},{float(p_b.y)}"
        self.dwg.add(self.dwg.path(d=path_data, fill="none", stroke=self.colors['aux'], stroke_width=1.5))
        # Punto un centro si se quiere
        # self.dwg.add(self.dwg.circle(center=((p_corner.x+v.x)/2, (p_corner.y+v.y)/2), r=1, fill=self.colors['aux']))

    def tick_mark(self, p1, p2, count=1):
        # Dibuja pequeñas marcas en el segmento p1-p2 para indicar igualdad
        mid = p1.midpoint(p2)
        # Vector dirección
        vec = p2 - p1
        length = math.sqrt(float(vec.x)**2 + float(vec.y)**2)
        u = Point(vec.x/length, vec.y/length)
        perp = Point(-u.y, u.x) # Vector perpendicular
        
        size = 5
        spacing = 3
        
        start_offset = - ((count - 1) * spacing) / 2
        
        for i in range(count):
            ox = start_offset + i * spacing
            center_tick = mid + u * ox
            t1 = center_tick + perp * size
            t2 = center_tick - perp * size
            self.line(t1, t2, stroke=self.colors['side'], stroke_width=1.5)

    def draw_triangle(self, A, B, C):
        self.dwg.add(self.dwg.polygon(points=[self.to_svg(A), self.to_svg(B), self.to_svg(C)], **self.styles['triangle_fill']))

    def point(self, p, label=None, off=(10,-10), **style):
        self.dwg.add(self.dwg.circle(center=self.to_svg(p), **style))
        if label:
            s = self.styles['text'].copy()
            if 'fill' in style: s['fill'] = style['fill'] # Match label color to point
            self.dwg.add(self.dwg.text(label, insert=(float(p.x)+off[0], float(p.y)+off[1]), **s))

    def draw_circle(self, center, radius, **style):
        coords = self.to_svg(center)
        self.dwg.add(self.dwg.circle(center=coords, r=float(radius), **style))

    def save(self):
        self.dwg.save()
        print(f"Saved {self.filename}")


def generate_points():
    output_dir = "public/images/geometria/triangulos"

    # --- 1. BARICENTRO (MEDIANAS) ---
    plot = GeometryPlotter(f"{output_dir}/baricentro.svg")
    A, B, C = Point(50, 300), Point(450, 300), Point(200, 50)
    T = Triangle(A, B, C)
    
    plot.draw_triangle(A, B, C)
    
    # Puntos medios
    M_a = T.sides[0].midpoint # de BC
    M_b = T.sides[1].midpoint # de AC
    M_c = T.sides[2].midpoint # de AB (lado c)
    
    G = T.centroid

    # Dibujar Medianas
    plot.line(A, M_a, **plot.styles['median_line'])
    plot.line(B, M_b, **plot.styles['median_line'])
    plot.line(C, M_c, **plot.styles['median_line'])
    
    # Marcas de igualdad en los lados (didáctico: M_a divide BC en dos iguales)
    plot.tick_mark(B, M_a, count=1)
    plot.tick_mark(M_a, C, count=1)
    
    plot.tick_mark(C, M_b, count=2)
    plot.tick_mark(M_b, A, count=2)
    
    # Puntos Clave
    plot.point(M_a, "Ma", off=(5,15), **plot.styles['midpoint'])
    plot.point(M_b, "Mb", off=(-25,0), **plot.styles['midpoint'])
    plot.point(M_c, "Mc", off=(5,15), **plot.styles['midpoint'])
    
    plot.point(A, "A", off=(-15, 0), **plot.styles['point'])
    plot.point(B, "B", off=(10, 0), **plot.styles['point'])
    plot.point(C, "C", off=(-5, -15), **plot.styles['point'])
    
    plot.point(G, "G (Baricentro)", off=(10,5), **plot.styles['highlight_point'])
    
    # Texto explicativo dentro del SVG (opcional, pero ayuda)
    plot.dwg.add(plot.dwg.text("Medianas: Unen vértice con punto medio opuesto", insert=(250, 380), text_anchor="middle", **plot.styles['text_sub']))

    plot.save()

    # --- 2. ORTOCENTRO (ALTURAS) --- 
    # Usaremos un acutángulo claro
    plot = GeometryPlotter(f"{output_dir}/ortocentro-acutangulo.svg")
    A, B, C = Point(100, 300), Point(400, 300), Point(200, 50)
    T = Triangle(A, B, C)
    plot.draw_triangle(A, B, C)
    H = T.orthocenter
    
    # Alturas
    # Pie de altura desde A a BC
    foot_A = T.sides[0].projection(A)
    foot_B = T.sides[1].projection(B)
    foot_C = T.sides[2].projection(C)
    
    plot.line(A, foot_A, **plot.styles['altitude_line'])
    plot.line(B, foot_B, **plot.styles['altitude_line'])
    plot.line(C, foot_C, **plot.styles['altitude_line'])
    
    # Marcas de 90 grados (CRUCIAL para didáctica)
    plot.right_angle_mark(foot_A, A, C) # A es el que baja, C es un extremo de la base
    plot.right_angle_mark(foot_B, B, A) # B baja a AC
    plot.right_angle_mark(foot_C, C, B) # C baja a AB
    
    plot.point(A, "A", off=(-15,10), **plot.styles['point'])
    plot.point(B, "B", off=(10,10), **plot.styles['point'])
    plot.point(C, "C", off=(-5,-15), **plot.styles['point'])
    plot.point(H, "H (Ortocentro)", off=(10, 5), **plot.styles['highlight_point'])
    
    plot.dwg.add(plot.dwg.text("Alturas: Perpendiculares desde el vértice al lado opuesto", insert=(250, 380), text_anchor="middle", **plot.styles['text_sub']))
    plot.save()

    # --- 3. INCENTRO (BISECTRICES) ---
    plot = GeometryPlotter(f"{output_dir}/incentro.svg")
    A, B, C = Point(50, 320), Point(450, 320), Point(150, 50)
    T = Triangle(A, B, C)
    plot.draw_triangle(A, B, C)
    I = T.incenter
    
    # Bisectrices (segmentos desde vértice hasta lado opuesto pasando por I)
    inter_a = intersection(Line(A, I), Line(B,C))[0]
    inter_b = intersection(Line(B, I), Line(A,C))[0]
    inter_c = intersection(Line(C, I), Line(A,B))[0]
    
    plot.line(A, inter_a, **plot.styles['bisector_line'])
    plot.line(B, inter_b, **plot.styles['bisector_line'])
    plot.line(C, inter_c, **plot.styles['bisector_line'])
    
    # Incírculo
    plot.draw_circle(I, T.inradius, **plot.styles['circle_main'])
    plot.dwg.add(plot.dwg.circle(center=plot.to_svg(I), r=float(T.inradius), **plot.styles['circle_fill']))
    
    # Marcas de ángulos iguales (Arcos pequeños en vértices)
    # Esto es complejo de hacer bien en script rápido, lo omito por limpieza
    # pero el incírculo ya deja claro la equidistancia a los lados
    
    # Radios perpendiculares (para mostrar propiedad de tangencia)
    # Proyección de I sobre los lados
    p_a = T.sides[0].projection(I)
    p_b = T.sides[1].projection(I)
    p_c = T.sides[2].projection(I)
    
    plot.line(I, p_a, stroke=plot.colors['aux'], stroke_dasharray='2,2')
    plot.line(I, p_b, stroke=plot.colors['aux'], stroke_dasharray='2,2')
    plot.line(I, p_c, stroke=plot.colors['aux'], stroke_dasharray='2,2')
    plot.point(p_a, r=2, fill=plot.colors['aux'])
    plot.point(p_b, r=2, fill=plot.colors['aux'])
    plot.point(p_c, r=2, fill=plot.colors['aux'])

    plot.point(A, "A", off=(-15,5), **plot.styles['point'])
    plot.point(B, "B", off=(10,5), **plot.styles['point'])
    plot.point(C, "C", off=(-5,-15), **plot.styles['point'])
    plot.point(I, "I (Incentro)", off=(0,5), **plot.styles['highlight_point'])
    
    plot.dwg.add(plot.dwg.text("Bisectrices: Dividen el ángulo en dos iguales", insert=(250, 380), text_anchor="middle", **plot.styles['text_sub']))
    plot.save()

    # --- 4. CIRCUNCENTRO (MEDIATRICES) ---
    plot = GeometryPlotter(f"{output_dir}/circuncentro.svg")
    A, B, C = Point(100, 280), Point(400, 280), Point(300, 80)
    T = Triangle(A, B, C)
    plot.draw_triangle(A, B, C)
    O = T.circumcenter
    R = T.circumradius
    
    # Circuncírculo
    plot.draw_circle(O, R, **plot.styles['circle_main'])
    plot.dwg.add(plot.dwg.circle(center=plot.to_svg(O), r=float(R), **plot.styles['circle_fill']))
    
    # Mediatrices (Perpendicular por el punto medio)
    # Lado AB. Midpoint M_c. Perpendicular line
    M_c = T.sides[2].midpoint
    M_a = T.sides[0].midpoint
    # Dibujar la línea de mediatriz un poco larga
    # Vector unitario perp a AB
    v_unit = Line(A, B).direction.unit
    v_perp = Point(-v_unit.y, v_unit.x)
    
    # Dibujar mediatriz AB
    plot.line(M_c - v_perp*50, M_c + v_perp*150, **plot.styles['mediator_line']) # Ajustar largo
    plot.right_angle_mark(M_c, M_c + v_perp*10, B)
    plot.point(M_c, r=2, fill=plot.colors['bisector_perp'])
    
    # Dibujar mediatriz BC
    # Vector perp a BC
    v_unit_a = Line(B, C).direction.unit
    v_perp_a = Point(-v_unit_a.y, v_unit_a.x)
    plot.line(M_a - v_perp_a*150, M_a + v_perp_a*50, **plot.styles['mediator_line'])
    plot.right_angle_mark(M_a, M_a + v_perp_a*10, C)
    plot.point(M_a, r=2, fill=plot.colors['bisector_perp'])

    # El punto O es la intersección
    plot.point(O, "O (Circuncentro)", off=(10,10), **plot.styles['highlight_point'])
    
    # Radios a vértices (opcional, para ver equidistancia)
    plot.line(O, A, stroke=plot.colors['aux'], stroke_dasharray='2,2')
    plot.line(O, B, stroke=plot.colors['aux'], stroke_dasharray='2,2')
    plot.line(O, C, stroke=plot.colors['aux'], stroke_dasharray='2,2')
    
    plot.point(A, "A", off=(-15,10), **plot.styles['point'])
    plot.point(B, "B", off=(10,10), **plot.styles['point'])
    plot.point(C, "C", off=(-5,-15), **plot.styles['point'])

    plot.dwg.add(plot.dwg.text("Mediatrices: Perpendiculares por el punto medio", insert=(250, 380), text_anchor="middle", **plot.styles['text_sub']))
    plot.save()

    # --- 5. RECTA EULER ---
    plot = GeometryPlotter(f"{output_dir}/recta-euler.svg")
    A, B, C = Point(50, 300), Point(450, 300), Point(350, 50) # Scalene visible
    T = Triangle(A, B, C)
    plot.draw_triangle(A, B, C)
    
    G = T.centroid
    H = T.orthocenter
    O = T.circumcenter
    
    # Linea de Euler
    # Extender segmento OH
    vec = H - O
    p_start = O - vec * 0.4
    p_end = H + vec * 0.4
    plot.line(p_start, p_end, **plot.styles['euler_line'])
    
    plot.point(A, "A", **plot.styles['point'])
    plot.point(B, "B", **plot.styles['point'])
    plot.point(C, "C", **plot.styles['point'])
    
    plot.point(O, "O", off=(-15,-10), fill=BASE_COLORS['primary'], r=5)
    plot.point(G, "G", off=(5,15), fill=BASE_COLORS['secondary'], r=5)
    plot.point(H, "H", off=(5,15), fill=BASE_COLORS['accent'], r=5)
    
    plot.dwg.add(plot.dwg.text("O, G y H siempre alineados", insert=(250, 380), text_anchor="middle", **plot.styles['text_sub']))
    plot.save()

if __name__ == "__main__":
    generate_points()

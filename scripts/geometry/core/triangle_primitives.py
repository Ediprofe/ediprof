"""
🔺 Triangle Primitives - Bloques reutilizables para dibujar triángulos

IMPORTANTE: Usar estos helpers en lugar de duplicar código en renderers.

Uso:
    from core.triangle_primitives import draw_triangle, draw_angle_arc, draw_tick_marks
"""

import math
from typing import List, Tuple, Optional
from .colors import COLORS


def draw_triangle(
    pts: List[Tuple[float, float]], 
    stroke: str = None,
    fill: str = "none",
    stroke_width: float = 2.5,
    stroke_colors: List[str] = None,
    fill_opacity: float = 1.0
) -> str:
    """
    Genera el SVG para un triángulo.
    
    Args:
        pts: Lista de 3 puntos [(x1,y1), (x2,y2), (x3,y3)]
        stroke: Color del borde (usa COLORS['primary'] por defecto)
        fill: Color de relleno
        stroke_width: Grosor del borde
        stroke_colors: Opcional, colores diferentes para cada lado [c1, c2, c3]
        fill_opacity: Opacidad del relleno (0.0 a 1.0)
    
    Returns:
        String SVG del triángulo
    """
    if stroke is None:
        stroke = COLORS.get('primary', '#3b82f6')
    
    if stroke_colors:
        # Cada lado con color diferente
        svg = ""
        # Si hay relleno, dibujamos el path de relleno primero (sin borde)
        if fill != "none":
            path = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} "
            path += f"L {pts[1][0]:.2f} {pts[1][1]:.2f} "
            path += f"L {pts[2][0]:.2f} {pts[2][1]:.2f} Z"
            svg += f'<path d="{path}" fill="{fill}" fill-opacity="{fill_opacity}" stroke="none"/>\n'

        for i in range(3):
            p_start = pts[i]
            p_end = pts[(i+1) % 3]
            color = stroke_colors[i]
            svg += f'<line x1="{p_start[0]:.2f}" y1="{p_start[1]:.2f}" '
            svg += f'x2="{p_end[0]:.2f}" y2="{p_end[1]:.2f}" '
            svg += f'stroke="{color}" stroke-width="{stroke_width+1}" stroke-linecap="round"/>\n'
        return svg
    else:
        path = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} "
        path += f"L {pts[1][0]:.2f} {pts[1][1]:.2f} "
        path += f"L {pts[2][0]:.2f} {pts[2][1]:.2f} Z"
        return f'<path d="{path}" fill="{fill}" fill-opacity="{fill_opacity}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-linejoin="round"/>'


def draw_angle_arc(
    center: Tuple[float, float],
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    marks: int = 1,
    radius: float = 25,
    color: str = None,
    fill_opacity: float = 0.2,
    is_right_angle: bool = False
) -> str:
    """
    Dibuja un arco de ángulo con marcas de congruencia.
    
    Args:
        center: Vértice del ángulo
        p1: Punto en un lado del ángulo
        p2: Punto en el otro lado del ángulo
        marks: Número de arcos (para indicar congruencia)
        radius: Radio del arco en píxeles
        color: Color del arco
        fill_opacity: Opacidad del relleno
        is_right_angle: Si es True, dibuja un cuadrado de ángulo recto
    
    Returns:
        String SVG del arco
    """
    if color is None:
        color = COLORS.get('primary', '#3b82f6')
    
    ang1 = math.atan2(p1[1] - center[1], p1[0] - center[0])
    ang2 = math.atan2(p2[1] - center[1], p2[0] - center[0])
    
    # Normalizar ángulos
    diff = ang2 - ang1
    while diff < 0:
        diff += 2 * math.pi
    while diff > 2 * math.pi:
        diff -= 2 * math.pi
    
    if diff > math.pi:
        ang1, ang2 = ang2, ang1
        diff = 2 * math.pi - diff

    # Dibujar ángulo recto
    if is_right_angle:
        # Calcular vectores unitarios aproximados con el radio
        u1x, u1y = math.cos(ang1), math.sin(ang1)
        u2x, u2y = math.cos(ang2), math.sin(ang2)
        
        # Puntos del cuadrado
        p_leg1 = (center[0] + radius * u1x, center[1] + radius * u1y)
        p_leg2 = (center[0] + radius * u2x, center[1] + radius * u2y)
        # El punto de esquina completa el paralelogramo
        p_corner = (center[0] + radius * (u1x + u2x), center[1] + radius * (u1y + u2y))
        
        path = f"M {center[0]:.2f} {center[1]:.2f} L {p_leg1[0]:.2f} {p_leg1[1]:.2f} "
        path += f"L {p_corner[0]:.2f} {p_corner[1]:.2f} L {p_leg2[0]:.2f} {p_leg2[1]:.2f} Z"
        
        return f'<path d="{path}" fill="{color}" fill-opacity="{fill_opacity}" stroke="{color}" stroke-width="2"/>\n'
    
    # Dibujar arco normal
    sx = center[0] + radius * math.cos(ang1)
    sy = center[1] + radius * math.sin(ang1)
    ex = center[0] + radius * math.cos(ang2)
    ey = center[1] + radius * math.sin(ang2)
    
    # Sector relleno
    sector_path = f"M {center[0]:.2f} {center[1]:.2f} L {sx:.2f} {sy:.2f} "
    sector_path += f"A {radius} {radius} 0 0 1 {ex:.2f} {ey:.2f} Z"
    svg = f'<path d="{sector_path}" fill="{color}" fill-opacity="{fill_opacity}" stroke="none"/>\n'
    
    # Arcos de marca
    gap = 5
    for i in range(marks):
        r = radius - i * gap
        sx_r = center[0] + r * math.cos(ang1)
        sy_r = center[1] + r * math.sin(ang1)
        ex_r = center[0] + r * math.cos(ang2)
        ey_r = center[1] + r * math.sin(ang2)
        svg += f'<path d="M {sx_r:.2f} {sy_r:.2f} A {r} {r} 0 0 1 {ex_r:.2f} {ey_r:.2f}" '
        svg += f'fill="none" stroke="{color}" stroke-width="2"/>\n'
    
    return svg


def draw_tick_marks(
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    count: int = 1,
    color: str = None
) -> str:
    """
    Dibuja marcas de congruencia en un segmento.
    
    Args:
        p1: Punto inicial del segmento
        p2: Punto final del segmento
        count: Número de marcas (1, 2, o 3)
        color: Color de las marcas
    
    Returns:
        String SVG de las marcas
    """
    if color is None:
        color = COLORS.get('text', '#1e293b')
    
    mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    length = math.hypot(dx, dy)
    
    if length < 1e-6:
        return ""
    
    ux, uy = dx / length, dy / length
    nx, ny = -uy, ux
    
    diag_x = ux * 0.5 + nx * 0.8
    diag_y = uy * 0.5 + ny * 0.8
    
    spacing = 6
    start = -((count - 1) * spacing) / 2
    
    svg = ""
    for i in range(count):
        off = start + i * spacing
        cx, cy = mx + ux * off, my + uy * off
        x1, y1 = cx - diag_x * 8, cy - diag_y * 8
        x2, y2 = cx + diag_x * 8, cy + diag_y * 8
        svg += f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
        svg += f'stroke="{color}" stroke-width="2"/>\n'
    
    return svg


def draw_label(
    x: float,
    y: float,
    text: str,
    color: str = None,
    size: int = 18,
    weight: str = "bold",
    font_family: str = "sans-serif"
) -> str:
    """
    Dibuja una etiqueta de texto.
    
    Args:
        x, y: Posición del texto
        text: Contenido
        color: Color del texto
        size: Tamaño de fuente
        weight: Peso (normal, bold)
        font_family: Familia de fuente
    
    Returns:
        String SVG del texto
    """
    if color is None:
        color = COLORS.get('text', '#1e293b')
    
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{font_family}" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="middle" dominant-baseline="middle">{text}</text>')


def draw_comparison_symbol(
    x: float,
    y: float,
    symbol: str = "≅",
    size: int = 45,
    color: str = None
) -> str:
    """
    Dibuja un símbolo de comparación (≅, ≠, ∼, etc.)
    
    Args:
        x, y: Posición
        symbol: Símbolo a mostrar
        size: Tamaño de fuente
        color: Color
    
    Returns:
        String SVG del símbolo
    """
    if color is None:
        color = COLORS.get('text', '#1e293b')
    
    return draw_label(x, y, symbol, color=color, size=size, weight="bold")


def transform_points(
    pts: List[Tuple[float, float]],
    scale: float = 1.0,
    offset: Tuple[float, float] = (0, 0)
) -> List[Tuple[float, float]]:
    """
    Escala y traslada una lista de puntos.
    
    Args:
        pts: Lista de puntos
        scale: Factor de escala
        offset: Traslación (dx, dy)
    
    Returns:
        Lista de puntos transformados
    """
    return [(p[0] * scale + offset[0], p[1] * scale + offset[1]) for p in pts]

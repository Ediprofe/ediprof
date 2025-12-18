"""
🔧 Primitives - Funciones helper compartidas entre renderers

IMPORTANTE: Este es el ÚNICO lugar donde se definen estos helpers.
Evita duplicar estas funciones en los renderers.

Uso:
    from core.primitives import escape_xml, point_on_circle, format_number
    # o
    from core import escape_xml, point_on_circle
"""

import math
from typing import Tuple, Optional


# ============================================================================
# ESCAPE DE TEXTO PARA SVG/XML
# ============================================================================

def escape_xml(text: str) -> str:
    """
    Escapa caracteres especiales para XML/SVG.
    
    ⚠️ CRÍTICO: Los caracteres <, >, & son inválidos en XML y causan errores.
    SIEMPRE usar esta función para texto que contenga símbolos matemáticos.
    
    Ejemplos:
        "d < r"  → "d &lt; r"
        "d > R"  → "d &gt; R"
        "A & B"  → "A &amp; B"
    
    Args:
        text: Texto a escapar
    
    Returns:
        Texto con caracteres especiales escapados
    """
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))


# Alias para compatibilidad
escape_svg_text = escape_xml


# ============================================================================
# GEOMETRÍA CIRCULAR
# ============================================================================

def point_on_circle(cx: float, cy: float, r: float, angle_deg: float) -> Tuple[float, float]:
    """
    Calcula punto en la circunferencia dado ángulo en grados.
    
    Args:
        cx: Coordenada X del centro
        cy: Coordenada Y del centro
        r: Radio
        angle_deg: Ángulo en grados (0° = derecha, crece antihorario)
    
    Returns:
        Tupla (x, y) del punto en la circunferencia
    
    Ejemplo:
        >>> point_on_circle(0, 0, 1, 90)
        (0.0, 1.0)
    """
    angle_rad = math.radians(angle_deg)
    x = cx + r * math.cos(angle_rad)
    y = cy + r * math.sin(angle_rad)
    return (x, y)


def point_on_circle_svg(cx: float, cy: float, r: float, angle_deg: float) -> Tuple[float, float]:
    """
    Calcula punto en circunferencia para coordenadas SVG (Y invertido).
    
    En SVG, Y crece hacia abajo, así que el seno se resta.
    
    Args:
        cx: Coordenada X del centro (SVG)
        cy: Coordenada Y del centro (SVG)
        r: Radio en píxeles
        angle_deg: Ángulo en grados (0° = derecha, crece antihorario visualmente)
    
    Returns:
        Tupla (x, y) en coordenadas SVG
    """
    angle_rad = math.radians(angle_deg)
    x = cx + r * math.cos(angle_rad)
    y = cy - r * math.sin(angle_rad)  # Invertido para SVG
    return (x, y)


def arc_path(cx: float, cy: float, r: float, 
             start_deg: float, end_deg: float,
             svg_coords: bool = True) -> str:
    """
    Genera el path SVG para un arco.
    
    Args:
        cx, cy: Centro
        r: Radio
        start_deg: Ángulo inicial en grados
        end_deg: Ángulo final en grados
        svg_coords: Si True, usa coordenadas SVG (Y invertido)
    
    Returns:
        String del atributo 'd' para un <path>
    """
    if svg_coords:
        x1, y1 = point_on_circle_svg(cx, cy, r, start_deg)
        x2, y2 = point_on_circle_svg(cx, cy, r, end_deg)
    else:
        x1, y1 = point_on_circle(cx, cy, r, start_deg)
        x2, y2 = point_on_circle(cx, cy, r, end_deg)
    
    # Determinar si es arco mayor (> 180°)
    delta = (end_deg - start_deg) % 360
    large_arc = 1 if delta > 180 else 0
    
    # sweep-flag: 0 para antihorario en SVG (porque Y está invertido)
    sweep = 0 if svg_coords else 1
    
    return f"M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 {large_arc} {sweep} {x2:.2f} {y2:.2f}"


# ============================================================================
# FORMATEO DE NÚMEROS
# ============================================================================

def format_number(n: float, decimals: int = 2) -> str:
    """
    Formatea un número para mostrar, eliminando decimales innecesarios.
    
    Args:
        n: Número a formatear
        decimals: Máximo de decimales
    
    Returns:
        String formateado
    
    Ejemplos:
        >>> format_number(3.0)
        '3'
        >>> format_number(3.14159, 2)
        '3.14'
        >>> format_number(3.10, 2)
        '3.1'
    """
    if n == int(n):
        return str(int(n))
    return f'{n:.{decimals}f}'.rstrip('0').rstrip('.')


def format_coord(x: float, y: float) -> str:
    """
    Formatea un par de coordenadas para etiquetas.
    
    Args:
        x, y: Coordenadas
    
    Returns:
        String como "(x, y)"
    
    Ejemplo:
        >>> format_coord(3.0, 4.5)
        '(3, 4.5)'
    """
    return f"({format_number(x)}, {format_number(y)})"


def format_angle(degrees: float) -> str:
    """
    Formatea un ángulo en grados para mostrar.
    
    Args:
        degrees: Ángulo en grados
    
    Returns:
        String con símbolo de grados
    
    Ejemplo:
        >>> format_angle(45.0)
        '45°'
    """
    return f"{format_number(degrees)}°"


# ============================================================================
# GEOMETRÍA GENERAL
# ============================================================================

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calcula la distancia entre dos puntos.
    
    Args:
        x1, y1: Primer punto
        x2, y2: Segundo punto
    
    Returns:
        Distancia euclidiana
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def midpoint(x1: float, y1: float, x2: float, y2: float) -> Tuple[float, float]:
    """
    Calcula el punto medio entre dos puntos.
    
    Args:
        x1, y1: Primer punto
        x2, y2: Segundo punto
    
    Returns:
        Tupla (x, y) del punto medio
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def lerp(a: float, b: float, t: float) -> float:
    """
    Interpolación lineal entre dos valores.
    
    Args:
        a: Valor inicial
        b: Valor final
        t: Factor de interpolación (0 = a, 1 = b)
    
    Returns:
        Valor interpolado
    """
    return a + (b - a) * t


def clamp(value: float, min_val: float, max_val: float) -> float:
    """
    Limita un valor a un rango.
    
    Args:
        value: Valor a limitar
        min_val: Mínimo
        max_val: Máximo
    
    Returns:
        Valor limitado al rango [min_val, max_val]
    """
    return max(min_val, min(max_val, value))


# ============================================================================
# UTILIDADES SVG
# ============================================================================

def svg_translate(x: float, y: float) -> str:
    """Genera atributo transform para traslación."""
    return f'translate({x:.2f}, {y:.2f})'


def svg_rotate(angle_deg: float, cx: float = 0, cy: float = 0) -> str:
    """Genera atributo transform para rotación."""
    if cx == 0 and cy == 0:
        return f'rotate({angle_deg:.2f})'
    return f'rotate({angle_deg:.2f}, {cx:.2f}, {cy:.2f})'


def svg_scale(sx: float, sy: Optional[float] = None) -> str:
    """Genera atributo transform para escala."""
    if sy is None:
        return f'scale({sx:.2f})'
    return f'scale({sx:.2f}, {sy:.2f})'

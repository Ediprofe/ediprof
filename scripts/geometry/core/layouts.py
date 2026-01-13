"""
📐 Layouts - Cálculos de posicionamiento para ilustraciones

Proporciona funciones para calcular offsets y centrar figuras en el canvas.

Uso:
    from core.layouts import side_by_side, centered_single
"""

from typing import Tuple, Dict
from .canvas import get_canvas_config


def side_by_side(
    canvas_size: str,
    figure_width: float,
    figure_height: float,
    gap: float = 80
) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """
    Calcula offsets para posicionar dos figuras lado a lado, centradas.
    
    Args:
        canvas_size: Tamaño del canvas ('simple', 'compound', 'horizontal', etc.)
        figure_width: Ancho de cada figura
        figure_height: Alto de cada figura
        gap: Espacio entre las figuras
    
    Returns:
        Tupla de dos offsets: ((x1, y1), (x2, y2))
        Donde y es la posición de la BASE de la figura.
    
    Ejemplo:
        off1, off2 = side_by_side('horizontal', 120, 100, gap=80)
        # Usar off1 para la primera figura, off2 para la segunda
    """
    config = get_canvas_config(canvas_size)
    width = config['width']
    height = config['height']
    
    # Horizontal: Centrar el conjunto de las dos figuras
    total_w = figure_width * 2 + gap
    start_x = (width - total_w) / 2
    
    # Vertical: Centrar en el área disponible (dejando espacio para título)
    title_space = 50  # Espacio reservado para título inferior
    available_height = height - title_space
    center_y = available_height / 2
    base_y = center_y + figure_height / 2
    
    off1 = (start_x, base_y)
    off2 = (start_x + figure_width + gap, base_y)
    
    return off1, off2


def side_by_side_asymmetric(
    canvas_size: str,
    width1: float,
    height1: float,
    width2: float,
    height2: float,
    gap: float = 80
) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """
    Calcula offsets para dos figuras de diferente tamaño lado a lado.
    
    Args:
        canvas_size: Tamaño del canvas
        width1, height1: Dimensiones de la primera figura
        width2, height2: Dimensiones de la segunda figura
        gap: Espacio entre las figuras
    
    Returns:
        Tupla de dos offsets
    """
    config = get_canvas_config(canvas_size)
    width = config['width']
    height = config['height']
    
    total_w = width1 + gap + width2
    start_x = (width - total_w) / 2
    
    title_space = 50
    available_height = height - title_space
    center_y = available_height / 2
    
    # Alinear por la base (la más alta determina la posición vertical)
    max_height = max(height1, height2)
    base_y = center_y + max_height / 2
    
    off1 = (start_x, base_y)
    off2 = (start_x + width1 + gap, base_y)
    
    return off1, off2


def centered_single(
    canvas_size: str,
    figure_width: float,
    figure_height: float
) -> Tuple[float, float]:
    """
    Calcula offset para centrar una sola figura.
    
    Args:
        canvas_size: Tamaño del canvas
        figure_width: Ancho de la figura
        figure_height: Alto de la figura
    
    Returns:
        Offset (x, y) donde y es la posición de la BASE
    """
    config = get_canvas_config(canvas_size)
    width = config['width']
    height = config['height']
    
    x = (width - figure_width) / 2
    
    title_space = 50
    available_height = height - title_space
    center_y = available_height / 2
    base_y = center_y + figure_height / 2
    
    return (x, base_y)


def get_title_position(canvas_size: str) -> Tuple[float, float]:
    """
    Obtiene la posición para el título inferior.
    
    Args:
        canvas_size: Tamaño del canvas
    
    Returns:
        Posición (x, y) para el título
    """
    config = get_canvas_config(canvas_size)
    x = config['width'] / 2
    y = config['height'] - 25
    return (x, y)


def get_symbol_position(
    off1: Tuple[float, float],
    off2: Tuple[float, float],
    figure_width: float,
    canvas_size: str
) -> Tuple[float, float]:
    """
    Calcula la posición para un símbolo entre dos figuras.
    
    Args:
        off1: Offset de la primera figura
        off2: Offset de la segunda figura
        figure_width: Ancho de cada figura
        canvas_size: Tamaño del canvas
    
    Returns:
        Posición (x, y) para el símbolo
    """
    config = get_canvas_config(canvas_size)
    title_space = 50
    available_height = config['height'] - title_space
    
    x = (off1[0] + figure_width + off2[0]) / 2
    y = available_height / 2
    
    return (x, y)

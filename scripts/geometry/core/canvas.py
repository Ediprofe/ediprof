"""
📐 Canvas - Tamaños estándar de canvas para ilustraciones

IMPORTANTE: Este es el ÚNICO lugar donde se definen tamaños.
Todos los renderers deben importar de aquí.

Uso:
    from core.canvas import CANVAS_SIZES, get_canvas_config
    # o
    from core import CANVAS_SIZES
"""

from enum import Enum
from typing import Dict, Tuple


# ============================================================================
# TAMAÑOS ESTÁNDAR (como tuplas simples)
# ============================================================================

# Formato: (width, height)
SIZE_SIMPLE = (500, 400)       # 1 concepto: radio, diámetro, cuerda, arco, ángulo
SIZE_COMPOUND = (600, 460)     # 2-3 elementos: sector+triángulo, teoremas
SIZE_MULTIPLE = (750, 450)     # 4+ elementos: posiciones, comparaciones
SIZE_HORIZONTAL = (750, 420)   # Operaciones A - B = C, lado a lado
SIZE_CARTESIAN = (600, 500)    # Plano cartesiano estándar
SIZE_SQUARE = (600, 600)       # Canvas cuadrado (escala uniforme)


# ============================================================================
# ENUM PARA TIPOS DE CANVAS
# ============================================================================

class CanvasSize(Enum):
    """Tamaños estándar de canvas."""
    SIMPLE = "simple"           # 500x400 - 1 concepto
    COMPOUND = "compound"       # 600x460 - 2-3 elementos
    MULTIPLE = "multiple"       # 750x450 - 4+ elementos
    HORIZONTAL = "horizontal"   # 750x420 - Operaciones lado a lado
    CARTESIAN = "cartesian"     # 600x500 - Plano cartesiano
    SQUARE = "square"           # 600x600 - Escala uniforme


# ============================================================================
# CONFIGURACIONES COMPLETAS
# ============================================================================

CANVAS_CONFIGS: Dict[str, Dict] = {
    CanvasSize.SIMPLE.value: {
        'width': 500,
        'height': 400,
        'padding': 40
    },
    CanvasSize.COMPOUND.value: {
        'width': 600,
        'height': 460,
        'padding': 40
    },
    CanvasSize.MULTIPLE.value: {
        'width': 750,
        'height': 450,
        'padding': 40
    },
    CanvasSize.HORIZONTAL.value: {
        'width': 750,
        'height': 420,
        'padding': 40
    },
    CanvasSize.CARTESIAN.value: {
        'width': 600,
        'height': 500,
        'padding': 50
    },
    CanvasSize.SQUARE.value: {
        'width': 600,
        'height': 600,
        'padding': 50
    }
}


def get_canvas_config(size: str) -> Dict:
    """
    Obtiene la configuración de canvas por nombre.
    
    Args:
        size: Nombre del tamaño ('simple', 'compound', etc.)
    
    Returns:
        Dict con 'width', 'height', 'padding'
    
    Raises:
        ValueError si el tamaño no existe
    """
    if size not in CANVAS_CONFIGS:
        valid = ', '.join(CANVAS_CONFIGS.keys())
        raise ValueError(f"Tamaño '{size}' no válido. Opciones: {valid}")
    return CANVAS_CONFIGS[size]


def get_canvas_dimensions(size: str) -> Tuple[int, int]:
    """
    Obtiene solo width y height.
    
    Args:
        size: Nombre del tamaño
    
    Returns:
        Tupla (width, height)
    """
    config = get_canvas_config(size)
    return (config['width'], config['height'])

"""
📐 Cartesian - Módulo para Geometría Analítica

Organizado por tema:
- points.py: Plano básico, distancia, punto medio, división, áreas
- slopes.py: Pendientes, inclinación, paralelas/perpendiculares
- lines.py: Ecuaciones de rectas
- circles.py: Circunferencias en el plano cartesiano
- parabolas.py: Parábolas

Uso:
    from cartesian import render_plano_basico, render_distancia
    from cartesian import render_tipos_pendiente
    from cartesian import render_ecuacion_general
    from cartesian import render_elementos_circunferencia
    from cartesian import render_elementos_parabola
"""

# Puntos y segmentos
from .points import (
    render_plano_basico,
    render_distancia,
    render_punto_medio,
    render_division_segmento,
    render_area_triangulo,
)

# Pendientes e inclinación
from .slopes import (
    render_tipos_pendiente,
    render_concepto_pendiente,
    render_calculo_pendiente,
    render_angulo_inclinacion,
    render_paralelas_perpendiculares,
)

# Ecuaciones de rectas
from .lines import (
    render_ecuacion_general,
    render_punto_pendiente,
    render_pendiente_ordenada,
    render_recta_dos_puntos,
    render_forma_simetrica,
    render_forma_normal,
    render_distancia_punto_recta,
    render_familias_rectas,
)

# Circunferencias
from .circles import (
    render_elementos_circunferencia,
    render_ecuacion_ordinaria_circ,
    render_posiciones_recta_circ,
    render_posiciones_dos_circ,
    render_circunferencias_concentricas,
    render_tangente_circunferencia,
)

# Parábolas
from .parabolas import (
    render_elementos_parabola,
    render_parabola_vertical_arriba,
    render_parabola_vertical_abajo,
    render_parabola_horizontal_derecha,
    render_parabola_horizontal_izquierda,
    render_cuatro_orientaciones_parabola,
)

__all__ = [
    # Puntos
    'render_plano_basico',
    'render_distancia',
    'render_punto_medio',
    'render_division_segmento',
    'render_area_triangulo',
    # Pendientes
    'render_tipos_pendiente',
    'render_concepto_pendiente',
    'render_calculo_pendiente',
    'render_angulo_inclinacion',
    'render_paralelas_perpendiculares',
    # Rectas
    'render_ecuacion_general',
    'render_punto_pendiente',
    'render_pendiente_ordenada',
    'render_recta_dos_puntos',
    'render_forma_simetrica',
    'render_forma_normal',
    'render_distancia_punto_recta',
    'render_familias_rectas',
    # Circunferencias
    'render_elementos_circunferencia',
    'render_ecuacion_ordinaria_circ',
    'render_posiciones_recta_circ',
    'render_posiciones_dos_circ',
    'render_circunferencias_concentricas',
    'render_tangente_circunferencia',
    # Parábolas
    'render_elementos_parabola',
    'render_parabola_vertical_arriba',
    'render_parabola_vertical_abajo',
    'render_parabola_horizontal_derecha',
    'render_parabola_horizontal_izquierda',
    'render_cuatro_orientaciones_parabola',
]

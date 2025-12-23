#!/usr/bin/env python3
"""
🎡 MCU Renderer - Renderizador de ilustraciones para Movimiento Circular Uniforme

Genera SVGs para:
1. ¿Qué es el MCU? (Definiciones básicas)
2. Aceleración Centrípeta

Uso:
    python scripts/physics/mcu_renderer.py
"""

import sys
import math
from pathlib import Path

# Agregar directorio raíz al path para importar core
sys.path.insert(0, str(Path(__file__).parents[2] / 'scripts' / 'geometry'))

from core import COLORS, Point, SVGBuilder, SIZE_COMPOUND, SIZE_SIMPLE

OUTPUT_DIR = Path('public/images/fisica/cinematica/mcu')

def render_que_es_mcu():
    """Genera ilustración: ¿Qué es el MCU?"""
    width, height = SIZE_COMPOUND # 600x460
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    builder.text("Movimiento Circular Uniforme", Point(width/2, 30), 
                 font_size=20, font_weight='bold', fill=COLORS['text'])
    
    # Configuración del círculo
    cx, cy = 200, 240
    r = 120
    center = Point(cx, cy)
    
    # Círculo trayectoria
    builder.circle(center, r, stroke=COLORS['primary'], stroke_width=2, fill='none')
    
    # Centro
    builder.point(center, radius=4, fill=COLORS['text'])
    builder.text("O", Point(cx - 10, cy + 5), font_size=12, fill=COLORS['text_light'])
    
    # Objeto en ángulo -30 grados (330 grados)
    angle_deg = -30
    angle_rad = math.radians(angle_deg)
    px = cx + r * math.cos(angle_rad)
    py = cy + r * math.sin(angle_rad)
    obj_pos = Point(px, py)
    
    # Radio
    builder.line(center, obj_pos, stroke=COLORS['amber'], stroke_width=2)
    builder.text("r", Point(cx + r/2, cy - 10), font_size=14, fill=COLORS['amber'], font_weight='bold')
    
    # Objeto
    builder.point(obj_pos, radius=10, fill=COLORS['accent'])
    
    # Vector Velocidad (Tangente)
    # Perpendicular al radio. Si radio es ángulo A, tangente es A - 90 (para ir horario) o A + 90
    # En SVG Y crece abajo. 
    # Vector r: (cos(a), sin(a))
    # Vector v: (sin(a), -cos(a)) para sentido antihorario?
    # Vamos a calcularlo visualmente. Tangente en -30 grados apunta hacia "arriba y derecha"
    vx = 60 * math.sin(angle_rad) * -1 # hacia arriba es Y negativo? no, espera.
    # Tangente a círculo: (-y, x) o (y, -x).
    # Radio vector normalizado: (cos, sin)
    # Tangente (+90 deg): (-sin, cos). 
    # Tangente (-90 deg): (sin, -cos).
    
    # Usemos lógica simple: en 0 grados (derecha), velocidad va arriba (0, -1).
    # En 90 grados (abajo en SVG), velocidad va izquierda (-1, 0).
    # Rotación horaria visual (SVG): 0 -> 90.
    # Si objeto gira antihorario (lo normal en física):
    # En 0 (derecha), v va arriba (negativo Y).
    
    v_len = 70
    # Antihorario:
    vx = -v_len * math.sin(angle_rad)
    vy = v_len * math.cos(angle_rad)
    
    v_end = Point(px + vx, py + vy)
    builder.arrow(obj_pos, v_end, stroke=COLORS['secondary'], stroke_width=3)
    builder.text("v", Point(v_end.x + 10, v_end.y), font_size=16, fill=COLORS['secondary'], font_weight='bold')
    
    # Ángulo theta
    builder.path(f"M {cx+40} {cy} A 40 40 0 0 0 {cx + 40*math.cos(angle_rad):.2f} {cy + 40*math.sin(angle_rad):.2f}", 
                 stroke=COLORS['purple'], stroke_width=2)
    builder.text("θ", Point(cx + 50, cy - 15), font_size=14, fill=COLORS['purple'])
    
    # Línea referencia horizontal
    builder.line(center, Point(cx + r + 20, cy), stroke=COLORS['auxiliary'], stroke_width=1, dashed=True)
    
    # Panel lateral de definiciones
    panel_x = 380
    panel_y = 80
    line_h = 35
    
    builder.text("Definiciones:", Point(panel_x, panel_y), font_size=14, font_weight='bold', anchor="start")
    
    defs = [
        ("T (Período)", "Tiempo de 1 vuelta", COLORS['primary']),
        ("f (Frecuencia)", "Vueltas por segundo", COLORS['amber']),
        ("ω (Vel. Angular)", "Ángulo por segundo", COLORS['purple']),
        ("v (Vel. Tangencial)", "Distancia / tiempo", COLORS['secondary']),
        ("ac (Acel. Centrípeta)", "Hacia el centro", COLORS['accent'])
    ]
    
    for i, (term, desc, color) in enumerate(defs):
        y = panel_y + 35 + i * line_h
        builder.text(term, Point(panel_x, y), font_size=13, fill=color, font_weight='bold', anchor="start")
        builder.text(desc, Point(panel_x, y + 15), font_size=11, fill=COLORS['text_light'], anchor="start")

    # Guardar
    output_path = OUTPUT_DIR / "que-es-el-mcu.svg"
    builder.save(output_path)
    print(f"✅ Generado: {output_path}")


def render_aceleracion_centripeta():
    """Genera ilustración: Aceleración Centrípeta"""
    width, height = SIZE_SIMPLE # 500x400
    builder = SVGBuilder(width, height)
    
    # Fondo
    builder.rect(0, 0, width, height, fill=COLORS['background'])
    
    # Título
    builder.text("Aceleración Centrípeta", Point(width/2, 30), 
                 font_size=20, font_weight='bold', fill=COLORS['text'])
    
    cx, cy = 250, 220
    r = 130
    center = Point(cx, cy)
    
    # Círculo
    builder.circle(center, r, stroke=COLORS['primary'], stroke_width=2, fill='none')
    builder.point(center, radius=4, fill=COLORS['text'])
    
    # Mostrar objeto en 2 posiciones para ver el cambio de dirección
    angles = [-40, 40]
    
    for i, angle_deg in enumerate(angles):
        angle_rad = math.radians(angle_deg)
        px = cx + r * math.cos(angle_rad)
        py = cy + r * math.sin(angle_rad)
        pos = Point(px, py)
        
        # Objeto
        builder.point(pos, radius=10, fill=COLORS['primary'])
        
        # Velocidad (Tangente)
        v_len = 60
        # Antihorario: (sin, -cos)
        vx = v_len * math.sin(angle_rad)
        vy = -v_len * math.cos(angle_rad)
        v_end = Point(px + vx, py + vy)
        
        builder.arrow(pos, v_end, stroke=COLORS['secondary'], stroke_width=3)
        
        # Etiqueta velocidad
        v_label_pos = Point(v_end.x + (10 if i==1 else -10), v_end.y + (-5 if i==0 else -5))
        builder.text("v", v_label_pos, font_size=16, fill=COLORS['secondary'], font_weight='bold')
        
        # Aceleración (Hacia el centro)
        ac_len = 50
        # Vector unitario hacia el centro es (-cos, -sin)
        ax = -ac_len * math.cos(angle_rad)
        ay = -ac_len * math.sin(angle_rad)
        ac_end = Point(px + ax, py + ay)
        
        builder.arrow(pos, ac_end, stroke=COLORS['accent'], stroke_width=3)
        
        # Etiqueta aceleración
        ac_label_pos = Point(ac_end.x + (10 if i==0 else -10), ac_end.y + 15)
        builder.text("ac", ac_label_pos, font_size=16, fill=COLORS['accent'], font_weight='bold')

    # Texto explicativo
    builder.text("La velocidad cambia de dirección", Point(width/2, 360), 
                 font_size=14, fill=COLORS['text'], font_weight='bold')
    builder.text("La aceleración apunta siempre al centro", Point(width/2, 380), 
                 font_size=14, fill=COLORS['text_light'])

    # Guardar
    output_path = OUTPUT_DIR / "aceleracion-centripeta.svg"
    builder.save(output_path)
    print(f"✅ Generado: {output_path}")

if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    render_que_es_mcu()
    render_aceleracion_centripeta()

#!/usr/bin/env python3
"""
GraphSpec Renderer - Genera SVGs animados de gráficas matemáticas
Soporta: funciones, histogramas, barras, pie charts, scatter plots

Uso: python renderer.py --spec archivo.json --output archivo.svg [--preview]
"""

import json
import math
import argparse
import webbrowser
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

# Constantes matemáticas
PI = math.pi

# Paleta de colores estándar
COLORS = {
    'primary': '#3b82f6',      # Azul
    'secondary': '#ef4444',    # Rojo
    'tertiary': '#22c55e',     # Verde
    'quaternary': '#8b5cf6',   # Violeta
    'quinary': '#f97316',      # Naranja
    'axis': '#374151',         # Gris oscuro - ejes
    'grid': '#e2e8f0',         # Gris claro - cuadrícula
    'background': '#f8fafc',   # Fondo
    'text': '#1e293b',         # Texto
    'muted': '#94a3b8',        # Gris - elementos secundarios
}

# Paleta para múltiples series
COLOR_PALETTE = [
    '#3b82f6',  # Azul
    '#ef4444',  # Rojo
    '#22c55e',  # Verde
    '#f97316',  # Naranja
    '#8b5cf6',  # Violeta
    '#ec4899',  # Rosa
    '#14b8a6',  # Teal
    '#f59e0b',  # Ámbar
]


def parse_math_expr(expr: str) -> float:
    """Convierte expresiones matemáticas simples a valores numéricos."""
    if isinstance(expr, (int, float)):
        return float(expr)
    
    expr = str(expr).strip()
    expr = expr.replace('pi', str(PI))
    expr = expr.replace('π', str(PI))
    
    try:
        allowed = {'__builtins__': None}
        return float(eval(expr, allowed, {}))
    except:
        return float(expr)


def safe_cot(x: float) -> float:
    """Cotangente segura (cos(x)/sin(x))."""
    s = math.sin(x)
    if abs(s) < 1e-10:
        return float('inf')
    return math.cos(x) / s

def safe_sec(x: float) -> float:
    """Secante segura (1/cos(x))."""
    c = math.cos(x)
    if abs(c) < 1e-10:
        return float('inf')
    return 1.0 / c

def safe_csc(x: float) -> float:
    """Cosecante segura (1/sin(x))."""
    s = math.sin(x)
    if abs(s) < 1e-10:
        return float('inf')
    return 1.0 / s

def evaluate_function(expression: str, x: float) -> Optional[float]:
    """Evalúa una función matemática en un punto x."""
    expr = expression.lower().replace('^', '**')
    
    context = {
        'x': x,
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'cot': safe_cot, 'sec': safe_sec, 'csc': safe_csc,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'arcsin': math.asin, 'arccos': math.acos, 'arctan': math.atan,
        'sqrt': math.sqrt, 'abs': abs, 'log': math.log,
        'exp': math.exp, 'pi': PI, 'e': math.e,
    }
    
    try:
        result = eval(expr, {'__builtins__': None}, context)
        if math.isnan(result) or math.isinf(result):
            return None
        return result
    except:
        return None


def generate_function_points(expression: str, x_min: float, x_max: float, 
                             num_points: int = 200) -> List[Tuple[float, float]]:
    """Genera puntos de una función en un rango dado."""
    points = []
    step = (x_max - x_min) / num_points
    
    for i in range(num_points + 1):
        x = x_min + i * step
        y = evaluate_function(expression, x)
        if y is not None:
            points.append((x, y))
    
    return points


def map_to_canvas(x: float, y: float, 
                  x_min: float, x_max: float, 
                  y_min: float, y_max: float,
                  canvas_width: float, canvas_height: float,
                  padding: float) -> Tuple[float, float]:
    """Convierte coordenadas matemáticas a coordenadas de canvas SVG."""
    plot_width = canvas_width - 2 * padding
    plot_height = canvas_height - 2 * padding
    
    canvas_x = padding + (x - x_min) / (x_max - x_min) * plot_width
    canvas_y = padding + (y_max - y) / (y_max - y_min) * plot_height
    
    return (canvas_x, canvas_y)


def format_pi_label(value: float) -> str:
    """Formatea un valor como múltiplo de π."""
    tol = 0.01
    
    if abs(value) < tol:
        return "0"
    
    multiples = [
        (2, "2π"), (1.5, "3π/2"), (1, "π"), (0.5, "π/2"),
        (-0.5, "-π/2"), (-1, "-π"), (-1.5, "-3π/2"), (-2, "-2π"),
        (0.25, "π/4"), (-0.25, "-π/4"), (0.75, "3π/4"), (-0.75, "-3π/4"),
    ]
    
    for mult, label in multiples:
        if abs(value - mult * PI) < tol:
            return label
    
    return ""


# ============================================================================
# GENERADORES POR TIPO DE GRÁFICO
# ============================================================================

def generate_function_svg(spec: Dict[str, Any]) -> str:
    """Genera SVG para gráficas de funciones (sin, cos, lineales, etc.)."""
    
    canvas = spec.get('canvas', {})
    width = canvas.get('width', 800)
    height = canvas.get('height', 400)
    padding = canvas.get('padding', 50)
    bg_color = canvas.get('background', COLORS['background'])
    
    axes = spec.get('axes', {})
    x_axis = axes.get('x', {})
    y_axis = axes.get('y', {})
    
    x_min = parse_math_expr(x_axis.get('min', -2 * PI))
    x_max = parse_math_expr(x_axis.get('max', 2 * PI))
    y_min = parse_math_expr(y_axis.get('min', -1.5))
    y_max = parse_math_expr(y_axis.get('max', 1.5))
    
    functions = spec.get('functions', [])
    markers = spec.get('markers', [])
    annotations = spec.get('annotations', [])
    animations = spec.get('animations', {})
    title = spec.get('metadata', {}).get('title', '')
    
    anim_enabled = animations.get('enabled', True)
    anim_duration = animations.get('duration', 2)
    markers_delay = animations.get('markersDelay', anim_duration)
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="max-width: 100%; height: auto; font-family: Inter, system-ui, sans-serif;">',
    ]
    
    # Estilos CSS
    svg_parts.append(f'''
  <style>
    .wave-path {{
      stroke-dasharray: 3000;
      stroke-dashoffset: {3000 if anim_enabled else 0};
      animation: {f'drawWave {anim_duration}s ease-out forwards' if anim_enabled else 'none'};
    }}
    .marker-group {{ opacity: {0 if anim_enabled else 1}; animation: {f'fadeIn 0.5s ease-out {markers_delay}s forwards' if anim_enabled else 'none'}; }}
    .label-group {{ opacity: {0 if anim_enabled else 1}; animation: {f'fadeIn 0.5s ease-out {markers_delay + 0.3}s forwards' if anim_enabled else 'none'}; }}
    .annotation-group {{ opacity: {0 if anim_enabled else 1}; animation: {f'fadeIn 0.5s ease-out {markers_delay + 0.5}s forwards' if anim_enabled else 'none'}; }}
    @keyframes drawWave {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes fadeIn {{ to {{ opacity: 1; }} }}
  </style>
''')
    
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="{bg_color}" rx="8"/>')
    
    if title:
        svg_parts.append(f'  <text x="{width/2}" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">{title}</text>')
    
    plot_x, plot_y = padding, padding
    plot_width = width - 2 * padding
    plot_height = height - 2 * padding
    
    # Cuadrícula
    svg_parts.append('  <g class="grid">')
    ticks_style = x_axis.get('ticks', 'pi')
    
    if ticks_style == 'pi':
        for mult in range(-4, 5):
            x_val = mult * PI / 2
            if x_min <= x_val <= x_max:
                cx, _ = map_to_canvas(x_val, 0, x_min, x_max, y_min, y_max, width, height, padding)
                svg_parts.append(f'    <line x1="{cx:.1f}" y1="{plot_y}" x2="{cx:.1f}" y2="{plot_y + plot_height}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
    else:
        # Cuadrícula numérica
        x_range = x_max - x_min
        step = 1 if x_range <= 10 else (5 if x_range <= 50 else 10)
        x_val = math.ceil(x_min / step) * step
        while x_val <= x_max:
            cx, _ = map_to_canvas(x_val, 0, x_min, x_max, y_min, y_max, width, height, padding)
            svg_parts.append(f'    <line x1="{cx:.1f}" y1="{plot_y}" x2="{cx:.1f}" y2="{plot_y + plot_height}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
            x_val += step
    
    for y_val in [-1, -0.5, 0.5, 1]:
        if y_min <= y_val <= y_max:
            _, cy = map_to_canvas(0, y_val, x_min, x_max, y_min, y_max, width, height, padding)
            svg_parts.append(f'    <line x1="{plot_x}" y1="{cy:.1f}" x2="{plot_x + plot_width}" y2="{cy:.1f}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
    svg_parts.append('  </g>')
    
    # Ejes
    origin_x, origin_y = map_to_canvas(0, 0, x_min, x_max, y_min, y_max, width, height, padding)
    
    svg_parts.append('  <g class="axes">')
    svg_parts.append(f'    <line x1="{plot_x}" y1="{origin_y:.1f}" x2="{plot_x + plot_width}" y2="{origin_y:.1f}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    svg_parts.append(f'    <polygon points="{plot_x + plot_width},{origin_y:.1f} {plot_x + plot_width - 8},{origin_y - 4:.1f} {plot_x + plot_width - 8},{origin_y + 4:.1f}" fill="{COLORS["axis"]}"/>')
    svg_parts.append(f'    <line x1="{origin_x:.1f}" y1="{plot_y}" x2="{origin_x:.1f}" y2="{plot_y + plot_height}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    svg_parts.append(f'    <polygon points="{origin_x:.1f},{plot_y} {origin_x - 4:.1f},{plot_y + 8} {origin_x + 4:.1f},{plot_y + 8}" fill="{COLORS["axis"]}"/>')
    
    x_label = x_axis.get('label', 'x')
    y_label = y_axis.get('label', 'y')
    svg_parts.append(f'    <text x="{plot_x + plot_width + 10}" y="{origin_y + 5:.1f}" font-size="14" font-weight="bold" fill="{COLORS["axis"]}">{x_label}</text>')
    svg_parts.append(f'    <text x="{origin_x + 8:.1f}" y="{plot_y - 5}" font-size="14" font-weight="bold" fill="{COLORS["axis"]}">{y_label}</text>')
    
    # Ticks
    if ticks_style == 'pi':
        for mult in range(-4, 5):
            x_val = mult * PI / 2
            if x_min < x_val < x_max and abs(x_val) > 0.1:
                cx, _ = map_to_canvas(x_val, 0, x_min, x_max, y_min, y_max, width, height, padding)
                label = format_pi_label(x_val)
                if label:
                    svg_parts.append(f'    <line x1="{cx:.1f}" y1="{origin_y - 4:.1f}" x2="{cx:.1f}" y2="{origin_y + 4:.1f}" stroke="{COLORS["axis"]}" stroke-width="1.5"/>')
                    svg_parts.append(f'    <text x="{cx:.1f}" y="{origin_y + 20:.1f}" text-anchor="middle" font-size="12" fill="{COLORS["axis"]}">{label}</text>')
    else:
        x_range = x_max - x_min
        step = 1 if x_range <= 10 else (5 if x_range <= 50 else 10)
        x_val = math.ceil(x_min / step) * step
        while x_val <= x_max:
            if abs(x_val) > 0.01:
                cx, _ = map_to_canvas(x_val, 0, x_min, x_max, y_min, y_max, width, height, padding)
                svg_parts.append(f'    <line x1="{cx:.1f}" y1="{origin_y - 4:.1f}" x2="{cx:.1f}" y2="{origin_y + 4:.1f}" stroke="{COLORS["axis"]}" stroke-width="1.5"/>')
                svg_parts.append(f'    <text x="{cx:.1f}" y="{origin_y + 20:.1f}" text-anchor="middle" font-size="12" fill="{COLORS["axis"]}">{int(x_val) if x_val == int(x_val) else x_val}</text>')
            x_val += step
    
    for y_val in [-1, 1]:
        if y_min < y_val < y_max:
            _, cy = map_to_canvas(0, y_val, x_min, x_max, y_min, y_max, width, height, padding)
            svg_parts.append(f'    <line x1="{origin_x - 4:.1f}" y1="{cy:.1f}" x2="{origin_x + 4:.1f}" y2="{cy:.1f}" stroke="{COLORS["axis"]}" stroke-width="1.5"/>')
            svg_parts.append(f'    <text x="{origin_x - 12:.1f}" y="{cy + 4:.1f}" text-anchor="end" font-size="12" fill="{COLORS["axis"]}">{y_val}</text>')
    svg_parts.append('  </g>')
    
    # Funciones
    for i, func in enumerate(functions):
        expr = func.get('expression', 'sin(x)')
        color = func.get('color', COLOR_PALETTE[i % len(COLOR_PALETTE)])
        stroke_width = func.get('strokeWidth', 3)
        func_id = func.get('id', f'func-{i}')
        
        points = generate_function_points(expr, x_min, x_max)
        
        if points:
            path_parts = []
            first = True
            
            for x, y in points:
                cx, cy = map_to_canvas(x, y, x_min, x_max, y_min, y_max, width, height, padding)
                if plot_y <= cy <= plot_y + plot_height:
                    path_parts.append(f'{"M" if first else "L"} {cx:.2f} {cy:.2f}')
                    first = False
                else:
                    first = True
            
            path_d = ' '.join(path_parts)
            svg_parts.append(f'  <path id="{func_id}" class="wave-path" d="{path_d}" fill="none" stroke="{color}" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"/>')
    
    # Marcadores
    if markers:
        svg_parts.append('  <g class="marker-group">')
        for marker in markers:
            mx = parse_math_expr(marker.get('x', 0))
            my_raw = marker.get('y')
            my = parse_math_expr(my_raw) if my_raw is not None else None
            if my is None and functions:
                my = evaluate_function(functions[0].get('expression', 'sin(x)'), mx)
            if my is not None:
                cx, cy = map_to_canvas(mx, my, x_min, x_max, y_min, y_max, width, height, padding)
                color = marker.get('color', COLORS['secondary'])
                svg_parts.append(f'    <circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{color}" stroke="white" stroke-width="2"/>')
        svg_parts.append('  </g>')
        
        svg_parts.append('  <g class="label-group">')
        for marker in markers:
            mx = parse_math_expr(marker.get('x', 0))
            my_raw = marker.get('y')
            my = parse_math_expr(my_raw) if my_raw is not None else None
            label = marker.get('label', '')
            if my is None and functions:
                my = evaluate_function(functions[0].get('expression', 'sin(x)'), mx)
            if my is not None and label:
                cx, cy = map_to_canvas(mx, my, x_min, x_max, y_min, y_max, width, height, padding)
                color = marker.get('color', COLORS['secondary'])
                pos = marker.get('labelPosition', 'top')
                label_x, label_y, anchor = cx, cy - 15 if pos == 'top' else cy + 25, 'middle'
                if pos == 'left': label_x, label_y, anchor = cx - 15, cy + 4, 'end'
                elif pos == 'right': label_x, label_y, anchor = cx + 15, cy + 4, 'start'
                svg_parts.append(f'    <rect x="{label_x - 50}" y="{label_y - 12}" width="100" height="16" fill="white" fill-opacity="0.9" rx="3"/>')
                svg_parts.append(f'    <text x="{label_x:.1f}" y="{label_y:.1f}" text-anchor="{anchor}" font-size="11" font-weight="bold" fill="{color}">{label}</text>')
        svg_parts.append('  </g>')
    
    # Leyenda (si hay funciones con label)
    functions_with_labels = [f for f in functions if f.get('label')]
    if functions_with_labels:
        legend_x = width - padding - 10
        legend_y = padding + 10
        legend_width = 180
        legend_height = 25 + len(functions_with_labels) * 22
        
        svg_parts.append(f'  <g class="annotation-group">')
        svg_parts.append(f'    <rect x="{legend_x - legend_width}" y="{legend_y}" width="{legend_width}" height="{legend_height}" rx="6" fill="white" fill-opacity="0.95" stroke="{COLORS["grid"]}" stroke-width="1"/>')
        svg_parts.append(f'    <text x="{legend_x - legend_width + 10}" y="{legend_y + 16}" font-size="11" font-weight="bold" fill="{COLORS["text"]}">Leyenda</text>')
        
        for i, func in enumerate(functions_with_labels):
            func_color = func.get('color', COLOR_PALETTE[i % len(COLOR_PALETTE)])
            func_label = func.get('label', '')
            ly = legend_y + 30 + i * 22
            svg_parts.append(f'    <line x1="{legend_x - legend_width + 10}" y1="{ly}" x2="{legend_x - legend_width + 35}" y2="{ly}" stroke="{func_color}" stroke-width="3" stroke-linecap="round"/>')
            svg_parts.append(f'    <text x="{legend_x - legend_width + 42}" y="{ly + 4}" font-size="10" fill="{COLORS["text"]}">{func_label}</text>')
        svg_parts.append('  </g>')
    
    # Anotaciones
    if annotations:
        svg_parts.append('  <g class="annotation-group">')
        for ann in annotations:
            ann_type = ann.get('type', 'text')
            color = ann.get('color', COLORS['quaternary'])
            style = ann.get('style', 'solid')
            dashed = ann.get('dashed', style == 'dashed')
            dasharray = '8,4' if dashed else 'none'
            
            # Saltar anotación de leyenda (ya procesada arriba)
            if ann_type == 'legend':
                continue
            
            if ann_type == 'brace':
                from_x = parse_math_expr(ann.get('from_x', 0))
                to_x = parse_math_expr(ann.get('to_x', 2 * PI))
                y_pos = parse_math_expr(ann.get('y', y_min - 0.1))
                label = ann.get('label', '')
                cx1, cy = map_to_canvas(from_x, y_pos, x_min, x_max, y_min, y_max, width, height, padding)
                cx2, _ = map_to_canvas(to_x, y_pos, x_min, x_max, y_min, y_max, width, height, padding)
                svg_parts.append(f'    <path d="M {cx1:.1f} {cy - 5:.1f} L {cx1:.1f} {cy:.1f} L {cx2:.1f} {cy:.1f} L {cx2:.1f} {cy - 5:.1f}" fill="none" stroke="{color}" stroke-width="2"/>')
                svg_parts.append(f'    <text x="{(cx1 + cx2) / 2:.1f}" y="{cy + 18:.1f}" text-anchor="middle" font-size="12" font-weight="bold" fill="{color}">{label}</text>')
            
            elif ann_type == 'arrow':
                from_x = parse_math_expr(ann.get('from_x', 0))
                from_y = parse_math_expr(ann.get('from_y', 0))
                to_x = parse_math_expr(ann.get('to_x', 1))
                to_y = parse_math_expr(ann.get('to_y', 0))
                label = ann.get('label', '')
                
                cx1, cy1 = map_to_canvas(from_x, from_y, x_min, x_max, y_min, y_max, width, height, padding)
                cx2, cy2 = map_to_canvas(to_x, to_y, x_min, x_max, y_min, y_max, width, height, padding)
                
                # Calcular ángulo para la punta de flecha
                angle = math.atan2(cy2 - cy1, cx2 - cx1)
                arrow_size = 10
                ax1 = cx2 - arrow_size * math.cos(angle - 0.4)
                ay1 = cy2 - arrow_size * math.sin(angle - 0.4)
                ax2 = cx2 - arrow_size * math.cos(angle + 0.4)
                ay2 = cy2 - arrow_size * math.sin(angle + 0.4)
                
                svg_parts.append(f'    <line x1="{cx1:.1f}" y1="{cy1:.1f}" x2="{cx2:.1f}" y2="{cy2:.1f}" stroke="{color}" stroke-width="2.5"/>')
                svg_parts.append(f'    <polygon points="{cx2:.1f},{cy2:.1f} {ax1:.1f},{ay1:.1f} {ax2:.1f},{ay2:.1f}" fill="{color}"/>')
                
                if label:
                    mid_x = (cx1 + cx2) / 2
                    mid_y = (cy1 + cy2) / 2 - 12
                    svg_parts.append(f'    <rect x="{mid_x - 22}" y="{mid_y - 10}" width="44" height="14" rx="3" fill="white" fill-opacity="0.9"/>')
                    svg_parts.append(f'    <text x="{mid_x:.1f}" y="{mid_y:.1f}" text-anchor="middle" font-size="11" font-weight="bold" fill="{color}">{label}</text>')
            
            elif ann_type == 'horizontal_line':
                y_val = parse_math_expr(ann.get('y', 0))
                label = ann.get('label', '')
                _, cy = map_to_canvas(0, y_val, x_min, x_max, y_min, y_max, width, height, padding)
                svg_parts.append(f'    <line x1="{padding}" y1="{cy:.1f}" x2="{width - padding}" y2="{cy:.1f}" stroke="{color}" stroke-width="1.5" stroke-dasharray="{dasharray}"/>')
                if label:
                    svg_parts.append(f'    <text x="{width - padding + 5}" y="{cy + 4:.1f}" text-anchor="start" font-size="10" fill="{color}">{label}</text>')
            
            elif ann_type == 'vertical_asymptote':
                x_val = parse_math_expr(ann.get('x', 0))
                label = ann.get('label', '')
                cx, _ = map_to_canvas(x_val, 0, x_min, x_max, y_min, y_max, width, height, padding)
                svg_parts.append(f'    <line x1="{cx:.1f}" y1="{padding}" x2="{cx:.1f}" y2="{height - padding}" stroke="{color}" stroke-width="1.5" stroke-dasharray="8,4"/>')
                if label:
                    svg_parts.append(f'    <text x="{cx + 5:.1f}" y="{padding + 15}" text-anchor="start" font-size="9" fill="{color}">{label}</text>')
            
            elif ann_type == 'text':
                x_pos = parse_math_expr(ann.get('x', 0))
                y_pos = parse_math_expr(ann.get('y', 0))
                text = ann.get('text', '')
                font_size = ann.get('fontSize', 11)
                font_weight = ann.get('fontWeight', 'normal')
                cx, cy = map_to_canvas(x_pos, y_pos, x_min, x_max, y_min, y_max, width, height, padding)
                # Manejar texto multilínea
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    svg_parts.append(f'    <text x="{cx:.1f}" y="{cy + i * 14:.1f}" text-anchor="middle" font-size="{font_size}" font-weight="{font_weight}" fill="{color}">{line}</text>')
        
        svg_parts.append('  </g>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_bar_svg(spec: Dict[str, Any]) -> str:
    """Genera SVG para gráficos de barras."""
    
    canvas = spec.get('canvas', {})
    width = canvas.get('width', 600)
    height = canvas.get('height', 400)
    padding = canvas.get('padding', 60)
    bg_color = canvas.get('background', COLORS['background'])
    
    data = spec.get('data', {})
    labels = data.get('labels', [])
    values = data.get('values', [])
    colors = data.get('colors', [])
    
    title = spec.get('metadata', {}).get('title', '')
    animations = spec.get('animations', {})
    anim_enabled = animations.get('enabled', True)
    
    if not labels or not values:
        return '<svg><text>Error: No data provided</text></svg>'
    
    y_max = max(values) * 1.2
    y_min = 0
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="max-width: 100%; height: auto; font-family: Inter, system-ui, sans-serif;">',
    ]
    
    svg_parts.append(f'''
  <style>
    .bar {{ transform-origin: bottom; transform: scaleY(0); animation: {f'growBar 0.8s ease-out forwards' if anim_enabled else 'none'}; }}
    .bar-label {{ opacity: 0; animation: {f'fadeIn 0.5s ease-out 0.8s forwards' if anim_enabled else 'none'}; }}
    @keyframes growBar {{ to {{ transform: scaleY(1); }} }}
    @keyframes fadeIn {{ to {{ opacity: 1; }} }}
  </style>
''')
    
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="{bg_color}" rx="8"/>')
    
    if title:
        svg_parts.append(f'  <text x="{width/2}" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">{title}</text>')
    
    plot_x = padding
    plot_y = 50
    plot_width = width - 2 * padding
    plot_height = height - 100
    
    # Eje Y
    svg_parts.append(f'  <line x1="{plot_x}" y1="{plot_y}" x2="{plot_x}" y2="{plot_y + plot_height}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    
    # Eje X
    svg_parts.append(f'  <line x1="{plot_x}" y1="{plot_y + plot_height}" x2="{plot_x + plot_width}" y2="{plot_y + plot_height}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    
    # Barras
    bar_width = plot_width / len(labels) * 0.7
    bar_gap = plot_width / len(labels) * 0.3
    
    for i, (label, value) in enumerate(zip(labels, values)):
        color = colors[i] if i < len(colors) else COLOR_PALETTE[i % len(COLOR_PALETTE)]
        
        bar_x = plot_x + (i + 0.5) * (plot_width / len(labels)) - bar_width / 2
        bar_height = (value / y_max) * plot_height
        bar_y = plot_y + plot_height - bar_height
        
        # Delay escalonado para cada barra
        delay = i * 0.1
        
        svg_parts.append(f'  <rect class="bar" x="{bar_x:.1f}" y="{bar_y:.1f}" width="{bar_width:.1f}" height="{bar_height:.1f}" fill="{color}" rx="4" style="animation-delay: {delay}s;"/>')
        
        # Etiqueta del valor
        svg_parts.append(f'  <text class="bar-label" x="{bar_x + bar_width/2:.1f}" y="{bar_y - 8:.1f}" text-anchor="middle" font-size="12" font-weight="bold" fill="{COLORS["text"]}" style="animation-delay: {delay + 0.8}s;">{value}</text>')
        
        # Etiqueta del eje X
        svg_parts.append(f'  <text x="{bar_x + bar_width/2:.1f}" y="{plot_y + plot_height + 20:.1f}" text-anchor="middle" font-size="11" fill="{COLORS["axis"]}">{label}</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_histogram_svg(spec: Dict[str, Any]) -> str:
    """Genera SVG para histogramas."""
    
    canvas = spec.get('canvas', {})
    width = canvas.get('width', 600)
    height = canvas.get('height', 400)
    padding = canvas.get('padding', 60)
    bg_color = canvas.get('background', COLORS['background'])
    
    data = spec.get('data', {})
    bins = data.get('bins', [])  # [{"from": 0, "to": 10, "count": 5}, ...]
    color = data.get('color', COLORS['primary'])
    
    title = spec.get('metadata', {}).get('title', '')
    x_label = spec.get('axes', {}).get('x', {}).get('label', '')
    y_label = spec.get('axes', {}).get('y', {}).get('label', 'Frecuencia')
    
    animations = spec.get('animations', {})
    anim_enabled = animations.get('enabled', True)
    
    if not bins:
        return '<svg><text>Error: No bins provided</text></svg>'
    
    max_count = max(b.get('count', 0) for b in bins)
    y_max = max_count * 1.2
    x_min = bins[0].get('from', 0)
    x_max = bins[-1].get('to', 100)
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="max-width: 100%; height: auto; font-family: Inter, system-ui, sans-serif;">',
    ]
    
    svg_parts.append(f'''
  <style>
    .hist-bar {{ transform-origin: bottom; transform: scaleY(0); animation: {f'growBar 0.6s ease-out forwards' if anim_enabled else 'none'}; }}
    @keyframes growBar {{ to {{ transform: scaleY(1); }} }}
  </style>
''')
    
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="{bg_color}" rx="8"/>')
    
    if title:
        svg_parts.append(f'  <text x="{width/2}" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">{title}</text>')
    
    plot_x = padding
    plot_y = 50
    plot_width = width - 2 * padding
    plot_height = height - 110
    
    # Ejes
    svg_parts.append(f'  <line x1="{plot_x}" y1="{plot_y}" x2="{plot_x}" y2="{plot_y + plot_height}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    svg_parts.append(f'  <line x1="{plot_x}" y1="{plot_y + plot_height}" x2="{plot_x + plot_width}" y2="{plot_y + plot_height}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    
    # Etiquetas de ejes
    if x_label:
        svg_parts.append(f'  <text x="{plot_x + plot_width/2}" y="{height - 10}" text-anchor="middle" font-size="12" fill="{COLORS["axis"]}">{x_label}</text>')
    if y_label:
        svg_parts.append(f'  <text x="15" y="{plot_y + plot_height/2}" text-anchor="middle" font-size="12" fill="{COLORS["axis"]}" transform="rotate(-90, 15, {plot_y + plot_height/2})">{y_label}</text>')
    
    # Barras del histograma
    total_range = x_max - x_min
    
    for i, bin_data in enumerate(bins):
        bin_from = bin_data.get('from', 0)
        bin_to = bin_data.get('to', 0)
        count = bin_data.get('count', 0)
        
        bar_x = plot_x + ((bin_from - x_min) / total_range) * plot_width
        bar_width = ((bin_to - bin_from) / total_range) * plot_width
        bar_height = (count / y_max) * plot_height if y_max > 0 else 0
        bar_y = plot_y + plot_height - bar_height
        
        delay = i * 0.08
        
        svg_parts.append(f'  <rect class="hist-bar" x="{bar_x:.1f}" y="{bar_y:.1f}" width="{bar_width:.1f}" height="{bar_height:.1f}" fill="{color}" stroke="white" stroke-width="1" style="animation-delay: {delay}s;"/>')
        
        # Etiqueta del rango
        svg_parts.append(f'  <text x="{bar_x + bar_width/2:.1f}" y="{plot_y + plot_height + 15:.1f}" text-anchor="middle" font-size="10" fill="{COLORS["axis"]}">{bin_from}-{bin_to}</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_pie_svg(spec: Dict[str, Any]) -> str:
    """Genera SVG para gráficos de pastel (fracciones)."""
    
    canvas = spec.get('canvas', {})
    width = canvas.get('width', 400)
    height = canvas.get('height', 400)
    bg_color = canvas.get('background', COLORS['background'])
    
    data = spec.get('data', {})
    segments = data.get('segments', [])  # [{"value": 3, "label": "3/4", "color": "#..."}, ...]
    show_labels = data.get('showLabels', True)
    
    title = spec.get('metadata', {}).get('title', '')
    animations = spec.get('animations', {})
    anim_enabled = animations.get('enabled', True)
    
    if not segments:
        return '<svg><text>Error: No segments provided</text></svg>'
    
    total = sum(s.get('value', 0) for s in segments)
    
    cx, cy = width / 2, height / 2 + 15
    radius = min(width, height) / 2 - 60
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="max-width: 100%; height: auto; font-family: Inter, system-ui, sans-serif;">',
    ]
    
    svg_parts.append(f'''
  <style>
    .pie-segment {{ transform-origin: {cx}px {cy}px; transform: scale(0); animation: {f'popIn 0.5s ease-out forwards' if anim_enabled else 'none'}; }}
    .pie-label {{ opacity: 0; animation: {f'fadeIn 0.5s ease-out 0.5s forwards' if anim_enabled else 'none'}; }}
    @keyframes popIn {{ to {{ transform: scale(1); }} }}
    @keyframes fadeIn {{ to {{ opacity: 1; }} }}
  </style>
''')
    
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="{bg_color}" rx="8"/>')
    
    if title:
        svg_parts.append(f'  <text x="{width/2}" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">{title}</text>')
    
    # Segmentos del pie
    start_angle = -90  # Empezar desde arriba
    
    for i, segment in enumerate(segments):
        value = segment.get('value', 0)
        label = segment.get('label', '')
        color = segment.get('color', COLOR_PALETTE[i % len(COLOR_PALETTE)])
        
        angle = (value / total) * 360 if total > 0 else 0
        end_angle = start_angle + angle
        
        # Convertir a radianes
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        # Puntos del arco
        x1 = cx + radius * math.cos(start_rad)
        y1 = cy + radius * math.sin(start_rad)
        x2 = cx + radius * math.cos(end_rad)
        y2 = cy + radius * math.sin(end_rad)
        
        # Flag para arco grande
        large_arc = 1 if angle > 180 else 0
        
        delay = i * 0.15
        
        # Path del segmento
        if angle >= 360:
            # Círculo completo
            svg_parts.append(f'  <circle class="pie-segment" cx="{cx}" cy="{cy}" r="{radius}" fill="{color}" stroke="white" stroke-width="2" style="animation-delay: {delay}s;"/>')
        else:
            svg_parts.append(f'  <path class="pie-segment" d="M {cx} {cy} L {x1:.1f} {y1:.1f} A {radius} {radius} 0 {large_arc} 1 {x2:.1f} {y2:.1f} Z" fill="{color}" stroke="white" stroke-width="2" style="animation-delay: {delay}s;"/>')
        
        # Etiqueta
        if show_labels and label:
            mid_angle = math.radians(start_angle + angle / 2)
            label_r = radius * 0.65
            lx = cx + label_r * math.cos(mid_angle)
            ly = cy + label_r * math.sin(mid_angle)
            svg_parts.append(f'  <text class="pie-label" x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="14" font-weight="bold" fill="white" style="animation-delay: {delay + 0.5}s;">{label}</text>')
        
        start_angle = end_angle
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_scatter_svg(spec: Dict[str, Any]) -> str:
    """Genera SVG para gráficos de dispersión (scatter plots)."""
    
    canvas = spec.get('canvas', {})
    width = canvas.get('width', 600)
    height = canvas.get('height', 400)
    padding = canvas.get('padding', 60)
    bg_color = canvas.get('background', COLORS['background'])
    
    data = spec.get('data', {})
    points = data.get('points', [])  # [{"x": 1, "y": 2, "label": "A"}, ...]
    point_color = data.get('color', COLORS['primary'])
    point_size = data.get('size', 8)
    
    axes = spec.get('axes', {})
    x_axis = axes.get('x', {})
    y_axis = axes.get('y', {})
    
    title = spec.get('metadata', {}).get('title', '')
    animations = spec.get('animations', {})
    anim_enabled = animations.get('enabled', True)
    
    if not points:
        return '<svg><text>Error: No points provided</text></svg>'
    
    x_values = [p.get('x', 0) for p in points]
    y_values = [p.get('y', 0) for p in points]
    
    x_min = x_axis.get('min', min(x_values) - 1)
    x_max = x_axis.get('max', max(x_values) + 1)
    y_min = y_axis.get('min', min(y_values) - 1)
    y_max = y_axis.get('max', max(y_values) + 1)
    
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" ',
        f'style="max-width: 100%; height: auto; font-family: Inter, system-ui, sans-serif;">',
    ]
    
    svg_parts.append(f'''
  <style>
    .scatter-point {{ transform: scale(0); animation: {f'popIn 0.3s ease-out forwards' if anim_enabled else 'none'}; }}
    @keyframes popIn {{ to {{ transform: scale(1); }} }}
  </style>
''')
    
    svg_parts.append(f'  <rect width="{width}" height="{height}" fill="{bg_color}" rx="8"/>')
    
    if title:
        svg_parts.append(f'  <text x="{width/2}" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="{COLORS["text"]}">{title}</text>')
    
    plot_x = padding
    plot_y = 50
    plot_width = width - 2 * padding
    plot_height = height - 100
    
    # Cuadrícula
    svg_parts.append('  <g class="grid">')
    x_step = (x_max - x_min) / 5
    for i in range(6):
        x_val = x_min + i * x_step
        cx, _ = map_to_canvas(x_val, 0, x_min, x_max, y_min, y_max, width, height, padding)
        svg_parts.append(f'    <line x1="{cx:.1f}" y1="{plot_y}" x2="{cx:.1f}" y2="{plot_y + plot_height}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
    
    y_step = (y_max - y_min) / 5
    for i in range(6):
        y_val = y_min + i * y_step
        _, cy = map_to_canvas(0, y_val, x_min, x_max, y_min, y_max, width, height, padding)
        svg_parts.append(f'    <line x1="{plot_x}" y1="{cy:.1f}" x2="{plot_x + plot_width}" y2="{cy:.1f}" stroke="{COLORS["grid"]}" stroke-dasharray="4,4"/>')
    svg_parts.append('  </g>')
    
    # Ejes
    origin_x, origin_y = map_to_canvas(0, 0, x_min, x_max, y_min, y_max, width, height, padding)
    svg_parts.append(f'  <line x1="{plot_x}" y1="{origin_y:.1f}" x2="{plot_x + plot_width}" y2="{origin_y:.1f}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    svg_parts.append(f'  <line x1="{origin_x:.1f}" y1="{plot_y}" x2="{origin_x:.1f}" y2="{plot_y + plot_height}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
    
    # Etiquetas de ejes
    x_label = x_axis.get('label', 'x')
    y_label = y_axis.get('label', 'y')
    svg_parts.append(f'  <text x="{plot_x + plot_width + 10}" y="{origin_y + 5:.1f}" font-size="14" font-weight="bold" fill="{COLORS["axis"]}">{x_label}</text>')
    svg_parts.append(f'  <text x="{origin_x + 8:.1f}" y="{plot_y - 5}" font-size="14" font-weight="bold" fill="{COLORS["axis"]}">{y_label}</text>')
    
    # Puntos
    for i, point in enumerate(points):
        px = point.get('x', 0)
        py = point.get('y', 0)
        label = point.get('label', '')
        color = point.get('color', point_color)
        
        cx, cy = map_to_canvas(px, py, x_min, x_max, y_min, y_max, width, height, padding)
        delay = i * 0.1
        
        svg_parts.append(f'  <circle class="scatter-point" cx="{cx:.1f}" cy="{cy:.1f}" r="{point_size}" fill="{color}" stroke="white" stroke-width="2" style="transform-origin: {cx:.1f}px {cy:.1f}px; animation-delay: {delay}s;"/>')
        
        if label:
            svg_parts.append(f'  <text x="{cx:.1f}" y="{cy - point_size - 5:.1f}" text-anchor="middle" font-size="11" font-weight="bold" fill="{COLORS["text"]}">{label}</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


# ============================================================================
# DISPATCHER PRINCIPAL
# ============================================================================

def generate_svg(spec: Dict[str, Any]) -> str:
    """Genera el SVG según el tipo de gráfico especificado."""
    
    graph_type = spec.get('type', 'function')
    
    generators = {
        'function': generate_function_svg,
        'bar': generate_bar_svg,
        'histogram': generate_histogram_svg,
        'pie': generate_pie_svg,
        'scatter': generate_scatter_svg,
    }
    
    generator = generators.get(graph_type, generate_function_svg)
    return generator(spec)


def main():
    parser = argparse.ArgumentParser(description='GraphSpec Renderer - Genera SVGs de gráficas matemáticas')
    parser.add_argument('--spec', required=True, help='Archivo JSON de especificación')
    parser.add_argument('--output', required=True, help='Archivo SVG de salida')
    parser.add_argument('--preview', action='store_true', help='Abrir en navegador')
    parser.add_argument('--validate-only', action='store_true', help='Solo validar, no generar')
    
    args = parser.parse_args()
    
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"Error: El archivo {args.spec} no existe")
        return 1
    
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    
    graph_type = spec.get('type', 'function')
    spec_id = spec.get('metadata', {}).get('id', 'sin-id')
    print(f"✓ Spec cargado: {spec_id} (tipo: {graph_type})")
    
    if args.validate_only:
        print("✓ Spec válido")
        return 0
    
    svg_content = generate_svg(spec)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"✓ SVG generado: {args.output}")
    
    if args.preview:
        webbrowser.open(f'file://{output_path.absolute()}')
        print("✓ Abierto en navegador")
    
    return 0


if __name__ == '__main__':
    exit(main())

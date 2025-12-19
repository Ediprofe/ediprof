"""
MindMap Renderer - Genera mapas conceptuales como SVG
Versión 2.0 - Diseño Premium
"""

import json
import argparse
import math
from pathlib import Path

# Estilos predefinidos - PREMIUM
STYLES = {
    "elegante": {
        "background": "linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%)",
        "bg_color": "#f1f5f9",
        "node_central": {
            "fill": "url(#gradient-central)",
            "gradient": ["#2563eb", "#1d4ed8"],
            "stroke": "#1e40af",
            "text": "#ffffff",
            "shadow": "0 4px 12px rgba(37, 99, 235, 0.35)"
        },
        "node_rama": {
            "fill": "#ffffff",
            "stroke_width": 2.5,
            "text": "#1e293b",
            "shadow": "0 2px 8px rgba(0, 0, 0, 0.08)"
        },
        "node_hoja": {
            "fill": "#ffffff",
            "text": "#475569",
            "shadow": "0 1px 4px rgba(0, 0, 0, 0.06)"
        },
        "linea": {"color": "#94a3b8", "width": 2},
        "font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    },
    "vibrante": {
        "background": "linear-gradient(135deg, #fdf4ff 0%, #fae8ff 100%)",
        "bg_color": "#fdf4ff",
        "node_central": {
            "fill": "url(#gradient-central)",
            "gradient": ["#9333ea", "#7c3aed"],
            "stroke": "#6b21a8",
            "text": "#ffffff",
            "shadow": "0 4px 12px rgba(147, 51, 234, 0.35)"
        },
        "node_rama": {
            "fill": "#ffffff",
            "stroke_width": 2.5,
            "text": "#1e1b4b",
            "shadow": "0 2px 8px rgba(0, 0, 0, 0.08)"
        },
        "node_hoja": {
            "fill": "#ffffff",
            "text": "#4c1d95",
            "shadow": "0 1px 4px rgba(0, 0, 0, 0.06)"
        },
        "linea": {"color": "#c4b5fd", "width": 2},
        "font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    },
    "oscuro-premium": {
        "background": "linear-gradient(135deg, #0f172a 0%, #1e293b 100%)",
        "bg_color": "#0f172a",
        "node_central": {
            "fill": "url(#gradient-central)",
            "gradient": ["#3b82f6", "#2563eb"],
            "stroke": "#60a5fa",
            "text": "#ffffff",
            "shadow": "0 4px 16px rgba(59, 130, 246, 0.4)"
        },
        "node_rama": {
            "fill": "#1e293b",
            "stroke_width": 2,
            "text": "#f1f5f9",
            "shadow": "0 2px 8px rgba(0, 0, 0, 0.3)"
        },
        "node_hoja": {
            "fill": "#1e293b",
            "text": "#cbd5e1",
            "shadow": "0 1px 4px rgba(0, 0, 0, 0.2)"
        },
        "linea": {"color": "#475569", "width": 2},
        "font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    }
}


def escape_xml(text: str) -> str:
    """Escapa caracteres especiales para XML/SVG."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))


def calculate_text_width(text: str, font_size: int) -> float:
    """Estima el ancho del texto en píxeles."""
    return len(text) * font_size * 0.55


def generate_mindmap_svg(spec: dict) -> str:
    """Genera SVG de mapa conceptual desde spec."""
    
    estilo_nombre = spec.get("estilo", "elegante")
    style = STYLES.get(estilo_nombre, STYLES["elegante"])
    
    nodo_central = spec.get("nodo_central", {})
    ramas = spec.get("ramas", [])
    
    # Calcular dimensiones basadas en contenido
    num_ramas = len(ramas)
    max_hijos = max(len(r.get("hijos", [])) for r in ramas) if ramas else 0
    
    # Dimensiones ajustadas al contenido (sin espacio vacío)
    padding = 30
    rama_spacing = 280  # espacio entre ramas
    width = padding * 2 + (num_ramas * rama_spacing)
    height = padding + 70 + 100 + (max_hijos * 44) + padding
    
    # Centro del nodo principal
    cx = width // 2
    cy = padding + 35
    
    svg_parts = []
    
    # Gradientes del nodo central
    grad = style["node_central"]["gradient"]
    
    # Header SVG con defs mejorados
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="gradient-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8fafc"/>
      <stop offset="100%" style="stop-color:#e2e8f0"/>
    </linearGradient>
    <linearGradient id="gradient-central" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{grad[0]}"/>
      <stop offset="100%" style="stop-color:{grad[1]}"/>
    </linearGradient>
    <filter id="shadow-lg" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="{grad[0]}" flood-opacity="0.25"/>
    </filter>
    <filter id="shadow-md" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.1"/>
    </filter>
    <filter id="shadow-sm" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.08"/>
    </filter>
  </defs>
  
  <style>
    .font-main {{ font-family: {style['font']}; }}
    .node-central {{ font-weight: 700; font-size: 20px; }}
    .node-rama {{ font-weight: 600; font-size: 15px; }}
    .node-hoja {{ font-weight: 500; font-size: 13px; }}
  </style>
  
  <!-- Fondo con gradiente -->
  <rect width="100%" height="100%" fill="url(#gradient-bg)"/>
''')
    
    # Nodo central
    texto_central = nodo_central.get("texto", "")
    icono = nodo_central.get("icono", "")
    texto_completo = f"{icono} {texto_central}".strip() if icono else texto_central
    
    central_width = max(160, calculate_text_width(texto_completo, 20) + 50)
    central_height = 52
    central_x = cx - central_width / 2
    central_y = cy - central_height / 2
    central_radius = 12
    
    ns = style["node_central"]
    svg_parts.append(f'''  <!-- Nodo Central -->
  <rect x="{central_x}" y="{central_y}" width="{central_width}" height="{central_height}" 
        rx="{central_radius}" fill="{ns['fill']}" stroke="{ns['stroke']}" stroke-width="2" 
        filter="url(#shadow-lg)"/>
  <text x="{cx}" y="{cy + 7}" text-anchor="middle" fill="{ns['text']}" 
        class="font-main node-central">{escape_xml(texto_completo)}</text>
''')
    
    # Ramas
    rama_spacing = width // (num_ramas + 1)
    
    for i, rama in enumerate(ramas):
        rama_x = rama_spacing * (i + 1)
        rama_y = 160
        
        rama_texto = rama.get("texto", "")
        rama_icono = rama.get("icono", "")
        rama_color = rama.get("color", "#3b82f6")
        hijos = rama.get("hijos", [])
        
        texto_rama = f"{rama_icono} {rama_texto}".strip() if rama_icono else rama_texto
        rama_width = max(130, calculate_text_width(texto_rama, 15) + 40)
        rama_height = 42
        
        # Línea curva elegante del centro a la rama
        mid_y = (cy + central_height/2 + rama_y - rama_height/2) / 2
        svg_parts.append(f'''  <!-- Rama: {escape_xml(rama_texto)} -->
  <path d="M {cx} {cy + central_height/2 + 4} 
           C {cx} {mid_y}, {rama_x} {mid_y}, {rama_x} {rama_y - rama_height/2 - 4}" 
        stroke="{style['linea']['color']}" stroke-width="{style['linea']['width']}" 
        fill="none" stroke-linecap="round"/>
''')
        
        # Nodo de rama con borde de color
        nr = style["node_rama"]
        svg_parts.append(f'''  <rect x="{rama_x - rama_width/2}" y="{rama_y - rama_height/2}" 
        width="{rama_width}" height="{rama_height}" rx="10" 
        fill="{nr['fill']}" stroke="{rama_color}" stroke-width="{nr['stroke_width']}" 
        filter="url(#shadow-md)"/>
  <text x="{rama_x}" y="{rama_y + 6}" text-anchor="middle" fill="{rama_color}" 
        class="font-main node-rama">{escape_xml(texto_rama)}</text>
''')
        
        # Línea vertical desde la rama
        first_hijo_y = rama_y + rama_height/2 + 25
        last_hijo_y = rama_y + rama_height/2 + 25 + (len(hijos) - 1) * 44
        
        if hijos:
            svg_parts.append(f'''  <line x1="{rama_x}" y1="{rama_y + rama_height/2}" 
        x2="{rama_x}" y2="{last_hijo_y}" 
        stroke="{rama_color}" stroke-width="2" stroke-opacity="0.3"/>
''')
        
        # Hijos
        for j, hijo in enumerate(hijos):
            hijo_y = rama_y + rama_height/2 + 25 + j * 44
            hijo_texto = hijo if isinstance(hijo, str) else hijo.get("texto", "")
            
            hijo_width = max(110, calculate_text_width(hijo_texto, 13) + 28)
            hijo_height = 32
            
            nh = style["node_hoja"]
            
            # Punto de conexión
            svg_parts.append(f'''  <circle cx="{rama_x}" cy="{hijo_y}" r="4" fill="{rama_color}" opacity="0.6"/>
  <line x1="{rama_x + 4}" y1="{hijo_y}" x2="{rama_x + 18}" y2="{hijo_y}" 
        stroke="{rama_color}" stroke-width="2" stroke-opacity="0.4"/>
''')
            
            # Nodo hijo con borde sutil del color de la rama
            svg_parts.append(f'''  <rect x="{rama_x + 22}" y="{hijo_y - hijo_height/2}" 
        width="{hijo_width}" height="{hijo_height}" rx="8" 
        fill="{nh['fill']}" stroke="{rama_color}" stroke-width="1.5" stroke-opacity="0.5"
        filter="url(#shadow-sm)"/>
  <text x="{rama_x + 22 + hijo_width/2}" y="{hijo_y + 5}" text-anchor="middle" 
        fill="{nh['text']}" class="font-main node-hoja">{escape_xml(hijo_texto)}</text>
''')
    
    svg_parts.append('</svg>')
    
    return '\n'.join(svg_parts)


def generate_flowchart_svg(spec: dict) -> str:
    """Genera SVG de diagrama de flujo/ciclo desde spec."""
    
    estilo_nombre = spec.get("estilo", "elegante")
    style = STYLES.get(estilo_nombre, STYLES["elegante"])
    
    pasos = spec.get("pasos", [])
    layout = spec.get("layout", "ciclo")  # ciclo, lineal, vertical
    titulo = spec.get("titulo", "")
    
    num_pasos = len(pasos)
    
    # Dimensiones ajustadas al contenido
    padding = 25
    node_width = 150
    node_height = 44
    h_gap = 60  # espacio horizontal entre nodos
    v_gap = 50  # espacio vertical entre filas
    
    # Calcular dimensiones basadas en layout
    if num_pasos >= 7:
        width = padding + (3 * node_width) + (2 * h_gap) + padding
        height = padding + (35 if titulo else 0) + node_height + v_gap + node_height + v_gap + node_height + padding
    else:
        width = padding + (3 * node_width) + (2 * h_gap) + padding
        height = padding + (35 if titulo else 0) + node_height + v_gap + node_height + padding
    
    # Gradiente del estilo
    grad = style["node_central"]["gradient"]
    
    svg_parts = []
    
    # Header
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="gradient-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8fafc"/>
      <stop offset="100%" style="stop-color:#e2e8f0"/>
    </linearGradient>
    <filter id="shadow-step" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-opacity="0.15"/>
    </filter>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#64748b"/>
    </marker>
  </defs>
  
  <style>
    .font-main {{ font-family: {style['font']}; }}
    .step-text {{ font-weight: 600; font-size: 13px; fill: white; }}
    .step-num {{ font-weight: 700; font-size: 11px; fill: rgba(255,255,255,0.8); }}
  </style>
  
  <rect width="100%" height="100%" fill="url(#gradient-bg)"/>
''')
    
    # Título si existe
    if titulo:
        svg_parts.append(f'''  <text x="{width/2}" y="35" text-anchor="middle" class="font-main" 
        font-size="18" font-weight="700" fill="#1e293b">{escape_xml(titulo)}</text>
''')
    
    num_pasos_internal = len(pasos)
    
    if layout == "ciclo":
        # Layout en forma de U invertida
        # Posiciones calculadas dinámicamente
        
        titulo_offset = 35 if titulo else 0
        fila1_y = padding + titulo_offset + node_height / 2
        fila2_y = fila1_y + node_height + v_gap
        fila3_y = fila2_y + node_height + v_gap if num_pasos >= 7 else 0
        
        # Centros de columnas
        col1 = padding + node_width / 2
        col2 = width / 2
        col3 = width - padding - node_width / 2
        
        # Posiciones de los pasos
        posiciones = []
        
        if num_pasos_internal >= 6:
            # Fila 1: 3 pasos de izq a der
            posiciones.append((col1, fila1_y))
            posiciones.append((col2, fila1_y))
            posiciones.append((col3, fila1_y))
            # Fila 2: 3 pasos de der a izq
            posiciones.append((col3, fila2_y))
            posiciones.append((col2, fila2_y))
            posiciones.append((col1, fila2_y))
            # Paso 7 al centro abajo
            if num_pasos_internal >= 7:
                posiciones.append((col2, fila3_y))
        
        # Dibujar flechas primero
        arrow_color = "#94a3b8"
        arrow_gap = 15
        
        # Flechas fila 1 (→)
        svg_parts.append(f'''  <!-- Flechas -->
  <line x1="{col1 + node_width/2 + arrow_gap}" y1="{fila1_y}" x2="{col2 - node_width/2 - arrow_gap}" y2="{fila1_y}" stroke="{arrow_color}" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="{col2 + node_width/2 + arrow_gap}" y1="{fila1_y}" x2="{col3 - node_width/2 - arrow_gap}" y2="{fila1_y}" stroke="{arrow_color}" stroke-width="2" marker-end="url(#arrowhead)"/>
''')
        
        # Flecha bajando (3→4)
        svg_parts.append(f'''  <line x1="{col3}" y1="{fila1_y + node_height/2 + 5}" x2="{col3}" y2="{fila2_y - node_height/2 - 5}" stroke="{arrow_color}" stroke-width="2" marker-end="url(#arrowhead)"/>
''')
        
        # Flechas fila 2 (←)
        svg_parts.append(f'''  <line x1="{col3 - node_width/2 - arrow_gap}" y1="{fila2_y}" x2="{col2 + node_width/2 + arrow_gap}" y2="{fila2_y}" stroke="{arrow_color}" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="{col2 - node_width/2 - arrow_gap}" y1="{fila2_y}" x2="{col1 + node_width/2 + arrow_gap}" y2="{fila2_y}" stroke="{arrow_color}" stroke-width="2" marker-end="url(#arrowhead)"/>
''')
        
        # Flecha a paso 7 (si existe)
        if num_pasos_internal >= 7:
            svg_parts.append(f'''  <path d="M {col1} {fila2_y + node_height/2 + 5} L {col1} {fila3_y} L {col2 - node_width/2 - arrow_gap} {fila3_y}" 
        stroke="{arrow_color}" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
''')
        
        # Flecha de retroalimentación
        svg_parts.append(f'''  <path d="M {col2} {fila2_y - node_height/2 - 5} C {col2} {fila1_y + 30}, {col3 - 30} {fila1_y + 30}, {col3} {fila1_y + node_height/2 + 5}" 
        stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="6,4" fill="none"/>
  <text x="{(col2 + col3)/2}" y="{fila1_y + 45}" class="font-main" font-size="10" fill="#94a3b8" text-anchor="middle">↺ Replantear</text>
''')
        
        # Dibujar nodos
        for i, paso in enumerate(pasos[:len(posiciones)]):
            x, y = posiciones[i]
            texto = paso.get("texto", f"Paso {i+1}")
            color = paso.get("color", grad[0])
            icono = paso.get("icono", "")
            
            texto_display = f"{icono} {texto}".strip() if icono else texto
            
            svg_parts.append(f'''  <!-- Paso {i+1} -->
  <rect x="{x - node_width/2}" y="{y - node_height/2}" width="{node_width}" height="{node_height}" 
        rx="10" fill="{color}" filter="url(#shadow-step)"/>
  <text x="{x}" y="{y + 5}" text-anchor="middle" class="font-main step-text">{escape_xml(texto_display)}</text>
''')
    
    svg_parts.append('</svg>')
    
    return '\n'.join(svg_parts)


def main():
    parser = argparse.ArgumentParser(description='Genera diagramas SVG (mindmap, flowchart)')
    parser.add_argument('--spec', required=True, help='Ruta al archivo spec JSON')
    parser.add_argument('--output', required=True, help='Ruta de salida del SVG')
    
    args = parser.parse_args()
    
    # Leer spec
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"Error: Spec no encontrado: {spec_path}")
        return 1
    
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    
    # Detectar tipo y generar SVG
    tipo = spec.get("tipo", "mindmap")
    
    if tipo == "flowchart":
        svg_content = generate_flowchart_svg(spec)
    else:
        svg_content = generate_mindmap_svg(spec)
    
    # Guardar
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"✓ SVG generado ({tipo}): {output_path}")
    print(f"  Tamaño: {len(svg_content)} bytes")
    
    return 0


if __name__ == "__main__":
    exit(main())


#!/usr/bin/env python3
"""
🗺️ Concept Map Renderer - Genera mapas conceptuales SVG desde specs JSON

Sistema ConceptMapSpec para crear diagramas jerárquicos educativos.

Uso:
    python3 scripts/diagrams/conceptmap_renderer.py \
        --spec specs/mapas/quimica/la-materia.json \
        --output public/images/quimica/mapas/la-materia.svg

Autor: Ediprofe
"""

import json
import math
import argparse
import sys
from pathlib import Path

# Importar colores del core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))
try:
    from core.colors import COLORS
except ImportError:
    # Fallback si core no está disponible
    COLORS = {
        'background': '#f8fafc',
        'text': '#1e293b',
        'primary': '#3b82f6',
        'secondary': '#22c55e',
        'accent': '#ef4444',
        'highlight': '#f97316',
        'purple': '#8b5cf6',
    }

# ============================================================================
# PALETA ESPECÍFICA PARA MAPAS CONCEPTUALES
# ============================================================================

CONCEPTMAP_COLORS = {
    'central': '#66BB6A',      # Verde menta - nodo central
    'propiedades': '#9575CD',  # Morado suave
    'estados': '#64B5F6',      # Azul cielo
    'cambios': '#FFB74D',      # Naranja
    'clasificacion': '#BA68C8', # Lila
    'separacion': '#FF8A65',   # Coral
    'default': '#90A4AE',      # Gris azulado
    'connection': '#607D8B',   # Gris oscuro para líneas
    'text_dark': '#263238',    # Texto oscuro
    'text_light': '#FFFFFF',   # Texto claro
}

# ============================================================================
# CLASE PRINCIPAL: ConceptMapRenderer
# ============================================================================

class ConceptMapRenderer:
    """Renderiza mapas conceptuales jerárquicos como SVG."""
    
    def __init__(self, spec: dict):
        self.spec = spec
        self.canvas = spec.get('canvas', {})
        self.width = self.canvas.get('width', 1200)
        self.height = self.canvas.get('height', 800)
        self.background = self.canvas.get('background', COLORS['background'])
        self.nodes = {n['id']: n for n in spec.get('nodes', [])}
        self.layout_config = spec.get('layout', {'type': 'horizontal', 'spacing': 100})
        self.node_positions = {}
        
    def _escape_xml(self, text: str) -> str:
        """Escapa caracteres especiales para XML."""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&apos;'))
    
    def _get_children(self, parent_id: str) -> list:
        """Obtiene los hijos de un nodo."""
        return [n for n in self.nodes.values() if n.get('parent') == parent_id]
    
    def _get_root_nodes(self) -> list:
        """Obtiene nodos sin padre (raíz)."""
        return [n for n in self.nodes.values() if not n.get('parent')]
    
    def _calculate_layout_horizontal(self):
        """
        Calcula posiciones con layout horizontal (árbol de izquierda a derecha).
        El nodo central a la izquierda, ramas hacia la derecha.
        """
        spacing_x = self.layout_config.get('spacing_x', 200)
        spacing_y = self.layout_config.get('spacing_y', 80)
        start_x = 100
        
        def layout_subtree(node_id, x, y_start, y_end):
            """Posiciona un nodo y sus descendientes recursivamente."""
            node = self.nodes[node_id]
            children = self._get_children(node_id)
            
            if not children:
                # Nodo hoja: centrar verticalmente en el espacio asignado
                y = (y_start + y_end) / 2
                self.node_positions[node_id] = {'x': x, 'y': y}
                return y, y  # Retorna el rango ocupado
            
            # Distribuir hijos en el espacio vertical
            child_count = len(children)
            section_height = (y_end - y_start) / child_count
            
            child_y_ranges = []
            for i, child in enumerate(children):
                child_y_start = y_start + i * section_height
                child_y_end = child_y_start + section_height
                y_min, y_max = layout_subtree(
                    child['id'], 
                    x + spacing_x, 
                    child_y_start, 
                    child_y_end
                )
                child_y_ranges.append((y_min, y_max))
            
            # Centrar padre entre sus hijos
            all_y = [self.node_positions[c['id']]['y'] for c in children]
            parent_y = sum(all_y) / len(all_y)
            self.node_positions[node_id] = {'x': x, 'y': parent_y}
            
            return min(all_y), max(all_y)
        
        # Procesar cada raíz
        roots = self._get_root_nodes()
        if len(roots) == 1:
            layout_subtree(roots[0]['id'], start_x, 50, self.height - 50)
        else:
            section = (self.height - 100) / len(roots)
            for i, root in enumerate(roots):
                layout_subtree(root['id'], start_x, 50 + i * section, 50 + (i + 1) * section)
    
    def _calculate_layout_radial(self):
        """
        Calcula posiciones con layout radial (nodo central en medio, ramas hacia afuera).
        """
        center_x = self.width / 2
        center_y = self.height / 2
        radius_step = self.layout_config.get('radius_step', 180)
        
        def layout_level(node_ids, level, angle_start, angle_end):
            """Posiciona nodos de un nivel en un arco."""
            if not node_ids:
                return
            
            radius = radius_step * level
            angle_range = angle_end - angle_start
            angle_step = angle_range / len(node_ids) if len(node_ids) > 1 else 0
            
            for i, node_id in enumerate(node_ids):
                angle = angle_start + i * angle_step + angle_step / 2
                if level == 0:
                    x, y = center_x, center_y
                else:
                    x = center_x + radius * math.cos(math.radians(angle))
                    y = center_y + radius * math.sin(math.radians(angle))
                
                self.node_positions[node_id] = {'x': x, 'y': y}
                
                # Procesar hijos
                children = self._get_children(node_id)
                if children:
                    child_angle_range = angle_step if level > 0 else 360
                    child_angle_start = angle - child_angle_range / 2 if level > 0 else 0
                    layout_level(
                        [c['id'] for c in children],
                        level + 1,
                        child_angle_start,
                        child_angle_start + child_angle_range
                    )
        
        roots = self._get_root_nodes()
        layout_level([r['id'] for r in roots], 0, 0, 360)
    
    def _calculate_layout(self):
        """Calcula las posiciones de todos los nodos según el tipo de layout."""
        layout_type = self.layout_config.get('type', 'horizontal')
        
        if layout_type == 'radial':
            self._calculate_layout_radial()
        else:
            self._calculate_layout_horizontal()
    
    def _get_node_dimensions(self, node: dict) -> tuple:
        """Calcula ancho y alto de un nodo basado en su texto."""
        text = node.get('text', '')
        level = node.get('level', 1)
        
        # Tamaño base según nivel
        if level == 0:
            base_width, base_height = 180, 60
            font_size = 18
        elif level == 1:
            base_width, base_height = 140, 45
            font_size = 14
        else:
            base_width, base_height = 120, 35
            font_size = 12
        
        # Ajustar al texto
        text_width = len(text) * font_size * 0.6
        width = max(base_width, text_width + 40)
        
        return width, base_height, font_size
    
    def _draw_connection(self, parent_id: str, child_id: str) -> str:
        """Dibuja una conexión curva entre padre e hijo."""
        parent_pos = self.node_positions[parent_id]
        child_pos = self.node_positions[child_id]
        
        parent_node = self.nodes[parent_id]
        child_node = self.nodes[child_id]
        
        pw, ph, _ = self._get_node_dimensions(parent_node)
        cw, ch, _ = self._get_node_dimensions(child_node)
        
        # Puntos de conexión (borde derecho del padre, borde izquierdo del hijo)
        x1 = parent_pos['x'] + pw / 2
        y1 = parent_pos['y']
        x2 = child_pos['x'] - cw / 2
        y2 = child_pos['y']
        
        # Curva bezier
        cx = (x1 + x2) / 2
        
        return f'''<path d="M {x1} {y1} C {cx} {y1}, {cx} {y2}, {x2} {y2}" 
            fill="none" 
            stroke="{CONCEPTMAP_COLORS['connection']}" 
            stroke-width="2" 
            stroke-opacity="0.6"
            class="connection"/>'''
    
    def _draw_node(self, node_id: str) -> str:
        """Dibuja un nodo con su caja y texto."""
        node = self.nodes[node_id]
        pos = self.node_positions[node_id]
        
        width, height, font_size = self._get_node_dimensions(node)
        x = pos['x'] - width / 2
        y = pos['y'] - height / 2
        
        # Color del nodo
        color = node.get('color', CONCEPTMAP_COLORS['default'])
        level = node.get('level', 1)
        
        # Determinar color de texto según luminosidad del fondo
        text_color = CONCEPTMAP_COLORS['text_light'] if level == 0 else CONCEPTMAP_COLORS['text_dark']
        
        # Radio de bordes
        rx = 12 if level == 0 else 8
        
        # Sombra para nodo central
        shadow = ''
        if level == 0:
            shadow = f'''<rect x="{x + 3}" y="{y + 3}" width="{width}" height="{height}" 
                rx="{rx}" fill="#00000020"/>'''
        
        text = self._escape_xml(node.get('text', ''))
        
        return f'''{shadow}
<rect x="{x}" y="{y}" width="{width}" height="{height}" 
    rx="{rx}" 
    fill="{color}" 
    stroke="{color}" 
    stroke-width="2"
    class="node level-{level}"/>
<text x="{pos['x']}" y="{pos['y']}" 
    text-anchor="middle" 
    dominant-baseline="middle" 
    fill="{text_color}" 
    font-family="Inter, system-ui, sans-serif" 
    font-size="{font_size}" 
    font-weight="{'600' if level <= 1 else '500'}"
    class="node-text">{text}</text>'''
    
    def render(self) -> str:
        """Genera el SVG completo del mapa conceptual."""
        self._calculate_layout()
        
        # Construir SVG
        connections = []
        nodes_svg = []
        
        # Dibujar conexiones primero (para que queden debajo)
        for node in self.nodes.values():
            parent_id = node.get('parent')
            if parent_id:
                connections.append(self._draw_connection(parent_id, node['id']))
        
        # Dibujar nodos (ordenados por nivel para z-index correcto)
        sorted_nodes = sorted(self.nodes.values(), key=lambda n: n.get('level', 0), reverse=True)
        for node in sorted_nodes:
            nodes_svg.append(self._draw_node(node['id']))
        
        # Título
        title = self.spec.get('metadata', {}).get('title', 'Mapa Conceptual')
        
        svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 {self.width} {self.height}" 
     width="{self.width}" 
     height="{self.height}">
  
  <title>{self._escape_xml(title)}</title>
  
  <!-- Fondo -->
  <rect width="100%" height="100%" fill="{self.background}"/>
  
  <!-- Estilos -->
  <style>
    .connection {{
      transition: stroke-opacity 0.3s;
    }}
    .node {{
      transition: transform 0.2s, filter 0.2s;
    }}
    .node:hover {{
      filter: brightness(1.05);
    }}
    .node-text {{
      pointer-events: none;
    }}
  </style>
  
  <!-- Conexiones -->
  <g class="connections">
    {''.join(connections)}
  </g>
  
  <!-- Nodos -->
  <g class="nodes">
    {''.join(nodes_svg)}
  </g>
  
</svg>'''
        
        return svg


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Genera mapas conceptuales SVG')
    parser.add_argument('--spec', required=True, help='Archivo JSON de especificación')
    parser.add_argument('--output', required=True, help='Archivo SVG de salida')
    parser.add_argument('--preview', action='store_true', help='Abrir en navegador')
    
    args = parser.parse_args()
    
    # Leer spec
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"❌ Error: No se encontró el archivo spec: {spec_path}")
        sys.exit(1)
    
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = json.load(f)
    
    # Renderizar
    renderer = ConceptMapRenderer(spec)
    svg = renderer.render()
    
    # Guardar
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)
    
    print(f"✅ SVG generado: {output_path}")
    
    # Preview
    if args.preview:
        import webbrowser
        webbrowser.open(f'file://{output_path.absolute()}')


if __name__ == '__main__':
    main()

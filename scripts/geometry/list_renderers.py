#!/usr/bin/env python3
"""
📋 List Renderers - Descubre todos los renderers y sus capacidades

Este script escanea los docstrings de *_renderer.py para encontrar
funciones disponibles y las lecciones que soportan.

Uso:
    python scripts/geometry/list_renderers.py
    python scripts/geometry/list_renderers.py --search "pendiente"
"""

import argparse
import re
from pathlib import Path


def list_renderers(search_term: str = None):
    """
    Escanea todos los renderers y lista sus funciones.
    
    Args:
        search_term: Opcional, filtrar por término de búsqueda
    
    Returns:
        Dict con renderers y sus funciones
    """
    renderers = {}
    geometry_dir = Path(__file__).parent
    
    for f in sorted(geometry_dir.glob("*_renderer.py")):
        if f.name == "renderer_template.py":
            continue
            
        content = f.read_text()
        
        # Buscar funciones render_* con docstrings que contengan "Para:"
        pattern = r'def (render_\w+)\([^)]*\):\s*"""[^"]*?Para:\s*([^\n]+)'
        matches = re.findall(pattern, content)
        
        if matches:
            # Filtrar por término de búsqueda si se proporciona
            if search_term:
                matches = [(func, lesson) for func, lesson in matches 
                          if search_term.lower() in func.lower() or 
                             search_term.lower() in lesson.lower()]
            
            if matches:
                renderers[f.stem] = matches
    
    return renderers


def print_renderers(renderers: dict, verbose: bool = False):
    """Imprime los renderers en formato legible."""
    if not renderers:
        print("❌ No se encontraron renderers que coincidan.")
        return
    
    total_funcs = 0
    for renderer, funcs in renderers.items():
        print(f"\n📦 {renderer}")
        for func, lesson in funcs:
            print(f"   • {func}() → {lesson.strip()}")
            total_funcs += 1
    
    print(f"\n✅ Total: {len(renderers)} renderers, {total_funcs} funciones")


def search_for_lesson(lesson_name: str):
    """
    Busca si existe una función para una lección específica.
    
    Args:
        lesson_name: Nombre o parte del nombre de la lección
    """
    renderers = list_renderers(lesson_name)
    
    if renderers:
        print(f"🔍 Encontrado para '{lesson_name}':")
        print_renderers(renderers)
    else:
        print(f"❌ No existe renderer para '{lesson_name}'")
        print("\n💡 Opciones:")
        print("   1. Copiar scripts/geometry/renderer_template.py")
        print("   2. Importar de core/ (OBLIGATORIO)")
        print("   3. Crear las funciones necesarias")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Descubre renderers disponibles y sus capacidades"
    )
    parser.add_argument(
        "--search", "-s",
        help="Buscar por término (nombre de lección o función)"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Listar todos los renderers"
    )
    args = parser.parse_args()
    
    if args.search:
        search_for_lesson(args.search)
    else:
        renderers = list_renderers()
        print_renderers(renderers)

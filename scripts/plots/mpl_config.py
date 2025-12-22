"""
🎨 Matplotlib Configuration - Puente entre los colores del proyecto y Matplotlib

⚠️ DEPRECADO: Este módulo está obsoleto.
   Usar MathPlotter en su lugar: scripts/geometry/core/plotter.py
   
   MathPlotter genera SVG nativo con el estilo exacto de Ediprofe,
   sin dependencias externas como Matplotlib.
   
   Ver: .agent/workflows/mathplotter-spec.md

---
CÓDIGO LEGACY (mantener solo para referencia):

Uso:
    import matplotlib.pyplot as plt
    from scripts.plots.mpl_config import setup_style, style_axis, COLORS
    
    setup_style()
    fig, ax = plt.subplots()
    ...
    style_axis(ax)
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl

# Importar colores del core
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

from geometry.core.colors import COLORS

def setup_style():
    """Configura el estilo de Matplotlib para coincidir con el diseño del sitio."""
    
    # Resetear a defaults primero
    mpl.rcdefaults()
    
    # Configuración base limpia
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Colores
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=[
        COLORS['primary'],
        COLORS['secondary'],
        COLORS['accent'],
        COLORS['highlight'],
        COLORS['purple'],
        COLORS['teal']
    ])
    
    # Fuentes - Priorizar Inter
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'Arial', 'sans-serif']
    mpl.rcParams['font.size'] = 11
    mpl.rcParams['axes.titlesize'] = 14
    mpl.rcParams['axes.labelsize'] = 11
    
    # Ejes y Grid - Más sutiles
    mpl.rcParams['axes.edgecolor'] = '#cbd5e1' # Slate 300
    mpl.rcParams['axes.linewidth'] = 1.5
    mpl.rcParams['axes.labelcolor'] = '#475569' # Slate 600
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.right'] = False
    
    mpl.rcParams['xtick.color'] = '#64748b' # Slate 500
    mpl.rcParams['ytick.color'] = '#64748b' # Slate 500
    mpl.rcParams['xtick.labelsize'] = 10
    mpl.rcParams['ytick.labelsize'] = 10
    
    mpl.rcParams['grid.color'] = '#e2e8f0' # Slate 200
    mpl.rcParams['grid.linestyle'] = '--'
    mpl.rcParams['grid.linewidth'] = 1
    mpl.rcParams['grid.alpha'] = 0.6
    
    # Fondo transparente
    mpl.rcParams['figure.facecolor'] = 'none'
    mpl.rcParams['axes.facecolor'] = 'none'
    
    # Líneas y Marcadores - Más gruesos y visibles
    mpl.rcParams['lines.linewidth'] = 2.5
    mpl.rcParams['lines.markersize'] = 7
    mpl.rcParams['lines.markeredgewidth'] = 2
    
    # Leyenda
    mpl.rcParams['legend.frameon'] = True
    mpl.rcParams['legend.framealpha'] = 0.9
    mpl.rcParams['legend.facecolor'] = 'white'
    mpl.rcParams['legend.edgecolor'] = '#e2e8f0'
    mpl.rcParams['legend.fontsize'] = 10

def style_axis(ax, x_label='x', y_label='y', show_grid=True):
    """
    Aplica estilos adicionales a un eje específico para que parezca una ilustración matemática.
    - Centra los ejes en (0,0) si es apropiado
    - Añade flechas a los ejes
    """
    # Eliminar spines innecesarios
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Color de spines
    ax.spines['left'].set_color('#94a3b8')
    ax.spines['bottom'].set_color('#94a3b8')
    
    # Grid
    ax.grid(show_grid, linestyle='--', alpha=0.5)
    
    # Etiquetas
    ax.set_xlabel(x_label, color='#475569', loc='right')
    ax.set_ylabel(y_label, color='#475569', loc='top', rotation=0)

def save_plot(filename, subdir='estadistica'):
    """Guarda el plot actual en la carpeta correcta."""
    output_dir = PROJECT_ROOT / 'public' / 'images' / subdir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / filename
    plt.savefig(output_path, bbox_inches='tight', transparent=True, dpi=150)
    print(f"✅ Gráfico guardado en: {output_path}")

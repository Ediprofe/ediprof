#!/usr/bin/env python3
"""
🧪 Demo de Capacidades Matplotlib vs Custom Renderers

⚠️ DEPRECADO: Este script fue un experimento.
   El resultado: Matplotlib NO es adecuado para Ediprofe (estilo "académico" no compatible).
   
   USAR EN SU LUGAR: MathPlotter
   - Módulo: scripts/geometry/core/plotter.py
   - Workflow: .agent/workflows/mathplotter-spec.md
   - Ejemplos: scripts/plots/sistemas_ecuaciones.py, ejemplo_histograma.py

---
CÓDIGO LEGACY (mantener solo para referencia histórica):
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_config import setup_style, save_plot

# Configurar estilo global
setup_style()

def demo_funcion_matematica():
    """Caso de uso 1: Gráficas de Funciones (Cálculo/Álgebra)"""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    x = np.linspace(-3, 3, 200)
    y = x**2
    
    # Función principal
    ax.plot(x, y, label=r'$f(x) = x^2$')
    
    # Tangente en x=1
    # f'(x) = 2x -> f'(1) = 2. Punto (1, 1). y - 1 = 2(x - 1) -> y = 2x - 1
    y_tan = 2*x - 1
    ax.plot(x, y_tan, linestyle='--', label='Tangente en $x=1$')
    
    # Punto de tangencia
    ax.plot([1], [1], 'o', color='red', zorder=5)
    ax.annotate('P(1,1)', xy=(1, 1), xytext=(1.5, 0.5),
                arrowprops=dict(facecolor='black', arrowstyle='->'))

    ax.set_title('Análisis de Funciones')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    save_plot('demo-funcion.svg', subdir='pruebas')

def demo_estadistica():
    """Caso de uso 2: Estadística y Datos"""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [23, 45, 56, 78, 32]
    
    # Gráfico de barras con colores del tema
    bars = ax.bar(categorias, valores, alpha=0.8)
    
    # Colorear barras individualmente usando el ciclo de colores
    from mpl_config import COLORS
    colores = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['purple'], COLORS['teal']]
    for bar, color in zip(bars, colores):
        bar.set_color(color)
    
    ax.set_title('Resultados Experimentales')
    ax.set_ylabel('Frecuencia')
    
    # Añadir valores sobre las barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}',
                ha='center', va='bottom')
                
    save_plot('demo-estadistica.svg', subdir='pruebas')

def demo_fisica_simple():
    """Caso de uso 3: Física (Cinemática)"""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    t = np.linspace(0, 10, 100)
    # Movimiento armónico amortiguado
    x = np.exp(-0.1*t) * np.cos(2*np.pi*t)
    
    ax.plot(t, x, color=plt.rcParams['axes.prop_cycle'].by_key()['color'][3]) # Usar color 'highlight'
    
    ax.set_title('Oscilador Armónico Amortiguado')
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Posición (m)')
    
    # Rellenar área bajo la curva
    ax.fill_between(t, x, alpha=0.1)
    
    save_plot('demo-fisica.svg', subdir='pruebas')

if __name__ == "__main__":
    print("Generando demos...")
    demo_funcion_matematica()
    demo_estadistica()
    demo_fisica_simple()
    print("¡Demos generados en public/images/pruebas/!")

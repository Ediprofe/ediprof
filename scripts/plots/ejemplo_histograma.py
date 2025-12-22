import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/funciones/estadistica"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_histograma_pesos():
    # Datos: Pesos de estudiantes
    # Intervalos ajustados para que sean contiguos (52-59, 59-66, etc.)
    intervals = [
        (52, 59), (59, 66), (66, 73), 
        (73, 80), (80, 87), (87, 94)
    ]
    freqs = [7, 8, 9, 8, 4, 4]
    
    # Definimos los ticks exactos que queremos en el eje X (los límites de los intervalos)
    ticks_x = [52, 59, 66, 73, 80, 87, 94]
    
    plot = MathPlotter(
        width=600, height=400,
        x_range=(50, 96),
        y_range=(0, 12),
        title="Distribución de Pesos (kg)",
        show_grid=True,
        show_axes=True,
        custom_x_ticks=ticks_x  # Usamos ticks personalizados
    )
    
    # Activamos show_values=True para ver la frecuencia encima de cada barra
    plot.histogram(intervals, freqs, color='primary', show_values=True)
    
    plot.save(f"{OUTPUT_DIR}/histograma-pesos.svg")

def generar_formas():
    # Configuración común para formas abstractas
    common_cfg = {
        'width': 400, 'height': 300,
        'x_range': (0, 8), 'y_range': (0, 16),
        'show_grid': False, 'show_axes': True
    }
    
    # 1. Simétrica
    p1 = MathPlotter(title="Simétrica (Campana)", **common_cfg)
    p1.histogram(
        [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], 
        [2, 8, 14, 14, 8, 2], 
        color='secondary'
    )
    p1.save(f"{OUTPUT_DIR}/distribucion-simetrica.svg")
    
    # 2. Sesgada Derecha
    p2 = MathPlotter(title="Sesgada a la Derecha", **common_cfg)
    p2.histogram(
        [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], 
        [14, 10, 6, 4, 2, 1], 
        color='accent'
    )
    p2.save(f"{OUTPUT_DIR}/distribucion-sesgada-derecha.svg")
    
    # 3. Sesgada Izquierda
    p3 = MathPlotter(title="Sesgada a la Izquierda", **common_cfg)
    p3.histogram(
        [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], 
        [1, 2, 4, 6, 10, 14], 
        color='accent'
    )
    p3.save(f"{OUTPUT_DIR}/distribucion-sesgada-izquierda.svg")
    
    # 4. Uniforme
    p4 = MathPlotter(title="Uniforme", **common_cfg)
    p4.histogram(
        [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], 
        [10, 10, 10, 10, 10, 10], 
        color='primary'
    )
    p4.save(f"{OUTPUT_DIR}/distribucion-uniforme.svg")
    
    # 5. Bimodal
    p5 = MathPlotter(title="Bimodal", **common_cfg)
    p5.histogram(
        [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], 
        [5, 10, 5, 2, 5, 10], 
        color='secondary'
    )
    p5.save(f"{OUTPUT_DIR}/distribucion-bimodal.svg")

if __name__ == "__main__":
    generar_histograma_pesos()
    generar_formas()

import sys
import os

# Añadir el directorio raíz al path para importar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

def generar_demo_estadistica():
    output_dir = "public/images/pruebas"
    os.makedirs(output_dir, exist_ok=True)
    
    # Datos de ejemplo
    categorias = ["Ene", "Feb", "Mar", "Abr", "May"]
    valores = [12, 19, 15, 25, 22]
    
    # Crear gráfico
    # Configuramos el rango Y para que quepan los valores (0 a 30)
    # Configuramos el rango X para que quepan las categorías (0 a 6)
    plot = MathPlotter(
        width=600, 
        height=400,
        x_range=(0, 6),
        y_range=(0, 30),
        title="Ventas Mensuales (Demo Nativo)",
        show_grid=False,  # No queremos grid cuadriculado feo
        show_axes=True    # Solo ejes
    )
    
    # Dibujar barras
    plot.bar(categorias, valores, color='secondary')
    
    # Guardar
    output_path = f"{output_dir}/demo_barras_nativa.svg"
    plot.save(output_path)
    print(f"Generado: {output_path}")

if __name__ == "__main__":
    generar_demo_estadistica()
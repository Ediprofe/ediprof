# 📈 MathPlotter Workflow

> **Para:** Gráficos de funciones, estadística, y sistemas de ecuaciones
> **Módulo:** `scripts/geometry/core/plotter.py`

---

## ¿Cuándo usar MathPlotter?

| ✅ SÍ usar | ❌ NO usar |
|-----------|----------|
| Sistemas de ecuaciones lineales | Geometría exacta (circuncentros, etc.) |
| Histogramas con intervalos | Circunferencias y arcos |
| Gráficos de barras | Puntos notables de triángulos |
| Distribuciones estadísticas | Plano cartesiano con mediciones |
| Funciones lineales simples | Big data / miles de puntos |

---

## Flujo de Trabajo

```
1. CREAR script en scripts/plots/{tema}.py
2. IMPORTAR MathPlotter
3. CONFIGURAR el plotter (rangos, título, grid)
4. DIBUJAR con métodos fluidos (.plot, .histogram, .bar, .scatter)
5. GUARDAR en public/images/{materia}/{subtema}/
6. ENLAZAR en markdown: ![Alt](/images/{materia}/{subtema}/nombre.svg)
```

---

## Plantilla Base

```python
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.geometry.core.plotter import MathPlotter

OUTPUT_DIR = "public/images/{materia}/{subtema}"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_grafico():
    plot = MathPlotter(
        width=600,
        height=400,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Mi Gráfico"
    )
    
    # Tu código aquí...
    
    plot.save(f"{OUTPUT_DIR}/nombre.svg")

if __name__ == "__main__":
    generar_grafico()
```

---

## Ejemplos por Tipo

### Funciones Lineales (Sistemas de Ecuaciones)

```python
plot = MathPlotter(
    x_range=(-1, 6), y_range=(-1, 6),
    title="Sistema Determinado"
)

plot.plot(lambda x: 4 - x, "x + y = 4", "primary")
plot.plot(lambda x: 2*x - 2, "2x - y = 2", "secondary", dashed=True)
plot.scatter(2, 2, "(2, 2)", "accent")
plot.add_legend()
plot.save("sistema.svg")
```

### Histograma Didáctico

```python
intervals = [(52, 59), (59, 66), (66, 73)]
freqs = [7, 8, 9]
ticks = [52, 59, 66, 73]  # Límites de clase

plot = MathPlotter(
    x_range=(50, 75), y_range=(0, 12),
    title="Distribución de Pesos",
    custom_x_ticks=ticks
)

plot.histogram(intervals, freqs, show_values=True)
plot.save("histograma.svg")
```

### Gráfico de Barras

```python
plot = MathPlotter(
    x_range=(0, 5), y_range=(0, 30),
    show_grid=False, show_axes=True,
    title="Ventas Mensuales"
)

plot.bar(["Ene", "Feb", "Mar", "Abr"], [12, 19, 15, 25], color='secondary')
plot.save("barras.svg")
```

### Distribuciones Estadísticas

```python
common_cfg = {
    'width': 400, 'height': 300,
    'x_range': (0, 8), 'y_range': (0, 16),
    'show_grid': False, 'show_axes': True
}

# Simétrica (Campana)
p1 = MathPlotter(title="Simétrica", **common_cfg)
p1.histogram([(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], [2, 8, 14, 14, 8, 2])
p1.save("simetrica.svg")

# Sesgada derecha
p2 = MathPlotter(title="Sesgada Derecha", **common_cfg)
p2.histogram([(1,2), (2,3), (3,4), (4,5), (5,6), (6,7)], [14, 10, 6, 4, 2, 1])
p2.save("sesgada-derecha.svg")
```

---

## Estándares de Texto Matemático

> **REGLA:** En títulos, etiquetas de ejes y leyendas, **NUNCA** usar el símbolo `^` para exponentes. Usar caracteres Unicode.

| Entrada | Salida Visual | Correcto (Python string) | Incorrecto |
|---|---|---|---|
| `x^2` | $x^2$ | `"x²"` | `"x^2"` |
| `x^3` | $x^3$ | `"x³"` | `"x^3"` |
| `2^x` | $2^x$ | `"2ˣ"` | `"2^x"` |
| `e^x` | $e^x$ | `"eˣ"` | `"e^x"` |
| `t^-1` | $t^{-1}$ | `"t⁻¹"` | `"t^-1"` |
| `0.5^x` | $(0.5)^x$ | `"(0.5)ˣ"` | `"(0.5)^x"` |

**Nota:** Si el exponente es complejo (ej: $x+1$), simplificar la etiqueta o usar texto descriptivo, pero evitar `2^(x+1)` visualmente.

---

## API Completa

### Constructor

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `width` | int | 600 | Ancho del SVG |
| `height` | int | 500 | Alto del SVG |
| `x_range` | tuple | (-6, 6) | Rango matemático eje X |
| `y_range` | tuple | (-5, 5) | Rango matemático eje Y |
| `title` | str | None | Título del gráfico |
| `show_grid` | bool | True | Mostrar cuadrícula |
| `show_axes` | bool | True | Mostrar ejes |
| `grid_step` | float | 1 | Paso general de cuadrícula |
| `grid_step_x` | float | None | Paso específico eje X |
| `grid_step_y` | float | None | Paso específico eje Y |
| `custom_x_ticks` | list | None | Ticks personalizados X |
| `custom_y_ticks` | list | None | Ticks personalizados Y |

### Métodos

| Método | Retorna | Descripción |
|--------|---------|-------------|
| `.plot(func, label, color, width, dashed)` | self | Dibuja función |
| `.scatter(x, y, label, color)` | self | Dibuja punto |
| `.bar(categories, values, color, width)` | self | Barras |
| `.histogram(intervals, freqs, color, show_values)` | self | Histograma |
| `.add_legend()` | self | Leyenda automática |
| `.save(filepath)` | None | Guarda SVG |

### Colores

```python
'primary'   # #3b82f6 - Azul (líneas principales)
'secondary' # #22c55e - Verde (líneas secundarias)
'accent'    # #ef4444 - Rojo (puntos, intersecciones)
'highlight' # #f97316 - Naranja
'purple'    # #8b5cf6 - Púrpura
```

---

## Checklist

- [ ] ¿Creé el script en `scripts/plots/`?
- [ ] ¿Usé colores de la paleta (`'primary'`, etc.)?
- [ ] ¿Usé Unicode para exponentes (x², 2ˣ) en lugar de ^?
- [ ] ¿Los rangos cubren todos los datos?
- [ ] ¿Usé `custom_x_ticks` si los números se amontonan?
- [ ] ¿Guardé en la carpeta correcta (`public/images/{materia}/`)?
- [ ] ¿Enlacé con path relativo en markdown?

---

## Ejecutar

```bash
# Desde la raíz del proyecto
.venv/bin/python scripts/plots/mi_script.py
```

---

## Referencia Rápida

```python
# Import
from scripts.geometry.core.plotter import MathPlotter

# Crear y configurar
plot = MathPlotter(x_range=(...), y_range=(...), title="...")

# Dibujar (encadenable)
plot.plot(...).scatter(...).add_legend()

# Guardar
plot.save("output.svg")
```

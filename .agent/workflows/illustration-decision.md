---
description: Árbol de decisión simplificado para elegir tecnología de ilustración globs: ["src/content/**/*.md"]
---

# 🌳 Workflow: Decisión de Ilustraciones (SIMPLIFICADO)

Este documento ayuda a elegir la **tecnología correcta** para cada tipo de ilustración.

---

## 🔑 Sistema Unificado: GraphSpec

> **GraphSpec** unifica todas las gráficas (funciones, datos, estadísticas) en un solo sistema:
> JSON → Python → SVG animado

| Antes | Ahora |
|-------|-------|
| FunctionSpec (funciones) | **GraphSpec** type: `function` |
| ECharts (barras, histogramas) | **GraphSpec** type: `bar`, `histogram` |
| Chart.js (fracciones) | **GraphSpec** type: `pie` |
| ECharts (dispersión) | **GraphSpec** type: `scatter` |

---

## 🌳 Árbol de Decisión

```
¿QUÉ TIPO DE ILUSTRACIÓN NECESITO?
│
├─── 📈 ¿Es una GRÁFICA?
│    │   (funciones, datos, estadísticas, fracciones)
│    │
│    ├── Función matemática (sin, cos, lineal, cuadrática)
│    │   └── GraphSpec type: "function"
│    │
│    ├── Histograma de frecuencias
│    │   └── GraphSpec type: "histogram"
│    │
│    ├── Gráfico de barras
│    │   └── GraphSpec type: "bar"
│    │
│    ├── Fracción como pastel
│    │   └── GraphSpec type: "pie"
│    │
│    └── Puntos dispersos (correlación)
│        └── GraphSpec type: "scatter"
│
├─── 📐 ¿Es GEOMETRÍA con propiedades exactas?
│    │   (perpendiculares, bisectrices, puntos notables)
│    └── GeometrySpec
│
├─── ✏️ ¿Es un DIAGRAMA ilustrativo/conceptual?
│    │   (situaciones físicas, modelos, procesos)
│    └── Rough.js
│
├─── 🎲 ¿Es GEOMETRÍA 3D?
│    └── Three.js
│
└─── 📝 ¿Es solo una FÓRMULA?
     └── LaTeX
```

---

## 📋 Ejemplos por Tipo de GraphSpec

### `type: "function"` - Funciones Matemáticas

| Ejemplo | Por qué GraphSpec |
|---------|-------------------|
| $y = \sin(x)$ | Animación que dibuja la curva |
| $y = \cos(x)$ con máximos marcados | Etiquetas precisas en puntos notables |
| $y = 2x + 3$ | Control total de ejes y grid |
| $y = x^2$ con vértice | Marcadores con coordenadas exactas |
| Comparar $\sin(x)$ vs $2\sin(x)$ | Múltiples funciones con leyenda |

### `type: "bar"` - Gráficos de Barras

| Ejemplo | Por qué GraphSpec |
|---------|-------------------|
| Notas de estudiantes por materia | Animación de crecimiento |
| Comparación de temperaturas | Barras con colores y etiquetas |
| Ventas mensuales | SVG ligero sin JavaScript |

### `type: "histogram"` - Histogramas

| Ejemplo | Por qué GraphSpec |
|---------|-------------------|
| Distribución de edades | Bins con rangos precisos |
| Frecuencias de datos | Animación secuencial |
| Datos agrupados en intervalos | Barras contiguas |

### `type: "pie"` - Gráficos de Pastel

| Ejemplo | Por qué GraphSpec |
|---------|-------------------|
| Fracción 3/4 | Segmentos animados |
| Distribución porcentual | Etiquetas centradas |
| Partes de un todo | Colores por segmento |

### `type: "scatter"` - Dispersión

| Ejemplo | Por qué GraphSpec |
|---------|-------------------|
| Correlación altura vs peso | Puntos animados |
| Datos experimentales | Etiquetas por punto |
| Relación entre variables | Grid y ejes automáticos |

---

## 📋 Ejemplos por Materia

### 🧮 MATEMÁTICAS

| Necesidad | Tecnología | Tipo |
|-----------|------------|------|
| Gráfica de $\sin x$, $\cos x$ | GraphSpec | `function` |
| Histograma de frecuencias | GraphSpec | `histogram` |
| Fracción 3/4 como pastel | GraphSpec | `pie` |
| Baricentro de triángulo | GeometrySpec | - |
| Circuncentro exacto | GeometrySpec | - |
| Mapa conceptual de tipos de números | Rough.js | - |

### 🚀 FÍSICA

| Necesidad | Tecnología | Tipo |
|-----------|------------|------|
| Gráfica posición vs tiempo | GraphSpec | `function` |
| Gráfica velocidad vs tiempo | GraphSpec | `function` |
| Gráfica de MRU (lineal) | GraphSpec | `function` |
| Bloque en plano inclinado | Rough.js | - |
| Diagrama de fuerzas | Rough.js | - |
| Circuito eléctrico | Rough.js | - |

### ⚛️ QUÍMICA

| Necesidad | Tecnología | Tipo |
|-----------|------------|------|
| Gráfica de solubilidad vs temperatura | GraphSpec | `function` |
| Distribución de electrones | GraphSpec | `bar` |
| Modelo atómico de Bohr | Rough.js | - |
| Enlace covalente | Rough.js | - |

### 🌍 CIENCIAS

| Necesidad | Tecnología | Tipo |
|-----------|------------|------|
| Gráfica de población vs tiempo | GraphSpec | `function` |
| Distribución de especies | GraphSpec | `pie` |
| Ciclo del agua | Rough.js | - |
| Cadena alimenticia | Rough.js | - |

---

## 🔧 Comandos Rápidos

### GraphSpec (todas las gráficas)

```bash
# Función matemática
python3 scripts/functions/renderer.py \
  --spec specs/funciones/trigonometria/seno-principal.json \
  --output public/images/funciones/trigonometria/seno-principal.svg

# Histograma
python3 scripts/functions/renderer.py \
  --spec specs/funciones/estadistica/histograma-edades.json \
  --output public/images/funciones/estadistica/histograma-edades.svg

# Pie chart
python3 scripts/functions/renderer.py \
  --spec specs/funciones/fracciones/tres-cuartos.json \
  --output public/images/funciones/fracciones/tres-cuartos.svg
```

### GeometrySpec

```bash
python3 scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --output public/images/geometria/ \
  --verify
```

---

## 🎯 Formato JSON por Tipo

### `function`

```json
{
  "type": "function",
  "metadata": { "id": "sin-x", "title": "y = sin(x)" },
  "canvas": { "width": 800, "height": 400, "padding": 50 },
  "axes": {
    "x": { "min": -6.28, "max": 6.28, "label": "x", "ticks": "pi" },
    "y": { "min": -1.5, "max": 1.5, "label": "y" }
  },
  "functions": [
    { "expression": "sin(x)", "color": "#3b82f6", "strokeWidth": 3 }
  ],
  "markers": [
    { "x": "pi/2", "y": 1, "label": "Máximo", "color": "#ef4444" }
  ]
}
```

### `bar`

```json
{
  "type": "bar",
  "metadata": { "id": "notas", "title": "Notas por Materia" },
  "canvas": { "width": 600, "height": 400 },
  "data": {
    "labels": ["Matemáticas", "Física", "Química"],
    "values": [85, 78, 92],
    "colors": ["#3b82f6", "#ef4444", "#22c55e"]
  }
}
```

### `histogram`

```json
{
  "type": "histogram",
  "metadata": { "id": "edades", "title": "Distribución de Edades" },
  "canvas": { "width": 600, "height": 400 },
  "axes": {
    "x": { "label": "Edad" },
    "y": { "label": "Frecuencia" }
  },
  "data": {
    "bins": [
      { "from": 0, "to": 10, "count": 5 },
      { "from": 10, "to": 20, "count": 15 },
      { "from": 20, "to": 30, "count": 25 }
    ],
    "color": "#3b82f6"
  }
}
```

### `pie`

```json
{
  "type": "pie",
  "metadata": { "id": "fraccion", "title": "Fracción 3/4" },
  "canvas": { "width": 400, "height": 400 },
  "data": {
    "segments": [
      { "value": 3, "label": "3/4", "color": "#3b82f6" },
      { "value": 1, "label": "1/4", "color": "#e2e8f0" }
    ]
  }
}
```

### `scatter`

```json
{
  "type": "scatter",
  "metadata": { "id": "correlacion", "title": "Altura vs Peso" },
  "canvas": { "width": 600, "height": 400 },
  "axes": {
    "x": { "label": "Altura (cm)", "min": 150, "max": 200 },
    "y": { "label": "Peso (kg)", "min": 50, "max": 100 }
  },
  "data": {
    "points": [
      { "x": 160, "y": 55 },
      { "x": 175, "y": 70 },
      { "x": 180, "y": 80 }
    ],
    "color": "#3b82f6",
    "size": 8
  }
}
```

---

## ✅ Resumen Ejecutivo

| Pregúntate | Usa |
|------------|-----|
| ¿Es una función matemática? | **GraphSpec** `function` |
| ¿Es un histograma? | **GraphSpec** `histogram` |
| ¿Es un gráfico de barras? | **GraphSpec** `bar` |
| ¿Es una fracción/porcentaje? | **GraphSpec** `pie` |
| ¿Son puntos dispersos? | **GraphSpec** `scatter` |
| ¿Es geometría con propiedades exactas? | GeometrySpec |
| ¿Es ilustrativo/conceptual? | Rough.js |
| ¿Es 3D? | Three.js |
| ¿Es solo texto matemático? | LaTeX |

---

## 🔧 Renderers Especializados por Tema

Además de los sistemas principales, existen renderers especializados:

| Tema | Renderer | Comando |
|------|----------|---------|
| Círculo unitario | `unit_circle_renderer.py` | `python3 scripts/geometry/unit_circle_renderer.py --type TYPE --output FILE.svg` |
| Identidades trig | `identity_renderer.py` | `python3 scripts/geometry/identity_renderer.py --type TYPE --output FILE.svg` |
| Triángulos trig | `trigonometry_renderer.py` | `python3 scripts/geometry/trigonometry_renderer.py --spec JSON --output FILE.svg` |

### Tipos disponibles:

**unit_circle_renderer.py:**
- `basic` - Círculo unitario con cuadrantes
- `point` - Punto P = (cos θ, sin θ)
- `quadrants` - Signos ASTC
- `reference` - Ángulos de referencia
- `negative` - Ángulos negativos
- `quadrantal` - Ángulos cuadrantales
- `cofunctions` - Cofunciones

**identity_renderer.py:**
- `map` - Mapa de identidades fundamentales
- `pythagorean` - Identidad pitagórica en círculo
- `double` - Fórmulas ángulo doble
- `half` - Fórmulas ángulo mitad
- `proof` - Estrategias de demostración
- `equations` - Soluciones de ecuaciones

### Organización de outputs:

```
public/images/
├── funciones/trigonometria/     # GraphSpec de sin, cos, tan
├── trigonometria/
│   ├── circulo-unitario/        # unit_circle_renderer.py
│   └── identidades/             # identity_renderer.py
└── geometria/trigonometria/     # trigonometry_renderer.py
```

---

## 🔗 Workflows Detallados

- [GraphSpec](./graphspec.md) - **Sistema unificado de gráficas** ⭐
- [GeometrySpec](./geometry-exact.md) - Geometría exacta
- [Rough.js](./roughjs.md) - Diagramas ilustrativos
- [Three.js](./threejs.md) - Geometría 3D

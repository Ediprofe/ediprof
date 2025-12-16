---
description: Sistema unificado de gráficas educativas (GraphSpec → Python → SVG animado) globs: ["specs/funciones/**/*.json", "scripts/functions/**/*.py"]
---

# 📈 Workflow: GraphSpec (Sistema Unificado de Gráficas)

Sistema para generar **todas las gráficas educativas** con animaciones CSS.

---

## 🎯 Principio Fundamental

> **GraphSpec** unifica todos los tipos de gráficas en un solo sistema:
> - ✅ Funciones matemáticas (sin, cos, lineales, cuadráticas)
> - ✅ Histogramas de frecuencias
> - ✅ Gráficos de barras
> - ✅ Pie charts (fracciones)
> - ✅ Scatter plots (dispersión)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  IA genera   │────▶│ Python calcula│───▶│    SVG       │
│  GraphSpec   │     │  y renderiza │     │  animado     │
│   (JSON)     │     │              │     │   (CSS)      │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## 📊 Tipos Disponibles

| Tipo | Uso | Ejemplo |
|------|-----|---------|
| `function` | Funciones matemáticas | $y = \sin(x)$, $y = 2x + 3$ |
| `bar` | Gráficos de barras | Notas por materia |
| `histogram` | Histogramas de frecuencias | Distribución de edades |
| `pie` | Gráficos de pastel | Fracción 3/4 |
| `scatter` | Gráficos de dispersión | Correlación altura-peso |

---

## 🔧 Comando General

```bash
python3 scripts/functions/renderer.py \
  --spec specs/funciones/[ruta]/archivo.json \
  --output public/images/funciones/[ruta]/archivo.svg
```

### Opciones

| Flag | Descripción |
|------|-------------|
| `--spec` | Archivo JSON de especificación |
| `--output` | Archivo SVG de salida |
| `--preview` | Abre en navegador al terminar |
| `--validate-only` | Solo valida sin generar |

---

## 📋 Formato JSON por Tipo

### 1️⃣ `function` - Funciones Matemáticas

```json
{
  "type": "function",
  "metadata": {
    "id": "seno-principal",
    "title": "La Onda del Seno: y = sin(x)",
    "lesson": "04-trigonometria/03-graficas/01-grafica-seno"
  },
  "canvas": {
    "width": 800,
    "height": 400,
    "padding": 55,
    "background": "#f8fafc"
  },
  "axes": {
    "x": {
      "min": -6.28,
      "max": 6.28,
      "label": "x",
      "ticks": "pi"
    },
    "y": {
      "min": -1.5,
      "max": 1.5,
      "label": "y"
    }
  },
  "functions": [
    {
      "id": "sin-x",
      "expression": "sin(x)",
      "color": "#3b82f6",
      "strokeWidth": 3,
      "animation": "draw"
    }
  ],
  "markers": [
    { "x": 0, "y": 0, "label": "Origen (0, 0)", "color": "#374151" },
    { "x": "pi/2", "y": 1, "label": "Máximo (π/2, 1)", "color": "#ef4444" },
    { "x": "pi", "y": 0, "label": "Cruza en π", "color": "#22c55e" }
  ],
  "annotations": [
    {
      "type": "brace",
      "from_x": 0,
      "to_x": "2pi",
      "label": "Período = 2π",
      "color": "#8b5cf6"
    }
  ],
  "animations": {
    "enabled": true,
    "duration": 2,
    "markersDelay": 2
  }
}
```

#### Expresiones Soportadas

| Expresión | Resultado |
|-----------|-----------|
| `sin(x)` | Seno |
| `cos(x)` | Coseno |
| `tan(x)` | Tangente |
| `2*x + 3` | Lineal |
| `x^2` o `x**2` | Cuadrática |
| `sqrt(x)` | Raíz cuadrada |
| `abs(x)` | Valor absoluto |
| `exp(x)` | Exponencial |
| `log(x)` | Logaritmo natural |

#### Valores Especiales

| Valor | Interpretación |
|-------|---------------|
| `"pi"` | π = 3.14159... |
| `"2pi"` o `"2*pi"` | 2π |
| `"pi/2"` | π/2 |
| `"-pi"` | -π |

---

### 2️⃣ `bar` - Gráficos de Barras

```json
{
  "type": "bar",
  "metadata": {
    "id": "notas-materias",
    "title": "Notas por Materia"
  },
  "canvas": {
    "width": 600,
    "height": 400,
    "padding": 60,
    "background": "#f8fafc"
  },
  "data": {
    "labels": ["Matemáticas", "Física", "Química", "Biología"],
    "values": [85, 78, 92, 88],
    "colors": ["#3b82f6", "#ef4444", "#22c55e", "#f97316"]
  },
  "animations": {
    "enabled": true
  }
}
```

#### Animación

Las barras crecen de abajo hacia arriba con delay escalonado.

---

### 3️⃣ `histogram` - Histogramas

```json
{
  "type": "histogram",
  "metadata": {
    "id": "distribucion-edades",
    "title": "Distribución de Edades"
  },
  "canvas": {
    "width": 600,
    "height": 400,
    "padding": 60,
    "background": "#f8fafc"
  },
  "axes": {
    "x": { "label": "Edad (años)" },
    "y": { "label": "Frecuencia" }
  },
  "data": {
    "bins": [
      { "from": 0, "to": 10, "count": 5 },
      { "from": 10, "to": 20, "count": 15 },
      { "from": 20, "to": 30, "count": 25 },
      { "from": 30, "to": 40, "count": 20 },
      { "from": 40, "to": 50, "count": 10 }
    ],
    "color": "#3b82f6"
  },
  "animations": {
    "enabled": true
  }
}
```

#### Estructura de Bins

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `from` | number | Límite inferior del intervalo |
| `to` | number | Límite superior del intervalo |
| `count` | number | Frecuencia (altura de la barra) |

---

### 4️⃣ `pie` - Gráficos de Pastel

```json
{
  "type": "pie",
  "metadata": {
    "id": "fraccion-tres-cuartos",
    "title": "Representación de 3/4"
  },
  "canvas": {
    "width": 400,
    "height": 400,
    "background": "#f8fafc"
  },
  "data": {
    "segments": [
      { "value": 3, "label": "3/4", "color": "#3b82f6" },
      { "value": 1, "label": "1/4", "color": "#e2e8f0" }
    ],
    "showLabels": true
  },
  "animations": {
    "enabled": true
  }
}
```

#### Estructura de Segments

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `value` | number | Proporción del segmento |
| `label` | string | Etiqueta que se muestra |
| `color` | string | Color del segmento (hex) |

---

### 5️⃣ `scatter` - Gráficos de Dispersión

```json
{
  "type": "scatter",
  "metadata": {
    "id": "correlacion-altura-peso",
    "title": "Correlación Altura vs Peso"
  },
  "canvas": {
    "width": 600,
    "height": 400,
    "padding": 60,
    "background": "#f8fafc"
  },
  "axes": {
    "x": { "label": "Altura (cm)", "min": 150, "max": 200 },
    "y": { "label": "Peso (kg)", "min": 40, "max": 100 }
  },
  "data": {
    "points": [
      { "x": 155, "y": 50 },
      { "x": 160, "y": 55, "label": "A" },
      { "x": 165, "y": 58 },
      { "x": 170, "y": 65 },
      { "x": 175, "y": 70, "label": "B" },
      { "x": 180, "y": 78 },
      { "x": 185, "y": 85 },
      { "x": 190, "y": 90, "label": "C" }
    ],
    "color": "#3b82f6",
    "size": 8
  },
  "animations": {
    "enabled": true
  }
}
```

#### Estructura de Points

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `x` | number | Coordenada X |
| `y` | number | Coordenada Y |
| `label` | string | (opcional) Etiqueta del punto |
| `color` | string | (opcional) Color específico del punto |

---

## 🎬 Animaciones CSS

### `function` - Draw Wave

```css
.wave-path {
  stroke-dasharray: 3000;
  stroke-dashoffset: 3000;
  animation: drawWave 2s ease-out forwards;
}
@keyframes drawWave {
  to { stroke-dashoffset: 0; }
}
```

### `bar` / `histogram` - Grow

```css
.bar {
  transform-origin: bottom;
  transform: scaleY(0);
  animation: growBar 0.8s ease-out forwards;
}
@keyframes growBar {
  to { transform: scaleY(1); }
}
```

### `pie` - Pop In

```css
.pie-segment {
  transform: scale(0);
  animation: popIn 0.5s ease-out forwards;
}
@keyframes popIn {
  to { transform: scale(1); }
}
```

### `scatter` - Pop In

```css
.scatter-point {
  transform: scale(0);
  animation: popIn 0.3s ease-out forwards;
}
```

---

## 🎨 Paleta de Colores

### Colores Estándar

| Elemento | Color | Hex |
|----------|-------|-----|
| Principal (azul) | 🔵 | `#3b82f6` |
| Secundario (rojo) | 🔴 | `#ef4444` |
| Terciario (verde) | 🟢 | `#22c55e` |
| Cuaternario (violeta) | 🟣 | `#8b5cf6` |
| Quinario (naranja) | 🟠 | `#f97316` |
| Ejes | ⬛ | `#374151` |
| Grid | ⬜ | `#e2e8f0` |
| Fondo | 🔲 | `#f8fafc` |
| Texto | ⬛ | `#1e293b` |

### Para Series Múltiples

```json
"colors": ["#3b82f6", "#ef4444", "#22c55e", "#f97316", "#8b5cf6", "#ec4899", "#14b8a6", "#f59e0b"]
```

---

## 📁 Estructura de Archivos

```
proyecto/
├── specs/
│   └── funciones/
│       ├── trigonometria/
│       │   ├── seno-principal.json
│       │   ├── seno-simetria.json
│       │   ├── coseno-principal.json
│       │   └── tangente-principal.json
│       ├── algebra/
│       │   ├── lineal-pendiente.json
│       │   └── cuadratica-vertice.json
│       ├── estadistica/
│       │   ├── histograma-edades.json
│       │   └── barras-notas.json
│       └── fracciones/
│           ├── tres-cuartos.json
│           └── un-medio.json
├── scripts/
│   └── functions/
│       └── renderer.py       # Motor unificado
└── public/
    └── images/
        └── funciones/
            ├── trigonometria/
            ├── algebra/
            ├── estadistica/
            └── fracciones/
```

---

## ✅ Checklist

- [ ] `"type"` especificado (`function`, `bar`, `histogram`, `pie`, `scatter`)
- [ ] `metadata.id` único
- [ ] Canvas con dimensiones apropiadas
- [ ] Colores de la paleta estándar
- [ ] Etiquetas en español
- [ ] Ejecutar con `--preview` para verificar
- [ ] Enlazar en markdown: `![Alt](/images/funciones/...)`

---

## ⚠️ Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| SVG en blanco | `"type"` no especificado | Agregar `"type": "function"` (o el tipo correcto) |
| Función cortada | Dominio muy pequeño | Ampliar `axes.x.min/max` |
| Barras no visibles | `values` vacío | Verificar array de datos |
| Pie sin segmentos | `segments` mal formado | Verificar estructura de segmentos |

---

## 📝 Ejemplos de Uso

### En Markdown

```markdown
## La función seno

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem;">Gráfica de y = sin(x)</strong>
  </div>
  <img src="/images/funciones/trigonometria/seno-principal.svg" alt="Gráfica del seno" style="width: 100%; height: auto;"/>
</div>
```

### Alternativa Simple

```markdown
![Gráfica de y = sin(x)](/images/funciones/trigonometria/seno-principal.svg)
```

---

## 🔗 Relacionados

- [Árbol de decisión](./illustration-decision.md)
- [GeometrySpec](./geometry-exact.md) - Para geometría exacta
- [Rough.js](./roughjs.md) - Para diagramas ilustrativos


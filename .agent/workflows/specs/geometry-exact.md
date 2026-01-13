---
description: Sistema de geometría exacta con validación matemática (GeometrySpec → Python → SVG) globs: ["specs/geometria/**/*.json", "scripts/geometry/**/*.py"]
---

# 📐 Workflow: Geometría Exacta (GeometrySpec)

Sistema para generar ilustraciones geométricas **matemáticamente perfectas** usando especificaciones declarativas.

---

## 🎯 Principio Fundamental

> **La IA NO dibuja.** La IA genera una especificación JSON que describe QUÉ construir.
> **SymPy calcula.** Las coordenadas se calculan con álgebra simbólica exacta.
> **El renderer dibuja.** SVG vectorial preciso y validado.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  IA genera   │────▶│ Python/SymPy │────▶│    SVG       │
│ GeometrySpec │     │   calcula    │     │   exacto     │
│   (JSON)     │     │ y valida     │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## ✅ Cuándo usar GeometrySpec

| Caso de uso | Usar GeometrySpec |
|-------------|-------------------|
| Baricentro, ortocentro, circuncentro, incentro | ✅ OBLIGATORIO |
| Medianas, alturas, bisectrices, mediatrices | ✅ OBLIGATORIO |
| Circunferencia inscrita/circunscrita | ✅ OBLIGATORIO |
| Perpendicularidad exacta | ✅ OBLIGATORIO |
| Paralelismo exacto | ✅ OBLIGATORIO |
| Recta de Euler | ✅ OBLIGATORIO |
| Teoremas geométricos (propiedad que debe cumplirse) | ✅ OBLIGATORIO |

### ❌ NO usar GeometrySpec para:

- Gráficas de funciones → CartesianSpec / MathPlotter
- Diagramas ilustrativos → PNG de tablet (ver CLAUDE.md)
- Geometría 3D → No soportado actualmente
- Figuras sin propiedades exactas → PNG de tablet

---

## 📋 Formato GeometrySpec

### Estructura básica

```json
{
  "metadata": {
    "id": "identificador-unico",
    "title": "Título descriptivo",
    "lesson": "ruta/de/la/leccion"
  },
  "canvas": {
    "width": 500,
    "height": 400,
    "padding": 40
  },
  "construction": {
    "type": "triangle_notable_points",
    "base": {
      "A": [50, 350],
      "B": [450, 350],
      "C": [250, 50]
    },
    "compute": ["baricentro", "medianas"],
    "show": {
      "triangle": true,
      "vertices_labels": true,
      "medianas": { "color": "#22c55e", "style": "dashed" },
      "baricentro": { "label": "G", "color": "#ef4444" }
    }
  },
  "assertions": [
    { "property": "concurrent", "elements": ["mediana_A", "mediana_B", "mediana_C"] },
    { "property": "ratio", "value": 2, "from": "A", "through": "G", "to": "Ma" }
  ]
}
```

---

## 🏗️ Tipos de Construcción

### `triangle_notable_points`

Calcula puntos notables de un triángulo.

```json
{
  "type": "triangle_notable_points",
  "base": { "A": [x, y], "B": [x, y], "C": [x, y] },
  "compute": ["baricentro", "ortocentro", "circuncentro", "incentro"],
  "show": {
    "triangle": true,
    "baricentro": { "label": "G", "color": "#ef4444" }
  }
}
```

**Opciones de `compute`:**
- `baricentro` - Intersección de medianas
- `ortocentro` - Intersección de alturas
- `circuncentro` - Intersección de mediatrices
- `incentro` - Intersección de bisectrices

### `triangle_medians`

Dibuja las medianas de un triángulo.

```json
{
  "type": "triangle_medians",
  "base": { "A": [x, y], "B": [x, y], "C": [x, y] },
  "compute": ["medianas", "puntos_medios"],
  "show": {
    "medianas": { "color": "#22c55e", "style": "dashed" },
    "puntos_medios": { "labels": ["Ma", "Mb", "Mc"] }
  }
}
```

### `triangle_altitudes`

Dibuja las alturas de un triángulo.

```json
{
  "type": "triangle_altitudes",
  "base": { "A": [x, y], "B": [x, y], "C": [x, y] },
  "compute": ["alturas", "pies_altura"],
  "show": {
    "alturas": { "color": "#f97316", "style": "dashed" },
    "right_angle_marks": true
  }
}
```

### `triangle_bisectors`

Dibuja las bisectrices y círculo inscrito.

```json
{
  "type": "triangle_bisectors",
  "base": { "A": [x, y], "B": [x, y], "C": [x, y] },
  "compute": ["bisectrices", "incentro", "circunferencia_inscrita"],
  "show": {
    "bisectrices": { "color": "#8b5cf6", "style": "dashed" },
    "circunferencia_inscrita": { "color": "#8b5cf6", "fill": "rgba(139, 92, 246, 0.1)" }
  }
}
```

### `triangle_perpendicular_bisectors`

Dibuja las mediatrices y círculo circunscrito.

```json
{
  "type": "triangle_perpendicular_bisectors",
  "base": { "A": [x, y], "B": [x, y], "C": [x, y] },
  "compute": ["mediatrices", "circuncentro", "circunferencia_circunscrita"],
  "show": {
    "mediatrices": { "color": "#ec4899", "style": "dashed" },
    "circunferencia_circunscrita": { "color": "#ec4899" }
  }
}
```

### `triangle_euler_line`

Dibuja la recta de Euler.

```json
{
  "type": "triangle_euler_line",
  "base": { "A": [x, y], "B": [x, y], "C": [x, y] },
  "compute": ["baricentro", "ortocentro", "circuncentro", "recta_euler"],
  "show": {
    "recta_euler": { "color": "#0ea5e9", "style": "solid", "width": 2 },
    "baricentro": { "label": "G" },
    "ortocentro": { "label": "H" },
    "circuncentro": { "label": "O" }
  }
}
```

---

## 🔧 Comandos

### Generar SVG

```bash
python scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --output public/images/geometria/triangulos/baricentro.svg
```

### Generar con validación (RECOMENDADO)

```bash
python scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --output public/images/geometria/triangulos/baricentro.svg \
  --verify
```

### Validar sin generar

```bash
python scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --validate-only
```

---

## 📁 Estructura de Archivos

```
proyecto/
├── specs/
│   └── geometria/
│       ├── triangulos/
│       │   ├── baricentro.json
│       │   ├── ortocentro.json
│       │   ├── circuncentro.json
│       │   ├── incentro.json
│       │   └── euler.json
│       ├── cuadrilateros/
│       └── circulos/
├── scripts/
│   └── geometry/
│       ├── renderer.py          # Motor principal
│       ├── verifier.py          # Validador matemático
│       └── primitives/
│           ├── triangle.py
│           └── circle.py
└── public/
    └── images/
        └── geometria/
            └── triangulos/
                └── baricentro.svg
```

---

## 🎨 Paleta de Colores Estándar

| Elemento | Color | Hex |
|----------|-------|-----|
| Medianas | Verde | `#22c55e` |
| Alturas | Naranja | `#f97316` |
| Bisectrices | Violeta | `#8b5cf6` |
| Mediatrices | Rosa | `#ec4899` |
| Puntos notables | Rojo | `#ef4444` |
| Recta de Euler | Cyan | `#0ea5e9` |
| Vértices | Gris oscuro | `#1e293b` |
| Triángulo (fill) | Gris claro | `#f1f5f9` |
| Triángulo (stroke) | Negro | `#1e293b` |

---

## ✅ Checklist

- [ ] Spec JSON válido (usar schema para validar)
- [ ] Coordenadas en píxeles (no coordenadas matemáticas)
- [ ] Canvas con padding suficiente (40px mínimo)
- [ ] Tipo de construcción correcto
- [ ] `compute` incluye lo necesario
- [ ] `show` configura visualización
- [ ] Ejecutar con `--verify`
- [ ] Enlazar SVG en markdown: `![Alt](/images/geometria/...)`

---

## ⚠️ Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Triángulo fuera de canvas | Coordenadas > canvas size | Ajustar coordenadas o canvas |
| Validación falla | Propiedad matemática no cumplida | Revisar spec, posible bug en renderer |
| SVG vacío | JSON mal formado | Validar JSON contra schema |
| Punto invisible | Fuera del viewport | Ajustar boundingbox |

---

## 📝 Ejemplo Completo

### 1. Crear spec

`specs/geometria/triangulos/baricentro-ejemplo.json`:

```json
{
  "metadata": {
    "id": "baricentro-leccion-01",
    "title": "Baricentro de un triángulo",
    "lesson": "03-geometria/04-triangulos/puntos-notables"
  },
  "canvas": {
    "width": 500,
    "height": 400,
    "padding": 40
  },
  "construction": {
    "type": "triangle_notable_points",
    "base": {
      "A": [50, 350],
      "B": [450, 350],
      "C": [250, 50]
    },
    "compute": ["baricentro", "medianas", "puntos_medios"],
    "show": {
      "triangle": { "fill": "#f8fafc", "stroke": "#1e293b", "strokeWidth": 2 },
      "vertices_labels": { "A": "A", "B": "B", "C": "C" },
      "medianas": { "color": "#22c55e", "style": "dashed", "width": 2 },
      "puntos_medios": { 
        "color": "#94a3b8", 
        "labels": { "Ma": "Mₐ", "Mb": "M_b", "Mc": "M_c" }
      },
      "baricentro": { "label": "G", "color": "#ef4444", "size": 6 }
    }
  },
  "assertions": [
    { "property": "concurrent", "elements": ["mediana_A", "mediana_B", "mediana_C"] },
    { "property": "ratio", "value": 2, "from": "A", "through": "G", "to": "Ma" }
  ]
}
```

### 2. Ejecutar renderer

```bash
python scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro-ejemplo.json \
  --output public/images/geometria/triangulos/baricentro-ejemplo.svg \
  --verify
```

### 3. Usar en markdown

```markdown
## El Baricentro

El baricentro G es la intersección de las medianas.

![Baricentro del triángulo](/images/geometria/triangulos/baricentro-ejemplo.svg)

Las coordenadas del baricentro se calculan como:

$$
G = \left( \frac{x_A + x_B + x_C}{3}, \frac{y_A + y_B + y_C}{3} \right)
$$
```

---

## 🔗 Relacionados

- [Árbol de decisión](../CLAUDE.md#-árbol-de-decisión)
- [ECharts](./echarts.md) - Para funciones (NO geometría)
- [Rough.js](./roughjs.md) - Para diagramas ilustrativos
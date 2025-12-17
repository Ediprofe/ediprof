---
description: Sistema de geometría exacta para circunferencias (CircleSpec → Python/SymPy → SVG)
globs: ["specs/geometria/circulos/**/*.json", "scripts/geometry/circle_spec_renderer.py"]
---

# 📐 Workflow: CircleSpec - Geometría Exacta para Circunferencias

Sistema para generar ilustraciones de circunferencias **matemáticamente perfectas** usando especificaciones declarativas JSON.

---

## 🎯 Principio Fundamental

> **La IA NO dibuja.** La IA genera una especificación JSON que describe QUÉ construir.
> **SymPy calcula.** Las coordenadas se calculan con precisión matemática.
> **El renderer dibuja.** SVG vectorial validado y consistente.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  IA genera   │────▶│ Python/SymPy │────▶│    SVG       │
│ CircleSpec   │     │   calcula    │     │   exacto     │
│   (JSON)     │     │ y valida     │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## ✅ Cuándo usar CircleSpec

| Caso de uso | Usar CircleSpec |
|-------------|-----------------|
| Radio, diámetro, cuerda | ✅ OBLIGATORIO |
| Arco, sector, segmento circular | ✅ OBLIGATORIO |
| Corona circular | ✅ OBLIGATORIO |
| Posiciones de un punto | ✅ OBLIGATORIO |
| Posiciones entre circunferencias | ✅ OBLIGATORIO |
| Ángulos en la circunferencia | ✅ OBLIGATORIO |
| Teoremas de circunferencia | ✅ OBLIGATORIO |
| Fórmulas de área/longitud | ✅ OBLIGATORIO |

### ❌ NO usar CircleSpec para:

- Gráficas de funciones trigonométricas → ECharts
- Diagramas ilustrativos sin precisión → Rough.js
- Geometría 3D → Three.js

---

## 📋 Formato CircleSpec

### Estructura básica

```json
{
  "tipo": "elemento-radio",
  "titulo": "Radio",
  "titulo_color": "#ef4444",
  "canvas": "simple",
  "circunferencia": {
    "centro": [250, 175],
    "radio": 110
  },
  "elemento": {
    "angulo": 45,
    "color": "#ef4444",
    "etiqueta": "r"
  },
  "leyenda": {
    "texto": "Segmento del centro a la circunferencia",
    "color": "#ef4444",
    "bg_color": "#fee2e2"
  }
}
```

---

## 🎨 Canvas Presets

En lugar de especificar dimensiones manualmente, usar presets:

| Preset | Dimensiones | Uso |
|--------|-------------|-----|
| `"simple"` | 500×400 | 1 concepto (radio, cuerda, arco) |
| `"compound"` | 600×460 | 2-3 elementos (teoremas, comparaciones) |
| `"multiple"` | 750×450 | 4+ elementos (posiciones múltiples) |
| `"horizontal"` | 750×420 | Operaciones lado a lado (A - B = C) |

```json
{
  "canvas": "simple"
}
```

O especificar manualmente:

```json
{
  "canvas": {
    "width": 600,
    "height": 450,
    "padding": 40
  }
}
```

---

## 🏗️ Tipos de Especificación

### `elemento-radio`

```json
{
  "tipo": "elemento-radio",
  "elemento": {
    "angulo": 45,
    "color": "#ef4444",
    "etiqueta": "r"
  }
}
```

### `elemento-cuerda`

```json
{
  "tipo": "elemento-cuerda",
  "elemento": {
    "angulo1": 120,
    "angulo2": 30,
    "color": "#22c55e"
  }
}
```

### `elemento-sector`

```json
{
  "tipo": "elemento-sector",
  "elemento": {
    "angulo1": 90,
    "angulo2": 20,
    "color": "#8b5cf6",
    "fill": "#ede9fe"
  }
}
```

### `posiciones-punto`

```json
{
  "tipo": "posiciones-punto",
  "canvas": "horizontal",
  "posiciones": [
    {"tipo": "interior", "etiqueta": "Interior", "formula": "d < r"},
    {"tipo": "sobre", "etiqueta": "Sobre la circ.", "formula": "d = r"},
    {"tipo": "exterior", "etiqueta": "Exterior", "formula": "d > r"}
  ]
}
```

---

## 🔧 Comandos

### Generar SVG desde spec

```bash
python3 scripts/geometry/circle_spec_renderer.py \
  --spec specs/geometria/circulos/01-elemento-radio.json \
  --output public/images/geometria/circulos/elemento-radio.svg
```

### Validar spec sin generar

```bash
python3 scripts/geometry/circle_spec_renderer.py \
  --spec specs/geometria/circulos/01-elemento-radio.json \
  --validate-only
```

### Procesar directorio completo (batch)

```bash
python3 scripts/geometry/circle_spec_renderer.py \
  --batch specs/geometria/circulos/
```

---

## 📁 Estructura de Archivos

```
proyecto/
├── specs/
│   └── geometria/
│       └── circulos/
│           ├── 01-elemento-radio.json
│           ├── 02-elemento-cuerda.json
│           ├── 03-elemento-sector.json
│           └── 04-posiciones-punto.json
├── scripts/
│   └── geometry/
│       ├── circle_spec_renderer.py    # Motor principal
│       └── circle_renderer.py         # Renderer legacy (funciones hardcodeadas)
└── public/
    └── images/
        └── geometria/
            └── circulos/
                └── *.svg
```

---

## 🎨 Paleta de Colores Estándar

| Elemento | Color | Hex |
|----------|-------|-----|
| Radio | Rojo | `#ef4444` |
| Diámetro | Violeta | `#8b5cf6` |
| Cuerda | Verde | `#22c55e` |
| Arco | Naranja | `#f97316` |
| Sector (fill) | Verde claro | `#dcfce7` |
| Segmento (fill) | Amarillo claro | `#fef3c7` |
| Tangente | Rosa | `#ec4899` |
| Secante | Teal | `#14b8a6` |
| Centro | Rojo | `#ef4444` |
| Circunferencia | Azul | `#3b82f6` |

---

## ✅ Garantías Automáticas

El renderer garantiza automáticamente:

1. **Escape de caracteres XML** - `<`, `>`, `&` se escapan en todo el texto
2. **Centrado correcto** - Los elementos se centran según el canvas
3. **viewBox consistente** - Según el preset seleccionado
4. **Cálculos exactos** - SymPy para coordenadas matemáticas
5. **Validación de bounds** - Advertencias si elementos están cerca del borde

---

## ✅ Checklist para Agente IA

Cuando se pida "genera las ilustraciones de circunferencia":

1. **Identificar** qué elementos necesita la lección
2. **Crear spec JSON** en `specs/geometria/circulos/`
3. **Ejecutar renderer**:
   ```bash
   python3 scripts/geometry/circle_spec_renderer.py --spec SPEC.json --output OUTPUT.svg
   ```
4. **Verificar** que el SVG se genera sin errores
5. **Insertar en markdown**:
   ```markdown
   ![Descripción](/images/geometria/circulos/nombre.svg)
   ```

---

## ⚠️ Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| "Campo requerido faltante" | Falta `tipo` o `canvas` | Agregar campos obligatorios |
| "Canvas preset no existe" | Nombre de preset incorrecto | Usar: simple, compound, multiple, horizontal |
| Elemento fuera del canvas | Coordenadas muy grandes | Ajustar ángulos o usar canvas más grande |
| Texto cortado | Leyenda muy larga | Reducir texto o aumentar altura del canvas |

---

## 🔗 Relacionados

- [Árbol de decisión](../CLAUDE.md#-árbol-de-decisión)
- [GeometrySpec para triángulos](./geometry-exact.md)
- [ECharts para funciones](./echarts.md)

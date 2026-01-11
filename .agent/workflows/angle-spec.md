---
description: Sistema para generar ilustraciones de ángulos exactas (AngleSpec → Python → SVG)
globs: ["specs/geometria/angulos/*.json", "scripts/geometry/angle_renderer.py"]
---

# 📐 Workflow: AngleSpec (Ángulos Exactos)

Sistema para generar ilustraciones de ángulos **con precisión trigonométrica** y **cero espacio en blanco innecesario**.

---

## 🚨 REGLAS CRÍTICAS PARA AGENTES IA

> **ESTAS REGLAS SON OBLIGATORIAS. SI NO LAS SIGUES, LAS ILUSTRACIONES QUEDARÁN MAL.**

### ✅ LO QUE SÍ DEBES HACER

1. **Solo definir QUÉ dibujar** → El renderer calcula DÓNDE automáticamente
2. **Usar ángulos en grados** → No coordenadas absolutas
3. **Ejecutar el renderer** → `python3 scripts/geometry/angle_renderer.py --spec ...`
4. **Verificar visualmente** → Abrir el SVG en navegador antes de insertar

### ❌ LO QUE NUNCA DEBES HACER

1. **NO especificar `center`, `x`, `y`** → El auto-viewBox lo maneja
2. **NO definir `canvas.width` o `canvas.height`** → Se calcula automáticamente
3. **NO usar coordenadas absolutas** → Solo ángulos relativos al vértice
4. **NO editar el SVG manualmente** → Siempre regenerar desde el spec

---

## 🎯 Principio Fundamental

```
┌──────────────────────────────────────────────────────────────────────┐
│   SPEC (JSON)          RENDERER (Python)         SVG (Output)       │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   {                     ┌─────────────┐          ┌─────────────┐    │
│     "type": "basic",    │ 1. Canvas   │          │  400x280    │    │
│     "rays": [           │    FIJO     │────────▶ │  (o 500x280)│    │
│       {"angle_deg":45}  │ 2. Contenido│          │  Contenido  │    │
│     ],                  │    centrado │          │  CENTRADO   │    │
│     "arc": {...}        │ 3. Escala   │          │             │    │
│   }                     │    si > max │          └─────────────┘    │
│                         └─────────────┘                              │
│                                                                      │
│   ✅ Sin coordenadas     ✅ Canvas 400x280       ✅ Altura           │
│      absolutas              (como gráficas)         controlada      │
└──────────────────────────────────────────────────────────────────────┘
```

### Tamaños de Canvas Estándar

| Tipo | Canvas | Uso |
|------|--------|-----|
| `angle_basic` | 400×280 | Ángulos simples |
| `angle_rotation` | 400×280 | Giros |
| `angle_notation` | 400×280 | Notaciones |
| `angle_special` | 400×280 | Ángulos especiales |
| `angle_comparison` | 500×280 | Comparaciones lado a lado |

> **Nota:** El contenido se centra automáticamente. Si es muy grande, se escala para caber.

---


## 📋 Tipos de Construcción

### 1. `angle_basic` — Ángulo simple

Para ilustrar un ángulo con vértice, lados y arco.

```json
{
  "construction": {
    "type": "angle_basic",
    "vertex": { "label": "O" },
    "rays": [
      { "angle_deg": 0, "label": "A" },
      { "angle_deg": 60, "label": "B" }
    ],
    "arc": { "label": "α", "color": "#22c55e" }
  }
}
```

**Parámetros opcionales:**
- `ray_length` → Longitud de rayos (default: 80px)
- `arc.radius` → Radio del arco (default: 30px)
- `custom_labels` → Etiquetas extra (ver ejemplo 5)

---

### 2. `angle_rotation` — Giro positivo/negativo

Para ilustrar el concepto de dirección del ángulo.

```json
{
  "construction": {
    "type": "angle_rotation",
    "angle_deg": 45,
    "direction": "ccw",
    "show_initial_label": true,
    "show_terminal_label": true,
    "show_sign": true
  }
}
```

**Valores de `direction`:**
- `"ccw"` → Counter-clockwise (antihorario) → Verde, signo +
- `"cw"` → Clockwise (horario) → Rojo, signo −

---

### 3. `angle_comparison` — Comparación lado a lado

Para mostrar que dos ángulos son iguales a pesar de diferencias visuales.

```json
{
  "construction": {
    "type": "angle_comparison",
    "angles": [
      { "title": "Rayos cortos", "angle_deg": 45, "ray_length": 50 },
      { "title": "Rayos largos", "angle_deg": 45, "ray_length": 90 }
    ],
    "message": "¡Mismo ángulo!"
  }
}
```

---

### 4. `angle_special` — Ángulos especiales

Para 0°, 90°, 180°, 360°.

```json
{
  "construction": {
    "type": "angle_special",
    "value": 0,
    "label": "Los rayos coinciden"
  }
}
```

**Valores de `value`:** `0`, `90`, `180`, `360`

---

### 5. `angle_notation` — Diferentes notaciones

Para mostrar ∠ABC, ∠B, θ en el mismo ángulo.

```json
{
  "construction": {
    "type": "angle_notation",
    "vertex_label": "Y",
    "rays": [
      { "angle_deg": -20, "label": "X" },
      { "angle_deg": 50, "label": "Z" }
    ],
    "notations": ["∠XYZ", "∠ZYX", "∠Y"]
  }
}
```

---

## 🔧 Comandos

### Generar un solo SVG

```bash
python3 scripts/geometry/angle_renderer.py \
  --spec specs/geometria/angulos/ejemplo-1.json \
  --output public/images/matematicas/geometria-euclidiana/angulos/ejemplo-1.svg
```

### Generar todos los SVGs de una carpeta

```bash
python3 scripts/geometry/angle_renderer.py \
  --spec-dir specs/geometria/angulos/ \
  --output-dir public/images/matematicas/geometria-euclidiana/angulos/
```

---

## 📁 Estructura de Archivos

```
specs/geometria/angulos/
├── ejemplo-1-identificacion.json   ← QUÉ dibujar
├── ejemplo-2-notacion.json
└── ...

public/images/matematicas/geometria-euclidiana/angulos/
├── ejemplo-1-identificacion.svg    ← OUTPUT auto-centrado
├── ejemplo-2-notacion.svg
└── ...
```

---

## 🎨 Paleta de Colores (USAR SIEMPRE ESTOS)

| Elemento | Hex | Variable |
|----------|-----|----------|
| Rayos normales | `#64748b` | `COLORS['text_light']` |
| Positivo/Correcto | `#22c55e` | `COLORS['success']` |
| Negativo/Error | `#ef4444` | `COLORS['accent']` |
| Primario | `#3b82f6` | `COLORS['primary']` |
| Texto | `#1e293b` | `COLORS['text']` |

---

## ✅ Checklist para Agentes IA

Antes de considerar terminada una ilustración:

- [ ] El spec NO tiene coordenadas absolutas (`center`, `x`, `y`)
- [ ] El spec NO define `canvas.width` o `canvas.height`
- [ ] Ejecuté el renderer con `python3 scripts/geometry/angle_renderer.py`
- [ ] Verifiqué visualmente que no hay espacio en blanco excesivo
- [ ] Inserté el SVG en el markdown: `![alt](/images/.../nombre.svg)`

---

## ⚠️ Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| Mucho espacio en blanco | Coordenadas absolutas en spec | Eliminar `center`, `x`, `y` del spec |
| Contenido descentrado | Canvas fijo | NO usar `canvas.width/height` |
| Etiquetas cortadas | Texto largo | Reducir tamaño de fuente o texto |
| Arco no visible | Ángulo muy pequeño | Aumentar `arc.radius` |

---

## 🔗 Relacionados

- [Árbol de decisión](./illustration-decision.md)
- [GeometrySpec](./geometry-exact.md) - Para triángulos
- [CircleSpec](./circle-spec.md) - Para circunferencias

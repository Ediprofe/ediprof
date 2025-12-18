---
description: Árbol de decisión para elegir tecnología de ilustración (SOLO Rough.js y SVG)
globs: ["src/content/**/*.md"]
---

# 🌳 Workflow: Decisión de Ilustraciones

> ⚠️ **SOLO DOS TECNOLOGÍAS: SVG estático y Rough.js**

Este documento ayuda a elegir la **tecnología correcta** para cada tipo de ilustración.

---

## 🚀 Resumen Ejecutivo

| Tecnología | Uso | JS |
|------------|-----|-----|
| **SVG estático** | Geometría exacta, gráficas de funciones | **0 KB** ⭐ |
| **Rough.js** | Diagramas conceptuales, situaciones físicas | ~50KB |

---

## 🌳 Árbol de Decisión

```
¿QUÉ TIPO DE ILUSTRACIÓN NECESITO?
│
├─── 📐 ¿Es GEOMETRÍA con propiedades exactas?
│    │   (circunferencias, triángulos, geometría analítica)
│    │
│    └─── SÍ → SVG ESTÁTICO (Python/SymPy → SVG)
│         • Circunferencias: radio, cuerda, arco, sector
│         • Triángulos: puntos notables, alturas, medianas
│         • Geometría analítica: plano cartesiano, rectas
│         📁 Ver: circle-spec.md, geometry-exact.md, cartesian-spec.md
│
├─── 📈 ¿Es una GRÁFICA de funciones?
│    │   (sin, cos, parábolas, exponenciales, rectas)
│    │
│    └─── SÍ → SVG ESTÁTICO (Python/SymPy → SVG)
│         • Funciones trigonométricas
│         • Funciones lineales y cuadráticas
│         • Funciones exponenciales y logarítmicas
│         📁 Ver: cartesian-spec.md, graphspec.md
│
├─── ✏️ ¿Es un DIAGRAMA ilustrativo/conceptual?
│    │   (situaciones físicas, modelos, procesos)
│    │
│    └─── SÍ → ROUGH.JS (inline en .md)
│         • Situaciones físicas (bloques, poleas, planos)
│         • Modelos atómicos, partículas, estados de materia
│         • Equipos de laboratorio, procesos químicos
│         • Mapas conceptuales, organigramas, ciclos
│         • Transformaciones geométricas (traslación, rotación)
│         • Fracciones visuales (círculos divididos)
│         📁 Ver: roughjs.md
│
└─── 📝 ¿Es solo una FÓRMULA?
     └─── SÍ → LATEX (inline en .md)
          • $inline$ o $$bloque$$
```

---

## 📋 Matriz de Decisión por Materia

### 🧮 MATEMÁTICAS

| Necesidad | Tecnología |
|-----------|------------|
| Gráfica de $\sin x$, $\cos x$ | **SVG** (CartesianSpec) |
| Gráfica de función lineal $y = mx + b$ | **SVG** (CartesianSpec) |
| Gráfica de parábola $y = x^2$ | **SVG** (CartesianSpec) |
| Baricentro de triángulo | **SVG** (GeometrySpec) |
| Circuncentro exacto | **SVG** (CircleSpec) |
| Fracción 3/4 visual | **Rough.js** |
| Mapa conceptual de tipos de números | **Rough.js** |
| Transformación geométrica | **Rough.js** |

### 🚀 FÍSICA

| Necesidad | Tecnología |
|-----------|------------|
| Gráfica posición vs tiempo | **SVG** (CartesianSpec) |
| Gráfica velocidad vs tiempo | **SVG** (CartesianSpec) |
| Bloque en plano inclinado | **Rough.js** |
| Diagrama de fuerzas | **Rough.js** |
| Circuito eléctrico | **Rough.js** |
| Tiro parabólico (diagrama) | **Rough.js** |

### ⚛️ QUÍMICA

| Necesidad | Tecnología |
|-----------|------------|
| Modelo atómico de Bohr | **Rough.js** |
| Enlace covalente/iónico | **Rough.js** |
| Estados de la materia | **Rough.js** |
| Equipos de laboratorio | **Rough.js** |
| Tabla periódica (elementos) | **SVG** estático |

### 🌍 CIENCIAS

| Necesidad | Tecnología |
|-----------|------------|
| Ciclo del agua | **Rough.js** |
| Cadena alimenticia | **Rough.js** |
| Célula (diagrama) | **Rough.js** |
| Sistema digestivo | **Rough.js** |

---

## 🔧 Comandos Rápidos

### SVG con GeometrySpec (triángulos)

```bash
python3 scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --output public/images/geometria/ \
  --verify
```

### SVG con CircleSpec (circunferencias)

```bash
python3 scripts/geometry/circle_spec_renderer.py \
  --spec specs/geometria/circulos/arco-sector.json \
  --output public/images/geometria/circulos/arco-sector.svg
```

### SVG con CartesianSpec (geometría analítica)

```bash
python3 scripts/geometry/cartesian_renderer.py \
  --spec specs/geometria/analitica/distancia-puntos.json \
  --output public/images/geometria/analitica/distancia-puntos.svg
```

### Rough.js (inline en markdown)

```html
<script type="module">
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';

const canvas = document.getElementById('rough-mi-diagrama');
if (canvas) {
  const rc = rough.canvas(canvas);
  // Dibujar elementos...
}
</script>
```

---

## ❌ TECNOLOGÍAS ELIMINADAS

| Tecnología | Estado | Razón |
|------------|--------|-------|
| ECharts | ❌ ELIMINADO | 1MB de JS, reemplazado por SVG |
| Chart.js | ❌ ELIMINADO | 200KB de JS, reemplazado por Rough.js |
| Three.js | ❌ ELIMINADO | 500KB de JS, no necesario |
| JSXGraph | ⚠️ Solo condicional | 600KB, solo si hay `.jxgbox` |

---

## 🔗 Workflows Detallados

- [Rough.js](./roughjs.md) - Diagramas ilustrativos ⭐
- [GeometrySpec](./geometry-exact.md) - Triángulos exactos
- [CircleSpec](./circle-spec.md) - Circunferencias
- [CartesianSpec](./cartesian-spec.md) - Geometría analítica
- [GraphSpec](./graphspec.md) - Gráficas de funciones

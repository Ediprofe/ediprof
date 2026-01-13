---
description: Árbol de decisión para elegir tecnología de ilustración (SVG generado + PNG de tablet)
globs: ["src/content/**/*.md"]
---

# 🌳 Workflow: Decisión de Ilustraciones

> ⚠️ **DOS TIPOS DE ILUSTRACIONES: SVG generado + PNG de tablet**

Este documento ayuda a elegir la **tecnología correcta** para cada tipo de ilustración.

---

## 🚀 Resumen Ejecutivo

| Tecnología | Uso | JS |
|------------|-----|-----|
| **SVG generado** | Geometría exacta, gráficas de funciones, química | **0 KB** ⭐ |
| **PNG de tablet** | Diagramas conceptuales, situaciones físicas | **0 KB** ⭐ |

---

## 🌳 Árbol de Decisión

```
¿QUÉ TIPO DE ILUSTRACIÓN NECESITO?
│
├─── 📐 ¿Es GEOMETRÍA con propiedades exactas?
│    │   (circunferencias, triángulos, geometría analítica)
│    │
│    └─── SÍ → SVG GENERADO (Python/SymPy → SVG)
│         • Circunferencias: radio, cuerda, arco, sector
│         • Triángulos: puntos notables, alturas, medianas
│         • Geometría analítica: plano cartesiano, rectas
│         📁 Ver: circle-spec.md, geometry-exact.md, cartesian-spec.md
│
├─── 📏 ¿Es un ÁNGULO con elementos exactos?
│    │   (vértice, lados, arcos, notación, giros)
│    │
│    └─── SÍ → SVG GENERADO (AngleSpec → SVG)
│         • Ángulos básicos con etiquetas
│         • Giro positivo/negativo
│         • Comparación de ángulos
│         • Ángulos especiales (0°, 90°, 180°, 360°)
│         📁 Ver: angle-spec.md
│
├─── ⚖️ ¿Es COMPARACIÓN de triángulos?
│    │   (congruencia, semejanza, proporciones)
│    │
│    └─── SÍ → SVG GENERADO (Building Blocks → SVG)
│         • Congruencia: LLL, LAL, ALA
│         • Semejanza: AA, LLL, LAL
│         • Comparación de proporciones
│         📁 Usar: scripts/geometry/renderer_template.py
│         ⚠️ OBLIGATORIO: Importar de core/ (ver CLAUDE.md sección 6)
│

├─── 📈 ¿Es una GRÁFICA de funciones?
│    │   (sin, cos, parábolas, exponenciales, rectas)
│    │
│    └─── SÍ → SVG GENERADO (Python/SymPy → SVG)
│         • Funciones trigonométricas
│         • Funciones lineales y cuadráticas
│         • Funciones exponenciales y logarítmicas
│         📁 Ver: cartesian-spec.md, graphspec.md
│
├─── ⚗️ ¿Es QUÍMICA (tabla periódica, tendencias)?
│    │
│    └─── SÍ → SVG GENERADO (ChemistrySpec → SVG)
│         • Tabla periódica
│         • Tendencias periódicas
│         📁 Ver: chemistry-spec.md
│
├─── ✏️ ¿Es un DIAGRAMA ilustrativo/conceptual?
│    │   (situaciones físicas, modelos, procesos)
│    │
│    └─── SÍ → PNG DE TABLET (dibujo manual → .mdx)
│         • Situaciones físicas (bloques, poleas, planos)
│         • Modelos atómicos, partículas, estados de materia
│         • Equipos de laboratorio, procesos químicos
│         • Mapas conceptuales, organigramas, ciclos
│         • Transformaciones geométricas ilustrativas
│         📁 Ver: CLAUDE.md sección "Workflow: Imágenes de Tablet"
│
└─── 📝 ¿Es solo una FÓRMULA?
     └─── SÍ → LATEX (inline en .md)
          • $inline$ o $$bloque$$
```

---

## ❓ ¿No existe renderer para mi caso?

> **Flujo cuando necesitas crear un renderer NUEVO:**

```
¿NO existe renderer?
│
├─── PASO 1: Copiar template
│    └─── scripts/geometry/renderer_template.py
│
├─── PASO 2: Importar de core/ (OBLIGATORIO)
│    ├── from core.colors import COLORS
│    ├── from core.canvas import get_canvas_config
│    ├── from core.layouts import side_by_side
│    └── from core.triangle_primitives import draw_triangle
│
├─── PASO 3: Ensamblar bloques
│    └─── 20 líneas, no 200
│
└─── ⚠️ NUNCA hardcodear width=600, height=300
```

📁 Ver: `CLAUDE.md` sección 6 (checklist obligatorio)

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
| Fracción 3/4 visual | **PNG tablet** |
| Mapa conceptual de tipos de números | **PNG tablet** |
| Transformación geométrica | **PNG tablet** |

### 🚀 FÍSICA

| Necesidad | Tecnología |
|-----------|------------|
| Gráfica posición vs tiempo | **SVG** (CartesianSpec) |
| Gráfica velocidad vs tiempo | **SVG** (CartesianSpec) |
| Bloque en plano inclinado | **PNG tablet** |
| Diagrama de fuerzas | **PNG tablet** |
| Circuito eléctrico | **PNG tablet** |
| Tiro parabólico (diagrama) | **PNG tablet** |

### ⚛️ QUÍMICA

| Necesidad | Tecnología |
|-----------|------------|
| Tabla periódica | **SVG** (ChemistrySpec) |
| Tendencias periódicas | **SVG** (ChemistrySpec) |
| Modelo atómico de Bohr | **PNG tablet** |
| Enlace covalente/iónico | **PNG tablet** |
| Estados de la materia | **PNG tablet** |
| Equipos de laboratorio | **PNG tablet** |

### 🌍 CIENCIAS

| Necesidad | Tecnología |
|-----------|------------|
| Ciclo del agua | **PNG tablet** |
| Cadena alimenticia | **PNG tablet** |
| Célula (diagrama) | **PNG tablet** |
| Sistema digestivo | **PNG tablet** |

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

### PNG de Tablet (en .mdx)

```mdx
import { Image } from 'astro:assets';
import miDiagrama from '/public/images/fisica/t-plano-inclinado.png';

<Image src={miDiagrama} alt="Bloque en plano inclinado" format="webp" />
```

---

## ✅ Checklist

- [ ] ¿Elegí la tecnología correcta según el árbol de decisión?
- [ ] ¿Los SVGs usan los renderers oficiales?
- [ ] ¿Los PNG de tablet tienen prefijo `t-`?
- [ ] ¿Los archivos con PNG de tablet son `.mdx`?
- [ ] ¿Incluí `format="webp"` en el componente Image?

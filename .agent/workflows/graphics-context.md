---
description: Guía para generar gráficos en lecciones educativas - JSXGraph y Chart.js
---

# 📊 Guía de Generación de Gráficos Educativos

Este documento define las buenas prácticas para generar gráficos en las lecciones de ediprofe.com. Se usan **dos librerías** según el tipo de contenido.

---

## 🎯 Cuándo usar cada librería

| Materia/Contenido | Librería | Razón |
|-------------------|----------|-------|
| **Fracciones** (pizzas, partes de un todo) | **Chart.js** | Pie charts limpios y profesionales |
| **Estadística** (barras, histogramas, líneas) | **Chart.js** | Su especialidad |
| **Porcentajes** | **Chart.js** | Pie/doughnut charts |
| **Vectores** | **JSXGraph** | Interactividad, puntos arrastrables |
| **Geometría** (figuras, ángulos, transformaciones) | **JSXGraph** | Construcciones dinámicas |
| **Funciones matemáticas** (gráficas, límites) | **JSXGraph** | Ejes coordenados, zoom |
| **Trigonometría** (círculo unitario) | **JSXGraph** | Interactividad angular |

> 💡 **Regla general:** Si necesitas mostrar "partes de un todo" → Chart.js. Si necesitas coordenadas o interactividad → JSXGraph.

---

# SECCIÓN A: Chart.js (Fracciones, Estadística)

## A.1 Configuración (ya en BaseLayout.astro)
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js" defer></script>
```

## A.2 Estructura HTML estándar
```html
<div style="max-width: 250px; margin: 1rem auto;">
  <canvas id="chart-NOMBRE-UNICO"></canvas>
</div>
```

## A.3 Estructura JavaScript estándar
```javascript
<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined' && document.getElementById('chart-ID')) {
    new Chart(document.getElementById('chart-ID'), {
      type: 'pie',  // o 'bar', 'doughnut', 'line'
      data: { /* ... */ },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: { enabled: false }
        }
      }
    });
  }
});
</script>
```

## A.4 Paleta de colores Chart.js

| Color | Hex | Uso |
|-------|-----|-----|
| Azul | `#3b82f6` | Partes tomadas (propia) |
| Rojo | `#ef4444` | Fracciones impropias |
| Verde | `#22c55e` | Unidades completas |
| Gris | `#e5e7eb` | Partes no tomadas/vacías |
| Borde | `#374151` | Bordes de todos los gráficos |

## A.5 Patrones comunes Chart.js

### Fracción simple (ej: 3/8)
```javascript
new Chart(document.getElementById('chart-fraccion'), {
  type: 'pie',
  data: {
    labels: ['1','2','3','4','5','6','7','8'],
    datasets: [{
      data: [1,1,1,1,1,1,1,1],
      backgroundColor: ['#3b82f6','#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb'],
      borderColor: '#374151',
      borderWidth: 2
    }]
  },
  options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
});
```

### Número mixto (ej: 2 3/4 = 1 + 1 + 3/4)
Usar múltiples canvas en un flexbox:
```html
<div style="display: flex; justify-content: center; gap: 0.5rem; margin: 1rem auto;">
  <div style="width: 80px;"><canvas id="chart-1"></canvas></div>
  <span>+</span>
  <div style="width: 80px;"><canvas id="chart-2"></canvas></div>
  <span>+</span>
  <div style="width: 80px;"><canvas id="chart-3"></canvas></div>
</div>
```

## A.6 Texto contextual obligatorio

Siempre añadir texto **antes** del gráfico que explique qué representa:
```markdown
En la siguiente figura, las **porciones azules** representan las partes que tomamos, mientras que las **porciones grises** son las que quedan:

[gráfico aquí]

**Interpretación:** "Tres de ocho partes" o "tres octavos".
```

---

# SECCIÓN B: JSXGraph (Vectores, Geometría, Funciones)

## B.1 Configuración (ya en BaseLayout.astro)
```html
<script src="https://cdn.jsdelivr.net/npm/jsxgraph@1.8.0/distrib/jsxgraphcore.js" defer></script>
```

## B.2 Estructura HTML estándar
```html
<div id="jsxgraph-NOMBRE-UNICO" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 350px; margin: 1.5rem auto;"></div>
```

## B.3 Estructura JavaScript estándar
```javascript
<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-ID', {
      boundingbox: [-1, 7, 9, -1],  // [xmin, ymax, xmax, ymin]
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // ... crear elementos ...
    
    board.unsuspendUpdate();
  }
});
</script>
```

## B.4 Paleta de colores JSXGraph

| Color | Hex | Uso |
|-------|-----|-----|
| Azul | `#3b82f6` | Vector A (primario) |
| Rojo | `#ef4444` | Vector B (secundario) |
| Verde | `#22c55e` | Resultante R |
| Naranja | `#f97316` | Auxiliares (-B) |
| Gris | `#64748b` | Origen, puntos neutros |
| Gris claro | `#94a3b8` | Líneas auxiliares punteadas |

## B.5 Interactivo vs Estático

### INTERACTIVO (puntos arrastrables)
- Exploración de conceptos
- El usuario puede mover elementos

### ESTÁTICO (puntos fijos)
```javascript
var P = board.create('point', [3, 2], {name: '', size: 3, fixed: true, color: '#3b82f6'});
```

## B.6 Etiquetas - NO usar LaTeX
```javascript
// ✅ CORRECTO
board.create('text', [x, y, 'A'], {
  fontSize: 16, 
  strokeColor: '#3b82f6', 
  cssStyle: 'font-weight: bold; font-style: italic;', 
  fixed: true
});

// ❌ INCORRECTO - LaTeX no funciona en JSXGraph
board.create('text', [x, y, '\\(\\vec{A}\\)'], {useMathJax: true});
```

---

## ✅ Checklist antes de generar gráficos

### Para Chart.js (fracciones):
- [ ] ¿Es un gráfico de "partes de un todo"? → Usar Chart.js
- [ ] ¿El ID del canvas es único?
- [ ] ¿Los colores siguen la paleta?
- [ ] ¿Hay texto explicativo antes y después del gráfico?
- [ ] ¿borderWidth: 2 en el dataset?

### Para JSXGraph (geometría/vectores):
- [ ] ¿Necesita coordenadas o interactividad? → Usar JSXGraph
- [ ] ¿El ID del contenedor es único?
- [ ] ¿Las etiquetas usan strokeColor (no color)?
- [ ] ¿Los puntos calculados tienen fixed: true?
- [ ] ¿Hay board.unsuspendUpdate() al final?

---

## ⚠️ Limitaciones conocidas

- **Modo oscuro**: Ambas librerías tienen fondo blanco fijo
- **LaTeX en JSXGraph**: No funciona, usar texto simple
- **SVG inline**: No se renderiza correctamente en markdown (no usar)

---

## 📋 Resumen rápido para la IA

Cuando generes una lección, pregúntate:

1. **¿Es sobre fracciones, porcentajes o estadística?** → **Chart.js pie/bar**
2. **¿Es sobre vectores, geometría o funciones?** → **JSXGraph**
3. **¿Solo necesitas una fórmula sin visualización?** → **KaTeX ($$...$$)**

Siempre añade texto contextual que explique qué representa el gráfico antes y después de incluirlo.

# 📍 Plano Cartesiano

En esta lección estudiaremos el plano cartesiano, el sistema de coordenadas donde representaremos las funciones lineales.

---

## 📖 El sistema de coordenadas cartesianas

El **plano cartesiano** es un sistema formado por dos rectas numéricas perpendiculares:

- **Eje X** (horizontal): también llamado eje de las abscisas
- **Eje Y** (vertical): también llamado eje de las ordenadas
- **Origen**: punto donde se cruzan ambos ejes, con coordenadas $(0, 0)$

En la siguiente visualización puedes ver el plano cartesiano con sus ejes y los cuatro cuadrantes:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-plano-intro" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-plano-intro', {
      boundingbox: [-6, 6, 6, -6],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Origen
    board.create('point', [0, 0], {
      name: 'Origen (0,0)',
      size: 4,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 12, offset: [10, -15] }
    });
    
    // Etiquetas de cuadrantes
    board.create('text', [3, 3, 'I'], {
      fontSize: 24,
      strokeColor: '#3b82f6',
      cssStyle: 'font-weight: bold;',
      fixed: true
    });
    board.create('text', [-3, 3, 'II'], {
      fontSize: 24,
      strokeColor: '#22c55e',
      cssStyle: 'font-weight: bold;',
      fixed: true
    });
    board.create('text', [-3.2, -3, 'III'], {
      fontSize: 24,
      strokeColor: '#f97316',
      cssStyle: 'font-weight: bold;',
      fixed: true
    });
    board.create('text', [3, -3, 'IV'], {
      fontSize: 24,
      strokeColor: '#a855f7',
      cssStyle: 'font-weight: bold;',
      fixed: true
    });
    
    // Etiquetas de ejes
    board.create('text', [5.3, 0.4, 'Eje X'], {
      fontSize: 12,
      strokeColor: '#374151',
      fixed: true
    });
    board.create('text', [0.3, 5.3, 'Eje Y'], {
      fontSize: 12,
      strokeColor: '#374151',
      fixed: true
    });
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Coordenadas de un punto

Cada punto en el plano se representa con un **par ordenado** $(x, y)$:

- $x$ = coordenada horizontal (abscisa)
- $y$ = coordenada vertical (ordenada)

### Ejemplo 1

El punto $P(3, 4)$ está ubicado:
- $3$ unidades a la derecha del origen
- $4$ unidades hacia arriba

### Ejemplo 2

El punto $Q(-2, 5)$ está ubicado:
- $2$ unidades a la izquierda del origen
- $5$ unidades hacia arriba

### Ejemplo 3

El punto $R(4, -3)$ está ubicado:
- $4$ unidades a la derecha
- $3$ unidades hacia abajo

### Ejemplo 4

El punto $S(-1, -2)$ está ubicado:
- $1$ unidad a la izquierda
- $2$ unidades hacia abajo

En la siguiente gráfica puedes ver los cuatro puntos ubicados en el plano:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-puntos-ejemplos" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-puntos-ejemplos', {
      boundingbox: [-6, 7, 6, -5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Punto P(3, 4) - Cuadrante I
    board.create('point', [3, 4], {
      name: 'P(3, 4)',
      size: 4,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 12, offset: [8, 8] }
    });
    
    // Punto Q(-2, 5) - Cuadrante II
    board.create('point', [-2, 5], {
      name: 'Q(-2, 5)',
      size: 4,
      fixed: true,
      color: '#22c55e',
      label: { fontSize: 12, offset: [-60, 8] }
    });
    
    // Punto R(4, -3) - Cuadrante IV
    board.create('point', [4, -3], {
      name: 'R(4, -3)',
      size: 4,
      fixed: true,
      color: '#a855f7',
      label: { fontSize: 12, offset: [8, -15] }
    });
    
    // Punto S(-1, -2) - Cuadrante III
    board.create('point', [-1, -2], {
      name: 'S(-1, -2)',
      size: 4,
      fixed: true,
      color: '#f97316',
      label: { fontSize: 12, offset: [-65, -15] }
    });
    
    // Líneas punteadas al origen para P
    board.create('segment', [[0, 0], [3, 0]], { strokeColor: '#3b82f6', strokeWidth: 1, dash: 2, fixed: true });
    board.create('segment', [[3, 0], [3, 4]], { strokeColor: '#3b82f6', strokeWidth: 1, dash: 2, fixed: true });
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Los cuatro cuadrantes

El plano se divide en cuatro regiones llamadas **cuadrantes**:

| Cuadrante | Signos de $(x, y)$ | Ubicación |
|:---------:|:------------------:|:----------|
| I | $(+, +)$ | Superior derecho |
| II | $(-, +)$ | Superior izquierdo |
| III | $(-, -)$ | Inferior izquierdo |
| IV | $(+, -)$ | Inferior derecho |

---

### Ejemplo 5

¿En qué cuadrante está cada punto?

| Punto | Cuadrante |
|:-----:|:---------:|
| $(5, 3)$ | I |
| $(-4, 2)$ | II |
| $(-3, -1)$ | III |
| $(2, -5)$ | IV |

Observa cada punto en su cuadrante correspondiente:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-cuadrantes" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-cuadrantes', {
      boundingbox: [-7, 7, 7, -7],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Cuadrante I: (5, 3)
    board2.create('point', [5, 3], {
      name: '(5, 3)',
      size: 4,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 11, offset: [5, 10] }
    });
    board2.create('text', [4, 5, 'Cuad. I'], {
      fontSize: 11,
      strokeColor: '#3b82f6',
      fixed: true
    });
    
    // Cuadrante II: (-4, 2)
    board2.create('point', [-4, 2], {
      name: '(-4, 2)',
      size: 4,
      fixed: true,
      color: '#22c55e',
      label: { fontSize: 11, offset: [-50, 10] }
    });
    board2.create('text', [-5.5, 5, 'Cuad. II'], {
      fontSize: 11,
      strokeColor: '#22c55e',
      fixed: true
    });
    
    // Cuadrante III: (-3, -1)
    board2.create('point', [-3, -1], {
      name: '(-3, -1)',
      size: 4,
      fixed: true,
      color: '#f97316',
      label: { fontSize: 11, offset: [-55, -12] }
    });
    board2.create('text', [-5.5, -5, 'Cuad. III'], {
      fontSize: 11,
      strokeColor: '#f97316',
      fixed: true
    });
    
    // Cuadrante IV: (2, -5)
    board2.create('point', [2, -5], {
      name: '(2, -5)',
      size: 4,
      fixed: true,
      color: '#a855f7',
      label: { fontSize: 11, offset: [5, -12] }
    });
    board2.create('text', [4, -5, 'Cuad. IV'], {
      fontSize: 11,
      strokeColor: '#a855f7',
      fixed: true
    });
    
    board2.unsuspendUpdate();
  }
});
</script>

---

## 📖 Puntos sobre los ejes

Los puntos sobre los ejes no pertenecen a ningún cuadrante:

### Sobre el eje X

Si $y = 0$, el punto está **sobre el eje X**.

Ejemplo: $(3, 0)$, $(-5, 0)$, $(0, 0)$

### Sobre el eje Y

Si $x = 0$, el punto está **sobre el eje Y**.

Ejemplo: $(0, 4)$, $(0, -2)$, $(0, 0)$

---

## 📖 Distancia entre dos puntos

La distancia entre dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ se calcula con:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

### Ejemplo 6

Encontrar la distancia entre $A(1, 2)$ y $B(4, 6)$.

$$
d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

$$
\boxed{d = 5}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-distancia1" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board3 = JXG.JSXGraph.initBoard('jsxgraph-distancia1', {
      boundingbox: [-1, 8, 7, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var A = board3.create('point', [1, 2], {
      name: 'A(1, 2)',
      size: 4,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 11, offset: [-50, -10] }
    });
    
    var B = board3.create('point', [4, 6], {
      name: 'B(4, 6)',
      size: 4,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 11, offset: [5, 10] }
    });
    
    // Línea de distancia
    board3.create('segment', [A, B], {
      strokeColor: '#22c55e',
      strokeWidth: 3,
      fixed: true
    });
    
    // Triángulo auxiliar
    board3.create('segment', [[1, 2], [4, 2]], { strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true });
    board3.create('segment', [[4, 2], [4, 6]], { strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true });
    
    // Etiquetas de catetos
    board3.create('text', [2.5, 1.5, '3'], { fontSize: 12, strokeColor: '#64748b', fixed: true });
    board3.create('text', [4.3, 4, '4'], { fontSize: 12, strokeColor: '#64748b', fixed: true });
    
    // Etiqueta de distancia
    board3.create('text', [2, 4.5, 'd = 5'], { fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true });
    
    board3.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 7

Encontrar la distancia entre $P(-3, 2)$ y $Q(5, -4)$.

$$
d = \sqrt{(5-(-3))^2 + (-4-2)^2} = \sqrt{64 + 36} = \sqrt{100} = 10
$$

$$
\boxed{d = 10}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-distancia2" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board4 = JXG.JSXGraph.initBoard('jsxgraph-distancia2', {
      boundingbox: [-5, 5, 7, -6],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var P = board4.create('point', [-3, 2], {
      name: 'P(-3, 2)',
      size: 4,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 11, offset: [-60, 10] }
    });
    
    var Q = board4.create('point', [5, -4], {
      name: 'Q(5, -4)',
      size: 4,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 11, offset: [5, -12] }
    });
    
    // Línea de distancia
    board4.create('segment', [P, Q], {
      strokeColor: '#22c55e',
      strokeWidth: 3,
      fixed: true
    });
    
    // Triángulo auxiliar
    board4.create('segment', [[-3, 2], [5, 2]], { strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true });
    board4.create('segment', [[5, 2], [5, -4]], { strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true });
    
    // Etiquetas de catetos
    board4.create('text', [1, 2.5, '8'], { fontSize: 12, strokeColor: '#64748b', fixed: true });
    board4.create('text', [5.3, -1, '6'], { fontSize: 12, strokeColor: '#64748b', fixed: true });
    
    // Etiqueta de distancia
    board4.create('text', [0, -1.5, 'd = 10'], { fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true });
    
    board4.unsuspendUpdate();
  }
});
</script>

---

## 📖 Punto medio

El **punto medio** $M$ entre $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ es:

$$
M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)
$$

### Ejemplo 8

Encontrar el punto medio entre $A(2, 4)$ y $B(8, 10)$.

$$
M = \left(\frac{2+8}{2}, \frac{4+10}{2}\right) = \left(\frac{10}{2}, \frac{14}{2}\right) = (5, 7)
$$

$$
\boxed{M = (5, 7)}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-puntomedio1" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board5 = JXG.JSXGraph.initBoard('jsxgraph-puntomedio1', {
      boundingbox: [-1, 12, 10, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var A = board5.create('point', [2, 4], {
      name: 'A(2, 4)',
      size: 4,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 11, offset: [-50, -10] }
    });
    
    var B = board5.create('point', [8, 10], {
      name: 'B(8, 10)',
      size: 4,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 11, offset: [5, 10] }
    });
    
    // Segmento AB
    board5.create('segment', [A, B], {
      strokeColor: '#94a3b8',
      strokeWidth: 2,
      fixed: true
    });
    
    // Punto medio
    var M = board5.create('point', [5, 7], {
      name: 'M(5, 7)',
      size: 5,
      fixed: true,
      color: '#22c55e',
      label: { fontSize: 12, offset: [8, 8], cssStyle: 'font-weight: bold;' }
    });
    
    board5.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 9

Encontrar el punto medio entre $P(-4, 3)$ y $Q(6, -1)$.

$$
M = \left(\frac{-4+6}{2}, \frac{3+(-1)}{2}\right) = \left(\frac{2}{2}, \frac{2}{2}\right) = (1, 1)
$$

$$
\boxed{M = (1, 1)}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-puntomedio2" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board6 = JXG.JSXGraph.initBoard('jsxgraph-puntomedio2', {
      boundingbox: [-6, 5, 8, -3],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var P = board6.create('point', [-4, 3], {
      name: 'P(-4, 3)',
      size: 4,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 11, offset: [-55, 10] }
    });
    
    var Q = board6.create('point', [6, -1], {
      name: 'Q(6, -1)',
      size: 4,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 11, offset: [5, -12] }
    });
    
    // Segmento PQ
    board6.create('segment', [P, Q], {
      strokeColor: '#94a3b8',
      strokeWidth: 2,
      fixed: true
    });
    
    // Punto medio
    board6.create('point', [1, 1], {
      name: 'M(1, 1)',
      size: 5,
      fixed: true,
      color: '#22c55e',
      label: { fontSize: 12, offset: [8, 8], cssStyle: 'font-weight: bold;' }
    });
    
    board6.unsuspendUpdate();
  }
});
</script>

---

## 📖 Graficando puntos

Para graficar un punto $(a, b)$:

1. Partimos del origen
2. Nos movemos $a$ unidades horizontalmente (derecha si $+$, izquierda si $-$)
3. Nos movemos $b$ unidades verticalmente (arriba si $+$, abajo si $-$)
4. Marcamos el punto

### Ejemplo 10

Graficar los puntos $A(3, 2)$, $B(-2, 4)$, $C(-3, -1)$ y $D(4, -3)$.

Cada punto se ubica siguiendo las reglas de signos y los pasos descritos:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-graficar" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board7 = JXG.JSXGraph.initBoard('jsxgraph-graficar', {
      boundingbox: [-6, 6, 6, -5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Cuadrante I: A(3, 2)
    board7.create('point', [3, 2], {
      name: 'A(3, 2)',
      size: 5,
      fixed: true,
      color: '#3b82f6',
      label: { fontSize: 12, offset: [8, 8] }
    });
    
    // Cuadrante II: B(-2, 4)
    board7.create('point', [-2, 4], {
      name: 'B(-2, 4)',
      size: 5,
      fixed: true,
      color: '#22c55e',
      label: { fontSize: 12, offset: [-60, 8] }
    });
    
    // Cuadrante III: C(-3, -1)
    board7.create('point', [-3, -1], {
      name: 'C(-3, -1)',
      size: 5,
      fixed: true,
      color: '#f97316',
      label: { fontSize: 12, offset: [-65, -15] }
    });
    
    // Cuadrante IV: D(4, -3)
    board7.create('point', [4, -3], {
      name: 'D(4, -3)',
      size: 5,
      fixed: true,
      color: '#a855f7',
      label: { fontSize: 12, offset: [8, -15] }
    });
    
    // Etiquetas de cuadrantes
    board7.create('text', [4.5, 4.5, 'I'], { fontSize: 18, strokeColor: '#cbd5e1', cssStyle: 'font-weight: bold;', fixed: true });
    board7.create('text', [-5, 4.5, 'II'], { fontSize: 18, strokeColor: '#cbd5e1', cssStyle: 'font-weight: bold;', fixed: true });
    board7.create('text', [-5, -4, 'III'], { fontSize: 18, strokeColor: '#cbd5e1', cssStyle: 'font-weight: bold;', fixed: true });
    board7.create('text', [4, -4, 'IV'], { fontSize: 18, strokeColor: '#cbd5e1', cssStyle: 'font-weight: bold;', fixed: true });
    
    board7.unsuspendUpdate();
  }
});
</script>

---

## 📋 Resumen

| Concepto | Fórmula |
|:---------|:-------:|
| Coordenadas | $(x, y)$ |
| Distancia | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Punto medio | $M = \left(\dfrac{x_1+x_2}{2}, \dfrac{y_1+y_2}{2}\right)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿En qué cuadrante está el punto $(-5, 7)$?

<details>
<summary>Ver solución</summary>

Cuadrante II ($x$ negativo, $y$ positivo)

</details>

---

**Ejercicio 2:** ¿Cuáles son las coordenadas del origen?

<details>
<summary>Ver solución</summary>

$(0, 0)$

</details>

---

**Ejercicio 3:** Calcula la distancia entre $A(0, 0)$ y $B(3, 4)$.

<details>
<summary>Ver solución</summary>

$$
d = \sqrt{9 + 16} = \sqrt{25} = 5
$$

</details>

---

**Ejercicio 4:** Encuentra el punto medio entre $(2, 6)$ y $(8, 2)$.

<details>
<summary>Ver solución</summary>

$$
M = (5, 4)
$$

</details>

---

**Ejercicio 5:** Si un punto tiene $y = 0$, ¿sobre qué eje está?

<details>
<summary>Ver solución</summary>

Sobre el eje X.

</details>

---

**Ejercicio 6:** Calcula la distancia entre $(-1, 2)$ y $(2, 6)$.

<details>
<summary>Ver solución</summary>

$$
d = \sqrt{(3)^2 + (4)^2} = \sqrt{25} = 5
$$

</details>

---

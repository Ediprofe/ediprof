# ✖️ Multiplicación de Números Naturales

En este tema aprenderemos a multiplicar números naturales usando el método de columnas con productos parciales.

---

## 📖 ¿Qué es la multiplicación?

La **multiplicación** es una forma abreviada de sumar un número varias veces.

$$
\text{factor} \times \text{factor} = \text{producto}
$$

### Ejemplo conceptual

$$
4 \times 3 = 4 + 4 + 4 = 12
$$

---

## 📖 Tablas de multiplicar

Es fundamental memorizar las tablas del 1 al 10.

| × | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **2** | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
| **3** | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 |
| **4** | 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 |
| **5** | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |
| **6** | 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 |
| **7** | 7 | 14 | 21 | 28 | 35 | 42 | 49 | 56 | 63 | 70 |
| **8** | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 |
| **9** | 9 | 18 | 27 | 36 | 45 | 54 | 63 | 72 | 81 | 90 |

---

## 📖 Multiplicación por una cifra

### Ejemplo 1: $123 \times 3 = 369$ (sin llevar)

<div id="jsxgraph-mult1" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 180px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult1', {
      boundingbox: [-0.5, 4.5, 5.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 123
    board.create('text', [1.5, 3.5, '1'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '2'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.9, 3.5, '3'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 3
    board.create('text', [0.8, 2.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.9, 2.5, '3'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.5, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 369
    board.create('text', [1.5, 1.2, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '6'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.9, 1.2, '9'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
- $3 \times 3 = 9$
- $3 \times 2 = 6$
- $3 \times 1 = 3$

---

### Ejemplo 2: $47 \times 6 = 282$ (con llevar)

<div id="jsxgraph-mult2" class="jsxgraph-container" style="width: 100%; max-width: 320px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult2', {
      boundingbox: [-0.5, 5, 5.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Lo que llevamos
    board.create('text', [1.5, 4.2, '⁴'], {fontSize: 12, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    // 47
    board.create('text', [2, 3.5, '4'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 3.5, '7'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 6
    board.create('text', [1, 2.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 2.5, '6'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.8, 2], [3.3, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 282
    board.create('text', [1.3, 1.2, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 1.2, '8'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 1.2, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Etiqueta
    board.create('text', [4.2, 4.2, '← llevo 4'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
- $6 \times 7 = 42$ → escribo **2**, llevo **4**
- $6 \times 4 = 24$, más 4 que llevaba = **28**

---

### Ejemplo 3: $58 \times 9 = 522$

<div id="jsxgraph-mult3" class="jsxgraph-container" style="width: 100%; max-width: 320px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult3', {
      boundingbox: [-0.5, 5, 5.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Lo que llevamos
    board.create('text', [1.5, 4.2, '⁷'], {fontSize: 12, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    // 58
    board.create('text', [2, 3.5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 3.5, '8'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 9
    board.create('text', [1, 2.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 2.5, '9'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.8, 2], [3.3, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 522
    board.create('text', [1.3, 1.2, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 1.2, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 1.2, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
- $9 \times 8 = 72$ → escribo **2**, llevo **7**
- $9 \times 5 = 45$, más 7 = **52**

---

## 📖 Multiplicación por dos cifras (productos parciales)

### Ejemplo 4: $34 \times 25 = 850$

<div id="jsxgraph-mult4" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 260px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult4')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult4', {
      boundingbox: [-0.5, 6.5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 34
    board.create('text', [2, 5.5, '3'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 5.5, '4'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 25
    board.create('text', [0.8, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 4.5, '2'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 4.5, '5'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.5, 4], [3.3, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Producto parcial 1: 34 × 5 = 170
    board.create('text', [1.3, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 3.2, '7'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 3.2, '0'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 3.2, '← 34×5'], {fontSize: 10, strokeColor: '#9333ea', fixed: true});
    // Producto parcial 2: 34 × 20 = 680
    board.create('text', [0.3, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 2.4, '6'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.3, 2.4, '8'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 2.4, '← 34×20'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true});
    // Línea de suma
    board.create('segment', [[0.2, 1.9], [3, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 850
    board.create('text', [1.3, 1.1, '8'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 1.1, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 1.1, '0'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $34 \times 5 = 170$
2. $34 \times 20 = 680$
3. Suma: $170 + 680 = 850$

---

### Ejemplo 5: $56 \times 12 = 672$

<div id="jsxgraph-mult5" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 260px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult5')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult5', {
      boundingbox: [-0.5, 6.5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 56
    board.create('text', [2, 5.5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 5.5, '6'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 12
    board.create('text', [0.8, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 4.5, '1'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 4.5, '2'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.5, 4], [3.3, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // 56 × 2 = 112
    board.create('text', [1.3, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 3.2, '2'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 56 × 10 = 560
    board.create('text', [0.3, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 2.4, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.3, 2.4, '6'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.2, 1.9], [3, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 672
    board.create('text', [1.3, 1.1, '6'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 1.1, '7'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 1.1, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $56 \times 2 = 112$
2. $56 \times 10 = 560$
3. Suma: $112 + 560 = 672$

---

### Ejemplo 6: $78 \times 34 = 2652$

<div id="jsxgraph-mult6" class="jsxgraph-container" style="width: 100%; max-width: 380px; height: 280px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult6')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult6', {
      boundingbox: [-0.5, 6.5, 6.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 78
    board.create('text', [2.3, 5.5, '7'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 5.5, '8'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 34
    board.create('text', [1.1, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 4.5, '3'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 4.5, '4'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.8, 4], [3.6, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // 78 × 4 = 312
    board.create('text', [1.6, 3.2, '3'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.2, '2'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 78 × 30 = 2340
    board.create('text', [0.5, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [0.9, 2.4, '2'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.6, 2.4, '3'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.4, '4'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.4, 1.9], [3.5, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 2652
    board.create('text', [0.9, 1.1, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.6, 1.1, '6'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.1, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.1, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $78 \times 4 = 312$
2. $78 \times 30 = 2340$
3. Suma: $312 + 2340 = 2652$

---

### Ejemplo 7: $156 \times 23 = 3588$

<div id="jsxgraph-mult7" class="jsxgraph-container" style="width: 100%; max-width: 400px; height: 280px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult7', {
      boundingbox: [-0.5, 6.5, 7, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 156
    board.create('text', [2, 5.5, '1'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 5.5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 5.5, '6'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 23
    board.create('text', [1, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 4.5, '2'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 4.5, '3'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.7, 4], [4, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // 156 × 3 = 468
    board.create('text', [2, 3.2, '4'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 3.2, '6'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 3.2, '8'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 156 × 20 = 3120
    board.create('text', [0.6, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [1.3, 2.4, '3'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 2.4, '1'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 2.4, '2'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.5, 1.9], [4, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 3588
    board.create('text', [1.3, 1.1, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 1.1, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 1.1, '8'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 1.1, '8'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $156 \times 3 = 468$
2. $156 \times 20 = 3120$
3. Suma: $468 + 3120 = 3588$

---

### Ejemplo 8: $245 \times 38 = 9310$

<div id="jsxgraph-mult8" class="jsxgraph-container" style="width: 100%; max-width: 420px; height: 280px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult8')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult8', {
      boundingbox: [-0.5, 6.5, 7.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 245
    board.create('text', [2.3, 5.5, '2'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 5.5, '4'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 5.5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 38
    board.create('text', [1.3, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 4.5, '3'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 4.5, '8'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[1, 4], [4.3, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // 245 × 8 = 1960
    board.create('text', [1.6, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.2, '9'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.2, '6'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 3.2, '0'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 245 × 30 = 7350
    board.create('text', [0.7, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [1.6, 2.4, '7'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.4, '3'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.4, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.5, 1.9], [4.3, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 9310
    board.create('text', [1.6, 1.1, '9'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.1, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.1, '1'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 1.1, '0'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $245 \times 8 = 1960$
2. $245 \times 30 = 7350$
3. Suma: $1960 + 7350 = 9310$

---

### Ejemplo 9: $325 \times 46 = 14950$

<div id="jsxgraph-mult9" class="jsxgraph-container" style="width: 100%; max-width: 440px; height: 280px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult9')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult9', {
      boundingbox: [-0.5, 6.5, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 325
    board.create('text', [2.6, 5.5, '3'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 5.5, '2'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 5.5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 46
    board.create('text', [1.6, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 4.5, '4'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 4.5, '6'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[1.3, 4], [4.6, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // 325 × 6 = 1950
    board.create('text', [1.9, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.2, '9'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 3.2, '5'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 3.2, '0'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 325 × 40 = 13000
    board.create('text', [0.9, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [1.2, 2.4, '1'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.9, 2.4, '3'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.7, 1.9], [4.6, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 14950
    board.create('text', [1.2, 1.1, '1'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.9, 1.1, '4'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.1, '9'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 1.1, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 1.1, '0'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $325 \times 6 = 1950$
2. $325 \times 40 = 13000$
3. Suma: $1950 + 13000 = 14950$

---

### Ejemplo 10: $512 \times 75 = 38400$

<div id="jsxgraph-mult10" class="jsxgraph-container" style="width: 100%; max-width: 440px; height: 280px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult10')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult10', {
      boundingbox: [-0.5, 6.5, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 512
    board.create('text', [2.6, 5.5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 5.5, '1'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 5.5, '2'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 75
    board.create('text', [1.6, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 4.5, '7'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 4.5, '5'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[1.3, 4], [4.6, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // 512 × 5 = 2560
    board.create('text', [1.9, 3.2, '2'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.2, '5'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 3.2, '6'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 3.2, '0'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 512 × 70 = 35840
    board.create('text', [0.9, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [1.2, 2.4, '3'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.9, 2.4, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.4, '8'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 2.4, '4'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.7, 1.9], [4.6, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 38400
    board.create('text', [1.2, 1.1, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.9, 1.1, '8'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.1, '4'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.3, 1.1, '0'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 1.1, '0'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $512 \times 5 = 2560$
2. $512 \times 70 = 35840$
3. Suma: $2560 + 35840 = 38400$

---

## 📖 Propiedades de la multiplicación

| Propiedad | Fórmula | Ejemplo |
|:----------|:--------|:--------|
| **Conmutativa** | $a \times b = b \times a$ | $7 \times 4 = 4 \times 7 = 28$ |
| **Asociativa** | $(a \times b) \times c = a \times (b \times c)$ | $(2 \times 3) \times 4 = 2 \times (3 \times 4) = 24$ |
| **Elemento neutro** | $a \times 1 = a$ | $8 \times 1 = 8$ |
| **Elemento absorbente** | $a \times 0 = 0$ | $5 \times 0 = 0$ |
| **Distributiva** | $a \times (b + c) = a \times b + a \times c$ | $3 \times (4 + 2) = 3 \times 4 + 3 \times 2 = 18$ |

---

## 📝 Ejercicios de práctica

| Ejercicio | Operación |
|:---------:|:----------|
| 1 | $8 \times 7$ |
| 2 | $56 \times 4$ |
| 3 | $67 \times 9$ |
| 4 | $25 \times 12$ |
| 5 | $48 \times 15$ |
| 6 | $134 \times 26$ |
| 7 | $245 \times 38$ |
| 8 | $367 \times 52$ |
| 9 | $458 \times 67$ |
| 10 | $625 \times 84$ |

---

## ✅ Soluciones

| Ejercicio | Solución |
|:---------:|:---------|
| 1 | $56$ |
| 2 | $224$ |
| 3 | $603$ |
| 4 | $300$ |
| 5 | $720$ |
| 6 | $3484$ |
| 7 | $9310$ |
| 8 | $19084$ |
| 9 | $30686$ |
| 10 | $52500$ |

---

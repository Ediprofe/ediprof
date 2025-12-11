# 🔬 Descomposición en Factores Primos

En este tema aprenderemos a expresar cualquier número como producto de números primos.

---

## 📖 ¿Qué es la factorización prima?

La **descomposición en factores primos** expresa un número como producto de primos.

$$
\text{Número} = p_1^{a_1} \times p_2^{a_2} \times \cdots
$$

---

## 📖 Método de divisiones sucesivas

Dividimos el número entre primos comenzando por el menor posible.

### Ejemplo 1: Descomponer 60

<div id="jsxgraph-fact60" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 220px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-fact60')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-fact60', {
      boundingbox: [-0.5, 5.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Línea vertical divisora
    board.create('segment', [[2, 5], [2, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Números a la izquierda
    board.create('text', [1, 4.5, '60'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 3.5, '30'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '15'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.5, '5'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 0.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Factores primos a la derecha
    board.create('text', [2.5, 4.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 3.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 2.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 1.5, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0.3, 4-i], [2.8, 4-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Dividimos sucesivamente entre primos hasta llegar a 1.

$$
60 = 2^2 \times 3 \times 5
$$

---

### Ejemplo 2: Descomponer 84

<div id="jsxgraph-fact84" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 220px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-fact84')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-fact84', {
      boundingbox: [-0.5, 5.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Línea vertical divisora
    board.create('segment', [[2, 5], [2, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Números a la izquierda
    board.create('text', [1, 4.5, '84'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 3.5, '42'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '21'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.5, '7'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 0.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Factores primos a la derecha
    board.create('text', [2.5, 4.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 3.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 2.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 1.5, '7'], {fontSize: 18, strokeColor: '#8b5cf6', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0.3, 4-i], [2.8, 4-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.unsuspendUpdate();
  }
});
</script>

$$
84 = 2^2 \times 3 \times 7
$$

---

### Ejemplo 3: Descomponer 72

<div id="jsxgraph-fact72" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 280px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-fact72')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-fact72', {
      boundingbox: [-0.5, 6.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Línea vertical divisora
    board.create('segment', [[2, 6], [2, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // 72 → 36 → 18 → 9 → 3 → 1
    board.create('text', [1, 5.5, '72'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 4.5, '36'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 3.5, '18'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '9'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.5, '3'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 0.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Factores primos
    board.create('text', [2.5, 5.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 4.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 3.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 2.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 1.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 5; i++) {
      board.create('segment', [[0.3, 5-i], [2.8, 5-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.unsuspendUpdate();
  }
});
</script>

$$
72 = 2^3 \times 3^2
$$

---

### Ejemplo 4: Descomponer 150

<div id="jsxgraph-fact150" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 250px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-fact150')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-fact150', {
      boundingbox: [-0.5, 5.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Línea vertical divisora
    board.create('segment', [[2, 5], [2, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // 150 → 75 → 25 → 5 → 1
    board.create('text', [1, 4.5, '150'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 3.5, '75'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '25'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.5, '5'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 0.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Factores primos
    board.create('text', [2.5, 4.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 3.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 2.5, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 1.5, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0.3, 4-i], [2.8, 4-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.unsuspendUpdate();
  }
});
</script>

$$
150 = 2 \times 3 \times 5^2
$$

---

## 📖 Método del árbol de factores

Descomponemos en cualquier par de factores y seguimos hasta llegar a primos.

### Ejemplo 1: Descomponer 36

<div id="jsxgraph-arbol36" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-arbol36')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-arbol36', {
      boundingbox: [-0.5, 4.5, 7, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Nivel 0: 36
    board.create('text', [3.5, 4, '36'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas
    board.create('segment', [[3.2, 3.6], [1.8, 2.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.8, 3.6], [5.2, 2.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 1: 6 × 6
    board.create('text', [1.5, 2.5, '6'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.5, 2.5, '6'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas nivel 1
    board.create('segment', [[1.2, 2.1], [0.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[1.8, 2.1], [2.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[5.2, 2.1], [4.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[5.8, 2.1], [6.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 2: primos (2 × 3) y (2 × 3)
    board.create('text', [0.3, 0.9, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 0.9, '3'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.3, 0.9, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [6.7, 0.9, '3'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Resultado
    board.create('text', [3.5, 0.2, '36 = 2² × 3²'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
36 = 6 \times 6 = (2 \times 3) \times (2 \times 3) = 2^2 \times 3^2
$$

---

### Ejemplo 2: Descomponer 100

<div id="jsxgraph-arbol100" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-arbol100')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-arbol100', {
      boundingbox: [-0.5, 4.5, 7, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Nivel 0: 100
    board.create('text', [3.5, 4, '100'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas
    board.create('segment', [[3.2, 3.6], [1.8, 2.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.8, 3.6], [5.2, 2.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 1: 10 × 10
    board.create('text', [1.5, 2.5, '10'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.5, 2.5, '10'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas nivel 1
    board.create('segment', [[1.2, 2.1], [0.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[1.8, 2.1], [2.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[5.2, 2.1], [4.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[5.8, 2.1], [6.5, 1.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 2: primos (2 × 5) y (2 × 5)
    board.create('text', [0.3, 0.9, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 0.9, '5'], {fontSize: 16, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.3, 0.9, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [6.7, 0.9, '5'], {fontSize: 16, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Resultado
    board.create('text', [3.5, 0.2, '100 = 2² × 5²'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
100 = 10 \times 10 = (2 \times 5) \times (2 \times 5) = 2^2 \times 5^2
$$

---

### Ejemplo 3: Descomponer 48

<div id="jsxgraph-arbol48" class="jsxgraph-container" style="width: 100%; max-width: 400px; height: 250px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-arbol48')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-arbol48', {
      boundingbox: [-0.5, 5.5, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Nivel 0: 48
    board.create('text', [4, 5, '48'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas nivel 0
    board.create('segment', [[3.7, 4.6], [2, 3.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[4.3, 4.6], [6, 3.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 1: 6 × 8
    board.create('text', [2, 3.5, '6'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [6, 3.5, '8'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas nivel 1
    board.create('segment', [[1.7, 3.1], [1, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[2.3, 3.1], [3, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[5.7, 3.1], [5, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[6.3, 3.1], [7, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 2: 2×3 y 2×4
    board.create('text', [1, 2, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2, '3'], {fontSize: 15, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5, 2, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [7, 2, '4'], {fontSize: 15, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas del 4
    board.create('segment', [[6.7, 1.6], [6.2, 0.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[7.3, 1.6], [7.8, 0.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 3: 2×2
    board.create('text', [6.2, 0.6, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [7.8, 0.6, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Resultado
    board.create('text', [4, 0.1, '48 = 2⁴ × 3'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
48 = 6 \times 8 = (2 \times 3) \times (2 \times 4) = 2^4 \times 3
$$

---

### Ejemplo 4: Descomponer 72

<div id="jsxgraph-arbol72" class="jsxgraph-container" style="width: 100%; max-width: 400px; height: 250px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-arbol72')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-arbol72', {
      boundingbox: [-0.5, 5.5, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Nivel 0: 72
    board.create('text', [4, 5, '72'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas nivel 0
    board.create('segment', [[3.7, 4.6], [2, 3.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[4.3, 4.6], [6, 3.8]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 1: 8 × 9
    board.create('text', [2, 3.5, '8'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [6, 3.5, '9'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas nivel 1
    board.create('segment', [[1.7, 3.1], [1, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[2.3, 3.1], [3, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[5.7, 3.1], [5, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[6.3, 3.1], [7, 2.3]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 2: 2×4 y 3×3
    board.create('text', [1, 2, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2, '4'], {fontSize: 15, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5, 2, '3'], {fontSize: 15, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [7, 2, '3'], {fontSize: 15, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ramas del 4
    board.create('segment', [[2.7, 1.6], [2.2, 0.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.3, 1.6], [3.8, 0.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Nivel 3: 2×2
    board.create('text', [2.2, 0.6, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.8, 0.6, '2'], {fontSize: 15, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Resultado
    board.create('text', [4, 0.1, '72 = 2³ × 3²'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
72 = 8 \times 9 = (2 \times 4) \times (3 \times 3) = 2^3 \times 3^2
$$

---

## 📖 Unicidad de la descomposición

Todo número compuesto tiene una **única** descomposición en factores primos (Teorema Fundamental de la Aritmética).

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Descompón $72$ en factores primos.

**Ejercicio 2:** Descompón $150$ en factores primos.

**Ejercicio 3:** Expresa $200$ como producto de potencias de primos.

**Ejercicio 4:** Si $n = 2^3 \times 5^2$, ¿cuánto vale $n$?

---

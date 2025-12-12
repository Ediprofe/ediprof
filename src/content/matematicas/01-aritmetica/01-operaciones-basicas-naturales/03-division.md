# ➗ División de Números Naturales

En este tema aprenderemos a dividir números naturales, donde el **dividendo va a la izquierda** y el **divisor a la derecha**.

---

## 📖 ¿Qué es la división?

La **división** reparte una cantidad en partes iguales. Es la operación inversa de la multiplicación.

$$
\text{dividendo} \div \text{divisor} = \text{cociente}
$$

---

## 📖 Divisiones exactas

Una división es **exacta** cuando el residuo es **cero**.

### Ejemplo 1

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 350px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div1" class="jsxgraph-container" style="width: 100%; height: 200px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div1', {
      boundingbox: [-0.5, 5, 7, 0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 56
    board.create('text', [1, 4, '5'], {fontSize: 26, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.9, 4, '6'], {fontSize: 26, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[2.6, 4.6], [2.6, 3.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[2.6, 3.2], [4.5, 3.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 8
    board.create('text', [3.4, 4, '8'], {fontSize: 26, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 7
    board.create('text', [3.4, 2.4, '7'], {fontSize: 26, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Desarrollo: 8 × 7 = 56
    board.create('text', [1, 2.8, '5'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.9, 2.8, '6'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 2.5], [2.3, 2.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 0
    board.create('text', [1.9, 1.8, '0'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $8 \times 7 = 56$. Resto: $56 - 56 = 0$ ✓

---

### Ejemplo 2

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 400px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div2" class="jsxgraph-container" style="width: 100%; height: 260px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div2', {
      boundingbox: [-0.5, 6, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 144
    board.create('text', [1, 5, '1'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 5, '4'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 5, '4'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.3, 5.6], [3.3, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.3, 4.2], [5.8, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 12
    board.create('text', [4, 5, '1'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.7, 5, '2'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 12
    board.create('text', [4, 3.4, '1'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.7, 3.4, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Desarrollo: 12 × 1 = 12
    board.create('text', [1, 3.8, '1'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 3.8, '2'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 3.5], [2.2, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 14 - 12 = 2, baja 4 → 24
    board.create('text', [1.8, 2.9, '2'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.9, '4'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 12 × 2 = 24
    board.create('text', [1.8, 2.2, '2'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.2, '4'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.4, 1.9], [3, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 0
    board.create('text', [2.6, 1.3, '0'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $12 \times 1 = 12$. Resto: $14 - 12 = 2$
2. Bajo el 4 → 24. $12 \times 2 = 24$. Resto: $0$ ✓

---

### Ejemplo 3

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 400px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div3" class="jsxgraph-container" style="width: 100%; height: 300px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div3', {
      boundingbox: [-0.5, 6, 8, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 245
    board.create('text', [1, 5, '2'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.9, 5, '4'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.8, 5, '5'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.5, 5.6], [3.5, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.5, 4.2], [6, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 7
    board.create('text', [4.5, 5, '7'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 35
    board.create('text', [4.2, 3.4, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.1, 3.4, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 7 × 3 = 21
    board.create('text', [1, 3.8, '2'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.9, 3.8, '1'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 3.5], [2.3, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 24 - 21 = 3, baja 5 → 35
    board.create('text', [1.9, 2.9, '3'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.8, 2.9, '5'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 7 × 5 = 35
    board.create('text', [1.9, 2.2, '3'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.8, 2.2, '5'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.5, 1.9], [3.2, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 0
    board.create('text', [2.8, 1.3, '0'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $7 \times 3 = 21$. Resto: $24 - 21 = 3$
2. Bajo el 5 → 35. $7 \times 5 = 35$. Resto: $0$ ✓

---

## 📖 Divisiones con residuo

Una división tiene **residuo** cuando no es exacta. El residuo siempre debe ser **menor que el divisor**.

### Ejemplo 4

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 400px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div4" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div4')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div4', {
      boundingbox: [-0.5, 6, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 83
    board.create('text', [1, 5, '8'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 5, '3'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[2.5, 5.6], [2.5, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[2.5, 4.2], [4.8, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 6
    board.create('text', [3.5, 5, '6'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 13
    board.create('text', [3.2, 3.4, '1'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 3.4, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 6 × 1 = 6
    board.create('text', [1, 3.8, '6'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 3.5], [1.4, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 8 - 6 = 2, baja 3 → 23
    board.create('text', [1, 2.9, '2'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 2.9, '3'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 6 × 3 = 18
    board.create('text', [1, 2.2, '1'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 2.2, '8'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 1.9], [2.2, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 5
    board.create('text', [1.8, 1.3, '5'], {fontSize: 20, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.8, 1.3, '← residuo'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $6 \times 1 = 6$. Resto: $8 - 6 = 2$
2. Bajo el 3 → 23. $6 \times 3 = 18$. Resto: $23 - 18 = 5$

---

### Ejemplo 5

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 400px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div5" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div5')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div5', {
      boundingbox: [-0.5, 6, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 100
    board.create('text', [1, 5, '1'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 5, '0'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 5, '0'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.3, 5.6], [3.3, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.3, 4.2], [5.5, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 7
    board.create('text', [4.2, 5, '7'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 14
    board.create('text', [4, 3.4, '1'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.8, 3.4, '4'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 7 × 1 = 7
    board.create('text', [1.8, 3.8, '7'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.4, 3.5], [2.2, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 10 - 7 = 3, baja 0 → 30
    board.create('text', [1.8, 2.9, '3'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.9, '0'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 7 × 4 = 28
    board.create('text', [1.8, 2.2, '2'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.2, '8'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.4, 1.9], [3, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 2
    board.create('text', [2.6, 1.3, '2'], {fontSize: 20, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
- $7 \times 1 = 7$. Resto: $10 - 7 = 3$
- Bajo el 0 → 30. $7 \times 4 = 28$. Resto: $30 - 28 = 2$

**Verificación:** $7 \times 14 + 2 = 98 + 2 = 100$ ✓

---

### Ejemplo 6

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 400px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div6" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div6')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div6', {
      boundingbox: [-0.5, 6, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 500
    board.create('text', [1, 5, '5'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 5, '0'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 5, '0'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.3, 5.6], [3.3, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.3, 4.2], [5.8, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 15
    board.create('text', [4, 5, '1'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.7, 5, '5'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 33
    board.create('text', [4, 3.4, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.7, 3.4, '3'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 15 × 3 = 45
    board.create('text', [1, 3.8, '4'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 3.8, '5'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 3.5], [2.2, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 50 - 45 = 5, baja 0 → 50
    board.create('text', [1.8, 2.9, '5'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.9, '0'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 15 × 3 = 45
    board.create('text', [1.8, 2.2, '4'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.2, '5'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.4, 1.9], [3, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 5
    board.create('text', [2.6, 1.3, '5'], {fontSize: 20, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $15 \times 3 = 45$. Resto: $50 - 45 = 5$
2. Bajo el 0 → 50. $15 \times 3 = 45$. Resto: $50 - 45 = 5$

**Verificación:** $15 \times 33 + 5 = 495 + 5 = 500$ ✓

---

### Ejemplo 7

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div7" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div7', {
      boundingbox: [-0.5, 6, 9, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 1000
    board.create('text', [1, 5, '1'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.7, 5, '0'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.4, 5, '0'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.1, 5, '0'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.8, 5.6], [3.8, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.8, 4.2], [6.3, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 23
    board.create('text', [4.5, 5, '2'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 5, '3'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 43
    board.create('text', [4.5, 3.4, '4'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 3.4, '3'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 23 × 4 = 92
    board.create('text', [1.7, 3.8, '9'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.4, 3.8, '2'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.3, 3.5], [2.8, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 100 - 92 = 8, baja 0 → 80
    board.create('text', [2.4, 2.9, '8'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 2.9, '0'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 23 × 3 = 69
    board.create('text', [2.4, 2.2, '6'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 2.2, '9'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[2, 1.9], [3.5, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 11
    board.create('text', [2.4, 1.3, '1'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.1, 1.3, '1'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $23 \times 4 = 92$. Resto: $100 - 92 = 8$
2. Bajo el 0 → 80. $23 \times 3 = 69$. Resto: $80 - 69 = 11$

**Verificación:** $23 \times 43 + 11 = 989 + 11 = 1000$ ✓

---

### Ejemplo 8

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div8" class="jsxgraph-container" style="width: 100%; height: 320px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div8')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div8', {
      boundingbox: [-0.5, 7, 10, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 1728
    board.create('text', [1, 6, '1'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.7, 6, '7'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.4, 6, '2'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.1, 6, '8'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.8, 6.5], [3.8, 5.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.8, 5.2], [6.5, 5.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 24
    board.create('text', [4.5, 6, '2'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 6, '4'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 72
    board.create('text', [4.5, 4.4, '7'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 4.4, '2'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 24 × 7 = 168
    board.create('text', [1, 4.8, '1'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.7, 4.8, '6'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.4, 4.8, '8'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 4.5], [2.8, 4.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 172 - 168 = 4, baja 8 → 48
    board.create('text', [2.4, 3.9, '4'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 3.9, '8'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 24 × 2 = 48
    board.create('text', [2.4, 3.2, '4'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 3.2, '8'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[2, 2.9], [3.5, 2.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 0
    board.create('text', [3.1, 2.3, '0'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $24 \times 7 = 168$. Resto: $172 - 168 = 4$
2. Bajo el 8 → 48. $24 \times 2 = 48$. Resto: $0$ ✓

---

### Ejemplo 9

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div9" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div9')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div9', {
      boundingbox: [-0.5, 6, 9, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 2500
    board.create('text', [1, 5, '2'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.7, 5, '5'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.4, 5, '0'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.1, 5, '0'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.8, 5.6], [3.8, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.8, 4.2], [6.3, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 35
    board.create('text', [4.5, 5, '3'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 5, '5'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 71
    board.create('text', [4.5, 3.4, '7'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 3.4, '1'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 35 × 7 = 245
    board.create('text', [1, 3.8, '2'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.7, 3.8, '4'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.4, 3.8, '5'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 3.5], [2.8, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 250 - 245 = 5, baja 0 → 50
    board.create('text', [2.4, 2.9, '5'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 2.9, '0'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 35 × 1 = 35
    board.create('text', [2.4, 2.2, '3'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 2.2, '5'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[2, 1.9], [3.5, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 15
    board.create('text', [2.4, 1.3, '1'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.1, 1.3, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $35 \times 7 = 245$. Resto: $250 - 245 = 5$
2. Bajo el 0 → 50. $35 \times 1 = 35$. Resto: $50 - 35 = 15$

**Verificación:** $35 \times 71 + 15 = 2485 + 15 = 2500$ ✓

---

### Ejemplo 10

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div10" class="jsxgraph-container" style="width: 100%; height: 340px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div10')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div10', {
      boundingbox: [-0.5, 7.5, 9, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 9999
    board.create('text', [1, 6.5, '9'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.7, 6.5, '9'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.4, 6.5, '9'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.1, 6.5, '9'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.8, 7.1], [3.8, 5.7]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.8, 5.7], [6.5, 5.7]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 11
    board.create('text', [4.5, 6.5, '1'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.2, 6.5, '1'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 909
    board.create('text', [4.2, 4.9, '9'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.9, 4.9, '0'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.6, 4.9, '9'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 11 × 9 = 99
    board.create('text', [1, 5.3, '9'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.7, 5.3, '9'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 5], [2.1, 5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 99 - 99 = 0, baja 9 → 9
    board.create('text', [1.7, 4.4, '0'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.4, 4.4, '9'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 11 × 0 = 0
    board.create('text', [2.4, 3.7, '0'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[2, 3.4], [2.8, 3.4]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 9 - 0 = 9, baja 9 → 99
    board.create('text', [2.4, 2.8, '9'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 2.8, '9'], {fontSize: 15, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 11 × 9 = 99
    board.create('text', [2.4, 2.1, '9'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [3.1, 2.1, '9'], {fontSize: 15, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[2, 1.8], [3.5, 1.8]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 0
    board.create('text', [3.1, 1.2, '0'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:**
1. $11 \times 9 = 99$. Resto: $99 - 99 = 0$
2. Bajo el 9 → 9. $11 \times 0 = 0$. Resto: $9 - 0 = 9$
3. Bajo el 9 → 99. $11 \times 9 = 99$. Resto: $99 - 99 = 0$ ✓

---

## 📖 Verificación de la división

Para comprobar que una división es correcta:

$$
\text{dividendo} = \text{divisor} \times \text{cociente} + \text{residuo}
$$

### Ejemplo

Para $83 \div 6 = 13$ (residuo 5):

$$
83 = 6 \times 13 + 5 = 78 + 5 = 83 \quad ✓
$$

---

## 📝 Ejercicios de práctica

| Ejercicio | Operación |
|:---------:|:----------|
| 1 | $72 \div 9$ |
| 2 | $84 \div 7$ |
| 3 | $96 \div 8$ |
| 4 | $125 \div 5$ |
| 5 | $156 \div 12$ |
| 6 | $89 \div 6$ (indicar cociente y residuo) |
| 7 | $250 \div 15$ (indicar cociente y residuo) |
| 8 | $1000 \div 8$ |
| 9 | $2340 \div 45$ |
| 10 | $5678 \div 23$ (indicar cociente y residuo) |

---

## ✅ Soluciones

| Ejercicio | Solución |
|:---------:|:---------|
| 1 | $8$ |
| 2 | $12$ |
| 3 | $12$ |
| 4 | $25$ |
| 5 | $13$ |
| 6 | Cociente: $14$, Residuo: $5$ |
| 7 | Cociente: $16$, Residuo: $10$ |
| 8 | $125$ |
| 9 | $52$ |
| 10 | Cociente: $246$, Residuo: $20$ |

---

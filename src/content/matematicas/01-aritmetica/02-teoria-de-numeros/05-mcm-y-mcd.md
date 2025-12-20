# 🔗 MCM y MCD

En este tema aprenderemos a calcular el Mínimo Común Múltiplo (MCM) y el Máximo Común Divisor (MCD).

---

## 📖 Máximo Común Divisor (MCD)

El **MCD** es el mayor número que divide exactamente a dos o más números.

### Método por factorización simultánea

Descomponemos ambos números al mismo tiempo, dividiendo por primos que dividan al menos a uno de ellos.

### Ejemplo 1: MCD de 12 y 18

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mcd1" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mcd1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mcd1', {
      boundingbox: [-0.5, 6, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Líneas divisoras
    board.create('segment', [[1.5, 5.5], [1.5, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    board.create('segment', [[3, 5.5], [3, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Encabezados
    board.create('text', [0.7, 5.5, '12'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 5.5, '18'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Fila 1: ÷2
    board.create('text', [0.7, 4.5, '6'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 4.5, '9'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 4.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // Fila 2: ÷3
    board.create('text', [0.7, 3.5, '2'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 3.5, '3'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    // Fila 3: ÷2
    board.create('text', [0.7, 2.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 2.5, '2'], {fontSize: 16, strokeColor: '#94a3b8', fixed: true, cssStyle: 'font-weight: bold;'});
    // Fila 4: ÷3
    board.create('text', [0.7, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 1.5, '3'], {fontSize: 16, strokeColor: '#94a3b8', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0, 5-i], [4.2, 5-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    // Resultado
    board.create('text', [2, 0.5, 'MCD = 2 × 3 = 6'], {fontSize: 14, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5, 3.5, '← comunes'], {fontSize: 11, strokeColor: '#22c55e', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Para el **MCD**: multiplicamos solo los primos que dividen **a ambos números** (filas donde ambos cambian).

$$
\text{MCD}(12, 18) = 2 \times 3 = 6
$$

---

### Ejemplo 2: MCD de 24 y 36

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mcd2" class="jsxgraph-container" style="width: 100%; height: 300px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mcd2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mcd2', {
      boundingbox: [-0.5, 6.5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[1.5, 6], [1.5, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    board.create('segment', [[3, 6], [3, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Encabezados
    board.create('text', [0.7, 5.8, '24'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 5.8, '36'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // 24÷2=12, 36÷2=18
    board.create('text', [0.7, 4.8, '12'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 4.8, '18'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 4.8, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // 12÷2=6, 18÷2=9
    board.create('text', [0.7, 3.8, '6'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.8, '9'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 3.8, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // 6÷3=2, 9÷3=3
    board.create('text', [0.7, 2.8, '2'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.8, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 2.8, '3'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    // Resto
    board.create('text', [0.7, 1.8, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.8, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 1.8, '2'], {fontSize: 16, strokeColor: '#94a3b8', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [0.7, 0.8, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 0.8, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 0.8, '3'], {fontSize: 16, strokeColor: '#94a3b8', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 5; i++) {
      board.create('segment', [[0, 5.3-i], [4.2, 5.3-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.create('text', [2, 0.1, 'MCD = 2 × 2 × 3 = 12'], {fontSize: 14, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
\text{MCD}(24, 36) = 2^2 \times 3 = 12
$$

---

## 📖 Mínimo Común Múltiplo (MCM)

El **MCM** es el menor número que es múltiplo de dos o más números.

### Método por factorización simultánea

Usamos el mismo proceso, pero multiplicamos **todos** los factores primos.

### Ejemplo 1: MCM de 12 y 18

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mcm1" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mcm1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mcm1', {
      boundingbox: [-0.5, 6, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[1.5, 5.5], [1.5, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    board.create('segment', [[3, 5.5], [3, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Encabezados
    board.create('text', [0.7, 5.5, '12'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 5.5, '18'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Filas
    board.create('text', [0.7, 4.5, '6'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 4.5, '9'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 4.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [0.7, 3.5, '2'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 3.5, '3'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [0.7, 2.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 2.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [0.7, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 1.5, '3'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0, 5-i], [4.2, 5-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.create('text', [2, 0.5, 'MCM = 2×3×2×3 = 36'], {fontSize: 14, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5, 3, '← todos'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Para el **MCM**: multiplicamos **todos** los primos de la columna derecha.

$$
\text{MCM}(12, 18) = 2 \times 3 \times 2 \times 3 = 36
$$

---

### Ejemplo 2: MCM de 8 y 12

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mcm2" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mcm2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mcm2', {
      boundingbox: [-0.5, 6, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[1.5, 5.5], [1.5, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    board.create('segment', [[3, 5.5], [3, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // 8 y 12
    board.create('text', [0.7, 5.5, '8'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 5.5, '12'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // ÷2
    board.create('text', [0.7, 4.5, '4'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 4.5, '6'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 4.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // ÷2
    board.create('text', [0.7, 3.5, '2'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 3.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // ÷2
    board.create('text', [0.7, 2.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 2.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // ÷3
    board.create('text', [0.7, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 1.5, '3'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0, 5-i], [4.2, 5-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.create('text', [2, 0.5, 'MCM = 2×2×2×3 = 24'], {fontSize: 14, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
\text{MCM}(8, 12) = 2^3 \times 3 = 24
$$

---

## 📖 Relación entre MCM y MCD

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-relacion" class="jsxgraph-container" style="width: 100%; height: 180px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-relacion')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-relacion', {
      boundingbox: [-0.5, 4, 9, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Caja de fórmula
    board.create('polygon', [[0.5, 3.6], [8.5, 3.6], [8.5, 2.6], [0.5, 2.6]], {fillColor: '#dbeafe', fillOpacity: 0.5, strokeColor: '#3b82f6', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [4.5, 3.1, 'MCM(a,b) × MCD(a,b) = a × b'], {fontSize: 16, strokeColor: '#1e40af', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Ejemplo
    board.create('text', [4.5, 1.8, 'Ejemplo: 12 y 18'], {fontSize: 13, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // MCM × MCD = a × b
    board.create('text', [1.5, 0.8, '36'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 0.8, '×'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [2.9, 0.8, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.6, 0.8, '='], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [4.5, 0.8, '216'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5.4, 0.8, '='], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [6.2, 0.8, '12'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [6.9, 0.8, '×'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [7.6, 0.8, '18'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Etiquetas
    board.create('text', [1.5, 0.2, 'MCM'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [2.9, 0.2, 'MCD'], {fontSize: 10, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [6.9, 0.2, 'a × b'], {fontSize: 10, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    // Check mark
    board.create('text', [8.3, 0.8, '✓'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
\text{MCM}(a, b) \times \text{MCD}(a, b) = a \times b
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula el MCD de $30$ y $45$.

**Ejercicio 2:** Calcula el MCM de $15$ y $20$.

**Ejercicio 3:** Calcula el MCD y MCM de $24$ y $60$.

**Ejercicio 4:** Si MCD$(a, 12) = 4$ y MCM$(a, 12) = 60$, ¿cuánto vale $a$?

---

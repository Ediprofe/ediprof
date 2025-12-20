# 🔢 Múltiplos y Divisores

En este tema aprenderemos a identificar múltiplos y divisores de un número.

---

## 📖 Múltiplos de un número

Un **múltiplo** de un número es el resultado de multiplicar ese número por cualquier natural.

$$
\text{Múltiplo de } a = a \times n \quad \text{donde } n \in \mathbb{N}
$$

### Ejemplo 1: Múltiplos de 3

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mult3" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult3', {
      boundingbox: [-1, 2, 20, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Recta numérica
    board.create('segment', [[0, 0.8], [18, 0.8]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    // Marcas cada 3 unidades (múltiplos de 3)
    for (var i = 0; i <= 18; i += 3) {
      board.create('point', [i, 0.8], {size: 5, fixed: true, color: '#22c55e', name: String(i), label: {offset: [0, -18], strokeColor: '#22c55e', fontSize: 11}});
    }
    // Marcas intermedias
    for (var i = 0; i <= 18; i++) {
      if (i % 3 !== 0) {
        board.create('point', [i, 0.8], {size: 2, fixed: true, color: '#94a3b8', name: '', withLabel: false});
      }
    }
    board.create('text', [9, 1.6, 'M(3) = {3, 6, 9, 12, 15, 18, ...}'], {fontSize: 12, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Los puntos verdes muestran los múltiplos de 3. Cada salto representa sumar 3.

$$
M(3) = \{3, 6, 9, 12, 15, \ldots\}
$$

---

### Ejemplo 2: Múltiplos de 7

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mult7" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult7', {
      boundingbox: [-2, 2, 40, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Recta numérica
    board.create('segment', [[0, 0.8], [35, 0.8]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    // Marcas cada 7 unidades
    for (var i = 0; i <= 35; i += 7) {
      board.create('point', [i, 0.8], {size: 5, fixed: true, color: '#3b82f6', name: String(i), label: {offset: [0, -18], strokeColor: '#3b82f6', fontSize: 11}});
    }
    board.create('text', [17.5, 1.6, 'M(7) = {7, 14, 21, 28, 35, ...}'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
M(7) = \{7, 14, 21, 28, 35, \ldots\}
$$

---

## 📖 Propiedades de los múltiplos

* Todo número es múltiplo de sí mismo y de $1$
* El cero es múltiplo de cualquier número
* Un número tiene **infinitos** múltiplos

---

## 📖 Divisores de un número

Un **divisor** de un número es aquel que lo divide exactamente (residuo cero).

### Ejemplo 1: Divisores de 12

Los divisores de 12 son aquellos números que permiten dividir 12 unidades en grupos iguales:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div12" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div12')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div12', {
      boundingbox: [-0.5, 5.5, 18, -0.8], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 12 = 3 × 4 (cuadrícula 3 filas, 4 columnas)
    for (var r = 0; r < 3; r++) {
      for (var c = 0; c < 4; c++) {
        board.create('polygon', [[c*1.2, 4.5-r*1.2], [c*1.2+0.9, 4.5-r*1.2], [c*1.2+0.9, 3.6-r*1.2], [c*1.2, 3.6-r*1.2]], {fillColor: '#22c55e', fillOpacity: 0.8, strokeColor: '#166534', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [2.3, 0.4, '3 × 4 = 12'], {fontSize: 13, strokeColor: '#166534', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 12 = 2 × 6 (cuadrícula 2 filas, 6 columnas)
    for (var r = 0; r < 2; r++) {
      for (var c = 0; c < 6; c++) {
        board.create('polygon', [[6+c*0.9, 4.5-r*1.2], [6+c*0.9+0.75, 4.5-r*1.2], [6+c*0.9+0.75, 3.6-r*1.2], [6+c*0.9, 3.6-r*1.2]], {fillColor: '#3b82f6', fillOpacity: 0.8, strokeColor: '#1d4ed8', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [8.3, 0.4, '2 × 6 = 12'], {fontSize: 13, strokeColor: '#1d4ed8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 12 = 1 × 12 (fila horizontal)
    for (var c = 0; c < 12; c++) {
      board.create('polygon', [[12.5+c*0.45, 3.3], [12.5+c*0.45+0.35, 3.3], [12.5+c*0.45+0.35, 4.2], [12.5+c*0.45, 4.2]], {fillColor: '#f59e0b', fillOpacity: 0.8, strokeColor: '#d97706', strokeWidth: 1, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [15.2, 0.4, '1 × 12'], {fontSize: 13, strokeColor: '#d97706', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Título
    board.create('text', [9, 5.2, 'D(12) = {1, 2, 3, 4, 6, 12}'], {fontSize: 15, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Los divisores permiten dividir 12 en grupos iguales sin que sobren unidades.

$$
D(12) = \{1, 2, 3, 4, 6, 12\}
$$

---

### Ejemplo 2: Divisores de 18

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div18" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div18')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div18', {
      boundingbox: [-0.5, 5.5, 18, -0.8], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 18 = 3 × 6
    for (var r = 0; r < 3; r++) {
      for (var c = 0; c < 6; c++) {
        board.create('polygon', [[c*1, 4.5-r*1.2], [c*1+0.8, 4.5-r*1.2], [c*1+0.8, 3.6-r*1.2], [c*1, 3.6-r*1.2]], {fillColor: '#8b5cf6', fillOpacity: 0.8, strokeColor: '#6d28d9', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [2.5, 0.4, '3 × 6 = 18'], {fontSize: 13, strokeColor: '#6d28d9', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 18 = 2 × 9
    for (var r = 0; r < 2; r++) {
      for (var c = 0; c < 9; c++) {
        board.create('polygon', [[6.5+c*0.7, 4.5-r*1.2], [6.5+c*0.7+0.55, 4.5-r*1.2], [6.5+c*0.7+0.55, 3.6-r*1.2], [6.5+c*0.7, 3.6-r*1.2]], {fillColor: '#ec4899', fillOpacity: 0.8, strokeColor: '#be185d', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [9.3, 0.4, '2 × 9 = 18'], {fontSize: 13, strokeColor: '#be185d', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 18 = 1 × 18 (fila)
    for (var c = 0; c < 18; c++) {
      board.create('polygon', [[13+c*0.28, 3.3], [13+c*0.28+0.22, 3.3], [13+c*0.28+0.22, 4.2], [13+c*0.28, 4.2]], {fillColor: '#06b6d4', fillOpacity: 0.8, strokeColor: '#0891b2', strokeWidth: 1, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [15.5, 0.4, '1 × 18'], {fontSize: 13, strokeColor: '#0891b2', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Título
    board.create('text', [9, 5.2, 'D(18) = {1, 2, 3, 6, 9, 18}'], {fontSize: 15, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
D(18) = \{1, 2, 3, 6, 9, 18\}
$$

---

## 📖 Propiedades de los divisores

* El $1$ es divisor de todos los números
* Todo número es divisor de sí mismo
* Un número tiene una cantidad **finita** de divisores

---

## 📖 Relación entre múltiplos y divisores

Si $a$ es múltiplo de $b$, entonces $b$ es divisor de $a$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-relacion" class="jsxgraph-container" style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-relacion')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-relacion', {
      boundingbox: [-1, 3, 10, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Ejemplo: 15 y 5
    board.create('text', [0.5, 2.3, '15 es múltiplo de 5'], {fontSize: 13, strokeColor: '#22c55e', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [6, 2.3, '→'], {fontSize: 16, strokeColor: '#374151', fixed: true});
    board.create('text', [6.8, 2.3, '5 es divisor de 15'], {fontSize: 13, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    // Ejemplo: 24 y 6
    board.create('text', [0.5, 1.0, '24 es múltiplo de 6'], {fontSize: 13, strokeColor: '#22c55e', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [6, 1.0, '→'], {fontSize: 16, strokeColor: '#374151', fixed: true});
    board.create('text', [6.8, 1.0, '6 es divisor de 24'], {fontSize: 13, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Múltiplo ↔ Divisor** son conceptos inversos.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Escribe los primeros 6 múltiplos de $8$.

**Ejercicio 2:** Encuentra todos los divisores de $24$.

**Ejercicio 3:** ¿Es $45$ múltiplo de $9$?

**Ejercicio 4:** ¿Es $7$ divisor de $42$?

---

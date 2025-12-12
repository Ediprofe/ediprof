# 🔢 Números Primos y Compuestos

En este tema aprenderemos a distinguir entre números primos y compuestos.

---

## 📖 Números primos

Un **número primo** es aquel que solo tiene dos divisores: el $1$ y él mismo.

### Ejemplo 1: El número 7 es primo

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 350px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-primo7" class="jsxgraph-container" style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-primo7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-primo7', {
      boundingbox: [-0.5, 2.5, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 7 cuadrados en una sola fila (no se puede dividir en más formas)
    for (var c = 0; c < 7; c++) {
      board.create('polygon', [[c*1.05, 1.8], [c*1.05+0.9, 1.8], [c*1.05+0.9, 1], [c*1.05, 1]], {fillColor: '#22c55e', fillOpacity: 0.8, strokeColor: '#166534', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [3.7, 2.3, '7 = 1 × 7 (única forma)'], {fontSize: 13, strokeColor: '#166534', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 0.4, 'D(7) = {1, 7}'], {fontSize: 12, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Un número primo **solo puede formar una fila** — no se puede dividir de otra manera.

$$
D(7) = \{1, 7\}
$$

---

### Ejemplo 2: El número 13 es primo

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-primo13" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-primo13')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-primo13', {
      boundingbox: [-0.5, 2, 14, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    for (var c = 0; c < 13; c++) {
      board.create('polygon', [[c*1.02, 1.5], [c*1.02+0.85, 1.5], [c*1.02+0.85, 0.7], [c*1.02, 0.7]], {fillColor: '#3b82f6', fillOpacity: 0.8, strokeColor: '#1d4ed8', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [6.5, 0.2, 'D(13) = {1, 13} — Solo 2 divisores ✓'], {fontSize: 12, strokeColor: '#1d4ed8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
D(13) = \{1, 13\}
$$

---

## 📖 Números compuestos

Un **número compuesto** tiene más de dos divisores.

### Ejemplo 1: El número 12 es compuesto

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 700px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-comp12" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-comp12')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-comp12', {
      boundingbox: [-0.5, 5.5, 18, -0.8], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 12 = 3 × 4
    for (var r = 0; r < 3; r++) {
      for (var c = 0; c < 4; c++) {
        board.create('polygon', [[c*1.2, 4.5-r*1.2], [c*1.2+0.9, 4.5-r*1.2], [c*1.2+0.9, 3.6-r*1.2], [c*1.2, 3.6-r*1.2]], {fillColor: '#ef4444', fillOpacity: 0.8, strokeColor: '#b91c1c', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [2.3, 0.4, '3 × 4'], {fontSize: 12, strokeColor: '#b91c1c', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 12 = 2 × 6
    for (var r = 0; r < 2; r++) {
      for (var c = 0; c < 6; c++) {
        board.create('polygon', [[6+c*0.9, 4.5-r*1.2], [6+c*0.9+0.75, 4.5-r*1.2], [6+c*0.9+0.75, 3.6-r*1.2], [6+c*0.9, 3.6-r*1.2]], {fillColor: '#f59e0b', fillOpacity: 0.8, strokeColor: '#d97706', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [8.3, 0.4, '2 × 6'], {fontSize: 12, strokeColor: '#d97706', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 12 = 1 × 12
    for (var c = 0; c < 12; c++) {
      board.create('polygon', [[12.5+c*0.45, 3.3], [12.5+c*0.45+0.35, 3.3], [12.5+c*0.45+0.35, 4.2], [12.5+c*0.45, 4.2]], {fillColor: '#8b5cf6', fillOpacity: 0.8, strokeColor: '#7c3aed', strokeWidth: 1, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [15.2, 0.4, '1 × 12'], {fontSize: 12, strokeColor: '#7c3aed', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [9, 5.2, '12 es COMPUESTO — Múltiples formas de dividirlo'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Un número compuesto se puede **dividir de varias formas** — tiene más de 2 divisores.

$$
D(12) = \{1, 2, 3, 4, 6, 12\} \quad \text{(6 divisores)}
$$

---

### Ejemplo 2: El número 15 es compuesto

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 600px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-comp15" class="jsxgraph-container" style="width: 100%; height: 180px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-comp15')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-comp15', {
      boundingbox: [-0.5, 4, 16, -0.8], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 15 = 3 × 5
    for (var r = 0; r < 3; r++) {
      for (var c = 0; c < 5; c++) {
        board.create('polygon', [[c*1.1, 3.2-r*1.1], [c*1.1+0.9, 3.2-r*1.1], [c*1.1+0.9, 2.2-r*1.1], [c*1.1, 2.2-r*1.1]], {fillColor: '#ec4899', fillOpacity: 0.8, strokeColor: '#be185d', strokeWidth: 2, fixed: true, vertices: {visible: false}});
      }
    }
    board.create('text', [2.7, -0.3, '3 × 5 = 15'], {fontSize: 12, strokeColor: '#be185d', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // 15 = 1 × 15
    for (var c = 0; c < 15; c++) {
      board.create('polygon', [[6.5+c*0.6, 1.8], [6.5+c*0.6+0.48, 1.8], [6.5+c*0.6+0.48, 2.6], [6.5+c*0.6, 2.6]], {fillColor: '#06b6d4', fillOpacity: 0.8, strokeColor: '#0891b2', strokeWidth: 1, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [11.5, -0.3, '1 × 15'], {fontSize: 12, strokeColor: '#0891b2', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [8, 3.6, 'D(15) = {1, 3, 5, 15} — 4 divisores'], {fontSize: 13, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

$$
D(15) = \{1, 3, 5, 15\}
$$

---

## 📖 Casos especiales

* El número $1$ **no es primo ni compuesto**
* El número $2$ es el único primo par

---

## 📖 Primeros números primos

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 700px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-primos-lista" class="jsxgraph-container" style="width: 100%; height: 80px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-primos-lista')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-primos-lista', {
      boundingbox: [-0.5, 2, 16, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47];
    for (var i = 0; i < primos.length; i++) {
      board.create('polygon', [[i*1.03, 1.5], [i*1.03+0.9, 1.5], [i*1.03+0.9, 0.7], [i*1.03, 0.7]], {fillColor: '#22c55e', fillOpacity: 0.8, strokeColor: '#166534', strokeWidth: 1, fixed: true, vertices: {visible: false}});
      board.create('text', [i*1.03+0.45, 1.1, String(primos[i])], {fontSize: 10, strokeColor: '#fff', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    }
    board.create('text', [7.5, 0.2, '← Primeros 15 números primos →'], {fontSize: 11, strokeColor: '#166534', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \ldots
$$

---

## 📖 Cómo identificar si un número es primo

Para saber si $n$ es primo, verificamos si tiene divisores entre $2$ y $\sqrt{n}$.

### Ejemplo 1

¿Es $29$ primo?

$\sqrt{29} \approx 5.4$, verificamos divisibilidad por 2, 3, 5:
- No es par
- $2+9 = 11$ (no múltiplo de 3)
- No termina en 0 o 5

$29$ **es primo** ✓

---

### Ejemplo 2

¿Es $51$ primo?

$\sqrt{51} \approx 7.1$, verificamos por 2, 3, 5, 7:
- $5+1 = 6$ (múltiplo de 3)
- $51 = 3 \times 17$

$51$ **no es primo** ✗

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Clasifica como primo o compuesto: $23$, $35$, $41$.

**Ejercicio 2:** Escribe todos los números primos menores que $30$.

**Ejercicio 3:** ¿Es $97$ un número primo?

**Ejercicio 4:** Encuentra los divisores de $28$ y clasifícalo.

---

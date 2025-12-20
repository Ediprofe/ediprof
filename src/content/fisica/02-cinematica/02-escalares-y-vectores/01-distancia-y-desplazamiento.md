# 📏 Distancia vs. Desplazamiento

Aunque en la vida diaria usamos estas palabras indistintamente, en física representan conceptos totalmente distintos. Es fundamental diferenciar entre "cuánto me moví" y "dónde terminé".

---

## 👣 Distancia

Es una magnitud **escalar** que mide la **longitud total del camino recorrido**.

* **Significado:** Es la suma de todos los pasos dados, sin importar la dirección.
* **Signo:** Siempre es positiva (+). Nunca resta.
* **Fórmula:** Suma de los valores absolutos de cada tramo.

$$
d = |d_1| + |d_2| + |d_3| + \dots
$$

---

## 📍 Desplazamiento

Es una magnitud **vectorial** que mide el **cambio de posición** desde el punto de inicio hasta el punto final.

* **Significado:** Es la línea recta que une el inicio con el final.
* **Signo:** Puede ser positivo, negativo o cero.
* **Fórmula:** Posición final menos posición inicial.

$$
\Delta x = x_f - x_i
$$

---

## ⚙️ Ejercicio 1 — El Tenista

Un tenista comienza en la línea de fondo ($x=0$ m), corre hasta la red ubicada a 12 m, y luego retrocede hasta la línea de saque, ubicada a 6 m.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tenista" class="jsxgraph-container" style="width: 100%; height: 150px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-tenista')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-tenista', {
      boundingbox: [-1, 4, 14, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 1], [12, 1]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 1], {name: 'Fondo (0m)', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -25], strokeColor: '#22c55e'}});
    board.create('point', [12, 1], {name: 'Red (12m)', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -25], strokeColor: '#3b82f6'}});
    board.create('point', [6, 1], {name: 'Saque (6m)', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -25], strokeColor: '#ef4444'}});
    board.create('arrow', [[0, 2.5], [12, 2.5]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('arrow', [[12, 2.2], [6, 2.2]], {strokeColor: '#ef4444', strokeWidth: 2, fixed: true});
    board.create('text', [6, 3.2, '12 m →'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [9, 1.7, '← 6 m'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### ✅ Solución

**Distancia:** Suma de todos los tramos recorridos.

$$d = 12 + 6 = 18\ \text{m}$$

**Desplazamiento:** Posición final menos posición inicial.

$$\Delta x = 6 - 0 = +6\ \text{m}$$

---

## ⚙️ Ejercicio 2 — El Ascensor

El ascensor sube de 0 m a 20 m, luego baja hasta -4 m.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-ascensor" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-ascensor')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-ascensor', {
      boundingbox: [-3, 25, 5, -8], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, -4], [0, 20]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 0], {name: 'Inicio (0m)', size: 4, fixed: true, color: '#22c55e', label: {offset: [10, 0], strokeColor: '#22c55e'}});
    board.create('point', [0, 20], {name: '20m', size: 4, fixed: true, color: '#3b82f6', label: {offset: [10, 0], strokeColor: '#3b82f6'}});
    board.create('point', [0, -4], {name: '-4m', size: 4, fixed: true, color: '#ef4444', label: {offset: [10, 0], strokeColor: '#ef4444'}});
    board.create('arrow', [[-1.5, 0], [-1.5, 20]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('arrow', [[-2.2, 20], [-2.2, -4]], {strokeColor: '#ef4444', strokeWidth: 2, fixed: true});
    board.create('text', [-2.5, 10, '20m ↑'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'right'});
    board.create('text', [-3, 8, '24m ↓'], {fontSize: 10, strokeColor: '#ef4444', fixed: true, anchorX: 'right'});
    board.unsuspendUpdate();
  }
});
</script>

### ✅ Solución

**Distancia:**

$$d = 20 + 24 = 44\ \text{m}$$

**Desplazamiento:**

$$\Delta x = -4 - 0 = -4\ \text{m}$$

---

## ⚙️ Ejercicio 3 — Vuelta a la Manzana

Una persona recorre una pista circular de 400 m y termina en el mismo punto.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-circular" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-circular')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-circular', {
      boundingbox: [-4, 4, 4, -4], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('circle', [[0, 0], 2.5], {strokeColor: '#3b82f6', strokeWidth: 3, fillColor: 'transparent', fixed: true});
    board.create('point', [2.5, 0], {name: 'Inicio/Fin', size: 5, fixed: true, color: '#22c55e', label: {offset: [10, 0], strokeColor: '#22c55e'}});
    board.create('arrow', [[0, 2.5], [1.5, 2]], {strokeColor: '#f59e0b', strokeWidth: 2, fixed: true});
    board.create('text', [0, 3.2, '400 m recorridos'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [0, -3.2, 'Desplazamiento = 0'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### ✅ Solución

**Distancia:**

$$d = 400\ \text{m}$$

**Desplazamiento:**

$$\Delta x = 0$$ (regresó al punto de partida)

---

## ⚙️ Ejercicio 4 — Caminata en Dos Dimensiones

Camina 30 m al norte y luego 40 m al este.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-2d" class="jsxgraph-container" style="width: 100%; height: 300px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-2d')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-2d', {
      boundingbox: [-10, 38, 48, -5], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var A = board.create('point', [0, 0], {name: 'Inicio', size: 4, fixed: true, color: '#22c55e', label: {offset: [-15, -15], strokeColor: '#22c55e'}});
    var B = board.create('point', [0, 30], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    var C = board.create('point', [40, 30], {name: 'Fin', size: 4, fixed: true, color: '#ef4444', label: {offset: [10, 0], strokeColor: '#ef4444'}});
    board.create('arrow', [A, B], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('arrow', [B, C], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('arrow', [A, C], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2, fixed: true});
    board.create('text', [-9, 15, '30m ↑'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [20, 33, '40m →'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [22, 12, 'Δx = 50m'], {fontSize: 12, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

### ✅ Solución

**Distancia:**

$$d = 30 + 40 = 70\ \text{m}$$

**Desplazamiento (Pitágoras):**

$$\Delta x = \sqrt{30^2 + 40^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50\ \text{m}$$

> 💡 **Observa:** La distancia recorrida (70 m) es **mayor** que el desplazamiento (50 m). El desplazamiento es siempre la **ruta más corta**.

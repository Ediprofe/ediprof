# ➕ Suma y Resta de Números Naturales

En este tema aprenderemos a sumar y restar números naturales usando el método de columnas.

---

## 📖 ¿Qué son los números naturales?

Los **números naturales** son los que usamos para contar:

$$
\mathbb{N} = \{1, 2, 3, 4, 5, 6, \ldots\}
$$

---

## 📖 La suma

La **suma** combina dos o más cantidades para obtener un total.

$$
\text{sumando} + \text{sumando} = \text{suma (resultado)}
$$

---

## 📖 Ejemplos de suma

### Ejemplo 1: $234 + 152 = 386$ (sin llevar)

<div id="jsxgraph-suma1" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 180px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma1', {
      boundingbox: [-0.5, 4.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 3.5, '2'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '3'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '4'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '+'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '1'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '5'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '2'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '3'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '8'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '6'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** Unidades: $4+2=6$, Decenas: $3+5=8$, Centenas: $2+1=3$

---

### Ejemplo 2: $478 + 256 = 734$ (con llevar)

<div id="jsxgraph-suma2" class="jsxgraph-container" style="width: 100%; max-width: 320px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma2', {
      boundingbox: [-0.5, 5, 5.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '4'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '7'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '8'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '+'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '2'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '5'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '6'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '7'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '3'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '4'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $8+6=14$ (escribo 4, llevo 1), $7+5+1=13$ (escribo 3, llevo 1), $4+2+1=7$

---

### Ejemplo 3: $567 + 389 = 956$

<div id="jsxgraph-suma3" class="jsxgraph-container" style="width: 100%; max-width: 320px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma3', {
      boundingbox: [-0.5, 5, 5.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '5'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '6'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '7'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '+'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '3'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '8'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '9'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '9'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '5'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '6'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $7+9=16$ (escribo 6, llevo 1), $6+8+1=15$ (escribo 5, llevo 1), $5+3+1=9$

---

### Ejemplo 4: $1245 + 3867 = 5112$

<div id="jsxgraph-suma4" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma4')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma4', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '1'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '2'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '4'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '5'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '8'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '2'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $5+7=12$, $4+6+1=11$, $2+8+1=11$, $1+3+1=5$

---

### Ejemplo 5: $2589 + 4376 = 6965$

<div id="jsxgraph-suma5" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma5')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma5', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '2'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '5'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '8'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '9'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $9+6=15$, $8+7+1=16$, $5+3+1=9$, $2+4=6$

---

### Ejemplo 6: $3456 + 2789 = 6245$

<div id="jsxgraph-suma6" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma6')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma6', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '4'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '5'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '6'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '2'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '8'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '9'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '2'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $6+9=15$, $5+8+1=14$, $4+7+1=12$, $3+2+1=6$

---

### Ejemplo 7: $5678 + 1234 = 6912$

<div id="jsxgraph-suma7" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma7', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [2.2, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '5'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '6'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '7'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '8'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '2'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '9'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '2'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $8+4=12$, $7+3+1=11$, $6+2+1=9$, $5+1=6$

---

### Ejemplo 8: $7890 + 2345 = 10235$

<div id="jsxgraph-suma8" class="jsxgraph-container" style="width: 100%; max-width: 380px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma8')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma8', {
      boundingbox: [-0.5, 5, 6.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.2, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '7'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '8'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 3.5, '0'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.2, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '2'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 2.5, '5'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.4, 2], [3.9, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.2, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.2, '0'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '2'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $0+5=5$, $9+4=13$, $8+3+1=12$, $7+2+1=10$

---

### Ejemplo 9: $4567 + 8765 = 13332$

<div id="jsxgraph-suma9" class="jsxgraph-container" style="width: 100%; max-width: 380px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma9')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma9', {
      boundingbox: [-0.5, 5, 6.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.2, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '4'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '5'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '6'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 3.5, '7'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.2, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '8'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 2.5, '5'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.4, 2], [3.9, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.2, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 1.2, '2'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $7+5=12$, $6+6+1=13$, $5+7+1=13$, $4+8+1=13$

---

### Ejemplo 10: $9999 + 1111 = 11110$

<div id="jsxgraph-suma10" class="jsxgraph-container" style="width: 100%; max-width: 380px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma10')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma10', {
      boundingbox: [-0.5, 5, 6.5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.2, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 4.3, '¹'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.2, 2.5, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.4, 2], [3.9, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.2, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '1'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.4, 1.2, '0'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $9+1=10$, $9+1+1=11$, $9+1+1=11$, $9+1+1=11$

---

## 📖 Propiedades de la suma

| Propiedad | Fórmula | Ejemplo |
|:----------|:--------|:--------|
| **Conmutativa** | $a + b = b + a$ | $5 + 3 = 3 + 5 = 8$ |
| **Asociativa** | $(a + b) + c = a + (b + c)$ | $(2 + 3) + 4 = 2 + (3 + 4) = 9$ |
| **Elemento neutro** | $a + 0 = a$ | $7 + 0 = 7$ |

---

## 📖 La resta

La **resta** quita una cantidad de otra.

$$
\text{minuendo} - \text{sustraendo} = \text{diferencia}
$$

---

## 📖 Ejemplos de resta

### Ejemplo 1: $587 - 234 = 353$ (sin prestar)

<div id="jsxgraph-resta1" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 180px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta1', {
      boundingbox: [-0.5, 4.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 3.5, '5'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '8'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '7'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '−'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '2'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '3'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '4'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '3'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '5'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '3'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $7-4=3$, $8-3=5$, $5-2=3$

---

### Ejemplo 2: $452 - 178 = 274$ (con prestar)

<div id="jsxgraph-resta2" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta2', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 4.3, '³'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 4.3, '¹⁴'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 4.3, '¹²'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '4̶'], {fontSize: 20, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '5̶'], {fontSize: 20, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '2'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '−'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '1'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '7'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '8'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '2'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '7'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '4'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $2<8$, presto: $12-8=4$. $4<7$, presto: $14-7=7$. $3-1=2$

---

### Ejemplo 3: $703 - 258 = 445$

<div id="jsxgraph-resta3" class="jsxgraph-container" style="width: 100%; max-width: 300px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta3', {
      boundingbox: [-0.5, 5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 4.3, '⁶'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 4.3, '¹³'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1, 3.5, '7̶'], {fontSize: 20, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '0̶'], {fontSize: 20, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '3'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '−'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '2'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '5'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '8'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '4'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '4'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '5'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $3<8$, presto: $13-8=5$. $9-5=4$. $6-2=4$

---

### Ejemplo 4: $1000 - 456 = 544$

<div id="jsxgraph-resta4" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta4')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta4', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '⁰'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [3, 4.3, '¹⁰'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '1̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '0'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '5'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1.4, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $10-6=4$, $9-5=4$, $9-4=5$

---

### Ejemplo 5: $5000 - 1234 = 3766$

<div id="jsxgraph-resta5" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta5')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta5', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '⁴'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [3, 4.3, '¹⁰'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '5̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '0'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '2'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '7'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $10-4=6$, $9-3=6$, $9-2=7$, $4-1=3$

---

### Ejemplo 6: $8765 - 3456 = 5309$

<div id="jsxgraph-resta6" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta6')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta6', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1.4, 4.3, '⁷'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '¹⁵'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '8'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '7̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '6̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '5'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '5'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '0'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '9'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $5<6$, presto: $15-6=9$. $5<5$ pero queda $5-5=0$. $7-4=3$. $8-3=5$

---

### Ejemplo 7: $9876 - 5432 = 4444$

<div id="jsxgraph-resta7" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta7', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 3.5, '9'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '8'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '7'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '6'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '5'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '3'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '2'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $6-2=4$, $7-3=4$, $8-4=4$, $9-5=4$

---

### Ejemplo 8: $7500 - 2867 = 4633$

<div id="jsxgraph-resta8" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta8')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta8', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '⁶'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '¹⁴'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [3, 4.3, '¹⁰'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '7̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '5̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '0'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '2'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '8'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $10-7=3$, $9-6=3$, $14-8=6$, $6-2=4$

---

### Ejemplo 9: $6543 - 1987 = 4556$

<div id="jsxgraph-resta9" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta9')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta9', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '⁵'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '¹⁴'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '¹³'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '6̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '5̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '4̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '9'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '8'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '5'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '6'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $3<7$, presto: $13-7=6$. $13-8=5$. $14-9=5$. $5-1=4$

---

### Ejemplo 10: $9001 - 4567 = 4434$

<div id="jsxgraph-resta10" class="jsxgraph-container" style="width: 100%; max-width: 350px; height: 200px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta10')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta10', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [0.6, 4.3, '⁸'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [1.4, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.2, 4.3, '⁹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [3, 4.3, '¹¹'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 3.5, '9̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 3.5, '0̶'], {fontSize: 18, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 3.5, '1'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.1, 2.5, '−'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.6, 2.5, '4'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 2.5, '5'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 2.5, '6'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 2.5, '7'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.1, 2], [3.5, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [0.6, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.4, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.2, 1.2, '3'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3, 1.2, '4'], {fontSize: 20, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

**Proceso:** $11-7=4$, $9-6=3$, $9-5=4$, $8-4=4$

---

## 📝 Ejercicios de práctica

### Sumas

| Ejercicio | Operación |
|:---------:|:----------|
| 1 | $345 + 234$ |
| 2 | $567 + 389$ |
| 3 | $789 + 456$ |
| 4 | $1234 + 5678$ |
| 5 | $2456 + 3789$ |
| 6 | $4567 + 2345$ |
| 7 | $5678 + 4567$ |
| 8 | $6789 + 1234$ |
| 9 | $8765 + 4321$ |
| 10 | $9999 + 8888$ |

### Restas

| Ejercicio | Operación |
|:---------:|:----------|
| 11 | $876 - 543$ |
| 12 | $654 - 278$ |
| 13 | $1000 - 567$ |
| 14 | $5000 - 2345$ |
| 15 | $7654 - 3210$ |
| 16 | $8765 - 4987$ |
| 17 | $9000 - 3567$ |
| 18 | $6543 - 2876$ |
| 19 | $4321 - 1987$ |
| 20 | $8000 - 4567$ |

---

## ✅ Soluciones

### Sumas

| Ejercicio | Solución |
|:---------:|:---------|
| 1 | $579$ |
| 2 | $956$ |
| 3 | $1245$ |
| 4 | $6912$ |
| 5 | $6245$ |
| 6 | $6912$ |
| 7 | $10245$ |
| 8 | $8023$ |
| 9 | $13086$ |
| 10 | $18887$ |

### Restas

| Ejercicio | Solución |
|:---------:|:---------|
| 11 | $333$ |
| 12 | $376$ |
| 13 | $433$ |
| 14 | $2655$ |
| 15 | $4444$ |
| 16 | $3778$ |
| 17 | $5433$ |
| 18 | $3667$ |
| 19 | $2334$ |
| 20 | $3433$ |

---

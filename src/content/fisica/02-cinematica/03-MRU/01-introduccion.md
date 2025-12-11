# 🚗 **MRU: Introducción**

El **Movimiento Rectilíneo Uniforme (MRU)** es el modelo de movimiento más fundamental en la física. Se caracteriza por cumplir estrictamente dos condiciones:

1.  **Trayectoria Rectilínea:** El objeto se desplaza en línea recta, sin cambiar su dirección.
2.  **Velocidad Constante:** El objeto mantiene siempre la misma rapidez y dirección. Esto implica que la aceleración es nula ($a=0$).

> 💡 **Principio Fundamental:**
> En el MRU, el objeto recorre **distancias iguales en tiempos iguales**.
> Una velocidad de $10\,\mathrm{m/s}$ significa físicamente que **por cada segundo que transcurre, el cuerpo avanza exactamente 10 metros**.

---

## ⚙️ **Ejercicio 1 — Análisis por definición**

Un robot de juguete se mueve en línea recta con una velocidad constante de $4\,\mathrm{m/s}$. Si parte desde la posición cero, determinar su posición final después de $3\,\mathrm{s}$.

<div id="jsxgraph-robot" class="jsxgraph-container" style="width: 100%; max-width: 550px; height: 150px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-robot')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-robot', {
      boundingbox: [-1, 3.5, 14, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 1], [12, 1]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    // Marcas cada 4 metros
    board.create('point', [0, 1], {name: 't=0s', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [4, 1], {name: 't=1s', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [8, 1], {name: 't=2s', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [12, 1], {name: 't=3s', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    // Etiquetas de posición
    board.create('text', [0, 1.8, '0m'], {fontSize: 11, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [4, 1.8, '4m'], {fontSize: 11, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [8, 1.8, '8m'], {fontSize: 11, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [12, 1.8, '12m'], {fontSize: 11, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    // Flechas de avance
    board.create('arrow', [[0, 2.6], [4, 2.6]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('arrow', [[4, 2.6], [8, 2.6]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('arrow', [[8, 2.6], [12, 2.6]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('text', [2, 3.1, '+4m'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [6, 3.1, '+4m'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [10, 3.1, '+4m'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 El gráfico muestra cómo el robot avanza **exactamente 4 metros cada segundo** (distancias iguales en tiempos iguales).

### **✅ Solución**

El dato $v = 4\,\mathrm{m/s}$ indica que el robot avanza **4 metros cada segundo**.

| Tiempo | Avance | Posición |
|--------|--------|----------|
| $t=0\,\mathrm{s}$ | — | $0\,\mathrm{m}$ |
| $t=1\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $4\,\mathrm{m}$ |
| $t=2\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $8\,\mathrm{m}$ |
| $t=3\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $12\,\mathrm{m}$ |

**Cálculo directo:**

$$
d = v \cdot t = 4\,\mathrm{m/s} \times 3\,\mathrm{s} = 12\,\mathrm{m}
$$

---

## ⚙️ **Ejercicio 2 — Deducción de parámetros**

Un corredor de larga distancia entrena manteniendo un ritmo constante. Se observa que recorre $20\,\mathrm{m}$ cada $4\,\mathrm{s}$.

1.  ¿Cuál es su velocidad constante?
2.  Si mantiene ese mismo ritmo, ¿qué distancia recorrerá en $10\,\mathrm{s}$?

<div id="jsxgraph-corredor" class="jsxgraph-container" style="width: 100%; max-width: 550px; height: 150px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-corredor')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-corredor', {
      boundingbox: [-3, 3.5, 55, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 1], [50, 1]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    // Marcas cada 5 metros (v = 5 m/s)
    for (var i = 0; i <= 10; i++) {
      var x = i * 5;
      var col = (i == 0) ? '#22c55e' : (i == 4) ? '#f59e0b' : (i == 10) ? '#ef4444' : '#94a3b8';
      board.create('point', [x, 1], {size: 3, fixed: true, color: col, name: '', withLabel: false});
      board.create('text', [x, 0.4, i + 's'], {fontSize: 9, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    }
    // Etiquetas de posición
    board.create('text', [0, 1.5, '0m'], {fontSize: 10, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [20, 1.5, '20m'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [50, 1.5, '50m'], {fontSize: 10, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    // Paso 1: Dato 20m en 4s
    board.create('arrow', [[0, 2.3], [20, 2.3]], {strokeColor: '#f59e0b', strokeWidth: 2, fixed: true});
    board.create('text', [10, 2.8, 'Dato: 20m en 4s'], {fontSize: 11, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

**Paso 1: Calcular la velocidad** (¿cuánto avanza por segundo?)

$$
v = \frac{20\,\mathrm{m}}{4\,\mathrm{s}} = 5\,\mathrm{m/s}
$$

El corredor avanza **5 metros cada segundo**.

**Paso 2: Predecir la distancia en 10 segundos**

$$
d = v \cdot t = 5\,\mathrm{m/s} \times 10\,\mathrm{s} = 50\,\mathrm{m}
$$

> 💡 El gráfico muestra: en 4s recorre 20m (dato), luego en los 6s restantes recorre 30m más → total 50m.
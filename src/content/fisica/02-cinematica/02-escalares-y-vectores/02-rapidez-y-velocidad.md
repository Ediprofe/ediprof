# 🏎️ **Rapidez vs. Velocidad**

Al igual que ocurre con la distancia y el desplazamiento, en el lenguaje cotidiano usamos "rapidez" y "velocidad" como sinónimos. Sin embargo, en física describen aspectos diferentes del movimiento.

---

## ⚡ **Rapidez**

Es una magnitud **escalar** que indica qué tan deprisa se recorrió una **distancia** total. No tiene en cuenta la dirección.

* **Relación:** Se calcula con la **distancia** ($d$).
* **Signo:** Siempre es positiva.

$$
\text{Rapidez media} = \frac{\text{distancia recorrida}}{\text{tiempo transcurrido}}
$$

$$
v = \frac{d}{t}
$$

## 🧭 **Velocidad**

Es una magnitud **vectorial** que indica qué tan rápido cambió la **posición** (desplazamiento) y en qué dirección.

* **Relación:** Se calcula con el **desplazamiento** ($\Delta x$).
* **Signo:** Puede ser positiva o negativa (indica el sentido del movimiento).

$$
\text{Velocidad media} = \frac{\text{desplazamiento}}{\text{tiempo transcurrido}}
$$

$$
\vec{v} = \frac{\Delta x}{t}
$$

---

## ⚙️ **Ejercicio 1 — Carrera de 100 metros**

Un atleta olímpico corre en una pista recta. Inicia en la línea de salida y cruza la meta ubicada a $100\,\mathrm{m}$ de distancia en un tiempo de $10\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-100m" class="jsxgraph-container" style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-100m')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-100m', {
      boundingbox: [-5, 3, 105, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 0.5], [100, 0.5]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 0.5], {name: 'Salida', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [100, 0.5], {name: 'Meta', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('arrow', [[0, 1.8], [100, 1.8]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('text', [50, 2.4, '100 m en 10 s'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

**Análisis:** Al ser línea recta sin retrocesos: $d = \Delta x = 100\,\mathrm{m}$

$$
\text{Rapidez} = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = 10\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{+100\,\mathrm{m}}{10\,\mathrm{s}} = +10\,\mathrm{m/s}
$$

> 💡 En movimiento rectilíneo sin retrocesos, rapidez = |velocidad|.

---

## ⚙️ **Ejercicio 2 — Caminata de ida y vuelta**

Una persona camina $60\,\mathrm{m}$ hacia el este, luego retrocede $20\,\mathrm{m}$ hacia el oeste. Tiempo total: $40\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-idavuelta" class="jsxgraph-container" style="width: 100%; height: 150px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-idavuelta')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-idavuelta', {
      boundingbox: [-5, 4, 70, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 1], [60, 1]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 1], {name: 'Inicio (0m)', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [60, 1], {name: '60m', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [40, 1], {name: 'Final (40m)', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('arrow', [[0, 2.5], [60, 2.5]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('arrow', [[60, 2.2], [40, 2.2]], {strokeColor: '#ef4444', strokeWidth: 2, fixed: true});
    board.create('text', [30, 3.2, '60 m →'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [50, 1.6, '← 20 m'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Magnitud | Cálculo | Resultado |
|----------|---------|-----------|
| Distancia | $60 + 20$ | $80\,\mathrm{m}$ |
| Desplazamiento | $60 - 20$ | $+40\,\mathrm{m}$ |

$$
\text{Rapidez} = \frac{80\,\mathrm{m}}{40\,\mathrm{s}} = 2\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{+40\,\mathrm{m}}{40\,\mathrm{s}} = +1\,\mathrm{m/s}
$$

> 💡 La rapidez es mayor porque considera todo el movimiento; la velocidad solo el cambio neto de posición.

---

## ⚙️ **Ejercicio 3 — Vuelta a la pista**

Un ciclista da una vuelta completa a un velódromo circular de $500\,\mathrm{m}$ en $50\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 250px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-velodromo" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-velodromo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-velodromo', {
      boundingbox: [-4, 4, 4, -4], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('circle', [[0, 0], 2.5], {strokeColor: '#3b82f6', strokeWidth: 3, fillColor: 'transparent', fixed: true});
    board.create('point', [2.5, 0], {name: 'Inicio/Fin', size: 5, fixed: true, color: '#22c55e', label: {offset: [10, 0], strokeColor: '#22c55e'}});
    board.create('arrow', [[0, 2.5], [1.5, 2]], {strokeColor: '#f59e0b', strokeWidth: 2, fixed: true});
    board.create('text', [0, 3.2, 'd = 500 m'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [0, -3.2, 'Δx = 0 m'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

$$
\text{Rapidez} = \frac{500\,\mathrm{m}}{50\,\mathrm{s}} = 10\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{0\,\mathrm{m}}{50\,\mathrm{s}} = 0\,\mathrm{m/s}
$$

> 💡 ¡Aunque se movió muy rápido, su velocidad media es cero porque regresó al punto de partida!

---

## ⚙️ **Ejercicio 4 — Movimiento en "L"**

Un robot se mueve $3\,\mathrm{m}$ al Norte en $2\,\mathrm{s}$, luego $4\,\mathrm{m}$ al Este en $3\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 300px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-robotL" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-robotL')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-robotL', {
      boundingbox: [-1, 5, 6, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var A = board.create('point', [0, 0], {name: 'Inicio', size: 4, fixed: true, color: '#22c55e', label: {offset: [-15, -15], strokeColor: '#22c55e'}});
    var B = board.create('point', [0, 3], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    var C = board.create('point', [4, 3], {name: 'Fin', size: 4, fixed: true, color: '#ef4444', label: {offset: [10, 0], strokeColor: '#ef4444'}});
    board.create('arrow', [A, B], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('arrow', [B, C], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('arrow', [A, C], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2, fixed: true});
    board.create('text', [-0.5, 1.5, '3m ↑'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true, anchorX: 'right'});
    board.create('text', [2, 3.5, '4m'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [2.5, 1, 'Δx=5m'], {fontSize: 11, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Magnitud | Cálculo | Resultado |
|----------|---------|-----------|
| Distancia | $3 + 4$ | $7\,\mathrm{m}$ |
| Desplazamiento | $\sqrt{3^2 + 4^2}$ | $5\,\mathrm{m}$ |
| Tiempo total | $2 + 3$ | $5\,\mathrm{s}$ |

$$
\text{Rapidez} = \frac{7\,\mathrm{m}}{5\,\mathrm{s}} = 1.4\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{5\,\mathrm{m}}{5\,\mathrm{s}} = 1\,\mathrm{m/s}
$$

> 💡 El robot recorrió más distancia de la que avanzó en línea recta.
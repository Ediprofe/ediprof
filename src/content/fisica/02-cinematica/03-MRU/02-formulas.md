# 📐 **Fórmulas del Movimiento Rectilíneo Uniforme (MRU)**

Para describir matemáticamente el movimiento de manera sencilla y progresiva, usaremos la letra **$x$** para representar el **Desplazamiento**.

### **1. El Caso Simple (Partiendo de Cero)**

Imaginemos la situación más común: encendemos el cronómetro justo cuando el objeto arranca desde el punto de inicio ($0$).

En este caso, el **desplazamiento ($x$)** es simplemente la multiplicación de la velocidad por el tiempo.

#### **A. Para calcular el Desplazamiento ($x$)**
$$
x = v \cdot t
$$

#### **B. Para calcular la Velocidad ($v$)**
$$
v = \frac{x}{t}
$$

#### **C. Para calcular el Tiempo ($t$)**
$$
t = \frac{x}{v}
$$

> **Nota:** Estas fórmulas asumen que el objeto parte desde el origen ($0$).

---

### **2. El Caso General (Con Posición Inicial)**

En la realidad, no siempre empezamos a contar desde cero. A veces el objeto ya se encuentra en una **Posición Inicial ($x_i$)** y termina en una **Posición Final ($x_f$)**.

Aquí debemos ser más precisos: el **Desplazamiento** ya no es solo $x$, sino la diferencia entre dónde terminas y dónde empezaste. A esto lo llamamos **Delta x ($\Delta x$)**.

$$
\Delta x = x_f - x_i
$$

Sustituyendo esto en nuestras fórmulas, la ecuación de la posición evoluciona así:

$$
x_f = x_i + v \cdot t
$$

**Donde:**
* $x_f$: **Posición Final** (Ubicación de llegada).
* $x_i$: **Posición Inicial** (Ubicación de partida).
* $v \cdot t$: **Desplazamiento** (Lo que recorrió).

**Para hallar el tiempo en este caso:**
Primero calculamos cuánto se desplazó realmente ($\Delta x$) y dividimos por la velocidad.

$$
t = \frac{x_f - x_i}{v}
$$

---

## ⚙️ **Ejercicio 1 — Caso Simple (Hallar Velocidad)**

Un atleta corre un desplazamiento de $100\,\mathrm{m}$ partiendo desde la línea de salida. Si tarda $10\,\mathrm{s}$ en llegar a la meta, ¿cuál fue su velocidad?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-atleta" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-atleta')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-atleta', {
      boundingbox: [-5, 2.5, 105, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 0.8], [100, 0.8]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 0.8], {name: '0m', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -18], strokeColor: '#22c55e'}});
    board.create('point', [100, 0.8], {name: '100m', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -18], strokeColor: '#ef4444'}});
    board.create('arrow', [[0, 1.6], [100, 1.6]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('text', [50, 2.1, 'x = 100m, t = 10s → v = ?'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $x$ | $100\,\mathrm{m}$ |
| $t$ | $10\,\mathrm{s}$ |

$$
v = \frac{x}{t} = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = \boxed{10\,\mathrm{m/s}}
$$

---

## ⚙️ **Ejercicio 2 — Caso Simple (Hallar Desplazamiento)**

El sonido viaja a una velocidad constante de $340\,\mathrm{m/s}$. Si un trueno se escucha $3\,\mathrm{s}$ después del relámpago, ¿cuál fue el desplazamiento ($x$) del sonido?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-trueno" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-trueno')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-trueno', {
      boundingbox: [-50, 2.5, 1100, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 0.8], [1020, 0.8]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 0.8], {name: '⚡ Nube', size: 4, fixed: true, color: '#f59e0b', label: {offset: [0, -18], strokeColor: '#f59e0b'}});
    board.create('point', [1020, 0.8], {name: '👂 Tú', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -18], strokeColor: '#22c55e'}});
    board.create('arrow', [[0, 1.6], [1020, 1.6]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('text', [510, 2.1, 'v = 340 m/s, t = 3s → x = ?'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $v$ | $340\,\mathrm{m/s}$ |
| $t$ | $3\,\mathrm{s}$ |

$$
x = v \cdot t = 340\,\mathrm{m/s} \times 3\,\mathrm{s} = \boxed{1020\,\mathrm{m}}
$$

---

## ⚙️ **Ejercicio 3 — Caso General (Hallar Posición Final)**

Un ciclista se encuentra en el **Kilómetro 10** ($x_i = 10\,\mathrm{km}$). Continúa a $20\,\mathrm{km/h}$ durante **2 horas**. ¿En qué kilómetro estará?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-ciclista" class="jsxgraph-container" style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-ciclista')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-ciclista', {
      boundingbox: [-3, 3, 55, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 1], [50, 1]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    // Marcas
    board.create('point', [0, 1], {name: 'km 0', size: 3, fixed: true, color: '#94a3b8', label: {offset: [0, -18], strokeColor: '#94a3b8'}});
    board.create('point', [10, 1], {name: 'km 10', size: 4, fixed: true, color: '#f59e0b', label: {offset: [0, -18], strokeColor: '#f59e0b'}});
    board.create('point', [50, 1], {name: 'km 50', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -18], strokeColor: '#22c55e'}});
    // Posición inicial
    board.create('text', [10, 1.6, 'xᵢ = 10'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    // Desplazamiento
    board.create('arrow', [[10, 2.2], [50, 2.2]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('text', [30, 2.6, 'v·t = 20×2 = 40 km'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $x_i$ | $10\,\mathrm{km}$ |
| $v$ | $20\,\mathrm{km/h}$ |
| $t$ | $2\,\mathrm{h}$ |

$$
x_f = x_i + v \cdot t = 10 + (20 \times 2) = 10 + 40 = \boxed{50\,\mathrm{km}}
$$

---

## ⚙️ **Ejercicio 4 — Caso General (Hallar Tiempo)**

Un tren sale de **Ciudad A** ($x_i = 200\,\mathrm{km}$) hacia **Ciudad B** ($x_f = 500\,\mathrm{km}$) a $100\,\mathrm{km/h}$. ¿Cuánto tiempo tardará?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tren" class="jsxgraph-container" style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-tren')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-tren', {
      boundingbox: [-30, 3, 550, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 1], [500, 1]], {strokeWidth: 3, strokeColor: '#374151', fixed: true});
    // Marcas
    board.create('point', [0, 1], {name: 'km 0', size: 3, fixed: true, color: '#94a3b8', label: {offset: [0, -18], strokeColor: '#94a3b8'}});
    board.create('point', [200, 1], {name: 'Ciudad A', size: 4, fixed: true, color: '#f59e0b', label: {offset: [0, -18], strokeColor: '#f59e0b'}});
    board.create('point', [500, 1], {name: 'Ciudad B', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -18], strokeColor: '#22c55e'}});
    // Posiciones
    board.create('text', [200, 1.5, '200 km'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [500, 1.5, '500 km'], {fontSize: 10, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    // Desplazamiento
    board.create('arrow', [[200, 2.2], [500, 2.2]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
    board.create('text', [350, 2.6, 'Δx = 300 km, v = 100 km/h'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $x_i$ | $200\,\mathrm{km}$ |
| $x_f$ | $500\,\mathrm{km}$ |
| $v$ | $100\,\mathrm{km/h}$ |

**Paso 1:** Calcular desplazamiento
$$\Delta x = x_f - x_i = 500 - 200 = 300\,\mathrm{km}$$

**Paso 2:** Calcular tiempo
$$t = \frac{\Delta x}{v} = \frac{300\,\mathrm{km}}{100\,\mathrm{km/h}} = \boxed{3\,\mathrm{h}}$$
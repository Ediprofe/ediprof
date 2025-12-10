# 📍 **Posición y Marco de Referencia**

La **posición** ($x$) es la ubicación de un objeto en el espacio. Sin embargo, para describir dónde está algo, siempre necesitamos un punto de comparación.

Este punto de comparación se llama **Marco de Referencia** u **Origen** ($x=0$).

---

## 📐 **¿Qué es un Marco de Referencia?**

El movimiento es **relativo**. Para describir la posición de una partícula, necesitamos un sistema desde donde observar y medir. Un marco de referencia consta de tres elementos esenciales:

1.  **Origen de coordenadas:** El punto $(0,0)$ desde donde se mide la posición.
2.  **Sistema de ejes:** Generalmente ejes cartesianos ($x, y, z$) para dar dirección.
3.  **Reloj:** Para medir el tiempo ($t$).

El siguiente diagrama muestra un marco de referencia con una partícula ubicada en la posición $(x, y)$:

<div id="jsxgraph-posicion" class="jsxgraph-container" style="width: 100%; max-width: 400px; height: 300px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-posicion')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-posicion', {
      boundingbox: [-1, 6, 8, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var O = board.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-15, -15]}});
    var P = board.create('point', [5, 3], {name: 'P', size: 5, color: '#3b82f6', label: {offset: [8, 8], strokeColor: '#3b82f6'}});
    board.create('arrow', [O, P], {strokeColor: '#22c55e', strokeWidth: 2});
    board.create('segment', [[function() {return P.X();}, 0], P], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    board.create('segment', [[0, function() {return P.Y();}], P], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    board.create('text', [function() {return P.X()/2;}, -0.5, function() {return 'x = ' + P.X().toFixed(1);}], {fontSize: 12, strokeColor: '#374151', fixed: true});
    board.create('text', [-0.8, function() {return P.Y()/2;}, function() {return 'y = ' + P.Y().toFixed(1);}], {fontSize: 12, strokeColor: '#374151', fixed: true});
    board.create('text', [function() {return P.X()/2 + 0.3;}, function() {return P.Y()/2 + 0.4;}, 'r'], {fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Arrastra el punto P** para ver cómo cambian las coordenadas $(x, y)$ respecto al origen O.

---

## 📐 **El origen puede estar en cualquier punto**

El origen del marco de referencia **no tiene que estar en un lugar "especial"**. Podemos elegirlo donde sea más conveniente. Observa cómo la **misma partícula** tiene coordenadas diferentes según dónde coloquemos el origen:

<div id="jsxgraph-marcos-ref" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-marcos-ref')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-marcos-ref', {
      boundingbox: [-1, 8, 10, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var O1 = board.create('point', [0, 0], {name: 'O₁', size: 4, fixed: true, color: '#3b82f6', label: {offset: [-15, -15], strokeColor: '#3b82f6'}});
    board.create('arrow', [O1, [5, 0]], {strokeColor: '#3b82f6', strokeWidth: 1});
    board.create('arrow', [O1, [0, 5]], {strokeColor: '#3b82f6', strokeWidth: 1});
    board.create('text', [4.8, -0.5, 'x₁'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [-0.5, 4.8, 'y₁'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    
    var O2 = board.create('point', [6, 1], {name: 'O₂', size: 4, fixed: true, color: '#ef4444', label: {offset: [-15, -15], strokeColor: '#ef4444'}});
    board.create('arrow', [O2, [9, 1]], {strokeColor: '#ef4444', strokeWidth: 1});
    board.create('arrow', [O2, [6, 4]], {strokeColor: '#ef4444', strokeWidth: 1});
    board.create('text', [8.8, 0.5, 'x₂'], {fontSize: 12, strokeColor: '#ef4444', fixed: true});
    board.create('text', [5.5, 3.8, 'y₂'], {fontSize: 12, strokeColor: '#ef4444', fixed: true});
    
    var P = board.create('point', [7, 5], {name: 'P', size: 5, color: '#22c55e', label: {offset: [8, 8], strokeColor: '#22c55e'}});
    board.create('arrow', [O1, P], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2});
    board.create('arrow', [O2, P], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    board.create('text', [0.5, 7.5, function() {return 'Respecto a O₁: (' + P.X().toFixed(1) + ', ' + P.Y().toFixed(1) + ')';}], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [0.5, 7, function() {return 'Respecto a O₂: (' + (P.X() - O2.X()).toFixed(1) + ', ' + (P.Y() - O2.Y()).toFixed(1) + ')';}], {fontSize: 12, strokeColor: '#ef4444', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Arrastra el punto P** y observa cómo una misma posición tiene **coordenadas diferentes** según el marco de referencia elegido (O₁ o O₂).

---

## 📏 **Posiciones Positivas y Negativas**

* Si el objeto está en el sentido positivo del eje (generalmente a la derecha), su posición es **positiva** ($+$).
* Si el objeto está en el sentido negativo (generalmente a la izquierda), su posición es **negativa** ($-$).

> **Regla de oro:** La posición física de un objeto **no es fija**; cambia si cambiamos el lugar desde donde lo miramos (el origen).

---

## ⚙️ **Ejercicio 1 — Los Salones del Colegio**

En un pasillo recto se encuentran tres lugares clave distribuidos en el siguiente orden: la **Rectoría**, el **Salón A** y el **Salón B**.

Las distancias son las siguientes:
* De la Rectoría al Salón A hay **20 metros**.
* Del Salón A al Salón B hay **10 metros**.

$$
\text{[Rectoría]} \xrightarrow{20\,\mathrm{m}} \text{[Salón A]} \xrightarrow{10\,\mathrm{m}} \text{[Salón B]}
$$

**Determine la posición ($x$) de cada uno de los tres lugares (Rectoría, Salón A y Salón B) respecto a los siguientes marcos de referencia:**

1.  **Origen en la Rectoría.**
2.  **Origen en el Salón A.**
3.  **Origen en el Salón B.**

### **✅ Solución**

**1. Marco de Referencia: Origen en la Rectoría ($x=0$)**
Ubicamos el cero en el extremo izquierdo. Todo lo demás queda a la derecha (positivo).

<div id="jsxgraph-salones1" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 100px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-salones1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-salones1', {
      boundingbox: [-5, 2, 35, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 0], [30, 0]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 0], {name: 'Rectoría', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [20, 0], {name: 'Salón A', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [30, 0], {name: 'Salón B', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('text', [0, 0.8, 'x=0'], {fontSize: 11, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [20, 0.8, 'x=+20'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [30, 0.8, 'x=+30'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

* **Posición Rectoría:** $x = 0\,\mathrm{m}$
* **Posición Salón A:** $x_A = +20\,\mathrm{m}$
* **Posición Salón B:** $x_B = +30\,\mathrm{m}$

**2. Marco de Referencia: Origen en el Salón A ($x=0$)**
Ubicamos el cero en el medio.

<div id="jsxgraph-salones2" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 100px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-salones2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-salones2', {
      boundingbox: [-25, 2, 15, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[-20, 0], [10, 0]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [-20, 0], {name: 'Rectoría', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [0, 0], {name: 'Salón A', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [10, 0], {name: 'Salón B', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('text', [-20, 0.8, 'x=-20'], {fontSize: 11, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [0, 0.8, 'x=0'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [10, 0.8, 'x=+10'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

* **Posición Salón A:** $x = 0\,\mathrm{m}$
* **Posición Salón B:** $x_B = +10\,\mathrm{m}$
* **Posición Rectoría:** $x_R = -20\,\mathrm{m}$

**3. Marco de Referencia: Origen en el Salón B ($x=0$)**
Ubicamos el cero en el extremo derecho. Todo lo demás queda a la izquierda (negativo).

<div id="jsxgraph-salones3" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 100px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-salones3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-salones3', {
      boundingbox: [-35, 2, 5, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[-30, 0], [0, 0]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [-30, 0], {name: 'Rectoría', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [-10, 0], {name: 'Salón A', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [0, 0], {name: 'Salón B', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('text', [-30, 0.8, 'x=-30'], {fontSize: 11, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [-10, 0.8, 'x=-10'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [0, 0.8, 'x=0'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

* **Posición Salón B:** $x = 0\,\mathrm{m}$
* **Posición Salón A:** $x_A = -10\,\mathrm{m}$
* **Posición Rectoría:** $x_R = -30\,\mathrm{m}$

---

## ⚙️ **Ejercicio 2 — La Carrera de Atletismo**

Tres atletas están calentando en una pista recta: **Atleta 1**, **Atleta 2** y **Atleta 3**. Su distribución es la siguiente:

* El **Atleta 2** está situado en el centro.
* El **Atleta 1** se encuentra **15 metros a la izquierda** del Atleta 2.
* El **Atleta 3** se encuentra **15 metros a la derecha** del Atleta 2.

$$
\text{[Atleta 1]} \xleftarrow{15\,\mathrm{m}} \text{[Atleta 2]} \xrightarrow{15\,\mathrm{m}} \text{[Atleta 3]}
$$

**Calcule la posición ($x$) de los tres atletas para los siguientes casos:**

1.  El entrenador pone el origen en la posición del **Atleta 2**.
2.  El entrenador pone el origen en la posición del **Atleta 1**.

### **✅ Solución**

**1. Marco de Referencia: Origen en el Atleta 2 ($x=0$)**
El observador está en el centro.

<div id="jsxgraph-atletas1" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 100px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-atletas1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-atletas1', {
      boundingbox: [-20, 2, 20, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[-15, 0], [15, 0]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [-15, 0], {name: 'Atleta 1', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [0, 0], {name: 'Atleta 2', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [15, 0], {name: 'Atleta 3', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('text', [-15, 0.8, 'x=-15'], {fontSize: 11, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [0, 0.8, 'x=0'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [15, 0.8, 'x=+15'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

* **Posición Atleta 2:** $x = 0\,\mathrm{m}$
* **Posición Atleta 3:** $x_3 = +15\,\mathrm{m}$
* **Posición Atleta 1:** $x_1 = -15\,\mathrm{m}$

**2. Marco de Referencia: Origen en el Atleta 1 ($x=0$)**
El observador está en el extremo izquierdo. Todos los demás están a su derecha (positivos).

<div id="jsxgraph-atletas2" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 100px; margin: 1rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-atletas2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-atletas2', {
      boundingbox: [-5, 2, 35, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('segment', [[0, 0], [30, 0]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    board.create('point', [0, 0], {name: 'Atleta 1', size: 4, fixed: true, color: '#22c55e', label: {offset: [0, -20], strokeColor: '#22c55e'}});
    board.create('point', [15, 0], {name: 'Atleta 2', size: 4, fixed: true, color: '#3b82f6', label: {offset: [0, -20], strokeColor: '#3b82f6'}});
    board.create('point', [30, 0], {name: 'Atleta 3', size: 4, fixed: true, color: '#ef4444', label: {offset: [0, -20], strokeColor: '#ef4444'}});
    board.create('text', [0, 0.8, 'x=0'], {fontSize: 11, strokeColor: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [15, 0.8, 'x=+15'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [30, 0.8, 'x=+30'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

* **Posición Atleta 1:** $x = 0\,\mathrm{m}$
* **Posición Atleta 2:** $x_2 = +15\,\mathrm{m}$
* **Posición Atleta 3:** $x_3 = +30\,\mathrm{m}$

---

> 💡 **Conclusión:**
> Un mismo objeto puede tener posiciones diferentes (ej: $x = 30\,\mathrm{m}$ o $x = -20\,\mathrm{m}$) dependiendo de **dónde pongas el cero ($0$)**, aunque la distancia física entre los objetos nunca cambió.

---

## ⚙️ **Ejercicio 3 — Posición en el Plano (2D)**

Un dron sobrevuela un parque. En un sistema de coordenadas donde el **kiosko** está en el origen $(0,0)$, el dron se encuentra en la posición $(4, 3)$ metros.

<div id="jsxgraph-dron" class="jsxgraph-container" style="width: 100%; max-width: 400px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-dron')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-dron', {
      boundingbox: [-2, 6, 7, -2],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var O = board.create('point', [0, 0], {name: 'Kiosko', size: 4, fixed: true, color: '#64748b', label: {offset: [-10, -20], strokeColor: '#64748b'}});
    var D = board.create('point', [4, 3], {name: 'Dron', size: 5, fixed: true, color: '#3b82f6', label: {offset: [8, 8], strokeColor: '#3b82f6'}});
    board.create('arrow', [O, D], {strokeColor: '#22c55e', strokeWidth: 2});
    board.create('segment', [[4, 0], D], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    board.create('segment', [[0, 3], D], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    board.create('text', [2, -0.5, 'x = 4 m'], {fontSize: 12, strokeColor: '#374151', fixed: true});
    board.create('text', [-1.2, 1.5, 'y = 3 m'], {fontSize: 12, strokeColor: '#374151', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

**Pregunta:** ¿Cuál es la distancia del dron al kiosko?

### ✅ Solución

Usamos el teorema de Pitágoras:

$$
d = \sqrt{x^2 + y^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\,\mathrm{m}
$$

---

## ⚙️ **Ejercicio 4 — Cambio de origen en el plano (2D)**

Tres amigos están en una plaza:
- **Ana** está en el origen $(0, 0)$
- **Beto** está en $(3, 4)$
- **Carlos** está en $(6, 0)$

<div id="jsxgraph-plaza" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-plaza')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-plaza', {
      boundingbox: [-2, 7, 9, -2],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var A = board.create('point', [0, 0], {name: 'Ana', size: 5, fixed: true, color: '#ec4899', label: {offset: [-15, -15], strokeColor: '#ec4899'}});
    var B = board.create('point', [3, 4], {name: 'Beto', size: 5, fixed: true, color: '#3b82f6', label: {offset: [8, 8], strokeColor: '#3b82f6'}});
    var C = board.create('point', [6, 0], {name: 'Carlos', size: 5, fixed: true, color: '#22c55e', label: {offset: [5, -15], strokeColor: '#22c55e'}});
    
    // Vectores desde Ana
    board.create('arrow', [A, B], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2});
    board.create('arrow', [A, C], {strokeColor: '#22c55e', strokeWidth: 2, dash: 2});
    
    board.create('text', [7, 5.5, 'Desde Ana:'], {fontSize: 11, strokeColor: '#374151', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [7, 5, 'Beto: (3, 4)'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [7, 4.5, 'Carlos: (6, 0)'], {fontSize: 11, strokeColor: '#22c55e', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

**Pregunta:** Si ahora **Carlos** es el nuevo origen, ¿cuáles son las posiciones de Ana y Beto?

### ✅ Solución

Restamos las coordenadas de Carlos a cada punto:

**Nuevo origen: Carlos en $(6, 0)$**

* **Posición de Ana:** 
  $$\vec{r}_A = (0 - 6, 0 - 0) = (-6, 0)$$
  
* **Posición de Beto:**
  $$\vec{r}_B = (3 - 6, 4 - 0) = (-3, 4)$$

* **Posición de Carlos:**
  $$\vec{r}_C = (0, 0) \quad \text{(es el nuevo origen)}$$

<div id="jsxgraph-plaza2" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-plaza2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-plaza2', {
      boundingbox: [-8, 6, 4, -2],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var C = board.create('point', [0, 0], {name: 'Carlos (origen)', size: 5, fixed: true, color: '#22c55e', label: {offset: [5, -15], strokeColor: '#22c55e'}});
    var A = board.create('point', [-6, 0], {name: 'Ana', size: 5, fixed: true, color: '#ec4899', label: {offset: [-15, -15], strokeColor: '#ec4899'}});
    var B = board.create('point', [-3, 4], {name: 'Beto', size: 5, fixed: true, color: '#3b82f6', label: {offset: [8, 8], strokeColor: '#3b82f6'}});
    
    board.create('arrow', [C, A], {strokeColor: '#ec4899', strokeWidth: 2, dash: 2});
    board.create('arrow', [C, B], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2});
    
    board.create('text', [1, 5, 'Desde Carlos:'], {fontSize: 11, strokeColor: '#374151', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 4.5, 'Ana: (-6, 0)'], {fontSize: 11, strokeColor: '#ec4899', fixed: true});
    board.create('text', [1, 4, 'Beto: (-3, 4)'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Observa:** ¡Las posiciones cambiaron completamente al cambiar el origen! Ana ahora está a la **izquierda** de Carlos (coordenada x negativa).
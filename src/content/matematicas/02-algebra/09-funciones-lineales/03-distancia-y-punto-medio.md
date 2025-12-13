# 📏 Distancia y Punto Medio

En esta lección aprenderemos a calcular la distancia entre dos puntos y a encontrar el punto medio de un segmento en el plano cartesiano.

---

## 📖 Distancia entre dos puntos

La distancia entre dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ se calcula con la **fórmula de la distancia**:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

> 💡 Esta fórmula proviene del **teorema de Pitágoras**: la distancia es la hipotenusa de un triángulo rectángulo cuyos catetos son las diferencias en $x$ y en $y$.

---

### Ejemplo 1

Encontrar la distancia entre $A(1, 2)$ y $B(4, 6)$.

$$
d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

$$
\boxed{d = 5}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-distancia1" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-distancia1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-distancia1', {
      boundingbox: [-1, 8, 7, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var A = board.create('point', [1, 2], {name: 'A(1, 2)', size: 4, fixed: true, color: '#3b82f6', label: {fontSize: 11, offset: [-50, -10]}});
    var B = board.create('point', [4, 6], {name: 'B(4, 6)', size: 4, fixed: true, color: '#3b82f6', label: {fontSize: 11, offset: [5, 10]}});
    
    // Línea de distancia
    board.create('segment', [A, B], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    
    // Triángulo auxiliar
    board.create('segment', [[1, 2], [4, 2]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('segment', [[4, 2], [4, 6]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    
    // Etiquetas de catetos
    board.create('text', [2.5, 1.5, '3'], {fontSize: 12, strokeColor: '#64748b', fixed: true});
    board.create('text', [4.3, 4, '4'], {fontSize: 12, strokeColor: '#64748b', fixed: true});
    
    // Etiqueta de distancia
    board.create('text', [2, 4.5, 'd = 5'], {fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 2

Encontrar la distancia entre $P(-3, 2)$ y $Q(5, -4)$.

$$
d = \sqrt{(5-(-3))^2 + (-4-2)^2} = \sqrt{64 + 36} = \sqrt{100} = 10
$$

$$
\boxed{d = 10}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-distancia2" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-distancia2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-distancia2', {
      boundingbox: [-5, 5, 7, -6], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var P = board.create('point', [-3, 2], {name: 'P(-3, 2)', size: 4, fixed: true, color: '#ef4444', label: {fontSize: 11, offset: [-60, 10]}});
    var Q = board.create('point', [5, -4], {name: 'Q(5, -4)', size: 4, fixed: true, color: '#ef4444', label: {fontSize: 11, offset: [5, -12]}});
    
    // Línea de distancia
    board.create('segment', [P, Q], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    
    // Triángulo auxiliar
    board.create('segment', [[-3, 2], [5, 2]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('segment', [[5, 2], [5, -4]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    
    // Etiquetas de catetos
    board.create('text', [1, 2.5, '8'], {fontSize: 12, strokeColor: '#64748b', fixed: true});
    board.create('text', [5.3, -1, '6'], {fontSize: 12, strokeColor: '#64748b', fixed: true});
    
    // Etiqueta de distancia
    board.create('text', [0, -1.5, 'd = 10'], {fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Punto medio

El **punto medio** $M$ entre $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ es:

$$
M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)
$$

> 💡 Es simplemente el **promedio** de las coordenadas $x$ y el **promedio** de las coordenadas $y$.

---

### Ejemplo 3

Encontrar el punto medio entre $A(2, 4)$ y $B(8, 10)$.

$$
M = \left(\frac{2+8}{2}, \frac{4+10}{2}\right) = \left(\frac{10}{2}, \frac{14}{2}\right) = (5, 7)
$$

$$
\boxed{M = (5, 7)}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-puntomedio1" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-puntomedio1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-puntomedio1', {
      boundingbox: [-1, 12, 10, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var A = board.create('point', [2, 4], {name: 'A(2, 4)', size: 4, fixed: true, color: '#3b82f6', label: {fontSize: 11, offset: [-50, -10]}});
    var B = board.create('point', [8, 10], {name: 'B(8, 10)', size: 4, fixed: true, color: '#3b82f6', label: {fontSize: 11, offset: [5, 10]}});
    
    // Segmento AB
    board.create('segment', [A, B], {strokeColor: '#94a3b8', strokeWidth: 2, fixed: true});
    
    // Punto medio
    board.create('point', [5, 7], {name: 'M(5, 7)', size: 5, fixed: true, color: '#22c55e', label: {fontSize: 12, offset: [8, 8], cssStyle: 'font-weight: bold;'}});
    
    board.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 4

Encontrar el punto medio entre $P(-4, 3)$ y $Q(6, -1)$.

$$
M = \left(\frac{-4+6}{2}, \frac{3+(-1)}{2}\right) = \left(\frac{2}{2}, \frac{2}{2}\right) = (1, 1)
$$

$$
\boxed{M = (1, 1)}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-puntomedio2" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-puntomedio2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-puntomedio2', {
      boundingbox: [-6, 5, 8, -3], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var P = board.create('point', [-4, 3], {name: 'P(-4, 3)', size: 4, fixed: true, color: '#ef4444', label: {fontSize: 11, offset: [-55, 10]}});
    var Q = board.create('point', [6, -1], {name: 'Q(6, -1)', size: 4, fixed: true, color: '#ef4444', label: {fontSize: 11, offset: [5, -12]}});
    
    // Segmento PQ
    board.create('segment', [P, Q], {strokeColor: '#94a3b8', strokeWidth: 2, fixed: true});
    
    // Punto medio
    board.create('point', [1, 1], {name: 'M(1, 1)', size: 5, fixed: true, color: '#22c55e', label: {fontSize: 12, offset: [8, 8], cssStyle: 'font-weight: bold;'}});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📋 Resumen

| Concepto | Fórmula |
|:---------|:-------:|
| Distancia | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Punto medio | $M = \left(\dfrac{x_1+x_2}{2}, \dfrac{y_1+y_2}{2}\right)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula la distancia entre $A(0, 0)$ y $B(3, 4)$.

<details>
<summary>Ver solución</summary>

$$
d = \sqrt{9 + 16} = \sqrt{25} = 5
$$

</details>

---

**Ejercicio 2:** Encuentra el punto medio entre $(2, 6)$ y $(8, 2)$.

<details>
<summary>Ver solución</summary>

$$
M = (5, 4)
$$

</details>

---

**Ejercicio 3:** Calcula la distancia entre $(-1, 2)$ y $(2, 6)$.

<details>
<summary>Ver solución</summary>

$$
d = \sqrt{(3)^2 + (4)^2} = \sqrt{25} = 5
$$

</details>

---

**Ejercicio 4:** Encuentra el punto medio entre $(-6, 4)$ y $(2, -2)$.

<details>
<summary>Ver solución</summary>

$$
M = \left(\frac{-6+2}{2}, \frac{4-2}{2}\right) = (-2, 1)
$$

</details>

---

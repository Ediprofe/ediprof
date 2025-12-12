


# **Suma y resta de vectores**

En física, muchas veces se necesita combinar varias magnitudes vectoriales.
Para hacerlo, utilizamos la **suma** y la **resta de vectores**, que pueden representarse **gráfica** o **analíticamente**.

---

## **1. Suma de vectores**

La **suma de vectores** consiste en obtener un **vector resultante** que tiene el mismo efecto que todos los vectores originales actuando juntos.

### **a) Método gráfico: regla del triángulo**

Si se quieren sumar dos vectores $\vec{A}$ y $\vec{B}$:

1. Dibuja el vector $\vec{A}$.
2. Coloca la **cola de $\vec{B}$ en la punta de $\vec{A}$**.
3. El vector resultante $\vec{R}$ se traza desde la **cola de $\vec{A}$** hasta la **punta de $\vec{B}$**.

$$
\vec{R} = \vec{A} + \vec{B}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-triangulo" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    
    var board1 = JXG.JSXGraph.initBoard('jsxgraph-triangulo', {
      boundingbox: [-1, 8, 10, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Origen fijo
    var O = board1.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Punto A - ARRASTRABLE (punta del vector A)
    var A = board1.create('point', [4, 1.5], {name: '', size: 4, color: '#3b82f6'});
    
    // Vector A (de O a A)
    board1.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board1.create('text', [function() { return A.X()/2 - 0.3; }, function() { return A.Y()/2 + 0.5; }, 'A'], 
      {fontSize: 16, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Punto R - ARRASTRABLE (punta del vector B, que es donde termina el resultante)
    var R = board1.create('point', [6, 5], {name: '', size: 4, color: '#ef4444'});
    
    // Vector B va de A a R (regla del triángulo). B = R - A conceptualmente.
    board1.create('arrow', [A, R], {strokeColor: '#ef4444', strokeWidth: 3});
    board1.create('text', [function() { return (A.X() + R.X())/2 + 0.4; }, function() { return (A.Y() + R.Y())/2 + 0.3; }, 'B'], 
      {fontSize: 16, strokeColor: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector Resultante R (desde O hasta R, punteado verde)
    board1.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2});
    board1.create('text', [function() { return R.X()/2 - 0.5; }, function() { return R.Y()/2 + 0.5; }, 'R'], 
      {fontSize: 16, strokeColor: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    board1.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra el punto azul (punta de A) o el punto rojo (punta de B) para ver cómo cambia el vector resultante R.


### **b) Método gráfico: regla del paralelogramo**

Si los vectores $\vec{A}$ y $\vec{B}$ parten del mismo punto, se completa un **paralelogramo** con ellos como lados adyacentes.
La **diagonal del paralelogramo** representa el vector resultante $\vec{R}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-paralelogramo" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-paralelogramo', {
      boundingbox: [-1, 7, 9, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Origen fijo
    var O = board2.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Punto A - ARRASTRABLE
    var A = board2.create('point', [5, 1], {name: '', size: 4, color: '#3b82f6'});
    board2.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board2.create('text', [function() { return A.X()/2; }, function() { return A.Y()/2 - 0.5; }, 'A'], 
      {fontSize: 16, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Punto B - ARRASTRABLE
    var B = board2.create('point', [2, 4], {name: '', size: 4, color: '#ef4444'});
    board2.create('arrow', [O, B], {strokeColor: '#ef4444', strokeWidth: 3});
    board2.create('text', [function() { return B.X()/2 - 0.6; }, function() { return B.Y()/2 + 0.3; }, 'B'], 
      {fontSize: 16, strokeColor: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Punto R (suma, calculado)
    var R = board2.create('point', [function() { return A.X() + B.X(); }, function() { return A.Y() + B.Y(); }], 
      {name: '', size: 3, color: '#22c55e', fixed: true});
    
    // Lados del paralelogramo (punteados)
    board2.create('segment', [A, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    board2.create('segment', [B, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    
    // Vector Resultante
    board2.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 3});
    board2.create('text', [function() { return (A.X() + B.X())/2 + 0.4; }, function() { return (A.Y() + B.Y())/2 + 0.4; }, 'R'], 
      {fontSize: 16, strokeColor: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    board2.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra los puntos azul y rojo para modificar los vectores y observar cómo la diagonal del paralelogramo siempre es el vector resultante.

### **c) Método analítico (por componentes)**

Cuando los vectores están en el plano cartesiano, se suman sus **componentes** en cada eje:

$$
\vec{R} = \vec{A} + \vec{B}
$$

Si

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

y

$$
\vec{B} = B_x\,\hat{i} + B_y\,\hat{j}
$$

entonces:

$$
\vec{R} = (A_x + B_x)\,\hat{i} + (A_y + B_y)\,\hat{j}
$$

La **magnitud** del vector resultante es:

$$
|\vec{R}| = \sqrt{R_x^2 + R_y^2}
$$

y la **dirección** con respecto al eje $x$ se obtiene con:

$$
\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)
$$

---

## **2. Resta de vectores**

La **resta de vectores** consiste en encontrar la diferencia entre dos vectores:

$$
\vec{R} = \vec{A} - \vec{B}
$$

Restar un vector equivale a **sumar su opuesto**, que tiene la **misma magnitud** pero **sentido contrario**:

$$
\vec{A} - \vec{B} = \vec{A} + (-\vec{B})
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 520px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-resta" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    
    var board3 = JXG.JSXGraph.initBoard('jsxgraph-resta', {
      boundingbox: [-5, 5, 6, -3],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Origen fijo
    var O = board3.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Vector A - ARRASTRABLE
    var A = board3.create('point', [4, 3], {name: '', size: 4, color: '#3b82f6'});
    board3.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board3.create('text', [function() { return A.X() + 0.3; }, function() { return A.Y() + 0.4; }, 'A'], 
      {fontSize: 16, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector B - ARRASTRABLE
    var B = board3.create('point', [3, 1], {name: '', size: 4, color: '#ef4444'});
    board3.create('arrow', [O, B], {strokeColor: '#ef4444', strokeWidth: 3});
    board3.create('text', [function() { return B.X() + 0.3; }, function() { return B.Y() - 0.5; }, 'B'], 
      {fontSize: 16, strokeColor: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector -B (calculado, punteado naranja)
    var negB = board3.create('point', [function() { return -B.X(); }, function() { return -B.Y(); }], {visible: false, fixed: true});
    board3.create('arrow', [O, negB], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    board3.create('text', [function() { return -B.X() - 0.6; }, function() { return -B.Y() - 0.4; }, '-B'], 
      {fontSize: 14, strokeColor: '#f97316', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector Resultante R = A - B (calculado)
    var R = board3.create('point', [function() { return A.X() - B.X(); }, function() { return A.Y() - B.Y(); }], 
      {name: '', size: 3, color: '#22c55e', fixed: true});
    board3.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 3});
    board3.create('text', [function() { return (A.X() - B.X()) + 0.4; }, function() { return (A.Y() - B.Y()) + 0.4; }, 'R'], 
      {fontSize: 16, strokeColor: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    board3.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra A y B para ver cómo cambia $-\vec{B}$ (naranja) y el vector resultante (verde) $\vec{R} = \vec{A} - \vec{B}$.

### **Ejemplo gráfico**

1. Dibuja $\vec{A}$.
2. Invierte el sentido de $\vec{B}$ para obtener $-\vec{B}$.
3. Suma $\vec{A}$ y $-\vec{B}$ con la regla del triángulo.

---

## **3. Ejemplo analítico**

Sean los vectores:

$$
\vec{A} = 6\,\hat{i} + 3\,\hat{j}
$$

$$
\vec{B} = 2\,\hat{i} + 5\,\hat{j}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-ejemplo" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    
    var board4 = JXG.JSXGraph.initBoard('jsxgraph-ejemplo', {
      boundingbox: [-1, 10, 10, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Origen fijo
    var O = board4.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Vector A = 6i + 3j (FIJO - es un ejemplo concreto)
    var A = board4.create('point', [6, 3], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    board4.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board4.create('text', [3, 2, 'A'], {fontSize: 16, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector B desde la punta de A (FIJO)
    var B_end = board4.create('point', [8, 8], {name: '', size: 3, fixed: true, color: '#ef4444'});
    board4.create('arrow', [A, B_end], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    board4.create('text', [7.3, 5, 'B'], {fontSize: 16, strokeColor: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector Resultante (FIJO)
    board4.create('arrow', [O, B_end], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board4.create('text', [3.5, 5, 'R = (8, 8)'], {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Ángulo de 45°
    board4.create('angle', [A, O, B_end], {
      radius: 1.3,
      name: '45°',
      strokeColor: '#22c55e',
      fillColor: 'rgba(34, 197, 94, 0.2)',
      fixed: true
    });
    
    // Líneas punteadas para componentes
    var projX = board4.create('point', [8, 0], {visible: false, fixed: true});
    board4.create('segment', [B_end, projX], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3});
    
    board4.unsuspendUpdate();
  }
});
</script>

Entonces:

$$
\vec{R} = \vec{A} + \vec{B} = (6 + 2)\,\hat{i} + (3 + 5)\,\hat{j}
$$

$$
\vec{R} = 8\,\hat{i} + 8\,\hat{j}
$$

La **magnitud** del vector resultante es:

$$
|\vec{R}| = \sqrt{8^2 + 8^2} = \sqrt{128} \approx 11.3\,\text{u}
$$

y la **dirección**:

$$
\theta = \tan^{-1}\left(\frac{8}{8}\right) = 45^\circ
$$

Por lo tanto, el vector resultante tiene una **magnitud de $11.3\,\text{u}$** y una **dirección de $45^\circ$** respecto al eje $x$.

---

## 📘 **En resumen**

* Los vectores se **suman y restan** respetando su dirección y sentido.
* En el plano cartesiano, se combinan **por componentes**.
* El vector resultante indica el **efecto combinado** de todas las magnitudes vectoriales.

---

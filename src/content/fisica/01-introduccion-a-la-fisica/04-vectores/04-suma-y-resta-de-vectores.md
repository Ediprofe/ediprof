


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

<div id="jsxgraph-triangulo" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board1 = JXG.JSXGraph.initBoard('jsxgraph-triangulo', {
      boundingbox: [-1, 6, 8, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vector A (azul)
    var A = board1.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#3b82f6'});
    var A_end = board1.create('point', [4, 2], {name: '', size: 3, color: '#3b82f6'});
    var vecA = board1.create('arrow', [A, A_end], {strokeColor: '#3b82f6', strokeWidth: 3});
    var labelA = board1.create('text', [2, 1.5, 'A'], {fontSize: 18, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector B (rojo) - cola en la punta de A
    var B_end = board1.create('point', [6, 5], {name: '', size: 3, color: '#ef4444'});
    var vecB = board1.create('arrow', [A_end, B_end], {strokeColor: '#ef4444', strokeWidth: 3});
    var labelB = board1.create('text', [5.5, 3.5, 'B'], {fontSize: 18, color: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector Resultante (verde)
    var vecR = board1.create('arrow', [A, B_end], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2});
    var labelR = board1.create('text', [3, 3, 'R'], {fontSize: 18, color: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    board1.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra los puntos azul y rojo para ver cómo cambia el vector resultante (verde punteado).

> 💡 Este método también puede extenderse para tres o más vectores, colocando cada uno a continuación del anterior.

### **b) Método gráfico: regla del paralelogramo**

Si los vectores $\vec{A}$ y $\vec{B}$ parten del mismo punto, se completa un **paralelogramo** con ellos como lados adyacentes.
La **diagonal del paralelogramo** representa el vector resultante $\vec{R}$.

<div id="jsxgraph-paralelogramo" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-paralelogramo', {
      boundingbox: [-1, 6, 8, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Punto origen
    var O = board2.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b'});
    
    // Vector A (azul)
    var A = board2.create('point', [5, 1], {name: '', size: 3, color: '#3b82f6'});
    var vecA = board2.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    var labelA = board2.create('text', [2.5, 0.2, 'A'], {fontSize: 18, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector B (rojo)
    var B = board2.create('point', [2, 4], {name: '', size: 3, color: '#ef4444'});
    var vecB = board2.create('arrow', [O, B], {strokeColor: '#ef4444', strokeWidth: 3});
    var labelB = board2.create('text', [0.7, 2.2, 'B'], {fontSize: 18, color: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Punto de la diagonal (suma de vectores)
    var R = board2.create('point', [function() { return A.X() + B.X(); }, function() { return A.Y() + B.Y(); }], 
      {name: '', size: 3, color: '#22c55e', visible: true});
    
    // Lados del paralelogramo (punteados)
    var lado1 = board2.create('segment', [A, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    var lado2 = board2.create('segment', [B, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2});
    
    // Vector Resultante (diagonal)
    var vecR = board2.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 3});
    var labelR = board2.create('text', [function() { return (A.X() + B.X())/2 + 0.3; }, function() { return (A.Y() + B.Y())/2 + 0.3; }, 'R'], 
      {fontSize: 18, color: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;'});
    
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

<div id="jsxgraph-resta" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 400px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board3 = JXG.JSXGraph.initBoard('jsxgraph-resta', {
      boundingbox: [-4, 5, 6, -3],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Punto origen
    var O = board3.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b'});
    
    // Vector A (azul)
    var A = board3.create('point', [4, 3], {name: '', size: 3, color: '#3b82f6'});
    var vecA = board3.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    var labelA = board3.create('text', [4.3, 3.3, 'A'], {fontSize: 18, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector B (rojo)
    var B = board3.create('point', [3, 1], {name: '', size: 3, color: '#ef4444'});
    var vecB = board3.create('arrow', [O, B], {strokeColor: '#ef4444', strokeWidth: 3});
    var labelB = board3.create('text', [3.3, 1.3, 'B'], {fontSize: 18, color: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector -B (naranja, punteado)
    var negB = board3.create('point', [function() { return -B.X(); }, function() { return -B.Y(); }], 
      {name: '', size: 2, color: '#f97316', visible: false});
    var vecNegB = board3.create('arrow', [O, negB], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    var labelNegB = board3.create('text', [function() { return -B.X() - 0.7; }, function() { return -B.Y() - 0.3; }, '-B'], 
      {fontSize: 16, color: '#f97316', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector Resultante R = A - B = A + (-B)
    var R = board3.create('point', [function() { return A.X() - B.X(); }, function() { return A.Y() - B.Y(); }], 
      {name: '', size: 3, color: '#22c55e'});
    var vecR = board3.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 3});
    var labelR = board3.create('text', [function() { return A.X() - B.X() + 0.3; }, function() { return A.Y() - B.Y() + 0.3; }, 'R = A - B'], 
      {fontSize: 14, color: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    board3.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Observa cómo $-\vec{B}$ (naranja punteado) es el opuesto de $\vec{B}$. El vector resultante verde es $\vec{A} + (-\vec{B})$.

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

<div id="jsxgraph-ejemplo" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 400px; margin: 1.5rem auto;"></div>

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
    
    // Punto origen
    var O = board4.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b'});
    
    // Vector A = 6i + 3j (azul)
    var A = board4.create('point', [6, 3], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    var vecA = board4.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    var labelA = board4.create('text', [6.3, 3.3, 'A = (6, 3)'], {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector B = 2i + 5j (rojo) - desde la punta de A
    var B_start = board4.create('point', [6, 3], {visible: false});
    var B_end = board4.create('point', [8, 8], {name: '', size: 3, fixed: true, color: '#ef4444'});
    var vecB = board4.create('arrow', [B_start, B_end], {strokeColor: '#ef4444', strokeWidth: 3});
    var labelB = board4.create('text', [7.3, 5.5, 'B = (2, 5)'], {fontSize: 14, color: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector Resultante R = 8i + 8j (verde)
    var vecR = board4.create('arrow', [O, B_end], {strokeColor: '#22c55e', strokeWidth: 3});
    var labelR = board4.create('text', [4, 4.5, 'R = (8, 8)'], {fontSize: 14, color: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Ángulo de 45°
    var angle = board4.create('angle', [A, O, B_end], {
      radius: 1.5,
      name: '45',
      color: '#22c55e',
      fillColor: 'rgba(34, 197, 94, 0.2)'
    });
    
    // Línea al eje X para mostrar componentes
    var projX = board4.create('point', [8, 0], {visible: false});
    var lineX = board4.create('segment', [B_end, projX], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3});
    var lineY = board4.create('segment', [projX, O], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3});
    
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

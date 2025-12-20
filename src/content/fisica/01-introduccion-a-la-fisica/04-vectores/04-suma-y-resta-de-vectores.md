

# **Suma y resta de vectores**

En física, muchas veces necesitamos combinar fuerzas, velocidades o desplazamientos.
Para hacerlo, utilizamos la **suma y resta de vectores**.

---

## **1. ¿Por qué sumar vectores?**

Imagina que estás nadando en un río. Nadas hacia la orilla opuesta a $2\,\text{m/s}$, pero la corriente te empuja río abajo a $3\,\text{m/s}$.

¿Hacia dónde te mueves realmente? ¿A qué velocidad?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-motivacion" class="jsxgraph-container" style="width: 100%; height: 300px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-motivacion')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-motivacion', {
      boundingbox: [-1, 5, 6, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    // Origen (nadador)
    var O = board.create('point', [1, 2], {name: '🏊', size: 0, fixed: true, label: {fontSize: 24, offset: [-12, -12]}});
    
    // Velocidad del nadador (hacia arriba)
    var Vn = board.create('point', [1, 4], {visible: false, fixed: true});
    board.create('arrow', [O, Vn], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    board.create('text', [0.2, 3.2, '2 m/s'], {fontSize: 12, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [0.2, 2.8, '(nadar)'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true});
    
    // Velocidad de corriente (hacia la derecha)
    var Vc = board.create('point', [4, 2], {visible: false, fixed: true});
    board.create('arrow', [O, Vc], {strokeColor: '#ef4444', strokeWidth: 4, fixed: true});
    board.create('text', [2.3, 1.3, '3 m/s (corriente)'], {fontSize: 12, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Velocidad resultante
    var R = board.create('point', [4, 4], {visible: false, fixed: true});
    board.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 4, dash: 2, fixed: true});
    board.create('text', [3.5, 4.2, '¿Resultado?'], {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Líneas del paralelogramo
    board.create('segment', [Vn, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('segment', [Vc, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

Para responder, necesitamos **sumar los vectores** de velocidad. ¡Eso es lo que aprenderemos!

---

## **2. Caso más simple: vectores en línea**

Empecemos con el caso más fácil: vectores que apuntan en la **misma dirección**.

### **a) Mismo sentido**

Si dos vectores apuntan en el **mismo sentido**, el resultante es la **suma de las magnitudes**:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mismosentido" class="jsxgraph-container" style="width: 100%; height: 180px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mismosentido')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mismosentido', {
      boundingbox: [-0.5, 3, 9, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    // Línea base
    board.create('line', [[0,1], [1,1]], {strokeColor: '#cbd5e1', strokeWidth: 1, straightFirst: false, straightLast: true, fixed: true, lastArrow: true});
    
    // Vector A (3 unidades)
    board.create('arrow', [[0, 1.8], [3, 1.8]], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    board.create('text', [1.2, 2.3, 'A = 3'], {fontSize: 13, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector B (2 unidades, desde la punta de A)
    board.create('arrow', [[3, 1.8], [5, 1.8]], {strokeColor: '#ef4444', strokeWidth: 4, fixed: true});
    board.create('text', [3.7, 2.3, 'B = 2'], {fontSize: 13, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Resultante (5 unidades)
    board.create('arrow', [[0, 0.3], [5, 0.3]], {strokeColor: '#22c55e', strokeWidth: 4, fixed: true});
    board.create('text', [2, -0.3, 'R = 3 + 2 = 5'], {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

$$
\vec{R} = \vec{A} + \vec{B} \quad \Rightarrow \quad |\vec{R}| = 3 + 2 = 5
$$

### **b) Sentidos opuestos**

Si apuntan en **sentidos opuestos**, el resultante es la **diferencia de magnitudes**:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-opuesto" class="jsxgraph-container" style="width: 100%; height: 180px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-opuesto')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-opuesto', {
      boundingbox: [-0.5, 3, 9, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    // Vector A (5 unidades hacia derecha)
    board.create('arrow', [[0, 1.8], [5, 1.8]], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    board.create('text', [2, 2.3, 'A = 5'], {fontSize: 13, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector B (2 unidades hacia izquierda, desde la punta de A)
    board.create('arrow', [[5, 1.8], [3, 1.8]], {strokeColor: '#ef4444', strokeWidth: 4, fixed: true});
    board.create('text', [3.7, 2.3, 'B = 2'], {fontSize: 13, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Resultante (3 unidades)
    board.create('arrow', [[0, 0.3], [3, 0.3]], {strokeColor: '#22c55e', strokeWidth: 4, fixed: true});
    board.create('text', [1, -0.3, 'R = 5 - 2 = 3'], {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

$$
|\vec{R}| = 5 - 2 = 3 \quad \text{(en la dirección del mayor)}
$$

> 💡 **Intuición:** Es como una tira y afloja. Si un equipo jala con 5 unidades y el otro con 2, gana el primero con una fuerza neta de 3.

---

## **3. Método del triángulo (punta a cola)**

Cuando los vectores **no están en línea**, usamos métodos gráficos. Uno de ellos es el **método del triángulo**.

### Pasos:
1. Dibuja el vector $\vec{A}$ desde el origen
2. Desde la **punta de A**, dibuja el vector $\vec{B}$
3. El resultante $\vec{R}$ va desde el **origen** hasta la **punta de B**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-triangulo" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-triangulo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-triangulo', {
      boundingbox: [-1, 8, 10, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    // Vector B guardado como offset
    var Bvec = {x: 2, y: 3.5};
    
    // Origen fijo
    var O = board.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Punto A - ARRASTRABLE (punta del vector A) - AZUL
    var A = board.create('point', [4, 1.5], {name: '', size: 5, color: '#3b82f6'});
    
    // Bend - ARRASTRABLE (punta del vector B) - ROJO
    var Bend = board.create('point', [4 + Bvec.x, 1.5 + Bvec.y], {name: '', size: 5, color: '#ef4444'});
    
    // Cuando A se mueve, Bend se mueve para mantener B constante
    A.on('drag', function() {
      Bend.moveTo([A.X() + Bvec.x, A.Y() + Bvec.y]);
    });
    
    // Cuando Bend se mueve, actualizamos Bvec
    Bend.on('drag', function() {
      Bvec.x = Bend.X() - A.X();
      Bvec.y = Bend.Y() - A.Y();
    });
    
    // Vector A (de O a A)
    board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board.create('text', [function() { return A.X()/2 - 0.3; }, function() { return A.Y()/2 + 0.5; }, '① A'], 
      {fontSize: 14, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector B (de A a Bend) - punta a cola
    board.create('arrow', [A, Bend], {strokeColor: '#ef4444', strokeWidth: 3});
    board.create('text', [function() { return (A.X() + Bend.X())/2 + 0.4; }, function() { return (A.Y() + Bend.Y())/2 + 0.3; }, '② B'], 
      {fontSize: 14, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector Resultante R (desde O hasta Bend)
    board.create('arrow', [O, Bend], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2});
    board.create('text', [function() { return Bend.X()/2 - 0.5; }, function() { return Bend.Y()/2 + 0.5; }, '③ R'], 
      {fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Etiquetas de ejes
    board.create('text', [9.5, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.5, 7.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra el **punto azul** (A) o el **punto rojo** (B) para explorar la regla del triángulo.

> **Analogía:** Es como caminar. Primero caminas en dirección A, luego en dirección B. El resultante es el camino directo desde donde empezaste hasta donde terminaste.

---

## **4. Método del paralelogramo**

Otra forma de sumar vectores es usar el **método del paralelogramo**:

### Pasos:
1. Dibuja ambos vectores **desde el mismo punto** (origen común)
2. Completa el **paralelogramo** usando los vectores como lados
3. La **diagonal** desde el origen es el vector resultante

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-paralelogramo" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-paralelogramo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-paralelogramo', {
      boundingbox: [-1, 7, 9, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var O = board.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    var A = board.create('point', [5, 1], {name: '', size: 5, color: '#3b82f6'});
    board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board.create('text', [function() { return A.X()/2; }, function() { return A.Y()/2 - 0.5; }, 'A'], 
      {fontSize: 16, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    var B = board.create('point', [2, 4], {name: '', size: 5, color: '#ef4444'});
    board.create('arrow', [O, B], {strokeColor: '#ef4444', strokeWidth: 3});
    board.create('text', [function() { return B.X()/2 - 0.6; }, function() { return B.Y()/2 + 0.3; }, 'B'], 
      {fontSize: 16, strokeColor: '#ef4444', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    var R = board.create('point', [function() { return A.X() + B.X(); }, function() { return A.Y() + B.Y(); }], 
      {name: '', size: 3, color: '#22c55e', fixed: true});
    
    board.create('segment', [A, R], {strokeColor: '#94a3b8', strokeWidth: 2, dash: 2});
    board.create('segment', [B, R], {strokeColor: '#94a3b8', strokeWidth: 2, dash: 2});
    
    board.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 4});
    board.create('text', [function() { return (A.X() + B.X())/2 + 0.4; }, function() { return (A.Y() + B.Y())/2 + 0.4; }, 'R'], 
      {fontSize: 16, strokeColor: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    board.create('text', [8.3, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.5, 6.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra los puntos **azul** (A) y **rojo** (B) para ver cómo la diagonal siempre es el resultante.

---

## **5. Vectores perpendiculares**

Cuando los vectores forman un **ángulo recto** (90°), podemos usar el **teorema de Pitágoras**:

$$
|\vec{R}| = \sqrt{|\vec{A}|^2 + |\vec{B}|^2}
$$

### Ejemplo:

Si $|\vec{A}| = 3$ y $|\vec{B}| = 4$ forman 90°:

$$
|\vec{R}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-perpendicular" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-perpendicular')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-perpendicular', {
      boundingbox: [-0.5, 5.5, 5.5, -0.5], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var O = board.create('point', [0, 0], {name: '', size: 2, fixed: true, color: '#64748b'});
    var A = board.create('point', [3, 0], {visible: false, fixed: true});
    var B = board.create('point', [3, 4], {visible: false, fixed: true});
    
    board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('text', [1.5, -0.5, 'A = 3'], {fontSize: 13, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.create('arrow', [A, B], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    board.create('text', [3.4, 2, 'B = 4'], {fontSize: 13, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.create('arrow', [O, B], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2, fixed: true});
    board.create('text', [0.8, 2.5, 'R = 5'], {fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.create('polygon', [[2.7, 0], [2.7, 0.3], [3, 0.3], A], {fillColor: 'transparent', strokeColor: '#64748b', fixed: true, vertices: {visible: false}});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## **6. Método analítico (por componentes)**

En el plano cartesiano, cada vector se puede escribir en **componentes**:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

$$
\vec{B} = B_x\,\hat{i} + B_y\,\hat{j}
$$

Para sumar, simplemente **sumamos componente a componente**:

$$
\vec{R} = (A_x + B_x)\,\hat{i} + (A_y + B_y)\,\hat{j}
$$

### Ejemplo:

$$
\vec{A} = 6\,\hat{i} + 3\,\hat{j}, \quad \vec{B} = 2\,\hat{i} + 5\,\hat{j}
$$

$$
\vec{R} = (6+2)\,\hat{i} + (3+5)\,\hat{j} = 8\,\hat{i} + 8\,\hat{j}
$$

**Magnitud:**

$$
|\vec{R}| = \sqrt{8^2 + 8^2} = \sqrt{128} \approx 11.3
$$

**Dirección:**

$$
\theta = \tan^{-1}\left(\frac{8}{8}\right) = 45°
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-analitico" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-analitico')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-analitico', {
      boundingbox: [-1, 10, 10, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var O = board.create('point', [0, 0], {name: 'O', size: 2, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    var A = board.create('point', [6, 3], {visible: false, fixed: true});
    var B_end = board.create('point', [8, 8], {visible: false, fixed: true});
    
    // Vector A
    board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('text', [3, 1.2, 'A = (6, 3)'], {fontSize: 12, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector B (desde punta de A)
    board.create('arrow', [A, B_end], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    board.create('text', [7.3, 5.5, 'B = (2, 5)'], {fontSize: 12, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Resultante
    board.create('arrow', [O, B_end], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2, fixed: true});
    board.create('text', [3, 5.5, 'R = (8, 8)'], {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Ángulo
    board.create('angle', [A, O, B_end], {radius: 1.2, name: '45°', strokeColor: '#22c55e', fillColor: 'rgba(34, 197, 94, 0.15)', fixed: true});
    
    // Componentes de R
    board.create('segment', [[8, 0], B_end], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, fixed: true});
    board.create('segment', [[0, 8], B_end], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, fixed: true});
    
    board.create('text', [9.3, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.5, 9.3, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## **7. Resta de vectores**

Restar un vector equivale a **sumar su opuesto**:

$$
\vec{A} - \vec{B} = \vec{A} + (-\vec{B})
$$

El vector $-\vec{B}$ tiene la **misma magnitud** que $\vec{B}$ pero **sentido contrario**.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-resta" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-resta')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-resta', {
      boundingbox: [-5, 5, 6, -3], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var O = board.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Vector A
    var A = board.create('point', [4, 3], {name: '', size: 5, color: '#3b82f6'});
    board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board.create('text', [function() { return A.X() + 0.3; }, function() { return A.Y() + 0.4; }, 'A'], 
      {fontSize: 16, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector B
    var B = board.create('point', [3, 1], {name: '', size: 5, color: '#ef4444'});
    board.create('arrow', [O, B], {strokeColor: '#ef4444', strokeWidth: 3});
    board.create('text', [function() { return B.X() + 0.3; }, function() { return B.Y() - 0.5; }, 'B'], 
      {fontSize: 16, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector -B
    var negB = board.create('point', [function() { return -B.X(); }, function() { return -B.Y(); }], {visible: false, fixed: true});
    board.create('arrow', [O, negB], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    board.create('text', [function() { return -B.X() - 0.6; }, function() { return -B.Y() - 0.4; }, '-B'], 
      {fontSize: 14, strokeColor: '#f97316', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Resultante R = A - B
    var R = board.create('point', [function() { return A.X() - B.X(); }, function() { return A.Y() - B.Y(); }], 
      {name: '', size: 3, color: '#22c55e', fixed: true});
    board.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 3});
    board.create('text', [function() { return (A.X() - B.X()) + 0.4; }, function() { return (A.Y() - B.Y()) + 0.4; }, 'R = A - B'], 
      {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.create('text', [5.3, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.5, 4.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra A y B para ver cómo cambia $-\vec{B}$ (naranja) y el resultante (verde).

---

## **8. Volviendo al nadador**

Ahora podemos resolver el problema del inicio:

- Velocidad del nadador: $\vec{v}_n = 2\,\hat{j}$ (hacia arriba)
- Velocidad de corriente: $\vec{v}_c = 3\,\hat{i}$ (hacia la derecha)

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-nadador-resuelto" class="jsxgraph-container" style="width: 100%; height: 320px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-nadador-resuelto')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-nadador-resuelto', {
      boundingbox: [-0.5, 5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    
    var O = board.create('point', [1, 1], {name: '🏊', size: 0, fixed: true, label: {fontSize: 22, offset: [-12, -12]}});
    
    // Velocidad del nadador (hacia arriba) - 2 m/s
    var Vn = board.create('point', [1, 3], {visible: false, fixed: true});
    board.create('arrow', [O, Vn], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    board.create('text', [0.2, 2.2, '2 m/s'], {fontSize: 12, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [0.2, 1.9, '(nadar)'], {fontSize: 10, strokeColor: '#3b82f6', fixed: true});
    
    // Velocidad de corriente (hacia la derecha) - 3 m/s
    var Vc = board.create('point', [4, 1], {visible: false, fixed: true});
    board.create('arrow', [O, Vc], {strokeColor: '#ef4444', strokeWidth: 4, fixed: true});
    board.create('text', [2.2, 0.5, '3 m/s (corriente)'], {fontSize: 12, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Velocidad resultante - √13 ≈ 3.6 m/s
    var R = board.create('point', [4, 3], {visible: false, fixed: true});
    board.create('arrow', [O, R], {strokeColor: '#22c55e', strokeWidth: 4, fixed: true});
    board.create('text', [3.5, 3.3, '3.6 m/s'], {fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [3.5, 3.7, '¡Resultado!'], {fontSize: 11, strokeColor: '#22c55e', fixed: true});
    
    // Líneas del paralelogramo
    board.create('segment', [Vn, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('segment', [Vc, R], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    
    // Ángulo
    board.create('angle', [Vc, O, R], {radius: 0.7, name: '33.7°', strokeColor: '#22c55e', fillColor: 'rgba(34, 197, 94, 0.15)', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

$$
\vec{v}_R = 3\,\hat{i} + 2\,\hat{j}
$$

**Magnitud:**

$$
|\vec{v}_R| = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3.6\,\text{m/s}
$$

**Dirección:**

$$
\theta = \tan^{-1}\left(\frac{2}{3}\right) \approx 33.7°
$$

> ✅ **Respuesta:** El nadador se mueve a **3.6 m/s** en dirección **33.7° respecto a la corriente** (hacia arriba-derecha).

---

## 📘 **En resumen**

| Situación | Método |
|-----------|--------|
| Vectores en línea (mismo sentido) | Suma de magnitudes |
| Vectores en línea (opuestos) | Resta de magnitudes |
| Vectores en ángulo (cualquiera) | Paralelogramo o Triángulo |
| Vectores perpendiculares (90°) | Pitágoras |
| Con componentes $(x, y)$ | Suma componente a componente |
| Resta de vectores | Suma del opuesto: $A - B = A + (-B)$ |

---

## 📝 **Ejercicios de práctica**

**Ejercicio 1:** Dos fuerzas de 5 N y 12 N actúan perpendicularmente sobre un objeto. ¿Cuál es la fuerza resultante?

<details>
<summary>Ver solución</summary>

$$
|\vec{R}| = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13\,\text{N}
$$

</details>

---

**Ejercicio 2:** Si $\vec{A} = 4\,\hat{i} + 3\,\hat{j}$ y $\vec{B} = 2\,\hat{i} - 1\,\hat{j}$, calcula $\vec{A} + \vec{B}$.

<details>
<summary>Ver solución</summary>

$$
\vec{R} = (4+2)\,\hat{i} + (3-1)\,\hat{j} = 6\,\hat{i} + 2\,\hat{j}
$$

</details>

---

**Ejercicio 3:** Calcula $\vec{A} - \vec{B}$ con los vectores del ejercicio anterior.

<details>
<summary>Ver solución</summary>

$$
\vec{R} = (4-2)\,\hat{i} + (3-(-1))\,\hat{j} = 2\,\hat{i} + 4\,\hat{j}
$$

</details>

---

**Ejercicio 4:** Un auto viaja 40 km al este y luego 30 km al norte. ¿Cuál es el desplazamiento total?

<details>
<summary>Ver solución</summary>

$$
|\vec{R}| = \sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50\,\text{km}
$$

Dirección: $\theta = \tan^{-1}(30/40) = \tan^{-1}(0.75) \approx 36.9°$ al norte del este.

</details>

---

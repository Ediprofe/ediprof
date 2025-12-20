
# Multiplicación de vectores

La **multiplicación de vectores** puede entenderse como una forma de **cambiar el tamaño o el sentido de un vector**.
En este nivel estudiaremos principalmente **la multiplicación de un vector por un número (escalar)** y cómo afecta a sus componentes.

---

## 1. Multiplicación de un vector por un número (escalar)

Cuando un vector se multiplica por un **número real** (escalar), se obtiene **otro vector en la misma dirección**, pero con **magnitud diferente**.

Si $\vec{A}$ es un vector y $k$ es un escalar, entonces:

$$
\vec{B} = k\vec{A}
$$

### Casos:

* Si $k > 1$, el vector $\vec{B}$ es **más largo**.
* Si $0 < k < 1$, el vector es **más corto**.
* Si $k = -1$, el vector mantiene la magnitud pero **invierte el sentido**.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-escalar" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var axisColor = isDark ? '#94a3b8' : '#888888';
    
    var board = JXG.JSXGraph.initBoard('jsxgraph-escalar', {
      boundingbox: [-7, 5, 8, -3],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false },
      defaultAxes: {x: {strokeColor: axisColor}, y: {strokeColor: axisColor}}
    });
    
    // Origen fijo
    var O = board.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Vector A original - ARRASTRABLE para explorar
    var A = board.create('point', [3, 2], {name: '', size: 4, color: '#3b82f6'});
    board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    board.create('text', [function() { return A.X() + 0.3; }, function() { return A.Y() + 0.3; }, 'A'], 
      {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector 2A (k=2) - calculado
    var A2 = board.create('point', [function() { return 2*A.X(); }, function() { return 2*A.Y(); }], {visible: false, fixed: true});
    board.create('arrow', [O, A2], {strokeColor: '#22c55e', strokeWidth: 2});
    board.create('text', [function() { return 2*A.X() + 0.3; }, function() { return 2*A.Y() + 0.3; }, '2A'], 
      {fontSize: 12, color: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector 0.5A (k=0.5) - calculado
    var Ahalf = board.create('point', [function() { return 0.5*A.X(); }, function() { return 0.5*A.Y(); }], {visible: false, fixed: true});
    board.create('arrow', [O, Ahalf], {strokeColor: '#f59e0b', strokeWidth: 2});
    board.create('text', [function() { return 0.5*A.X() - 0.8; }, function() { return 0.5*A.Y() + 0.3; }, '0.5A'], 
      {fontSize: 11, color: '#f59e0b', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector -A (k=-1) - calculado
    var Aneg = board.create('point', [function() { return -A.X(); }, function() { return -A.Y(); }], {visible: false, fixed: true});
    board.create('arrow', [O, Aneg], {strokeColor: '#ef4444', strokeWidth: 2});
    board.create('text', [function() { return -A.X() - 0.5; }, function() { return -A.Y() - 0.4; }, '-A'], 
      {fontSize: 12, color: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Etiquetas de ejes
    board.create('text', [7.5, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.5, 4.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra el punto **A** (azul) y observa cómo todos los múltiplos cambian: **2A** (verde), **0.5A** (naranja), **-A** (rojo).

### Ejemplo:

Supón que $\vec{A}$ representa una velocidad de $4\,\text{m/s}$ hacia el este:

* $2\vec{A} \rightarrow 8\,\text{m/s}$ hacia el este
* $\tfrac12\vec{A} \rightarrow 2\,\text{m/s}$ hacia el este
* $-\vec{A} \rightarrow 4\,\text{m/s}$ hacia el oeste

$$
\vec{A} = 4\,\text{m/s} \ (\text{este})
\quad\Rightarrow\quad
-\vec{A} = 4\,\text{m/s} \ (\text{oeste})
$$

---

## 2. Multiplicación por componentes

Todo vector en el plano puede escribirse como:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

Si lo multiplicamos por un escalar $k$:

$$
k\vec{A} = (kA_x)\,\hat{i} + (kA_y)\,\hat{j}
$$

Es decir: **cada componente se multiplica por $k$**.

### Ejemplo:

$$
\vec{A} = 3\,\hat{i} + 2\,\hat{j}, \qquad k = 2
$$

Entonces:

$$
2\vec{A} = 6\,\hat{i} + 4\,\hat{j}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-componentes" class="jsxgraph-container" style="width: 100%; height: 320px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var axisColor = isDark ? '#94a3b8' : '#888888';
    
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-componentes', {
      boundingbox: [-1, 6, 8, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false },
      defaultAxes: {x: {strokeColor: axisColor}, y: {strokeColor: axisColor}}
    });
    
    // Origen fijo
    var O = board2.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Vector A = 3i + 2j (FIJO - ejemplo concreto)
    var A = board2.create('point', [3, 2], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    board2.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board2.create('text', [3.3, 2.3, 'A = (3, 2)'], {fontSize: 12, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Vector 2A = 6i + 4j (FIJO)
    var A2 = board2.create('point', [6, 4], {name: '', size: 3, fixed: true, color: '#22c55e'});
    board2.create('arrow', [O, A2], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board2.create('text', [6.3, 4.3, '2A = (6, 4)'], {fontSize: 12, color: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Línea de dirección (punteada)
    board2.create('line', [O, A], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, straightFirst: false, straightLast: true, fixed: true});
    
    // Etiquetas de ejes
    board2.create('text', [7.5, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board2.create('text', [-0.5, 5.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board2.unsuspendUpdate();
  }
});
</script>

> 💡 Observa cómo **A** y **2A** tienen la misma dirección, pero **2A** es el doble de largo.

---

## 3. Interpretación gráfica

Al representar $\vec{A}$ y $k\vec{A}$:

* Tienen la **misma dirección**.
* Si $k > 0$, apuntan al **mismo sentido**.
* Si $k < 0$, apuntan en **sentidos opuestos**.
* La **longitud** depende de $|k|$.

> **En resumen:**
>
> * Multiplicar un vector por un escalar cambia su **magnitud** y posiblemente su **sentido**.
> * Las **componentes** también se multiplican por ese escalar.

---

## 4. Aplicación práctica

En física vemos esta operación en muchas situaciones:

* $$\vec{F} = m\vec{a}$$
  (Aumentar la masa escala la fuerza.)
* $$\vec{v} = \vec{a}t$$
  (Mayor tiempo → mayor velocidad.)
* Escalado de vectores en gráficos o simulaciones.

$$
\vec{v} = \vec{a}t
\quad\Rightarrow\quad
t \uparrow \ \Rightarrow\ |\vec{v}| \uparrow
$$

---

## Conclusión

La multiplicación de un vector por un escalar permite **modificar su tamaño** y, si el escalar es negativo, **invertir su sentido**.
Más adelante podrás estudiar el **producto punto** y el **producto cruz**, pero esta operación es la base para comprenderlos.

---


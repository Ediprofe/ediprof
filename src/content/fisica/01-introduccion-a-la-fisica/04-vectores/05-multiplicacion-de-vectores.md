

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

<div id="jsxgraph-escalar" class="jsxgraph-container" style="width: 100%; max-width: 550px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-escalar', {
      boundingbox: [-6, 5, 10, -3],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Punto origen
    var O = board.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b'});
    
    // Vector A original (referencia)
    var A = board.create('point', [3, 2], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    var vecA = board.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    var labelA = board.create('text', [3.3, 2.3, 'A (original)'], {fontSize: 12, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector 2A (k=2)
    var A2 = board.create('point', [6, 4], {visible: false});
    var vecA2 = board.create('arrow', [O, A2], {strokeColor: '#22c55e', strokeWidth: 2});
    var labelA2 = board.create('text', [6.3, 4.3, '2A (k=2)'], {fontSize: 12, color: '#22c55e', cssStyle: 'font-weight: bold;'});
    
    // Vector 0.5A (k=0.5)
    var Ahalf = board.create('point', [1.5, 1], {visible: false});
    var vecAhalf = board.create('arrow', [O, Ahalf], {strokeColor: '#f59e0b', strokeWidth: 2});
    var labelAhalf = board.create('text', [1.7, 1.3, '0.5A (k=0.5)'], {fontSize: 11, color: '#f59e0b', cssStyle: 'font-weight: bold;'});
    
    // Vector -A (k=-1)
    var Aneg = board.create('point', [-3, -2], {visible: false});
    var vecAneg = board.create('arrow', [O, Aneg], {strokeColor: '#ef4444', strokeWidth: 2});
    var labelAneg = board.create('text', [-4, -2.3, '-A (k=-1)'], {fontSize: 12, color: '#ef4444', cssStyle: 'font-weight: bold;'});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Observa cómo el vector **azul original** se transforma: **verde** al duplicarlo ($k=2$), **naranja** al reducirlo ($k=0.5$), y **rojo** al invertirlo ($k=-1$).

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

<div id="jsxgraph-componentes" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-componentes', {
      boundingbox: [-1, 6, 8, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Punto origen
    var O = board2.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b'});
    
    // Vector A = 3i + 2j
    var A = board2.create('point', [3, 2], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    var vecA = board2.create('arrow', [O, A], {strokeColor: '#3b82f6', strokeWidth: 3});
    var labelA = board2.create('text', [3.2, 2.3, 'A = (3, 2)'], {fontSize: 12, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Vector 2A = 6i + 4j
    var A2 = board2.create('point', [6, 4], {name: '', size: 3, fixed: true, color: '#22c55e'});
    var vecA2 = board2.create('arrow', [O, A2], {strokeColor: '#22c55e', strokeWidth: 3});
    var labelA2 = board2.create('text', [6.2, 4.3, '2A = (6, 4)'], {fontSize: 12, color: '#22c55e', cssStyle: 'font-weight: bold; font-style: italic;'});
    
    // Línea de dirección
    var lineDir = board2.create('line', [O, A], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, straightFirst: false, straightLast: true});
    
    board2.unsuspendUpdate();
  }
});
</script>

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


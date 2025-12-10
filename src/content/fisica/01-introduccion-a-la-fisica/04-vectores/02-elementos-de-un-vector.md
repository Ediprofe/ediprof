
# Elementos de un vector

Un **vector** es una magnitud que tiene **módulo (magnitud)**, **dirección** y **sentido**.
Se representa mediante una **flecha**.
La longitud de la flecha indica la magnitud, la inclinación muestra la dirección y la punta señala el sentido.

<div id="jsxgraph-elementos" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 320px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var axisColor = isDark ? '#94a3b8' : '#ccc';
    
    var board = JXG.JSXGraph.initBoard('jsxgraph-elementos', {
      boundingbox: [-0.5, 5.5, 8, -0.5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Ejes manuales para control de color
    board.create('axis', [[0, 0], [1, 0]], {
      ticks: {visible: false},
      strokeColor: axisColor
    });
    board.create('axis', [[0, 0], [0, 1]], {
      ticks: {visible: false},
      strokeColor: axisColor
    });
    
    // Puntos del vector (ocultos y fijos - NO interactivo)
    var O = board.create('point', [1, 1], {visible: false, fixed: true});
    var P = board.create('point', [6, 4], {visible: false, fixed: true});
    
    // Vector principal
    var vec = board.create('arrow', [O, P], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    
    // Punto visible en origen (sin arrastrar)
    board.create('point', [1, 1], {name: '', size: 4, color: '#64748b', fixed: true});
    
    // Punto visible en extremo (sin arrastrar)  
    board.create('point', [6, 4], {name: '', size: 4, color: '#3b82f6', fixed: true});
    
    // Etiquetas posicionadas para NO superponerse
    board.create('text', [0.3, 0.5, 'Origen'], {fontSize: 11, color: '#64748b', fixed: true});
    board.create('text', [6.2, 4.3, 'Extremo'], {fontSize: 11, color: '#3b82f6', fixed: true});
    
    // Magnitud - etiqueta ARRIBA del vector
    board.create('text', [3, 3.5, 'Magnitud'], {fontSize: 13, color: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Flecha pequeña indicando sentido
    board.create('text', [5.5, 5, 'Sentido'], {fontSize: 11, color: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('arrow', [[5.2, 4.6], [5.8, 4.2]], {strokeColor: '#22c55e', strokeWidth: 1, fixed: true});
    
    // Ángulo theta
    var puntoEjeX = board.create('point', [3, 1], {visible: false, fixed: true});
    board.create('angle', [puntoEjeX, O, P], {
      radius: 0.8,
      name: 'θ',
      color: '#8b5cf6',
      fillColor: 'rgba(139, 92, 246, 0.2)',
      fixed: true
    });
    
    // Dirección - etiqueta a la derecha
    board.create('text', [7, 2.5, 'Direccion'], {fontSize: 11, color: '#8b5cf6', cssStyle: 'font-style: italic;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 El gráfico muestra los elementos de un vector: **magnitud** (longitud), **dirección** (ángulo θ) y **sentido** (hacia dónde apunta la flecha).

## 1. Magnitud (o módulo)

La **magnitud** de un vector es el valor numérico que indica *cuánto mide* la cantidad física que representa.
Por ejemplo, si un objeto se desplaza 5 metros, la magnitud del vector desplazamiento es:

$$
|\vec{d}| = \text{5 m}
$$

La magnitud **siempre es positiva** y **se mide con la unidad correspondiente** (metros, newtons, metros por segundo, etc.).

---

## 2. Dirección

La **dirección** indica la **línea sobre la que actúa el vector**.
Puede describirse mediante un ángulo, una orientación en el plano (por ejemplo, "norte-sur", "este-oeste") o con respecto a un eje de referencia.

Por ejemplo, si un vector forma un ángulo de $30^\circ$ con el eje $x$, decimos que su dirección es de $30^\circ$ respecto a dicho eje.

---

## 3. Sentido

El **sentido** señala **hacia dónde apunta el vector** a lo largo de su dirección.
Por ejemplo, un vector velocidad hacia el norte y otro hacia el sur tienen la misma dirección (vertical), pero **sentidos opuestos**.

<div id="jsxgraph-sentido" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 280px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var textColor = isDark ? '#e2e8f0' : '#64748b';
    
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-sentido', {
      boundingbox: [-4, 4, 4, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Título
    board2.create('text', [-2.5, 3.5, 'Misma direccion, sentidos opuestos'], {fontSize: 12, color: textColor, cssStyle: 'font-style: italic;', fixed: true});
    
    // Línea de referencia (dirección vertical)
    board2.create('line', [[0, -3], [0, 3]], {strokeColor: '#cbd5e1', strokeWidth: 1, dash: 2, straightFirst: false, straightLast: false, fixed: true});
    
    // Vector hacia arriba (norte) - puntos ocultos
    var O1 = board2.create('point', [-1.5, 0], {visible: false, fixed: true});
    var P1 = board2.create('point', [-1.5, 2.5], {visible: false, fixed: true});
    board2.create('arrow', [O1, P1], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    board2.create('text', [-2.3, 1.2, 'Norte'], {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Vector hacia abajo (sur) - puntos ocultos
    var O2 = board2.create('point', [1.5, 0], {visible: false, fixed: true});
    var P2 = board2.create('point', [1.5, -2.5], {visible: false, fixed: true});
    board2.create('arrow', [O2, P2], {strokeColor: '#ef4444', strokeWidth: 4, fixed: true});
    board2.create('text', [1.8, -1.2, 'Sur'], {fontSize: 14, color: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    board2.unsuspendUpdate();
  }
});
</script>

---

## 4. Representación simbólica

Los vectores se representan con una **letra y una flecha encima**, como $\vec{v}$ o $\vec{F}$.
A veces también se escriben con una letra en **negrita**, por ejemplo **v** o **F**, especialmente en textos impresos.

> 💡 **Ejemplo:**
> Si un cuerpo se desplaza 8 metros hacia el este, su vector desplazamiento puede expresarse como:
>
> $$
> \vec{d} = \text{8 m (este)}
> $$
>
> Aquí, *8 m* es la magnitud, la "línea este-oeste" es la dirección y "hacia el este" es el sentido.

---

## 5. Flecha representativa

Gráficamente, un vector se dibuja como una **flecha**:

* El **origen** (cola) indica el punto donde actúa la magnitud.
* La **punta** (cabeza) indica hacia dónde se dirige.
* La **longitud** es proporcional a la magnitud.
* La **orientación** muestra su dirección y sentido.

---

| Elemento  | Qué indica                     | Cómo se representa     |
| --------- | ------------------------------ | ---------------------- |
| Magnitud  | Tamaño o valor numérico        | Longitud de la flecha  |
| Dirección | Línea o ángulo de acción       | Inclinación del vector |
| Sentido   | Hacia dónde apunta             | Punta de la flecha     |
| Origen    | Punto donde comienza el vector | Cola del vector        |

---

> 📘 **En resumen:**
> Un vector combina *cuánto*, *en qué línea* y *hacia dónde*.
> Por eso se diferencia de una magnitud escalar, que solo indica *cuánto*.

---


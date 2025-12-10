# Elementos de un vector

Un **vector** es una magnitud que tiene **módulo (magnitud)**, **dirección** y **sentido**.
Se representa mediante una **flecha**.
La longitud de la flecha indica la magnitud, la inclinación muestra la dirección y la punta señala el sentido.

<div id="jsxgraph-elementos" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 350px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-elementos', {
      boundingbox: [-1, 6, 8, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Punto origen
    var O = board.create('point', [1, 1], {name: 'Origen', size: 4, fixed: true, color: '#64748b', label: {offset: [-40, -15]}});
    
    // Punto final del vector
    var P = board.create('point', [6, 4], {name: 'Extremo', size: 4, color: '#3b82f6', label: {offset: [10, 5]}});
    
    // Vector principal
    var vec = board.create('arrow', [O, P], {strokeColor: '#3b82f6', strokeWidth: 4});
    
    // Etiqueta del vector
    var labelVec = board.create('text', [3.5, 3.2, 'Magnitud'], {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold;'});
    
    // Línea de dirección (extendida)
    var lineDir = board.create('line', [O, P], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, straightFirst: true, straightLast: true});
    var labelDir = board.create('text', [7, 5, 'Direccion'], {fontSize: 12, color: '#94a3b8', cssStyle: 'font-style: italic;'});
    
    // Ángulo con el eje X
    var puntoEjeX = board.create('point', [6, 1], {visible: false});
    var angulo = board.create('angle', [puntoEjeX, O, P], {
      radius: 1,
      name: 'θ',
      color: '#22c55e',
      fillColor: 'rgba(34, 197, 94, 0.2)'
    });
    
    // Flecha indicando sentido
    var labelSentido = board.create('text', [5.5, 4.5, 'Sentido'], {fontSize: 12, color: '#ef4444', cssStyle: 'font-weight: bold;'});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra el punto azul (extremo) para ver cómo cambian los elementos del vector.

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

<div id="jsxgraph-sentido" class="jsxgraph-container" style="width: 100%; max-width: 500px; height: 280px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-sentido', {
      boundingbox: [-5, 4, 5, -4],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vector hacia arriba (norte)
    var O1 = board2.create('point', [-2, 0], {visible: false});
    var P1 = board2.create('point', [-2, 3], {visible: false});
    var vec1 = board2.create('arrow', [O1, P1], {strokeColor: '#3b82f6', strokeWidth: 3});
    var label1 = board2.create('text', [-2.5, 1.5, 'Norte'], {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold;'});
    
    // Vector hacia abajo (sur)
    var O2 = board2.create('point', [2, 0], {visible: false});
    var P2 = board2.create('point', [2, -3], {visible: false});
    var vec2 = board2.create('arrow', [O2, P2], {strokeColor: '#ef4444', strokeWidth: 3});
    var label2 = board2.create('text', [2.3, -1.5, 'Sur'], {fontSize: 14, color: '#ef4444', cssStyle: 'font-weight: bold;'});
    
    // Etiqueta central
    var labelCentral = board2.create('text', [-0.5, 3.5, 'Misma direccion, sentidos opuestos'], {fontSize: 12, color: '#64748b', cssStyle: 'font-style: italic;'});
    
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


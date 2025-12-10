# Escalares y vectores

En física, las magnitudes se dividen en **escalares** y **vectoriales**, según la información necesaria para describirlas por completo.

---

## Magnitudes escalares

Las **magnitudes escalares** se definen únicamente por **un número y una unidad de medida**. No necesitan dirección ni sentido.

Por ejemplo:

* **Tiempo:** $t = 5\,\mathrm{s}$
* **Masa:** $m = 2\,\mathrm{kg}$
* **Temperatura:** $T = 25\,^\circ\mathrm{C}$

En estos casos, basta con conocer el valor numérico y la unidad. No tiene sentido decir que la masa o el tiempo "apuntan" hacia algún lugar.

---

## Magnitudes vectoriales

Las **magnitudes vectoriales**, además del número y la unidad, requieren **dirección y sentido** para quedar completamente definidas.

Por ejemplo:

* **Desplazamiento:** indica *cuánto* y *hacia dónde* se mueve un objeto. Si una persona camina 10 metros hacia el norte, su desplazamiento es:

$$
\vec{d} = 10\,\mathrm{m}\text{ (norte)}
$$

* **Velocidad:** indica *qué tan rápido* y *en qué dirección* se mueve un cuerpo. Si un auto viaja a $60\,\mathrm{km/h}$ hacia el este, su velocidad es:

$$
\vec{v} = 60\,\mathrm{km/h}\text{ (este)}
$$

En cambio, la **distancia** y la **rapidez** son escalares, porque solo expresan *cuánto* se recorrió o *qué tan rápido* se mueve algo, sin importar la dirección.

<div id="jsxgraph-comparacion" class="jsxgraph-container" style="width: 100%; max-width: 550px; height: 300px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-comparacion', {
      boundingbox: [-1, 5, 10, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Título Escalar
    var titleEsc = board.create('text', [1.5, 4.5, 'ESCALAR'], {fontSize: 14, color: '#64748b', cssStyle: 'font-weight: bold;'});
    
    // Representación de escalar (solo número)
    var escBox = board.create('polygon', [[0.5, 2], [3.5, 2], [3.5, 3.5], [0.5, 3.5]], {
      fillColor: 'rgba(148, 163, 184, 0.2)',
      strokeColor: '#94a3b8',
      strokeWidth: 2
    });
    var escText = board.create('text', [1.2, 2.6, '5 kg'], {fontSize: 20, color: '#64748b', cssStyle: 'font-weight: bold;'});
    var escDesc = board.create('text', [0.8, 1.3, 'Solo magnitud'], {fontSize: 11, color: '#64748b', cssStyle: 'font-style: italic;'});
    
    // Título Vector
    var titleVec = board.create('text', [6.5, 4.5, 'VECTOR'], {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold;'});
    
    // Representación de vector (flecha)
    var O = board.create('point', [5.5, 2.7], {visible: false});
    var P = board.create('point', [8.5, 2.7], {visible: false});
    var vec = board.create('arrow', [O, P], {strokeColor: '#3b82f6', strokeWidth: 4});
    var vecText = board.create('text', [6.2, 3.2, '10 m/s'], {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold;'});
    var vecDir = board.create('text', [8.2, 2.2, 'Este'], {fontSize: 11, color: '#3b82f6', cssStyle: 'font-style: italic;'});
    var vecDesc = board.create('text', [5.5, 1.3, 'Magnitud + Direccion + Sentido'], {fontSize: 11, color: '#3b82f6', cssStyle: 'font-style: italic;'});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Observa la diferencia: el **escalar** solo tiene un valor numérico, mientras que el **vector** tiene valor, dirección (línea horizontal) y sentido (hacia el este).

---

## Comparación entre escalares y vectores

| Tipo de magnitud | Qué necesita para definirse         | Ejemplos                                       | Representación                            |
| ---------------- | ----------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| Escalar          | Número y unidad                     | tiempo, masa, temperatura, distancia, rapidez  | $5\,\mathrm{s}$, $2\,\mathrm{kg}$           |
| Vectorial        | Número, unidad, dirección y sentido | desplazamiento, velocidad, fuerza, aceleración | $\vec{v}$, flecha con dirección y sentido |

> 💡 **Recuerda:**
> Las magnitudes vectoriales se representan con una flecha encima del símbolo, como $\vec{v}$, y gráficamente con un vector que indica su dirección y sentido.

---
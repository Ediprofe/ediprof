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

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 550px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-comparacion" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-comparacion')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-comparacion', {
      boundingbox: [0, 5, 10, 0],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // === LADO ESCALAR (izquierda) ===
    board.create('text', [1.5, 4.3, 'ESCALAR'], {fontSize: 15, strokeColor: '#64748b', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [1.2, 2.8, '5 kg'], {fontSize: 28, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [0.8, 1.5, 'Solo número + unidad'], {fontSize: 11, strokeColor: '#64748b', cssStyle: 'font-style: italic;', fixed: true});
    
    // Línea divisoria vertical
    board.create('segment', [[5, 0.5], [5, 4.5]], {strokeColor: '#cbd5e1', strokeWidth: 2, dash: 2, fixed: true});
    
    // === LADO VECTOR (derecha) ===
    board.create('text', [7.3, 4.3, 'VECTOR'], {fontSize: 15, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Línea punteada verde para mostrar la DIRECCIÓN (horizontal extendida)
    board.create('segment', [[5.2, 2.5], [9.8, 2.5]], {strokeColor: '#22c55e', strokeWidth: 2, dash: 3, fixed: true});
    board.create('text', [5.3, 2.9, 'Dirección'], {fontSize: 9, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Flecha del vector (encima de la línea punteada)
    board.create('arrow', [[5.5, 2.5], [9.2, 2.5]], {strokeColor: '#3b82f6', strokeWidth: 5, fixed: true});
    
    // Etiqueta de magnitud
    board.create('text', [6.6, 3.5, '10 m/s'], {fontSize: 14, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [6.6, 3.1, '(magnitud)'], {fontSize: 9, strokeColor: '#3b82f6', fixed: true});
    
    // Señalar el SENTIDO (la punta de la flecha)
    board.create('text', [8.8, 1.8, 'Sentido'], {fontSize: 9, strokeColor: '#f97316', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [8.8, 1.4, '(hacia el Este)'], {fontSize: 9, strokeColor: '#f97316', fixed: true});
    // Flecha pequeña señalando la punta
    board.create('arrow', [[9.1, 1.7], [9.1, 2.3]], {strokeColor: '#f97316', strokeWidth: 2, fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Observa la diferencia: el **escalar** solo tiene un valor numérico, mientras que el **vector** tiene valor, dirección y sentido (representado por la flecha).

---

## Comparación entre escalares y vectores

| Tipo de magnitud | Qué necesita para definirse         | Ejemplos                                       | Representación                            |
| ---------------- | ----------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| Escalar          | Número y unidad                     | tiempo, masa, temperatura, distancia, rapidez  | $5\,\mathrm{s}$, $2\,\mathrm{kg}$           |
| Vectorial        | Número, unidad, dirección y sentido | desplazamiento, velocidad, fuerza, aceleración | $\vec{v}$, flecha con dirección y sentido |

> 💡 **Recuerda:**
> Las magnitudes vectoriales se representan con una flecha encima del símbolo, como $\vec{v}$, y gráficamente con un vector que indica su dirección y sentido.

---
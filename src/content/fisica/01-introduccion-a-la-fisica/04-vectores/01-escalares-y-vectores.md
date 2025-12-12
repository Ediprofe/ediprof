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
  <div id="jsxgraph-comparacion" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var textColor = isDark ? '#e2e8f0' : '#64748b';
    
    var board = JXG.JSXGraph.initBoard('jsxgraph-comparacion', {
      boundingbox: [-0.5, 4.5, 10, -0.5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // === LADO ESCALAR ===
    var titleEsc = board.create('text', [1.8, 4, 'ESCALAR'], {fontSize: 15, color: textColor, cssStyle: 'font-weight: bold;', fixed: true});
    
    // Caja para escalar (sin puntos visibles)
    var escBox = board.create('polygon', [[0.5, 1.5], [3.5, 1.5], [3.5, 3], [0.5, 3]], {
      fillColor: 'rgba(148, 163, 184, 0.15)',
      strokeColor: '#94a3b8',
      strokeWidth: 2,
      vertices: {visible: false, fixed: true}
    });
    var escText = board.create('text', [1.4, 2.1, '5 kg'], {fontSize: 22, color: textColor, cssStyle: 'font-weight: bold;', fixed: true});
    var escDesc = board.create('text', [1.2, 0.8, 'Solo magnitud'], {fontSize: 11, color: textColor, cssStyle: 'font-style: italic;', fixed: true});
    
    // === LADO VECTOR ===
    var titleVec = board.create('text', [7, 4, 'VECTOR'], {fontSize: 15, color: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Flecha del vector (puntos ocultos y fijos)
    var O = board.create('point', [5.5, 2.2], {visible: false, fixed: true});
    var P = board.create('point', [9, 2.2], {visible: false, fixed: true});
    var vec = board.create('arrow', [O, P], {strokeColor: '#3b82f6', strokeWidth: 4, fixed: true});
    
    // Etiquetas posicionadas para no superponerse
    var vecText = board.create('text', [6.5, 3], '10 m/s', {fontSize: 14, color: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    var vecDir = board.create('text', [8.5, 1.6, 'Este'], {fontSize: 12, color: '#3b82f6', cssStyle: 'font-style: italic;', fixed: true});
    var vecDesc = board.create('text', [5.3, 0.8, 'Magnitud + Direccion + Sentido'], {fontSize: 11, color: '#3b82f6', cssStyle: 'font-style: italic;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Observa la diferencia: el **escalar** solo tiene un valor numérico, mientras que el **vector** tiene valor, dirección y sentido.

---

## Comparación entre escalares y vectores

| Tipo de magnitud | Qué necesita para definirse         | Ejemplos                                       | Representación                            |
| ---------------- | ----------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| Escalar          | Número y unidad                     | tiempo, masa, temperatura, distancia, rapidez  | $5\,\mathrm{s}$, $2\,\mathrm{kg}$           |
| Vectorial        | Número, unidad, dirección y sentido | desplazamiento, velocidad, fuerza, aceleración | $\vec{v}$, flecha con dirección y sentido |

> 💡 **Recuerda:**
> Las magnitudes vectoriales se representan con una flecha encima del símbolo, como $\vec{v}$, y gráficamente con un vector que indica su dirección y sentido.

---
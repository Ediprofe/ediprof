# 📏 Representación de Fracciones en la Recta Numérica

En este tema aprenderemos a ubicar fracciones en la recta numérica.

---

## 📖 Ubicación de fracciones propias

Las fracciones propias se ubican entre $0$ y $1$.

**Método:**
1. Dividir el intervalo $[0, 1]$ en partes iguales según el denominador
2. Contar las partes según el numerador

### Ejemplo 1

Ubicar $\frac{3}{4}$:

Dividimos el intervalo en $4$ partes y avanzamos $3$:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-recta-34" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-recta-34')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-recta-34', {
      boundingbox: [-0.2, 1.5, 1.2, -0.5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Recta numérica
    board.create('line', [[0, 0], [1, 0]], {straightFirst: false, straightLast: false, strokeWidth: 2, strokeColor: '#374151'});
    
    // Marcas en cuartos
    for (var i = 0; i <= 4; i++) {
      board.create('point', [i/4, 0], {size: 2, fixed: true, color: '#374151', name: ''});
      board.create('segment', [[i/4, -0.15], [i/4, 0.15]], {strokeWidth: 1, strokeColor: '#374151', fixed: true});
    }
    
    // Etiquetas
    board.create('text', [0, -0.35, '0'], {fontSize: 12, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [0.25, -0.35, '1/4'], {fontSize: 10, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle'});
    board.create('text', [0.5, -0.35, '2/4'], {fontSize: 10, strokeColor: '#94a3b8', fixed: true, anchorX: 'middle'});
    board.create('text', [0.75, -0.35, '3/4'], {fontSize: 12, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true, anchorX: 'middle'});
    board.create('text', [1, -0.35, '1'], {fontSize: 12, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    
    // Punto resaltado en 3/4
    board.create('point', [0.75, 0], {size: 5, fixed: true, color: '#3b82f6', name: ''});
    
    board.unsuspendUpdate();
  }
});
</script>

El punto azul marca la posición de $\frac{3}{4}$ en la recta.

---

### Ejemplo 2

Ubicar $\frac{2}{5}$:

Dividimos el intervalo en $5$ partes y avanzamos $2$:

$$
0 \quad \frac{1}{5} \quad \frac{2}{5} \quad \frac{3}{5} \quad \frac{4}{5} \quad 1
$$

---

## 📖 Ubicación de fracciones impropias y números mixtos

Las fracciones impropias y números mixtos se ubican a partir del $1$.

### Ejemplo 1

Ubicar $\frac{7}{4} = 1\frac{3}{4}$:

Está entre $1$ y $2$, a $\frac{3}{4}$ del camino hacia $2$:

$$
1 \quad 1\frac{1}{4} \quad 1\frac{2}{4} \quad 1\frac{3}{4} \quad 2
$$

---

### Ejemplo 2

Ubicar $2\frac{1}{3}$:

Está entre $2$ y $3$, en el primer tercio:

$$
2 \quad 2\frac{1}{3} \quad 2\frac{2}{3} \quad 3
$$

---

## 📖 Fracciones equivalentes en la recta

Fracciones equivalentes ocupan el **mismo punto** en la recta.

### Ejemplo

$$
\frac{1}{2} = \frac{2}{4} = \frac{3}{6}
$$

Todas están en el punto medio entre $0$ y $1$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Ubica en la recta: $\frac{2}{3}$

**Ejercicio 2:** Ubica en la recta: $\frac{5}{4}$

**Ejercicio 3:** Ordena de menor a mayor ubicando en la recta: $\frac{1}{4}$, $\frac{1}{2}$, $\frac{3}{4}$

**Ejercicio 4:** ¿Entre qué números enteros se ubica $\frac{11}{5}$?

---
---
title: "Representación de Fracciones en la Recta"
---

# **Representación de Fracciones en la Recta**

Hasta ahora hemos visto fracciones como pedazos de pizza. Ahora vamos a verlas como **direcciones** en un mapa. La recta numérica es ese mapa, y las fracciones nos dicen exactamente dónde "vive" cada número.

---

## 🎯 ¿Qué vas a aprender?

- Ubicar fracciones propias (entre 0 y 1).
- Ubicar fracciones impropias y números mixtos (más allá del 1).
- Entender que fracciones diferentes pueden vivir en la misma casa (equivalentes).
- Ordenar fracciones visualmente.

---

## Ubicando Fracciones Propias

Como son menores que 1, siempre viven entre el **0** y el **1**.

**Pasos:**
1.  Dibuja el tramo del 0 al 1.
2.  Divide ese tramo en tantas partes como diga el **denominador**.
3.  Salta tantas partes como diga el **numerador**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Ubicar $\frac{3}{4}$
-   Tramo: 0 al 1.
-   Divido en 4 partes iguales.
-   Salto 3 veces desde el 0.

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
    board.create('text', [0.75, -0.35, '3/4'], {fontSize: 14, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true, anchorX: 'middle'});
    board.create('text', [1, -0.35, '1'], {fontSize: 12, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    
    // Punto resaltado en 3/4
    board.create('point', [0.75, 0], {size: 5, fixed: true, color: '#3b82f6', name: ''});
    
    board.unsuspendUpdate();
  }
});
</script>

#### Ejemplo 2: Ubicar $\frac{1}{2}$
-   Divido en 2 partes.
-   Tomo 1.
-   Está justo en el medio.

#### Ejemplo 3: Ubicar $\frac{4}{5}$
-   Divido en 5 partes.
-   Cuento 4 saltos: $\frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \boxed{\frac{4}{5}}$.

#### Ejemplo 4: Ubicar $\frac{2}{3}$
-   Divido en 3 tercios.
-   Tomo el segundo punto.

#### Ejemplo 5: Ubicar $\frac{0}{4}$
-   Es el mismo punto que el **0**.

---

## Ubicando Fracciones Impropias y Mixtos

Como son mayores que 1, viven a la derecha del 1. A veces es más fácil convertirlas a número mixto primero.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: Ubicar $1\frac{1}{4}$
-   Busco el entero **1**.
-   Desde el 1, avanzo $\frac{1}{4}$ hacia el 2.

#### Ejemplo 7: Ubicar $\frac{3}{2}$
-   Es impropia. Convertimos: $\frac{3}{2} = 1\frac{1}{2}$.
-   Está entre el 1 y el 2, justo en la mitad.

#### Ejemplo 8: Ubicar $\frac{5}{3}$
-   Divido cada unidad (0-1, 1-2) en 3 partes.
-   Cuento 5 tercios desde el 0:
    $\frac{1}{3}, \frac{2}{3}, \frac{3}{3} (1), \frac{4}{3}, \boxed{\frac{5}{3}}$.

#### Ejemplo 9: Ubicar $2\frac{3}{4}$
-   Me paro en el **2**.
-   Avanzo 3 pasos de cuartos hacia el 3.

#### Ejemplo 10: Ubicar $\frac{10}{2}$
-   $10 \div 2 = 5$.
-   Es el punto exacto del entero **5**.

---

## Fracciones Equivalentes en la Recta

Si dos fracciones son equivalentes, viven en la **misma dirección**. Son vecinos que comparten casa.

### ⚙️ Ejemplos Visuales

$$ \frac{1}{2} = \frac{2}{4} = \frac{4}{8} $$

Todas marcan el centro exacto entre 0 y 1.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Entre qué números enteros está $\frac{1}{3}$?

<details>
<summary>Ver solución</summary>

Es propia.
**Resultado:** $\boxed{0 \text{ y } 1}$

</details>

### Ejercicio 2
¿Entre qué números enteros está $\frac{5}{3}$?

<details>
<summary>Ver solución</summary>

$\frac{5}{3} = 1\frac{2}{3}$.
**Resultado:** $\boxed{1 \text{ y } 2}$

</details>

### Ejercicio 3
Ubica el número $1.5$ en fracción.

<details>
<summary>Ver solución</summary>

$1.5 = 1\frac{1}{2} = \frac{3}{2}$.
**Resultado:** $\boxed{\frac{3}{2}}$

</details>

### Ejercicio 4
Si divido del 0 al 1 en 10 partes, ¿dónde queda $\frac{1}{2}$?

<details>
<summary>Ver solución</summary>

$\frac{1}{2} = \frac{5}{10}$.
**Resultado:** $\boxed{\text{En la quinta marca}}$

</details>

### Ejercicio 5
¿Qué fracción está justo a la mitad de 2 y 3?

<details>
<summary>Ver solución</summary>

$2\frac{1}{2} = \frac{5}{2}$.
**Resultado:** $\boxed{2\frac{1}{2}}$

</details>

### Ejercicio 6
Ubica $\frac{7}{7}$ en la recta.

<details>
<summary>Ver solución</summary>

$7 \div 7 = 1$.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 7
Ordena de menor a mayor: $0$, $\frac{1}{2}$, $1$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{0 < \frac{1}{2} < 1}$

</details>

### Ejercicio 8
¿Cuántos cuartos ($\frac{1}{4}$) necesitas para llegar al 2?

<details>
<summary>Ver solución</summary>

$2 \times 4 = 8$.
**Resultado:** $\boxed{8 \text{ cuartos}}$

</details>

### Ejercicio 9
Ubica $3\frac{1}{4}$.

<details>
<summary>Ver solución</summary>

Entre 3 y 4, en el primer cuarto.
**Resultado:** $\boxed{3.25}$

</details>

### Ejercicio 10
¿La fracción $\frac{8}{4}$ es un punto o un tramo?

<details>
<summary>Ver solución</summary>

Todas las fracciones son **puntos** específicos. En este caso el punto 2.
**Resultado:** $\boxed{\text{Punto}}$

</details>

---

## 🔑 Resumen

| Tipo | Ubicación |
| :--- | :--- |
| **Propia** | Entre 0 y 1. |
| **Impropia** | A partir del 1 (o en el 1). |
| **Mixta** | Entre el entero y el siguiente. |

> **Conclusión:** La recta numérica nos permite ver qué fracción es más grande o más pequeña simplemente mirando cuál está más a la derecha.
# **Descomposición en Factores Primos**

Imagina que cada número compuesto es una construcción de Lego. La **descomposición prima** es desarmar esa construcción hasta tener solo los bloques originales (los números primos) que la formaron. Cualquier número mayor que 1 es primo o se puede escribir de forma única como una multiplicación de primos.

---

## 🎯 ¿Qué vas a aprender?

- Descomponer cualquier número en sus factores primos.
- Usar el método de "divisiones sucesivas" (la línea vertical).
- Escribir la factorización usando potencias (ej. $2^3 \times 3$).
- Entender el "ADN matemático" de los números.

---

## Método de Divisiones Sucesivas

Es el método más ordenado. Trazamos una línea vertical y dividimos por números primos en orden ($2, 3, 5, 7, 11...$).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Factorizar 60
1.  ¿Divisible por 2? $60 \div 2 = 30$.
2.  ¿Divisible por 2? $30 \div 2 = 15$.
3.  ¿Divisible por 2? No. ¿Por 3? $15 \div 3 = 5$.
4.  ¿Divisible por 3? No. ¿Por 5? $5 \div 5 = 1$.
**Resultado:** $60 = 2 \times 2 \times 3 \times 5 = \boxed{2^2 \times 3 \times 5}$

#### Ejemplo 2: Factorizar 24
- $24 \div 2 = 12$
- $12 \div 2 = 6$
- $6 \div 2 = 3$
- $3 \div 3 = 1$
**Resultado:** $24 = 2^3 \times 3$.

#### Ejemplo 3: Factorizar 98
- $98 \div 2 = 49$
- ¿49 por 2? No. ¿3? No ($4+9=13$). ¿5? No. ¿7? Sí.
- $49 \div 7 = 7$
- $7 \div 7 = 1$
**Resultado:** $98 = 2 \times 7^2$.

#### Ejemplo 4: Factorizar 100
- $100 \div 2 = 50$
- $50 \div 2 = 25$
- $25 \div 5 = 5$
- $5 \div 5 = 1$
**Resultado:** $100 = 2^2 \times 5^2$.

#### Ejemplo 5: Factorizar 17
- Es primo. No se descompone (salvo $17 \times 1$).
**Resultado:** $17$.

---

<!-- Conservando imágenes existentes -->

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-fact60" class="jsxgraph-container" style="width: 100%; height: 220px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-fact60')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-fact60', {
      boundingbox: [-0.5, 5.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Línea vertical divisora
    board.create('segment', [[2, 5], [2, 0.5]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Números a la izquierda
    board.create('text', [1, 4.5, '60'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 3.5, '30'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '15'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 1.5, '5'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 0.5, '1'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Factores primos a la derecha
    board.create('text', [2.5, 4.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 3.5, '2'], {fontSize: 18, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 2.5, '3'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 1.5, '5'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0.3, 4-i], [2.8, 4-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Descompón el número 12.

<details>
<summary>Ver solución</summary>

$12 \div 2 = 6$, $6 \div 2 = 3$, $3 \div 3 = 1$.
**Resultado:** $\boxed{2^2 \times 3}$

</details>

### Ejercicio 2
Descompón el número 50.

<details>
<summary>Ver solución</summary>

$50 \div 2 = 25$, $25 \div 5 = 5$, $5 \div 5 = 1$.
**Resultado:** $\boxed{2 \times 5^2}$

</details>

### Ejercicio 3
Descompón el número 36.

<details>
<summary>Ver solución</summary>

$36 = 2 \times 18 = 2 \times 2 \times 9 = 2 \times 2 \times 3 \times 3$.
**Resultado:** $\boxed{2^2 \times 3^2}$

</details>

### Ejercicio 4
Descompón el número 45.

<details>
<summary>Ver solución</summary>

$45 \div 3 = 15$, $15 \div 3 = 5$, $5 \div 5 = 1$.
**Resultado:** $\boxed{3^2 \times 5}$

</details>

### Ejercicio 5
Descompón el número 32.

<details>
<summary>Ver solución</summary>

$2 \times 2 \times 2 \times 2 \times 2$.
**Resultado:** $\boxed{2^5}$

</details>

### Ejercicio 6
Descompón 110.

<details>
<summary>Ver solución</summary>

$110 \div 2 = 55$, $55 \div 5 = 11$, $11 \div 11 = 1$.
**Resultado:** $\boxed{2 \times 5 \times 11}$

</details>

### Ejercicio 7
Si un número es $2^2 \times 5$, ¿cuál es?

<details>
<summary>Ver solución</summary>

$4 \times 5 = 20$.
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 8
Descompón 72.

<details>
<summary>Ver solución</summary>

$72 \div 2=36$, $36 \div 2=18$, $18 \div 2=9$, $9 \div 3=3$.
**Resultado:** $\boxed{2^3 \times 3^2}$

</details>

### Ejercicio 9
Descompón 1000.

<details>
<summary>Ver solución</summary>

$1000 = 10^3 = (2 \times 5)^3$.
**Resultado:** $\boxed{2^3 \times 5^3}$

</details>

### Ejercicio 10
Descompón 19.

<details>
<summary>Ver solución</summary>

Es primo.
**Resultado:** $\boxed{19}$

</details>

---

## 🔑 Resumen

> **Dato Clave:** Todo número mayor que 1 tiene un **ADN único**. Por ejemplo, el 12 siempre será $2^2 \times 3$. No hay otra combinación de primos que dé 12. ¡Esta unicidad se llama el **Teorema Fundamental de la Aritmética**!

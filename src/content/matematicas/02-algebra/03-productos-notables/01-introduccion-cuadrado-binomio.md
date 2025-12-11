# ✨ Introducción y Cuadrado de un Binomio

En esta lección aprenderemos qué son los productos notables y estudiaremos el primero de ellos: el cuadrado de un binomio.

---

## 📖 ¿Qué son los productos notables?

Los **productos notables** son multiplicaciones de expresiones algebraicas que siguen patrones fijos y dan resultados que se pueden memorizar. Conocerlos nos permite:

- Realizar cálculos más rápido
- Evitar errores comunes
- Factorizar expresiones algebraicas

### ¿Por qué se llaman "notables"?

Se llaman **notables** porque:
1. Son muy frecuentes en álgebra
2. Sus resultados siguen patrones fáciles de recordar
3. Son la base para técnicas más avanzadas

---

## 📋 Resumen de Productos Notables

A continuación se presenta un resumen de todos los productos notables que estudiaremos en este tema:

| Nombre | Fórmula | Resultado |
|:-------|:--------|:----------|
| Cuadrado de una suma | $(a + b)^2$ | $a^2 + 2ab + b^2$ |
| Cuadrado de una diferencia | $(a - b)^2$ | $a^2 - 2ab + b^2$ |
| Cuadrado de un trinomio | $(a + b + c)^2$ | $a^2 + b^2 + c^2 + 2ab + 2ac + 2bc$ |
| Producto de conjugados | $(a + b)(a - b)$ | $a^2 - b^2$ |
| Binomios con término común | $(x + a)(x + b)$ | $x^2 + (a+b)x + ab$ |
| Cubo de una suma | $(a + b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |
| Cubo de una diferencia | $(a - b)^3$ | $a^3 - 3a^2b + 3ab^2 - b^3$ |

> **Nota:** Cada producto notable se estudia en detalle en las siguientes lecciones de este tema.

---

## 📖 Cuadrado de un binomio

El **cuadrado de un binomio** es el resultado de multiplicar un binomio por sí mismo.

### Cuadrado de una suma

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

**En palabras:** El cuadrado de una suma es igual al cuadrado del primer término, más el doble del producto de ambos términos, más el cuadrado del segundo término.

### Demostración

$$
(a + b)^2 = (a + b)(a + b)
$$

$$
= a \cdot a + a \cdot b + b \cdot a + b \cdot b
$$

$$
= a^2 + ab + ab + b^2
$$

$$
= a^2 + 2ab + b^2
$$

### Ejemplo 1

Desarrolla: $(x + 3)^2$

Identificamos: $a = x$, $b = 3$

$$
(x + 3)^2 = x^2 + 2(x)(3) + 3^2
$$

$$
= x^2 + 6x + 9
$$

$$
\boxed{x^2 + 6x + 9}
$$

### Ejemplo 2

Desarrolla: $(2a + 5)^2$

Identificamos: $a = 2a$, $b = 5$

$$
(2a + 5)^2 = (2a)^2 + 2(2a)(5) + 5^2
$$

$$
= 4a^2 + 20a + 25
$$

$$
\boxed{4a^2 + 20a + 25}
$$

### Ejemplo 3

Desarrolla: $(3x + 2y)^2$

Identificamos: $a = 3x$, $b = 2y$

$$
(3x + 2y)^2 = (3x)^2 + 2(3x)(2y) + (2y)^2
$$

$$
= 9x^2 + 12xy + 4y^2
$$

$$
\boxed{9x^2 + 12xy + 4y^2}
$$

### Ejemplo 4

Desarrolla: $\left(x + \frac{1}{2}\right)^2$

$$
\left(x + \frac{1}{2}\right)^2 = x^2 + 2(x)\left(\frac{1}{2}\right) + \left(\frac{1}{2}\right)^2
$$

$$
= x^2 + x + \frac{1}{4}
$$

$$
\boxed{x^2 + x + \frac{1}{4}}
$$

---

## 📖 Cuadrado de una diferencia

$$
(a - b)^2 = a^2 - 2ab + b^2
$$

**En palabras:** El cuadrado de una diferencia es igual al cuadrado del primer término, menos el doble del producto de ambos términos, más el cuadrado del segundo término.

### Demostración

$$
(a - b)^2 = (a - b)(a - b)
$$

$$
= a \cdot a + a \cdot (-b) + (-b) \cdot a + (-b) \cdot (-b)
$$

$$
= a^2 - ab - ab + b^2
$$

$$
= a^2 - 2ab + b^2
$$

### Representación geométrica de $(a-b)^2$

<div id="jsxgraph-binomio-resta" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 380px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-binomio-resta')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-binomio-resta', {
      boundingbox: [-1, 7.5, 7.5, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var a = 5, b = 2;
    // Cuadrado grande a² (todo el cuadrado original)
    board.create('polygon', [[0, 0], [a, 0], [a, a], [0, a]], {fillColor: '#dbeafe', fillOpacity: 0.5, strokeColor: '#3b82f6', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    // Cuadrado (a-b)² resultado
    board.create('polygon', [[0, 0], [a-b, 0], [a-b, a-b], [0, a-b]], {fillColor: '#3b82f6', fillOpacity: 0.8, strokeColor: '#1d4ed8', strokeWidth: 3, fixed: true, vertices: {visible: false}});
    board.create('text', [(a-b)/2, (a-b)/2, '(a-b)²'], {fontSize: 16, strokeColor: '#1e40af', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Área que se resta (L invertida)
    // Rectángulo superior
    board.create('polygon', [[0, a-b], [a, a-b], [a, a], [0, a]], {fillColor: '#ef4444', fillOpacity: 0.4, strokeColor: '#dc2626', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a/2, a - b/2, 'ab'], {fontSize: 14, strokeColor: '#991b1b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Rectángulo derecho (sin la esquina)
    board.create('polygon', [[a-b, 0], [a, 0], [a, a-b], [a-b, a-b]], {fillColor: '#ef4444', fillOpacity: 0.4, strokeColor: '#dc2626', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a - b/2, (a-b)/2, 'ab'], {fontSize: 14, strokeColor: '#991b1b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Esquina b² (se resta dos veces, hay que sumar una)
    board.create('polygon', [[a-b, a-b], [a, a-b], [a, a], [a-b, a]], {fillColor: '#22c55e', fillOpacity: 0.7, strokeColor: '#166534', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a - b/2, a - b/2, '+b²'], {fontSize: 13, strokeColor: '#166534', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Dimensiones
    board.create('segment', [[0, -0.4], [a, -0.4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [a/2, -0.8, 'a'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[-0.4, 0], [-0.4, a]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [-0.8, a/2, 'a'], {fontSize: 14, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Fórmula
    board.create('text', [3.5, 7, '(a - b)² = a² - 2ab + b²'], {fontSize: 15, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Interpretación:** Empezamos con $a^2$, restamos dos áreas $ab$ (rojo), pero como la esquina $b^2$ se restó dos veces, la sumamos una vez (verde).

### Ejemplo 5

Desarrolla: $(x - 4)^2$

$$
(x - 4)^2 = x^2 - 2(x)(4) + 4^2
$$

$$
= x^2 - 8x + 16
$$

$$
\boxed{x^2 - 8x + 16}
$$

### Ejemplo 6

Desarrolla: $(3m - 2)^2$

$$
(3m - 2)^2 = (3m)^2 - 2(3m)(2) + 2^2
$$

$$
= 9m^2 - 12m + 4
$$

$$
\boxed{9m^2 - 12m + 4}
$$

### Ejemplo 7

Desarrolla: $(5a - 3b)^2$

$$
(5a - 3b)^2 = (5a)^2 - 2(5a)(3b) + (3b)^2
$$

$$
= 25a^2 - 30ab + 9b^2
$$

$$
\boxed{25a^2 - 30ab + 9b^2}
$$

### Ejemplo 8

Desarrolla: $\left(2x - \frac{1}{3}\right)^2$

$$
\left(2x - \frac{1}{3}\right)^2 = (2x)^2 - 2(2x)\left(\frac{1}{3}\right) + \left(\frac{1}{3}\right)^2
$$

$$
= 4x^2 - \frac{4x}{3} + \frac{1}{9}
$$

$$
\boxed{4x^2 - \frac{4x}{3} + \frac{1}{9}}
$$

---

## 📖 Error común: NO cometas este error

> ⚠️ **Error frecuente:**
> 
> $(a + b)^2 \neq a^2 + b^2$

El cuadrado de un binomio **NO** es igual a la suma de los cuadrados.

### Ejemplo incorrecto vs correcto

**Incorrecto:** $(x + 3)^2 = x^2 + 9$ ❌

**Correcto:** $(x + 3)^2 = x^2 + 6x + 9$ ✓

### Verificación numérica

Si $x = 2$:

- $(2 + 3)^2 = 5^2 = 25$
- $2^2 + 9 = 4 + 9 = 13$ ❌
- $2^2 + 6(2) + 9 = 4 + 12 + 9 = 25$ ✓

---

## 📖 Representación geométrica

El cuadrado de un binomio tiene una interpretación geométrica muy clara:

$(a + b)^2$ representa el **área de un cuadrado** de lado $(a + b)$.

<div id="jsxgraph-binomio" class="jsxgraph-container" style="width: 100%; max-width: 450px; height: 400px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-binomio')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-binomio', {
      boundingbox: [-1.5, 8.5, 8, -1.8], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var a = 4, b = 2.5; // valores para visualización
    // Cuadrado a² (esquina inferior izquierda)
    board.create('polygon', [[0, 0], [a, 0], [a, a], [0, a]], {fillColor: '#3b82f6', fillOpacity: 0.7, strokeColor: '#1d4ed8', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a/2, a/2, 'a²'], {fontSize: 20, strokeColor: '#1e40af', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cuadrado b² (esquina superior derecha)
    board.create('polygon', [[a, a], [a+b, a], [a+b, a+b], [a, a+b]], {fillColor: '#22c55e', fillOpacity: 0.7, strokeColor: '#166534', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a+b/2, a+b/2, 'b²'], {fontSize: 18, strokeColor: '#166534', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Rectángulo ab (derecha abajo)
    board.create('polygon', [[a, 0], [a+b, 0], [a+b, a], [a, a]], {fillColor: '#f59e0b', fillOpacity: 0.7, strokeColor: '#d97706', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a+b/2, a/2, 'ab'], {fontSize: 18, strokeColor: '#92400e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Rectángulo ab (arriba izquierda)
    board.create('polygon', [[0, a], [a, a], [a, a+b], [0, a+b]], {fillColor: '#f59e0b', fillOpacity: 0.7, strokeColor: '#d97706', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    board.create('text', [a/2, a+b/2, 'ab'], {fontSize: 18, strokeColor: '#92400e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Etiquetas de dimensiones
    // Base: a
    board.create('segment', [[0, -0.6], [a, -0.6]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('text', [a/2, -1.2, 'a'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Base: b
    board.create('segment', [[a, -0.6], [a+b, -0.6]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('text', [a+b/2, -1.2, 'b'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Lado izquierdo: a
    board.create('segment', [[-0.6, 0], [-0.6, a]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('text', [-1.1, a/2, 'a'], {fontSize: 18, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Lado izquierdo: b
    board.create('segment', [[-0.6, a], [-0.6, a+b]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('text', [-1.1, a+b/2, 'b'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Fórmula
    board.create('text', [3.25, 7.8, '(a + b)² = a² + 2ab + b²'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Interpretación visual:** El cuadrado grande de lado $(a+b)$ se divide en **4 regiones**:
> - 🔵 Un cuadrado azul de área $a^2$
> - 🟢 Un cuadrado verde de área $b^2$  
> - 🟠 Dos rectángulos naranjas de área $ab$ cada uno

**Total:** $a^2 + ab + ab + b^2 = a^2 + 2ab + b^2$

---

## 📖 Resumen de fórmulas

| Producto notable | Resultado |
|:----------------:|:----------|
| $(a + b)^2$ | $a^2 + 2ab + b^2$ |
| $(a - b)^2$ | $a^2 - 2ab + b^2$ |

---

## 📝 Ejercicios de práctica

### Cuadrado de una suma

**Ejercicio 1:** $(x + 5)^2$

**Ejercicio 2:** $(4m + 1)^2$

**Ejercicio 3:** $(2x + 3y)^2$

**Ejercicio 4:** $\left(a + \frac{2}{3}\right)^2$

---

### Cuadrado de una diferencia

**Ejercicio 5:** $(x - 7)^2$

**Ejercicio 6:** $(5n - 2)^2$

**Ejercicio 7:** $(4a - 5b)^2$

**Ejercicio 8:** $\left(3x - \frac{1}{2}\right)^2$

---

### Ejercicios mixtos

**Ejercicio 9:** $(a + 1)^2 - (a - 1)^2$

**Ejercicio 10:** Desarrolla y simplifica: $(2x + 3)^2 - 4x^2$

---

## ✅ Soluciones

### Cuadrado de una suma

| Ejercicio | Solución |
|:---------:|:---------|
| 1 | $x^2 + 10x + 25$ |
| 2 | $16m^2 + 8m + 1$ |
| 3 | $4x^2 + 12xy + 9y^2$ |
| 4 | $a^2 + \frac{4a}{3} + \frac{4}{9}$ |

### Cuadrado de una diferencia

| Ejercicio | Solución |
|:---------:|:---------|
| 5 | $x^2 - 14x + 49$ |
| 6 | $25n^2 - 20n + 4$ |
| 7 | $16a^2 - 40ab + 25b^2$ |
| 8 | $9x^2 - 3x + \frac{1}{4}$ |

### Ejercicios mixtos

**Ejercicio 9:**

$$
(a + 1)^2 - (a - 1)^2 = (a^2 + 2a + 1) - (a^2 - 2a + 1)
$$

$$
= a^2 + 2a + 1 - a^2 + 2a - 1 = 4a
$$

**Ejercicio 10:**

$$
(2x + 3)^2 - 4x^2 = 4x^2 + 12x + 9 - 4x^2 = 12x + 9
$$

---

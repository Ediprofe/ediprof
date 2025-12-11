# ➖ Diferencia de Cuadrados

En esta lección aprenderemos a factorizar expresiones que son diferencia de dos cuadrados perfectos.

---

## 📖 Fórmula de la diferencia de cuadrados

La diferencia de cuadrados se factoriza como el producto de dos binomios conjugados:

$$
a^2 - b^2 = (a + b)(a - b)
$$

### Demostración algebraica

Podemos verificar esta fórmula multiplicando los binomios conjugados:

$$
(a + b)(a - b)
$$

$$
= a \cdot a + a \cdot (-b) + b \cdot a + b \cdot (-b)
$$

$$
= a^2 - ab + ab - b^2
$$

$$
= a^2 - b^2 \quad ✓
$$

### Ejemplo: Si $a = 5$ y $b = 2$

$$
(5 + 2)(5 - 2) = 7 \times 3 = 21
$$

$$
5^2 - 2^2 = 25 - 4 = 21 \quad ✓
$$

---

### Interpretación geométrica (con $a = 5$, $b = 2$)

<div id="jsxgraph-diff-sq" class="jsxgraph-container" style="width: 100%; max-width: 650px; height: 380px; margin: 1.5rem auto;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-diff-sq')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-diff-sq', {
      boundingbox: [-2.5, 9.5, 19, -3.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var a = 5, b = 2;
    // Título fórmula
    board.create('text', [8, 8.8, '5² − 2² = (5+2)(5−2)'], {fontSize: 17, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    
    // === LADO IZQUIERDO: Cuadrado grande con cuadrado restado ===
    // Cuadrado grande a² (azul)
    board.create('polygon', [[0, 0], [a, 0], [a, a], [0, a]], {fillColor: '#3b82f6', fillOpacity: 0.6, strokeColor: '#1d4ed8', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    // Cuadrado pequeño b² (rojo)
    board.create('polygon', [[a-b, a-b], [a, a-b], [a, a], [a-b, a]], {fillColor: '#ef4444', fillOpacity: 0.85, strokeColor: '#b91c1c', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    // Etiqueta b² = 4
    board.create('text', [a - b/2, a - b/2, 'b²=4'], {fontSize: 13, strokeColor: '#fff', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Etiqueta a² = 25 dentro
    board.create('text', [1.3, 1.5, 'a²=25'], {fontSize: 14, strokeColor: '#1e40af', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    
    // Dimensión inferior: a = 5
    board.create('segment', [[0, -0.7], [a, -0.7]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('text', [a/2, -1.6, 'a = 5'], {fontSize: 15, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Dimensión lateral: a = 5
    board.create('segment', [[-0.7, 0], [-0.7, a]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('text', [-1.8, a/2, 'a = 5'], {fontSize: 15, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Dimensión b = 2 (lado del cuadrado rojo)
    board.create('segment', [[a+0.3, a-b], [a+0.3, a]], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    board.create('text', [a + 1.2, a - b/2, 'b = 2'], {fontSize: 13, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    
    // Resultado lado izquierdo: a² - b² = 21
    board.create('text', [2.5, 7.5, 'a² − b² = 21'], {fontSize: 15, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.5, 6.5, '5² − 2² = 21'], {fontSize: 14, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    
    // === SIGNO IGUAL ===
    board.create('text', [8, 3, '='], {fontSize: 36, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    
    // === LADO DERECHO: Rectángulo (a+b)(a-b) ===
    var xOff = 10;
    var rectW = a + b; // 7
    var rectH = a - b; // 3
    board.create('polygon', [[xOff, 0.5], [xOff + rectW, 0.5], [xOff + rectW, rectH + 0.5], [xOff, rectH + 0.5]], {fillColor: '#22c55e', fillOpacity: 0.7, strokeColor: '#166534', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    // Valor dentro 7 × 3
    board.create('text', [xOff + rectW/2, 2, '7 × 3'], {fontSize: 18, strokeColor: '#166534', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    
    // Dimensión inferior: (5+2) = 7
    board.create('segment', [[xOff, -0.3], [xOff + rectW, -0.3]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('text', [xOff + rectW/2, -1.2, '(5+2) = 7'], {fontSize: 14, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [xOff + rectW/2, -2.3, 'a + b'], {fontSize: 12, strokeColor: '#64748b', fixed: true, anchorX: 'middle', cssStyle: 'font-style: italic;'});
    
    // Dimensión lateral: (5-2) = 3
    board.create('segment', [[xOff - 0.5, 0.5], [xOff - 0.5, rectH + 0.5]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('text', [xOff - 1.5, 2, '(5−2)'], {fontSize: 13, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [xOff - 1.5, 1.1, '= 3'], {fontSize: 13, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [xOff - 1.5, 0.2, 'a − b'], {fontSize: 11, strokeColor: '#64748b', fixed: true, anchorX: 'middle', cssStyle: 'font-style: italic;'});
    
    // Resultado lado derecho: (a+b)(a-b) = 21
    board.create('text', [xOff + rectW/2, 7.5, '(a+b)(a−b) = 21'], {fontSize: 15, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [xOff + rectW/2, 6.5, '(5+2)(5−2) = 21'], {fontSize: 14, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Interpretación:** El área del cuadrado azul ($25$) menos el área del cuadrado rojo ($4$) es igual al área del rectángulo verde ($7 \times 3 = 21$). ¡Ambas áreas son **21**!

**En palabras:** La diferencia de dos cuadrados es igual al producto de la suma de sus raíces por la diferencia de sus raíces.

---

## 📖 ¿Cómo identificar una diferencia de cuadrados?

Una expresión es diferencia de cuadrados si:

1. Tiene **exactamente dos términos**
2. Los términos están **restados** (no sumados)
3. **Ambos términos son cuadrados perfectos**

### Cuadrados perfectos comunes

| Número | Cuadrado perfecto |
|:------:|:-----------------:|
| $1$ | $1^2$ |
| $4$ | $2^2$ |
| $9$ | $3^2$ |
| $16$ | $4^2$ |
| $25$ | $5^2$ |
| $36$ | $6^2$ |
| $49$ | $7^2$ |
| $64$ | $8^2$ |
| $81$ | $9^2$ |
| $100$ | $10^2$ |

---

## 📖 Ejemplos básicos

### Ejemplo 1

Factoriza: $x^2 - 9$

**Identificamos los cuadrados:**
- $x^2 = (x)^2$ ✓
- $9 = (3)^2$ ✓

$$
x^2 - 9 = (x + 3)(x - 3)
$$

$$
\boxed{(x + 3)(x - 3)}
$$

### Ejemplo 2

Factoriza: $y^2 - 25$

**Identificamos:**
- $y^2 = (y)^2$
- $25 = (5)^2$

$$
y^2 - 25 = (y + 5)(y - 5)
$$

$$
\boxed{(y + 5)(y - 5)}
$$

### Ejemplo 3

Factoriza: $a^2 - 1$

$$
a^2 - 1 = (a + 1)(a - 1)
$$

$$
\boxed{(a + 1)(a - 1)}
$$

### Ejemplo 4

Factoriza: $m^2 - 100$

$$
m^2 - 100 = (m + 10)(m - 10)
$$

$$
\boxed{(m + 10)(m - 10)}
$$

---

## 📖 Ejemplos con coeficientes

### Ejemplo 5

Factoriza: $4x^2 - 9$

**Identificamos:**
- $4x^2 = (2x)^2$ ✓
- $9 = (3)^2$ ✓

$$
4x^2 - 9 = (2x + 3)(2x - 3)
$$

$$
\boxed{(2x + 3)(2x - 3)}
$$

### Ejemplo 6

Factoriza: $25a^2 - 16$

**Identificamos:**
- $25a^2 = (5a)^2$
- $16 = (4)^2$

$$
25a^2 - 16 = (5a + 4)(5a - 4)
$$

$$
\boxed{(5a + 4)(5a - 4)}
$$

### Ejemplo 7

Factoriza: $49m^2 - 36n^2$

**Identificamos:**
- $49m^2 = (7m)^2$
- $36n^2 = (6n)^2$

$$
49m^2 - 36n^2 = (7m + 6n)(7m - 6n)
$$

$$
\boxed{(7m + 6n)(7m - 6n)}
$$

### Ejemplo 8

Factoriza: $81x^2 - 64y^2$

$$
81x^2 - 64y^2 = (9x + 8y)(9x - 8y)
$$

$$
\boxed{(9x + 8y)(9x - 8y)}
$$

---

## 📖 Ejemplos con exponentes mayores

### Ejemplo 9

Factoriza: $x^4 - 16$

**Identificamos:**
- $x^4 = (x^2)^2$ ✓
- $16 = (4)^2$ ✓

$$
x^4 - 16 = (x^2 + 4)(x^2 - 4)
$$

Pero $x^2 - 4$ también es diferencia de cuadrados:

$$
x^2 - 4 = (x + 2)(x - 2)
$$

**Resultado final:**

$$
x^4 - 16 = (x^2 + 4)(x + 2)(x - 2)
$$

$$
\boxed{(x^2 + 4)(x + 2)(x - 2)}
$$

### Ejemplo 10

Factoriza: $a^6 - b^6$

**Identificamos:**
- $a^6 = (a^3)^2$
- $b^6 = (b^3)^2$

$$
a^6 - b^6 = (a^3 + b^3)(a^3 - b^3)
$$

Cada factor se puede factorizar más (suma y diferencia de cubos):

$$
= (a + b)(a^2 - ab + b^2)(a - b)(a^2 + ab + b^2)
$$

$$
\boxed{(a + b)(a - b)(a^2 - ab + b^2)(a^2 + ab + b^2)}
$$

### Ejemplo 11

Factoriza: $x^8 - 1$

$$
x^8 - 1 = (x^4 + 1)(x^4 - 1)
$$

Continuamos con $x^4 - 1$:

$$
x^4 - 1 = (x^2 + 1)(x^2 - 1)
$$

Y con $x^2 - 1$:

$$
x^2 - 1 = (x + 1)(x - 1)
$$

**Resultado final:**

$$
x^8 - 1 = (x^4 + 1)(x^2 + 1)(x + 1)(x - 1)
$$

$$
\boxed{(x^4 + 1)(x^2 + 1)(x + 1)(x - 1)}
$$

---

## 📖 Ejemplos con fracciones

### Ejemplo 12

Factoriza: $\frac{x^2}{4} - 9$

**Identificamos:**
- $\frac{x^2}{4} = \left(\frac{x}{2}\right)^2$
- $9 = (3)^2$

$$
\frac{x^2}{4} - 9 = \left(\frac{x}{2} + 3\right)\left(\frac{x}{2} - 3\right)
$$

$$
\boxed{\left(\frac{x}{2} + 3\right)\left(\frac{x}{2} - 3\right)}
$$

### Ejemplo 13

Factoriza: $\frac{a^2}{9} - \frac{b^2}{16}$

$$
= \left(\frac{a}{3} + \frac{b}{4}\right)\left(\frac{a}{3} - \frac{b}{4}\right)
$$

$$
\boxed{\left(\frac{a}{3} + \frac{b}{4}\right)\left(\frac{a}{3} - \frac{b}{4}\right)}
$$

---

## 📖 Diferencia de cuadrados con factor común

Siempre extrae el factor común primero.

### Ejemplo 14

Factoriza: $3x^2 - 12$

**Paso 1:** Factor común $3$:

$$
3x^2 - 12 = 3(x^2 - 4)
$$

**Paso 2:** Diferencia de cuadrados:

$$
= 3(x + 2)(x - 2)
$$

$$
\boxed{3(x + 2)(x - 2)}
$$

### Ejemplo 15

Factoriza: $2a^3 - 8a$

**Paso 1:** Factor común $2a$:

$$
2a^3 - 8a = 2a(a^2 - 4)
$$

**Paso 2:** Diferencia de cuadrados:

$$
= 2a(a + 2)(a - 2)
$$

$$
\boxed{2a(a + 2)(a - 2)}
$$

### Ejemplo 16

Factoriza: $5x^4 - 45x^2$

**Paso 1:** Factor común $5x^2$:

$$
5x^4 - 45x^2 = 5x^2(x^2 - 9)
$$

**Paso 2:** Diferencia de cuadrados:

$$
= 5x^2(x + 3)(x - 3)
$$

$$
\boxed{5x^2(x + 3)(x - 3)}
$$

---

## 📖 ¿Qué NO es diferencia de cuadrados?

### Suma de cuadrados

La **suma de cuadrados** $a^2 + b^2$ **NO se puede factorizar** con números reales.

$$
x^2 + 9 \neq (x + 3)(x + 3) \quad \text{¡Error!}
$$

$x^2 + 9$ no es factorizable (es **primo** en los reales).

### Ejemplo incorrecto

$(x + 3)(x + 3) = x^2 + 6x + 9 \neq x^2 + 9$

---

## 📝 Ejercicios de práctica

### Diferencia de cuadrados básica

**Ejercicio 1:** $x^2 - 49$

**Ejercicio 2:** $a^2 - 81$

**Ejercicio 3:** $m^2 - 144$

---

### Con coeficientes

**Ejercicio 4:** $9x^2 - 4$

**Ejercicio 5:** $16a^2 - 25b^2$

**Ejercicio 6:** $100m^2 - 49n^2$

---

### Con exponentes mayores

**Ejercicio 7:** $x^4 - 81$

**Ejercicio 8:** $a^4 - 1$

---

### Con factor común

**Ejercicio 9:** $5x^2 - 20$

**Ejercicio 10:** $3a^3 - 27a$

---

## ✅ Soluciones

### Diferencia de cuadrados básica

| Ejercicio | Solución |
|:---------:|:---------|
| 1 | $(x + 7)(x - 7)$ |
| 2 | $(a + 9)(a - 9)$ |
| 3 | $(m + 12)(m - 12)$ |

### Con coeficientes

| Ejercicio | Solución |
|:---------:|:---------|
| 4 | $(3x + 2)(3x - 2)$ |
| 5 | $(4a + 5b)(4a - 5b)$ |
| 6 | $(10m + 7n)(10m - 7n)$ |

### Con exponentes mayores

**Ejercicio 7:**

$$
x^4 - 81 = (x^2 + 9)(x^2 - 9) = (x^2 + 9)(x + 3)(x - 3)
$$

**Ejercicio 8:**

$$
a^4 - 1 = (a^2 + 1)(a^2 - 1) = (a^2 + 1)(a + 1)(a - 1)
$$

### Con factor común

**Ejercicio 9:**

$$
5x^2 - 20 = 5(x^2 - 4) = 5(x + 2)(x - 2)
$$

**Ejercicio 10:**

$$
3a^3 - 27a = 3a(a^2 - 9) = 3a(a + 3)(a - 3)
$$

---

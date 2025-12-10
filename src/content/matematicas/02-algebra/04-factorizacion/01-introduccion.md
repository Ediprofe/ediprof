# 🔧 Introducción a la Factorización

En esta lección aprenderemos qué es la factorización, su importancia en álgebra y cómo se relaciona con la factorización de números naturales que ya conocemos.

---

## 📋 Resumen de Casos de Factorización

A continuación se presenta un resumen de todos los casos de factorización que estudiaremos en este tema:

| Caso | Nombre | Forma | Factorización |
|:----:|:-------|:------|:--------------|
| 1 | Factor común | $ab + ac$ | $a(b + c)$ |
| 2 | Agrupación de términos | $ax + ay + bx + by$ | $(a+b)(x+y)$ |
| 3 | Diferencia de cuadrados | $a^2 - b^2$ | $(a+b)(a-b)$ |
| 4 | Trinomio cuadrado perfecto | $a^2 \pm 2ab + b^2$ | $(a \pm b)^2$ |
| 5 | Trinomio $x^2 + bx + c$ | $x^2 + bx + c$ | $(x + m)(x + n)$ donde $m + n = b$, $mn = c$ |
| 6 | Trinomio $ax^2 + bx + c$ | $ax^2 + bx + c$ | Método de descomposición |
| 7 | Suma de cubos | $a^3 + b^3$ | $(a+b)(a^2 - ab + b^2)$ |
| 8 | Diferencia de cubos | $a^3 - b^3$ | $(a-b)(a^2 + ab + b^2)$ |
| 9 | Potencias impares | $a^n \pm b^n$ | Ver lección específica |
| 10 | Completar el cuadrado | $x^2 + bx + c$ | $(x + \frac{b}{2})^2 - k$ |

> **Nota:** Cada caso se estudia en detalle en las siguientes lecciones de este tema.

---

## 📖 ¿Qué es factorizar?

**Factorizar** significa expresar una cantidad como el producto de sus factores. Es el proceso inverso de multiplicar.

### Analogía con números naturales

Recordemos la factorización de números:

| Número | Factorización |
|:------:|:-------------|
| $12$ | $12 = 2 \times 2 \times 3 = 2^2 \times 3$ |
| $30$ | $30 = 2 \times 3 \times 5$ |
| $100$ | $100 = 2^2 \times 5^2$ |

De la misma forma, en álgebra factorizamos **expresiones algebraicas**.

---

## 📖 Factorización algebraica

La **factorización algebraica** consiste en expresar un polinomio como el producto de otros polinomios más simples (sus factores).

### Ejemplo conceptual

| Expresión | Forma factorizada |
|:---------:|:-----------------|
| $x^2 - 4$ | $(x + 2)(x - 2)$ |
| $x^2 + 5x + 6$ | $(x + 2)(x + 3)$ |
| $6x^2 + 9x$ | $3x(2x + 3)$ |

### Verificación

Podemos verificar una factorización multiplicando los factores:

$$
(x + 2)(x - 2) = x^2 - 2x + 2x - 4 = x^2 - 4 \quad ✓
$$

---

## 📖 Relación con productos notables

La factorización es el **proceso inverso** de los productos notables:

| Producto Notable | Factorización |
|:-----------------|:--------------|
| $(a + b)^2 = a^2 + 2ab + b^2$ | $a^2 + 2ab + b^2 = (a + b)^2$ |
| $(a - b)^2 = a^2 - 2ab + b^2$ | $a^2 - 2ab + b^2 = (a - b)^2$ |
| $(a + b)(a - b) = a^2 - b^2$ | $a^2 - b^2 = (a + b)(a - b)$ |
| $(x + a)(x + b) = x^2 + (a+b)x + ab$ | $x^2 + (a+b)x + ab = (x + a)(x + b)$ |

---

## 📖 ¿Por qué es importante factorizar?

La factorización es fundamental para:

### 1. Simplificar fracciones algebraicas

$$
\frac{x^2 - 9}{x - 3} = \frac{(x+3)(x-3)}{x-3} = x + 3
$$

### 2. Resolver ecuaciones

$$
x^2 - 5x + 6 = 0
$$

$$
(x - 2)(x - 3) = 0
$$

$$
x = 2 \quad \text{o} \quad x = 3
$$

### 3. Encontrar raíces de polinomios

Los factores de un polinomio nos dicen dónde la función cruza el eje $x$.

### 4. Operaciones con fracciones

Para sumar fracciones algebraicas necesitamos factorizar para encontrar el mínimo común denominador.

---
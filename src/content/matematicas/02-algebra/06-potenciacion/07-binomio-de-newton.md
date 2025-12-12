# 📐 Binomio de Newton

En esta lección aprenderemos a expandir potencias de binomios utilizando el Binomio de Newton, una fórmula que nos permite calcular cualquier potencia de la forma $(a + b)^n$.

---

## 📖 ¿Qué es el Binomio de Newton?

El **Binomio de Newton** es una fórmula que permite expandir cualquier potencia de un binomio:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

Donde $\binom{n}{k}$ son los coeficientes binomiales que estudiamos en la lección anterior.

---

## 📖 Forma expandida

La expansión completa es:

$$
(a+b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n}b^n
$$

### Características de la expansión

- Hay $n + 1$ términos
- Los exponentes de $a$ van de $n$ a $0$
- Los exponentes de $b$ van de $0$ a $n$
- La suma de los exponentes en cada término es $n$

---

## 📖 Casos conocidos

### Cuadrado de un binomio

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

### Cubo de un binomio

$$
(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
$$

---

## 📖 Expansión para diferentes potencias

### Ejemplo 1

Expandir $(a + b)^4$.

**Los coeficientes binomiales son:**

$$
\binom{4}{0} = 1, \quad \binom{4}{1} = 4, \quad \binom{4}{2} = 6, \quad \binom{4}{3} = 4, \quad \binom{4}{4} = 1
$$

**Expansión:**

$$
(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4
$$

$$
\boxed{(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4}
$$

---

### Ejemplo 2

Expandir $(a + b)^5$.

**Los coeficientes:** $1, 5, 10, 10, 5, 1$

$$
(a+b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5
$$

$$
\boxed{(a+b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5}
$$

---

### Ejemplo 3

Expandir $(x + 2)^4$.

**Usamos** $a = x$, $b = 2$:

$$
(x+2)^4 = x^4 + 4x^3(2) + 6x^2(2)^2 + 4x(2)^3 + (2)^4
$$

$$
= x^4 + 8x^3 + 24x^2 + 32x + 16
$$

$$
\boxed{(x+2)^4 = x^4 + 8x^3 + 24x^2 + 32x + 16}
$$

---

### Ejemplo 4

Expandir $(2x + 1)^3$.

**Usamos** $a = 2x$, $b = 1$:

$$
(2x+1)^3 = (2x)^3 + 3(2x)^2(1) + 3(2x)(1)^2 + (1)^3
$$

$$
= 8x^3 + 12x^2 + 6x + 1
$$

$$
\boxed{(2x+1)^3 = 8x^3 + 12x^2 + 6x + 1}
$$

---

### Ejemplo 5

Expandir $(3x + 2y)^3$.

$$
(3x+2y)^3 = (3x)^3 + 3(3x)^2(2y) + 3(3x)(2y)^2 + (2y)^3
$$

$$
= 27x^3 + 3(9x^2)(2y) + 3(3x)(4y^2) + 8y^3
$$

$$
= 27x^3 + 54x^2y + 36xy^2 + 8y^3
$$

$$
\boxed{(3x+2y)^3 = 27x^3 + 54x^2y + 36xy^2 + 8y^3}
$$

---

## 📖 Binomio con resta

Para $(a - b)^n$, los signos se alternan:

$$
(a - b)^n = a^n - \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 - \binom{n}{3}a^{n-3}b^3 + \cdots
$$

Los términos con exponente par de $b$ son positivos, los impares son negativos.

---

### Ejemplo 6

Expandir $(x - y)^4$.

$$
(x-y)^4 = x^4 - 4x^3y + 6x^2y^2 - 4xy^3 + y^4
$$

$$
\boxed{(x-y)^4 = x^4 - 4x^3y + 6x^2y^2 - 4xy^3 + y^4}
$$

---

### Ejemplo 7

Expandir $(a - 2)^5$.

Los coeficientes son: $1, 5, 10, 10, 5, 1$

$$
(a-2)^5 = a^5 - 5a^4(2) + 10a^3(4) - 10a^2(8) + 5a(16) - 32
$$

$$
= a^5 - 10a^4 + 40a^3 - 80a^2 + 80a - 32
$$

$$
\boxed{(a-2)^5 = a^5 - 10a^4 + 40a^3 - 80a^2 + 80a - 32}
$$

---

### Ejemplo 8

Expandir $(2x - 3y)^3$.

$$
(2x-3y)^3 = (2x)^3 - 3(2x)^2(3y) + 3(2x)(3y)^2 - (3y)^3
$$

$$
= 8x^3 - 3(4x^2)(3y) + 3(2x)(9y^2) - 27y^3
$$

$$
= 8x^3 - 36x^2y + 54xy^2 - 27y^3
$$

$$
\boxed{(2x-3y)^3 = 8x^3 - 36x^2y + 54xy^2 - 27y^3}
$$

---

## 📖 Término general

El término en la posición $k+1$ de la expansión de $(a+b)^n$ es:

$$
T_{k+1} = \binom{n}{k} a^{n-k} b^k
$$

### Ejemplo 9

Encontrar el quinto término de $(x + 2)^7$.

El quinto término corresponde a $k = 4$:

$$
T_5 = \binom{7}{4} x^{7-4} (2)^4 = 35 \cdot x^3 \cdot 16 = 560x^3
$$

$$
\boxed{\text{El quinto término es } 560x^3}
$$

---

### Ejemplo 10

Encontrar el término medio de $(a + b)^6$.

Para $n = 6$, hay $7$ términos. El término medio es el $4^{\circ}$ (cuando $k = 3$):

$$
T_4 = \binom{6}{3} a^3 b^3 = 20a^3b^3
$$

$$
\boxed{\text{El término medio es } 20a^3b^3}
$$

---

## 📋 Resumen

| Fórmula | Expresión |
|:--------|:---------:|
| Binomio de Newton | $(a+b)^n = \sum \binom{n}{k} a^{n-k} b^k$ |
| Término general | $T_{k+1} = \binom{n}{k} a^{n-k} b^k$ |
| Número de términos | $n + 1$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Expande $(x + y)^5$.

<details>
<summary>Ver solución</summary>

$$
x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5
$$

</details>

---

**Ejercicio 2:** Expande $(a + 3)^4$.

<details>
<summary>Ver solución</summary>

$$
a^4 + 12a^3 + 54a^2 + 108a + 81
$$

</details>

---

**Ejercicio 3:** Expande $(x - 1)^5$.

<details>
<summary>Ver solución</summary>

$$
x^5 - 5x^4 + 10x^3 - 10x^2 + 5x - 1
$$

</details>

---

**Ejercicio 4:** Expande $(2a - b)^4$.

<details>
<summary>Ver solución</summary>

$$
16a^4 - 32a^3b + 24a^2b^2 - 8ab^3 + b^4
$$

</details>

---

**Ejercicio 5:** Encuentra el cuarto término de $(x + 3)^6$.

<details>
<summary>Ver solución</summary>

$k = 3$:

$$
T_4 = \binom{6}{3} x^3 (3)^3 = 20 \cdot x^3 \cdot 27 = 540x^3
$$

</details>

---

**Ejercicio 6:** Encuentra el término que contiene $x^3$ en $(x + 2)^5$.

<details>
<summary>Ver solución</summary>

Para $x^3$, necesitamos $n - k = 3$, así que $k = 2$:

$$
T_3 = \binom{5}{2} x^3 (2)^2 = 10 \cdot x^3 \cdot 4 = 40x^3
$$

</details>

---

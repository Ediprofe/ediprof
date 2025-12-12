# 🔺 Triángulo de Pascal

En esta lección aprenderemos sobre el Triángulo de Pascal, una herramienta visual que nos permite obtener rápidamente los coeficientes binomiales para la expansión del Binomio de Newton.

---

## 📖 ¿Qué es el Triángulo de Pascal?

El **Triángulo de Pascal** es un arreglo triangular de números donde cada número es la suma de los dos números que están directamente encima de él.

```
              1                 (n = 0)
            1   1               (n = 1)
          1   2   1             (n = 2)
        1   3   3   1           (n = 3)
      1   4   6   4   1         (n = 4)
    1   5  10  10   5   1       (n = 5)
  1   6  15  20  15   6   1     (n = 6)
1   7  21  35  35  21   7   1   (n = 7)
```

---

## 📖 Construcción del triángulo

### Reglas de construcción

1. El primer y último número de cada fila es siempre $1$
2. Cada número interior es la suma de los dos números de arriba

### Ejemplo visual

```
        1
       ↙ ↘
      1   1
     ↙ ↘ ↙ ↘
    1   2   1      (2 = 1 + 1)
   ↙ ↘ ↙ ↘ ↙ ↘
  1   3   3   1    (3 = 1 + 2, 3 = 2 + 1)
```

---

## 📖 Relación con los coeficientes binomiales

Cada fila $n$ del triángulo contiene los coeficientes binomiales $\binom{n}{k}$ para $k = 0, 1, 2, \ldots, n$.

| Fila | Coeficientes | Binomio |
|:----:|:------------:|:--------|
| 0 | $1$ | $(a+b)^0 = 1$ |
| 1 | $1, 1$ | $(a+b)^1 = a + b$ |
| 2 | $1, 2, 1$ | $(a+b)^2 = a^2 + 2ab + b^2$ |
| 3 | $1, 3, 3, 1$ | $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ |
| 4 | $1, 4, 6, 4, 1$ | $(a+b)^4 = \ldots$ |

---

## 📖 Usando el triángulo para expandir binomios

### Ejemplo 1

Expandir $(x + y)^4$ usando el Triángulo de Pascal.

**Paso 1:** La fila 4 es: $1, 4, 6, 4, 1$

**Paso 2:** Escribimos la expansión:

$$
(x+y)^4 = 1 \cdot x^4 + 4 \cdot x^3y + 6 \cdot x^2y^2 + 4 \cdot xy^3 + 1 \cdot y^4
$$

$$
\boxed{(x+y)^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4}
$$

---

### Ejemplo 2

Expandir $(a + b)^6$ usando el Triángulo de Pascal.

**Paso 1:** La fila 6 es: $1, 6, 15, 20, 15, 6, 1$

**Paso 2:** Escribimos:

$$
(a+b)^6 = a^6 + 6a^5b + 15a^4b^2 + 20a^3b^3 + 15a^2b^4 + 6ab^5 + b^6
$$

$$
\boxed{(a+b)^6 = a^6 + 6a^5b + 15a^4b^2 + 20a^3b^3 + 15a^2b^4 + 6ab^5 + b^6}
$$

---

### Ejemplo 3

Expandir $(x + 2)^5$ usando el Triángulo de Pascal.

**Paso 1:** La fila 5 es: $1, 5, 10, 10, 5, 1$

**Paso 2:** Sustituimos $a = x$, $b = 2$:

$$
(x+2)^5 = 1 \cdot x^5 + 5 \cdot x^4 \cdot 2 + 10 \cdot x^3 \cdot 4 + 10 \cdot x^2 \cdot 8 + 5 \cdot x \cdot 16 + 1 \cdot 32
$$

$$
= x^5 + 10x^4 + 40x^3 + 80x^2 + 80x + 32
$$

$$
\boxed{(x+2)^5 = x^5 + 10x^4 + 40x^3 + 80x^2 + 80x + 32}
$$

---

### Ejemplo 4

Expandir $(2a - b)^4$ usando el Triángulo de Pascal.

**Paso 1:** La fila 4 es: $1, 4, 6, 4, 1$

**Paso 2:** Como es una resta, alternamos signos:

$$
(2a-b)^4 = (2a)^4 - 4(2a)^3b + 6(2a)^2b^2 - 4(2a)b^3 + b^4
$$

$$
= 16a^4 - 4(8a^3)b + 6(4a^2)b^2 - 4(2a)b^3 + b^4
$$

$$
= 16a^4 - 32a^3b + 24a^2b^2 - 8ab^3 + b^4
$$

$$
\boxed{(2a-b)^4 = 16a^4 - 32a^3b + 24a^2b^2 - 8ab^3 + b^4}
$$

---

### Ejemplo 5

Expandir $(3x + y)^3$ usando el Triángulo de Pascal.

**Paso 1:** La fila 3 es: $1, 3, 3, 1$

**Paso 2:**

$$
(3x+y)^3 = (3x)^3 + 3(3x)^2y + 3(3x)y^2 + y^3
$$

$$
= 27x^3 + 27x^2y + 9xy^2 + y^3
$$

$$
\boxed{(3x+y)^3 = 27x^3 + 27x^2y + 9xy^2 + y^3}
$$

---

## 📖 Propiedades del Triángulo de Pascal

### Simetría

El triángulo es simétrico respecto a su eje vertical central:

$$
\binom{n}{k} = \binom{n}{n-k}
$$

### Suma de una fila

La suma de todos los números en la fila $n$ es $2^n$:

| Fila | Suma | $2^n$ |
|:----:|:----:|:-----:|
| 0 | $1$ | $2^0 = 1$ |
| 1 | $1 + 1 = 2$ | $2^1 = 2$ |
| 2 | $1 + 2 + 1 = 4$ | $2^2 = 4$ |
| 3 | $1 + 3 + 3 + 1 = 8$ | $2^3 = 8$ |
| 4 | $1 + 4 + 6 + 4 + 1 = 16$ | $2^4 = 16$ |

---

### Ejemplo 6

Verificar que la suma de la fila 5 es $2^5 = 32$.

$$
1 + 5 + 10 + 10 + 5 + 1 = 32 \quad ✓
$$

---

## 📖 Identidad de Pascal

La regla de construcción del triángulo se expresa como:

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

### Ejemplo 7

Verificar que $\binom{5}{2} = \binom{4}{1} + \binom{4}{2}$.

$$
\binom{5}{2} = 10
$$

$$
\binom{4}{1} + \binom{4}{2} = 4 + 6 = 10 \quad ✓
$$

---

## 📖 Construyendo más filas

### Ejemplo 8

Construir la fila 8 del Triángulo de Pascal.

Partimos de la fila 7: $1, 7, 21, 35, 35, 21, 7, 1$

Fila 8:
$$
1, (1+7), (7+21), (21+35), (35+35), (35+21), (21+7), (7+1), 1
$$

$$
= 1, 8, 28, 56, 70, 56, 28, 8, 1
$$

$$
\boxed{\text{Fila 8: } 1, 8, 28, 56, 70, 56, 28, 8, 1}
$$

---

## 📋 Triángulo de Pascal completo hasta la fila 10

| $n$ | Coeficientes |
|:---:|:-------------|
| 0 | 1 |
| 1 | 1, 1 |
| 2 | 1, 2, 1 |
| 3 | 1, 3, 3, 1 |
| 4 | 1, 4, 6, 4, 1 |
| 5 | 1, 5, 10, 10, 5, 1 |
| 6 | 1, 6, 15, 20, 15, 6, 1 |
| 7 | 1, 7, 21, 35, 35, 21, 7, 1 |
| 8 | 1, 8, 28, 56, 70, 56, 28, 8, 1 |
| 9 | 1, 9, 36, 84, 126, 126, 84, 36, 9, 1 |
| 10 | 1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1 |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Construye la fila 9 del Triángulo de Pascal.

<details>
<summary>Ver solución</summary>

Partiendo de la fila 8: $1, 8, 28, 56, 70, 56, 28, 8, 1$

Fila 9: $1, 9, 36, 84, 126, 126, 84, 36, 9, 1$

</details>

---

**Ejercicio 2:** Expande $(a + b)^7$ usando el Triángulo de Pascal.

<details>
<summary>Ver solución</summary>

Fila 7: $1, 7, 21, 35, 35, 21, 7, 1$

$$
a^7 + 7a^6b + 21a^5b^2 + 35a^4b^3 + 35a^3b^4 + 21a^2b^5 + 7ab^6 + b^7
$$

</details>

---

**Ejercicio 3:** Expande $(x - 1)^6$ usando el Triángulo de Pascal.

<details>
<summary>Ver solución</summary>

Fila 6: $1, 6, 15, 20, 15, 6, 1$ con signos alternados:

$$
x^6 - 6x^5 + 15x^4 - 20x^3 + 15x^2 - 6x + 1
$$

</details>

---

**Ejercicio 4:** Verifica que la suma de la fila 7 es $2^7$.

<details>
<summary>Ver solución</summary>

$$
1 + 7 + 21 + 35 + 35 + 21 + 7 + 1 = 128 = 2^7 \quad ✓
$$

</details>

---

**Ejercicio 5:** Expande $(2x + 1)^4$ usando el Triángulo de Pascal.

<details>
<summary>Ver solución</summary>

Fila 4: $1, 4, 6, 4, 1$

$$
(2x)^4 + 4(2x)^3 + 6(2x)^2 + 4(2x) + 1
$$

$$
= 16x^4 + 32x^3 + 24x^2 + 8x + 1
$$

</details>

---

**Ejercicio 6:** Usando $\binom{6}{2} = 15$ y $\binom{6}{3} = 20$, encuentra $\binom{7}{3}$.

<details>
<summary>Ver solución</summary>

Por la identidad de Pascal:

$$
\binom{7}{3} = \binom{6}{2} + \binom{6}{3} = 15 + 20 = 35
$$

</details>

---

# 🔢 Trinomio de la Forma ax² + bx + c

En esta lección aprenderemos a factorizar trinomios donde el coeficiente del término cuadrático es diferente de 1.

---

## 📖 Forma general

El trinomio de la forma:

$$
ax^2 + bx + c \quad \text{donde } a \neq 1
$$

Es más complejo de factorizar. Existen varios métodos para hacerlo.

---

## 📖 Método 1: Descomposición del término medio

Este método consiste en reescribir el término medio $bx$ como la suma de dos términos, para luego factorizar por agrupación.

### Pasos

1. Calcular $a \times c$
2. Buscar dos números $m$ y $n$ tales que:
   - $m + n = b$
   - $m \times n = a \times c$
3. Reescribir $bx$ como $mx + nx$
4. Factorizar por agrupación

### Ejemplo 1

Factoriza: $2x^2 + 7x + 3$

**Paso 1:** $a \times c = 2 \times 3 = 6$

**Paso 2:** Buscamos $m + n = 7$ y $m \times n = 6$

Los números son $1$ y $6$: $\quad 1 + 6 = 7$, $\quad 1 \times 6 = 6$

**Paso 3:** Reescribimos: $2x^2 + x + 6x + 3$

**Paso 4:** Agrupamos:

$$
(2x^2 + x) + (6x + 3)
$$

$$
= x(2x + 1) + 3(2x + 1)
$$

$$
= (2x + 1)(x + 3)
$$

$$
\boxed{(2x + 1)(x + 3)}
$$

### Ejemplo 2

Factoriza: $3x^2 + 10x + 8$

**Paso 1:** $a \times c = 3 \times 8 = 24$

**Paso 2:** $m + n = 10$, $m \times n = 24$

Los números son $4$ y $6$: $\quad 4 + 6 = 10$, $\quad 4 \times 6 = 24$

**Paso 3:** $3x^2 + 4x + 6x + 8$

**Paso 4:**

$$
(3x^2 + 4x) + (6x + 8)
$$

$$
= x(3x + 4) + 2(3x + 4)
$$

$$
= (3x + 4)(x + 2)
$$

$$
\boxed{(3x + 4)(x + 2)}
$$

### Ejemplo 3

Factoriza: $6x^2 - 11x + 4$

**Paso 1:** $a \times c = 6 \times 4 = 24$

**Paso 2:** $m + n = -11$, $m \times n = 24$ (positivo)

Ambos negativos: $-3$ y $-8$: $\quad (-3) + (-8) = -11$, $\quad (-3) \times (-8) = 24$

**Paso 3:** $6x^2 - 3x - 8x + 4$

**Paso 4:**

$$
(6x^2 - 3x) + (-8x + 4)
$$

$$
= 3x(2x - 1) - 4(2x - 1)
$$

$$
= (2x - 1)(3x - 4)
$$

$$
\boxed{(2x - 1)(3x - 4)}
$$

---

## 📖 Método 2: Tanteo o prueba y error

Este método consiste en probar combinaciones de factores hasta encontrar la correcta.

### Pasos

1. Factorizar $a$ (coeficiente de $x^2$)
2. Factorizar $c$ (término independiente)
3. Probar combinaciones hasta que el término medio sea correcto

### Ejemplo 4

Factoriza: $2x^2 + 5x + 2$

**Factores de 2 (coef. de $x^2$):** $1 \times 2$ o $2 \times 1$

**Factores de 2 (término indep.):** $1 \times 2$ o $2 \times 1$

**Probamos:** $(2x + 1)(x + 2)$

Verificamos el término medio:

$$
2x \cdot 2 + 1 \cdot x = 4x + x = 5x \quad ✓
$$

$$
2x^2 + 5x + 2 = (2x + 1)(x + 2)
$$

$$
\boxed{(2x + 1)(x + 2)}
$$

### Ejemplo 5

Factoriza: $3x^2 - 7x + 2$

**Factores de 3:** $1 \times 3$

**Factores de 2:** $1 \times 2$ (negativos porque $c > 0$ y $b < 0$)

**Probamos:** $(3x - 1)(x - 2)$

Verificamos:

$$
3x \cdot (-2) + (-1) \cdot x = -6x - x = -7x \quad ✓
$$

$$
3x^2 - 7x + 2 = (3x - 1)(x - 2)
$$

$$
\boxed{(3x - 1)(x - 2)}
$$

---

## 📖 Ejemplos con c negativo

### Ejemplo 6

Factoriza: $2x^2 + 3x - 5$

**Método de descomposición:**

$a \times c = 2 \times (-5) = -10$

Buscamos: $m + n = 3$, $m \times n = -10$

Los números son $5$ y $-2$: $\quad 5 + (-2) = 3$, $\quad 5 \times (-2) = -10$

$$
2x^2 + 5x - 2x - 5
$$

$$
= x(2x + 5) - 1(2x + 5)
$$

$$
= (2x + 5)(x - 1)
$$

$$
\boxed{(2x + 5)(x - 1)}
$$

### Ejemplo 7

Factoriza: $4x^2 - 4x - 3$

$a \times c = 4 \times (-3) = -12$

Buscamos: $m + n = -4$, $m \times n = -12$

Los números son $-6$ y $2$: $\quad (-6) + 2 = -4$, $\quad (-6) \times 2 = -12$

$$
4x^2 - 6x + 2x - 3
$$

$$
= 2x(2x - 3) + 1(2x - 3)
$$

$$
= (2x - 3)(2x + 1)
$$

$$
\boxed{(2x - 3)(2x + 1)}
$$

### Ejemplo 8

Factoriza: $5x^2 + 13x - 6$

$a \times c = 5 \times (-6) = -30$

Buscamos: $m + n = 13$, $m \times n = -30$

Los números son $15$ y $-2$: $\quad 15 + (-2) = 13$, $\quad 15 \times (-2) = -30$

$$
5x^2 + 15x - 2x - 6
$$

$$
= 5x(x + 3) - 2(x + 3)
$$

$$
= (x + 3)(5x - 2)
$$

$$
\boxed{(x + 3)(5x - 2)}
$$

---

## 📖 Con factor común

Siempre busca factor común primero.

### Ejemplo 9

Factoriza: $6x^2 + 15x + 6$

**Paso 1:** Factor común $3$:

$$
6x^2 + 15x + 6 = 3(2x^2 + 5x + 2)
$$

**Paso 2:** Factorizamos $2x^2 + 5x + 2$:

$a \times c = 2 \times 2 = 4$

$m + n = 5$, $m \times n = 4$ → $4$ y $1$

$$
3(2x^2 + 4x + x + 2) = 3[2x(x + 2) + 1(x + 2)]
$$

$$
= 3(x + 2)(2x + 1)
$$

$$
\boxed{3(x + 2)(2x + 1)}
$$

### Ejemplo 10

Factoriza: $12x^3 - 10x^2 - 8x$

**Paso 1:** Factor común $2x$:

$$
12x^3 - 10x^2 - 8x = 2x(6x^2 - 5x - 4)
$$

**Paso 2:** Factorizamos $6x^2 - 5x - 4$:

$a \times c = 6 \times (-4) = -24$

$m + n = -5$, $m \times n = -24$ → $-8$ y $3$

$$
2x(6x^2 - 8x + 3x - 4) = 2x[2x(3x - 4) + 1(3x - 4)]
$$

$$
= 2x(3x - 4)(2x + 1)
$$

$$
\boxed{2x(3x - 4)(2x + 1)}
$$

---

## 📖 Ejemplos con coeficientes grandes

### Ejemplo 11

Factoriza: $6x^2 + 17x + 12$

$a \times c = 6 \times 12 = 72$

Buscamos: $m + n = 17$, $m \times n = 72$

Los números son $8$ y $9$: $\quad 8 + 9 = 17$, $\quad 8 \times 9 = 72$

$$
6x^2 + 8x + 9x + 12
$$

$$
= 2x(3x + 4) + 3(3x + 4)
$$

$$
= (3x + 4)(2x + 3)
$$

$$
\boxed{(3x + 4)(2x + 3)}
$$

### Ejemplo 12

Factoriza: $10x^2 - 19x + 6$

$a \times c = 10 \times 6 = 60$

Buscamos: $m + n = -19$, $m \times n = 60$

Los números son $-4$ y $-15$

$$
10x^2 - 4x - 15x + 6
$$

$$
= 2x(5x - 2) - 3(5x - 2)
$$

$$
= (5x - 2)(2x - 3)
$$

$$
\boxed{(5x - 2)(2x - 3)}
$$

---

## 📖 Resumen de métodos

| Método | Cuándo usarlo |
|:-------|:--------------|
| Descomposición | Siempre funciona, más sistemático |
| Tanteo | Coeficientes pequeños, más rápido con práctica |

---

## 📝 Ejercicios de práctica

### Método de descomposición

**Ejercicio 1:** $2x^2 + 9x + 4$

**Ejercicio 2:** $3x^2 + 11x + 10$

**Ejercicio 3:** $4x^2 - 8x + 3$

---

### Con c negativo

**Ejercicio 4:** $2x^2 + x - 6$

**Ejercicio 5:** $3x^2 - 2x - 5$

**Ejercicio 6:** $5x^2 + 7x - 6$

---

### Con factor común

**Ejercicio 7:** $4x^2 + 10x + 4$

**Ejercicio 8:** $6x^3 + 7x^2 - 3x$

---

### Coeficientes grandes

**Ejercicio 9:** $8x^2 + 14x + 3$

**Ejercicio 10:** $12x^2 - 17x + 6$

---

## ✅ Soluciones

### Método de descomposición

| Ejercicio | $a \times c$ | Números | Solución |
|:---------:|:------------:|:-------:|:---------|
| 1 | $8$ | $1, 8$ | $(2x + 1)(x + 4)$ |
| 2 | $30$ | $5, 6$ | $(3x + 5)(x + 2)$ |
| 3 | $12$ | $-2, -6$ | $(2x - 1)(2x - 3)$ |

### Con c negativo

| Ejercicio | $a \times c$ | Números | Solución |
|:---------:|:------------:|:-------:|:---------|
| 4 | $-12$ | $4, -3$ | $(2x - 3)(x + 2)$ |
| 5 | $-15$ | $-5, 3$ | $(3x - 5)(x + 1)$ |
| 6 | $-30$ | $10, -3$ | $(5x - 3)(x + 2)$ |

### Con factor común

**Ejercicio 7:**

$$
4x^2 + 10x + 4 = 2(2x^2 + 5x + 2) = 2(2x + 1)(x + 2)
$$

**Ejercicio 8:**

$$
6x^3 + 7x^2 - 3x = x(6x^2 + 7x - 3) = x(3x - 1)(2x + 3)
$$

### Coeficientes grandes

| Ejercicio | Números | Solución |
|:---------:|:-------:|:---------|
| 9 | $2, 12$ | $(4x + 1)(2x + 3)$ |
| 10 | $-8, -9$ | $(4x - 3)(3x - 2)$ |

---

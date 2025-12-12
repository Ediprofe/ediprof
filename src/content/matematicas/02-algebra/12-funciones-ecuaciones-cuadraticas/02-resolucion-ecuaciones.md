# 🔍 Resolución de Ecuaciones Cuadráticas

En esta lección aprenderemos diferentes métodos para resolver ecuaciones cuadráticas.

---

## 📖 Ecuación cuadrática

Una **ecuación cuadrática** tiene la forma:

$$
ax^2 + bx + c = 0
$$

donde $a \neq 0$.

---

## 📖 Método 1: Factorización

Si podemos factorizar la expresión, usamos la propiedad del producto cero.

### Ejemplo 1

Resolver $x^2 - 5x + 6 = 0$.

$$
(x - 2)(x - 3) = 0
$$

$$
x = 2 \quad \text{o} \quad x = 3
$$

$$
\boxed{x = 2, \quad x = 3}
$$

---

### Ejemplo 2

Resolver $x^2 - 9 = 0$.

$$
(x - 3)(x + 3) = 0
$$

$$
\boxed{x = 3, \quad x = -3}
$$

---

## 📖 Método 2: Fórmula general

La **fórmula cuadrática** resuelve cualquier ecuación $ax^2 + bx + c = 0$:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Ejemplo 3

Resolver $2x^2 + 5x - 3 = 0$.

$$
a = 2, \quad b = 5, \quad c = -3
$$

$$
x = \frac{-5 \pm \sqrt{25 + 24}}{4} = \frac{-5 \pm 7}{4}
$$

$$
x_1 = \frac{2}{4} = \frac{1}{2}, \quad x_2 = \frac{-12}{4} = -3
$$

$$
\boxed{x = \frac{1}{2}, \quad x = -3}
$$

---

### Ejemplo 4

Resolver $x^2 - 4x + 1 = 0$.

$$
x = \frac{4 \pm \sqrt{16 - 4}}{2} = \frac{4 \pm \sqrt{12}}{2} = \frac{4 \pm 2\sqrt{3}}{2} = 2 \pm \sqrt{3}
$$

$$
\boxed{x = 2 + \sqrt{3}, \quad x = 2 - \sqrt{3}}
$$

---

## 📖 El discriminante

El **discriminante** $\Delta = b^2 - 4ac$ determina el número de soluciones:

| Discriminante | Soluciones |
|:-------------:|:-----------|
| $\Delta > 0$ | 2 soluciones reales distintas |
| $\Delta = 0$ | 1 solución real (doble) |
| $\Delta < 0$ | 2 soluciones complejas |

---

### Ejemplo 5

¿Cuántas soluciones tiene $x^2 - 6x + 9 = 0$?

$$
\Delta = 36 - 36 = 0
$$

Una solución (raíz doble): $x = 3$

---

### Ejemplo 6

¿Cuántas soluciones tiene $x^2 + x + 1 = 0$?

$$
\Delta = 1 - 4 = -3 < 0
$$

Dos soluciones complejas.

---

## 📖 Método 3: Completar el cuadrado

### Ejemplo 7

Resolver $x^2 + 6x + 5 = 0$ completando el cuadrado.

$$
x^2 + 6x = -5
$$
$$
x^2 + 6x + 9 = -5 + 9
$$
$$
(x + 3)^2 = 4
$$
$$
x + 3 = \pm 2
$$
$$
x = -1 \quad \text{o} \quad x = -5
$$

$$
\boxed{x = -1, \quad x = -5}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $x^2 - 7x + 12 = 0$ por factorización.

<details>
<summary>Ver solución</summary>

$(x - 3)(x - 4) = 0$

$x = 3$ o $x = 4$

</details>

---

**Ejercicio 2:** Resuelve $x^2 + 2x - 8 = 0$ usando la fórmula general.

<details>
<summary>Ver solución</summary>

$x = \frac{-2 \pm \sqrt{4 + 32}}{2} = \frac{-2 \pm 6}{2}$

$x = 2$ o $x = -4$

</details>

---

**Ejercicio 3:** Calcula el discriminante de $3x^2 - 2x + 5 = 0$.

<details>
<summary>Ver solución</summary>

$\Delta = 4 - 60 = -56 < 0$ (soluciones complejas)

</details>

---

**Ejercicio 4:** Resuelve $x^2 = 16$.

<details>
<summary>Ver solución</summary>

$x = \pm 4$

</details>

---

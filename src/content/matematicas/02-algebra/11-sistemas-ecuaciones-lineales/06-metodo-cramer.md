# 📋 Método de Cramer

En esta lección aprenderemos a resolver sistemas de ecuaciones lineales usando determinantes y la Regla de Cramer.

---

## 📖 Determinantes 2×2

El **determinante** de una matriz 2×2 se calcula:

$$
\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
$$

### Ejemplo de determinante

$$
\begin{vmatrix} 3 & 2 \\ 1 & 4 \end{vmatrix} = 3(4) - 2(1) = 12 - 2 = 10
$$

---

## 📖 Regla de Cramer

Para el sistema:
$$
\begin{cases}
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
\end{cases}
$$

Definimos los determinantes:

$$
D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}
$$

$$
D_x = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}
$$

$$
D_y = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}
$$

Las soluciones son:

$$
x = \frac{D_x}{D}, \quad y = \frac{D_y}{D} \quad \text{(si } D \neq 0\text{)}
$$

---

## 📖 Ejemplos

### Ejemplo 1

Resolver:
$$
\begin{cases}
2x + 3y = 7 \\
x - y = 1
\end{cases}
$$

**Calculamos los determinantes:**

$$
D = \begin{vmatrix} 2 & 3 \\ 1 & -1 \end{vmatrix} = 2(-1) - 3(1) = -2 - 3 = -5
$$

$$
D_x = \begin{vmatrix} 7 & 3 \\ 1 & -1 \end{vmatrix} = 7(-1) - 3(1) = -7 - 3 = -10
$$

$$
D_y = \begin{vmatrix} 2 & 7 \\ 1 & 1 \end{vmatrix} = 2(1) - 7(1) = 2 - 7 = -5
$$

**Solución:**

$$
x = \frac{-10}{-5} = 2, \quad y = \frac{-5}{-5} = 1
$$

$$
\boxed{x = 2, \quad y = 1}
$$

---

### Ejemplo 2

Resolver:
$$
\begin{cases}
3x + 2y = 12 \\
5x - 3y = 1
\end{cases}
$$

$$
D = \begin{vmatrix} 3 & 2 \\ 5 & -3 \end{vmatrix} = 3(-3) - 2(5) = -9 - 10 = -19
$$

$$
D_x = \begin{vmatrix} 12 & 2 \\ 1 & -3 \end{vmatrix} = 12(-3) - 2(1) = -36 - 2 = -38
$$

$$
D_y = \begin{vmatrix} 3 & 12 \\ 5 & 1 \end{vmatrix} = 3(1) - 12(5) = 3 - 60 = -57
$$

$$
x = \frac{-38}{-19} = 2, \quad y = \frac{-57}{-19} = 3
$$

$$
\boxed{x = 2, \quad y = 3}
$$

---

### Ejemplo 3

Resolver:
$$
\begin{cases}
4x - y = 10 \\
2x + 3y = 12
\end{cases}
$$

$$
D = \begin{vmatrix} 4 & -1 \\ 2 & 3 \end{vmatrix} = 12 - (-2) = 14
$$

$$
D_x = \begin{vmatrix} 10 & -1 \\ 12 & 3 \end{vmatrix} = 30 - (-12) = 42
$$

$$
D_y = \begin{vmatrix} 4 & 10 \\ 2 & 12 \end{vmatrix} = 48 - 20 = 28
$$

$$
x = \frac{42}{14} = 3, \quad y = \frac{28}{14} = 2
$$

$$
\boxed{x = 3, \quad y = 2}
$$

---

### Ejemplo 4

Resolver:
$$
\begin{cases}
x + 2y = 8 \\
3x - 4y = -2
\end{cases}
$$

$$
D = \begin{vmatrix} 1 & 2 \\ 3 & -4 \end{vmatrix} = -4 - 6 = -10
$$

$$
D_x = \begin{vmatrix} 8 & 2 \\ -2 & -4 \end{vmatrix} = -32 - (-4) = -28
$$

$$
D_y = \begin{vmatrix} 1 & 8 \\ 3 & -2 \end{vmatrix} = -2 - 24 = -26
$$

$$
x = \frac{-28}{-10} = \frac{14}{5}, \quad y = \frac{-26}{-10} = \frac{13}{5}
$$

$$
\boxed{x = \frac{14}{5}, \quad y = \frac{13}{5}}
$$

---

## 📖 Casos especiales

### Cuando $D = 0$

Si $D = 0$, el sistema puede ser:
- **Incompatible** (sin solución) si $D_x \neq 0$ o $D_y \neq 0$
- **Indeterminado** (infinitas soluciones) si $D = D_x = D_y = 0$

### Ejemplo 5

$$
\begin{cases}
2x + 4y = 6 \\
x + 2y = 5
\end{cases}
$$

$$
D = \begin{vmatrix} 2 & 4 \\ 1 & 2 \end{vmatrix} = 4 - 4 = 0
$$

$$
D_x = \begin{vmatrix} 6 & 4 \\ 5 & 2 \end{vmatrix} = 12 - 20 = -8 \neq 0
$$

Como $D = 0$ y $D_x \neq 0$: **Sin solución**.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve por Cramer: $\begin{cases} x + y = 5 \\ 2x - y = 4 \end{cases}$

<details>
<summary>Ver solución</summary>

$D = -1 - 2 = -3$

$D_x = -5 - 4 = -9$, $D_y = 4 - 10 = -6$

$x = 3$, $y = 2$

</details>

---

**Ejercicio 2:** Resuelve por Cramer: $\begin{cases} 3x + 2y = 11 \\ x - y = 2 \end{cases}$

<details>
<summary>Ver solución</summary>

$D = -3 - 2 = -5$

$D_x = -11 - 4 = -15$, $D_y = 6 - 11 = -5$

$x = 3$, $y = 1$

</details>

---

**Ejercicio 3:** Calcula el determinante: $\begin{vmatrix} 5 & -2 \\ 3 & 4 \end{vmatrix}$

<details>
<summary>Ver solución</summary>

$5(4) - (-2)(3) = 20 + 6 = 26$

</details>

---

**Ejercicio 4:** Si $D = 0$ y $D_x = 0$ y $D_y = 0$, ¿cuántas soluciones hay?

<details>
<summary>Ver solución</summary>

Infinitas soluciones (sistema compatible indeterminado).

</details>

---

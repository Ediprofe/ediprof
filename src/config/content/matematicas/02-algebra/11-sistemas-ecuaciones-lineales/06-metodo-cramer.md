---
title: "Método de Cramer (Determinantes)"
---

# **Método de Cramer (Determinantes)**

Hasta ahora hemos usado trucos algebraicos. El método de Cramer es diferente: es una fórmula mágica. Si organizas los números en una matriz y calculas sus "determinantes", la respuesta aparece automáticamente sin tener que despejar nada. Es ideal para programar computadoras o para quienes prefieren la aritmética sobre el álgebra.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un determinante de 2×2 y cómo calcularlo.
- La Regla de Cramer para encontrar $x$ y $y$.
- Cómo detectar sistemas sin solución o infinitas soluciones usando el determinante principal.
- Aplicar la fórmula mecánicamente.

---

## 🧮 El Determinante 2×2

Un determinante es un número especial asociado a un cuadrado de números. Se calcula multiplicando en cruz y restando.

$$
\text{Det} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = (a \cdot d) - (c \cdot b)
$$

**Ejemplo:**
$$
\begin{vmatrix} 3 & 2 \\ 1 & 5 \end{vmatrix} = (3 \cdot 5) - (1 \cdot 2) = 15 - 2 = 13
$$

---

## 📐 La Regla de Cramer

Dado el sistema:
$$
\left\{
\begin{array}{ll}
ax + by = e \\
cx + dy = f
\end{array}
\right.
$$

Necesitamos calcular 3 determinantes:

1.  **Determinante del Sistema ($\Delta_S$):** Solo con los coeficientes de $x$ y $y$.
    $$
    \Delta_S = \begin{vmatrix} a & b \\ c & d \end{vmatrix}
    $$

2.  **Determinante de X ($\Delta_x$):** Cambiamos la columna de las $x$ por los resultados ($e, f$).
    $$
    \Delta_x = \begin{vmatrix} e & b \\ f & d \end{vmatrix}
    $$

3.  **Determinante de Y ($\Delta_y$):** Cambiamos la columna de las $y$ por los resultados.
    $$
    \Delta_y = \begin{vmatrix} a & e \\ c & f \end{vmatrix}
    $$

**Solución:**
$$
x = \frac{\Delta_x}{\Delta_S}, \quad y = \frac{\Delta_y}{\Delta_S}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo Directo
Resolver:
$$
\left\{
\begin{array}{ll}
2x + 3y = 7 \\
x - y = 1
\end{array}
\right.
$$

**Paso 1: Determinante del Sistema ($\Delta_S$)**
$$
\Delta_S = \begin{vmatrix} 2 & 3 \\ 1 & -1 \end{vmatrix} = (2)(-1) - (1)(3) = -2 - 3 = -5
$$

**Paso 2: Determinante de X ($\Delta_x$)**
Reemplazamos columna $x$ ($2, 1$) por resultados ($7, 1$).
$$
\Delta_x = \begin{vmatrix} 7 & 3 \\ 1 & -1 \end{vmatrix} = (7)(-1) - (1)(3) = -7 - 3 = -10
$$

**Paso 3: Determinante de Y ($\Delta_y$)**
Reemplazamos columna $y$ ($3, -1$) por resultados ($7, 1$).
$$
\Delta_y = \begin{vmatrix} 2 & 7 \\ 1 & 1 \end{vmatrix} = (2)(1) - (1)(7) = 2 - 7 = -5
$$

**Paso 4: Solución**
$$
x = \frac{-10}{-5} = 2
$$
$$
y = \frac{-5}{-5} = 1
$$

**Resultado:**
$$
\boxed{x = 2, \quad y = 1}
$$

![Solución gráfica Ejemplo 1](/images/matematicas/algebra/sistemas-ecuaciones-lineales/cramer_ex1.svg)

---

### Ejemplo 2: Números Grandes
Resolver:
$$
\left\{
\begin{array}{ll}
3x + 2y = 12 \\
5x - 3y = 1
\end{array}
\right.
$$

**Calculamos:**
$$
\Delta_S = \begin{vmatrix} 3 & 2 \\ 5 & -3 \end{vmatrix} = -9 - 10 = -19
$$

$$
\Delta_x = \begin{vmatrix} 12 & 2 \\ 1 & -3 \end{vmatrix} = -36 - 2 = -38
$$

$$
\Delta_y = \begin{vmatrix} 3 & 12 \\ 5 & 1 \end{vmatrix} = 3 - 60 = -57
$$

**Dividimos:**
$$
x = \frac{-38}{-19} = 2
$$
$$
y = \frac{-57}{-19} = 3
$$

**Resultado:**
$$
\boxed{x = 2, \quad y = 3}
$$

![Solución gráfica Ejemplo 2](/images/matematicas/algebra/sistemas-ecuaciones-lineales/cramer_ex2.svg)

---

### Ejemplo 3: Sistema Imposible ($\Delta_S = 0$)
Resolver:
$$
\left\{
\begin{array}{ll}
2x + 4y = 6 \\
x + 2y = 5
\end{array}
\right.
$$

**Calculamos $\Delta_S$:**
$$
\Delta_S = \begin{vmatrix} 2 & 4 \\ 1 & 2 \end{vmatrix} = 4 - 4 = 0
$$

Como no se puede dividir por cero, **el sistema no tiene solución única**.
Calculamos $\Delta_x$:
$$
\Delta_x = \begin{vmatrix} 6 & 4 \\ 5 & 2 \end{vmatrix} = 12 - 20 = -8
$$

Como $\Delta_S = 0$ pero $\Delta_x \neq 0$:

**Resultado:**
$$
\boxed{\text{Sin Solución}}
$$

![Solución gráfica Ejemplo 3 (Paralelas)](/images/matematicas/algebra/sistemas-ecuaciones-lineales/cramer_ex3.svg)

---

### Ejemplo 4: Sistema Indeterminado ($\Delta_S = \Delta_x = 0$)
Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 2 \\
2x + 2y = 4
\end{array}
\right.
$$

**Cálculos:**
$$
\Delta_S = \begin{vmatrix} 1 & 1 \\ 2 & 2 \end{vmatrix} = 2 - 2 = 0
$$
$$
\Delta_x = \begin{vmatrix} 2 & 1 \\ 4 & 2 \end{vmatrix} = 4 - 4 = 0
$$

Todo es cero:

**Resultado:**
$$
\boxed{\text{Infinitas soluciones}}
$$

![Solución gráfica Ejemplo 4 (Coincidentes)](/images/matematicas/algebra/sistemas-ecuaciones-lineales/cramer_ex4.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\begin{vmatrix} 5 & 3 \\ 2 & 4 \end{vmatrix}$.

<details>
<summary>Ver solución</summary>

$(5)(4) - (2)(3) = 20 - 6$.
**Resultado:** $\boxed{14}$

</details>

---

### Ejercicio 2
Calcula $\begin{vmatrix} -2 & 5 \\ 3 & -1 \end{vmatrix}$.

<details>
<summary>Ver solución</summary>

$(-2)(-1) - (3)(5) = 2 - 15$.
**Resultado:** $\boxed{-13}$

</details>

---

### Ejercicio 3
Resuelve: $\begin{cases} x + y = 5 \\ 2x - y = 4 \end{cases}$

<details>
<summary>Ver solución</summary>

$\Delta_S = -3$, $\Delta_x = -9$, $\Delta_y = -6$.
$x = 3, y = 2$.
**Resultado:** $\boxed{(3, 2)}$

</details>

---

### Ejercicio 4
Resuelve: $\begin{cases} 3x + 2y = 11 \\ x - y = 2 \end{cases}$

<details>
<summary>Ver solución</summary>

$\Delta_S = -5$, $\Delta_x = -15$, $\Delta_y = -5$.
$x = 3, y = 1$.
**Resultado:** $\boxed{(3, 1)}$

</details>

---

### Ejercicio 5
Resuelve: $\begin{cases} 2x + 3y = 8 \\ 3x + y = 5 \end{cases}$

<details>
<summary>Ver solución</summary>

$\Delta_S = -7$, $\Delta_x = -7$, $\Delta_y = -14$.
$x = 1, y = 2$.
**Resultado:** $\boxed{(1, 2)}$

</details>

---

### Ejercicio 6
Resuelve: $\begin{cases} 5x - y = 9 \\ 2x + 3y = 7 \end{cases}$

<details>
<summary>Ver solución</summary>

$\Delta_S = 17$, $\Delta_x = 34$, $\Delta_y = 17$.
$x = 2, y = 1$.
**Resultado:** $\boxed{(2, 1)}$

</details>

---

### Ejercicio 7
Si $\Delta_S = 10$, $\Delta_x = 20$ y $\Delta_y = 50$, halla la solución.

<details>
<summary>Ver solución</summary>

$x = 20/10 = 2$.
$y = 50/10 = 5$.
**Resultado:** $\boxed{(2, 5)}$

</details>

---

### Ejercicio 8
¿Qué pasa si $\Delta_S = 0$ y $\Delta_x = 5$?

<details>
<summary>Ver solución</summary>

División por cero con numerador distinto de cero.
**Resultado:** $\boxed{\text{Sin Solución}}$

</details>

---

### Ejercicio 9
Resuelve: $\begin{cases} x = 2y + 10 \\ y = 2x - 14 \end{cases}$ (Ordena primero)

<details>
<summary>Ver solución</summary>

$x - 2y = 10$ y $-2x + y = -14$.
$\Delta_S = -3$, $\Delta_x = -18$, $\Delta_y = 6$.
$x = 6, y = -2$.
**Resultado:** $\boxed{(6, -2)}$

</details>

---

### Ejercicio 10
Resuelve: $\begin{cases} 4x + 3y = 2 \\ 2x + 5y = -6 \end{cases}$

<details>
<summary>Ver solución</summary>

$\Delta_S = 14$, $\Delta_x = 28$, $\Delta_y = -28$.
$x = 2, y = -2$.
**Resultado:** $\boxed{(2, -2)}$

</details>

---

## 🔑 Resumen

| Símbolo | Significado | Fórmula |
|:--- |:--- |:--- |
| **$\Delta_S$** | Determinante del sistema | Números de las letras $x, y$. |
| **$\Delta_x$** | Determinante de $x$ | Columna $x$ reemplazada por resultados. |
| **$\Delta_y$** | Determinante de $y$ | Columna $y$ reemplazada por resultados. |

> **Conclusión:** Cramer es un método mecánico y seguro. Si no te gusta pensar en qué multiplicar o cómo despejar, Cramer es tu mejor amigo. Solo ten cuidado con los signos al restar en el determinante.

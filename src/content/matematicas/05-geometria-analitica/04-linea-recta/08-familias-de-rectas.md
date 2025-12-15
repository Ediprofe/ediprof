# Familias de Rectas

Una **familia de rectas** es un conjunto de rectas que comparten alguna propiedad común, descrita por un parámetro. Este concepto nos permite representar infinitas rectas con una sola ecuación parametrizada.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una familia de rectas
- Tipos de familias comunes
- El haz de rectas por un punto

---

## 📖 Lo Esencial de Familias de Rectas

| Familia | Ecuación | Parámetro |
|---------|----------|-----------|
| Rectas paralelas | $y = mx + k$ | $k$ varía, $m$ fijo |
| Rectas por un punto $(a, b)$ | $y - b = m(x - a)$ | $m$ varía |
| Haz por intersección | $L_1 + \lambda L_2 = 0$ | $\lambda$ varía |

---

## 📖 Familia de Rectas Paralelas

Todas las rectas con la **misma pendiente** forman una familia de rectas paralelas.

**Forma general:**
$$
y = mx + k
$$

donde $m$ es fijo y $k$ es el parámetro que varía.

### ⚙️ Ejemplo 1: Rectas paralelas a y = 2x

Todas las rectas paralelas a $y = 2x$ tienen la forma:
$$
y = 2x + k
$$

Para diferentes valores de $k$:
- $k = 0$: $y = 2x$ (pasa por el origen)
- $k = 3$: $y = 2x + 3$
- $k = -1$: $y = 2x - 1$

Todas tienen pendiente $m = 2$.

### ⚙️ Ejemplo 2: Encontrar una recta específica de la familia

De la familia $y = 3x + k$, encuentra la recta que pasa por $(2, 7)$.

**Sustituimos $(2, 7)$:**
$$
7 = 3(2) + k
$$
$$
7 = 6 + k
$$
$$
k = 1
$$

**Respuesta:** $y = 3x + 1$

---

## 📖 Familia de Rectas por un Punto

Todas las rectas que pasan por un punto fijo $(a, b)$ forman una familia.

**Forma:**
$$
y - b = m(x - a)
$$

donde $m$ es el parámetro que varía.

### ⚙️ Ejemplo 3: Rectas por el origen

Todas las rectas que pasan por el origen $(0, 0)$:
$$
y = mx
$$

Para diferentes valores de $m$:
- $m = 1$: $y = x$
- $m = 2$: $y = 2x$
- $m = -\frac{1}{2}$: $y = -\frac{1}{2}x$

### ⚙️ Ejemplo 4: Rectas por (3, -1)

La familia de rectas que pasa por $(3, -1)$:
$$
y + 1 = m(x - 3)
$$

Para $m = 2$: $y = 2x - 7$

Para $m = -1$: $y = -x + 2$

> 💡 Esta familia incluye todas las rectas **excepto la vertical** $x = 3$.

---

## 📖 Haz de Rectas

Un **haz de rectas** es el conjunto de todas las rectas que pasan por un punto común llamado **vértice** o **centro** del haz.

Si conocemos dos rectas del haz, $L_1 = 0$ y $L_2 = 0$, todas las demás rectas del haz se escriben como:

$$
L_1 + \lambda L_2 = 0
$$

donde $\lambda$ es un parámetro real.

### ⚙️ Ejemplo 5: Haz de rectas

Las rectas $x + y - 2 = 0$ y $2x - y + 1 = 0$ se intersectan. Encuentra el haz de rectas que pasan por su intersección.

**Paso 1:** El haz se escribe como:
$$
(x + y - 2) + \lambda(2x - y + 1) = 0
$$

**Paso 2:** Desarrollando:
$$
x + y - 2 + 2\lambda x - \lambda y + \lambda = 0
$$
$$
(1 + 2\lambda)x + (1 - \lambda)y + (-2 + \lambda) = 0
$$

**Para diferentes valores de $\lambda$:**
- $\lambda = 0$: $x + y - 2 = 0$
- $\lambda = 1$: $3x + 0y - 1 = 0$ → $x = \frac{1}{3}$
- $\lambda = -1$: $-x + 2y - 3 = 0$

### ⚙️ Ejemplo 6: Encontrar recta del haz con condición

Del haz del Ejemplo 5, encuentra la recta que pasa por $(0, 0)$.

**Sustituimos $(0, 0)$ en la ecuación del haz:**
$$
(0 + 0 - 2) + \lambda(0 - 0 + 1) = 0
$$
$$
-2 + \lambda = 0
$$
$$
\lambda = 2
$$

**La recta es:**
$$
(x + y - 2) + 2(2x - y + 1) = 0
$$
$$
5x - y = 0
$$
$$
y = 5x
$$

---

## 📖 Familia con Pendiente Variable sobre una Curva

### ⚙️ Ejemplo 7: Tangentes a la parábola (concepto)

Las rectas tangentes a la parábola $y = x^2$ forman una familia. Cada punto de tangencia $(a, a^2)$ genera una recta:

$$
y - a^2 = 2a(x - a)
$$

donde $2a$ es la pendiente en el punto de tangencia.

---

## 📖 Resumen de Tipos de Familias

| Tipo | Característica común | Ecuación |
|------|---------------------|----------|
| Paralelas | Misma pendiente | $y = mx + k$ |
| Concurrentes | Pasan por el mismo punto | $y - b = m(x - a)$ |
| Haz | Pasan por intersección de dos rectas | $L_1 + \lambda L_2 = 0$ |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| Familia de rectas | Conjunto de rectas con propiedad común |
| Parámetro | Variable que genera cada recta de la familia |
| Haz | Rectas por un punto (intersección de dos rectas dadas) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la familia de rectas paralelas a $4x - y + 3 = 0$.

<details>
<summary>Ver solución</summary>

La pendiente es $m = 4$.

Familia: $y = 4x + k$ o equivalentemente $4x - y + k = 0$

</details>

### Ejercicio 2
De la familia $y = -2x + k$, encuentra la recta que pasa por $(3, 1)$.

<details>
<summary>Ver solución</summary>

$$
1 = -2(3) + k
$$
$$
1 = -6 + k
$$
$$
k = 7
$$

**Recta:** $y = -2x + 7$

</details>

### Ejercicio 3
Escribe la familia de rectas que pasan por $(2, -3)$.

<details>
<summary>Ver solución</summary>

$$
y + 3 = m(x - 2)
$$

O en forma desarrollada: $y = mx - 2m - 3$

</details>

### Ejercicio 4
Las rectas $x - y + 1 = 0$ y $x + 2y - 4 = 0$ se cortan. Encuentra la recta del haz que es paralela al eje X.

<details>
<summary>Ver solución</summary>

Haz: $(x - y + 1) + \lambda(x + 2y - 4) = 0$

$(1 + \lambda)x + (-1 + 2\lambda)y + (1 - 4\lambda) = 0$

Para ser paralela al eje X, el coeficiente de $x$ debe ser 0:
$$
1 + \lambda = 0 \Rightarrow \lambda = -1
$$

Sustituyendo:
$$
0 \cdot x + (-1 - 2)y + (1 + 4) = 0
$$
$$
-3y + 5 = 0
$$
$$
y = \frac{5}{3}
$$

</details>

### Ejercicio 5
Del haz formado por $2x + y - 3 = 0$ y $x - y + 1 = 0$, encuentra la recta que pasa por el origen.

<details>
<summary>Ver solución</summary>

$(2x + y - 3) + \lambda(x - y + 1) = 0$

Sustituyendo $(0, 0)$:
$$
-3 + \lambda = 0 \Rightarrow \lambda = 3
$$

La recta:
$$
(2x + y - 3) + 3(x - y + 1) = 0
$$
$$
5x - 2y = 0
$$

</details>

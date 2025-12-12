# ➕ Método de Reducción (Eliminación)

En esta lección aprenderemos a resolver sistemas de ecuaciones usando el método de reducción o eliminación.

---

## 📖 ¿En qué consiste el método?

1. **Multiplicar** una o ambas ecuaciones por constantes
2. **Sumar o restar** las ecuaciones para eliminar una variable
3. **Resolver** la ecuación resultante
4. **Sustituir** para encontrar la otra variable

---

## 📖 Caso 1: Coeficientes opuestos

### Ejemplo 1

Resolver:
$$
\begin{cases}
x + y = 7 \\
x - y = 3
\end{cases}
$$

Los coeficientes de $y$ son opuestos ($+1$ y $-1$).

**Sumamos las ecuaciones:**
$$
(x + y) + (x - y) = 7 + 3
$$
$$
2x = 10
$$
$$
x = 5
$$

**Sustituimos:** $5 + y = 7$, $y = 2$

$$
\boxed{x = 5, \quad y = 2}
$$

---

### Ejemplo 2

Resolver:
$$
\begin{cases}
3x + 2y = 13 \\
3x - 2y = 7
\end{cases}
$$

**Sumamos:**
$$
6x = 20
$$
$$
x = \frac{10}{3}
$$

**Sustituimos:** $3 \cdot \frac{10}{3} + 2y = 13$, $2y = 3$, $y = \frac{3}{2}$

$$
\boxed{x = \frac{10}{3}, \quad y = \frac{3}{2}}
$$

---

## 📖 Caso 2: Coeficientes iguales

### Ejemplo 3

Resolver:
$$
\begin{cases}
2x + 3y = 12 \\
2x + y = 8
\end{cases}
$$

Los coeficientes de $x$ son iguales.

**Restamos:**
$$
(2x + 3y) - (2x + y) = 12 - 8
$$
$$
2y = 4
$$
$$
y = 2
$$

**Sustituimos:** $2x + 2 = 8$, $x = 3$

$$
\boxed{x = 3, \quad y = 2}
$$

---

## 📖 Caso 3: Multiplicar una ecuación

### Ejemplo 4

Resolver:
$$
\begin{cases}
x + 3y = 7 \\
2x - y = 7
\end{cases}
$$

**Multiplicamos la primera por 2:**
$$
2x + 6y = 14
$$

**Restamos la segunda:**
$$
(2x + 6y) - (2x - y) = 14 - 7
$$
$$
7y = 7
$$
$$
y = 1
$$

**Sustituimos:** $x + 3 = 7$, $x = 4$

$$
\boxed{x = 4, \quad y = 1}
$$

---

### Ejemplo 5

Resolver:
$$
\begin{cases}
3x + 4y = 25 \\
2x - 3y = 6
\end{cases}
$$

**Multiplicamos la primera por 3 y la segunda por 4:**
$$
9x + 12y = 75
$$
$$
8x - 12y = 24
$$

**Sumamos:**
$$
17x = 99
$$
$$
x = \frac{99}{17}
$$

**Sustituimos para hallar $y$:**
$$
3 \cdot \frac{99}{17} + 4y = 25
$$
$$
4y = 25 - \frac{297}{17} = \frac{425 - 297}{17} = \frac{128}{17}
$$
$$
y = \frac{32}{17}
$$

$$
\boxed{x = \frac{99}{17}, \quad y = \frac{32}{17}}
$$

---

### Ejemplo 6

Resolver:
$$
\begin{cases}
5x - 2y = 11 \\
3x + 4y = 24
\end{cases}
$$

**Multiplicamos la primera por 2:**
$$
10x - 4y = 22
$$

**Sumamos con la segunda:**
$$
10x - 4y + 3x + 4y = 22 + 24
$$
$$
13x = 46
$$
$$
x = \frac{46}{13}
$$

**Sustituimos:**
$$
3 \cdot \frac{46}{13} + 4y = 24
$$
$$
4y = 24 - \frac{138}{13} = \frac{312 - 138}{13} = \frac{174}{13}
$$
$$
y = \frac{87}{26}
$$

$$
\boxed{x = \frac{46}{13}, \quad y = \frac{87}{26}}
$$

---

### Ejemplo 7 (Sistema más sencillo)

Resolver:
$$
\begin{cases}
4x + 3y = 10 \\
2x + y = 4
\end{cases}
$$

**Multiplicamos la segunda por $-2$:**
$$
-4x - 2y = -8
$$

**Sumamos:**
$$
4x + 3y - 4x - 2y = 10 - 8
$$
$$
y = 2
$$

**Sustituimos:** $2x + 2 = 4$, $x = 1$

$$
\boxed{x = 1, \quad y = 2}
$$

---

## 📖 Estrategia para elegir qué eliminar

1. Buscar coeficientes opuestos o iguales
2. Si no hay, elegir la variable con coeficientes más simples
3. Buscar el MCM de los coeficientes a igualar

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve: $\begin{cases} 2x + y = 7 \\ 2x - y = 3 \end{cases}$

<details>
<summary>Ver solución</summary>

Sumando: $4x = 10$, $x = \frac{5}{2}$, $y = 2$

</details>

---

**Ejercicio 2:** Resuelve: $\begin{cases} x + 2y = 10 \\ 3x + 2y = 18 \end{cases}$

<details>
<summary>Ver solución</summary>

Restando: $-2x = -8$, $x = 4$, $y = 3$

</details>

---

**Ejercicio 3:** Resuelve: $\begin{cases} 3x + y = 11 \\ x - 2y = -5 \end{cases}$

<details>
<summary>Ver solución</summary>

Multiplicamos primera por 2: $6x + 2y = 22$

Sumamos: $7x = 17$, $x = \frac{17}{7}$

$y = 11 - 3 \cdot \frac{17}{7} = \frac{26}{7}$

</details>

---

**Ejercicio 4:** Resuelve: $\begin{cases} 2x + 3y = 1 \\ 5x - 2y = 12 \end{cases}$

<details>
<summary>Ver solución</summary>

Primera × 2, Segunda × 3:

$4x + 6y = 2$, $15x - 6y = 36$

$19x = 38$, $x = 2$, $y = -1$

</details>

---

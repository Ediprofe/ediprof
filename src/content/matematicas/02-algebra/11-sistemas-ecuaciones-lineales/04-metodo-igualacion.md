# **Método de Igualación**

Este método se basa en una verdad muy simple: si Juan tiene la misma edad que Pedro, y Luis tiene la misma edad que Pedro, entonces Juan y Luis tienen la misma edad. En matemáticas: si $x = A$ y $x = B$, entonces obligatoriamente $A = B$.

---

## 🎯 ¿Qué vas a aprender?

- Cómo aislar la misma incógnita en dos ecuaciones diferentes.
- La lógica transitiva ($A=C$ y $B=C \implies A=B$).
- Resolver sistemas eliminando una variable mediante comparación.
- Manejar despejes con fracciones sin miedo.

---

## ⚖️ El Algoritmo de Igualación

1.  **Despejar:** Elige una letra ($x$ o $y$) y despéjala en **ambas** ecuaciones.
2.  **Igualar:** Pon los dos resultados frente a frente con un igual en medio. ¡La letra despejada desaparece!
3.  **Resolver:** Ahora tienes una ecuación simple con una sola incógnita. Resuélvela.
4.  **Recuperar:** Usa el valor encontrado en cualquiera de los despejes del paso 1.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Caso Sencillo
Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 10 \\
x - y = 2
\end{array}
\right.
$$

**Paso 1: Despejar $x$ en ambas**
- Ecuación 1: $x = 10 - y$
- Ecuación 2: $x = 2 + y$

**Paso 2: Igualar**
$$
10 - y = 2 + y
$$

**Paso 3: Resolver**
$$
10 - 2 = y + y
$$
$$
8 = 2y \implies y = 4
$$

**Paso 4: Recuperar $x$**
$$
x = 10 - (4) = 6
$$

**Resultado:**
$$
\boxed{x = 6, \quad y = 4}
$$

![Solución gráfica Ejemplo 1](/images/matematicas/algebra/sistemas-ecuaciones-lineales/igualacion_ex1.svg)

---

### Ejemplo 2: Despejando $y$
Resolver:
$$
\left\{
\begin{array}{ll}
2x + y = 11 \\
3x - y = 4
\end{array}
\right.
$$

**Paso 1: Despejar $y$**
- Ecuación 1: $y = 11 - 2x$
- Ecuación 2: $-y = 4 - 3x \implies y = 3x - 4$

**Paso 2: Igualar**
$$
11 - 2x = 3x - 4
$$

**Paso 3: Resolver**
$$
11 + 4 = 3x + 2x
$$
$$
15 = 5x \implies x = 3
$$

**Paso 4: Recuperar $y$**
$$
y = 11 - 2(3) = 11 - 6 = 5
$$

**Resultado:**
$$
\boxed{x = 3, \quad y = 5}
$$

![Solución gráfica Ejemplo 2](/images/matematicas/algebra/sistemas-ecuaciones-lineales/igualacion_ex2.svg)

---

### Ejemplo 3: Con Fracciones
Resolver:
$$
\left\{
\begin{array}{ll}
2x + 3y = 13 \\
4x - y = 5
\end{array}
\right.
$$

**Paso 1: Despejar $y$**
- Ecuación 1: $3y = 13 - 2x \implies y = \frac{13 - 2x}{3}$
- Ecuación 2: $-y = 5 - 4x \implies y = 4x - 5$

**Paso 2: Igualar**
$$
\frac{13 - 2x}{3} = 4x - 5
$$

**Paso 3: Resolver**
El 3 pasa multiplicando a *todo* el otro lado:
$$
13 - 2x = 3(4x - 5)
$$
$$
13 - 2x = 12x - 15
$$
$$
13 + 15 = 12x + 2x
$$
$$
28 = 14x \implies x = 2
$$

**Paso 4: Recuperar $y$**
$$
y = 4(2) - 5 = 3
$$

**Resultado:**
$$
\boxed{x = 2, \quad y = 3}
$$

![Solución gráfica Ejemplo 3](/images/matematicas/algebra/sistemas-ecuaciones-lineales/igualacion_ex3.svg)

---

### Ejemplo 4: Fracciones en Ambos Lados
Resolver:
$$
\left\{
\begin{array}{ll}
5x - 3y = 7 \\
2x + 3y = 14
\end{array}
\right.
$$

**Paso 1: Despejar $y$**
- Ecuación 1: $-3y = 7 - 5x \implies y = \frac{5x - 7}{3}$ (cambiando signos)
- Ecuación 2: $3y = 14 - 2x \implies y = \frac{14 - 2x}{3}$

**Paso 2: Igualar**
$$
\frac{5x - 7}{3} = \frac{14 - 2x}{3}
$$

**Paso 3: Resolver**
Como los denominadores son iguales (3 y 3), se cancelan:
$$
5x - 7 = 14 - 2x
$$
$$
7x = 21 \implies x = 3
$$

**Paso 4: Recuperar $y$**
$$
y = \frac{14 - 2(3)}{3} = \frac{8}{3}
$$

**Resultado:**
$$
\boxed{x = 3, \quad y = \frac{8}{3}}
$$

![Solución gráfica Ejemplo 4](/images/matematicas/algebra/sistemas-ecuaciones-lineales/igualacion_ex4.svg)

---

### Ejemplo 5: Sistema Imposible
Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 3 \\
x + y = 7
\end{array}
\right.
$$

**Despejamos $x$:**
- $x = 3 - y$
- $x = 7 - y$

**Igualamos:**
$$
3 - y = 7 - y
$$
$$
3 = 7
$$
¡Absurdo!

**Resultado:**
$$
\boxed{\text{Sin Solución}}
$$

![Solución gráfica Ejemplo 5 (Paralelas)](/images/matematicas/algebra/sistemas-ecuaciones-lineales/igualacion_ex5.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve: $\begin{cases} x = 2y \\ x = y + 5 \end{cases}$

<details>
<summary>Ver solución</summary>

$2y = y + 5 \implies y = 5$.
$x = 10$.
**Resultado:** $\boxed{(10, 5)}$

</details>

---

### Ejercicio 2
Resuelve: $\begin{cases} 3x + y = 10 \\ x - y = 2 \end{cases}$

<details>
<summary>Ver solución</summary>

Despejo $y$: $10 - 3x = x - 2$.
$12 = 4x \implies x=3$.
$y = 1$.
**Resultado:** $\boxed{(3, 1)}$

</details>

---

### Ejercicio 3
Resuelve: $\begin{cases} x + 2y = 8 \\ x + y = 5 \end{cases}$

<details>
<summary>Ver solución</summary>

$8 - 2y = 5 - y \implies 3 = y$.
$x = 2$.
**Resultado:** $\boxed{(2, 3)}$

</details>

---

### Ejercicio 4
Resuelve: $\begin{cases} 2x = y + 4 \\ 4x = y + 10 \end{cases}$

<details>
<summary>Ver solución</summary>

Despejo $y$: $2x - 4 = 4x - 10$.
$6 = 2x \implies x = 3$.
$y = 2$.
**Resultado:** $\boxed{(3, 2)}$

</details>

---

### Ejercicio 5
Resuelve: $\begin{cases} 5x + 2y = 20 \\ 5x - y = 5 \end{cases}$

<details>
<summary>Ver solución</summary>

Despejo $5x$: $20 - 2y = 5 + y$.
$15 = 3y \implies y = 5$.
$5x = 10 \implies x = 2$.
**Resultado:** $\boxed{(2, 5)}$

</details>

---

### Ejercicio 6
Resuelve: $\begin{cases} y = 3x - 1 \\ y = -2x + 9 \end{cases}$

<details>
<summary>Ver solución</summary>

$3x - 1 = -2x + 9$.
$5x = 10 \implies x = 2$.
$y = 5$.
**Resultado:** $\boxed{(2, 5)}$

</details>

---

### Ejercicio 7
Resuelve: $\begin{cases} x + y = 100 \\ x - y = 20 \end{cases}$

<details>
<summary>Ver solución</summary>

$100 - y = 20 + y$.
$80 = 2y \implies y = 40$.
$x = 60$.
**Resultado:** $\boxed{(60, 40)}$

</details>

---

### Ejercicio 8
Resuelve: $\begin{cases} 2x + 3y = 7 \\ 2x + 3y = 9 \end{cases}$

<details>
<summary>Ver solución</summary>

$7 - 3y = 9 - 3y \implies 7 = 9$.
**Resultado:** $\boxed{\text{Sin Solución}}$

</details>

---

### Ejercicio 9
Resuelve: $\begin{cases} x/2 = y \\ x/3 = y - 2 \end{cases}$

<details>
<summary>Ver solución</summary>

$x/2 = x/3 + 2$.
$3x = 2x + 12 \implies x = 12$.
$y = 6$.
**Resultado:** $\boxed{(12, 6)}$

</details>

---

### Ejercicio 10
Resuelve: $\begin{cases} x + y = 0 \\ x - y = 0 \end{cases}$

<details>
<summary>Ver solución</summary>

$-y = y \implies 2y = 0 \implies y=0$.
$x = 0$.
**Resultado:** $\boxed{(0, 0)}$

</details>

---

## 🔑 Resumen

| Paso Crítico | Consejo |
|:--- |:--- |
| **Elección** | Despeja la misma letra en ambas ecuaciones. Si despejas $x$ arriba y $y$ abajo, no sirve. |
| **Denominadores** | Si te quedan fracciones, pasa el denominador al otro lado multiplicando a *todo* el bloque. |
| **Orden** | Mantén el "=" alineado para no perderte. |

> **Conclusión:** El método de igualación es perfecto cuando las ecuaciones ya están "medio despejadas" o cuando quieres evitar sustituciones anidadas confusas. Es el método más simétrico de todos.

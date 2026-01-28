---
title: "Método de Sustitución"
---

# **Método de Sustitución**

Imagina que tienes una ecuación donde conoces el valor de $y$ en función de $x$ (por ejemplo, $y = 2x + 1$). El método de sustitución aprovecha esto: toma esa expresión y la "enchufa" en la otra ecuación, reemplazando la $y$ por su equivalente. Así, pasas de tener dos problemas difíciles a uno solo más fácil.

---

## 🎯 ¿Qué vas a aprender?

- La lógica detrás de "reemplazar una letra por su equivalente".
- Cuándo es el mejor momento para usar sustitución (pista: cuando una letra está sola).
- Cómo evitar los errores comunes con los signos negativos al sustituir.
- Resolver sistemas lineales paso a paso sin gráficas.

---

## 🔄 El Algoritmo de Sustitución

El proceso es un ciclo de 3 pasos:

1.  **Aislar:** Elige una ecuación y despeja una variable (la que veas más fácil, ojalá con coeficiente 1).
2.  **Sustituir:** Mete esa expresión en la *otra* ecuación. Ahora tendrás una ecuación con una sola incógnita. ¡Resuélvela!
3.  **Recuperar:** Toma el valor hallado y úsalo en el despeje del paso 1 para encontrar la segunda incógnita.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Caso Ideal

Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 7 \\
2x - y = 5
\end{array}
\right.
$$

**Paso 1: Despejar**
De la primera ecuación, despejamos $y$ (es fácil):
$$
y = 7 - x
$$

**Paso 2: Sustituir**
En la segunda ecuación ($2x - y = 5$), reemplazamos la $y$ por $(7 - x)$:
$$
2x - (7 - x) = 5
$$

Resolvemos la ecuación resultante:
$$
2x - 7 + x = 5
$$
$$
3x = 12 \implies x = 4
$$

**Paso 3: Recuperar**
Usamos $x=4$ en el despeje original:
$$
y = 7 - (4) = 3
$$

**Resultado:**
$$
\boxed{x = 4, \quad y = 3}
$$

![Solución gráfica Ejemplo 1](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sustitucion_ex1.svg)

---

### Ejemplo 2: Despejando $x$

Resolver:
$$
\left\{
\begin{array}{ll}
3x + 2y = 12 \\
x - y = 1
\end{array}
\right.
$$

**Paso 1: Despejar**
La $x$ en la segunda ecuación está sola, así que la elegimos:
$$
x = y + 1
$$

**Paso 2: Sustituir**
En la primera ecuación ($3x + 2y = 12$):
$$
3(y + 1) + 2y = 12
$$
$$
3y + 3 + 2y = 12
$$
$$
5y = 9 \implies y = \frac{9}{5}
$$

**Paso 3: Recuperar**
$$
x = \left(\frac{9}{5}\right) + 1 = \frac{14}{5}
$$

**Resultado:**
$$
\boxed{x = \frac{14}{5}, \quad y = \frac{9}{5}}
$$

![Solución gráfica Ejemplo 2](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sustitucion_ex2.svg)

---

### Ejemplo 3: Variable ya despejada

Resolver:
$$
\left\{
\begin{array}{ll}
5x - 2y = 8 \\
x = 3y - 1
\end{array}
\right.
$$

**Razonamiento:**
La segunda ecuación ya nos dice cuánto vale $x$. Nos saltamos el paso 1.

**Sustituir:**
$$
5(3y - 1) - 2y = 8
$$
$$
15y - 5 - 2y = 8
$$
$$
13y = 13 \implies y = 1
$$

**Recuperar:**
$$
x = 3(1) - 1 = 2
$$

**Resultado:**
$$
\boxed{x = 2, \quad y = 1}
$$

![Solución gráfica Ejemplo 3](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sustitucion_ex3.svg)

---

### Ejemplo 4: Con Fracciones

Resolver:
$$
\left\{
\begin{array}{ll}
\frac{x}{2} + y = 5 \\
x - 2y = 4
\end{array}
\right.
$$

**Paso 1: Despejar**
De la segunda ecuación, despejamos $x$:
$$
x = 2y + 4
$$

**Paso 2: Sustituir**
$$
\frac{2y + 4}{2} + y = 5
$$
Simplificamos la fracción:
$$
(y + 2) + y = 5
$$
$$
2y = 3 \implies y = \frac{3}{2}
$$

**Paso 3: Recuperar**
$$
x = 2\left(\frac{3}{2}\right) + 4 = 3 + 4 = 7
$$

**Resultado:**
$$
\boxed{x = 7, \quad y = 1.5}
$$

![Solución gráfica Ejemplo 4](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sustitucion_ex4.svg)

---

### Ejemplo 5: Sistema Incompatible

Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 3 \\
2x + 2y = 8
\end{array}
\right.
$$

**Despeje:** $y = 3 - x$.
**Sustitución:**
$$
2x + 2(3 - x) = 8
$$
$$
2x + 6 - 2x = 8
$$
$$
6 = 8
$$

¡Imposible! Cuando las letras desaparecen y llegamos a una falsedad, no hay solución.

**Resultado:**
$$
\boxed{\text{Sin Solución}}
$$

![Solución gráfica Ejemplo 5 (Paralelas)](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sustitucion_ex5.svg)

---

### Ejemplo 6: Sistema Indeterminado

Resolver:
$$
\left\{
\begin{array}{ll}
x - 2y = 4 \\
3x - 6y = 12
\end{array}
\right.
$$

**Despeje:** $x = 2y + 4$.
**Sustitución:**
$$
3(2y + 4) - 6y = 12
$$
$$
6y + 12 - 6y = 12
$$
$$
12 = 12
$$

¡Siempre verdad! Cuando llegamos a una verdad absoluta (0=0, 12=12), hay infinitas soluciones.

**Resultado:**
$$
\boxed{\text{Infinitas soluciones}}
$$

![Solución gráfica Ejemplo 6 (Coincidentes)](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sustitucion_ex6.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve por sustitución: $\begin{cases} y = 3x \\ x + y = 8 \end{cases}$

<details>
<summary>Ver solución</summary>

$x + (3x) = 8 \implies 4x = 8 \implies x = 2$
$y = 6$
**Resultado:** $\boxed{(2, 6)}$

</details>

---

### Ejercicio 2
Resuelve: $\begin{cases} x + y = 5 \\ y = x + 1 \end{cases}$

<details>
<summary>Ver solución</summary>

$x + (x+1) = 5 \implies 2x = 4 \implies x = 2$
$y = 3$
**Resultado:** $\boxed{(2, 3)}$

</details>

---

### Ejercicio 3
Resuelve: $\begin{cases} 2x + y = 10 \\ 3x - y = 5 \end{cases}$

<details>
<summary>Ver solución</summary>

Despejo $y = 10 - 2x$.
$3x - (10 - 2x) = 5 \implies 5x = 15 \implies x = 3$
$y = 4$
**Resultado:** $\boxed{(3, 4)}$

</details>

---

### Ejercicio 4
Resuelve: $\begin{cases} x = 2y + 3 \\ 2x - 5y = 8 \end{cases}$

<details>
<summary>Ver solución</summary>

$2(2y+3) - 5y = 8 \implies 4y+6-5y = 8 \implies -y = 2 \implies y = -2$
$x = -1$
**Resultado:** $\boxed{(-1, -2)}$

</details>

---

### Ejercicio 5
Resuelve: $\begin{cases} x + y = 0 \\ x - y = 2 \end{cases}$

<details>
<summary>Ver solución</summary>

$x = -y$.
$-y - y = 2 \implies -2y = 2 \implies y = -1$
$x = 1$
**Resultado:** $\boxed{(1, -1)}$

</details>

---

### Ejercicio 6
Resuelve: $\begin{cases} 2x + 3y = 12 \\ x = 3 \end{cases}$

<details>
<summary>Ver solución</summary>

Sustituyo directo $x=3$.
$2(3) + 3y = 12 \implies 6 + 3y = 12 \implies 3y = 6 \implies y = 2$
**Resultado:** $\boxed{(3, 2)}$

</details>

---

### Ejercicio 7
Resuelve: $\begin{cases} x - y = 4 \\ x + y = 4 \end{cases}$

<details>
<summary>Ver solución</summary>

$x = y + 4$.
$(y+4) + y = 4 \implies 2y = 0 \implies y = 0$
$x = 4$
**Resultado:** $\boxed{(4, 0)}$

</details>

---

### Ejercicio 8
Resuelve: $\begin{cases} 4x + y = 5 \\ y = -4x + 6 \end{cases}$

<details>
<summary>Ver solución</summary>

$4x + (-4x + 6) = 5 \implies 6 = 5$ (Falso).
**Resultado:** $\boxed{\text{Sin Solución}}$

</details>

---

### Ejercicio 9
Resuelve: $\begin{cases} x + 2y = 1 \\ x = 1 - 2y \end{cases}$

<details>
<summary>Ver solución</summary>

$(1 - 2y) + 2y = 1 \implies 1 = 1$.
**Resultado:** $\boxed{\text{Infinitas Soluciones}}$

</details>

---

### Ejercicio 10
Resuelve: $\begin{cases} 3m - n = 5 \\ m + n = 3 \end{cases}$

<details>
<summary>Ver solución</summary>

Desde segunda: $n = 3 - m$.
$3m - (3 - m) = 5 \implies 4m = 8 \implies m = 2$.
$n = 1$.
**Resultado:** $\boxed{(2, 1)}$

</details>

---

## 🔑 Resumen

| Paso Crítico | Consejo |
|:--- |:--- |
| **Elección** | Despeja siempre la variable que tenga coeficiente 1 o -1. Te ahorrarás fracciones. |
| **Paréntesis** | Al sustituir, usa SIEMPRE paréntesis, especialmente si hay restas. |
| **Comprobación** | Si tienes tiempo, prueba tus valores finales en ambas ecuaciones. |

> **Conclusión:** La sustitución es como un trasplante quirúrgico: sacamos una pieza compleja y ponemos otra equivalente para sanar (resolver) el sistema.

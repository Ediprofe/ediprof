---
title: "Introducción a los Sistemas de Ecuaciones"
---

# **Introducción a los Sistemas de Ecuaciones**

Imagina que estás en una tienda y sabes que 2 manzanas y 1 pera cuestan 5 pesos, pero 1 manzana y 3 peras cuestan 10 pesos. Con esa información, podrías averiguar el precio exacto de cada fruta. Eso es un sistema de ecuaciones: usar múltiples pistas para descubrir varios valores desconocidos al mismo tiempo.

![sistema-de-ecuaciones](https://cdn.ediprofe.com/img/matematicas/wnld-sistema-de-ecuaciones.webp)

---

## 🎯 ¿Qué vas a aprender?

- Qué es un sistema de ecuaciones lineales 2×2.
- Cómo saber si un sistema tiene solución, no tiene, o tiene infinitas.
- La interpretación geométrica: rectas que se cruzan.
- Cómo clasificar sistemas sin necesidad de resolverlos.

---

## 🔗 ¿Qué es un Sistema 2×2?

Un sistema de 2×2 es un conjunto de **dos ecuaciones** con **dos incógnitas** (generalmente $x$ y $y$) que deben cumplirse a la vez.

$$
\left\{
\begin{array}{ll}
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
\end{array}
\right.
$$

Resolverlo significa encontrar un par de números $(x, y)$ que hagan verdaderas a **ambas** igualdades simultáneamente.

### Ejemplo de Verificación

Verificar si $x = 3$ y $y = 2$ es solución del sistema:

$$
\left\{
\begin{array}{ll}
x + y = 5 \\
2x - y = 4
\end{array}
\right.
$$

**Paso 1: Probar en la primera ecuación**
$$
3 + 2 = 5 \quad \text{(Verdadero)}
$$

**Paso 2: Probar en la segunda ecuación**
$$
2(3) - 2 = 6 - 2 = 4 \quad \text{(Verdadero)}
$$

Como funciona en ambas, **sí es la solución**.

---

## 📍 Interpretación Gráfica

Cada ecuación lineal representa una **línea recta** en el plano cartesiano. La solución del sistema es el punto exacto donde esas dos líneas se cortan (se intersectan).

Dependiendo de cómo sean las rectas, tenemos tres casos:

### 1. Sistema Compatible Determinado (Una Solución)

![Gráfica de Sistema Compatible Determinado](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sistema_determinado.svg)
Las rectas se **cruzan en un único punto**. Es el caso más común.
- Significa que hay un único valor para $x$ y $y$.

### 2. Sistema Incompatible (Sin Solución)

![Gráfica de Sistema Incompatible](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sistema_incompatible.svg)
Las rectas son **paralelas** y nunca se tocan.
- No existe ningún par de números que cumpla ambas ecuaciones.

### 3. Sistema Compatible Indeterminado (Infinitas Soluciones)

![Gráfica de Sistema Indeterminado](/images/matematicas/algebra/sistemas-ecuaciones-lineales/sistema_indeterminado.svg)
Las rectas son **coincidentes** (una está encima de la otra).
- Cualquier punto de la recta sirve como solución.

---

## 🔮 Cómo Clasificarlo a Simple Vista

No necesitas resolver o graficar para saber qué tipo de sistema tienes. Solo compara los coeficientes (los números que acompañan a las letras).

Dado el sistema:
$$
\left\{
\begin{array}{ll}
Ax + By = C \\
Dx + Ey = F
\end{array}
\right.
$$

Calculamos las razones: $\frac{A}{D}$, $\frac{B}{E}$ y $\frac{C}{F}$.

| Comparación | Tipo de Sistema | Interpretación |
|:--- |:--- |:--- |
| $\frac{A}{D} \neq \frac{B}{E}$ | **Compatible Determinado** | Rectas con distinta inclinación. Se cruzan. |
| $\frac{A}{D} = \frac{B}{E} \neq \frac{C}{F}$ | **Incompatible** | Rectas paralelas (misma inclinación) pero a distinta altura. No se tocan. |
| $\frac{A}{D} = \frac{B}{E} = \frac{C}{F}$ | **Compatible Indeterminado** | Es la misma recta disfrazada (una es múltiplo de la otra). |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Clasificación Rápida
Clasifica el siguiente sistema:

$$
\left\{
\begin{array}{ll}
2x + 3y = 7 \\
4x + 5y = 9
\end{array}
\right.
$$

**Razonamiento:**
Comparamos los coeficientes de $x$ y $y$:

$$
\frac{2}{4} \quad \text{vs} \quad \frac{3}{5}
$$

Simplificando $\frac{2}{4}$ obtenemos $\frac{1}{2}$ ($0.5$).
$\frac{3}{5}$ es $0.6$.

Como $0.5 \neq 0.6$, las pendientes son distintas.

**Resultado:**
$$
\boxed{\text{Compatible Determinado (Una solución)}}
$$

### Ejemplo 2: Detectando Paralelas
Clasifica:

$$
\left\{
\begin{array}{ll}
x - 2y = 4 \\
3x - 6y = 5
\end{array}
\right.
$$

**Razonamiento:**
Comparamos $x$ y $y$:

$$
\frac{1}{3} \quad \text{vs} \quad \frac{-2}{-6}
$$

$$
\frac{-2}{-6} = \frac{1}{3}
$$

Son iguales, así que las rectas son paralelas. Ahora miramos los términos independientes ($C$ y $F$):

$$
\frac{4}{5}
$$

Como $\frac{1}{3} \neq \frac{4}{5}$, son paralelas separadas.

**Resultado:**
$$
\boxed{\text{Incompatible (Sin solución)}}
$$

### Ejemplo 3: La misma recta
Clasifica:

$$
\left\{
\begin{array}{ll}
x + y = 3 \\
2x + 2y = 6
\end{array}
\right.
$$

**Razonamiento:**
$$
\frac{1}{2} = \frac{1}{2} = \frac{3}{6}
$$

Todo da $\frac{1}{2}$. La segunda ecuación es simplemente la primera multiplicada por 2. No aporta información nueva.

**Resultado:**
$$
\boxed{\text{Compatible Indeterminado (Infinitas soluciones)}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Verifica si $(2, 5)$ es solución de:
$$
\left\{
\begin{array}{ll}
x + y = 7 \\
2x - y = -1
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

$$
2 + 5 = 7 \quad (Sí)
$$
$$
2(2) - 5 = 4 - 5 = -1 \quad (Sí)
$$

**Resultado:** $\boxed{\text{Sí es solución}}$

</details>

---

### Ejercicio 2
Clasifica el sistema:
$$
\left\{
\begin{array}{ll}
3x+2y=8 \\
6x+4y=10
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

$$
\frac{3}{6} = \frac{2}{4} = \frac{1}{2}
$$
$$
\frac{8}{10} = \frac{4}{5}
$$
Como $\frac{1}{2} \neq \frac{4}{5}$, son paralelas.

**Resultado:** $\boxed{\text{Incompatible}}$

</details>

---

### Ejercicio 3
Clasifica el sistema:
$$
\left\{
\begin{array}{ll}
x+y=10 \\
x-y=2
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

$$
\frac{1}{1} \neq \frac{1}{-1}
$$
Se cruzan.

**Resultado:** $\boxed{\text{Compatible Determinado}}$

</details>

---

### Ejercicio 4
¿Es $(0, 0)$ solución del sistema?
$$
\left\{
\begin{array}{ll}
3x+5y=0 \\
x-2y=1
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Primera: $0=0$ (Bien).
Segunda: $0 - 0 = 0 \neq 1$.

**Resultado:** $\boxed{\text{No}}$

</details>

---

### Ejercicio 5
Si dos rectas se cortan en el punto $(4, -1)$, ¿cuál es la solución del sistema?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{x=4, y=-1}$

</details>

---

### Ejercicio 6
Clasifica:
$$
\left\{
\begin{array}{ll}
-x+y=3 \\
x-y=-3
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

$$
\frac{-1}{1} = -1, \quad \frac{1}{-1} = -1, \quad \frac{3}{-3} = -1
$$
Todo igual.

**Resultado:** $\boxed{\text{Compatible Indeterminado}}$

</details>

---

### Ejercicio 7
Escribe un sistema que tenga como solución $(1, 1)$.

<details>
<summary>Ver solución</summary>

Ejemplo:
$$
\left\{
\begin{array}{ll}
x+y=2 \\
x-y=0
\end{array}
\right.
$$

</details>

---

### Ejercicio 8
¿Cuántas soluciones tiene el sistema formado por las rectas $y = 2x + 1$ y $y = 2x + 5$?

<details>
<summary>Ver solución</summary>

Tienen la misma pendiente ($m=2$) pero diferente intercepto. Son paralelas.

**Resultado:** $\boxed{\text{Cero soluciones}}$

</details>

---

### Ejercicio 9
Determina $k$ para que el sistema sea incompatible:
$$
\left\{
\begin{array}{ll}
2x+3y=5 \\
4x+ky=8
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Necesitamos $\frac{2}{4} = \frac{3}{k}$.
$$
\frac{1}{2} = \frac{3}{k} \implies k=6
$$

**Resultado:** $\boxed{k=6}$

</details>

---

### Ejercicio 10
Si graficas un sistema y obtienes una sola línea recta (una encima de la otra), ¿qué tipo de sistema es?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\text{Compatible Indeterminado}}$

</details>

---

## 🔑 Resumen

| Tipo de Sistema | Relación de Rectas | Número de Soluciones | Pista Visual |
|:--- |:--- |:--- |:--- |
| **Determinado** | Se cruzan (X) | Una única $(x, y)$ | Pendientes diferentes. |
| **Incompatible** | Paralelas (\|\|) | Cero | Misma pendiente, distinta altura. |
| **Indeterminado** | Coincidentes (=) | Infinitas | Misma pendiente y altura. |

> **Conclusión:** Antes de lanzarte a calcular a ciegas, dale un vistazo a los coeficientes. A veces el sistema te grita "¡no tengo solución!" o "¡soy una trampa duplicada!" antes de que escribas el primer número.

---
title: "Sistemas de Ecuaciones 3×3"
---

# **Sistemas de Ecuaciones 3×3**

Un sistema 3×3 es como un rompecabezas tridimensional: tenemos 3 incógnitas ($x, y, z$) y necesitamos 3 pistas (ecuaciones) para resolverlo. Imagina tres aviones volando en el espacio; el punto donde sus trayectorias (planos) se cruzan es nuestra solución.

---

## 🎯 ¿Qué vas a aprender?

- Cómo visualizar un sistema de 3 ecuaciones con 3 variables.
- La estrategia de reducir un problema "imposible" de 3×3 a uno "fácil" de 2×2.
- Resolución ordenada paso a paso para no perderse en los cálculos.
- Métodos de sustitución y reducción aplicados a 3 variables.

---

## 📐 La Estrategia General

Resolver un sistema 3×3 puede ser largo, pero no difícil si eres ordenado.  El plan maestro es:

1.  **Elegir una pareja de ecuaciones** y eliminar una letra (digamos la $z$). Te queda una ecuación con $x$ e $y$.
2.  **Elegir otra pareja diferente** y eliminar LA MISMA letra ($z$). Te queda otra ecuación con $x$ e $y$.
3.  ¡Ahora tienes un sistema 2×2! Resuélvelo como ya sabes.
4.  Con $x$ y $y$ en mano, regresa a cualquiera de las ecuaciones originales para hallar $z$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Método Paso a Paso
Resolver:
$$
\left\{
\begin{array}{ll}
x + y + z = 6 & (1) \\
2x - y + z = 3 & (2) \\
x + 2y - z = 1 & (3)
\end{array}
\right.
$$

**Paso 1: Eliminar $z$ usando (2) y (3)**
Como tenemos $+z$ en (2) y $-z$ en (3), las sumamos directo:
$$
\begin{array}{rcl}
2x - y + z &=& 3 \\
x + 2y - z &=& 1 \\
\hline
3x + y &=& 4 \quad (A)
\end{array}
$$

**Paso 2: Eliminar $z$ usando (1) y (3)**
$$
\begin{array}{rcl}
x + y + z &=& 6 \\
x + 2y - z &=& 1 \\
\hline
2x + 3y &=& 7 \quad (B)
\end{array}
$$

**Paso 3: Resolver el sistema 2×2 formado por (A) y (B)**
$$
\left\{
\begin{array}{ll}
3x + y = 4 \\
2x + 3y = 7
\end{array}
\right.
$$
Despejamos $y$ de la primera: $y = 4 - 3x$.
Sustituimos en la segunda:
$$
2x + 3(4 - 3x) = 7
$$
$$
2x + 12 - 9x = 7 \implies -7x = -5 \implies x = 5/7 \quad (\text{¡Ups, fracción!})
$$
Mejor usemos reducción en este 2×2 también.
Multiplicamos (A) por -3:
$$
-9x - 3y = -12
$$
Sumamos con (B):
$$
\begin{array}{rcl}
-9x - 3y &=& -12 \\
2x + 3y &=& 7 \\
\hline
-7x \quad &=& -5 \implies x = 5/7
\end{array}
$$
Hallamos $y$:
$$
y = 4 - 3(5/7) = 28/7 - 15/7 = 13/7
$$

**Paso 4: Hallar $z$ en la original (1)**
$$
5/7 + 13/7 + z = 6
$$
$$
18/7 + z = 42/7
$$
$$
z = 24/7
$$

**Resultado:**
$$
\boxed{x = \frac{5}{7}, \quad y = \frac{13}{7}, \quad z = \frac{24}{7}}
$$

---

### Ejemplo 2: Más Sencillo (Números Enteros)
Resolver:
$$
\left\{
\begin{array}{ll}
x + y - z = 4 & (1) \\
x - 2y + z = 5 & (2) \\
3x + y + z = 19 & (3)
\end{array}
\right.
$$

**Paso 1: Eliminar $z$ (sumando 1 y 2)**
$$
2x - y = 9 \quad (A)
$$

**Paso 2: Eliminar $z$ (sumando 1 y 3)**
$$
4x + 2y = 23 \quad (B)
$$

**Paso 3: Resolver 2×2**
De (A): $y = 2x - 9$.
Sustituimos en (B):
$$
4x + 2(2x - 9) = 23
$$
$$
4x + 4x - 18 = 23
$$
$$
8x = 41 \implies x = 41/8
$$
Hallamos $y$:
$$
y = 2(41/8) - 9 = 41/4 - 36/4 = 5/4
$$

**Paso 4: Hallar $z$ en (2)**
$$
41/8 - 2(5/4) + z = 5
$$
$$
41/8 - 20/8 + z = 40/8
$$
$$
21/8 + z = 40/8 \implies z = 19/8
$$

**Resultado:**
$$
\boxed{x = \frac{41}{8}, \quad y = \frac{5}{4}, \quad z = \frac{19}{8}}
$$

---

### Ejemplo 3: Sistema "Escalonado"
Resolver:
$$
\left\{
\begin{array}{ll}
x + 2y - z = 3 & (1) \\
3y + z = 10 & (2) \\
2z = 4 & (3)
\end{array}
\right.
$$

**Razonamiento:**
Este sistema es un regalo. Ya está semi-resuelto. Vamos de abajo hacia arriba (sustitución hacia atrás).

1.  De (3): $2z = 4 \implies z = 2$.
2.  En (2): $3y + 2 = 10 \implies 3y = 8 \implies y = 8/3$.
3.  En (1): $x + 2(8/3) - 2 = 3$.
    $$
    x + 16/3 - 6/3 = 9/3
    $$
    $$
    x + 10/3 = 9/3 \implies x = -1/3
    $$

**Resultado:**
$$
\boxed{x = -1/3, \quad y = 8/3, \quad z = 2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve:
$$
\left\{
\begin{array}{ll}
x + y + z = 6 \\
x - y + z = 2 \\
x + y - z = 0
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Sumando 1ª y 3ª: $2x + 2y = 6$.
Sumando 1ª y 2ª: $2x + 2z = 8$.
Sumando 2ª y 3ª: $2x = 2 \implies x=1$.
$y=2, z=3$.
**Resultado:** $\boxed{(1, 2, 3)}$

</details>

---

### Ejercicio 2
Resuelve el sistema escalonado:
$$
\left\{
\begin{array}{ll}
x + y + z = 10 \\
y + z = 7 \\
z = 3
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

$z=3$.
$y+3=7 \implies y=4$.
$x+4+3=10 \implies x=3$.
**Resultado:** $\boxed{(3, 4, 3)}$

</details>

---

### Ejercicio 3
Resuelve:
$$
\left\{
\begin{array}{ll}
x + z = 4 \\
y - z = 1 \\
x + y = 5
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Sumando todo: $2x + 2y = 10$.
$x=2, y=3, z=2$.
**Resultado:** $\boxed{(2, 3, 2)}$

</details>

---

### Ejercicio 4
Resuelve:
$$
\left\{
\begin{array}{ll}
x + y = 3 \\
y + z = 5 \\
x + z = 4
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Sumando todo: $2(x+y+z) = 12 \implies x+y+z=6$.
Restamos cada ec:
$(x+y+z) - (x+y) = z \implies z = 3$.
$x=1, y=2$.
**Resultado:** $\boxed{(1, 2, 3)}$

</details>

---

### Ejercicio 5
Resuelve:
$$
\left\{
\begin{array}{ll}
x - z = 0 \implies x=z \\
y + z = 10 \\
x + y + z = 15
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Sustituir $x=z$:
$z + y + z = 15 \implies y + 2z = 15$.
Tenemos $y + z = 10$.
Restar: $z = 5$.
$x=5, y=5$.
**Resultado:** $\boxed{(5, 5, 5)}$

</details>

---

### Ejercicio 6
Resuelve:
$$
\left\{
\begin{array}{ll}
2x - y + z = 3 \\
2y - z = 1 \\
-x + y = 1
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Despejo $y = x+1$.
$2(x+1) - z = 1 \implies 2x+2-z=1 \implies z = 2x+1$.
Sustituyo en 1ª: $2x - (x+1) + (2x+1) = 3$.
$3x = 3 \implies x=1$.
$y=2, z=3$.
**Resultado:** $\boxed{(1, 2, 3)}$

</details>

---

### Ejercicio 7
Resuelve:
$$
\left\{
\begin{array}{ll}
x + y + z = 3 \\
2x + 2y + 2z = 6 \\
x - y = 0
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

1ª y 2ª son la misma (multiplicada pot 2). Infinitas soluciones.
Restricción: $x=y$.
$2x + z = 3$.
**Resultado:** $\boxed{\text{Infinitas Soluciones}}$

</details>

---

### Ejercicio 8
Resuelve:
$$
\left\{
\begin{array}{ll}
x + y + z = 12 \\
2x = 10 \\
3y = 9
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

$x=5, y=3$.
$5+3+z=12 \implies z=4$.
**Resultado:** $\boxed{(5, 3, 4)}$

</details>

---

### Ejercicio 9
Resuelve:
$$
\left\{
\begin{array}{ll}
x + y = 3 \\
z = 5 \\
x - y = 1
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

2x = 4 \implies x=2.
y = 1.
z = 5.
**Resultado:** $\boxed{(2, 1, 5)}$

</details>

---

### Ejercicio 10
Resuelve:
$$
\left\{
\begin{array}{ll}
3x + 2y + z = 1 \\
5x + 3y + 4z = 2 \\
x + y - z = 1
\end{array}
\right.
$$

<details>
<summary>Ver solución</summary>

Sumando 1ª y 3ª: $4x + 3y = 2$.
Sumando 3ª por 4 y 2ª: $4x + 4y - 4z = 4 \dots 9x + 7y = 6$.
Resolver sistema 2x2. $x=-4, y=6, z=-1$.
**Resultado:** $\boxed{(-4, 6, -1)}$

</details>

---

## 🔑 Resumen

| Concepto | Estrategia |
|:--- |:--- |
| **Meta** | Eliminar una variable para convertir el 3×3 en un 2×2 conocido. |
| **Orden** | Etiqueta tus ecuaciones (1), (2), (3) y sé metódico. |
| **Tipos** | Escalonados (fáciles), completos (trabajosos) o afortunados ("x" ya despejada). |

> **Conclusión:** Resolver un 3×3 requiere paciencia y papel. Si mantienes el orden, es simplemente resolver tres sistemas pequeños uno tras otro.

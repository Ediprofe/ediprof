---
title: "Método de Reducción (Eliminación)"
---

# **Método de Reducción (Eliminación)**

Este método es el favorito de muchos porque va directo al grano: sumar o restar las ecuaciones completas para que una de las letras "desaparezca" mágicamente. Es como enfrentar dos ejércitos: si tienes 5 soldados positivos y 5 negativos, se anulan mutuamente y el campo queda despejado.

---

## 🎯 ¿Qué vas a aprender?

- Cómo eliminar una incógnita sumando verticalmente.
- Multiplicar ecuaciones enteras para preparar el terreno.
- Manejar signos para lograr la cancelación perfecta.
- La estrategia del MCM aplicada a sistemas de ecuaciones.

---

## ➕ El Arte de Sumar Ecuaciones

Si $A=B$ y $C=D$, entonces $A+C = B+D$. ¡Podemos sumar igualdades!
El truco es lograr que al sumar, una de las variables tenga coeficientes opuestos (ej: $3x$ y $-3x$), para que el resultado sea cero.

**Pasos:**
1.  **Alinear:** Asegúrate de que las $x$, las $y$ y los números estén en columnas ordenadas.
2.  **Preparar:** Multiplica una (o ambas) ecuaciones para que los números de la letra que quieres borrar sean iguales pero con signo contrario.
3.  **Sumar:** Suma las dos ecuaciones verticalmente. ¡Una letra morirá!
4.  **Resolver y Recuperar:** Resuelve lo que quedó y busca la otra incógnita.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Caso Perfecto
Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 7 \\
x - y = 3
\end{array}
\right.
$$

**Razonamiento:**
Fíjate en las $y$. Tenemos $+y$ arriba y $-y$ abajo. ¡Ya están listas para cancelarse!

**Sumamos verticalmente:**
$$
\begin{array}{rcl}
x + y &=& 7 \\
x - y &=& 3 \\
\hline
2x + 0 &=& 10
\end{array}
$$

**Resolver:**
$$
2x = 10 \implies x = 5
$$

**Recuperar:**
Sustituimos $x=5$ en la primera ecuación:
$$
5 + y = 7 \implies y = 2
$$

**Resultado:**
$$
\boxed{x = 5, \quad y = 2}
$$

![Solución gráfica Ejemplo 1](/images/matematicas/algebra/sistemas-ecuaciones-lineales/reduccion_ex1.svg)

---

### Ejemplo 2: Multiplicar una Ecuación
Resolver:
$$
\left\{
\begin{array}{ll}
x + 3y = 7 \\
2x - y = 7
\end{array}
\right.
$$

**Estrategia:** Queremos eliminar la $y$. Arriba hay $3y$, abajo $-y$. Si multiplicamos la de abajo por 3, tendremos $-3y$.

**Operación:**
Dejamos la 1ª igual:
$$
x + 3y = 7
$$
Multiplicamos la 2ª por 3:
$$
3(2x - y) = 3(7) \implies 6x - 3y = 21
$$

**Suma:**
$$
\begin{array}{rcl}
x + 3y &=& 7 \\
6x - 3y &=& 21 \\
\hline
7x \quad &=& 28
\end{array}
$$

**Resolver:**
$$
x = 4
$$

**Recuperar:** (en la original 2ª)
$$
2(4) - y = 7 \implies 8 - y = 7 \implies y = 1
$$

**Resultado:**
$$
\boxed{x = 4, \quad y = 1}
$$

![Solución gráfica Ejemplo 2](/images/matematicas/algebra/sistemas-ecuaciones-lineales/reduccion_ex2.svg)

---

### Ejemplo 3: Reducción Doble (MCM)
Resolver:
$$
\left\{
\begin{array}{ll}
3x + 4y = 25 \\
2x - 3y = 6
\end{array}
\right.
$$

**Estrategia:** Eliminar $y$. Coeficientes 4 y 3. El MCM es 12.
- Multiplicamos la 1ª por 3 (para tener $12y$).
- Multiplicamos la 2ª por 4 (para tener $-12y$).

**Preparación:**
$$
\begin{array}{ll}
3(3x + 4y = 25) & \implies 9x + 12y = 75 \\
4(2x - 3y = 6) & \implies 8x - 12y = 24
\end{array}
$$

**Suma:**
$$
\begin{array}{rcl}
9x + 12y &=& 75 \\
8x - 12y &=& 24 \\
\hline
17x \quad &=& 99
\end{array}
$$

**Resolver:**
$$
x = \frac{99}{17}
$$

Para hallar $y$, podemos sustituir o... ¡hacer reducción de nuevo para eliminar $x$!
MCM de $3x$ y $2x$ es 6.
- 1ª por -2: $-6x - 8y = -50$
- 2ª por 3: $6x - 9y = 18$

Suma: $-17y = -32 \implies y = \frac{32}{17}$.

**Resultado:**
$$
\boxed{x = \frac{99}{17}, \quad y = \frac{32}{17}}
$$

![Solución gráfica Ejemplo 3](/images/matematicas/algebra/sistemas-ecuaciones-lineales/reduccion_ex3.svg)

---

### Ejemplo 4: Signos Iguales
Resolver:
$$
\left\{
\begin{array}{ll}
5x + y = 10 \\
2x + y = 4
\end{array}
\right.
$$

**Estrategia:** Las $y$ son iguales. Restamos las ecuaciones (o multiplicamos una por -1).

**Multiplicar la 2ª por -1:**
$$
\begin{array}{rcl}
5x + y &=& 10 \\
-2x - y &=& -4 \\
\hline
3x \quad &=& 6
\end{array}
$$

**Resolver:**
$$
3x = 6 \implies x = 2
$$

**Recuperar:**
$$
2(2) + y = 4 \implies 4 + y = 4 \implies y = 0
$$

**Resultado:**
$$
\boxed{x = 2, \quad y = 0}
$$

![Solución gráfica Ejemplo 4](/images/matematicas/algebra/sistemas-ecuaciones-lineales/reduccion_ex4.svg)

---

### Ejemplo 5: Sistema Incompatible
Resolver:
$$
\left\{
\begin{array}{ll}
2x - y = 4 \\
-4x + 2y = 8
\end{array}
\right.
$$

**Estrategia:** Multiplicar la 1ª por 2.
$$
4x - 2y = 8
$$

**Sumar con la 2ª:**
$$
\begin{array}{rcl}
4x - 2y &=& 8 \\
-4x + 2y &=& 8 \\
\hline
0 \quad &=& 16
\end{array}
$$

¡Imposible!

**Resultado:**
$$
\boxed{\text{Sin Solución}}
$$

![Solución gráfica Ejemplo 5 (Paralelas)](/images/matematicas/algebra/sistemas-ecuaciones-lineales/reduccion_ex5.svg)

---

## 📝 Ejercicios de Práctica

### Ejemplo 1
Resuelve: $\begin{cases} 3x + y = 10 \\ 2x - y = 5 \end{cases}$

<details>
<summary>Ver solución</summary>

Suma directa: $5x = 15 \implies x=3$.
$3(3) + y = 10 \implies y = 1$.
**Resultado:** $\boxed{(3, 1)}$

</details>

---

### Ejemplo 2
Resuelve: $\begin{cases} x + 2y = 8 \\ x - 2y = 4 \end{cases}$

<details>
<summary>Ver solución</summary>

Suma directa: $2x = 12 \implies x=6$.
$6 - 2y = 4 \implies 2 = 2y \implies y=1$.
**Resultado:** $\boxed{(6, 1)}$

</details>

---

### Ejemplo 3
Resuelve: $\begin{cases} 5x + 3y = 20 \\ 2x + y = 9 \end{cases}$

<details>
<summary>Ver solución</summary>

2ª por -3: $-6x - 3y = -27$.
Suma: $-x = -7 \implies x=7$.
$2(7) + y = 9 \implies y = -5$.
**Resultado:** $\boxed{(7, -5)}$

</details>

---

### Ejemplo 4
Resuelve: $\begin{cases} 3x - 4y = 6 \\ x + 2y = 12 \end{cases}$

<details>
<summary>Ver solución</summary>

2ª por 2: $2x + 4y = 24$.
Suma: $5x = 30 \implies x=6$.
$6 + 2y = 12 \implies 2y = 6 \implies y=3$.
**Resultado:** $\boxed{(6, 3)}$

</details>

---

### Ejemplo 5
Resuelve: $\begin{cases} 4x + 9y = 1 \\ 4x + 9y = 2 \end{cases}$

<details>
<summary>Ver solución</summary>

Restar: $0 = -1$.
**Resultado:** $\boxed{\text{Sin Solución}}$

</details>

---

### Ejemplo 6
Resuelve: $\begin{cases} 10x - 3y = 36 \\ 2x + 5y = -4 \end{cases}$

<details>
<summary>Ver solución</summary>

2ª por -5: $-10x - 25y = 20$.
Suma: $-28y = 56 \implies y=-2$.
$2x + 5(-2) = -4 \implies 2x = 6 \implies x=3$.
**Resultado:** $\boxed{(3, -2)}$

</details>

---

### Ejemplo 7
Resuelve: $\begin{cases} 7x + 2y = 10 \\ 7x + 2y = 10 \end{cases}$

<details>
<summary>Ver solución</summary>

Restar: $0=0$.
**Resultado:** $\boxed{\text{Infinitas Soluciones}}$

</details>

---

### Ejemplo 8
Resuelve: $\begin{cases} 3x + 2y = 7 \\ 4x - 3y = -2 \end{cases}$

<details>
<summary>Ver solución</summary>

1ª por 3, 2ª por 2.
$9x + 6y = 21$
$8x - 6y = -4$
$17x = 17 \implies x=1$.
$y=2$.
**Resultado:** $\boxed{(1, 2)}$

</details>

---

### Ejemplo 9
Resuelve: $\begin{cases} x + y = 50 \\ x - y = 10 \end{cases}$

<details>
<summary>Ver solución</summary>

Suma: $2x = 60 \implies x=30$.
$y=20$.
**Resultado:** $\boxed{(30, 20)}$

</details>

---

### Ejemplo 10
Resuelve: $\begin{cases} 2x - 5y = 1 \\ 3x + 2y = 11 \end{cases}$

<details>
<summary>Ver solución</summary>

1ª por 2, 2ª por 5.
$4x - 10y = 2$
$15x + 10y = 55$
$19x = 57 \implies x=3$.
$y=1$.
**Resultado:** $\boxed{(3, 1)}$

</details>

---

## 🔑 Resumen

| Método | Estrategia |
|:--- |:--- |
| **Sumas y Restas** | Si los números son iguales, ¡resta! Si son opuestos, ¡suma! |
| **Multiplicación Cruzada** | Si tienes $3x$ y $5x$, multiplica arriba por 5 y abajo por -3. |
| **Objetivo** | Crear un cero donde antes había una letra. |

> **Conclusión:** La reducción es el método más potente para sistemas complicados o con número grandes. Es limpio, ordenado y evita tener que trabajar con fracciones en la mitad del proceso.

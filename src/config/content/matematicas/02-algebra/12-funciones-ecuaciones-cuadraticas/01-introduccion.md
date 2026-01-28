---
title: "Funciones Cuadráticas"
---

# **Funciones Cuadráticas**

Desde la trayectoria de un balón de fútbol hasta el diseño de antenas satelitales, las curvas están en todas partes. La "madre" de todas estas curvas en forma de U es la función cuadrática. En esta lección, aprenderás a identificarla y entender su anatomía básica.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una función cuadrática y cómo se diferencia de una lineal.
- El papel de los coeficientes $a$, $b$ y $c$.
- Cómo saber si la parábola sonríe (U) o está triste (n).
- Calcular el vértice: el punto más importante de la curva.

---

## 🏗️ La Estructura

Una función cuadrática tiene la forma general:

$$
f(x) = ax^2 + bx + c
$$

Donde $a \neq 0$.
Si $a$ fuera cero, el término cuadrado desaparecería y volveríamos a tener una línea recta ($bx+c$). ¡El término $x^2$ es el que crea la curva!

### El Rol de $a$ (El Jefe)

El coeficiente $a$ decide la forma y dirección:
- **Si $a > 0$:** La parábola abre hacia **arriba** (carita feliz). Tiene un punto mínimo.
  
  ![Gráfica a > 0](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_a_positive.svg)

- **Si $a < 0$:** La parábola abre hacia **abajo** (carita triste). Tiene un punto máximo.

  ![Gráfica a < 0](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_a_negative.svg)

- **Valor absoluto:** Mientras más grande sea $|a|$, más "flaca" y cerrada será la parábola.

  ![Comparación de aperturas](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/width_comparison.svg)

---

## 📍 El Vértice: El Corazón de la Parábola

El vértice $(h, k)$ es el punto de inflexión donde la curva cambia de dirección.

![Concepto de Vértice](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/vertex_concept.svg)

Para encontrar la coordenada $x$ del vértice ($x_v$):

$$
x_v = \frac{-b}{2a}
$$

Para encontrar la coordenada $y$ ($y_v$), simplemente evaluamos la función en ese punto:

$$
y_v = f(x_v)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Identificación Básica
Analizar la función $f(x) = x^2 - 4x + 3$.

**1. Identificar coeficientes:**
$$
a = 1, \quad b = -4, \quad c = 3
$$

**2. Orientación:**
Como $a = 1$ (positivo), la parábola abre hacia **arriba**.

**3. Vértice:**
Calculamos la coordenada $x$:
$$
x_v = \frac{-(-4)}{2(1)} = \frac{4}{2} = 2
$$

Calculamos la altura $y$:
$$
f(2) = (2)^2 - 4(2) + 3
$$
$$
f(2) = 4 - 8 + 3 = -1
$$

**Resultado:**
$$
\boxed{\text{Vértice en } (2, -1)}
$$

![Ejemplo 1: Gráfica](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_ex1.svg)

---

### Ejemplo 2: Hacia Abajo
Analizar $g(x) = -2x^2 + 8x - 6$.

**1. Coeficientes:**
$$
a = -2, \quad b = 8, \quad c = -6
$$

**2. Orientación:**
Como $a = -2$ (negativo), abre hacia **abajo**.

**3. Vértice:**
$$
x_v = \frac{-8}{2(-2)} = \frac{-8}{-4} = 2
$$
$$
y_v = -2(2)^2 + 8(2) - 6
$$
$$
y_v = -2(4) + 16 - 6 = -8 + 16 - 6 = 2
$$

**Resultado:**
$$
\boxed{\text{Vértice en } (2, 2)}
$$

![Ejemplo 2: Gráfica](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_ex2.svg)

---

### Ejemplo 3: Parábola Incompleta
Analizar $h(x) = 3x^2 + 6x$.

**1. Coeficientes:**
$$
a = 3, \quad b = 6, \quad c = 0
$$

**2. Vértice:**
$$
x_v = \frac{-6}{2(3)} = \frac{-6}{6} = -1
$$
$$
y_v = 3(-1)^2 + 6(-1) = 3(1) - 6 = -3
$$

**Resultado:**
$$
\boxed{\text{Vértice en } (-1, -3)}
$$

![Ejemplo 3: Gráfica](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_ex3.svg)

---

### Ejemplo 4: Evaluación
Si $f(x) = x^2 - 5x + 6$, calcular $f(3)$.

**Razonamiento:**
Sustituimos $x$ por 3.

$$
f(3) = (3)^2 - 5(3) + 6
$$
$$
f(3) = 9 - 15 + 6 = 0
$$

**Resultado:**
$$
\boxed{f(3) = 0}
$$

![Ejemplo 4: Evaluación](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_ex4.svg)

---

### Ejemplo 5: Intercepto con el Eje Y
¿Dónde corta al eje Y la función $f(x) = -x^2 + 4x + 10$?

**Razonamiento:**
El corte con Y ocurre cuando $x=0$.
$$
f(0) = -(0)^2 + 4(0) + 10 = 10
$$
Es decir, es simplemente el valor de $c$.

**Resultado:**
$$
\boxed{\text{Punto } (0, 10)}
$$

![Ejemplo 5: Intercepto](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/intro_ex5.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica $a, b, c$ en $f(x) = -x^2 + 6x - 5$.

<details>
<summary>Ver solución</summary>

$$
a = -1, \quad b = 6, \quad c = -5
$$

</details>

---

### Ejercicio 2
¿Hacia dónde abre la función $y = 5 - 3x^2$?

<details>
<summary>Ver solución</summary>

Ordenando: $y = -3x^2 + 5$. Como $a = -3$, abre hacia **abajo**.

</details>

---

### Ejercicio 3
Calcula el vértice de $y = x^2 - 6x + 5$.

<details>
<summary>Ver solución</summary>

$x_v = -(-6)/2 = 3$.
$y_v = 3^2 - 18 + 5 = 9 - 18 + 5 = -4$.
**Resultado:** $\boxed{(3, -4)}$

</details>

---

### Ejercicio 4
Evalúa $f(x) = 2x^2 + 3x - 1$ para $x = -1$.

<details>
<summary>Ver solución</summary>

$2(1) - 3 - 1 = -2$.
**Resultado:** $\boxed{-2}$

</details>

---

### Ejercicio 5
¿Cuál es el intercepto $y$ de $f(x) = 4x^2 - 100$?

<details>
<summary>Ver solución</summary>

Es el término independiente $c$.
**Resultado:** $\boxed{-100}$

</details>

---

### Ejercicio 6
Encuentra el eje de simetría de $y = 2x^2 + 8x$.

<details>
<summary>Ver solución</summary>

$x = -8 / 4 = -2$.
**Resultado:** $\boxed{x = -2}$

</details>

---

### Ejercicio 7
Si el vértice está en $(2, 5)$ y abre hacia abajo, ¿el 5 es un máximo o un mínimo?

<details>
<summary>Ver solución</summary>

Si abre hacia abajo, es el punto más alto.
**Resultado:** $\boxed{\text{Máximo}}$

</details>

---

### Ejercicio 8
Escribe una función cuadrática que tenga $a=1, b=0, c=-4$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{f(x) = x^2 - 4}$

</details>

---

### Ejercicio 9
Calcula el vértice de $y = -x^2 + 4$.

<details>
<summary>Ver solución</summary>

$b=0$, así que $x_v = 0$.
$y_v = 4$.
**Resultado:** $\boxed{(0, 4)}$

</details>

---

### Ejercicio 10
¿Qué efecto tiene cambiar $f(x) = x^2$ a $g(x) = 3x^2$?

<details>
<summary>Ver solución</summary>

Se hace más estrecha (crece más rápido).

</details>

---

## 🔑 Resumen

| Elemento | Fórmula/Concepto | Descripción |
|:--- |:--- |:--- |
| **$a$** | Coeficiente cuadrático | Define si abre arriba ($+$) o abajo ($-$). |
| **$c$** | Término independiente | Es el corte con el eje Y. |
| **Vértice** | $x = -b/2a$ | El punto de retorno de la curva. |

> **Conclusión:** Conocer los coeficientes es conocer el destino de la parábola. Antes de graficar nada, $a$, $b$ y $c$ ya te cuentan la historia completa.

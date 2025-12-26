# **Binomio de Newton**

Si te pido calcular $(a+b)^2$, seguro sabes que es $a^2 + 2ab + b^2$. Pero, ¿qué pasa si te pido $(a+b)^{10}$? Multiplicar el paréntesis 10 veces sería una pesadilla interminable.

Para evitar ese trabajo manual, Isaac Newton generalizó un patrón elegante que nos permite expandir cualquier potencia de un binomio en segundos.

---

## �� ¿Qué vas a aprender?

- Cómo expandir potencias como $(x+y)^5$ sin multiplicar paso a paso.
- El patrón secreto de los exponentes que suben y bajan.
- Cómo usar los números combinatorios para hallar los coeficientes.
- Cómo encontrar un término específico sin desarrollar toda la fórmula.

---

## 🔍 El Patrón Oculto

Observemos qué pasa cuando elevamos un binomio a diferentes potencias:

$$
(a+b)^1 = 1a + 1b
$$

$$
(a+b)^2 = 1a^2 + 2ab + 1b^2
$$

$$
(a+b)^3 = 1a^3 + 3a^2b + 3ab^2 + 1b^3
$$

Si miramos con atención, hay tres reglas de oro:

1.  **Exponentes de $a$:** Empiezan en el máximo ($n$) y bajan de uno en uno hasta desaparecer ($a^0$).
2.  **Exponentes de $b$:** Empiezan en cero ($b^0$) y suben de uno en uno hasta el máximo ($n$).
3.  **Coeficientes:** Los números que acompañan ($1, 3, 3, 1$) no son aleatorios. ¡Son combinaciones!

---

## 📝 La Fórmula General

El **Teorema del Binomio** dice que para cualquier entero positivo $n$:

$$
(a + b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \dots + \binom{n}{n}b^n
$$

Donde $\binom{n}{k}$ es el número combinatorio (o coeficiente binomial):

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

> 💡 **Truco:** La suma de los exponentes en cada término siempre debe dar $n$.

---

## ⚡ Caso con Resta (Signos Alternados)

Si el binomio es una resta $(a - b)^n$, la fórmula es idéntica, pero los signos se alternan: **positivo, negativo, positivo, negativo...**

$$
(a - b)^n = \binom{n}{0}a^n - \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 - \dots
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Expansión básica

Desarrolla la expresión $(x + 2)^4$.

**Paso 1: Los Coeficientes**
Para $n=4$, calculamos las combinaciones:
$\binom{4}{0}=1, \binom{4}{1}=4, \binom{4}{2}=6, \binom{4}{3}=4, \binom{4}{4}=1$.

**Paso 2: Los Exponentes**
$x$ baja: $x^4, x^3, x^2, x^1, x^0$
$2$ sube: $2^0, 2^1, 2^2, 2^3, 2^4$

**Paso 3: Armar la fórmula**

$$
1(x^4) + 4(x^3)(2) + 6(x^2)(2^2) + 4(x)(2^3) + 1(2^4)
$$

**Paso 4: Simplificar**

$$
x^4 + 8x^3 + 6x^2(4) + 4x(8) + 16
$$

$$
x^4 + 8x^3 + 24x^2 + 32x + 16
$$

**Resultado:**

$$
\boxed{x^4 + 8x^3 + 24x^2 + 32x + 16}
$$

---

### Ejemplo 2: Binomio con resta y coeficientes

Desarrolla $(2x - 3)^3$.

**Datos:**
- $a = 2x$
- $b = 3$
- Signos alternados ($+, -, +, -$)
- Coeficientes para $n=3$: $1, 3, 3, 1$.

**Razonamiento:**

$$
1(2x)^3 - 3(2x)^2(3)^1 + 3(2x)^1(3)^2 - 1(3)^3
$$

Resolvemos potencias primero:

$$
1(8x^3) - 3(4x^2)(3) + 3(2x)(9) - 27
$$

Multiplicamos:

$$
8x^3 - 36x^2 + 54x - 27
$$

**Resultado:**

$$
\boxed{8x^3 - 36x^2 + 54x - 27}
$$

---

### Ejemplo 3: Hallar un término específico

Encuentra el **cuarto término** de la expansión de $(x + 2y)^{10}$.

**Razonamiento:**
No necesitamos expandir todo. Usamos la fórmula del término general $T_{k+1}$.
Para el término 4, $k = 3$ (porque empezamos a contar desde $k=0$).

$$
T_{k+1} = \binom{n}{k} a^{n-k} b^k
$$

Sustituimos $n=10, k=3, a=x, b=2y$:

$$
T_4 = \binom{10}{3} (x)^{10-3} (2y)^3
$$

Calculamos el coeficiente $\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$.

$$
T_4 = 120 (x^7) (8y^3)
$$

$$
T_4 = 120 \times 8 \times x^7 y^3
$$

$$
T_4 = 960 x^7 y^3
$$

**Resultado:**

$$
\boxed{960 x^7 y^3}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Expande $(x + 1)^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Coeficientes: 1, 4, 6, 4, 1.

$$
x^4 + 4x^3(1) + 6x^2(1)^2 + 4x(1)^3 + 1^4
$$

**Resultado:**
$$
\boxed{x^4 + 4x^3 + 6x^2 + 4x + 1}
$$

</details>

### Ejercicio 2
Expande $(m - 2)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Coeficientes: 1, 3, 3, 1. Signos alternados.

$$
m^3 - 3m^2(2) + 3m(2^2) - 2^3
$$

$$
m^3 - 6m^2 + 12m - 8
$$

**Resultado:**
$$
\boxed{m^3 - 6m^2 + 12m - 8}
$$

</details>

### Ejercicio 3
Expande $(2x + 3)^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es un trinomio cuadrado perfecto.

$$
(2x)^2 + 2(2x)(3) + 3^2
$$

**Resultado:**
$$
\boxed{4x^2 + 12x + 9}
$$

</details>

### Ejercicio 4
Halla el coeficiente del tercer término de $(a + b)^5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tercer término implica $k=2$. $n=5$.

$$
\binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10
$$

**Resultado:**
$$
\boxed{10}
$$

</details>

### Ejercicio 5
Expande $(x^2 + 1)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a = x^2$.

$$
(x^2)^3 + 3(x^2)^2(1) + 3(x^2)(1)^2 + 1^3
$$

**Resultado:**
$$
\boxed{x^6 + 3x^4 + 3x^2 + 1}
$$

</details>

### Ejercicio 6
Encuentra el término central de $(x + y)^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $n=4$, hay 5 términos. El central es el 3º ($k=2$).

$$
\binom{4}{2} x^{4-2} y^2 = 6x^2y^2
$$

**Resultado:**
$$
\boxed{6x^2y^2}
$$

</details>

### Ejercicio 7
Expande $(3 - x)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
3^3 - 3(3^2)(x) + 3(3)(x^2) - x^3
$$

$$
27 - 27x + 9x^2 - x^3
$$

**Resultado:**
$$
\boxed{27 - 27x + 9x^2 - x^3}
$$

</details>

### Ejercicio 8
Calcula el valor de $\binom{6}{3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{6 \times 5 \times 4}{3 \times 2 \times 1} = \frac{120}{6} = 20
$$

**Resultado:**
$$
\boxed{20}
$$

</details>

### Ejercicio 9
Expande $(x + \frac{1}{x})^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
x^2 + 2(x)(\frac{1}{x}) + (\frac{1}{x})^2
$$

$$
x^2 + 2 + \frac{1}{x^2}
$$

**Resultado:**
$$
\boxed{x^2 + 2 + \frac{1}{x^2}}
$$

</details>

### Ejercicio 10
¿Cuántos términos tiene la expansión de $(a+b)^{12}$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El número de términos siempre es $n + 1$.

$$
12 + 1 = 13
$$

**Resultado:**
$$
\boxed{13}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula / Regla |
|----------|-----------------|
| **Binomio de Newton** | $(a+b)^n = \sum \binom{n}{k} a^{n-k} b^k$ |
| **Exponentes** | $a$ baja, $b$ sube. Suma siempre es $n$. |
| **Coeficientes** | Se obtienen con $\binom{n}{k}$ o Triángulo de Pascal. |
| **Signos** | Si es resta, alternan: $+ - + - \dots$ |

> El Binomio de Newton convierte multiplicaciones tediosas en un proceso de sustitución simple y elegante.

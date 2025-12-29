# **Término General del Binomio**

En la lección del Binomio de Newton (Potenciación) aprendiste a desarrollar expansiones completas como $(a+b)^5$. Pero, ¿qué pasa cuando solo te piden **un término específico** sin desarrollar todo? Aquí aprenderás el atajo.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula del "Término General" ($T_{k+1}$) para el binomio.
- Cómo encontrar cualquier término sin expandir todo.
- A calcular coeficientes específicos de una expansión.
- Cómo identificar el término central o un término con exponente dado.

---

## 🔍 La Fórmula del Término General

Cuando haces una expansión binomial, cada uno de los términos tiene la forma:

$$
T_{k+1} = \binom{n}{k} a^{n-k} b^k
$$

Donde:
- $n$ = Exponente del binomio.
- $k$ = Posición del término **menos 1** (porque empezamos en $k=0$).
- $a$ = Primer término del binomio.
- $b$ = Segundo término del binomio.

> **Regla Clave:** Para el término $k$-ésimo, el valor de $k$ es uno menos que la posición. Es decir, para el 4º término usas $k=3$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar el 4º término
Encuentra el **cuarto término** de la expansión de $(x + 2y)^{10}$.

**Paso 1: Identificar los datos.**
- $n = 10$
- $a = x$
- $b = 2y$
- Posición buscada: 4. Por lo tanto, $k = 3$.

**Paso 2: Sustituir en la fórmula.**

$$
T_4 = \binom{10}{3} (x)^{10-3} (2y)^3
$$

**Paso 3: Calcular cada parte.**

1. Coeficiente binomial:
$$
\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120
$$

2. Potencia de $a$:
$$
x^7
$$

3. Potencia de $b$:
$$
(2y)^3 = 8y^3
$$

**Paso 4: Multiplicar todo.**

$$
T_4 = 120 \cdot x^7 \cdot 8y^3 = 960x^7y^3
$$

**Resultado:**
$$
\boxed{960x^7y^3}
$$

---

### Ejemplo 2: Término con exponente específico
Encuentra el término que contiene $x^4$ en la expansión de $(x + 2)^6$.

**Paso 1: Plantear qué necesitamos.**
El término general es:
$$
T_{k+1} = \binom{6}{k} x^{6-k} 2^k
$$

Queremos que el exponente de $x$ sea 4:
$$
6 - k = 4 \implies k = 2
$$

**Paso 2: Sustituir $k=2$.**

$$
T_3 = \binom{6}{2} x^4 (2)^2
$$

**Paso 3: Calcular.**

$$
T_3 = 15 \cdot x^4 \cdot 4 = 60x^4
$$

**Resultado:**
$$
\boxed{60x^4}
$$

---

### Ejemplo 3: Coeficiente del 5º término
Halla el coeficiente del 5º término de $(a + b)^8$.

**Paso 1:** 5º término implica $k = 4$.

**Paso 2:** El coeficiente es simplemente $\binom{8}{4}$.

$$
\binom{8}{4} = \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = 70
$$

**Resultado:**
$$
\boxed{70}
$$

---

### Ejemplo 4: Término central
Halla el término central de $(x + y)^6$.

**Razonamiento:**
Si $n=6$, hay 7 términos. El central es el 4º (posición $\frac{7+1}{2} = 4$, para $n$ par).
$k = 3$.

$$
T_4 = \binom{6}{3} x^{6-3} y^3 = 20x^3y^3
$$

**Resultado:**
$$
\boxed{20x^3y^3}
$$

---

### Ejemplo 5: Binomio con resta
Encuentra el 3er término de $(2x - 3)^5$.

**Paso 1:** $k = 2$, $a = 2x$, $b = 3$.
> Nota: Como es una resta, aplicamos la regla de signos alternados. El término $k$-ésimo tiene signo $(-1)^k$.

**Paso 2:**

$$
T_3 = \binom{5}{2} (2x)^{5-2} (-3)^2
$$

$$
T_3 = 10 \cdot (2x)^3 \cdot 9
$$

$$
T_3 = 10 \cdot 8x^3 \cdot 9 = 720x^3
$$

**Resultado:**
$$
\boxed{720x^3}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el 3er término de $(a + b)^7$.

<details>
<summary>Ver solución</summary>

$k=2$. $T_3 = \binom{7}{2} a^5 b^2 = 21a^5b^2$.
**Resultado:** $\boxed{21a^5b^2}$

</details>

### Ejercicio 2
Halla el coeficiente del 4º término de $(x + 1)^9$.

<details>
<summary>Ver solución</summary>

$k=3$. Coeficiente = $\binom{9}{3} = 84$.
**Resultado:** $\boxed{84}$

</details>

### Ejercicio 3
Encuentra el término que contiene $y^5$ en $(x + y)^8$.

<details>
<summary>Ver solución</summary>

$k = 5$. $T_6 = \binom{8}{5} x^3 y^5 = 56x^3y^5$.
**Resultado:** $\boxed{56x^3y^5}$

</details>

### Ejercicio 4
Encuentra el 5º término de $(2 + x)^6$.

<details>
<summary>Ver solución</summary>

$k=4$. $T_5 = \binom{6}{4} (2)^{2} x^4 = 15 \cdot 4 \cdot x^4 = 60x^4$.
**Resultado:** $\boxed{60x^4}$

</details>

### Ejercicio 5
Halla el término central de $(a + b)^4$.

<details>
<summary>Ver solución</summary>

5 términos, el central es el 3º ($k=2$).
$T_3 = \binom{4}{2} a^2 b^2 = 6a^2b^2$.
**Resultado:** $\boxed{6a^2b^2}$

</details>

### Ejercicio 6
Encuentra el 2do término de $(x - 2)^5$.

<details>
<summary>Ver solución</summary>

$k=1$. Signo = $(-1)^1 = -$.
$T_2 = -\binom{5}{1} x^4 (2)^1 = -5 \cdot 2 \cdot x^4 = -10x^4$.
**Resultado:** $\boxed{-10x^4}$

</details>

### Ejercicio 7
Halla el término que contiene $x^3$ en $(1 + x)^7$.

<details>
<summary>Ver solución</summary>

$k = 3$. $T_4 = \binom{7}{3} (1)^4 x^3 = 35x^3$.
**Resultado:** $\boxed{35x^3}$

</details>

### Ejercicio 8
Encuentra el 6º término de $(a + b)^{10}$.

<details>
<summary>Ver solución</summary>

$k=5$. $T_6 = \binom{10}{5} a^5 b^5 = 252a^5b^5$.
**Resultado:** $\boxed{252a^5b^5}$

</details>

### Ejercicio 9
Halla el coeficiente del término $x^2y^4$ en $(x + y)^6$.

<details>
<summary>Ver solución</summary>

Exponente de $y$ es 4, entonces $k=4$.
Coeficiente = $\binom{6}{4} = 15$.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 10
Encuentra el 4º término de $(3x - 1)^4$.

<details>
<summary>Ver solución</summary>

$k=3$. Signo = $(-1)^3 = -$.
$T_4 = -\binom{4}{3} (3x)^1 (1)^3 = -4 \cdot 3x \cdot 1 = -12x$.
**Resultado:** $\boxed{-12x}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula |
|:--- |:--- |
| **Término General** | $T_{k+1} = \binom{n}{k} a^{n-k} b^k$ |
| **Posición** | Para el término número $m$, usa $k = m - 1$. |
| **Signo (restas)** | El signo del término $k$ es $(-1)^k$. |

> **Consejo:** Esta fórmula es un "atajo" que evita desarrollar todo el binomio. Úsala cuando te pidan un término específico o un coeficiente.

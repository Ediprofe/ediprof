# **Suma y Diferencia de Potencias Impares**

Ya sabes cómo factorizar diferencias de cuadrados ($x^2 - y^2$) y sumas o diferencias de cubos ($x^3 \pm y^3$). ¿Qué pasa si el exponente es 5, 7 o cualquier otro número impar? Hoy aprenderás que estas expresiones siguen un **patrón muy elegante** que te permitirá factorizarlas fácilmente, sin importar qué tan grande sea el exponente.

---

## 🎯 ¿Qué vas a aprender?

- A identificar cuándo aplicar este caso (potencias iguales impares).
- A construir el segundo factor "bajando y subiendo" exponentes.
- A manejar correctamente los signos en sumas y diferencias.
- A aplicar la fórmula general para cualquier potencia impar $n$.

---

## 🔍 El Patrón: De lo conocido a lo nuevo

Recuerda cómo factorizamos una diferencia de cubos ($n=3$):

$$
x^3 - y^3 = (x - y)(x^2 + xy + y^2)
$$

Observa el segundo paréntesis (el factor largo):
1.  Empieza con $x^2$ (uno menos que el original).
2.  La $x$ baja: $x^2 \to x^1 \to \text{desaparece}$.
3.  La $y$ sube: $\text{no está} \to y^1 \to y^2$.
4.  Todos los signos son positivos.

**¡Para potencias mayores ($n=5, 7, \dots$) funciona exactamente igual!**

---

## ⚡ Caso 1: Diferencia de Potencias Impares ($a^n - b^n$)

Cuando tienes una resta, el patrón de signos es el más fácil: **todos son positivos**.

### La Fórmula

$$
\boxed{a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + \dots + b^{n-1})}
$$

**Cómo construirla paso a paso:**
1.  **Primer factor (la raíz):** Es la resta de las bases $(a - b)$.
2.  **Segundo factor (el polinomio):**
    *   El primer término empieza con exponente $n-1$.
    *   Vas **bajando** el exponente de $a$ y **subiendo** el de $b$.
    *   **Todos** los signos son positivos ($+$).

### Ejemplo 1: Diferencia de quintas

Factoriza la expresión:

$$
x^5 - 32
$$

**Razonamiento:**

1.  Verificamos que sean potencias quintas:

$$
x^5 - 2^5
$$

2.  Escribimos el primer factor con la resta de las bases:

$$
(x - 2)
$$

3.  Construimos el segundo factor. Como era $x^5$, empezamos con $x^4$.
    *   $x$ baja: $x^4 \to x^3 \to x^2 \to x \to 1$
    *   $2$ sube: $1 \to 2 \to 2^2 \to 2^3 \to 2^4$

    Escribámoslo término a término:

$$
x^4 + x^3(2) + x^2(2^2) + x(2^3) + 2^4
$$

4.  Simplificamos las potencias de los números:

$$
x^4 + 2x^3 + 4x^2 + 8x + 16
$$

**Resultado:**

$$
\boxed{(x - 2)(x^4 + 2x^3 + 4x^2 + 8x + 16)}
$$

---

## ⚡ Caso 2: Suma de Potencias Impares ($a^n + b^n$)

Cuando tienes una suma, el patrón es casi idéntico, pero los signos del segundo factor **se alternan**.

### La Fórmula

$$
\boxed{a^n + b^n = (a + b)(a^{n-1} - a^{n-2}b + \dots + b^{n-1})}
$$

**Regla de signos para la SUMA:**
*   Empiezas con positivo (+).
*   Luego negativo (-).
*   Luego positivo (+).
*   Y así sucesivamente... (**+ , - , + , - , ...**)

### Ejemplo 2: Suma de quintas

Factoriza la expresión:

$$
m^5 + 243
$$

**Razonamiento:**

1.  Identificamos las potencias. Sabemos que $3^5 = 243$:

$$
m^5 + 3^5
$$

2.  Primer factor (suma de bases):

$$
(m + 3)
$$

3.  Segundo factor (alternando signos):
    *   Empieza con $m^4$.
    *   Signos: $+ - + - +$

    Construyamos:

$$
m^4 - m^3(3) + m^2(3^2) - m(3^3) + 3^4
$$

4.  Simplificamos:

$$
m^4 - 3m^3 + 9m^2 - 27m + 81
$$

**Resultado:**

$$
\boxed{(m + 3)(m^4 - 3m^3 + 9m^2 - 27m + 81)}
$$

---

## ⚙️ Ejemplos Resueltos Complejos

### Ejemplo 3: Con coeficientes en ambos términos

Factoriza:

$$
32x^5 + 1
$$

**Datos:**
*   $\sqrt[5]{32x^5} = 2x$
*   $\sqrt[5]{1} = 1$

**Razonamiento:**

1.  Primer factor:

$$
(2x + 1)
$$

2.  Segundo factor (alternando signos).
    *   Cuidado: el primer término $(2x)$ debe elevarse completo entre paréntesis.

$$
(2x)^4 - (2x)^3(1) + (2x)^2(1^2) - (2x)(1^3) + 1^4
$$

3.  Desarrollamos las potencias:
    *   $(2x)^4 = 16x^4$
    *   $(2x)^3 = 8x^3$
    *   $(2x)^2 = 4x^2$

$$
16x^4 - 8x^3 + 4x^2 - 2x + 1
$$

**Resultado:**

$$
\boxed{(2x + 1)(16x^4 - 8x^3 + 4x^2 - 2x + 1)}
$$

### Ejemplo 4: Séptima potencia (n=7)

Factoriza:

$$
x^7 - y^7
$$

**Razonamiento:**

1.  Primer factor (es resta, así que resta de bases):

$$
(x - y)
$$

2.  Segundo factor (es resta, así que **todos positivos**).
    *   Empezamos con exponente 6 ($7-1$).

$$
x^6 + x^5y + x^4y^2 + x^3y^3 + x^2y^4 + xy^5 + y^6
$$

**Resultado:**

$$
\boxed{(x - y)(x^6 + x^5y + x^4y^2 + x^3y^3 + x^2y^4 + xy^5 + y^6)}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Factoriza: $x^5 - 1$

<details>
<summary>Ver solución</summary>

**Datos:** Diferencia de quintas ($1 = 1^5$).

**Razonamiento:**
El primer factor es $(x-1)$. El segundo tiene todos los signos positivos, empezando en $x^4$.

$$
(x - 1)(x^4 + x^3(1) + x^2(1)^2 + x(1)^3 + 1^4)
$$

**Resultado:**

$$
\boxed{(x - 1)(x^4 + x^3 + x^2 + x + 1)}
$$

</details>

### Ejercicio 2
Factoriza: $a^5 + 1$

<details>
<summary>Ver solución</summary>

**Datos:** Suma de quintas. Signos alternados.

**Razonamiento:**

$$
(a + 1)(a^4 - a^3 + a^2 - a + 1)
$$

**Resultado:**

$$
\boxed{(a + 1)(a^4 - a^3 + a^2 - a + 1)}
$$

</details>

### Ejercicio 3
Factoriza: $x^7 + 1$

<details>
<summary>Ver solución</summary>

**Datos:** Suma de séptimas ($n=7$). Signos alternados.

**Razonamiento:**
Empezamos con $x^6$.

$$
(x + 1)(x^6 - x^5 + x^4 - x^3 + x^2 - x + 1)
$$

**Resultado:**

$$
\boxed{(x + 1)(x^6 - x^5 + x^4 - x^3 + x^2 - x + 1)}
$$

</details>

### Ejercicio 4
Factoriza: $32 - b^5$

<details>
<summary>Ver solución</summary>

**Datos:** $32 = 2^5$.

**Razonamiento:**
Primer factor $(2 - b)$. Segundo factor con todos positivos.

$$
(2 - b)(2^4 + 2^3b + 2^2b^2 + 2b^3 + b^4)
$$

Simplificamos las potencias de 2:

**Resultado:**

$$
\boxed{(2 - b)(16 + 8b + 4b^2 + 2b^3 + b^4)}
$$

</details>

### Ejercicio 5
Factoriza: $x^5 + 32y^5$

<details>
<summary>Ver solución</summary>

**Datos:** $32y^5 = (2y)^5$.

**Razonamiento:**
Primer factor $(x + 2y)$. Segundo factor alterna signos.

$$
x^4 - x^3(2y) + x^2(2y)^2 - x(2y)^3 + (2y)^4
$$

**Resultado:**

$$
\boxed{(x + 2y)(x^4 - 2x^3y + 4x^2y^2 - 8xy^3 + 16y^4)}
$$

</details>

### Ejercicio 6
Factoriza: $243x^5 - 1$

<details>
<summary>Ver solución</summary>

**Datos:** $243x^5 = (3x)^5$.

**Razonamiento:**
Primer factor $(3x - 1)$. Segundo factor todo positivo.

$$
(3x)^4 + (3x)^3 + (3x)^2 + (3x) + 1
$$

**Resultado:**

$$
\boxed{(3x - 1)(81x^4 + 27x^3 + 9x^2 + 3x + 1)}
$$

</details>

### Ejercicio 7
Factoriza: $m^7 - n^7$

<details>
<summary>Ver solución</summary>

**Datos:** Diferencia de séptimas.

**Razonamiento:**
Primer factor $(m-n)$. Segundo factor positivo, bajando de $m^6$ a $m^0$.

**Resultado:**

$$
\boxed{(m - n)(m^6 + m^5n + m^4n^2 + m^3n^3 + m^2n^4 + mn^5 + n^6)}
$$

</details>

### Ejercicio 8
Factoriza: $a^5b^5 + 32$

<details>
<summary>Ver solución</summary>

**Datos:** $(ab)^5 + 2^5$.

**Razonamiento:**

$$
(ab + 2)((ab)^4 - (ab)^3(2) + (ab)^2(4) - (ab)(8) + 16)
$$

**Resultado:**

$$
\boxed{(ab + 2)(a^4b^4 - 2a^3b^3 + 4a^2b^2 - 8ab + 16)}
$$

</details>

### Ejercicio 9
Factoriza: $x^{10} + 1$ (Nota: $x^{10} = (x^2)^5$)

<details>
<summary>Ver solución</summary>

**Datos:** Podemos verlo como una suma de quintas de $x^2$.

**Razonamiento:**
$(x^2)^5 + 1^5$. Bases son $x^2$ y $1$.

Primer factor: $(x^2 + 1)$.
Segundo factor (alternando):

$$
(x^2)^4 - (x^2)^3 + (x^2)^2 - x^2 + 1
$$

**Resultado:**

$$
\boxed{(x^2 + 1)(x^8 - x^6 + x^4 - x^2 + 1)}
$$

</details>

### Ejercicio 10
Factoriza: $2a^5 + 64$

<details>
<summary>Ver solución</summary>

**Datos:** Primero hay un **Factor Común** 2.

**Razonamiento:**

1.  Saca el factor común:

$$
2(a^5 + 32)
$$

2.  Factoriza la suma de quintas dentro:

$$
2(a + 2)(a^4 - 2a^3 + 4a^2 - 8a + 16)
$$

**Resultado:**

$$
\boxed{2(a + 2)(a^4 - 2a^3 + 4a^2 - 8a + 16)}
$$

</details>

---

## 🔑 Resumen

Para factorizar $a^n \pm b^n$ con $n$ impar:

| Caso | Fórmula básica | Signos 2do Factor |
| :--- | :--- | :--- |
| **Resta (-)** | $(a-b)(\dots)$ | **Todos +** $(+,+,+, \dots)$ |
| **Suma (+)** | $(a+b)(\dots)$ | **Alternados** $(+,-,+,-, \dots)$ |

> **Truco final:** El segundo factor siempre tiene exactamente **$n$ términos**. Si factorizas potencia 5, el paréntesis largo tendrá 5 términos.

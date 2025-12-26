# **Suma y Diferencia de Potencias Impares**

Este caso es una generalización de la suma y diferencia de cubos. Aplica cuando tienes dos términos elevados a la misma potencia impar (5, 7, 9, etc.).

---

## 🎯 ¿Qué vas a aprender?

- A identificar potencias impares iguales.
- A aplicar la fórmula general de diferencia de potencias.
- A aplicar la fórmula general de suma de potencias impares.
- Por qué la suma de potencias pares no se factoriza.

---

## 🔍 Potencias impares comunes

| Potencia | Valores |
| :---: | :---: |
| $n = 5$ | $1^5 = 1$, $2^5 = 32$, $3^5 = 243$ |
| $n = 7$ | $1^7 = 1$, $2^7 = 128$, $3^7 = 2187$ |

---

## 📐 Las Fórmulas

**Diferencia de potencias** (funciona para cualquier $n$):

$$
\boxed{a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + a^{n-3}b^2 + \cdots + b^{n-1})}
$$

**Suma de potencias impares** (solo cuando $n$ es impar):

$$
\boxed{a^n + b^n = (a + b)(a^{n-1} - a^{n-2}b + a^{n-3}b^2 - \cdots + b^{n-1})}
$$

**Cómo recordarlas:**
- El primer factor tiene el **mismo signo** que la expresión.
- En la diferencia, los signos del segundo factor son **todos positivos**.
- En la suma, los signos **alternan** (empezando con positivo).
- El segundo factor tiene **$n$ términos**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Diferencia de quintas potencias

Factoriza: $x^5 - 32$

**Datos:**
- $x^5 = (x)^5$
- $32 = (2)^5$

**Razonamiento:**

1. Primer factor: 

$$
(x - 2)
$$

2. Segundo factor: 5 términos con signos positivos.

3.
$$
x^4 + x^3 \cdot 2 + x^2 \cdot 4 + x \cdot 8 + 16
$$

**Resultado:** $\boxed{(x - 2)(x^4 + 2x^3 + 4x^2 + 8x + 16)}$

---

### Ejemplo 2: Suma de quintas potencias

Factoriza: $x^5 + 32$

**Datos:**
- $x^5 = (x)^5$
- $32 = (2)^5$

**Razonamiento:**

1. Primer factor: 

$$
(x + 2)
$$

2. Segundo factor: 5 términos con signos alternados.

3.
$$
x^4 - 2x^3 + 4x^2 - 8x + 16
$$

**Resultado:** $\boxed{(x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)}$

---

### Ejemplo 3: Diferencia con coeficientes

Factoriza: $32m^5 - 243$

**Datos:**
- $32m^5 = (2m)^5$
- $243 = (3)^5$

**Razonamiento:**

1. Primer factor: 

$$
(2m - 3)
$$

2. Segundo factor: 

$$
(2m)^4 + (2m)^3(3) + (2m)^2(9) + (2m)(27) + 81
$$

3. Simplificamos: 

$$
16m^4 + 24m^3 + 36m^2 + 54m + 81
$$

**Resultado:** $\boxed{(2m - 3)(16m^4 + 24m^3 + 36m^2 + 54m + 81)}$

---

### Ejemplo 4: Séptimas potencias

Factoriza: $x^7 - y^7$

**Datos:**
- Ambos términos a la séptima potencia.

**Razonamiento:**

1. Primer factor: 

$$
(x - y)
$$

2. Segundo factor: 7 términos con signos positivos.

**Resultado:** $\boxed{(x - y)(x^6 + x^5y + x^4y^2 + x^3y^3 + x^2y^4 + xy^5 + y^6)}$

---

### Ejemplo 5: Con factor común

Factoriza: $2x^5 + 64$

**Datos:**
- Factor común 2.

**Razonamiento:**

1. Sacamos el 2: 

$$
2(x^5 + 32)
$$

2. Adentro es suma de quintas: 

$$
2(x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)
$$

**Resultado:** $\boxed{2(x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Factoriza: $x^5 - 1$

<details>
<summary>Ver solución</summary>

**Datos:** $1 = 1^5$
**Razonamiento:** 

$$
(x - 1)(x^4 + x^3 + x^2 + x + 1)
$$

**Resultado:** $\boxed{(x - 1)(x^4 + x^3 + x^2 + x + 1)}$

</details>

### Ejercicio 2
Factoriza: $a^5 + 1$

<details>
<summary>Ver solución</summary>

**Datos:** $1 = 1^5$
**Razonamiento:** 

$$
(a + 1)(a^4 - a^3 + a^2 - a + 1)
$$

**Resultado:** $\boxed{(a + 1)(a^4 - a^3 + a^2 - a + 1)}$

</details>

### Ejercicio 3
Factoriza: $a^5 - 243$

<details>
<summary>Ver solución</summary>

**Datos:** $243 = 3^5$
**Razonamiento:** 

$$
(a - 3)(a^4 + 3a^3 + 9a^2 + 27a + 81)
$$

**Resultado:** $\boxed{(a - 3)(a^4 + 3a^3 + 9a^2 + 27a + 81)}$

</details>

### Ejercicio 4
Factoriza: $a^5 + 32$

<details>
<summary>Ver solución</summary>

**Datos:** $32 = 2^5$
**Razonamiento:** 

$$
(a + 2)(a^4 - 2a^3 + 4a^2 - 8a + 16)
$$

**Resultado:** $\boxed{(a + 2)(a^4 - 2a^3 + 4a^2 - 8a + 16)}$

</details>

### Ejercicio 5
Factoriza: $32x^5 - 1$

<details>
<summary>Ver solución</summary>

**Datos:** $32x^5 = (2x)^5$
**Razonamiento:** 

$$
(2x - 1)(16x^4 + 8x^3 + 4x^2 + 2x + 1)
$$

**Resultado:** $\boxed{(2x - 1)(16x^4 + 8x^3 + 4x^2 + 2x + 1)}$

</details>

### Ejercicio 6
Factoriza: $243m^5 + 32n^5$

<details>
<summary>Ver solución</summary>

**Datos:** $(3m)^5$ y $(2n)^5$
**Razonamiento:** 

$$
(3m + 2n)(81m^4 - 54m^3n + 36m^2n^2 - 24mn^3 + 16n^4)
$$

**Resultado:** $\boxed{(3m + 2n)(81m^4 - 54m^3n + 36m^2n^2 - 24mn^3 + 16n^4)}$

</details>

### Ejercicio 7
Factoriza: $x^7 + y^7$

<details>
<summary>Ver solución</summary>

**Datos:** Potencia 7 (impar).
**Razonamiento:** 

$$
(x + y)(x^6 - x^5y + x^4y^2 - x^3y^3 + x^2y^4 - xy^5 + y^6)
$$

**Resultado:** $\boxed{(x + y)(x^6 - x^5y + x^4y^2 - x^3y^3 + x^2y^4 - xy^5 + y^6)}$

</details>

### Ejercicio 8
Factoriza: $x^6 - 1$ (usar diferencia de cuadrados primero)

<details>
<summary>Ver solución</summary>

**Datos:** $x^6 - 1 = (x^3)^2 - 1^2$
**Razonamiento:** 

$$
(x^3 + 1)(x^3 - 1)
$$

Luego cada uno es suma/diferencia de cubos.

**Resultado:** $\boxed{(x + 1)(x^2 - x + 1)(x - 1)(x^2 + x + 1)}$

</details>

### Ejercicio 9
Factoriza: $2x^5 - 2$

<details>
<summary>Ver solución</summary>

**Datos:** Factor común 2.
**Razonamiento:** 

$$
2(x^5 - 1) = 2(x - 1)(x^4 + x^3 + x^2 + x + 1)
$$

**Resultado:** $\boxed{2(x - 1)(x^4 + x^3 + x^2 + x + 1)}$

</details>

### Ejercicio 10
Factoriza: $5a^7 + 5$

<details>
<summary>Ver solución</summary>

**Datos:** Factor común 5.
**Razonamiento:** 

$$
5(a^7 + 1) = 5(a + 1)(a^6 - a^5 + a^4 - a^3 + a^2 - a + 1)
$$

**Resultado:** $\boxed{5(a + 1)(a^6 - a^5 + a^4 - a^3 + a^2 - a + 1)}$

</details>

---

## 🔑 Resumen

| Caso | Fórmula | Signos del 2do factor |
| :--- | :--- | :--- |
| **Diferencia** $a^n - b^n$ | $(a - b)(\text{n términos})$ | Todos positivos |
| **Suma** $a^n + b^n$ (n impar) | $(a + b)(\text{n términos})$ | Alternados (+, -, +, ...) |

> La suma de potencias pares ($a^4 + b^4$, $a^6 + b^6$, etc.) no se puede factorizar con esta fórmula.

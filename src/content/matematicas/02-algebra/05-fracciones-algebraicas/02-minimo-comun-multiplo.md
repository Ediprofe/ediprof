# 🔢 Mínimo Común Múltiplo (MCM)

En esta lección aprenderemos a encontrar el mínimo común múltiplo de expresiones algebraicas, una herramienta esencial para sumar y restar fracciones algebraicas con diferentes denominadores.

---

## 📖 Recordatorio: MCM de números

El **Mínimo Común Múltiplo (MCM)** de dos o más números es el menor número positivo que es múltiplo de todos ellos.

### Ejemplo con números

Encontrar el MCM de $12$ y $18$:

**Paso 1:** Descomponemos en factores primos:

$$
12 = 2^2 \times 3
$$

$$
18 = 2 \times 3^2
$$

**Paso 2:** Tomamos todos los factores con su **mayor exponente**:

- Factor $2$: el mayor exponente es $2$
- Factor $3$: el mayor exponente es $2$

$$
\text{MCM}(12, 18) = 2^2 \times 3^2 = 4 \times 9 = 36
$$

---

## 📖 Diferencia entre MCD y MCM

| Concepto | MCD | MCM |
|:---------|:---:|:---:|
| Significado | Mayor divisor común | Menor múltiplo común |
| Exponentes | Se toman los **menores** | Se toman los **mayores** |
| Variables | Solo las **comunes** | **Todas** las variables |

---

## 📖 MCM de monomios

Para encontrar el **MCM de monomios**, seguimos estas reglas:

### Regla para el MCM de monomios

1. **Coeficientes:** Encontrar el MCM de los coeficientes numéricos
2. **Variables:** Tomar **todas** las variables con su **mayor exponente**

---

### Ejemplo 1

Encontrar el MCM de $12x^3y^2$ y $18x^2y^4$.

**Solución:**

**Coeficientes:** $\text{MCM}(12, 18) = 36$

**Variables:**
- Variable $x$: mayor exponente es $3$ → tomamos $x^3$
- Variable $y$: mayor exponente es $4$ → tomamos $y^4$

$$
\boxed{\text{MCM}(12x^3y^2, 18x^2y^4) = 36x^3y^4}
$$

---

### Ejemplo 2

Encontrar el MCM de $8a^4b^3$ y $20a^2b^5$.

**Solución:**

**Coeficientes:** $\text{MCM}(8, 20) = 40$

**Variables:**
- Variable $a$: mayor exponente es $4$ → tomamos $a^4$
- Variable $b$: mayor exponente es $5$ → tomamos $b^5$

$$
\boxed{\text{MCM}(8a^4b^3, 20a^2b^5) = 40a^4b^5}
$$

---

### Ejemplo 3

Encontrar el MCM de $6xy^2$ y $9x^3z$.

**Solución:**

**Coeficientes:** $\text{MCM}(6, 9) = 18$

**Variables:**
- Variable $x$: mayor exponente es $3$ → tomamos $x^3$
- Variable $y$: solo aparece en el primero con exponente $2$ → tomamos $y^2$
- Variable $z$: solo aparece en el segundo con exponente $1$ → tomamos $z$

$$
\boxed{\text{MCM}(6xy^2, 9x^3z) = 18x^3y^2z}
$$

---

### Ejemplo 4

Encontrar el MCM de $15x^2yz^3$, $25xy^2z$ y $35xyz^2$.

**Solución:**

**Coeficientes:** $\text{MCM}(15, 25, 35) = 525$

**Variables:**
- Variable $x$: mayor exponente es $2$
- Variable $y$: mayor exponente es $2$
- Variable $z$: mayor exponente es $3$

$$
\boxed{\text{MCM}(15x^2yz^3, 25xy^2z, 35xyz^2) = 525x^2y^2z^3}
$$

---

## 📖 MCM de polinomios

Para encontrar el **MCM de polinomios**, debemos factorizar cada polinomio y luego tomar todos los factores con su mayor exponente.

### Regla para el MCM de polinomios

1. **Factorizar** completamente cada polinomio
2. **Tomar todos** los factores (comunes y no comunes)
3. **Usar** cada factor con su **mayor exponente**

---

### Ejemplo 5

Encontrar el MCM de $x^2 - 4$ y $x^2 + 4x + 4$.

**Paso 1:** Factorizamos cada polinomio:

$$
x^2 - 4 = (x + 2)(x - 2)
$$

$$
x^2 + 4x + 4 = (x + 2)^2
$$

**Paso 2:** Tomamos todos los factores con su mayor exponente:

- $(x + 2)$: mayor exponente es $2$ → tomamos $(x + 2)^2$
- $(x - 2)$: solo aparece en el primero → tomamos $(x - 2)$

$$
\boxed{\text{MCM}(x^2 - 4, x^2 + 4x + 4) = (x + 2)^2(x - 2)}
$$

---

### Ejemplo 6

Encontrar el MCM de $6x^2 + 12x$ y $9x^3 + 18x^2$.

**Paso 1:** Factorizamos cada polinomio:

$$
6x^2 + 12x = 6x(x + 2)
$$

$$
9x^3 + 18x^2 = 9x^2(x + 2)
$$

**Paso 2:** Tomamos todos los factores:

- Factor numérico: $\text{MCM}(6, 9) = 18$
- Factor $x$: mayor exponente es $2$ → tomamos $x^2$
- Factor $(x + 2)$: aparece en ambos con exponente $1$

$$
\boxed{\text{MCM}(6x^2 + 12x, 9x^3 + 18x^2) = 18x^2(x + 2)}
$$

---

### Ejemplo 7

Encontrar el MCM de $x^3 - x^2$ y $x^2 - 1$.

**Paso 1:** Factorizamos cada polinomio:

$$
x^3 - x^2 = x^2(x - 1)
$$

$$
x^2 - 1 = (x + 1)(x - 1)
$$

**Paso 2:** Tomamos todos los factores:

- Factor $x^2$: solo aparece en el primero
- Factor $(x - 1)$: aparece en ambos
- Factor $(x + 1)$: solo aparece en el segundo

$$
\boxed{\text{MCM}(x^3 - x^2, x^2 - 1) = x^2(x + 1)(x - 1)}
$$

---

### Ejemplo 8

Encontrar el MCM de $4x^2 - 16$ y $2x^2 - 8x + 8$.

**Paso 1:** Factorizamos cada polinomio:

$$
4x^2 - 16 = 4(x^2 - 4) = 4(x + 2)(x - 2)
$$

$$
2x^2 - 8x + 8 = 2(x^2 - 4x + 4) = 2(x - 2)^2
$$

**Paso 2:** Tomamos todos los factores con su mayor exponente:

- Factor numérico: $\text{MCM}(4, 2) = 4$
- Factor $(x + 2)$: solo en el primero
- Factor $(x - 2)$: mayor exponente es $2$

$$
\boxed{\text{MCM}(4x^2 - 16, 2x^2 - 8x + 8) = 4(x + 2)(x - 2)^2}
$$

---

## 📖 Aplicación: Denominador común

El MCM es fundamental para encontrar el **denominador común** cuando sumamos o restamos fracciones algebraicas.

### Ejemplo 9

Para sumar $\dfrac{1}{x+2} + \dfrac{1}{x-2}$, el denominador común será:

$$
\text{MCM}(x+2, x-2) = (x+2)(x-2)
$$

---

## 📋 Resumen comparativo

| Expresiones | MCD | MCM |
|:------------|:---:|:---:|
| $12x^3y^2$ y $18x^2y^4$ | $6x^2y^2$ | $36x^3y^4$ |
| $x^2 - 4$ y $(x + 2)^2$ | $(x + 2)$ | $(x + 2)^2(x - 2)$ |
| $6x(x + 2)$ y $9x^2(x + 2)$ | $3x(x + 2)$ | $18x^2(x + 2)$ |

---

## 📝 Ejercicios de práctica

### MCM de monomios

**Ejercicio 1:** Encuentra el MCM de $24a^3b^2$ y $36a^2b^4$.

<details>
<summary>Ver solución</summary>

**Coeficientes:** $\text{MCM}(24, 36) = 72$

**Variables:**
- $a$: mayor exponente es $3$
- $b$: mayor exponente es $4$

$$
\text{MCM} = 72a^3b^4
$$

</details>

---

**Ejercicio 2:** Encuentra el MCM de $10x^4y^3z$ y $15x^2y^5z^2$.

<details>
<summary>Ver solución</summary>

**Coeficientes:** $\text{MCM}(10, 15) = 30$

**Variables:**
- $x$: mayor exponente es $4$
- $y$: mayor exponente es $5$
- $z$: mayor exponente es $2$

$$
\text{MCM} = 30x^4y^5z^2
$$

</details>

---

### MCM de polinomios

**Ejercicio 3:** Encuentra el MCM de $x^2 - 9$ y $x^2 + 6x + 9$.

<details>
<summary>Ver solución</summary>

**Factorizamos:**

$$
x^2 - 9 = (x + 3)(x - 3)
$$

$$
x^2 + 6x + 9 = (x + 3)^2
$$

**Tomamos todos los factores con mayor exponente:**

$$
\text{MCM} = (x + 3)^2(x - 3)
$$

</details>

---

**Ejercicio 4:** Encuentra el MCM de $2x^2 + 6x$ y $4x^3 + 12x^2$.

<details>
<summary>Ver solución</summary>

**Factorizamos:**

$$
2x^2 + 6x = 2x(x + 3)
$$

$$
4x^3 + 12x^2 = 4x^2(x + 3)
$$

**Tomamos todos los factores:**
- Numérico: $\text{MCM}(2, 4) = 4$
- $x$: mayor exponente es $2$
- $(x + 3)$: exponente $1$

$$
\text{MCM} = 4x^2(x + 3)
$$

</details>

---

**Ejercicio 5:** Encuentra el MCM de $x^2 - 4x + 4$ y $x^2 - 4$.

<details>
<summary>Ver solución</summary>

**Factorizamos:**

$$
x^2 - 4x + 4 = (x - 2)^2
$$

$$
x^2 - 4 = (x + 2)(x - 2)
$$

**Tomamos todos los factores con mayor exponente:**

$$
\text{MCM} = (x + 2)(x - 2)^2
$$

</details>

---

**Ejercicio 6:** Encuentra el MCM de $18m^3n^2$, $24m^2n^4$ y $30m^4n$.

<details>
<summary>Ver solución</summary>

**Coeficientes:** $\text{MCM}(18, 24, 30) = 360$

**Variables:**
- $m$: mayor exponente es $4$
- $n$: mayor exponente es $4$

$$
\text{MCM} = 360m^4n^4
$$

</details>

---

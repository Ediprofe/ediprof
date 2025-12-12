# 🔢 Máximo Común Divisor (MCD)

En esta lección aprenderemos a encontrar el máximo común divisor de expresiones algebraicas, una herramienta fundamental para simplificar fracciones algebraicas.

---

## 📖 Recordatorio: MCD de números

El **Máximo Común Divisor (MCD)** de dos o más números es el mayor número que divide exactamente a todos ellos.

### Ejemplo con números

Encontrar el MCD de $12$ y $18$:

**Paso 1:** Descomponemos en factores primos:

$$
12 = 2^2 \times 3
$$

$$
18 = 2 \times 3^2
$$

**Paso 2:** Tomamos los factores comunes con su menor exponente:

- Factor $2$: el menor exponente es $1$
- Factor $3$: el menor exponente es $1$

$$
\text{MCD}(12, 18) = 2^1 \times 3^1 = 6
$$

---

## 📖 MCD de monomios

Para encontrar el **MCD de monomios**, seguimos un procedimiento similar:

### Regla para el MCD de monomios

1. **Coeficientes:** Encontrar el MCD de los coeficientes numéricos
2. **Variables:** Tomar las variables comunes con su **menor exponente**

---

### Ejemplo 1

Encontrar el MCD de $12x^3y^2$ y $18x^2y^4$.

**Solución:**

**Coeficientes:** $\text{MCD}(12, 18) = 6$

**Variables:**
- Variable $x$: menor exponente es $2$ → tomamos $x^2$
- Variable $y$: menor exponente es $2$ → tomamos $y^2$

$$
\boxed{\text{MCD}(12x^3y^2, 18x^2y^4) = 6x^2y^2}
$$

---

### Ejemplo 2

Encontrar el MCD de $8a^4b^3$ y $20a^2b^5$.

**Solución:**

**Coeficientes:** $\text{MCD}(8, 20) = 4$

**Variables:**
- Variable $a$: menor exponente es $2$ → tomamos $a^2$
- Variable $b$: menor exponente es $3$ → tomamos $b^3$

$$
\boxed{\text{MCD}(8a^4b^3, 20a^2b^5) = 4a^2b^3}
$$

---

### Ejemplo 3

Encontrar el MCD de $15x^2yz^3$, $25xy^2z$ y $35xyz^2$.

**Solución:**

**Coeficientes:** $\text{MCD}(15, 25, 35) = 5$

**Variables:**
- Variable $x$: menor exponente es $1$ → tomamos $x$
- Variable $y$: menor exponente es $1$ → tomamos $y$
- Variable $z$: menor exponente es $1$ → tomamos $z$

$$
\boxed{\text{MCD}(15x^2yz^3, 25xy^2z, 35xyz^2) = 5xyz}
$$

---

## 📖 MCD de polinomios

Para encontrar el **MCD de polinomios**, debemos factorizar cada polinomio y luego identificar los factores comunes.

### Regla para el MCD de polinomios

1. **Factorizar** completamente cada polinomio
2. **Identificar** los factores comunes
3. **Tomar** cada factor común con su **menor exponente**

---

### Ejemplo 4

Encontrar el MCD de $x^2 - 4$ y $x^2 + 4x + 4$.

**Paso 1:** Factorizamos cada polinomio:

$$
x^2 - 4 = (x + 2)(x - 2)
$$

$$
x^2 + 4x + 4 = (x + 2)^2
$$

**Paso 2:** Identificamos los factores comunes:

El único factor común es $(x + 2)$.

**Paso 3:** Tomamos el menor exponente:

- $(x + 2)$: aparece con exponente $1$ en el primero y exponente $2$ en el segundo → tomamos $(x + 2)^1$

$$
\boxed{\text{MCD}(x^2 - 4, x^2 + 4x + 4) = (x + 2)}
$$

---

### Ejemplo 5

Encontrar el MCD de $6x^2 + 12x$ y $9x^3 + 18x^2$.

**Paso 1:** Factorizamos cada polinomio:

$$
6x^2 + 12x = 6x(x + 2)
$$

$$
9x^3 + 18x^2 = 9x^2(x + 2)
$$

**Paso 2:** Identificamos los factores comunes:

- Factor numérico: $\text{MCD}(6, 9) = 3$
- Factor $x$: menor exponente es $1$
- Factor $(x + 2)$: aparece en ambos

$$
\boxed{\text{MCD}(6x^2 + 12x, 9x^3 + 18x^2) = 3x(x + 2)}
$$

---

### Ejemplo 6

Encontrar el MCD de $x^3 - x^2$ y $x^2 - 1$.

**Paso 1:** Factorizamos cada polinomio:

$$
x^3 - x^2 = x^2(x - 1)
$$

$$
x^2 - 1 = (x + 1)(x - 1)
$$

**Paso 2:** El único factor común es $(x - 1)$:

$$
\boxed{\text{MCD}(x^3 - x^2, x^2 - 1) = (x - 1)}
$$

---

### Ejemplo 7

Encontrar el MCD de $4x^2 - 16$ y $2x^2 - 8x + 8$.

**Paso 1:** Factorizamos cada polinomio:

$$
4x^2 - 16 = 4(x^2 - 4) = 4(x + 2)(x - 2)
$$

$$
2x^2 - 8x + 8 = 2(x^2 - 4x + 4) = 2(x - 2)^2
$$

**Paso 2:** Identificamos los factores comunes:

- Factor numérico: $\text{MCD}(4, 2) = 2$
- Factor $(x - 2)$: menor exponente es $1$

$$
\boxed{\text{MCD}(4x^2 - 16, 2x^2 - 8x + 8) = 2(x - 2)}
$$

---

## 📖 Casos especiales

### Cuando no hay factores comunes

Si dos expresiones no tienen factores comunes (excepto $1$), decimos que su MCD es $1$ y que son **relativamente primos** o **coprimos**.

### Ejemplo 8

Encontrar el MCD de $x^2 + 1$ y $x - 1$.

El polinomio $x^2 + 1$ no se puede factorizar (en los números reales) y no comparte factores con $(x - 1)$.

$$
\boxed{\text{MCD}(x^2 + 1, x - 1) = 1}
$$

---

## 📋 Resumen

| Expresiones | MCD |
|:------------|:---:|
| $12x^3y^2$ y $18x^2y^4$ | $6x^2y^2$ |
| $x^2 - 4$ y $(x + 2)^2$ | $(x + 2)$ |
| $6x(x + 2)$ y $9x^2(x + 2)$ | $3x(x + 2)$ |

---

## 📝 Ejercicios de práctica

### MCD de monomios

**Ejercicio 1:** Encuentra el MCD de $24a^3b^2$ y $36a^2b^4$.

<details>
<summary>Ver solución</summary>

**Coeficientes:** $\text{MCD}(24, 36) = 12$

**Variables:**
- $a$: menor exponente es $2$
- $b$: menor exponente es $2$

$$
\text{MCD} = 12a^2b^2
$$

</details>

---

**Ejercicio 2:** Encuentra el MCD de $10x^4y^3z$ y $15x^2y^5z^2$.

<details>
<summary>Ver solución</summary>

**Coeficientes:** $\text{MCD}(10, 15) = 5$

**Variables:**
- $x$: menor exponente es $2$
- $y$: menor exponente es $3$
- $z$: menor exponente es $1$

$$
\text{MCD} = 5x^2y^3z
$$

</details>

---

### MCD de polinomios

**Ejercicio 3:** Encuentra el MCD de $x^2 - 9$ y $x^2 + 6x + 9$.

<details>
<summary>Ver solución</summary>

**Factorizamos:**

$$
x^2 - 9 = (x + 3)(x - 3)
$$

$$
x^2 + 6x + 9 = (x + 3)^2
$$

**Factor común:** $(x + 3)$ con menor exponente $1$

$$
\text{MCD} = (x + 3)
$$

</details>

---

**Ejercicio 4:** Encuentra el MCD de $2x^2 + 6x$ y $4x^3 + 12x^2$.

<details>
<summary>Ver solución</summary>

**Factorizamos:**

$$
2x^2 + 6x = 2x(x + 3)
$$

$$
4x^3 + 12x^2 = 4x^2(x + 3)
$$

**Factores comunes:**
- Numérico: $\text{MCD}(2, 4) = 2$
- $x$: menor exponente es $1$
- $(x + 3)$: aparece en ambos

$$
\text{MCD} = 2x(x + 3)
$$

</details>

---

**Ejercicio 5:** Encuentra el MCD de $x^2 - 4x + 4$ y $x^2 - 4$.

<details>
<summary>Ver solución</summary>

**Factorizamos:**

$$
x^2 - 4x + 4 = (x - 2)^2
$$

$$
x^2 - 4 = (x + 2)(x - 2)
$$

**Factor común:** $(x - 2)$ con menor exponente $1$

$$
\text{MCD} = (x - 2)
$$

</details>

---

**Ejercicio 6:** Encuentra el MCD de $18m^3n^2$, $24m^2n^4$ y $30m^4n$.

<details>
<summary>Ver solución</summary>

**Coeficientes:** $\text{MCD}(18, 24, 30) = 6$

**Variables:**
- $m$: menor exponente es $2$
- $n$: menor exponente es $1$

$$
\text{MCD} = 6m^2n
$$

</details>

---

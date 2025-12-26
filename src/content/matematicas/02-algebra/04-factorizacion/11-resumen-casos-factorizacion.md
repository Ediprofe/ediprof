# **Resumen de Casos de Factorización**

Esta lección es un repaso general de todos los métodos de factorización que hemos estudiado. Es útil para identificar rápidamente qué método aplicar en cada situación.

---

## 🎯 ¿Qué vas a aprender?

- A identificar el tipo de expresión que tienes.
- A elegir el método de factorización correcto.
- El orden lógico para factorizar cualquier expresión.
- A verificar tus resultados multiplicando.

---

## 📐 Tabla de Fórmulas

| Caso | Forma | Factorización |
| :--- | :--- | :--- |
| **Factor Común** | $ab + ac$ | $a(b + c)$ |
| **Agrupación** | $ax + ay + bx + by$ | $(a + b)(x + y)$ |
| **Diferencia de Cuadrados** | $a^2 - b^2$ | $(a + b)(a - b)$ |
| **TCP (+)** | $a^2 + 2ab + b^2$ | $(a + b)^2$ |
| **TCP (-)** | $a^2 - 2ab + b^2$ | $(a - b)^2$ |
| **Trinomio Simple** | $x^2 + bx + c$ | $(x + m)(x + n)$ |
| **Trinomio General** | $ax^2 + bx + c$ | Por agrupación o tanteo |
| **Suma de Cubos** | $a^3 + b^3$ | $(a + b)(a^2 - ab + b^2)$ |
| **Diferencia de Cubos** | $a^3 - b^3$ | $(a - b)(a^2 + ab + b^2)$ |

---

## 🔍 Estrategia de Factorización

Sigue este orden cuando tengas que factorizar:

**Paso 1:** ¿Hay factor común? → Siempre es lo primero.

**Paso 2:** ¿Cuántos términos tiene?
- **2 términos:** Diferencia de cuadrados, suma o diferencia de cubos.
- **3 términos:** TCP, trinomio simple ($x^2 + bx + c$) o trinomio general ($ax^2 + bx + c$).
- **4 o más:** Agrupación.

**Paso 3:** ¿Se puede factorizar más?

**Paso 4:** Verifica multiplicando.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Factor común primero

Factoriza: $6x^3 - 12x^2 + 18x$

**Datos:**
- Todos los términos tienen factor común $6x$.

**Razonamiento:**

1. Sacamos $6x$: 

$$
6x(x^2 - 2x + 3)
$$

2. Verificamos si el trinomio se factoriza más: No es TCP ni tiene factores enteros.

**Resultado:** $\boxed{6x(x^2 - 2x + 3)}$

---

### Ejemplo 2: Diferencia de cuadrados iterada

Factoriza: $x^4 - 81$

**Datos:**
- Es diferencia de cuadrados: $(x^2)^2 - 9^2$.

**Razonamiento:**

1. Primera factorización: 

$$
(x^2 + 9)(x^2 - 9)
$$

2. El segundo factor es otra diferencia de cuadrados: 

$$
(x^2 - 9) = (x + 3)(x - 3)
$$

3. El primero no se factoriza (suma de cuadrados).

**Resultado:** $\boxed{(x^2 + 9)(x + 3)(x - 3)}$

---

### Ejemplo 3: Trinomio simple

Factoriza: $x^2 - 5x + 6$

**Datos:**
- Coeficiente de $x^2$ es 1.
- Buscamos números que multipliquen 6 y sumen -5.

**Razonamiento:**

1. Números: 

$$
-2 \quad \text{y} \quad -3
$$

2. Verificación: 

$$
(-2) + (-3) = -5
$$

$$
(-2) \times (-3) = 6
$$

**Resultado:** $\boxed{(x - 2)(x - 3)}$

---

### Ejemplo 4: Suma de cubos

Factoriza: $8a^3 + 27$

**Datos:**
- $8a^3 = (2a)^3$ y $27 = 3^3$.

**Razonamiento:**

1. Aplicamos fórmula de suma de cubos.

2. Primer factor: 

$$
(2a + 3)
$$

3. Segundo factor: 

$$
(2a)^2 - (2a)(3) + 3^2 = 4a^2 - 6a + 9
$$

**Resultado:** $\boxed{(2a + 3)(4a^2 - 6a + 9)}$

---

### Ejemplo 5: Combinación de métodos

Factoriza: $2x^3 - 8x$

**Datos:**
- Hay factor común $2x$.

**Razonamiento:**

1. Sacamos $2x$: 

$$
2x(x^2 - 4)
$$

2. Adentro es diferencia de cuadrados: 

$$
2x(x + 2)(x - 2)
$$

**Resultado:** $\boxed{2x(x + 2)(x - 2)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica el caso y factoriza: $5x^2 - 20$

<details>
<summary>Ver solución</summary>

**Caso:** Factor común + diferencia de cuadrados.
**Razonamiento:** 

$$
5(x^2 - 4) = 5(x + 2)(x - 2)
$$

**Resultado:** $\boxed{5(x + 2)(x - 2)}$

</details>

### Ejercicio 2
Factoriza: $x^2 - 49$

<details>
<summary>Ver solución</summary>

**Caso:** Diferencia de cuadrados.
**Razonamiento:** 

$$
x^2 - 7^2 = (x + 7)(x - 7)
$$

**Resultado:** $\boxed{(x + 7)(x - 7)}$

</details>

### Ejercicio 3
Factoriza: $x^2 + 10x + 25$

<details>
<summary>Ver solución</summary>

**Caso:** Trinomio cuadrado perfecto.
**Razonamiento:** $(x + 5)^2$
**Resultado:** $\boxed{(x + 5)^2}$

</details>

### Ejercicio 4
Factoriza: $x^2 + 3x - 10$

<details>
<summary>Ver solución</summary>

**Caso:** Trinomio simple.
**Razonamiento:** 

$$
(x + 5)(x - 2)
$$

**Resultado:** $\boxed{(x + 5)(x - 2)}$

</details>

### Ejercicio 5
Factoriza: $2x^2 + 5x + 2$

<details>
<summary>Ver solución</summary>

**Caso:** Trinomio general.
**Razonamiento:** $(2x + 1)(x + 2)$
**Resultado:** $\boxed{(2x + 1)(x + 2)}$

</details>

### Ejercicio 6
Factoriza: $x^3 + 125$

<details>
<summary>Ver solución</summary>

**Caso:** Suma de cubos.
**Razonamiento:** 

$$
(x + 5)(x^2 - 5x + 25)
$$

**Resultado:** $\boxed{(x + 5)(x^2 - 5x + 25)}$

</details>

### Ejercicio 7
Factoriza: $27a^3 - 64b^3$

<details>
<summary>Ver solución</summary>

**Caso:** Diferencia de cubos.
**Razonamiento:** 

$$
(3a - 4b)(9a^2 + 12ab + 16b^2)
$$

**Resultado:** $\boxed{(3a - 4b)(9a^2 + 12ab + 16b^2)}$

</details>

### Ejercicio 8
Factoriza: $ax + ay - bx - by$

<details>
<summary>Ver solución</summary>

**Caso:** Agrupación.
**Razonamiento:** 

$$
a(x + y) - b(x + y) = (x + y)(a - b)
$$

**Resultado:** $\boxed{(x + y)(a - b)}$

</details>

### Ejercicio 9
Factoriza: $x^6 - 1$

<details>
<summary>Ver solución</summary>

**Caso:** Diferencia de cuadrados + cubos.
**Razonamiento:** 

$$
(x^3 + 1)(x^3 - 1) = (x + 1)(x^2 - x + 1)(x - 1)(x^2 + x + 1)
$$

**Resultado:** $\boxed{(x + 1)(x - 1)(x^2 - x + 1)(x^2 + x + 1)}$

</details>

### Ejercicio 10
Factoriza: $3x^3 + 6x^2 - 9x$

<details>
<summary>Ver solución</summary>

**Caso:** Factor común + trinomio.
**Razonamiento:** 

$$
3x(x^2 + 2x - 3) = 3x(x + 3)(x - 1)
$$

**Resultado:** $\boxed{3x(x + 3)(x - 1)}$

</details>

---

## 🔑 Resumen

| Términos | Posibles Casos |
| :--- | :--- |
| **2 términos** | Diferencia de cuadrados, suma/diferencia de cubos |
| **3 términos** | TCP, trinomio simple, trinomio general |
| **4+ términos** | Agrupación |

> Siempre empieza buscando factor común. Luego cuenta los términos para decidir qué método usar. Y al final, verifica multiplicando.

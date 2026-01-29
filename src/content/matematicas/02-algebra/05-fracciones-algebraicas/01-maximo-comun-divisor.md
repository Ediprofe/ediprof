# **Máximo Común Divisor (MCD)**

Imagina que tienes dos cuerdas de diferente longitud y quieres cortarlas en trozos del mismo tamaño, lo más largos posible, sin que sobre nada. En álgebra, el Máximo Común Divisor (MCD) es exactamente eso: la expresión más grande que está "contenida" exactamente dentro de otras expresiones.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de MCD aplicado al álgebra.
- A calcular el MCD de coeficientes numéricos.
- La regla de los exponentes para variables comunes.
- A encontrar el MCD de polinomios complejos usando factorización.

---

## 🔍 Reglas Fundamentales

Para encontrar el MCD, analizamos por separado los números y las letras:

1.  **Coeficientes (Números):** Calculamos el MCD aritmético (el número más grande que divide a todos).
2.  **Variables (Letras):** Elegimos solo las letras que se repiten en **todos** los términos, con su **menor exponente**.
3.  **Polinomios:** Si son expresiones compuestas (como $x^2-1$), primero debemos **factorizar** todo y luego aplicar la regla de los exponentes.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: MCD de Monomios

Encuentra el MCD de $12x^3y^2$ y $18x^2y^4$.

**Datos:**
- Expresión 1: $12x^3y^2$
- Expresión 2: $18x^2y^4$

**Razonamiento:**

1. **Números:** MCD de 12 y 18.
   - Divisores de 12: $1, 2, 3, 4, 6, 12$
   - Divisores de 18: $1, 2, 3, 6, 9, 18$
   - El mayor común es **6**.

2. **Letras:**
   - $x$: Aparece en ambos. Menor exponente: 
   
$$
x^2
$$

   - $y$: Aparece en ambos. Menor exponente: 

$$
y^2
$$

**Resultado:** $\boxed{6x^2y^2}$

---

### Ejemplo 2: Monomios con tres términos

Calcula el MCD de $8a^4b^3$, $20a^2b^5$ y $12a^3b^4$.

**Datos:**
- Tres monomios.

**Razonamiento:**

1. **Números:** MCD(8, 20, 12).
   - Todos se dividen por 2 y por 4. El mayor es **4**.

2. **Letras:**
   - $a$: Exponentes 4, 2, 3. El menor es: 
   
$$
a^2
$$

   - $b$: Exponentes 3, 5, 4. El menor es: 

$$
b^3
$$

**Resultado:** $\boxed{4a^2b^3}$

---

### Ejemplo 3: Polinomios factorizados (Caso simple)

Halla el MCD de $6x(x-1)$ y $9x^2(x-1)^2$.

**Datos:**
- Las expresiones ya tienen factores visibles.

**Razonamiento:**

1. **Coeficientes:** MCD(6, 9) es **3**.

2. **Variable $x$:** Tenemos $x$ y $x^2$. El menor es: 

$$
x
$$

3. **Factor $(x-1)$:** Aparece en ambos. Exponentes 1 y 2. El menor es: 

$$
(x-1)^1
$$

**Resultado:** $\boxed{3x(x-1)}$

---

### Ejemplo 4: Polinomios que requieren factorización

Encuentra el MCD de $x^2 - 4$ y $x^2 + 4x + 4$.

**Datos:**
- Polinomio 1: Diferencia de cuadrados.
- Polinomio 2: Trinomio Cuadrado Perfecto.

**Razonamiento:**

1. Factorizamos el primero:

$$
x^2 - 4 = (x+2)(x-2)
$$

2. Factorizamos el segundo:

$$
x^2 + 4x + 4 = (x+2)^2
$$

3. Buscamos factores comunes con menor exponente:
   - Común: $(x+2)$.
   - Menor exponente: 1 (del primer polinomio).

**Resultado:** $\boxed{x+2}$

---

### Ejemplo 5: Polinomios complejos

Calcula el MCD de $2x^2 + 6x$ y $x^3 + 3x^2$.

**Datos:**
- Ambos requieren factor común primero.

**Razonamiento:**

1. Factorizamos $2x^2 + 6x$:
   - Factor común: 

$$
2x(x+3)
$$

2. Factorizamos $x^3 + 3x^2$:
   - Factor común: 

$$
x^2(x+3)
$$

3. Comparamos $2x(x+3)$ con $x^2(x+3)$.
   - Coeficientes: MCD(2, 1) = 1.
   - Variables: Entre $x$ y $x^2$, el menor es $x$.
   - Paréntesis: $(x+3)$ es común.

**Resultado:** $\boxed{x(x+3)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el MCD de $15a^2b$ y $25ab^2$.

<details>
<summary>Ver solución</summary>

**Datos:** Numéricos 15 y 25. Letras a, b.
**Razonamiento:** 

$$
MCD(15, 25) = 5
$$

Menor exponente de $a$: 1. 

Menor de $b$: 1.
**Resultado:** $\boxed{5ab}$

</details>

### Ejercicio 2
Encuentra el MCD de $x^2y$, $xy^2$ y $x^3y^3$.

<details>
<summary>Ver solución</summary>

**Datos:** Solo variables.
**Razonamiento:** 

La $x$ y la $y$ están en todos. 

Menor exponente de $x$ es 1. 

Menor de $y$ es 1.
**Resultado:** $\boxed{xy}$

</details>

### Ejercicio 3
Calcula el MCD de $6m^2n^3$ y $9mn^4$.

<details>
<summary>Ver solución</summary>

**Datos:** Coeficientes 6, 9.
**Razonamiento:** 

MCD(6,9) = 3. 

Variables: 

$$
mn^3
$$

**Resultado:** $\boxed{3mn^3}$

</details>

### Ejercicio 4
Halla el MCD de $3(a+1)$ y $3(a+1)^2$.

<details>
<summary>Ver solución</summary>

**Datos:** Factor 3 y factor (a+1).
**Razonamiento:** 

El 3 es común. 

El $(a+1)$ está en ambos, su menor exponente es 1.

$$
MCD = 3(a+1)
$$
**Resultado:** $\boxed{3(a+1)}$

</details>

### Ejercicio 5
Encuentra el MCD de $x^2 - 1$ y $x^2 - x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
1. 
$$
x^2 - 1 = (x+1)(x-1)
$$

2. 
$$
x^2 - x = x(x-1)
$$

3. Común: 

$$
(x-1)
$$

**Resultado:** $\boxed{x-1}$

</details>

### Ejercicio 6
Calcula el MCD de $x^2 + 5x + 6$ y $x^2 + 6x + 9$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
x^2 + 5x + 6 = (x+2)(x+3)
$$

2. 
$$
x^2 + 6x + 9 = (x+3)^2
$$

3. Común: 

$$
(x+3)
$$

**Resultado:** $\boxed{x+3}$

</details>

### Ejercicio 7
Encuentra el MCD de $4a^2$ y $8a^3 - 4a^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. $4a^2$ ya es monomio.

2. 
$$
8a^3 - 4a^2 = 4a^2(2a - 1)
$$

3. El factor $4a^2$ está en ambos.

**Resultado:** $\boxed{4a^2}$

</details>

### Ejercicio 8
Halla el MCD de $x^3 - x$ y $x^2 + x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
x^3 - x = x(x^2-1) = x(x+1)(x-1)
$$

2. 
$$
x^2 + x = x(x+1)
$$

3. Comunes: 

$$
x(x+1)
$$

**Resultado:** $\boxed{x(x+1)}$

</details>

### Ejercicio 9
Calcula el MCD de $2x - 2$, $x^2 - 1$ y $x^2 - 2x + 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
2(x-1)
$$

2. 
$$
(x+1)(x-1)
$$

3. 
$$
(x-1)^2
$$

Factor común en los tres: 

$$
(x-1)
$$

**Resultado:** $\boxed{x-1}$

</details>

### Ejercicio 10
Encuentra el MCD de $15a^2b$ y $20x^2y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
**Razonamiento:** 

1. $MCD(15, 20) = 5$.

2. No hay letras comunes.
**Resultado:** $\boxed{5}$

</details>

---

## 🔑 Resumen

| Tipo | Regla Clave | Ejemplo |
| :--- | :--- | :--- |
| **Coeficientes** | Número más grande que divide a todos | MCD(12, 18) = 6 |
| **Variables** | Letras repetidas con **menor** exponente | MCD($x^3, x^5$) = $x^3$ |
| **Polinomios** | Factores repetidos con **menor** exponente | MCD($(x+1)^2, x+1$) = $(x+1)$ |

> Recuerda: El MCD es "selectivo", solo toma lo que todos comparten y en la cantidad mínima garantizada.

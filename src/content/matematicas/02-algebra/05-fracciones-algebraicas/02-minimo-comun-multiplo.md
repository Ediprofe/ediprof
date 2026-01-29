# **Mínimo Común Múltiplo (MCM)**

Imagina que dos corredores parten al mismo tiempo en una pista circular. Uno tarda 4 minutos en dar la vuelta y el otro 6 minutos. ¿Cuándo volverán a encontrarse en la línea de salida? ¡En el minuto 12! Eso es el Mínimo Común Múltiplo: el primer punto de encuentro. En álgebra, sirve para encontrar un denominador común que contenga a todos los demás.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de MCM como "contenedor universal".
- A calcular el MCM de coeficientes numéricos.
- La regla de los exponentes para el MCM (¡al revés que el MCD!).
- A encontrar el MCM de polinomios usando factorización.

---

## 🔍 Reglas Fundamentales

A diferencia del MCD que es selectivo, el MCM es **inclusivo**: quiere tenerlo todo.

1.  **Coeficientes (Números):** Calculamos el MCM aritmético (el número más pequeño que es múltiplo de todos).
2.  **Variables (Letras):** Elegimos **todas** las letras (comunes y no comunes), con su **mayor exponente**.
3.  **Polinomios:** Primero **factorizamos** todo. Luego tomamos **todos** los factores diferentes, cada uno con su **mayor exponente**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: MCM de Monomios

Encuentra el MCM de $12x^3y^2$ y $18x^2y^4$.

**Datos:**
- Expresión 1: $12x^3y^2$
- Expresión 2: $18x^2y^4$

**Razonamiento:**

1. **Números:** MCM de 12 y 18.
   - Múltiplos de 12: $12, 24, 36, 48...$
   - Múltiplos de 18: $18, 36, 54...$
   - El primero en coincidir es **36**.

2. **Letras:** Tomamos todas con el exponente más alto.
   - $x$: Exponentes 3 y 2. Gana: 
   
$$
x^3
$$

   - $y$: Exponentes 2 y 4. Gana: 

$$
y^4
$$

**Resultado:** $\boxed{36x^3y^4}$

---

### Ejemplo 2: Monomios con letras diferentes

Calcula el MCM de $8a^2b$ y $12bc^3$.

**Datos:**
- Monomio 1: tiene $a$ y $b$.
- Monomio 2: tiene $b$ y $c$.

**Razonamiento:**

1. **Números:** MCM(8, 12) = 24.

2. **Letras:**
   - $a$: Solo está en el primero ($a^2$). ¡La incluimos!
   - $b$: Está en ambos ($b^1$). Tomamos $b$.
   - $c$: Solo está en el segundo ($c^3$). ¡La incluimos!

**Resultado:** $\boxed{24a^2bc^3}$

---

### Ejemplo 3: Polinomios factorizados

Halla el MCM de $6(x-1)$ y $9(x-1)^2$.

**Datos:**
- Factores numéricos y binomios.

**Razonamiento:**

1. **Coeficientes:** MCM(6, 9) = 18.

2. **Factor $(x-1)$:** Aparece como $(x-1)^1$ y $(x-1)^2$.

3. Elegimos el de **mayor exponente**: 

$$
(x-1)^2
$$

**Resultado:** $\boxed{18(x-1)^2}$

---

### Ejemplo 4: Polinomios que requieren factorización

Encuentra el MCM de $x^2 - 4$ y $x^2 - 4x + 4$.

**Datos:**
- Polinomio 1: Diferencia de cuadrados.
- Polinomio 2: Trinomio Cuadrado Perfecto.

**Razonamiento:**

1. Factorizamos primero:
   
$$
x^2 - 4 = (x+2)(x-2)
$$

$$
x^2 - 4x + 4 = (x-2)^2
$$

2. Hacemos la lista de factores únicos: $(x+2)$ y $(x-2)$.

3. Elegimos el mayor exponente para cada uno:
   - $(x+2)$: Solo aparece a la 1. $\to (x+2)$
   - $(x-2)$: Aparece a la 1 y a la 2. Gana la 2. $\to (x-2)^2$

**Resultado:** $\boxed{(x+2)(x-2)^2}$

---

### Ejemplo 5: Tres polinomios distintos

Calcula el MCM de $2x$, $x^2+x$ y $x^2-1$.

**Datos:**
- Monomio, binomio y binomio.

**Razonamiento:**

1. Factorizamos todo:
   - $2x$ (ya está).
   - $x^2+x = x(x+1)$.
   - $x^2-1 = (x+1)(x-1)$.

2. Recopilamos factores: $2$, $x$, $(x+1)$, $(x-1)$.

3. Multiplicamos todos (todos tienen exponente 1).

**Resultado:** $\boxed{2x(x+1)(x-1)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el MCM de $15a^2b$ y $10ab^3$.

<details>
<summary>Ver solución</summary>

**Datos:** Números 15 y 10. Letras a, b.
**Razonamiento:** 

$$
MCM(15, 10) = 30
$$

Mayores exponentes: $a^2$ y $b^3$.
**Resultado:** $\boxed{30a^2b^3}$

</details>

### Ejercicio 2
Encuentra el MCM de $x^2y$ y $xy^2z$.

<details>
<summary>Ver solución</summary>

**Datos:** Variables x, y, z.
**Razonamiento:** 

Tomamos todas con mayor exponente: 

$$
x^2 \quad , \quad y^2 \quad , \quad z
$$
**Resultado:** $\boxed{x^2y^2z}$

</details>

### Ejercicio 3
Calcula el MCM de $4m^2$ y $6m^3$.

<details>
<summary>Ver solución</summary>

**Datos:** Coeficientes 4, 6. Variable m.
**Razonamiento:** 

$$
MCM(4,6) = 12
$$

Mayor variable: $m^3$.
**Resultado:** $\boxed{12m^3}$

</details>

### Ejercicio 4
Halla el MCM de $2(a+1)$ y $3(a+1)^2$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM(2,3)=6. Factor $(a+1)$.
**Razonamiento:** 

$$
MCM(2,3) = 6
$$

Mayor exponente del paréntesis es 2.
**Resultado:** $\boxed{6(a+1)^2}$

</details>

### Ejercicio 5
Encuentra el MCM de $x^2 - 1$ y $x+1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
x^2 - 1 = (x+1)(x-1)
$$

2. $x+1$ es irreducible.

3. Factores: 

$$
(x+1) \quad \text{y} \quad (x-1)
$$

**Resultado:** $\boxed{(x+1)(x-1)}$

</details>

### Ejercicio 6
Calcula el MCM de $x^2 + 2x + 1$ y $x^2 - 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
(x+1)^2
$$

2. 
$$
(x+1)(x-1)
$$

3. Tomamos: 

$$
(x+1)^2 \quad \text{y} \quad (x-1)
$$

**Resultado:** $\boxed{(x+1)^2(x-1)}$

</details>

### Ejercicio 7
Encuentra el MCM de $3x^2$ y $9x(x-2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. $3x^2$
2. $9x(x-2)$

Coeficiente: 9. 

Variable $x$: $x^2$ (mayor). 

Factor $(x-2)$.

**Resultado:** $\boxed{9x^2(x-2)}$

</details>

### Ejercicio 8
Halla el MCM de $x^3 - x$ y $x^2 - x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
x(x^2-1) = x(x+1)(x-1)
$$

2. 
$$
x(x-1)
$$

MCM incluye todo lo del primero que ya cubre al segundo.

**Resultado:** $\boxed{x(x+1)(x-1)}$

</details>

### Ejercicio 9
Calcula el MCM de $m-1$, $m^2-1$ y $m+1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
m^2-1 = (m+1)(m-1)
$$

Este término ya contiene a los otros dos.

**Resultado:** $\boxed{(m+1)(m-1)} \quad \text{o} \quad \boxed{m^2-1}$

</details>

### Ejercicio 10
Halla el MCM de $x^2-25$ y $x^2-10x+25$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

1. 
$$
(x+5)(x-5)
$$

2. 
$$
(x-5)^2
$$

Tomamos: 

$$
(x+5) \quad \text{y} \quad (x-5)^2
$$

**Resultado:** $\boxed{(x+5)(x-5)^2}$

</details>

---

## 🔑 Resumen

| MCD (Divisor) | MCM (Múltiplo) |
| :--- | :--- |
| El más **pequeño** posible | El más **grande** (completo) posible |
| Solo factores **comunes** | **Todos** los factores |
| **Menor** exponente | **Mayor** exponente |

> El MCM es como una maleta de viaje: debes asegurarte de que quepa todo lo que llevan los polinomios originales, sin dejar nada fuera.

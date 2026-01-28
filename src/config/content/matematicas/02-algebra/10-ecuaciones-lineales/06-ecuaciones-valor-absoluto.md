---
title: "Ecuaciones con Valor Absoluto"
---

# **Ecuaciones con Valor Absoluto**

A menudo nos enseñan que el valor absoluto "hace positivos los números", pero esa definición es incompleta. Para entender realmente las ecuaciones, debemos pensar en el valor absoluto como una **distancia**.

Cuando resuelves una ecuación normal como $x = 5$, hay un solo camino. Pero el valor absoluto abre **dos caminos** posibles para llegar al mismo destino (la misma distancia).

---

## 🎯 ¿Qué vas a aprender?

- 📏 **Visión Geométrica:** Entender $|x|$ como distancia pura.
- 🔀 **El "Desdoblamiento":** Por qué una ecuación se rompe en dos.
- 🚫 **Imposibles:** Detectar cuándo no hay solución.
- 🛠️ **Técnica:** Resolver ecuaciones complejas paso a paso.

---

## 📏 Concepto 1: La Distancia al Origen

Imagina que estás parado en el cero de una recta numérica y te piden caminar una **distancia de 4 pasos**. ¿A dónde puedes llegar?

$$
|x| = 4
$$

Tienes dos opciones:
1. Caminar 4 pasos a la **derecha** $\rightarrow$ Llegas al **4**.
2. Caminar 4 pasos a la **izquierda** $\rightarrow$ Llegas al **-4**.

![Distancia al origen](/images/matematicas/algebra/ecuaciones-lineales/absolute_value_basic.svg)

Matemáticamente, esto crea dos ecuaciones sencillas:

$$
x = 4 \quad \text{o} \quad x = -4
$$

---

## 📍 Concepto 2: Anatomía de la Ecuación

Para no perderte, usa este **mapa visual**. Rompemos la ecuación $|x - 2| = 3$ en sus componentes reales:

![Anatomía de Ecuación Valor Absoluto](/images/matematicas/algebra/ecuaciones-lineales/absolute_value_anatomy.svg)

**La Lógica en 3 Pasos:**
1.  **Centro (2):** Empiezas en el 2.
2.  **Distancia (3):** Caminas 3 pasos a la derecha (positivo) y 3 a la izquierda (negativo).
3.  **Destino (x):** Llegas al **5** y al **-1**. Esas son tus soluciones.

> **💡 Regla Rápida:**
> ¿Ves $|x - 2|$? Piensa: "La distancia desde x hasta 2".
>
> Para resolverlo algebraicamente, solo aplica los dos caminos del dibujo:
> 1.  **Camino Derecho (+):** $x - 2 = 3$
> 2.  **Camino Izquierdo (-):** $x - 2 = -3$

---

## ⚙️ Ejemplos Resueltos: Método Paso a Paso

### Ejemplo 1: El caso básico
Resolver $|x| = 7$.

![Solución visual para |x|=7](/images/matematicas/algebra/ecuaciones-lineales/ex_basic_7.svg)

**Razonamiento:**
Buscamos números a distancia 7 del cero.

**Opción A (Derecha):**
$$
x = 7
$$

**Opción B (Izquierda):**
$$
x = -7
$$

$$
\boxed{x = 7, \quad x = -7}
$$

### Ejemplo 2: Centro desplazado
Resolver $|x - 5| = 2$.

![Solución visual para |x-5|=2](/images/matematicas/algebra/ecuaciones-lineales/ex_shifted_5_2.svg)

**Razonamiento:**
La distancia desde 5 es de 2 unidades. Desdoblamos:

1. **Caso Positivo:**
   
$$
x - 5 = 2 \implies x = 7
$$

2. **Caso Negativo:**
   
$$
x - 5 = -2 \implies x = 3
$$

$$
\boxed{x = 7, \quad x = 3}
$$

### Ejemplo 3: El coeficente en la variable
Resolver $|2x + 1| = 9$.

![Solución en la recta numérica](/images/matematicas/algebra/ecuaciones-lineales/ex_coeff_2x.svg)

**Razonamiento:**
Aunque haya un $2x$, la lógica es idéntica. Lo de adentro vale 9 o vale -9.

1. **Caso Positivo:**
   
$$
2x + 1 = 9 \implies 2x = 8 \implies x = 4
$$

2. **Caso Negativo:**
   
$$
2x + 1 = -9 \implies 2x = -10 \implies x = -5
$$

$$
\boxed{x = 4, \quad x = -5}
$$

### Ejemplo 4: El Caso Imposible
Resolver $|x + 3| = -4$.

![Representación de la imposibilidad](/images/matematicas/algebra/ecuaciones-lineales/ex_impossible.svg)

**Razonamiento:**
¡Alto ahí! 🛑
El valor absoluto es una **distancia**. ¿Puedes caminar "-4 pasos" de distancia? No. Las distancias siempre son positivas o cero.

$$
\boxed{\text{Sin Solución}}
$$

### Ejemplo 5: Despeje Previo
Resolver $3|x - 2| + 5 = 17$.

![Solución visual tras despeje](/images/matematicas/algebra/ecuaciones-lineales/ex_clearance.svg)

**Razonamiento:**
El valor absoluto es el "rey" de la ecuación, pero está rodeado de guardias ($+5$ y $\times 3$). Primero debemos dejarlo solo.

1. Restamos 5:
   
$$
3|x - 2| = 12
$$

2. Dividimos por 3:
   
$$
|x - 2| = 4
$$

3. **¡Ahora sí desdoblamos!**
   - Caso 1: $x - 2 = 4 \implies x = 6$
   - Caso 2: $x - 2 = -4 \implies x = -2$

$$
\boxed{x = 6, \quad x = -2}
$$

### Ejemplo 6: Doble Valor Absoluto
Resolver $|x - 3| = |2x + 1|$.

![Ubicación de las soluciones](/images/matematicas/algebra/ecuaciones-lineales/ex_double.svg)

**Razonamiento:**
Si dos distancias son iguales, es porque los números son iguales ($a = b$) o son opuestos ($a = -b$).

1. **Iguales:**
   
$$
x - 3 = 2x + 1 \implies -x = 4 \implies x = -4
$$

2. **Opuestos:**
   
$$
x - 3 = -(2x + 1)
$$

$$
x - 3 = -2x - 1
$$

$$
3x = 2 \implies x = 2/3
$$

$$
\boxed{x = -4, \quad x = \frac{2}{3}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve la ecuación básica: $|x| = 15$.

<details>
<summary>Ver solución</summary>

$$
x = 15 \quad \text{o} \quad x = -15
$$

**Resultado:**
$$
\boxed{\pm 15}
$$

</details>

---

### Ejercicio 2
Resuelve: $|x + 4| = 7$.

<details>
<summary>Ver solución</summary>

$$
x + 4 = 7 \implies x = 3
$$

$$
x + 4 = -7 \implies x = -11
$$

**Resultado:**
$$
\boxed{3, -11}
$$

</details>

---

### Ejercicio 3
Resuelve: $|3x| = 12$.

<details>
<summary>Ver solución</summary>

$$
3x = 12 \implies x = 4
$$

$$
3x = -12 \implies x = -4
$$

**Resultado:**
$$
\boxed{\pm 4}
$$

</details>

---

### Ejercicio 4
Resuelve: $|x - 8| = -2$.

<details>
<summary>Ver solución</summary>

Una distancia no puede ser negativa.

**Resultado:**
$$
\boxed{\text{Sin Solución}}
$$

</details>

---

### Ejercicio 5
Resuelve: $|2x - 5| = 9$.

<details>
<summary>Ver solución</summary>

$$
2x - 5 = 9 \implies 2x = 14 \implies x = 7
$$

$$
2x - 5 = -9 \implies 2x = -4 \implies x = -2
$$

**Resultado:**
$$
\boxed{7, -2}
$$

</details>

---

### Ejercicio 6
Resuelve despejando primero: $|x + 1| - 3 = 5$.

<details>
<summary>Ver solución</summary>

Primero:
$$
|x + 1| = 8
$$

Casos:
$$
x + 1 = 8 \implies x = 7
$$
$$
x + 1 = -8 \implies x = -9
$$

**Resultado:**
$$
\boxed{7, -9}
$$

</details>

---

### Ejercicio 7
Resuelve: $2|x - 3| = 10$.

<details>
<summary>Ver solución</summary>

Primero:
$$
|x - 3| = 5
$$

Casos:
$$
x - 3 = 5 \implies x = 8
$$
$$
x - 3 = -5 \implies x = -2
$$

**Resultado:**
$$
\boxed{8, -2}
$$

</details>

---

### Ejercicio 8
Resuelve el caso anidado: $|4 - x| = 1$.

<details>
<summary>Ver solución</summary>

$$
4 - x = 1 \implies -x = -3 \implies x = 3
$$

$$
4 - x = -1 \implies -x = -5 \implies x = 5
$$

**Resultado:**
$$
\boxed{3, 5}
$$

</details>

---

### Ejercicio 9
Resuelve: $3|2x| - 4 = 14$.

<details>
<summary>Ver solución</summary>

Despeje:
$$
3|2x| = 18 \implies |2x| = 6
$$

Casos:
$$
2x = 6 \implies x = 3
$$
$$
2x = -6 \implies x = -3
$$

**Resultado:**
$$
\boxed{\pm 3}
$$

</details>

---

### Ejercicio 10
Resuelve: $|x + 2| = |x - 8|$.

<details>
<summary>Ver solución</summary>

Caso 1 (Iguales):
$$
x + 2 = x - 8 \implies 2 = -8 \quad (\text{Falso, sin solución aquí})
$$

Caso 2 (Opuestos):
$$
x + 2 = -(x - 8)
$$
$$
x + 2 = -x + 8
$$
$$
2x = 6 \implies x = 3
$$

**Resultado:**
$$
\boxed{3}
$$

</details>

---

## 🔑 Resumen

| Forma | Significado Visual | Procedimiento |
|:--- |:--- |:--- |
| $\lvert x \rvert = d$ | Puntos a distancia $d$ del 0 | $x=d$ ó $x=-d$ |
| $\lvert x-a \rvert = d$ | Puntos a distancia $d$ de $a$ | $x-a=d$ ó $x-a=-d$ |
| $\lvert \dots \rvert = -k$ | Distancia negativa (Imposible) | Escribe "Sin solución" |

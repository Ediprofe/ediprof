---
title: "Multiplicación de Complejos"
---

# **Multiplicación de Complejos**

Multiplicar números complejos puede parecer intimidante, pero en realidad ya sabes hacerlo. Es idéntico a multiplicar binomios en álgebra (como $(x+2)(x+3)$), con un único giro final: **siempre que veas $i^2$, debes cambiarlo por -1**.

---

## 🎯 ¿Qué vas a aprender?

- Cómo multiplicar dos números complejos con la propiedad distributiva (todos con todos).
- Por qué $a \cdot c$ y $b \cdot d$ terminan siendo la parte real.
- El caso especial: multiplicar un complejo por su conjugado.
- Cómo elevar un complejo al cuadrado.

---

## ✖️ Propiedad Distributiva (Todos con Todos)

Para multiplicar $(a + bi)(c + di)$, aplicamos la propiedad distributiva:

1. **Primeros:** $a \cdot c$
2. **Exteriores:** $a \cdot di$
3. **Interiores:** $bi \cdot c$
4. **Últimos:** $bi \cdot di = bd \cdot i^2$

> **¡El paso mágico!**
> El último término siempre tendrá $i^2$. Como $i^2 = -1$, ese término cambia de signo y se vuelve **real**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Multiplicación Paso a Paso

Calcula $(2 + 3i)(4 + 5i)$.

**Paso 1: Distribuir (Todos con todos)**
- $2 \cdot 4 = 8$
- $2 \cdot 5i = 10i$
- $3i \cdot 4 = 12i$
- $3i \cdot 5i = 15i^2$

**Paso 2: Simplificar $i^2$**
Recordemos que $15i^2 = 15(-1) = -15$.

$$
8 + 10i + 12i - 15
$$

**Paso 3: Agrupar**
- Reales: $8 - 15 = -7$
- Imaginarios: $10i + 12i = 22i$

**Resultado:**

$$
\boxed{-7 + 22i}
$$

---

### Ejemplo 2: Cuidado con los Negativos

Calcula $(3 - 2i)(1 - 4i)$.

**Paso 1: Distribuir**
- $3 \cdot 1 = 3$
- $3 \cdot (-4i) = -12i$
- $-2i \cdot 1 = -2i$
- $-2i \cdot (-4i) = +8i^2$

**Paso 2: Simplificar**
$8i^2 = 8(-1) = -8$.

$$
3 - 12i - 2i - 8
$$

**Paso 3: Agrupar**
- $3 - 8 = -5$
- $-12i - 2i = -14i$

**Resultado:**

$$
\boxed{-5 - 14i}
$$

---

### Ejemplo 3: Cuadrado de un Binomio

Calcula $(4 + i)^2$.

**Razonamiento:**
Es lo mismo que $(4 + i)(4 + i)$.

$$
16 + 4i + 4i + i^2
$$

$$
16 + 8i - 1
$$

**Resultado:**

$$
\boxed{15 + 8i}
$$

---

### Ejemplo 4: Producto de Conjugados (¡Muy Útil!)

Calcula $(3 + 4i)(3 - 4i)$.

**Paso 1: Distribuir**
- $3 \cdot 3 = 9$
- $3 \cdot (-4i) = -12i$
- $4i \cdot 3 = +12i$
- $4i \cdot (-4i) = -16i^2$

**Paso 2: Simplificar**
Los términos centrales ($-12i + 12i$) **se cancelan**.
$-16i^2$ se convierte en $+16$.

$$
9 + 16
$$

**Resultado:**

$$
\boxed{25}
$$

> **Regla de Oro:** Multiplicar conjugados $(a+bi)(a-bi)$ siempre da $a^2 + b^2$ (Sumas de cuadrados).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $(1 + 2i)(3 + i)$.

<details>
<summary>Ver solución</summary>

$$
3 + i + 6i + 2i^2 = 3 + 7i - 2 = 1 + 7i
$$

**Resultado:** $\boxed{1 + 7i}$

</details>

---

### Ejercicio 2
Calcula $(2 - 3i)(4 - i)$.

<details>
<summary>Ver solución</summary>

$$
8 - 2i - 12i + 3i^2 = 8 - 14i - 3 = 5 - 14i
$$

**Resultado:** $\boxed{5 - 14i}$

</details>

---

### Ejercicio 3
Calcula $(5 + i)^2$.

<details>
<summary>Ver solución</summary>

$$
25 + 10i + i^2 = 25 + 10i - 1 = 24 + 10i
$$

**Resultado:** $\boxed{24 + 10i}$

</details>

---

### Ejercicio 4
Calcula $(2 + 5i)(2 - 5i)$.

<details>
<summary>Ver solución</summary>

Es suma de cuadrados ($2^2 + 5^2$).
$4 + 25 = 29$.

**Resultado:** $\boxed{29}$

</details>

---

### Ejercicio 5
Calcula $(1 - i)^2$.

<details>
<summary>Ver solución</summary>

$$
1 - 2i + i^2 = 1 - 2i - 1 = -2i
$$

**Resultado:** $\boxed{-2i}$

</details>

---

### Ejercicio 6
Calcula $i(3 + 4i)(1 - i)$.

<details>
<summary>Ver solución</summary>
Primero $(3+4i)(1-i) = 3 - 3i + 4i - 4i^2 = 7 + i$.
Luego $i(7+i) = 7i + i^2 = 7i - 1$.

**Resultado:** $\boxed{-1 + 7i}$

</details>

---

### Ejercicio 7
Calcula $(3i)(2 - i)$.

<details>
<summary>Ver solución</summary>

$$
6i - 3i^2 = 6i - 3(-1) = 3 + 6i
$$

**Resultado:** $\boxed{3 + 6i}$

</details>

---

### Ejercicio 8
Calcula $(4 + 3i)(4 - 3i)$.

<details>
<summary>Ver solución</summary>

$$
16 + 9 = 25
$$

**Resultado:** $\boxed{25}$

</details>

---

### Ejercicio 9
Calcula $(2 + 2i)(1 + i)$.

<details>
<summary>Ver solución</summary>

$$
2 + 2i + 2i + 2i^2 = 2 + 4i - 2 = 4i
$$

**Resultado:** $\boxed{4i}$

</details>

---

### Ejercicio 10
Calcula $(1 - 3i)(5 + 2i)$.

<details>
<summary>Ver solución</summary>

$$
5 + 2i - 15i - 6i^2 = 5 - 13i + 6 = 11 - 13i
$$

**Resultado:** $\boxed{11 - 13i}$

</details>

---

## 🔑 Resumen

| Operación | Truco | Fórmula Mental |
|:--- |:--- |:--- |
| **Producto Estándar** | Propiedad Distributiva | "Todos con todos" + "Ojo con $i^2$" |
| **Conjugados** | Suma de cuadrados | $(a+bi)(a-bi) = a^2 + b^2$ |
| **Cuadrados** | Binomio al cuadrado | $a^2 + 2abi - b^2$ |

> **Conclusión:** La multiplicación de complejos es álgebra normal, pero el último término siempre "da la vuelta" y se vuelve real.

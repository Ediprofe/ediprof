# 🔢 Progresión Aritmética

En esta lección estudiaremos las progresiones aritméticas.

---

## 📖 Definición

Una **progresión aritmética (PA)** es una sucesión donde cada término se obtiene sumando una cantidad fija (llamada **diferencia común** $d$) al término anterior.

$$
a_n = a_1 + (n-1)d
$$

---

## 📖 Ejemplos

### Ejemplo 1

$2, 5, 8, 11, 14, ...$

Diferencia: $d = 5 - 2 = 3$

Término general: $a_n = 2 + (n-1) \cdot 3 = 3n - 1$

---

### Ejemplo 2

Encontrar el término 10 de la PA $3, 7, 11, 15, ...$

$a_1 = 3$, $d = 4$

$$
a_{10} = 3 + (10-1) \cdot 4 = 3 + 36 = 39
$$

$$
\boxed{a_{10} = 39}
$$

---

### Ejemplo 3

Encontrar $a_{20}$ si $a_1 = 5$ y $d = -2$.

$$
a_{20} = 5 + 19(-2) = 5 - 38 = -33
$$

$$
\boxed{a_{20} = -33}
$$

---

## 📖 Suma de una PA

La suma de los primeros $n$ términos:

$$
S_n = \frac{n(a_1 + a_n)}{2} = \frac{n(2a_1 + (n-1)d)}{2}
$$

### Ejemplo 4

Sumar los primeros 10 términos de $1, 3, 5, 7, ...$

$a_1 = 1$, $d = 2$, $a_{10} = 1 + 9(2) = 19$

$$
S_{10} = \frac{10(1 + 19)}{2} = \frac{200}{2} = 100
$$

$$
\boxed{S_{10} = 100}
$$

---

### Ejemplo 5

Sumar: $2 + 5 + 8 + ... + 29$

$a_1 = 2$, $d = 3$, $a_n = 29$

Encontrar $n$: $29 = 2 + (n-1) \cdot 3$ → $n = 10$

$$
S_{10} = \frac{10(2 + 29)}{2} = 155
$$

$$
\boxed{S_{10} = 155}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra $a_8$ si $a_1 = 4$ y $d = 5$.

<details>
<summary>Ver solución</summary>

$a_8 = 4 + 7(5) = 39$

</details>

---

**Ejercicio 2:** Calcula la suma de los primeros 20 números naturales.

<details>
<summary>Ver solución</summary>

$S_{20} = \frac{20(1 + 20)}{2} = 210$

</details>

---

**Ejercicio 3:** ¿Cuál es la diferencia común de $10, 7, 4, 1, ...$?

<details>
<summary>Ver solución</summary>

$d = 7 - 10 = -3$

</details>

---

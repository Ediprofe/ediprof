# **Suma y Resta de Complejos**

Sumar números complejos es la operación más intuitiva que existe en este tema: simplemente seguimos la lógica de "peras con peras, manzanas con manzanas". Agrupamos lo real con lo real y lo imaginario con lo imaginario.

---

## 🎯 ¿Qué vas a aprender?

- Cómo sumar dos números complejos.
- Cómo restar números complejos (¡cuidado con los signos!).
- Cómo simplificar expresiones con paréntesis y signos negativos.
- Propiedades básicas de la suma y resta de conjugados.

---

## ➕ Regla de Suma y Resta

Para operar complejos, tratamos a la $i$ como si fuera una variable $x$ en álgebra:

1. **Sumas las Partes Reales** entre sí.
2. **Sumas las Partes Imaginarias** entre sí.

### **Fórmulas**

$$
(a + bi) + (c + di) = (a + c) + (b + d)i
$$

$$
(a + bi) - (c + di) = (a - c) + (b - d)i
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Suma Básica

Calcula $(3 + 2i) + (5 + 4i)$.

**Razonamiento:**
Agrupamos reales ($3+5$) y agrupamos imaginarios ($2+4$).

$$
(3 + 5) + (2 + 4)i
$$

**Resultado:**

$$
\boxed{8 + 6i}
$$

---

### Ejemplo 2: Resta (Distribución del Signo)

Calcula $(6 + 5i) - (2 + 3i)$.

**Razonamiento:**
El signo menos afecta a **todo** el paréntesis de la derecha. Es como multiplicar por -1.
$(6 + 5i) - 2 - 3i$.

Ahora agrupamos:
- Reales: $6 - 2 = 4$
- Imaginarios: $5i - 3i = 2i$

**Resultado:**

$$
\boxed{4 + 2i}
$$

---

### Ejemplo 3: Resta con Negativos

Calcula $(4 - 2i) - (-3 + 5i)$.

**Razonamiento:**
Cuidado con el doble negativo: $-(-3)$ se vuelve $+3$, y $-(+5i)$ se vuelve $-5i$.

$$
4 - 2i + 3 - 5i
$$

Agrupamos:
- Reales: $4 + 3 = 7$.
- Imaginarios: $-2i - 5i = -7i$.

**Resultado:**

$$
\boxed{7 - 7i}
$$

---

### Ejemplo 4: Suma con Conjugados

Suma $z = 3 + 4i$ con su conjugado $\bar{z} = 3 - 4i$.

**Razonamiento:**

$$
(3 + 4i) + (3 - 4i)
$$

Observa que las partes imaginarias ($4i$ y $-4i$) se cancelan.

$$
3 + 3
$$

**Resultado:**

$$
\boxed{6}
$$

> **Propiedad:** La suma de un complejo y su conjugado siempre es un número **real**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Suma $(2 + 3i) + (4 + i)$.

<details>
<summary>Ver solución</summary>

$$
(2+4) + (3+1)i = 6 + 4i
$$

**Resultado:** $\boxed{6 + 4i}$

</details>

---

### Ejercicio 2
Resta $(8 + 5i) - (2 + 2i)$.

<details>
<summary>Ver solución</summary>

$$
(8-2) + (5-2)i = 6 + 3i
$$

**Resultado:** $\boxed{6 + 3i}$

</details>

---

### Ejercicio 3
Suma $(-3 + 4i) + (5 - 6i)$.

<details>
<summary>Ver solución</summary>

$$
(-3+5) + (4-6)i = 2 - 2i
$$

**Resultado:** $\boxed{2 - 2i}$

</details>

---

### Ejercicio 4
Resta $(2 - i) - (5 - 3i)$.

<details>
<summary>Ver solución</summary>

$$
2 - i - 5 + 3i = -3 + 2i
$$

**Resultado:** $\boxed{-3 + 2i}$

</details>

---

### Ejercicio 5
Calcula $5 + (2 - 3i)$.

<details>
<summary>Ver solución</summary>

Solo sumamos la parte real.

$$
7 - 3i
$$

**Resultado:** $\boxed{7 - 3i}$

</details>

---

### Ejercicio 6
Calcula $(4i) - (3 - i)$.

<details>
<summary>Ver solución</summary>

$$
4i - 3 + i = -3 + 5i
$$

**Resultado:** $\boxed{-3 + 5i}$

</details>

---

### Ejercicio 7
Suma $(1/2 + 2i) + (3/2 - i)$.

<details>
<summary>Ver solución</summary>

Reales: $1/2 + 3/2 = 4/2 = 2$.
Imag: $2i - i = i$.

**Resultado:** $\boxed{2 + i}$

</details>

---

### Ejercicio 8
Simplifica $(3 + 2i) + (3 - 2i)$.

<details>
<summary>Ver solución</summary>

Solo la parte real se duplica.

$$
6
$$

**Resultado:** $\boxed{6}$

</details>

---

### Ejercicio 9
Simplifica $(4 + 5i) - (4 - 5i)$.

<details>
<summary>Ver solución</summary>

Los reales se cancelan. $5i - (-5i) = 10i$.

$$
10i
$$

**Resultado:** $\boxed{10i}$

</details>

---

### Ejercicio 10
Calcula $(2 + \sqrt{-9}) + (3 - \sqrt{-4})$.

<details>
<summary>Ver solución</summary>

Convertir primero: $(2 + 3i) + (3 - 2i)$.
Sumar: $(2+3) + (3-2)i$.

**Resultado:** $\boxed{5 + i}$

</details>

---

## 🔑 Resumen

| Operación | Clave | Ejemplo |
|:--- |:--- |:--- |
| **Suma** | Real+Real, Imag+Imag | $(1+i)+(2+i) = 3+2i$ |
| **Resta** | Distribuir signo y agrupar | $(2+i)-(1+i) = 1$ |
| **Conjugados (Suma)** | Se anula parte imaginaria | $z + \bar{z} = 2a$ (Real) |
| **Conjugados (Resta)** | Se anula parte real | $z - \bar{z} = 2bi$ (Imag) |

> **Conclusión:** El error más común en la resta es olvidar que el signo menos cambia **ambos** signos del segundo número. ¡Distribúyelo primero!

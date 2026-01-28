---
title: "División de Complejos"
---

# **División de Complejos**

Dividir números complejos parece imposible al principio: ¿cómo divides entre algo que tiene una parte imaginaria? El truco no es dividir, sino eliminar la parte imaginaria del denominador usando una herramienta que ya conoces: la **racionalización** con el conjugado.

---

## 🎯 ¿Qué vas a aprender?

- Cómo eliminar la $i$ del denominador.
- El uso del **conjugado** para dividir.
- Cómo dividir entre un imaginario puro.
- El algoritmo paso a paso para cualquier división.

---

## ➗ El Método del Conjugado

El objetivo es convertir el denominador en un simple número real.

Si tenemos $\frac{z_1}{z_2}$, multiplicamos arriba y abajo por $\bar{z_2}$ (el conjugado del denominador).

$$
\frac{a + bi}{c + di} \cdot \frac{c - di}{c - di}
$$

¿Por qué funciona? Porque en el denominador obtenemos una suma de cuadrados ($c^2 + d^2$), que **siempre es real**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: División Estándar

Calcula:

$$
\frac{3 + 2i}{1 + i}
$$

**Paso 1: Identificar el conjugado**
El denominador es $1 + i$. Su conjugado es $1 - i$.

**Paso 2: Multiplicar**

$$
\frac{3 + 2i}{1 + i} \cdot \frac{1 - i}{1 - i}
$$

**Paso 3: Operar**
- **Numerador (Propiedad distributiva):** $(3+2i)(1-i) = 3 - 3i + 2i - 2i^2 = 3 - i + 2 = 5 - i$.
- **Denominador (Suma Cuadrados):** $1^2 + 1^2 = 2$.

**Paso 4: Separar**

$$
\frac{5 - i}{2} = \frac{5}{2} - \frac{1}{2}i
$$

**Resultado:**

$$
\boxed{\frac{5}{2} - \frac{1}{2}i}
$$

---

### Ejemplo 2: Denominador Imaginario Puro

Calcula:

$$
\frac{10}{2i}
$$

**Razonamiento:**
Aquí no hace falta todo el conjugado complejo. Basta con multiplicar por $-i$ (o simplemente $i$) para eliminar la $i$.

$$
\frac{10}{2i} \cdot \frac{i}{i} = \frac{10i}{2i^2}
$$

$$
\frac{10i}{-2}
$$

**Resultado:**

$$
\boxed{-5i}
$$

---

### Ejemplo 3: División con Resultado Entero

Calcula:

$$
\frac{4 + 2i}{1 - i}
$$

**Paso 1: Conjugado**
Multiplicar por $1 + i$.

**Paso 2: Operar**
- **Numerador:** $(4+2i)(1+i) = 4 + 4i + 2i + 2i^2 = 4 + 6i - 2 = 2 + 6i$.
- **Denominador:** $1^2 + 1^2 = 2$.

**Paso 3: Simplificar**

$$
\frac{2 + 6i}{2} = \frac{2}{2} + \frac{6i}{2}
$$

**Resultado:**

$$
\boxed{1 + 3i}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\dfrac{2i}{1 + i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{2i(1-i)}{2} = \frac{2i - 2i^2}{2} = \frac{2 + 2i}{2} = 1 + i
$$

**Resultado:** $\boxed{1 + i}$

</details>

---

### Ejercicio 2
Calcula $\dfrac{5}{2 - i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{5(2+i)}{4+1} = \frac{10+5i}{5} = 2 + i
$$

**Resultado:** $\boxed{2 + i}$

</details>

---

### Ejercicio 3
Calcula $\dfrac{1 + 3i}{i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{(1+3i)(-i)}{1} = -i - 3i^2 = 3 - i
$$

**Resultado:** $\boxed{3 - i}$

</details>

---

### Ejercicio 4
Calcula $\dfrac{2 + 3i}{2 - 3i}$.

<details>
<summary>Ver solución</summary>

Numerador: $4 + 12i - 9 = -5 + 12i$.
Denominador: $4 + 9 = 13$.

**Resultado:** $\boxed{-\frac{5}{13} + \frac{12}{13}i}$

</details>

---

### Ejercicio 5
Calcula $\dfrac{4}{1 + i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{4(1-i)}{2} = 2(1-i) = 2 - 2i
$$

**Resultado:** $\boxed{2 - 2i}$

</details>

---

### Ejercicio 6
Calcula $\dfrac{8 + 6i}{2}$.

<details>
<summary>Ver solución</summary>

Directamente dividimos entre 2.

**Resultado:** $\boxed{4 + 3i}$

</details>

---

### Ejercicio 7
Calcula $\dfrac{3 - 4i}{3 + 4i}$.

<details>
<summary>Ver solución</summary>

Numerador: $(3-4i)^2 = 9 - 24i - 16 = -7 - 24i$.
Denominador: $25$.

**Resultado:** $\boxed{-\frac{7}{25} - \frac{24}{25}i}$

</details>

---

### Ejercicio 8
Calcula $\dfrac{10i}{1 + 2i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{10i(1-2i)}{5} = \frac{10i + 20}{5} = 4 + 2i
$$

**Resultado:** $\boxed{4 + 2i}$

</details>

---

### Ejercicio 9
Calcula $\dfrac{1}{i}$.

<details>
<summary>Ver solución</summary>

Multiplicar por $-i$.

**Resultado:** $\boxed{-i}$

</details>

---

### Ejercicio 10
Calcula $\dfrac{5 - 5i}{5}$.

<details>
<summary>Ver solución</summary>

Divide todo por 5.

**Resultado:** $\boxed{1 - i}$

</details>

---

## 🔑 Resumen

| Paso | Acción | ¿Por qué? |
|:--- |:--- |:--- |
| **1** | Hallar conjugado de abajo | Para eliminar la parte imaginaria. |
| **2** | Multiplicar arriba y abajo | Mantener la fracción equilibrada. |
| **3** | Simplificar denominador | Siempre será $a^2 + b^2$ (Real). |
| **4** | Separar partes | Dar formato estándar $a+bi$. |

> **Conclusión:** ¡En la división nunca dividimos de verdad! Solo multiplicamos estratégicamente para quitar el problema de abajo.

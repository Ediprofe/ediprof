# **Multiplicación y División de Imaginarios**

Hasta ahora hemos sumado y restado números imaginarios como si fueran una variable cualquiera (como $x$). Pero al multiplicar o dividir, sucede algo mágico: la $i$ puede desaparecer o transformarse en un número real negativo. Esto se debe a la propiedad fundamental que define a los números imaginarios: $i^2 = -1$.

---

## 🎯 ¿Qué vas a aprender?

- Cómo multiplicar dos números imaginarios puros.
- Por qué el resultado de multiplicar dos imaginarios es un **número real**.
- Cómo multiplicar un número real por un imaginario.
- Cómo dividir números imaginarios.

---

## ✖️ Multiplicación de Imaginarios

Cuando multiplicamos dos números imaginarios, multiplicamos los coeficientes (los números normales) y las $i$ por separado.

### **La Regla de Oro**

$$
(ai) \cdot (bi) = (a \cdot b) \cdot i^2
$$

Como $i^2 = -1$, el resultado final es:

$$
-ab
$$

> **¡Ojo!** El producto de dos números imaginarios puros es un **número real**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Multiplicación Simple

Calcula $(3i)(4i)$.

**Razonamiento:**
Multiplicamos $3 \times 4$ y $i \times i$.

$$
12 \cdot i^2
$$

Sustituimos $i^2 = -1$.

$$
12 \cdot (-1)
$$

**Resultado:**

$$
\boxed{-12}
$$

---

### Ejemplo 2: Con Signos Negativos

Calcula $(-5i)(2i)$.

**Razonamiento:**
$(-5) \times 2 = -10$.

$$
-10 \cdot i^2
$$

$$
-10 \cdot (-1)
$$

**Resultado:**

$$
\boxed{10}
$$

---

### Ejemplo 3: Real por Imaginario

Calcula $5 \cdot (3i)$.

**Razonamiento:**
Aquí solo hay una $i$. Multiplicamos los números y dejamos la $i$ quieta.

$$
(5 \cdot 3)i
$$

**Resultado:**

$$
\boxed{15i}
$$

---

### Ejemplo 4: Multiplicación de Raíces Negativas

Calcula $\sqrt{-4} \cdot \sqrt{-9}$.

**Paso Crítico:**
⚠️ **Nunca** multipliques los radicandos negativos directamente ($\sqrt{(-4)(-9)} \neq \sqrt{36}$).
Primero convierte a imaginarios.

**Paso 1: Convertir**
$\sqrt{-4} = 2i$
$\sqrt{-9} = 3i$

**Paso 2: Multiplicar**

$$
(2i)(3i) = 6i^2
$$

**Resultado:**

$$
\boxed{-6}
$$

---

## ➗ División de Imaginarios

Al dividir, las $i$ se pueden cancelar, dejando solo un número real.

### Ejemplo 5: División Simple

Calcula $\frac{12i}{4i}$.

**Razonamiento:**
Dividimos los números y cancelamos las $i$ (porque $i/i = 1$).

$$
\frac{12}{4} \cdot \frac{i}{i} = 3 \cdot 1
$$

**Resultado:**

$$
\boxed{3}
$$

---

### Ejemplo 6: División Real entre Imaginario

Calcula $\frac{10}{2i}$.

**Razonamiento:**
Tenemos una $i$ en el denominador. Para quitarla, multiplicamos arriba y abajo por $i$ (racionalización).

$$
\frac{10}{2i} \cdot \frac{i}{i} = \frac{10i}{2i^2}
$$

$$
\frac{10i}{2(-1)} = \frac{10i}{-2}
$$

**Resultado:**

$$
\boxed{-5i}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $(2i)(5i)$.

<details>
<summary>Ver solución</summary>

$$
10i^2 = -10
$$

**Resultado:** $\boxed{-10}$

</details>

---

### Ejercicio 2
Calcula $(-3i)(4i)$.

<details>
<summary>Ver solución</summary>

$$
-12i^2 = -12(-1) = 12
$$

**Resultado:** $\boxed{12}$

</details>

---

### Ejercicio 3
Calcula $(-6i)(-2i)$.

<details>
<summary>Ver solución</summary>

$$
12i^2 = -12
$$

**Resultado:** $\boxed{-12}$

</details>

---

### Ejercicio 4
Calcula $4(3i)$.

<details>
<summary>Ver solución</summary>

$$
12i
$$

**Resultado:** $\boxed{12i}$

</details>

---

### Ejercicio 5
Calcula $\sqrt{-25} \cdot \sqrt{-4}$.

<details>
<summary>Ver solución</summary>

$$
(5i)(2i) = 10i^2 = -10
$$

**Resultado:** $\boxed{-10}$

</details>

---

### Ejercicio 6
Divide $\frac{20i}{5i}$.

<details>
<summary>Ver solución</summary>

Se cancelan las $i$.

$$
20 / 5 = 4
$$

**Resultado:** $\boxed{4}$

</details>

---

### Ejercicio 7
Divide $\frac{8i}{-2i}$.

<details>
<summary>Ver solución</summary>

$$
8 / -2 = -4
$$

**Resultado:** $\boxed{-4}$

</details>

---

### Ejercicio 8
Divide $\frac{6}{3i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{6i}{3i^2} = \frac{6i}{-3} = -2i
$$

**Resultado:** $\boxed{-2i}$

</details>

---

### Ejercicio 9
Calcula $(i\sqrt{2})(i\sqrt{8})$.

<details>
<summary>Ver solución</summary>

$$
i^2 \sqrt{16} = (-1)(4) = -4
$$

**Resultado:** $\boxed{-4}$

</details>

---

### Ejercicio 10
Calcula $(3i)^2$.

<details>
<summary>Ver solución</summary>

$$
3^2 \cdot i^2 = 9(-1) = -9
$$

**Resultado:** $\boxed{-9}$

</details>

---

## 🔑 Resumen

| Operación | Fórmula | Resultado Típico |
|:--- |:--- |:--- |
| **Imag $\times$ Imag** | $(ai)(bi) = ab \cdot i^2$ | Real (signo invertido) |
| **Real $\times$ Imag** | $a(bi)$ | Imaginario |
| **Imag / Imag** | $\frac{ai}{bi}$ | Real |
| **Real / Imag** | $\frac{a}{bi}$ | Imaginario (con signo invertido) |

> **Conclusión:** La clave siempre es recordar que **cada par de $i$ que se multiplican se convierten en un -1**.

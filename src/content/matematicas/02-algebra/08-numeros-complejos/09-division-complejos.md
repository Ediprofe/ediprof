# ➗ División de Números Complejos

En esta lección aprenderemos a dividir números complejos usando el conjugado del denominador.

---

## 📖 Método de división

Para dividir números complejos, multiplicamos numerador y denominador por el **conjugado** del denominador:

$$
\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(a + bi)(c - di)}{c^2 + d^2}
$$

Esto funciona porque $(c + di)(c - di) = c^2 + d^2$, que es un número real.

---

### Ejemplo 1

Calcular $\dfrac{3 + 2i}{1 + i}$.

**Paso 1:** El conjugado de $1 + i$ es $1 - i$.

**Paso 2:** Multiplicamos:

$$
\frac{3 + 2i}{1 + i} \cdot \frac{1 - i}{1 - i} = \frac{(3 + 2i)(1 - i)}{(1 + i)(1 - i)}
$$

**Paso 3:** Calculamos el numerador:

$$
(3 + 2i)(1 - i) = 3 - 3i + 2i - 2i^2 = 3 - i + 2 = 5 - i
$$

**Paso 4:** Calculamos el denominador:

$$
(1 + i)(1 - i) = 1 + 1 = 2
$$

**Paso 5:** Dividimos:

$$
\frac{5 - i}{2} = \frac{5}{2} - \frac{1}{2}i
$$

$$
\boxed{\frac{3 + 2i}{1 + i} = \frac{5}{2} - \frac{1}{2}i}
$$

---

### Ejemplo 2

Calcular $\dfrac{4 + 3i}{2 - i}$.

$$
\frac{4 + 3i}{2 - i} \cdot \frac{2 + i}{2 + i} = \frac{(4 + 3i)(2 + i)}{(2 - i)(2 + i)}
$$

Numerador:

$$
(4 + 3i)(2 + i) = 8 + 4i + 6i + 3i^2 = 8 + 10i - 3 = 5 + 10i
$$

Denominador:

$$
4 + 1 = 5
$$

$$
\frac{5 + 10i}{5} = 1 + 2i
$$

$$
\boxed{\frac{4 + 3i}{2 - i} = 1 + 2i}
$$

---

### Ejemplo 3

Calcular $\dfrac{5}{2 + 3i}$.

$$
\frac{5}{2 + 3i} \cdot \frac{2 - 3i}{2 - 3i} = \frac{5(2 - 3i)}{4 + 9} = \frac{10 - 15i}{13}
$$

$$
= \frac{10}{13} - \frac{15}{13}i
$$

$$
\boxed{\frac{5}{2 + 3i} = \frac{10}{13} - \frac{15}{13}i}
$$

---

### Ejemplo 4

Calcular $\dfrac{2i}{3 + 4i}$.

$$
\frac{2i}{3 + 4i} \cdot \frac{3 - 4i}{3 - 4i} = \frac{2i(3 - 4i)}{9 + 16} = \frac{6i - 8i^2}{25}
$$

$$
= \frac{6i + 8}{25} = \frac{8}{25} + \frac{6}{25}i
$$

$$
\boxed{\frac{2i}{3 + 4i} = \frac{8}{25} + \frac{6}{25}i}
$$

---

### Ejemplo 5

Calcular $\dfrac{1 + i}{1 - i}$.

$$
\frac{1 + i}{1 - i} \cdot \frac{1 + i}{1 + i} = \frac{(1 + i)^2}{1 + 1} = \frac{1 + 2i + i^2}{2}
$$

$$
= \frac{1 + 2i - 1}{2} = \frac{2i}{2} = i
$$

$$
\boxed{\frac{1 + i}{1 - i} = i}
$$

---

### Ejemplo 6

Calcular $\dfrac{3 - 4i}{3 + 4i}$.

$$
\frac{(3 - 4i)^2}{(3 + 4i)(3 - 4i)} = \frac{9 - 24i + 16i^2}{9 + 16}
$$

$$
= \frac{9 - 24i - 16}{25} = \frac{-7 - 24i}{25}
$$

$$
= -\frac{7}{25} - \frac{24}{25}i
$$

$$
\boxed{\frac{3 - 4i}{3 + 4i} = -\frac{7}{25} - \frac{24}{25}i}
$$

---

### Ejemplo 7

Calcular $\dfrac{6 + 8i}{2}$.

Cuando el denominador es real, simplemente dividimos cada parte:

$$
\frac{6 + 8i}{2} = \frac{6}{2} + \frac{8}{2}i = 3 + 4i
$$

$$
\boxed{\frac{6 + 8i}{2} = 3 + 4i}
$$

---

### Ejemplo 8

Calcular $\dfrac{10 - 5i}{5i}$.

$$
\frac{10 - 5i}{5i} \cdot \frac{-i}{-i} = \frac{(10 - 5i)(-i)}{5i(-i)} = \frac{-10i + 5i^2}{-5i^2}
$$

$$
= \frac{-10i - 5}{5} = \frac{-5 - 10i}{5} = -1 - 2i
$$

$$
\boxed{\frac{10 - 5i}{5i} = -1 - 2i}
$$

---

## 📋 Resumen del método

1. Identificar el conjugado del denominador
2. Multiplicar numerador y denominador por el conjugado
3. Simplificar el numerador usando $i^2 = -1$
4. El denominador se convierte en $c^2 + d^2$
5. Separar en parte real e imaginaria

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $\dfrac{5 + 3i}{2 + i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{(5 + 3i)(2 - i)}{5} = \frac{10 - 5i + 6i - 3i^2}{5} = \frac{13 + i}{5} = \frac{13}{5} + \frac{1}{5}i
$$

</details>

---

**Ejercicio 2:** Calcula $\dfrac{4}{1 - 2i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{4(1 + 2i)}{1 + 4} = \frac{4 + 8i}{5} = \frac{4}{5} + \frac{8}{5}i
$$

</details>

---

**Ejercicio 3:** Calcula $\dfrac{2 + i}{3 - 2i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{(2 + i)(3 + 2i)}{9 + 4} = \frac{6 + 4i + 3i + 2i^2}{13} = \frac{4 + 7i}{13}
$$

</details>

---

**Ejercicio 4:** Calcula $\dfrac{i}{1 + i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{i(1 - i)}{2} = \frac{i - i^2}{2} = \frac{i + 1}{2} = \frac{1}{2} + \frac{1}{2}i
$$

</details>

---

**Ejercicio 5:** Calcula $\dfrac{2 - 3i}{2 + 3i}$.

<details>
<summary>Ver solución</summary>

$$
\frac{(2 - 3i)^2}{13} = \frac{4 - 12i + 9i^2}{13} = \frac{-5 - 12i}{13}
$$

</details>

---

**Ejercicio 6:** Calcula $\dfrac{8 + 6i}{4}$.

<details>
<summary>Ver solución</summary>

$$
2 + \frac{3}{2}i
$$

</details>

---

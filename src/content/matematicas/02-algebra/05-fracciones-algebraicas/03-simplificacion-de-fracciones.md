# ✂️ Simplificación de Fracciones Algebraicas

En esta lección aprenderemos a simplificar fracciones algebraicas, reduciendo las expresiones a su forma más simple mediante la cancelación de factores comunes.

---

## 📖 ¿Qué es una fracción algebraica?

Una **fracción algebraica** es el cociente de dos expresiones algebraicas (polinomios), donde el denominador no puede ser cero.

$$
\frac{P(x)}{Q(x)} \quad \text{donde } Q(x) \neq 0
$$

### Ejemplos de fracciones algebraicas

| Fracción | Numerador | Denominador |
|:--------:|:---------:|:-----------:|
| $\dfrac{3x}{x+1}$ | $3x$ | $x+1$ |
| $\dfrac{x^2-4}{x-2}$ | $x^2-4$ | $x-2$ |
| $\dfrac{2a+6}{a^2-9}$ | $2a+6$ | $a^2-9$ |

---

## 📖 Principio fundamental de las fracciones

Podemos **multiplicar** o **dividir** el numerador y el denominador por una misma expresión (distinta de cero) sin cambiar el valor de la fracción:

$$
\frac{a}{b} = \frac{a \cdot c}{b \cdot c} = \frac{a \div c}{b \div c}
$$

Este principio nos permite **simplificar** fracciones.

---

## 📖 Simplificación de fracciones algebraicas

**Simplificar** una fracción algebraica significa reducirla a su expresión más simple, cancelando los factores comunes entre el numerador y el denominador.

### Pasos para simplificar

1. **Factorizar** completamente el numerador
2. **Factorizar** completamente el denominador
3. **Cancelar** los factores comunes
4. **Escribir** la fracción simplificada

---

## 📖 Simplificación con monomios

### Ejemplo 1

Simplificar $\dfrac{12x^3y^2}{18x^2y^4}$.

**Solución:**

**Paso 1:** Simplificamos coeficientes: $\dfrac{12}{18} = \dfrac{2}{3}$

**Paso 2:** Simplificamos variables usando las propiedades de exponentes:

$$
\frac{x^3}{x^2} = x^{3-2} = x
$$

$$
\frac{y^2}{y^4} = y^{2-4} = y^{-2} = \frac{1}{y^2}
$$

**Resultado:**

$$
\boxed{\frac{12x^3y^2}{18x^2y^4} = \frac{2x}{3y^2}}
$$

---

### Ejemplo 2

Simplificar $\dfrac{15a^4b^3}{25a^2b^5}$.

**Solución:**

$$
\frac{15}{25} = \frac{3}{5}, \quad \frac{a^4}{a^2} = a^2, \quad \frac{b^3}{b^5} = \frac{1}{b^2}
$$

$$
\boxed{\frac{15a^4b^3}{25a^2b^5} = \frac{3a^2}{5b^2}}
$$

---

### Ejemplo 3

Simplificar $\dfrac{8x^2y^3z}{4xy^2z^3}$.

**Solución:**

$$
\frac{8}{4} = 2, \quad \frac{x^2}{x} = x, \quad \frac{y^3}{y^2} = y, \quad \frac{z}{z^3} = \frac{1}{z^2}
$$

$$
\boxed{\frac{8x^2y^3z}{4xy^2z^3} = \frac{2xy}{z^2}}
$$

---

## 📖 Simplificación con factor común

### Ejemplo 4

Simplificar $\dfrac{6x + 12}{3x + 6}$.

**Paso 1:** Factorizamos numerador y denominador:

$$
\frac{6x + 12}{3x + 6} = \frac{6(x + 2)}{3(x + 2)}
$$

**Paso 2:** Cancelamos el factor común $(x + 2)$:

$$
= \frac{6}{3} = 2
$$

$$
\boxed{\frac{6x + 12}{3x + 6} = 2}
$$

---

### Ejemplo 5

Simplificar $\dfrac{4x^2 + 8x}{2x}$.

**Paso 1:** Factorizamos el numerador:

$$
\frac{4x^2 + 8x}{2x} = \frac{4x(x + 2)}{2x}
$$

**Paso 2:** Cancelamos el factor común $2x$:

$$
= \frac{2(x + 2)}{1} = 2(x + 2) = 2x + 4
$$

$$
\boxed{\frac{4x^2 + 8x}{2x} = 2x + 4}
$$

---

### Ejemplo 6

Simplificar $\dfrac{x^3 - x^2}{x^2 - x}$.

**Paso 1:** Factorizamos:

$$
\frac{x^3 - x^2}{x^2 - x} = \frac{x^2(x - 1)}{x(x - 1)}
$$

**Paso 2:** Cancelamos los factores comunes $x$ y $(x - 1)$:

$$
= \frac{x^2}{x} = x
$$

$$
\boxed{\frac{x^3 - x^2}{x^2 - x} = x}
$$

---

## 📖 Simplificación con productos notables

### Ejemplo 7

Simplificar $\dfrac{x^2 - 4}{x + 2}$.

**Paso 1:** Reconocemos la diferencia de cuadrados en el numerador:

$$
\frac{x^2 - 4}{x + 2} = \frac{(x + 2)(x - 2)}{x + 2}
$$

**Paso 2:** Cancelamos $(x + 2)$:

$$
= x - 2
$$

$$
\boxed{\frac{x^2 - 4}{x + 2} = x - 2}
$$

---

### Ejemplo 8

Simplificar $\dfrac{x^2 - 9}{x^2 + 6x + 9}$.

**Paso 1:** Factorizamos:

$$
x^2 - 9 = (x + 3)(x - 3)
$$

$$
x^2 + 6x + 9 = (x + 3)^2
$$

**Paso 2:** Escribimos y cancelamos:

$$
\frac{(x + 3)(x - 3)}{(x + 3)^2} = \frac{x - 3}{x + 3}
$$

$$
\boxed{\frac{x^2 - 9}{x^2 + 6x + 9} = \frac{x - 3}{x + 3}}
$$

---

### Ejemplo 9

Simplificar $\dfrac{x^2 - 4x + 4}{x^2 - 4}$.

**Paso 1:** Factorizamos:

$$
x^2 - 4x + 4 = (x - 2)^2
$$

$$
x^2 - 4 = (x + 2)(x - 2)
$$

**Paso 2:** Cancelamos $(x - 2)$:

$$
\frac{(x - 2)^2}{(x + 2)(x - 2)} = \frac{x - 2}{x + 2}
$$

$$
\boxed{\frac{x^2 - 4x + 4}{x^2 - 4} = \frac{x - 2}{x + 2}}
$$

---

### Ejemplo 10

Simplificar $\dfrac{x^2 + 5x + 6}{x^2 + 4x + 4}$.

**Paso 1:** Factorizamos:

$$
x^2 + 5x + 6 = (x + 2)(x + 3)
$$

$$
x^2 + 4x + 4 = (x + 2)^2
$$

**Paso 2:** Cancelamos $(x + 2)$:

$$
\frac{(x + 2)(x + 3)}{(x + 2)^2} = \frac{x + 3}{x + 2}
$$

$$
\boxed{\frac{x^2 + 5x + 6}{x^2 + 4x + 4} = \frac{x + 3}{x + 2}}
$$

---

## ⚠️ Errores comunes a evitar

### Error 1: Cancelar términos en lugar de factores

❌ **Incorrecto:**
$$
\frac{x + 2}{x + 3} \neq \frac{2}{3}
$$

No se pueden cancelar los términos $x$ porque no son factores.

✅ **Solo se cancelan FACTORES, no términos.**

---

### Error 2: Cancelar sin verificar que es factor

❌ **Incorrecto:**
$$
\frac{x^2 + 4}{x + 2} \neq x + 2
$$

El numerador $x^2 + 4$ **no se puede factorizar** como $(x+2)(\text{algo})$.

---

## 📝 Ejercicios de práctica

### Simplificación de monomios

**Ejercicio 1:** Simplifica $\dfrac{24a^3b^2}{36a^2b^4}$.

<details>
<summary>Ver solución</summary>

$$
\frac{24}{36} = \frac{2}{3}, \quad \frac{a^3}{a^2} = a, \quad \frac{b^2}{b^4} = \frac{1}{b^2}
$$

$$
\frac{24a^3b^2}{36a^2b^4} = \frac{2a}{3b^2}
$$

</details>

---

**Ejercicio 2:** Simplifica $\dfrac{9x^2 + 18x}{3x}$.

<details>
<summary>Ver solución</summary>

$$
\frac{9x^2 + 18x}{3x} = \frac{9x(x + 2)}{3x} = 3(x + 2) = 3x + 6
$$

</details>

---

### Simplificación con productos notables

**Ejercicio 3:** Simplifica $\dfrac{x^2 - 16}{x + 4}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x^2 - 16}{x + 4} = \frac{(x + 4)(x - 4)}{x + 4} = x - 4
$$

</details>

---

**Ejercicio 4:** Simplifica $\dfrac{x^2 - 6x + 9}{x^2 - 9}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x^2 - 6x + 9}{x^2 - 9} = \frac{(x - 3)^2}{(x + 3)(x - 3)} = \frac{x - 3}{x + 3}
$$

</details>

---

**Ejercicio 5:** Simplifica $\dfrac{x^2 + 7x + 12}{x^2 + 6x + 9}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x^2 + 7x + 12}{x^2 + 6x + 9} = \frac{(x + 3)(x + 4)}{(x + 3)^2} = \frac{x + 4}{x + 3}
$$

</details>

---

**Ejercicio 6:** Simplifica $\dfrac{2x^2 - 8}{x^2 + 4x + 4}$.

<details>
<summary>Ver solución</summary>

$$
\frac{2x^2 - 8}{x^2 + 4x + 4} = \frac{2(x^2 - 4)}{(x + 2)^2} = \frac{2(x + 2)(x - 2)}{(x + 2)^2} = \frac{2(x - 2)}{x + 2}
$$

</details>

---

# 🔀 Combinación de Operaciones

En esta lección aprenderemos a resolver ejercicios que combinan suma, resta, multiplicación y división de fracciones algebraicas.

---

## 📖 Orden de las operaciones

Al combinar operaciones con fracciones algebraicas, debemos seguir la **jerarquía de operaciones**:

1. **Paréntesis** primero
2. **Multiplicación y división** (de izquierda a derecha)
3. **Suma y resta** (de izquierda a derecha)

---

## 📖 Multiplicación y división combinadas

### Ejemplo 1

Resolver $\dfrac{x^2-4}{x+1} \times \dfrac{x+1}{x+2} \div \dfrac{x-2}{3}$.

**Paso 1:** Convertimos la división en multiplicación:

$$
\frac{x^2-4}{x+1} \times \frac{x+1}{x+2} \times \frac{3}{x-2}
$$

**Paso 2:** Factorizamos $x^2-4 = (x+2)(x-2)$:

$$
\frac{(x+2)(x-2)}{x+1} \times \frac{x+1}{x+2} \times \frac{3}{x-2}
$$

**Paso 3:** Cancelamos:

$$
= \frac{\cancel{(x+2)}\cancel{(x-2)}}{\cancel{x+1}} \times \frac{\cancel{x+1}}{\cancel{x+2}} \times \frac{3}{\cancel{x-2}} = 3
$$

$$
\boxed{\frac{x^2-4}{x+1} \times \frac{x+1}{x+2} \div \frac{x-2}{3} = 3}
$$

---

### Ejemplo 2

Resolver $\dfrac{x+3}{x-2} \div \dfrac{x+3}{x+2} \times \dfrac{x-2}{x+2}$.

**Paso 1:** Resolvemos de izquierda a derecha. Primero la división:

$$
\frac{x+3}{x-2} \times \frac{x+2}{x+3} = \frac{x+2}{x-2}
$$

**Paso 2:** Ahora multiplicamos:

$$
\frac{x+2}{x-2} \times \frac{x-2}{x+2} = 1
$$

$$
\boxed{\frac{x+3}{x-2} \div \frac{x+3}{x+2} \times \frac{x-2}{x+2} = 1}
$$

---

## 📖 Suma y resta combinadas

### Ejemplo 3

Resolver $\dfrac{2}{x} + \dfrac{3}{x+1} - \dfrac{1}{x}$.

**Paso 1:** Agrupamos las fracciones con denominador $x$:

$$
\left(\frac{2}{x} - \frac{1}{x}\right) + \frac{3}{x+1} = \frac{1}{x} + \frac{3}{x+1}
$$

**Paso 2:** El MCM de $x$ y $x+1$ es $x(x+1)$:

$$
\frac{x+1}{x(x+1)} + \frac{3x}{x(x+1)} = \frac{x + 1 + 3x}{x(x+1)} = \frac{4x + 1}{x(x+1)}
$$

$$
\boxed{\frac{2}{x} + \frac{3}{x+1} - \frac{1}{x} = \frac{4x + 1}{x(x+1)}}
$$

---

### Ejemplo 4

Resolver $\dfrac{1}{x-1} - \dfrac{2}{x+1} + \dfrac{1}{x^2-1}$.

**Paso 1:** Factorizamos $x^2-1 = (x+1)(x-1)$, que es el MCM.

**Paso 2:** Convertimos todas las fracciones:

$$
\frac{x+1}{(x-1)(x+1)} - \frac{2(x-1)}{(x-1)(x+1)} + \frac{1}{(x-1)(x+1)}
$$

**Paso 3:** Operamos:

$$
= \frac{(x+1) - 2(x-1) + 1}{(x-1)(x+1)} = \frac{x + 1 - 2x + 2 + 1}{x^2-1}
$$

$$
= \frac{-x + 4}{x^2-1} = \frac{4 - x}{x^2-1}
$$

$$
\boxed{\frac{1}{x-1} - \frac{2}{x+1} + \frac{1}{x^2-1} = \frac{4-x}{x^2-1}}
$$

---

## 📖 Las cuatro operaciones

### Ejemplo 5

Resolver $\dfrac{x+2}{x-1} + \dfrac{x-2}{x-1} \times \dfrac{x-1}{x+2}$.

**Paso 1:** Por jerarquía, primero resolvemos la multiplicación:

$$
\frac{x-2}{x-1} \times \frac{x-1}{x+2} = \frac{x-2}{x+2}
$$

**Paso 2:** Ahora sumamos:

$$
\frac{x+2}{x-1} + \frac{x-2}{x+2}
$$

**Paso 3:** El MCM es $(x-1)(x+2)$:

$$
\frac{(x+2)^2}{(x-1)(x+2)} + \frac{(x-2)(x-1)}{(x-1)(x+2)}
$$

$$
= \frac{(x+2)^2 + (x-2)(x-1)}{(x-1)(x+2)}
$$

**Paso 4:** Expandimos:

$$
(x+2)^2 = x^2 + 4x + 4
$$

$$
(x-2)(x-1) = x^2 - 3x + 2
$$

$$
= \frac{x^2 + 4x + 4 + x^2 - 3x + 2}{(x-1)(x+2)} = \frac{2x^2 + x + 6}{(x-1)(x+2)}
$$

$$
\boxed{\frac{x+2}{x-1} + \frac{x-2}{x-1} \times \frac{x-1}{x+2} = \frac{2x^2 + x + 6}{(x-1)(x+2)}}
$$

---

### Ejemplo 6

Resolver $\dfrac{x^2-9}{x} \div \dfrac{x+3}{2} - \dfrac{x-3}{1}$.

**Paso 1:** Primero resolvemos la división:

$$
\frac{x^2-9}{x} \times \frac{2}{x+3} = \frac{(x+3)(x-3)}{x} \times \frac{2}{x+3} = \frac{2(x-3)}{x}
$$

**Paso 2:** Ahora restamos:

$$
\frac{2(x-3)}{x} - (x-3) = \frac{2(x-3)}{x} - \frac{x(x-3)}{x}
$$

$$
= \frac{2(x-3) - x(x-3)}{x} = \frac{(x-3)(2-x)}{x}
$$

$$
\boxed{\frac{x^2-9}{x} \div \frac{x+3}{2} - (x-3) = \frac{(x-3)(2-x)}{x}}
$$

---

### Ejemplo 7

Resolver $\left(\dfrac{1}{x} + \dfrac{1}{y}\right) \times xy$.

**Paso 1:** Resolvemos primero el paréntesis:

$$
\frac{1}{x} + \frac{1}{y} = \frac{y + x}{xy}
$$

**Paso 2:** Multiplicamos:

$$
\frac{x + y}{xy} \times xy = x + y
$$

$$
\boxed{\left(\frac{1}{x} + \frac{1}{y}\right) \times xy = x + y}
$$

---

### Ejemplo 8

Resolver $\left(\dfrac{x+1}{x-1} - \dfrac{x-1}{x+1}\right) \div \dfrac{4x}{x^2-1}$.

**Paso 1:** Resolvemos el paréntesis con MCM $(x-1)(x+1)$:

$$
\frac{(x+1)^2 - (x-1)^2}{(x-1)(x+1)}
$$

Expandimos:

$$
(x+1)^2 = x^2 + 2x + 1
$$

$$
(x-1)^2 = x^2 - 2x + 1
$$

$$
= \frac{x^2 + 2x + 1 - x^2 + 2x - 1}{x^2-1} = \frac{4x}{x^2-1}
$$

**Paso 2:** Dividimos:

$$
\frac{4x}{x^2-1} \div \frac{4x}{x^2-1} = 1
$$

$$
\boxed{\left(\frac{x+1}{x-1} - \frac{x-1}{x+1}\right) \div \frac{4x}{x^2-1} = 1}
$$

---

## 📖 Con tres o más términos

### Ejemplo 9

Resolver $\dfrac{a}{a+b} + \dfrac{b}{a-b} - \dfrac{2ab}{a^2-b^2}$.

**Paso 1:** El MCM es $a^2-b^2 = (a+b)(a-b)$.

**Paso 2:** Convertimos:

$$
\frac{a(a-b)}{(a+b)(a-b)} + \frac{b(a+b)}{(a+b)(a-b)} - \frac{2ab}{(a+b)(a-b)}
$$

**Paso 3:** Operamos el numerador:

$$
= \frac{a(a-b) + b(a+b) - 2ab}{a^2-b^2}
$$

$$
= \frac{a^2 - ab + ab + b^2 - 2ab}{a^2-b^2} = \frac{a^2 - 2ab + b^2}{a^2-b^2}
$$

$$
= \frac{(a-b)^2}{(a+b)(a-b)} = \frac{a-b}{a+b}
$$

$$
\boxed{\frac{a}{a+b} + \frac{b}{a-b} - \frac{2ab}{a^2-b^2} = \frac{a-b}{a+b}}
$$

---

### Ejemplo 10

Resolver $\dfrac{1}{x} \times \dfrac{x}{x+1} + \dfrac{1}{x+1} \times \dfrac{x+1}{x+2}$.

**Paso 1:** Resolvemos cada multiplicación:

$$
\frac{1}{x} \times \frac{x}{x+1} = \frac{1}{x+1}
$$

$$
\frac{1}{x+1} \times \frac{x+1}{x+2} = \frac{1}{x+2}
$$

**Paso 2:** Sumamos:

$$
\frac{1}{x+1} + \frac{1}{x+2} = \frac{(x+2) + (x+1)}{(x+1)(x+2)} = \frac{2x + 3}{(x+1)(x+2)}
$$

$$
\boxed{\frac{1}{x} \times \frac{x}{x+1} + \frac{1}{x+1} \times \frac{x+1}{x+2} = \frac{2x+3}{(x+1)(x+2)}}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $\dfrac{x+1}{x} \times \dfrac{x}{x-1} \div \dfrac{x+1}{x-1}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x+1}{x} \times \frac{x}{x-1} \times \frac{x-1}{x+1} = 1
$$

</details>

---

**Ejercicio 2:** Resuelve $\dfrac{3}{x-2} + \dfrac{2}{x+2} - \dfrac{5x}{x^2-4}$.

<details>
<summary>Ver solución</summary>

MCM = $(x-2)(x+2)$:

$$
\frac{3(x+2) + 2(x-2) - 5x}{x^2-4} = \frac{3x + 6 + 2x - 4 - 5x}{x^2-4} = \frac{2}{x^2-4}
$$

</details>

---

**Ejercicio 3:** Resuelve $\left(\dfrac{2}{x} - \dfrac{1}{x+1}\right) \times x(x+1)$.

<details>
<summary>Ver solución</summary>

Primero el paréntesis:

$$
\frac{2(x+1) - x}{x(x+1)} = \frac{2x + 2 - x}{x(x+1)} = \frac{x + 2}{x(x+1)}
$$

Multiplicamos: $\dfrac{x+2}{x(x+1)} \times x(x+1) = x + 2$

</details>

---

**Ejercicio 4:** Resuelve $\dfrac{x^2-1}{x} \div \dfrac{x-1}{2} + \dfrac{x+1}{x}$.

<details>
<summary>Ver solución</summary>

Primero la división:

$$
\frac{(x+1)(x-1)}{x} \times \frac{2}{x-1} = \frac{2(x+1)}{x}
$$

Sumamos:

$$
\frac{2(x+1)}{x} + \frac{x+1}{x} = \frac{3(x+1)}{x}
$$

</details>

---

**Ejercicio 5:** Resuelve $\dfrac{a+b}{a} \times \dfrac{a}{a-b} - \dfrac{2b}{a-b}$.

<details>
<summary>Ver solución</summary>

$$
\frac{a+b}{a-b} - \frac{2b}{a-b} = \frac{a + b - 2b}{a-b} = \frac{a - b}{a-b} = 1
$$

</details>

---

**Ejercicio 6:** Resuelve $\left(\dfrac{x}{x+2} + \dfrac{x}{x-2}\right) \div \dfrac{2x^2}{x^2-4}$.

<details>
<summary>Ver solución</summary>

Paréntesis:

$$
\frac{x(x-2) + x(x+2)}{x^2-4} = \frac{x^2 - 2x + x^2 + 2x}{x^2-4} = \frac{2x^2}{x^2-4}
$$

División:

$$
\frac{2x^2}{x^2-4} \div \frac{2x^2}{x^2-4} = 1
$$

</details>

---

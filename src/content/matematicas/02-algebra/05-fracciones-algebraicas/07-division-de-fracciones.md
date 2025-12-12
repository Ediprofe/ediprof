# ➗ División de Fracciones Algebraicas

En esta lección aprenderemos a dividir fracciones algebraicas, una operación que se reduce a una multiplicación por el recíproco.

---

## 📖 Regla de división

Para dividir fracciones, se multiplica la primera por el **recíproco** (o inverso) de la segunda:

$$
\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{ad}{bc}
$$

En otras palabras: **invertimos la segunda fracción y multiplicamos**.

---

## 📖 División de monomios

### Ejemplo 1

Resolver $\dfrac{6x^3}{5y^2} \div \dfrac{3x}{10y}$.

**Paso 1:** Invertimos la segunda fracción:

$$
\frac{6x^3}{5y^2} \times \frac{10y}{3x}
$$

**Paso 2:** Multiplicamos y simplificamos:

$$
= \frac{6x^3 \cdot 10y}{5y^2 \cdot 3x} = \frac{60x^3y}{15xy^2} = \frac{4x^2}{y}
$$

$$
\boxed{\frac{6x^3}{5y^2} \div \frac{3x}{10y} = \frac{4x^2}{y}}
$$

---

### Ejemplo 2

Resolver $\dfrac{12a^2b^3}{7c} \div \dfrac{4ab^2}{21c^2}$.

**Solución:**

$$
\frac{12a^2b^3}{7c} \times \frac{21c^2}{4ab^2} = \frac{12a^2b^3 \cdot 21c^2}{7c \cdot 4ab^2}
$$

$$
= \frac{252a^2b^3c^2}{28abc} = \frac{9abc}{1} = 9abc
$$

$$
\boxed{\frac{12a^2b^3}{7c} \div \frac{4ab^2}{21c^2} = 9abc}
$$

---

### Ejemplo 3

Resolver $\dfrac{15x^4y}{8z^2} \div \dfrac{5x^2y^3}{4z}$.

**Solución:**

$$
\frac{15x^4y}{8z^2} \times \frac{4z}{5x^2y^3} = \frac{15x^4y \cdot 4z}{8z^2 \cdot 5x^2y^3}
$$

$$
= \frac{60x^4yz}{40x^2y^3z^2} = \frac{3x^2}{2y^2z}
$$

$$
\boxed{\frac{15x^4y}{8z^2} \div \frac{5x^2y^3}{4z} = \frac{3x^2}{2y^2z}}
$$

---

## 📖 División con polinomios

### Ejemplo 4

Resolver $\dfrac{x+3}{4} \div \dfrac{x+3}{8}$.

**Solución:**

$$
\frac{x+3}{4} \times \frac{8}{x+3} = \frac{(x+3) \cdot 8}{4 \cdot (x+3)} = \frac{8}{4} = 2
$$

$$
\boxed{\frac{x+3}{4} \div \frac{x+3}{8} = 2}
$$

---

### Ejemplo 5

Resolver $\dfrac{x^2-4}{x+1} \div \dfrac{x-2}{x+1}$.

**Paso 1:** Invertimos y escribimos:

$$
\frac{x^2-4}{x+1} \times \frac{x+1}{x-2}
$$

**Paso 2:** Factorizamos $x^2-4 = (x+2)(x-2)$:

$$
= \frac{(x+2)(x-2)}{x+1} \times \frac{x+1}{x-2}
$$

**Paso 3:** Cancelamos $(x+1)$ y $(x-2)$:

$$
= \frac{(x+2)\cancel{(x-2)}}{\cancel{x+1}} \times \frac{\cancel{x+1}}{\cancel{x-2}} = x + 2
$$

$$
\boxed{\frac{x^2-4}{x+1} \div \frac{x-2}{x+1} = x + 2}
$$

---

### Ejemplo 6

Resolver $\dfrac{x^2-9}{x^2+4x+4} \div \dfrac{x-3}{x+2}$.

**Paso 1:** Invertimos:

$$
\frac{x^2-9}{x^2+4x+4} \times \frac{x+2}{x-3}
$$

**Paso 2:** Factorizamos:

$$
x^2-9 = (x+3)(x-3), \quad x^2+4x+4 = (x+2)^2
$$

**Paso 3:** Cancelamos:

$$
\frac{(x+3)(x-3)}{(x+2)^2} \times \frac{x+2}{x-3} = \frac{(x+3)\cancel{(x-3)}}{(x+2)^{\cancel{2}}} \times \frac{\cancel{x+2}}{\cancel{x-3}}
$$

$$
= \frac{x+3}{x+2}
$$

$$
\boxed{\frac{x^2-9}{x^2+4x+4} \div \frac{x-3}{x+2} = \frac{x+3}{x+2}}
$$

---

### Ejemplo 7

Resolver $\dfrac{x^2+5x+6}{x^2-1} \div \dfrac{x+3}{x-1}$.

**Paso 1:** Invertimos:

$$
\frac{x^2+5x+6}{x^2-1} \times \frac{x-1}{x+3}
$$

**Paso 2:** Factorizamos:

$$
x^2+5x+6 = (x+2)(x+3), \quad x^2-1 = (x+1)(x-1)
$$

**Paso 3:** Cancelamos:

$$
\frac{(x+2)(x+3)}{(x+1)(x-1)} \times \frac{x-1}{x+3} = \frac{(x+2)\cancel{(x+3)}}{(x+1)\cancel{(x-1)}} \times \frac{\cancel{x-1}}{\cancel{x+3}}
$$

$$
= \frac{x+2}{x+1}
$$

$$
\boxed{\frac{x^2+5x+6}{x^2-1} \div \frac{x+3}{x-1} = \frac{x+2}{x+1}}
$$

---

### Ejemplo 8

Resolver $\dfrac{3x+6}{x^2-16} \div \dfrac{x+2}{x-4}$.

**Paso 1:** Invertimos:

$$
\frac{3x+6}{x^2-16} \times \frac{x-4}{x+2}
$$

**Paso 2:** Factorizamos:

$$
3x+6 = 3(x+2), \quad x^2-16 = (x+4)(x-4)
$$

**Paso 3:** Cancelamos:

$$
\frac{3(x+2)}{(x+4)(x-4)} \times \frac{x-4}{x+2} = \frac{3\cancel{(x+2)}}{(x+4)\cancel{(x-4)}} \times \frac{\cancel{x-4}}{\cancel{x+2}}
$$

$$
= \frac{3}{x+4}
$$

$$
\boxed{\frac{3x+6}{x^2-16} \div \frac{x+2}{x-4} = \frac{3}{x+4}}
$$

---

### Ejemplo 9

Resolver $\dfrac{x^2-4x+4}{x^2+3x} \div \dfrac{x-2}{x^2-9}$.

**Paso 1:** Invertimos:

$$
\frac{x^2-4x+4}{x^2+3x} \times \frac{x^2-9}{x-2}
$$

**Paso 2:** Factorizamos todo:

$$
x^2-4x+4 = (x-2)^2, \quad x^2+3x = x(x+3), \quad x^2-9 = (x+3)(x-3)
$$

**Paso 3:** Simplificamos:

$$
\frac{(x-2)^2}{x(x+3)} \times \frac{(x+3)(x-3)}{x-2}
$$

$$
= \frac{(x-2)^{\cancel{2}}}{x\cancel{(x+3)}} \times \frac{\cancel{(x+3)}(x-3)}{\cancel{x-2}} = \frac{(x-2)(x-3)}{x}
$$

$$
\boxed{\frac{x^2-4x+4}{x^2+3x} \div \frac{x-2}{x^2-9} = \frac{(x-2)(x-3)}{x}}
$$

---

### Ejemplo 10

Resolver $(x^2 - 25) \div \dfrac{x+5}{3}$.

**Paso 1:** Escribimos $x^2-25$ como fracción:

$$
\frac{x^2-25}{1} \div \frac{x+5}{3} = \frac{x^2-25}{1} \times \frac{3}{x+5}
$$

**Paso 2:** Factorizamos y simplificamos:

$$
= \frac{(x+5)(x-5)}{1} \times \frac{3}{x+5} = 3(x-5)
$$

$$
\boxed{(x^2-25) \div \frac{x+5}{3} = 3(x-5)}
$$

---

## 📝 Ejercicios de práctica

### División de monomios

**Ejercicio 1:** Resuelve $\dfrac{8x^4}{3y^2} \div \dfrac{2x^2}{9y}$.

<details>
<summary>Ver solución</summary>

$$
\frac{8x^4}{3y^2} \times \frac{9y}{2x^2} = \frac{72x^4y}{6x^2y^2} = \frac{12x^2}{y}
$$

</details>

---

**Ejercicio 2:** Resuelve $\dfrac{15a^3b}{4c^2} \div \dfrac{5ab^2}{8c}$.

<details>
<summary>Ver solución</summary>

$$
\frac{15a^3b}{4c^2} \times \frac{8c}{5ab^2} = \frac{120a^3bc}{20ab^2c^2} = \frac{6a^2}{bc}
$$

</details>

---

### División con factorización

**Ejercicio 3:** Resuelve $\dfrac{x^2-9}{x+4} \div \dfrac{x+3}{x+4}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x^2-9}{x+4} \times \frac{x+4}{x+3} = \frac{(x+3)(x-3)}{x+4} \times \frac{x+4}{x+3} = x - 3
$$

</details>

---

**Ejercicio 4:** Resuelve $\dfrac{x^2+4x+3}{x^2-4} \div \dfrac{x+1}{x-2}$.

<details>
<summary>Ver solución</summary>

$x^2+4x+3 = (x+1)(x+3)$ y $x^2-4 = (x+2)(x-2)$:

$$
\frac{(x+1)(x+3)}{(x+2)(x-2)} \times \frac{x-2}{x+1} = \frac{x+3}{x+2}
$$

</details>

---

**Ejercicio 5:** Resuelve $\dfrac{2x-8}{x^2-1} \div \dfrac{x-4}{x+1}$.

<details>
<summary>Ver solución</summary>

$2x-8 = 2(x-4)$ y $x^2-1 = (x+1)(x-1)$:

$$
\frac{2(x-4)}{(x+1)(x-1)} \times \frac{x+1}{x-4} = \frac{2}{x-1}
$$

</details>

---

**Ejercicio 6:** Resuelve $(x^2 - 16) \div \dfrac{x-4}{5}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x^2-16}{1} \times \frac{5}{x-4} = \frac{(x+4)(x-4)}{1} \times \frac{5}{x-4} = 5(x+4)
$$

</details>

---

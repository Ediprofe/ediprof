# 📚 Fracciones Complejas

En esta lección aprenderemos a simplificar fracciones complejas, que son fracciones que contienen otras fracciones en su numerador, denominador, o ambos.

---

## 📖 ¿Qué es una fracción compleja?

Una **fracción compleja** (también llamada fracción compuesta) es una expresión donde el numerador, el denominador, o ambos, contienen fracciones.

### Ejemplos de fracciones complejas

$$
\frac{\dfrac{1}{x}}{\dfrac{1}{y}}, \quad \frac{1 + \dfrac{1}{x}}{2}, \quad \frac{\dfrac{a}{b} + \dfrac{c}{d}}{\dfrac{a}{b} - \dfrac{c}{d}}
$$

---

## 📖 Métodos de simplificación

Existen dos métodos principales para simplificar fracciones complejas:

### Método 1: División de fracciones

Convertir la fracción compleja en una división de fracciones.

### Método 2: Multiplicar por el MCM

Multiplicar numerador y denominador por el MCM de todos los denominadores internos.

---

## 📖 Fracciones simples sobre simples

### Ejemplo 1

Simplificar $\dfrac{\dfrac{2}{3}}{\dfrac{4}{5}}$.

**Método: División de fracciones**

$$
\frac{2}{3} \div \frac{4}{5} = \frac{2}{3} \times \frac{5}{4} = \frac{10}{12} = \frac{5}{6}
$$

$$
\boxed{\dfrac{\dfrac{2}{3}}{\dfrac{4}{5}} = \frac{5}{6}}
$$

---

### Ejemplo 2

Simplificar $\dfrac{\dfrac{x}{y}}{\dfrac{x^2}{y^2}}$.

**Solución:**

$$
\frac{x}{y} \div \frac{x^2}{y^2} = \frac{x}{y} \times \frac{y^2}{x^2} = \frac{xy^2}{x^2y} = \frac{y}{x}
$$

$$
\boxed{\dfrac{\dfrac{x}{y}}{\dfrac{x^2}{y^2}} = \frac{y}{x}}
$$

---

### Ejemplo 3

Simplificar $\dfrac{\dfrac{x+1}{x-1}}{\dfrac{x+1}{x+2}}$.

**Solución:**

$$
\frac{x+1}{x-1} \div \frac{x+1}{x+2} = \frac{x+1}{x-1} \times \frac{x+2}{x+1} = \frac{x+2}{x-1}
$$

$$
\boxed{\dfrac{\dfrac{x+1}{x-1}}{\dfrac{x+1}{x+2}} = \frac{x+2}{x-1}}
$$

---

## 📖 Numerador o denominador con suma de fracciones

### Ejemplo 4

Simplificar $\dfrac{1 + \dfrac{1}{x}}{1 - \dfrac{1}{x}}$.

**Método 1: Simplificar numerador y denominador por separado**

Numerador: $1 + \dfrac{1}{x} = \dfrac{x + 1}{x}$

Denominador: $1 - \dfrac{1}{x} = \dfrac{x - 1}{x}$

Entonces:

$$
\frac{\dfrac{x+1}{x}}{\dfrac{x-1}{x}} = \frac{x+1}{x} \times \frac{x}{x-1} = \frac{x+1}{x-1}
$$

$$
\boxed{\dfrac{1 + \dfrac{1}{x}}{1 - \dfrac{1}{x}} = \frac{x+1}{x-1}}
$$

---

**Método 2: Multiplicar por el MCM**

El MCM de los denominadores internos es $x$.

$$
\frac{1 + \dfrac{1}{x}}{1 - \dfrac{1}{x}} \times \frac{x}{x} = \frac{x + 1}{x - 1}
$$

El mismo resultado.

---

### Ejemplo 5

Simplificar $\dfrac{\dfrac{1}{x} + \dfrac{1}{y}}{xy}$.

**Paso 1:** Simplificamos el numerador:

$$
\frac{1}{x} + \frac{1}{y} = \frac{y + x}{xy}
$$

**Paso 2:** Dividimos:

$$
\frac{\dfrac{x+y}{xy}}{xy} = \frac{x+y}{xy} \times \frac{1}{xy} = \frac{x+y}{x^2y^2}
$$

$$
\boxed{\dfrac{\dfrac{1}{x} + \dfrac{1}{y}}{xy} = \frac{x+y}{x^2y^2}}
$$

---

### Ejemplo 6

Simplificar $\dfrac{1}{\dfrac{1}{a} + \dfrac{1}{b}}$.

**Paso 1:** Simplificamos el denominador:

$$
\frac{1}{a} + \frac{1}{b} = \frac{a + b}{ab}
$$

**Paso 2:** Invertimos:

$$
\frac{1}{\dfrac{a+b}{ab}} = \frac{ab}{a+b}
$$

$$
\boxed{\dfrac{1}{\dfrac{1}{a} + \dfrac{1}{b}} = \frac{ab}{a+b}}
$$

---

### Ejemplo 7

Simplificar $\dfrac{\dfrac{1}{x-1} - \dfrac{1}{x+1}}{\dfrac{2}{x^2-1}}$.

**Paso 1:** Simplificamos el numerador con MCM $(x-1)(x+1)$:

$$
\frac{1}{x-1} - \frac{1}{x+1} = \frac{(x+1) - (x-1)}{(x-1)(x+1)} = \frac{2}{x^2-1}
$$

**Paso 2:** Dividimos:

$$
\frac{\dfrac{2}{x^2-1}}{\dfrac{2}{x^2-1}} = 1
$$

$$
\boxed{\dfrac{\dfrac{1}{x-1} - \dfrac{1}{x+1}}{\dfrac{2}{x^2-1}} = 1}
$$

---

## 📖 Fracciones complejas con varios niveles

### Ejemplo 8

Simplificar $\dfrac{x - \dfrac{1}{x}}{x + \dfrac{1}{x}}$.

**Paso 1:** Simplificamos numerador y denominador:

Numerador: $x - \dfrac{1}{x} = \dfrac{x^2 - 1}{x}$

Denominador: $x + \dfrac{1}{x} = \dfrac{x^2 + 1}{x}$

**Paso 2:** Dividimos:

$$
\frac{\dfrac{x^2-1}{x}}{\dfrac{x^2+1}{x}} = \frac{x^2-1}{x} \times \frac{x}{x^2+1} = \frac{x^2-1}{x^2+1}
$$

Factorizamos el numerador:

$$
= \frac{(x+1)(x-1)}{x^2+1}
$$

$$
\boxed{\dfrac{x - \dfrac{1}{x}}{x + \dfrac{1}{x}} = \frac{x^2-1}{x^2+1}}
$$

---

### Ejemplo 9

Simplificar $\dfrac{\dfrac{a}{b} - \dfrac{b}{a}}{\dfrac{a}{b} + \dfrac{b}{a}}$.

**Paso 1:** Numerador con MCM $ab$:

$$
\frac{a}{b} - \frac{b}{a} = \frac{a^2 - b^2}{ab}
$$

**Paso 2:** Denominador con MCM $ab$:

$$
\frac{a}{b} + \frac{b}{a} = \frac{a^2 + b^2}{ab}
$$

**Paso 3:** Dividimos:

$$
\frac{\dfrac{a^2-b^2}{ab}}{\dfrac{a^2+b^2}{ab}} = \frac{a^2-b^2}{a^2+b^2}
$$

Factorizamos:

$$
= \frac{(a+b)(a-b)}{a^2+b^2}
$$

$$
\boxed{\dfrac{\dfrac{a}{b} - \dfrac{b}{a}}{\dfrac{a}{b} + \dfrac{b}{a}} = \frac{a^2-b^2}{a^2+b^2}}
$$

---

### Ejemplo 10

Simplificar $1 + \dfrac{1}{1 + \dfrac{1}{x}}$.

**Paso 1:** Simplificamos de adentro hacia afuera. Primero $1 + \dfrac{1}{x}$:

$$
1 + \frac{1}{x} = \frac{x + 1}{x}
$$

**Paso 2:** Ahora tenemos:

$$
1 + \frac{1}{\dfrac{x+1}{x}} = 1 + \frac{x}{x+1}
$$

**Paso 3:** Sumamos:

$$
= \frac{x+1}{x+1} + \frac{x}{x+1} = \frac{x + 1 + x}{x+1} = \frac{2x + 1}{x+1}
$$

$$
\boxed{1 + \dfrac{1}{1 + \dfrac{1}{x}} = \frac{2x+1}{x+1}}
$$

---

## 📋 Resumen de métodos

| Tipo de fracción compleja | Método recomendado |
|:--------------------------|:-------------------|
| Fracción simple sobre fracción simple | División directa |
| Con sumas/restas en numerador o denominador | Simplificar primero, luego dividir |
| Con múltiples niveles | Trabajar de adentro hacia afuera |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Simplifica $\dfrac{\dfrac{3}{4}}{\dfrac{9}{8}}$.

<details>
<summary>Ver solución</summary>

$$
\frac{3}{4} \div \frac{9}{8} = \frac{3}{4} \times \frac{8}{9} = \frac{24}{36} = \frac{2}{3}
$$

</details>

---

**Ejercicio 2:** Simplifica $\dfrac{\dfrac{x-1}{x}}{\dfrac{x-1}{x+2}}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x-1}{x} \times \frac{x+2}{x-1} = \frac{x+2}{x}
$$

</details>

---

**Ejercicio 3:** Simplifica $\dfrac{1 - \dfrac{1}{x^2}}{1 - \dfrac{1}{x}}$.

<details>
<summary>Ver solución</summary>

Numerador: $1 - \dfrac{1}{x^2} = \dfrac{x^2-1}{x^2}$

Denominador: $1 - \dfrac{1}{x} = \dfrac{x-1}{x}$

$$
\frac{\dfrac{x^2-1}{x^2}}{\dfrac{x-1}{x}} = \frac{(x+1)(x-1)}{x^2} \times \frac{x}{x-1} = \frac{x+1}{x}
$$

</details>

---

**Ejercicio 4:** Simplifica $\dfrac{1}{\dfrac{1}{x} - \dfrac{1}{y}}$.

<details>
<summary>Ver solución</summary>

Denominador: $\dfrac{1}{x} - \dfrac{1}{y} = \dfrac{y-x}{xy}$

$$
\frac{1}{\dfrac{y-x}{xy}} = \frac{xy}{y-x}
$$

</details>

---

**Ejercicio 5:** Simplifica $\dfrac{\dfrac{2}{x+1} + \dfrac{1}{x-1}}{\dfrac{3}{x^2-1}}$.

<details>
<summary>Ver solución</summary>

Numerador con MCM $(x+1)(x-1)$:

$$
\frac{2(x-1) + (x+1)}{x^2-1} = \frac{2x - 2 + x + 1}{x^2-1} = \frac{3x - 1}{x^2-1}
$$

División:

$$
\frac{\dfrac{3x-1}{x^2-1}}{\dfrac{3}{x^2-1}} = \frac{3x-1}{3}
$$

</details>

---

**Ejercicio 6:** Simplifica $1 - \dfrac{1}{1 - \dfrac{1}{x+1}}$.

<details>
<summary>Ver solución</summary>

Primero: $1 - \dfrac{1}{x+1} = \dfrac{x+1-1}{x+1} = \dfrac{x}{x+1}$

Luego: $\dfrac{1}{\dfrac{x}{x+1}} = \dfrac{x+1}{x}$

Finalmente: $1 - \dfrac{x+1}{x} = \dfrac{x - (x+1)}{x} = \dfrac{-1}{x}$

</details>

---

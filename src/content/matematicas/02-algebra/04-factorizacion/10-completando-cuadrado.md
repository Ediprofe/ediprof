# 🔲 Trinomio Cuadrado Perfecto Completando el Cuadrado

En esta lección aprenderemos la técnica de **completar el cuadrado**, que nos permite convertir cualquier trinomio en un trinomio cuadrado perfecto más una constante.

---

## 📖 ¿Qué es completar el cuadrado?

**Completar el cuadrado** es una técnica algebraica que transforma una expresión de la forma:

$$
x^2 + bx
$$

En un trinomio cuadrado perfecto menos una constante.

---

## 📖 La idea fundamental

Recordemos que un trinomio cuadrado perfecto tiene la forma:

$$
x^2 + 2kx + k^2 = (x + k)^2
$$

Si tenemos solo $x^2 + 2kx$, nos falta el término $k^2$ para completar el cuadrado.

### Fórmula clave

Para completar el cuadrado en $x^2 + bx$:

1. Tomamos la mitad de $b$: $\frac{b}{2}$
2. Lo elevamos al cuadrado: $\left(\frac{b}{2}\right)^2$
3. Sumamos y restamos este valor

$$
x^2 + bx = x^2 + bx + \left(\frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2 = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2
$$

---

## 📖 Ejemplos paso a paso

### Ejemplo 1

Completa el cuadrado: $x^2 + 6x$

**Paso 1:** Identificamos $b = 6$

**Paso 2:** Calculamos $\frac{b}{2} = \frac{6}{2} = 3$

**Paso 3:** Calculamos $\left(\frac{b}{2}\right)^2 = 3^2 = 9$

**Paso 4:** Sumamos y restamos $9$:

$$
x^2 + 6x + 9 - 9 = (x + 3)^2 - 9
$$

$$
\boxed{(x + 3)^2 - 9}
$$

### Ejemplo 2

Completa el cuadrado: $x^2 - 8x$

**Paso 1:** $b = -8$

**Paso 2:** $\frac{b}{2} = \frac{-8}{2} = -4$

**Paso 3:** $\left(\frac{b}{2}\right)^2 = (-4)^2 = 16$

**Paso 4:**

$$
x^2 - 8x + 16 - 16 = (x - 4)^2 - 16
$$

$$
\boxed{(x - 4)^2 - 16}
$$

### Ejemplo 3

Completa el cuadrado: $x^2 + 10x$

$$
\frac{10}{2} = 5 \quad \Rightarrow \quad 5^2 = 25
$$

$$
x^2 + 10x = (x + 5)^2 - 25
$$

$$
\boxed{(x + 5)^2 - 25}
$$

---

## 📖 Completar el cuadrado en trinomios

### Ejemplo 4

Escribe en forma de cuadrado: $x^2 + 6x + 5$

**Paso 1:** Completamos el cuadrado en $x^2 + 6x$:

$$
x^2 + 6x = (x + 3)^2 - 9
$$

**Paso 2:** Agregamos el término constante:

$$
x^2 + 6x + 5 = (x + 3)^2 - 9 + 5 = (x + 3)^2 - 4
$$

$$
\boxed{(x + 3)^2 - 4}
$$

### Ejemplo 5

Escribe en forma de cuadrado: $x^2 - 4x + 7$

$$
x^2 - 4x = (x - 2)^2 - 4
$$

$$
x^2 - 4x + 7 = (x - 2)^2 - 4 + 7 = (x - 2)^2 + 3
$$

$$
\boxed{(x - 2)^2 + 3}
$$

### Ejemplo 6

Escribe en forma de cuadrado: $x^2 + 8x + 10$

$$
x^2 + 8x = (x + 4)^2 - 16
$$

$$
x^2 + 8x + 10 = (x + 4)^2 - 16 + 10 = (x + 4)^2 - 6
$$

$$
\boxed{(x + 4)^2 - 6}
$$

---

## 📖 Factorización usando completar el cuadrado

Cuando el resultado es una **diferencia de cuadrados**, podemos factorizar.

### Ejemplo 7

Factoriza: $x^2 + 6x + 5$

**Paso 1:** Completamos el cuadrado:

$$
x^2 + 6x + 5 = (x + 3)^2 - 4
$$

**Paso 2:** Reconocemos diferencia de cuadrados:

$$
= (x + 3)^2 - 2^2
$$

**Paso 3:** Factorizamos:

$$
= [(x + 3) + 2][(x + 3) - 2]
$$

$$
= (x + 5)(x + 1)
$$

$$
\boxed{(x + 5)(x + 1)}
$$

### Ejemplo 8

Factoriza: $x^2 - 2x - 8$

**Paso 1:** Completamos el cuadrado:

$$
x^2 - 2x = (x - 1)^2 - 1
$$

$$
x^2 - 2x - 8 = (x - 1)^2 - 1 - 8 = (x - 1)^2 - 9
$$

**Paso 2:** Diferencia de cuadrados:

$$
= (x - 1)^2 - 3^2 = [(x - 1) + 3][(x - 1) - 3]
$$

$$
= (x + 2)(x - 4)
$$

$$
\boxed{(x + 2)(x - 4)}
$$

### Ejemplo 9

Factoriza: $x^2 + 4x - 12$

$$
x^2 + 4x = (x + 2)^2 - 4
$$

$$
x^2 + 4x - 12 = (x + 2)^2 - 4 - 12 = (x + 2)^2 - 16
$$

$$
= (x + 2)^2 - 4^2 = (x + 2 + 4)(x + 2 - 4)
$$

$$
= (x + 6)(x - 2)
$$

$$
\boxed{(x + 6)(x - 2)}
$$

---

## 📖 Con coeficiente diferente de 1

Cuando el coeficiente de $x^2$ no es 1, primero lo factorizamos.

### Ejemplo 10

Completa el cuadrado: $2x^2 + 12x + 10$

**Paso 1:** Factorizamos el coeficiente de $x^2$:

$$
2x^2 + 12x + 10 = 2(x^2 + 6x + 5)
$$

**Paso 2:** Completamos el cuadrado dentro del paréntesis:

$$
= 2[(x + 3)^2 - 9 + 5]
$$

$$
= 2[(x + 3)^2 - 4]
$$

$$
= 2(x + 3)^2 - 8
$$

$$
\boxed{2(x + 3)^2 - 8}
$$

### Ejemplo 11

Factoriza: $3x^2 - 6x - 24$

**Paso 1:** Factor común $3$:

$$
3x^2 - 6x - 24 = 3(x^2 - 2x - 8)
$$

**Paso 2:** Completamos el cuadrado:

$$
x^2 - 2x = (x - 1)^2 - 1
$$

$$
x^2 - 2x - 8 = (x - 1)^2 - 9
$$

**Paso 3:** Diferencia de cuadrados:

$$
= [(x - 1) + 3][(x - 1) - 3] = (x + 2)(x - 4)
$$

**Resultado:**

$$
3x^2 - 6x - 24 = 3(x + 2)(x - 4)
$$

$$
\boxed{3(x + 2)(x - 4)}
$$

---

## 📖 Aplicaciones

### Resolver ecuaciones cuadráticas

Completar el cuadrado es útil para resolver ecuaciones.

### Ejemplo 12

Resuelve: $x^2 + 6x + 5 = 0$

**Paso 1:** Completamos el cuadrado:

$$
(x + 3)^2 - 4 = 0
$$

**Paso 2:** Despejamos:

$$
(x + 3)^2 = 4
$$

$$
x + 3 = \pm 2
$$

$$
x = -3 + 2 = -1 \quad \text{o} \quad x = -3 - 2 = -5
$$

$$
\boxed{x = -1 \text{ o } x = -5}
$$

### Encontrar el vértice de una parábola

La forma $(x - h)^2 + k$ nos da el vértice $(h, -k)$ de la parábola.

### Ejemplo 13

Encuentra el vértice de $y = x^2 - 4x + 7$

$$
y = (x - 2)^2 - 4 + 7 = (x - 2)^2 + 3
$$

**Vértice:** $(2, 3)$

---

## 📖 Con fracciones

### Ejemplo 14

Completa el cuadrado: $x^2 + 5x$

$$
\frac{5}{2} = 2.5 \quad \Rightarrow \quad \left(\frac{5}{2}\right)^2 = \frac{25}{4}
$$

$$
x^2 + 5x = \left(x + \frac{5}{2}\right)^2 - \frac{25}{4}
$$

$$
\boxed{\left(x + \frac{5}{2}\right)^2 - \frac{25}{4}}
$$

### Ejemplo 15

Factoriza: $x^2 + 3x - 4$

$$
x^2 + 3x = \left(x + \frac{3}{2}\right)^2 - \frac{9}{4}
$$

$$
x^2 + 3x - 4 = \left(x + \frac{3}{2}\right)^2 - \frac{9}{4} - 4 = \left(x + \frac{3}{2}\right)^2 - \frac{25}{4}
$$

$$
= \left(x + \frac{3}{2}\right)^2 - \left(\frac{5}{2}\right)^2
$$

$$
= \left(x + \frac{3}{2} + \frac{5}{2}\right)\left(x + \frac{3}{2} - \frac{5}{2}\right)
$$

$$
= (x + 4)(x - 1)
$$

$$
\boxed{(x + 4)(x - 1)}
$$

---

## 📝 Ejercicios de práctica

### Completar el cuadrado

**Ejercicio 1:** $x^2 + 4x$

**Ejercicio 2:** $x^2 - 12x$

**Ejercicio 3:** $x^2 + 2x + 5$

**Ejercicio 4:** $x^2 - 6x + 2$

---

### Factorizar completando el cuadrado

**Ejercicio 5:** $x^2 + 2x - 3$

**Ejercicio 6:** $x^2 - 8x + 15$

**Ejercicio 7:** $x^2 + 10x + 9$

---

### Con coeficiente diferente de 1

**Ejercicio 8:** $2x^2 + 8x - 10$

**Ejercicio 9:** $4x^2 - 16x + 12$

---

### Resolver ecuaciones

**Ejercicio 10:** Resuelve $x^2 - 6x + 5 = 0$ completando el cuadrado.

---

## ✅ Soluciones

### Completar el cuadrado

| Ejercicio | Proceso | Solución |
|:---------:|:--------|:---------|
| 1 | $(\frac{4}{2})^2 = 4$ | $(x + 2)^2 - 4$ |
| 2 | $(\frac{-12}{2})^2 = 36$ | $(x - 6)^2 - 36$ |
| 3 | $(x + 1)^2 - 1 + 5$ | $(x + 1)^2 + 4$ |
| 4 | $(x - 3)^2 - 9 + 2$ | $(x - 3)^2 - 7$ |

### Factorizar

**Ejercicio 5:**
$$
x^2 + 2x - 3 = (x + 1)^2 - 1 - 3 = (x + 1)^2 - 4 = (x + 3)(x - 1)
$$

**Ejercicio 6:**
$$
x^2 - 8x + 15 = (x - 4)^2 - 16 + 15 = (x - 4)^2 - 1 = (x - 3)(x - 5)
$$

**Ejercicio 7:**
$$
x^2 + 10x + 9 = (x + 5)^2 - 25 + 9 = (x + 5)^2 - 16 = (x + 9)(x + 1)
$$

### Con coeficiente diferente de 1

**Ejercicio 8:**
$$
2x^2 + 8x - 10 = 2(x^2 + 4x - 5) = 2[(x + 2)^2 - 9] = 2(x + 5)(x - 1)
$$

**Ejercicio 9:**
$$
4x^2 - 16x + 12 = 4(x^2 - 4x + 3) = 4(x - 3)(x - 1)
$$

### Resolver ecuaciones

**Ejercicio 10:**
$$
x^2 - 6x + 5 = 0 \Rightarrow (x - 3)^2 - 4 = 0 \Rightarrow (x - 3)^2 = 4
$$
$$
x - 3 = \pm 2 \Rightarrow x = 5 \text{ o } x = 1
$$

---

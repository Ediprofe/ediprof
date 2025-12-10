# ➗ División de Polinomios

En esta lección aprenderemos a dividir polinomios y a utilizar la Regla de Ruffini como método simplificado para divisiones específicas.

---

## 📖 División de un polinomio entre un monomio

Para dividir un polinomio entre un monomio, se divide cada término del polinomio entre el monomio.

### Ejemplo 1

Calcula: $\frac{6x^3 + 9x^2 - 3x}{3x}$

$$
= \frac{6x^3}{3x} + \frac{9x^2}{3x} - \frac{3x}{3x}
$$

$$
= 2x^2 + 3x - 1
$$

$$
\boxed{2x^2 + 3x - 1}
$$

### Ejemplo 2

Calcula: $\frac{12a^4b^2 - 8a^3b + 4a^2b^3}{4a^2b}$

$$
= \frac{12a^4b^2}{4a^2b} - \frac{8a^3b}{4a^2b} + \frac{4a^2b^3}{4a^2b}
$$

$$
= 3a^2b - 2a + b^2
$$

$$
\boxed{3a^2b - 2a + b^2}
$$

### Ejemplo 3

Calcula: $\frac{15x^5 - 10x^4 + 20x^3}{5x^2}$

$$
= \frac{15x^5}{5x^2} - \frac{10x^4}{5x^2} + \frac{20x^3}{5x^2}
$$

$$
= 3x^3 - 2x^2 + 4x
$$

$$
\boxed{3x^3 - 2x^2 + 4x}
$$

### Ejemplo 4

Calcula: $\frac{24m^3n^2 - 18m^2n^3 + 12mn^4}{6mn^2}$

$$
= \frac{24m^3n^2}{6mn^2} - \frac{18m^2n^3}{6mn^2} + \frac{12mn^4}{6mn^2}
$$

$$
= 4m^2 - 3mn + 2n^2
$$

$$
\boxed{4m^2 - 3mn + 2n^2}
$$

### Ejemplo 5

Calcula: $\frac{8x^6 - 4x^4 + 16x^3 - 2x^2}{2x^2}$

$$
= \frac{8x^6}{2x^2} - \frac{4x^4}{2x^2} + \frac{16x^3}{2x^2} - \frac{2x^2}{2x^2}
$$

$$
= 4x^4 - 2x^2 + 8x - 1
$$

$$
\boxed{4x^4 - 2x^2 + 8x - 1}
$$

---

## 📖 División de polinomios (método clásico)

La división de polinomios es similar a la división larga de números. Se busca un cociente y un resto tal que:

$$
\text{Dividendo} = \text{Divisor} \times \text{Cociente} + \text{Resto}
$$

### Procedimiento

1. Ordenar ambos polinomios en forma descendente
2. Dividir el primer término del dividendo entre el primer término del divisor
3. Multiplicar el resultado por todo el divisor
4. Restar del dividendo
5. Repetir con el nuevo polinomio hasta que el grado del resto sea menor que el del divisor

### Ejemplo 6

Divide: $(x^2 + 5x + 6) \div (x + 2)$

**Paso 1:** $\frac{x^2}{x} = x$ → primer término del cociente

**Paso 2:** $x \cdot (x + 2) = x^2 + 2x$

**Paso 3:** $(x^2 + 5x + 6) - (x^2 + 2x) = 3x + 6$

**Paso 4:** $\frac{3x}{x} = 3$ → segundo término del cociente

**Paso 5:** $3 \cdot (x + 2) = 3x + 6$

**Paso 6:** $(3x + 6) - (3x + 6) = 0$ → resto

$$
\boxed{\text{Cociente} = x + 3, \quad \text{Resto} = 0}
$$

### Ejemplo 7

Divide: $(2x^3 - 5x^2 + 3x - 4) \div (x - 2)$

**Paso 1:** $\frac{2x^3}{x} = 2x^2$

**Paso 2:** $2x^2 \cdot (x - 2) = 2x^3 - 4x^2$

**Paso 3:** $(2x^3 - 5x^2) - (2x^3 - 4x^2) = -x^2$

Bajamos el siguiente término: $-x^2 + 3x$

**Paso 4:** $\frac{-x^2}{x} = -x$

**Paso 5:** $-x \cdot (x - 2) = -x^2 + 2x$

**Paso 6:** $(-x^2 + 3x) - (-x^2 + 2x) = x$

Bajamos el siguiente término: $x - 4$

**Paso 7:** $\frac{x}{x} = 1$

**Paso 8:** $1 \cdot (x - 2) = x - 2$

**Paso 9:** $(x - 4) - (x - 2) = -2$

$$
\boxed{\text{Cociente} = 2x^2 - x + 1, \quad \text{Resto} = -2}
$$

### Ejemplo 8

Divide: $(x^3 - 8) \div (x - 2)$

> **Nota:** El dividendo tiene términos "faltantes". Debemos completarlos con coeficiente cero: $x^3 + 0x^2 + 0x - 8$

**Paso 1:** $\frac{x^3}{x} = x^2$

**Paso 2:** $x^2 \cdot (x - 2) = x^3 - 2x^2$

**Paso 3:** $(x^3 + 0x^2) - (x^3 - 2x^2) = 2x^2$

Bajamos: $2x^2 + 0x$

**Paso 4:** $\frac{2x^2}{x} = 2x$

**Paso 5:** $2x \cdot (x - 2) = 2x^2 - 4x$

**Paso 6:** $(2x^2 + 0x) - (2x^2 - 4x) = 4x$

Bajamos: $4x - 8$

**Paso 7:** $\frac{4x}{x} = 4$

**Paso 8:** $4 \cdot (x - 2) = 4x - 8$

**Paso 9:** $(4x - 8) - (4x - 8) = 0$

$$
\boxed{\text{Cociente} = x^2 + 2x + 4, \quad \text{Resto} = 0}
$$

### Ejemplo 9

Divide: $(3x^3 + 2x^2 - 7x + 2) \div (x + 2)$

**Paso 1:** $\frac{3x^3}{x} = 3x^2$

**Paso 2:** $3x^2 \cdot (x + 2) = 3x^3 + 6x^2$

**Paso 3:** $(3x^3 + 2x^2) - (3x^3 + 6x^2) = -4x^2$

Bajamos: $-4x^2 - 7x$

**Paso 4:** $\frac{-4x^2}{x} = -4x$

**Paso 5:** $-4x \cdot (x + 2) = -4x^2 - 8x$

**Paso 6:** $(-4x^2 - 7x) - (-4x^2 - 8x) = x$

Bajamos: $x + 2$

**Paso 7:** $\frac{x}{x} = 1$

**Paso 8:** $1 \cdot (x + 2) = x + 2$

**Paso 9:** $(x + 2) - (x + 2) = 0$

$$
\boxed{\text{Cociente} = 3x^2 - 4x + 1, \quad \text{Resto} = 0}
$$

### Ejemplo 10

Divide: $(4x^4 - 2x^3 + 6x^2 - 3x + 1) \div (2x - 1)$

**Paso 1:** $\frac{4x^4}{2x} = 2x^3$

**Paso 2:** $2x^3 \cdot (2x - 1) = 4x^4 - 2x^3$

**Paso 3:** $(4x^4 - 2x^3) - (4x^4 - 2x^3) = 0$

Bajamos: $6x^2$

**Paso 4:** $\frac{6x^2}{2x} = 3x$

**Paso 5:** $3x \cdot (2x - 1) = 6x^2 - 3x$

**Paso 6:** $(6x^2 - 3x) - (6x^2 - 3x) = 0$

Bajamos: $1$

**Paso 7:** $\frac{1}{2x}$ → No es posible (el grado del resto es menor que el del divisor)

$$
\boxed{\text{Cociente} = 2x^3 + 3x, \quad \text{Resto} = 1}
$$

---

## 📖 Regla de Ruffini

La **Regla de Ruffini** es un método abreviado para dividir un polinomio entre un binomio de la forma $(x - a)$.

### Condiciones para usar Ruffini

1. El divisor debe ser de la forma $(x - a)$
2. El coeficiente de $x$ en el divisor debe ser $1$

### Procedimiento

1. Escribir los coeficientes del dividendo (incluyendo ceros para términos faltantes)
2. Escribir el valor de $a$ (con signo contrario al del divisor)
3. Bajar el primer coeficiente
4. Multiplicar por $a$ y sumar con el siguiente coeficiente
5. Repetir hasta terminar
6. El último número es el resto; los demás son los coeficientes del cociente

### Ejemplo 11

Divide: $(x^3 - 2x^2 - 5x + 6) \div (x - 3)$

**Divisor:** $x - 3$ → $a = 3$

**Coeficientes del dividendo:** $1, -2, -5, 6$

$$
\begin{array}{c|cccc}
3 & 1 & -2 & -5 & 6 \\
  &   & 3 & 3 & -6 \\
\hline
  & 1 & 1 & -2 & 0 \\
\end{array}
$$

**Proceso:**
- Bajamos el $1$
- $1 \times 3 = 3$, luego $-2 + 3 = 1$
- $1 \times 3 = 3$, luego $-5 + 3 = -2$
- $-2 \times 3 = -6$, luego $6 + (-6) = 0$

$$
\boxed{\text{Cociente} = x^2 + x - 2, \quad \text{Resto} = 0}
$$

### Ejemplo 12

Divide: $(2x^4 - 3x^3 + 5x - 1) \div (x - 1)$

**Divisor:** $x - 1$ → $a = 1$

**Coeficientes:** $2, -3, 0, 5, -1$ (nota: agregamos $0$ para el término $x^2$ faltante)

$$
\begin{array}{c|ccccc}
1 & 2 & -3 & 0 & 5 & -1 \\
  &   & 2 & -1 & -1 & 4 \\
\hline
  & 2 & -1 & -1 & 4 & 3 \\
\end{array}
$$

$$
\boxed{\text{Cociente} = 2x^3 - x^2 - x + 4, \quad \text{Resto} = 3}
$$

### Ejemplo 13

Divide: $(x^3 + 8) \div (x + 2)$

**Divisor:** $x + 2 = x - (-2)$ → $a = -2$

**Coeficientes:** $1, 0, 0, 8$

$$
\begin{array}{c|cccc}
-2 & 1 & 0 & 0 & 8 \\
   &   & -2 & 4 & -8 \\
\hline
   & 1 & -2 & 4 & 0 \\
\end{array}
$$

$$
\boxed{\text{Cociente} = x^2 - 2x + 4, \quad \text{Resto} = 0}
$$

### Ejemplo 14

Divide: $(3x^3 - 7x^2 + 2x + 5) \div (x + 1)$

**Divisor:** $x + 1 = x - (-1)$ → $a = -1$

**Coeficientes:** $3, -7, 2, 5$

$$
\begin{array}{c|cccc}
-1 & 3 & -7 & 2 & 5 \\
   &   & -3 & 10 & -12 \\
\hline
   & 3 & -10 & 12 & -7 \\
\end{array}
$$

$$
\boxed{\text{Cociente} = 3x^2 - 10x + 12, \quad \text{Resto} = -7}
$$

### Ejemplo 15

Divide: $(x^4 - 5x^3 + 8x^2 - 4x + 1) \div (x - 2)$

**Divisor:** $x - 2$ → $a = 2$

**Coeficientes:** $1, -5, 8, -4, 1$

$$
\begin{array}{c|ccccc}
2 & 1 & -5 & 8 & -4 & 1 \\
  &   & 2 & -6 & 4 & 0 \\
\hline
  & 1 & -3 & 2 & 0 & 1 \\
\end{array}
$$

$$
\boxed{\text{Cociente} = x^3 - 3x^2 + 2x, \quad \text{Resto} = 1}
$$

---

## 📖 Teorema del Resto

Si dividimos un polinomio $P(x)$ entre $(x - a)$, el resto es igual a $P(a)$.

### Ejemplo 16

Sin realizar la división, encuentra el resto de dividir $P(x) = x^3 - 2x^2 + 3x - 1$ entre $(x - 2)$.

$$
P(2) = (2)^3 - 2(2)^2 + 3(2) - 1
$$

$$
= 8 - 8 + 6 - 1 = 5
$$

$$
\boxed{\text{Resto} = 5}
$$

### Ejemplo 17

Sin realizar la división, encuentra el resto de dividir $P(x) = 2x^4 - 3x^2 + x - 5$ entre $(x + 1)$.

**Divisor:** $x + 1 = x - (-1)$ → evaluamos en $a = -1$

$$
P(-1) = 2(-1)^4 - 3(-1)^2 + (-1) - 5
$$

$$
= 2(1) - 3(1) - 1 - 5 = 2 - 3 - 1 - 5 = -7
$$

$$
\boxed{\text{Resto} = -7}
$$

### Ejemplo 18

Sin realizar la división, encuentra el resto de dividir $P(x) = x^5 - 32$ entre $(x - 2)$.

$$
P(2) = (2)^5 - 32 = 32 - 32 = 0
$$

$$
\boxed{\text{Resto} = 0}
$$

> **Nota:** Un resto de cero indica que $(x - 2)$ es un factor de $x^5 - 32$.

### Ejemplo 19

Sin realizar la división, encuentra el resto de dividir $P(x) = 3x^3 + 2x^2 - 5x + 7$ entre $(x - 1)$.

$$
P(1) = 3(1)^3 + 2(1)^2 - 5(1) + 7
$$

$$
= 3 + 2 - 5 + 7 = 7
$$

$$
\boxed{\text{Resto} = 7}
$$

---

## 📝 Ejercicios de práctica

### División entre un monomio

**Ejercicio 1:** $\frac{10x^4 - 15x^3 + 5x^2}{5x^2}$

**Ejercicio 2:** $\frac{18a^3b^2 - 12a^2b^3 + 6ab}{6ab}$

**Ejercicio 3:** $\frac{21m^5 - 14m^4 + 7m^3}{7m^2}$

**Ejercicio 4:** $\frac{24x^4y^3 - 16x^3y^2 + 8x^2y}{8x^2y}$

**Ejercicio 5:** $\frac{30a^6 - 20a^4 + 10a^2}{10a^2}$

---

### División de polinomios

**Ejercicio 6:** $(x^2 + 7x + 12) \div (x + 3)$

**Ejercicio 7:** $(2x^3 - 3x^2 + 4x - 5) \div (x - 1)$

**Ejercicio 8:** $(x^3 + 27) \div (x + 3)$

**Ejercicio 9:** $(4x^3 - 6x^2 + 2x - 1) \div (2x - 1)$

**Ejercicio 10:** $(x^4 - 16) \div (x - 2)$

---

### Regla de Ruffini

**Ejercicio 11:** $(x^3 - 6x^2 + 11x - 6) \div (x - 2)$

**Ejercicio 12:** $(x^4 - 1) \div (x - 1)$

**Ejercicio 13:** $(2x^3 + 5x^2 - 4x - 3) \div (x + 3)$

**Ejercicio 14:** $(x^4 + 2x^3 - x^2 - 2x) \div (x + 1)$

**Ejercicio 15:** $(3x^3 - 2x^2 + x - 4) \div (x - 2)$

---

### Teorema del resto

**Ejercicio 16:** Sin dividir, calcula el resto de $(x^3 - 4x + 2) \div (x - 3)$

**Ejercicio 17:** Sin dividir, calcula el resto de $(2x^4 + x^3 - 3x + 1) \div (x + 2)$

**Ejercicio 18:** Sin dividir, calcula el resto de $(x^5 + x^4 - x - 1) \div (x - 1)$

**Ejercicio 19:** Sin dividir, calcula el resto de $(4x^3 - 2x^2 + x - 3) \div (x - 1)$

**Ejercicio 20:** Sin dividir, calcula el resto de $(x^4 - 81) \div (x + 3)$

---

## ✅ Soluciones

### División entre un monomio

**Ejercicio 1:**
$$
\frac{10x^4}{5x^2} - \frac{15x^3}{5x^2} + \frac{5x^2}{5x^2} = 2x^2 - 3x + 1
$$

**Ejercicio 2:**
$$
\frac{18a^3b^2}{6ab} - \frac{12a^2b^3}{6ab} + \frac{6ab}{6ab} = 3a^2b - 2ab^2 + 1
$$

**Ejercicio 3:**
$$
\frac{21m^5}{7m^2} - \frac{14m^4}{7m^2} + \frac{7m^3}{7m^2} = 3m^3 - 2m^2 + m
$$

**Ejercicio 4:**
$$
\frac{24x^4y^3}{8x^2y} - \frac{16x^3y^2}{8x^2y} + \frac{8x^2y}{8x^2y} = 3x^2y^2 - 2xy + 1
$$

**Ejercicio 5:**
$$
\frac{30a^6}{10a^2} - \frac{20a^4}{10a^2} + \frac{10a^2}{10a^2} = 3a^4 - 2a^2 + 1
$$

### División de polinomios

**Ejercicio 6:**
$$
\text{Cociente} = x + 4, \quad \text{Resto} = 0
$$

**Ejercicio 7:**
$$
\text{Cociente} = 2x^2 - x + 3, \quad \text{Resto} = -2
$$

**Ejercicio 8:**
$$
\text{Cociente} = x^2 - 3x + 9, \quad \text{Resto} = 0
$$

**Ejercicio 9:**
$$
\text{Cociente} = 2x^2 - 2x, \quad \text{Resto} = -1
$$

**Ejercicio 10:**
$$
\text{Cociente} = x^3 + 2x^2 + 4x + 8, \quad \text{Resto} = 0
$$

### Regla de Ruffini

**Ejercicio 11:**
Cociente: $x^2 - 4x + 3$, Resto: $0$

**Ejercicio 12:**
Cociente: $x^3 + x^2 + x + 1$, Resto: $0$

**Ejercicio 13:**
Cociente: $2x^2 - x - 1$, Resto: $0$

**Ejercicio 14:**
Cociente: $x^3 + x^2 - 2x$, Resto: $0$

**Ejercicio 15:**
Cociente: $3x^2 + 4x + 9$, Resto: $14$

### Teorema del resto

**Ejercicio 16:**
$$
P(3) = (3)^3 - 4(3) + 2 = 27 - 12 + 2 = 17
$$

**Ejercicio 17:**
$$
P(-2) = 2(-2)^4 + (-2)^3 - 3(-2) + 1 = 32 - 8 + 6 + 1 = 31
$$

**Ejercicio 18:**
$$
P(1) = (1)^5 + (1)^4 - (1) - 1 = 1 + 1 - 1 - 1 = 0
$$

**Ejercicio 19:**
$$
P(1) = 4(1)^3 - 2(1)^2 + (1) - 3 = 4 - 2 + 1 - 3 = 0
$$

**Ejercicio 20:**
$$
P(-3) = (-3)^4 - 81 = 81 - 81 = 0
$$

---

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

### Ejemplo 3

Divide: $(x^2 + 5x + 6) \div (x + 2)$

$$
\begin{array}{c|cc}
 & x^2 + 5x + 6 & \underline{x + 2} \\
\hline
-(x^2 + 2x) & & x + 3 \\
\hline
 & 3x + 6 & \\
-(3x + 6) & & \\
\hline
 & 0 & \\
\end{array}
$$

**Paso a paso:**

1. $\frac{x^2}{x} = x$ → primer término del cociente
2. $x \cdot (x + 2) = x^2 + 2x$
3. $(x^2 + 5x + 6) - (x^2 + 2x) = 3x + 6$
4. $\frac{3x}{x} = 3$ → segundo término del cociente
5. $3 \cdot (x + 2) = 3x + 6$
6. $(3x + 6) - (3x + 6) = 0$ → resto

$$
\boxed{\text{Cociente} = x + 3, \quad \text{Resto} = 0}
$$

### Ejemplo 4

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

**Verificación:**

$$
(x - 2)(2x^2 - x + 1) + (-2)
$$

$$
= 2x^3 - x^2 + x - 4x^2 + 2x - 2 - 2
$$

$$
= 2x^3 - 5x^2 + 3x - 4 \quad ✓
$$

### Ejemplo 5

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

### Ejemplo 6

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

### Ejemplo 7

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

### Ejemplo 8

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

### Ejemplo 9

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

---

## 📖 Teorema del Resto

Si dividimos un polinomio $P(x)$ entre $(x - a)$, el resto es igual a $P(a)$.

### Ejemplo 10

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

---

## 📝 Ejercicios de práctica

### División entre un monomio

**Ejercicio 1:** $\frac{10x^4 - 15x^3 + 5x^2}{5x^2}$

**Ejercicio 2:** $\frac{18a^3b^2 - 12a^2b^3 + 6ab}{6ab}$

---

### División de polinomios

**Ejercicio 3:** $(x^2 + 7x + 12) \div (x + 3)$

**Ejercicio 4:** $(2x^3 - 3x^2 + 4x - 5) \div (x - 1)$

---

### Regla de Ruffini

**Ejercicio 5:** $(x^3 - 6x^2 + 11x - 6) \div (x - 2)$

**Ejercicio 6:** $(x^4 - 1) \div (x - 1)$

**Ejercicio 7:** $(2x^3 + 5x^2 - 4x - 3) \div (x + 3)$

---

### Teorema del resto

**Ejercicio 8:** Sin dividir, calcula el resto de $(x^3 - 4x + 2) \div (x - 3)$

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

### División de polinomios

**Ejercicio 3:**
$$
\text{Cociente} = x + 4, \quad \text{Resto} = 0
$$

**Ejercicio 4:**
$$
\text{Cociente} = 2x^2 - x + 3, \quad \text{Resto} = -2
$$

### Regla de Ruffini

**Ejercicio 5:**

$$
\begin{array}{c|cccc}
2 & 1 & -6 & 11 & -6 \\
  &   & 2 & -8 & 6 \\
\hline
  & 1 & -4 & 3 & 0 \\
\end{array}
$$

Cociente: $x^2 - 4x + 3$, Resto: $0$

**Ejercicio 6:**

$$
\begin{array}{c|ccccc}
1 & 1 & 0 & 0 & 0 & -1 \\
  &   & 1 & 1 & 1 & 1 \\
\hline
  & 1 & 1 & 1 & 1 & 0 \\
\end{array}
$$

Cociente: $x^3 + x^2 + x + 1$, Resto: $0$

**Ejercicio 7:**

$$
\begin{array}{c|cccc}
-3 & 2 & 5 & -4 & -3 \\
   &   & -6 & 3 & 3 \\
\hline
   & 2 & -1 & -1 & 0 \\
\end{array}
$$

Cociente: $2x^2 - x - 1$, Resto: $0$

### Teorema del resto

**Ejercicio 8:**
$$
P(3) = (3)^3 - 4(3) + 2 = 27 - 12 + 2 = 17
$$

Resto: $17$

---

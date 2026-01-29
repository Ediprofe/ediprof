# Fracciones Parciales

La técnica de fracciones parciales descompone funciones racionales en sumas de fracciones simples que se pueden integrar directamente.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo usar fracciones parciales
- Factores lineales simples y repetidos
- Factores cuadráticos irreducibles
- El método de descomposición

---

## 📖 Requisito previo

La función racional $\frac{P(x)}{Q(x)}$ debe tener grado de $P$ menor que grado de $Q$.

Si no es así, primero dividir para obtener:

$$
\frac{P(x)}{Q(x)} = S(x) + \frac{R(x)}{Q(x)}
$$

---

## 📖 Caso 1: Factores lineales distintos

Si $Q(x) = (x - a)(x - b)(x - c)...$

$$
\frac{P(x)}{Q(x)} = \frac{A}{x-a} + \frac{B}{x-b} + \frac{C}{x-c} + ...
$$

---

## ⚙️ Ejemplo 1: Dos factores lineales

Calcula:

$$
\int \frac{1}{x^2 - 1}\,dx = \int \frac{1}{(x-1)(x+1)}\,dx
$$

**Descomponemos:**

$$
\frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}
$$

Multiplicando por $(x-1)(x+1)$:

$$
1 = A(x+1) + B(x-1)
$$

$x = 1$: $1 = 2A$ → $A = \frac{1}{2}$

$x = -1$: $1 = -2B$ → $B = -\frac{1}{2}$

$$
= \int \left(\frac{1/2}{x-1} - \frac{1/2}{x+1}\right)\,dx
$$

$$
= \frac{1}{2}\ln|x-1| - \frac{1}{2}\ln|x+1| + C = \frac{1}{2}\ln\left|\frac{x-1}{x+1}\right| + C
$$

---

## 📖 Caso 2: Factores lineales repetidos

Si $(x-a)^n$ es factor:

$$
\frac{A_1}{x-a} + \frac{A_2}{(x-a)^2} + ... + \frac{A_n}{(x-a)^n}
$$

---

## ⚙️ Ejemplo 2: Factor repetido

Calcula:

$$
\int \frac{x+2}{(x-1)^2}\,dx
$$

**Descomposición:**

$$
= \frac{A}{x-1} + \frac{B}{(x-1)^2}
$$

$$
x + 2 = A(x-1) + B
$$

$x = 1$: $3 = B$

Igualando coeficientes de $x$: $1 = A$

$$
= \int \left(\frac{1}{x-1} + \frac{3}{(x-1)^2}\right)\,dx
$$

$$
= \ln|x-1| - \frac{3}{x-1} + C
$$

---

## 📖 Caso 3: Factor cuadrático irreducible

Si $ax^2 + bx + c$ no factoriza (discriminante negativo):

$$
\frac{Ax + B}{ax^2 + bx + c}
$$

---

## ⚙️ Ejemplo 3: Factor cuadrático

Calcula:

$$
\int \frac{2x + 3}{x^2 + x + 1}\,dx
$$

**Solución:** Completamos el cuadrado:

$$
x^2 + x + 1 = \left(x + \frac{1}{2}\right)^2 + \frac{3}{4}
$$

Reescribimos el numerador:

$$
2x + 3 = 2\left(x + \frac{1}{2}\right) + 2
$$

$$
= \int \frac{2(x + \frac{1}{2})}{(x+\frac{1}{2})^2 + \frac{3}{4}}\,dx + \int \frac{2}{(x+\frac{1}{2})^2 + \frac{3}{4}}\,dx
$$

Primera: $u = (x+\frac{1}{2})^2 + \frac{3}{4}$ → $\ln u$

Segunda: forma $\frac{1}{u^2 + a^2}$ → $\arctan$

$$
= \ln(x^2+x+1) + \frac{4}{\sqrt{3}}\arctan\frac{2x+1}{\sqrt{3}} + C
$$

---

## ⚙️ Ejemplo 4: Combinación

Calcula:

$$
\int \frac{x^2 + 1}{x(x^2 + 4)}\,dx
$$

**Descomposición:**

$$
= \frac{A}{x} + \frac{Bx + C}{x^2 + 4}
$$

$$
x^2 + 1 = A(x^2 + 4) + (Bx + C)x
$$

$x = 0$: $1 = 4A$ → $A = \frac{1}{4}$

Coef. de $x^2$: $1 = A + B$ → $B = \frac{3}{4}$

Coef. de $x$: $0 = C$

$$
= \int \left(\frac{1/4}{x} + \frac{3x/4}{x^2+4}\right)\,dx
$$

$$
= \frac{1}{4}\ln|x| + \frac{3}{8}\ln(x^2+4) + C
$$

---

## 📊 Resumen

| Tipo de factor | Descomposición |
|---------------|----------------|
| $(x-a)$ | $\frac{A}{x-a}$ |
| $(x-a)^n$ | $\frac{A_1}{x-a} + ... + \frac{A_n}{(x-a)^n}$ |
| $ax^2+bx+c$ | $\frac{Ax+B}{ax^2+bx+c}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

$$
\int \frac{3x + 5}{x^2 + 2x - 3}\,dx
$$

<details>
<summary>Ver solución</summary>

$x^2 + 2x - 3 = (x+3)(x-1)$

$$
\frac{3x+5}{(x+3)(x-1)} = \frac{A}{x+3} + \frac{B}{x-1}
$$

$x = 1$: $8 = 4B$ → $B = 2$

$x = -3$: $-4 = -4A$ → $A = 1$

$$
= \ln|x+3| + 2\ln|x-1| + C
$$

</details>

---

**Ejercicio 2:** Calcula:

$$
\int \frac{1}{x(x^2+1)}\,dx
$$

<details>
<summary>Ver solución</summary>

$$
= \frac{A}{x} + \frac{Bx+C}{x^2+1}
$$

$$
1 = A(x^2+1) + (Bx+C)x
$$

$x = 0$: $A = 1$; Coef. $x^2$: $0 = A + B$ → $B = -1$; Coef. $x$: $C = 0$

$$
= \ln|x| - \frac{1}{2}\ln(x^2+1) + C
$$

</details>

# 🔢 Factorial de un Número

En esta lección aprenderemos qué es el factorial de un número, cómo calcularlo y sus propiedades fundamentales, que serán esenciales para el estudio del Binomio de Newton.

---

## 📖 Definición de factorial

El **factorial** de un número natural $n$, denotado como $n!$, es el producto de todos los números naturales desde $1$ hasta $n$:

$$
n! = n \times (n-1) \times (n-2) \times \cdots \times 3 \times 2 \times 1
$$

Se lee "n factorial".

---

## 📖 Ejemplos de factoriales

### Ejemplo 1

Calcular $5!$.

$$
5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
$$

$$
\boxed{5! = 120}
$$

---

### Ejemplo 2

Calcular $7!$.

$$
7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5040
$$

$$
\boxed{7! = 5040}
$$

---

### Ejemplo 3

Calcular $3!$.

$$
3! = 3 \times 2 \times 1 = 6
$$

$$
\boxed{3! = 6}
$$

---

## 📖 Casos especiales

### Factorial de 1

$$
1! = 1
$$

### Factorial de 0

Por convención matemática:

$$
0! = 1
$$

> Esta definición es necesaria para que muchas fórmulas matemáticas funcionen correctamente.

---

## 📖 Tabla de factoriales

| $n$ | $n!$ |
|:---:|:----:|
| $0$ | $1$ |
| $1$ | $1$ |
| $2$ | $2$ |
| $3$ | $6$ |
| $4$ | $24$ |
| $5$ | $120$ |
| $6$ | $720$ |
| $7$ | $5040$ |
| $8$ | $40320$ |
| $9$ | $362880$ |
| $10$ | $3628800$ |

> **Nota:** Los factoriales crecen muy rápidamente.

---

## 📖 Propiedad recursiva

El factorial tiene una propiedad recursiva muy útil:

$$
n! = n \times (n-1)!
$$

### Ejemplo 4

Usando $4! = 24$, calcular $5!$.

$$
5! = 5 \times 4! = 5 \times 24 = 120
$$

$$
\boxed{5! = 120}
$$

---

### Ejemplo 5

Usando $6! = 720$, calcular $7!$.

$$
7! = 7 \times 6! = 7 \times 720 = 5040
$$

$$
\boxed{7! = 5040}
$$

---

## 📖 Simplificación de expresiones con factoriales

### Ejemplo 6

Simplificar $\dfrac{8!}{6!}$.

**Método:** Expandimos parcialmente:

$$
\frac{8!}{6!} = \frac{8 \times 7 \times 6!}{6!} = 8 \times 7 = 56
$$

$$
\boxed{\frac{8!}{6!} = 56}
$$

---

### Ejemplo 7

Simplificar $\dfrac{10!}{8!}$.

$$
\frac{10!}{8!} = \frac{10 \times 9 \times 8!}{8!} = 10 \times 9 = 90
$$

$$
\boxed{\frac{10!}{8!} = 90}
$$

---

### Ejemplo 8

Simplificar $\dfrac{n!}{(n-2)!}$.

$$
\frac{n!}{(n-2)!} = \frac{n \times (n-1) \times (n-2)!}{(n-2)!} = n(n-1)
$$

$$
\boxed{\frac{n!}{(n-2)!} = n(n-1)}
$$

---

### Ejemplo 9

Simplificar $\dfrac{(n+1)!}{(n-1)!}$.

$$
\frac{(n+1)!}{(n-1)!} = \frac{(n+1) \times n \times (n-1)!}{(n-1)!} = (n+1) \times n = n^2 + n
$$

$$
\boxed{\frac{(n+1)!}{(n-1)!} = n(n+1)}
$$

---

### Ejemplo 10

Simplificar $\dfrac{6!}{3! \cdot 3!}$.

$$
\frac{6!}{3! \cdot 3!} = \frac{720}{6 \times 6} = \frac{720}{36} = 20
$$

$$
\boxed{\frac{6!}{3! \cdot 3!} = 20}
$$

---

## 📖 Coeficientes binomiales

Una aplicación importante del factorial es el cálculo de **coeficientes binomiales**:

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

Se lee "n sobre r" o "combinaciones de n en r".

### Ejemplo 11

Calcular $\binom{5}{2}$.

$$
\binom{5}{2} = \frac{5!}{2!(5-2)!} = \frac{5!}{2! \cdot 3!} = \frac{120}{2 \times 6} = \frac{120}{12} = 10
$$

$$
\boxed{\binom{5}{2} = 10}
$$

---

### Ejemplo 12

Calcular $\binom{6}{4}$.

$$
\binom{6}{4} = \frac{6!}{4! \cdot 2!} = \frac{720}{24 \times 2} = \frac{720}{48} = 15
$$

$$
\boxed{\binom{6}{4} = 15}
$$

---

## 📋 Resumen

| Concepto | Fórmula |
|:---------|:-------:|
| Factorial | $n! = n \times (n-1) \times \cdots \times 1$ |
| Casos especiales | $0! = 1$, $1! = 1$ |
| Propiedad recursiva | $n! = n \times (n-1)!$ |
| Coeficiente binomial | $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $6!$.

<details>
<summary>Ver solución</summary>

$$
6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720
$$

</details>

---

**Ejercicio 2:** Simplifica $\dfrac{9!}{7!}$.

<details>
<summary>Ver solución</summary>

$$
\frac{9!}{7!} = 9 \times 8 = 72
$$

</details>

---

**Ejercicio 3:** Simplifica $\dfrac{n!}{(n-3)!}$.

<details>
<summary>Ver solución</summary>

$$
\frac{n!}{(n-3)!} = n(n-1)(n-2)
$$

</details>

---

**Ejercicio 4:** Calcula $\binom{7}{3}$.

<details>
<summary>Ver solución</summary>

$$
\binom{7}{3} = \frac{7!}{3! \cdot 4!} = \frac{5040}{6 \times 24} = \frac{5040}{144} = 35
$$

</details>

---

**Ejercicio 5:** Calcula $\binom{8}{5}$.

<details>
<summary>Ver solución</summary>

$$
\binom{8}{5} = \frac{8!}{5! \cdot 3!} = \frac{40320}{120 \times 6} = \frac{40320}{720} = 56
$$

</details>

---

**Ejercicio 6:** Simplifica $\dfrac{(n+2)!}{n!}$.

<details>
<summary>Ver solución</summary>

$$
\frac{(n+2)!}{n!} = (n+2)(n+1)
$$

</details>

---

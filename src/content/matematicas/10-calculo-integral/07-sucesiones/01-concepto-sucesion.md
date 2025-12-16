# Concepto de Sucesión

Una sucesión es una lista ordenada de números que sigue un patrón. Las sucesiones son la base para estudiar series infinitas.

---

## 🎯 ¿Qué vas a aprender?

- Definición de sucesión
- Notación y terminología
- Sucesiones definidas explícita y recursivamente
- Ejemplos fundamentales

---

## 📖 Definición

Una **sucesión** es una función cuyo dominio son los enteros positivos:

$$a: \mathbb{N} \to \mathbb{R}$$

Escribimos $a_n$ en lugar de $a(n)$.

La sucesión es: $\{a_1, a_2, a_3, ...\}$ o $\{a_n\}_{n=1}^{\infty}$

---

## 📖 Ejemplos básicos

| Sucesión | Primeros términos | Fórmula |
|----------|-------------------|---------|
| Naturales | 1, 2, 3, 4, ... | $a_n = n$ |
| Pares | 2, 4, 6, 8, ... | $a_n = 2n$ |
| Cuadrados | 1, 4, 9, 16, ... | $a_n = n^2$ |
| Potencias de 2 | 2, 4, 8, 16, ... | $a_n = 2^n$ |
| Alternante | 1, -1, 1, -1, ... | $a_n = (-1)^{n+1}$ |

---

## 📖 Definición explícita

Fórmula directa para el n-ésimo término:

$$a_n = f(n)$$

**Ejemplo:** $a_n = \frac{n}{n+1}$ da $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, ...$

---

## 📖 Definición recursiva

Cada término se define en función de términos anteriores:

$$a_1 = \text{valor inicial}, \quad a_{n+1} = g(a_n)$$

---

## ⚙️ Ejemplo 1: Fibonacci

$F_1 = 1, F_2 = 1, F_{n+2} = F_{n+1} + F_n$

Términos: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

---

## ⚙️ Ejemplo 2: Factorial

$n! = n \cdot (n-1)!$ con $0! = 1$

Términos: 1, 1, 2, 6, 24, 120, 720, ...

---

## ⚙️ Ejemplo 3: Geométrica

$a_1 = 3, a_{n+1} = 2a_n$

Términos: 3, 6, 12, 24, 48, ...

Fórmula explícita: $a_n = 3 \cdot 2^{n-1}$

---

## 📖 Sucesiones especiales

### Aritmética
$a_n = a_1 + (n-1)d$, donde $d$ es la diferencia común.

### Geométrica
$a_n = a_1 \cdot r^{n-1}$, donde $r$ es la razón común.

---

## ⚙️ Ejemplo 4: Identificar patrón

Sucesión: $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, ...$

Patrón: numerador = posición, denominador = posición + 1

Fórmula: $a_n = \frac{n}{n+1}$

---

## ⚙️ Ejemplo 5: Alternante

Sucesión: $-1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, ...$

Patrón: signos alternan, denominador = posición

Fórmula: $a_n = \frac{(-1)^n}{n}$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Escribe los primeros 5 términos de:

a) $a_n = \frac{2^n}{n!}$
b) $a_n = \cos(n\pi)$

<details>
<summary>Ver soluciones</summary>

a) $2, 2, \frac{4}{3}, \frac{2}{3}, \frac{4}{15}$

b) $-1, 1, -1, 1, -1$
</details>

---

**Ejercicio 2:** Encuentra la fórmula explícita para la sucesión 3, 7, 11, 15, 19, ...

<details>
<summary>Ver solución</summary>

Es aritmética con $a_1 = 3$ y $d = 4$

$a_n = 3 + (n-1)(4) = 4n - 1$
</details>

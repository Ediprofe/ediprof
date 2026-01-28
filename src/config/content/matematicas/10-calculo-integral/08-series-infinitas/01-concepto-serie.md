---
title: "Concepto de Serie"
---

# Concepto de Serie

Una serie es la suma de los términos de una sucesión infinita. Es uno de los conceptos más importantes del análisis matemático.

---

## 🎯 ¿Qué vas a aprender?

- Definición de serie
- Sumas parciales
- Convergencia y divergencia
- Notación y terminología

---

## 📖 Definición

Dada una sucesión $\{a_n\}$, la **serie** es:

$$
\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + ...
$$

---

## 📖 Sumas parciales

La **n-ésima suma parcial** es:

$$
S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + ... + a_n
$$

La serie converge si la sucesión $\{S_n\}$ converge.

---

## 📖 Convergencia

$$
\sum_{n=1}^{\infty} a_n = S \quad \Leftrightarrow \quad \lim_{n \to \infty} S_n = S
$$

Si el límite no existe o es infinito, la serie **diverge**.

---

## ⚙️ Ejemplo 1: Serie geométrica

$$
\sum_{n=0}^{\infty} r^n = 1 + r + r^2 + r^3 + ...
$$

**Suma parcial:**

$$
S_n = \frac{1 - r^n}{1 - r} \quad (r \neq 1)
$$

Si $|r| < 1$: $\lim_{n \to \infty} r^n = 0$, así que:

$$
\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}
$$

Si $|r| \geq 1$: diverge.

---

## ⚙️ Ejemplo 2: Serie geométrica concreta

$$
\sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ...
$$

$$
= \frac{1}{1 - 1/2} = 2
$$

---

## ⚙️ Ejemplo 3: Serie armónica

$$
\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + ...
$$

Esta serie **diverge** (aunque los términos van a 0).

---

## ⚙️ Ejemplo 4: Serie telescópica

$$
\sum_{n=1}^{\infty} \frac{1}{n(n+1)} = \sum_{n=1}^{\infty} \left(\frac{1}{n} - \frac{1}{n+1}\right)
$$

**Suma parcial:**

$$
S_n = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + ... + \left(\frac{1}{n} - \frac{1}{n+1}\right)
$$

$$
= 1 - \frac{1}{n+1}
$$

$$
\lim_{n \to \infty} S_n = 1
$$

---

## 📖 Propiedades básicas

Si $\sum a_n = A$ y $\sum b_n = B$ convergen:

$$
\sum (a_n + b_n) = A + B
$$

$$
\sum ca_n = cA
$$

---

## 📖 Criterio de divergencia

> Si $\lim_{n \to \infty} a_n \neq 0$, entonces $\sum a_n$ diverge.

**Nota:** Si $\lim a_n = 0$, la serie **puede** converger o diverger.

---

## ⚙️ Ejemplo 5: Criterio de divergencia

$$
\sum_{n=1}^{\infty} \frac{n}{n+1}
$$

$\lim \frac{n}{n+1} = 1 \neq 0$

**Diverge.**

---

## 📊 Resumen

| Serie | Convergencia | Suma |
|-------|-------------|------|
| $\sum r^n$ ($|r| < 1$) | Converge | $\frac{1}{1-r}$ |
| $\sum \frac{1}{n}$ | Diverge | - |
| $\sum \frac{1}{n^2}$ | Converge | $\frac{\pi^2}{6}$ |
| $\sum \frac{1}{n(n+1)}$ | Converge | 1 |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la suma: $\sum_{n=1}^{\infty} \frac{3}{4^n}$

<details>
<summary>Ver solución</summary>

$$
= 3 \sum_{n=1}^{\infty} \left(\frac{1}{4}\right)^n = 3 \cdot \frac{1/4}{1 - 1/4} = 3 \cdot \frac{1}{3} = 1
$$
</details>

---

**Ejercicio 2:** ¿Converge $\sum_{n=1}^{\infty} \frac{n^2}{n^2+1}$?

<details>
<summary>Ver solución</summary>

$$
\lim \frac{n^2}{n^2+1} = 1 \neq 0
$$

Por el criterio de divergencia, **diverge**.
</details>

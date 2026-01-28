---
title: "Criterio de la Integral"
---

# Criterio de la Integral

El criterio de la integral conecta la convergencia de series con la convergencia de integrales impropias.

---

## 🎯 ¿Qué vas a aprender?

- El criterio de la integral
- Condiciones de aplicación
- Series p
- Estimación de sumas

---

## 📖 Enunciado del criterio

Sea $f$ una función positiva, continua y decreciente para $x \geq 1$. Si $a_n = f(n)$:

$$
\sum_{n=1}^{\infty} a_n \text{ converge } \Leftrightarrow \int_1^{\infty} f(x)\,dx \text{ converge}
$$

---

## 📖 Condiciones importantes

1. **Positiva:** $f(x) > 0$
2. **Continua:** sin discontinuidades
3. **Decreciente:** $f'(x) < 0$ (o $f(x) \geq f(x+1)$)

---

## ⚙️ Ejemplo 1: Serie p

$$
\sum_{n=1}^{\infty} \frac{1}{n^p}
$$

$f(x) = \frac{1}{x^p}$ es positiva, continua y decreciente para $x \geq 1$.

$$
\int_1^{\infty} x^{-p}\,dx = \begin{cases} \left[\frac{x^{1-p}}{1-p}\right]_1^{\infty} & p \neq 1 \\ [\ln x]_1^{\infty} & p = 1 \end{cases}
$$

- Si $p > 1$: $= \frac{1}{p-1}$ (converge)
- Si $p \leq 1$: $= \infty$ (diverge)

---

## 📖 Resultado: Series p

$$
\boxed{\sum_{n=1}^{\infty} \frac{1}{n^p} \text{ converge si } p > 1, \text{ diverge si } p \leq 1}
$$

---

## ⚙️ Ejemplo 2: Logaritmo

$$
\sum_{n=2}^{\infty} \frac{1}{n\ln n}
$$

$$
\int_2^{\infty} \frac{dx}{x\ln x} = [\ln(\ln x)]_2^{\infty} = \infty
$$

**Diverge.**

---

## ⚙️ Ejemplo 3: Logaritmo al cuadrado

$$
\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^2}
$$

$$
\int_2^{\infty} \frac{dx}{x(\ln x)^2} = \left[-\frac{1}{\ln x}\right]_2^{\infty} = 0 + \frac{1}{\ln 2}
$$

**Converge.**

---

## 📖 Estimación del error

Si $\sum a_n$ converge y $S$ es la suma, $S_n$ la suma parcial:

$$
\int_{n+1}^{\infty} f(x)\,dx \leq S - S_n \leq \int_n^{\infty} f(x)\,dx
$$

El error al usar $n$ términos está acotado por la integral.

---

## ⚙️ Ejemplo 4: Estimar suma

Para $S = \sum_{n=1}^{\infty} \frac{1}{n^2}$, ¿cuántos términos para error < 0.01?

$$
\int_n^{\infty} \frac{1}{x^2}\,dx = \frac{1}{n} < 0.01
$$

$n > 100$, así que necesitamos 100 términos.

---

## ⚙️ Ejemplo 5: Cota mejorada

$$
S \approx S_n + \int_n^{\infty} f(x)\,dx
$$

Para $\sum \frac{1}{n^2}$ con $n = 10$:

$S_{10} \approx 1.5498$

$\int_{10}^{\infty} \frac{1}{x^2}\,dx = 0.1$

$S \approx 1.6498$ (valor real: $\frac{\pi^2}{6} \approx 1.6449$)

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Converge $\sum_{n=1}^{\infty} \frac{1}{\sqrt{n}}$?

<details>
<summary>Ver solución</summary>

Es serie p con $p = \frac{1}{2} < 1$. **Diverge.**
</details>

---

**Ejercicio 2:** ¿Converge $\sum_{n=3}^{\infty} \frac{1}{n\ln n \cdot \ln(\ln n)}$?

<details>
<summary>Ver solución</summary>

$$
\int \frac{dx}{x\ln x \cdot \ln(\ln x)} = \ln(\ln(\ln x)) \to \infty
$$

**Diverge.**
</details>

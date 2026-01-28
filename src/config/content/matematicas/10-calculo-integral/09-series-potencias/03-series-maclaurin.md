---
title: "Series de Maclaurin"
---

# Series de Maclaurin

Las series de Maclaurin son series de Taylor centradas en $x = 0$. Son las más usadas por su simplicidad.

---

## 🎯 ¿Qué vas a aprender?

- Serie de Maclaurin de funciones elementales
- Manipulación de series
- Aproximaciones polinomiales
- Cálculo de límites usando series

---

## 📖 Definición

La serie de Maclaurin de $f(x)$:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n
$$

---

## 📖 Series fundamentales

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ... = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

$$
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - ... = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}
$$

$$
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - ... = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}
$$

$$
\frac{1}{1-x} = 1 + x + x^2 + x^3 + ... = \sum_{n=0}^{\infty} x^n \quad (|x| < 1)
$$

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - ... = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}x^n}{n}
$$

$$
(1+x)^k = 1 + kx + \frac{k(k-1)}{2!}x^2 + ... = \sum_{n=0}^{\infty} \binom{k}{n}x^n
$$

---

## ⚙️ Ejemplo 1: Sustitución

Encuentra la serie de $e^{2x}$:

$$
e^u = \sum \frac{u^n}{n!}
$$

con $u = 2x$:

$$
e^{2x} = \sum_{n=0}^{\infty} \frac{(2x)^n}{n!} = \sum_{n=0}^{\infty} \frac{2^n x^n}{n!}
$$

---

## ⚙️ Ejemplo 2: Multiplicación

$e^x \sin x = ?$ (primeros términos)

$$
e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + ...
$$

$$
\sin x = x - \frac{x^3}{6} + ...
$$

Multiplicando:

$$
= x + x^2 + \frac{x^3}{3} + ...
$$

---

## ⚙️ Ejemplo 3: Integración término a término

$$
\int \frac{\sin x}{x}\,dx = \int \left(1 - \frac{x^2}{3!} + \frac{x^4}{5!} - ...\right)\,dx
$$

$$
= x - \frac{x^3}{3 \cdot 3!} + \frac{x^5}{5 \cdot 5!} - ... + C
$$

---

## ⚙️ Ejemplo 4: Límites con series

$$
\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}
$$

$$
e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + ...
$$

$$
\frac{e^x - 1 - x}{x^2} = \frac{\frac{x^2}{2} + \frac{x^3}{6} + ...}{x^2} = \frac{1}{2} + \frac{x}{6} + ...
$$

$$
\lim_{x \to 0} = \frac{1}{2}
$$

---

## ⚙️ Ejemplo 5: Aproximación numérica

Calcular $\sin(0.1)$ con error < $10^{-6}$:

$$
\sin(0.1) = 0.1 - \frac{(0.1)^3}{6} + \frac{(0.1)^5}{120} - ...
$$

$$
\approx 0.1 - 0.000167 + 0.0000000083 - ...
$$

$$
\approx 0.099833
$$

(error $\approx 10^{-9}$)

---

## 📖 Derivación e integración

Si $f(x) = \sum a_n x^n$:

$$
f'(x) = \sum n a_n x^{n-1}
$$

$$
\int f(x)\,dx = \sum \frac{a_n}{n+1} x^{n+1} + C
$$

El radio de convergencia se preserva.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la serie de $\frac{1}{1+x^2}$.

<details>
<summary>Ver solución</summary>

$\frac{1}{1-u} = \sum u^n$ con $u = -x^2$:

$$
\frac{1}{1+x^2} = \sum_{n=0}^{\infty} (-x^2)^n = \sum_{n=0}^{\infty} (-1)^n x^{2n}
$$

$$
= 1 - x^2 + x^4 - x^6 + ...
$$
</details>

---

**Ejercicio 2:** Usa series para calcular $\lim_{x \to 0} \frac{\sin x - x}{x^3}$

<details>
<summary>Ver solución</summary>

$$
\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - ...
$$

$$
\frac{\sin x - x}{x^3} = \frac{-\frac{x^3}{6} + ...}{x^3} = -\frac{1}{6} + ...
$$

$$
\lim = -\frac{1}{6}
$$
</details>

---
title: "Límites en el Infinito"
---

# Límites en el Infinito

¿Qué le sucede a una función cuando $x$ crece sin límite? Los límites en el infinito describen el comportamiento "a largo plazo" de las funciones.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa $\lim_{x \to \infty} f(x)$
- Límites de funciones racionales en el infinito
- Límites de funciones exponenciales y logarítmicas
- Jerarquía de crecimiento

---

## 📖 Definición

$$
\lim_{x \to +\infty} f(x) = L
$$

significa que $f(x)$ se aproxima a $L$ cuando $x$ crece sin límite.

$$
\lim_{x \to -\infty} f(x) = L
$$

significa que $f(x)$ se aproxima a $L$ cuando $x$ decrece sin límite.

---

## 📖 Límites básicos

$$
\lim_{x \to \infty} \frac{1}{x} = 0
$$

$$
\lim_{x \to \infty} \frac{1}{x^n} = 0 \quad (n > 0)
$$

$$
\lim_{x \to \infty} c = c \quad \text{(constante)}
$$

---

## 📖 Funciones racionales

Para $f(x) = \frac{a_n x^n + \cdots + a_0}{b_m x^m + \cdots + b_0}$:

### Regla de grados

| Relación | $\lim_{x \to \infty} f(x)$ |
|----------|---------------------------|
| $n < m$ | $0$ |
| $n = m$ | $\frac{a_n}{b_m}$ |
| $n > m$ | $\pm\infty$ |

### Técnica: Dividir por mayor potencia

Dividimos numerador y denominador por $x^{\max(n,m)}$.

---

## ⚙️ Ejemplo 1: Grados iguales

$$\lim_{x \to \infty} \frac{4x^3 - 2x + 1}{2x^3 + 5x^2 - 3}$$

Dividimos por $x^3$:

$$= \lim_{x \to \infty} \frac{4 - \frac{2}{x^2} + \frac{1}{x^3}}{2 + \frac{5}{x} - \frac{3}{x^3}}$$

$$= \frac{4 - 0 + 0}{2 + 0 - 0} = \frac{4}{2} = 2$$

---

## ⚙️ Ejemplo 2: Grado mayor en numerador

$$\lim_{x \to \infty} \frac{x^3 - 1}{2x + 3}$$

Grado 3 > Grado 1 → El límite es $\pm\infty$

Dividimos por $x$:
$$= \lim_{x \to \infty} \frac{x^2 - \frac{1}{x}}{2 + \frac{3}{x}} = \frac{\infty}{2} = +\infty$$

---

## ⚙️ Ejemplo 3: Grado mayor en denominador

$$\lim_{x \to \infty} \frac{3x + 2}{x^2 - 1}$$

Grado 1 < Grado 2 → El límite es $0$

Dividimos por $x^2$:
$$= \lim_{x \to \infty} \frac{\frac{3}{x} + \frac{2}{x^2}}{1 - \frac{1}{x^2}} = \frac{0}{1} = 0$$

---

## 📖 Funciones con raíces

Para funciones con radicales, factorizamos la mayor potencia **dentro** del radical.

---

## ⚙️ Ejemplo 4: Raíz cuadrada

$$\lim_{x \to \infty} \frac{\sqrt{x^2 + 1}}{x}$$

Para $x > 0$: $\sqrt{x^2} = |x| = x$

$$= \lim_{x \to \infty} \frac{\sqrt{x^2(1 + \frac{1}{x^2})}}{x}$$

$$= \lim_{x \to \infty} \frac{x\sqrt{1 + \frac{1}{x^2}}}{x}$$

$$= \lim_{x \to \infty} \sqrt{1 + \frac{1}{x^2}} = \sqrt{1} = 1$$

---

## ⚙️ Ejemplo 5: Diferencia de raíces

$$\lim_{x \to \infty} (\sqrt{x^2 + x} - x)$$

Forma: $\infty - \infty$ (indeterminada)

**Racionalizamos:**
$$= \lim_{x \to \infty} \frac{(\sqrt{x^2 + x} - x)(\sqrt{x^2 + x} + x)}{\sqrt{x^2 + x} + x}$$

$$= \lim_{x \to \infty} \frac{x^2 + x - x^2}{\sqrt{x^2 + x} + x}$$

$$= \lim_{x \to \infty} \frac{x}{\sqrt{x^2 + x} + x}$$

Dividimos por $x$:
$$= \lim_{x \to \infty} \frac{1}{\sqrt{1 + \frac{1}{x}} + 1} = \frac{1}{1 + 1} = \frac{1}{2}$$

---

## 📖 Funciones exponenciales

$$
\lim_{x \to +\infty} e^x = +\infty
$$

$$
\lim_{x \to -\infty} e^x = 0
$$

$$
\lim_{x \to +\infty} e^{-x} = 0
$$

$$
\lim_{x \to -\infty} e^{-x} = +\infty
$$

---

## 📖 Funciones logarítmicas

$$
\lim_{x \to +\infty} \ln x = +\infty
$$

$$
\lim_{x \to 0^+} \ln x = -\infty
$$

---

## 📖 Jerarquía de crecimiento

Cuando $x \to +\infty$, el orden de "velocidad de crecimiento" es:

$$\ln x \ll x^a \ll a^x \ll x! \ll x^x$$

Esto significa que funciones "más rápidas" dominan en cocientes:

$$
\lim_{x \to \infty} \frac{x^{100}}{e^x} = 0
$$

$$
\lim_{x \to \infty} \frac{\ln x}{x} = 0
$$

---

## ⚙️ Ejemplo 6: Exponencial vs polinomio

$$\lim_{x \to \infty} \frac{x^3}{e^x}$$

La exponencial crece más rápido que cualquier potencia:

$$= 0$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\lim_{x \to \infty} \frac{5x^2 - 3x}{2x^2 + 1}$

b) $\lim_{x \to -\infty} \frac{x^3 + 1}{x^2 - 4}$

<details>
<summary>Ver soluciones</summary>

a) Grados iguales: $\frac{5}{2}$

b) Grado mayor en numerador. Cuando $x \to -\infty$, $x^3 \to -\infty$, $x^2 \to +\infty$:
$$= \frac{-\infty}{+\infty}$$ Dividiendo: $\lim \frac{x + \frac{1}{x^2}}{1 - \frac{4}{x^2}} = -\infty$
</details>

---

**Ejercicio 2:** Calcula:

$$\lim_{x \to \infty} \frac{\sqrt{4x^2 + 1}}{3x - 2}$$

<details>
<summary>Ver solución</summary>

$$= \lim_{x \to \infty} \frac{x\sqrt{4 + \frac{1}{x^2}}}{x(3 - \frac{2}{x})} = \frac{\sqrt{4}}{3} = \frac{2}{3}$$
</details>

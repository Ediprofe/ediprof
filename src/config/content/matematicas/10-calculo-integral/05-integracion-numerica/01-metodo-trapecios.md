---
title: "Método de los Trapecios"
---

# Método de los Trapecios

El método de los trapecios aproxima una integral usando trapecios en lugar de rectángulos, obteniendo mejor precisión.

---

## 🎯 ¿Qué vas a aprender?

- La idea geométrica
- La fórmula del trapecio
- Implementación numérica
- Cuándo usarlo

---

## 📖 La idea

En vez de usar rectángulos (sumas de Riemann), usamos trapecios que conectan los puntos consecutivos de la curva.

Un trapecio tiene área: $\frac{1}{2}(b_1 + b_2)h$

---

## 📖 Fórmula del trapecio compuesto

$$
\boxed{\int_a^b f(x)\,dx \approx \frac{\Delta x}{2}[f(x_0) + 2f(x_1) + 2f(x_2) + ... + 2f(x_{n-1}) + f(x_n)]}
$$

donde:
- $\Delta x = \frac{b-a}{n}$
- $x_i = a + i \cdot \Delta x$

---

## 📖 Forma compacta

$$
T_n = \frac{\Delta x}{2}\left[f(x_0) + f(x_n) + 2\sum_{i=1}^{n-1} f(x_i)\right]
$$

---

## ⚙️ Ejemplo 1: Integral conocida

Aproximar $\int_0^1 x^2\,dx$ con $n = 4$.

$\Delta x = 0.25$

| $i$ | $x_i$ | $f(x_i) = x_i^2$ |
|-----|-------|-----------------|
| 0 | 0 | 0 |
| 1 | 0.25 | 0.0625 |
| 2 | 0.5 | 0.25 |
| 3 | 0.75 | 0.5625 |
| 4 | 1 | 1 |

$$
T_4 = \frac{0.25}{2}[0 + 2(0.0625) + 2(0.25) + 2(0.5625) + 1]
$$

$$
= 0.125[0 + 0.125 + 0.5 + 1.125 + 1] = 0.125(2.75) = 0.34375
$$

**Valor exacto:** $\frac{1}{3} \approx 0.333...$

**Error:** $\approx 0.01$

---

## ⚙️ Ejemplo 2: Integral difícil

Aproximar $\int_0^1 e^{-x^2}\,dx$ con $n = 4$.

$\Delta x = 0.25$

| $x_i$ | $f(x_i) = e^{-x_i^2}$ |
|-------|----------------------|
| 0 | 1 |
| 0.25 | 0.9394 |
| 0.5 | 0.7788 |
| 0.75 | 0.5698 |
| 1 | 0.3679 |

$$
T_4 = \frac{0.25}{2}[1 + 2(0.9394 + 0.7788 + 0.5698) + 0.3679]
$$

$$
= 0.125[1 + 4.576 + 0.3679] = 0.125(5.944) \approx 0.743
$$

---

## ⚙️ Ejemplo 3: Más subdivisiones

Misma integral con $n = 8$: $T_8 \approx 0.7462$

Con $n = 16$: $T_{16} \approx 0.7468$

Valor real: $\approx 0.7468...$

Más subdivisiones = mejor aproximación.

---

## 📖 Ventajas del trapecio

- Más preciso que sumas de Riemann con el mismo $n$
- Fácil de programar
- Funciona bien para funciones suaves

---

## 📖 Error del método

El error está acotado por:

$$
|E_T| \leq \frac{(b-a)^3}{12n^2} \cdot \max|f''(x)|
$$

El error decrece como $\frac{1}{n^2}$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa el método del trapecio con $n = 4$ para aproximar $\int_1^3 \frac{1}{x}\,dx$.

<details>
<summary>Ver solución</summary>

$\Delta x = 0.5$

$f(1) = 1$, $f(1.5) = 0.667$, $f(2) = 0.5$, $f(2.5) = 0.4$, $f(3) = 0.333$

$$
T_4 = \frac{0.5}{2}[1 + 2(0.667 + 0.5 + 0.4) + 0.333]
$$

$$
= 0.25[1 + 3.134 + 0.333] = 1.117
$$

Valor exacto: $\ln 3 \approx 1.099$
</details>

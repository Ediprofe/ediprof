# Regla de Simpson

La regla de Simpson usa parábolas para aproximar la curva en cada subintervalo, logrando mayor precisión que los trapecios.

---

## 🎯 ¿Qué vas a aprender?

- La idea detrás de Simpson
- La fórmula de Simpson 1/3
- Cuándo usarla
- Comparación con trapecios

---

## 📖 La idea

En vez de líneas rectas (trapecios), ajustamos parábolas a través de grupos de tres puntos.

**Requisito:** $n$ debe ser **par**.

---

## 📖 Fórmula de Simpson

$$\boxed{\int_a^b f(x)\,dx \approx \frac{\Delta x}{3}[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + ... + 4f(x_{n-1}) + f(x_n)]}$$

**Patrón de coeficientes:** 1, 4, 2, 4, 2, ..., 4, 2, 4, 1

---

## 📖 Forma compacta

$$S_n = \frac{\Delta x}{3}\left[f(x_0) + f(x_n) + 4\sum_{\text{impares}} f(x_i) + 2\sum_{\text{pares}} f(x_i)\right]$$

---

## ⚙️ Ejemplo 1: Comparación

Aproximar $\int_0^1 x^2\,dx$ con $n = 4$.

$\Delta x = 0.25$

$$S_4 = \frac{0.25}{3}[f(0) + 4f(0.25) + 2f(0.5) + 4f(0.75) + f(1)]$$

$$= \frac{0.25}{3}[0 + 4(0.0625) + 2(0.25) + 4(0.5625) + 1]$$

$$= \frac{0.25}{3}[0 + 0.25 + 0.5 + 2.25 + 1] = \frac{0.25}{3}(4)$$

$$= \frac{1}{3} = 0.333...$$

**¡Valor exacto!** Simpson da el resultado exacto para polinomios de grado ≤ 3.

---

## ⚙️ Ejemplo 2: Función no polinomial

Aproximar $\int_0^1 e^{-x^2}\,dx$ con $n = 4$.

$$S_4 = \frac{0.25}{3}[1 + 4(0.9394) + 2(0.7788) + 4(0.5698) + 0.3679]$$

$$= \frac{0.25}{3}[1 + 3.758 + 1.558 + 2.279 + 0.368]$$

$$= \frac{0.25}{3}(8.963) \approx 0.7469$$

Con $n = 4$, Simpson ya da 0.7469, muy cerca del valor real.

---

## ⚙️ Ejemplo 3: Integral de seno

$\int_0^{\pi} \sin x\,dx$ con $n = 4$:

$\Delta x = \frac{\pi}{4}$

$$S_4 = \frac{\pi/4}{3}[\sin 0 + 4\sin\frac{\pi}{4} + 2\sin\frac{\pi}{2} + 4\sin\frac{3\pi}{4} + \sin\pi]$$

$$= \frac{\pi}{12}[0 + 4(\frac{\sqrt{2}}{2}) + 2(1) + 4(\frac{\sqrt{2}}{2}) + 0]$$

$$= \frac{\pi}{12}[2\sqrt{2} + 2 + 2\sqrt{2}] = \frac{\pi}{12}(4\sqrt{2} + 2) \approx 2.005$$

**Valor exacto:** 2 (error de solo 0.25%)

---

## 📖 Error de Simpson

$$|E_S| \leq \frac{(b-a)^5}{180n^4} \cdot \max|f^{(4)}(x)|$$

El error decrece como $\frac{1}{n^4}$, ¡mucho más rápido que trapecios!

---

## 📊 Comparación

| Método | Error proporcional a | Coeficientes |
|--------|---------------------|--------------|
| Rectángulos | $1/n$ | Todos iguales |
| Trapecios | $1/n^2$ | 1, 2, 2, ..., 2, 1 |
| Simpson | $1/n^4$ | 1, 4, 2, 4, ..., 4, 1 |

---

## 📖 Simpson 3/8

Variante que usa cúbicas (requiere $n$ múltiplo de 3):

$$\frac{3\Delta x}{8}[f_0 + 3f_1 + 3f_2 + 2f_3 + 3f_4 + 3f_5 + 2f_6 + ... + f_n]$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa Simpson con $n = 4$ para $\int_1^3 \frac{1}{x}\,dx$.

<details>
<summary>Ver solución</summary>

$\Delta x = 0.5$

$S_4 = \frac{0.5}{3}[1 + 4(0.667) + 2(0.5) + 4(0.4) + 0.333]$

$= \frac{0.5}{3}[1 + 2.668 + 1 + 1.6 + 0.333]$

$= \frac{0.5}{3}(6.601) = 1.100$

Valor exacto: $\ln 3 \approx 1.099$ (excelente aproximación)
</details>

---

**Ejercicio 2:** ¿Por qué Simpson da resultado exacto para $\int x^3\,dx$?

<details>
<summary>Ver solución</summary>

Simpson es exacto para polinomios de grado ≤ 3 porque la aproximación parabólica captura perfectamente el comportamiento de polinomios hasta ese grado. La cuarta derivada de $x^3$ es cero, haciendo el error teóricamente cero.
</details>

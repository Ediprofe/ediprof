# Definición de la Integral Definida

La integral definida formaliza el concepto de área mediante el límite de sumas de Riemann.

---

## 🎯 ¿Qué vas a aprender?

- La definición formal de integral definida
- Notación y terminología
- Interpretación como área neta
- Existencia de la integral

---

## 📖 Definición formal

$$
\boxed{\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x}
$$

cuando el límite existe y es el mismo para cualquier elección de puntos $x_i^*$.

---

## 📖 Terminología

| Símbolo/Término | Significado |
|-----------------|-------------|
| $\int$ | Signo de integración |
| $a$ | Límite inferior |
| $b$ | Límite superior |
| $f(x)$ | Integrando |
| $dx$ | Diferencial (variable de integración) |
| $\int_a^b f(x)\,dx$ | Integral definida de $f$ de $a$ a $b$ |

---

## 📖 Diferencia con integral indefinida

| Integral indefinida | Integral definida |
|---------------------|-------------------|
| $\int f(x)\,dx$ | $\int_a^b f(x)\,dx$ |
| Resultado: función + C | Resultado: número |
| Sin límites | Con límites $a$ y $b$ |
| Antiderivada | Área neta |

---

## 📖 Interpretación geométrica

La integral definida representa el **área neta** entre la curva y el eje $x$:

$$
\int_a^b f(x)\,dx = \text{(área arriba del eje)} - \text{(área abajo del eje)}
$$

- Si $f(x) \geq 0$: área positiva
- Si $f(x) \leq 0$: área negativa
- Mixto: área neta (con signo)

---

## ⚙️ Ejemplo 1: Área positiva

$$
\int_0^2 x\,dx
$$

representa el área del triángulo con vértices $(0,0)$, $(2,0)$, $(2,2)$.

$$
\text{Área} = \frac{1}{2} \cdot 2 \cdot 2 = 2
$$

---

## ⚙️ Ejemplo 2: Área bajo el eje

$$
\int_0^1 (-x)\,dx
$$

El triángulo está debajo del eje $x$.

Área geométrica $= \frac{1}{2}$, pero la integral $= -\frac{1}{2}$

---

## ⚙️ Ejemplo 3: Área mixta

$$
\int_{-1}^{1} x\,dx
$$

De $-1$ a $0$: área negativa $= -\frac{1}{2}$
De $0$ a $1$: área positiva $= \frac{1}{2}$

**Integral $= 0$** (se cancelan)

---

## 📖 Existencia de la integral

> **Teorema:** Si $f$ es continua en $[a, b]$, entonces $\int_a^b f(x)\,dx$ existe.

También existe si $f$ tiene un número finito de discontinuidades de salto.

---

## 📖 Funciones integrables

- Todas las funciones continuas son integrables
- Funciones con discontinuidades de salto finitas son integrables
- Funciones acotadas con discontinuidades no "demasiado malas" son integrables

---

## ⚙️ Ejemplo 4: Cálculo directo

Usando la definición, calcular $\int_0^3 (2x + 1)\,dx$.

$\Delta x = \frac{3}{n}$, $x_i = \frac{3i}{n}$

$$
R_n = \sum_{i=1}^{n}\left(\frac{6i}{n} + 1\right)\frac{3}{n}
$$

$$
= \frac{18}{n^2}\sum i + \frac{3}{n}\sum 1 = \frac{18}{n^2} \cdot \frac{n(n+1)}{2} + 3
$$

$$
= \frac{9(n+1)}{n} + 3 = 9 + \frac{9}{n} + 3
$$

$$
\lim_{n \to \infty} R_n = 12
$$

---

## 📖 Notación alternativa

$$
\int_a^b f(x)\,dx = \int_a^b f(t)\,dt = \int_a^b f(u)\,du
$$

La variable de integración es una **variable muda**.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Interpreta geométricamente:

$$
\int_0^4 (2 - x)\,dx
$$

<details>
<summary>Ver solución</summary>

La función cruza el eje x en $x = 2$.

De 0 a 2: triángulo arriba, área = $\frac{1}{2}(2)(2) = 2$

De 2 a 4: triángulo abajo, área = $-\frac{1}{2}(2)(2) = -2$

Integral = $2 + (-2) = 0$
</details>

---

**Ejercicio 2:** ¿Cuál es mayor: $\int_0^1 x^2\,dx$ o $\int_0^1 x\,dx$?

<details>
<summary>Ver solución</summary>

Para $0 < x < 1$: $x^2 < x$, por lo que la curva $y = x^2$ está debajo de $y = x$.

Por lo tanto: $\int_0^1 x^2\,dx < \int_0^1 x\,dx$

(Valores: $\frac{1}{3} < \frac{1}{2}$)
</details>

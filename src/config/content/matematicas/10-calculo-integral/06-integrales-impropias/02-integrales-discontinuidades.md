---
title: "Integrales con Discontinuidades"
---

# Integrales con Discontinuidades

Las integrales impropias de tipo II tienen un integrando con discontinuidad en el intervalo de integración.

---

## 🎯 ¿Qué vas a aprender?

- Definición de integral impropia tipo II
- Discontinuidades en los extremos
- Discontinuidades interiores
- Evaluación mediante límites

---

## 📖 Discontinuidad en el extremo superior

Si $f$ tiene discontinuidad en $x = b$:

$$
\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx
$$

---

## 📖 Discontinuidad en el extremo inferior

Si $f$ tiene discontinuidad en $x = a$:

$$
\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx
$$

---

## 📖 Discontinuidad interior

Si $f$ tiene discontinuidad en $c \in (a, b)$:

$$
\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx
$$

Ambas integrales deben converger.

---

## ⚙️ Ejemplo 1: Discontinuidad en extremo

Evaluemos:

$$
\int_0^1 \frac{1}{\sqrt{x}}\,dx
$$

**Solución:** Hay discontinuidad en $x = 0$.

$$
= \lim_{t \to 0^+} \int_t^1 x^{-1/2}\,dx
$$

$$
= \lim_{t \to 0^+} [2\sqrt{x}]_t^1 = \lim_{t \to 0^+} (2 - 2\sqrt{t}) = \boxed{2}
$$

**Converge a 2.**

---

## ⚙️ Ejemplo 2: Divergente

Evaluemos:

$$
\int_0^1 \frac{1}{x}\,dx
$$

**Solución:**

$$
= \lim_{t \to 0^+} [\ln x]_t^1 = \lim_{t \to 0^+} (0 - \ln t) = +\infty
$$

**Diverge.**

---

## 📖 La Prueba p para discontinuidades

Esta es la fórmula clave para integrales tipo II:

$$
\int_0^1 \frac{1}{x^p}\,dx = \begin{cases} \dfrac{1}{1-p} & \text{si } p < 1 \text{ (converge)} \\ \text{diverge} & \text{si } p \geq 1 \end{cases}
$$

> 💡 **Contraste importante:** Compara con $\int_1^{\infty} \frac{1}{x^p}\,dx$ que converge para $p > 1$. ¡Los criterios son opuestos!

---

## ⚙️ Ejemplo 3: En el extremo superior

Evaluemos:

$$
\int_0^2 \frac{1}{(2-x)^{2/3}}\,dx
$$

**Solución:** Discontinuidad en $x = 2$.

$$
= \lim_{t \to 2^-} \int_0^t (2-x)^{-2/3}\,dx
$$

Con $u = 2 - x$, $du = -dx$:

$$
= \lim_{t \to 2^-} [-3(2-x)^{1/3}]_0^t
$$

$$
= \lim_{t \to 2^-} (-3(2-t)^{1/3} + 3 \cdot 2^{1/3}) = \boxed{3\sqrt[3]{2}}
$$

---

## ⚙️ Ejemplo 4: Discontinuidad interior

Evaluemos:

$$
\int_0^3 \frac{1}{(x-1)^{2/3}}\,dx
$$

**Solución:** Discontinuidad en $x = 1$. Debemos separar:

$$
= \int_0^1 \frac{dx}{(x-1)^{2/3}} + \int_1^3 \frac{dx}{(x-1)^{2/3}}
$$

**Primera integral:**

$$
\lim_{t \to 1^-} [3(x-1)^{1/3}]_0^t = \lim_{t \to 1^-} (3(t-1)^{1/3} - 3(-1)^{1/3}) = 0 + 3 = 3
$$

**Segunda integral:**

$$
\lim_{s \to 1^+} [3(x-1)^{1/3}]_s^3 = 3(2)^{1/3} - 0 = 3\sqrt[3]{2}
$$

**Total:** 

$$
= 3 + 3\sqrt[3]{2}
$$

---

## ⚙️ Ejemplo 5: Tangente

Evaluemos:

$$
\int_0^{\pi/2} \tan x\,dx
$$

**Solución:** $\tan x$ tiene discontinuidad en $x = \frac{\pi}{2}$.

$$
= \int_0^{\pi/2} \frac{\sin x}{\cos x}\,dx
$$

$$
= \lim_{t \to \pi/2^-} [-\ln|\cos x|]_0^t = \lim_{t \to \pi/2^-} (-\ln|\cos t| + 0)
$$

Como $\cos t \to 0$, $-\ln|\cos t| \to +\infty$

**Diverge.**

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Evalúa:

$$
\int_0^4 \frac{1}{\sqrt{4-x}}\,dx
$$

<details>
<summary>Ver solución</summary>

$$
= \lim_{t \to 4^-} [-2\sqrt{4-x}]_0^t = \lim_{t \to 4^-} (-2\sqrt{4-t} + 4) = \boxed{4}
$$

</details>

---

**Ejercicio 2:** Evalúa:

$$
\int_{-1}^1 \frac{1}{x^{2/3}}\,dx
$$

<details>
<summary>Ver solución</summary>

Discontinuidad en $x = 0$:

$$
= \int_{-1}^0 x^{-2/3}\,dx + \int_0^1 x^{-2/3}\,dx
$$

$$
= [3x^{1/3}]_{-1}^0 + [3x^{1/3}]_0^1
$$

$$
= (0 - (-3)) + (3 - 0) = \boxed{6}
$$

</details>

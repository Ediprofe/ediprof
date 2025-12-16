# Integrales con Límites Infinitos

Las integrales impropias de tipo I tienen al menos un límite de integración infinito. Se evalúan mediante límites.

---

## 🎯 ¿Qué vas a aprender?

- Definición de integral impropia tipo I
- Cómo evaluarlas
- Convergencia y divergencia
- Ejemplos importantes

---

## 📖 Definición

**Límite superior infinito:**

$$
\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx
$$

**Límite inferior infinito:**

$$
\int_{-\infty}^{b} f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx
$$

**Ambos límites infinitos:**

$$
\int_{-\infty}^{\infty} f(x)\,dx = \int_{-\infty}^{c} f(x)\,dx + \int_c^{\infty} f(x)\,dx
$$

---

## 📖 Convergencia y divergencia

- Si el límite existe y es finito: la integral **converge**
- Si el límite es infinito o no existe: la integral **diverge**

---

## ⚙️ Ejemplo 1: Integral convergente

Evaluemos:

$$
\int_1^{\infty} \frac{1}{x^2}\,dx
$$

**Solución:**

$$
= \lim_{t \to \infty} \int_1^t x^{-2}\,dx = \lim_{t \to \infty} \left[-\frac{1}{x}\right]_1^t
$$

$$
= \lim_{t \to \infty} \left(-\frac{1}{t} + 1\right) = 0 + 1 = \boxed{1}
$$

**Converge a 1.**

---

## ⚙️ Ejemplo 2: Integral divergente

Evaluemos:

$$
\int_1^{\infty} \frac{1}{x}\,dx
$$

**Solución:**

$$
= \lim_{t \to \infty} [\ln x]_1^t = \lim_{t \to \infty} (\ln t - 0) = \infty
$$

**Diverge.**

---

## 📖 La Prueba p

Esta es una de las fórmulas más importantes para determinar convergencia:

$$
\int_1^{\infty} \frac{1}{x^p}\,dx = \begin{cases} \dfrac{1}{p-1} & \text{si } p > 1 \text{ (converge)} \\ \text{diverge} & \text{si } p \leq 1 \end{cases}
$$

> 💡 **Regla rápida:** Si el exponente $p > 1$, converge. Si $p \leq 1$, diverge.

---

## ⚙️ Ejemplo 3: Exponencial

Evaluemos:

$$
\int_0^{\infty} e^{-x}\,dx
$$

**Solución:**

$$
= \lim_{t \to \infty} [-e^{-x}]_0^t = \lim_{t \to \infty} (-e^{-t} + 1) = 0 + 1 = \boxed{1}
$$

---

## ⚙️ Ejemplo 4: Ambos límites infinitos

Evaluemos:

$$
\int_{-\infty}^{\infty} \frac{1}{1+x^2}\,dx
$$

**Solución:** Separamos en el punto $c = 0$:

$$
= \int_{-\infty}^{0} \frac{1}{1+x^2}\,dx + \int_0^{\infty} \frac{1}{1+x^2}\,dx
$$

$$
= \lim_{s \to -\infty} [\arctan x]_s^0 + \lim_{t \to \infty} [\arctan x]_0^t
$$

$$
= \left(0 - \left(-\frac{\pi}{2}\right)\right) + \left(\frac{\pi}{2} - 0\right) = \boxed{\pi}
$$

---

## ⚙️ Ejemplo 5: Integral gaussiana

Una de las integrales más famosas en matemáticas:

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

> 💡 Esta integral aparece constantemente en estadística y física. Se demuestra con métodos de cálculo multivariable.

---

## 📖 Criterio de comparación

Si $0 \leq f(x) \leq g(x)$ para $x \geq a$:

- Si $\int_a^{\infty} g(x)\,dx$ converge, entonces $\int_a^{\infty} f(x)\,dx$ también converge
- Si $\int_a^{\infty} f(x)\,dx$ diverge, entonces $\int_a^{\infty} g(x)\,dx$ también diverge

> 💡 **Intuición:** Si una función más grande converge, una más pequeña también. Si una más pequeña diverge, una más grande también.

---

## ⚙️ Ejemplo 6: Comparación

¿Converge la siguiente integral?

$$
\int_1^{\infty} \frac{1}{x^2 + 1}\,dx
$$

**Solución:** Para $x \geq 1$:

$$
\frac{1}{x^2 + 1} < \frac{1}{x^2}
$$

Como $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge (prueba p con $p = 2 > 1$), nuestra integral también **converge**.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Evalúa:

$$
\int_2^{\infty} \frac{1}{x^3}\,dx
$$

<details>
<summary>Ver solución</summary>

$$
= \lim_{t \to \infty} \left[-\frac{1}{2x^2}\right]_2^t = \lim_{t \to \infty} \left(-\frac{1}{2t^2} + \frac{1}{8}\right) = \boxed{\frac{1}{8}}
$$

</details>

---

**Ejercicio 2:** ¿Converge o diverge?

$$
\int_0^{\infty} xe^{-x}\,dx
$$

<details>
<summary>Ver solución</summary>

**Por partes:** $u = x$, $dv = e^{-x}\,dx$

$$
= \lim_{t \to \infty} [-xe^{-x} - e^{-x}]_0^t
$$

$$
= \lim_{t \to \infty} (-te^{-t} - e^{-t} + 1)
$$

$$
= 0 - 0 + 1 = \boxed{1}
$$

**Converge a 1.**

</details>

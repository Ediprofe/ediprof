# Convergencia y Divergencia

Determinar si una integral impropia converge sin calcularla es crucial. Los criterios de comparación nos dan herramientas poderosas.

---

## 🎯 ¿Qué vas a aprender?

- Criterio de comparación directa
- Criterio de comparación por límite
- Funciones de referencia
- Estrategias prácticas

---

## 📖 Criterio de comparación directa

Si $0 \leq f(x) \leq g(x)$ para $x \geq a$:

1. Si $\int_a^{\infty} g(x)\,dx$ converge → $\int_a^{\infty} f(x)\,dx$ converge
2. Si $\int_a^{\infty} f(x)\,dx$ diverge → $\int_a^{\infty} g(x)\,dx$ diverge

> 💡 **Regla mnemotécnica:** "Menor que convergente = convergente" y "Mayor que divergente = divergente"

---

## ⚙️ Ejemplo 1: Comparación directa

¿Converge la siguiente integral?

$$
\int_1^{\infty} \frac{1}{x^3 + 1}\,dx
$$

**Solución:** Para $x \geq 1$:

$$
x^3 + 1 > x^3 \quad \Rightarrow \quad \frac{1}{x^3 + 1} < \frac{1}{x^3}
$$

Como $\int_1^{\infty} \frac{1}{x^3}\,dx$ converge (prueba p con $p = 3 > 1$), nuestra integral también **converge**.

---

## ⚙️ Ejemplo 2: Divergencia

¿Converge la siguiente integral?

$$
\int_1^{\infty} \frac{1}{\sqrt{x} - 0.5}\,dx
$$

**Solución:** Para $x$ grande:

$$
\frac{1}{\sqrt{x} - 0.5} > \frac{1}{2\sqrt{x}}
$$

Como $\int_1^{\infty} \frac{1}{2\sqrt{x}}\,dx$ diverge (prueba p con $p = \frac{1}{2} < 1$), nuestra integral **diverge**.

---

## 📖 Criterio de comparación por límite

Si $f, g > 0$ para $x$ grande y:

$$
\lim_{x \to \infty} \frac{f(x)}{g(x)} = L
$$

Entonces:
- Si $0 < L < \infty$: ambas convergen o ambas divergen
- Si $L = 0$: converge $g$ → converge $f$
- Si $L = \infty$: diverge $g$ → diverge $f$

---

## ⚙️ Ejemplo 3: Comparación por límite

¿Converge la siguiente integral?

$$
\int_1^{\infty} \frac{x^2 + 1}{x^4 - 3x}\,dx
$$

**Solución:** Comparamos con $\frac{1}{x^2}$:

$$
\lim_{x \to \infty} \frac{\frac{x^2+1}{x^4-3x}}{\frac{1}{x^2}} = \lim_{x \to \infty} \frac{x^2(x^2+1)}{x^4-3x} = \lim_{x \to \infty} \frac{x^4+x^2}{x^4-3x} = 1
$$

Como $0 < 1 < \infty$ y $\int \frac{1}{x^2}$ converge, nuestra integral **converge**.

---

## ⚙️ Ejemplo 4: Función exponencial

¿Converge la siguiente integral?

$$
\int_1^{\infty} \frac{e^{-x}}{x}\,dx
$$

**Solución:** Para $x \geq 1$:

$$
\frac{e^{-x}}{x} \leq e^{-x}
$$

Como $\int_1^{\infty} e^{-x}\,dx = e^{-1}$ converge, nuestra integral **converge**.

---

## 📖 Funciones de referencia

| Integral | Convergencia |
|----------|-------------|
| $\int_1^{\infty} \frac{1}{x^p}\,dx$ | $p > 1$: converge |
| $\int_0^1 \frac{1}{x^p}\,dx$ | $p < 1$: converge |
| $\int_1^{\infty} e^{-x}\,dx$ | converge |
| $\int_0^1 \ln x\,dx$ | converge |

---

## ⚙️ Ejemplo 5: Combinación de tipos

¿Converge la siguiente integral?

$$
\int_0^{\infty} \frac{1}{1 + x^2}\,dx
$$

**Solución:** Esta tiene ambos límites: 0 a $\infty$. Separamos:

$$
\int_0^{\infty} = \int_0^1 + \int_1^{\infty}
$$

- En $[0,1]$: el integrando está acotado (no hay problema)
- En $[1,\infty)$: $\frac{1}{1+x^2} < \frac{1}{x^2}$, así que converge

**Converge** (de hecho, $= \frac{\pi}{2}$)

---

## ⚙️ Ejemplo 6: Logaritmo

¿Converge la siguiente integral?

$$
\int_1^{\infty} \frac{\ln x}{x^2}\,dx
$$

**Solución:** Para $x$ grande, $\ln x$ crece más lento que cualquier potencia positiva:

$$
\frac{\ln x}{x^2} < \frac{x^{0.5}}{x^2} = \frac{1}{x^{1.5}}
$$

(para $x$ suficientemente grande)

Como $\int \frac{1}{x^{1.5}}$ converge (prueba p con $p = 1.5 > 1$), **converge**.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Converge o diverge?

$$
\int_2^{\infty} \frac{1}{x\ln x}\,dx
$$

<details>
<summary>Ver solución</summary>

Por sustitución: $u = \ln x$

$$
\int_{\ln 2}^{\infty} \frac{1}{u}\,du = \lim_{t \to \infty} \ln u \Big|_{\ln 2}^t = \infty
$$

**Diverge** (caso límite tipo $1/x$)

</details>

---

**Ejercicio 2:** ¿Converge o diverge?

$$
\int_1^{\infty} \frac{\sin^2 x}{x^2}\,dx
$$

<details>
<summary>Ver solución</summary>

$$
0 \leq \frac{\sin^2 x}{x^2} \leq \frac{1}{x^2}
$$

Como $\int_1^{\infty} \frac{1}{x^2}\,dx$ converge, **converge**.

</details>

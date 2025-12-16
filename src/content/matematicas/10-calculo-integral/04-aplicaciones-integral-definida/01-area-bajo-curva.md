# Área Bajo una Curva

La integral definida calcula el área entre una curva y el eje x. Esta es la aplicación geométrica fundamental de la integración.

---

## 🎯 ¿Qué vas a aprender?

- Área cuando $f(x) \geq 0$
- Área cuando $f(x) < 0$
- Área con partes positivas y negativas
- Área total vs. área neta

---

## 📖 Caso 1: $f(x) \geq 0$

Si $f(x) \geq 0$ en $[a, b]$:

$$\text{Área} = \int_a^b f(x)\,dx$$

---

## ⚙️ Ejemplo 1: Parábola

Área bajo $f(x) = x^2$ de $x = 0$ a $x = 3$:

$$A = \int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = \frac{27}{3} = 9$$

---

## 📖 Caso 2: $f(x) \leq 0$

Si $f(x) \leq 0$ en $[a, b]$, el área (positiva) es:

$$\text{Área} = -\int_a^b f(x)\,dx = \int_a^b |f(x)|\,dx$$

---

## ⚙️ Ejemplo 2: Función negativa

Área entre $f(x) = -x^2$ y el eje x, de $x = 0$ a $x = 2$:

$$A = -\int_0^2 (-x^2)\,dx = \int_0^2 x^2\,dx = \frac{8}{3}$$

---

## 📖 Caso 3: Función que cruza el eje

Si $f$ cambia de signo, hay que dividir la integral:

$$\text{Área total} = \int_a^c |f(x)|\,dx = \int_a^b f(x)\,dx - \int_b^c f(x)\,dx$$

donde $b$ es donde $f$ cruza el eje.

---

## ⚙️ Ejemplo 3: Seno en un período

Área entre $f(x) = \sin x$ y el eje x, de $0$ a $2\pi$:

$$A = \int_0^{\pi} \sin x\,dx + \left|\int_{\pi}^{2\pi} \sin x\,dx\right|$$

$$= [-\cos x]_0^{\pi} + |[-\cos x]_{\pi}^{2\pi}|$$

$$= (1 + 1) + |(-1 - 1)| = 2 + 2 = 4$$

**Nota:** La integral directa $\int_0^{2\pi} \sin x\,dx = 0$ (área neta).

---

## 📖 Área neta vs. Área total

| Concepto | Fórmula |
|----------|---------|
| Área neta | $\int_a^b f(x)\,dx$ (con signo) |
| Área total | $\int_a^b \|f(x)\|\,dx$ (siempre positiva) |

---

## ⚙️ Ejemplo 4: Polinomio que cruza

Área entre $f(x) = x^3 - x$ y el eje x, de $x = -1$ a $x = 1$.

Raíces: $x(x^2 - 1) = 0 \Rightarrow x = -1, 0, 1$

$$A = \left|\int_{-1}^0 (x^3-x)\,dx\right| + \left|\int_0^1 (x^3-x)\,dx\right|$$

$$= \left|\left[\frac{x^4}{4} - \frac{x^2}{2}\right]_{-1}^0\right| + \left|\left[\frac{x^4}{4} - \frac{x^2}{2}\right]_0^1\right|$$

$$= \left|0 - \left(\frac{1}{4} - \frac{1}{2}\right)\right| + \left|\frac{1}{4} - \frac{1}{2}\right|$$

$$= \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$

---

## ⚙️ Ejemplo 5: Área acotada

Área acotada por $y = 4 - x^2$ y el eje x:

Intersecciones: $4 - x^2 = 0 \Rightarrow x = \pm 2$

$$A = \int_{-2}^{2} (4 - x^2)\,dx$$

Por simetría: $= 2\int_0^2 (4 - x^2)\,dx$

$$= 2\left[4x - \frac{x^3}{3}\right]_0^2 = 2\left(8 - \frac{8}{3}\right) = 2 \cdot \frac{16}{3} = \frac{32}{3}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula el área bajo $f(x) = \sqrt{x}$ de $x = 0$ a $x = 4$.

<details>
<summary>Ver solución</summary>

$A = \int_0^4 x^{1/2}\,dx = \left[\frac{2x^{3/2}}{3}\right]_0^4 = \frac{2(8)}{3} = \frac{16}{3}$
</details>

---

**Ejercicio 2:** Calcula el área total entre $f(x) = x^2 - 1$ y el eje x, de $x = -2$ a $x = 2$.

<details>
<summary>Ver solución</summary>

Raíces: $x = \pm 1$

$A = \int_{-2}^{-1}(x^2-1)\,dx + \left|\int_{-1}^{1}(x^2-1)\,dx\right| + \int_1^2(x^2-1)\,dx$

Por simetría: $= 2\int_1^2(x^2-1)\,dx + \left|\int_{-1}^1(x^2-1)\,dx\right|$

$= 2[\frac{x^3}{3}-x]_1^2 + |[\frac{x^3}{3}-x]_{-1}^1|$

$= 2(\frac{8}{3}-2-\frac{1}{3}+1) + |(\frac{1}{3}-1)-(-\frac{1}{3}+1)|$

$= 2(\frac{4}{3}) + |\frac{-4}{3}| = \frac{8}{3} + \frac{4}{3} = 4$
</details>

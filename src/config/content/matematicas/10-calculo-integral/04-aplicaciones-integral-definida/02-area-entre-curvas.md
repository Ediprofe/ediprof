---
title: "Área entre Curvas"
---

# Área entre Curvas

Cuando calculamos el área entre dos curvas, integramos la diferencia entre la función superior e inferior.

---

## 🎯 ¿Qué vas a aprender?

- Área entre dos curvas (integración en x)
- Cuándo integrar respecto a y
- Encontrar puntos de intersección
- Regiones con múltiples partes

---

## 📖 Fórmula básica

Si $f(x) \geq g(x)$ en $[a, b]$:

$$
\text{Área} = \int_a^b [f(x) - g(x)]\,dx
$$

donde $f$ es la curva "de arriba" y $g$ la "de abajo".

---

## 📖 Método paso a paso

1. **Graficar** las curvas (al menos mentalmente)
2. **Encontrar** los puntos de intersección
3. **Determinar** cuál curva está arriba
4. **Integrar** la diferencia
5. **Evaluar**

---

## ⚙️ Ejemplo 1: Parábola y recta

Área entre $y = x^2$ y $y = x + 2$.

**Intersecciones:**

$$
x^2 = x + 2 \Rightarrow x^2 - x - 2 = 0 \Rightarrow (x-2)(x+1) = 0
$$

$$
x = -1, 2
$$

**¿Cuál arriba?** Probamos $x = 0$: $y = 0$ vs $y = 2$. La recta está arriba.

$$
A = \int_{-1}^{2} [(x + 2) - x^2]\,dx
$$

$$
= \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2}
$$

$$
= \left(2 + 4 - \frac{8}{3}\right) - \left(\frac{1}{2} - 2 + \frac{1}{3}\right)
$$

$$
= \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{10}{3} + \frac{7}{6} = \frac{27}{6} = \frac{9}{2}
$$

---

## ⚙️ Ejemplo 2: Dos parábolas

Área entre $y = x^2$ y $y = 2 - x^2$.

**Intersecciones:**

$$
x^2 = 2 - x^2 \Rightarrow 2x^2 = 2 \Rightarrow x = \pm 1
$$

**¿Cuál arriba?** Para $x = 0$: $0$ vs $2$. La segunda está arriba.

$$
A = \int_{-1}^{1} [(2 - x^2) - x^2]\,dx = \int_{-1}^{1} (2 - 2x^2)\,dx
$$

$$
= 2\int_0^1 (2 - 2x^2)\,dx = 2\left[2x - \frac{2x^3}{3}\right]_0^1
$$

$$
= 2\left(2 - \frac{2}{3}\right) = 2 \cdot \frac{4}{3} = \frac{8}{3}
$$

---

## 📖 Integración respecto a y

Cuando las curvas se expresan mejor como $x = f(y)$:

$$
\text{Área} = \int_c^d [f_{derecha}(y) - f_{izquierda}(y)]\,dy
$$

---

## ⚙️ Ejemplo 3: Integrar en y

Área entre $x = y^2$ y $x = y + 2$.

**Intersecciones:**

$$
y^2 = y + 2 \Rightarrow y^2 - y - 2 = 0 \Rightarrow y = -1, 2
$$

La recta está a la derecha:

$$
A = \int_{-1}^{2} [(y + 2) - y^2]\,dy = \frac{9}{2}
$$

(Mismo resultado que el Ejemplo 1, ¡es la misma región vista horizontalmente!)

---

## ⚙️ Ejemplo 4: Obligatorio en y

Área entre $x = y^2 - 4$ y $x = 6 - 3y^2$ (de $y = -1$ a $y = 1$).

En este caso, integrar en $y$ es mucho más simple:

$$
A = \int_{-1}^{1} [(6-3y^2) - (y^2-4)]\,dy
$$

$$
= \int_{-1}^{1} (10 - 4y^2)\,dy = 2\int_0^1 (10 - 4y^2)\,dy
$$

$$
= 2\left[10y - \frac{4y^3}{3}\right]_0^1 = 2\left(10 - \frac{4}{3}\right) = \frac{52}{3}
$$

---

## ⚙️ Ejemplo 5: Curvas que se cruzan

Área entre $y = \sin x$ y $y = \cos x$ de $0$ a $\frac{\pi}{2}$.

Se cruzan cuando $\sin x = \cos x \Rightarrow x = \frac{\pi}{4}$

$$
A = \int_0^{\pi/4} (\cos x - \sin x)\,dx + \int_{\pi/4}^{\pi/2} (\sin x - \cos x)\,dx
$$

$$
= [\sin x + \cos x]_0^{\pi/4} + [-\cos x - \sin x]_{\pi/4}^{\pi/2}
$$

$$
= (\sqrt{2} - 1) + (-1 - (-\sqrt{2})) = \sqrt{2} - 1 + \sqrt{2} - 1 = 2\sqrt{2} - 2
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el área entre $y = x$ y $y = x^2$ de $x = 0$ a $x = 1$.

<details>
<summary>Ver solución</summary>

$$
A = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}
$$
</details>

---

**Ejercicio 2:** Encuentra el área encerrada por $y = x^3$ y $y = x$.

<details>
<summary>Ver solución</summary>

Intersecciones: $x^3 = x \Rightarrow x = 0, \pm 1$

Por simetría: 

$$
A = 2\int_0^1 (x - x^3)\,dx = 2\left[\frac{x^2}{2} - \frac{x^4}{4}\right]_0^1 = 2\left(\frac{1}{4}\right) = \frac{1}{2}
$$
</details>

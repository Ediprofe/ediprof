# Recta Tangente

La recta tangente es la mejor aproximación lineal a una curva en un punto. La derivada nos da directamente su pendiente.

---

## 🎯 ¿Qué vas a aprender?

- Ecuación de la recta tangente usando la derivada
- Tangentes horizontales y verticales
- Tangentes a curvas implícitas
- Aplicaciones prácticas

---

## 📖 Ecuación de la recta tangente

La recta tangente a $y = f(x)$ en el punto $(a, f(a))$:

$$\boxed{y - f(a) = f'(a)(x - a)}$$

O en forma explícita:

$$y = f(a) + f'(a)(x - a)$$

---

## ⚙️ Ejemplo 1: Tangente básica

Encuentra la tangente a $f(x) = x^2$ en $x = 3$.

**Punto:** $(3, 9)$

**Derivada:** $f'(x) = 2x \Rightarrow f'(3) = 6$

**Tangente:**
$$y - 9 = 6(x - 3)$$
$$y = 6x - 9$$

---

## ⚙️ Ejemplo 2: Función más compleja

Tangente a $f(x) = \sqrt{x}$ en $x = 4$.

**Punto:** $(4, 2)$

**Derivada:** $f'(x) = \frac{1}{2\sqrt{x}} \Rightarrow f'(4) = \frac{1}{4}$

**Tangente:**
$$y - 2 = \frac{1}{4}(x - 4)$$
$$y = \frac{1}{4}x + 1$$

---

## 📖 Tangente horizontal

La tangente es **horizontal** cuando:
$$f'(a) = 0$$

En estos puntos, la tangente tiene la forma $y = f(a)$ (constante).

---

## ⚙️ Ejemplo 3: Encontrar tangentes horizontales

Para $f(x) = x^3 - 3x$:

$$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 0$$
$$x = \pm 1$$

**Puntos con tangente horizontal:**
- $(1, -2)$ → tangente: $y = -2$
- $(-1, 2)$ → tangente: $y = 2$

---

## 📖 Tangente de pendiente dada

Para encontrar dónde la tangente tiene pendiente $m$, resolvemos:
$$f'(x) = m$$

---

## ⚙️ Ejemplo 4: Tangente con pendiente específica

¿Dónde tiene $f(x) = x^3$ tangente con pendiente 12?

$$f'(x) = 3x^2 = 12$$
$$x^2 = 4 \Rightarrow x = \pm 2$$

**Puntos:** $(2, 8)$ y $(-2, -8)$

**Tangentes:**
- En $(2, 8)$: $y - 8 = 12(x - 2)$ → $y = 12x - 16$
- En $(-2, -8)$: $y + 8 = 12(x + 2)$ → $y = 12x + 16$

---

## 📖 Tangente a curva implícita

Para $F(x, y) = 0$:
1. Derivar implícitamente para encontrar $\frac{dy}{dx}$
2. Evaluar en el punto dado
3. Usar la fórmula de tangente

---

## ⚙️ Ejemplo 5: Círculo

Tangente a $x^2 + y^2 = 25$ en $(3, 4)$.

**Derivada implícita:**
$$2x + 2y \cdot y' = 0 \Rightarrow y' = -\frac{x}{y}$$

**En $(3, 4)$:** $y' = -\frac{3}{4}$

**Tangente:**
$$y - 4 = -\frac{3}{4}(x - 3)$$
$$y = -\frac{3}{4}x + \frac{25}{4}$$

---

## 📖 Aproximación lineal

La tangente aproxima la función cerca del punto de tangencia:

$$f(x) \approx f(a) + f'(a)(x - a)$$

para $x$ cerca de $a$.

---

## ⚙️ Ejemplo 6: Aproximación

Estimar $\sqrt{4.1}$ usando la tangente a $f(x) = \sqrt{x}$ en $x = 4$.

Tangente: $y = \frac{1}{4}x + 1$

$$\sqrt{4.1} \approx \frac{1}{4}(4.1) + 1 = 1.025 + 1 = 2.025$$

Valor real: $\sqrt{4.1} \approx 2.0248$ (muy cercano)

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la tangente a $f(x) = x^3 - 2x$ en $x = 1$.

<details>
<summary>Ver solución</summary>

$f(1) = -1$, $f'(x) = 3x^2 - 2$, $f'(1) = 1$

Tangente: $y + 1 = 1(x - 1)$ → $y = x - 2$
</details>

---

**Ejercicio 2:** Encuentra todos los puntos de $f(x) = x^4 - 2x^2$ donde la tangente es horizontal.

<details>
<summary>Ver solución</summary>

$f'(x) = 4x^3 - 4x = 4x(x^2 - 1) = 0$

$x = 0, \pm 1$

Puntos: $(0, 0)$, $(1, -1)$, $(-1, -1)$
</details>

---
title: "Interpretación Geométrica de la Derivada"
---

# Interpretación Geométrica de la Derivada

La derivada tiene un significado geométrico fundamental: es la pendiente de la recta tangente a la curva en un punto. Esta interpretación conecta el cálculo con la geometría.

---

## 🎯 ¿Qué vas a aprender?

- La derivada como pendiente de la tangente
- Ecuación de la recta tangente
- Ecuación de la recta normal
- Aplicaciones geométricas

---

## 📖 De la secante a la tangente

### Recta secante

Pasa por dos puntos $(a, f(a))$ y $(a+h, f(a+h))$:

$$m_{\text{secante}} = \frac{f(a + h) - f(a)}{h}$$

### Recta tangente

Es el límite de las secantes cuando $h \to 0$:

$$m_{\text{tangente}} = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} = f'(a)$$

---

## 📖 La derivada como pendiente

$$\boxed{f'(a) = \text{pendiente de la recta tangente a } f \text{ en } x = a}$$

### Interpretación visual

- Si $f'(a) > 0$: la tangente sube → función creciente en $a$
- Si $f'(a) < 0$: la tangente baja → función decreciente en $a$
- Si $f'(a) = 0$: la tangente es horizontal → posible máximo, mínimo o inflexión

---

## 📖 Ecuación de la recta tangente

La recta tangente a $f$ en el punto $(a, f(a))$ tiene:
- Pendiente: $m = f'(a)$
- Pasa por: $(a, f(a))$

**Ecuación punto-pendiente:**

$$y - f(a) = f'(a)(x - a)$$

O en forma explícita:

$$y = f(a) + f'(a)(x - a)$$

---

## ⚙️ Ejemplo 1: Tangente a una parábola

Encuentra la ecuación de la tangente a $f(x) = x^2$ en $x = 3$.

**Paso 1:** Punto de tangencia
$$f(3) = 9 \quad \Rightarrow \quad (3, 9)$$

**Paso 2:** Pendiente (derivada)
$$f'(x) = 2x \quad \Rightarrow \quad f'(3) = 6$$

**Paso 3:** Ecuación de la tangente
$$y - 9 = 6(x - 3)$$
$$y = 6x - 18 + 9$$
$$\boxed{y = 6x - 9}$$

---

## ⚙️ Ejemplo 2: Tangente a una cúbica

Encuentra la tangente a $f(x) = x^3 - 2x$ en $x = 1$.

**Punto:** $f(1) = 1 - 2 = -1$ → $(1, -1)$

**Derivada:** $f'(x) = 3x^2 - 2$ → $f'(1) = 1$

**Tangente:**
$$y - (-1) = 1(x - 1)$$
$$y = x - 2$$

---

## 📖 Recta normal

La **recta normal** es perpendicular a la tangente en el punto de tangencia.

Si la tangente tiene pendiente $m = f'(a)$:

$$m_{\text{normal}} = -\frac{1}{f'(a)} \quad (\text{si } f'(a) \neq 0)$$

**Ecuación:**
$$y - f(a) = -\frac{1}{f'(a)}(x - a)$$

---

## ⚙️ Ejemplo 3: Recta normal

Encuentra la normal a $f(x) = \sqrt{x}$ en $x = 4$.

**Punto:** $f(4) = 2$ → $(4, 2)$

**Derivada:** $f'(x) = \frac{1}{2\sqrt{x}}$ → $f'(4) = \frac{1}{4}$

**Pendiente normal:** $m_n = -4$

**Normal:**
$$y - 2 = -4(x - 4)$$
$$y = -4x + 18$$

---

## ⚙️ Ejemplo 4: Punto con tangente horizontal

¿En qué punto(s) la tangente a $f(x) = x^3 - 3x$ es horizontal?

**Tangente horizontal:** $f'(x) = 0$

$$f'(x) = 3x^2 - 3 = 0$$
$$3(x^2 - 1) = 0$$
$$x = \pm 1$$

**Puntos:** $(1, -2)$ y $(-1, 2)$

En ambos puntos la tangente es horizontal (pendiente 0).

---

## ⚙️ Ejemplo 5: Tangente que pasa por un punto exterior

¿Por qué punto(s) de $f(x) = x^2$ pasa una tangente que también pasa por $(0, -4)$?

Sea $(a, a^2)$ el punto de tangencia.

Pendiente de la tangente: $f'(a) = 2a$

La tangente pasa por $(a, a^2)$ y $(0, -4)$:

$$\frac{a^2 - (-4)}{a - 0} = 2a$$

$$\frac{a^2 + 4}{a} = 2a$$

$$a^2 + 4 = 2a^2$$

$$a^2 = 4$$

$$a = \pm 2$$

**Puntos:** $(2, 4)$ y $(-2, 4)$

---

## 📊 Resumen

| Recta | Pendiente | Ecuación |
|-------|-----------|----------|
| Tangente | $m = f'(a)$ | $y - f(a) = f'(a)(x - a)$ |
| Normal | $m = -\frac{1}{f'(a)}$ | $y - f(a) = -\frac{1}{f'(a)}(x - a)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la ecuación de la tangente a $f(x) = x^2 - 4x + 3$ en $x = 2$.

<details>
<summary>Ver solución</summary>

$f(2) = 4 - 8 + 3 = -1$ → $(2, -1)$

$f'(x) = 2x - 4$ → $f'(2) = 0$

Tangente horizontal: $y = -1$
</details>

---

**Ejercicio 2:** Encuentra los puntos de $f(x) = x^3$ donde la tangente tiene pendiente 12.

<details>
<summary>Ver solución</summary>

$f'(x) = 3x^2 = 12$
$x^2 = 4$
$x = \pm 2$

Puntos: $(2, 8)$ y $(-2, -8)$
</details>

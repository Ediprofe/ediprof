---
title: "Límites Infinitos"
---

# Límites Infinitos

¿Qué sucede cuando una función crece sin límite al acercarnos a un punto? Los límites infinitos describen este comportamiento y están relacionados con las asíntotas verticales.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa que un límite sea infinito
- Límites infinitos por la izquierda y derecha
- Cómo determinar el signo ($+\infty$ o $-\infty$)
- Operaciones con infinito

---

## 📖 Definición

Decimos que:

$$
\lim_{x \to a} f(x) = +\infty
$$

si $f(x)$ puede hacerse arbitrariamente grande (positivo) cuando $x$ se acerca a $a$.

$$
\lim_{x \to a} f(x) = -\infty
$$

si $f(x)$ puede hacerse arbitrariamente grande en valor absoluto (negativo) cuando $x$ se acerca a $a$.

### ⚠️ Nota técnica

Cuando escribimos "$= \infty$", el límite **no existe** en el sentido tradicional. Es una descripción del comportamiento.

---

## 📖 Límites laterales infinitos

$$\lim_{x \to a^+} f(x) = +\infty \quad \text{o} \quad -\infty$$

$$\lim_{x \to a^-} f(x) = +\infty \quad \text{o} \quad -\infty$$

Los límites laterales pueden tener signos diferentes.

---

## ⚙️ Ejemplo 1: Función recíproca

$$f(x) = \frac{1}{x}$$

En $x = 0$:

**Por la derecha ($x > 0$):**

$$
\lim_{x \to 0^+} \frac{1}{x} = +\infty
$$

**Por la izquierda ($x < 0$):**

$$
\lim_{x \to 0^-} \frac{1}{x} = -\infty
$$

---

## ⚙️ Ejemplo 2: Potencia par

$$g(x) = \frac{1}{x^2}$$

En $x = 0$:

**Por ambos lados:** $x^2 > 0$ siempre

$$\lim_{x \to 0^+} \frac{1}{x^2} = +\infty$$
$$\lim_{x \to 0^-} \frac{1}{x^2} = +\infty$$

Podemos escribir: $\lim_{x \to 0} \frac{1}{x^2} = +\infty$

---

## 📖 Determinar el signo del límite

Para $\lim_{x \to a} \frac{p(x)}{q(x)}$ donde $q(a) = 0$ y $p(a) \neq 0$:

1. **Determinar el signo de $p(a)$** (numerador)
2. **Determinar el signo de $q(x)$** cerca de $a$ (por cada lado)
3. **El signo del cociente** según las reglas de signos

| $p(a)$ | $q(x) \to 0$ | Límite |
|--------|--------------|--------|
| $+$ | $0^+$ | $+\infty$ |
| $+$ | $0^-$ | $-\infty$ |
| $-$ | $0^+$ | $-\infty$ |
| $-$ | $0^-$ | $+\infty$ |

---

## ⚙️ Ejemplo 3: Análisis de signos

$$\lim_{x \to 2} \frac{x + 1}{x - 2}$$

**Numerador en $x = 2$:** $2 + 1 = 3 > 0$

**Denominador:**
- Por la derecha ($x > 2$): $x - 2 > 0 \to 0^+$
- Por la izquierda ($x < 2$): $x - 2 < 0 \to 0^-$

**Límites:**
$$\lim_{x \to 2^+} \frac{x + 1}{x - 2} = \frac{3}{0^+} = +\infty$$
$$\lim_{x \to 2^-} \frac{x + 1}{x - 2} = \frac{3}{0^-} = -\infty$$

---

## ⚙️ Ejemplo 4: Factor repetido

$$\lim_{x \to 3} \frac{2x}{(x - 3)^2}$$

**Numerador en $x = 3$:** $6 > 0$

**Denominador:** $(x - 3)^2 > 0$ para todo $x \neq 3$

Por ambos lados: $\to 0^+$

$$
\lim_{x \to 3} \frac{2x}{(x - 3)^2} = \frac{6}{0^+} = +\infty
$$

---

## 📖 Operaciones con infinito

| Operación | Resultado |
|-----------|-----------|
| $L + \infty$ | $\infty$ |
| $L \cdot \infty$ ($L > 0$) | $\infty$ |
| $L \cdot \infty$ ($L < 0$) | $-\infty$ |
| $\frac{L}{\infty}$ | $0$ |
| $\frac{\infty}{L}$ ($L > 0$) | $\infty$ |
| $\infty + \infty$ | $\infty$ |
| $\infty \cdot \infty$ | $\infty$ |

### Formas indeterminadas

| Expresión | Tipo |
|-----------|------|
| $\infty - \infty$ | Indeterminada |
| $\frac{\infty}{\infty}$ | Indeterminada |
| $0 \cdot \infty$ | Indeterminada |

---

## ⚙️ Ejemplo 5: Múltiples raíces

$$\lim_{x \to 1} \frac{x^2 - 1}{(x - 1)^2}$$

$$= \lim_{x \to 1} \frac{(x-1)(x+1)}{(x - 1)^2} = \lim_{x \to 1} \frac{x+1}{x - 1}$$

**Numerador:** $2 > 0$

**Denominador:**
- $x \to 1^+$: $x - 1 \to 0^+$
- $x \to 1^-$: $x - 1 \to 0^-$

$$\lim_{x \to 1^+} = +\infty, \quad \lim_{x \to 1^-} = -\infty$$

---

## 📖 Funciones trigonométricas

$$
\lim_{x \to \pi/2^-} \tan x = +\infty
$$

$$
\lim_{x \to \pi/2^+} \tan x = -\infty
$$

La tangente tiene asíntotas verticales en $x = \frac{\pi}{2} + n\pi$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula los límites laterales:

$$\lim_{x \to -1} \frac{3}{x + 1}$$

<details>
<summary>Ver solución</summary>

$$\lim_{x \to -1^+} \frac{3}{x + 1} = \frac{3}{0^+} = +\infty$$
$$\lim_{x \to -1^-} \frac{3}{x + 1} = \frac{3}{0^-} = -\infty$$
</details>

---

**Ejercicio 2:** Determina:

$$\lim_{x \to 4} \frac{x - 5}{(x - 4)^2}$$

<details>
<summary>Ver solución</summary>

Numerador en $x = 4$: $-1 < 0$
Denominador: $(x-4)^2 > 0 \to 0^+$

$$= \frac{-1}{0^+} = -\infty$$
</details>

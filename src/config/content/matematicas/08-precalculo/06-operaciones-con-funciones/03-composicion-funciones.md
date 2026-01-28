---
title: "Composición de Funciones"
---

# Composición de Funciones

La composición conecta funciones en cadena: la salida de una se convierte en la entrada de la otra. Es una de las operaciones más poderosas y útiles en matemáticas.

---

## 🎯 ¿Qué vas a aprender?

- La definición de composición
- Cómo calcular $(f \circ g)(x)$
- El dominio de una composición
- La diferencia entre $(f \circ g)$ y $(g \circ f)$

---

## 📖 Definición

La **composición** de $f$ con $g$ se denota $(f \circ g)$ y se define como:

$$
(f \circ g)(x) = f(g(x))
$$

Se lee: "$f$ de $g$ de $x$" o "$f$ compuesta con $g$".

### Interpretación

1. Primero aplicas $g$ a $x$: obtienes $g(x)$
2. Luego aplicas $f$ al resultado: obtienes $f(g(x))$

Es una "cadena de funciones".

---

## ⚙️ Ejemplo 1: Composición básica

Sean $f(x) = x^2$ y $g(x) = x + 3$.

**(f ∘ g)(x):**
$$
(f \circ g)(x) = f(g(x)) = f(x + 3) = (x + 3)^2
$$

**(g ∘ f)(x):**
$$
(g \circ f)(x) = g(f(x)) = g(x^2) = x^2 + 3
$$

### ⚠️ ¡El orden importa!

$(x + 3)^2 \neq x^2 + 3$

La composición **no es conmutativa**.

---

## ⚙️ Ejemplo 2: Evaluación numérica

Sean $f(x) = 2x - 1$ y $g(x) = x^2 + 1$.

**Calcula $(f \circ g)(2)$:**

**Método 1:** Primero $g$, luego $f$
- $g(2) = 4 + 1 = 5$
- $f(5) = 10 - 1 = 9$

**Método 2:** Primero la fórmula
- $(f \circ g)(x) = f(x^2 + 1) = 2(x^2 + 1) - 1 = 2x^2 + 1$
- $(f \circ g)(2) = 2(4) + 1 = 9$ ✓

---

## 📖 Dominio de la composición

Para que $(f \circ g)(x)$ esté definida:
1. $x$ debe estar en el dominio de $g$
2. $g(x)$ debe estar en el dominio de $f$

$$
\text{Dom}(f \circ g) = \{x \in \text{Dom}(g) : g(x) \in \text{Dom}(f)\}
$$

---

## ⚙️ Ejemplo 3: Dominio con restricciones

Sean $f(x) = \sqrt{x}$ y $g(x) = x - 4$.

**(f ∘ g)(x) = f(g(x)) = f(x - 4) = √(x - 4)**

**Dominio de $g$:** $\mathbb{R}$

**Restricción:** $g(x) = x - 4 \geq 0$ (para que $f$ lo acepte)
$$x \geq 4$$

**Dominio de $f \circ g$:** $[4, +\infty)$

---

## ⚙️ Ejemplo 4: Composición con fracciones

Sean $f(x) = \frac{1}{x}$ y $g(x) = x - 2$.

**(f ∘ g)(x) = f(x - 2) = 1/(x - 2)**

**Dominio de $g$:** $\mathbb{R}$

**Restricción:** $g(x) = x - 2 \neq 0 \Rightarrow x \neq 2$

**Dominio:** $\mathbb{R} - \{2\}$

---

## ⚙️ Ejemplo 5: Descomponer una función

A veces necesitamos expresar una función como composición de otras más simples.

**Expresa $h(x) = \sqrt{x^2 + 1}$ como composición.**

Identificamos las partes:
- Función "interior": $g(x) = x^2 + 1$
- Función "exterior": $f(u) = \sqrt{u}$

Entonces: $h(x) = (f \circ g)(x) = f(g(x))$

Verificación: $f(g(x)) = f(x^2 + 1) = \sqrt{x^2 + 1}$ ✓

---

## ⚙️ Ejemplo 6: Descomposición alternativa

**Expresa $h(x) = (3x - 5)^4$**

**Opción 1:**
- $g(x) = 3x - 5$
- $f(u) = u^4$
- $h = f \circ g$

**Opción 2:**
- $g(x) = 3x$
- $f(u) = (u - 5)^4$
- $h = f \circ g$

Hay múltiples formas de descomponer.

---

## 📖 Propiedades de la composición

| Propiedad | Fórmula | Ejemplo |
|-----------|---------|---------|
| No conmutativa | $(f \circ g) \neq (g \circ f)$ en general | Ver Ejemplo 1 |
| Asociativa | $(f \circ (g \circ h)) = ((f \circ g) \circ h)$ | Triple composición |
| Elemento neutro | $(f \circ I) = (I \circ f) = f$ | $I(x) = x$ |

---

## ⚙️ Ejemplo 7: Triple composición

Sean $f(x) = x^2$, $g(x) = x + 1$, $h(x) = 2x$.

$$(f \circ g \circ h)(x) = f(g(h(x)))$$

**Paso a paso:**
1. $h(x) = 2x$
2. $g(h(x)) = g(2x) = 2x + 1$
3. $f(g(h(x))) = f(2x + 1) = (2x + 1)^2$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Sean $f(x) = 3x - 2$ y $g(x) = x^2 + 1$. Calcula:

a) $(f \circ g)(x)$
b) $(g \circ f)(x)$
c) $(f \circ g)(2)$

<details>
<summary>Ver soluciones</summary>

a) $(f \circ g)(x) = f(x^2 + 1) = 3(x^2 + 1) - 2 = 3x^2 + 1$

b) $(g \circ f)(x) = g(3x - 2) = (3x - 2)^2 + 1 = 9x^2 - 12x + 5$

c) $(f \circ g)(2) = 3(4) + 1 = 13$
</details>

---

**Ejercicio 2:** Encuentra el dominio de $(f \circ g)(x)$:

a) $f(x) = \sqrt{x}$, $g(x) = 2x - 8$
b) $f(x) = \frac{1}{x - 1}$, $g(x) = x^2$

<details>
<summary>Ver soluciones</summary>

a) $(f \circ g)(x) = \sqrt{2x - 8}$
   
   Restricción: $2x - 8 \geq 0 \Rightarrow x \geq 4$
   
   **Dominio:** $[4, +\infty)$

b) $(f \circ g)(x) = \frac{1}{x^2 - 1}$
   
   Restricción: $x^2 - 1 \neq 0 \Rightarrow x \neq \pm 1$
   
   **Dominio:** $\mathbb{R} - \{-1, 1\}$
</details>

---

**Ejercicio 3:** Descompón como $f \circ g$:

a) $h(x) = |2x - 5|$
b) $h(x) = \frac{1}{(x + 3)^2}$

<details>
<summary>Ver soluciones</summary>

a) $g(x) = 2x - 5$, $f(u) = |u|$

b) $g(x) = x + 3$, $f(u) = \frac{1}{u^2}$
</details>

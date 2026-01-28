---
title: "Propiedades de los Límites"
---

# Propiedades de los Límites

Las propiedades de los límites nos permiten descomponer límites complejos en partes más simples. Son las herramientas fundamentales para el cálculo algebraico de límites.

---

## 🎯 ¿Qué vas a aprender?

- Las propiedades básicas de los límites
- Cómo combinar límites
- Límites de funciones compuestas
- Cuándo aplicar cada propiedad

---

## 📖 Propiedades fundamentales

Sean $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$, donde $L$ y $M$ son números reales.

### 1. Límite de una constante

$$
\lim_{x \to a} c = c
$$

El límite de una constante es la misma constante.

### 2. Límite de la identidad

$$
\lim_{x \to a} x = a
$$

El límite de $x$ cuando $x \to a$ es $a$.

---

## 📖 Propiedades algebraicas

### 3. Suma y resta

$$
\lim_{x \to a} [f(x) \pm g(x)] = L \pm M
$$

"El límite de la suma es la suma de los límites."

### 4. Producto por constante

$$
\lim_{x \to a} [c \cdot f(x)] = c \cdot L
$$

### 5. Producto

$$
\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M
$$

"El límite del producto es el producto de los límites."

### 6. Cociente

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M} \quad \text{si } M \neq 0
$$

"El límite del cociente es el cociente de los límites."

---

## 📖 Propiedades de potencias y raíces

### 7. Potencia

$$
\lim_{x \to a} [f(x)]^n = L^n
$$

### 8. Raíz

$$
\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{L}
$$

(Si $n$ es par, requiere $L \geq 0$)

---

## ⚙️ Ejemplo 1: Aplicación directa

Calcula $\lim_{x \to 2} (3x^2 - 4x + 5)$

**Solución:**

$$= \lim_{x \to 2} 3x^2 - \lim_{x \to 2} 4x + \lim_{x \to 2} 5$$

$$= 3 \cdot \lim_{x \to 2} x^2 - 4 \cdot \lim_{x \to 2} x + 5$$

$$= 3 \cdot 4 - 4 \cdot 2 + 5$$

$$= 12 - 8 + 5 = 9$$

---

## ⚙️ Ejemplo 2: Con cociente

Calcula $\lim_{x \to 3} \frac{x^2 + 1}{x - 1}$

**Verificamos:** El denominador cuando $x \to 3$ es $3 - 1 = 2 \neq 0$.

$$
= \frac{\lim_{x \to 3}(x^2 + 1)}{\lim_{x \to 3}(x - 1)} = \frac{9 + 1}{3 - 1} = \frac{10}{2} = 5
$$

---

## ⚙️ Ejemplo 3: Con raíz

Calcula $\lim_{x \to 4} \sqrt{x^2 + 9}$

$$
= \sqrt{\lim_{x \to 4}(x^2 + 9)} = \sqrt{16 + 9} = \sqrt{25} = 5
$$

---

## 📖 Límites de polinomios

Para cualquier polinomio $P(x)$:

$$
\lim_{x \to a} P(x) = P(a)
$$

**Simplemente sustituimos** $x = a$ en el polinomio.

### ⚙️ Ejemplo 4

$$\lim_{x \to -1} (x^4 + 2x^3 - x + 7)$$

$$= (-1)^4 + 2(-1)^3 - (-1) + 7 = 1 - 2 + 1 + 7 = 7$$

---

## 📖 Límites de funciones racionales

Para una función racional $\frac{P(x)}{Q(x)}$ donde $Q(a) \neq 0$:

$$
\lim_{x \to a} \frac{P(x)}{Q(x)} = \frac{P(a)}{Q(a)}
$$

### ⚙️ Ejemplo 5

$$\lim_{x \to 2} \frac{x^3 - 1}{x^2 + 3}$$

$$= \frac{8 - 1}{4 + 3} = \frac{7}{7} = 1$$

---

## 📖 Límite de función compuesta

Si $\lim_{x \to a} g(x) = L$ y $f$ es continua en $L$:

$$
\lim_{x \to a} f(g(x)) = f\left(\lim_{x \to a} g(x)\right) = f(L)
$$

### ⚙️ Ejemplo 6

$$\lim_{x \to 0} \sin(x^2 + \pi)$$

$$= \sin\left(\lim_{x \to 0}(x^2 + \pi)\right) = \sin(0 + \pi) = \sin\pi = 0$$

---

## 📖 Teorema del encaje (Sandwich)

Si $g(x) \leq f(x) \leq h(x)$ para todo $x$ cerca de $a$ (excepto posiblemente en $a$), y:

Si $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$

$$
\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L
$$

Entonces:

$$
\lim_{x \to a} f(x) = L
$$

### ⚙️ Ejemplo 7

Calcula $\lim_{x \to 0} x^2 \sin\left(\frac{1}{x}\right)$

Sabemos: $-1 \leq \sin\left(\frac{1}{x}\right) \leq 1$

Entonces: $-x^2 \leq x^2 \sin\left(\frac{1}{x}\right) \leq x^2$

Como $\lim_{x \to 0} (-x^2) = 0$ y $\lim_{x \to 0} x^2 = 0$:

$$
\lim_{x \to 0} x^2 \sin\left(\frac{1}{x}\right) = 0
$$

---

## 📊 Resumen de propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Constante | $\lim c = c$ |
| Suma | $\lim(f + g) = \lim f + \lim g$ |
| Producto | $\lim(f \cdot g) = \lim f \cdot \lim g$ |
| Cociente | $\lim(f/g) = \lim f / \lim g$ (si $\lim g \neq 0$) |
| Potencia | $\lim f^n = (\lim f)^n$ |
| Raíz | $\lim \sqrt[n]{f} = \sqrt[n]{\lim f}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula usando propiedades:

a) $\lim_{x \to 1} (x^3 + 2x^2 - x + 4)$
b) $\lim_{x \to -2} \frac{x^2 - 1}{x + 3}$

<details>
<summary>Ver soluciones</summary>

a) $= 1 + 2 - 1 + 4 = 6$

b) $= \frac{4 - 1}{-2 + 3} = \frac{3}{1} = 3$
</details>

---

**Ejercicio 2:** Calcula:

$$\lim_{x \to 4} \sqrt{\frac{x + 5}{x - 1}}$$

<details>
<summary>Ver solución</summary>

$$= \sqrt{\frac{4 + 5}{4 - 1}} = \sqrt{\frac{9}{3}} = \sqrt{3}$$
</details>

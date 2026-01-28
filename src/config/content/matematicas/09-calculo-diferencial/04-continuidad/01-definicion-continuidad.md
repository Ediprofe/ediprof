---
title: "Definición de Continuidad"
---

# Definición de Continuidad

Una función continua es aquella que puedes graficar sin levantar el lápiz del papel. Esta idea intuitiva tiene una definición formal precisa basada en límites.

---

## 🎯 ¿Qué vas a aprender?

- La definición formal de continuidad en un punto
- Las tres condiciones de continuidad
- Cómo verificar continuidad algebraicamente
- Funciones continuas comunes

---

## 📖 Definición formal

Una función $f$ es **continua en $x = a$** si se cumplen tres condiciones:

### Las tres condiciones de continuidad

1. **$f(a)$ existe** (la función está definida en $a$)

2. **$\lim_{x \to a} f(x)$ existe** (el límite existe)

3. **$\lim_{x \to a} f(x) = f(a)$** (el límite iguala al valor de la función)

Si **cualquiera** de estas condiciones falla, la función es **discontinua** en $x = a$.

---

## 📖 Definición compacta

$$
f \text{ es continua en } a \quad \Leftrightarrow \quad \lim_{x \to a} f(x) = f(a)
$$

Esta ecuación implica las tres condiciones simultáneamente.

---

## ⚙️ Ejemplo 1: Verificar continuidad

¿Es $f(x) = x^2 + 3x - 1$ continua en $x = 2$?

**Condición 1:** $f(2) = 4 + 6 - 1 = 9$ ✓ (existe)

**Condición 2:** $\lim_{x \to 2} (x^2 + 3x - 1) = 9$ ✓ (existe)

**Condición 3:** $\lim_{x \to 2} f(x) = 9 = f(2)$ ✓

**Conclusión:** $f$ es continua en $x = 2$.

---

## ⚙️ Ejemplo 2: Falla condición 1

$$
g(x) = \frac{x^2 - 4}{x - 2}
$$

¿Es continua en $x = 2$?

**Condición 1:** $g(2) = \frac{0}{0}$ no está definida ✗

**Conclusión:** $g$ es discontinua en $x = 2$ (aunque el límite existe e iguala 4).

---

## ⚙️ Ejemplo 3: Falla condición 3

$$
h(x) = \begin{cases} x^2 & \text{si } x \neq 1 \\ 5 & \text{si } x = 1 \end{cases}
$$

¿Es continua en $x = 1$?

**Condición 1:** $h(1) = 5$ ✓

**Condición 2:** $\lim_{x \to 1} h(x) = \lim_{x \to 1} x^2 = 1$ ✓

**Condición 3:** $\lim_{x \to 1} h(x) = 1 \neq 5 = h(1)$ ✗

**Conclusión:** $h$ es discontinua en $x = 1$.

---

## ⚙️ Ejemplo 4: Función por partes continua

$$
p(x) = \begin{cases} 2x + 1 & \text{si } x < 3 \\ x^2 - 2 & \text{si } x \geq 3 \end{cases}
$$

¿Es continua en $x = 3$?

**Condición 1:** $p(3) = 9 - 2 = 7$ ✓

**Condición 2:** 
- $\lim_{x \to 3^-} (2x + 1) = 7$
- $\lim_{x \to 3^+} (x^2 - 2) = 7$
- Límite existe: $\lim_{x \to 3} p(x) = 7$ ✓

**Condición 3:** $\lim_{x \to 3} p(x) = 7 = p(3)$ ✓

**Conclusión:** $p$ es continua en $x = 3$.

---

## 📖 Funciones continuas en todo su dominio

Las siguientes funciones son continuas en **todo su dominio natural**:

| Tipo | Ejemplos |
|------|----------|
| Polinomios | $x^2 + 3x - 1$ |
| Funciones racionales | $\frac{1}{x}$ (continua para $x \neq 0$) |
| Raíces | $\sqrt{x}$ (continua para $x \geq 0$) |
| Exponenciales | $e^x$, $2^x$ |
| Logaritmos | $\ln x$ (continua para $x > 0$) |
| Trigonométricas | $\sin x$, $\cos x$ |

---

## 📖 Propiedades de funciones continuas

Si $f$ y $g$ son continuas en $a$, entonces también lo son:

| Operación | Función |
|-----------|---------|
| Suma | $f + g$ |
| Resta | $f - g$ |
| Producto | $f \cdot g$ |
| Cociente | $\frac{f}{g}$ (si $g(a) \neq 0$) |
| Composición | $f \circ g$ (bajo ciertas condiciones) |
| Múltiplo constante | $c \cdot f$ |

---

## ⚙️ Ejemplo 5: Composición continua

¿Es $f(x) = \sqrt{x^2 + 1}$ continua en todo $\mathbb{R}$?

- $g(x) = x^2 + 1$ es un polinomio → continua en $\mathbb{R}$
- $g(x) \geq 1 > 0$ para todo $x$
- $h(u) = \sqrt{u}$ es continua para $u > 0$

Por composición: $f = h \circ g$ es continua en todo $\mathbb{R}$.

---

## 📖 Continuidad lateral

$f$ es **continua por la derecha** en $a$ si:

$$
\lim_{x \to a^+} f(x) = f(a)
$$

$f$ es **continua por la izquierda** en $a$ si:

$$
\lim_{x \to a^-} f(x) = f(a)
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Determina si la función es continua en el punto indicado:

$$
f(x) = \frac{x^2 - 9}{x - 3}
$$

en $x = 3$

<details>
<summary>Ver solución</summary>

$f(3)$ no existe (división por cero).

**Discontinua en $x = 3$** (falla condición 1)
</details>

---

**Ejercicio 2:** Encuentra el valor de $k$ para que $f$ sea continua en $x = 2$:

$$
f(x) = \begin{cases} x^2 - 1 & \text{si } x < 2 \\ kx + 1 & \text{si } x \geq 2 \end{cases}
$$

<details>
<summary>Ver solución</summary>

Para continuidad: $\lim_{x \to 2^-} f(x) = f(2)$

$\lim_{x \to 2^-} (x^2 - 1) = 3$

$f(2) = 2k + 1$

Igualando: $2k + 1 = 3 \Rightarrow k = 1$
</details>

---
title: "Función Inversa"
---

# Función Inversa

La función inversa "deshace" lo que hace la función original. Si $f$ convierte $a$ en $b$, entonces $f^{-1}$ convierte $b$ de vuelta en $a$.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de función inversa
- Cuándo existe una inversa
- Cómo encontrar la inversa algebraicamente
- Relación gráfica entre $f$ y $f^{-1}$

---

## 📖 Definición

La **función inversa** de $f$, denotada $f^{-1}$, satisface:

$$
f^{-1}(f(x)) = x \quad \text{para todo } x \text{ en Dom}(f)
$$

$$
f(f^{-1}(y)) = y \quad \text{para todo } y \text{ en Ran}(f)
$$

### ⚠️ Notación importante

$f^{-1}(x)$ **NO** significa $\frac{1}{f(x)}$.

- $f^{-1}$ = función inversa
- $\frac{1}{f}$ = recíproco de $f$

---

## 📖 Condición de existencia

Una función tiene inversa si y solo si es **biyectiva** (inyectiva y suprayectiva).

En la práctica, para que exista $f^{-1}$:

> La función debe ser **inyectiva** (uno a uno): diferentes entradas dan diferentes salidas.

Esto se verifica con la **prueba de la línea horizontal**.

---

## ⚙️ Ejemplo 1: Función con inversa

$f(x) = 2x + 3$ es inyectiva (es una recta con pendiente no nula).

**Para encontrar $f^{-1}$:**

1. Escribimos $y = 2x + 3$
2. Despejamos $x$:
   $$y - 3 = 2x$$
   $$x = \frac{y - 3}{2}$$
3. Intercambiamos $x$ y $y$:
   $$y = \frac{x - 3}{2}$$

**Resultado:** $f^{-1}(x) = \frac{x - 3}{2}$

**Verificación:**
$$f(f^{-1}(x)) = f\left(\frac{x - 3}{2}\right) = 2 \cdot \frac{x - 3}{2} + 3 = x - 3 + 3 = x \quad ✓$$

---

## ⚙️ Ejemplo 2: Función sin inversa (sin restricción)

$f(x) = x^2$ no es inyectiva en $\mathbb{R}$ porque $f(2) = f(-2) = 4$.

No tiene inversa en todo $\mathbb{R}$.

**Con restricción de dominio:**

Si definimos $f: [0, +\infty) \to [0, +\infty)$ con $f(x) = x^2$:

Ahora sí es inyectiva, y su inversa es $f^{-1}(x) = \sqrt{x}$.

---

## 📖 Algoritmo para encontrar la inversa

1. Verifica que $f$ sea inyectiva
2. Escribe $y = f(x)$
3. Despeja $x$ en términos de $y$
4. Intercambia $x$ y $y$
5. El resultado es $f^{-1}(x)$

---

## ⚙️ Ejemplo 3: Función racional

Encuentra la inversa de $f(x) = \frac{3x + 2}{x - 1}$, $x \neq 1$.

**Paso 1:** $y = \frac{3x + 2}{x - 1}$

**Paso 2:** Despejamos $x$:
$$y(x - 1) = 3x + 2$$
$$yx - y = 3x + 2$$
$$yx - 3x = y + 2$$
$$x(y - 3) = y + 2$$
$$x = \frac{y + 2}{y - 3}$$

**Paso 3:** Intercambiamos:
$$f^{-1}(x) = \frac{x + 2}{x - 3}, \quad x \neq 3$$

---

## 📖 Relación gráfica

Las gráficas de $f$ y $f^{-1}$ son **simétricas respecto a la recta $y = x$**.

### Interpretación

Si $(a, b)$ está en la gráfica de $f$, entonces $(b, a)$ está en la gráfica de $f^{-1}$.

Se "intercambian" las coordenadas.

---

## ⚙️ Ejemplo 4: Dominio y rango de la inversa

Sea $f(x) = \sqrt{x - 2}$ con dominio $[2, +\infty)$ y rango $[0, +\infty)$.

**Inversa:**

$y = \sqrt{x - 2} \Rightarrow y^2 = x - 2 \Rightarrow x = y^2 + 2$

$f^{-1}(x) = x^2 + 2$

**Pero con restricción:** Solo para $x \geq 0$ (el rango de $f$).

**Dominio de $f^{-1}$:** $[0, +\infty)$ = Rango de $f$

**Rango de $f^{-1}$:** $[2, +\infty)$ = Dominio de $f$

---

## 📊 Resumen de propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Definición | $f^{-1}(f(x)) = x$ y $f(f^{-1}(x)) = x$ |
| Composición | $(f \circ f^{-1}) = (f^{-1} \circ f) = I$ |
| Dominio de $f^{-1}$ | = Rango de $f$ |
| Rango de $f^{-1}$ | = Dominio de $f$ |
| Inversa de la inversa | $(f^{-1})^{-1} = f$ |
| Simetría gráfica | Respecto a $y = x$ |

---

## ⚙️ Ejemplo 5: Verificación

Verifica que $f(x) = x^3$ y $g(x) = \sqrt[3]{x}$ son inversas.

$$(f \circ g)(x) = f(\sqrt[3]{x}) = (\sqrt[3]{x})^3 = x \quad ✓$$

$$(g \circ f)(x) = g(x^3) = \sqrt[3]{x^3} = x \quad ✓$$

Son inversas entre sí.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la inversa:

a) $f(x) = 5x - 7$
b) $g(x) = \frac{x + 4}{3}$
c) $h(x) = x^3 + 1$

<details>
<summary>Ver soluciones</summary>

a) $y = 5x - 7 \Rightarrow x = \frac{y + 7}{5}$
   
   $f^{-1}(x) = \frac{x + 7}{5}$

b) $y = \frac{x + 4}{3} \Rightarrow 3y = x + 4 \Rightarrow x = 3y - 4$
   
   $g^{-1}(x) = 3x - 4$

c) $y = x^3 + 1 \Rightarrow x^3 = y - 1 \Rightarrow x = \sqrt[3]{y - 1}$
   
   $h^{-1}(x) = \sqrt[3]{x - 1}$
</details>

---

**Ejercicio 2:** ¿Tiene inversa? Justifica.

a) $f(x) = x^2 - 4$
b) $g(x) = 2^x$
c) $h(x) = |x|$

<details>
<summary>Ver soluciones</summary>

a) **No** en $\mathbb{R}$ (no es inyectiva: $f(2) = f(-2) = 0$). Con restricción $x \geq 0$ o $x \leq 0$, sí.

b) **Sí**, es inyectiva (exponencial siempre creciente). $g^{-1}(x) = \log_2 x$

c) **No** en $\mathbb{R}$ (no es inyectiva: $|2| = |-2| = 2$)
</details>

---

**Ejercicio 3:** Si $f(3) = 7$, ¿cuánto vale $f^{-1}(7)$?

<details>
<summary>Ver solución</summary>

$f^{-1}(7) = 3$

Porque la inversa "deshace" lo que hace $f$.
</details>

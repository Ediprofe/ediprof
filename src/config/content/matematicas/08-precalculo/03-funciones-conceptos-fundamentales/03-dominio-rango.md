---
title: "Dominio y Rango"
---

# Dominio y Rango

¿Para qué valores de $x$ tiene sentido una función? ¿Qué valores de $y$ puede producir? Responder estas preguntas es encontrar el dominio y el rango.

---

## 🎯 ¿Qué vas a aprender?

- Dominio: valores permitidos de entrada
- Rango: valores posibles de salida
- Técnicas para encontrar el dominio algebraicamente
- Cómo determinar el rango desde la gráfica

---

## 📖 Definiciones

| Concepto | Definición |
|----------|------------|
| **Dominio** | Conjunto de todos los valores de $x$ para los cuales $f(x)$ está definida |
| **Rango** | Conjunto de todos los valores de $y$ que la función puede producir |

**Notación:**
- Dominio: $\text{Dom}(f)$ o $D_f$
- Rango: $\text{Ran}(f)$ o $R_f$ o $\text{Im}(f)$

---

## 📖 Restricciones del dominio

El dominio incluye todos los números reales **excepto** aquellos que causan:

| Problema | Ejemplo | Restricción |
|----------|---------|-------------|
| División por cero | $f(x) = \frac{1}{x-3}$ | $x \neq 3$ |
| Raíz cuadrada de negativo | $f(x) = \sqrt{x-2}$ | $x \geq 2$ |
| Logaritmo de no positivo | $f(x) = \ln(x+1)$ | $x > -1$ |

---

## ⚙️ Ejemplo 1: Función polinómica

Encuentra el dominio de $f(x) = x^3 - 4x + 2$

**Análisis:** Los polinomios no tienen restricciones.

**Dominio:** $\mathbb{R}$ o $(-\infty, +\infty)$

---

## ⚙️ Ejemplo 2: Función racional

Encuentra el dominio de $f(x) = \frac{x + 5}{x^2 - 9}$

**Paso 1:** El denominador no puede ser cero.
$$x^2 - 9 = 0 \quad \Rightarrow \quad x = \pm 3$$

**Paso 2:** Excluimos esos valores.

**Dominio:** $\mathbb{R} - \{-3, 3\}$ o $(-\infty, -3) \cup (-3, 3) \cup (3, +\infty)$

---

## ⚙️ Ejemplo 3: Raíz cuadrada

Encuentra el dominio de $f(x) = \sqrt{5 - 2x}$

**Paso 1:** El radicando debe ser $\geq 0$.
$$5 - 2x \geq 0$$
$$-2x \geq -5$$
$$x \leq \frac{5}{2}$$

**Dominio:** $\left(-\infty, \frac{5}{2}\right]$

---

## ⚙️ Ejemplo 4: Combinación de restricciones

Encuentra el dominio de $f(x) = \frac{\sqrt{x - 1}}{x - 4}$

**Restricción 1 (raíz):** $x - 1 \geq 0 \Rightarrow x \geq 1$

**Restricción 2 (denominador):** $x - 4 \neq 0 \Rightarrow x \neq 4$

**Combinamos:** $x \geq 1$ **y** $x \neq 4$

**Dominio:** $[1, 4) \cup (4, +\infty)$

---

## ⚙️ Ejemplo 5: Raíz en el denominador

Encuentra el dominio de $g(x) = \frac{3}{\sqrt{x + 2}}$

**Restricción 1 (raíz):** $x + 2 \geq 0 \Rightarrow x \geq -2$

**Restricción 2 (denominador):** $\sqrt{x + 2} \neq 0 \Rightarrow x \neq -2$

**Combinamos:** $x > -2$

**Dominio:** $(-2, +\infty)$

---

## 📖 Encontrar el rango

El rango es más difícil de determinar algebraicamente. Las estrategias principales son:

1. **Analizar la gráfica** (método visual)
2. **Despejar $x$ en términos de $y$** y ver para qué valores de $y$ es posible
3. **Analizar el comportamiento** de la función

---

## ⚙️ Ejemplo 6: Rango de una función cuadrática

Encuentra el rango de $f(x) = x^2 - 4$

**Análisis:** Es una parábola que abre hacia arriba con vértice en $(0, -4)$.

El valor mínimo de $f(x)$ es $-4$ (en el vértice).

**Rango:** $[-4, +\infty)$

---

## ⚙️ Ejemplo 7: Rango de una función racional

Encuentra el rango de $f(x) = \frac{x}{x + 1}$

**Método:** Despejamos $x$ en términos de $y$.

Sea $y = \frac{x}{x + 1}$

**Paso 1:** Multiplicamos por $(x + 1)$
$$y(x + 1) = x$$
$$yx + y = x$$

**Paso 2:** Agrupamos términos con $x$
$$yx - x = -y$$
$$x(y - 1) = -y$$

**Paso 3:** Despejamos $x$
$$x = \frac{-y}{y - 1} = \frac{y}{1 - y}$$

**Paso 4:** Para que exista $x$ real, necesitamos $y - 1 \neq 0$, es decir, $y \neq 1$.

**Rango:** $\mathbb{R} - \{1\}$ o $(-\infty, 1) \cup (1, +\infty)$

---

## ⚙️ Ejemplo 8: Rango de raíz cuadrada

Encuentra el rango de $f(x) = \sqrt{x - 3}$

**Análisis:** La raíz cuadrada siempre da valores $\geq 0$.

Cuando $x = 3$: $f(3) = 0$
Cuando $x \to \infty$: $f(x) \to \infty$

**Rango:** $[0, +\infty)$

---

## 📊 Resumen: Funciones comunes

| Función | Dominio | Rango |
|---------|---------|-------|
| $f(x) = c$ (constante) | $\mathbb{R}$ | $\{c\}$ |
| $f(x) = x$ (identidad) | $\mathbb{R}$ | $\mathbb{R}$ |
| $f(x) = x^2$ | $\mathbb{R}$ | $[0, +\infty)$ |
| $f(x) = x^3$ | $\mathbb{R}$ | $\mathbb{R}$ |
| $f(x) = \sqrt{x}$ | $[0, +\infty)$ | $[0, +\infty)$ |
| $f(x) = \frac{1}{x}$ | $\mathbb{R} - \{0\}$ | $\mathbb{R} - \{0\}$ |
| $f(x) = \|x\|$ | $\mathbb{R}$ | $[0, +\infty)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el dominio:

a) $f(x) = \frac{2x + 1}{x^2 - 4}$
b) $g(x) = \sqrt{3x - 6}$
c) $h(x) = \frac{1}{\sqrt{x - 5}}$

<details>
<summary>Ver soluciones</summary>

a) $x^2 - 4 \neq 0 \Rightarrow x \neq \pm 2$
   
   **Dominio:** $\mathbb{R} - \{-2, 2\}$

b) $3x - 6 \geq 0 \Rightarrow x \geq 2$
   
   **Dominio:** $[2, +\infty)$

c) Necesitamos $x - 5 > 0$ (estricto porque está en denominador)
   
   **Dominio:** $(5, +\infty)$
</details>

---

**Ejercicio 2:** Encuentra el dominio y el rango:

a) $f(x) = x^2 + 2$
b) $g(x) = -\sqrt{x} + 4$
c) $h(x) = |x - 1|$

<details>
<summary>Ver soluciones</summary>

a) **Dominio:** $\mathbb{R}$
   
   **Rango:** $[2, +\infty)$ (el mínimo de $x^2$ es 0, entonces el mínimo de $x^2 + 2$ es 2)

b) **Dominio:** $[0, +\infty)$
   
   **Rango:** $(-\infty, 4]$ (cuando $x = 0$, $g = 4$; cuando $x \to \infty$, $g \to -\infty$)

c) **Dominio:** $\mathbb{R}$
   
   **Rango:** $[0, +\infty)$ (el valor absoluto siempre es $\geq 0$)
</details>

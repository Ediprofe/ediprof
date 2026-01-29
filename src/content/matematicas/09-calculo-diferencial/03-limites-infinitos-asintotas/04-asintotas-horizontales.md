# Asíntotas Horizontales

Las asíntotas horizontales describen el comportamiento de una función cuando $x$ tiende a infinito. Representan el valor al que la función se "estabiliza" a largo plazo.

---

## 🎯 ¿Qué vas a aprender?

- Definición de asíntota horizontal
- Cómo calcularlas usando límites
- Relación con funciones racionales
- Funciones con asíntotas horizontales diferentes

---

## 📖 Definición

La recta $y = L$ es una **asíntota horizontal** de $f(x)$ si:

$$
\lim_{x \to +\infty} f(x) = L \quad \text{o} \quad \lim_{x \to -\infty} f(x) = L
$$

Una función puede tener:
- Una sola asíntota horizontal (misma en $\pm\infty$)
- Dos asíntotas horizontales diferentes
- Ninguna asíntota horizontal

---

## 📖 Funciones racionales

Para $f(x) = \frac{a_n x^n + \cdots}{b_m x^m + \cdots}$:

| Relación de grados | Asíntota horizontal |
|-------------------|---------------------|
| $n < m$ | $y = 0$ |
| $n = m$ | $y = \frac{a_n}{b_m}$ |
| $n > m$ | No existe |

---

## ⚙️ Ejemplo 1: Grados iguales

$$
f(x) = \frac{3x^2 + x - 1}{2x^2 - 5}
$$

Grados iguales (ambos 2):

$$
\lim_{x \to \pm\infty} f(x) = \frac{3}{2}
$$

**Asíntota horizontal:** $y = \frac{3}{2}$

---

## ⚙️ Ejemplo 2: Grado menor en numerador

$$
g(x) = \frac{x + 2}{x^2 + 1}
$$

Grado 1 < Grado 2:

$$
\lim_{x \to \pm\infty} g(x) = 0
$$

**Asíntota horizontal:** $y = 0$

---

## ⚙️ Ejemplo 3: Sin asíntota horizontal

$$
h(x) = \frac{x^3 - 1}{x + 2}
$$

Grado 3 > Grado 1:

$$
\lim_{x \to \pm\infty} h(x) = \pm\infty
$$

**No hay asíntota horizontal** (hay asíntota oblicua).

---

## 📖 Asíntotas horizontales diferentes

Algunas funciones tienen límites diferentes en $+\infty$ y $-\infty$.

---

## ⚙️ Ejemplo 4: Dos asíntotas horizontales

$$
f(x) = \frac{2x}{\sqrt{x^2 + 1}}
$$

**Para $x \to +\infty$:**

$$
\sqrt{x^2 + 1} = |x|\sqrt{1 + \frac{1}{x^2}} = x\sqrt{1 + \frac{1}{x^2}}
$$ 

(porque $x > 0$)

$$
\lim_{x \to +\infty} \frac{2x}{x\sqrt{1 + \frac{1}{x^2}}} = \frac{2}{\sqrt{1}} = 2
$$

**Para $x \to -\infty$:**

$$
\sqrt{x^2 + 1} = |x|\sqrt{1 + \frac{1}{x^2}} = -x\sqrt{1 + \frac{1}{x^2}}
$$

(porque $x < 0$, $|x| = -x$)

$$
\lim_{x \to -\infty} \frac{2x}{-x\sqrt{1 + \frac{1}{x^2}}} = \frac{2}{-1} = -2
$$

**Asíntotas horizontales:** $y = 2$ (derecha) y $y = -2$ (izquierda)

---

## 📖 Funciones exponenciales

$$
f(x) = \frac{1}{1 + e^{-x}}
$$

**Para $x \to +\infty$:** $e^{-x} \to 0$
$$
\lim_{x \to +\infty} f(x) = \frac{1}{1 + 0} = 1
$$

**Para $x \to -\infty$:** $e^{-x} \to +\infty$
$$
\lim_{x \to -\infty} f(x) = \frac{1}{1 + \infty} = 0
$$

**Asíntotas horizontales:** $y = 1$ y $y = 0$

---

## 📖 La curva puede cruzar su asíntota

A diferencia de las asíntotas verticales, una función **puede cruzar** su asíntota horizontal.

---

## ⚙️ Ejemplo 5: Cruzando la asíntota

$$
f(x) = \frac{\sin x}{x}
$$

**Asíntota horizontal:** $y = 0$ (porque $\lim_{x \to \pm\infty} \frac{\sin x}{x} = 0$)

Pero $f(x) = 0$ cuando $\sin x = 0$, es decir, en $x = n\pi$.

La función cruza la asíntota infinitas veces.

---

## ⚙️ Ejemplo 6: Función arcotangente

$$
f(x) = \arctan x
$$

$$
\lim_{x \to +\infty} \arctan x = \frac{\pi}{2}
$$

$$
\lim_{x \to -\infty} \arctan x = -\frac{\pi}{2}
$$

**Asíntotas horizontales:** $y = \frac{\pi}{2}$ y $y = -\frac{\pi}{2}$

---

## 📊 Resumen de asíntotas horizontales

| Tipo de función | Asíntota horizontal |
|-----------------|---------------------|
| $\frac{ax^n + \cdots}{bx^n + \cdots}$ | $y = \frac{a}{b}$ |
| $\frac{\text{menor grado}}{\text{mayor grado}}$ | $y = 0$ |
| $e^{-x}$ cuando $x \to +\infty$ | $y = 0$ |
| $e^{x}$ cuando $x \to -\infty$ | $y = 0$ |
| $\arctan x$ | $y = \pm\frac{\pi}{2}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra las asíntotas horizontales:

a) $f(x) = \frac{5x - 3}{2x + 7}$

b) $g(x) = \frac{4}{x^2 + 1}$

<details>
<summary>Ver soluciones</summary>

a) Grados iguales: $y = \frac{5}{2}$

b) Grado menor en numerador: $y = 0$
</details>

---

**Ejercicio 2:** Encuentra las asíntotas horizontales:

$$
h(x) = \frac{3x}{\sqrt{x^2 + 4}}
$$

<details>
<summary>Ver solución</summary>

**Para $x \to +\infty$:**
$$
\lim_{x \to +\infty} \frac{3x}{x\sqrt{1 + \frac{4}{x^2}}} = \frac{3}{1} = 3
$$

**Para $x \to -\infty$:**
$$
\lim_{x \to -\infty} \frac{3x}{-x\sqrt{1 + \frac{4}{x^2}}} = \frac{3}{-1} = -3
$$

**A.H.:** $y = 3$ y $y = -3$
</details>

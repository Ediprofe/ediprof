---
title: "Sucesiones Recursivas"
---

# Sucesiones Recursivas

Las sucesiones definidas recursivamente calculan cada término a partir de los anteriores. Son útiles para modelar procesos iterativos.

---

## 🎯 ¿Qué vas a aprender?

- Sucesiones de primer orden
- Sucesiones lineales
- Encontrar fórmulas explícitas
- Análisis de estabilidad

---

## 📖 Definición

Una **sucesión recursiva de primer orden** tiene la forma:

$$
a_{n+1} = f(a_n), \quad a_1 = a_0
$$

donde $f$ es alguna función.

---

## 📖 Sucesiones recursivas lineales

$$
a_{n+1} = ra_n + b
$$

**Solución general:**
- Si $r \neq 1$: $a_n = r^{n-1}(a_1 - L) + L$ donde $L = \frac{b}{1-r}$
- Si $r = 1$: $a_n = a_1 + (n-1)b$

---

## ⚙️ Ejemplo 1: Sucesión lineal

$$
a_1 = 5, \quad a_{n+1} = 2a_n + 3
$$

Aquí $r = 2$, $b = 3$, $L = \frac{3}{1-2} = -3$

$$
a_n = 2^{n-1}(5 - (-3)) + (-3) = 8 \cdot 2^{n-1} - 3 = 2^{n+2} - 3
$$

Verificación: $a_1 = 8 - 3 = 5$ ✓, $a_2 = 16 - 3 = 13 = 2(5) + 3$ ✓

---

## ⚙️ Ejemplo 2: Punto fijo

$$
a_{n+1} = \frac{1}{2}(a_n + 4), \quad a_1 = 0
$$

Punto fijo: $L = \frac{1}{2}(L + 4)$ → $L = 4$

Aquí $r = \frac{1}{2}$, así que:

$$
a_n = \left(\frac{1}{2}\right)^{n-1}(0 - 4) + 4 = 4 - \frac{4}{2^{n-1}}
$$

Como $|r| < 1$, converge al punto fijo 4.

---

## 📖 Estabilidad de puntos fijos

Para $a_{n+1} = f(a_n)$, un punto fijo $L$ satisface $L = f(L)$.

- Si $|f'(L)| < 1$: punto fijo **estable** (atractor)
- Si $|f'(L)| > 1$: punto fijo **inestable** (repulsor)

---

## ⚙️ Ejemplo 3: Logística

$$
a_{n+1} = 2a_n(1 - a_n), \quad a_1 = 0.1
$$

Puntos fijos: $L = 2L(1-L)$ → $L = 0$ o $L = \frac{1}{2}$

$f(x) = 2x(1-x)$, $f'(x) = 2 - 4x$

- En $L = 0$: $f'(0) = 2$ → inestable
- En $L = \frac{1}{2}$: $f'(\frac{1}{2}) = 0$ → muy estable

La sucesión converge a $\frac{1}{2}$.

---

## ⚙️ Ejemplo 4: Método de Newton-Raphson

Para encontrar $\sqrt{2}$: resolver $x^2 = 2$

$$
a_{n+1} = a_n - \frac{a_n^2 - 2}{2a_n} = \frac{a_n + 2/a_n}{2}
$$

Con $a_1 = 1$:
- $a_1 = 1$
- $a_2 = 1.5$
- $a_3 = 1.4167$
- $a_4 = 1.4142...$

¡Convergencia muy rápida!

---

## 📖 Sucesiones de segundo orden

$$
a_{n+2} = f(a_{n+1}, a_n)
$$

Ejemplo: Fibonacci: $F_{n+2} = F_{n+1} + F_n$

---

## ⚙️ Ejemplo 5: Fibonacci

$$
F_1 = F_2 = 1, \quad F_{n+2} = F_{n+1} + F_n
$$

Fórmula de Binet:

$$
F_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $a_1 = 3$, $a_{n+1} = 3a_n - 4$.

<details>
<summary>Ver solución</summary>

$r = 3$, $b = -4$, $L = \frac{-4}{1-3} = 2$

$$
a_n = 3^{n-1}(3 - 2) + 2 = 3^{n-1} + 2
$$
</details>

---

**Ejercicio 2:** Si $a_1 = 2$ y $a_{n+1} = \sqrt{2a_n}$, encuentra el límite.

<details>
<summary>Ver solución</summary>

$L = \sqrt{2L}$ → $L^2 = 2L$ → $L = 2$ (descartando 0)
</details>

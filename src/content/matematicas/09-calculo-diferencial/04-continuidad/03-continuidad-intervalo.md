# Continuidad en un Intervalo

Una función puede ser continua en un punto pero discontinua en otro. Estudiar la continuidad en intervalos nos da una visión global del comportamiento de la función.

---

## 🎯 ¿Qué vas a aprender?

- Continuidad en intervalos abiertos y cerrados
- Continuidad lateral en extremos
- Funciones continuas por partes
- Continuidad uniforme (concepto básico)

---

## 📖 Continuidad en intervalo abierto

$f$ es **continua en $(a, b)$** si es continua en cada punto del intervalo.

$$
\forall c \in (a, b): \lim_{x \to c} f(x) = f(c)
$$

---

## 📖 Continuidad en intervalo cerrado

$f$ es **continua en $[a, b]$** si:

1. $f$ es continua en $(a, b)$ (interior)
2. $f$ es continua por la **derecha** en $a$: $\lim_{x \to a^+} f(x) = f(a)$
3. $f$ es continua por la **izquierda** en $b$: $\lim_{x \to b^-} f(x) = f(b)$

Los extremos solo requieren continuidad **unilateral**.

---

## ⚙️ Ejemplo 1: Continuidad en intervalo cerrado

$$
f(x) = \sqrt{x}
$$

en $[0, 4]$

**En el interior $(0, 4)$:** $f$ es continua (composición de funciones continuas)

**En $x = 0$:** $\lim_{x \to 0^+} \sqrt{x} = 0 = f(0)$ ✓

**En $x = 4$:** $\lim_{x \to 4^-} \sqrt{x} = 2 = f(4)$ ✓

**Conclusión:** $f$ es continua en $[0, 4]$

---

## ⚙️ Ejemplo 2: Raíz cuadrada modificada

$$
g(x) = \sqrt{4 - x^2}
$$

en $[-2, 2]$

**Dominio:** $4 - x^2 \geq 0 \Rightarrow |x| \leq 2$

**En el interior $(-2, 2)$:** Continua

**En $x = -2$:** $\lim_{x \to -2^+} g(x) = 0 = g(-2)$ ✓

**En $x = 2$:** $\lim_{x \to 2^-} g(x) = 0 = g(2)$ ✓

**Conclusión:** $g$ es continua en $[-2, 2]$

---

## 📖 Funciones continuas en su dominio

Una función es **continua** (sin especificar dónde) si es continua en cada punto de su dominio natural.

### Ejemplos

| Función | Dominio | Continuidad |
|---------|---------|-------------|
| $x^2 + 1$ | $\mathbb{R}$ | Continua en $\mathbb{R}$ |
| $\frac{1}{x}$ | $\mathbb{R} - \{0\}$ | Continua en su dominio |
| $\sqrt{x}$ | $[0, +\infty)$ | Continua en $[0, +\infty)$ |
| $\ln x$ | $(0, +\infty)$ | Continua en $(0, +\infty)$ |

---

## 📖 Funciones continuas por partes

Una función es **continua por partes** en $[a, b]$ si:

1. El intervalo se puede dividir en un número finito de subintervalos
2. En cada subintervalo la función es continua
3. En los puntos de división, los límites laterales existen (pueden ser diferentes)

---

## ⚙️ Ejemplo 3: Continua por partes

$$
f(x) = \begin{cases} x^2 & \text{si } x < 1 \\ 2x - 1 & \text{si } x \geq 1 \end{cases}
$$

**En $(-\infty, 1)$:** $x^2$ es continua

**En $[1, +\infty)$:** $2x - 1$ es continua

**En $x = 1$:**
- $\lim_{x \to 1^-} x^2 = 1$
- $\lim_{x \to 1^+} (2x - 1) = 1$

Los límites laterales son iguales, así que $f$ es **continua** en $x = 1$ también.

$f$ es continua en todo $\mathbb{R}$.

---

## ⚙️ Ejemplo 4: Continua por partes con saltos

La función escalón:

$$
\lfloor x \rfloor = \text{mayor entero } \leq x
$$

- Es continua en cada intervalo $[n, n+1)$
- Tiene discontinuidades de salto en cada entero

Es **continua por partes** en $\mathbb{R}$.

---

## 📖 Propiedades de funciones continuas en intervalos cerrados

Si $f$ es continua en $[a, b]$:

1. **Teorema del valor extremo:** $f$ alcanza su máximo y mínimo en $[a, b]$

2. **Teorema del valor intermedio:** $f$ toma todos los valores entre $f(a)$ y $f(b)$

3. **Acotación:** $f$ está acotada en $[a, b]$

---

## ⚙️ Ejemplo 5: Determinar intervalo de continuidad

$$
h(x) = \frac{x + 2}{x^2 - 4}
$$

**Discontinuidades:** $x^2 - 4 = 0 \Rightarrow x = \pm 2$

**Intervalos de continuidad:**
- $(-\infty, -2)$
- $(-2, 2)$
- $(2, +\infty)$

---

## 📊 Resumen

| Tipo de intervalo | Condiciones de continuidad |
|-------------------|---------------------------|
| Abierto $(a, b)$ | Continua en cada punto interior |
| Cerrado $[a, b]$ | + Continuidad lateral en extremos |
| Semiabierto $[a, b)$ | Continua por la derecha en $a$ |
| Semiabierto $(a, b]$ | Continua por la izquierda en $b$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Determina los intervalos de continuidad:

$$
f(x) = \frac{1}{x(x-3)}
$$

<details>
<summary>Ver solución</summary>

Discontinuidades en $x = 0$ y $x = 3$

**Intervalos de continuidad:**
- $(-\infty, 0)$
- $(0, 3)$
- $(3, +\infty)$
</details>

---

**Ejercicio 2:** ¿Es continua en $[0, 2]$?

$$
g(x) = \begin{cases} x + 1 & \text{si } 0 \leq x < 1 \\ 2 & \text{si } x = 1 \\ 3 - x & \text{si } 1 < x \leq 2 \end{cases}
$$

<details>
<summary>Ver solución</summary>

En $x = 1$:
- $\lim_{x \to 1^-} (x + 1) = 2$
- $\lim_{x \to 1^+} (3 - x) = 2$
- $g(1) = 2$

Los tres son iguales. **Sí, es continua en $[0, 2]$**
</details>

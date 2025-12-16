# Criterios de Convergencia

Los criterios de convergencia nos permiten determinar si una serie converge sin necesidad de encontrar su suma.

---

## 🎯 ¿Qué vas a aprender?

- Criterio de divergencia
- Criterio de la integral
- Criterio de comparación
- Criterio de comparación por límite

---

## 📖 Criterio de divergencia (n-ésimo término)

> Si $\lim_{n \to \infty} a_n \neq 0$, entonces $\sum a_n$ diverge.

**Importante:** Si $\lim a_n = 0$, NO se puede concluir nada.

---

## ⚙️ Ejemplo 1: Divergencia inmediata

$$\sum_{n=1}^{\infty} \frac{n+1}{2n+3}$$

$\lim \frac{n+1}{2n+3} = \frac{1}{2} \neq 0$ → **Diverge**

---

## 📖 Criterio de la integral

Si $f$ es positiva, continua y decreciente para $x \geq 1$, y $a_n = f(n)$:

$$\sum_{n=1}^{\infty} a_n \text{ converge } \Leftrightarrow \int_1^{\infty} f(x)\,dx \text{ converge}$$

---

## ⚙️ Ejemplo 2: Serie p

$$\sum_{n=1}^{\infty} \frac{1}{n^p}$$

$$\int_1^{\infty} \frac{1}{x^p}\,dx = \begin{cases} \frac{1}{p-1} & p > 1 \\ \infty & p \leq 1 \end{cases}$$

**Resultado:** $\sum \frac{1}{n^p}$ converge si y solo si $p > 1$.

---

## ⚙️ Ejemplo 3: Logaritmo

$$\sum_{n=2}^{\infty} \frac{1}{n\ln n}$$

$$\int_2^{\infty} \frac{1}{x\ln x}\,dx = [\ln(\ln x)]_2^{\infty} = \infty$$

**Diverge.**

---

## 📖 Criterio de comparación directa

Si $0 \leq a_n \leq b_n$ para todo $n$:

- $\sum b_n$ converge → $\sum a_n$ converge
- $\sum a_n$ diverge → $\sum b_n$ diverge

---

## ⚙️ Ejemplo 4: Comparación

$$\sum_{n=1}^{\infty} \frac{1}{n^2 + 1}$$

$\frac{1}{n^2 + 1} < \frac{1}{n^2}$ y $\sum \frac{1}{n^2}$ converge (p = 2 > 1)

**Converge.**

---

## 📖 Criterio de comparación por límite

Si $a_n, b_n > 0$ y $\lim \frac{a_n}{b_n} = L$:

- $0 < L < \infty$: ambas convergen o ambas divergen
- $L = 0$: $\sum b_n$ converge → $\sum a_n$ converge
- $L = \infty$: $\sum b_n$ diverge → $\sum a_n$ diverge

---

## ⚙️ Ejemplo 5: Comparación por límite

$$\sum_{n=1}^{\infty} \frac{n^2 + 3n}{n^4 - 2}$$

Comparamos con $\frac{1}{n^2}$:

$$\lim \frac{\frac{n^2+3n}{n^4-2}}{\frac{1}{n^2}} = \lim \frac{n^4 + 3n^3}{n^4 - 2} = 1$$

Como $\sum \frac{1}{n^2}$ converge y $L = 1$, **converge**.

---

## 📊 Resumen de criterios

| Criterio | Condición | Conclusión |
|----------|-----------|------------|
| n-ésimo término | $\lim a_n \neq 0$ | Diverge |
| Integral | $\int f$ converge | Serie converge |
| Comparación | $a_n < b_n$, $\sum b_n$ conv. | $\sum a_n$ conv. |
| Comparación límite | $\lim \frac{a_n}{b_n} = L$ finito | Mismo comportamiento |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Converge $\sum_{n=1}^{\infty} \frac{1}{n^3 + n}$?

<details>
<summary>Ver solución</summary>

$\frac{1}{n^3+n} < \frac{1}{n^3}$ y $\sum \frac{1}{n^3}$ converge (p = 3 > 1)

**Converge** por comparación.
</details>

---

**Ejercicio 2:** ¿Converge $\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^2}$?

<details>
<summary>Ver solución</summary>

$\int_2^{\infty} \frac{1}{x(\ln x)^2}\,dx = [-\frac{1}{\ln x}]_2^{\infty} = 0 + \frac{1}{\ln 2}$

**Converge** por el criterio de la integral.
</details>

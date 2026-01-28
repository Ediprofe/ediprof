---
title: "Criterios de Comparación"
---

# Criterios de Comparación

Los criterios de comparación determinan convergencia comparando con series conocidas.

---

## 🎯 ¿Qué vas a aprender?

- Comparación directa
- Comparación por límite
- Estrategias de uso
- Series de referencia

---

## 📖 Comparación directa

Si $0 \leq a_n \leq b_n$ para todo $n$ suficientemente grande:

- Si $\sum b_n$ converge → $\sum a_n$ converge
- Si $\sum a_n$ diverge → $\sum b_n$ diverge

---

## ⚙️ Ejemplo 1: Convergencia

$$
\sum \frac{1}{n^2 + 5}
$$

$\frac{1}{n^2+5} < \frac{1}{n^2}$ y $\sum \frac{1}{n^2}$ converge.

**Converge.**

---

## ⚙️ Ejemplo 2: Divergencia

$$
\sum \frac{1}{\sqrt{n} - 1}
$$

para $n \geq 2$

$\frac{1}{\sqrt{n}-1} > \frac{1}{\sqrt{n}}$ y $\sum \frac{1}{\sqrt{n}}$ diverge (p = 1/2).

**Diverge.**

---

## 📖 Comparación por límite

Si $a_n, b_n > 0$ y:

$$
\lim_{n \to \infty} \frac{a_n}{b_n} = L
$$

| Valor de L | Conclusión |
|------------|------------|
| $0 < L < \infty$ | Mismo comportamiento |
| $L = 0$ | $\sum b_n$ conv. → $\sum a_n$ conv. |
| $L = \infty$ | $\sum b_n$ div. → $\sum a_n$ div. |

---

## ⚙️ Ejemplo 3: Comparación límite

$$
\sum \frac{3n^2 + 2n}{n^4 + 1}
$$

Se comporta como $\frac{n^2}{n^4} = \frac{1}{n^2}$.

$$
\lim \frac{\frac{3n^2+2n}{n^4+1}}{\frac{1}{n^2}} = \lim \frac{3n^4 + 2n^3}{n^4+1} = 3
$$

Como $0 < 3 < \infty$ y $\sum \frac{1}{n^2}$ converge, **converge**.

---

## ⚙️ Ejemplo 4: Con logaritmo

$$
\sum \frac{\ln n}{n^2}
$$

$\ln n$ crece más lento que $\sqrt{n}$:

$$
\frac{\ln n}{n^2} < \frac{\sqrt{n}}{n^2} = \frac{1}{n^{3/2}}
$$

Como $\sum \frac{1}{n^{3/2}}$ converge (p = 3/2 > 1), **converge**.

---

## 📖 Series de referencia

| Serie | Comportamiento |
|-------|----------------|
| $\sum \frac{1}{n^p}$, $p > 1$ | Converge |
| $\sum \frac{1}{n^p}$, $p \leq 1$ | Diverge |
| $\sum r^n$, $\|r\| < 1$ | Converge |
| $\sum \frac{1}{n!}$ | Converge |

---

## ⚙️ Ejemplo 5: Factorial

$$
\sum \frac{n^{10}}{n!}
$$

Para $n$ grande: $\frac{n^{10}}{n!} < \frac{1}{2^n}$ (la factorial domina)

Como $\sum \frac{1}{2^n}$ converge, **converge**.

---

## 📖 Estrategia general

1. Identificar el término dominante (mayor potencia)
2. Comparar con serie p o geométrica apropiada
3. Usar comparación directa o por límite

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Converge $\sum \frac{n+5}{n^3-n}$?

<details>
<summary>Ver solución</summary>

Se comporta como $\frac{n}{n^3} = \frac{1}{n^2}$.

$$
\lim \frac{\frac{n+5}{n^3-n}}{\frac{1}{n^2}} = \lim \frac{n^3+5n^2}{n^3-n} = 1
$$

Como $\sum \frac{1}{n^2}$ converge, **converge**.
</details>

---

**Ejercicio 2:** ¿Converge $\sum \frac{1}{n - \ln n}$?

<details>
<summary>Ver solución</summary>

Para $n$ grande, $n - \ln n \approx n$.

$$
\lim \frac{1/(n-\ln n)}{1/n} = \lim \frac{n}{n-\ln n} = 1
$$

Como $\sum \frac{1}{n}$ diverge, **diverge**.
</details>

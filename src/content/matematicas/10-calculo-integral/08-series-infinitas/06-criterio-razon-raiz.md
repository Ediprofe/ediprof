# Criterios de la Razón y la Raíz

Los criterios de la razón y la raíz son especialmente útiles para series con factoriales o exponenciales.

---

## 🎯 ¿Qué vas a aprender?

- Criterio de la razón (D'Alembert)
- Criterio de la raíz (Cauchy)
- Cuándo usar cada uno
- Limitaciones

---

## 📖 Criterio de la razón

Sea $L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|$

| Valor de L | Conclusión |
|------------|------------|
| $L < 1$ | Converge absolutamente |
| $L > 1$ | Diverge |
| $L = 1$ | Inconcluso |

---

## ⚙️ Ejemplo 1: Factorial

$$
\sum \frac{n!}{n^n}
$$

$$
\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} = \frac{n^n}{(n+1)^n} = \left(\frac{n}{n+1}\right)^n
$$

$$
L = \lim \left(\frac{n}{n+1}\right)^n = \lim \left(1 - \frac{1}{n+1}\right)^n = \frac{1}{e} < 1
$$

**Converge.**

---

## ⚙️ Ejemplo 2: Exponencial sobre factorial

$$
\sum \frac{2^n}{n!}
$$

$$
\frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n} = \frac{2}{n+1}
$$

$$
L = \lim \frac{2}{n+1} = 0 < 1
$$

**Converge.**

---

## ⚙️ Ejemplo 3: Divergencia

$$
\sum \frac{3^n}{n^2}
$$

$$
\frac{a_{n+1}}{a_n} = \frac{3^{n+1}/(n+1)^2}{3^n/n^2} = 3 \cdot \frac{n^2}{(n+1)^2}
$$

$$
L = 3 \cdot 1 = 3 > 1
$$

**Diverge.**

---

## 📖 Criterio de la raíz

Sea $L = \lim_{n \to \infty} \sqrt[n]{|a_n|}$

| Valor de L | Conclusión |
|------------|------------|
| $L < 1$ | Converge absolutamente |
| $L > 1$ | Diverge |
| $L = 1$ | Inconcluso |

---

## ⚙️ Ejemplo 4: Usando raíz

$$
\sum \left(\frac{n}{2n+1}\right)^n
$$

$$
\sqrt[n]{a_n} = \frac{n}{2n+1}
$$

$$
L = \lim \frac{n}{2n+1} = \frac{1}{2} < 1
$$

**Converge.**

---

## ⚙️ Ejemplo 5: Exponente en n

$$
\sum \left(\frac{3n+1}{2n+5}\right)^n
$$

$$
\sqrt[n]{a_n} = \frac{3n+1}{2n+5}
$$

$$
L = \lim \frac{3n+1}{2n+5} = \frac{3}{2} > 1
$$

**Diverge.**

---

## 📖 Cuándo usar cada criterio

| Tipo de serie | Criterio preferido |
|---------------|-------------------|
| Factoriales | Razón |
| $a^n / n!$ | Razón |
| $(f(n))^n$ | Raíz |
| Potencias simples | Comparación |

---

## 📖 El caso L = 1

Cuando $L = 1$, el criterio falla. Ejemplos:

- $\sum \frac{1}{n}$: razón da $L = 1$, pero diverge
- $\sum \frac{1}{n^2}$: razón da $L = 1$, pero converge

Usar otro criterio (comparación, integral).

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Converge $\sum \frac{n^{100}}{2^n}$?

<details>
<summary>Ver solución</summary>

$$
\frac{a_{n+1}}{a_n} = \frac{(n+1)^{100}}{2^{n+1}} \cdot \frac{2^n}{n^{100}} = \frac{1}{2}\left(\frac{n+1}{n}\right)^{100}
$$

$$
L = \frac{1}{2} \cdot 1 = \frac{1}{2} < 1
$$

**Converge.**
</details>

---

**Ejercicio 2:** ¿Converge $\sum \left(\frac{n^2}{2n^2+1}\right)^n$?

<details>
<summary>Ver solución</summary>

$$
\sqrt[n]{a_n} = \frac{n^2}{2n^2+1} \to \frac{1}{2} < 1
$$

**Converge.**
</details>

# Definición de Serie de Potencias

Una serie de potencias es una serie infinita donde cada término es una potencia de $(x - c)$. Son la herramienta principal para representar funciones como series.

---

## 🎯 ¿Qué vas a aprender?

- Definición de serie de potencias
- Radio de convergencia
- Intervalo de convergencia
- Ejemplos fundamentales

---

## 📖 Definición

Una **serie de potencias** centrada en $c$ tiene la forma:

$$
\sum_{n=0}^{\infty} a_n(x-c)^n = a_0 + a_1(x-c) + a_2(x-c)^2 + ...
$$

Si $c = 0$:

$$
\sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + ...
$$

---

## 📖 Radio de convergencia

Toda serie de potencias tiene un **radio de convergencia** $R$ tal que:

- Converge absolutamente para $|x - c| < R$
- Diverge para $|x - c| > R$
- En $|x - c| = R$: hay que verificar

**Casos especiales:** $R = 0$ (solo converge en $c$), $R = \infty$ (converge para todo $x$)

---

## 📖 Cálculo de R usando razón

$$
R = \lim_{n \to \infty} \left|\frac{a_n}{a_{n+1}}\right|
$$

o equivalentemente:

$$
\frac{1}{R} = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|
$$

---

## ⚙️ Ejemplo 1: Radio de convergencia

$$
\sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

$$
\frac{1}{R} = \lim \left|\frac{1/(n+1)!}{1/n!}\right| = \lim \frac{1}{n+1} = 0
$$

$R = \infty$ (converge para todo $x$)

Esta es la serie de $e^x$.

---

## ⚙️ Ejemplo 2: Radio finito

$$
\sum_{n=0}^{\infty} n! x^n
$$

$$
\frac{1}{R} = \lim \left|\frac{(n+1)!}{n!}\right| = \lim (n+1) = \infty
$$

$R = 0$ (solo converge en $x = 0$)

---

## ⚙️ Ejemplo 3: Serie geométrica

$$
\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}
$$

$R = 1$ (todos los coeficientes son 1)

Converge para $|x| < 1$, diverge para $|x| > 1$.

En $x = 1$: $\sum 1$ diverge. En $x = -1$: $\sum (-1)^n$ diverge.

**Intervalo de convergencia:** $(-1, 1)$

---

## ⚙️ Ejemplo 4: Verificar extremos

$$
\sum_{n=1}^{\infty} \frac{x^n}{n}
$$

$R = 1$ (coeficientes $1/n$)

En $x = 1$: $\sum \frac{1}{n}$ diverge (armónica)
En $x = -1$: $\sum \frac{(-1)^n}{n}$ converge (alternante)

**Intervalo:** $[-1, 1)$

---

## 📖 Intervalo de convergencia

El intervalo de convergencia es $(c - R, c + R)$ posiblemente incluyendo uno o ambos extremos.

**Siempre verificar los extremos por separado.**

---

## 📊 Resumen

| Elemento | Descripción |
|----------|-------------|
| Serie de potencias | $\sum a_n(x-c)^n$ |
| Radio $R$ | Distancia de convergencia desde $c$ |
| Interior | Convergencia absoluta |
| Exterior | Divergencia |
| Extremos | Verificar cada uno |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra R e intervalo para $\sum_{n=1}^{\infty} \frac{x^n}{n^2}$

<details>
<summary>Ver solución</summary>

$R = 1$ (coef. $1/n^2$)

En $x = 1$: $\sum \frac{1}{n^2}$ converge
En $x = -1$: $\sum \frac{(-1)^n}{n^2}$ converge absolutamente

Intervalo: $[-1, 1]$
</details>

---

**Ejercicio 2:** Encuentra R para $\sum_{n=0}^{\infty} \frac{n! x^n}{n^n}$

<details>
<summary>Ver solución</summary>

$$
\frac{a_{n+1}}{a_n} = \frac{(n+1)!/(n+1)^{n+1}}{n!/n^n} = \frac{n^n}{(n+1)^n} \to \frac{1}{e}
$$

$R = e$
</details>

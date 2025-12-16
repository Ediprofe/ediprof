# Aplicaciones de Series de Potencias

Las series de potencias tienen numerosas aplicaciones: resolver ecuaciones diferenciales, calcular integrales difíciles y aproximar valores.

---

## 🎯 ¿Qué vas a aprender?

- Cálculo de integrales difíciles
- Resolución de ecuaciones diferenciales
- Aproximaciones numéricas
- La identidad de Euler

---

## 📖 Integrales mediante series

Algunas integrales no tienen forma cerrada pero se pueden expresar como series.

---

## ⚙️ Ejemplo 1: Integral de error

$$\int e^{-x^2}\,dx$$

$$e^{-x^2} = \sum_{n=0}^{\infty} \frac{(-x^2)^n}{n!} = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{n!}$$

$$\int e^{-x^2}\,dx = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)n!} + C$$

$$= x - \frac{x^3}{3} + \frac{x^5}{10} - \frac{x^7}{42} + ...$$

---

## ⚙️ Ejemplo 2: Integral de seno

$$\int \frac{\sin x}{x}\,dx$$

$$\frac{\sin x}{x} = \frac{1}{x}\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n+1)!}$$

$$\int = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)(2n+1)!} + C$$

---

## 📖 Ecuaciones diferenciales

Muchas ED se resuelven suponiendo solución en serie.

---

## ⚙️ Ejemplo 3: ED simple

$y' = y$, $y(0) = 1$

Supongamos $y = \sum a_n x^n$

$y' = \sum n a_n x^{n-1}$

De $y' = y$: $\sum n a_n x^{n-1} = \sum a_n x^n$

Comparando coeficientes: $a_{n+1} = \frac{a_n}{n+1}$

Con $a_0 = y(0) = 1$: $a_n = \frac{1}{n!}$

$$y = \sum \frac{x^n}{n!} = e^x$$

---

## 📖 Aproximación numérica

Los polinomios de Taylor aproximan funciones cerca del punto de expansión.

---

## ⚙️ Ejemplo 4: Calcular $e$

$$e = e^1 = \sum_{n=0}^{\infty} \frac{1}{n!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + ...$$

Con 10 términos:
$$e \approx 1 + 1 + 0.5 + 0.1667 + 0.0417 + 0.0083 + 0.0014 + ...$$
$$\approx 2.7183$$

---

## 📖 Identidad de Euler

La conexión entre exponencial y funciones trigonométricas:

$$e^{ix} = \cos x + i\sin x$$

Con $x = \pi$:

$$\boxed{e^{i\pi} + 1 = 0}$$

"La ecuación más bella de las matemáticas."

---

## ⚙️ Ejemplo 5: Suma de serie

Calcula $\sum_{n=1}^{\infty} \frac{1}{n \cdot 2^n}$

Sabemos que $\ln(1-x) = -\sum_{n=1}^{\infty} \frac{x^n}{n}$

Con $x = \frac{1}{2}$:

$$\ln\frac{1}{2} = -\sum_{n=1}^{\infty} \frac{1}{n \cdot 2^n}$$

$$\sum_{n=1}^{\infty} \frac{1}{n \cdot 2^n} = \ln 2 \approx 0.693$$

---

## 📊 Resumen de aplicaciones

| Aplicación | Método |
|------------|--------|
| Integrales sin forma cerrada | Integrar término a término |
| ED con coef. variables | Método de series de potencias |
| Cálculos numéricos | Truncar serie en $n$ términos |
| Límites difíciles | Expandir numerador y denominador |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Expresa $\int_0^{1} e^{-x^2}\,dx$ como serie y estima con 3 términos.

<details>
<summary>Ver solución</summary>

$\int_0^1 e^{-x^2}\,dx = \left[x - \frac{x^3}{3} + \frac{x^5}{10} - ...\right]_0^1$

$\approx 1 - \frac{1}{3} + \frac{1}{10} \approx 0.767$

(Valor real: $\approx 0.746$)
</details>

---

**Ejercicio 2:** Usa series para resolver $y'' + y = 0$, $y(0) = 1$, $y'(0) = 0$.

<details>
<summary>Ver solución</summary>

$y = \sum a_n x^n$, $y'' = \sum n(n-1)a_n x^{n-2}$

De $y'' + y = 0$: $a_{n+2} = -\frac{a_n}{(n+2)(n+1)}$

$a_0 = 1$, $a_1 = 0$

$a_2 = -\frac{1}{2}$, $a_4 = \frac{1}{24}$, ...

$y = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - ... = \cos x$
</details>

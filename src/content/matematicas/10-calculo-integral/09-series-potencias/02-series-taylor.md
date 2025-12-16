# Series de Taylor

Las series de Taylor representan funciones como sumas infinitas de potencias, permitiendo aproximaciones y cálculos.

---

## 🎯 ¿Qué vas a aprender?

- Construcción de la serie de Taylor
- Condiciones de existencia
- Series de funciones comunes
- Aplicaciones

---

## 📖 Serie de Taylor

La **serie de Taylor** de $f(x)$ centrada en $x = a$ es:

$$\boxed{f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n}$$

$$= f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + ...$$

---

## 📖 Serie de Maclaurin

Si $a = 0$, se llama **serie de Maclaurin**:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

---

## ⚙️ Ejemplo 1: Exponencial

$f(x) = e^x$, $f^{(n)}(x) = e^x$, $f^{(n)}(0) = 1$

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ...$$

Válida para todo $x \in \mathbb{R}$.

---

## ⚙️ Ejemplo 2: Seno

$f(x) = \sin x$

$f(0) = 0$, $f'(0) = 1$, $f''(0) = 0$, $f'''(0) = -1$, ...

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...$$

$$= \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$$

---

## ⚙️ Ejemplo 3: Coseno

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + ...$$

$$= \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$

Nota: $(\sin x)' = \cos x$ y $(\cos x)' = -\sin x$ ✓

---

## ⚙️ Ejemplo 4: Logaritmo

$f(x) = \ln(1 + x)$

$f(0) = 0$, $f^{(n)}(x) = (-1)^{n+1}(n-1)!/x^n$

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + ...$$

$$= \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}$$

Converge para $-1 < x \leq 1$.

---

## 📖 Series importantes

| Función | Serie de Maclaurin | Intervalo |
|---------|-------------------|-----------|
| $e^x$ | $\sum \frac{x^n}{n!}$ | $(-\infty, \infty)$ |
| $\sin x$ | $\sum \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $(-\infty, \infty)$ |
| $\cos x$ | $\sum \frac{(-1)^n x^{2n}}{(2n)!}$ | $(-\infty, \infty)$ |
| $\frac{1}{1-x}$ | $\sum x^n$ | $(-1, 1)$ |
| $\ln(1+x)$ | $\sum \frac{(-1)^{n+1}x^n}{n}$ | $(-1, 1]$ |

---

## ⚙️ Ejemplo 5: Usando serie conocida

Encuentra la serie de $e^{-x^2}$:

$$e^u = \sum \frac{u^n}{n!}$$ con $u = -x^2$:

$$e^{-x^2} = \sum_{n=0}^{\infty} \frac{(-x^2)^n}{n!} = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{n!}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra los primeros 4 términos de la serie de Taylor de $f(x) = \sqrt{1+x}$ en $a = 0$.

<details>
<summary>Ver solución</summary>

$f(0) = 1$, $f'(0) = \frac{1}{2}$, $f''(0) = -\frac{1}{4}$, $f'''(0) = \frac{3}{8}$

$\sqrt{1+x} \approx 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - ...$
</details>

---

**Ejercicio 2:** Usa series para encontrar $\sum_{n=0}^{\infty} \frac{1}{n!}$

<details>
<summary>Ver solución</summary>

$e^x = \sum \frac{x^n}{n!}$

En $x = 1$: $e^1 = \sum \frac{1}{n!}$

La suma es $e \approx 2.718$
</details>

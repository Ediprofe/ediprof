# Series Alternantes

Las series alternantes tienen términos que alternan entre positivos y negativos. Tienen propiedades especiales de convergencia.

---

## 🎯 ¿Qué vas a aprender?

- Definición de serie alternante
- Criterio de Leibniz
- Estimación del error
- Ejemplos importantes

---

## 📖 Definición

Una **serie alternante** tiene la forma:

$$\sum_{n=1}^{\infty} (-1)^{n+1} b_n = b_1 - b_2 + b_3 - b_4 + ...$$

o

$$\sum_{n=1}^{\infty} (-1)^n b_n = -b_1 + b_2 - b_3 + b_4 - ...$$

donde $b_n > 0$.

---

## 📖 Criterio de Leibniz (series alternantes)

La serie alternante $\sum (-1)^{n+1} b_n$ converge si:

1. $b_{n+1} \leq b_n$ (decreciente)
2. $\lim_{n \to \infty} b_n = 0$

---

## ⚙️ Ejemplo 1: Serie armónica alternante

$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + ...$$

$b_n = \frac{1}{n}$: decreciente ✓ y $\lim = 0$ ✓

**Converge** (a $\ln 2$).

Nota: La serie armónica normal $\sum \frac{1}{n}$ diverge, pero la alternante converge.

---

## ⚙️ Ejemplo 2: Otra alternante

$$\sum_{n=1}^{\infty} \frac{(-1)^n n}{n^2+1}$$

$b_n = \frac{n}{n^2+1} \to 0$ ✓

¿Es decreciente? $b'(n) < 0$ para $n$ grande ✓

**Converge.**

---

## 📖 Estimación del error

Si $S = \sum (-1)^{n+1} b_n$ y $S_n$ es la suma parcial:

$$|S - S_n| \leq b_{n+1}$$

El error está acotado por el primer término omitido.

---

## ⚙️ Ejemplo 3: Error de aproximación

Para $\ln 2 = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$:

Con 10 términos: $|S - S_{10}| \leq \frac{1}{11} \approx 0.091$

Con 100 términos: $|S - S_{100}| \leq \frac{1}{101} \approx 0.0099$

---

## ⚙️ Ejemplo 4: Convergencia condicional

$$\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt{n}}$$

Alternante con $b_n = \frac{1}{\sqrt{n}} \to 0$ ✓

**Converge** por Leibniz.

Pero $\sum \frac{1}{\sqrt{n}}$ diverge (p = 1/2 < 1).

Esta serie converge **condicionalmente** (no absolutamente).

---

## ⚙️ Ejemplo 5: Fallo del criterio

$$\sum (-1)^n \frac{n}{n+1}$$

$b_n = \frac{n}{n+1} \to 1 \neq 0$

El criterio de Leibniz no aplica, y de hecho la serie **diverge** (criterio del término n-ésimo).

---

## 📖 Convergencia absoluta vs. condicional

- **Absoluta:** $\sum |a_n|$ converge
- **Condicional:** $\sum a_n$ converge pero $\sum |a_n|$ diverge

Convergencia absoluta → Convergencia (pero no al revés)

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Converge $\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}$?

<details>
<summary>Ver solución</summary>

$b_n = \frac{1}{n^2}$: decreciente ✓ y $\to 0$ ✓

**Converge** por Leibniz.

Además, $\sum \frac{1}{n^2}$ converge, así que converge **absolutamente**.
</details>

---

**Ejercicio 2:** ¿Cuántos términos de $\sum \frac{(-1)^{n+1}}{n!}$ se necesitan para error < 0.001?

<details>
<summary>Ver solución</summary>

$b_{n+1} = \frac{1}{(n+1)!} < 0.001$

$(n+1)! > 1000$

$7! = 5040 > 1000$, así que $n = 6$ términos bastan.
</details>

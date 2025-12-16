# Serie Geométrica

La serie geométrica es una de las pocas series cuya suma se puede calcular exactamente. Es fundamental en matemáticas y aplicaciones.

---

## 🎯 ¿Qué vas a aprender?

- Fórmula de la serie geométrica
- Condición de convergencia
- Aplicaciones
- Variantes

---

## 📖 La serie geométrica

$$\boxed{\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ar^3 + ... = \frac{a}{1-r} \quad (|r| < 1)}$$

- $a$ = primer término
- $r$ = razón común

---

## 📖 Derivación

$$S_n = a + ar + ar^2 + ... + ar^{n-1}$$

$$rS_n = ar + ar^2 + ... + ar^n$$

$$S_n - rS_n = a - ar^n$$

$$S_n = \frac{a(1-r^n)}{1-r}$$

Si $|r| < 1$: $\lim r^n = 0$, así $S = \frac{a}{1-r}$

---

## ⚙️ Ejemplo 1: Serie básica

$$\sum_{n=0}^{\infty} \left(\frac{1}{3}\right)^n = \frac{1}{1 - 1/3} = \frac{3}{2}$$

---

## ⚙️ Ejemplo 2: Con primer término

$$\sum_{n=0}^{\infty} 5 \cdot \left(\frac{2}{5}\right)^n = \frac{5}{1 - 2/5} = \frac{5}{3/5} = \frac{25}{3}$$

---

## ⚙️ Ejemplo 3: Empezando en n=1

$$\sum_{n=1}^{\infty} 2 \cdot \left(\frac{1}{2}\right)^n = \sum_{n=1}^{\infty} \frac{1}{2^{n-1}}$$

$$= 2 \cdot \frac{1/2}{1 - 1/2} = 2 \cdot 1 = 2$$

O: $\sum_{n=1}^{\infty} = \sum_{n=0}^{\infty} - \text{(término n=0)}$

---

## ⚙️ Ejemplo 4: Razón negativa

$$\sum_{n=0}^{\infty} (-1)^n \cdot \frac{1}{2^n} = \sum_{n=0}^{\infty} \left(-\frac{1}{2}\right)^n = \frac{1}{1-(-1/2)} = \frac{2}{3}$$

---

## 📖 Decimal periódico como serie

$$0.333... = \frac{3}{10} + \frac{3}{100} + \frac{3}{1000} + ...$$

$$= \sum_{n=1}^{\infty} \frac{3}{10^n} = 3 \cdot \frac{1/10}{1 - 1/10} = 3 \cdot \frac{1}{9} = \frac{1}{3}$$

---

## ⚙️ Ejemplo 5: Otro decimal

$$0.272727... = \frac{27}{100} + \frac{27}{10000} + ...$$

$$= \sum_{n=1}^{\infty} \frac{27}{100^n} = 27 \cdot \frac{1/100}{1 - 1/100} = \frac{27}{99} = \frac{3}{11}$$

---

## 📖 Divergencia

Si $|r| \geq 1$, la serie diverge:

- $|r| > 1$: los términos crecen sin límite
- $r = 1$: $S_n = a + a + a + ... = na \to \infty$
- $r = -1$: $S_n$ oscila entre $a$ y $0$

---

## ⚙️ Ejemplo 6: Serie divergente

$$\sum_{n=0}^{\infty} 2^n = 1 + 2 + 4 + 8 + ... = \infty$$

$r = 2 > 1$, diverge.

---

## 📊 Resumen

| Condición | Convergencia | Suma |
|-----------|-------------|------|
| $\|r\| < 1$ | Converge | $\frac{a}{1-r}$ |
| $\|r\| \geq 1$ | Diverge | - |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

$$\sum_{n=2}^{\infty} \left(\frac{3}{4}\right)^n$$

<details>
<summary>Ver solución</summary>

$= \left(\frac{3}{4}\right)^2 + \left(\frac{3}{4}\right)^3 + ...$

$= \frac{(3/4)^2}{1 - 3/4} = \frac{9/16}{1/4} = \frac{9}{4}$
</details>

---

**Ejercicio 2:** Expresa $0.123123123...$ como fracción.

<details>
<summary>Ver solución</summary>

$= \frac{123}{1000} + \frac{123}{1000000} + ...$

$= \frac{123}{1000} \cdot \frac{1}{1 - 1/1000} = \frac{123}{999} = \frac{41}{333}$
</details>

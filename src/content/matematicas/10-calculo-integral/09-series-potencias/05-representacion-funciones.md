# Representación de Funciones como Series

Diferentes funciones se pueden representar como series de potencias, lo que permite manipularlas algebraicamente.

---

## 🎯 ¿Qué vas a aprender?

- Generar nuevas series a partir de conocidas
- Operaciones con series
- Series binomiales
- Funciones especiales

---

## 📖 Series de referencia

$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n, \quad |x| < 1$$

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$

$$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}x^n}{n}, \quad -1 < x \leq 1$$

---

## 📖 Técnicas de generación

1. **Sustitución:** reemplazar $x$ por una expresión
2. **Derivación:** derivar término a término
3. **Integración:** integrar término a término
4. **Multiplicación:** multiplicar series
5. **División:** dividir series (más complejo)

---

## ⚙️ Ejemplo 1: Sustitución

Encontrar la serie de $\frac{1}{1+x^2}$:

$$\frac{1}{1-u} = \sum u^n \text{ con } u = -x^2$$

$$\frac{1}{1+x^2} = \sum_{n=0}^{\infty} (-x^2)^n = 1 - x^2 + x^4 - x^6 + ...$$

---

## ⚙️ Ejemplo 2: Derivación

De $\frac{1}{1-x} = \sum x^n$:

$$\frac{d}{dx}\left[\frac{1}{1-x}\right] = \frac{1}{(1-x)^2} = \sum_{n=1}^{\infty} nx^{n-1}$$

O equivalentemente: $\frac{1}{(1-x)^2} = \sum_{n=0}^{\infty} (n+1)x^n$

---

## ⚙️ Ejemplo 3: Integración

De $\frac{1}{1+x} = \sum_{n=0}^{\infty} (-1)^n x^n$:

$$\int \frac{dx}{1+x} = \ln(1+x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{n+1}}{n+1} + C$$

Con $C = 0$ (evaluando en $x = 0$):

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - ...$$

---

## 📖 Serie binomial

$$(1+x)^k = \sum_{n=0}^{\infty} \binom{k}{n} x^n$$

donde $\binom{k}{n} = \frac{k(k-1)(k-2)...(k-n+1)}{n!}$

Válida para $|x| < 1$ si $k$ no es entero no negativo.

---

## ⚙️ Ejemplo 4: Raíz cuadrada

$$\sqrt{1+x} = (1+x)^{1/2}$$

$$= 1 + \frac{1}{2}x + \frac{\frac{1}{2}(-\frac{1}{2})}{2!}x^2 + \frac{\frac{1}{2}(-\frac{1}{2})(-\frac{3}{2})}{3!}x^3 + ...$$

$$= 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - ...$$

---

## ⚙️ Ejemplo 5: Arco tangente

De $\frac{1}{1+x^2} = 1 - x^2 + x^4 - ...$:

$$\arctan x = \int \frac{dx}{1+x^2} = x - \frac{x^3}{3} + \frac{x^5}{5} - ...$$

Con $x = 1$:

$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + ...$$

(Serie de Leibniz para $\pi$)

---

## ⚙️ Ejemplo 6: Combinación

La serie de $\frac{x}{(1-x)^2}$:

De $\frac{1}{(1-x)^2} = \sum (n+1)x^n$:

$$\frac{x}{(1-x)^2} = \sum_{n=0}^{\infty} (n+1)x^{n+1} = \sum_{n=1}^{\infty} nx^n$$

---

## 📊 Operaciones resumen

| Operación | Resultado |
|-----------|-----------|
| $f(-x)$ | Alternar signos |
| $f(x^2)$ | Solo potencias pares |
| $xf(x)$ | Sumar 1 a cada exponente |
| $f'(x)$ | $n a_n x^{n-1}$ |
| $\int f$ | $\frac{a_n}{n+1}x^{n+1}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la serie de $\frac{x}{1-x^2}$.

<details>
<summary>Ver solución</summary>

$\frac{1}{1-x^2} = \sum (x^2)^n = \sum x^{2n}$

$\frac{x}{1-x^2} = \sum x^{2n+1} = x + x^3 + x^5 + ...$
</details>

---

**Ejercicio 2:** Encuentra la serie de $\frac{1}{\sqrt{1-x}}$.

<details>
<summary>Ver solución</summary>

$(1-x)^{-1/2} = 1 + \frac{1}{2}x + \frac{3}{8}x^2 + \frac{5}{16}x^3 + ...$

$= \sum_{n=0}^{\infty} \binom{-1/2}{n}(-x)^n$
</details>

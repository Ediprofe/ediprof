# Derivadas de Orden Superior

La derivada de una derivada es una derivada de segundo orden. Se puede continuar derivando indefinidamente, obteniendo derivadas de cualquier orden.

---

## 🎯 ¿Qué vas a aprender?

- Notación para derivadas de orden superior
- Cálculo de segundas y terceras derivadas
- Interpretación física (aceleración)
- Patrones en derivadas repetidas

---

## 📖 Definición

Si $f'(x)$ es la primera derivada de $f$, entonces:

- **Segunda derivada:** $f''(x) = (f'(x))'$
- **Tercera derivada:** $f'''(x) = (f''(x))'$
- **n-ésima derivada:** $f^{(n)}(x)$

---

## 📖 Notaciones

| Orden | Notación de Lagrange | Notación de Leibniz |
|-------|---------------------|---------------------|
| 1 | $f'(x)$ | $\frac{dy}{dx}$ |
| 2 | $f''(x)$ | $\frac{d^2y}{dx^2}$ |
| 3 | $f'''(x)$ | $\frac{d^3y}{dx^3}$ |
| n | $f^{(n)}(x)$ | $\frac{d^ny}{dx^n}$ |

---

## ⚙️ Ejemplo 1: Polinomio

$f(x) = x^4 - 3x^3 + 2x^2 - x + 5$

$$f'(x) = 4x^3 - 9x^2 + 4x - 1$$

$$f''(x) = 12x^2 - 18x + 4$$

$$f'''(x) = 24x - 18$$

$$f^{(4)}(x) = 24$$

$$f^{(5)}(x) = 0$$

A partir de la quinta derivada, todas son cero.

---

## 📖 Regla para polinomios

Para $f(x) = x^n$:
- $f^{(k)}(x) = n(n-1)(n-2)\cdots(n-k+1)x^{n-k}$ para $k \leq n$
- $f^{(k)}(x) = 0$ para $k > n$

En particular: $f^{(n)}(x) = n!$

---

## ⚙️ Ejemplo 2: Función exponencial

$f(x) = e^x$

$$f'(x) = e^x$$
$$f''(x) = e^x$$
$$f^{(n)}(x) = e^x$$ para todo $n$

La exponencial es su propia derivada de cualquier orden.

---

## ⚙️ Ejemplo 3: Función seno

$f(x) = \sin x$

$$f'(x) = \cos x$$
$$f''(x) = -\sin x$$
$$f'''(x) = -\cos x$$
$$f^{(4)}(x) = \sin x$$

El ciclo se repite cada 4 derivadas.

**Patrón:**

$$
f^{(n)}(x) = \sin\left(x + \frac{n\pi}{2}\right)
$$

---

## ⚙️ Ejemplo 4: Función coseno

$g(x) = \cos x$

$$g'(x) = -\sin x$$
$$g''(x) = -\cos x$$
$$g'''(x) = \sin x$$
$$g^{(4)}(x) = \cos x$$

---

## 📖 Interpretación física

Si $s(t)$ es la posición de un objeto:

| Derivada | Significado |
|----------|-------------|
| $s(t)$ | Posición |
| $s'(t) = v(t)$ | Velocidad |
| $s''(t) = a(t)$ | Aceleración |
| $s'''(t)$ | Tirón (jerk) |

---

## ⚙️ Ejemplo 5: Movimiento

La posición de una partícula es $s(t) = t^3 - 6t^2 + 9t$

**Velocidad:**
$$v(t) = s'(t) = 3t^2 - 12t + 9$$

**Aceleración:**
$$a(t) = s''(t) = 6t - 12$$

**¿Cuándo la aceleración es cero?**
$$6t - 12 = 0 \Rightarrow t = 2$$

---

## ⚙️ Ejemplo 6: Con regla de la cadena

$f(x) = (2x + 1)^5$

$$f'(x) = 5(2x + 1)^4 \cdot 2 = 10(2x + 1)^4$$

$$f''(x) = 10 \cdot 4(2x + 1)^3 \cdot 2 = 80(2x + 1)^3$$

$$f'''(x) = 80 \cdot 3(2x + 1)^2 \cdot 2 = 480(2x + 1)^2$$

---

## ⚙️ Ejemplo 7: Producto

$f(x) = x^2 e^x$

$$f'(x) = 2xe^x + x^2e^x = e^x(2x + x^2)$$

$$f''(x) = e^x(2x + x^2) + e^x(2 + 2x)$$
$$= e^x(x^2 + 4x + 2)$$

---

## 📊 Patrones útiles

| Función | n-ésima derivada |
|---------|------------------|
| $x^n$ | $\frac{n!}{(n-k)!}x^{n-k}$ (k ≤ n) |
| $e^{ax}$ | $a^n e^{ax}$ |
| $\sin(ax)$ | $a^n\sin(ax + \frac{n\pi}{2})$ |
| $\ln x$ | $(-1)^{n-1}\frac{(n-1)!}{x^n}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra $f''(x)$:

a) $f(x) = x^5 - 2x^3 + x$
b) $f(x) = e^{2x}$

<details>
<summary>Ver soluciones</summary>

a) $f'(x) = 5x^4 - 6x^2 + 1$
   
   $f''(x) = 20x^3 - 12x$

b) $f'(x) = 2e^{2x}$
   
   $f''(x) = 4e^{2x}$
</details>

---

**Ejercicio 2:** Si $s(t) = t^4 - 4t^3$, encuentra la aceleración cuando $t = 2$.

<details>
<summary>Ver solución</summary>

$s'(t) = 4t^3 - 12t^2$

$s''(t) = 12t^2 - 24t$

$s''(2) = 48 - 48 = 0$
</details>

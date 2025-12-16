# Notación Sigma y Propiedades de Sumas

La notación sigma es esencial para expresar sumas de Riemann y otras expresiones con muchos términos de forma compacta.

---

## 🎯 ¿Qué vas a aprender?

- La notación sigma ($\sum$)
- Propiedades de las sumas
- Fórmulas de sumas especiales
- Aplicación en límites

---

## 📖 Notación sigma

$$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + a_{m+2} + ... + a_n$$

- $i$ = índice (variable muda)
- $m$ = límite inferior
- $n$ = límite superior
- $a_i$ = término general

---

## ⚙️ Ejemplo 1: Expansión

$$\sum_{i=1}^{4} i^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30$$

$$\sum_{k=0}^{3} 2^k = 2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15$$

---

## 📖 Propiedades de sumas

### 1. Constante multiplicativa

$$\sum_{i=1}^{n} c \cdot a_i = c \sum_{i=1}^{n} a_i$$

### 2. Suma de sumas

$$\sum_{i=1}^{n} (a_i + b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i$$

### 3. Suma de constante

$$\sum_{i=1}^{n} c = n \cdot c$$

---

## 📖 Fórmulas fundamentales

$$\sum_{i=1}^{n} 1 = n$$

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{i=1}^{n} i^3 = \left[\frac{n(n+1)}{2}\right]^2$$

---

## ⚙️ Ejemplo 2: Usar fórmulas

$$\sum_{i=1}^{100} i = \frac{100(101)}{2} = 5050$$

$$\sum_{i=1}^{10} i^2 = \frac{10(11)(21)}{6} = \frac{2310}{6} = 385$$

---

## ⚙️ Ejemplo 3: Combinación

$$\sum_{i=1}^{n} (3i^2 + 2i - 5)$$

$$= 3\sum_{i=1}^{n} i^2 + 2\sum_{i=1}^{n} i - \sum_{i=1}^{n} 5$$

$$= 3 \cdot \frac{n(n+1)(2n+1)}{6} + 2 \cdot \frac{n(n+1)}{2} - 5n$$

$$= \frac{n(n+1)(2n+1)}{2} + n(n+1) - 5n$$

---

## 📖 Aplicación: Sumas de Riemann

Para $\int_0^1 x^2\,dx$ con suma derecha:

$$R_n = \sum_{i=1}^{n} \left(\frac{i}{n}\right)^2 \cdot \frac{1}{n} = \frac{1}{n^3}\sum_{i=1}^{n} i^2$$

$$= \frac{1}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6n^2}$$

$$\lim_{n \to \infty} R_n = \lim_{n \to \infty} \frac{2n^2 + 3n + 1}{6n^2} = \frac{2}{6} = \frac{1}{3}$$

Verificación: $\int_0^1 x^2\,dx = \frac{1}{3}$ ✓

---

## ⚙️ Ejemplo 4: Otra suma de Riemann

Calcula $\int_0^2 x^3\,dx$ por límite.

$\Delta x = \frac{2}{n}$, $x_i = \frac{2i}{n}$

$$R_n = \sum_{i=1}^{n} \left(\frac{2i}{n}\right)^3 \cdot \frac{2}{n} = \frac{16}{n^4}\sum_{i=1}^{n} i^3$$

$$= \frac{16}{n^4} \cdot \left[\frac{n(n+1)}{2}\right]^2 = \frac{16n^2(n+1)^2}{4n^4} = \frac{4(n+1)^2}{n^2}$$

$$\lim_{n \to \infty} \frac{4(n+1)^2}{n^2} = 4$$

Verificación: $\int_0^2 x^3\,dx = \frac{x^4}{4}\Big|_0^2 = 4$ ✓

---

## 📖 Serie geométrica

$$\sum_{i=0}^{n-1} r^i = \frac{1 - r^n}{1 - r} \quad (r \neq 1)$$

Para $|r| < 1$ y $n \to \infty$:
$$\sum_{i=0}^{\infty} r^i = \frac{1}{1-r}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\sum_{i=1}^{50} i$
b) $\sum_{k=1}^{5} k^3$

<details>
<summary>Ver soluciones</summary>

a) $\frac{50(51)}{2} = 1275$

b) $\left[\frac{5(6)}{2}\right]^2 = 15^2 = 225$
</details>

---

**Ejercicio 2:** Usa límite de suma de Riemann para calcular $\int_0^1 (2x + 1)\,dx$.

<details>
<summary>Ver solución</summary>

$R_n = \sum_{i=1}^{n}\left(\frac{2i}{n} + 1\right)\frac{1}{n} = \frac{2}{n^2}\sum i + \frac{1}{n}\sum 1$

$= \frac{2}{n^2} \cdot \frac{n(n+1)}{2} + 1 = \frac{n+1}{n} + 1$

$\lim = 1 + 1 = 2$

Verificación: $\int_0^1(2x+1)\,dx = x^2 + x\Big|_0^1 = 2$ ✓
</details>

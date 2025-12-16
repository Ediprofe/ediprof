# Límite de una Sucesión

El límite de una sucesión describe el comportamiento de sus términos cuando n crece hacia infinito.

---

## 🎯 ¿Qué vas a aprender?

- Definición de convergencia
- Propiedades de límites de sucesiones
- Técnicas de cálculo
- Sucesiones divergentes

---

## 📖 Definición

Una sucesión $\{a_n\}$ **converge** a $L$ si:

$$\lim_{n \to \infty} a_n = L$$

significa que para todo $\varepsilon > 0$, existe $N$ tal que $|a_n - L| < \varepsilon$ siempre que $n > N$.

Si el límite no existe o es infinito, la sucesión **diverge**.

---

## ⚙️ Ejemplo 1: Sucesión convergente

$$a_n = \frac{n}{n+1}$$

$$\lim_{n \to \infty} \frac{n}{n+1} = \lim_{n \to \infty} \frac{1}{1 + 1/n} = 1$$

---

## ⚙️ Ejemplo 2: Sucesión divergente

$$a_n = n^2$$

$$\lim_{n \to \infty} n^2 = \infty$$

Diverge (a infinito).

---

## 📖 Propiedades de límites

Si $\lim a_n = L$ y $\lim b_n = M$:

| Propiedad | Fórmula |
|-----------|---------|
| Suma | $\lim(a_n + b_n) = L + M$ |
| Producto | $\lim(a_n \cdot b_n) = L \cdot M$ |
| Cociente | $\lim\frac{a_n}{b_n} = \frac{L}{M}$ (si $M \neq 0$) |
| Potencia | $\lim a_n^k = L^k$ |

---

## 📖 Límites importantes

$$\lim_{n \to \infty} \frac{1}{n^p} = 0 \quad (p > 0)$$

$$\lim_{n \to \infty} r^n = 0 \quad (|r| < 1)$$

$$\lim_{n \to \infty} \sqrt[n]{n} = 1$$

$$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$$

$$\lim_{n \to \infty} \frac{x^n}{n!} = 0 \quad \text{(para todo } x)$$

---

## ⚙️ Ejemplo 3: Forma indeterminada

$$\lim_{n \to \infty} \frac{3n^2 + 2n}{n^2 - 5}$$

Dividir por $n^2$:

$$= \lim_{n \to \infty} \frac{3 + 2/n}{1 - 5/n^2} = \frac{3 + 0}{1 - 0} = 3$$

---

## ⚙️ Ejemplo 4: Exponencial vs polinomio

$$\lim_{n \to \infty} \frac{n^{100}}{2^n}$$

La exponencial crece más rápido que cualquier polinomio.

Aplicando L'Hôpital (o el criterio de razón): = 0

---

## ⚙️ Ejemplo 5: Raíz n-ésima

$$\lim_{n \to \infty} \sqrt[n]{2}$$

$$= \lim_{n \to \infty} 2^{1/n} = 2^0 = 1$$

---

## 📖 Teorema del sándwich

Si $a_n \leq b_n \leq c_n$ y $\lim a_n = \lim c_n = L$, entonces $\lim b_n = L$.

---

## ⚙️ Ejemplo 6: Sándwich

$$\lim_{n \to \infty} \frac{\sin n}{n}$$

Como $-1 \leq \sin n \leq 1$:

$$-\frac{1}{n} \leq \frac{\sin n}{n} \leq \frac{1}{n}$$

Ambos extremos tienden a 0, así que $\lim = 0$.

---

## 📖 Sucesiones oscilantes

$a_n = (-1)^n$ no converge: oscila entre -1 y 1.

$a_n = (-1)^n \cdot \frac{1}{n}$ sí converge a 0 (la oscilación se "amortigua").

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el límite:

a) $\lim \frac{5n^3 - 2n}{n^3 + 1}$
b) $\lim \left(\frac{n}{n+1}\right)^n$

<details>
<summary>Ver soluciones</summary>

a) $= 5$

b) $= \left(1 + \frac{1}{n}\right)^{-n} \to e^{-1} = \frac{1}{e}$
</details>

---

**Ejercicio 2:** ¿Converge $a_n = \frac{n!}{n^n}$?

<details>
<summary>Ver solución</summary>

$\frac{n!}{n^n} = \frac{1 \cdot 2 \cdot 3 \cdots n}{n \cdot n \cdot n \cdots n} = \prod_{k=1}^n \frac{k}{n} \leq \frac{n}{n} \cdot \frac{1}{n} \cdot ... = \frac{1}{n^{n-1}}$

Converge a 0.
</details>

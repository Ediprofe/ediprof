# Propiedades de la Integral Definida

Las propiedades de la integral definida nos permiten simplificar cálculos y relacionar diferentes integrales.

---

## 🎯 ¿Qué vas a aprender?

- Propiedades algebraicas
- Propiedades de los límites
- Propiedades de desigualdad
- Aplicaciones

---

## 📖 Propiedades algebraicas

### 1. Constante multiplicativa

$$\int_a^b c \cdot f(x)\,dx = c \int_a^b f(x)\,dx$$

### 2. Suma y resta

$$\int_a^b [f(x) \pm g(x)]\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$$

---

## 📖 Propiedades de los límites

### 3. Intervalo de longitud cero

$$\int_a^a f(x)\,dx = 0$$

### 4. Intercambio de límites

$$\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$$

### 5. Aditividad de intervalos

$$\int_a^c f(x)\,dx = \int_a^b f(x)\,dx + \int_b^c f(x)\,dx$$

para cualquier $b$ entre $a$ y $c$ (o fuera).

---

## ⚙️ Ejemplo 1: Aditividad

Si $\int_0^5 f(x)\,dx = 10$ y $\int_0^3 f(x)\,dx = 4$, encuentra $\int_3^5 f(x)\,dx$.

$$\int_0^5 f(x)\,dx = \int_0^3 f(x)\,dx + \int_3^5 f(x)\,dx$$

$$10 = 4 + \int_3^5 f(x)\,dx$$

$$\int_3^5 f(x)\,dx = 6$$

---

## ⚙️ Ejemplo 2: Intercambio

$$\int_5^2 x\,dx = -\int_2^5 x\,dx = -\left[\frac{x^2}{2}\right]_2^5 = -\left(\frac{25}{2} - 2\right) = -\frac{21}{2}$$

---

## 📖 Propiedades de desigualdad

### 6. Conservación de desigualdad

Si $f(x) \leq g(x)$ para todo $x \in [a, b]$:

$$\int_a^b f(x)\,dx \leq \int_a^b g(x)\,dx$$

### 7. Cotas

Si $m \leq f(x) \leq M$ para todo $x \in [a, b]$:

$$m(b-a) \leq \int_a^b f(x)\,dx \leq M(b-a)$$

---

## ⚙️ Ejemplo 3: Estimar integral

Estima $\int_1^4 \sqrt{x}\,dx$ sin calcularla.

En $[1, 4]$: $1 \leq \sqrt{x} \leq 2$

$$1 \cdot 3 \leq \int_1^4 \sqrt{x}\,dx \leq 2 \cdot 3$$

$$3 \leq \int_1^4 \sqrt{x}\,dx \leq 6$$

(Valor real: $\frac{14}{3} \approx 4.67$)

---

## 📖 Propiedades de simetría

### 8. Función par

Si $f(-x) = f(x)$:
$$\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx$$

### 9. Función impar

Si $f(-x) = -f(x)$:
$$\int_{-a}^{a} f(x)\,dx = 0$$

---

## ⚙️ Ejemplo 4: Función par

$$\int_{-2}^{2} x^2\,dx = 2\int_0^2 x^2\,dx = 2 \cdot \frac{8}{3} = \frac{16}{3}$$

---

## ⚙️ Ejemplo 5: Función impar

$$\int_{-\pi}^{\pi} \sin x\,dx = 0$$

(El área positiva cancela la negativa por simetría)

---

## ⚙️ Ejemplo 6: Combinación

$$\int_{-1}^{1} (x^3 + x^2)\,dx$$

$x^3$ es impar → integral = 0

$x^2$ es par → $2\int_0^1 x^2\,dx = \frac{2}{3}$

**Total = $\frac{2}{3}$**

---

## 📖 Valor promedio

El **valor promedio** de $f$ en $[a, b]$ es:

$$f_{prom} = \frac{1}{b-a}\int_a^b f(x)\,dx$$

---

## ⚙️ Ejemplo 7: Valor promedio

Valor promedio de $f(x) = x^2$ en $[0, 3]$:

$$f_{prom} = \frac{1}{3}\int_0^3 x^2\,dx = \frac{1}{3} \cdot 9 = 3$$

---

## 📊 Resumen de propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Constante | $\int c \cdot f = c \int f$ |
| Suma | $\int (f + g) = \int f + \int g$ |
| Aditividad | $\int_a^c = \int_a^b + \int_b^c$ |
| Intercambio | $\int_a^b = -\int_b^a$ |
| Par | $\int_{-a}^a f = 2\int_0^a f$ |
| Impar | $\int_{-a}^a f = 0$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Si $\int_1^6 f(x)\,dx = 8$ y $\int_1^4 f(x)\,dx = 3$, encuentra $\int_4^6 f(x)\,dx$.

<details>
<summary>Ver solución</summary>

$\int_1^6 = \int_1^4 + \int_4^6$

$8 = 3 + \int_4^6$

$\int_4^6 f(x)\,dx = 5$
</details>

---

**Ejercicio 2:** Calcula $\int_{-2}^{2} (x^5 - 3x^3 + 2x)\,dx$.

<details>
<summary>Ver solución</summary>

Todos los términos ($x^5$, $x^3$, $x$) son funciones impares.

La suma de impares es impar.

$\int_{-2}^{2} = 0$
</details>

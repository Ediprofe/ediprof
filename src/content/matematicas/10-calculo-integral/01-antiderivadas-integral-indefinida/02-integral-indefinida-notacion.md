# Integral Indefinida y Notación

La integral indefinida es la notación formal para representar la familia de antiderivadas. Es una de las operaciones fundamentales del cálculo.

---

## 🎯 ¿Qué vas a aprender?

- La notación de integral indefinida
- Propiedades algebraicas de la integral
- Terminología estándar
- Relación con la derivada

---

## 📖 Notación de la integral indefinida

$$\int f(x)\,dx = F(x) + C$$

significa que $F'(x) = f(x)$.

---

## 📖 Partes de la notación

| Símbolo | Nombre | Significado |
|---------|--------|-------------|
| $\int$ | Signo integral | Indica antiderivación |
| $f(x)$ | Integrando | Función a integrar |
| $dx$ | Diferencial | Indica variable de integración |
| $F(x)$ | Antiderivada | Resultado de la integración |
| $C$ | Constante de integración | Representa todas las antiderivadas |

---

## 📖 Propiedades de la integral

### 1. Constante multiplicativa

$$\int k \cdot f(x)\,dx = k \int f(x)\,dx$$

Las constantes "salen" de la integral.

### 2. Suma y resta

$$\int [f(x) \pm g(x)]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$$

Se integra término a término.

---

## ⚠️ Lo que NO se puede hacer

$$\int f(x) \cdot g(x)\,dx \neq \int f(x)\,dx \cdot \int g(x)\,dx$$

$$\int \frac{f(x)}{g(x)}\,dx \neq \frac{\int f(x)\,dx}{\int g(x)\,dx}$$

Los productos y cocientes **no** se pueden separar.

---

## ⚙️ Ejemplo 1: Constante multiplicativa

$$\int 5x^2\,dx = 5 \int x^2\,dx = 5 \cdot \frac{x^3}{3} + C = \frac{5x^3}{3} + C$$

---

## ⚙️ Ejemplo 2: Suma de términos

$$\int (3x^2 + 2x)\,dx = \int 3x^2\,dx + \int 2x\,dx$$

$$= 3 \cdot \frac{x^3}{3} + 2 \cdot \frac{x^2}{2} + C = x^3 + x^2 + C$$

---

## ⚙️ Ejemplo 3: Combinación

$$\int (4x^3 - 6x^2 + 2)\,dx$$

$$= 4 \cdot \frac{x^4}{4} - 6 \cdot \frac{x^3}{3} + 2x + C$$

$$= x^4 - 2x^3 + 2x + C$$

---

## 📖 Notación alternativa

A veces se usan otras variables:

$$\int f(t)\,dt, \quad \int g(u)\,du, \quad \int h(\theta)\,d\theta$$

La variable de integración puede ser cualquiera.

---

## 📖 La integral "deshace" la derivada

$$\frac{d}{dx}\left[\int f(x)\,dx\right] = f(x)$$

$$\int f'(x)\,dx = f(x) + C$$

La derivación y la integración son operaciones inversas (excepto por la constante).

---

## ⚙️ Ejemplo 4: Inversa de la derivada

Si $F(x) = x^3 + 2x$, entonces:

$$\int F'(x)\,dx = \int (3x^2 + 2)\,dx = x^3 + 2x + C$$

Recuperamos $F(x)$ (más una constante).

---

## 📖 Condición inicial

Para determinar el valor de $C$, necesitamos una **condición inicial**:

Si $F(a) = b$ (un valor específico), podemos encontrar $C$.

---

## ⚙️ Ejemplo 5: Con condición inicial

Si $f(x) = 2x$ y $F(0) = 3$, encuentra $F(x)$.

**Paso 1:** Integrar
$$F(x) = \int 2x\,dx = x^2 + C$$

**Paso 2:** Aplicar condición
$$F(0) = 0 + C = 3 \Rightarrow C = 3$$

**Respuesta:** $F(x) = x^2 + 3$

---

## 📊 Resumen de propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Constante | $\int kf = k\int f$ |
| Suma | $\int (f + g) = \int f + \int g$ |
| Resta | $\int (f - g) = \int f - \int g$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

$$\int (6x^2 - 4x + 7)\,dx$$

<details>
<summary>Ver solución</summary>

$$= 6 \cdot \frac{x^3}{3} - 4 \cdot \frac{x^2}{2} + 7x + C = 2x^3 - 2x^2 + 7x + C$$
</details>

---

**Ejercicio 2:** Si $F'(x) = 3x^2 - 1$ y $F(1) = 2$, encuentra $F(x)$.

<details>
<summary>Ver solución</summary>

$F(x) = x^3 - x + C$

$F(1) = 1 - 1 + C = 2 \Rightarrow C = 2$

$F(x) = x^3 - x + 2$
</details>

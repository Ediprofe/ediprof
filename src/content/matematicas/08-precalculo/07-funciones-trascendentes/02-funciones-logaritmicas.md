# Funciones Logarítmicas

El logaritmo es la operación inversa de la exponenciación. Si $2^3 = 8$, entonces $\log_2 8 = 3$. Los logaritmos convierten multiplicaciones en sumas, lo que los hace poderosos para cálculos.

---

## 🎯 ¿Qué vas a aprender?

- Definición del logaritmo
- Propiedades de los logaritmos
- Logaritmo natural y común
- Gráfica de funciones logarítmicas

---

## 📖 Definición

$$
\log_a x = y \quad \Leftrightarrow \quad a^y = x
$$

Se lee: "logaritmo base $a$ de $x$ es igual a $y$".

**Restricciones:**
- $a > 0$, $a \neq 1$ (la base)
- $x > 0$ (el argumento debe ser positivo)

---

## ⚙️ Ejemplo 1: Conversión entre formas

| Forma exponencial | Forma logarítmica |
|-------------------|-------------------|
| $2^3 = 8$ | $\log_2 8 = 3$ |
| $10^2 = 100$ | $\log_{10} 100 = 2$ |
| $5^0 = 1$ | $\log_5 1 = 0$ |
| $3^{-2} = \frac{1}{9}$ | $\log_3 \frac{1}{9} = -2$ |

---

## 📖 Logaritmos especiales

### Logaritmo común (base 10)

$$\log x = \log_{10} x$$

Usado en: decibeles, pH, escala Richter.

### Logaritmo natural (base $e$)

$$\ln x = \log_e x$$

Fundamental en cálculo y ciencias naturales.

---

## 📖 Propiedades de los logaritmos

| Propiedad | Fórmula |
|-----------|---------|
| **Logaritmo de 1** | $\log_a 1 = 0$ |
| **Logaritmo de la base** | $\log_a a = 1$ |
| **Producto** | $\log_a(xy) = \log_a x + \log_a y$ |
| **Cociente** | $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$ |
| **Potencia** | $\log_a(x^n) = n \cdot \log_a x$ |
| **Cambio de base** | $\log_a x = \frac{\log_b x}{\log_b a}$ |

---

## ⚙️ Ejemplo 2: Aplicar propiedades

Expande: $\log_2\left(\frac{x^3 \cdot y}{z^2}\right)$

$$= \log_2(x^3 \cdot y) - \log_2(z^2)$$
$$= \log_2(x^3) + \log_2 y - \log_2(z^2)$$
$$= 3\log_2 x + \log_2 y - 2\log_2 z$$

---

## ⚙️ Ejemplo 3: Condensar logaritmos

Escribe como un solo logaritmo: $2\log x - 3\log y + \frac{1}{2}\log z$

$$= \log x^2 - \log y^3 + \log z^{1/2}$$
$$= \log\left(\frac{x^2 \cdot \sqrt{z}}{y^3}\right)$$

---

## 📖 La función logarítmica

$$f(x) = \log_a x$$

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $(0, +\infty)$ |
| **Rango** | $\mathbb{R}$ |
| **Intercepto X** | $(1, 0)$ siempre |
| **Asíntota vertical** | $x = 0$ (el eje Y) |
| **Inyectiva** | Sí |

### Relación con exponencial

$f(x) = \log_a x$ es la **inversa** de $g(x) = a^x$.

Sus gráficas son simétricas respecto a $y = x$.

---

## ⚙️ Ejemplo 4: Graficar $f(x) = \log_2 x$

| $x$ | $\log_2 x$ |
|-----|------------|
| $\frac{1}{4}$ | $-2$ |
| $\frac{1}{2}$ | $-1$ |
| $1$ | $0$ |
| $2$ | $1$ |
| $4$ | $2$ |
| $8$ | $3$ |

---

## 📖 Transformaciones

$$f(x) = a \cdot \log_b(cx - h) + k$$

| Parámetro | Efecto |
|-----------|--------|
| $h$ | Desplazamiento horizontal (nueva asíntota: $x = h/c$) |
| $k$ | Desplazamiento vertical |
| $a$ | Estiramiento vertical |
| $c$ | Compresión horizontal |

---

## ⚙️ Ejemplo 5: Transformación

Analiza $f(x) = \ln(x - 2) + 3$

**Dominio:** $x - 2 > 0 \Rightarrow x > 2$

**Asíntota vertical:** $x = 2$

**Transformaciones:**
- Desplazamiento 2 a la derecha
- Desplazamiento 3 hacia arriba

**Intercepto X:** Cuando $f(x) = 0$:
$$\ln(x - 2) + 3 = 0$$
$$\ln(x - 2) = -3$$
$$x - 2 = e^{-3}$$
$$x = 2 + e^{-3} \approx 2.05$$

---

## 📖 Ecuaciones logarítmicas

### Método 1: Convertir a forma exponencial

$\log_3 x = 4 \Rightarrow x = 3^4 = 81$

### Método 2: Igualar logaritmos

Si $\log_a x = \log_a y$, entonces $x = y$.

---

## ⚙️ Ejemplo 6: Resolver ecuación

Resuelve: $\log_2(x + 3) + \log_2(x - 1) = 3$

**Paso 1:** Condensamos
$$\log_2[(x + 3)(x - 1)] = 3$$

**Paso 2:** Convertimos a exponencial
$$(x + 3)(x - 1) = 2^3 = 8$$
$$x^2 + 2x - 3 = 8$$
$$x^2 + 2x - 11 = 0$$

**Paso 3:** Fórmula general
$$x = \frac{-2 \pm \sqrt{4 + 44}}{2} = \frac{-2 \pm \sqrt{48}}{2} = -1 \pm 2\sqrt{3}$$

**Paso 4:** Verificar dominio ($x > 1$)

$x = -1 + 2\sqrt{3} \approx 2.46$ ✓

$x = -1 - 2\sqrt{3} \approx -4.46$ ✗ (no cumple $x > 1$)

**Solución:** $x = -1 + 2\sqrt{3}$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Evalúa sin calculadora:

a) $\log_3 27$
b) $\log_5 \frac{1}{25}$
c) $\ln e^4$
d) $\log 10000$

<details>
<summary>Ver soluciones</summary>

a) $3$ (porque $3^3 = 27$)

b) $-2$ (porque $5^{-2} = \frac{1}{25}$)

c) $4$ (por definición $\ln e^x = x$)

d) $4$ (porque $10^4 = 10000$)
</details>

---

**Ejercicio 2:** Expande:

$\log\left(\frac{x^2 y^3}{\sqrt{z}}\right)$

<details>
<summary>Ver solución</summary>

$$= \log(x^2 y^3) - \log(z^{1/2})$$
$$= \log x^2 + \log y^3 - \frac{1}{2}\log z$$
$$= 2\log x + 3\log y - \frac{1}{2}\log z$$
</details>

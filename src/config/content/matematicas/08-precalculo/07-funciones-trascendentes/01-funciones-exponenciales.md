---
title: "Funciones Exponenciales"
---

# Funciones Exponenciales

Las funciones exponenciales modelan crecimiento y decrecimiento en la naturaleza: poblaciones, radiactividad, interés compuesto. Su característica distintiva es que la variable está en el exponente.

---

## 🎯 ¿Qué vas a aprender?

- La forma general de la función exponencial
- La constante $e$ y su importancia
- Propiedades de las funciones exponenciales
- Aplicaciones al crecimiento y decrecimiento

---

## 📖 Definición

Una **función exponencial** tiene la forma:

$$
f(x) = a^x \quad \text{donde } a > 0, \, a \neq 1
$$

- $a$ se llama la **base**
- $x$ es el **exponente** (variable)

### Casos según la base

| Condición | Comportamiento |
|-----------|----------------|
| $a > 1$ | Creciente (crecimiento exponencial) |
| $0 < a < 1$ | Decreciente (decaimiento exponencial) |

---

## 📖 Propiedades fundamentales

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $(0, +\infty)$ |
| **Intercepto Y** | $(0, 1)$ siempre (porque $a^0 = 1$) |
| **Asíntota horizontal** | $y = 0$ (el eje X) |
| **Inyectiva** | Sí |
| **Paridad** | Ninguna |

---

## ⚙️ Ejemplo 1: $f(x) = 2^x$

| $x$ | $2^x$ |
|-----|-------|
| $-2$ | $\frac{1}{4}$ |
| $-1$ | $\frac{1}{2}$ |
| $0$ | $1$ |
| $1$ | $2$ |
| $2$ | $4$ |
| $3$ | $8$ |

**Observación:** Se duplica cada vez que $x$ aumenta en 1.

---

## ⚙️ Ejemplo 2: $g(x) = \left(\frac{1}{2}\right)^x$

| $x$ | $\left(\frac{1}{2}\right)^x$ |
|-----|-----------------------------|
| $-2$ | $4$ |
| $-1$ | $2$ |
| $0$ | $1$ |
| $1$ | $\frac{1}{2}$ |
| $2$ | $\frac{1}{4}$ |

**Observación:** Se reduce a la mitad cada vez que $x$ aumenta en 1.

**Nota:** $\left(\frac{1}{2}\right)^x = 2^{-x}$ (reflexión respecto al eje Y).

---

## 📖 El número $e$

La base más importante en matemáticas es el número $e$:

$$
e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2.71828...
$$

Es irracional y trascendente.

### ¿Por qué es especial?

La función $f(x) = e^x$ es su propia derivada:
$$\frac{d}{dx}[e^x] = e^x$$

Esta propiedad hace que $e^x$ sea fundamental en cálculo.

---

## 📖 Forma general transformada

$$
f(x) = a \cdot b^{c(x-h)} + k
$$

| Parámetro | Efecto |
|-----------|--------|
| $a$ | Estiramiento vertical |
| $b$ | Base (crecimiento si $b > 1$) |
| $c$ | Compresión horizontal |
| $h$ | Desplazamiento horizontal |
| $k$ | Desplazamiento vertical (nueva asíntota: $y = k$) |

---

## ⚙️ Ejemplo 3: Transformación

Analiza $f(x) = 3 \cdot 2^{x-1} + 2$

**Base:** $2$ → creciente

**Transformaciones:**
- Factor vertical: $3$ (estira)
- Desplazamiento: 1 a la derecha
- Desplazamiento: 2 hacia arriba

**Asíntota:** $y = 2$

**Intercepto Y:** $f(0) = 3 \cdot 2^{-1} + 2 = \frac{3}{2} + 2 = 3.5$

---

## 📖 Aplicaciones

### Crecimiento exponencial

$$P(t) = P_0 \cdot e^{kt}$$

donde:
- $P_0$ = población inicial
- $k > 0$ = tasa de crecimiento
- $t$ = tiempo

### Decaimiento exponencial

$$N(t) = N_0 \cdot e^{-kt}$$

Usado para: radiactividad, enfriamiento, depreciación.

---

## ⚙️ Ejemplo 4: Interés compuesto

Una inversión de \$1,000 gana 5% anual compuesto continuamente.

$$A(t) = 1000 \cdot e^{0.05t}$$

**Después de 10 años:**
$$A(10) = 1000 \cdot e^{0.5} \approx 1000 \cdot 1.6487 \approx \$1,648.72$$

---

## 📊 Comparación de exponenciales

| Base | Comportamiento | Ejemplo |
|------|---------------|---------|
| $e \approx 2.718$ | Crecimiento natural | $e^x$ |
| $2$ | Duplicación | $2^x$ |
| $10$ | Órdenes de magnitud | $10^x$ |
| $\frac{1}{2}$ | Reducción a mitad | $\left(\frac{1}{2}\right)^x$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Evalúa:

a) $3^4$
b) $2^{-3}$
c) $e^0$
d) $\left(\frac{1}{3}\right)^2$

<details>
<summary>Ver soluciones</summary>

a) $81$

b) $\frac{1}{8}$

c) $1$

d) $\frac{1}{9}$
</details>

---

**Ejercicio 2:** Para $f(x) = 5^x$, encuentra:

a) $f(2)$
b) $f(-1)$
c) El dominio y rango

<details>
<summary>Ver soluciones</summary>

a) $f(2) = 25$

b) $f(-1) = \frac{1}{5}$

c) Dominio: $\mathbb{R}$, Rango: $(0, +\infty)$
</details>

---

**Ejercicio 3:** Una población de bacterias se duplica cada 3 horas. Si inicialmente hay 500 bacterias, ¿cuántas habrá después de 12 horas?

<details>
<summary>Ver solución</summary>

$$P(t) = 500 \cdot 2^{t/3}$$

Después de 12 horas:
$$P(12) = 500 \cdot 2^{12/3} = 500 \cdot 2^4 = 500 \cdot 16 = 8000$$
</details>

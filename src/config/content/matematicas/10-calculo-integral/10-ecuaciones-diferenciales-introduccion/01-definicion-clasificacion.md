---
title: "Definición y Clasificación de Ecuaciones Diferenciales"
---

# Definición y Clasificación de Ecuaciones Diferenciales

Las ecuaciones diferenciales modelan cambios y procesos dinámicos. Son fundamentales en física, ingeniería y ciencias naturales.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una ecuación diferencial
- Clasificación por tipo
- Orden y grado
- Soluciones generales y particulares

---

## 📖 Definición

Una **ecuación diferencial** es una ecuación que involucra derivadas de una función desconocida.

$$
F(x, y, y', y'', ..., y^{(n)}) = 0
$$

---

## 📖 Clasificación por tipo

### Ecuación Diferencial Ordinaria (EDO)
La función depende de una sola variable independiente.

$$
\frac{dy}{dx} + y = x
$$

### Ecuación Diferencial Parcial (EDP)
La función depende de varias variables independientes.

$$
\frac{\partial u}{\partial t} = k\frac{\partial^2 u}{\partial x^2}
$$

---

## 📖 Orden

El **orden** es el de la derivada más alta que aparece.

| Ejemplo | Orden |
|---------|-------|
| $y' + y = 0$ | 1 |
| $y'' + y' + y = 0$ | 2 |
| $y''' - y = x$ | 3 |

---

## 📖 Grado

El **grado** es la potencia de la derivada de mayor orden (cuando está despejada).

| Ejemplo | Grado |
|---------|-------|
| $y'' + y = 0$ | 1 |
| $(y')^2 + y = 0$ | 2 |
| $(y'')^3 + y' = 0$ | 3 |

---

## 📖 Linealidad

Una ED es **lineal** si tiene la forma:

$$
a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + ... + a_1(x)y' + a_0(x)y = g(x)
$$

**No lineal** si contiene productos $yy'$, potencias $y^2$, funciones $\sin(y)$, etc.

---

## ⚙️ Ejemplo 1: Clasificar

| ED | Orden | Grado | Lineal |
|----|-------|-------|--------|
| $y' = x + y$ | 1 | 1 | Sí |
| $y'' + \sin y = 0$ | 2 | 1 | No |
| $(y')^2 = y$ | 1 | 2 | No |
| $y''' - xy' + y = e^x$ | 3 | 1 | Sí |

---

## 📖 Solución de una ED

Una **solución** es una función que satisface la ecuación.

**Solución general:** Contiene constantes arbitrarias (tantas como el orden).

**Solución particular:** Se obtiene dando valores a las constantes (usando condiciones iniciales).

---

## ⚙️ Ejemplo 2: Verificar solución

¿Es $y = e^{2x}$ solución de $y' - 2y = 0$?

$y' = 2e^{2x}$

$y' - 2y = 2e^{2x} - 2e^{2x} = 0$ ✓

---

## ⚙️ Ejemplo 3: Solución general

$y' = 2x$ tiene solución general $y = x^2 + C$

Con condición inicial $y(0) = 3$:
$3 = 0 + C \Rightarrow C = 3$

Solución particular: $y = x^2 + 3$

---

## 📖 Problema de valor inicial (PVI)

Un PVI consiste en:
- Una ED
- Condiciones iniciales

$$
y' = f(x, y), \quad y(x_0) = y_0
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Clasifica cada ED:

a) $\frac{d^2y}{dx^2} + 3\frac{dy}{dx} = x$
b) $y \cdot y' = x$

<details>
<summary>Ver soluciones</summary>

a) Orden 2, grado 1, lineal (EDO)

b) Orden 1, grado 1, no lineal (producto $yy'$)
</details>

---

**Ejercicio 2:** Verifica que $y = Ce^x$ es solución de $y' = y$.

<details>
<summary>Ver solución</summary>

$y' = Ce^x = y$ ✓
</details>

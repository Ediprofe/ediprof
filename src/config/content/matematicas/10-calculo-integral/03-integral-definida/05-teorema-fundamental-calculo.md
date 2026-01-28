---
title: "Teorema Fundamental del Cálculo"
---

# Teorema Fundamental del Cálculo

El Teorema Fundamental del Cálculo conecta derivación e integración, mostrando que son operaciones inversas. Es el resultado más importante del cálculo.

---

## 🎯 ¿Qué vas a aprender?

- Las dos partes del TFC
- Cómo evaluar integrales definidas
- La función acumuladora
- Aplicaciones inmediatas

---

## 📖 TFC Parte 1

> **Teorema:** Si $f$ es continua en $[a, b]$, entonces la función:
>
> $$
> F(x) = \int_a^x f(t)\,dt
> $$
>
> es diferenciable y $F'(x) = f(x)$.

**En símbolos:**

$$
\frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x)
$$

---

## 📖 Interpretación de Parte 1

La derivada de la "función acumuladora de área" es la función original.

La integración y derivación son inversas.

---

## ⚙️ Ejemplo 1: Parte 1 directa

$$
\frac{d}{dx}\left[\int_1^x t^3\,dt\right] = x^3
$$

$$
\frac{d}{dx}\left[\int_0^x \cos t\,dt\right] = \cos x
$$

---

## ⚙️ Ejemplo 2: Con regla de la cadena

$$
\frac{d}{dx}\left[\int_0^{x^2} \sin t\,dt\right]
$$

Sea $u = x^2$, entonces:

$$
= \sin(x^2) \cdot \frac{d}{dx}[x^2] = \sin(x^2) \cdot 2x = 2x\sin(x^2)
$$

**Fórmula general:**

$$
\frac{d}{dx}\left[\int_a^{g(x)} f(t)\,dt\right] = f(g(x)) \cdot g'(x)
$$

---

## 📖 TFC Parte 2 (Regla de evaluación)

> **Teorema:** Si $f$ es continua en $[a, b]$ y $F$ es cualquier antiderivada de $f$:
>
> $$
> \int_a^b f(x)\,dx = F(b) - F(a)
> $$

---

## 📖 Notación de evaluación

$$
\int_a^b f(x)\,dx = \left[F(x)\right]_a^b = F(x)\Big|_a^b = F(b) - F(a)
$$

---

## ⚙️ Ejemplo 3: Evaluación básica

$$
\int_1^4 x^2\,dx = \left[\frac{x^3}{3}\right]_1^4 = \frac{64}{3} - \frac{1}{3} = \frac{63}{3} = 21
$$

---

## ⚙️ Ejemplo 4: Con trigonométrica

$$
\int_0^{\pi} \sin x\,dx = \left[-\cos x\right]_0^{\pi} = (-\cos\pi) - (-\cos 0)
$$

$$
= -(-1) - (-1) = 1 + 1 = 2
$$

---

## ⚙️ Ejemplo 5: Exponencial

$$
\int_0^1 e^x\,dx = \left[e^x\right]_0^1 = e^1 - e^0 = e - 1
$$

---

## ⚙️ Ejemplo 6: Logaritmo

$$
\int_1^e \frac{1}{x}\,dx = \left[\ln x\right]_1^e = \ln e - \ln 1 = 1 - 0 = 1
$$

---

## 📖 Conexión entre las dos partes

Parte 1: $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ (derivar integral = original)

Parte 2: $\int_a^b F'(x)\,dx = F(b) - F(a)$ (integral de derivada = función evaluada)

Son operaciones inversas, pero la integral recupera la función "salvo constante".

---

## ⚙️ Ejemplo 7: Combinación

$$
\int_0^2 (3x^2 - 4x + 1)\,dx
$$

$$
= \left[x^3 - 2x^2 + x\right]_0^2
$$

$$
= (8 - 8 + 2) - (0) = 2
$$

---

## ⚙️ Ejemplo 8: Con sustitución

$$
\int_0^{\pi/2} \cos^2 x \sin x\,dx
$$

$u = \cos x$, $du = -\sin x\,dx$

Cambio de límites: $x=0 \to u=1$, $x=\pi/2 \to u=0$

$$
= -\int_1^0 u^2\,du = \int_0^1 u^2\,du = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3}
$$

---

## 📊 Resumen

| Parte | Fórmula | Significado |
|-------|---------|-------------|
| TFC 1 | $\frac{d}{dx}\int_a^x f = f(x)$ | Derivar integral = integrando |
| TFC 2 | $\int_a^b f = F(b) - F(a)$ | Integral = antiderivada evaluada |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\int_1^3 (2x - 1)\,dx$
b) $\int_0^{\pi/4} \sec^2 x\,dx$

<details>
<summary>Ver soluciones</summary>

a) 

$$
[x^2 - x]_1^3 = (9-3) - (1-1) = 6
$$

b) 

$$
[\tan x]_0^{\pi/4} = 1 - 0 = 1
$$
</details>

---

**Ejercicio 2:** Encuentra $F'(x)$:

$$
F(x) = \int_2^{x^3} \sqrt{t+1}\,dt
$$

<details>
<summary>Ver solución</summary>

Por Parte 1 con cadena:

$$
F'(x) = \sqrt{x^3+1} \cdot 3x^2
$$
</details>

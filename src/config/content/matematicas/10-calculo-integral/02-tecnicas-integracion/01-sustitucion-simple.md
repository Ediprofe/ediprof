---
title: "Sustitución Simple (Cambio de Variable)"
---

# Sustitución Simple (Cambio de Variable)

La sustitución es la técnica más fundamental de integración. Es la "inversa" de la regla de la cadena para derivadas.

---

## 🎯 ¿Qué vas a aprender?

- El método de sustitución
- Cómo identificar $u$ y $du$
- Cuándo usar sustitución
- Sustituciones comunes

---

## 📖 La idea

Si reconocemos una integral de la forma:

$$
\int f(g(x)) \cdot g'(x)\,dx
$$

Podemos sustituir $u = g(x)$, $du = g'(x)\,dx$ y obtener:

$$
\int f(u)\,du
$$

que suele ser más simple.

---

## 📖 El método paso a paso

1. **Elegir** $u$ (usualmente la parte "interior")
2. **Calcular** $du = \frac{du}{dx} \cdot dx$
3. **Sustituir** $u$ y $du$ en la integral
4. **Integrar** en términos de $u$
5. **Revertir** sustituyendo $u$ por su expresión en $x$

---

## ⚙️ Ejemplo 1: Sustitución básica

Calcula:

$$
\int 2x(x^2 + 1)^5\,dx
$$

**Paso 1:** $u = x^2 + 1$

**Paso 2:** $du = 2x\,dx$ ✓ (¡ya está en la integral!)

**Paso 3:** 

$$
\int u^5\,du
$$

**Paso 4:** 

$$
= \frac{u^6}{6} + C
$$

**Paso 5:** 

$$
= \frac{(x^2 + 1)^6}{6} + C
$$

---

## ⚙️ Ejemplo 2: Ajustar constantes

Calcula:

$$
\int x(x^2 + 3)^4\,dx
$$

**Solución:** $u = x^2 + 3$, $du = 2x\,dx$

Pero tenemos $x\,dx$, no $2x\,dx$. Ajustamos:

$$
x\,dx = \frac{1}{2}\,du
$$

$$
\int x(x^2 + 3)^4\,dx = \int u^4 \cdot \frac{1}{2}\,du = \frac{1}{2} \cdot \frac{u^5}{5} + C
$$

$$
= \frac{(x^2 + 3)^5}{10} + C
$$

---

## ⚙️ Ejemplo 3: Exponencial

Calcula:

$$
\int e^{3x}\,dx
$$

**Solución:** $u = 3x$, $du = 3\,dx$ → $dx = \frac{du}{3}$

$$
\int e^u \cdot \frac{du}{3} = \frac{1}{3}e^u + C = \frac{e^{3x}}{3} + C
$$

---

## ⚙️ Ejemplo 4: Con raíz

Calcula:

$$
\int \frac{x}{\sqrt{x^2 + 1}}\,dx
$$

**Solución:** $u = x^2 + 1$, $du = 2x\,dx$ → $x\,dx = \frac{du}{2}$

$$
= \int \frac{1}{\sqrt{u}} \cdot \frac{du}{2} = \frac{1}{2}\int u^{-1/2}\,du
$$

$$
= \frac{1}{2} \cdot 2u^{1/2} + C = \sqrt{x^2 + 1} + C
$$

---

## ⚙️ Ejemplo 5: Trigonométrica

Calcula:

$$
\int \cos x \cdot \sin^3 x\,dx
$$

**Solución:** $u = \sin x$, $du = \cos x\,dx$

$$
= \int u^3\,du = \frac{u^4}{4} + C = \frac{\sin^4 x}{4} + C
$$

---

## ⚙️ Ejemplo 6: Logaritmo

Calcula:

$$
\int \frac{1}{x \ln x}\,dx
$$

**Solución:** $u = \ln x$, $du = \frac{1}{x}\,dx$

$$
= \int \frac{1}{u}\,du = \ln|u| + C = \ln|\ln x| + C
$$

---

## 📖 Cómo elegir u

| Forma de integral | Buena elección de $u$ |
|-------------------|----------------------|
| $\int f(ax + b)\,dx$ | $u = ax + b$ |
| $\int f(x^n) \cdot x^{n-1}\,dx$ | $u = x^n$ |
| $\int f(\sin x) \cdot \cos x\,dx$ | $u = \sin x$ |
| $\int f(e^x) \cdot e^x\,dx$ | $u = e^x$ |
| $\int f(\ln x) \cdot \frac{1}{x}\,dx$ | $u = \ln x$ |

---

## ⚙️ Ejemplo 7: Forma ax + b

Calcula:

$$
\int (2x + 5)^7\,dx
$$

**Solución:** $u = 2x + 5$, $du = 2\,dx$ → $dx = \frac{du}{2}$

$$
= \frac{1}{2}\int u^7\,du = \frac{1}{2} \cdot \frac{u^8}{8} + C = \frac{(2x+5)^8}{16} + C
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\int 4x(x^2 - 1)^3\,dx$
b) $\int e^{-2x}\,dx$
c) $\int \frac{\cos x}{\sin x}\,dx$

<details>
<summary>Ver soluciones</summary>

a) $u = x^2 - 1$, $du = 2x\,dx$
   
$$
= 2\int u^3\,du = \frac{u^4}{2} + C = \frac{(x^2-1)^4}{2} + C
$$

b) $u = -2x$, $du = -2\,dx$
   
$$
= -\frac{1}{2}e^{-2x} + C
$$

c) $u = \sin x$, $du = \cos x\,dx$
   
$$
= \ln|\sin x| + C
$$

</details>

---

**Ejercicio 2:** Calcula:

$$
\int \frac{e^{\sqrt{x}}}{\sqrt{x}}\,dx
$$

<details>
<summary>Ver solución</summary>

$u = \sqrt{x}$, $du = \frac{1}{2\sqrt{x}}\,dx$

$$
\frac{dx}{\sqrt{x}} = 2\,du
$$

$$
= 2\int e^u\,du = 2e^u + C = 2e^{\sqrt{x}} + C
$$

</details>

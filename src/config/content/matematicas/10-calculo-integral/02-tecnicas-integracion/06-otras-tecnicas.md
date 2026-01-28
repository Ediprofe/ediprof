---
title: "Otras Técnicas de Integración"
---

# Otras Técnicas de Integración

Además de las técnicas principales, existen métodos adicionales para integrales especiales que no encajan en las categorías anteriores.

---

## 🎯 ¿Qué vas a aprender?

- Sustitución de Weierstrass
- Integrales de funciones racionales de seno y coseno
- Fórmulas de reducción
- Estrategias generales

---

## 📖 Sustitución de Weierstrass

Para integrales racionales de $\sin x$ y $\cos x$, la sustitución:

$$
t = \tan\frac{x}{2}
$$

transforma todo en una función racional de $t$.

**Fórmulas resultantes:**

$$
\sin x = \frac{2t}{1+t^2}, \quad \cos x = \frac{1-t^2}{1+t^2}, \quad dx = \frac{2}{1+t^2}\,dt
$$

---

## ⚙️ Ejemplo 1: Weierstrass

Calcula:

$$
\int \frac{1}{1 + \sin x}\,dx
$$

**Solución:** Con $t = \tan\frac{x}{2}$:

$$
= \int \frac{1}{1 + \frac{2t}{1+t^2}} \cdot \frac{2}{1+t^2}\,dt
$$

$$
= \int \frac{2}{1+t^2+2t}\,dt = \int \frac{2}{(1+t)^2}\,dt
$$

$$
= -\frac{2}{1+t} + C = -\frac{2}{1+\tan\frac{x}{2}} + C
$$

---

## 📖 Fórmulas de reducción

Las fórmulas de reducción expresan integrales de potencia alta en términos de potencias más bajas.

---

## ⚙️ Ejemplo 2: Reducción para seno

$$
\int \sin^n x\,dx = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}\int \sin^{n-2}x\,dx
$$

Para $\int \sin^4 x\,dx$:

$$
= -\frac{\sin^3 x\cos x}{4} + \frac{3}{4}\int \sin^2 x\,dx
$$

$$
= -\frac{\sin^3 x\cos x}{4} + \frac{3}{4}\left(\frac{x}{2} - \frac{\sin 2x}{4}\right) + C
$$

---

## 📖 Fórmulas de reducción comunes

$$
\int \sin^n x\,dx = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}\int \sin^{n-2}x\,dx
$$

$$
\int \cos^n x\,dx = \frac{\cos^{n-1}x\sin x}{n} + \frac{n-1}{n}\int \cos^{n-2}x\,dx
$$

$$
\int \tan^n x\,dx = \frac{\tan^{n-1}x}{n-1} - \int \tan^{n-2}x\,dx
$$

$$
\int \sec^n x\,dx = \frac{\sec^{n-2}x\tan x}{n-1} + \frac{n-2}{n-1}\int \sec^{n-2}x\,dx
$$

---

## 📖 Completar el cuadrado

Para integrales con $ax^2 + bx + c$, completar el cuadrado convierte a formas estándar.

---

## ⚙️ Ejemplo 3: Completar cuadrado

Calcula:

$$
\int \frac{1}{x^2 + 6x + 13}\,dx
$$

**Solución:**

$$
x^2 + 6x + 13 = (x+3)^2 + 4
$$

$$
= \int \frac{1}{(x+3)^2 + 4}\,dx
$$

$u = x + 3$:

$$
= \frac{1}{2}\arctan\frac{x+3}{2} + C
$$

---

## ⚙️ Ejemplo 4: Raíz con cuadrado completo

Calcula:

$$
\int \frac{1}{\sqrt{x^2 - 4x + 5}}\,dx
$$

**Solución:**

$$
= \int \frac{1}{\sqrt{(x-2)^2 + 1}}\,dx
$$

$u = x - 2$:

$$
= \ln\left|u + \sqrt{u^2+1}\right| + C = \ln\left|x - 2 + \sqrt{x^2-4x+5}\right| + C
$$

---

## 📖 Sustitución racionalizante

Para raíces de la forma $\sqrt[n]{ax + b}$, sustituir $u = \sqrt[n]{ax + b}$.

---

## ⚙️ Ejemplo 5: Raíz cúbica

Calcula:

$$
\int \frac{1}{1 + \sqrt[3]{x}}\,dx
$$

**Solución:** $u = \sqrt[3]{x}$ → $x = u^3$, $dx = 3u^2\,du$

$$
= \int \frac{3u^2}{1 + u}\,du
$$

División larga: $\frac{u^2}{1+u} = u - 1 + \frac{1}{1+u}$

$$
= 3\int \left(u - 1 + \frac{1}{1+u}\right)\,du
$$

$$
= 3\left(\frac{u^2}{2} - u + \ln|1+u|\right) + C
$$

$$
= \frac{3\sqrt[3]{x^2}}{2} - 3\sqrt[3]{x} + 3\ln|1+\sqrt[3]{x}| + C
$$

---

## 📖 Estrategia general de integración

1. ¿Es una fórmula básica? → Usar directamente
2. ¿Hay una sustitución obvia? → Sustituir
3. ¿Es producto de funciones? → Integración por partes
4. ¿Es función racional? → Fracciones parciales
5. ¿Tiene raíz cuadrática? → Sustitución trigonométrica
6. ¿Tiene potencias trigonométricas? → Identidades
7. ¿Combinación? → Aplicar varias técnicas

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa la fórmula de reducción:

$$
\int \cos^3 x\,dx
$$

<details>
<summary>Ver solución</summary>

$$
= \frac{\cos^2 x \sin x}{3} + \frac{2}{3}\int \cos x\,dx
$$

$$
= \frac{\cos^2 x \sin x}{3} + \frac{2\sin x}{3} + C
$$

$$
= \frac{\sin x(2 + \cos^2 x)}{3} + C
$$

(O más fácil: $\int \cos x(1-\sin^2 x)\,dx = \sin x - \frac{\sin^3 x}{3} + C$)

</details>

---

**Ejercicio 2:** Calcula:

$$
\int \frac{1}{\sqrt{2x - x^2}}\,dx
$$

<details>
<summary>Ver solución</summary>

$$
2x - x^2 = -(x^2 - 2x) = 1 - (x-1)^2
$$

$$
= \int \frac{1}{\sqrt{1-(x-1)^2}}\,dx = \arcsin(x-1) + C
$$

</details>

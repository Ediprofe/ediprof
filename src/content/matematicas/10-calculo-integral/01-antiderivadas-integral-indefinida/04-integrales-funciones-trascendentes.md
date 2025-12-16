# Integrales de Funciones Trascendentes

Las funciones trascendentes (exponenciales, logarítmicas, trigonométricas y sus inversas) tienen fórmulas de integración específicas que complementan las reglas básicas.

---

## 🎯 ¿Qué vas a aprender?

- Integrales de funciones exponenciales
- Integrales de funciones trigonométricas
- Integrales que producen funciones inversas
- Combinaciones con otras reglas

---

## 📖 Integrales exponenciales

$$\int e^x\,dx = e^x + C$$

$$\int e^{ax}\,dx = \frac{e^{ax}}{a} + C$$

$$\int a^x\,dx = \frac{a^x}{\ln a} + C$$

---

## ⚙️ Ejemplo 1: Exponenciales

$$\int e^{3x}\,dx = \frac{e^{3x}}{3} + C$$

$$\int 2^x\,dx = \frac{2^x}{\ln 2} + C$$

$$\int 5e^{-x}\,dx = 5 \cdot \frac{e^{-x}}{-1} + C = -5e^{-x} + C$$

---

## 📖 Integrales trigonométricas

| Integral | Resultado |
|----------|-----------|
| $\int \sin x\,dx$ | $-\cos x + C$ |
| $\int \cos x\,dx$ | $\sin x + C$ |
| $\int \tan x\,dx$ | $-\ln\|\cos x\| + C$ = $\ln\|\sec x\| + C$ |
| $\int \cot x\,dx$ | $\ln\|\sin x\| + C$ |
| $\int \sec x\,dx$ | $\ln\|\sec x + \tan x\| + C$ |
| $\int \csc x\,dx$ | $-\ln\|\csc x + \cot x\| + C$ |

---

## ⚙️ Ejemplo 2: Seno y coseno

$$\int (3\sin x + 2\cos x)\,dx = -3\cos x + 2\sin x + C$$

---

## ⚙️ Ejemplo 3: Secante cuadrado

$$\int 4\sec^2 x\,dx = 4\tan x + C$$

---

## 📖 Integrales que producen inversas trigonométricas

$$\int \frac{1}{\sqrt{1-x^2}}\,dx = \arcsin x + C$$

$$\int \frac{-1}{\sqrt{1-x^2}}\,dx = \arccos x + C$$

$$\int \frac{1}{1+x^2}\,dx = \arctan x + C$$

---

## 📖 Formas generales

$$\int \frac{1}{\sqrt{a^2-x^2}}\,dx = \arcsin\frac{x}{a} + C$$

$$\int \frac{1}{a^2+x^2}\,dx = \frac{1}{a}\arctan\frac{x}{a} + C$$

---

## ⚙️ Ejemplo 4: Arco tangente

$$\int \frac{1}{1+x^2}\,dx = \arctan x + C$$

$$\int \frac{1}{4+x^2}\,dx = \frac{1}{2}\arctan\frac{x}{2} + C$$

---

## ⚙️ Ejemplo 5: Arco seno

$$\int \frac{1}{\sqrt{1-x^2}}\,dx = \arcsin x + C$$

$$\int \frac{1}{\sqrt{9-x^2}}\,dx = \arcsin\frac{x}{3} + C$$

---

## ⚙️ Ejemplo 6: Combinación

$$\int \left(e^x + \cos x + \frac{1}{1+x^2}\right)\,dx$$

$$= e^x + \sin x + \arctan x + C$$

---

## 📖 Integral logarítmica

$$\int \ln x\,dx = x\ln x - x + C$$

(Se obtiene por integración por partes, que veremos después)

---

## ⚙️ Ejemplo 7: Con identidades

$$\int \tan^2 x\,dx = \int (\sec^2 x - 1)\,dx = \tan x - x + C$$

(usando $\tan^2 x = \sec^2 x - 1$)

---

## ⚙️ Ejemplo 8: Simplificar primero

$$\int \frac{\sin x}{\cos^2 x}\,dx = \int \sec x \tan x\,dx = \sec x + C$$

---

## 📊 Tabla resumen

| Función | Integral |
|---------|----------|
| $e^x$ | $e^x + C$ |
| $e^{ax}$ | $\frac{e^{ax}}{a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |
| $\frac{1}{1+x^2}$ | $\arctan x + C$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\int (e^{2x} + \sin x)\,dx$
b) $\int \frac{3}{x^2 + 1}\,dx$
c) $\int 10^x\,dx$

<details>
<summary>Ver soluciones</summary>

a) $\frac{e^{2x}}{2} - \cos x + C$

b) $3\arctan x + C$

c) $\frac{10^x}{\ln 10} + C$
</details>

---

**Ejercicio 2:** Calcula:

$$\int \frac{2}{\sqrt{4 - x^2}}\,dx$$

<details>
<summary>Ver solución</summary>

$$= 2 \int \frac{1}{\sqrt{4-x^2}}\,dx = 2\arcsin\frac{x}{2} + C$$
</details>

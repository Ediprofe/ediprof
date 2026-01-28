---
title: "Fórmulas de Integración Básicas"
---

# Fórmulas de Integración Básicas

Las fórmulas básicas de integración son las "inversas" de las reglas de derivación. Memorizar estas fórmulas es esencial para la integración.

---

## 🎯 ¿Qué vas a aprender?

- Fórmulas fundamentales de integración
- Regla de la potencia para integrales
- Integrales de funciones básicas
- Aplicación sistemática

---

## 📖 Tabla de integrales básicas

### Potencias

$$
\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)
$$

$$
\int \frac{1}{x}\,dx = \ln|x| + C
$$

$$
\int 1\,dx = x + C
$$

---

### Exponenciales

$$
\int e^x\,dx = e^x + C
$$

$$
\int a^x\,dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)
$$

---

### Trigonométricas

$$
\int \sin x\,dx = -\cos x + C
$$

$$
\int \cos x\,dx = \sin x + C
$$

$$
\int \sec^2 x\,dx = \tan x + C
$$

$$
\int \csc^2 x\,dx = -\cot x + C
$$

$$
\int \sec x \tan x\,dx = \sec x + C
$$

$$
\int \csc x \cot x\,dx = -\csc x + C
$$

---

## 📖 Regla de la potencia

$$
\boxed{\int x^n\,dx = \frac{x^{n+1}}{n+1} + C}
$$

> 💡 **Regla mnemotécnica:** "Sumar 1 al exponente y dividir entre el nuevo exponente."

---

## ⚙️ Ejemplo 1: Potencias enteras

$$
\int x^5\,dx = \frac{x^6}{6} + C
$$

$$
\int x^{100}\,dx = \frac{x^{101}}{101} + C
$$

---

## ⚙️ Ejemplo 2: Potencias negativas

$$
\int x^{-3}\,dx = \frac{x^{-2}}{-2} + C = -\frac{1}{2x^2} + C
$$

$$
\int \frac{1}{x^4}\,dx = \int x^{-4}\,dx = \frac{x^{-3}}{-3} + C = -\frac{1}{3x^3} + C
$$

---

## ⚙️ Ejemplo 3: Raíces

$$
\int \sqrt{x}\,dx = \int x^{1/2}\,dx = \frac{x^{3/2}}{3/2} + C = \frac{2}{3}x^{3/2} + C
$$

$$
\int \sqrt[3]{x}\,dx = \int x^{1/3}\,dx = \frac{x^{4/3}}{4/3} + C = \frac{3}{4}x^{4/3} + C
$$

---

## ⚙️ Ejemplo 4: El caso especial n = -1

$$
\int \frac{1}{x}\,dx = \int x^{-1}\,dx = \ln|x| + C
$$

> ⚠️ ¡La regla de potencia no aplica aquí! ($\frac{x^0}{0}$ no existe)

---

## ⚙️ Ejemplo 5: Polinomio completo

Calcula:

$$
\int (3x^4 - 2x^2 + 5x - 1)\,dx
$$

**Solución:**

$$
= 3 \cdot \frac{x^5}{5} - 2 \cdot \frac{x^3}{3} + 5 \cdot \frac{x^2}{2} - x + C
$$

$$
= \frac{3x^5}{5} - \frac{2x^3}{3} + \frac{5x^2}{2} - x + C
$$

---

## ⚙️ Ejemplo 6: Simplificar antes de integrar

Calcula:

$$
\int \frac{x^3 + 2x}{x}\,dx
$$

**Solución:**

$$
= \int \left(x^2 + 2\right)\,dx = \frac{x^3}{3} + 2x + C
$$

---

## ⚙️ Ejemplo 7: Expandir antes de integrar

Calcula:

$$
\int (x + 1)^2\,dx
$$

**Solución:**

$$
= \int (x^2 + 2x + 1)\,dx = \frac{x^3}{3} + x^2 + x + C
$$

---

## ⚙️ Ejemplo 8: Combinación

Calcula:

$$
\int \left(\frac{3}{x^2} + 2\sqrt{x}\right)\,dx
$$

**Solución:**

$$
= \int (3x^{-2} + 2x^{1/2})\,dx
$$

$$
= 3 \cdot \frac{x^{-1}}{-1} + 2 \cdot \frac{x^{3/2}}{3/2} + C
$$

$$
= -\frac{3}{x} + \frac{4}{3}x^{3/2} + C
$$

---

## 📊 Resumen de fórmulas

| Función | Integral |
|---------|----------|
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln\|x\| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\int x^7\,dx$
b) $\int \frac{5}{x^3}\,dx$
c) $\int \sqrt[4]{x^3}\,dx$

<details>
<summary>Ver soluciones</summary>

a) 

$$
\frac{x^8}{8} + C
$$

b) 

$$
\int 5x^{-3}\,dx = -\frac{5}{2}x^{-2} + C = -\frac{5}{2x^2} + C
$$

c) 

$$
\int x^{3/4}\,dx = \frac{x^{7/4}}{7/4} + C = \frac{4}{7}x^{7/4} + C
$$

</details>

---

**Ejercicio 2:** Calcula:

$$
\int \left(x + \frac{1}{x}\right)^2\,dx
$$

<details>
<summary>Ver solución</summary>

Expandimos:

$$
\left(x + \frac{1}{x}\right)^2 = x^2 + 2 + \frac{1}{x^2}
$$

Integramos:

$$
\int (x^2 + 2 + x^{-2})\,dx = \frac{x^3}{3} + 2x - \frac{1}{x} + C
$$

</details>

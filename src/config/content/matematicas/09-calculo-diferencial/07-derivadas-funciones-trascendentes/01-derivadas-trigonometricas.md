---
title: "Derivadas Trigonométricas"
---

# Derivadas Trigonométricas

Las funciones trigonométricas tienen derivadas que forman un patrón elegante y cíclico. Conocerlas es esencial para el cálculo.

---

## 🎯 ¿Qué vas a aprender?

- Derivadas de las seis funciones trigonométricas
- Demostración de $(\sin x)' = \cos x$
- Combinación con la regla de la cadena
- Patrones y mnemotécnicos

---

## 📖 Las seis derivadas trigonométricas

| Función | Derivada |
|---------|----------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |

---

## 📖 Demostración: $(\sin x)' = \cos x$

Usando la definición de derivada:

$$
(\sin x)' = \lim_{h \to 0} \frac{\sin(x + h) - \sin x}{h}
$$

Aplicamos la fórmula de suma: $\sin(x + h) = \sin x \cos h + \cos x \sin h$

$$= \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h}$$

$$= \lim_{h \to 0} \frac{\sin x(\cos h - 1) + \cos x \sin h}{h}$$

$$= \sin x \lim_{h \to 0} \frac{\cos h - 1}{h} + \cos x \lim_{h \to 0} \frac{\sin h}{h}$$

$$= \sin x \cdot 0 + \cos x \cdot 1 = \cos x$$

---

## 📖 Demostración: $(\cos x)' = -\sin x$

Similarmente:

$$
(\cos x)' = \lim_{h \to 0} \frac{\cos(x + h) - \cos x}{h}
$$

Usando $\cos(x + h) = \cos x \cos h - \sin x \sin h$:

$$= \cos x \lim_{h \to 0} \frac{\cos h - 1}{h} - \sin x \lim_{h \to 0} \frac{\sin h}{h}$$

$$= \cos x \cdot 0 - \sin x \cdot 1 = -\sin x$$

---

## 📖 Patrón cíclico

$$\sin x \xrightarrow{d/dx} \cos x \xrightarrow{d/dx} -\sin x \xrightarrow{d/dx} -\cos x \xrightarrow{d/dx} \sin x$$

Las derivadas giran en ciclo de cuatro.

---

## ⚙️ Ejemplo 1: Derivadas directas

a) $\frac{d}{dx}[\sin x] = \cos x$

b) $\frac{d}{dx}[3\cos x] = -3\sin x$

c) $\frac{d}{dx}[\tan x + \sec x] = \sec^2 x + \sec x \tan x$

---

## ⚙️ Ejemplo 2: Con regla de la cadena

Deriva $f(x) = \sin(3x)$

$$
f'(x) = \cos(3x) \cdot 3 = 3\cos(3x)
$$

---

## ⚙️ Ejemplo 3: Coseno de expresión

Deriva $g(x) = \cos(x^2 + 1)$

$$
g'(x) = -\sin(x^2 + 1) \cdot 2x = -2x\sin(x^2 + 1)
$$

---

## ⚙️ Ejemplo 4: Tangente compuesta

Deriva $h(x) = \tan(\sqrt{x})$

$$
h'(x) = \sec^2(\sqrt{x}) \cdot \frac{1}{2\sqrt{x}} = \frac{\sec^2(\sqrt{x})}{2\sqrt{x}}
$$

---

## ⚙️ Ejemplo 5: Potencia de trigonométrica

Deriva $f(x) = \sin^3 x = (\sin x)^3$

$$
f'(x) = 3(\sin x)^2 \cdot \cos x = 3\sin^2 x \cos x
$$

---

## ⚙️ Ejemplo 6: Producto

Deriva $g(x) = x^2 \sin x$

$$
g'(x) = 2x \sin x + x^2 \cos x = x(2\sin x + x\cos x)
$$

---

## ⚙️ Ejemplo 7: Secante

Deriva $h(x) = \sec(2x)$

$$
h'(x) = \sec(2x)\tan(2x) \cdot 2 = 2\sec(2x)\tan(2x)
$$

---

## 📖 Mnemotécnicos

**"Co"** en el nombre → signo negativo en la derivada:
- $\cos x \to -\sin x$
- $\cot x \to -\csc^2 x$
- $\csc x \to -\csc x \cot x$

**Sin "co"** → signo positivo:
- $\sin x \to \cos x$
- $\tan x \to \sec^2 x$
- $\sec x \to \sec x \tan x$

---

## 📊 Resumen con cadena

| $f(u)$ donde $u = u(x)$ | $\frac{d}{dx}[f(u)]$ |
|-------------------------|----------------------|
| $\sin u$ | $\cos u \cdot u'$ |
| $\cos u$ | $-\sin u \cdot u'$ |
| $\tan u$ | $\sec^2 u \cdot u'$ |
| $\sec u$ | $\sec u \tan u \cdot u'$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $\sin(5x)$
b) $\cos(x^3)$
c) $\tan(2x + 1)$

<details>
<summary>Ver soluciones</summary>

a) $5\cos(5x)$

b) $-3x^2 \sin(x^3)$

c) $2\sec^2(2x + 1)$
</details>

---

**Ejercicio 2:** Deriva $f(x) = \sin x \cos x$

<details>
<summary>Ver solución</summary>

$f'(x) = \cos x \cdot \cos x + \sin x \cdot (-\sin x)$

$= \cos^2 x - \sin^2 x = \cos 2x$
</details>

---
title: "Derivadas en Coordenadas Polares"
---

# Derivadas en Coordenadas Polares

Las coordenadas polares describen puntos usando distancia y ángulo: $(r, \theta)$. Derivar en polares requiere convertir a la pendiente cartesiana.

---

## 🎯 ¿Qué vas a aprender?

- Repaso de coordenadas polares
- Derivada $\frac{dy}{dx}$ en polares
- Tangentes a curvas polares
- Tangentes horizontales y verticales

---

## 📖 Coordenadas polares

Un punto se describe por:
- $r$ = distancia al origen
- $\theta$ = ángulo desde el eje positivo X

**Conversión a cartesianas:**

$$
x = r\cos\theta, \quad y = r\sin\theta
$$

---

## 📖 Curvas polares

Una curva polar tiene la forma $r = f(\theta)$.

**Ejemplos:**
- Círculo: $r = a$ (constante)
- Cardioide: $r = 1 + \cos\theta$
- Rosa: $r = \cos(n\theta)$
- Espiral: $r = \theta$

---

## 📖 Derivada en polares

Dado $r = f(\theta)$:

$$
x = r\cos\theta = f(\theta)\cos\theta
$$

$$
y = r\sin\theta = f(\theta)\sin\theta
$$

$$
\frac{dx}{d\theta} = \frac{dr}{d\theta}\cos\theta - r\sin\theta
$$

$$
\frac{dy}{d\theta} = \frac{dr}{d\theta}\sin\theta + r\cos\theta
$$

$$\boxed{\frac{dy}{dx} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta}}$$

---

## ⚙️ Ejemplo 1: Cardioide

$r = 1 + \cos\theta$

$$\frac{dr}{d\theta} = -\sin\theta$$

$$\frac{dy}{dx} = \frac{(-\sin\theta)\sin\theta + (1 + \cos\theta)\cos\theta}{(-\sin\theta)\cos\theta - (1 + \cos\theta)\sin\theta}$$

$$= \frac{-\sin^2\theta + \cos\theta + \cos^2\theta}{-\sin\theta\cos\theta - \sin\theta - \sin\theta\cos\theta}$$

$$= \frac{\cos 2\theta + \cos\theta}{-\sin 2\theta - \sin\theta}$$

---

## ⚙️ Ejemplo 2: Círculo

$r = 2$

$$\frac{dr}{d\theta} = 0$$

$$\frac{dy}{dx} = \frac{0 \cdot \sin\theta + 2\cos\theta}{0 \cdot \cos\theta - 2\sin\theta} = \frac{2\cos\theta}{-2\sin\theta} = -\cot\theta$$

---

## ⚙️ Ejemplo 3: Espiral

$r = \theta$

$$\frac{dr}{d\theta} = 1$$

$$\frac{dy}{dx} = \frac{\sin\theta + \theta\cos\theta}{\cos\theta - \theta\sin\theta}$$

---

## 📖 Tangentes especiales

**Tangente horizontal:** $\frac{dy}{d\theta} = 0$ (con $\frac{dx}{d\theta} \neq 0$)

$$
\frac{dr}{d\theta}\sin\theta + r\cos\theta = 0
$$

**Tangente vertical:** $\frac{dx}{d\theta} = 0$ (con $\frac{dy}{d\theta} \neq 0$)

$$
\frac{dr}{d\theta}\cos\theta - r\sin\theta = 0
$$

---

## ⚙️ Ejemplo 4: Tangentes de la cardioide

$r = 1 + \cos\theta$, $\frac{dr}{d\theta} = -\sin\theta$

**Tangente horizontal:**
$$-\sin\theta \cdot \sin\theta + (1 + \cos\theta)\cos\theta = 0$$
$$\cos\theta + \cos^2\theta - \sin^2\theta = 0$$
$$\cos\theta + \cos 2\theta = 0$$

Resolviendo: $\theta = \frac{\pi}{3}, \pi, \frac{5\pi}{3}$

---

## ⚙️ Ejemplo 5: Pendiente en un punto

Para $r = 2\cos\theta$ en $\theta = \frac{\pi}{3}$:

$$r = 2\cos\frac{\pi}{3} = 1$$

$$\frac{dr}{d\theta} = -2\sin\theta = -\sqrt{3}$$

$$\frac{dy}{dx} = \frac{-\sqrt{3} \cdot \frac{\sqrt{3}}{2} + 1 \cdot \frac{1}{2}}{-\sqrt{3} \cdot \frac{1}{2} - 1 \cdot \frac{\sqrt{3}}{2}}$$

$$= \frac{-\frac{3}{2} + \frac{1}{2}}{-\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2}} = \frac{-1}{-\sqrt{3}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$$

---

## 📖 Caso $r = 0$ (paso por el origen)

Cuando $r = 0$ en $\theta = \theta_0$:

La tangente en el origen tiene pendiente $\tan\theta_0$ (la curva es tangente a la línea $\theta = \theta_0$).

---

## 📊 Resumen

| Expresión | Fórmula |
|-----------|---------|
| $\frac{dx}{d\theta}$ | $r'\cos\theta - r\sin\theta$ |
| $\frac{dy}{d\theta}$ | $r'\sin\theta + r\cos\theta$ |
| $\frac{dy}{dx}$ | $\frac{dy/d\theta}{dx/d\theta}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra $\frac{dy}{dx}$ para $r = 1 + \sin\theta$ en $\theta = \frac{\pi}{2}$.

<details>
<summary>Ver solución</summary>

$r = 1 + 1 = 2$, $\frac{dr}{d\theta} = \cos\theta = 0$

$\frac{dy}{dx} = \frac{0 + 2 \cdot 0}{0 - 2 \cdot 1} = \frac{0}{-2} = 0$

(Tangente horizontal)
</details>

---

**Ejercicio 2:** Para $r = \sin\theta$, encuentra los ángulos donde hay tangente vertical.

<details>
<summary>Ver solución</summary>

$\frac{dx}{d\theta} = \cos\theta\cos\theta - \sin\theta\sin\theta = \cos 2\theta = 0$

$\theta = \frac{\pi}{4}, \frac{3\pi}{4}$
</details>

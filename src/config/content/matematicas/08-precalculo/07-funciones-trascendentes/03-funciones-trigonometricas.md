---
title: "Funciones Trigonométricas"
---

# Funciones Trigonométricas

Las funciones trigonométricas relacionan ángulos con razones. Son esenciales para modelar fenómenos periódicos como ondas, rotaciones y ciclos naturales.

---

## 🎯 ¿Qué vas a aprender?

- Las seis funciones trigonométricas
- El círculo unitario y radianes
- Valores exactos de ángulos especiales
- Propiedades fundamentales

---

## 📖 El círculo unitario

Un **círculo unitario** es un círculo de radio 1 centrado en el origen.

Para un ángulo $\theta$ medido desde el eje X positivo:
- El punto en el círculo tiene coordenadas $(\cos\theta, \sin\theta)$

### Radianes vs grados

| Grados | Radianes |
|--------|----------|
| $0°$ | $0$ |
| $30°$ | $\frac{\pi}{6}$ |
| $45°$ | $\frac{\pi}{4}$ |
| $60°$ | $\frac{\pi}{3}$ |
| $90°$ | $\frac{\pi}{2}$ |
| $180°$ | $\pi$ |
| $360°$ | $2\pi$ |

**Conversión:** $\text{radianes} = \text{grados} \times \frac{\pi}{180}$

---

## 📖 Las seis funciones trigonométricas

### Funciones principales

$$\sin\theta = \frac{\text{opuesto}}{\text{hipotenusa}} \quad \cos\theta = \frac{\text{adyacente}}{\text{hipotenusa}} \quad \tan\theta = \frac{\sin\theta}{\cos\theta}$$

### Funciones recíprocas

$$\csc\theta = \frac{1}{\sin\theta} \quad \sec\theta = \frac{1}{\cos\theta} \quad \cot\theta = \frac{1}{\tan\theta}$$

---

## 📖 Valores exactos de ángulos especiales

| $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|----------|-----|-----------------|-----------------|-----------------|-----------------|
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ |
| $\tan\theta$ | $0$ | $\frac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | ∄ |

### 💡 Patrón para memorizar seno

Los valores de $\sin$ en ángulos $0°, 30°, 45°, 60°, 90°$ siguen el patrón:

$$\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2} = 0, \frac{1}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, 1$$

---

## 📖 Identidades fundamentales

### Identidad pitagórica

$$\sin^2\theta + \cos^2\theta = 1$$

### Identidades derivadas

$$1 + \tan^2\theta = \sec^2\theta$$
$$1 + \cot^2\theta = \csc^2\theta$$

---

## 📖 Propiedades de seno y coseno

| Propiedad | $\sin x$ | $\cos x$ |
|-----------|----------|----------|
| **Dominio** | $\mathbb{R}$ | $\mathbb{R}$ |
| **Rango** | $[-1, 1]$ | $[-1, 1]$ |
| **Período** | $2\pi$ | $2\pi$ |
| **Paridad** | Impar | Par |
| **Simetría** | Origen | Eje Y |

---

## ⚙️ Ejemplo 1: Evaluar funciones

Calcula todas las funciones trigonométricas para $\theta = \frac{\pi}{3}$.

$$\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$$
$$\cos\frac{\pi}{3} = \frac{1}{2}$$
$$\tan\frac{\pi}{3} = \frac{\sqrt{3}/2}{1/2} = \sqrt{3}$$
$$\csc\frac{\pi}{3} = \frac{2}{\sqrt{3}} = \frac{2\sqrt{3}}{3}$$
$$\sec\frac{\pi}{3} = 2$$
$$\cot\frac{\pi}{3} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$$

---

## ⚙️ Ejemplo 2: Usando la identidad pitagórica

Si $\sin\theta = \frac{3}{5}$ y $\theta$ está en el primer cuadrante, encuentra $\cos\theta$.

$$\sin^2\theta + \cos^2\theta = 1$$
$$\left(\frac{3}{5}\right)^2 + \cos^2\theta = 1$$
$$\frac{9}{25} + \cos^2\theta = 1$$
$$\cos^2\theta = \frac{16}{25}$$
$$\cos\theta = \frac{4}{5}$$ (positivo en Q1)

---

## 📖 Signos por cuadrante

| Cuadrante | $\sin$ | $\cos$ | $\tan$ |
|-----------|--------|--------|--------|
| I ($0$ a $\frac{\pi}{2}$) | $+$ | $+$ | $+$ |
| II ($\frac{\pi}{2}$ a $\pi$) | $+$ | $-$ | $-$ |
| III ($\pi$ a $\frac{3\pi}{2}$) | $-$ | $-$ | $+$ |
| IV ($\frac{3\pi}{2}$ a $2\pi$) | $-$ | $+$ | $-$ |

### 💡 Mnemotécnico

**"All Students Take Calculus"** (Todos, Seno, Tangente, Coseno son positivos en Q1, Q2, Q3, Q4 respectivamente)

---

## ⚙️ Ejemplo 3: Ángulo de referencia

Evalúa $\cos\frac{5\pi}{6}$.

**Paso 1:** $\frac{5\pi}{6}$ está en el cuadrante II.

**Paso 2:** Ángulo de referencia: $\pi - \frac{5\pi}{6} = \frac{\pi}{6}$

**Paso 3:** $\cos\frac{\pi}{6} = \frac{\sqrt{3}}{2}$

**Paso 4:** En Q2, coseno es negativo.

**Resultado:** $\cos\frac{5\pi}{6} = -\frac{\sqrt{3}}{2}$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Evalúa sin calculadora:

a) $\sin\frac{\pi}{4}$
b) $\cos\frac{2\pi}{3}$
c) $\tan\pi$

<details>
<summary>Ver soluciones</summary>

a) $\frac{\sqrt{2}}{2}$

b) $\frac{2\pi}{3}$ está en Q2, ángulo de referencia $\frac{\pi}{3}$. $\cos\frac{2\pi}{3} = -\frac{1}{2}$

c) $\tan\pi = \frac{\sin\pi}{\cos\pi} = \frac{0}{-1} = 0$
</details>

---

**Ejercicio 2:** Si $\cos\theta = -\frac{5}{13}$ y $\theta$ está en Q3, encuentra $\sin\theta$ y $\tan\theta$.

<details>
<summary>Ver solución</summary>

$\sin^2\theta = 1 - \cos^2\theta = 1 - \frac{25}{169} = \frac{144}{169}$

$\sin\theta = -\frac{12}{13}$ (negativo en Q3)

$\tan\theta = \frac{-12/13}{-5/13} = \frac{12}{5}$ (positivo en Q3)
</details>

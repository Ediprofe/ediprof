# Gráficas de Cotangente, Secante y Cosecante

Las **funciones recíprocas** tienen personalidades dramáticas: nunca tocan el cero, tienen asíntotas, y sus formas son espejos invertidos de sus funciones base.

---

## 🎯 En esta lección aprenderás

- Las gráficas de cot(x), sec(x) y csc(x)
- Por qué tienen asíntotas (y dónde)
- La relación visual con sus funciones base
- Por qué nunca valen entre -1 y 1 (excepto cot)

---

## 📋 Cheat Sheet General

| Función | Definición | Período | Asíntotas en... | Rango |
|---------|------------|---------|-----------------|-------|
| $\cot x$ | $\frac{\cos x}{\sin x}$ | $\pi$ | $k\pi$ | $\mathbb{R}$ |
| $\sec x$ | $\frac{1}{\cos x}$ | $2\pi$ | $\frac{\pi}{2} + k\pi$ | $(-\infty,-1] \cup [1,\infty)$ |
| $\csc x$ | $\frac{1}{\sin x}$ | $2\pi$ | $k\pi$ | $(-\infty,-1] \cup [1,\infty)$ |

---

## 📖 Gráfica de la Cotangente

### Definición

$$
\cot x = \frac{\cos x}{\sin x} = \frac{1}{\tan x}
$$

> 🔄 Es como la tangente "volteada y reflejada".

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = cot(x)</strong>
  </div>

![Gráfica de la cotangente](/images/funciones/trigonometria/cotangente.svg)

</div>

### Características de la cotangente

| Propiedad | Valor |
|-----------|-------|
| Dominio | $x \neq k\pi$ |
| Rango | Todos los reales |
| Período | $\pi$ |
| Asíntotas | Donde $\sin x = 0$ (en $x = k\pi$) |
| Cruza eje X | Donde $\cos x = 0$ (en $x = \frac{\pi}{2} + k\pi$) |
| Comportamiento | **Siempre decreciente** en cada período |

> 💡 **Nota clave:** A diferencia de la tangente que siempre crece, la cotangente siempre decrece.

---

## 📖 Gráfica de la Secante

### Definición

$$
\sec x = \frac{1}{\cos x}
$$

> 🪞 Es el recíproco del coseno.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = sec(x) vs y = cos(x)</strong>
  </div>

![Gráfica de la secante](/images/funciones/trigonometria/secante.svg)

</div>

### Características de la secante

| Propiedad | Valor |
|-----------|-------|
| Dominio | $x \neq \frac{\pi}{2} + k\pi$ |
| Rango | $(-\infty, -1] \cup [1, \infty)$ |
| Período | $2\pi$ |
| Asíntotas | Donde $\cos x = 0$ |
| Mínimo local | $\sec x = 1$ cuando $\cos x = 1$ |
| Máximo local | $\sec x = -1$ cuando $\cos x = -1$ |

> ⚠️ **Nunca vale entre -1 y 1:** Si $|\cos x| \leq 1$, entonces $|\sec x| = \frac{1}{|\cos x|} \geq 1$.

---

## 📖 Gráfica de la Cosecante

### Definición

$$
\csc x = \frac{1}{\sin x}
$$

> 🪞 Es el recíproco del seno.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = csc(x) vs y = sin(x)</strong>
  </div>

![Gráfica de la cosecante](/images/funciones/trigonometria/cosecante.svg)

</div>

### Características de la cosecante

| Propiedad | Valor |
|-----------|-------|
| Dominio | $x \neq k\pi$ |
| Rango | $(-\infty, -1] \cup [1, \infty)$ |
| Período | $2\pi$ |
| Asíntotas | Donde $\sin x = 0$ (en $x = k\pi$) |
| Mínimo local | $\csc x = 1$ cuando $\sin x = 1$ |
| Máximo local | $\csc x = -1$ cuando $\sin x = -1$ |

---

## 📖 Relación entre las funciones

### Regla de oro para las asíntotas

| Función recíproca | Tiene asíntotas donde... |
|-------------------|-------------------------|
| $\sec x = \frac{1}{\cos x}$ | $\cos x = 0$ (ceros del coseno) |
| $\csc x = \frac{1}{\sin x}$ | $\sin x = 0$ (ceros del seno) |
| $\cot x = \frac{1}{\tan x}$ | $\tan x = 0$ → realmente donde $\sin x = 0$ |

> 💡 **Patrón:** Los ceros de la función base se convierten en asíntotas de la función recíproca.

---

## 🧠 Resumen Visual

| Función | Forma de la gráfica | Asíntotas |
|---------|---------------------|-----------|
| $\cot x$ | Curvas "S" descendentes | $x = k\pi$ |
| $\sec x$ | "Parábolas" arriba y abajo | $x = \frac{\pi}{2} + k\pi$ |
| $\csc x$ | "Parábolas" arriba y abajo | $x = k\pi$ |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar asíntotas

¿Dónde están las asíntotas de cada función (entre 0 y $2\pi$)?

1. $\cot x$
2. $\sec x$
3. $\csc x$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **$\cot x$:** en $x = 0, \pi, 2\pi$ (donde $\sin x = 0$)
2. **$\sec x$:** en $x = \frac{\pi}{2}, \frac{3\pi}{2}$ (donde $\cos x = 0$)
3. **$\csc x$:** en $x = 0, \pi, 2\pi$ (donde $\sin x = 0$)

</details>

---

### Ejercicio 2: Valores especiales

Calcula:

1. $\sec 0$
2. $\csc \frac{\pi}{2}$
3. $\cot \frac{\pi}{4}$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sec 0 = \frac{1}{\cos 0} = \frac{1}{1} = 1$
2. $\csc \frac{\pi}{2} = \frac{1}{\sin \frac{\pi}{2}} = \frac{1}{1} = 1$
3. $\cot \frac{\pi}{4} = \frac{1}{\tan \frac{\pi}{4}} = \frac{1}{1} = 1$

¡Los tres valen 1 en estos puntos especiales!

</details>

---

### Ejercicio 3: Rango

¿Es posible que $\sec x = 0.5$?

<details>
<summary><strong>Ver respuesta</strong></summary>

**No**, porque el rango de $\sec x$ es $(-\infty, -1] \cup [1, \infty)$.

El valor 0.5 está entre -1 y 1, así que es **imposible**.

Para que $\sec x = 0.5$, necesitaríamos $\cos x = 2$, lo cual nunca ocurre.

</details>

---

### Ejercicio 4: Verdadero o Falso

1. $\cot x$ tiene período $2\pi$.
2. $\csc x$ nunca vale cero.
3. $\sec x$ tiene las mismas asíntotas que $\tan x$.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** — El período de $\cot x$ es $\pi$
2. **Verdadero** — $\csc x = \frac{1}{\sin x}$ nunca puede ser cero
3. **Verdadero** — Ambas tienen asíntotas donde $\cos x = 0$

</details>

---

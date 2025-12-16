# Gráfica de la Función Tangente

La **tangente** rompe el molde. A diferencia de las ondas suaves del seno y coseno, la tangente tiene "explosiones" hacia el infinito y huecos donde no existe. Es la rebelde de la familia trigonométrica.

---

## 🎯 En esta lección aprenderás

- Por qué la tangente tiene asíntotas (líneas que nunca toca)
- Cómo su período es la mitad que el del seno/coseno
- El comportamiento dramático de la función
- Cómo identificar dónde está definida y dónde no

---

## 📋 Cheat Sheet + Ilustración

| Propiedad | Valor |
|-----------|-------|
| Definición | $\tan x = \frac{\sin x}{\cos x}$ |
| Dominio | $x \neq \frac{\pi}{2} + k\pi$ |
| Rango | $\mathbb{R}$ (todos los reales) |
| Período | $\pi$ (¡la mitad!) |
| Paridad | Impar: $\tan(-x) = -\tan x$ |
| Asíntotas | En $x = \frac{\pi}{2} + k\pi$ |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = tan(x)</strong>
  </div>

![Gráfica de la función tangente](/images/funciones/trigonometria/tangente-principal.svg)

</div>

---

## 📖 ¿Por qué tiene agujeros?

La tangente se define como:

$$
\tan x = \frac{\sin x}{\cos x}
$$

> ⚠️ **Problema:** Cuando el denominador ($\cos x$) vale **cero**, la división explota.

¿Cuándo $\cos x = 0$? En $x = \frac{\pi}{2}, \frac{3\pi}{2}, -\frac{\pi}{2}, \ldots$

En esos puntos, la tangente **no existe** y la gráfica tiene **asíntotas verticales**.

---

## 📖 Anatomía de la tangente

En cada período (entre dos asíntotas consecutivas):

| Evento | Descripción |
|--------|-------------|
| 📉 Viene desde $-\infty$ | Cerca de la asíntota izquierda |
| ↗️ Cruza el eje X | En el centro del período |
| 📈 Se va hacia $+\infty$ | Cerca de la asíntota derecha |

### Puntos clave en el período central $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$:

| $x$ | $x$ (grados) | $\tan x$ |
|-----|--------------|----------|
| $-\frac{\pi}{4}$ | -45° | -1 |
| 0 | 0° | 0 |
| $\frac{\pi}{4}$ | 45° | 1 |

---

## 📖 El período es π (¡la mitad!)

Mientras que seno y coseno se repiten cada $2\pi$, la tangente lo hace cada $\pi$:

$$
\tan(x + \pi) = \tan x
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Período de la tangente: π</strong>
  </div>

![Período de la tangente](/images/funciones/trigonometria/tangente-periodo.svg)

</div>

> 💡 **¿Por qué?** Porque $\sin x$ y $\cos x$ ambos cambian de signo después de $\pi$, así que su cociente queda igual.

---

## 📖 Propiedades matemáticas

### 1. Asíntotas verticales

$$
x = \frac{\pi}{2} + k\pi, \quad k \in \mathbb{Z}
$$

En estos puntos, $\cos x = 0$ y la tangente no existe.

### 2. Interceptos con el eje X

$$
\tan x = 0 \quad \Rightarrow \quad x = k\pi
$$

(Donde $\sin x = 0$)

### 3. Siempre creciente

Dentro de cada período, la tangente es **estrictamente creciente**.

### 4. Sin máximos ni mínimos

La función no tiene valores máximo ni mínimo: va de $-\infty$ a $+\infty$.

---

## 📖 Simetría: función impar

$$
\tan(-x) = -\tan x
$$

> 🔄 La gráfica tiene simetría respecto al origen.

---

## 📖 Comportamiento en los límites

Cuando $x$ se acerca a una asíntota:

$$
\lim_{x \to \frac{\pi}{2}^-} \tan x = +\infty
$$

$$
\lim_{x \to \frac{\pi}{2}^+} \tan x = -\infty
$$

> 📊 La función "salta" de $+\infty$ a $-\infty$ al cruzar la asíntota (por eso hay discontinuidad).

---

## 🧠 Comparación de las tres funciones básicas

| Propiedad | Seno | Coseno | Tangente |
|-----------|------|--------|----------|
| Período | $2\pi$ | $2\pi$ | $\pi$ |
| Rango | $[-1, 1]$ | $[-1, 1]$ | $\mathbb{R}$ |
| Asíntotas | No | No | **Sí** |
| Paridad | Impar | Par | Impar |
| Valor en 0 | 0 | 1 | 0 |
| Valor en 45° | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | **1** |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Valores de la gráfica

Determina el valor de:

1. $\tan 0$
2. $\tan \frac{\pi}{4}$
3. $\tan \pi$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\tan 0 = \frac{\sin 0}{\cos 0} = \frac{0}{1} = 0$
2. $\tan \frac{\pi}{4} = \frac{\sin 45°}{\cos 45°} = \frac{\frac{\sqrt{2}}{2}}{\frac{\sqrt{2}}{2}} = 1$
3. $\tan \pi = \frac{\sin \pi}{\cos \pi} = \frac{0}{-1} = 0$

</details>

---

### Ejercicio 2: Asíntotas

¿En qué valores de $x$ (entre $-\pi$ y $\pi$) hay asíntotas verticales?

<details>
<summary><strong>Ver respuesta</strong></summary>

Las asíntotas están donde $\cos x = 0$:

$$x = -\frac{\pi}{2} \quad \text{y} \quad x = \frac{\pi}{2}$$

</details>

---

### Ejercicio 3: Límites

¿Qué pasa con $\tan x$ cuando $x$ se acerca a $\frac{\pi}{2}$ desde la izquierda?

<details>
<summary><strong>Ver respuesta</strong></summary>

Cuando $x \to \frac{\pi}{2}^-$:
- $\sin x \to 1$ (positivo)
- $\cos x \to 0^+$ (positivo, acercándose a cero)

Por lo tanto:

$$\lim_{x \to \frac{\pi}{2}^-} \tan x = \frac{1}{0^+} = +\infty$$

La función "explota" hacia arriba.

</details>

---

### Ejercicio 4: Verdadero o Falso

1. La tangente tiene período $2\pi$.
2. $\tan \frac{\pi}{2}$ no existe.
3. La tangente es una función acotada.
4. La gráfica cruza el origen.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** — El período es $\pi$
2. **Verdadero** — Hay asíntota en $x = \frac{\pi}{2}$
3. **Falso** — Va de $-\infty$ a $+\infty$
4. **Verdadero** — $\tan 0 = 0$

</details>

---

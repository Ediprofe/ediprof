# Gráfica de la Función Seno

¿Te has preguntado cómo se mueve una ola en el mar, o por qué el sonido viaja en ondas? La función **seno** es la matemática detrás de todo lo que oscila y vibra en el universo.

---

## 🎯 En esta lección aprenderás

- Cómo se ve la gráfica de $y = \sin x$
- Por qué es una "onda" perfecta
- Los puntos clave que definen su forma
- Cómo leer información de la gráfica

---

## 📋 Cheat Sheet + Ilustración

| Propiedad | Valor |
|-----------|-------|
| Dominio | $\mathbb{R}$ (todos los reales) |
| Rango | $[-1, 1]$ |
| Período | $2\pi$ (o 360°) |
| Amplitud | 1 |
| Paridad | Impar: $\sin(-x) = -\sin x$ |
| Cruza el eje X | En $x = k\pi$ ($k$ entero) |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = sin(x)</strong>
  </div>

![Gráfica de la función seno](/images/funciones/trigonometria/seno-principal.svg)

</div>

---

## 📖 La función seno básica

$$
f(x) = \sin x
$$

> 💡 **Dato clave:** El seno convierte un ángulo en un número entre -1 y 1. Es como un traductor entre rotaciones y alturas.

---

## 📖 Anatomía de la onda

La gráfica del seno tiene una forma característica que se repite. Observa cómo **un ciclo completo** ocurre en el intervalo $[0, 2\pi]$:

| Punto | $x$ (rad) | $x$ (grados) | $\sin x$ | ¿Qué pasa? |
|-------|-----------|--------------|----------|------------|
| Inicio | 0 | 0° | 0 | Cruza el eje X |
| Máximo | $\frac{\pi}{2}$ | 90° | 1 | 📈 Punto más alto |
| Mitad | $\pi$ | 180° | 0 | Cruza el eje X de nuevo |
| Mínimo | $\frac{3\pi}{2}$ | 270° | -1 | 📉 Punto más bajo |
| Fin ciclo | $2\pi$ | 360° | 0 | Vuelve al inicio |

---

## 📖 ¿Por qué se llama "onda"?

Piensa en la gráfica como el movimiento de una pelota atada a un resorte:

1. **Sube** desde el equilibrio (0) hasta el máximo (1)
2. **Baja** pasando por el equilibrio hasta el mínimo (-1)
3. **Vuelve** al equilibrio
4. **Repite** eternamente

Este patrón de "arriba-abajo-arriba" es lo que vemos en:
- 🌊 Olas del mar
- 🎵 Ondas de sonido
- 📻 Señales de radio
- ❤️ Latidos del corazón

---

## 📖 Propiedades matemáticas

### 1. Interceptos con el eje X

La función seno vale cero cuando:

$$
\sin x = 0 \quad \Rightarrow \quad x = k\pi \quad (k \in \mathbb{Z})
$$

Es decir, en $x = 0, \pm\pi, \pm 2\pi, \pm 3\pi, \ldots$

### 2. Máximos (donde vale 1)

$$
\sin x = 1 \quad \Rightarrow \quad x = \frac{\pi}{2} + 2k\pi
$$

### 3. Mínimos (donde vale -1)

$$
\sin x = -1 \quad \Rightarrow \quad x = \frac{3\pi}{2} + 2k\pi
$$

---

## 📖 Simetría: función impar

Una propiedad hermosa del seno es que es una **función impar**:

$$
\sin(-x) = -\sin x
$$

> 🔄 **¿Qué significa?** Si reflejas la gráfica respecto al origen (rotación de 180°), obtienes la misma gráfica.

**Ejemplo:** $\sin(-30°) = -\sin(30°) = -0.5$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Simetría del seno (función impar)</strong>
  </div>

![Simetría del seno - función impar](/images/funciones/trigonometria/seno-simetria.svg)

</div>

---

## 📖 Intervalos de crecimiento y decrecimiento

### ↗️ Creciente

En los intervalos donde la onda "sube":

$$
\left[-\frac{\pi}{2} + 2k\pi, \frac{\pi}{2} + 2k\pi\right]
$$

### ↘️ Decreciente

En los intervalos donde la onda "baja":

$$
\left[\frac{\pi}{2} + 2k\pi, \frac{3\pi}{2} + 2k\pi\right]
$$

---

## 🧠 Tip para recordar

> **"El seno comienza en CERO, sube al UNO, baja al menos UNO, y regresa."**

Memoriza: **0 → 1 → 0 → -1 → 0** (en un ciclo completo de $2\pi$)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Lectura de la gráfica

Observando la gráfica, responde:

1. ¿Cuál es $\sin 0$?
2. ¿En qué punto la función alcanza su máximo en $[0, 2\pi]$?
3. ¿En qué valor de $x$ la función vale -1 por primera vez (para $x > 0$)?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sin 0 = 0$ (la onda empieza en el origen)
2. En $x = \frac{\pi}{2}$ (90°), donde $\sin x = 1$
3. En $x = \frac{3\pi}{2}$ (270°)

</details>

---

### Ejercicio 2: Interceptos

¿En qué valores de $x$ (entre 0 y $4\pi$) cruza $\sin x$ el eje X?

<details>
<summary><strong>Ver respuesta</strong></summary>

El seno cruza el eje X cuando $\sin x = 0$, es decir, en múltiplos de $\pi$:

$$x = 0, \pi, 2\pi, 3\pi, 4\pi$$

Son **5 puntos** en ese intervalo.

</details>

---

### Ejercicio 3: Desigualdad

¿Para qué valores de $x$ (en $[0, 2\pi]$) es $\sin x > 0$?

<details>
<summary><strong>Ver respuesta</strong></summary>

El seno es positivo (la onda está "arriba" del eje X) cuando:

$$x \in (0, \pi)$$

Es decir, entre 0° y 180° (sin incluir los extremos donde vale 0).

</details>

---

### Ejercicio 4: Simetría

Si $\sin 45° = \frac{\sqrt{2}}{2}$, ¿cuánto vale $\sin(-45°)$?

<details>
<summary><strong>Ver respuesta</strong></summary>

Por la propiedad de función impar:

$$\sin(-45°) = -\sin(45°) = -\frac{\sqrt{2}}{2}$$

</details>

---

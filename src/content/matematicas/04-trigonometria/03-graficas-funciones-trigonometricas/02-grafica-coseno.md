# Gráfica de la Función Coseno

El **coseno** es el "hermano gemelo" del seno. Su gráfica tiene exactamente la misma forma de onda, pero con un pequeño giro: ¡empieza en el máximo en lugar de en cero!

---

## 🎯 En esta lección aprenderás

- Cómo se ve la gráfica de $y = \cos x$
- La relación visual entre seno y coseno
- Por qué el coseno es una función "par"
- Cómo identificar máximos, mínimos y ceros

---

## 📋 Cheat Sheet + Ilustración

| Propiedad | Valor |
|-----------|-------|
| Dominio | $\mathbb{R}$ (todos los reales) |
| Rango | $[-1, 1]$ |
| Período | $2\pi$ (o 360°) |
| Amplitud | 1 |
| Paridad | Par: $\cos(-x) = \cos x$ |
| Cruza el eje X | En $x = \frac{\pi}{2} + k\pi$ |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = cos(x)</strong>
  </div>

![Gráfica de la función coseno](/images/funciones/trigonometria/coseno-principal.svg)

</div>

---

## 📖 La función coseno básica

$$
f(x) = \cos x
$$

> 💡 **Diferencia clave con el seno:** El coseno empieza en su valor máximo (1) cuando $x = 0$, mientras que el seno empieza en 0.

---

## 📖 Anatomía de la onda coseno

| Punto | $x$ (rad) | $x$ (grados) | $\cos x$ | ¿Qué pasa? |
|-------|-----------|--------------|----------|------------|
| Inicio | 0 | 0° | 1 | 📈 Máximo |
| Primer cero | $\frac{\pi}{2}$ | 90° | 0 | Cruza eje X bajando |
| Mínimo | $\pi$ | 180° | -1 | 📉 Punto más bajo |
| Segundo cero | $\frac{3\pi}{2}$ | 270° | 0 | Cruza eje X subiendo |
| Fin ciclo | $2\pi$ | 360° | 1 | 📈 Vuelve al máximo |

---

## 📖 Seno vs Coseno: ¡Son la misma onda desplazada!

Esta es una de las relaciones más bellas de la trigonometría:

$$
\cos x = \sin\left(x + \frac{\pi}{2}\right)
$$

> 🔑 **Traducción:** El coseno es el seno "adelantado" 90° (o $\frac{\pi}{2}$ radianes).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Comparación: Seno vs Coseno</strong>
  </div>

![Comparación sin(x) vs cos(x)](/images/funciones/trigonometria/seno-vs-coseno.svg)

</div>

---

## 📖 Simetría: función par

A diferencia del seno, el coseno es una **función par**:

$$
\cos(-x) = \cos x
$$

> 🪞 **¿Qué significa?** La gráfica es simétrica respecto al eje Y (como mirarse en un espejo vertical).

**Ejemplo:** $\cos(-60°) = \cos(60°) = 0.5$

---

## 📖 Tabla comparativa completa

| Propiedad | Seno | Coseno |
|-----------|------|--------|
| Valor en $x = 0$ | 0 | **1** |
| Paridad | Impar | **Par** |
| Primer máximo | $\frac{\pi}{2}$ | **0** |
| Primer cero positivo | 0 | **$\frac{\pi}{2}$** |
| Simetría | Respecto al origen | **Respecto al eje Y** |
| Fórmula equivalente | $\sin x = \cos(x - \frac{\pi}{2})$ | $\cos x = \sin(x + \frac{\pi}{2})$ |

---

## 📖 Propiedades matemáticas

### 1. Interceptos con el eje X

$$
\cos x = 0 \quad \Rightarrow \quad x = \frac{\pi}{2} + k\pi \quad (k \in \mathbb{Z})
$$

Es decir, en $x = \frac{\pi}{2}, \frac{3\pi}{2}, -\frac{\pi}{2}, \ldots$

### 2. Máximos (donde vale 1)

$$
\cos x = 1 \quad \Rightarrow \quad x = 2k\pi
$$

### 3. Mínimos (donde vale -1)

$$
\cos x = -1 \quad \Rightarrow \quad x = \pi + 2k\pi
$$

---

## 🧠 Tip para recordar

> **"El coseno empieza en UNO, baja a CERO, llega al menos UNO, sube a CERO, y regresa al UNO."**

Memoriza: **1 → 0 → -1 → 0 → 1** (en un ciclo de $2\pi$)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Lectura de la gráfica

1. ¿Cuál es $\cos 0$?
2. ¿En qué punto $x$ (en $[0, 2\pi]$) la función vale 0 por primera vez?
3. ¿Dónde alcanza su mínimo en $[0, 2\pi]$?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\cos 0 = 1$ (empieza en el máximo)
2. En $x = \frac{\pi}{2}$ (90°)
3. En $x = \pi$ (180°), donde $\cos \pi = -1$

</details>

---

### Ejercicio 2: Interceptos

¿En qué valores de $x$ (entre $-\pi$ y $\pi$) cruza $\cos x$ el eje X?

<details>
<summary><strong>Ver respuesta</strong></summary>

El coseno vale 0 cuando $x = \frac{\pi}{2} + k\pi$:

$$x = -\frac{\pi}{2} \quad \text{y} \quad x = \frac{\pi}{2}$$

</details>

---

### Ejercicio 3: Desigualdad

¿Para qué valores de $x$ (en $[0, 2\pi]$) es $\cos x < 0$?

<details>
<summary><strong>Ver respuesta</strong></summary>

El coseno es negativo (la onda está "debajo" del eje X) cuando:

$$x \in \left(\frac{\pi}{2}, \frac{3\pi}{2}\right)$$

Es decir, entre 90° y 270°.

</details>

---

### Ejercicio 4: Usando la simetría

Si $\cos 30° = \frac{\sqrt{3}}{2}$, ¿cuánto vale $\cos(-30°)$?

<details>
<summary><strong>Ver respuesta</strong></summary>

Como el coseno es función **par**:

$$\cos(-30°) = \cos(30°) = \frac{\sqrt{3}}{2}$$

¡Los valores son iguales!

</details>

---

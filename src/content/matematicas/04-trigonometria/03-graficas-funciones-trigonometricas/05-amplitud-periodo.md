# Amplitud y Período

¿Qué pasa cuando pones un número delante del seno? ¿Y si multiplicas la $x$? Los parámetros **A** y **B** son como controles de volumen y velocidad de la onda trigonométrica.

---

## 🎯 En esta lección aprenderás

- Cómo **A** estira o comprime verticalmente (amplitud)
- Cómo **B** estira o comprime horizontalmente (período)
- Las fórmulas para calcular amplitud y período
- A identificar estos valores en cualquier función

---

## 📋 Cheat Sheet

| Parámetro | Fórmula | Efecto |
|-----------|---------|--------|
| **Amplitud** | $\|A\|$ | Altura de la onda |
| **Período** | $\frac{2\pi}{\|B\|}$ | Longitud de un ciclo |

Para la función generalizada:

$$
y = A \sin(Bx) \quad \text{o} \quad y = A \cos(Bx)
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Efecto de la amplitud: A = 1, 2, 0.5</strong>
  </div>

![Efecto de la amplitud](/images/funciones/trigonometria/amplitud-comparacion.svg)

</div>

---

## 📖 Amplitud: el "volumen" de la onda

### Definición

> **Amplitud** = distancia desde el eje central hasta el máximo (o hasta el mínimo).

$$
\text{Amplitud} = |A|
$$

### ¿Qué hace A?

| Valor de A | Efecto visual | Rango resultante |
|------------|---------------|------------------|
| $A > 1$ | Estira verticalmente (onda más alta) | $[-A, A]$ |
| $0 < A < 1$ | Comprime verticalmente (onda más baja) | $[-A, A]$ |
| $A < 0$ | Refleja respecto al eje X (onda invertida) | $[A, -A]$ |

### Ejemplos concretos

| Función | Amplitud | Rango |
|---------|----------|-------|
| $\sin x$ | 1 | $[-1, 1]$ |
| $2\sin x$ | 2 | $[-2, 2]$ |
| $0.5\sin x$ | 0.5 | $[-0.5, 0.5]$ |
| $-3\cos x$ | 3 | $[-3, 3]$ |

> 💡 **Nota:** El signo negativo invierte la onda pero NO cambia la amplitud.

---

## 📖 Período: la "longitud" de un ciclo

### Definición

> **Período** = distancia horizontal que recorre la función antes de repetirse.

$$
\text{Período} = \frac{2\pi}{|B|}
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Efecto del período: B = 1, 2, 0.5</strong>
  </div>

![Efecto del período](/images/funciones/trigonometria/periodo-comparacion.svg)

</div>

### ¿Qué hace B?

| Valor de B | Efecto | Período resultante |
|------------|--------|-------------------|
| $B > 1$ | Comprime horizontalmente (más ciclos) | $< 2\pi$ |
| $0 < B < 1$ | Estira horizontalmente (menos ciclos) | $> 2\pi$ |
| $B < 0$ | Refleja respecto al eje Y | $\frac{2\pi}{\|B\|}$ |

### Ejemplos concretos

| Función | B | Período |
|---------|---|---------|
| $\sin x$ | 1 | $2\pi$ |
| $\sin 2x$ | 2 | $\pi$ |
| $\sin \frac{x}{2}$ | 0.5 | $4\pi$ |
| $\cos 3x$ | 3 | $\frac{2\pi}{3}$ |

---

## 📖 Ejemplo completo

Analicemos $y = 3\sin(2x)$:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">y = 3sin(2x): Amplitud 3, Período π</strong>
  </div>

![Ejemplo: y = 3sin(2x)](/images/funciones/trigonometria/amplitud-periodo-ejemplo.svg)

</div>

### Análisis paso a paso

| Parámetro | Valor | Cálculo |
|-----------|-------|---------|
| A | 3 | Amplitud = $\|3\| = 3$ |
| B | 2 | Período = $\frac{2\pi}{2} = \pi$ |
| Rango | $[-3, 3]$ | |

---

## 📖 Para tangente y cotangente

Las funciones tangente y cotangente tienen período base $\pi$ (no $2\pi$):

$$
\text{Período de } \tan(Bx) = \frac{\pi}{|B|}
$$

| Función | Período |
|---------|---------|
| $\tan x$ | $\pi$ |
| $\tan 2x$ | $\frac{\pi}{2}$ |
| $\tan \frac{x}{3}$ | $3\pi$ |

> ⚠️ **No confundir:** $\tan$ y $\cot$ usan $\frac{\pi}{|B|}$, mientras que $\sin$, $\cos$, $\sec$ y $\csc$ usan $\frac{2\pi}{|B|}$.

---

## 📖 Frecuencia

La **frecuencia** es el recíproco del período:

$$
\text{Frecuencia} = \frac{1}{\text{Período}} = \frac{|B|}{2\pi}
$$

> 🔊 Indica cuántos ciclos completos hay en el intervalo $[0, 2\pi]$.

| Función | Frecuencia |
|---------|------------|
| $\sin x$ | $\frac{1}{2\pi}$ (≈ 0.16 ciclos por radián) |
| $\sin 2x$ | $\frac{2}{2\pi} = \frac{1}{\pi}$ (≈ 0.32 ciclos por radián) |

---

## 🧠 Receta rápida

Para $y = A\sin(Bx)$ o $y = A\cos(Bx)$:

1. **Amplitud** = $|A|$
2. **Período** = $\frac{2\pi}{|B|}$
3. **Rango** = $[-|A|, |A|]$
4. **Frecuencia** = $\frac{|B|}{2\pi}$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar amplitud

¿Cuál es la amplitud de cada función?

1. $y = 4\sin x$
2. $y = -2\cos x$
3. $y = 0.3\sin x$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Amplitud = $|4| = 4$
2. Amplitud = $|-2| = 2$ (el signo negativo no afecta)
3. Amplitud = $|0.3| = 0.3$

</details>

---

### Ejercicio 2: Calcular período

¿Cuál es el período de cada función?

1. $y = \sin 3x$
2. $y = \cos \frac{x}{4}$
3. $y = \tan 2x$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Período = $\frac{2\pi}{3}$
2. Período = $\frac{2\pi}{1/4} = 8\pi$
3. Período = $\frac{\pi}{2}$ (¡tangente usa $\frac{\pi}{|B|}$!)

</details>

---

### Ejercicio 3: Escribir función

Escribe una función seno con:

1. Amplitud 5, período $2\pi$
2. Amplitud 2, período $\pi$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $y = 5\sin x$ 
   - (A = 5, B = 1 da período $\frac{2\pi}{1} = 2\pi$)

2. $y = 2\sin(2x)$ 
   - (A = 2, B = 2 da período $\frac{2\pi}{2} = \pi$)

</details>

---

### Ejercicio 4: Análisis completo

Para $y = 4\cos(3x)$, determina:

1. Amplitud
2. Período
3. Rango

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Amplitud = $|4| = 4$
2. Período = $\frac{2\pi}{3}$
3. Rango = $[-4, 4]$

</details>

---

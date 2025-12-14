# Definición de Funciones Trigonométricas

Las **funciones trigonométricas** extienden las razones del triángulo rectángulo a **cualquier ángulo real**, usando el círculo unitario.

---

## 📖 De razones a funciones

En el triángulo rectángulo, las razones trigonométricas solo se definían para ángulos agudos (0° a 90°).

Con el círculo unitario, podemos definir **funciones** que aceptan cualquier ángulo como entrada.

---

## 📖 Definiciones mediante el círculo unitario

Para un ángulo $\theta$, sea $P = (x, y)$ el punto correspondiente en el círculo unitario.

| Función | Definición |
|---------|------------|
| $\sin\theta$ | $y$ (coordenada vertical) |
| $\cos\theta$ | $x$ (coordenada horizontal) |
| $\tan\theta$ | $\frac{y}{x}$ (si $x \neq 0$) |
| $\csc\theta$ | $\frac{1}{y}$ (si $y \neq 0$) |
| $\sec\theta$ | $\frac{1}{x}$ (si $x \neq 0$) |
| $\cot\theta$ | $\frac{x}{y}$ (si $y \neq 0$) |

---

## 📖 Dominio y rango

### Seno y Coseno

| Función | Dominio | Rango |
|---------|---------|-------|
| $\sin\theta$ | Todos los reales | $[-1, 1]$ |
| $\cos\theta$ | Todos los reales | $[-1, 1]$ |

### Tangente y Cotangente

| Función | Dominio | Rango |
|---------|---------|-------|
| $\tan\theta$ | $\theta \neq 90° + k \cdot 180°$ | Todos los reales |
| $\cot\theta$ | $\theta \neq k \cdot 180°$ | Todos los reales |

### Secante y Cosecante

| Función | Dominio | Rango |
|---------|---------|-------|
| $\sec\theta$ | $\theta \neq 90° + k \cdot 180°$ | $(-\infty, -1] \cup [1, \infty)$ |
| $\csc\theta$ | $\theta \neq k \cdot 180°$ | $(-\infty, -1] \cup [1, \infty)$ |

---

## 📖 Periodicidad

Las funciones trigonométricas son **periódicas**: se repiten después de cierto intervalo.

| Función | Período |
|---------|---------|
| $\sin\theta$ | $360°$ (o $2\pi$) |
| $\cos\theta$ | $360°$ (o $2\pi$) |
| $\tan\theta$ | $180°$ (o $\pi$) |
| $\cot\theta$ | $180°$ (o $\pi$) |
| $\sec\theta$ | $360°$ (o $2\pi$) |
| $\csc\theta$ | $360°$ (o $2\pi$) |

Esto significa:

$$
\sin(\theta + 360°) = \sin\theta
$$

---

## 📖 Paridad de las funciones

### Funciones pares

$f(-\theta) = f(\theta)$

- **Coseno**: $\cos(-\theta) = \cos\theta$
- **Secante**: $\sec(-\theta) = \sec\theta$

### Funciones impares

$f(-\theta) = -f(\theta)$

- **Seno**: $\sin(-\theta) = -\sin\theta$
- **Tangente**: $\tan(-\theta) = -\tan\theta$
- **Cotangente**: $\cot(-\theta) = -\cot\theta$
- **Cosecante**: $\csc(-\theta) = -\csc\theta$

---

## 📖 Relaciones fundamentales

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}
$$

$$
\cot\theta = \frac{\cos\theta}{\sin\theta}
$$

$$
\sec\theta = \frac{1}{\cos\theta}
$$

$$
\csc\theta = \frac{1}{\sin\theta}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Dominio

¿Para qué ángulos $\tan\theta$ no está definida?

<details>
<summary><strong>Ver respuesta</strong></summary>

Cuando $\cos\theta = 0$, es decir, en $90°$, $270°$, $-90°$, etc.

En general: $\theta = 90° + k \cdot 180°$ donde $k$ es entero.

</details>

---

### Ejercicio 2: Periodicidad

Si $\sin 30° = 0.5$, ¿cuánto vale $\sin 390°$?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\sin 390° = \sin(30° + 360°) = \sin 30° = 0.5
$$

</details>

---

### Ejercicio 3: Paridad

Sabiendo que $\cos 60° = 0.5$, ¿cuánto vale $\cos(-60°)$?

<details>
<summary><strong>Ver respuesta</strong></summary>

Como el coseno es función par:

$$
\cos(-60°) = \cos(60°) = 0.5
$$

</details>

---

### Ejercicio 4: Función impar

Si $\sin 45° = \frac{\sqrt{2}}{2}$, ¿cuánto vale $\sin(-45°)$?

<details>
<summary><strong>Ver respuesta</strong></summary>

Como el seno es función impar:

$$
\sin(-45°) = -\sin(45°) = -\frac{\sqrt{2}}{2}
$$

</details>

---

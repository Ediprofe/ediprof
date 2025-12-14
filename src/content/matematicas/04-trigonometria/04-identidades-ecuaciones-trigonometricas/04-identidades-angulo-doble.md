# Identidades del Ángulo Doble

Las **identidades del ángulo doble** expresan las funciones de $2\theta$ en términos de funciones de $\theta$.

---

## 📖 Seno del ángulo doble

$$
\sin 2\theta = 2\sin\theta\cos\theta
$$

### Derivación

Usando $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$ con $\alpha = \beta = \theta$:

$$
\sin(\theta + \theta) = \sin\theta\cos\theta + \cos\theta\sin\theta = 2\sin\theta\cos\theta
$$

---

## 📖 Coseno del ángulo doble

El coseno del ángulo doble tiene **tres formas equivalentes**:

### Forma 1

$$
\cos 2\theta = \cos^2\theta - \sin^2\theta
$$

### Forma 2 (solo en términos de coseno)

$$
\cos 2\theta = 2\cos^2\theta - 1
$$

### Forma 3 (solo en términos de seno)

$$
\cos 2\theta = 1 - 2\sin^2\theta
$$

### ¿Cómo pasar de una a otra?

Usando $\sin^2\theta + \cos^2\theta = 1$:

$$
\cos^2\theta - \sin^2\theta = (1 - \sin^2\theta) - \sin^2\theta = 1 - 2\sin^2\theta
$$

$$
\cos^2\theta - \sin^2\theta = \cos^2\theta - (1 - \cos^2\theta) = 2\cos^2\theta - 1
$$

---

## 📖 Tangente del ángulo doble

$$
\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta}
$$

---

## 📖 Resumen

| Función | Identidad del ángulo doble |
|---------|----------------------------|
| $\sin 2\theta$ | $2\sin\theta\cos\theta$ |
| $\cos 2\theta$ | $\cos^2\theta - \sin^2\theta$ |
| $\cos 2\theta$ | $2\cos^2\theta - 1$ |
| $\cos 2\theta$ | $1 - 2\sin^2\theta$ |
| $\tan 2\theta$ | $\frac{2\tan\theta}{1 - \tan^2\theta}$ |

---

## 📖 Ejemplo 1

Si $\sin\theta = \frac{3}{5}$ y $\cos\theta = \frac{4}{5}$, encuentra $\sin 2\theta$ y $\cos 2\theta$.

$$
\sin 2\theta = 2 \cdot \frac{3}{5} \cdot \frac{4}{5} = \frac{24}{25}
$$

$$
\cos 2\theta = \left(\frac{4}{5}\right)^2 - \left(\frac{3}{5}\right)^2 = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}
$$

---

## 📖 Ejemplo 2: Calcular $\sin 60°$

Usando $\sin 60° = \sin(2 \cdot 30°) = 2\sin 30°\cos 30°$:

$$
= 2 \cdot \frac{1}{2} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{2} \quad ✓
$$

---

## 📖 Identidades derivadas

Despejando de las formas de $\cos 2\theta$:

### Fórmulas de reducción de potencia

$$
\sin^2\theta = \frac{1 - \cos 2\theta}{2}
$$

$$
\cos^2\theta = \frac{1 + \cos 2\theta}{2}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular ángulo doble

Si $\sin\theta = \frac{5}{13}$ y $\cos\theta = \frac{12}{13}$, calcula:

1. $\sin 2\theta$
2. $\cos 2\theta$
3. $\tan 2\theta$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sin 2\theta = 2 \cdot \frac{5}{13} \cdot \frac{12}{13} = \frac{120}{169}$

2. $\cos 2\theta = \left(\frac{12}{13}\right)^2 - \left(\frac{5}{13}\right)^2 = \frac{144 - 25}{169} = \frac{119}{169}$

3. $\tan 2\theta = \frac{\sin 2\theta}{\cos 2\theta} = \frac{120}{119}$

</details>

---

### Ejercicio 2: Simplificar

Simplifica: $\sin\theta\cos\theta$

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\sin\theta\cos\theta = \frac{1}{2}(2\sin\theta\cos\theta) = \frac{1}{2}\sin 2\theta
$$

</details>

---

### Ejercicio 3: Valores exactos

Calcula $\cos 120°$ usando la identidad del ángulo doble con $\theta = 60°$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\cos 120° = \cos(2 \cdot 60°) = 2\cos^2 60° - 1
$$

$$
= 2\left(\frac{1}{2}\right)^2 - 1 = 2 \cdot \frac{1}{4} - 1 = \frac{1}{2} - 1 = -\frac{1}{2}
$$

</details>

---

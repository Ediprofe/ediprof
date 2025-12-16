# Cofunciones

Dos funciones trigonométricas son **cofunciones** si el valor de una para un ángulo es igual al valor de la otra para el ángulo complementario.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Cofunciones en el triángulo rectángulo</strong>
  </div>

![Cofunciones](/images/trigonometria/circulo-unitario/cofunciones.svg)

</div>

---

## 📖 Definición de cofunciones

> **Definición:** Dos funciones son cofunciones si:
> $$f(\theta) = g(90° - \theta)$$

El prefijo "co-" en coseno, cotangente y cosecante viene de "complemento".

---

## 📖 Pares de cofunciones

| Función | Cofunción |
|---------|-----------|
| Seno | Coseno |
| Tangente | Cotangente |
| Secante | Cosecante |

---

## 📖 Identidades de cofunciones

### Seno y Coseno

$$
\sin\theta = \cos(90° - \theta)
$$

$$
\cos\theta = \sin(90° - \theta)
$$

### Tangente y Cotangente

$$
\tan\theta = \cot(90° - \theta)
$$

$$
\cot\theta = \tan(90° - \theta)
$$

### Secante y Cosecante

$$
\sec\theta = \csc(90° - \theta)
$$

$$
\csc\theta = \sec(90° - \theta)
$$

---

## 📖 ¿Por qué funcionan?

En un triángulo rectángulo con ángulos agudos $\theta$ y $(90° - \theta)$:

- El cateto opuesto a $\theta$ es el **adyacente** a $(90° - \theta)$
- El cateto adyacente a $\theta$ es el **opuesto** a $(90° - \theta)$

Por lo tanto:

$$
\sin\theta = \frac{O}{H} = \frac{\text{adyacente a } (90°-\theta)}{H} = \cos(90° - \theta)
$$

---

## 📖 Ejemplos

### Ejemplo 1

$$
\sin 30° = \cos(90° - 30°) = \cos 60°
$$

Verificación: $\sin 30° = \frac{1}{2}$ y $\cos 60° = \frac{1}{2}$ ✓

### Ejemplo 2

$$
\tan 20° = \cot(90° - 20°) = \cot 70°
$$

### Ejemplo 3

$$
\cos 75° = \sin(90° - 75°) = \sin 15°
$$

---

## 📖 En radianes

$$
\sin\theta = \cos\left(\frac{\pi}{2} - \theta\right)
$$

$$
\cos\theta = \sin\left(\frac{\pi}{2} - \theta\right)
$$

$$
\tan\theta = \cot\left(\frac{\pi}{2} - \theta\right)
$$

---

## 📖 Aplicaciones

### Simplificar expresiones

Las identidades de cofunciones permiten simplificar expresiones trigonométricas.

### Ejemplo

Simplificar: $\sin 25° + \cos 65°$

$$
\cos 65° = \sin(90° - 65°) = \sin 25°
$$

Por lo tanto:

$$
\sin 25° + \cos 65° = \sin 25° + \sin 25° = 2\sin 25°
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Aplicar cofunciones

Expresa como cofunción:

1. $\sin 40°$
2. $\tan 55°$
3. $\sec 70°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sin 40° = \cos(90° - 40°) = \cos 50°$
2. $\tan 55° = \cot(90° - 55°) = \cot 35°$
3. $\sec 70° = \csc(90° - 70°) = \csc 20°$

</details>

---

### Ejercicio 2: Verificar igualdades

¿Son iguales?

1. $\sin 15°$ y $\cos 75°$
2. $\tan 30°$ y $\cot 30°$
3. $\cos 45°$ y $\sin 45°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí**, $\sin 15° = \cos(90° - 15°) = \cos 75°$
2. **No**, deberían compararse $\tan 30°$ con $\cot 60°$
3. **Sí**, $\cos 45° = \sin(90° - 45°) = \sin 45°$

</details>

---

### Ejercicio 3: Simplificar

Simplifica:

1. $\sin 35° - \cos 55°$
2. $\tan 22° \cdot \cot 68°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\cos 55° = \sin 35°$, entonces $\sin 35° - \sin 35° = 0$
2. $\cot 68° = \tan(90° - 68°) = \tan 22°$, entonces $\tan 22° \cdot \tan 22° = \tan^2 22°$

</details>

---

### Ejercicio 4: Encontrar el ángulo

Si $\sin\theta = \cos 40°$, ¿cuánto vale $\theta$?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\sin\theta = \cos 40° = \sin(90° - 40°) = \sin 50°
$$

Por lo tanto, $\theta = 50°$ (para el ángulo agudo)

</details>

---

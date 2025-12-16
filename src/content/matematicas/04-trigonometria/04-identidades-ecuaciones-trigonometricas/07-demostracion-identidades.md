# Demostración de Identidades

**Demostrar una identidad** significa mostrar que ambos lados de la ecuación son equivalentes para todos los valores donde están definidos.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Estrategias para Demostrar Identidades</strong>
  </div>

![Estrategias de demostración](/images/trigonometria/identidades/estrategias-demostracion.svg)

</div>

---

## 📖 Estrategias de demostración

### Estrategia 1: Trabajar un solo lado

Transforma **un lado** hasta que sea igual al otro. Generalmente se trabaja el lado más complicado.

### Estrategia 2: Trabajar ambos lados

Transforma **ambos lados** hasta que lleguen a una expresión común.

### Estrategia 3: Convertir todo a seno y coseno

Expresar todas las funciones en términos de $\sin$ y $\cos$.

---

## 📖 Reglas importantes

1. **Nunca** cruces el signo igual (no hagas operaciones en ambos lados a la vez)
2. Los pasos deben ser **reversibles**
3. Trabaja un lado a la vez, manteniendo el otro intacto

---

## 📖 Ejemplo 1

Demuestra: $\tan\theta + \cot\theta = \sec\theta\csc\theta$

### Solución (lado izquierdo)

$$
\tan\theta + \cot\theta = \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta}
$$

$$
= \frac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta}
$$

$$
= \frac{1}{\sin\theta\cos\theta}
$$

$$
= \frac{1}{\sin\theta} \cdot \frac{1}{\cos\theta} = \csc\theta\sec\theta \quad ✓
$$

---

## 📖 Ejemplo 2

Demuestra: $\frac{1 - \cos\theta}{\sin\theta} = \frac{\sin\theta}{1 + \cos\theta}$

### Solución

Multiplicamos el numerador y denominador del lado izquierdo por $(1 + \cos\theta)$:

$$
\frac{1 - \cos\theta}{\sin\theta} \cdot \frac{1 + \cos\theta}{1 + \cos\theta}
$$

$$
= \frac{(1 - \cos\theta)(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)}
$$

$$
= \frac{1 - \cos^2\theta}{\sin\theta(1 + \cos\theta)}
$$

$$
= \frac{\sin^2\theta}{\sin\theta(1 + \cos\theta)}
$$

$$
= \frac{\sin\theta}{1 + \cos\theta} \quad ✓
$$

---

## 📖 Ejemplo 3

Demuestra: $\sec^2\theta - 1 = \tan^2\theta$

### Solución

Usando la identidad pitagórica $1 + \tan^2\theta = \sec^2\theta$:

$$
\sec^2\theta - 1 = \tan^2\theta \quad ✓
$$

(Es directamente una identidad pitagórica despejada)

---

## 📖 Consejos prácticos

| Situación | Técnica recomendada |
|-----------|---------------------|
| Hay fracciones | Buscar denominador común |
| Hay $\tan$, $\cot$, $\sec$, $\csc$ | Convertir a $\sin$ y $\cos$ |
| Hay $1 \pm \sin$ o $1 \pm \cos$ | Multiplicar por el conjugado |
| Hay potencias pares | Usar identidades pitagóricas |

---

## 📝 Ejercicios de práctica

### Ejercicio 1

Demuestra: $\sin\theta\sec\theta = \tan\theta$

<details>
<summary><strong>Ver demostración</strong></summary>

$$
\sin\theta\sec\theta = \sin\theta \cdot \frac{1}{\cos\theta} = \frac{\sin\theta}{\cos\theta} = \tan\theta \quad ✓
$$

</details>

---

### Ejercicio 2

Demuestra: $\frac{\cos\theta}{1 - \sin\theta} = \sec\theta + \tan\theta$

<details>
<summary><strong>Ver demostración</strong></summary>

Multiplicamos por el conjugado:

$$
\frac{\cos\theta}{1 - \sin\theta} \cdot \frac{1 + \sin\theta}{1 + \sin\theta} = \frac{\cos\theta(1 + \sin\theta)}{1 - \sin^2\theta}
$$

$$
= \frac{\cos\theta(1 + \sin\theta)}{\cos^2\theta} = \frac{1 + \sin\theta}{\cos\theta}
$$

$$
= \frac{1}{\cos\theta} + \frac{\sin\theta}{\cos\theta} = \sec\theta + \tan\theta \quad ✓
$$

</details>

---

### Ejercicio 3

Demuestra: $\sin^4\theta - \cos^4\theta = \sin^2\theta - \cos^2\theta$

<details>
<summary><strong>Ver demostración</strong></summary>

Factorizando como diferencia de cuadrados:

$$
\sin^4\theta - \cos^4\theta = (\sin^2\theta)^2 - (\cos^2\theta)^2
$$

$$
= (\sin^2\theta + \cos^2\theta)(\sin^2\theta - \cos^2\theta)
$$

$$
= 1 \cdot (\sin^2\theta - \cos^2\theta) = \sin^2\theta - \cos^2\theta \quad ✓
$$

</details>

---

### Ejercicio 4

Demuestra: $\cot^2\theta - \cos^2\theta = \cot^2\theta\cos^2\theta$

<details>
<summary><strong>Ver demostración</strong></summary>

$$
\cot^2\theta - \cos^2\theta = \frac{\cos^2\theta}{\sin^2\theta} - \cos^2\theta
$$

$$
= \cos^2\theta\left(\frac{1}{\sin^2\theta} - 1\right) = \cos^2\theta\left(\frac{1 - \sin^2\theta}{\sin^2\theta}\right)
$$

$$
= \cos^2\theta \cdot \frac{\cos^2\theta}{\sin^2\theta} = \cot^2\theta\cos^2\theta \quad ✓
$$

</details>

---

# Identidades Fundamentales

Las **identidades trigonométricas** son igualdades que se cumplen para todos los valores donde están definidas. Son herramientas esenciales para simplificar expresiones.

---

## 📖 ¿Qué es una identidad?

> **Definición:** Una identidad es una ecuación que es verdadera para **todos** los valores de la variable donde ambos lados están definidos.

### Diferencia con una ecuación

| Tipo | Ejemplo | Soluciones |
|------|---------|------------|
| Ecuación | $\sin x = 0.5$ | Solo algunos valores |
| Identidad | $\sin^2 x + \cos^2 x = 1$ | Todos los valores |

---

## 📖 Identidades recíprocas

$$
\csc\theta = \frac{1}{\sin\theta}
$$

$$
\sec\theta = \frac{1}{\cos\theta}
$$

$$
\cot\theta = \frac{1}{\tan\theta}
$$

---

## 📖 Identidades de cociente

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}
$$

$$
\cot\theta = \frac{\cos\theta}{\sin\theta}
$$

---

## 📖 Identidades pitagóricas

### La identidad fundamental

$$
\sin^2\theta + \cos^2\theta = 1
$$

### Derivadas de la fundamental

Dividiendo entre $\cos^2\theta$:

$$
\tan^2\theta + 1 = \sec^2\theta
$$

Dividiendo entre $\sin^2\theta$:

$$
1 + \cot^2\theta = \csc^2\theta
$$

---

## 📖 Resumen de identidades fundamentales

| Tipo | Identidades |
|------|-------------|
| Recíprocas | $\csc = \frac{1}{\sin}$, $\sec = \frac{1}{\cos}$, $\cot = \frac{1}{\tan}$ |
| Cociente | $\tan = \frac{\sin}{\cos}$, $\cot = \frac{\cos}{\sin}$ |
| Pitagóricas | $\sin^2 + \cos^2 = 1$, $\tan^2 + 1 = \sec^2$, $1 + \cot^2 = \csc^2$ |

---

## 📖 Uso de identidades

### Para simplificar expresiones

**Ejemplo:** Simplificar $\sin\theta \cdot \csc\theta$

$$
\sin\theta \cdot \csc\theta = \sin\theta \cdot \frac{1}{\sin\theta} = 1
$$

### Para convertir entre funciones

**Ejemplo:** Expresar $\tan\theta$ en términos de $\sin\theta$ y $\cos\theta$

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}
$$

---

## 📖 Despejando de las identidades pitagóricas

De $\sin^2\theta + \cos^2\theta = 1$:

$$
\sin^2\theta = 1 - \cos^2\theta
$$

$$
\cos^2\theta = 1 - \sin^2\theta
$$

$$
\sin\theta = \pm\sqrt{1 - \cos^2\theta}
$$

$$
\cos\theta = \pm\sqrt{1 - \sin^2\theta}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Simplificar

Simplifica usando identidades:

1. $\cos\theta \cdot \sec\theta$
2. $\frac{\sin\theta}{\tan\theta}$
3. $\sin^2\theta(1 + \cot^2\theta)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\cos\theta \cdot \frac{1}{\cos\theta} = 1$
2. $\frac{\sin\theta}{\frac{\sin\theta}{\cos\theta}} = \cos\theta$
3. $\sin^2\theta \cdot \csc^2\theta = \sin^2\theta \cdot \frac{1}{\sin^2\theta} = 1$

</details>

---

### Ejercicio 2: Expresar

Expresa en términos de seno y coseno:

1. $\tan\theta + \cot\theta$
2. $\sec^2\theta - \tan^2\theta$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta} = \frac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta} = \frac{1}{\sin\theta\cos\theta}$

2. Por identidad pitagórica: $\sec^2\theta - \tan^2\theta = 1$

</details>

---

### Ejercicio 3: Verificar

Verifica que $\tan^2\theta + 1 = \sec^2\theta$ para $\theta = 45°$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\tan^2 45° + 1 = 1^2 + 1 = 2
$$

$$
\sec^2 45° = \left(\frac{1}{\cos 45°}\right)^2 = \left(\frac{1}{\frac{\sqrt{2}}{2}}\right)^2 = (\sqrt{2})^2 = 2
$$

Ambos lados son iguales. ✓

</details>

---

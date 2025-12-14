# Ecuaciones Trigonométricas

Una **ecuación trigonométrica** es una ecuación que contiene funciones trigonométricas y queremos encontrar los valores del ángulo que la satisfacen.

---

## 📖 Diferencia con identidades

| Tipo | Descripción | Soluciones |
|------|-------------|------------|
| Identidad | Verdadera para todos los valores | Infinitas (todas) |
| Ecuación | Verdadera para algunos valores | Algunas específicas |

---

## 📖 Tipos de soluciones

### Soluciones principales

Las soluciones en el intervalo $[0°, 360°)$ o $[0, 2\pi)$.

### Solución general

Incluye todas las soluciones, usando la periodicidad:

$$
\theta = \theta_0 + k \cdot 360° \quad \text{(o } + k \cdot 2\pi)
$$

---

## 📖 Método general

1. **Aislar** la función trigonométrica
2. **Encontrar** el ángulo de referencia
3. **Determinar** en qué cuadrantes está la solución
4. **Escribir** las soluciones (principales o generales)

---

## 📖 Ejemplo 1: $\sin\theta = 0.5$

### Paso 1: Ángulo de referencia

$$
\theta_{ref} = \arcsin(0.5) = 30°
$$

### Paso 2: Cuadrantes

El seno es positivo en los cuadrantes I y II.

### Paso 3: Soluciones principales

$$
\theta = 30° \quad \text{(QI)}
$$

$$
\theta = 180° - 30° = 150° \quad \text{(QII)}
$$

### Paso 4: Solución general

$$
\theta = 30° + k \cdot 360°
$$

$$
\theta = 150° + k \cdot 360°
$$

---

## 📖 Ejemplo 2: $\cos\theta = -\frac{\sqrt{2}}{2}$

### Ángulo de referencia

$$
\theta_{ref} = \arccos\left(\frac{\sqrt{2}}{2}\right) = 45°
$$

### Cuadrantes

El coseno es negativo en QII y QIII.

### Soluciones principales

$$
\theta = 180° - 45° = 135° \quad \text{(QII)}
$$

$$
\theta = 180° + 45° = 225° \quad \text{(QIII)}
$$

---

## 📖 Ejemplo 3: $2\sin^2\theta - \sin\theta - 1 = 0$

### Factorización

Sea $u = \sin\theta$:

$$
2u^2 - u - 1 = 0
$$

$$
(2u + 1)(u - 1) = 0
$$

$$
u = -\frac{1}{2} \quad \text{o} \quad u = 1
$$

### Resolver cada caso

**Caso 1:** $\sin\theta = -\frac{1}{2}$

Ref = 30°, QIII y QIV:

$\theta = 210°$ o $\theta = 330°$

**Caso 2:** $\sin\theta = 1$

$\theta = 90°$

### Soluciones principales

$$
\theta = 90°, 210°, 330°
$$

---

## 📖 Ecuaciones con tangente

Para $\tan\theta = a$:

$$
\theta = \arctan(a) + k \cdot 180°
$$

(La tangente tiene período $180°$)

---

## 📝 Ejercicios de práctica

### Ejercicio 1

Resuelve $\cos\theta = \frac{1}{2}$ en $[0°, 360°)$.

<details>
<summary><strong>Ver respuesta</strong></summary>

Ref = 60°, coseno positivo en QI y QIV:

$$
\theta = 60° \quad \text{y} \quad \theta = 360° - 60° = 300°
$$

</details>

---

### Ejercicio 2

Resuelve $\tan\theta = 1$ en $[0°, 360°)$.

<details>
<summary><strong>Ver respuesta</strong></summary>

Ref = 45°, tangente positiva en QI y QIII:

$$
\theta = 45° \quad \text{y} \quad \theta = 180° + 45° = 225°
$$

</details>

---

### Ejercicio 3

Resuelve $2\cos^2\theta - 1 = 0$ en $[0°, 360°)$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\cos^2\theta = \frac{1}{2}
$$

$$
\cos\theta = \pm\frac{1}{\sqrt{2}} = \pm\frac{\sqrt{2}}{2}
$$

Ref = 45°, los cuatro cuadrantes:

$$
\theta = 45°, 135°, 225°, 315°
$$

</details>

---

### Ejercicio 4

Resuelve $\sin 2\theta = 0$ en $[0°, 360°)$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$2\theta = 0°, 180°, 360°, 540°, ...$

Dividiendo entre 2:

$$
\theta = 0°, 90°, 180°, 270°
$$

</details>

---

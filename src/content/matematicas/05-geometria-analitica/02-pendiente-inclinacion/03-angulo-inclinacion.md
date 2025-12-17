# Ángulo de Inclinación

La pendiente nos da un número, pero ¿qué ángulo forma realmente la recta con el eje horizontal? El **ángulo de inclinación** es otra forma de medir la inclinación de una recta, y está directamente relacionado con la pendiente a través de la función tangente.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el ángulo de inclinación
- La relación entre pendiente y ángulo
- Cómo calcular uno a partir del otro

---

## 📖 Lo Esencial del Ángulo de Inclinación

| Relación | Fórmula |
|----------|---------|
| Pendiente a partir del ángulo | $m = \tan(\theta)$ |
| Ángulo a partir de la pendiente | $\theta = \arctan(m)$ |

| Pendiente | Ángulo |
|-----------|--------|
| $m = 0$ | $\theta = 0°$ |
| $m = 1$ | $\theta = 45°$ |
| $m = -1$ | $\theta = 135°$ |
| $m \to +\infty$ | $\theta \to 90°$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/angulo-inclinacion.svg" alt="Ángulo de inclinación θ de una recta" style="width: 100%; height: auto;" />
</div>

---

## 📖 Definición del Ángulo de Inclinación

> El **ángulo de inclinación** $\theta$ de una recta es el ángulo medido desde el semieje positivo de $X$ hasta la recta, en sentido **antihorario**.

**Propiedades:**
- Se mide en grados o radianes
- Siempre está en el rango $0° \leq \theta < 180°$
- Para rectas horizontales: $\theta = 0°$
- Para rectas verticales: $\theta = 90°$

---

## 📖 Relación entre Pendiente y Ángulo

La pendiente $m$ y el ángulo de inclinación $\theta$ están relacionados por la **función tangente**:

$$
m = \tan(\theta)
$$

Y para encontrar el ángulo a partir de la pendiente:

$$
\theta = \arctan(m)
$$

> 💡 **Nota:** Si $\arctan$ te da un ángulo negativo, suma 180° para obtener el ángulo de inclinación correcto (que debe estar entre 0° y 180°).

---

## 📖 Ángulos Notables

Algunos valores son tan frecuentes que vale la pena memorizarlos:

| Pendiente $m$ | Ángulo $\theta$ | Descripción |
|---------------|-----------------|-------------|
| $0$ | $0°$ | Recta horizontal |
| $\frac{\sqrt{3}}{3} \approx 0.577$ | $30°$ | Inclinación suave |
| $1$ | $45°$ | Recta a 45° |
| $\sqrt{3} \approx 1.732$ | $60°$ | Inclinación pronunciada |
| No definida | $90°$ | Recta vertical |
| $-1$ | $135°$ | Recta descendente a 45° |

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Del ángulo a la pendiente

Una recta tiene ángulo de inclinación $\theta = 60°$. ¿Cuál es su pendiente?

**Aplicamos la fórmula:**

$$
m = \tan(60°) = \sqrt{3} \approx 1.732
$$

**Respuesta:** La pendiente es $m = \sqrt{3} \approx 1.732$.

### ⚙️ Ejemplo 2: De la pendiente al ángulo

Una recta tiene pendiente $m = 2$. ¿Cuál es su ángulo de inclinación?

**Aplicamos la fórmula:**

$$
\theta = \arctan(2) \approx 63.43°
$$

**Respuesta:** El ángulo de inclinación es aproximadamente $63.43°$.

### ⚙️ Ejemplo 3: Pendiente negativa

Una recta tiene pendiente $m = -1$. ¿Cuál es su ángulo de inclinación?

**Cálculo:**

$$
\arctan(-1) = -45°
$$

Pero el ángulo de inclinación debe estar entre $0°$ y $180°$, así que sumamos $180°$:

$$
\theta = -45° + 180° = 135°
$$

**Respuesta:** El ángulo de inclinación es $135°$.

### ⚙️ Ejemplo 4: Calcular ángulo desde dos puntos

Encuentra el ángulo de inclinación de la recta que pasa por $A(1, 2)$ y $B(5, 6)$.

**Paso 1:** Calcular la pendiente:

$$
m = \frac{6 - 2}{5 - 1} = \frac{4}{4} = 1
$$

**Paso 2:** Calcular el ángulo:

$$
\theta = \arctan(1) = 45°
$$

**Respuesta:** El ángulo de inclinación es $45°$.

### ⚙️ Ejemplo 5: Recta descendente

Encuentra el ángulo de inclinación de la recta que pasa por $P(0, 5)$ y $Q(5, 0)$.

**Paso 1:** Calcular la pendiente:

$$
m = \frac{0 - 5}{5 - 0} = \frac{-5}{5} = -1
$$

**Paso 2:** Calcular el ángulo:

$$
\arctan(-1) = -45°
$$

Como es negativo, sumamos $180°$:

$$
\theta = -45° + 180° = 135°
$$

**Respuesta:** El ángulo de inclinación es $135°$.

---

## 📖 Casos Especiales

### Recta horizontal

- Pendiente: $m = 0$
- Ángulo: $\theta = \arctan(0) = 0°$

### Recta vertical

- Pendiente: indefinida
- Ángulo: $\theta = 90°$
- La tangente de $90°$ no existe (tiende a infinito)

---

## 🔑 Resumen

| Conversión | Fórmula | Rango |
|------------|---------|-------|
| Pendiente → Ángulo | $\theta = \arctan(m)$ | Ajustar a $[0°, 180°)$ |
| Ángulo → Pendiente | $m = \tan(\theta)$ | $m$ cualquier real o indefinida |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la pendiente de una recta con ángulo de inclinación $\theta = 30°$.

<details>
<summary>Ver solución</summary>

$$
m = \tan(30°) = \frac{\sqrt{3}}{3} \approx 0.577
$$

**Respuesta:** $m = \frac{\sqrt{3}}{3}$

</details>

### Ejercicio 2
Encuentra el ángulo de inclinación de una recta con pendiente $m = 3$.

<details>
<summary>Ver solución</summary>

$$
\theta = \arctan(3) \approx 71.57°
$$

**Respuesta:** $\theta \approx 71.57°$

</details>

### Ejercicio 3
Una recta pasa por los puntos $A(2, 1)$ y $B(6, 9)$. Encuentra su ángulo de inclinación.

<details>
<summary>Ver solución</summary>

**Paso 1:** Pendiente
$$
m = \frac{9 - 1}{6 - 2} = \frac{8}{4} = 2
$$

**Paso 2:** Ángulo
$$
\theta = \arctan(2) \approx 63.43°
$$

**Respuesta:** $\theta \approx 63.43°$

</details>

### Ejercicio 4
Si el ángulo de inclinación de una recta es $\theta = 120°$, ¿cuál es su pendiente?

<details>
<summary>Ver solución</summary>

$$
m = \tan(120°) = -\sqrt{3} \approx -1.732
$$

**Respuesta:** $m = -\sqrt{3}$

> Nota: El ángulo está en el segundo cuadrante, por eso la pendiente es negativa.

</details>

### Ejercicio 5
Una recta tiene pendiente $m = -\frac{1}{2}$. ¿Cuál es su ángulo de inclinación?

<details>
<summary>Ver solución</summary>

$$
\arctan\left(-\frac{1}{2}\right) \approx -26.57°
$$

Sumamos $180°$:

$$
\theta \approx -26.57° + 180° = 153.43°
$$

**Respuesta:** $\theta \approx 153.43°$

</details>

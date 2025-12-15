# Ángulo Entre Dos Rectas

Cuando dos rectas se intersectan, forman ángulos. ¿Cómo calculamos el ángulo que forman entre sí, conociendo solo sus pendientes? Esta lección te enseñará la fórmula del ángulo entre dos rectas.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula del ángulo entre dos rectas
- Cómo interpretar el ángulo agudo y obtuso
- Casos especiales

---

## 📖 Lo Esencial del Ángulo Entre Rectas

| Fórmula | Descripción |
|---------|-------------|
| $\tan(\phi) = \left\|\dfrac{m_2 - m_1}{1 + m_1 \cdot m_2}\right\|$ | Tangente del ángulo agudo |
| $\phi = \arctan\left(\left\|\dfrac{m_2 - m_1}{1 + m_1 \cdot m_2}\right\|\right)$ | Ángulo agudo entre las rectas |

| Caso especial | Resultado |
|--------------|-----------|
| $m_1 = m_2$ | $\phi = 0°$ (paralelas) |
| $m_1 \cdot m_2 = -1$ | $\phi = 90°$ (perpendiculares) |

---

## 📖 El Problema

Cuando dos rectas no paralelas se intersectan, forman **cuatro ángulos**: dos pares de ángulos opuestos por el vértice.

Los ángulos opuestos son iguales, así que solo hay dos medidas diferentes:
- Un ángulo **agudo** (menor que 90°)
- Un ángulo **obtuso** (mayor que 90°)

Estos dos ángulos son **suplementarios** (suman 180°).

En general, nos interesa el **ángulo agudo** entre las rectas.

---

## 📖 La Fórmula del Ángulo

Sean $\ell_1$ y $\ell_2$ dos rectas con pendientes $m_1$ y $m_2$ respectivamente. El ángulo agudo $\phi$ entre ellas se calcula con:

$$
\tan(\phi) = \left|\frac{m_2 - m_1}{1 + m_1 \cdot m_2}\right|
$$

Y el ángulo es:

$$
\phi = \arctan\left(\left|\frac{m_2 - m_1}{1 + m_1 \cdot m_2}\right|\right)
$$

> 💡 **¿Por qué el valor absoluto?** Para garantizar que siempre obtengamos el ángulo agudo (positivo y menor que 90°).

---

## 📖 Deducción de la Fórmula

Si $\theta_1$ y $\theta_2$ son los ángulos de inclinación de las rectas, el ángulo entre ellas es:

$$
\phi = \theta_2 - \theta_1
$$

Usando la identidad de la tangente de la diferencia:

$$
\tan(\phi) = \tan(\theta_2 - \theta_1) = \frac{\tan\theta_2 - \tan\theta_1}{1 + \tan\theta_1 \cdot \tan\theta_2}
$$

Como $m = \tan\theta$:

$$
\tan(\phi) = \frac{m_2 - m_1}{1 + m_1 \cdot m_2}
$$

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Ángulo entre dos rectas

Encuentra el ángulo agudo entre las rectas $y = 2x + 1$ y $y = \frac{1}{2}x - 3$.

**Pendientes:**
- $m_1 = 2$
- $m_2 = \frac{1}{2}$

**Aplicamos la fórmula:**

$$
\tan(\phi) = \left|\frac{\frac{1}{2} - 2}{1 + 2 \cdot \frac{1}{2}}\right| = \left|\frac{-\frac{3}{2}}{1 + 1}\right| = \left|\frac{-\frac{3}{2}}{2}\right| = \frac{3}{4}
$$

$$
\phi = \arctan\left(\frac{3}{4}\right) \approx 36.87°
$$

**Respuesta:** El ángulo agudo es aproximadamente $36.87°$.

### ⚙️ Ejemplo 2: Ángulo entre rectas perpendiculares

Verifica que el ángulo entre $y = 3x$ y $y = -\frac{1}{3}x$ es $90°$.

**Pendientes:**
- $m_1 = 3$
- $m_2 = -\frac{1}{3}$

**Calculamos:**

$$
1 + m_1 \cdot m_2 = 1 + 3 \times \left(-\frac{1}{3}\right) = 1 - 1 = 0
$$

El denominador es 0, lo que significa que $\tan(\phi)$ es indefinida.

$$
\tan(\phi) \to \infty \implies \phi = 90°
$$

**Respuesta:** Las rectas son perpendiculares (forman un ángulo de $90°$).

### ⚙️ Ejemplo 3: Rectas con pendientes negativas

Encuentra el ángulo entre las rectas con pendientes $m_1 = -2$ y $m_2 = 1$.

**Aplicamos la fórmula:**

$$
\tan(\phi) = \left|\frac{1 - (-2)}{1 + (-2)(1)}\right| = \left|\frac{3}{1 - 2}\right| = \left|\frac{3}{-1}\right| = 3
$$

$$
\phi = \arctan(3) \approx 71.57°
$$

**Respuesta:** El ángulo agudo es aproximadamente $71.57°$.

### ⚙️ Ejemplo 4: Ángulo dado por puntos

Encuentra el ángulo entre la recta que pasa por $A(0, 0)$, $B(2, 4)$ y la que pasa por $C(1, 3)$, $D(4, 3)$.

**Pendiente de AB:**
$$
m_1 = \frac{4 - 0}{2 - 0} = 2
$$

**Pendiente de CD:**
$$
m_2 = \frac{3 - 3}{4 - 1} = 0
$$

(CD es horizontal)

**Cálculo del ángulo:**

$$
\tan(\phi) = \left|\frac{0 - 2}{1 + 2 \cdot 0}\right| = \left|\frac{-2}{1}\right| = 2
$$

$$
\phi = \arctan(2) \approx 63.43°
$$

**Respuesta:** El ángulo es aproximadamente $63.43°$.

> Nota: Este es el mismo ángulo de inclinación de la recta AB, lo cual tiene sentido porque CD es horizontal.

### ⚙️ Ejemplo 5: Ángulo entre rectas paralelas

Encuentra el ángulo entre $y = 4x + 2$ y $y = 4x - 7$.

**Pendientes:** $m_1 = m_2 = 4$

**Cálculo:**

$$
\tan(\phi) = \left|\frac{4 - 4}{1 + 4 \cdot 4}\right| = \left|\frac{0}{17}\right| = 0
$$

$$
\phi = \arctan(0) = 0°
$$

**Respuesta:** El ángulo es $0°$ (las rectas son paralelas, nunca se intersectan).

---

## 🔑 Resumen

| Situación | Resultado |
|-----------|-----------|
| Rectas generales | $\phi = \arctan\left(\left\|\dfrac{m_2 - m_1}{1 + m_1m_2}\right\|\right)$ |
| $m_1 = m_2$ | $\phi = 0°$ (paralelas) |
| $m_1 \cdot m_2 = -1$ | $\phi = 90°$ (perpendiculares) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el ángulo agudo entre las rectas $y = x + 4$ y $y = 3x - 2$.

<details>
<summary>Ver solución</summary>

$m_1 = 1$, $m_2 = 3$

$$
\tan(\phi) = \left|\frac{3 - 1}{1 + 1 \cdot 3}\right| = \left|\frac{2}{4}\right| = \frac{1}{2}
$$

$$
\phi = \arctan\left(\frac{1}{2}\right) \approx 26.57°
$$

**Respuesta:** $\approx 26.57°$

</details>

### Ejercicio 2
Encuentra el ángulo entre las rectas con pendientes $m_1 = 5$ y $m_2 = -\frac{1}{5}$.

<details>
<summary>Ver solución</summary>

$$
1 + m_1 \cdot m_2 = 1 + 5 \times \left(-\frac{1}{5}\right) = 1 - 1 = 0
$$

Como el denominador es 0, las rectas son **perpendiculares**.

**Respuesta:** $\phi = 90°$

</details>

### Ejercicio 3
Calcula el ángulo entre la recta que pasa por $(1, 2)$, $(3, 6)$ y la recta que pasa por $(0, 0)$, $(5, 2)$.

<details>
<summary>Ver solución</summary>

**Pendiente 1:**
$$
m_1 = \frac{6 - 2}{3 - 1} = 2
$$

**Pendiente 2:**
$$
m_2 = \frac{2 - 0}{5 - 0} = \frac{2}{5}
$$

**Ángulo:**
$$
\tan(\phi) = \left|\frac{\frac{2}{5} - 2}{1 + 2 \cdot \frac{2}{5}}\right| = \left|\frac{-\frac{8}{5}}{\frac{9}{5}}\right| = \frac{8}{9}
$$

$$
\phi = \arctan\left(\frac{8}{9}\right) \approx 41.63°
$$

**Respuesta:** $\approx 41.63°$

</details>

### Ejercicio 4
Dos rectas forman un ángulo de $45°$. Si una tiene pendiente $m_1 = 2$, encuentra las posibles pendientes de la otra.

<details>
<summary>Ver solución</summary>

Usamos $\tan(45°) = 1$:

$$
1 = \left|\frac{m_2 - 2}{1 + 2m_2}\right|
$$

**Caso 1:** $\frac{m_2 - 2}{1 + 2m_2} = 1$

$$
m_2 - 2 = 1 + 2m_2
$$
$$
-3 = m_2
$$

**Caso 2:** $\frac{m_2 - 2}{1 + 2m_2} = -1$

$$
m_2 - 2 = -1 - 2m_2
$$
$$
3m_2 = 1
$$
$$
m_2 = \frac{1}{3}
$$

**Respuesta:** $m_2 = -3$ o $m_2 = \frac{1}{3}$

</details>

### Ejercicio 5
Un triángulo tiene vértices en $A(0, 0)$, $B(4, 0)$ y $C(2, 3)$. Encuentra el ángulo en el vértice $A$.

<details>
<summary>Ver solución</summary>

El ángulo en $A$ está formado por los lados $AB$ y $AC$.

**Pendiente de AB:**
$$
m_1 = \frac{0 - 0}{4 - 0} = 0
$$

**Pendiente de AC:**
$$
m_2 = \frac{3 - 0}{2 - 0} = \frac{3}{2}
$$

**Ángulo:**
$$
\tan(\phi) = \left|\frac{\frac{3}{2} - 0}{1 + 0}\right| = \frac{3}{2}
$$

$$
\phi = \arctan\left(\frac{3}{2}\right) \approx 56.31°
$$

**Respuesta:** El ángulo en $A$ es aproximadamente $56.31°$

</details>

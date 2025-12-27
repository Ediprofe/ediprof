# **Ángulos Mayores de 90°**

No importa qué tan grande sea un ángulo: siempre podemos calcular sus funciones trigonométricas comparándolo con un triángulo pequeño en el primer cuadrante. A este triángulo "clon" lo llamamos **ángulo de referencia**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el ángulo de referencia y cómo calcularlo.
- Cómo reducir cualquier ángulo a uno del primer cuadrante.
- El procedimiento paso a paso para calcular funciones de ángulos grandes.
- Cómo resolver ecuaciones simples como "encuentra el ángulo" sabiendo el cuadrante.

---

## 📐 El Ángulo de Referencia

> **Definición:** El ángulo de referencia ($\alpha$) es el ángulo agudo (menor a 90°) que forma el lado terminal con el **eje X** más cercano.

**¡Ojo!** Siempre es con el eje X (horizontal), nunca con el Y.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Ángulos de referencia en cada cuadrante</strong>
  </div>

![Ángulos de referencia](/images/trigonometria/circulo-unitario/angulos-referencia.svg)

</div>

| Cuadrante | Operación | Explicación |
| :---: | :---: | :--- |
| **I** | $\alpha = \theta$ | Es él mismo. |
| **II** | $\alpha = 180° - \theta$ | Lo que le falta para llegar a 180°. |
| **III** | $\alpha = \theta - 180°$ | Lo que se pasó de 180°. |
| **IV** | $\alpha = 360° - \theta$ | Lo que le falta para llegar a 360°. |

---

## 🛠️ Procedimiento Maestro

Para calcular cualquier función trigonométrica sin calculadora:

1.  **Encuentra el Ángulo de Referencia ($\alpha$).**
2.  **Calcula la función para $\alpha$** (usando la tabla de 30°, 45°, 60°).
3.  **Decide el signo** (+ o -) según el cuadrante original (regla "Todos Sin TaCos").

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular $\sin(150°)$

**Paso 1: Referencia**
150° está en el Cuadrante II.
$\alpha = 180° - 150° = 30°$.

**Paso 2: Valor base**
$\sin(30°) = 0.5$.

**Paso 3: Signo**
En el Cuadrante II, el Seno es Positivo.

**Resultado:**

$$
\boxed{\sin(150°) = 0.5}
$$

---

### Ejemplo 2: Calcular $\cos(240°)$

**Paso 1: Referencia**
240° está en el Cuadrante III.
$\alpha = 240° - 180° = 60°$.

**Paso 2: Valor base**
$\cos(60°) = 0.5$.

**Paso 3: Signo**
En el Cuadrante III, el Coseno es Negativo.

**Resultado:**

$$
\boxed{\cos(240°) = -0.5}
$$

---

### Ejemplo 3: Calcular $\tan(315°)$

**Paso 1: Referencia**
315° está en el Cuadrante IV.
$\alpha = 360° - 315° = 45°$.

**Paso 2: Valor base**
$\tan(45°) = 1$.

**Paso 3: Signo**
En el Cuadrante IV, la Tangente es Negativa.

**Resultado:**

$$
\boxed{\tan(315°) = -1}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el ángulo de referencia para $120°$.

<details>
<summary>Ver solución</summary>
Cuadrante II: $180° - 120°$.

**Respuesta:** $\boxed{60°}$
</details>

---

### Ejercicio 2
Encuentra el ángulo de referencia para $225°$.

<details>
<summary>Ver solución</summary>
Cuadrante III: $225° - 180°$.

**Respuesta:** $\boxed{45°}$
</details>

---

### Ejercicio 3
Encuentra el ángulo de referencia para $330°$.

<details>
<summary>Ver solución</summary>
Cuadrante IV: $360° - 330°$.

**Respuesta:** $\boxed{30°}$
</details>

---

### Ejercicio 4
Calcula el valor exacto de $\sin(135°)$.

<details>
<summary>Ver solución</summary>

1.  QII, Ref = $45°$.
2.  $\sin(45°) = \frac{\sqrt{2}}{2}$.
3.  Seno en QII es (+).

**Respuesta:** $\boxed{\frac{\sqrt{2}}{2}}$
</details>

---

### Ejercicio 5
Calcula el valor exacto de $\cos(210°)$.

<details>
<summary>Ver solución</summary>

1.  QIII, Ref = $210° - 180° = 30°$.
2.  $\cos(30°) = \frac{\sqrt{3}}{2}$.
3.  Coseno en QIII es (-).

**Respuesta:** $\boxed{-\frac{\sqrt{3}}{2}}$
</details>

---

### Ejercicio 6
Calcula el valor exacto de $\tan(300°)$.

<details>
<summary>Ver solución</summary>

1.  QIV, Ref = $60°$.
2.  $\tan(60°) = \sqrt{3}$.
3.  Tangente en QIV es (-).

**Respuesta:** $\boxed{-\sqrt{3}}$
</details>

---

### Ejercicio 7
Calcula el valor exacto de $\sec(135°)$.

<details>
<summary>Ver solución</summary>

1.  Ref = $45°$. $\sec(45°) = \sqrt{2}$.
2.  Secante en QII (como coseno) es (-).

**Respuesta:** $\boxed{-\sqrt{2}}$
</details>

---

### Ejercicio 8
Si $\sin\theta = 0.5$ y $\theta$ está en el segundo cuadrante, ¿cuánto vale $\theta$?

<details>
<summary>Ver solución</summary>

1.  El ángulo de referencia cuyo seno es 0.5 es **30°**.
2.  En QII: $\theta = 180° - 30°$.

**Respuesta:** $\boxed{150°}$
</details>

---

### Ejercicio 9
Si $\tan\theta = -1$ y $\theta$ está en el cuarto cuadrante, ¿cuánto vale $\theta$?

<details>
<summary>Ver solución</summary>

1.  El ángulo de referencia cuya tangente es 1 es **45°**.
2.  En QIV: $\theta = 360° - 45°$.

**Respuesta:** $\boxed{315°}$
</details>

---

### Ejercicio 10
Calcula el valor de $\sin(405°)$.

<details>
<summary>Ver solución</summary>

1.  Restamos 360°: $405° - 360° = 45°$.
2.  Es directamente el ángulo de 45° en QI.

**Respuesta:** $\boxed{\frac{\sqrt{2}}{2}}$
</details>

---

## 🔑 Resumen

| Paso | Pregunta Clave | Acción |
| :--- | :--- | :--- |
| **1. Referencia** | ¿Cuánto le falta para el eje X? | Calcula $\alpha$ (siempre positivo). |
| **2. Valor** | ¿Cuánto vale la función en $\alpha$? | Usa la tabla de 30-45-60. |
| **3. Signo** | ¿En qué cuadrante estoy? | Aplica ASTC. |

> **Conclusión:** Cualquier problema de trigonometría grande se puede romper en tres problemas pequeños: geometría simple (referencia), memoria (tabla básica) y signo (cuadrante).

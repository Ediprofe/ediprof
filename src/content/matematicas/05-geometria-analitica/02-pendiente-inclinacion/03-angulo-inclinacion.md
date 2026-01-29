# **Ángulo de Inclinación**

Hasta ahora hemos medido la inclinación como un número (pendiente $m=2$, $m=0.5$). Pero en el mundo real, los arquitectos y carpinteros usan **grados**. Dicen "un techo de 30 grados", no "un techo con pendiente 0.57". Hoy aprenderemos a traducir entre estos dos lenguajes.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el ángulo de inclinación ($\theta$).
- Cómo traducir de Pendiente ($m$) a Ángulo ($\theta$) y viceversa.
- Por qué usamos la función Tangente.
- Cómo manejar ángulos negativos o mayores de 90°.

---

## 📐 El Concepto Visual

El ángulo de inclinación es el ángulo que forma la recta con el eje X positivo, medido en contra de las manecillas del reloj.

- **Si la recta es horizontal:** $\theta = 0°$.
- **Si la recta es vertical:** $\theta = 90°$.
- **Si la recta sube:** El ángulo es agudo ($0° < \theta < 90°$).
- **Si la recta baja:** El ángulo es obtuso ($90° < \theta < 180°$).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Pendiente vs Ángulo</strong>
  </div>
  <img src="/images/geometria/analitica/angulo-inclinacion.svg" alt="Ángulo de inclinación θ de una recta" style="width: 100%; height: auto;" />
</div>

---

## 🧬 La Relación Secreta: Tangente

Recuerda trigonometría básica. En un triángulo, $\tan(\theta) = \frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$.
En nuestra recta, el opuesto es la subida ($\Delta y$) y el adyacente es el avance ($\Delta x$).
¡Es lo mismo que la pendiente!

$$
m = \tan(\theta)
$$

Si quieres encontrar el ángulo, usas la función inversa:

$$
\theta = \tan^{-1}(m) \quad \text{o} \quad \arctan(m)
$$

> **Nota Importante:** Si la pendiente es negativa, la calculadora te dará un ángulo negativo (ej. $-45°$). Para obtener el ángulo de inclinación real, **súmale 180°**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: De Pendiente a Ángulo
Una rampa tiene pendiente $m = 1$. ¿Cuál es su ángulo?
$$ \theta = \tan^{-1}(1) = 45° $$

### Ejemplo 2: De Ángulo a Pendiente
Una carretera sube con un ángulo de $30°$. ¿Cuál es su pendiente?
$$ m = \tan(30°) \approx 0.577 $$

### Ejemplo 3: Pendiente Negativa
Una recta tiene pendiente $m = -2$.
1.  Calculamos en la calculadora: $\tan^{-1}(-2) \approx -63.4°$.
2.  Como es negativo, sumamos 180°: $-63.4° + 180° = 116.6°$.
**Resultado:** $\theta = 116.6°$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el ángulo si $m = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan^{-1}(0) = 0°$.

**Respuesta:** $\boxed{0°}$
</details>

---

### Ejercicio 2
Si el ángulo es 45°, ¿cuánto vale $m$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(45°) = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 3
Calcula el ángulo para $m = \sqrt{3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan^{-1}(\sqrt{3}) = 60°$.

**Respuesta:** $\boxed{60°}$
</details>

---

### Ejercicio 4
Si una recta es vertical, ¿cuál es su ángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es perpendicular al eje X.

**Respuesta:** $\boxed{90°}$
</details>

---

### Ejercicio 5
Calcula el ángulo si $m = -1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan^{-1}(-1) = -45°$.
Sumar 180: $135°$.

**Respuesta:** $\boxed{135°}$
</details>

---

### Ejercicio 6
Una recta pasa por $(0,0)$ y $(3,4)$. Halla su ángulo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = 4/3 \approx 1.33$.
$\tan^{-1}(1.33) \approx 53.13°$.

**Respuesta:** $\boxed{53.13°}$
</details>

---

### Ejercicio 7
Si el ángulo es 150°, ¿cuánto vale $m$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(150°) = -\frac{\sqrt{3}}{3} \approx -0.577$.

**Respuesta:** $\boxed{-0.577}$
</details>

---

### Ejercicio 8
¿Qué pasa si intentas calcular $\tan(90°)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Error matemático. Pendiente indefinida.

**Respuesta:** **Error (Indefinido)**
</details>

---

### Ejercicio 9
Si $m = 100$ (muy empinada), ¿el ángulo es mayor o menor a 89°?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(89°) \approx 57$. $\tan(89.5°) \approx 114$.
Es cercano a 90°.

**Respuesta:** **Mayor a 89° (aprox 89.4°)**
</details>

---

### Ejercicio 10
Halla el ángulo de la recta $y = -x + 5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = -1$.
Ángulo = $135°$.

**Respuesta:** $\boxed{135°}$
</details>

---

## 🔑 Resumen

| Pendiente ($m$) | Ángulo ($\theta$) |
| :--- | :--- |
| **0** | $0°$ |
| **1** | $45°$ |
| **Positiva** | Agudo ($0-90°$) |
| **Indefinida** | $90°$ |
| **Negativa** | Obtuso ($90-180°$) |
| **-1** | $135°$ |

> **Conclusión:** La pendiente y el ángulo son dos caras de la misma moneda. Usa $m$ para ecuaciones y $\theta$ para visualización o construcción.

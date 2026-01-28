---
title: "📈 Gráficas de Movimiento"
---

# 📈 **Gráficas de Movimiento**

## 🎯 **¿Qué vas a aprender?**

En esta lección aprenderás a:

*   **Interpretar** gráficas de posición, velocidad y aceleración.
*   **Relacionar** la pendiente y el área bajo la curva con variables físicas.
*   **Identificar** el tipo de movimiento (MRU, MRUA, Reposo) a partir de su gráfica.
*   **Calcular** desplazamiento y aceleración usando datos gráficos.

---

## 🎯 **Las Tres Gráficas Fundamentales**

| Gráfica | Eje vertical | ¿Qué muestra? |
|---------|-------------|---------------|
| **x vs t** | Posición (m) | Dónde está el objeto |
| **v vs t** | Velocidad (m/s) | Qué tan rápido y hacia dónde |
| **a vs t** | Aceleración (m/s²) | Cómo cambia la velocidad |

### **Relaciones clave**

| Relación | Significado |
|----------|-------------|
| Pendiente de **x-t** | = **velocidad** |
| Pendiente de **v-t** | = **aceleración** |
| Área bajo **v-t** | = **desplazamiento** |
| Área bajo **a-t** | = **cambio de velocidad** |

---

## 📊 **Gráficas por Tipo de Movimiento**

### **1. Reposo (Objeto quieto)**

<div style="display: flex; flex-direction: column; align-items: center; gap: 2rem; margin: 2rem 0;">
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/reposo-x.svg" alt="x vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/reposo-v.svg" alt="v vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/reposo-a.svg" alt="a vs t" style="width: 100%; height: auto;">
  </div>
</div>

**Características:** x = constante, v = 0, a = 0

---

### **2. MRU hacia adelante (v > 0)**

<div style="display: flex; flex-direction: column; align-items: center; gap: 2rem; margin: 2rem 0;">
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mru-adelante-x.svg" alt="x vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mru-adelante-v.svg" alt="v vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mru-adelante-a.svg" alt="a vs t" style="width: 100%; height: auto;">
  </div>
</div>

**Características:** x crece linealmente (recta ↗), v = constante positiva, a = 0

---

### **3. MRU hacia atrás (v < 0)**

<div style="display: flex; flex-direction: column; align-items: center; gap: 2rem; margin: 2rem 0;">
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mru-atras-x.svg" alt="x vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mru-atras-v.svg" alt="v vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mru-atras-a.svg" alt="a vs t" style="width: 100%; height: auto;">
  </div>
</div>

**Características:** x decrece linealmente (recta ↘), v = constante negativa, a = 0

---

### **4. MRUA — Acelerando (a > 0)**

<div style="display: flex; flex-direction: column; align-items: center; gap: 2rem; margin: 2rem 0;">
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mrua-acelera-x.svg" alt="x vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mrua-acelera-v.svg" alt="v vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mrua-acelera-a.svg" alt="a vs t" style="width: 100%; height: auto;">
  </div>
</div>

**Características:** x es parábola (crece cada vez más), v crece linealmente, a = constante positiva

---

### **5. MRUA — Frenando (a < 0)**

<div style="display: flex; flex-direction: column; align-items: center; gap: 2rem; margin: 2rem 0;">
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mrua-frena-x.svg" alt="x vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mrua-frena-v.svg" alt="v vs t" style="width: 100%; height: auto;">
  </div>
  <div style="width: 100%; max-width: 500px;">
    <img src="/images/fisica/cinematica/graficas/mrua-frena-a.svg" alt="a vs t" style="width: 100%; height: auto;">
  </div>
</div>

**Características:** x es parábola (crece cada vez menos hasta detenerse), v decrece linealmente hasta 0, a = constante negativa

---

## 📋 **Tabla: Resumen de Gráficas**

| Tipo de movimiento | x vs t | v vs t | a vs t |
|--------------------|--------|--------|--------|
| **Reposo** | Horizontal | En cero | En cero |
| **MRU adelante** | Recta ↗ | Horizontal positiva | En cero |
| **MRU atrás** | Recta ↘ | Horizontal negativa | En cero |
| **MRUA acelera** | Parábola ⌒ | Recta ↗ | Horizontal positiva |
| **MRUA frena** | Parábola ⌒ aplana | Recta ↘ | Horizontal negativa |

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1 — El ciclista en la ciudad**

Un ciclista recorre una avenida. Su gráfica x-t se muestra abajo. Describe su movimiento en cada tramo.

<img src="/images/fisica/cinematica/graficas/ejercicio-1-ciclista.svg" alt="Ejercicio 1: El ciclista" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

| Tramo | Tiempo | Forma | Interpretación |
|-------|--------|-------|----------------|
| **A** | 0-5 min | Recta ↗ | MRU hacia adelante (v = 1 km/min) |
| **B** | 5-10 min | Horizontal | Reposo (semáforo o descanso) |
| **C** | 10-15 min | Recta ↗ | MRU hacia adelante (v = 1 km/min) |
| **D** | 15-20 min | Horizontal | Reposo (llegó al destino) |

</details>

---

### **Ejercicio 2 — La carrera de autos**

Dos autos parten del mismo lugar. Observa sus gráficas v-t y responde: ¿Cuál recorrió más distancia en 4 segundos?

<img src="/images/fisica/cinematica/graficas/ejercicio-2-carrera.svg" alt="Ejercicio 2: Carrera de autos" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

El **área bajo v-t** = desplazamiento:

- **Auto A:** Área = 8 × 4 = **32 m** (rectángulo)
- **Auto B:** Área = ½ × 16 × 4 = **32 m** (triángulo)

**¡Ambos recorrieron la misma distancia!** Aunque B aceleró y A fue constante.

</details>

---

### **Ejercicio 3 — El tren que frena**

Un tren viaja a 20 m/s y frena uniformemente hasta detenerse en 10 segundos. Calcula la aceleración y la distancia de frenado.

<img src="/images/fisica/cinematica/graficas/ejercicio-3-tren.svg" alt="Ejercicio 3: Tren frenando" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

**Aceleración** (pendiente de v-t):
$$
a = \frac{\Delta v}{\Delta t} = \frac{0 - 20}{10 - 0} = -2\,\mathrm{m/s^2}
$$

**Distancia** (área bajo v-t):
$$
d = \frac{1}{2} \times 20 \times 10 = 100\,\mathrm{m}
$$

</details>

---

### **Ejercicio 4 — La pelota que rebota**

Una pelota se lanza hacia arriba y cae. Observa su gráfica v-t. ¿En qué instante alcanzó la altura máxima?

<img src="/images/fisica/cinematica/graficas/ejercicio-4-pelota.svg" alt="Ejercicio 4: Pelota lanzada" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

La altura máxima se alcanza cuando **v = 0**.

Observando la gráfica: v = 0 en **t = 2 s**.

En ese instante la pelota alcanzó la altura máxima y comenzó a caer (v se vuelve negativa).

</details>

---

### **Ejercicio 5 — Comparación de movimientos**

Tres objetos tienen las siguientes gráficas x-t. ¿Cuál tiene mayor velocidad?

<img src="/images/fisica/cinematica/graficas/ejercicio-5-comparacion.svg" alt="Ejercicio 5: Comparación" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

La **velocidad = pendiente** de la gráfica x-t:

| Objeto | Pendiente | Velocidad |
|--------|-----------|-----------|
| A | 8/4 = 2 | **2 m/s** |
| B | 16/4 = 4 | **4 m/s** |
| C | 24/4 = 6 | **6 m/s** |

**El objeto C tiene la mayor velocidad** porque su línea tiene la mayor pendiente.

</details>

---

### **Ejercicio 6 — Regreso a casa**

Un objeto se mueve según la siguiente gráfica x-t. ¿Cuál es su velocidad?

<img src="/images/fisica/cinematica/graficas/ejercicio-6-regreso.svg" alt="Ejercicio 6: Regreso a casa" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

La velocidad es la **pendiente** de la gráfica x-t.

$$
v = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}
$$

Tomando los puntos $(0, 12)$ y $(6, 0)$:

$$
v = \frac{0 - 12}{6 - 0} = \frac{-12}{6} = -2\,\mathrm{m/s}
$$

> El objeto se mueve hacia atrás a **2 m/s**.

</details>

---

### **Ejercicio 7 — Ida y vuelta**

Calcula el desplazamiento total del objeto observando su gráfica v-t.

<img src="/images/fisica/cinematica/graficas/ejercicio-7-ida-vuelta.svg" alt="Ejercicio 7: Ida y vuelta" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

El desplazamiento es el **área bajo la curva**.

1.  **Área positiva (0-3s):** Rectángulo de $3 \times 4 = 12\,\mathrm{m}$.
2.  **Área negativa (3-6s):** Rectángulo de $3 \times (-4) = -12\,\mathrm{m}$.

$$
\Delta x_{\text{total}} = 12 + (-12) = 0\,\mathrm{m}
$$

> El objeto regresó a su punto de partida.

</details>

---

### **Ejercicio 8 — El despegue**

Un cohete acelera durante 5 segundos y luego mantiene su velocidad. Calcula su aceleración en la primera fase.

<img src="/images/fisica/cinematica/graficas/ejercicio-8-despegue.svg" alt="Ejercicio 8: Despegue" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

La aceleración es la **pendiente** de la gráfica v-t.

En el intervalo $t=0$ a $t=5$:
*   $v_i = 0$
*   $v_f = 10$

$$
a = \frac{10 - 0}{5 - 0} = 2\,\mathrm{m/s^2}
$$

</details>

---

### **Ejercicio 9 — El encuentro**

Dos corredores se mueven según la gráfica. ¿En qué momento y posición se encuentran?

<img src="/images/fisica/cinematica/graficas/ejercicio-9-encuentro.svg" alt="Ejercicio 9: El encuentro" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

El encuentro ocurre donde las líneas se **cruzan**.

Observando la gráfica, la intersección está en:
*   **Tiempo:** $t = 4\,\mathrm{s}$
*   **Posición:** $x = 8\,\mathrm{m}$

> Se encuentran a los 4 segundos en la marca de 8 metros.

</details>

---

### **Ejercicio 10 — Aceleración constante**

Si un objeto tiene esta gráfica de aceleración, ¿cuánto cambia su velocidad en 4 segundos?

<img src="/images/fisica/cinematica/graficas/ejercicio-10-aceleracion.svg" alt="Ejercicio 10: Aceleración constante" style="width: 100%; height: auto;">

<details>
<summary><strong>Ver solución</strong></summary>

El cambio de velocidad ($\Delta v$) es el **área bajo la gráfica a-t**.

$$
\Delta v = \text{base} \times \text{altura}
$$
$$
\Delta v = 4\,\mathrm{s} \times 3\,\mathrm{m/s^2} = 12\,\mathrm{m/s}
$$

> Su velocidad aumenta en **12 m/s**.

</details>

---

## 🔑 **Resumen**

![Resumen - Gráficas de movimiento](/images/fisica/cinematica/graficas/resumen-graficas.png)

*   **x vs t (Posición):**
    *   Pendiente = **Velocidad**.
    *   Recta inclinada = MRU.
    *   Parábola = MRUA.
*   **v vs t (Velocidad):**
    *   Pendiente = **Aceleración**.
    *   Área bajo la curva = **Desplazamiento**.
    *   Horizontal = MRU.
    *   Inclinada = MRUA.
*   **a vs t (Aceleración):**
    *   Área bajo la curva = **Cambio de velocidad**.
    *   En cero = MRU o Reposo.
    *   Constante (no cero) = MRUA.

# **Valores de Ángulos Cuadrantales**

Los **ángulos cuadrantales** son los reyes del círculo: 0°, 90°, 180° y 270°. Al coincidir exactamente con los ejes X e Y, sus valores son los más fáciles de calcular... ¡pero también los más fáciles de olvidar! Vamos a aprender a deducirlos sin memorizar.

---

## 🎯 ¿Qué vas a aprender?

- Qué son los ángulos cuadrantales y dónde se ubican.
- Cómo deducir sus valores de seno y coseno usando coordenadas $(x, y)$.
- Por qué algunas funciones como la tangente o secante se vuelven **indefinidas** (infinito).
- Un truco simple para recordar el patrón $0, 1, 0, -1$.

---

## 📍 Ubicación en el Círculo

Recuerda: El círculo unitario tiene radio **1**.
*   **0°** está "todo a la derecha".
*   **90°** está "todo arriba".
*   **180°** está "todo a la izquierda".
*   **270°** está "todo abajo".

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Los 4 ángulos cuadrantales</strong>
  </div>

![Ángulos cuadrantales](/images/trigonometria/circulo-unitario/angulos-cuadrantales.svg)

</div>

| Ángulo | Coordenada $(x, y)$ | $\cos$ ($x$) | $\sin$ ($y$) |
| :---: | :---: | :---: | :---: |
| **0°** | $(1, 0)$ | $1$ | $0$ |
| **90°** | $(0, 1)$ | $0$ | $1$ |
| **180°** | $(-1, 0)$ | $-1$ | $0$ |
| **270°** | $(0, -1)$ | $0$ | $-1$ |

---

## 🚫 El Misterio de las Indefiniciones

Algunas funciones implican **dividir**. Y ya sabes la regla de oro de matemáticas: **¡Prohibido dividir por cero!**

*   **Tangente** ($\sin/\cos$) falla cuando Coseno es 0 (en 90° y 270°).
*   **Cotangente** ($\cos/\sin$) falla cuando Seno es 0 (en 0° y 180°).

> **Indefinido** significa que el valor se dispara hacia infinito ($\infty$). En la gráfica, esto crea una asíntota vertical.

---

## 📊 Tabla Maestra

| Ángulo | $\sin$ | $\cos$ | $\tan$ | $\csc$ | $\sec$ | $\cot$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0°** | 0 | 1 | 0 | 🚫 | 1 | 🚫 |
| **90°** | 1 | 0 | 🚫 | 1 | 🚫 | 0 |
| **180°** | 0 | -1 | 0 | 🚫 | -1 | 🚫 |
| **270°** | -1 | 0 | 🚫 | -1 | 🚫 | 0 |

*(🚫 = Indefinido)*

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\sin(180°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
180° está a la izquierda.
El punto es $(-1, 0)$.
El seno es la coordenada $y$, que es 0.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 2
Calcula $\cos(270°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
270° está abajo.
El punto es $(0, -1)$.
El coseno es la coordenada $x$, que es 0.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 3
Calcula $\tan(90°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan = \sin / \cos$.
En 90°, $\cos = 0$.
Dividir por cero es imposible.

**Respuesta:** **Indefinido**
</details>

---

### Ejercicio 4
Calcula $\sec(180°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sec = 1 / \cos$.
En 180°, $\cos = -1$.
$1 / (-1) = -1$.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 5
Calcula $\sin(-90°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
-90° es lo mismo que 270° (abajo).
El punto es $(0, -1)$.
El seno es $y = -1$.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 6
Calcula $\csc(90°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\csc = 1 / \sin$.
En 90°, $\sin = 1$.
$1 / 1 = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 7
Calcula $\cot(270°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cot = \cos / \sin$.
En 270°, $\cos=0$ y $\sin=-1$.
$0 / (-1) = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 8
Calcula $\cos(720°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
720° son dos vueltas completas ($360 \times 2$).
Es equivalente a 0°.
$\cos(0°) = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 9
Calcula $\tan(180°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan = \sin / \cos$.
$\sin(180°) = 0$, $\cos(180°) = -1$.
$0 / (-1) = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 10
Determina si $\sec(90°)$ está definido.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sec = 1 / \cos$.
$\cos(90°) = 0$.
Dividir por cero es imposible.

**Respuesta:** **No (Indefinido)**
</details>

---

## 🔑 Resumen

| Ángulo | Seno | Coseno | ¿Por qué? |
| :---: | :---: | :---: | :--- |
| **0° / 360°** | **0** | **1** | Todo en X, nada en Y. |
| **90°** | **1** | **0** | Todo en Y, nada en X. |
| **180°** | **0** | **-1** | Todo en X (negativo). |
| **270°** | **-1** | **0** | Todo en Y (negativo). |

> **Conclusión:** Si la coordenada es 0, su función inversa (secante o cosecante) será indefinida. Si la coordenada es $\pm 1$, su inversa también será $\pm 1$.

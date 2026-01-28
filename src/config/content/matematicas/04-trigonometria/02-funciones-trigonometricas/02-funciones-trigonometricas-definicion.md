---
title: "Definición de Funciones Trigonométricas"
---

# **Definición de Funciones Trigonométricas**

Las razones trigonométricas que aprendiste con triángulos (cateto opuesto, hipotenusa...) tienen una limitación: solo sirven para ángulos entre 0° y 90°. ¿Qué pasa si el ángulo es de 120° o negativo? Aquí es donde el **Círculo Unitario** transforma esas razones en funciones completas.

---

## 🎯 ¿Qué vas a aprender?

- Cómo definir las 6 funciones trigonométricas para cualquier ángulo real.
- Cuáles son los dominios (entradas válidas) y rangos (salidas posibles) de cada función.
- El concepto de periodicidad: por qué las funciones se repiten.
- Las propiedades de paridad (simetría) de las funciones.

---

## 🏗️ De Razones a Funciones

En el círculo unitario, para cualquier ángulo $\theta$, tenemos un punto $P=(x,y)$ en la circunferencia.

| Función | Definición en Círculo | Definición Geométrica | Restricción |
|:---:|:---:|:---:|:---:|
| **Seno** ($\sin$) | $y$ | Altura | Ninguna |
| **Coseno** ($\cos$) | $x$ | Desplazamiento horizontal | Ninguna |
| **Tangente** ($\tan$) | $y/x$ | Pendiente del radio | $x \neq 0$ |
| **Cosecante** ($\csc$) | $1/y$ | Inverso del seno | $y \neq 0$ |
| **Secante** ($\sec$) | $1/x$ | Inverso del coseno | $x \neq 0$ |
| **Cotangente** ($\cot$) | $x/y$ | Inverso de tangente | $y \neq 0$ |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Las funciones en el círculo unitario</strong>
  </div>

![El punto P = (cos θ, sin θ)](/images/trigonometria/circulo-unitario/punto-cos-sin.svg)

</div>

---

## 📏 Dominio y Rango

No todas las funciones aceptan cualquier ángulo, ni producen cualquier valor.

### Seno y Coseno
Son las funciones "suaves" y continuas.
*   **Dominio:** Todos los números reales (puedes calcular seno de cualquier cosa).
*   **Rango:** $[-1, 1]$ (nunca salen de este intervalo).

### Tangente y Secante
Tienen problemas cuando $x=0$ (en 90°, 270°...).
*   **Dominio:** Todos los reales excepto $90° + k \cdot 180°$.
*   **Rango Tangente:** Todos los reales $(-\infty, \infty)$.
*   **Rango Secante:** $(-\infty, -1] \cup [1, \infty)$.

---

## 🔄 Periodicidad: Todo se repite

Como girar 360° te deja en el mismo lugar, los valores de las funciones se repiten cíclicamente.

> **Definición:** El **período** es el intervalo mínimo tras el cual la función se repite.

*   **Periodo $360°$ ($2\pi$):** Seno, Coseno, Secante, Cosecante.
*   **Periodo $180°$ ($\pi$):** Tangente, Cotangente (se repiten más rápido).

**Ejemplo:**
$$
\sin(390°) = \sin(30° + 360°) = \sin(30°)
$$

---

## 🪞 Paridad: Simetría

¿Qué pasa si cambias el signo del ángulo ($\theta \rightarrow -\theta$)?

### Funciones Pares (Simetría eje Y)
El signo negativo **desaparece**.
*   **Coseno:** $\cos(-\theta) = \cos(\theta)$
*   **Secante:** $\sec(-\theta) = \sec(\theta)$

### Funciones Impares (Simetría origen)
El signo negativo **sale fuera**.
*   **Seno:** $\sin(-\theta) = -\sin(\theta)$
*   **Tangente:** $\tan(-\theta) = -\tan(\theta)$
*   **Cosecante:** $\csc(-\theta) = -\csc(\theta)$
*   **Cotangente:** $\cot(-\theta) = -\cot(\theta)$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Para qué ángulos la función tangente **no** está definida?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La tangente es $y/x$. No existe cuando $x=0$.
En el círculo unitario, $x=0$ en los ángulos verticales (arriba y abajo).

**Respuesta:**
90°, 270°, 450°, etc. (En general: $90° + 180°k$).

</details>

---

### Ejercicio 2
Si $\sin(30°) = 0.5$, ¿cuánto vale $\sin(390°)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El periodo del seno es 360°.
$\sin(390°) = \sin(30° + 360°) = \sin(30°)$.

**Respuesta:**

$$
\boxed{0.5}
$$

</details>

---

### Ejercicio 3
Si $\cos(60°) = 0.5$, calcula $\cos(-60°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El coseno es una función **par**. El signo negativo del ángulo no afecta el resultado.
$\cos(-60°) = \cos(60°)$.

**Respuesta:**

$$
\boxed{0.5}
$$

</details>

---

### Ejercicio 4
Si $\sin(45°) \approx 0.707$, calcula $\sin(-45°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El seno es una función **impar**. El signo negativo sale afuera.
$\sin(-45°) = -\sin(45°)$.

**Respuesta:**

$$
\boxed{-0.707}
$$

</details>

---

### Ejercicio 5
Calcula el valor de $\sec(60°)$ sabiendo que $\cos(60°) = 0.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La secante es el recíproco del coseno ($\sec = 1/\cos$).
$\sec(60°) = 1 / 0.5$.

**Respuesta:**

$$
\boxed{2}
$$

</details>

---

### Ejercicio 6
Si $\tan(45°) = 1$, ¿cuánto vale $\tan(225°)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El periodo de la tangente es 180°.
$\tan(225°) = \tan(45° + 180°) = \tan(45°)$.

**Respuesta:**

$$
\boxed{1}
$$

</details>

---

### Ejercicio 7
Determina si la función cosecante está definida para el ángulo de 180°.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\csc(180°) = 1 / \sin(180°)$.
Sabemos que en 180° (izquierda), la altura $y$ (seno) es 0.
Dividir por cero es imposible.

**Respuesta:**
**No está definida**.

</details>

---

### Ejercicio 8
Si $\tan(30°) = 0.577$, ¿cuánto vale $\cot(30°)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La cotangente es el recíproco de la tangente ($1/\tan$).
$\cot(30°) = 1 / 0.577$.

**Respuesta:**

$$
\boxed{1.732}
$$

</details>

---

### Ejercicio 9
Sabiendo que $\sin(270°) = -1$, ¿cuánto vale $\csc(270°)$?

<details>
<summary>Ver solución</summary>

**Datos:**
$\sin = -1$.
$\csc = 1 / \sin$.

**Cálculo:**
$\csc(270°) = 1 / (-1)$.

**Respuesta:**

$$
\boxed{-1}
$$

</details>

---

### Ejercicio 10
Determina el signo de $\sec(120°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
120° está en el Cuadrante II.
En el Cuadrante II, el coseno ($x$) es negativo.
La secante ($1/x$) tiene el mismo signo que el coseno.

**Respuesta:**
**Negativo (-)**.

</details>

---

## 🔑 Resumen

| Característica | Seno / Coseno | Tangente | Secante / Cosecante |
| :--- | :--- | :--- | :--- |
| **Dominio** | Todo $\mathbb{R}$ | Con huecos cada 180° | Con huecos cada 180° |
| **Rango** | Limitado $[-1, 1]$ | Infinito $(-\infty, \infty)$ | Hueco en medio $(-\infty, -1] \cup [1, \infty)$ |
| **Período** | 360° | 180° | 360° |

> **Conclusión:** Las identidades de paridad y periodicidad son atajos poderosos. Te permiten calcular valores de ángulos grandes o negativos reduciéndolos simplemente a los valores básicos del primer cuadrante.

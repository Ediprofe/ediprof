---
title: "El Círculo Unitario"
---

# **El Círculo Unitario**

El **círculo unitario** es la herramienta fundamental para entender la trigonometría más allá de los triángulos. Nos permite definir el seno y el coseno para cualquier ángulo, incluso los negativos o mayores a 360°.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el círculo unitario y por qué es tan importante.
- Cómo las coordenadas $(x, y)$ se convierten en $(\cos\theta, \sin\theta)$.
- Cómo identificar los valores de las funciones trigonométricas en los cuatro cuadrantes.
- El valor del seno y coseno en los ángulos clave ($0°, 90°, 180°, ...$).

---

## 📋 Definición Fundamental

> **Definición:** El círculo unitario es una circunferencia de **radio 1** centrada en el **origen $(0,0)$** del plano cartesiano.

Su ecuación matemática es:

$$
x^2 + y^2 = 1
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">El Círculo Unitario</strong>
  </div>

![El círculo unitario](/images/trigonometria/circulo-unitario/circulo-unitario-basico.svg)

</div>

---

## 🔄 De Coordenadas a Trigonometría

Lo más poderoso del círculo unitario es que conecta la geometría (círculos) con la trigonometría. Si tomamos cualquier punto $P$ en el borde del círculo:

1.  La coordenada **X** representa el **Coseno**.
2.  La coordenada **Y** representa el **Seno**.

Para cualquier ángulo $\theta$:

$$
P = (\cos\theta, \sin\theta)
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">El punto P = (cos θ, sin θ)</strong>
  </div>

![Punto P en el círculo unitario](/images/trigonometria/circulo-unitario/punto-cos-sin.svg)

</div>

**¿Por qué funciona esto?**
Imagina un triángulo rectángulo dentro del círculo.
*   La hipotenusa es el radio = 1.
*   El cateto adyacente es $x$.
*   El cateto opuesto es $y$.

Entonces:

$$
\cos\theta = \frac{\text{Adyacente}}{\text{Hipotenusa}} = \frac{x}{1} = x
$$

$$
\sin\theta = \frac{\text{Opuesto}}{\text{Hipotenusa}} = \frac{y}{1} = y
$$

---

## 📍 Puntos Clave: Los Ejes

Si rotamos el punto a posiciones exactas sobre los ejes, podemos leer el seno y el coseno directamente de las coordenadas.

| Ángulo | Punto $(x, y)$ | $\cos$ (x) | $\sin$ (y) |
|--------|----------------|------------|------------|
| **0°** | $(1, 0)$ | $1$ | $0$ |
| **90°** | $(0, 1)$ | $0$ | $1$ |
| **180°** | $(-1, 0)$ | $-1$ | $0$ |
| **270°** | $(0, -1)$ | $0$ | $-1$ |
| **360°** | $(1, 0)$ | $1$ | $0$ |

---

## 🧭 Los Cuatro Cuadrantes

Dependiendo de dónde esté el punto, las coordenadas $x$ y $y$ cambian de signo. Esto determina el signo de las funciones trigonométricas.

| Cuadrante | Ángulo | $x$ ($\cos\theta$) | $y$ ($\sin\theta$) |
|-----------|--------|------------------|------------------|
| **I** | $0° < \theta < 90°$ | **+** | **+** |
| **II** | $90° < \theta < 180°$ | **−** | **+** |
| **III** | $180° < \theta < 270°$ | **−** | **−** |
| **IV** | $270° < \theta < 360°$ | **+** | **−** |

---

## 📐 Ángulos Notables (Cuadrante I)

Memorizar estos tres puntos te ayudará a deducir el resto del círculo.

| Ángulo | Radianes | Coordenadas $(\cos, \sin)$ |
|--------|----------|------------------------|
| **30°** | $\pi/6$ | $(\frac{\sqrt{3}}{2}, \frac{1}{2})$ |
| **45°** | $\pi/4$ | $(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$ |
| **60°** | $\pi/3$ | $(\frac{1}{2}, \frac{\sqrt{3}}{2})$ |

---

## 🧠 Identidad Fundamental

Como el punto $(x, y)$ está siempre sobre el círculo, siempre debe cumplir la ecuación $x^2 + y^2 = 1$. Sustituyendo $x$ y $y$:

$$
(\cos\theta)^2 + (\sin\theta)^2 = 1
$$

Esta es la identidad más famosa de la trigonometría:

$$
\cos^2\theta + \sin^2\theta = 1
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuáles son las coordenadas del punto en el círculo unitario para $\theta = 0°$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El ángulo de 0° está sobre el eje X positivo.
La distancia es el radio, que vale 1.

**Respuesta:**

$$
(1, 0)
$$

</details>

---

### Ejercicio 2
¿Cuáles son las coordenadas para $\theta = 90°$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El ángulo de 90° apunta verticalmente hacia arriba (eje Y positivo).

**Respuesta:**

$$
(0, 1)
$$

</details>

---

### Ejercicio 3
Encuentra el valor exacto de $\sin(270°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
270° apunta directamente hacia abajo (eje Y negativo).
El punto es $(0, -1)$.
El seno es la coordenada $y$.

**Respuesta:**

$$
\sin(270°) = -1
$$

</details>

---

### Ejercicio 4
Encuentra el valor exacto de $\cos(180°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
180° apunta a la izquierda (eje X negativo).
El punto es $(-1, 0)$.
El coseno es la coordenada $x$.

**Respuesta:**

$$
\cos(180°) = -1
$$

</details>

---

### Ejercicio 5
¿En qué cuadrante están el seno y el coseno ambos negativos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Necesitamos que $x < 0$ y $y < 0$.
Esto ocurre abajo a la izquierda.

**Respuesta:**
**Cuadrante III**.

</details>

---

### Ejercicio 6
Un punto en el círculo tiene coordenadas $P = (-0.6, 0.8)$. ¿Cuánto valen el seno y el coseno?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sabemos que $P = (\cos\theta, \sin\theta)$.
Simplemente leemos las coordenadas.

**Respuesta:**

$$
\cos\theta = -0.6, \quad \sin\theta = 0.8
$$

</details>

---

### Ejercicio 7
Si el ángulo es de 45°, ¿cuáles son sus coordenadas $(x, y)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Para 45°, los catetos son iguales y la hipotenusa es 1.
Los valores son $(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$.

**Respuesta:**

$$
\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)
$$

</details>

---

### Ejercicio 8
Determina si el punto $(\frac{1}{2}, \frac{1}{2})$ está sobre el círculo unitario.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Para estar en el círculo, debe cumplir $x^2 + y^2 = 1$.
$(\frac{1}{2})^2 + (\frac{1}{2})^2 = \frac{1}{4} + \frac{1}{4} = \frac{2}{4} = 0.5$.
Como $0.5 \neq 1$, no está en el círculo.

**Respuesta:**
**No**.

</details>

---

### Ejercicio 9
¿Cuál es el signo de $\cos(300°)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
300° está en el Cuadrante IV (entre 270° y 360°).
En este cuadrante, la $x$ es positiva y la $y$ es negativa.
El coseno es $x$.

**Respuesta:**
**Positivo (+)**.

</details>

---

### Ejercicio 10
Si $\sin\theta = 1$, ¿cuánto vale $\cos\theta$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $\sin\theta = 1$, estamos en el punto más alto del círculo $(0, 1)$, que corresponde a 90°.
La coordenada $x$ en ese punto es 0.

**Respuesta:**

$$
\cos\theta = 0
$$

</details>

---

## 🔑 Resumen

| Concepto | Relación | Significado |
| :--- | :---: | :--- |
| **Coseno** | Coordenada **X** | Desplazamiento horizontal del punto |
| **Seno** | Coordenada **Y** | Altura vertical del punto |
| **Radio** | **1** | La hipotenusa siempre vale 1 |
| **Ecuación** | $x^2+y^2=1$ | Identidad Pitagórica Fundamental |

> **Conclusión:** No necesitas memorizar tablas infinitas. Si recuerdas que el Coseno es X y el Seno es Y en un círculo de radio 1, puedes deducir el valor de cualquier ángulo visualizando su posición.

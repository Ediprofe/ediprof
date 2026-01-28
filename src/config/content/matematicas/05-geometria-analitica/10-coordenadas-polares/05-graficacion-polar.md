---
title: "Graficación en Coordenadas Polares"
---

# **Graficación en Coordenadas Polares**

Graficar en polares es como dibujar con un espirógrafo. En lugar de moverte de izquierda a derecha, das vueltas. Aprenderemos a detectar patrones antes de graficar punto por punto.

---

## 🎯 ¿Qué vas a aprender?

- Tests de Simetría (Eje Polar, Eje Normal, Polo).
- Cómo construir una tabla polar.
- Graficar cardioides y rosas paso a paso.

---

## 🦋 Concepto 1: Pruebas de Simetría

Antes de calcular mil puntos, verifica si la gráfica se repite como un espejo.

### 1. Simetría respecto al Eje Polar (Eje X)
Ocurre si al cambiar $\theta \to -\theta$ la ecuación no cambia. (Típico en funciones con **coseno**).
*   *Ejemplo 1.1:* $r = 2 \cos \theta$. Como $\cos(-\theta) = \cos(\theta)$, es simétrica arriba/abajo.

### 2. Simetría respecto al Eje Normal (Eje Y)
Ocurre si al cambiar $\theta \to \pi - \theta$ no cambia. (Típico en funciones con **seno**).
*   *Ejemplo 1.2:* $r = 4 \sin \theta$. $\sin(\pi-\theta) = \sin \theta$. Simétrica izq/der.

### 3. Simetría respecto al Polo (Origen)
Ocurre si al cambiar $r \to -r$ la ecuación se mantiene. (Típico en **lemniscata** $r^2 \dots$).
*   *Ejemplo 1.3:* $r^2 = 4 \sin(2\theta)$.
*   *Ejemplo 1.4:* $r = 3$ (Círculo). Simetría total.
*   *Ejemplo 1.5:* $r = 1 + \cos\theta$. Solo simétrica al Eje Polar.

---

## 📊 Concepto 2: Tabulación Estratégica

No elijas ángulos al azar. Usa los "ángulos notables" ($0, \pi/6, \pi/4, \pi/3, \pi/2$).

**5 Puntos Clave para Graficar $r = 1 + \cos \theta$ (Cardioide):**

| Ángulo $\theta$ | Cálculo | Radio $r$ | Punto Aprox |
| :--- | :--- | :--- | :--- |
| **$0^\circ$** | $1 + 1$ | 2 | $(2, 0^\circ)$ (Punta derecha) |
| **$60^\circ$** | $1 + 0.5$ | 1.5 | $(1.5, 60^\circ)$ |
| **$90^\circ$** | $1 + 0$ | 1 | $(1, 90^\circ)$ (Arriba) |
| **$120^\circ$** | $1 - 0.5$ | 0.5 | $(0.5, 120^\circ)$ |
| **$180^\circ$** | $1 - 1$ | 0 | $(0, 180^\circ)$ (En el Polo) |

*(Gracias a la simetría, solo calculamos la mitad superior y luego la reflejamos abajo).*

---

## 🌹 Concepto 3: Análisis de Rosas

Para dibujar $r = a \cos(n\theta)$, encuentra las "puntas de los pétalos" (donde $|r|$ es máximo).

**5 Ejemplos de Intersección:**

### Ejemplo 3.1
$r = 2 \cos(2\theta)$. (4 pétalos).
Máximo r=2 cuando $\cos(2\theta)=1 \Rightarrow 2\theta = 0 \Rightarrow \theta = 0$. Primer pétalo en el eje X.

### Ejemplo 3.2
$r = 4 \sin(3\theta)$. (3 pétalos).
Máximo r=4 cuando $\sin(3\theta)=1 \Rightarrow 3\theta = 90^\circ \Rightarrow \theta = 30^\circ$. Primer pétalo a $30^\circ$.

### Ejemplo 3.3
$r = 5 \cos(4\theta)$. (8 pétalos).
Primer pétalo en $0^\circ$. Separación entre pétalos: $360/8 = 45^\circ$.

### Ejemplo 3.4
$r = \sin(\theta)$. (1 "pétalo", es un círculo).
Máximo en $90^\circ$.

### Ejemplo 3.5
$r = \cos(5\theta)$. (5 pétalos).
Primer pétalo en $0^\circ$. Separación $72^\circ$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simetría de $r = 2$.

<details>
<summary>Ver solución</summary>
Total (Eje X, Y y Polo).
</details>

---

### Ejercicio 2
Simetría de $r = \sin \theta$.

<details>
<summary>Ver solución</summary>
Eje Y (Vertical).
</details>

---

### Ejercicio 3
Valor de $r$ en $180^\circ$ para $r = 1 + \sin \theta$.

<details>
<summary>Ver solución</summary>
$1 + 0 = 1$.
</details>

---

### Ejercicio 4
¿Pasa por el polo $r = \cos(2\theta)$?

<details>
<summary>Ver solución</summary>
Sí, cuando $\cos(2\theta)=0$ ($45^\circ$).
</details>

---

### Ejercicio 5
Ángulo del primer pétalo de $r = \sin(2\theta)$.

<details>
<summary>Ver solución</summary>
$2\theta = 90 \Rightarrow \theta = 45^\circ$.
</details>

---

### Ejercicio 6
Longitud del pétalo de $r = 5 \cos(3\theta)$.

<details>
<summary>Ver solución</summary>
5 unidades.
</details>

---

### Ejercicio 7
¿Qué curva es $r = 1 - \sin \theta$?

<details>
<summary>Ver solución</summary>
Cardioide (Hacia abajo).
</details>

---

### Ejercicio 8
Separación entre pétalos para $r = \cos(3\theta)$.

<details>
<summary>Ver solución</summary>
$360/3 = 120^\circ$.
</details>

---

### Ejercicio 9
Dibuja $r = \theta$ para $\theta > 0$.

<details>
<summary>Ver solución</summary>
Espiral saliendo del origen.
</details>

---

### Ejercicio 10
Valor mínimo de $r$ en $r = 2 + \cos \theta$.

<details>
<summary>Ver solución</summary>
$2 + (-1) = 1$. (La curva no toca el polo, es un caracol con agujero).
</details>

---

## 🔑 Resumen

| Simetría | Función Típica |
| :--- | :--- |
| **Eje Polar (X)** | Coseno ($\cos \theta$) |
| **Eje Normal (Y)** | Seno ($\sin \theta$) |
| **Polo** | Cuadrados ($r^2$) |

> **Conclusión:** No calcules a ciegas. Busca simetrías y ceros (donde $r=0$) primero. Eso te dará el esqueleto de la gráfica antes de poner un solo punto.

---
title: "Cónicas en Forma Paramétrica"
---

# **Cónicas en Forma Paramétrica**

Ya conocemos las ecuaciones "famosas" ($x^2+y^2=r^2$), pero a veces es más útil describir estas curvas usando un parámetro $t$ (que suele ser el ángulo). Esto es vital en física para describir el movimiento orbital y de proyectiles.

---

## 🎯 ¿Qué vas a aprender?

- Parametrizar Circunferencias y Elipses usando el ángulo.
- Parametrizar Parábolas e Hipérbolas.
- Cómo convertir entre ecuación cartesiana y paramétrica.

---

## 🔵 Concepto 1: Curvas Cerradas (Circunferencia y Elipse)

Usamos las identidades de **seno** y **coseno** porque oscilan y repiten, perfecto para figuras cerradas.

### Fórmulas Clave
*   **Circunferencia ($r$):**
    $$ x = r \cos t, \quad y = r \sin t $$
*   **Elipse ($a, b$):**
    $$ x = a \cos t, \quad y = b \sin t $$

**5 Ejemplos Prácticos:**

### Ejemplo 1.1: El Círculo Unitario
Ecuación: $x^2 + y^2 = 1$.
*   Radio $r=1$.
*   Paramétrica: $x = \cos t$, $y = \sin t$.

### Ejemplo 1.2: Elipse Horizontal
Ecuación: $\frac{x^2}{16} + \frac{y^2}{9} = 1$.
*   $a = 4$ (eje x), $b = 3$ (eje y).
*   Paramétrica:
    $$ x = 4 \cos t, \quad y = 3 \sin t $$

### Ejemplo 1.3: Círculo Desplazado
Cuya ecuación es $(x-2)^2 + (y+3)^2 = 25$.
*   Centro $(2, -3)$, Radio $5$.
*   Sumamos las coordenadas del centro a la fórmula básica.
*   Paramétrica:
    $$ x = 2 + 5 \cos t, \quad y = -3 + 5 \sin t $$

### Ejemplo 1.4: Elipse Vertical
Ecuación: $4x^2 + y^2 = 4$.
*   Normalizamos: $\frac{x^2}{1} + \frac{y^2}{4} = 1$.
*   $a=1, b=2$.
*   Paramétrica: $x = \cos t$, $y = 2 \sin t$.

### Ejemplo 1.5: Movimiento en Elipse
Una partícula se mueve tal que $x = 10 \cos(2\pi t)$, $y = 5 \sin(2\pi t)$.
*   Es una elipse de ancho 20 ($a=10$) y alto 10 ($b=5$).
*   El $2\pi t$ indica la velocidad angular (una vuelta por segundo).

---

## 🚀 Concepto 2: Curvas Abiertas (Parábola e Hipérbola)

Para curvas que van al infinito, usamos polinomios ($t, t^2$) o funciones como **secante y tangente**.

### Fórmulas Clave
*   **Parábola ($y^2 = 4px$):**
    $$ x = p t^2, \quad y = 2pt $$
    *(Truco: Sustituye y verás $(2pt)^2 = 4p(pt^2) \to 4p^2t^2 = 4p^2t^2$)*.
*   **Hipérbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$):**
    $$ x = a \sec t, \quad y = b \tan t $$
    *(Usa $\sec^2 t - \tan^2 t = 1$)*.

**5 Ejemplos Prácticos:**

### Ejemplo 2.1: Parábola Básica
Ecuación: $y^2 = 4x$ ($p=1$).
*   Paramétrica:
    $$ x = t^2, \quad y = 2t $$

### Ejemplo 2.2: Hipérbola Estándar
Ecuación: $\frac{x^2}{9} - \frac{y^2}{16} = 1$.
*   $a=3, b=4$.
*   Paramétrica:
    $$ x = 3 \sec t, \quad y = 4 \tan t $$

### Ejemplo 2.3: Parábola Libre ($x = y^2$)
Si queremos parametrizar $x = (y-1)^2$, podemos hacer simplemente:
*   Sea $y = t$.
*   Entonces $x = (t-1)^2$.
*   Es la forma más fácil para funciones.

### Ejemplo 2.4: Hipérbola Vertical
Ecuación: $\frac{y^2}{25} - \frac{x^2}{4} = 1$.
*   Ojo: aquí el positivo es $Y$. Usamos secante para $Y$.
*   Paramétrica:
    $$ x = 2 \tan t, \quad y = 5 \sec t $$

### Ejemplo 2.5: Proyectil (Parábola Física)
El movimiento clásico:
$$ x = v_0 t, \quad y = h - \frac{1}{2}gt^2 $$
*   Despejando $t = x/v_0$ y sustituyendo, obtienes la ecuación $y = ax^2 + bx + c$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Parametriza $x^2 + y^2 = 49$.

<details>
<summary>Ver solución</summary>
$r=7$.
$x = 7 \cos t, \ y = 7 \sin t$.
</details>

---

### Ejercicio 2
Ecuación cartesiana de $x = 3 \cos t, y = 3 \sin t$.

<details>
<summary>Ver solución</summary>
$x^2 + y^2 = 9$.
</details>

---

### Ejercicio 3
Parametriza la elipse $\frac{(x-1)^2}{4} + \frac{(y-2)^2}{9} = 1$.

<details>
<summary>Ver solución</summary>
$x = 1 + 2 \cos t, \ y = 2 + 3 \sin t$.
</details>

---

### Ejercicio 4
Parametriza $y = x^2$.

<details>
<summary>Ver solución</summary>
Sea $x = t$. Entonces $y = t^2$.
</details>

---

### Ejercicio 5
¿Qué curva es $x = \sec t, y = \tan t$?

<details>
<summary>Ver solución</summary>
Hipérbola unitaria ($x^2 - y^2 = 1$).
</details>

---

### Ejercicio 6
Parametriza hipérbola $x^2 - y^2 = 16$.

<details>
<summary>Ver solución</summary>
Divide por 16: $x^2/16 - y^2/16 = 1$. $a=4, b=4$.
$x = 4 \sec t, \ y = 4 \tan t$.
</details>

---

### Ejercicio 7
Si $x = \sin t, y = \cos t$, ¿es un círculo?

<details>
<summary>Ver solución</summary>
Sí. $x^2 + y^2 = \sin^2 + \cos^2 = 1$. Solo empieza en lugar diferente (eje Y) y gira al revés (horario).
</details>

---

### Ejercicio 8
Parametriza $y^2 = 12x$. ($4p=12 \to p=3$).

<details>
<summary>Ver solución</summary>
$x = 3t^2, \ y = 6t$.
</details>

---

### Ejercicio 9
Centro de la elipse $x = 5 + \cos t, y = -1 + 2 \sin t$.

<details>
<summary>Ver solución</summary>
$(5, -1)$.
</details>

---

### Ejercicio 10
Diferencia entre $y=x^2$ y $x=t^2, y=t^4$.

<details>
<summary>Ver solución</summary>
En la paramétrica $x$ nunca es negativo ($t^2 \ge 0$). Es media parábola.
</details>

---

## 🔑 Resumen

| Cónica | Parametrización Típica($t$) | Identidad Base |
| :--- | :--- | :--- |
| **Círculo/Elipse** | $\cos t, \sin t$ | $\cos^2 + \sin^2 = 1$ |
| **Hipérbola** | $\sec t, \tan t$ | $\sec^2 - \tan^2 = 1$ |
| **Parábola** | $t, t^2$ o $t^2, t$ | Algebraica |

> **Conclusión:** La forma paramétrica es el lenguaje del movimiento. Si la curva es el riel, la ecuación paramétrica te dice dónde está el tren en cada segundo.

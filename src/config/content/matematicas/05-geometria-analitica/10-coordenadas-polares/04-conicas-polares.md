---
title: "Cónicas en Coordenadas Polares"
---

# **Cónicas en Coordenadas Polares**

¿Recuerdas las complejas ecuaciones generales $Ax^2 + Bxy \dots$? En el mundo polar, todas esas curvas (elipses, parábolas, hipérbolas) se unifican en una sola ecuación elegante y compacta.

---

## 🎯 ¿Qué vas a aprender?

- La ecuación unificada: $r = \frac{ed}{1 \pm e \cos \theta}$.
- El papel clave de la excentricidad ($e$).
- Cómo identificar la cónica a simple vista.

---

## 👁️ Concepto 1: La Ecuación Maestra

Si colocamos uno de los focos de la cónica en el **Polo (Origen)**, la ecuación es:

$$ r = \frac{ed}{1 \pm e \cos \theta} \quad \text{o} \quad r = \frac{ed}{1 \pm e \sin \theta} $$

*   **$e$:** Excentricidad (Define la forma).
*   **$d$:** Distancia del foco a la directriz.
*   **$\cos \theta$:** Cónica horizontal (Eje focal en X).
*   **$\sin \theta$:** Cónica vertical (Eje focal en Y).

Veamos **5 ejemplos de lectura**:

### Ejemplo 1.1
$$ r = \frac{2}{1 + \cos \theta} $$
*   Aquí $e=1$.
*   Es una **Parábola**.

### Ejemplo 1.2
$$ r = \frac{6}{2 + \cos \theta} $$
*   *Truco:* El "1" debe ser un 1. Dividimos todo por 2.
    $$ r = \frac{3}{1 + 0.5 \cos \theta} $$
*   $e = 0.5$. Como $e < 1$, es una **Elipse**.

### Ejemplo 1.3
$$ r = \frac{10}{1 - 3 \sin \theta} $$
*   $e = 3$. Como $e > 1$, es una **Hipérbola**.
*   Vertical (por el seno).

### Ejemplo 1.4
$$ r = \frac{4}{1 - \cos \theta} $$
*   $e = 1$. Es una **Parábola**.
*   Abre hacia la derecha (por el signo menos).

### Ejemplo 1.5
$$ r = \frac{5}{1 + 0 \cos \theta} = 5 $$
*   $e = 0$. Es una **Circunferencia** ($r=5$).

---

## 🔍 Concepto 2: Clasificación por Excentricidad

La $e$ es el ADN de la curva.

| Valor de $e$ | Cónica |
| :--- | :--- |
| **$e = 0$** | Circunferencia |
| **$0 < e < 1$** | Elipse |
| **$e = 1$** | Parábola |
| **$e > 1$** | Hipérbola |

**5 Ejemplos de Identificación Rápida:**

### Ejemplo 2.1
$r = \frac{8}{4 - 3 \cos \theta}$.
Dividir por 4: $r = \frac{2}{1 - 0.75 \cos \theta}$.
$e = 0.75 \to$ **Elipse**.

### Ejemplo 2.2
$r = \frac{12}{3 + 4 \sin \theta}$.
Dividir su denominador para dejar un 1: $r = \frac{4}{1 + 1.33 \sin \theta}$.
$e = 1.33 \to$ **Hipérbola**.

### Ejemplo 2.3
$r = \frac{1}{1 + \sin \theta}$.
$e = 1 \to$ **Parábola**.

### Ejemplo 2.4
$r = 3 / (2 + 2\cos\theta)$.
$e = 1 \to$ **Parábola**.

### Ejemplo 2.5
$r = 5 / (5 - \cos\theta)$.
$r = 1 / (1 - 0.2\cos\theta)$. $e=0.2 \to$ **Elipse**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica $r = \frac{4}{1 + 2\sin\theta}$.

<details>
<summary>Ver solución</summary>
$e=2 \to$ Hipérbola (Vertical).
</details>

---

### Ejercicio 2
Identifica $r = \frac{2}{1 + \cos\theta}$.

<details>
<summary>Ver solución</summary>
$e=1 \to$ Parábola (Horizontal).
</details>

---

### Ejercicio 3
Identifica $r = \frac{3}{1 - 0.5\cos\theta}$.

<details>
<summary>Ver solución</summary>
$e=0.5 \to$ Elipse.
</details>

---

### Ejercicio 4
Si hay $\sin \theta$, ¿cuál es el eje focal?

<details>
<summary>Ver solución</summary>
Eje Y (Vertical, $\pi/2$).
</details>

---

### Ejercicio 5
Calcula $d$ en $r = \frac{6}{1 + 2\cos\theta}$.

<details>
<summary>Ver solución</summary>
Numerador $ed = 6$. Como $e=2$, entonces $2d=6 \Rightarrow d=3$.
</details>

---

### Ejercicio 6
Ecuación de parábola con $d=2$ (Horizontal +).

<details>
<summary>Ver solución</summary>
$e=1$. $r = \frac{1(2)}{1 + \cos\theta} = \frac{2}{1 + \cos\theta}$.
</details>

---

### Ejercicio 7
¿Dónde está el foco en estas ecuaciones?

<details>
<summary>Ver solución</summary>
En el Polo $(0,0)$.
</details>

---

### Ejercicio 8
Excentricidad de $r = 10$.

<details>
<summary>Ver solución</summary>
$0$.
</details>

---

### Ejercicio 9
Identifica $r = \frac{5}{2 - 2\sin\theta}$.

<details>
<summary>Ver solución</summary>
$r = \frac{2.5}{1 - \sin\theta}$. $e=1 \to$ Parábola.
</details>

---

### Ejercicio 10
Significado de $d$.

<details>
<summary>Ver solución</summary>
Distancia Foco-Directriz.
</details>

---

## 🔑 Resumen

| Ecuación | Truco |
| :--- | :--- |
| **Normalizar** | Divide todo para que el primer número del denominador sea un **1**. |
| **Leer $e$** | El coeficiente de la función trigonométrica es tu excentricidad. |

> **Conclusión:** Si vas a modelar órbitas de planetas o cometas (Elipses), las coordenadas polares con el sol en el foco son la única opción sensata.

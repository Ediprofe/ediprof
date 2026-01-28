---
title: "Representación de vectores en el plano"
---

# Representación de vectores en el plano

Los vectores pueden representarse en un **plano cartesiano**, lo que permite visualizar su magnitud, dirección y sentido de manera precisa, y realizar operaciones matemáticas con ellos.

---

## 📘 Idea intuitiva: ¿qué muestra un vector?

Un vector se visualiza como una flecha que resume tres elementos: **magnitud**, **dirección** y **sentido**. En adelante usaremos el mismo ejemplo en todas las secciones para mantener la progresión natural.

---

## 🎯 ¿Qué vas a aprender?

- Cómo representar un vector en el plano cartesiano
- Qué son las componentes de un vector ($A_x$ y $A_y$)
- Cómo calcular la magnitud usando el teorema de Pitágoras
- Cómo encontrar las componentes a partir del ángulo

---

## 📊 **Vector en el plano cartesiano**

Un vector en el plano se puede ubicar con dos puntos:

- **Origen (cola):** donde empieza el vector
- **Extremo (punta):** donde termina el vector

### Ejemplo:

Si un vector $\vec{A}$ parte del origen $O(0,0)$ y llega al punto $P(4,3)$:

$$
\vec{A} = \overrightarrow{OP}
$$

Esto significa que el vector "va desde $(0,0)$ hasta $(4,3)$".

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/fisica/vectores/vector-plano.svg" alt="Vector en el plano cartesiano" style="width: 100%; height: auto;" />
</div>

> Observa la **magnitud** (longitud), la **dirección** (ángulo θ) y el **sentido** (punta) resaltados en la ilustración.

> 💡 La **longitud de la flecha** representa la magnitud, la **inclinación** muestra la dirección, y la **punta** indica el sentido.

---

## 📐 **Componentes de un vector**

Todo vector en el plano puede descomponerse en dos **componentes perpendiculares**:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

Donde:
- $A_x$ = **componente horizontal** (proyección sobre el eje $x$)
- $A_y$ = **componente vertical** (proyección sobre el eje $y$)
- $\hat{i}$ y $\hat{j}$ = **vectores unitarios** en las direcciones $x$ y $y$

### Visualización:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/fisica/vectores/componentes-vector.svg" alt="Componentes de un vector" style="width: 100%; height: auto;" />
</div>

> 💡 Las componentes $A_x$ y $A_y$ forman un **triángulo rectángulo** con el vector $\vec{A}$.

---

## 📏 **Magnitud del vector**

La **magnitud** del vector se calcula con el **teorema de Pitágoras**:

$$
|\vec{A}| = \sqrt{A_x^2 + A_y^2}
$$

### Ejemplo:

Si $\vec{A} = 4\,\hat{i} + 3\,\hat{j}$, entonces:

$$
|\vec{A}| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5
$$

---

## 🔄 **Componentes a partir del ángulo**

Si conoces la **magnitud** $|\vec{A}|$ y el **ángulo** $\theta$ que forma con el eje $x$:

$$
A_x = |\vec{A}| \cos\theta
$$

$$
A_y = |\vec{A}| \sin\theta
$$

### Ejemplo (mismo vector del plano):

Para $\vec{A}$ que va de $O(0,0)$ a $P(4,3)$, su magnitud es $|\vec{A}| = 5$ y su ángulo es $\theta = \tan^{-1}(3/4) \approx 36.87°$.

**Componentes:**

$$
A_x = |\vec{A}|\cos\theta = 5\cdot\frac{4}{5} = 4
$$

$$
A_y = |\vec{A}|\sin\theta = 5\cdot\frac{3}{5} = 3
$$

**Representación:**

$$
\vec{A} = 4\,\hat{i} + 3\,\hat{j}
$$

> 💡 **Relación útil:** para este vector, $\cos\theta = 4/5$ y $\sin\theta = 3/5$.

---

## 📐 **Ángulo a partir de las componentes**

Si conoces las componentes y quieres encontrar el ángulo:

$$
\theta = \tan^{-1}\left(\frac{A_y}{A_x}\right)
$$

### Ejemplo (mismo vector del plano):

Si $\vec{A} = 4\,\hat{i} + 3\,\hat{j}$:

$$
\theta = \tan^{-1}\left(\frac{3}{4}\right) \approx 36.87°
$$

---

## 📋 **Tabla resumen: Dos formas de expresar un vector**

| Forma | Notación | Información |
| :--- | :--- | :--- |
| **Por componentes** | $\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}$ | Componentes en $x$ y $y$ |
| **Por magnitud y ángulo** | $(|\vec{A}|, \theta)$ | Magnitud y dirección |

> 🔄 Ambas formas representan el **mismo vector**. Puedes convertir de una a otra usando las fórmulas anteriores.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Un vector tiene componentes $A_x = 6$ y $A_y = 8$. Calcula su magnitud.**

<details>
<summary>Ver solución</summary>

$$
|\vec{A}| = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10
$$

</details>

---

### Ejercicio 2
**Un vector tiene magnitud $|\vec{B}| = 13\,\mathrm{m}$ y forma un ángulo de $53°$ con el eje $x$. Encuentra sus componentes.**

*Datos útiles:* $\cos 53° \approx 0.6$, $\sin 53° \approx 0.8$

<details>
<summary>Ver solución</summary>

$$
B_x = 13 \times 0.6 = 7.8\,\mathrm{m}
$$

$$
B_y = 13 \times 0.8 = 10.4\,\mathrm{m}
$$

$$
\vec{B} = 7.8\,\hat{i} + 10.4\,\hat{j}
$$

</details>

---

### Ejercicio 3
**Un vector es $\vec{C} = 5\,\hat{i} + 5\,\hat{j}$. Calcula su magnitud y el ángulo que forma con el eje $x$.**

<details>
<summary>Ver solución</summary>

**Magnitud:**

$$
|\vec{C}| = \sqrt{5^2 + 5^2} = \sqrt{50} = 5\sqrt{2} \approx 7.07
$$

**Ángulo:**

$$
\theta = \tan^{-1}\left(\frac{5}{5}\right) = \tan^{-1}(1) = 45°
$$

</details>

---

### Ejercicio 4
**¿Por qué es útil expresar un vector por sus componentes en lugar de solo dar su magnitud y dirección?**

<details>
<summary>Ver solución</summary>

Porque las **componentes facilitan las operaciones matemáticas**:

- Para **sumar vectores**, simplemente sumamos las componentes correspondientes
- Para **restar vectores**, restamos las componentes
- Para calcular el **trabajo** de una fuerza, multiplicamos la componente paralela por la distancia

Además, muchos problemas de física involucran movimiento en ejes perpendiculares (horizontal y vertical), y trabajar con componentes permite analizar cada dirección por separado.

</details>

---

## 🔑 Resumen

| Concepto | Fórmula |
| :--- | :--- |
| **Componentes** | $\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}$ |
| **Magnitud** | $\vert\vec{A}\vert = \sqrt{A_x^2 + A_y^2}$ |
| **Componente X** | $A_x = \vert\vec{A}\vert \cos\theta$ |
| **Componente Y** | $A_y = \vert\vec{A}\vert \sin\theta$ |
| **Ángulo** | $\theta = \tan^{-1}(A_y / A_x)$ |

> **Recuerda:** Un vector en el plano puede expresarse como **componentes** $(A_x, A_y)$ o como **magnitud y ángulo** $(|\vec{A}|, \theta)$. Ambas formas contienen la misma información.

---
title: "Suma y resta de vectores"
---

# Suma y resta de vectores

En física es común combinar fuerzas, velocidades o desplazamientos. Para hacerlo, utilizamos la **suma y resta de vectores**.

---

## 🎯 ¿Qué vas a aprender?

- A sumar vectores usando diferentes métodos
- A restar vectores usando el concepto del vector opuesto
- A calcular la magnitud y dirección del vector resultante
- El método analítico (por componentes)

---

## 🤔 **¿Por qué sumar vectores?**

Imagina que estás nadando en un río:
- Nadas hacia la orilla opuesta a $2\,\mathrm{m/s}$
- La corriente te empuja río abajo a $3\,\mathrm{m/s}$

¿Hacia dónde te mueves realmente? ¿A qué velocidad?

Para responder, necesitas **sumar los vectores** de velocidad. ¡Eso es lo que aprenderemos!

---

## ➡️ **Caso 1: Vectores en la misma línea**

### a) Mismo sentido (suma)

Si dos vectores apuntan en el **mismo sentido**, la magnitud del resultante es la **suma**:

![alt text](/images/fisica/vectores/suma.png)

$$
|\vec{R}| = |\vec{A}| + |\vec{B}| = 3 + 2 = 5
$$

### b) Sentidos opuestos (resta)

Si apuntan en **sentidos opuestos**, la magnitud del resultante es la **diferencia**:

![alt text](/images/fisica/vectores/resta.png)

$$
|\vec{R}| = |\vec{A}| - |\vec{B}| = 5 - 2 = 3
$$

> 💡 **Analogía:** Es como una competencia de tira y afloja. Si un equipo jala con 5 unidades y el otro con 2, gana el primero con fuerza neta de 3.

---

## 🔺 **Caso 2: Método del triángulo (punta a cola)**

Cuando los vectores **no están en línea**, usamos métodos gráficos.

### Pasos:

1. Dibuja el vector $\vec{A}$ desde el origen
2. Desde la **punta de A**, dibuja el vector $\vec{B}$
3. El resultante $\vec{R}$ va desde el **origen** hasta la **punta de B**
 
 <div class="image-card">
   <img src="/images/fisica/vectores/suma-triangulo.svg" alt="Método del triángulo para suma de vectores" />
 </div>
 
 > 💡 **Analogía:** Es como caminar. Primero caminas en dirección A, luego en dirección B. El resultante es el camino directo desde donde empezaste hasta donde terminaste.

---

## ▱ **Caso 3: Método del paralelogramo**

Otra forma de sumar vectores:

### Pasos:

1. Dibuja ambos vectores desde el **mismo punto** (origen común)
2. Completa el **paralelogramo** usando los vectores como lados
3. La **diagonal** desde el origen es el vector resultante

<div class="image-card">
  <img src="/images/fisica/vectores/suma-paralelogramo.svg" alt="Método del paralelogramo para suma de vectores" />
</div>

> 💡 Ambos métodos (triángulo y paralelogramo) dan el **mismo resultado**.

---

## 📐 **Caso 4: Vectores perpendiculares**

Cuando los vectores forman un **ángulo de 90°**, usamos el **teorema de Pitágoras**:

$$
|\vec{R}| = \sqrt{|\vec{A}|^2 + |\vec{B}|^2}
$$

### Ejemplo:

Si $|\vec{A}| = 3$ y $|\vec{B}| = 4$ forman 90°:

$$
|\vec{R}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

La dirección del resultante:

$$
\theta = \tan^{-1}\left(\frac{4}{3}\right) \approx 53°
$$

---

## 🧮 **Método analítico (por componentes)**

Este es el método **más útil y exacto** para sumar vectores de cualquier dirección.

### Paso 1: Expresar cada vector en componentes

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

$$
\vec{B} = B_x\,\hat{i} + B_y\,\hat{j}
$$

### Paso 2: Sumar componente a componente

$$
\vec{R} = (A_x + B_x)\,\hat{i} + (A_y + B_y)\,\hat{j}
$$

### Paso 3: Calcular magnitud y dirección

$$
|\vec{R}| = \sqrt{R_x^2 + R_y^2}
$$

$$
\theta = \tan^{-1}\left(\frac{R_y}{R_x}\right)
$$

### Ejemplo completo:

Dados:
$$
\vec{A} = 6\,\hat{i} + 3\,\hat{j}, \quad \vec{B} = 2\,\hat{i} + 5\,\hat{j}
$$

**Suma:**
$$
\vec{R} = (6+2)\,\hat{i} + (3+5)\,\hat{j} = 8\,\hat{i} + 8\,\hat{j}
$$

**Magnitud:**
$$
|\vec{R}| = \sqrt{8^2 + 8^2} = \sqrt{128} \approx 11.3
$$

**Dirección:**
$$
\theta = \tan^{-1}\left(\frac{8}{8}\right) = 45°
$$

---

## ➖ **Resta de vectores**

Restar un vector equivale a **sumar su opuesto**:

$$
\vec{A} - \vec{B} = \vec{A} + (-\vec{B})
$$

El vector $-\vec{B}$ tiene la **misma magnitud** que $\vec{B}$ pero **sentido contrario**.

### Por componentes:

$$
\vec{A} - \vec{B} = (A_x - B_x)\,\hat{i} + (A_y - B_y)\,\hat{j}
$$

### Ejemplo:

$$
\vec{A} = 4\,\hat{i} + 3\,\hat{j}, \quad \vec{B} = 2\,\hat{i} + 1\,\hat{j}
$$

$$
\vec{A} - \vec{B} = (4-2)\,\hat{i} + (3-1)\,\hat{j} = 2\,\hat{i} + 2\,\hat{j}
$$

---

## 🏊 **Ejemplo aplicado: El nadador**

Volvamos al problema del inicio:

- Velocidad del nadador: $\vec{v}_n = 2\,\hat{j}$ (hacia arriba)
- Velocidad de corriente: $\vec{v}_c = 3\,\hat{i}$ (hacia la derecha)

**Velocidad resultante:**

$$
\vec{v}_R = 3\,\hat{i} + 2\,\hat{j}
$$

**Magnitud:**

$$
|\vec{v}_R| = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3.6\,\mathrm{m/s}
$$

**Dirección:**

$$
\theta = \tan^{-1}\left(\frac{2}{3}\right) \approx 33.7°
$$

> ✅ **Respuesta:** El nadador se mueve a **3.6 m/s** en dirección **33.7° respecto a la corriente**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Dos fuerzas de 5 N y 12 N actúan perpendicularmente sobre un objeto. ¿Cuál es la fuerza resultante?**

<details>
<summary>Ver solución</summary>

$$
|\vec{R}| = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13\,\mathrm{N}
$$

</details>

---

### Ejercicio 2
**Si $\vec{A} = 4\,\hat{i} + 3\,\hat{j}$ y $\vec{B} = 2\,\hat{i} - 1\,\hat{j}$, calcula $\vec{A} + \vec{B}$.**

<details>
<summary>Ver solución</summary>

$$
\vec{R} = (4+2)\,\hat{i} + (3+(-1))\,\hat{j} = 6\,\hat{i} + 2\,\hat{j}
$$

</details>

---

### Ejercicio 3
**Calcula $\vec{A} - \vec{B}$ con los vectores del ejercicio anterior.**

<details>
<summary>Ver solución</summary>

$$
\vec{R} = (4-2)\,\hat{i} + (3-(-1))\,\hat{j} = 2\,\hat{i} + 4\,\hat{j}
$$

</details>

---

### Ejercicio 4
**Un auto viaja 40 km al este y luego 30 km al norte. ¿Cuál es el desplazamiento total (magnitud y dirección)?**

<details>
<summary>Ver solución</summary>

**Magnitud:**

$$
|\vec{R}| = \sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50\,\mathrm{km}
$$

**Dirección:**

$$
\theta = \tan^{-1}\left(\frac{30}{40}\right) = \tan^{-1}(0.75) \approx 36.9°
$$

El desplazamiento es de **50 km** en dirección **36.9° al norte del este**.

</details>

---

## 🔑 Resumen

| Situación | Método |
| :--- | :--- |
| Vectores en línea (mismo sentido) | Suma de magnitudes |
| Vectores en línea (opuestos) | Resta de magnitudes |
| Vectores en ángulo cualquiera | Triángulo, Paralelogramo, o Analítico |
| Vectores perpendiculares (90°) | Teorema de Pitágoras |
| Resta de vectores | Sumar el opuesto: $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$ |

| Operación | Fórmula por componentes |
| :--- | :--- |
| **Suma** | $\vec{R} = (A_x + B_x)\,\hat{i} + (A_y + B_y)\,\hat{j}$ |
| **Resta** | $\vec{R} = (A_x - B_x)\,\hat{i} + (A_y - B_y)\,\hat{j}$ |
| **Magnitud** | $\vert\vec{R}\vert = \sqrt{R_x^2 + R_y^2}$ |
| **Dirección** | $\theta = \tan^{-1}(R_y / R_x)$ |

> **Recuerda:** Los vectores se suman gráficamente (punta a cola o paralelogramo) o analíticamente (sumando componentes). Restar un vector equivale a sumar su opuesto.

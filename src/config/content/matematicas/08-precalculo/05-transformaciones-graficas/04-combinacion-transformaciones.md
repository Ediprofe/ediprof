---
title: "Combinación de Transformaciones"
---

# Combinación de Transformaciones

En la práctica, las funciones suelen tener múltiples transformaciones aplicadas. Dominar el orden correcto es esencial para analizar y graficar cualquier función.

---

## 🎯 ¿Qué vas a aprender?

- El orden correcto de las transformaciones
- Cómo descomponer una función transformada
- Graficar paso a paso
- Ir de la gráfica a la ecuación

---

## 📖 Forma general de transformaciones

$$g(x) = a \cdot f(b(x - h)) + k$$

| Parámetro | Transformación | Orden |
|-----------|----------------|-------|
| $h$ | Desplazamiento horizontal | 1° (horizontal) |
| $b$ | Compresión/estiramiento horizontal | 2° (horizontal) |
| $a$ | Compresión/estiramiento vertical + reflexión X | 3° (vertical) |
| $k$ | Desplazamiento vertical | 4° (vertical) |

---

## 📖 Orden de aplicación

### Al graficar (desde $f$ hacia $g$):

**Transformaciones horizontales primero** (en orden inverso de como aparecen):
1. Desplazamiento horizontal
2. Estiramiento/compresión horizontal
3. Reflexión en eje Y (si $b < 0$)

**Luego transformaciones verticales**:
4. Estiramiento/compresión vertical
5. Reflexión en eje X (si $a < 0$)
6. Desplazamiento vertical

### 💡 Regla práctica

Trabaja "de adentro hacia afuera":
- Primero lo que afecta a $x$
- Luego lo que afecta a $f(x)$

---

## ⚙️ Ejemplo 1: Análisis completo

Identifica todas las transformaciones de:

$$g(x) = -2(x + 3)^2 - 1$$

desde $f(x) = x^2$.

**Paso 1:** Identificamos parámetros
- Forma: $a \cdot f(x - h) + k$
- $a = -2$
- $h = -3$ (porque $x + 3 = x - (-3)$)
- $k = -1$

**Paso 2:** Describimos transformaciones
1. Desplazamiento 3 unidades a la **izquierda**
2. Estiramiento vertical por factor 2
3. Reflexión en el eje X
4. Desplazamiento 1 unidad hacia **abajo**

**Resultado:**
- Vértice: $(-3, -1)$
- Abre hacia abajo
- Más angosta que $x^2$

---

## ⚙️ Ejemplo 2: Con factor horizontal

Analiza $h(x) = \sqrt{2x - 6} + 4$ desde $f(x) = \sqrt{x}$.

**Paso 1:** Factorizamos el argumento
$$h(x) = \sqrt{2(x - 3)} + 4$$

**Parámetros:**
- $b = 2$: Compresión horizontal por $\frac{1}{2}$
- $h = 3$: Desplazamiento 3 a la derecha
- $k = 4$: Desplazamiento 4 hacia arriba

**Punto inicial:** De $(0, 0)$ a $(3, 4)$

**Dominio:** $2(x - 3) \geq 0 \Rightarrow x \geq 3$

---

## ⚙️ Ejemplo 3: Graficar paso a paso

Grafica $g(x) = -|x - 2| + 3$ partiendo de $f(x) = |x|$.

**Transformaciones:**

| Paso | Función | Descripción |
|------|---------|-------------|
| 0 | $\|x\|$ | Función base |
| 1 | $\|x - 2\|$ | Derecha 2 |
| 2 | $-\|x - 2\|$ | Reflexión en X |
| 3 | $-\|x - 2\| + 3$ | Arriba 3 |

**Puntos clave:**

| Paso | Vértice |
|------|---------|
| 0 | $(0, 0)$ |
| 1 | $(2, 0)$ |
| 2 | $(2, 0)$ |
| 3 | $(2, 3)$ |

**Resultado final:** V invertida con vértice en $(2, 3)$, abriendo hacia abajo.

---

## 📖 De la gráfica a la ecuación

### ⚙️ Ejemplo 4: Encontrar la ecuación

Una parábola tiene vértice en $(1, -4)$ y pasa por $(3, 0)$. Encuentra su ecuación.

**Paso 1:** Forma del vértice
$$y = a(x - 1)^2 - 4$$

**Paso 2:** Usamos el punto $(3, 0)$
$$0 = a(3 - 1)^2 - 4$$
$$0 = 4a - 4$$
$$a = 1$$

**Ecuación:** $y = (x - 1)^2 - 4$

---

## ⚙️ Ejemplo 5: Función raíz transformada

La gráfica de una función raíz tiene punto inicial en $(-2, 5)$ y pasa por $(2, 3)$. Encuentra la ecuación.

**Paso 1:** Forma general
$$y = a\sqrt{x - h} + k = a\sqrt{x - (-2)} + 5 = a\sqrt{x + 2} + 5$$

**Paso 2:** Usamos $(2, 3)$
$$3 = a\sqrt{2 + 2} + 5$$
$$3 = 2a + 5$$
$$a = -1$$

**Ecuación:** $y = -\sqrt{x + 2} + 5$

La función está reflejada hacia abajo.

---

## 📊 Tabla resumen de efectos

| Cambio en ecuación | Efecto en gráfica |
|-------------------|-------------------|
| $f(x) \to f(x) + k$ | Sube ($k > 0$) o baja ($k < 0$) |
| $f(x) \to f(x - h)$ | Derecha ($h > 0$) o izquierda ($h < 0$) |
| $f(x) \to af(x)$ | Estira ($\|a\| > 1$) o comprime ($\|a\| < 1$) |
| $f(x) \to -f(x)$ | Refleja en eje X |
| $f(x) \to f(-x)$ | Refleja en eje Y |
| $f(x) \to f(bx)$ | Comprime ($\|b\| > 1$) o estira ($\|b\| < 1$) |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Describe todas las transformaciones y encuentra el punto clave:

a) $g(x) = 3(x - 1)^2 + 2$ desde $f(x) = x^2$
b) $h(x) = -\sqrt{x + 4} - 1$ desde $f(x) = \sqrt{x}$
c) $k(x) = |2x - 6| + 3$ desde $f(x) = |x|$

<details>
<summary>Ver soluciones</summary>

a) Derecha 1, estiramiento vertical ×3, arriba 2. Vértice: $(1, 2)$

b) Izquierda 4, reflexión X, abajo 1. Punto inicial: $(-4, -1)$

c) Reescribimos: $|2(x - 3)| + 3$
   
   Derecha 3, compresión horizontal $\frac{1}{2}$, arriba 3. Vértice: $(3, 3)$
</details>

---

**Ejercicio 2:** Escribe la ecuación:

a) $f(x) = x^2$ desplazada 2 a la izquierda, estirada verticalmente ×4, y desplazada 5 hacia abajo
b) $f(x) = |x|$ reflejada en X, desplazada 3 a la derecha, y 2 hacia arriba

<details>
<summary>Ver soluciones</summary>

a) $g(x) = 4(x + 2)^2 - 5$

b) $g(x) = -|x - 3| + 2$
</details>

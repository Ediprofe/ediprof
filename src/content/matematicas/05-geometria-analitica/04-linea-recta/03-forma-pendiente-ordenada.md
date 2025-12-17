# Forma Pendiente-Ordenada al Origen

La forma más común de escribir la ecuación de una recta es la **forma pendiente-ordenada** (también llamada forma explícita). Es especialmente útil porque muestra directamente la pendiente y el punto donde la recta cruza el eje Y.

---

## 🎯 ¿Qué vas a aprender?

- La forma $y = mx + b$ y su significado
- Cómo identificar la pendiente y el intercepto
- Cómo graficar rápidamente usando esta forma

---

## 📖 Lo Esencial de Pendiente-Ordenada

| Elemento | Símbolo | Significado |
|----------|---------|-------------|
| Pendiente | $m$ | Inclinación de la recta |
| Ordenada al origen | $b$ | Donde cruza el eje Y |
| Forma completa | $y = mx + b$ | Ecuación explícita |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/pendiente-ordenada.svg" alt="Forma pendiente-ordenada" style="width: 100%; height: auto;" />
</div>

---

## 📖 La Forma Pendiente-Ordenada

La ecuación de una recta en **forma pendiente-ordenada** es:

$$
y = mx + b
$$

donde:
- $m$ es la **pendiente** de la recta
- $b$ es la **ordenada al origen** (el valor de $y$ cuando $x = 0$)

> 💡 El punto $(0, b)$ es donde la recta **cruza el eje Y**.

### ¿Por qué es tan útil?

1. **Lees directamente:** La pendiente ($m$) y el intercepto ($b$)
2. **Graficas fácilmente:** Empiezas en $(0, b)$ y usas la pendiente
3. **Comparas rectas:** Paralelas tienen igual $m$

---

## 📖 Identificar Pendiente e Intercepto

### ⚙️ Ejemplo 1: Lectura directa

Para $y = 3x - 7$:
- Pendiente: $m = 3$
- Ordenada al origen: $b = -7$
- La recta cruza el eje Y en $(0, -7)$

### ⚙️ Ejemplo 2: Pendiente negativa

Para $y = -\frac{2}{5}x + 4$:
- Pendiente: $m = -\frac{2}{5}$
- Ordenada al origen: $b = 4$
- La recta cruza el eje Y en $(0, 4)$

### ⚙️ Ejemplo 3: Casos especiales

**Para $y = 5$:**
- Podemos escribirla como $y = 0x + 5$
- Pendiente: $m = 0$ (horizontal)
- Intercepto: $b = 5$

**Para $y = 2x$:**
- Podemos escribirla como $y = 2x + 0$
- Pendiente: $m = 2$
- Intercepto: $b = 0$ (pasa por el origen)

---

## 📖 Graficar Usando Pendiente-Ordenada

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/graficar-pendiente-ordenada.svg" alt="Graficar con pendiente-ordenada" style="width: 100%; height: auto;" />
</div>

**Método rápido para graficar:**

1. Ubica el punto $(0, b)$ en el eje Y
2. Desde ahí, usa la pendiente: $m = \frac{\text{subida}}{\text{avance}}$
3. Marca el segundo punto
4. Traza la recta

### ⚙️ Ejemplo 4: Graficar paso a paso

Grafica $y = \frac{2}{3}x + 1$.

**Paso 1:** El intercepto es $(0, 1)$. Marca este punto.

**Paso 2:** La pendiente es $\frac{2}{3}$:
- Subida = 2
- Avance = 3
- Desde $(0, 1)$: avanza 3 unidades a la derecha y sube 2 → llegamos a $(3, 3)$

**Paso 3:** Marca $(3, 3)$ y traza la recta por ambos puntos.

### ⚙️ Ejemplo 5: Pendiente negativa

Grafica $y = -2x + 4$.

**Paso 1:** Intercepto: $(0, 4)$

**Paso 2:** Pendiente $m = -2 = \frac{-2}{1}$:
- Desde $(0, 4)$: avanza 1 a la derecha y baja 2 → llegamos a $(1, 2)$

**Paso 3:** Traza la recta por $(0, 4)$ y $(1, 2)$.

---

## 📖 Obtener la Forma Pendiente-Ordenada

### Desde la forma general

Para convertir $Ax + By + C = 0$ a $y = mx + b$:

$$
By = -Ax - C
$$
$$
y = -\frac{A}{B}x - \frac{C}{B}
$$

### ⚙️ Ejemplo 6: Conversión

Convierte $4x - 2y + 6 = 0$ a forma $y = mx + b$.

$$
-2y = -4x - 6
$$
$$
y = 2x + 3
$$

**Pendiente:** $m = 2$
**Intercepto:** $b = 3$

### Desde dos puntos

Si conoces dos puntos $(x_1, y_1)$ y $(x_2, y_2)$:

1. Calcula $m = \frac{y_2 - y_1}{x_2 - x_1}$
2. Usa punto-pendiente y simplifica a $y = mx + b$

### ⚙️ Ejemplo 7: Desde dos puntos

Encuentra la ecuación de la recta que pasa por $(1, 3)$ y $(4, 9)$.

**Paso 1:** Pendiente:
$$
m = \frac{9 - 3}{4 - 1} = \frac{6}{3} = 2
$$

**Paso 2:** Punto-pendiente con $(1, 3)$:
$$
y - 3 = 2(x - 1)
$$
$$
y = 2x - 2 + 3
$$
$$
y = 2x + 1
$$

---

## 📖 Comparación de Rectas

### Rectas paralelas

Dos rectas son paralelas si tienen la **misma pendiente**.

$y = 3x + 2$ y $y = 3x - 5$ son paralelas (ambas tienen $m = 3$).

### Rectas que se intersectan

Dos rectas se intersectan si tienen **diferentes pendientes**.

$y = 2x + 1$ y $y = -x + 4$ se intersectan (tienen $m = 2$ y $m = -1$).

### Rectas perpendiculares

Dos rectas son perpendiculares si $m_1 \cdot m_2 = -1$.

$y = 2x + 1$ y $y = -\frac{1}{2}x + 3$ son perpendiculares.

---

## 🔑 Resumen

| Forma | $y = mx + b$ |
|-------|--------------|
| $m$ | Pendiente |
| $b$ | Ordenada al origen |
| $(0, b)$ | Punto donde cruza el eje Y |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica la pendiente y el intercepto de $y = -4x + 9$.

<details>
<summary>Ver solución</summary>

- Pendiente: $m = -4$
- Intercepto Y: $b = 9$
- La recta cruza el eje Y en $(0, 9)$

</details>

### Ejercicio 2
Convierte $6x + 3y - 12 = 0$ a forma $y = mx + b$.

<details>
<summary>Ver solución</summary>

$$
3y = -6x + 12
$$
$$
y = -2x + 4
$$

Pendiente: $m = -2$, Intercepto: $b = 4$

</details>

### Ejercicio 3
Escribe la ecuación de la recta que pasa por $(0, -5)$ con pendiente $m = 3$.

<details>
<summary>Ver solución</summary>

Como pasa por $(0, -5)$, el intercepto es $b = -5$.

$$
y = 3x - 5
$$

</details>

### Ejercicio 4
¿Son paralelas las rectas $2x - y + 3 = 0$ y $4x - 2y - 7 = 0$?

<details>
<summary>Ver solución</summary>

**Primera recta:** $y = 2x + 3$ → $m_1 = 2$

**Segunda recta:** $2y = 4x - 7$ → $y = 2x - \frac{7}{2}$ → $m_2 = 2$

Como $m_1 = m_2 = 2$, las rectas son **paralelas**.

</details>

### Ejercicio 5
Encuentra la ecuación de la recta que pasa por $(2, 5)$ y $(6, 1)$ en forma $y = mx + b$.

<details>
<summary>Ver solución</summary>

**Pendiente:**
$$
m = \frac{1 - 5}{6 - 2} = \frac{-4}{4} = -1
$$

**Usando punto-pendiente:**
$$
y - 5 = -1(x - 2)
$$
$$
y = -x + 2 + 5
$$
$$
y = -x + 7
$$

</details>

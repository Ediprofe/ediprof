# Traslación de Parábolas

Cuando el vértice de la parábola **no** está en el origen, trabajamos con parábolas **trasladadas**. Las ecuaciones se modifican para reflejar la posición del nuevo vértice.

---

## 🎯 ¿Qué vas a aprender?

- Ecuaciones de parábolas trasladadas
- Cómo identificar el vértice y otros elementos
- Cómo convertir entre formas

---

## 📖 Lo Esencial de Parábolas Trasladadas

| Orientación | Ecuación estándar | Vértice |
|-------------|-------------------|---------|
| Vertical arriba | $(x - h)^2 = 4p(y - k)$ | $(h, k)$ |
| Vertical abajo | $(x - h)^2 = -4p(y - k)$ | $(h, k)$ |
| Horizontal derecha | $(y - k)^2 = 4p(x - h)$ | $(h, k)$ |
| Horizontal izquierda | $(y - k)^2 = -4p(x - h)$ | $(h, k)$ |

---

## 📖 Parábola Vertical Trasladada

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/parabola-trasladada.svg" alt="Parábola trasladada" style="width: 100%; height: auto;" />
</div>

**Ecuación:**
$$
(x - h)^2 = 4p(y - k)
$$

**Elementos:**
- Vértice: $(h, k)$
- Foco: $(h, k + p)$ (arriba) o $(h, k - p)$ (abajo)
- Directriz: $y = k - p$ (arriba) o $y = k + p$ (abajo)
- Eje: $x = h$

### ⚙️ Ejemplo 1: Identificar elementos

Para $(x - 2)^2 = 8(y + 3)$:

- Vértice: $(2, -3)$
- $4p = 8 \Rightarrow p = 2$
- Abre hacia arriba (positivo)
- Foco: $(2, -3 + 2) = (2, -1)$
- Directriz: $y = -3 - 2 = -5$

### ⚙️ Ejemplo 2: Construir la ecuación

Vértice en $(1, 4)$, abre hacia abajo, $p = 3$.

$$
(x - 1)^2 = -4(3)(y - 4)
$$

$$
(x - 1)^2 = -12(y - 4)
$$

---

## 📖 Parábola Horizontal Trasladada

**Ecuación:**
$$
(y - k)^2 = 4p(x - h)
$$

**Elementos:**
- Vértice: $(h, k)$
- Foco: $(h + p, k)$ (derecha) o $(h - p, k)$ (izquierda)
- Directriz: $x = h - p$ (derecha) o $x = h + p$ (izquierda)
- Eje: $y = k$

### ⚙️ Ejemplo 3: Parábola horizontal trasladada

Para $(y + 1)^2 = 16(x - 5)$:

- Vértice: $(5, -1)$
- $4p = 16 \Rightarrow p = 4$
- Abre hacia la derecha
- Foco: $(5 + 4, -1) = (9, -1)$
- Directriz: $x = 5 - 4 = 1$

### ⚙️ Ejemplo 4: Construir ecuación horizontal

Vértice en $(-2, 3)$, foco en $(-2 - 5, 3) = (-7, 3)$.

El foco está a la izquierda del vértice, entonces abre hacia la izquierda.

$p = 5$

$$
(y - 3)^2 = -20(x + 2)
$$

---

## 📖 Conversión de Forma General a Estándar

La forma general de una parábola vertical es:
$$
Ax^2 + Bx + Cy + D = 0
$$

Para convertir a forma estándar, completamos el cuadrado.

### ⚙️ Ejemplo 5: Completar el cuadrado

Convierte $x^2 - 6x - 8y + 1 = 0$ a forma estándar.

**Paso 1:** Agrupar términos en $x$:
$$
x^2 - 6x = 8y - 1
$$

**Paso 2:** Completar el cuadrado:
$$
x^2 - 6x + 9 = 8y - 1 + 9
$$
$$
(x - 3)^2 = 8y + 8
$$
$$
(x - 3)^2 = 8(y + 1)
$$

**Resultado:**
- Vértice: $(3, -1)$
- $4p = 8 \Rightarrow p = 2$
- Foco: $(3, 1)$

### ⚙️ Ejemplo 6: Forma general horizontal

Convierte $y^2 + 4y - 12x + 16 = 0$ a forma estándar.

$$
y^2 + 4y = 12x - 16
$$
$$
y^2 + 4y + 4 = 12x - 16 + 4
$$
$$
(y + 2)^2 = 12x - 12
$$
$$
(y + 2)^2 = 12(x - 1)
$$

- Vértice: $(1, -2)$
- $p = 3$
- Foco: $(4, -2)$

---

## 📖 De Forma Estándar a General

Expande y simplifica.

### ⚙️ Ejemplo 7: Expansión

$(x + 1)^2 = -8(y - 2)$

$$
x^2 + 2x + 1 = -8y + 16
$$
$$
x^2 + 2x + 8y + 1 - 16 = 0
$$
$$
x^2 + 2x + 8y - 15 = 0
$$

---

## 🔑 Resumen

| Aspecto | Cómo encontrarlo |
|---------|-----------------|
| Vértice | Directamente de $(h, k)$ |
| Parámetro $p$ | De $4p$ en la ecuación |
| Dirección | Signo y variable al cuadrado |
| Foco | Vértice + $p$ en dirección de apertura |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra vértice, foco y directriz de $(x + 4)^2 = 12(y - 1)$.

<details>
<summary>Ver solución</summary>

Vértice: $(-4, 1)$

$p = 3$, abre hacia arriba

Foco: $(-4, 4)$

Directriz: $y = -2$

</details>

### Ejercicio 2
Escribe la ecuación de la parábola con vértice $(3, 2)$ y foco $(3, 5)$.

<details>
<summary>Ver solución</summary>

Foco arriba del vértice → abre hacia arriba

$p = 5 - 2 = 3$

$(x - 3)^2 = 12(y - 2)$

</details>

### Ejercicio 3
Convierte $x^2 + 4x + 12y - 8 = 0$ a forma estándar.

<details>
<summary>Ver solución</summary>

$x^2 + 4x = -12y + 8$

$(x + 2)^2 - 4 = -12y + 8$

$(x + 2)^2 = -12y + 12$

$(x + 2)^2 = -12(y - 1)$

Vértice: $(-2, 1)$, $p = 3$, abre hacia abajo

</details>

### Ejercicio 4
Encuentra los elementos de $(y - 5)^2 = -8(x + 2)$.

<details>
<summary>Ver solución</summary>

Vértice: $(-2, 5)$

$p = 2$, abre hacia la izquierda

Foco: $(-4, 5)$

Directriz: $x = 0$

</details>

### Ejercicio 5
Una parábola tiene directriz $y = 6$ y foco $(2, 2)$. Encuentra su ecuación.

<details>
<summary>Ver solución</summary>

Vértice: punto medio entre foco y directriz

$k = \frac{2 + 6}{2} = 4$, $h = 2$

Vértice: $(2, 4)$

$p = 4 - 2 = 2$, abre hacia abajo

$(x - 2)^2 = -8(y - 4)$

</details>

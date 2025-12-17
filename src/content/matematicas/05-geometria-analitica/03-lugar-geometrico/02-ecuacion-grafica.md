# Ecuación y Gráfica de un Lugar Geométrico

Una ecuación describe un lugar geométrico, pero ¿cómo pasamos de una ecuación a su gráfica, y viceversa? Esta lección explora la relación fundamental entre ecuaciones algebraicas y sus representaciones gráficas.

---

## 🎯 ¿Qué vas a aprender?

- Cómo graficar una ecuación usando tabulación
- Cómo interpretar una gráfica para deducir su ecuación
- Propiedades de simetría y características de curvas

---

## 📖 Lo Esencial de Ecuación y Gráfica

| Tipo de curva | Forma general | Característica visual |
|---------------|---------------|----------------------|
| Recta | $ax + by + c = 0$ | Línea sin curvatura |
| Circunferencia | $x^2 + y^2 = r^2$ | Curva cerrada, todos los puntos equidistantes del centro |
| Parábola | $y = ax^2$ o $x = ay^2$ | Curva abierta en U |
| Elipse | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | Óvalo |
| Hipérbola | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | Dos ramas separadas |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/parabola-tabulacion.svg" alt="Gráfica de parábola por tabulación" style="width: 100%; height: auto;" />
</div>

---

## 📖 De la Ecuación a la Gráfica

El método más básico para graficar una ecuación es la **tabulación**: elegir valores de $x$, calcular los correspondientes valores de $y$, y marcar los puntos.

### ⚙️ Ejemplo 1: Graficar una recta

Grafica la ecuación $y = 2x - 1$.

**Tabulación:**

| $x$ | $y = 2x - 1$ |
|-----|--------------|
| $-2$ | $-5$ |
| $-1$ | $-3$ |
| $0$ | $-1$ |
| $1$ | $1$ |
| $2$ | $3$ |

Marcamos los puntos $(-2, -5)$, $(-1, -3)$, $(0, -1)$, $(1, 1)$, $(2, 3)$ y trazamos la recta.

### ⚙️ Ejemplo 2: Graficar una parábola

Grafica la ecuación $y = x^2 - 4$.

**Tabulación:**

| $x$ | $y = x^2 - 4$ |
|-----|---------------|
| $-3$ | $5$ |
| $-2$ | $0$ |
| $-1$ | $-3$ |
| $0$ | $-4$ |
| $1$ | $-3$ |
| $2$ | $0$ |
| $3$ | $5$ |

El vértice está en $(0, -4)$ y la parábola abre hacia arriba.

---

## 📖 Interceptos con los Ejes

Los **interceptos** son puntos muy útiles para graficar:

### Intercepto con el eje Y
Punto donde la curva cruza el eje Y (cuando $x = 0$).

Para encontrarlo: sustituye $x = 0$ y resuelve para $y$.

### Intercepto con el eje X
Punto(s) donde la curva cruza el eje X (cuando $y = 0$).

Para encontrarlo: sustituye $y = 0$ y resuelve para $x$.

### ⚙️ Ejemplo 3: Encontrar interceptos

Encuentra los interceptos de $y = x^2 - 4x + 3$.

**Intercepto Y:** ($x = 0$)
$$
y = 0 - 0 + 3 = 3
$$
Intercepto: $(0, 3)$

**Interceptos X:** ($y = 0$)
$$
x^2 - 4x + 3 = 0
$$
$$
(x - 1)(x - 3) = 0
$$
$$
x = 1 \text{ o } x = 3
$$
Interceptos: $(1, 0)$ y $(3, 0)$

---

## 📖 Simetrías

Una curva puede tener diferentes tipos de **simetría**:

| Tipo de simetría | Prueba | Significado |
|------------------|--------|-------------|
| Respecto al eje Y | $f(-x) = f(x)$ | Función par |
| Respecto al eje X | Si $(x, y)$ está, también $(-x, y)$ | — |
| Respecto al origen | $f(-x) = -f(x)$ | Función impar |

### ⚙️ Ejemplo 4: Determinar simetrías

Determina las simetrías de $y = x^2$.

**Prueba de simetría respecto al eje Y:**

Sustituimos $x$ por $-x$:
$$
y = (-x)^2 = x^2
$$

La ecuación no cambia, así que **tiene simetría respecto al eje Y**.

### ⚙️ Ejemplo 5: Simetría respecto al origen

Determina las simetrías de $y = x^3$.

Sustituimos $x$ por $-x$ y $y$ por $-y$:
$$
-y = (-x)^3 = -x^3
$$
$$
y = x^3
$$

La ecuación se mantiene, así que **tiene simetría respecto al origen**.

---

## 📖 De la Gráfica a la Ecuación

Si conocemos características de una gráfica, podemos deducir su ecuación:

### ⚙️ Ejemplo 6: Deducir ecuación de una circunferencia

Una circunferencia tiene centro en $(2, -1)$ y pasa por el punto $(5, 3)$.

**Paso 1:** Calcular el radio
$$
r = \sqrt{(5-2)^2 + (3-(-1))^2} = \sqrt{9 + 16} = 5
$$

**Paso 2:** Escribir la ecuación
$$
(x - 2)^2 + (y + 1)^2 = 25
$$

### ⚙️ Ejemplo 7: Deducir ecuación de una recta

Una recta pasa por $(1, 3)$ y $(4, 9)$.

**Paso 1:** Calcular la pendiente
$$
m = \frac{9 - 3}{4 - 1} = \frac{6}{3} = 2
$$

**Paso 2:** Usar punto-pendiente
$$
y - 3 = 2(x - 1)
$$
$$
y = 2x + 1
$$

---

## 📖 Dominio y Rango

El **dominio** son los valores de $x$ para los que existe la curva.

El **rango** son los valores de $y$ que toma la curva.

### ⚙️ Ejemplo 8: Dominio y rango de una circunferencia

Para $x^2 + y^2 = 9$:

- **Dominio:** $-3 \leq x \leq 3$
- **Rango:** $-3 \leq y \leq 3$

### ⚙️ Ejemplo 9: Dominio y rango de una parábola

Para $y = x^2$:

- **Dominio:** Todos los reales $(-\infty, \infty)$
- **Rango:** $y \geq 0$ o $[0, \infty)$

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| Tabulación | Método básico para graficar |
| Interceptos | Puntos donde la curva cruza los ejes |
| Simetría | Propiedades de reflexión de la curva |
| Dominio | Valores válidos de $x$ |
| Rango | Valores que toma $y$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra los interceptos de la ecuación $y = x^2 - 9$.

<details>
<summary>Ver solución</summary>

**Intercepto Y:** ($x = 0$)
$$
y = 0 - 9 = -9
$$
Intercepto: $(0, -9)$

**Interceptos X:** ($y = 0$)
$$
x^2 - 9 = 0
$$
$$
x = \pm 3
$$
Interceptos: $(3, 0)$ y $(-3, 0)$

</details>

### Ejercicio 2
Determina si la curva $y = \frac{1}{x}$ tiene simetría respecto al origen.

<details>
<summary>Ver solución</summary>

Sustituimos $x$ por $-x$ y $y$ por $-y$:

$$
-y = \frac{1}{-x} = -\frac{1}{x}
$$

$$
y = \frac{1}{x}
$$

La ecuación se mantiene, así que **sí tiene simetría respecto al origen**.

</details>

### Ejercicio 3
¿Cuál es el dominio y rango de $(x-1)^2 + (y+2)^2 = 16$?

<details>
<summary>Ver solución</summary>

Es una circunferencia con centro $(1, -2)$ y radio $4$.

**Dominio:** $1 - 4 \leq x \leq 1 + 4$ → $-3 \leq x \leq 5$

**Rango:** $-2 - 4 \leq y \leq -2 + 4$ → $-6 \leq y \leq 2$

</details>

### Ejercicio 4
Una parábola tiene vértice en $(2, 3)$ y pasa por $(4, 7)$. Encuentra su ecuación.

<details>
<summary>Ver solución</summary>

Forma con vértice: $y = a(x - 2)^2 + 3$

Usamos el punto $(4, 7)$:
$$
7 = a(4 - 2)^2 + 3
$$
$$
7 = 4a + 3
$$
$$
a = 1
$$

**Ecuación:** $y = (x - 2)^2 + 3$

</details>

### Ejercicio 5
Grafica mentalmente la ecuación $y = |x|$. ¿Cuáles son sus interceptos y qué simetría tiene?

<details>
<summary>Ver solución</summary>

**Interceptos:**
- Intercepto Y: $(0, 0)$
- Intercepto X: $(0, 0)$

(Solo un intercepto, en el origen)

**Simetría:** $|{-x}| = |x|$, así que tiene **simetría respecto al eje Y**.

**Forma:** Es una "V" con vértice en el origen, abriendo hacia arriba.

</details>

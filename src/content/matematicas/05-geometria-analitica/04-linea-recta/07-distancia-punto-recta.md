# Distancia de un Punto a una Recta

¿Cuál es la distancia más corta entre un punto y una recta? Esta pregunta tiene aplicaciones importantes en navegación, diseño y física. La respuesta es la **distancia perpendicular**.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula de distancia punto-recta
- Cómo aplicarla en diferentes situaciones
- Aplicaciones prácticas

---

## 📖 Lo Esencial de Distancia Punto-Recta

| Fórmula | Descripción |
|---------|-------------|
| $d = \dfrac{\|Ax_0 + By_0 + C\|}{\sqrt{A^2 + B^2}}$ | Distancia del punto $(x_0, y_0)$ a la recta $Ax + By + C = 0$ |

---

## 📖 La Fórmula de Distancia

La distancia de un punto $P(x_0, y_0)$ a una recta $Ax + By + C = 0$ es:

$$
d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}
$$

> 💡 **Importante:** 
> - La recta debe estar en forma general $Ax + By + C = 0$
> - El numerador siempre lleva valor absoluto
> - Esta fórmula da la distancia **perpendicular** (la más corta)

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Distancia básica

Encuentra la distancia del punto $(3, 4)$ a la recta $3x + 4y - 5 = 0$.

**Identificamos:**
- Punto: $(x_0, y_0) = (3, 4)$
- Recta: $A = 3$, $B = 4$, $C = -5$

**Aplicamos la fórmula:**
$$
d = \frac{|3(3) + 4(4) - 5|}{\sqrt{3^2 + 4^2}}
$$

$$
d = \frac{|9 + 16 - 5|}{\sqrt{9 + 16}} = \frac{|20|}{5} = 4
$$

**Respuesta:** La distancia es 4 unidades.

### ⚙️ Ejemplo 2: El punto está sobre la recta

Calcula la distancia del punto $(1, 2)$ a la recta $x + y - 3 = 0$.

$$
d = \frac{|1 + 2 - 3|}{\sqrt{1 + 1}} = \frac{|0|}{\sqrt{2}} = 0
$$

**Respuesta:** La distancia es 0, lo que significa que el punto está **sobre la recta**.

### ⚙️ Ejemplo 3: Con coeficientes negativos

Encuentra la distancia del punto $(-2, 5)$ a la recta $2x - 3y + 4 = 0$.

$$
d = \frac{|2(-2) - 3(5) + 4|}{\sqrt{4 + 9}}
$$

$$
d = \frac{|-4 - 15 + 4|}{\sqrt{13}} = \frac{|-15|}{\sqrt{13}} = \frac{15}{\sqrt{13}} = \frac{15\sqrt{13}}{13} \approx 4.16
$$

---

## 📖 Casos Especiales

### Distancia a una recta horizontal

Para la recta $y = k$ (o $y - k = 0$, o $0x + 1y - k = 0$):

$$
d = \frac{|0 \cdot x_0 + 1 \cdot y_0 - k|}{\sqrt{0 + 1}} = |y_0 - k|
$$

### ⚙️ Ejemplo 4: Distancia a recta horizontal

Distancia del punto $(3, 7)$ a la recta $y = 2$:

$$
d = |7 - 2| = 5
$$

### Distancia a una recta vertical

Para la recta $x = k$ (o $x - k = 0$, o $1x + 0y - k = 0$):

$$
d = \frac{|1 \cdot x_0 + 0 \cdot y_0 - k|}{\sqrt{1 + 0}} = |x_0 - k|
$$

### ⚙️ Ejemplo 5: Distancia a recta vertical

Distancia del punto $(8, 3)$ a la recta $x = 5$:

$$
d = |8 - 5| = 3
$$

---

## 📖 Convertir la Recta a Forma General

Si la recta está en otra forma, primero conviértela a forma general.

### ⚙️ Ejemplo 6: Recta en forma explícita

Encuentra la distancia del punto $(2, 1)$ a la recta $y = 3x + 1$.

**Paso 1:** Convertir a forma general:
$$
y = 3x + 1 \Rightarrow 3x - y + 1 = 0
$$

**Paso 2:** Aplicar la fórmula:
$$
d = \frac{|3(2) - 1(1) + 1|}{\sqrt{9 + 1}} = \frac{|6 - 1 + 1|}{\sqrt{10}} = \frac{6}{\sqrt{10}} = \frac{6\sqrt{10}}{10} = \frac{3\sqrt{10}}{5}
$$

---

## 📖 Aplicaciones

### Distancia entre rectas paralelas

Dos rectas paralelas $Ax + By + C_1 = 0$ y $Ax + By + C_2 = 0$ tienen una distancia constante:

$$
d = \frac{|C_2 - C_1|}{\sqrt{A^2 + B^2}}
$$

### ⚙️ Ejemplo 7: Distancia entre paralelas

Encuentra la distancia entre $2x + 3y - 6 = 0$ y $2x + 3y + 9 = 0$.

$$
d = \frac{|9 - (-6)|}{\sqrt{4 + 9}} = \frac{15}{\sqrt{13}} = \frac{15\sqrt{13}}{13} \approx 4.16
$$

### Encontrar el pie de la perpendicular

El **pie de la perpendicular** es el punto sobre la recta más cercano al punto dado.

### ⚙️ Ejemplo 8: Pie de la perpendicular

El punto $(5, 0)$ y la recta $y = x$. Encuentra el pie de la perpendicular.

**Paso 1:** La recta $y = x$ tiene pendiente $m = 1$.

**Paso 2:** La perpendicular desde $(5, 0)$ tiene pendiente $m_\perp = -1$.

**Paso 3:** Ecuación de la perpendicular:
$$
y - 0 = -1(x - 5)
$$
$$
y = -x + 5
$$

**Paso 4:** Intersección con $y = x$:
$$
x = -x + 5 \Rightarrow 2x = 5 \Rightarrow x = 2.5
$$
$$
y = 2.5
$$

**Pie de la perpendicular:** $(2.5, 2.5)$

---

## 🔑 Resumen

| Situación | Fórmula |
|-----------|---------|
| Punto a recta general | $d = \frac{\|Ax_0 + By_0 + C\|}{\sqrt{A^2 + B^2}}$ |
| Punto a recta horizontal $y = k$ | $d = \|y_0 - k\|$ |
| Punto a recta vertical $x = k$ | $d = \|x_0 - k\|$ |
| Entre paralelas | $d = \frac{\|C_2 - C_1\|}{\sqrt{A^2 + B^2}}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la distancia del punto $(0, 0)$ a la recta $3x + 4y - 15 = 0$.

<details>
<summary>Ver solución</summary>

$$
d = \frac{|3(0) + 4(0) - 15|}{\sqrt{9 + 16}} = \frac{15}{5} = 3
$$

</details>

### Ejercicio 2
¿A qué distancia está el punto $(4, 5)$ de la recta $y = -2$?

<details>
<summary>Ver solución</summary>

$$
d = |5 - (-2)| = |7| = 7
$$

</details>

### Ejercicio 3
Calcula la distancia del punto $(1, 1)$ a la recta $y = 2x - 3$.

<details>
<summary>Ver solución</summary>

Forma general: $2x - y - 3 = 0$

$$
d = \frac{|2(1) - 1 - 3|}{\sqrt{4 + 1}} = \frac{|-2|}{\sqrt{5}} = \frac{2\sqrt{5}}{5} \approx 0.894
$$

</details>

### Ejercicio 4
Encuentra la distancia entre las rectas paralelas $x - 2y + 3 = 0$ y $x - 2y - 7 = 0$.

<details>
<summary>Ver solución</summary>

$$
d = \frac{|-7 - 3|}{\sqrt{1 + 4}} = \frac{10}{\sqrt{5}} = 2\sqrt{5} \approx 4.47
$$

</details>

### Ejercicio 5
Un punto $P(x, 3)$ está a distancia 2 de la recta $4x - 3y + 1 = 0$. Encuentra los posibles valores de $x$.

<details>
<summary>Ver solución</summary>

$$
2 = \frac{|4x - 3(3) + 1|}{\sqrt{16 + 9}} = \frac{|4x - 8|}{5}
$$

$$
10 = |4x - 8|
$$

**Caso 1:** $4x - 8 = 10 \Rightarrow x = 4.5$

**Caso 2:** $4x - 8 = -10 \Rightarrow x = -0.5$

**Respuesta:** $x = 4.5$ o $x = -0.5$

</details>

# Forma Normal de la Recta

La **forma normal** (o forma polar normalizada) es una representación especial de la recta que usa la distancia perpendicular desde el origen hasta la recta. Es particularmente útil en aplicaciones de geometría computacional y física.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la forma normal de una recta
- Cómo obtenerla a partir de otras formas
- Sus aplicaciones en el cálculo de distancias

---

## 📖 Lo Esencial de Forma Normal

| Concepto | Expresión |
|----------|-----------|
| Forma normal | $x\cos\omega + y\sin\omega - p = 0$ |
| Distancia al origen | $p$ (siempre positiva) |
| Ángulo del vector normal | $\omega$ |
| Normalización | Dividir entre $\sqrt{A^2 + B^2}$ |

---

## 📖 Concepto de Forma Normal

La **forma normal** de una recta es:

$$
x\cos\omega + y\sin\omega = p
$$

o equivalentemente:

$$
x\cos\omega + y\sin\omega - p = 0
$$

donde:
- $p$ es la **distancia perpendicular** desde el origen hasta la recta (siempre $p > 0$)
- $\omega$ es el ángulo que forma la recta perpendicular (desde el origen a la recta) con el eje X positivo

> 💡 Esta forma es útil porque el coeficiente del lado derecho directamente nos da la distancia al origen.

---

## 📖 Propiedades de la Forma Normal

La forma normal tiene una propiedad especial:

$$
\cos^2\omega + \sin^2\omega = 1
$$

Esto significa que los coeficientes de $x$ y $y$ satisfacen que la suma de sus cuadrados es 1.

---

## 📖 De Forma General a Forma Normal

Para convertir $Ax + By + C = 0$ a forma normal:

**Paso 1:** Calcula el factor de normalización:
$$
\sqrt{A^2 + B^2}
$$

**Paso 2:** Divide toda la ecuación por $\pm\sqrt{A^2 + B^2}$, eligiendo el signo para que $p > 0$ (es decir, para que el término constante sea negativo después de pasar al lado derecho).

$$
\frac{A}{\pm\sqrt{A^2 + B^2}}x + \frac{B}{\pm\sqrt{A^2 + B^2}}y + \frac{C}{\pm\sqrt{A^2 + B^2}} = 0
$$

### ⚙️ Ejemplo 1: Normalizar una ecuación

Convierte $3x + 4y - 10 = 0$ a forma normal.

**Paso 1:** Factor de normalización:
$$
\sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

**Paso 2:** Como $C = -10 < 0$, dividimos entre $+5$:
$$
\frac{3}{5}x + \frac{4}{5}y - 2 = 0
$$

**Forma normal:**
$$
\frac{3}{5}x + \frac{4}{5}y = 2
$$

Donde:
- $\cos\omega = \frac{3}{5}$
- $\sin\omega = \frac{4}{5}$
- $p = 2$ (distancia al origen)

### ⚙️ Ejemplo 2: Con término constante positivo

Convierte $4x - 3y + 10 = 0$ a forma normal.

**Paso 1:** Factor de normalización:
$$
\sqrt{16 + 9} = 5
$$

**Paso 2:** Como $C = 10 > 0$, dividimos entre $-5$ para que $p > 0$:
$$
-\frac{4}{5}x + \frac{3}{5}y - 2 = 0
$$

**Forma normal:**
$$
-\frac{4}{5}x + \frac{3}{5}y = 2
$$

- $p = 2$

### ⚙️ Ejemplo 3: Encontrar la distancia al origen

¿Cuál es la distancia del origen a la recta $8x - 6y + 20 = 0$?

**Paso 1:** Factor de normalización:
$$
\sqrt{64 + 36} = 10
$$

**Paso 2:** Distancia:
$$
p = \frac{|C|}{\sqrt{A^2 + B^2}} = \frac{|20|}{10} = 2
$$

**Respuesta:** La distancia es 2 unidades.

---

## 📖 Cálculo del Ángulo ω

Una vez en forma normal $x\cos\omega + y\sin\omega = p$:

$$
\cos\omega = \frac{A}{\pm\sqrt{A^2 + B^2}}, \quad \sin\omega = \frac{B}{\pm\sqrt{A^2 + B^2}}
$$

El ángulo $\omega$ se encuentra usando:
$$
\omega = \arctan\left(\frac{\sin\omega}{\cos\omega}\right)
$$

### ⚙️ Ejemplo 4: Encontrar el ángulo

Para $3x + 4y - 10 = 0$:

$$
\cos\omega = \frac{3}{5} = 0.6, \quad \sin\omega = \frac{4}{5} = 0.8
$$

$$
\tan\omega = \frac{0.8}{0.6} = \frac{4}{3}
$$

$$
\omega = \arctan\left(\frac{4}{3}\right) \approx 53.13°
$$

---

## 📖 Aplicación: Fórmula de Distancia Punto-Recta

La forma normal lleva naturalmente a la fórmula de distancia de un punto a una recta.

Si la recta es $Ax + By + C = 0$ y el punto es $(x_0, y_0)$:

$$
d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}
$$

### ⚙️ Ejemplo 5: Distancia de un punto a una recta

Encuentra la distancia del punto $(1, 2)$ a la recta $3x - 4y + 5 = 0$.

$$
d = \frac{|3(1) - 4(2) + 5|}{\sqrt{9 + 16}} = \frac{|3 - 8 + 5|}{5} = \frac{|0|}{5} = 0
$$

El punto está **sobre la recta**.

### ⚙️ Ejemplo 6: Otro ejemplo de distancia

Encuentra la distancia del punto $(3, 4)$ a la recta $5x + 12y - 26 = 0$.

$$
d = \frac{|5(3) + 12(4) - 26|}{\sqrt{25 + 144}} = \frac{|15 + 48 - 26|}{13} = \frac{37}{13} \approx 2.85
$$

---

## 🔑 Resumen

| Concepto | Fórmula |
|----------|---------|
| Forma normal | $x\cos\omega + y\sin\omega = p$ |
| Distancia al origen | $p = \frac{\|C\|}{\sqrt{A^2 + B^2}}$ |
| Normalización | Dividir entre $\sqrt{A^2 + B^2}$ |
| Distancia punto-recta | $d = \frac{\|Ax_0 + By_0 + C\|}{\sqrt{A^2 + B^2}}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Convierte $5x + 12y - 26 = 0$ a forma normal.

<details>
<summary>Ver solución</summary>

$$
\sqrt{25 + 144} = 13
$$

$$
\frac{5}{13}x + \frac{12}{13}y - 2 = 0
$$

Forma normal: $\frac{5}{13}x + \frac{12}{13}y = 2$

Distancia al origen: $p = 2$

</details>

### Ejercicio 2
¿Cuál es la distancia del origen a la recta $x + y - 5 = 0$?

<details>
<summary>Ver solución</summary>

$$
p = \frac{|-5|}{\sqrt{1 + 1}} = \frac{5}{\sqrt{2}} = \frac{5\sqrt{2}}{2} \approx 3.54
$$

</details>

### Ejercicio 3
Encuentra la distancia del punto $(5, 1)$ a la recta $3x + 4y - 7 = 0$.

<details>
<summary>Ver solución</summary>

$$
d = \frac{|3(5) + 4(1) - 7|}{\sqrt{9 + 16}} = \frac{|15 + 4 - 7|}{5} = \frac{12}{5} = 2.4
$$

</details>

### Ejercicio 4
Si la forma normal de una recta es $\frac{1}{2}x + \frac{\sqrt{3}}{2}y = 4$, encuentra su forma general.

<details>
<summary>Ver solución</summary>

Multiplicamos por 2:
$$
x + \sqrt{3}y = 8
$$

Forma general: $x + \sqrt{3}y - 8 = 0$

</details>

### Ejercicio 5
Verifica que $(2, 3)$ está a distancia 1 de la recta $4x - 3y - 4 = 0$.

<details>
<summary>Ver solución</summary>

$$
d = \frac{|4(2) - 3(3) - 4|}{\sqrt{16 + 9}} = \frac{|8 - 9 - 4|}{5} = \frac{|-5|}{5} = 1
$$

Sí, la distancia es exactamente 1. ✓

</details>

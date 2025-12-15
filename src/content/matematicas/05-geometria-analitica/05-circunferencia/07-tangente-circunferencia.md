# Recta Tangente a la Circunferencia

Una **recta tangente** a una circunferencia es aquella que la toca en exactamente un punto. Calcular la ecuación de esta tangente es uno de los problemas clásicos de la geometría analítica.

---

## 🎯 ¿Qué vas a aprender?

- Cómo encontrar la ecuación de la tangente desde un punto de la circunferencia
- Cómo encontrar tangentes desde un punto exterior
- Propiedades de las tangentes

---

## 📖 Lo Esencial de Tangentes

| Situación | Fórmula |
|-----------|---------|
| Tangente en $(x_0, y_0)$ sobre $x^2 + y^2 = r^2$ | $x_0 x + y_0 y = r^2$ |
| Tangente en $(x_0, y_0)$ sobre $(x-h)^2 + (y-k)^2 = r^2$ | $(x_0 - h)(x - h) + (y_0 - k)(y - k) = r^2$ |

---

## 📖 Tangente Desde un Punto de la Circunferencia

Si el punto $P(x_0, y_0)$ está **sobre** la circunferencia, la tangente en ese punto es perpendicular al radio que une el centro con $P$.

### Para circunferencia centrada en el origen

Para $x^2 + y^2 = r^2$, la tangente en $(x_0, y_0)$ es:

$$
x_0 x + y_0 y = r^2
$$

### ⚙️ Ejemplo 1: Tangente en punto de la circunferencia

Encuentra la tangente a $x^2 + y^2 = 25$ en el punto $(3, 4)$.

**Verificamos que el punto está en la circunferencia:**
$3^2 + 4^2 = 9 + 16 = 25$ ✓

**Tangente:**
$$
3x + 4y = 25
$$

### Para circunferencia con centro $(h, k)$

Para $(x - h)^2 + (y - k)^2 = r^2$, la tangente en $(x_0, y_0)$ es:

$$
(x_0 - h)(x - h) + (y_0 - k)(y - k) = r^2
$$

### ⚙️ Ejemplo 2: Tangente con centro desplazado

Encuentra la tangente a $(x - 2)^2 + (y - 3)^2 = 25$ en el punto $(5, 7)$.

**Verificamos:** $(5-2)^2 + (7-3)^2 = 9 + 16 = 25$ ✓

**Tangente:**
$$
(5 - 2)(x - 2) + (7 - 3)(y - 3) = 25
$$
$$
3(x - 2) + 4(y - 3) = 25
$$
$$
3x - 6 + 4y - 12 = 25
$$
$$
3x + 4y = 43
$$

---

## 📖 Tangente con Pendiente Dada

Si queremos una tangente a $x^2 + y^2 = r^2$ con pendiente $m$:

La ecuación es $y = mx + c$, donde:

$$
c = \pm r\sqrt{1 + m^2}
$$

Hay **dos tangentes** paralelas con esa pendiente.

### ⚙️ Ejemplo 3: Tangente con pendiente dada

Encuentra las tangentes a $x^2 + y^2 = 4$ con pendiente $m = 1$.

$$
c = \pm 2\sqrt{1 + 1} = \pm 2\sqrt{2}
$$

**Tangentes:**
- $y = x + 2\sqrt{2}$
- $y = x - 2\sqrt{2}$

---

## 📖 Tangentes Desde un Punto Exterior

Desde un punto $P$ exterior a la circunferencia se pueden trazar **dos tangentes**.

### Método 1: Usando la condición de tangencia

Para que $y - y_0 = m(x - x_0)$ sea tangente a $x^2 + y^2 = r^2$:

1. Sustituir en la circunferencia
2. Igualar el discriminante a cero
3. Resolver para $m$

### ⚙️ Ejemplo 4: Tangentes desde punto exterior

Encuentra las tangentes a $x^2 + y^2 = 4$ desde el punto $(4, 0)$.

**Ecuación de la recta por $(4, 0)$:** $y = m(x - 4)$

**Sustituimos en la circunferencia:**
$$
x^2 + m^2(x - 4)^2 = 4
$$
$$
x^2 + m^2 x^2 - 8m^2 x + 16m^2 = 4
$$
$$
(1 + m^2)x^2 - 8m^2 x + (16m^2 - 4) = 0
$$

**Para tangencia, discriminante = 0:**
$$
64m^4 - 4(1 + m^2)(16m^2 - 4) = 0
$$
$$
64m^4 - 4(16m^2 - 4 + 16m^4 - 4m^2) = 0
$$
$$
64m^4 - 64m^4 - 48m^2 + 16 = 0
$$
$$
-48m^2 + 16 = 0
$$
$$
m^2 = \frac{1}{3}
$$
$$
m = \pm \frac{1}{\sqrt{3}}
$$

**Tangentes:**
- $y = \frac{1}{\sqrt{3}}(x - 4) = \frac{\sqrt{3}}{3}x - \frac{4\sqrt{3}}{3}$
- $y = -\frac{1}{\sqrt{3}}(x - 4) = -\frac{\sqrt{3}}{3}x + \frac{4\sqrt{3}}{3}$

---

## 📖 Longitud de la Tangente

La **longitud de la tangente** desde un punto $P(x_1, y_1)$ a la circunferencia $x^2 + y^2 + Dx + Ey + F = 0$ es:

$$
L = \sqrt{x_1^2 + y_1^2 + Dx_1 + Ey_1 + F}
$$

(Esta cantidad también se llama **potencia del punto**.)

### ⚙️ Ejemplo 5: Longitud de tangente

Encuentra la longitud de la tangente desde $(5, 6)$ a $x^2 + y^2 = 16$.

Forma general: $x^2 + y^2 - 16 = 0$

$$
L = \sqrt{25 + 36 - 16} = \sqrt{45} = 3\sqrt{5}
$$

---

## 🔑 Resumen

| Situación | Fórmula/Método |
|-----------|----------------|
| Tangente en punto de la curva (origen) | $x_0 x + y_0 y = r^2$ |
| Tangente con pendiente $m$ | $c = \pm r\sqrt{1 + m^2}$ |
| Tangentes desde punto exterior | Discriminante = 0 |
| Longitud de tangente | $\sqrt{x_1^2 + y_1^2 + Dx_1 + Ey_1 + F}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la tangente a $x^2 + y^2 = 13$ en el punto $(2, 3)$.

<details>
<summary>Ver solución</summary>

Verificamos: $4 + 9 = 13$ ✓

Tangente: $2x + 3y = 13$

</details>

### Ejercicio 2
Encuentra las tangentes a $x^2 + y^2 = 9$ con pendiente $m = 2$.

<details>
<summary>Ver solución</summary>

$c = \pm 3\sqrt{1 + 4} = \pm 3\sqrt{5}$

Tangentes: $y = 2x + 3\sqrt{5}$ y $y = 2x - 3\sqrt{5}$

</details>

### Ejercicio 3
Encuentra la tangente a $(x-1)^2 + (y-2)^2 = 9$ en $(4, 2)$.

<details>
<summary>Ver solución</summary>

Verificamos: $(4-1)^2 + 0 = 9$ ✓

Tangente: $(4-1)(x-1) + (2-2)(y-2) = 9$

$3(x-1) = 9$

$x = 4$

(Es una recta vertical en $x = 4$)

</details>

### Ejercicio 4
Calcula la longitud de la tangente desde $(7, 1)$ a $x^2 + y^2 - 4x - 6y + 9 = 0$.

<details>
<summary>Ver solución</summary>

$L = \sqrt{49 + 1 - 28 - 6 + 9} = \sqrt{25} = 5$

</details>

### Ejercicio 5
Desde el punto $(0, 5)$, ¿cuántas tangentes se pueden trazar a $x^2 + y^2 = 9$?

<details>
<summary>Ver solución</summary>

Distancia del punto al centro: $d = 5$

Radio: $r = 3$

Como $d > r$ (el punto es exterior), se pueden trazar **2 tangentes**.

</details>

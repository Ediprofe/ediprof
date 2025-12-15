# Ecuación General de la Circunferencia

La **ecuación general** de la circunferencia es una forma expandida que no muestra directamente el centro y radio, pero es útil para ciertos cálculos y análisis.

---

## 🎯 ¿Qué vas a aprender?

- La forma general de la circunferencia
- Cómo identificar si una ecuación es una circunferencia
- Condiciones para que represente una circunferencia real

---

## 📖 Lo Esencial de Ecuación General

| Forma | Ecuación |
|-------|----------|
| General | $x^2 + y^2 + Dx + Ey + F = 0$ |
| Centro | $\left(-\frac{D}{2}, -\frac{E}{2}\right)$ |
| Radio | $r = \sqrt{\frac{D^2}{4} + \frac{E^2}{4} - F}$ |
| Condición | $\frac{D^2 + E^2}{4} > F$ para circunferencia real |

---

## 📖 Forma General

La **ecuación general** de la circunferencia es:

$$
x^2 + y^2 + Dx + Ey + F = 0
$$

**Características:**
- Los coeficientes de $x^2$ y $y^2$ son **iguales** (ambos 1)
- No hay término $xy$
- $D$, $E$ y $F$ son constantes reales

---

## 📖 De Forma Ordinaria a Forma General

Para convertir $(x - h)^2 + (y - k)^2 = r^2$ a forma general:

1. Expande los binomios al cuadrado
2. Pasa todo al lado izquierdo
3. Simplifica

### ⚙️ Ejemplo 1: Expansión

Convertir $(x - 3)^2 + (y + 2)^2 = 25$ a forma general.

**Paso 1:** Expandir:
$$
x^2 - 6x + 9 + y^2 + 4y + 4 = 25
$$

**Paso 2:** Simplificar:
$$
x^2 + y^2 - 6x + 4y + 9 + 4 - 25 = 0
$$

$$
x^2 + y^2 - 6x + 4y - 12 = 0
$$

**Forma general:** $D = -6$, $E = 4$, $F = -12$

---

## 📖 De Forma General a Forma Ordinaria

Para convertir $x^2 + y^2 + Dx + Ey + F = 0$ a forma ordinaria:

1. Agrupa los términos en $x$ y los términos en $y$
2. Completa el cuadrado para cada grupo
3. Pasa el término constante al lado derecho

### El Método de Completar el Cuadrado

Para completar el cuadrado en $x^2 + Dx$:
$$
x^2 + Dx = \left(x + \frac{D}{2}\right)^2 - \frac{D^2}{4}
$$

### ⚙️ Ejemplo 2: Completar cuadrado

Convertir $x^2 + y^2 - 4x + 6y - 12 = 0$ a forma ordinaria.

**Paso 1:** Agrupar:
$$
(x^2 - 4x) + (y^2 + 6y) = 12
$$

**Paso 2:** Completar cuadrados:
- Para $x$: $x^2 - 4x = (x - 2)^2 - 4$
- Para $y$: $y^2 + 6y = (y + 3)^2 - 9$

**Paso 3:** Sustituir:
$$
(x - 2)^2 - 4 + (y + 3)^2 - 9 = 12
$$

$$
(x - 2)^2 + (y + 3)^2 = 12 + 4 + 9 = 25
$$

**Resultado:** Centro $(2, -3)$, radio $r = 5$

### ⚙️ Ejemplo 3: Otro ejemplo

Convertir $x^2 + y^2 + 8x - 2y - 8 = 0$ a forma ordinaria.

**Agrupamos y completamos:**
$$
(x^2 + 8x) + (y^2 - 2y) = 8
$$

$$
(x + 4)^2 - 16 + (y - 1)^2 - 1 = 8
$$

$$
(x + 4)^2 + (y - 1)^2 = 25
$$

Centro: $(-4, 1)$, Radio: $5$

---

## 📖 Fórmulas Directas

De la ecuación $x^2 + y^2 + Dx + Ey + F = 0$:

**Centro:**
$$
C = \left(-\frac{D}{2}, -\frac{E}{2}\right)
$$

**Radio:**
$$
r = \sqrt{\frac{D^2}{4} + \frac{E^2}{4} - F} = \frac{1}{2}\sqrt{D^2 + E^2 - 4F}
$$

### ⚙️ Ejemplo 4: Fórmulas directas

Para $x^2 + y^2 - 6x + 4y - 12 = 0$:

- $D = -6$, $E = 4$, $F = -12$

**Centro:**
$$
C = \left(-\frac{-6}{2}, -\frac{4}{2}\right) = (3, -2)
$$

**Radio:**
$$
r = \frac{1}{2}\sqrt{36 + 16 + 48} = \frac{1}{2}\sqrt{100} = 5
$$

---

## 📖 Condiciones de Existencia

Para que la ecuación represente una **circunferencia real**:

$$
\frac{D^2 + E^2}{4} - F > 0
$$

O equivalentemente: $D^2 + E^2 - 4F > 0$

| Condición | Resultado |
|-----------|-----------|
| $D^2 + E^2 - 4F > 0$ | Circunferencia real |
| $D^2 + E^2 - 4F = 0$ | Circunferencia puntual (radio 0) |
| $D^2 + E^2 - 4F < 0$ | Circunferencia imaginaria (no existe) |

### ⚙️ Ejemplo 5: Verificar existencia

¿$x^2 + y^2 - 2x + 4y + 10 = 0$ es una circunferencia real?

- $D = -2$, $E = 4$, $F = 10$
- $D^2 + E^2 - 4F = 4 + 16 - 40 = -20 < 0$

**No es una circunferencia real** (el radio sería imaginario).

---

## 🔑 Resumen

| Conversión | Método |
|------------|--------|
| Ordinaria → General | Expandir y simplificar |
| General → Ordinaria | Completar el cuadrado |
| Centro directo | $\left(-\frac{D}{2}, -\frac{E}{2}\right)$ |
| Radio directo | $\frac{1}{2}\sqrt{D^2 + E^2 - 4F}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Convierte $(x + 1)^2 + (y - 3)^2 = 16$ a forma general.

<details>
<summary>Ver solución</summary>

$$
x^2 + 2x + 1 + y^2 - 6y + 9 = 16
$$

$$
x^2 + y^2 + 2x - 6y - 6 = 0
$$

</details>

### Ejercicio 2
Encuentra el centro y radio de $x^2 + y^2 + 10x - 4y - 7 = 0$.

<details>
<summary>Ver solución</summary>

$D = 10$, $E = -4$, $F = -7$

Centro: $\left(-5, 2\right)$

Radio: $r = \frac{1}{2}\sqrt{100 + 16 + 28} = \frac{1}{2}\sqrt{144} = 6$

</details>

### Ejercicio 3
Convierte $x^2 + y^2 - 6x + 2y + 1 = 0$ a forma ordinaria.

<details>
<summary>Ver solución</summary>

$(x^2 - 6x + 9) + (y^2 + 2y + 1) = -1 + 9 + 1$

$(x - 3)^2 + (y + 1)^2 = 9$

Centro: $(3, -1)$, Radio: $3$

</details>

### Ejercicio 4
¿Representa $x^2 + y^2 + 4x - 6y + 15 = 0$ una circunferencia real?

<details>
<summary>Ver solución</summary>

$D^2 + E^2 - 4F = 16 + 36 - 60 = -8 < 0$

**No**, es una circunferencia imaginaria.

</details>

### Ejercicio 5
Encuentra los valores de $k$ para que $x^2 + y^2 - 4x + 2y + k = 0$ sea una circunferencia real.

<details>
<summary>Ver solución</summary>

Condición: $D^2 + E^2 - 4F > 0$

$16 + 4 - 4k > 0$

$20 > 4k$

$k < 5$

</details>

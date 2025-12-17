# Definición de la Circunferencia

La circunferencia es una de las figuras geométricas más perfectas y fascinantes. Desde las ruedas hasta las órbitas de los planetas, los círculos están en todas partes. En geometría analítica, estudiaremos cómo representar una circunferencia mediante una ecuación.

---

## 🎯 ¿Qué vas a aprender?

- La definición de circunferencia como lugar geométrico
- Sus elementos fundamentales
- Cómo construir la ecuación a partir de la definición

---

## 📖 Lo Esencial de la Circunferencia

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/elementos-circunferencia.svg" alt="Elementos de la circunferencia" style="width: 100%; height: auto;" />
</div>

| Elemento | Símbolo | Descripción |
|----------|---------|-------------|
| Centro | $C(h, k)$ | Punto equidistante de todos los puntos de la circunferencia |
| Radio | $r$ | Distancia del centro a cualquier punto de la circunferencia |
| Diámetro | $d = 2r$ | Segmento que pasa por el centro uniendo dos puntos |
| Cuerda | — | Segmento que une dos puntos de la circunferencia |

---

## 📖 Definición como Lugar Geométrico

> Una **circunferencia** es el lugar geométrico de todos los puntos del plano que están a una **distancia fija** (radio $r$) de un punto fijo (centro $C$).

Matemáticamente, si el centro es $C(h, k)$ y el radio es $r$:

$$
\text{Circunferencia} = \{P(x, y) : d(P, C) = r\}
$$

Es decir, un punto $P(x, y)$ pertenece a la circunferencia si y solo si:

$$
\sqrt{(x - h)^2 + (y - k)^2} = r
$$

---

## 📖 Construcción de la Ecuación

A partir de la definición de distancia:

$$
\sqrt{(x - h)^2 + (y - k)^2} = r
$$

Elevando al cuadrado ambos lados:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

Esta es la **ecuación canónica** (u ordinaria) de la circunferencia.

### Caso especial: Centro en el origen

Si el centro está en el origen $C(0, 0)$:

$$
x^2 + y^2 = r^2
$$

---

## 📖 Elementos de la Circunferencia

### Centro
El **centro** $C(h, k)$ es el punto desde el cual todos los puntos de la circunferencia están a igual distancia.

### Radio
El **radio** $r$ es la distancia constante del centro a cualquier punto de la circunferencia. Siempre es positivo: $r > 0$.

### Diámetro
El **diámetro** es el segmento que pasa por el centro y tiene sus extremos en la circunferencia. Su longitud es $d = 2r$.

### Cuerda
Una **cuerda** es un segmento cuyos extremos están sobre la circunferencia. El diámetro es la cuerda de mayor longitud.

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Circunferencia con centro en el origen

Escribe la ecuación de la circunferencia con centro en $(0, 0)$ y radio 4.

$$
x^2 + y^2 = 16
$$

### ⚙️ Ejemplo 2: Circunferencia con centro desplazado

Escribe la ecuación de la circunferencia con centro en $(3, -2)$ y radio 5.

$$
(x - 3)^2 + (y - (-2))^2 = 25
$$

$$
(x - 3)^2 + (y + 2)^2 = 25
$$

### ⚙️ Ejemplo 3: Identificar centro y radio

Identifica el centro y radio de $(x + 1)^2 + (y - 4)^2 = 9$.

**Centro:** Comparamos con $(x - h)^2 + (y - k)^2 = r^2$

- $(x + 1) = (x - (-1))$ → $h = -1$
- $(y - 4)$ → $k = 4$
- $r^2 = 9$ → $r = 3$

**Respuesta:** Centro $C(-1, 4)$, radio $r = 3$.

### ⚙️ Ejemplo 4: Verificar si un punto pertenece

¿El punto $(3, 4)$ está sobre la circunferencia $x^2 + y^2 = 25$?

**Verificamos:**
$$
3^2 + 4^2 = 9 + 16 = 25 ✓
$$

Sí, el punto está sobre la circunferencia.

### ⚙️ Ejemplo 5: Circunferencia dado centro y un punto

Encuentra la ecuación de la circunferencia con centro en $(2, 1)$ que pasa por $(5, 5)$.

**Paso 1:** Calcular el radio (distancia del centro al punto):
$$
r = \sqrt{(5-2)^2 + (5-1)^2} = \sqrt{9 + 16} = 5
$$

**Paso 2:** Escribir la ecuación:
$$
(x - 2)^2 + (y - 1)^2 = 25
$$

---

## 📖 Interior, Exterior y Frontera

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/interior-exterior-circ.svg" alt="Interior, exterior y frontera" style="width: 100%; height: auto;" />
</div>

Para una circunferencia $(x - h)^2 + (y - k)^2 = r^2$:

| Ubicación del punto $P(x_0, y_0)$ | Condición |
|----------------------------------|-----------|
| Sobre la circunferencia | $(x_0 - h)^2 + (y_0 - k)^2 = r^2$ |
| Interior | $(x_0 - h)^2 + (y_0 - k)^2 < r^2$ |
| Exterior | $(x_0 - h)^2 + (y_0 - k)^2 > r^2$ |

### ⚙️ Ejemplo 6: Clasificar puntos

Para la circunferencia $x^2 + y^2 = 25$, clasifica los puntos $(0, 0)$, $(3, 4)$ y $(4, 4)$.

**Punto $(0, 0)$:** $0 + 0 = 0 < 25$ → **Interior**

**Punto $(3, 4)$:** $9 + 16 = 25$ → **Sobre la circunferencia**

**Punto $(4, 4)$:** $16 + 16 = 32 > 25$ → **Exterior**

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| Definición | Puntos a distancia $r$ de un centro $C$ |
| Ecuación canónica | $(x - h)^2 + (y - k)^2 = r^2$ |
| Centro en origen | $x^2 + y^2 = r^2$ |
| Radio | $r = \sqrt{(x_0-h)^2 + (y_0-k)^2}$ para punto conocido |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la ecuación de la circunferencia con centro $(-4, 3)$ y radio 6.

<details>
<summary>Ver solución</summary>

$$
(x + 4)^2 + (y - 3)^2 = 36
$$

</details>

### Ejercicio 2
Identifica el centro y radio de $(x - 5)^2 + (y + 2)^2 = 49$.

<details>
<summary>Ver solución</summary>

Centro: $(5, -2)$
Radio: $r = 7$

</details>

### Ejercicio 3
¿El punto $(1, 1)$ está dentro, fuera o sobre la circunferencia $(x-2)^2 + (y-2)^2 = 4$?

<details>
<summary>Ver solución</summary>

$(1-2)^2 + (1-2)^2 = 1 + 1 = 2$

Como $2 < 4$, el punto está en el **interior**.

</details>

### Ejercicio 4
Encuentra la ecuación de la circunferencia con centro en $(0, 3)$ que pasa por el origen.

<details>
<summary>Ver solución</summary>

Radio = distancia de $(0, 3)$ al origen:
$$
r = \sqrt{0 + 9} = 3
$$

Ecuación:
$$
x^2 + (y - 3)^2 = 9
$$

</details>

### Ejercicio 5
Una circunferencia tiene como diámetro el segmento de $A(1, 2)$ a $B(7, 10)$. Encuentra su ecuación.

<details>
<summary>Ver solución</summary>

**Centro** (punto medio del diámetro):
$$
C = \left(\frac{1+7}{2}, \frac{2+10}{2}\right) = (4, 6)
$$

**Radio** (mitad del diámetro):
$$
d = \sqrt{(7-1)^2 + (10-2)^2} = \sqrt{36 + 64} = 10
$$
$$
r = 5
$$

**Ecuación:**
$$
(x - 4)^2 + (y - 6)^2 = 25
$$

</details>

# Área de Triángulos y Polígonos

¿Cómo calcular el área de una figura cuando solo conocemos las coordenadas de sus vértices? La geometría analítica nos da una fórmula elegante basada en **determinantes** que funciona para triángulos y polígonos de cualquier forma.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula del área de un triángulo usando coordenadas
- La fórmula del "cordón de zapato" para polígonos
- Cómo determinar si tres puntos son colineales

---

## 📖 Lo Esencial de Áreas con Coordenadas

| Figura | Fórmula |
|--------|---------|
| Triángulo con vértices $(x_1, y_1)$, $(x_2, y_2)$, $(x_3, y_3)$ | $A = \dfrac{1}{2}\|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)\|$ |
| Polígono de $n$ vértices (cordón de zapato) | $A = \dfrac{1}{2}\left\|\sum_{i=1}^{n}(x_i y_{i+1} - x_{i+1} y_i)\right\|$ |
| Puntos colineales | Área = 0 |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/area-triangulo.svg" alt="Área de un triángulo usando coordenadas" style="width: 100%; height: auto;" />
</div>

---

## 📖 Área de un Triángulo

Dado un triángulo con vértices $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$, su área es:

$$
\text{Área} = \frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|
$$

O en forma de determinante:

$$
\text{Área} = \frac{1}{2} \left| \begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix} \right|
$$

> 💡 **¿Por qué valor absoluto?** Porque dependiendo del orden de los puntos, la fórmula puede dar resultado positivo o negativo. El área siempre es positiva.

### ⚙️ Ejemplo 1: Triángulo con vértices A(1, 1), B(5, 1), C(3, 5)

**Identificamos las coordenadas:**
- $(x_1, y_1) = (1, 1)$
- $(x_2, y_2) = (5, 1)$
- $(x_3, y_3) = (3, 5)$

**Aplicamos la fórmula:**

$$
\text{Área} = \frac{1}{2} |1(1 - 5) + 5(5 - 1) + 3(1 - 1)|
$$

$$
\text{Área} = \frac{1}{2} |1(-4) + 5(4) + 3(0)|
$$

$$
\text{Área} = \frac{1}{2} |-4 + 20 + 0| = \frac{1}{2} |16| = 8
$$

**Respuesta:** El área del triángulo es 8 unidades cuadradas.

### ⚙️ Ejemplo 2: Triángulo con vértices P(0, 0), Q(6, 0), R(4, 5)

**Coordenadas:**
- $(x_1, y_1) = (0, 0)$
- $(x_2, y_2) = (6, 0)$
- $(x_3, y_3) = (4, 5)$

**Cálculo:**

$$
\text{Área} = \frac{1}{2} |0(0 - 5) + 6(5 - 0) + 4(0 - 0)|
$$

$$
\text{Área} = \frac{1}{2} |0 + 30 + 0| = 15
$$

**Respuesta:** El área es 15 unidades cuadradas.

---

## 📖 Puntos Colineales

Tres puntos son **colineales** (están sobre la misma línea) si y solo si el área del "triángulo" que forman es **cero**.

> Si el área = 0, los puntos están alineados.

### ⚙️ Ejemplo 3: ¿Son colineales los puntos A(1, 2), B(3, 4), C(5, 6)?

**Calculamos el área:**

$$
\text{Área} = \frac{1}{2} |1(4 - 6) + 3(6 - 2) + 5(2 - 4)|
$$

$$
\text{Área} = \frac{1}{2} |1(-2) + 3(4) + 5(-2)|
$$

$$
\text{Área} = \frac{1}{2} |-2 + 12 - 10| = \frac{1}{2} |0| = 0
$$

**Respuesta:** Sí, los puntos son colineales porque el área es 0.

---

## 📖 Fórmula del Cordón de Zapato (Polígonos)

Para calcular el área de cualquier polígono con vértices $(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)$ ordenados en sentido antihorario o horario, usamos la **fórmula del cordón de zapato** (Shoelace formula):

$$
\text{Área} = \frac{1}{2} \left| \sum_{i=1}^{n-1}(x_i y_{i+1} - x_{i+1} y_i) + (x_n y_1 - x_1 y_n) \right|
$$

### Procedimiento visual:

1. Lista los vértices en orden (horario o antihorario)
2. Repite el primer vértice al final
3. Multiplica en diagonal (↘) y suma
4. Multiplica en diagonal (↙) y suma
5. Resta y divide entre 2

### ⚙️ Ejemplo 4: Área de un cuadrilátero

Encuentra el área del cuadrilátero con vértices $A(1, 1)$, $B(4, 1)$, $C(5, 4)$, $D(2, 5)$.

**Organizamos los vértices (y repetimos el primero al final):**

| Vértice | $x$ | $y$ |
|---------|-----|-----|
| A | 1 | 1 |
| B | 4 | 1 |
| C | 5 | 4 |
| D | 2 | 5 |
| A | 1 | 1 |

**Productos diagonales ↘ (hacia abajo-derecha):**
$$
(1 \times 1) + (4 \times 4) + (5 \times 5) + (2 \times 1) = 1 + 16 + 25 + 2 = 44
$$

**Productos diagonales ↙ (hacia abajo-izquierda):**
$$
(1 \times 4) + (1 \times 5) + (4 \times 2) + (5 \times 1) = 4 + 5 + 8 + 5 = 22
$$

**Área:**
$$
\text{Área} = \frac{1}{2} |44 - 22| = \frac{1}{2} \times 22 = 11
$$

**Respuesta:** El área del cuadrilátero es 11 unidades cuadradas.

### ⚙️ Ejemplo 5: Pentágono

Encuentra el área del pentágono con vértices $(0, 0)$, $(4, 0)$, $(5, 3)$, $(2, 5)$, $(-1, 3)$.

**Tabla de coordenadas:**

| $x$ | $y$ |
|-----|-----|
| 0 | 0 |
| 4 | 0 |
| 5 | 3 |
| 2 | 5 |
| -1 | 3 |
| 0 | 0 |

**Suma ↘:** $(0 \times 0) + (4 \times 3) + (5 \times 5) + (2 \times 3) + (-1 \times 0)$
$$= 0 + 12 + 25 + 6 + 0 = 43$$

**Suma ↙:** $(0 \times 4) + (0 \times 5) + (3 \times 2) + (5 \times (-1)) + (3 \times 0)$
$$= 0 + 0 + 6 - 5 + 0 = 1$$

**Área:**
$$
\text{Área} = \frac{1}{2} |43 - 1| = \frac{42}{2} = 21
$$

**Respuesta:** El área del pentágono es 21 unidades cuadradas.

---

## 🔑 Resumen

| Concepto | Aplicación |
|----------|------------|
| Fórmula del área del triángulo | Conociendo 3 vértices |
| Fórmula del cordón de zapato | Polígonos de cualquier número de lados |
| Área = 0 | Los puntos son colineales |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el área del triángulo con vértices $A(2, 1)$, $B(6, 1)$, $C(4, 5)$.

<details>
<summary>Ver solución</summary>

$$
\text{Área} = \frac{1}{2} |2(1 - 5) + 6(5 - 1) + 4(1 - 1)|
$$

$$
= \frac{1}{2} |2(-4) + 6(4) + 0|
$$

$$
= \frac{1}{2} |-8 + 24| = \frac{1}{2} \times 16 = 8
$$

**Respuesta:** 8 unidades cuadradas

</details>

### Ejercicio 2
Determina si los puntos $A(2, 3)$, $B(4, 7)$, $C(6, 11)$ son colineales.

<details>
<summary>Ver solución</summary>

$$
\text{Área} = \frac{1}{2} |2(7 - 11) + 4(11 - 3) + 6(3 - 7)|
$$

$$
= \frac{1}{2} |2(-4) + 4(8) + 6(-4)|
$$

$$
= \frac{1}{2} |-8 + 32 - 24| = \frac{1}{2} |0| = 0
$$

**Respuesta:** Sí, son colineales porque el área es 0.

</details>

### Ejercicio 3
Calcula el área del triángulo con vértices $A(-2, -1)$, $B(4, 3)$, $C(0, 5)$.

<details>
<summary>Ver solución</summary>

$$
\text{Área} = \frac{1}{2} |(-2)(3 - 5) + 4(5 - (-1)) + 0((-1) - 3)|
$$

$$
= \frac{1}{2} |(-2)(-2) + 4(6) + 0(-4)|
$$

$$
= \frac{1}{2} |4 + 24 + 0| = \frac{28}{2} = 14
$$

**Respuesta:** 14 unidades cuadradas

</details>

### Ejercicio 4
Encuentra el área del rectángulo con vértices $A(0, 0)$, $B(6, 0)$, $C(6, 4)$, $D(0, 4)$ usando la fórmula del cordón de zapato.

<details>
<summary>Ver solución</summary>

**Tabla de coordenadas:**

| $x$ | $y$ |
|-----|-----|
| 0 | 0 |
| 6 | 0 |
| 6 | 4 |
| 0 | 4 |
| 0 | 0 |

**Suma ↘:** $(0 \times 0) + (6 \times 4) + (6 \times 4) + (0 \times 0) = 0 + 24 + 24 + 0 = 48$

**Suma ↙:** $(0 \times 6) + (0 \times 6) + (4 \times 0) + (4 \times 0) = 0 + 0 + 0 + 0 = 0$

**Área:**
$$
\text{Área} = \frac{1}{2} |48 - 0| = 24
$$

**Verificación:** Base × Altura = $6 \times 4 = 24$ ✓

**Respuesta:** 24 unidades cuadradas

</details>

### Ejercicio 5
El triángulo con vértices $A(1, 2)$, $B(k, 4)$, $C(7, 6)$ tiene área 0. Encuentra el valor de $k$.

<details>
<summary>Ver solución</summary>

Si el área es 0, los puntos son colineales:

$$
0 = \frac{1}{2} |1(4 - 6) + k(6 - 2) + 7(2 - 4)|
$$

$$
0 = 1(-2) + k(4) + 7(-2)
$$

$$
0 = -2 + 4k - 14
$$

$$
0 = 4k - 16
$$

$$
k = 4
$$

**Respuesta:** $k = 4$

**Verificación:** Los puntos $A(1, 2)$, $B(4, 4)$, $C(7, 6)$ están sobre la recta $y = x + 1$ ✓

</details>

# Cálculo de la Pendiente

Ahora que entiendes qué es la pendiente, es momento de aprender a **calcularla**. Dados dos puntos en una recta, existe una fórmula sencilla que nos permite encontrar su pendiente.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula para calcular la pendiente
- Cómo aplicarla con diferentes tipos de puntos
- Casos especiales y errores comunes

---

## 📖 Lo Esencial del Cálculo de Pendiente

| Fórmula | Descripción |
|---------|-------------|
| $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ | Pendiente dados dos puntos |
| $m = \dfrac{\Delta y}{\Delta x}$ | Cambio en $y$ sobre cambio en $x$ |

---

## 📖 Fórmula de la Pendiente

Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ sobre una recta, la pendiente $m$ es:

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

También se escribe como:

$$
m = \frac{\Delta y}{\Delta x}
$$

donde $\Delta y = y_2 - y_1$ (cambio en $y$) y $\Delta x = x_2 - x_1$ (cambio en $x$).

> 💡 **Importante:** No importa cuál punto elijas como "primero" o "segundo", siempre obtendrás la misma pendiente (siempre que seas consistente).

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Puntos con coordenadas positivas

Calcula la pendiente de la recta que pasa por $A(2, 3)$ y $B(6, 7)$.

**Datos:**
- $(x_1, y_1) = (2, 3)$
- $(x_2, y_2) = (6, 7)$

**Aplicamos la fórmula:**

$$
m = \frac{7 - 3}{6 - 2} = \frac{4}{4} = 1
$$

**Respuesta:** La pendiente es $m = 1$.

> La recta sube a 45°, por cada unidad horizontal sube una vertical.

### ⚙️ Ejemplo 2: Pendiente negativa

Calcula la pendiente de la recta que pasa por $P(1, 8)$ y $Q(5, 2)$.

**Datos:**
- $(x_1, y_1) = (1, 8)$
- $(x_2, y_2) = (5, 2)$

**Cálculo:**

$$
m = \frac{2 - 8}{5 - 1} = \frac{-6}{4} = -\frac{3}{2}
$$

**Respuesta:** La pendiente es $m = -\frac{3}{2}$.

> La recta baja (pendiente negativa): por cada 2 unidades a la derecha, baja 3.

### ⚙️ Ejemplo 3: Puntos con coordenadas negativas

Calcula la pendiente de la recta que pasa por $A(-3, -2)$ y $B(4, 5)$.

**Datos:**
- $(x_1, y_1) = (-3, -2)$
- $(x_2, y_2) = (4, 5)$

**Cálculo:**

$$
m = \frac{5 - (-2)}{4 - (-3)} = \frac{5 + 2}{4 + 3} = \frac{7}{7} = 1
$$

**Respuesta:** La pendiente es $m = 1$.

### ⚙️ Ejemplo 4: Recta horizontal

Calcula la pendiente de la recta que pasa por $P(-2, 5)$ y $Q(7, 5)$.

**Observación:** Ambos puntos tienen la misma ordenada ($y = 5$).

**Cálculo:**

$$
m = \frac{5 - 5}{7 - (-2)} = \frac{0}{9} = 0
$$

**Respuesta:** La pendiente es $m = 0$ (recta horizontal).

### ⚙️ Ejemplo 5: Recta vertical

Calcula la pendiente de la recta que pasa por $A(3, 1)$ y $B(3, 8)$.

**Observación:** Ambos puntos tienen la misma abscisa ($x = 3$).

**Cálculo:**

$$
m = \frac{8 - 1}{3 - 3} = \frac{7}{0}
$$

**Respuesta:** La pendiente es **indefinida** (no existe).

> División entre cero significa que la recta es vertical.

---

## 📖 El Orden de los Puntos No Importa

Verifiquemos con el Ejemplo 1:

**Forma 1:** $P_1 = A(2, 3)$, $P_2 = B(6, 7)$

$$
m = \frac{7 - 3}{6 - 2} = \frac{4}{4} = 1
$$

**Forma 2:** $P_1 = B(6, 7)$, $P_2 = A(2, 3)$

$$
m = \frac{3 - 7}{2 - 6} = \frac{-4}{-4} = 1
$$

¡El mismo resultado! La clave es ser **consistente**: si restas $y_2 - y_1$ arriba, debes restar $x_2 - x_1$ abajo.

---

## 📖 Verificación con Triángulo Rectángulo

Podemos visualizar el cálculo de la pendiente como un triángulo rectángulo:

- El **cateto horizontal** es $\Delta x = x_2 - x_1$
- El **cateto vertical** es $\Delta y = y_2 - y_1$
- La pendiente es la razón entre ellos: $m = \frac{\Delta y}{\Delta x}$

### ⚙️ Ejemplo 6: Visualización

Para los puntos $A(1, 2)$ y $B(4, 8)$:

- $\Delta x = 4 - 1 = 3$
- $\Delta y = 8 - 2 = 6$
- $m = \frac{6}{3} = 2$

Esto significa: "avanzamos 3 hacia la derecha y subimos 6".

---

## 🔑 Resumen

| Situación | Resultado |
|-----------|-----------|
| $\Delta x \neq 0$ | $m = \frac{\Delta y}{\Delta x}$ |
| $\Delta y = 0$ | $m = 0$ (recta horizontal) |
| $\Delta x = 0$ | $m$ indefinida (recta vertical) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la pendiente de la recta que pasa por $A(0, 0)$ y $B(4, 12)$.

<details>
<summary>Ver solución</summary>

$$
m = \frac{12 - 0}{4 - 0} = \frac{12}{4} = 3
$$

**Respuesta:** $m = 3$

</details>

### Ejercicio 2
Calcula la pendiente de la recta que pasa por $P(-3, 7)$ y $Q(2, -3)$.

<details>
<summary>Ver solución</summary>

$$
m = \frac{-3 - 7}{2 - (-3)} = \frac{-10}{5} = -2
$$

**Respuesta:** $m = -2$

</details>

### Ejercicio 3
Determina la pendiente de la recta que pasa por $A(5, -2)$ y $B(-1, -2)$.

<details>
<summary>Ver solución</summary>

$$
m = \frac{-2 - (-2)}{-1 - 5} = \frac{0}{-6} = 0
$$

**Respuesta:** $m = 0$ (recta horizontal, ecuación $y = -2$)

</details>

### Ejercicio 4
Tres puntos $A(1, 3)$, $B(3, 7)$ y $C(5, 11)$ ¿están sobre la misma recta?

<details>
<summary>Ver solución</summary>

Calculamos las pendientes entre pares de puntos:

**Pendiente AB:**
$$
m_{AB} = \frac{7 - 3}{3 - 1} = \frac{4}{2} = 2
$$

**Pendiente BC:**
$$
m_{BC} = \frac{11 - 7}{5 - 3} = \frac{4}{2} = 2
$$

Como $m_{AB} = m_{BC} = 2$, los tres puntos están **alineados** (colineales).

**Respuesta:** Sí, están sobre la misma recta.

</details>

### Ejercicio 5
El punto $A(-2, 3)$ y el punto $B(4, k)$ están sobre una recta con pendiente $m = 2$. Encuentra el valor de $k$.

<details>
<summary>Ver solución</summary>

Usando la fórmula de la pendiente:

$$
2 = \frac{k - 3}{4 - (-2)} = \frac{k - 3}{6}
$$

Despejamos $k$:

$$
k - 3 = 2 \times 6 = 12
$$

$$
k = 15
$$

**Respuesta:** $k = 15$

**Verificación:** $m = \frac{15 - 3}{4 - (-2)} = \frac{12}{6} = 2$ ✓

</details>

# Punto Medio de un Segmento

Si tienes que encontrarte con un amigo que está a cierta distancia de ti, ¿cuál es el punto justo a la mitad del camino? En geometría analítica, este problema tiene una solución muy elegante: la **fórmula del punto medio**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el punto medio de un segmento
- La fórmula para calcularlo
- Cómo aplicarla en diferentes situaciones

---

## 📖 Lo Esencial del Punto Medio

| Concepto | Fórmula |
|----------|---------|
| Punto medio | $M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)$ |
| Coordenada $x$ del punto medio | $x_M = \dfrac{x_1 + x_2}{2}$ |
| Coordenada $y$ del punto medio | $y_M = \dfrac{y_1 + y_2}{2}$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/punto-medio.svg" alt="Punto medio de un segmento" style="width: 100%; height: auto;" />
</div>

---

## 📖 Concepto de Punto Medio

> El **punto medio** de un segmento es el punto que lo divide en dos partes iguales.

Si tenemos un segmento con extremos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$, el punto medio $M$ cumple que:
- La distancia de $P_1$ a $M$ es igual a la distancia de $M$ a $P_2$
- $M$ está exactamente a la mitad entre $P_1$ y $P_2$

---

## 📖 Deducción de la Fórmula

Para encontrar el punto medio, simplemente calculamos el **promedio** de las coordenadas:

**Para la coordenada x:**
- El punto medio en x está a la mitad entre $x_1$ y $x_2$
- Eso es el promedio: $x_M = \dfrac{x_1 + x_2}{2}$

**Para la coordenada y:**
- El punto medio en y está a la mitad entre $y_1$ y $y_2$
- Eso es el promedio: $y_M = \dfrac{y_1 + y_2}{2}$

### Fórmula del Punto Medio

Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$, el punto medio $M$ es:

$$
M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)
$$

> 💡 **Truco para recordar:** El punto medio es simplemente el "promedio" de los puntos. ¡Sumas y divides entre 2!

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Punto medio entre A(2, 4) y B(6, 8)

**Datos:**
- $P_1 = A(2, 4)$ → $x_1 = 2$, $y_1 = 4$
- $P_2 = B(6, 8)$ → $x_2 = 6$, $y_2 = 8$

**Aplicamos la fórmula:**

$$
x_M = \frac{2 + 6}{2} = \frac{8}{2} = 4
$$

$$
y_M = \frac{4 + 8}{2} = \frac{12}{2} = 6
$$

**Respuesta:** El punto medio es $M(4, 6)$.

### ⚙️ Ejemplo 2: Punto medio entre P(-3, 5) y Q(7, -1)

**Datos:**
- $x_1 = -3$, $y_1 = 5$
- $x_2 = 7$, $y_2 = -1$

**Cálculo:**

$$
x_M = \frac{-3 + 7}{2} = \frac{4}{2} = 2
$$

$$
y_M = \frac{5 + (-1)}{2} = \frac{4}{2} = 2
$$

**Respuesta:** El punto medio es $M(2, 2)$.

### ⚙️ Ejemplo 3: Punto medio entre R(-4, -2) y S(-8, 6)

**Datos:**
- $x_1 = -4$, $y_1 = -2$
- $x_2 = -8$, $y_2 = 6$

**Cálculo:**

$$
x_M = \frac{-4 + (-8)}{2} = \frac{-12}{2} = -6
$$

$$
y_M = \frac{-2 + 6}{2} = \frac{4}{2} = 2
$$

**Respuesta:** El punto medio es $M(-6, 2)$.

---

## 📖 Problema Inverso: Encontrar un Extremo

A veces conocemos un extremo y el punto medio, y necesitamos encontrar el **otro extremo**.

### Estrategia

Si $M$ es el punto medio de $P_1$ y $P_2$, entonces:

$$
x_M = \frac{x_1 + x_2}{2} \Rightarrow x_2 = 2x_M - x_1
$$

$$
y_M = \frac{y_1 + y_2}{2} \Rightarrow y_2 = 2y_M - y_1
$$

### ⚙️ Ejemplo 4: Encontrar el otro extremo

Si $A(3, 1)$ es un extremo de un segmento y $M(5, 4)$ es su punto medio, ¿cuál es el otro extremo $B$?

**Despejamos $B(x_2, y_2)$:**

$$
x_2 = 2(5) - 3 = 10 - 3 = 7
$$

$$
y_2 = 2(4) - 1 = 8 - 1 = 7
$$

**Respuesta:** El otro extremo es $B(7, 7)$.

**Verificación:** 
$$
M = \left(\frac{3 + 7}{2}, \frac{1 + 7}{2}\right) = \left(\frac{10}{2}, \frac{8}{2}\right) = (5, 4) ✓
$$

---

## 📖 Aplicación: Centro de un Segmento Diagonal

El punto medio también nos permite encontrar el **centro de figuras geométricas**.

### ⚙️ Ejemplo 5: Centro de un rectángulo

Un rectángulo tiene vértices opuestos en $A(-2, -1)$ y $C(6, 5)$. Encuentra su centro.

El centro de un rectángulo está en el punto medio de su diagonal.

$$
x_c = \frac{-2 + 6}{2} = \frac{4}{2} = 2
$$

$$
y_c = \frac{-1 + 5}{2} = \frac{4}{2} = 2
$$

**Respuesta:** El centro del rectángulo es $(2, 2)$.

---

## 🔑 Resumen

| Problema | Fórmula |
|----------|---------|
| Punto medio de $P_1$ y $P_2$ | $M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)$ |
| Encontrar extremo $P_2$ dado $P_1$ y $M$ | $x_2 = 2x_M - x_1$, $y_2 = 2y_M - y_1$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el punto medio del segmento con extremos $A(4, 7)$ y $B(-2, 3)$.

<details>
<summary>Ver solución</summary>

$$
x_M = \frac{4 + (-2)}{2} = \frac{2}{2} = 1
$$

$$
y_M = \frac{7 + 3}{2} = \frac{10}{2} = 5
$$

**Respuesta:** $M(1, 5)$

</details>

### Ejercicio 2
Encuentra el punto medio entre $P(0, 0)$ y $Q(8, -6)$.

<details>
<summary>Ver solución</summary>

$$
x_M = \frac{0 + 8}{2} = 4
$$

$$
y_M = \frac{0 + (-6)}{2} = -3
$$

**Respuesta:** $M(4, -3)$

</details>

### Ejercicio 3
Si $A(-1, 5)$ es un extremo de un segmento y $M(2, 3)$ es su punto medio, encuentra el otro extremo $B$.

<details>
<summary>Ver solución</summary>

Usamos las fórmulas para encontrar el extremo:

$$
x_2 = 2(2) - (-1) = 4 + 1 = 5
$$

$$
y_2 = 2(3) - 5 = 6 - 5 = 1
$$

**Respuesta:** $B(5, 1)$

**Verificación:**
$$
M = \left(\frac{-1 + 5}{2}, \frac{5 + 1}{2}\right) = \left(\frac{4}{2}, \frac{6}{2}\right) = (2, 3) ✓
$$

</details>

### Ejercicio 4
Un triángulo tiene vértices en $A(0, 0)$, $B(6, 0)$ y $C(3, 6)$. Encuentra el punto medio de cada lado.

<details>
<summary>Ver solución</summary>

**Punto medio de AB:**
$$
M_{AB} = \left(\frac{0 + 6}{2}, \frac{0 + 0}{2}\right) = (3, 0)
$$

**Punto medio de BC:**
$$
M_{BC} = \left(\frac{6 + 3}{2}, \frac{0 + 6}{2}\right) = (4.5, 3)
$$

**Punto medio de CA:**
$$
M_{CA} = \left(\frac{3 + 0}{2}, \frac{6 + 0}{2}\right) = (1.5, 3)
$$

**Respuestas:** $M_{AB}(3, 0)$, $M_{BC}(4.5, 3)$, $M_{CA}(1.5, 3)$

</details>

### Ejercicio 5
El punto $M(4, -2)$ es el punto medio del segmento $\overline{PQ}$. Si $P$ está en el origen, ¿dónde está $Q$?

<details>
<summary>Ver solución</summary>

Dado $P(0, 0)$ y $M(4, -2)$:

$$
x_Q = 2(4) - 0 = 8
$$

$$
y_Q = 2(-2) - 0 = -4
$$

**Respuesta:** $Q(8, -4)$

**Verificación:**
$$
M = \left(\frac{0 + 8}{2}, \frac{0 + (-4)}{2}\right) = (4, -2) ✓
$$

</details>

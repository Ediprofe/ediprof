# **Distancia y Punto Medio**

Cuando tenemos dos puntos en un mapa, a menudo queremos saber dos cosas: ¿qué tan lejos están el uno del otro? y ¿dónde está exactamente la mitad del camino entre ellos? Para responder esto no necesitamos una regla, sino un par de fórmulas matemáticas muy sencillas basadas en el sentido común y la geometría.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular la distancia exacta entre dos puntos usando Pitágoras.
- Cómo encontrar el punto que divide un segmento justo a la mitad.
- Por qué las diferencias de coordenadas nos dan la clave de la distancia.
- Aplicaciones prácticas de estas medidas en el plano.

---

## 📏 Distancia entre dos Puntos

Imagina que quieres ir de un punto $A$ a un punto $B$. Si trazas líneas horizontales y verticales, formas un triángulo rectángulo. El camino directo es la hipotenusa. Por eso usamos el **Teorema de Pitágoras**.

La fórmula para la distancia $d$ es:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

---

## 📍 Punto Medio

El punto medio es simplemente el **promedio** de las posiciones. Sumamos las coordenadas correspondientes y las dividimos entre dos.

$$
M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Distancia Estándar

Calcula la distancia entre $P_1(1, 2)$ y $P_2(4, 6)$.

**Razonamiento:**
Identificamos $x_1=1, y_1=2, x_2=4, y_2=6$. Aplicamos fórmula:

$$
d = \sqrt{(4 - 1)^2 + (6 - 2)^2}
$$

$$
d = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25}
$$

**Resultado:**

$$
\boxed{5}
$$

---

### Ejemplo 2: Punto Medio

Encuentra el punto medio entre $A(2, 10)$ y $B(8, 4)$.

**Razonamiento:**
Promediamos las $x$: $(2 + 8)/2 = 5$.
Promediamos las $y$: $(10 + 4)/2 = 7$.

**Resultado:**

$$
\boxed{M(5, 7)}
$$

---

### Ejemplo 3: Distancia con Negativos

Encuentra la distancia entre $A(-1, -1)$ y $B(2, 3)$.

**Razonamiento:**
Cuidado con los signos al restar: $2 - (-1) = 3$.

$$
d = \sqrt{(3)^2 + (4)^2} = \sqrt{9 + 16} = \sqrt{25}
$$

**Resultado:**

$$
\boxed{5}
$$

---

### Ejemplo 4: Distancia en Línea Recta

Encuentra la distancia entre $P(2, 8)$ y $Q(2, -2)$.

**Razonamiento:**
Como la $x$ es la misma (2), es una línea vertical. Solo restamos las $y$:
$$
8 - (-2) = 10
$$

**Resultado:**

$$
\boxed{10}
$$

---

### Ejemplo 5: Punto Medio en el Origen

Halla el punto medio entre $R(-10, 5)$ y $S(10, -5)$.

**Razonamiento:**
Promedio de $x$: $(-10 + 10)/2 = 0$.
Promedio de $y$: $(5 - 5)/2 = 0$.

**Resultado:**

$$
\boxed{M(0, 0)}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la distancia entre $(0, 0)$ y $(6, 8)$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10
$$

**Resultado:** $\boxed{10}$

</details>

---

### Ejercicio 2
Calcula el punto medio entre $(1, 5)$ y $(7, 9)$.

<details>
<summary>Ver solución</summary>

$$
M = \left( \frac{1+7}{2}, \frac{5+9}{2} \right) = (4, 7)
$$

**Resultado:** $\boxed{(4, 7)}$

</details>

---

### Ejercicio 3
¿Cuál es la distancia entre $(-3, 0)$ y $(3, 0)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Es una línea horizontal. La distancia es $3 - (-3) = 6$.

**Resultado:** $\boxed{6}$

</details>

---

### Ejercicio 4
Encuentra el punto medio entre $(-4, 2)$ y $(4, -2)$.

<details>
<summary>Ver solución</summary>

$$
M = \left( \frac{0}{2}, \frac{0}{2} \right) = (0, 0)
$$

**Resultado:** $\boxed{(0, 0)}$

</details>

---

### Ejercicio 5
Calcula la distancia entre $(2, 2)$ y $(5, 5)$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{(5-2)^2 + (5-2)^2} = \sqrt{3^2 + 3^2} = \sqrt{18}
$$

**Resultado:** $\boxed{3\sqrt{2}}$

</details>

---

### Ejercicio 6
Si el punto medio entre $(0, 0)$ y $(x, y)$ es $(5, 3)$, ¿cuánto valen $x$ e $y$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** El doble de la mitad.
**Resultado:** $\boxed{x=10, y=6}$

</details>

---

### Ejercicio 7
Encuentra la distancia entre $(1, 10)$ y $(1, -2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Distancia vertical: $10 - (-2) = 12$.
**Resultado:** $\boxed{12}$

</details>

---

### Ejercicio 8
Calcula el punto medio entre $(10, 20)$ y $(20, 10)$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{(15, 15)}$

</details>

---

### Ejercicio 9
Determina la distancia entre $(1, 2)$ y $(-2, -2)$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{(-2-1)^2 + (-2-2)^2} = \sqrt{(-3)^2 + (-4)^2} = \sqrt{9+16} = 5
$$

**Resultado:** $\boxed{5}$

</details>

---

### Ejercicio 10
¿Qué fórmula usarías para saber si un punto está justo en el centro de dos ciudades en un mapa coordenado?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\text{Fórmula del Punto Medio}}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Idea Clave |
|:--- |:---: |:--- |
| **Distancia** | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ | Teorema de Pitágoras. |
| **Punto Medio** | $M = \left( \frac{x_1+x_2}{2}, \frac{y_1+y_2}{2} \right)$ | Promedio de posiciones. |

> **Conclusión:** La distancia nos dice cuánto caminar y el punto medio nos dice dónde descansar. Ambas herramientas son fundamentales para entender la geometría del plano.

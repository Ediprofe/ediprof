# Rectas Notables de un Triángulo

En geometría euclidiana estudiamos las rectas notables de un triángulo (medianas, alturas, mediatrices, bisectrices). Ahora, con geometría analítica, podemos **calcular** sus ecuaciones cuando conocemos las coordenadas de los vértices.

---

## 🎯 ¿Qué vas a aprender?

- Cómo encontrar ecuaciones de mediatrices, alturas y medianas
- Cómo calcular los puntos notables (baricentro, ortocentro, circuncentro)
- Aplicaciones prácticas

---

## 📖 Lo Esencial de Rectas Notables

| Recta | Definición | Punto notable |
|-------|------------|---------------|
| **Mediana** | Une vértice con punto medio del lado opuesto | Baricentro (G) |
| **Altura** | Perpendicular desde vértice al lado opuesto | Ortocentro (H) |
| **Mediatriz** | Perpendicular al lado por su punto medio | Circuncentro (O) |
| **Bisectriz** | Divide ángulo en dos partes iguales | Incentro (I) |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/rectas-notables.svg" alt="Rectas notables del triángulo" style="width: 100%; height: auto;" />
</div>

---

## 📖 Medianas y Baricentro

### Definición
Una **mediana** es el segmento que une un vértice con el **punto medio** del lado opuesto.

### Cálculo de una mediana

Para el triángulo con vértices $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

1. Encuentra el punto medio del lado opuesto
2. Encuentra la ecuación de la recta que une el vértice con ese punto medio

### ⚙️ Ejemplo 1: Mediana desde A

Encuentra la mediana desde $A(0, 0)$ al lado $\overline{BC}$ donde $B(6, 0)$ y $C(3, 6)$.

**Paso 1:** Punto medio de $\overline{BC}$:
$$
M_{BC} = \left(\frac{6+3}{2}, \frac{0+6}{2}\right) = (4.5, 3)
$$

**Paso 2:** Ecuación de la recta $AM$:

Pendiente:
$$
m = \frac{3 - 0}{4.5 - 0} = \frac{3}{4.5} = \frac{2}{3}
$$

Ecuación:
$$
y - 0 = \frac{2}{3}(x - 0)
$$
$$
y = \frac{2}{3}x
$$

### El Baricentro

El **baricentro** (o centroide) $G$ es la intersección de las tres medianas:

$$
G = \left(\frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3}\right)
$$

### ⚙️ Ejemplo 2: Baricentro

Para el triángulo $A(0, 0)$, $B(6, 0)$, $C(3, 6)$:

$$
G = \left(\frac{0 + 6 + 3}{3}, \frac{0 + 0 + 6}{3}\right) = (3, 2)
$$

---

## 📖 Alturas y Ortocentro

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/alturas-ortocentro.svg" alt="Alturas y ortocentro" style="width: 100%; height: auto;" />
</div>

### Definición
Una **altura** es el segmento perpendicular desde un vértice al lado opuesto (o su prolongación).

### Cálculo de una altura

1. Encuentra la pendiente del lado opuesto
2. La altura tiene pendiente perpendicular ($m_\perp = -\frac{1}{m}$)
3. Usa punto-pendiente con el vértice

### ⚙️ Ejemplo 3: Altura desde C

Para el triángulo $A(0, 0)$, $B(6, 0)$, $C(3, 6)$, encuentra la altura desde $C$ a $\overline{AB}$.

**Paso 1:** Pendiente de $\overline{AB}$:
$$
m_{AB} = \frac{0 - 0}{6 - 0} = 0
$$

El lado $AB$ es horizontal.

**Paso 2:** La altura desde $C$ es vertical (perpendicular a horizontal):
$$
x = 3
$$

### ⚙️ Ejemplo 4: Altura con pendientes no triviales

Para $A(1, 2)$, $B(5, 4)$, $C(3, 8)$, encuentra la altura desde $A$ a $\overline{BC}$.

**Paso 1:** Pendiente de $\overline{BC}$:
$$
m_{BC} = \frac{8 - 4}{3 - 5} = \frac{4}{-2} = -2
$$

**Paso 2:** Pendiente perpendicular:
$$
m_\perp = \frac{1}{2}
$$

**Paso 3:** Ecuación de la altura:
$$
y - 2 = \frac{1}{2}(x - 1)
$$
$$
y = \frac{1}{2}x + \frac{3}{2}
$$

### El Ortocentro

El **ortocentro** $H$ es la intersección de las tres alturas. Se calcula encontrando la intersección de dos alturas.

---

## 📖 Mediatrices y Circuncentro

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/mediatrices-circuncentro.svg" alt="Mediatrices y circuncentro" style="width: 100%; height: auto;" />
</div>

### Definición
Una **mediatriz** es la recta perpendicular a un lado que pasa por su punto medio.

### Cálculo de una mediatriz

1. Encuentra el punto medio del lado
2. Encuentra la pendiente del lado
3. La mediatriz tiene pendiente perpendicular y pasa por el punto medio

### ⚙️ Ejemplo 5: Mediatriz de un lado

Para $A(0, 0)$ y $B(6, 0)$, encuentra la mediatriz de $\overline{AB}$.

**Paso 1:** Punto medio:
$$
M = (3, 0)
$$

**Paso 2:** Pendiente de $\overline{AB}$: $m = 0$ (horizontal)

**Paso 3:** La mediatriz es vertical:
$$
x = 3
$$

### ⚙️ Ejemplo 6: Mediatriz general

Para $P(2, 1)$ y $Q(6, 5)$, encuentra la mediatriz de $\overline{PQ}$.

**Paso 1:** Punto medio:
$$
M = \left(\frac{2+6}{2}, \frac{1+5}{2}\right) = (4, 3)
$$

**Paso 2:** Pendiente de $\overline{PQ}$:
$$
m = \frac{5-1}{6-2} = 1
$$

**Paso 3:** Pendiente perpendicular: $m_\perp = -1$

**Paso 4:** Ecuación:
$$
y - 3 = -1(x - 4)
$$
$$
y = -x + 7
$$

### El Circuncentro

El **circuncentro** $O$ es la intersección de las tres mediatrices. Es el centro de la circunferencia circunscrita al triángulo.

---

## 📖 Ejemplo Completo

### ⚙️ Ejemplo 7: Todos los puntos notables

Para el triángulo $A(0, 0)$, $B(4, 0)$, $C(2, 4)$:

**Baricentro:**
$$
G = \left(\frac{0+4+2}{3}, \frac{0+0+4}{3}\right) = (2, \frac{4}{3})
$$

**Circuncentro:** (intersección de mediatrices)

Mediatriz de $\overline{AB}$: $x = 2$

Mediatriz de $\overline{AC}$: Punto medio $(1, 2)$, pendiente de AC = $2$, mediatriz: $y - 2 = -\frac{1}{2}(x - 1)$

Sustituyendo $x = 2$: $y = 2 - \frac{1}{2} = \frac{3}{2}$

Circuncentro: $O = (2, \frac{3}{2})$

---

## 🔑 Resumen

| Punto notable | Fórmula directa |
|--------------|-----------------|
| Baricentro | $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$ |
| Circuncentro | Intersección de mediatrices |
| Ortocentro | Intersección de alturas |
| Incentro | Intersección de bisectrices |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Para el triángulo $A(0, 0)$, $B(8, 0)$, $C(4, 6)$, calcula el baricentro.

<details>
<summary>Ver solución</summary>

$$
G = \left(\frac{0+8+4}{3}, \frac{0+0+6}{3}\right) = (4, 2)
$$

</details>

### Ejercicio 2
Encuentra la ecuación de la mediana desde $A(1, 3)$ en el triángulo con $B(5, 1)$ y $C(3, 7)$.

<details>
<summary>Ver solución</summary>

Punto medio de $\overline{BC}$:
$$
M = (4, 4)
$$

Pendiente de $AM$:
$$
m = \frac{4-3}{4-1} = \frac{1}{3}
$$

Ecuación:
$$
y - 3 = \frac{1}{3}(x - 1)
$$
$$
y = \frac{1}{3}x + \frac{8}{3}
$$

</details>

### Ejercicio 3
Encuentra la altura desde $C(0, 6)$ al lado $\overline{AB}$ donde $A(0, 0)$ y $B(8, 4)$.

<details>
<summary>Ver solución</summary>

Pendiente de $\overline{AB}$:
$$
m_{AB} = \frac{4}{8} = \frac{1}{2}
$$

Pendiente de la altura: $m_\perp = -2$

Ecuación:
$$
y - 6 = -2(x - 0)
$$
$$
y = -2x + 6
$$

</details>

### Ejercicio 4
Encuentra la mediatriz del segmento con extremos $P(1, 2)$ y $Q(5, 6)$.

<details>
<summary>Ver solución</summary>

Punto medio: $(3, 4)$

Pendiente de $\overline{PQ}$: $m = \frac{6-2}{5-1} = 1$

Pendiente de la mediatriz: $m_\perp = -1$

Ecuación:
$$
y - 4 = -1(x - 3)
$$
$$
y = -x + 7
$$

O en forma general: $x + y - 7 = 0$

</details>

### Ejercicio 5
Verifica que el baricentro de $A(0, 0)$, $B(6, 0)$, $C(3, 9)$ está a $\frac{2}{3}$ de la distancia de cada vértice al punto medio opuesto.

<details>
<summary>Ver solución</summary>

Baricentro: $G = (3, 3)$

Punto medio de $\overline{BC}$: $M = (4.5, 4.5)$

Distancia $AM$:
$$
|AM| = \sqrt{4.5^2 + 4.5^2} = 4.5\sqrt{2}
$$

Distancia $AG$:
$$
|AG| = \sqrt{3^2 + 3^2} = 3\sqrt{2}
$$

Razón:
$$
\frac{|AG|}{|AM|} = \frac{3\sqrt{2}}{4.5\sqrt{2}} = \frac{3}{4.5} = \frac{2}{3} ✓
$$

</details>

# Construcción de Ecuaciones

Hasta ahora hemos aprendido a analizar ecuaciones dadas. Pero, ¿cómo construimos una ecuación a partir de una descripción geométrica? Esta habilidad es fundamental en geometría analítica.

---

## 🎯 ¿Qué vas a aprender?

- Cómo traducir condiciones geométricas a ecuaciones
- El proceso paso a paso para construir ecuaciones
- Aplicaciones a diferentes tipos de lugares geométricos

---

## 📖 Lo Esencial de Construcción

| Paso | Acción |
|------|--------|
| 1 | Sea $P(x, y)$ un punto genérico del lugar |
| 2 | Traduce la condición geométrica a lenguaje algebraico |
| 3 | Usa fórmulas (distancia, pendiente, etc.) |
| 4 | Simplifica hasta obtener la forma estándar |
| 5 | Verifica con puntos conocidos |

---

## 📖 El Método General

Para construir la ecuación de un lugar geométrico:

### Paso 1: Definir el punto genérico
Sea $P(x, y)$ un punto cualquiera que pertenece al lugar geométrico.

### Paso 2: Escribir la condición
Expresa la condición geométrica en términos de $P(x, y)$ y los datos del problema.

### Paso 3: Aplicar fórmulas
Usa las fórmulas de distancia, pendiente, área, etc.

### Paso 4: Simplificar
Elimina radicales, desarrolla y simplifica.

### Paso 5: Identificar
Reconoce el tipo de curva obtenida.

---

## 📖 Ejemplos de Construcción

### ⚙️ Ejemplo 1: Circunferencia

**Problema:** Encuentra la ecuación del lugar geométrico de los puntos que están a distancia 4 del punto $C(3, -2)$.

**Paso 1:** Sea $P(x, y)$ un punto del lugar.

**Paso 2:** Condición: La distancia de $P$ a $C$ es 4.
$$
d(P, C) = 4
$$

**Paso 3:** Aplicar la fórmula de distancia:
$$
\sqrt{(x - 3)^2 + (y - (-2))^2} = 4
$$

**Paso 4:** Elevar al cuadrado:
$$
(x - 3)^2 + (y + 2)^2 = 16
$$

**Resultado:** Circunferencia con centro $(3, -2)$ y radio $4$.

### ⚙️ Ejemplo 2: Mediatriz

**Problema:** Encuentra la ecuación del lugar geométrico de los puntos equidistantes de $A(1, 3)$ y $B(5, -1)$.

**Paso 1:** Sea $P(x, y)$ un punto del lugar.

**Paso 2:** Condición: $d(P, A) = d(P, B)$

**Paso 3:**
$$
\sqrt{(x-1)^2 + (y-3)^2} = \sqrt{(x-5)^2 + (y+1)^2}
$$

**Paso 4:** Elevamos al cuadrado:
$$
(x-1)^2 + (y-3)^2 = (x-5)^2 + (y+1)^2
$$

Desarrollamos:
$$
x^2 - 2x + 1 + y^2 - 6y + 9 = x^2 - 10x + 25 + y^2 + 2y + 1
$$

Simplificamos:
$$
-2x - 6y + 10 = -10x + 2y + 26
$$

$$
8x - 8y = 16
$$

$$
x - y = 2
$$

**Resultado:** La recta $x - y = 2$ (o $y = x - 2$).

### ⚙️ Ejemplo 3: Parábola

**Problema:** Encuentra el lugar geométrico de los puntos equidistantes del punto $F(0, 2)$ y la recta $y = -2$.

**Paso 1:** Sea $P(x, y)$ un punto del lugar.

**Paso 2:** Condición: distancia a $F$ = distancia a la recta.

**Paso 3:** 
- Distancia a $F(0, 2)$: $\sqrt{x^2 + (y-2)^2}$
- Distancia a la recta $y = -2$: $|y - (-2)| = |y + 2|$

$$
\sqrt{x^2 + (y-2)^2} = |y + 2|
$$

**Paso 4:** Elevamos al cuadrado (asumiendo $y \geq -2$):
$$
x^2 + (y-2)^2 = (y+2)^2
$$

$$
x^2 + y^2 - 4y + 4 = y^2 + 4y + 4
$$

$$
x^2 = 8y
$$

**Resultado:** Parábola con ecuación $x^2 = 8y$ (o $y = \frac{x^2}{8}$).

### ⚙️ Ejemplo 4: Lugar geométrico con razón de distancias

**Problema:** Encuentra el lugar geométrico de los puntos $P(x, y)$ tales que la distancia a $A(3, 0)$ es el doble de la distancia a $B(-3, 0)$.

**Paso 1:** Sea $P(x, y)$ un punto del lugar.

**Paso 2:** Condición: $d(P, A) = 2 \cdot d(P, B)$

**Paso 3:**
$$
\sqrt{(x-3)^2 + y^2} = 2\sqrt{(x+3)^2 + y^2}
$$

**Paso 4:** Elevamos al cuadrado:
$$
(x-3)^2 + y^2 = 4[(x+3)^2 + y^2]
$$

$$
x^2 - 6x + 9 + y^2 = 4x^2 + 24x + 36 + 4y^2
$$

$$
0 = 3x^2 + 30x + 27 + 3y^2
$$

$$
x^2 + 10x + 9 + y^2 = 0
$$

Completando el cuadrado:
$$
(x + 5)^2 - 25 + 9 + y^2 = 0
$$

$$
(x + 5)^2 + y^2 = 16
$$

**Resultado:** Circunferencia con centro $(-5, 0)$ y radio $4$.

### ⚙️ Ejemplo 5: Lugar geométrico con pendiente constante

**Problema:** Encuentra el lugar geométrico de los puntos $P(x, y)$ tales que la pendiente de la recta que une $P$ con $(2, 3)$ es siempre igual a $-1$.

**Paso 1:** Sea $P(x, y)$ un punto del lugar.

**Paso 2:** Condición: pendiente de $\overline{P(2,3)}$ es $-1$.

**Paso 3:**
$$
\frac{y - 3}{x - 2} = -1
$$

**Paso 4:**
$$
y - 3 = -(x - 2)
$$

$$
y - 3 = -x + 2
$$

$$
y = -x + 5
$$

**Resultado:** La recta $y = -x + 5$ (excepto el punto $(2, 3)$ donde la pendiente no está definida).

---

## 📖 Estrategias Clave

| Condición geométrica | Fórmula a usar |
|---------------------|----------------|
| Distancia entre puntos | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Distancia a una recta | $d = \frac{|ax + by + c|}{\sqrt{a^2 + b^2}}$ |
| Pendiente constante | $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| Área constante | Usar fórmula del determinante |

---

## 🔑 Resumen

| Paso | Descripción |
|------|-------------|
| 1 | Definir $P(x, y)$ como punto genérico |
| 2 | Traducir la condición a ecuación |
| 3 | Aplicar fórmulas geométricas |
| 4 | Simplificar algebraicamente |
| 5 | Identificar la curva resultante |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la ecuación del lugar geométrico de los puntos que están a distancia 5 del origen.

<details>
<summary>Ver solución</summary>

$$
\sqrt{x^2 + y^2} = 5
$$

$$
x^2 + y^2 = 25
$$

**Respuesta:** Circunferencia centrada en el origen con radio 5.

</details>

### Ejercicio 2
Encuentra la ecuación de la mediatriz del segmento con extremos en $A(0, 0)$ y $B(8, 6)$.

<details>
<summary>Ver solución</summary>

Condición: $d(P, A) = d(P, B)$

$$
\sqrt{x^2 + y^2} = \sqrt{(x-8)^2 + (y-6)^2}
$$

Elevando al cuadrado:
$$
x^2 + y^2 = x^2 - 16x + 64 + y^2 - 12y + 36
$$

$$
0 = -16x - 12y + 100
$$

$$
4x + 3y = 25
$$

**Respuesta:** La recta $4x + 3y = 25$.

</details>

### Ejercicio 3
Encuentra el lugar geométrico de los puntos cuya distancia al punto $(4, 0)$ es igual a su distancia al eje Y.

<details>
<summary>Ver solución</summary>

Distancia a $(4, 0)$: $\sqrt{(x-4)^2 + y^2}$

Distancia al eje Y: $|x|$

Para $x \geq 0$:
$$
\sqrt{(x-4)^2 + y^2} = x
$$

Elevando al cuadrado:
$$
(x-4)^2 + y^2 = x^2
$$

$$
x^2 - 8x + 16 + y^2 = x^2
$$

$$
y^2 = 8x - 16
$$

$$
y^2 = 8(x - 2)
$$

**Respuesta:** Parábola con vértice en $(2, 0)$ que abre hacia la derecha.

</details>

### Ejercicio 4
Encuentra el lugar geométrico de los puntos tales que la suma de su distancia a $(3, 0)$ y a $(-3, 0)$ es igual a 10.

<details>
<summary>Ver solución</summary>

$$
\sqrt{(x-3)^2 + y^2} + \sqrt{(x+3)^2 + y^2} = 10
$$

Esta es la definición de una **elipse** con focos en $(\pm 3, 0)$ y $2a = 10$, por lo que $a = 5$.

Usando $c = 3$ y $a = 5$:
$$
b^2 = a^2 - c^2 = 25 - 9 = 16
$$

**Respuesta:** $\frac{x^2}{25} + \frac{y^2}{16} = 1$

</details>

### Ejercicio 5
Encuentra el lugar geométrico de los puntos cuya distancia al punto $A(1, 2)$ es el triple de su distancia al punto $B(4, 2)$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{(x-1)^2 + (y-2)^2} = 3\sqrt{(x-4)^2 + (y-2)^2}
$$

Elevando al cuadrado:
$$
(x-1)^2 + (y-2)^2 = 9[(x-4)^2 + (y-2)^2]
$$

$$
x^2 - 2x + 1 + (y-2)^2 = 9[x^2 - 8x + 16 + (y-2)^2]
$$

$$
x^2 - 2x + 1 + (y-2)^2 = 9x^2 - 72x + 144 + 9(y-2)^2
$$

$$
-8x^2 + 70x - 143 - 8(y-2)^2 = 0
$$

$$
8x^2 - 70x + 143 + 8(y-2)^2 = 0
$$

$$
x^2 - \frac{70}{8}x + \frac{143}{8} + (y-2)^2 = 0
$$

Completando el cuadrado para $x$:
$$
\left(x - \frac{35}{8}\right)^2 - \frac{1225}{64} + \frac{1144}{64} + (y-2)^2 = 0
$$

$$
\left(x - \frac{35}{8}\right)^2 + (y-2)^2 = \frac{81}{64}
$$

**Respuesta:** Circunferencia con centro $\left(\frac{35}{8}, 2\right)$ y radio $\frac{9}{8}$.

</details>

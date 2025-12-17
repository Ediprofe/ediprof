# Concepto de Lugar Geométrico

En geometría analítica, queremos describir figuras geométricas usando ecuaciones. Pero, ¿cómo pasamos de una descripción verbal ("todos los puntos a distancia 5 del origen") a una ecuación matemática? La respuesta está en el concepto de **lugar geométrico**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un lugar geométrico
- Cómo identificar lugares geométricos comunes
- La conexión entre geometría y álgebra

---

## 📖 Lo Esencial de Lugares Geométricos

| Descripción verbal | Lugar geométrico | Ecuación |
|-------------------|------------------|----------|
| Puntos a distancia $r$ del origen | Circunferencia | $x^2 + y^2 = r^2$ |
| Puntos equidistantes de dos puntos fijos | Mediatriz | Línea recta |
| Puntos a distancia fija de una recta | Rectas paralelas | — |
| Puntos a igual distancia de los ejes | Bisectrices | $y = x$ o $y = -x$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/lugar-circunferencia.svg" alt="Circunferencia como lugar geométrico" style="width: 100%; height: auto;" />
</div>

---

## 📖 Definición de Lugar Geométrico

> Un **lugar geométrico** es el conjunto de todos los puntos que satisfacen una condición geométrica específica.

En otras palabras:
- Se nos da una **condición** (por ejemplo, "estar a distancia 3 del punto A")
- El lugar geométrico es la **figura** formada por todos los puntos que cumplen esa condición
- Podemos expresar esa figura con una **ecuación**

### La Gran Idea

La geometría analítica conecta:

| Geometría | Álgebra |
|-----------|---------|
| Punto | Par ordenado $(x, y)$ |
| Curva o figura | Ecuación $f(x, y) = 0$ |
| Condición geométrica | Relación algebraica |

---

## 📖 Ejemplos de Lugares Geométricos

### ⚙️ Ejemplo 1: Circunferencia

**Condición:** "Todos los puntos que están a distancia 5 del origen"

**Análisis:** Si un punto $P(x, y)$ está a distancia 5 del origen $O(0, 0)$:

$$
\sqrt{x^2 + y^2} = 5
$$

Elevando al cuadrado:

$$
x^2 + y^2 = 25
$$

**Lugar geométrico:** Una **circunferencia** de radio 5 centrada en el origen.

### ⚙️ Ejemplo 2: Mediatriz

**Condición:** "Todos los puntos equidistantes de $A(0, 0)$ y $B(6, 0)$"

**Análisis:** Si $P(x, y)$ está a igual distancia de $A$ y $B$:

$$
\sqrt{x^2 + y^2} = \sqrt{(x-6)^2 + y^2}
$$

Elevando al cuadrado:

$$
x^2 + y^2 = (x-6)^2 + y^2
$$

$$
x^2 = x^2 - 12x + 36
$$

$$
0 = -12x + 36
$$

$$
x = 3
$$

**Lugar geométrico:** La **recta vertical** $x = 3$ (la mediatriz del segmento $\overline{AB}$).

### ⚙️ Ejemplo 3: Bisectriz

**Condición:** "Todos los puntos equidistantes del eje X y del eje Y"

**Análisis:** La distancia de $P(x, y)$ al eje X es $|y|$, y al eje Y es $|x|$.

$$
|y| = |x|
$$

Esto da dos soluciones:
- $y = x$
- $y = -x$

**Lugar geométrico:** Las dos **bisectrices** de los ejes coordenados.

### ⚙️ Ejemplo 4: Parábola

**Condición:** "Todos los puntos equidistantes del punto $F(0, 1)$ y la recta $y = -1$"

**Análisis:** 
- Distancia al punto $F(0, 1)$: $\sqrt{x^2 + (y-1)^2}$
- Distancia a la recta $y = -1$: $|y + 1|$

Igualando:

$$
\sqrt{x^2 + (y-1)^2} = |y + 1|
$$

Elevando al cuadrado (para $y \geq -1$):

$$
x^2 + (y-1)^2 = (y+1)^2
$$

$$
x^2 + y^2 - 2y + 1 = y^2 + 2y + 1
$$

$$
x^2 = 4y
$$

**Lugar geométrico:** Una **parábola** con vértice en el origen.

---

## 📖 El Proceso General

Para encontrar la ecuación de un lugar geométrico:

1. **Lee la condición** y tradúcela a lenguaje matemático
2. **Usa las fórmulas** de distancia, punto medio, etc.
3. **Simplifica** la ecuación resultante
4. **Identifica** la curva (recta, circunferencia, parábola, etc.)

### ⚙️ Ejemplo 5: Proceso completo

**Condición:** Encontrar el lugar geométrico de los puntos cuya distancia al punto $A(3, 0)$ es el doble de su distancia al origen.

**Paso 1:** Sea $P(x, y)$ un punto del lugar geométrico.

**Paso 2:** Escribimos la condición:
$$
\text{distancia de } P \text{ a } A = 2 \times \text{distancia de } P \text{ al origen}
$$

$$
\sqrt{(x-3)^2 + y^2} = 2\sqrt{x^2 + y^2}
$$

**Paso 3:** Elevamos al cuadrado:
$$
(x-3)^2 + y^2 = 4(x^2 + y^2)
$$

$$
x^2 - 6x + 9 + y^2 = 4x^2 + 4y^2
$$

$$
-3x^2 - 6x + 9 - 3y^2 = 0
$$

$$
x^2 + 2x - 3 + y^2 = 0
$$

**Paso 4:** Completamos el cuadrado:
$$
(x^2 + 2x + 1) + y^2 = 3 + 1
$$

$$
(x + 1)^2 + y^2 = 4
$$

**Lugar geométrico:** Una **circunferencia** de radio 2 centrada en $(-1, 0)$.

---

## 🔑 Resumen

| Elemento | Descripción |
|----------|-------------|
| Lugar geométrico | Conjunto de puntos que cumplen una condición |
| Ecuación | Expresión algebraica que describe el lugar |
| Proceso | Traducir condición → aplicar fórmulas → simplificar → identificar |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la ecuación del lugar geométrico de los puntos que están a distancia 4 del punto $(2, 3)$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{(x-2)^2 + (y-3)^2} = 4
$$

Elevando al cuadrado:

$$
(x-2)^2 + (y-3)^2 = 16
$$

**Respuesta:** Es una circunferencia de radio 4 centrada en $(2, 3)$.

</details>

### Ejercicio 2
Encuentra el lugar geométrico de los puntos equidistantes de $A(-2, 0)$ y $B(4, 0)$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{(x+2)^2 + y^2} = \sqrt{(x-4)^2 + y^2}
$$

Elevando al cuadrado:
$$
(x+2)^2 = (x-4)^2
$$

$$
x^2 + 4x + 4 = x^2 - 8x + 16
$$

$$
12x = 12
$$

$$
x = 1
$$

**Respuesta:** Es la recta vertical $x = 1$ (la mediatriz de $\overline{AB}$).

</details>

### Ejercicio 3
Encuentra el lugar geométrico de los puntos cuya suma de distancias al eje X y al eje Y es igual a 6.

<details>
<summary>Ver solución</summary>

$$
|x| + |y| = 6
$$

Esta ecuación define un **rombo** (o cuadrado rotado) con vértices en:
- $(6, 0)$
- $(-6, 0)$
- $(0, 6)$
- $(0, -6)$

En el primer cuadrante: $x + y = 6$

**Respuesta:** Es un rombo centrado en el origen con vértices a distancia 6 de él en cada eje.

</details>

### Ejercicio 4
Encuentra la ecuación del lugar geométrico de los puntos $(x, y)$ tales que su distancia al punto $(4, 0)$ es igual a su distancia a la recta $x = -4$.

<details>
<summary>Ver solución</summary>

Distancia al punto $(4, 0)$: $\sqrt{(x-4)^2 + y^2}$

Distancia a la recta $x = -4$: $|x + 4|$

$$
\sqrt{(x-4)^2 + y^2} = |x + 4|
$$

Para $x \geq -4$, elevamos al cuadrado:

$$
(x-4)^2 + y^2 = (x+4)^2
$$

$$
x^2 - 8x + 16 + y^2 = x^2 + 8x + 16
$$

$$
y^2 = 16x
$$

**Respuesta:** Es una parábola con ecuación $y^2 = 16x$.

</details>

### Ejercicio 5
Describe el lugar geométrico de los puntos que están a distancia 3 tanto del eje X como del eje Y.

<details>
<summary>Ver solución</summary>

La distancia al eje X es $|y| = 3$, entonces $y = 3$ o $y = -3$.

La distancia al eje Y es $|x| = 3$, entonces $x = 3$ o $x = -3$.

Para cumplir **ambas** condiciones simultáneamente, el lugar geométrico son los **cuatro puntos**:
- $(3, 3)$
- $(3, -3)$
- $(-3, 3)$
- $(-3, -3)$

**Respuesta:** Cuatro puntos que forman los vértices de un cuadrado.

</details>

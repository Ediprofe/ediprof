# **Propiedades Generales y Clasificación**

Hemos recorrido la familia de los cuadriláteros desde los más desordenados (trapezoides) hasta los más perfectos (cuadrados). En esta lección final, organizaremos todo en un mapa mental para que nunca confundas un rombo con un trapecio.

---

## 🎯 ¿Qué vas a aprender?

- Clasificar cualquier cuadrilátero según sus lados paralelos.
- Entender la jerarquía (quién es padre de quién).
- Comparar propiedades de diagonales en una sola tabla.
- Tener a mano todas las fórmulas de área y perímetro.
- Resolver problemas de identificación tipo "Adivina quién soy".

---

## 🌳 El Árbol Genealógico

Todo empieza con el **Cuadrilátero** (4 lados).
De ahí, se dividen según el paralelismo:

1.  **Ningún par paralelo:** Trapezoide.
2.  **Un solo par paralelo:** Trapecio.
3.  **Dos pares paralelos:** Paralelogramo.

![Jerarquía de Cuadriláteros](/illustrations/geometria/cuadrilateros/jerarquia-cuadrilateros.svg)

Dentro de los **Paralelogramos** hay una élite:
-   Si tiene **Ángulos Rectos** $\rightarrow$ Rectángulo.
-   Si tiene **Lados Iguales** $\rightarrow$ Rombo.
-   Si tiene **AMBOS** $\rightarrow$ Cuadrado.

> **Regla de Oro:** Un cuadrado es a la vez rectángulo, rombo, paralelogramo y cuadrilátero. ¡Lo tiene todo!

---

## 📊 Tabla Maestra de Propiedades

| Figura | Lados Paralelos | Lados Iguales | Ángulos Rectos | Diagonales |
| :--- | :---: | :---: | :---: | :--- |
| **Trapezoide** | 0 | 0* | 0* | Sin propiedad especial |
| **Trapecio** | 1 | 0* | 0* | Sin propiedad especial* |
| **Paralelogramo**| 2 | Opuestos | 0* | Se bisecan |
| **Rectángulo** | 2 | Opuestos | 4 | Se bisecan + Iguales |
| **Rombo** | 2 | 4 | 0* | Se bisecan + Perpendiculares |
| **Cuadrado** | 2 | 4 | 4 | Se bisecan + Iguales + Perp. |

*\*Nota: "0" significa "no necesariamente", salvo casos especiales.*

---

## 📏 Resumen de Fórmulas

| Figura | Área | Perímetro |
| :--- | :--- | :--- |
| **Cuadrado** | $A = l^2$ | $P = 4l$ |
| **Rectángulo** | $A = b \cdot h$ | $P = 2b + 2h$ |
| **Rombo** | $A = \frac{D \cdot d}{2}$ | $P = 4l$ |
| **Paralelogramo**| $A = b \cdot h$ | $P = 2a + 2b$ |
| **Trapecio** | $A = \frac{B+b}{2} \cdot h$ | Suma de lados |
| **Deltoide** | $A = \frac{D \cdot d}{2}$ | $2a + 2b$ |

![Mapa de Fórmulas de Área](/illustrations/geometria/cuadrilateros/mapa-areas.svg)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Identificación

"Tengo diagonales iguales que se cortan en el punto medio, pero mis lados consecutivos son diferentes". ¿Quién soy?

Analizaremos las propiedades de las diagonales para identificar la figura.

![Identificación de Rectángulo](/illustrations/geometria/cuadrilateros/identificacion-rectangulo.svg)

**Razonamiento:**

*   **Diagonales se bisecan:** Significa que se cortan en su punto medio, lo que garantiza que es un **paralelogramo**.
*   **Diagonales iguales:** En los paralelogramos, esto ocurre solo en el **rectángulo** y el **cuadrado**.
*   **Lados consecutivos diferentes:** Descarta al cuadrado (que tiene los 4 lados iguales).

**Resultado:**
$$
\boxed{\text{Rectángulo}}
$$

### Ejemplo 2: Cálculo Mixto

Un trapecio isósceles tiene bases de 10 y 20, y altura de 12. Calcula su perímetro.

Utilizaremos el Teorema de Pitágoras para hallar el lado lateral faltante.

![Perímetro de Trapecio Isósceles](/illustrations/geometria/cuadrilateros/perimetro-isosceles-calculo.svg)

**Razonamiento:**

1.  **Diferencia de bases:** $20 - 10 = 10$. Como es isósceles, esa diferencia se reparte en dos segmentos de 5 a cada lado.
2.  **Triángulo rectángulo:** Se forma un triángulo de catetos 5 (base) y 12 (altura).
3.  **Hipotenusa ($L$):** Calculamos el lado lateral usando Pitágoras:

$$
L = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13
$$

4.  **Perímetro:** Sumamos los cuatro lados ($B + b + 2L$):

$$
P = 10 + 20 + 13 + 13
$$

**Resultado:**
$$
\boxed{56}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Soy un cuadrilátero con diagonales perpendiculares pero NO soy un rombo. ¿Quién soy?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Las diagonales perpendiculares aparecen en: Rombo, Cuadrado y Deltoide.
Si no es rombo (ni cuadrado), queda la opción del deltoide (cometa).

**Resultado:**
$$
\boxed{\text{Deltoide}}
$$

</details>

### Ejercicio 2
Verdadero o Falso: Las diagonales de un trapecio isósceles se bisecan.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Son iguales, pero NO se cortan en el punto medio (una parte es más larga que la otra). Solo los paralelogramos se bisecan.

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 3
Calcula el área de un cuadrilátero si sus diagonales miden 10 m y 12 m y son perpendiculares.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cualquier cuadrilátero con diagonales perpendiculares (ortodiagonal) tiene área $D \cdot d / 2$.

$$
A = \frac{10 \cdot 12}{2} = 60
$$

**Resultado:**
$$
\boxed{60 \text{ m}^2}
$$

</details>

### Ejercicio 4
Si $AB \parallel CD$ y $AB = CD$, ¿qué figura es $ABCD$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Un par de lados opuestos que son paralelos E iguales garantizan un paralelogramo.

**Resultado:**
$$
\boxed{\text{Paralelogramo}}
$$

</details>

### Ejercicio 5
Un cuadrilátero tiene 4 lados iguales. ¿Es necesariamente un cuadrado?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. Podría ser un rombo (que está "achatado" y no tiene ángulos de 90°).

**Resultado:**
$$
\boxed{\text{No, podría ser un rombo}}
$$

</details>

### Ejercicio 6
¿Cuál es la suma de los ángulos exteriores de un trapezoide?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La suma de exteriores de cualquier polígono convexo es $360^\circ$.

**Resultado:**
$$
\boxed{360^\circ}
$$

</details>

### Ejercicio 7
Clasifica: Lados paralelos 2 a 2. Diagonales de diferente longitud.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Lados paralelos 2 a 2 = Paralelogramo.
Diagonales distintas = No es rectángulo ni cuadrado.
Puede ser un Rombo o un Romboide.

**Resultado:**
$$
\boxed{\text{Rombo o Romboide}}
$$

</details>

### Ejercicio 8
Calcula el área de un cuadrado cuyo perímetro es 20 m.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Lado = $20/4 = 5$.
Área = $5^2$.

**Resultado:**
$$
\boxed{25 \text{ m}^2}
$$

</details>

### Ejercicio 9
Si duplicamos la base y la altura de un rectángulo, ¿qué pasa con su área?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A_1 = b \cdot h$.
$A_2 = (2b) \cdot (2h) = 4(b \cdot h)$.
Se cuadruplica.

**Resultado:**
$$
\boxed{\text{Se multiplica por 4}}
$$

</details>

### Ejercicio 10
Nombra el cuadrilátero más específico posible si: Diagonales iguales y perpendiculares.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Iguales $\rightarrow$ Rectángulo o Cuadrado o Trapecio Isósceles.
Perpendiculares $\rightarrow$ Rombo, Cuadrado o Deltoide.
La intersección es el Cuadrado.

**Resultado:**
$$
\boxed{\text{Cuadrado}}
$$

</details>

---

## 🔑 Resumen

| Propiedad | ¿Quién la tiene? |
| :--- | :--- |
| **Simetría Total** | Cuadrado |
| **Ángulos Rectos** | Rectángulo, Cuadrado |
| **Lados Iguales** | Rombo, Cuadrado |
| **Diagonales $\perp$** | Rombo, Cuadrado, Deltoide |
| **Diagonales $=$** | Rectángulo, Cuadrado, Trap. Isósceles |

> Conocer estas propiedades es como tener la "llave maestra" de la geometría plana.

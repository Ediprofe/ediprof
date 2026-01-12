# Puntos Notables del Triángulo

Las rectas notables (medianas, alturas, bisectrices, mediatrices) se cortan en 4 puntos clave.

## ⚡ Conceptos Clave

| Punto | Rectas | Característica |
|---|---|---|
| **Baricentro (G)** | Medianas | Centro de Gravedad (2:1) |
| **Ortocentro (H)** | Alturas | Puede caer FUERA del triángulo |
| **Incentro (I)** | Bisectrices | Centro del círculo INSCRITO |
| **Circuncentro (O)** | Mediatrices | Centro del círculo CIRCUNSCRITO |

---

## 1. El Baricentro (G)

Es la intersección de las **Medianas**.

> **📝 ¿Qué es una Mediana?**
> Es la línea que une un **vértice** con el **punto medio** del lado opuesto.

El baricentro es el **centro de gravedad**. Si sostienes el triángulo por este punto, se mantiene en equilibrio.

### Propiedad Clave: Regla 2 a 1
Divide la mediana en dos partes proporcionales:
*   La parte larga (vértice a $G$) mide el **doble** que la corta.

> **⚙️ Ejemplo:**
> Si la mediana mide 9 cm:
> *   Lado largo ($AG$): 6 cm
> *   Lado corto ($GM$): 3 cm

![barycenter](/images/geometria/triangulos/barycenter.svg)

### Coordenadas del baricentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
$$

---

## 2. El Ortocentro (H)

Es la intersección de las **Alturas**.

> **📝 ¿Qué es una Altura?**
> Es la línea que baja desde un **vértice** perpendicularmente ($90^\circ$) al lado opuesto (o su prolongación).

Su ubicación depende totalmente del tipo de triángulo:

> **⚙️ Ejemplo de Identificación:**
> En un triángulo rectángulo ($90^\circ$), el Ortocentro es **el mismo vértice del ángulo recto**.

### 1. Acutángulo (Dentro)
Cae **dentro** del triángulo.

![orthocenter-acute](/images/geometria/triangulos/orthocenter-acute.svg)


### 2. Rectángulo (En el Vértice)
Coincide con el **vértice del ángulo recto**.

![orthocenter-right](/images/geometria/triangulos/orthocenter-right.svg)

### 3. Obtusángulo (Fuera)
Cae **fuera** del triángulo (en la prolongación de los lados).

![orthocenter-obtuse](/images/geometria/triangulos/orthocenter-obtuse.svg)

---

## 3. El Incentro (I)

Es la intersección de las **Bisectrices**.

> **📝 ¿Qué es una Bisectriz?**
> Es la semirrecta que divide un **ángulo** en dos partes iguales.

### Propiedad Clave
Está a la **misma distancia de los tres lados**.
Esto permite dibujar una circunferencia que toca los 3 lados por dentro (**Inscrita**).

> **⚙️ Ejemplo:**
> Si el incentro está a 5 cm del lado base, también está a 5 cm de los otros dos lados.

![incenter](/images/geometria/triangulos/incenter.svg)

---

## 4. El Circuncentro (O)

Es la intersección de las **Mediatrices**.

> **📝 ¿Qué es una Mediatriz?**
> Es la recta perpendicular ($90^\circ$) que pasa por el **punto medio** de un lado.
> *(Ojo: No necesariamente sale de un vértice).*

### Propiedad Clave
Está a la **misma distancia de los tres vértices**.
Esto permite dibujar una circunferencia que pasa por las 3 esquinas (**Circunscrita**).

> **⚙️ Ejemplo:**
> En un triángulo rectángulo, el circuncentro siempre es el **punto medio de la hipotenusa**.

![circumcenter](/images/geometria/triangulos/circumcenter.svg)

---

## 📖 Resumen de ubicaciones

| Tipo de triángulo | Baricentro | Ortocentro | Incentro | Circuncentro |
|-------------------|------------|------------|----------|--------------|
| Acutángulo | Dentro | Dentro | Dentro | Dentro |
| Rectángulo | Dentro | En vértice recto | Dentro | Medio de hipotenusa |
| Obtusángulo | Dentro | Fuera | Dentro | Fuera |

---

## 5. La Recta de Euler

En la mayoría de triángulos, tres puntos están **alineados en una recta**:
1.  **O**rtocentro
2.  **B**aricentro
3.  **C**ircuncentro

> **Nota:** El Incentro NO suele estar en esta recta.

![euler-line](/images/geometria/triangulos/euler-line.svg)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar puntos

Indica qué punto notable corresponde a cada descripción:

1. Centro de la circunferencia que pasa por los tres vértices
2. Punto donde se equilibra el triángulo en cartón
3. Punto equidistante a los tres lados
4. Intersección de las alturas

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Circuncentro**
2. **Baricentro**
3. **Incentro**
4. **Ortocentro**

</details>

---

### Ejercicio 2: Ubicación del ortocentro

¿Dónde está el ortocentro en cada caso?

1. Triángulo con ángulos 60°, 70°, 50°
2. Triángulo con ángulos 90°, 45°, 45°
3. Triángulo con ángulos 120°, 30°, 30°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Dentro** (es acutángulo, todos los ángulos < 90°)
2. **En el vértice del ángulo recto** (es rectángulo)
3. **Fuera** (es obtusángulo, tiene un ángulo > 90°)

</details>

---

### Ejercicio 3: Razón del baricentro

Si la mediana desde el vértice $A$ hasta el punto medio $M$ del lado opuesto mide 12 cm, calcula:

1. La distancia del vértice $A$ al baricentro $G$
2. La distancia del baricentro $G$ al punto medio $M$

<details>
<summary><strong>Ver respuestas</strong></summary>

El baricentro divide la mediana en razón 2:1.

1. $AG = \frac{2}{3} \times 12 = 8$ cm
2. $GM = \frac{1}{3} \times 12 = 4$ cm

</details>

---

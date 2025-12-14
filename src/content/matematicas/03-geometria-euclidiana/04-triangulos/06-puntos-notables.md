# Puntos Notables del Triángulo

Las rectas notables de un triángulo (medianas, alturas, bisectrices y mediatrices) se cortan en puntos especiales llamados **puntos notables**. Cada punto tiene propiedades geométricas únicas.

---

## 📖 Los cuatro puntos notables

| Punto | Intersección de | Característica principal |
|-------|-----------------|-------------------------|
| Baricentro (G) | Medianas | Centro de gravedad |
| Ortocentro (H) | Alturas | Depende del tipo de triángulo |
| Incentro (I) | Bisectrices | Centro de circunferencia inscrita |
| Circuncentro (O) | Mediatrices | Centro de circunferencia circunscrita |

---

## 📖 El Baricentro (G)

El **baricentro** es el punto donde se cortan las tres medianas del triángulo.

### Propiedades

1. **Siempre está dentro** del triángulo (sin importar el tipo)
2. Es el **centro de gravedad** o centro de masa del triángulo
3. Divide cada mediana en razón **2:1** desde el vértice

### La razón 2:1

Si $G$ es el baricentro y $M$ es el punto medio del lado opuesto al vértice $A$:

$$
\frac{AG}{GM} = \frac{2}{1}
$$

Esto significa que la distancia del vértice al baricentro es el **doble** de la distancia del baricentro al punto medio del lado.

### Ejemplo

Si la mediana $\overline{AM}$ mide 9 cm:
- $AG = \frac{2}{3} \times 9 = 6$ cm (del vértice al baricentro)
- $GM = \frac{1}{3} \times 9 = 3$ cm (del baricentro al punto medio)

### Coordenadas del baricentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
$$

---

## 📖 El Ortocentro (H)

El **ortocentro** es el punto donde se cortan las tres alturas del triángulo.

### Propiedades

1. Su posición depende del **tipo de triángulo** (por ángulos)
2. En triángulos **acutángulos**: el ortocentro está **dentro**
3. En triángulos **obtusángulos**: el ortocentro está **fuera**
4. En triángulos **rectángulos**: el ortocentro coincide con el **vértice del ángulo recto**

### Ejemplo

En un triángulo rectángulo con el ángulo recto en $C$, el ortocentro es exactamente el punto $C$.

---

## 📖 El Incentro (I)

El **incentro** es el punto donde se cortan las tres bisectrices interiores del triángulo.

### Propiedades

1. **Siempre está dentro** del triángulo
2. Es **equidistante a los tres lados**
3. Es el centro de la **circunferencia inscrita** (la más grande que cabe dentro)

### El radio del incírculo

El radio de la circunferencia inscrita se llama **inradio** ($r$) y se calcula:

$$
r = \frac{\text{Área del triángulo}}{\text{Semiperímetro}}
$$

Donde el semiperímetro es $s = \frac{a + b + c}{2}$.

### Ejemplo

Si un triángulo tiene área $= 30$ cm² y semiperímetro $= 10$ cm:

$$
r = \frac{30}{10} = 3 \text{ cm}
$$

---

## 📖 El Circuncentro (O)

El **circuncentro** es el punto donde se cortan las tres mediatrices del triángulo.

### Propiedades

1. Es **equidistante a los tres vértices**
2. Es el centro de la **circunferencia circunscrita** (la que pasa por los tres vértices)
3. Su posición depende del tipo de triángulo:
   - **Acutángulo**: dentro del triángulo
   - **Rectángulo**: en el punto medio de la hipotenusa
   - **Obtusángulo**: fuera del triángulo

### El radio del circuncírculo

El radio de la circunferencia circunscrita se llama **circunradio** ($R$).

### Ejemplo especial

En un triángulo rectángulo, el circuncentro está en el **punto medio de la hipotenusa**, y el circunradio es la **mitad de la hipotenusa**.

---

## 📖 Resumen de ubicaciones

| Tipo de triángulo | Baricentro | Ortocentro | Incentro | Circuncentro |
|-------------------|------------|------------|----------|--------------|
| Acutángulo | Dentro | Dentro | Dentro | Dentro |
| Rectángulo | Dentro | En vértice recto | Dentro | Medio de hipotenusa |
| Obtusángulo | Dentro | Fuera | Dentro | Fuera |

---

## 📖 La recta de Euler

En todo triángulo, tres de los puntos notables están **alineados**: el **Baricentro (G)**, el **Ortocentro (H)** y el **Circuncentro (O)**.

Esta recta se llama **recta de Euler**.

### Propiedad adicional

El baricentro $G$ divide el segmento $\overline{OH}$ en razón $1:2$:

$$
OG = \frac{1}{3} OH, \quad GH = \frac{2}{3} OH
$$

> **Nota:** El incentro generalmente NO está en la recta de Euler.

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

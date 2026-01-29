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

![barycenter](/images/geometria/triangulos/barycenter.svg)

El baricentro es el **centro de gravedad**. Si sostienes el triángulo por este punto, se mantiene en equilibrio.

### Propiedad Clave: Regla 2 a 1
Divide la mediana en dos partes proporcionales:
*   La parte larga (vértice a $G$) mide el **doble** que la corta.

> **⚙️ Ejemplo:**
> Si la mediana mide 9 cm:
> *   Lado largo ($AG$): 6 cm
> *   Lado corto ($GM$): 3 cm

![barycenter-ratio](/images/geometria/triangulos/barycenter-ratio.svg)

Esta propiedad se cumple para **las tres medianas** al mismo tiempo:

![barycenter-ratio-all](/images/geometria/triangulos/barycenter-ratio-all.svg)

> **💡 Propiedad Mágica de las Áreas:**
> Las tres medianas dividen al triángulo en **6 triángulos pequeños** que tienen exactamente la **misma área**. Por eso el peso se distribuye perfectamente.
> *Nota que esto ocurre sin importar la forma del triángulo (ver abajo un triángulo asimétrico).*

![barycenter-areas](/images/geometria/triangulos/barycenter-areas.svg)

### Coordenadas del baricentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
$$

![barycenter-coordinates](/images/geometria/triangulos/barycenter-coordinates.svg)

> **💡 Centro de Masa:** El baricentro es el **centro de gravedad** (o centroide) del triángulo. Si recortaras un triángulo en cartón, este sería el punto exacto donde podrías sostenerlo en perfecto equilibrio sobre la punta de un lápiz.

![centro-de-masa-baricentro](https://cdn.ediprofe.com/img/matematicas/13wk-centro-de-masa-baricentro.webp)

---

## 2. El Ortocentro (H)

Es la intersección de las **Alturas**.

> **📝 ¿Qué es una Altura?**
> Es la línea que baja desde un **vértice** perpendicularmente ($90^\circ$) al lado opuesto (o su prolongación).

Su ubicación depende totalmente del tipo de triángulo:

### 1. Acutángulo (Dentro)
Cae **dentro** del triángulo.

![orthocenter-acute](/images/geometria/triangulos/orthocenter-acute.svg)

### 2. Rectángulo (En el Vértice)

Es **el mismo vértice del ángulo recto**.

![orthocenter-right](/images/geometria/triangulos/orthocenter-right.svg)

### 3. Obtusángulo (Fuera)
Cae **fuera** del triángulo (en la prolongación de los lados).

![orthocenter-obtuse](/images/geometria/triangulos/orthocenter-obtuse.svg)

---

## 3. El Incentro (I)

Es la intersección de las **Bisectrices**.

> **📝 ¿Qué es una Bisectriz?**
> Es la semirrecta que divide un **ángulo** en dos partes iguales.

![incenter](/images/geometria/triangulos/incenter.svg)

### Propiedad Clave
Está a la **misma distancia de los tres lados**.
Esto permite dibujar una circunferencia que toca los 3 lados por dentro (**Inscrita**).

> **💡 Piénsalo así:** El incentro es el lugar donde debes poner la punta del compás para dibujar el círculo más grande posible que quepa **dentro** del triángulo sin salirse.

**⚙️ Ejemplo:**
Si el incentro está a 5 cm del lado base, también está a 5 cm de los otros dos lados.

![incenter-equidistant](/images/geometria/triangulos/incenter-equidistant.svg)


---

## 4. El Circuncentro (O)

Es la intersección de las **Mediatrices**.

> **📝 ¿Qué es una Mediatriz?**
> Es la recta perpendicular ($90^\circ$) que pasa por el **punto medio** de un lado.
> *(Ojo: No necesariamente sale de un vértice).*

![circumcenter](/images/geometria/triangulos/circumcenter.svg)


### Propiedad Clave
Está a la **misma distancia de los tres vértices**.
Esto permite dibujar una circunferencia que pasa por las 3 esquinas (**Circunscrita**).

> **💡 Piénsalo así:** El circuncentro es el único lugar donde puedes poner la punta del compás para dibujar un círculo que toque las tres esquinas del triángulo a la vez.

![circuncentro-interseccion-de-mediatrices](https://cdn.ediprofe.com/img/matematicas/4flj-circuncentro-interseccion-de-mediatrices.webp)

> **⚙️ Ejemplo:**
> En un triángulo rectángulo, el circuncentro siempre es el **punto medio de la hipotenusa**.

![circumcenter-right](/images/geometria/triangulos/circumcenter-right.svg)


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

### Ejercicio 4: Coordenadas del baricentro

Calcula las coordenadas del baricentro $G$ de un triángulo cuyos vértices son $A(2, 4)$, $B(6, 10)$ y $C(10, -2)$.

<details>
<summary><strong>Ver solución</strong></summary>

Usamos la fórmula del promedio:

$$
x_G = \frac{2 + 6 + 10}{3} = \frac{18}{3} = 6
$$

$$
y_G = \frac{4 + 10 + (-2)}{3} = \frac{12}{3} = 4
$$

El baricentro es **$G(6, 4)$**.

</details>

---

### Ejercicio 5: Distancias al Incentro

En un triángulo, el incentro está a una distancia de 4 cm del lado $AB$. ¿A qué distancia está el incentro del lado $BC$?

<details>
<summary><strong>Ver solución</strong></summary>

**4 cm**.

El incentro equidista de los tres lados. Si la distancia a uno es 4 cm, la distancia a los otros dos también debe ser 4 cm (es el radio de la circunferencia inscrita).

</details>

---

### Ejercicio 6: Circuncentro en triángulo rectángulo

Se tiene un triángulo rectángulo cuya hipotenusa mide 20 cm. ¿A qué distancia del vértice del ángulo recto se encuentra el circuncentro?

<details>
<summary><strong>Ver solución</strong></summary>

En un triángulo rectángulo, el circuncentro es el **punto medio de la hipotenusa**.

1.  Si la hipotenusa mide 20 cm, el punto medio está a 10 cm de cada extremo.
2.  El circuncentro equidista de los tres vértices.
3.  Por tanto, la distancia al vértice recto también es **10 cm** (el circunradio mide la mitad de la hipotenusa).

</details>

---

### Ejercicio 7: Verdadero o Falso

Indica si las siguientes afirmaciones son verdaderas (V) o falsas (F):

1.  El incentro siempre está dentro del triángulo.
2.  El ortocentro siempre está dentro del triángulo.
3.  El baricentro divide a la mediana en partes iguales.
4.  El circuncentro puede estar fuera del triángulo.

<details>
<summary><strong>Ver respuestas</strong></summary>

1.  **V** (Siempre dentro)
2.  **F** (Puede estar fuera en obtusángulos o en el vértice en rectángulos)
3.  **F** (La divide en razón 2:1, no iguales)
4.  **V** (En triángulos obtusángulos está fuera)

</details>

---

### Ejercicio 8: Recta de Euler

En un triángulo escaleno, ¿cuáles de los siguientes puntos están alineados en la Recta de Euler? (Elige 3)

*   Incentro
*   Baricentro
*   Ortocentro
*   Circuncentro

<details>
<summary><strong>Ver solución</strong></summary>

Los puntos alineados son:
1.  **Ortocentro**
2.  **Baricentro**
3.  **Circuncentro**

*(El Incentro generalmente no está en esta línea).*

</details>

---

### Ejercicio 9: Ángulos y bisectrices

En el triángulo $ABC$, el ángulo $A$ mide $60^\circ$. Si trazamos la bisectriz desde $A$, ¿cuánto miden los dos ángulos que se forman en ese vértice?

<details>
<summary><strong>Ver solución</strong></summary>

La bisectriz divide el ángulo en dos partes iguales.

$$
\frac{60^\circ}{2} = 30^\circ
$$

Se forman dos ángulos de **$30^\circ$** cada uno.

</details>

---

### Ejercicio 10: Mediana y área

Si una mediana divide a un triángulo en dos triángulos más pequeños, ¿qué relación hay entre las áreas de esos dos triángulos pequeños?

<details>
<summary><strong>Ver solución</strong></summary>

**Tienen la misma área.**

Una mediana divide al triángulo en dos regiones de igual área (equiparables), porque ambos triángulos resultantes tienen:
1.  La misma base (la mitad del lado original).
2.  La misma altura (la altura del triángulo original hacia ese lado).

</details>

---

## 🔑 Resumen

![summary-notable-points](/images/geometria/triangulos/summary-notable-points.svg)
| Punto | Propiedad Mágica | Construcción | Definición Línea |
|:---:|---|:---:|---|
| **Baricentro (G)** | Centro de equilibrio (razón 2:1) | **M**edianas | Une cada vértice con el punto medio del lado opuesto |
| **Ortocentro (H)** | Puede estar fuera del triángulo | **A**lturas | Segmento perpendicular trazado desde el vértice al lado opuesto |
| **Incentro (I)** | Centro de la circunferencia **inscrita** | **Bi**sectrices | Línea que divide un ángulo interior en dos partes iguales |
| **Circuncentro (O)** | Centro de la circunferencia **circunscrita** | **Me**diatrices | Recta perpendicular que pasa por el punto medio de un lado |

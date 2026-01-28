---
title: "Polígonos Regulares"
---

# **Polígonos Regulares**

Cuando la naturaleza quiere eficiencia, crea polígonos regulares. Piénsalo: las abejas usan hexágonos, los copos de nieve tienen estructura hexagonal, y las flores suelen tener simetría pentagonal. Son las figuras geométricamente "perfectas".

---

## 🎯 ¿Qué vas a aprender?

- Identificar los elementos exclusivos de un polígono regular (centro, radio, apotema).
- Calcular el perímetro de forma rápida ($n \times l$).
- Calcular el área usando el perímetro y la apotema.
- Comprender la diferencia entre el radio (al vértice) y la apotema (al centro del lado).

---

## 👑 Anatomía de la Perfección

Un polígono regular es **equilátero** (lados iguales) y **equiángulo** (ángulos iguales). Esta simetría crea nuevos elementos que no existen en los polígonos irregulares.

### 1. Centro ($C$)
Es el punto que está a la misma distancia de todos los vértices. Es el "corazón" de la figura.

### 2. Radio ($R$)
Es la distancia del Centro a cualquiera de los **Vértices**.
*(Es el radio de la circunferencia imaginaria que rodea al polígono).*

### 3. Apotema ($a$)
Es la distancia del Centro al **punto medio de un lado**.
-   Funciona como la **altura** de los triángulos internos.
-   Siempre es perpendicular al lado ($90^\circ$).
-   *(Es el radio de la circunferencia que cabe dentro del polígono).*

> **Ojo:** No confundas Radio con Apotema. El Radio va a la esquina (es más largo), la Apotema va al lado (es más corta).

---

## 📏 Cálculos Básicos

### Perímetro ($P$)
Como todos los lados medin lo mismo ($l$) y hay $n$ lados:

$$
P = n \cdot l
$$

### Ángulo Central
Si te paras en el centro y das una vuelta completa ($360^\circ$) mirando a cada vértice:

$$
\text{Ángulo Central} = \frac{360^\circ}{n}
$$

---

## 🟥 El Área del Polígono Regular

Imagina que cortas el polígono como una pizza. Si unes el centro con cada vértice, obtienes **$n$ triángulos iguales**.

1.  El área de un triángulo es $\frac{\text{base} \cdot \text{altura}}{2}$.
2.  Aquí, la base es el lado ($l$) y la altura es la apotema ($a$).
3.  Área de un triángulo = $\frac{l \cdot a}{2}$.
4.  Como hay $n$ triángulos: $A = n \cdot \frac{l \cdot a}{2}$.
5.  Pero como $n \cdot l$ es el Perímetro ($P$):

$$
A = \frac{P \cdot a}{2}
$$

> **Fórmula Maestra:** El área es el semiperímetro por la apotema.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Área de un Pentágono

Un pentágono regular tiene 6 cm de lado y su apotema mide 4 cm. Calcula su área.

**Datos:**
-   $n = 5$
-   $l = 6$
-   $a = 4$

**Razonamiento:**
Primero hallamos el perímetro.
$$P = 5 \times 6 = 30 \text{ cm}$$

Ahora el área:
$$
A = \frac{30 \cdot 4}{2}
$$

$$
A = \frac{120}{2}
$$

**Resultado:**
$$
\boxed{60 \text{ cm}^2}
$$

### Ejemplo 2: Hallar la Apotema

Un octágono tiene un perímetro de 80 m y un área de 400 m². ¿Cuánto mide su apotema?

**Razonamiento:**
Usamos la fórmula y despejamos $a$.

$$
400 = \frac{80 \cdot a}{2}
$$

$$
400 = 40 \cdot a
$$

$$
a = \frac{400}{40}
$$

**Resultado:**
$$
\boxed{10 \text{ m}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el perímetro de un hexágono regular de lado 10.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
P = 6 \times 10
$$

**Resultado:**
$$
\boxed{60}
$$

</details>

### Ejercicio 2
Calcula el ángulo central de un decágono regular ($n=10$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\frac{360}{10}
$$

**Resultado:**
$$
\boxed{36^\circ}
$$

</details>

### Ejercicio 3
Calcula el área de un heptágono regular con perímetro 70 y apotema 10.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
A = \frac{70 \cdot 10}{2} = \frac{700}{2}
$$

**Resultado:**
$$
\boxed{350}
$$

</details>

### Ejercicio 4
Si el radio de un hexágono regular es igual a su lado (propiedad especial del hexágono), y el lado mide 8, ¿cuánto mide el radio?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En el hexágono, los triángulos internos son equiláteros. Radio = Lado.

**Resultado:**
$$
\boxed{8}
$$

</details>

### Ejercicio 5
Un cuadrado tiene lado 10. ¿Cuánto mide su apotema?
*(Pista: La apotema va del centro a la mitad del lado).*

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En un cuadrado, la apotema es exactamente la mitad del lado.
$10 / 2 = 5$.

**Resultado:**
$$
\boxed{5}
$$

</details>

### Ejercicio 6
Calcula el área de un dodecágono regular ($n=12$) de lado 2 y apotema 3.7.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Perímetro $P = 12 \times 2 = 24$.
$$
A = \frac{24 \cdot 3.7}{2} = 12 \cdot 3.7
$$

**Resultado:**
$$
\boxed{44.4}
$$

</details>

### Ejercicio 7
Verdadero o Falso: La apotema siempre es menor que el radio.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí. En el triángulo rectángulo formado (Centro-MitadLado-Vértice), el Radio es la hipotenusa y la Apotema es un cateto.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 8
Si el área de un polígono regular es 100 y su perímetro es 50, ¿cuál es su apotema?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
100 = \frac{50 \cdot a}{2} \Rightarrow 100 = 25a \Rightarrow a=4
$$

**Resultado:**
$$
\boxed{4}
$$

</details>

### Ejercicio 9
Calcula el lado de un eneágono regular ($n=9$) si su perímetro es 81.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
l = \frac{81}{9}
$$

**Resultado:**
$$
\boxed{9}
$$

</details>

### Ejercicio 10
Un triángulo equilátero tiene lado 6 y altura total 5.2. ¿Cuánto mide su apotema?
*(Nota avanzada: El centroide divide la altura en razón 2:1).*

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La apotema es $\frac{1}{3}$ de la altura en un triángulo equilátero.
$a = \frac{5.2}{3} \approx 1.73$.
O usando fórmula de área:
$A_{\text{triángulo}} = \frac{6 \cdot 5.2}{2} = 15.6$.
$P = 18$.
$15.6 = \frac{18 \cdot a}{2} \Rightarrow 15.6 = 9a \Rightarrow a = 1.73$.

**Resultado:**
$$
\boxed{1.73}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula / Definición |
| :--- | :--- |
| **Apotema ($a$)** | Distancia Centro $\rightarrow$ Lado ($90^\circ$). |
| **Radio ($R$)** | Distancia Centro $\rightarrow$ Vértice. |
| **Perímetro** | $n \cdot l$ |
| **Área** | $\frac{P \cdot a}{2}$ |

> El área de un polígono regular es, en el fondo, la suma de muchos triángulos idénticos.

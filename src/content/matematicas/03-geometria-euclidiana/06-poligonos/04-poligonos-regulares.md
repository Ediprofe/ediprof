# Polígonos Regulares

Los **polígonos regulares** tienen propiedades especiales que los hacen muy útiles en geometría, arquitectura y diseño. En esta lección profundizamos en sus características.

---

## 📖 Definición

> **Definición:** Un polígono regular es aquel que tiene **todos sus lados iguales** (equilátero) y **todos sus ángulos iguales** (equiángulo).

### Ejemplos

- Triángulo equilátero (3 lados)
- Cuadrado (4 lados)
- Pentágono regular (5 lados)
- Hexágono regular (6 lados)

---

## 📖 Elementos de un polígono regular

### Centro

El **centro** del polígono regular es el punto equidistante de todos los vértices y de todos los lados.

### Radio

El **radio** ($R$) es la distancia desde el centro hasta cualquier vértice. Es el radio de la circunferencia **circunscrita**.

### Apotema

El **apotema** ($a$) es la distancia desde el centro hasta el punto medio de cualquier lado. Es el radio de la circunferencia **inscrita**.

### Ángulo central

El **ángulo central** es el ángulo formado por dos radios consecutivos:

$$
\theta = \frac{360°}{n}
$$

---

## 📖 Tabla de elementos

| Polígono regular | n | Ángulo central | Ángulo interior |
|------------------|---|----------------|-----------------|
| Triángulo | 3 | 120° | 60° |
| Cuadrado | 4 | 90° | 90° |
| Pentágono | 5 | 72° | 108° |
| Hexágono | 6 | 60° | 120° |
| Octágono | 8 | 45° | 135° |
| Decágono | 10 | 36° | 144° |
| Dodecágono | 12 | 30° | 150° |

---

## 📖 Relación entre radio y apotema

Para un polígono regular de $n$ lados:

$$
a = R \cos\left(\frac{180°}{n}\right)
$$

### Relación con el lado

Si $l$ es la longitud del lado:

$$
l = 2R \sin\left(\frac{180°}{n}\right)
$$

---

## 📖 Perímetro

El perímetro de un polígono regular es:

$$
P = n \times l
$$

Donde $l$ es la longitud de cada lado.

---

## 📖 Área de un polígono regular

La fórmula general del área es:

$$
A = \frac{P \times a}{2} = \frac{n \times l \times a}{2}
$$

Donde:
- $P$ = perímetro
- $a$ = apotema
- $n$ = número de lados
- $l$ = longitud de cada lado

### Interpretación

El área es igual a la suma de las áreas de $n$ triángulos, cada uno con:
- Base = lado del polígono
- Altura = apotema

---

## 📖 Casos especiales

### Triángulo equilátero

Para un triángulo de lado $l$:

$$
A = \frac{l^2 \sqrt{3}}{4}
$$

### Cuadrado

Para un cuadrado de lado $l$:

$$
A = l^2
$$

### Hexágono regular

Para un hexágono de lado $l$:

$$
A = \frac{3l^2\sqrt{3}}{2}
$$

---

## 📖 Circunferencias asociadas

### Circunferencia circunscrita

Pasa por **todos los vértices**. Su radio es $R$.

### Circunferencia inscrita

Es **tangente a todos los lados**. Su radio es $a$ (apotema).

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Ángulo central

Calcula el ángulo central de:

1. Pentágono regular
2. Octágono regular
3. Decágono regular

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\theta = \frac{360°}{5} = 72°$
2. $\theta = \frac{360°}{8} = 45°$
3. $\theta = \frac{360°}{10} = 36°$

</details>

---

### Ejercicio 2: Perímetro

Calcula el perímetro de:

1. Hexágono regular de lado 5 cm
2. Octágono regular de lado 4 cm
3. Decágono regular de lado 3 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P = 6 \times 5 = 30$ cm
2. $P = 8 \times 4 = 32$ cm
3. $P = 10 \times 3 = 30$ cm

</details>

---

### Ejercicio 3: Área

Calcula el área de polígonos regulares con:

1. Perímetro = 24 cm, apotema = 4 cm
2. Perímetro = 36 cm, apotema = 6 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{24 \times 4}{2} = 48$ cm²
2. $A = \frac{36 \times 6}{2} = 108$ cm²

</details>

---

### Ejercicio 4: Problema completo

Un hexágono regular tiene lado de 6 cm y apotema de aproximadamente 5.2 cm. Calcula:

1. El perímetro
2. El área
3. El ángulo central

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Perímetro = $6 \times 6 = 36$ cm
2. Área = $\frac{36 \times 5.2}{2} = 93.6$ cm²
3. Ángulo central = $\frac{360°}{6} = 60°$

</details>

---

### Ejercicio 5: Encontrar el lado

Un pentágono regular tiene perímetro de 45 cm. ¿Cuánto mide cada lado?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
l = \frac{P}{n} = \frac{45}{5} = 9 \text{ cm}
$$

</details>

---

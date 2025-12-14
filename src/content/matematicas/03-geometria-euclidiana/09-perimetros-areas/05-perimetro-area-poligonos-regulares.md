# Perímetro y Área de Polígonos Regulares

Los polígonos regulares tienen fórmulas específicas que involucran el número de lados, el lado y el apotema.

---

## 📖 Elementos de un polígono regular

| Elemento | Símbolo | Descripción |
|----------|---------|-------------|
| Número de lados | $n$ | Cantidad de lados iguales |
| Longitud del lado | $l$ | Medida de cada lado |
| Apotema | $a$ | Distancia del centro al punto medio de un lado |
| Radio | $R$ | Distancia del centro a un vértice |

---

## 📖 Perímetro

El perímetro es la suma de todos los lados:

$$
P = n \times l
$$

### Ejemplos

| Polígono | n | Lado | Perímetro |
|----------|---|------|-----------|
| Hexágono | 6 | 5 cm | 30 cm |
| Octágono | 8 | 4 cm | 32 cm |
| Decágono | 10 | 3 cm | 30 cm |

---

## 📖 Área

> **Fórmula general:** El área de un polígono regular es:

$$
A = \frac{P \times a}{2} = \frac{n \times l \times a}{2}
$$

### Interpretación

El polígono se puede dividir en $n$ triángulos iguales, cada uno con:
- Base = lado $l$
- Altura = apotema $a$
- Área de cada triángulo = $\frac{l \times a}{2}$
- Área total = $n \times \frac{l \times a}{2} = \frac{n \times l \times a}{2}$

---

## 📖 Relaciones entre elementos

### Apotema en función del lado

$$
a = \frac{l}{2 \tan\left(\frac{180°}{n}\right)}
$$

### Radio en función del lado

$$
R = \frac{l}{2 \sin\left(\frac{180°}{n}\right)}
$$

---

## 📖 Polígonos regulares comunes

### Triángulo equilátero (n = 3)

$$
A = \frac{l^2\sqrt{3}}{4}
$$

$$
a = \frac{l\sqrt{3}}{6}
$$

### Cuadrado (n = 4)

$$
A = l^2
$$

$$
a = \frac{l}{2}
$$

### Hexágono regular (n = 6)

$$
A = \frac{3l^2\sqrt{3}}{2}
$$

$$
a = \frac{l\sqrt{3}}{2}
$$

---

## 📖 Tabla de valores aproximados

Para un lado $l = 1$:

| Polígono | n | Apotema | Área |
|----------|---|---------|------|
| Triángulo equilátero | 3 | 0.289 | 0.433 |
| Cuadrado | 4 | 0.500 | 1.000 |
| Pentágono | 5 | 0.688 | 1.720 |
| Hexágono | 6 | 0.866 | 2.598 |
| Octágono | 8 | 1.207 | 4.828 |

---

## 📖 Ejemplos

### Ejemplo 1

Hexágono regular con lado 4 cm y apotema ≈ 3.46 cm:

$$
P = 6 \times 4 = 24 \text{ cm}
$$

$$
A = \frac{24 \times 3.46}{2} \approx 41.5 \text{ cm}^2
$$

### Ejemplo 2

Octágono regular con lado 5 cm y apotema ≈ 6.04 cm:

$$
P = 8 \times 5 = 40 \text{ cm}
$$

$$
A = \frac{40 \times 6.04}{2} \approx 120.8 \text{ cm}^2
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Perímetros

Calcula el perímetro de:

1. Pentágono regular, lado = 6 cm
2. Heptágono regular, lado = 4 cm
3. Dodecágono regular, lado = 3 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P = 5 \times 6 = 30$ cm
2. $P = 7 \times 4 = 28$ cm
3. $P = 12 \times 3 = 36$ cm

</details>

---

### Ejercicio 2: Áreas

Calcula el área de polígonos regulares con:

1. Perímetro = 30 cm, apotema = 4 cm
2. Perímetro = 48 cm, apotema = 6 cm
3. 6 lados, lado = 5 cm, apotema ≈ 4.33 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{30 \times 4}{2} = 60$ cm²
2. $A = \frac{48 \times 6}{2} = 144$ cm²
3. $P = 30$ cm, $A = \frac{30 \times 4.33}{2} \approx 65$ cm²

</details>

---

### Ejercicio 3: Encontrar el apotema

El área de un hexágono regular es 93.6 cm² y el perímetro es 36 cm. ¿Cuánto mide el apotema?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
a = \frac{2A}{P} = \frac{2 \times 93.6}{36} = 5.2 \text{ cm}
$$

</details>

---

### Ejercicio 4: Encontrar el lado

Un octágono regular tiene perímetro de 56 cm. ¿Cuánto mide cada lado?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
l = \frac{P}{n} = \frac{56}{8} = 7 \text{ cm}
$$

</details>

---

### Ejercicio 5: Cuadrado vs Hexágono

Compara el área de un cuadrado de lado 6 cm con un hexágono regular de lado 4 cm (apotema ≈ 3.46 cm).

<details>
<summary><strong>Ver respuesta</strong></summary>

Cuadrado: $A = 6^2 = 36$ cm²

Hexágono: $P = 24$ cm, $A = \frac{24 \times 3.46}{2} \approx 41.5$ cm²

El **hexágono** tiene mayor área.

</details>

---

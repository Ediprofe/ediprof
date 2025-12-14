# Cono

El **cono** es un cuerpo de revolución con una base circular y un vértice (cúspide) en el extremo opuesto.

---

## 📖 Definición

> **Definición:** Un cono recto es un cuerpo geométrico limitado por una **base circular** y una **superficie lateral curva** que se estrecha hasta un punto llamado **vértice** o **cúspide**.

---

## 📖 Elementos del cono

| Elemento | Símbolo | Descripción |
|----------|---------|-------------|
| Base | --- | Círculo en la parte inferior |
| Radio | $r$ | Radio de la base |
| Altura | $h$ | Distancia perpendicular de la base al vértice |
| Generatriz | $g$ | Segmento desde el borde de la base al vértice |
| Vértice | --- | Punto donde converge la superficie lateral |

---

## 📖 Relación entre elementos

La altura, el radio y la generatriz forman un triángulo rectángulo:

$$
g^2 = r^2 + h^2
$$

$$
g = \sqrt{r^2 + h^2}
$$

---

## 📖 Desarrollo plano

Al "desenrollar" un cono se obtiene:
- Un **sector circular** (la superficie lateral)
- Un **círculo** (la base)

El sector tiene:
- Radio = generatriz $g$
- Longitud de arco = circunferencia de la base = $2\pi r$

---

## 📖 Área del cono

### Área lateral

$$
A_L = \pi r g
$$

### Área de la base

$$
A_{base} = \pi r^2
$$

### Área total

$$
A_T = \pi r g + \pi r^2 = \pi r(g + r)
$$

---

## 📖 Volumen del cono

$$
V = \frac{\pi r^2 h}{3} = \frac{A_{base} \times h}{3}
$$

> El volumen del cono es **un tercio** del volumen de un cilindro con la misma base y altura.

---

## 📖 Ejemplos

### Ejemplo 1

Cono con radio 3 cm y altura 4 cm:

$$
g = \sqrt{9 + 16} = \sqrt{25} = 5 \text{ cm}
$$

$$
A_L = \pi(3)(5) = 15\pi \approx 47.12 \text{ cm}^2
$$

$$
A_T = \pi(3)(8) = 24\pi \approx 75.4 \text{ cm}^2
$$

$$
V = \frac{\pi(9)(4)}{3} = 12\pi \approx 37.7 \text{ cm}^3
$$

### Ejemplo 2

Cono con radio 6 cm y generatriz 10 cm:

$$
h = \sqrt{100 - 36} = \sqrt{64} = 8 \text{ cm}
$$

$$
V = \frac{\pi(36)(8)}{3} = 96\pi \approx 301.6 \text{ cm}^3
$$

---

## 📖 Relación con el cilindro

$$
V_{cono} = \frac{1}{3} V_{cilindro}
$$

(Con la misma base y altura)

Esto significa que **3 conos** llenan un cilindro de igual base y altura.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Generatriz

Calcula la generatriz de conos con:

1. Radio = 6 cm, altura = 8 cm
2. Radio = 5 cm, altura = 12 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $g = \sqrt{36 + 64} = \sqrt{100} = 10$ cm
2. $g = \sqrt{25 + 144} = \sqrt{169} = 13$ cm

</details>

---

### Ejercicio 2: Área y volumen

Cono con radio 4 cm y altura 3 cm. Calcula:

1. Generatriz
2. Área lateral
3. Área total
4. Volumen

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $g = \sqrt{16 + 9} = 5$ cm
2. $A_L = \pi(4)(5) = 20\pi \approx 62.83$ cm²
3. $A_T = \pi(4)(9) = 36\pi \approx 113.1$ cm²
4. $V = \frac{\pi(16)(3)}{3} = 16\pi \approx 50.27$ cm³

</details>

---

### Ejercicio 3: Encontrar la altura

Un cono tiene radio 5 cm y generatriz 13 cm. ¿Cuál es la altura?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
h = \sqrt{169 - 25} = \sqrt{144} = 12 \text{ cm}
$$

</details>

---

### Ejercicio 4: Problema inverso

El volumen de un cono es 100π cm³ y la altura es 12 cm. ¿Cuál es el radio?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
100\pi = \frac{\pi r^2 \times 12}{3}
$$

$$
100 = 4r^2
$$

$$
r = 5 \text{ cm}
$$

</details>

---

### Ejercicio 5: Comparación cono-cilindro

¿Cuántos conos de helado (radio 3 cm, altura 10 cm) se necesitan para llenar un vaso cilíndrico (radio 3 cm, altura 10 cm)?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\frac{V_{cilindro}}{V_{cono}} = \frac{\pi r^2 h}{\frac{\pi r^2 h}{3}} = 3
$$

Se necesitan **3 conos**.

</details>

---

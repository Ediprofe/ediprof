# Troncos de Pirámide y Cono

Un **tronco** es la porción de una pirámide o cono que queda al cortarlo con un plano paralelo a la base.

---

## 📖 ¿Qué es un tronco?

> **Definición:** Un tronco (o frustum) es el cuerpo geométrico que resulta al cortar una pirámide o cono con un **plano paralelo a la base**, eliminando la parte superior.

El tronco tiene **dos bases paralelas** de diferente tamaño.

---

## 📖 Elementos del tronco

| Elemento | Descripción |
|----------|-------------|
| Base mayor ($B$ o $R$) | La base original de la pirámide/cono |
| Base menor ($b$ o $r$) | La sección del corte |
| Altura ($h$) | Distancia perpendicular entre las bases |
| Apotema ($a_p$) | Altura de las caras laterales (en troncos regulares) |

---

## 📖 Tronco de pirámide

### Área lateral

Para un tronco de pirámide regular:

$$
A_L = \frac{(P_B + P_b) \times a_p}{2}
$$

Donde $P_B$ y $P_b$ son los perímetros de las bases.

### Área total

$$
A_T = A_L + A_B + A_b
$$

### Volumen

$$
V = \frac{h}{3}(A_B + A_b + \sqrt{A_B \times A_b})
$$

---

## 📖 Tronco de cono

### Área lateral

$$
A_L = \pi(R + r) \times g
$$

Donde $g$ es la generatriz del tronco:

$$
g = \sqrt{h^2 + (R-r)^2}
$$

### Área total

$$
A_T = \pi(R + r)g + \pi R^2 + \pi r^2
$$

### Volumen

$$
V = \frac{\pi h}{3}(R^2 + r^2 + Rr)
$$

---

## 📖 Ejemplo: Tronco de cono

Tronco con $R = 6$ cm, $r = 3$ cm, $h = 4$ cm:

### Generatriz

$$
g = \sqrt{16 + 9} = 5 \text{ cm}
$$

### Área lateral

$$
A_L = \pi(6 + 3)(5) = 45\pi \approx 141.37 \text{ cm}^2
$$

### Volumen

$$
V = \frac{\pi \times 4}{3}(36 + 9 + 18) = \frac{4\pi \times 63}{3} = 84\pi \approx 263.89 \text{ cm}^3
$$

---

## 📖 Ejemplo: Tronco de pirámide cuadrada

Tronco con bases cuadradas de lados 10 cm y 6 cm, altura 8 cm:

### Áreas de las bases

$$
A_B = 100 \text{ cm}^2, \quad A_b = 36 \text{ cm}^2
$$

### Volumen

$$
V = \frac{8}{3}(100 + 36 + \sqrt{100 \times 36})
$$

$$
= \frac{8}{3}(100 + 36 + 60) = \frac{8 \times 196}{3} \approx 522.67 \text{ cm}^3
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Tronco de cono

Tronco con $R = 8$ cm, $r = 4$ cm, $h = 6$ cm. Calcula:

1. Generatriz
2. Volumen

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $g = \sqrt{36 + 16} = \sqrt{52} \approx 7.21$ cm
2. $V = \frac{\pi \times 6}{3}(64 + 16 + 32) = 2\pi \times 112 = 224\pi \approx 703.72$ cm³

</details>

---

### Ejercicio 2: Tronco de pirámide

Tronco de pirámide cuadrada con bases de lados 12 cm y 8 cm, altura 9 cm. Calcula el volumen.

<details>
<summary><strong>Ver respuesta</strong></summary>

$A_B = 144$ cm², $A_b = 64$ cm²

$$
V = \frac{9}{3}(144 + 64 + \sqrt{144 \times 64}) = 3(144 + 64 + 96) = 3 \times 304 = 912 \text{ cm}^3
$$

</details>

---

### Ejercicio 3: Generatriz

En un tronco de cono, $R = 5$ cm, $r = 2$ cm y $h = 4$ cm. ¿Cuánto mide la generatriz?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
g = \sqrt{4^2 + (5-2)^2} = \sqrt{16 + 9} = \sqrt{25} = 5 \text{ cm}
$$

</details>

---

### Ejercicio 4: Problema aplicado

Un vaso con forma de tronco de cono tiene radio superior 4 cm, radio inferior 3 cm y altura 10 cm. ¿Cuántos ml caben? (1 cm³ = 1 ml)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V = \frac{\pi \times 10}{3}(16 + 9 + 12) = \frac{10\pi \times 37}{3} \approx 387.46 \text{ cm}^3
$$

Caben aproximadamente **387 ml**.

</details>

---

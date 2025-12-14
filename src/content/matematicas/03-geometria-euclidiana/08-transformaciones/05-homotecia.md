# Homotecia

La **homotecia** es una transformación que amplía o reduce una figura desde un punto fijo, manteniendo su forma pero cambiando su tamaño.

---

## 📖 Definición

> **Definición:** Una homotecia con centro $O$ y razón $k$ transforma cada punto $P$ en un punto $P'$ tal que $P'$ está en la recta $OP$ y $\overline{OP'} = k \cdot \overline{OP}$.

### Elementos de la homotecia

| Elemento | Descripción |
|----------|-------------|
| Centro ($O$) | Punto fijo desde donde se mide |
| Razón ($k$) | Factor de escala |

---

## 📖 La razón de homotecia

| Valor de $k$ | Efecto |
|--------------|--------|
| $k > 1$ | Ampliación |
| $0 < k < 1$ | Reducción |
| $k = 1$ | Figura igual (identidad) |
| $k < 0$ | Ampliación/reducción + inversión |

### Ejemplos

- $k = 2$: la figura se duplica
- $k = 0.5$: la figura se reduce a la mitad
- $k = -1$: simetría central (reflexión por el centro)

---

## 📖 Fórmula de homotecia

Si el centro es $O(a, b)$ y la razón es $k$, el punto $P(x, y)$ se transforma en:

$$
x' = a + k(x - a)
$$

$$
y' = b + k(y - b)
$$

### Centro en el origen

Si $O = (0, 0)$:

$$
P'(x', y') = (kx, ky)
$$

### Ejemplo

Homotecia con centro $(0, 0)$ y $k = 3$ aplicada a $P(2, 4)$:

$$
P' = (3 \cdot 2, 3 \cdot 4) = (6, 12)
$$

---

## 📖 Propiedades de la homotecia

### Conserva

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Forma | Sí |
| Ángulos | Sí |
| Paralelismo | Sí |
| Razón entre segmentos | Sí |

### Cambia

| Propiedad | ¿Cómo cambia? |
|-----------|---------------|
| Distancias | Se multiplican por $|k|$ |
| Perímetro | Se multiplica por $|k|$ |
| Área | Se multiplica por $k^2$ |

---

## 📖 Punto fijo

El único punto fijo de una homotecia es el **centro** $O$.

$$
H(O) = O
$$

---

## 📖 Homotecia inversa

La homotecia inversa tiene razón $\frac{1}{k}$:

$$
H_{O,k}^{-1} = H_{O, 1/k}
$$

---

## 📖 Relación con semejanza

Una homotecia produce figuras **semejantes**:
- Misma forma
- Tamaño proporcional
- Razón de semejanza = $|k|$

---

## 📖 Ejemplo completo

Aplicar homotecia con centro $(1, 2)$ y razón $k = 2$ al punto $P(4, 5)$:

$$
x' = 1 + 2(4 - 1) = 1 + 2(3) = 1 + 6 = 7
$$

$$
y' = 2 + 2(5 - 2) = 2 + 2(3) = 2 + 6 = 8
$$

$$
P' = (7, 8)
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Centro en el origen

Aplica homotecia con centro en el origen:

1. $P(3, 2)$ con $k = 2$
2. $Q(8, 4)$ con $k = 0.5$
3. $R(-2, 6)$ con $k = 3$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P' = (6, 4)$
2. $Q' = (4, 2)$
3. $R' = (-6, 18)$

</details>

---

### Ejercicio 2: Centro diferente del origen

Aplica homotecia con centro $(2, 1)$ y $k = 3$ al punto $P(4, 3)$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
x' = 2 + 3(4 - 2) = 2 + 6 = 8
$$

$$
y' = 1 + 3(3 - 1) = 1 + 6 = 7
$$

$$
P' = (8, 7)
$$

</details>

---

### Ejercicio 3: Efectos en área

Un triángulo tiene área 12 cm². ¿Cuál es el área después de una homotecia con $k = 2$?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A' = k^2 \cdot A = 2^2 \cdot 12 = 4 \cdot 12 = 48 \text{ cm}^2
$$

</details>

---

### Ejercicio 4: Encontrar la razón

Un segmento de 5 cm se transforma en uno de 15 cm mediante una homotecia. ¿Cuál es la razón?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
k = \frac{15}{5} = 3
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. Una homotecia con $k = 1$ deja la figura igual.
2. El área se multiplica por $k$ en una homotecia.
3. Una homotecia conserva los ángulos.
4. Con $k = -1$, la homotecia es una simetría central.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Es la identidad
2. **Falso** - Se multiplica por $k^2$
3. **Verdadero**
4. **Verdadero** - Equivale a rotación de 180°

</details>

---

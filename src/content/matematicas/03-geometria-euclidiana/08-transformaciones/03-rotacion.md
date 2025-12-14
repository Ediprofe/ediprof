# Rotación

La **rotación** es el movimiento circular alrededor de un punto fijo. Es como girar una figura sobre un eje.

---

## 📖 Definición

> **Definición:** Una rotación gira todos los puntos de una figura alrededor de un punto fijo llamado **centro**, a través de un **ángulo** determinado.

### Elementos de la rotación

| Elemento | Descripción |
|----------|-------------|
| Centro | Punto fijo alrededor del cual se gira |
| Ángulo | Cantidad de giro (en grados) |
| Sentido | Antihorario (+) o horario (−) |

---

## 📖 Notación

$$
R_{O,\theta}
$$

- $O$ = centro de rotación
- $\theta$ = ángulo de rotación

### Convención de signos

- $\theta > 0$: sentido **antihorario** (contrario a las agujas del reloj)
- $\theta < 0$: sentido **horario** (en el sentido de las agujas del reloj)

---

## 📖 Fórmula de rotación

Para rotar el punto $P(x, y)$ alrededor del **origen** un ángulo $\theta$:

$$
x' = x \cos\theta - y \sin\theta
$$

$$
y' = x \sin\theta + y \cos\theta
$$

### En forma matricial

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
$$

---

## 📖 Rotaciones especiales (centro en origen)

### Rotación de 90° (antihorario)

$$
P(x, y) \to P'(-y, x)
$$

### Rotación de 180°

$$
P(x, y) \to P'(-x, -y)
$$

### Rotación de 270° (o −90°)

$$
P(x, y) \to P'(y, -x)
$$

### Rotación de 360°

$$
P(x, y) \to P(x, y)
$$

(Vuelve a la posición original)

---

## 📖 Ejemplos

### Ejemplo 1: Rotación de 90°

Rotar $P(3, 2)$ un ángulo de 90° alrededor del origen:

$$
P' = (-2, 3)
$$

### Ejemplo 2: Rotación de 180°

Rotar $P(4, -1)$ un ángulo de 180° alrededor del origen:

$$
P' = (-4, 1)
$$

---

## 📖 Propiedades de la rotación

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Distancias | Sí |
| Ángulos | Sí |
| Área | Sí |
| Forma | Sí |
| Orientación | Sí |

### La rotación es una isometría

Conserva todas las distancias y ángulos.

### Punto fijo

Solo el **centro** de rotación queda fijo (excepto si $\theta = 0°$ o múltiplo de 360°).

---

## 📖 Rotación con centro fuera del origen

Si el centro es $C(h, k)$:

1. Trasladar para que $C$ quede en el origen
2. Rotar
3. Trasladar de vuelta

$$
x' = (x - h)\cos\theta - (y - k)\sin\theta + h
$$

$$
y' = (x - h)\sin\theta + (y - k)\cos\theta + k
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Rotaciones especiales

Aplica cada rotación al punto $P(4, 1)$ alrededor del origen:

1. Rotación de 90°
2. Rotación de 180°
3. Rotación de 270°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P' = (-1, 4)$
2. $P' = (-4, -1)$
3. $P' = (1, -4)$

</details>

---

### Ejercicio 2: Rotación de 180°

Rota el punto $Q(-2, 5)$ un ángulo de 180° alrededor del origen.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
Q' = (2, -5)
$$

</details>

---

### Ejercicio 3: Identificar la rotación

El punto $A(3, 0)$ se transforma en $A'(0, 3)$. ¿Cuál fue el ángulo de rotación?

<details>
<summary><strong>Ver respuesta</strong></summary>

Era $(3, 0) \to (0, 3)$, que corresponde a una **rotación de 90°** antihorario.

</details>

---

### Ejercicio 4: Triángulo

Rota el triángulo con vértices $A(1, 0)$, $B(3, 0)$, $C(2, 2)$ un ángulo de 180° alrededor del origen.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A' = (-1, 0)
$$

$$
B' = (-3, 0)
$$

$$
C' = (-2, -2)
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. En una rotación de 360°, todos los puntos son fijos.
2. El centro de rotación es el único punto fijo en una rotación no nula.
3. Una rotación de −90° es igual a una rotación de 270°.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Verdadero**
3. **Verdadero** (ambas dan el mismo resultado)

</details>

---

---
title: "Rotación"
---

# **Rotación**

Imagina que clavas un alfiler en una foto y la haces girar sobre ese punto. Eso es una rotación. Todo se mueve en círculos alrededor de un centro, excepto el propio centro.

---

## 🎯 ¿Qué vas a aprender?

- Definir una rotación mediante un centro, un ángulo y un sentido.
- Rotar puntos en el plano cartesiano ($90^\circ$, $180^\circ$, $270^\circ$).
- Entender que la rotación es una isometría (conserva la forma y el tamaño).

---

## 🌀 Elementos de la Rotación

Para girar algo con precisión matemática, necesitas definir tres cosas:

1.  **Centro de Rotación ($O$):** El punto que se queda quieto. El eje del giro.
2.  **Ángulo ($\theta$):** Cuánto vas a girar (en grados).
3.  **Sentido:** Hacia dónde girar.
    *   **Antihorario (+):** Contra las manecillas del reloj. (Estándar matemático).
    *   **Horario (-):** A favor de las manecillas del reloj.

---

## 📐 Fórmulas de Rotación (Centro en el Origen)

Si el centro de rotación es $(0,0)$, las coordenadas cambian siguiendo reglas fijas para los ángulos principales (en sentido antihorario):

### 1. Rotación de $90^\circ$
El punto pasa del primer cuadrante al segundo. La $x$ se vuelve $y$, y la $y$ se vuelve $x$ (con cambio de signo).

$$
P(x, y) \rightarrow P'(-y, x)
$$

### 2. Rotación de $180^\circ$
Es media vuelta. El punto pasa al cuadrante opuesto. Ambos signos se invierten. (Equivale a una simetría central).

$$
P(x, y) \rightarrow P'(-x, -y)
$$

### 3. Rotación de $270^\circ$ (o $-90^\circ$)
Es tres cuartos de vuelta.

$$
P(x, y) \rightarrow P'(y, -x)
$$

### 4. Rotación de $360^\circ$
Vuelta completa. Quedas donde empezaste.

$$
P(x, y) \rightarrow P'(x, y)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Rotar $90^\circ$

Rota el punto $A(3, 5)$ un ángulo de $90^\circ$ respecto al origen.

**Razonamiento:**
Regla $90^\circ$: $(-y, x)$.
$x=3, y=5$.
$-y = -5$.
$x = 3$.

**Resultado:**
$$
\boxed{A'(-5, 3)}
$$

### Ejemplo 2: Rotar $180^\circ$

Rota el punto $B(-2, 4)$ un ángulo de $180^\circ$.

**Razonamiento:**
Regla $180^\circ$: $(-x, -y)$.
$-(-2) = 2$.
$-(4) = -4$.

**Resultado:**
$$
\boxed{B'(2, -4)}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Rota el punto $P(2, 8)$ en $90^\circ$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(-y, x) \to (-8, 2)$.

**Resultado:**
$$
\boxed{P'(-8, 2)}
$$

</details>

### Ejercicio 2
Rota el punto $Q(5, -1)$ en $180^\circ$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Invierte signos.

**Resultado:**
$$
\boxed{Q'(-5, 1)}
$$

</details>

### Ejercicio 3
Rota el punto $R(3, 4)$ en $270^\circ$ (o $-90^\circ$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(y, -x) \to (4, -3)$.

**Resultado:**
$$
\boxed{R'(4, -3)}
$$

</details>

### Ejercicio 4
Si aplicas una rotación de $90^\circ$ dos veces seguidas, ¿a qué equivale?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$90 + 90 = 180$.

**Resultado:**
$$
\boxed{\text{Rotación de } 180^\circ}
$$

</details>

### Ejercicio 5
¿Cuál es la imagen de $(0, 5)$ tras una rotación de $90^\circ$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(-5, 0)$.

**Resultado:**
$$
\boxed{(-5, 0)}
$$

</details>

### Ejercicio 6
Verdadero o Falso: En una rotación, la distancia desde el punto al centro cambia.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. Es un movimiento circular, el radio (distancia al centro) es constante.

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 7
Rota el triángulo de vértices $A(1, 0)$, $B(3, 0)$, $C(1, 2)$ en $180^\circ$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A \to (-1, 0)$
$B \to (-3, 0)$
$C \to (-1, -2)$

**Resultado:**
$$
A'(-1, 0), B'(-3, 0), C'(-1, -2)
$$

</details>

### Ejercicio 8
¿Qué rotación transforma $(1, 1)$ en $(-1, 1)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$P(1, 1) \to P'(-1, 1)$.
La regla aplicada es $(-x, y)$? No, eso es reflexión eje Y.
Veamos: $(-y, x)$ sería $(-1, 1)$. ¡Coincide!
Entonces es $90^\circ$.

**Resultado:**
$$
\boxed{90^\circ}
$$

</details>

### Ejercicio 9
Una rotación horaria de $90^\circ$ es lo mismo que...

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Rotación antihoraria de } 270^\circ
$$

</details>

### Ejercicio 10
Si el centro de rotación no es el origen, ¿qué debes hacer primero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Trasladar todo para que el centro coincida con el origen, rotar, y trasladar de vuelta.

**Resultado:**
$$
\boxed{\text{Trasladar al origen}}
$$

</details>

---

## 🔑 Resumen

| Ángulo | Regla de Transformación |
| :--- | :--- |
| **$90^\circ$** | $(x, y) \to (-y, x)$ |
| **$180^\circ$** | $(x, y) \to (-x, -y)$ |
| **$270^\circ$** | $(x, y) \to (y, -x)$ |
| **$360^\circ$** | $(x, y) \to (x, y)$ |

> Recuerda: El sentido positivo en matemáticas es **antihorario**.

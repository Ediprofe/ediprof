# **Homotecia (Semejanza)**

Imagina que proyectas la sombra de tu mano en la pared. Dependiendo de cuán cerca estés de la luz, la sombra puede ser enorme o pequeña. Eso es una homotecia: cambiar el tamaño de una figura sin alterar su forma.

---

## 🎯 ¿Qué vas a aprender?

- Definir una **homotecia** usando un centro ($O$) y una razón ($k$).
- Calcular la imagen de un punto en el plano.
- Entender cómo cambia el tamaño (distancias, perímetros, áreas).
- Distinguir entre ampliación, reducción e identidad.

---

## 📏 Elementos de la Homotecia

Para "escalar" una figura, necesitamos:

1.  **Centro de Homotecia ($O$):** El punto fijo desde donde se proyectan los rayos (la fuente de luz).
2.  **Razón de Homotecia ($k$):** El factor de zoom.
    *   Si $k > 1$: **Ampliación**.
    *   Si $0 < k < 1$: **Reducción**.
    *   Si $k = 1$: Misma figura (**Identidad**).
    *   Si $k < 0$: Inversión (la figura se voltea al otro lado del centro).

---

## 📐 Fórmulas

En la homotecia, las distancias desde el centro se multiplican por $k$.

$$
\text{Distancia Final} = k \times \text{Distancia Inicial}
$$

### Si el Centro es el Origen $(0,0)$
Es muy sencillo. Solo multiplicas las coordenadas por $k$.

$$
P(x, y) \rightarrow P'(kx, ky)
$$

### Si el Centro es $(a, b)$
Usamos la fórmula general vectorial:

$$
P' = O + k(P - O)
$$

O coordenada a coordenada:

$$
x' = a + k(x - a)
$$

$$
y' = b + k(y - b)
$$

---

## ⚙️ Efectos en el Tamaño

Si aplicas una homotecia de razón $k$:

1.  **Lados y Distancias:** Se multiplican por $|k|$.
2.  **Perímetro:** Se multiplica por $|k|$.
3.  **Área:** Se multiplica por $k^2$ (¡El área crece al cuadrado!).
4.  **Ángulos:** Se conservan (No cambian nunca).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Ampliación ($k=2$)

Aplica una homotecia con centro en el origen y razón $k=2$ al punto $A(3, 4)$.

**Razonamiento:**
Multiplicamos cada coordenada por 2.
$x' = 2 \times 3 = 6$.
$y' = 2 \times 4 = 8$.

**Resultado:**
$$
\boxed{A'(6, 8)}
$$

### Ejemplo 2: Reducción ($k=0.5$)

Reduce el punto $B(10, -6)$ a la mitad desde el origen.

**Razonamiento:**
$x' = 0.5 \times 10 = 5$.
$y' = 0.5 \times (-6) = -3$.

**Resultado:**
$$
\boxed{B'(5, -3)}
$$

### Ejemplo 3: Efecto en el Área

Un cuadrado tiene área 100 cm². Si se le aplica una homotecia con $k=3$, ¿cuál es su nueva área?

**Razonamiento:**
El área se multiplica por $k^2$.
$k^2 = 3^2 = 9$.
Nueva área = $100 \times 9$.

**Resultado:**
$$
\boxed{900 \text{ cm}^2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Amplía el punto $P(2, 5)$ con $k=3$ desde el origen.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(3\times2, 3\times5)$.

**Resultado:**
$$
\boxed{P'(6, 15)}
$$

</details>

### Ejercicio 2
Si $A(4, 4)$ se transforma en $A'(2, 2)$, ¿cuánto vale $k$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2 = k \times 4$.
$k = 2/4 = 0.5$.

**Resultado:**
$$
\boxed{k = 0.5}
$$

</details>

### Ejercicio 3
Una homotecia con $k=-2$ desde el origen. Aplícala a $Q(1, -3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$( -2 \times 1, -2 \times -3 )$.

**Resultado:**
$$
\boxed{Q'(-2, 6)}
$$

</details>

### Ejercicio 4
Si $k=5$, ¿cuánto aumenta el perímetro?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{5 veces}
$$

</details>

### Ejercicio 5
Si $k=4$, ¿cuánto aumenta el área?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$4^2 = 16$.

**Resultado:**
$$
\boxed{16 \text{ veces}}
$$

</details>

### Ejercicio 6
Verdadero o Falso: La homotecia conserva los ángulos.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Verdadero. La forma no cambia.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 7
¿Qué punto nunca se mueve en una homotecia?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{El Centro de Homotecia}
$$

</details>

### Ejercicio 8
Aplica $k=0$ a un punto $(5, 8)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(0 \times 5, 0 \times 8) = (0, 0)$. Todo colapsa al origen.

**Resultado:**
$$
\boxed{(0, 0)}
$$

</details>

### Ejercicio 9
Si $k=1$, ¿qué pasa?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Nada (La figura queda igual)}
$$

</details>

### Ejercicio 10
Desde el centro $C(1, 1)$, aplica $k=2$ al punto $P(2, 2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Vector $CP = (2-1, 2-1) = (1, 1)$.
Multiplicamos vector por 2: $(2, 2)$.
Sumamos al centro: $(1+2, 1+2) = (3, 3)$.

**Resultado:**
$$
\boxed{P'(3, 3)}
$$

</details>

---

## 🔑 Resumen

| Razón ($k$) | Efecto |
| :--- | :--- |
| **$k > 1$** | Ampliación (Zoom in). |
| **$0 < k < 1$** | Reducción (Zoom out). |
| **$k < 0$** | Inversión + Escala. |
| **$k = 1$** | Identidad. |

> Recuerda: La homotecia es la única de las transformaciones básicas que cambia el tamaño y el área.

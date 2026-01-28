---
title: "Traslación"
---

# **Traslación**

Imagínate moviendo una pieza de ajedrez en línea recta, o deslizando un icono en tu pantalla táctil. Eso es una traslación: mover algo de un lugar a otro sin girarlo, ni reflejarlo, ni cambiarlo de tamaño.

---

## 🎯 ¿Qué vas a aprender?

- Definir una traslación usando un vector.
- Mover puntos y figuras en el plano cartesiano usando coordenadas.
- Comprender que una traslación es una isometría (no deforma la figura).
- Calcular el vector de traslación si conoces el punto inicial y el final.

---

## 📏 El Vector de Traslación

Para describir una traslación, necesitamos un **vector** $\vec{v} = (a, b)$.
Este vector nos dice dos cosas:
1.  **Cuánto movernos en $x$ ($a$):** Derecha (positivo) o Izquierda (negativo).
2.  **Cuánto movernos en $y$ ($b$):** Arriba (positivo) o Abajo (negativo).

Si aplicamos este vector a un punto original $P(x, y)$, obtenemos su imagen $P'(x', y')$ sumando las coordenadas.

$$
P'(x', y') = (x + a, \quad y + b)
$$

---

## ⚙️ Propiedades Clave

1.  **Isometría:** La figura resultante es idéntica a la original. Los lados miden lo mismo y los ángulos también.
2.  **Paralelismo:** Los segmentos que unen cada punto original con su imagen ($PP'$, $AA'$, etc.) son paralelos entre sí y tienen la misma longitud.
3.  **Sin Rotación:** La orientación de la figura no cambia (si el triángulo apuntaba hacia arriba, sigue apuntando hacia arriba).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Trasladar un Punto

Mueve el punto $A(2, 3)$ según el vector $\vec{v} = (4, -5)$.

**Razonamiento:**
Sumamos la componente $x$ del vector a la $x$ del punto, y la $y$ a la $y$.
$x' = 2 + 4 = 6$
$y' = 3 + (-5) = -2$

**Resultado:**
$$
A'(6, -2)
$$

### Ejemplo 2: Hallar el Vector

Un punto $B(1, 5)$ se trasladó hasta $B'(7, 9)$. ¿Cuál fue el vector de traslación?

**Razonamiento:**
El vector es la diferencia entre el punto final y el inicial ($\text{Final} - \text{Inicial}$).
$a = 7 - 1 = 6$
$b = 9 - 5 = 4$

**Resultado:**
$$
\vec{v} = (6, 4)
$$

### Ejemplo 3: Trasladar una Figura

Traslada el triángulo con vértices $A(0,0)$, $B(3,0)$ y $C(0,4)$ usando el vector $\vec{v}=(2, 1)$.

**Razonamiento:**
Aplicamos la suma a cada vértice:
$A(0,0) \to (0+2, 0+1) \to A'(2, 1)$
$B(3,0) \to (3+2, 0+1) \to B'(5, 1)$
$C(0,4) \to (0+2, 4+1) \to C'(2, 5)$

**Resultado:**
$$
\text{Vértices: } A'(2, 1), B'(5, 1), C'(2, 5)
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Traslada el punto $P(-2, 4)$ con el vector $\vec{v} = (5, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(-2+5, 4+3)$

**Resultado:**
$$
\boxed{P'(3, 7)}
$$

</details>

### Ejercicio 2
Si $Q(10, 10)$ se mueve a $Q'(8, 12)$, halla el vector de traslación.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a = 8 - 10 = -2$
$b = 12 - 10 = 2$

**Resultado:**
$$
\boxed{\vec{v} = (-2, 2)}
$$

</details>

### Ejercicio 3
Una traslación mueve el origen $(0,0)$ al punto $(3, -4)$. ¿Cuál es el vector?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El desplazamiento desde el origen es el mismo vector.

**Resultado:**
$$
\boxed{\vec{v} = (3, -4)}
$$

</details>

### Ejercicio 4
Si aplicas una traslación $\vec{v}=(2, 0)$, ¿cómo se mueve la figura?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{2 unidades a la derecha (horizontalmente)}
$$

</details>

### Ejercicio 5
Traslada el segmento $A(1, 1)$ a $B(2, 2)$ con vector $\vec{v}=(-1, -1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A' = (1-1, 1-1) = (0, 0)$
$B' = (2-1, 2-1) = (1, 1)$

**Resultado:**
$$
\text{Segmento } A'(0,0) \text{ a } B'(1,1)
$$

</details>

### Ejercicio 6
Verdadero o Falso: Trasladar una figura cambia sus ángulos internos.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. Es una isometría (rígida).

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 7
¿Qué vector necesitas para "deshacer" una traslación de $\vec{v}=(3, 5)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El vector inverso (negativo).
$(-3, -5)$.

**Resultado:**
$$
\boxed{\vec{u} = (-3, -5)}
$$

</details>

### Ejercicio 8
Si trasladas un círculo de radio 5 con $\vec{v}=(100, 100)$, ¿cuál es el nuevo radio?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El tamaño no cambia.

**Resultado:**
$$
\boxed{5}
$$

</details>

### Ejercicio 9
Calcula la distancia que se ha movido un punto trasladado con $\vec{v}=(3, 4)$.
*(Pista: Es la magnitud del vector)*.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Pitágoras con las componentes del vector.
$d = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5$.

**Resultado:**
$$
\boxed{5 \text{ unidades}}
$$

</details>

### Ejercicio 10
Tienes el punto $M(5, 5)$. Le aplicas $\vec{v}=(2, 0)$ y luego $\vec{u}=(0, 3)$. ¿Dónde termina?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$5+2+0 = 7$.
$5+0+3 = 8$.

**Resultado:**
$$
\boxed{M''(7, 8)}
$$

</details>

---

## 🔑 Resumen

| Operación | Componente $x$ | Componente $y$ |
| :--- | :--- | :--- |
| **Traslación (+)** | $x + a$ | $y + b$ |
| **Hallar Vector** | $x_{\text{final}} - x_{\text{inicial}}$ | $y_{\text{final}} - y_{\text{inicial}}$ |

> La traslación es la "suma" de la geometría. Simplemente sumas el vector a cada punto.

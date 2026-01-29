# **Introducción a Ecuaciones Paramétricas**

¿Cómo describir la trayectoria de una mosca volando? No basta con decir por dónde pasa ($y=x^2$), necesitas decir **cuándo** pasa por ahí. Las ecuaciones paramétricas añaden esa tercera dimensión invisible: el tiempo.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un parámetro ($t$).
- Cómo separar $x$ e $y$ en dos funciones independientes.
- Graficar punto a punto siguiendo el "reloj".

---

## ⏱️ El Concepto del Parámetro

En lugar de relacionar $y$ directamente con $x$, relacionamos ambas con un tercero en discordia: el parámetro $t$.

$$ x = f(t) $$
$$ y = g(t) $$

Imagina que $t$ es el **tiempo**.
*   $x(t)$ te dice tu posición horizontal en el segundo $t$.
*   $y(t)$ te dice tu altura en el segundo $t$.

---

## 🚗 Concepto 1: Trayectorias Simples

Veamos cómo se mueve un punto en **5 ejemplos diferentes**:

### Ejemplo 1.1: Movimiento Lineal
$$ x = t, \quad y = 2t $$
*   $t=0 \to (0,0)$.
*   $t=1 \to (1,2)$.
*   $t=2 \to (2,4)$.
*   *Descripción:* Una recta que sale del origen y sube rápido.

### Ejemplo 1.2: El Círculo Trigonométrico
$$ x = \cos t, \quad y = \sin t $$
*   $t=0 \to (1,0)$.
*   $t=\pi/2 \to (0,1)$.
*   $t=\pi \to (-1,0)$.
*   *Descripción:* Un círculo unitario recorrido en sentido antihorario.

### Ejemplo 1.3: La Parábola
$$ x = t, \quad y = t^2 $$
*   $t=-1 \to (-1,1)$.
*   $t=0 \to (0,0)$.
*   $t=1 \to (1,1)$.
*   *Descripción:* La clásica parábola $y=x^2$.

### Ejemplo 1.4: Movimiento Horizontal
$$ x = \sin t, \quad y = 2 $$
*   $x$ oscila entre -1 y 1. $y$ siempre es 2.
*   *Descripción:* Un punto rebotando de izquierda a derecha sobre una línea horizontal.

### Ejemplo 1.5: La Cicloide (Rueda)
$$ x = t - \sin t, \quad y = 1 - \cos t $$
*   Describe el camino de un punto en el borde de una llanta que rueda. Es una serie de arcos.

---

## 🛑 Concepto 2: Restricciones del Dominio

El parámetro $t$ suele tener límites (ej. $0 \le t \le 10$). Esto significa que la curva no es infinita; tiene un **punto inicial** y un **punto final**.

**5 Ejemplos de Segmentos:**

### Ejemplo 2.1
$x=t, y=t$, para $0 \le t \le 1$.
*   Inicia en $(0,0)$.
*   Termina en $(1,1)$.
*   Es un **segmento de recta**.

### Ejemplo 2.2
$x=\cos t, y=\sin t$, para $0 \le t \le \pi$.
*   Inicia en $(1,0)$.
*   Pasa por $(0,1)$.
*   Termina en $(-1,0)$.
*   Es **medio círculo** (arco superior).

### Ejemplo 2.3
$x=t^2, y=t$, para $t \ge 0$.
*   Solo la rama superior de la parábola horizontal ($y = \sqrt{x}$).

### Ejemplo 2.4
$x = e^t, y = e^{2t}$. (Observa que $e^t$ siempre es positivo).
*   $x > 0$.
*   Es la rama derecha de la parábola $y=x^2$.

### Ejemplo 2.5
$x = 2t, y = 3t$, para $-1 \le t \le 1$.
*   Va desde $(-2, -3)$ hasta $(2, 3)$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Punto inicial de $x=t+1, y=t-1$ ($t \ge 0$).

<details>
<summary>Ver solución</summary>
$t=0 \Rightarrow (1, -1)$.
</details>

---

### Ejercicio 2
Si $x=\cos t, y=\sin t$, ubica $t=\pi/2$.

<details>
<summary>Ver solución</summary>
$(0, 1)$.
</details>

---

### Ejercicio 3
¿Es $x=t^2, y=t^4$ lo mismo que $y=x^2$?

<details>
<summary>Ver solución</summary>
Sí, pero solo para $x \ge 0$ (porque $t^2$ es positivo).
</details>

---

### Ejercicio 4
Describe $x=3, y=t$.

<details>
<summary>Ver solución</summary>
Recta vertical en $x=3$.
</details>

---

### Ejercicio 5
Calcula $y$ cuando $x=0$ en la cicloide clásica ($t=0$).

<details>
<summary>Ver solución</summary>
$y = 1 - \cos(0) = 0$.
</details>

---

### Ejercicio 6
Punto final de $x=t, y=t$ en $t \in [0, 5]$.

<details>
<summary>Ver solución</summary>
$(5, 5)$.
</details>

---

### Ejercicio 7
¿Puede una curva paramétrica cruzarse a sí misma?

<details>
<summary>Ver solución</summary>
Sí (ej. un 8 figura). Significa pasar por el mismo lugar en distinto tiempo.
</details>

---

### Ejercicio 8
Elimina el parámetro de $x=t, y=3t$.

<details>
<summary>Ver solución</summary>
$y = 3x$.
</details>

---

### Ejercicio 9
Diferencia entre $x=t, y=t$ y $x=t^3, y=t^3$.

<details>
<summary>Ver solución</summary>
La gráfica es idéntica (recta $y=x$), pero la velocidad de trazado es diferente.
</details>

---

### Ejercicio 10
Si $x=5\cos t, y=2\sin t$, ¿qué figura es?

<details>
<summary>Ver solución</summary>
Elipse ($a=5, b=2$).
</details>

---

## 🔑 Resumen

| Característica | Importancia |
| :--- | :--- |
| **Independencia** | $x$ e $y$ no dependen una de la otra, sino de $t$. |
| **Dirección** | Al aumentar $t$, la curva tiene un sentido de recorrido (flechas). |
| **Velocidad** | Podemos analizar qué tan rápido se dibuja la curva. |

> **Conclusión:** Las paramétricas son el cine de las matemáticas. Convierten una foto estática en una película con movimiento.

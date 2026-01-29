# **Ecuaciones Literales**

Hasta ahora, $x$ era la única letra en un mar de números. Pero en física, ingeniería y economía, las ecuaciones suelen ser pura "sopa de letras". Aquí aprenderás a tratar a las letras $a, b, c$ como si fueran números comunes para despejar la incógnita que te interesa.

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar cuál es la verdadera incógnita y cuáles son constantes.
- El proceso de despeje cuando todo son letras.
- Resolución de ecuaciones con parámetros en ambos lados.
- Manejo de restricciones (división por cero con letras).

---

## 🔡 Constantes Disfrazadas

En una ecuación como $ax + b = c$, asumimos que:
- **$x$** es la variable que cambia.
- **$a, b, c$** son parámetros fijos (números disfrazados).

El objetivo es dejar la $x$ sola, moviendo todo lo demás al otro lado, igual que si fueran números.

---

## ⚙️ Ejemplos Resueltos: Básicos

### Ejemplo 1
Despejar $x$ en $ax = b$.

**Razonamiento:**
La $a$ está multiplicando. Pasa dividiendo.

$$
x = \frac{b}{a}
$$

*(Nota: Esto solo es válido si $a \neq 0$)*.

### Ejemplo 2
Despejar $x$ en $x + a = b$.

**Razonamiento:**
La $a$ está sumando. Pasa restando.

$$
x = b - a
$$

### Ejemplo 3
Despejar $x$ en $ax + b = c$.

**Paso 1:** Restamos $b$.
$$
ax = c - b
$$

**Paso 2:** Dividimos por $a$.
$$
x = \frac{c - b}{a}
$$

### Ejemplo 4
Despejar $x$ en $ax - b = cx + d$.

**Paso 1 (Agrupar):** Llevamos las $x$ a la izquierda.
$$
ax - cx = d + b
$$

**Paso 2 (Factorizar):** Sacamos factor común $x$.
$$
x(a - c) = d + b
$$

**Paso 3 (Despejar):** El paréntesis pasa dividiendo.
$$
x = \frac{d + b}{a - c}
$$

### Ejemplo 5
Despejar $y$ en $my + n = py - q$.

**Paso 1:** Agrupar $y$.
$$
my - py = -q - n
$$

**Paso 2:** Factorizar $y$.
$$
y(m - p) = -q - n
$$

**Paso 3:** Despejar.
$$
y = \frac{-q - n}{m - p}
$$

Se puede escribir más elegante multiplicando por $-1$ arriba y abajo:
$$
\boxed{y = \frac{q + n}{p - m}}
$$

---

## ⚙️ Ejemplos Resueltos: Avanzados

### Ejemplo 6
Despejar $x$ en $a(x + b) = c$.

**Paso 1:** Distribuir.
$$
ax + ab = c
$$

**Paso 2:** Mover $ab$.
$$
ax = c - ab
$$

**Paso 3:** Dividir por $a$.
$$
x = \frac{c - ab}{a}
$$

### Ejemplo 7: Cinemática
Despejar $t$ en $v = v_0 + at$.

$$
v - v_0 = at \implies t = \frac{v - v_0}{a}
$$

### Ejemplo 8: Fracciones
Despejar $x$ en $\frac{x}{a} + \frac{x}{b} = 1$.

**Paso 1:** Factorizar $x$.
$$
x \left( \frac{1}{a} + \frac{1}{b} \right) = 1
$$

**Paso 2:** Sumar las fracciones del paréntesis.
$$
x \left( \frac{b + a}{ab} \right) = 1
$$

**Paso 3:** Despejar (multiplicar por el inverso).
$$
x = \frac{ab}{a + b}
$$

### Ejemplo 9: Proporción
Despejar $x$ en $\frac{x - a}{b} = \frac{x - b}{a}$.

**Paso 1:** Cruzar denominadores.
$$
a(x - a) = b(x - b)
$$

**Paso 2:** Expandir.
$$
ax - a^2 = bx - b^2
$$

**Paso 3:** Agrupar $x$.
$$
ax - bx = a^2 - b^2
$$

**Paso 4:** Factorizar ambos lados (diferencia de cuadrados a la derecha).
$$
x(a - b) = (a - b)(a + b)
$$

**Paso 5:** Dividir.
$$
x = a + b
$$

### Ejemplo 10: Interés
Despejar $r$ en $A = P(1 + rt)$.

$$
A = P + Prt
$$
$$
A - P = Prt
$$
$$
r = \frac{A - P}{Pt}
$$

### Ejemplo 11: Restricciones
Despejar $x$ en $ax = bx + c$.

$$
ax - bx = c \implies x(a - b) = c \implies x = \frac{c}{a - b}
$$

**Restricción:** $a \neq b$ (para no dividir por cero).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Despeja $x$ en $bx = a$.

<details>
<summary>Ver solución</summary>

$$
x = \frac{a}{b}
$$
</details>

---

### Ejercicio 2
Despeja $x$ en $ax + c = d$.

<details>
<summary>Ver solución</summary>

$$
x = \frac{d - c}{a}
$$
</details>

---

### Ejercicio 3
Despeja $x$ en $mx = nx + p$.

<details>
<summary>Ver solución</summary>

$$
mx - nx = p \implies x(m-n) = p \implies x = \frac{p}{m-n}
$$
</details>

---

### Ejercicio 4
Despeja $w$ en $P = 2l + 2w$.

<details>
<summary>Ver solución</summary>

$$
2w = P - 2l \implies w = \frac{P - 2l}{2}
$$
</details>

---

### Ejercicio 5
Despeja $x$ en $\frac{x}{a} = \frac{b}{c}$.

<details>
<summary>Ver solución</summary>

$$
x = \frac{ab}{c}
$$
</details>

---

### Ejercicio 6
Despeja $h$ en $V = \frac{1}{3}\pi r^2 h$.

<details>
<summary>Ver solución</summary>

$$
3V = \pi r^2 h \implies h = \frac{3V}{\pi r^2}
$$
</details>

---

### Ejercicio 7
Despeja $y$ en $x + y = z$.

<details>
<summary>Ver solución</summary>

$$
y = z - x
$$
</details>

---

### Ejercicio 8
Despeja $a$ en $F = ma$.

<details>
<summary>Ver solución</summary>

$$
a = \frac{F}{m}
$$
</details>

---

### Ejercicio 9
Despeja $x$ en $ax - b = 0$.

<details>
<summary>Ver solución</summary>

$$
x = \frac{b}{a}
$$
</details>

---

### Ejercicio 10
Despeja $m$ en $y = mx + b$.

<details>
<summary>Ver solución</summary>

$$
y - b = mx \implies m = \frac{y-b}{x}
$$
</details>

---

## 🔑 Resumen

| Situación | Acción |
|:--- |:--- |
| **Suma ($+a$)** | Pasa como $-a$. |
| **Multiplicación ($a \cdot x$)** | Pasa como denominador $/a$. |
| **Dos términos con $x$ ($ax + bx$)** | Se factoriza $x(a+b)$ y el paréntesis pasa dividiendo. |

> **Conclusión:** Las letras no muerden. Trátalas con las mismas reglas que a los números y verás que el álgebra es el mismo juego, solo que con piezas más genéricas.

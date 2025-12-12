# 🔢 Sistemas 3×3 - Introducción

En esta lección introduciremos los sistemas de ecuaciones lineales con tres incógnitas.

---

## 📖 Sistema de 3×3

Un sistema de tres ecuaciones con tres incógnitas tiene la forma:

$$
\begin{cases}
a_1x + b_1y + c_1z = d_1 \\
a_2x + b_2y + c_2z = d_2 \\
a_3x + b_3y + c_3z = d_3
\end{cases}
$$

**Resolver** el sistema significa encontrar los valores de $x$, $y$ y $z$ que satisfacen las tres ecuaciones simultáneamente.

---

## 📖 Interpretación geométrica

- Cada ecuación representa un **plano** en el espacio 3D
- La solución es el **punto** donde se intersectan los tres planos
- Pueden haber uno, ninguno o infinitos puntos de intersección

---

## 📖 Método de reducción para 3×3

1. Usar dos ecuaciones para eliminar una variable
2. Usar otras dos ecuaciones para eliminar la misma variable
3. Obtener un sistema 2×2
4. Resolver el sistema 2×2
5. Sustituir para encontrar la tercera variable

---

## 📖 Ejemplo completo

### Ejemplo 1

Resolver:
$$
\begin{cases}
x + y + z = 6 \\
2x - y + z = 3 \\
x + 2y - z = 1
\end{cases}
$$

**Paso 1:** Eliminamos $z$ de las ecuaciones (1) y (2):
$$
(1) + (2): 3x + 2z = 9 \quad \text{Error, mejor sumamos (1) y (3)}
$$

Sumamos (1) y (3):
$$
(x + y + z) + (x + 2y - z) = 6 + 1
$$
$$
2x + 3y = 7 \quad \text{... (A)}
$$

Sumamos (2) y (3):
$$
(2x - y + z) + (x + 2y - z) = 3 + 1
$$
$$
3x + y = 4 \quad \text{... (B)}
$$

**Paso 2:** Resolvemos el sistema 2×2 con (A) y (B):

De (B): $y = 4 - 3x$

Sustituimos en (A):
$$
2x + 3(4 - 3x) = 7
$$
$$
2x + 12 - 9x = 7
$$
$$
-7x = -5
$$
$$
x = \frac{5}{7}
$$

$$
y = 4 - 3 \cdot \frac{5}{7} = \frac{28 - 15}{7} = \frac{13}{7}
$$

**Paso 3:** Encontramos $z$ usando la ecuación (1):
$$
\frac{5}{7} + \frac{13}{7} + z = 6
$$
$$
z = 6 - \frac{18}{7} = \frac{42 - 18}{7} = \frac{24}{7}
$$

$$
\boxed{x = \frac{5}{7}, \quad y = \frac{13}{7}, \quad z = \frac{24}{7}}
$$

---

### Ejemplo 2 (Sistema más simple)

Resolver:
$$
\begin{cases}
x + y + z = 6 \\
x - y + z = 2 \\
x + y - z = 0
\end{cases}
$$

**Sumando (1) y (2):**
$$
2x + 2z = 8 \quad \Rightarrow \quad x + z = 4 \quad \text{...(A)}
$$

**Sumando (1) y (3):**
$$
2x + 2y = 6 \quad \Rightarrow \quad x + y = 3 \quad \text{...(B)}
$$

**Sumando (2) y (3):**
$$
2x = 2 \quad \Rightarrow \quad x = 1
$$

**Sustituyendo:**
- De (B): $1 + y = 3$, $y = 2$
- De (A): $1 + z = 4$, $z = 3$

$$
\boxed{x = 1, \quad y = 2, \quad z = 3}
$$

---

### Ejemplo 3

Resolver:
$$
\begin{cases}
2x + y - z = 3 \\
x - 2y + z = 1 \\
3x + y + 2z = 8
\end{cases}
$$

**Sumamos (1) y (2):**
$$
3x - y = 4 \quad \text{...(A)}
$$

**De (1) × 2 + (3):**
$$
4x + 2y - 2z = 6
$$
$$
3x + y + 2z = 8
$$
$$
7x + 3y = 14 \quad \text{...(B)}
$$

**De (A): $y = 3x - 4$. Sustituimos en (B):**
$$
7x + 3(3x - 4) = 14
$$
$$
16x - 12 = 14
$$
$$
x = \frac{26}{16} = \frac{13}{8}
$$

$$
y = 3 \cdot \frac{13}{8} - 4 = \frac{39 - 32}{8} = \frac{7}{8}
$$

**De ecuación (2):**
$$
\frac{13}{8} - 2 \cdot \frac{7}{8} + z = 1
$$
$$
\frac{13 - 14}{8} + z = 1
$$
$$
z = 1 + \frac{1}{8} = \frac{9}{8}
$$

$$
\boxed{x = \frac{13}{8}, \quad y = \frac{7}{8}, \quad z = \frac{9}{8}}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve: $\begin{cases} x + y + z = 10 \\ x - y = 2 \\ y + z = 7 \end{cases}$

<details>
<summary>Ver solución</summary>

De (2): $x = y + 2$

De (3): $z = 7 - y$

Sustituyendo en (1): $(y + 2) + y + (7 - y) = 10$

$y + 9 = 10$, $y = 1$

$x = 3$, $z = 6$

</details>

---

**Ejercicio 2:** Resuelve: $\begin{cases} 2x + y + z = 9 \\ x - y + z = 4 \\ x + y - z = 2 \end{cases}$

<details>
<summary>Ver solución</summary>

(1)+(2): $3x + 2z = 13$

(2)+(3): $2x = 6$, $x = 3$

$z = 2$, $y = 1$

</details>

---

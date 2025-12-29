# **Propiedades de las Potencias (I)**

Imagina que estás multiplicando bacterias en un laboratorio. Cada hora se duplican. Si comienzas con $2^5$ bacterias y luego las multiplicas por otro grupo de $2^3$, ¿cómo calculas rápidamente el total? No necesitas hacer la cuenta larga cada vez. Las matemáticas tienen "atajos" llamados propiedades que nos permiten operar con exponentes rápidamente.

---

## 🎯 ¿Qué vas a aprender?

- El comportamiento de las potencias cuando se multiplican (Producto de bases iguales).
- Qué sucede cuando se dividen (Cociente de bases iguales).
- La demostración visual de por qué "sumamos" o "restamos" los exponentes.
- Cómo manejar exponentes negativos en medio de estas operaciones.

---

## 🔍 Reglas de Juego para la Misma Base

Estas reglas **SOLO** funcionan si la base es idéntica (ej. $x$ con $x$, $2$ con $2$). Si tienes $x^2 \cdot y^3$, ¡no inventes reglas!

### 1. Producto (Multiplicación)

Si multiplicas bases iguales, los exponentes se **SUMAN**.

$$
a^m \cdot a^n = a^{m+n}
$$

### 2. Cociente (División)

Si divides bases iguales, los exponentes se **RESTAN** (el de arriba menos el de abajo).

$$
\frac{a^m}{a^n} = a^{m-n}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Multiplicación básica

Simplifica $x^3 \cdot x^4$.

**Datos:**
- Misma base: $x$.
- Exponentes: 3 y 4.
- Operación: Multiplicación → Suma.

**Razonamiento:**

$$
x^3 \cdot x^4 = (x \cdot x \cdot x) \cdot (x \cdot x \cdot x \cdot x)
$$

En total hay 7 equis multiplicándose.

$$
= x^{3+4}
$$

$$
= x^7
$$

**Resultado:** $\boxed{x^7}$

---

### Ejemplo 2: División básica

Simplifica $\dfrac{y^8}{y^3}$.

**Datos:**
- Operación: División → Resta.

**Razonamiento:**

$$
y^{8-3}
$$

$$
= y^5
$$

(Cancelamos $y^3$ arriba con $y^3$ abajo).

**Resultado:** $\boxed{y^5}$

---

### Ejemplo 3: Multiplicación con negativos

Simplifica $a^{-5} \cdot a^2$.

**Datos:**
- Sumar exponentes con distintos signos.

**Razonamiento:**

$$
a^{-5 + 2}
$$

Debo 5 y pago 2, quedo debiendo 3.

$$
= a^{-3}
$$

Para dejarlo elegante (con exponente positivo):

$$
= \frac{1}{a^3}
$$

**Resultado:** $\boxed{\frac{1}{a^3}}$

---

### Ejemplo 4: El "sándwich" de potencias

Simplifica $\dfrac{x^5 \cdot x^2}{x^4}$.

**Datos:**
- Combinación de multiplicar (arriba) y dividir.

**Razonamiento:**

1. **Arriba:**

$$
x^5 \cdot x^2 = x^{5+2} = x^7
$$

2. **División:**

$$
\frac{x^7}{x^4}
$$

3. **Resta:**

$$
x^{7-4} = x^3
$$

**Resultado:** $\boxed{x^3}$

---

### Ejemplo 5: División "trampa" (Resta de negativos)

Simplifica $\dfrac{m^2}{m^{-3}}$.

**Datos:**
- El exponente de abajo es negativo.
- La regla dice: Restar el de abajo.

**Razonamiento:**

$$
m^{2 - (-3)}
$$

Menos por menos es más ('El enemigo de mi enemigo es mi amigo').

$$
m^{2 + 3}
$$

$$
= m^5
$$

**Resultado:** $\boxed{m^5}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $x^5 \cdot x^5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
5 + 5 = 10
$$

**Resultado:** $\boxed{x^{10}}$

</details>

### Ejercicio 2
Simplifica $\dfrac{a^{10}}{a^2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
10 - 2 = 8
$$

**Resultado:** $\boxed{a^8}$

</details>

### Ejercicio 3
Simplifica $2^3 \cdot 2^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
2^{3+2} = 2^5 = 32
$$

**Resultado:** $\boxed{32}$

</details>

### Ejercicio 4
Simplifica $y \cdot y^6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

La primera y tiene un 1 invisible.

$$
1 + 6 = 7
$$

**Resultado:** $\boxed{y^7}$

</details>

### Ejercicio 5
Simplifica $\dfrac{x^5}{x^5}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
5 - 5 = 0
$$

Todo $x^0 = 1$.

**Resultado:** $\boxed{1}$

</details>

### Ejercicio 6
Simplifica $b^{-2} \cdot b^{-3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
-2 + (-3) = -5
$$

**Resultado:** $\boxed{\frac{1}{b^5}}$

</details>

### Ejercicio 7
Simplifica $\dfrac{x^3}{x^{-2}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
3 - (-2) = 3 + 2 = 5
$$

**Resultado:** $\boxed{x^5}$

</details>

### Ejercicio 8
Simplifica $a^3 \cdot a^2 \cdot a^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
3 + 2 + 4 = 9
$$

**Resultado:** $\boxed{a^9}$

</details>

### Ejercicio 9
Simplifica $\dfrac{10^7}{10^4}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
10^{7-4} = 10^3 = 1000
$$

**Resultado:** $\boxed{1000}$

</details>

### Ejercicio 10
Simplifica $\dfrac{x^2 \cdot x^4}{x^3 \cdot x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Numerador:

$$
x^6
$$

Denominador:

$$
x^3 \cdot x^1 = x^4
$$

División:

$$
6 - 4 = 2
$$

**Resultado:** $\boxed{x^2}$

</details>

---

## 🔑 Resumen

| Operación | Clave | Ejemplo |
| :--- | :--- | :--- |
| **Multiplicación** ($\cdot$) | **Suma** exponentes | $x^2 \cdot x^3 = x^5$ |
| **División** ($\div$) | **Resta** exponentes | $x^5 / x^2 = x^3$ |

> Recuerda: La base se queda quieta, ¡solo se mueven los exponentes!

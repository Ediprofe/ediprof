# **Propiedades de las Potencias (II)**

¿Qué pasa si tienes una potencia que ya está elevada y la vuelves a elevar? Es como una muñeca rusa *matrioska*: una dentro de otra. En esta lección aprenderemos cómo simplificar estas "torres de potencias" y qué hacer cuando un exponente afecta a todo un grupo de números multiplicándose.

---

## 🎯 ¿Qué vas a aprender?

- La regla de "Potencia de una potencia" (Multiplicar exponentes).
- La regla de "Potencia de un producto" (Distribuir el exponente).
- Cómo diferenciar $(x^2)^3$ de $x^2 \cdot x^3$.
- A expandir expresiones algebraicas como $(3x^2y)^3$ en un solo paso.

---

## 🔍 Reglas de "Elevación"

### 1. Potencia de una Potencia

Si elevas una potencia a otro exponente, los exponentes se **MULTIPLICAN**.

$$
(a^n)^m = a^{n \cdot m}
$$

> Piénsalo así: Si tienes 3 bolsas, y en cada bolsa hay 2 gatos, en total tienes $3 \times 2 = 6$ gatos.

### 2. Potencia de un Producto

El exponente afecta a **cada uno** de los factores dentro del paréntesis. "El sol sale para todos".

$$
(a \cdot b)^n = a^n \cdot b^n
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Potencia de potencia simple

Simplifica $(x^3)^4$.

**Datos:**
- Base: $x$.
- Exponentes anidados: 3 y 4.
- Operación: Multiplicación.

**Razonamiento:**

$$
(x^3)^4 = x^{3 \cdot 4}
$$

$$
= x^{12}
$$

Demostración: $(x^3) \cdot (x^3) \cdot (x^3) \cdot (x^3) = x^{3+3+3+3} = x^{12}$.

**Resultado:** $\boxed{x^{12}}$

---

### Ejemplo 2: Distribuir exponente

Simplifica $(2x)^3$.

**Datos:**
- El 3 afecta al 2 **Y** a la $x$.

**Razonamiento:**

$$
2^3 \cdot x^3
$$

$$
= 8 \cdot x^3
$$

$$
= 8x^3
$$

¡Error común! Muchos escriben $2x^3$. El 2 también se eleva.

**Resultado:** $\boxed{8x^3}$

---

### Ejemplo 3: Combinando ambas

Simplifica $(3a^2)^2$.

**Datos:**
- Coeficiente 3.
- Potencia $a^2$.
- Todo elevado a la 2.

**Razonamiento:**

1. Elevamos el número:

$$
3^2 = 9
$$

2. Elevamos la letra:

$$
(a^2)^2 = a^{2 \cdot 2} = a^4
$$

3. Juntamos:

$$
9a^4
$$

**Resultado:** $\boxed{9a^4}$

---

### Ejemplo 4: Con exponentes negativos

Simplifica $(y^{-2})^3$.

**Datos:**
- Multiplicamos -2 por 3.

**Razonamiento:**

$$
y^{-2 \cdot 3}
$$

$$
= y^{-6}
$$

Forma positiva:

$$
= \frac{1}{y^6}
$$

**Resultado:** $\boxed{\frac{1}{y^6}}$

---

### Ejemplo 5: Expresión compleja

Simplifica $(-2x^3y^4)^3$.

**Datos:**
- Base negativa.
- Exponente impar (3).
- Variables con exponentes.

**Razonamiento:**

1. **Signo:** Base negativa, exponente impar → Negativo.

2. **Número:**

$$
2^3 = 8
$$

3. **Variable x:**

$$
(x^3)^3 = x^9
$$

4. **Variable y:**

$$
(y^4)^3 = y^{12}
$$

5. **Juntamos:**

$$
-8x^9y^{12}
$$

**Resultado:** $\boxed{-8x^9y^{12}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $(a^2)^5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
2 \cdot 5 = 10
$$

**Resultado:** $\boxed{a^{10}}$

</details>

### Ejercicio 2
Simplifica $(xy)^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Distribuimos el 4.

$$
x^4y^4
$$

**Resultado:** $\boxed{x^4y^4}$

</details>

### Ejercicio 3
Simplifica $(3x)^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
3^2 \cdot x^2 = 9x^2
$$

**Resultado:** $\boxed{9x^2}$

</details>

### Ejercicio 4
Simplifica $(b^3)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
3 \cdot 3 = 9
$$

**Resultado:** $\boxed{b^9}$

</details>

### Ejercicio 5
Simplifica $(2a^2b)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
2^3 \cdot (a^2)^3 \cdot b^3
$$

$$
= 8a^6b^3
$$

**Resultado:** $\boxed{8a^6b^3}$

</details>

### Ejercicio 6
Simplifica $(x^{-1})^{-1}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
-1 \cdot -1 = 1
$$

$$
x^1 = x
$$

**Resultado:** $\boxed{x}$

</details>

### Ejercicio 7
Simplifica $(-x^2)^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Base negativa al cuadrado → Positivo.

$$
(x^2)^2 = x^4
$$

**Resultado:** $\boxed{x^4}$

</details>

### Ejercicio 8
Simplifica $(10^2)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
10^6 = 1,000,000
$$

**Resultado:** $\boxed{1,000,000}$

</details>

### Ejercicio 9
Simplifica $\left(\dfrac{x}{y}\right)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Distribuimos arriba y abajo.

$$
\frac{x^3}{y^3}
$$

**Resultado:** $\boxed{\frac{x^3}{y^3}}$

</details>

### Ejercicio 10
Simplifica $(4x^0)^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
x^0 = 1
$$

$$
(4 \cdot 1)^2 = 4^2 = 16
$$

**Resultado:** $\boxed{16}$

</details>

---

## 🔑 Resumen

| Situación | Acción | Ejemplo |
| :--- | :--- | :--- |
| **Potencia de Potencia** | **Multiplicar** exponentes | $(x^2)^3 = x^6$ |
| **Potencia de Producto** | **Distribuir** exponente | $(xy)^2 = x^2y^2$ |

> Recuerda: Los paréntesis son sagrados. Si el exponente está afuera, afecta a TODO lo que está adentro.

---
title: "Combinación de Operaciones"
---

# **Combinación de Operaciones**

En el mundo real, los problemas no vienen etiquetados como "solo suma" o "solo multiplicación". ¡Vienen todos juntos! En esta lección aprenderemos a ser los directores de orquesta que ponen orden en el caos de las operaciones combinadas, respetando la jerarquía para llegar al resultado correcto.

---

## 🎯 ¿Qué vas a aprender?

- La jerarquía de operaciones (PEMDAS) aplicada a fracciones.
- Cómo manejar signos de agrupación (paréntesis, corchetes).
- Estrategias para no perder el hilo en ejercicios largos.
- Cómo simplificar expresiones complejas paso a paso.

---

## 🔍 La Jerarquía Sagrada

Si no respetas este orden, el resultado será incorrecto. ¡Tatúalo en tu mente!

1.  **Paréntesis:** Resuelve primero lo que está dentro de signos de agrupación.
2.  **Multiplicación y División:** De izquierda a derecha.
3.  **Suma y Resta:** Al final, de izquierda a derecha.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Multiplicación y División

Calcula: $\dfrac{4a^2}{3b} \cdot \dfrac{5b^2}{2a} \div \dfrac{10ab}{9}$

**Datos:**
- Tres fracciones. Multiplicación y División.

**Razonamiento:**

1. **De izquierda a derecha**. Primero la multiplicación:

$$
\frac{4a^2}{3b} \cdot \frac{5b^2}{2a} = \frac{20a^2b^2}{6ab} = \frac{10ab}{3}
$$

2. Ahora la división (invertimos la segunda):

$$
\frac{10ab}{3} \cdot \frac{9}{10ab}
$$

3. **Cancelamos:**
   - $10ab$ con $10ab$.
   - $9/3 = 3$.

**Resultado:** $\boxed{3}$

---

### Ejemplo 2: Suma con Paréntesis y Multiplicación

Calcula: $\left( \dfrac{1}{x} + \dfrac{1}{y} \right) \cdot \dfrac{xy}{x+y}$

**Datos:**
- Primero el paréntesis.

**Razonamiento:**

1. **Paréntesis:** Sumamos $\frac{1}{x} + \frac{1}{y}$ con MCM $xy$: 

$$
\frac{y + x}{xy}
$$

2. **Multiplicación:** Ahora operamos con el término de fuera: 

$$
\frac{x+y}{xy} \cdot \frac{xy}{x+y}
$$

3. **Simplificación:**
   - $(x+y)$ con $(x+y)$.
   - $xy$ con $xy$.
   - Todo se cancela $\to 1$.

**Resultado:** $\boxed{1}$

---

### Ejemplo 3: División y Resta (¡Cuidado con el orden!)

Calcula: $\dfrac{x^2-1}{x} \div \dfrac{x+1}{2} - \dfrac{x-2}{x}$

**Datos:**
- Primero la división, luego la resta.

**Razonamiento:**

1. **División:**

$$
\frac{(x+1)(x-1)}{x} \cdot \frac{2}{x+1}
$$

Cancelamos $(x+1) \to \frac{2(x-1)}{x} = \frac{2x-2}{x}$.

2. **Sustitución y Resta:**

$$
\frac{2x-2}{x} - \frac{x-2}{x}
$$

3. **Operamos:**

$$
\frac{(2x-2) - (x-2)}{x} = \frac{2x-2-x+2}{x}
$$

4. Reducimos:

$$
\frac{x}{x} = 1
$$

**Resultado:** $\boxed{1}$

---

### Ejemplo 4: Suma, Resta y Paréntesis anidados

Calcula: $\left( \dfrac{x+1}{x-1} - \dfrac{x-1}{x+1} \right) \div \dfrac{4x}{x+1}$

**Datos:**
- Paréntesis con denominadores diferentes.

**Razonamiento:**

1. **Paréntesis (Resta):** MCM es $(x-1)(x+1)$: 

$$
\frac{(x+1)^2 - (x-1)^2}{(x-1)(x+1)}
$$

2. Expandimos los cuadrados:

$$
\frac{(x^2+2x+1) - (x^2-2x+1)}{(x-1)(x+1)}
$$

$$
\frac{4x}{(x-1)(x+1)}
$$

3. **División:**

$$
\frac{4x}{(x-1)(x+1)} \cdot \frac{x+1}{4x}
$$

4. **Cancelación:**
   - $4x$ con $4x$.
   - $(x+1)$ con $(x+1)$.
   - Queda $\frac{1}{x-1}$.

**Resultado:** $\boxed{\frac{1}{x-1}}$

---

### Ejemplo 5: El "Castillo" de Fracciones

Calcula: $\dfrac{1 - \frac{1}{x}}{1 + \frac{1}{x}}$

**Datos:**
- Operaciones en numerador y denominador por separado.

**Razonamiento:**

1. **Numerador:** $1 - \frac{1}{x} = \frac{x-1}{x}$.

2. **Denominador:** $1 + \frac{1}{x} = \frac{x+1}{x}$.

3. **División:**

$$
\frac{x-1}{x} \div \frac{x+1}{x}
$$

$$
\frac{x-1}{x} \cdot \frac{x}{x+1}
$$

4. Cancelamos $x$.

**Resultado:** $\boxed{\frac{x-1}{x+1}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\dfrac{2}{3} \cdot \dfrac{3}{4} + \dfrac{1}{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Mult: $6/12 = 1/2$. 

Suma: 

$$
1/2 + 1/2 = 1
$$

**Resultado:** $\boxed{1}$

</details>

### Ejercicio 2
Calcula $\dfrac{1}{x} \div \dfrac{1}{x^2} - x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Div: $x$. 

Resta: 

$$
x - x = 0
$$

**Resultado:** $\boxed{0}$

</details>

### Ejercicio 3
Calcula $\left(\dfrac{a}{b} + \dfrac{b}{a}\right) \cdot ab$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\left(\frac{a^2+b^2}{ab}\right) \cdot ab = a^2+b^2
$$

**Resultado:** $\boxed{a^2+b^2}$

</details>

### Ejercicio 4
Calcula $\dfrac{x-2}{x} \cdot \dfrac{x}{x^2-4} + \dfrac{1}{x+2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Mult: $\frac{1}{x+2}$.

Suma: 

$$
\frac{1}{x+2} + \frac{1}{x+2} = \frac{2}{x+2}
$$

**Resultado:** $\boxed{\frac{2}{x+2}}$

</details>

### Ejercicio 5
Calcula $\left(1 + \dfrac{1}{x}\right) \div (x+1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{x+1}{x} \cdot \frac{1}{x+1} = \frac{1}{x}
$$

**Resultado:** $\boxed{\frac{1}{x}}$

</details>

### Ejercicio 6
Calcula $\dfrac{a}{a+1} \div \dfrac{a^2}{a^2-1} \cdot a$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Div: 

$$
\frac{a}{a+1} \cdot \frac{(a+1)(a-1)}{a^2} = \frac{a-1}{a}
$$

Mult: 

$$
\frac{a-1}{a} \cdot a = a-1
$$

**Resultado:** $\boxed{a-1}$

</details>

### Ejercicio 7
Calcula $\dfrac{x^2}{y^2} \cdot \dfrac{y}{x} \div \dfrac{x}{y}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Mult: $\frac{x}{y}$.

Div: 

$$
\frac{x}{y} \cdot \frac{y}{x} = 1
$$

**Resultado:** $\boxed{1}$

</details>

### Ejercicio 8
Calcula $\left(\dfrac{1}{a} - \dfrac{1}{b}\right) \div \dfrac{b-a}{ab}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Paréntesis: 

$$
\frac{b-a}{ab}
$$

Div: Una cosa entre la misma cosa = 1.

**Resultado:** $\boxed{1}$

</details>

### Ejercicio 9
Calcula $\dfrac{3}{x+1} - \dfrac{2}{x+1} \cdot \dfrac{x+1}{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Primero Mult: 

$$
\frac{2}{x+1} \cdot \frac{x+1}{2} = 1
$$

Resta: 

$$
\frac{3}{x+1} - 1 = \frac{3 - (x+1)}{x+1} = \frac{2-x}{x+1}
$$

**Resultado:** $\boxed{\frac{2-x}{x+1}}$

</details>

### Ejercicio 10
Calcula $\dfrac{x+1}{x} \cdot \left( x - \dfrac{x^2}{x+1} \right)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Paréntesis: 

$$
\frac{x(x+1) - x^2}{x+1} = \frac{x}{x+1}
$$

Mult: 

$$
\frac{x+1}{x} \cdot \frac{x}{x+1} = 1
$$

**Resultado:** $\boxed{1}$

</details>

---

## 🔑 Resumen

| Prioridad | Operación |
| :--- | :--- |
| **1** | **(  )** Paréntesis y agrupaciones |
| **2** | **$\times$ y $\div$** De izquierda a derecha |
| **3** | **$+$ y $-$** De izquierda a derecha |

> El orden lo es todo: altera el orden y alterarás el resultado. ¡Siempre respeta la jerarquía!

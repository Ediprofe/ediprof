# **Diferencia de Cuadrados**

Este es uno de los casos más sencillos de factorización. Cuando tienes una **resta de dos cuadrados perfectos**, siempre se puede escribir como el producto de una suma por una resta.

---

## 🎯 ¿Qué vas a aprender?

- A reconocer cuadrados perfectos en números y variables.
- A aplicar la fórmula para factorizar una diferencia de cuadrados.
- Por qué este método no funciona con la suma de cuadrados.
- A factorizar sucesivamente cuando hay exponentes altos.

---

## 🔍 ¿Qué es una Diferencia de Cuadrados?

Para usar este método, la expresión debe cumplir tres condiciones estrictas:
1.  Tener **exactamente dos términos**.
2.  Que los términos se estén **restando** (por eso se llama diferencia).
3.  Que a ambos términos se les pueda sacar una **raíz cuadrada exacta**.

### **Ejemplo: El patrón de la resta**

Observa: $x^2 - 16$
- ¿Es una resta? Sí.
- ¿$x^2$ tiene raíz? Sí, es $x$.
- ¿16 tiene raíz? Sí, es 4.

**La Regla:** Escribe dos paréntesis con esas raíces, uno con $+$ y otro con $-$.

**Resultado:** $\boxed{(x + 4)(x - 4)}$

---

## 📐 La Regla General

Si tienes dos cuadrados restándose, su factorización siempre será:

$$
\boxed{a^2 - b^2 = (a + b)(a - b)}
$$

> **En palabras:** Saca la raíz de cada uno y ponlas a sumar y a restar en dos paréntesis.

---

## ⚠️ ¡Cuidado con la Suma!

Un error muy común es intentar factorizar $x^2 + 25$ como $(x+5)(x-5)$. 
**¡Esto es imposible!** Si multiplicas $(x+5)(x-5)$ el resultado es una resta ($x^2-25$). La suma de cuadrados no se puede factorizar con este método.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Con coeficientes

Factoriza: $9a^2 - 25$

**Razonamiento:**

1. Raíz de $9a^2$: 

$$
\sqrt{9} = 3 \quad \text{y} \quad \sqrt{a^2} = a
$$

Raíz total = $3a$.

2. Raíz de $25$: 

$$
\sqrt{25} = 5
$$

3. Aplicamos la regla: un paréntesis suma y otro resta.

**Resultado:** $\boxed{(3a + 5)(3a - 5)}$

---

### Ejemplo 2: Doble factorización

Factoriza completamente: $x^4 - 1$

**Razonamiento:**

1. Primera vuelta: Las raíces son $x^2$ y $1$. 

Resultado: 

$$
(x^2 + 1)(x^2 - 1)
$$

2. Analizamos: El bloque $(x^2 - 1)$ ¡vuelve a ser una diferencia de cuadrados!

3. Segunda vuelta: $(x^2 - 1)$ se convierte en:

$$
(x + 1)(x - 1)
$$

4. El bloque $(x^2 + 1)$ se queda igual porque es una suma.

**Resultado:** $\boxed{(x^2 + 1)(x + 1)(x - 1)}$

---

### Ejemplo 3: Varias variables mezcladas

Factoriza: $100a^2 - 49b^2c^4$

**Razonamiento:**

1. Raíz de $100a^2$: 

$$
\sqrt{100}=10 \quad \text{y} \quad \sqrt{a^2}=a
$$

Raíz total: $10a$.

2. Raíz de $49b^2c^4$: 

$$
\sqrt{49}=7, \quad \sqrt{b^2}=b, \quad \sqrt{c^4}=c^2
$$

Raíz total: $7bc^2$.

3. Aplicamos la regla: 

$$
(10a + 7bc^2)(10a - 7bc^2)
$$

**Resultado:** $\boxed{(10a + 7bc^2)(10a - 7bc^2)}$

---

### Ejemplo 4: Exponentes altos y factor común

Factoriza: $2x^3 - 50x$

**Razonamiento:**

1. **Paso 1:** Notamos que hay un factor común $2x$. Lo extraemos: 

$$
2x(x^2 - 25)
$$

2. **Paso 2:** El bloque $(x^2 - 25)$ es una diferencia de cuadrados. Raíces: $x$ y $5$.

3. Escribimos todo junto: 

$$
2x(x+5)(x-5)
$$

**Resultado:** $\boxed{2x(x + 5)(x - 5)}$

---

### Ejemplo 5: Con fracciones complejas

Factoriza: $\frac{1}{64} - \frac{y^2}{49}$

**Razonamiento:**

1. Raíz del primer término: 

$$
\sqrt{1/64} = 1/8
$$

2. Raíz del segundo término: 

$$
\sqrt{y^2/49} = y/7
$$

3. Aplicamos binomios conjugados.

**Resultado:** $\boxed{(\frac{1}{8} + \frac{y}{7})(\frac{1}{8} - \frac{y}{7})}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica la raíz cuadrada de $49x^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Sacamos la raíz del número y de la letra: 

$$
\sqrt{49} = 7 \quad \text{y} \quad \sqrt{x^2} = x
$$

**Resultado:** $\boxed{7x}$

</details>

### Ejercicio 2
Factoriza: $m^2 - 36$.

<details>
<summary>Ver solución</summary>

**Datos:** Raíces son $m$ y $6$.
**Razonamiento:** 

Colocamos las raíces en suma y resta:

$$
(m + 6)(m - 6)
$$

**Resultado:** $\boxed{(m + 6)(m - 6)}$

</details>

### Ejercicio 3
¿Se puede factorizar $a^2 + 16$ por este método?

<details>
<summary>Ver solución</summary>

**Razonamiento:** No, este método solo funciona con diferencias (restas), nunca con sumas.
**Resultado:** $\boxed{\text{No, por ser una suma}}$

</details>

### Ejercicio 4
Resuelve: $4a^2 - 81b^2$.

<details>
<summary>Ver solución</summary>

**Datos:** Raíz del primero $2a$, raíz del segundo $9b$.
**Razonamiento:** 

Aplicamos la fórmula: 

$$
(2a+9b)(2a-9b)
$$

**Resultado:** $\boxed{(2a + 9b)(2a - 9b)}$

</details>

### Ejercicio 5
Factoriza: $1 - x^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

La raíz de 1 es 1. La raíz de $x^2$ es $x$:

$$
(1 + x)(1 - x)
$$

**Resultado:** $\boxed{(1 + x)(1 - x)}$

</details>

### Ejercicio 6
Factoriza: $x^6 - y^6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Dividimos los exponentes entre 2 para hallar la raíz: 

$$
x^3, \quad y^3
$$

**Resultado:** $\boxed{(x^3 + y^3)(x^3 - y^3)}$

</details>

### Ejercicio 7
Factoriza: $\frac{x^2}{4} - 9$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Raíz de la fracción: $\frac{x}{2}$. Raíz de 9: 3.

$$
(\frac{x}{2} + 3)(\frac{x}{2} - 3)
$$

**Resultado:** $\boxed{(\frac{x}{2} + 3)(\frac{x}{2} - 3)}$

</details>

### Ejercicio 8
Factoriza: $100 - m^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Raíz de 100 es 10. Raíz de $m^4$ es $m^2$.

$$
(10 + m^2)(10 - m^2)
$$

**Resultado:** $\boxed{(10 + m^2)(10 - m^2)}$

</details>

### Ejercicio 9
Resuelve: $25x^2 - 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Raíces: $5x$ y $1$.

$$
(5x + 1)(5x - 1)
$$

**Resultado:** $\boxed{(5x + 1)(5x - 1)}$

</details>

### Ejercicio 10
Simplifica usando factorización: $\frac{x^2 - 4}{x + 2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Factorizamos arriba: 

$$
(x+2)(x-2)
$$

Tachamos el $(x+2)$ con el de abajo.

**Resultado:** $\boxed{x - 2}$

</details>

---

## 🔑 Resumen

| Identidad | Fórmula | Resultado |
| :--- | :--- | :--- |
| **Diferencia** | $a^2 - b^2$ | $(a + b)(a - b)$ |
| **Doble** | $a^4 - b^4$ | $(a^2 + b^2)(a + b)(a - b)$ |
| **Suma** | $a^2 + b^2$ | **No factorizable (en $\mathbb{R}$)** |

> La diferencia de cuadrados es el "espejo" del álgebra: lo que ves de un lado, aparece del otro con el signo contrario. ¡Es la forma más rápida de simplificar expresiones binomias!

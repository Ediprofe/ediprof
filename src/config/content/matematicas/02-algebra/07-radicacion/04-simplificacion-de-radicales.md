---
title: "Simplificación de Radicales"
---

# **Simplificación de Radicales**

Imagina que estás empacando para un viaje y solo puedes llevar maletas que pesen exactamente 20 kg. Si tienes 45 kg de ropa, tendrás que llenar 2 maletas y dejar 5 kg en casa.

Simplificar un radical es exactamente eso: sacar todo lo que se pueda "empacar" en grupos perfectos y dejar adentro solo lo que sobra.

---

## 🎯 ¿Qué vas a aprender?

- Cómo descomponer números grandes dentro de una raíz.
- La regla de "grupos de $n$" para sacar factores fuera de la raíz.
- Cómo simplificar expresiones con letras y exponentes gigantes.
- Por qué $\sqrt{18}$ es lo mismo que $3\sqrt{2}$.

---

## 🔓 Primera Propiedad: Extracción de Factores

### Formulación Formal

Sea $\sqrt[n]{a}$ un radical y $a = b^n \cdot c$ donde $b^n$ es el mayor factor perfecto de $a$ con exponente múltiplo de $n$. Entonces:

$$
\sqrt[n]{a} = \sqrt[n]{b^n \cdot c} = b \cdot \sqrt[n]{c}
$$

### ¿Por qué funciona?

Partimos de la **propiedad del producto de raíces** (que ya conoces):

$$
\sqrt[n]{x \cdot y} = \sqrt[n]{x} \cdot \sqrt[n]{y}
$$

Si $x = b^n$, entonces $\sqrt[n]{b^n} = b$, por definición de raíz. Por lo tanto:

$$
\sqrt[n]{b^n \cdot c} = \sqrt[n]{b^n} \cdot \sqrt[n]{c} = b \cdot \sqrt[n]{c}
$$

### Regla Práctica

| Índice | Grupo mínimo para salir |
|--------|------------------------|
| 2 ($\sqrt{}$) | Pares (2 factores iguales) |
| 3 ($\sqrt[3]{}$) | Tríos (3 factores iguales) |
| $n$ ($\sqrt[n]{}$) | Grupos de $n$ factores |

### Ejemplo Visual

$$
\sqrt{2 \cdot 2 \cdot 2 \cdot 2 \cdot 3} = \sqrt{(2 \cdot 2) \cdot (2 \cdot 2) \cdot 3} = \sqrt{2^2 \cdot 2^2 \cdot 3} = 2 \cdot 2 \cdot \sqrt{3} = 4\sqrt{3}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Simplificando números

Simplifica $\sqrt{72}$.

**Paso 1: Descomponer en primos**
$72 = 2 \cdot 36 = 2 \cdot 2 \cdot 18 = 2 \cdot 2 \cdot 2 \cdot 9 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3$.
O más fácil: $72 = 2^3 \cdot 3^2$.

**Paso 2: Formar grupos de 2 (porque es raíz cuadrada)**
- $2^3$ tiene una pareja de 2 ($2^2$) y sobra uno ($2^1$).
- $3^2$ es una pareja perfecta.

$$
\sqrt{2^2 \cdot 2 \cdot 3^2}
$$

**Paso 3: Sacar los grupos**
Sale un 2 y un 3. Se queda el 2 que sobró.

$$
2 \cdot 3 \sqrt{2}
$$

**Resultado:**

$$
\boxed{6\sqrt{2}}
$$

### Ejemplo 2: Simplificando letras

Simplifica $\sqrt[3]{x^7}$.

**Razonamiento:**
El índice es 3. Buscamos grupos de 3.
$x^7 = x^3 \cdot x^3 \cdot x^1$.
Salen dos grupos de $x$. Sobra una $x$.

$$
x \cdot x \sqrt[3]{x}
$$

**Resultado:**

$$
\boxed{x^2 \sqrt[3]{x}}
$$

### Ejemplo 3: Método rápido (División)

Simplifica $\sqrt[4]{a^{13}}$.

**Razonamiento:**
Dividimos exponente entre índice: $13 \div 4$.
- **Cociente (lo que sale):** 3 (porque $4 \times 3 = 12$).
- **Residuo (lo que queda):** 1 (porque $13 - 12 = 1$).

$$
a^3 \sqrt[4]{a^1}
$$

**Resultado:**

$$
\boxed{a^3 \sqrt[4]{a}}
$$

---

## � Recordatorio: Propiedades Clave

Antes de pasar a los ejercicios, recuerda estas herramientas que ya tienes en tu cinturón:

### 1. Producto de Raíces
La raíz de una multiplicación se puede separar. Esto es lo que usamos para "sacar" factores.
$$
\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b}
$$

### 2. Cociente de Raíces
La raíz de una división también se separa.
$$
\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}
$$

### 3. Exponente Fraccionario
Una raíz siempre se puede escribir como un exponente fraccionario.
$$
\sqrt[n]{a^m} = a^{\frac{m}{n}}
$$

---

## �📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $\sqrt{12}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$12 = 4 \cdot 3 = 2^2 \cdot 3$. Sale el 2.

**Resultado:**
$$
\boxed{2\sqrt{3}}
$$

</details>

### Ejercicio 2
Simplifica $\sqrt{50}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$50 = 25 \cdot 2 = 5^2 \cdot 2$. Sale el 5.

**Resultado:**
$$
\boxed{5\sqrt{2}}
$$

</details>

### Ejercicio 3
Simplifica $\sqrt{x^5}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^5 = x^4 \cdot x$. Sale $x^2$.

**Resultado:**
$$
\boxed{x^2\sqrt{x}}
$$

</details>

### Ejercicio 4
Simplifica $\sqrt[3]{16}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$16 = 2^4 = 2^3 \cdot 2$. Sale un 2.

**Resultado:**
$$
\boxed{2\sqrt[3]{2}}
$$

</details>

### Ejercicio 5
Simplifica $\sqrt{200}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$200 = 100 \cdot 2 = 10^2 \cdot 2$.

**Resultado:**
$$
\boxed{10\sqrt{2}}
$$

</details>

### Ejercicio 6
Simplifica $\sqrt[4]{x^9}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$9 \div 4 = 2$ sobra 1. Sale $x^2$, queda $x^1$.

**Resultado:**
$$
\boxed{x^2\sqrt[4]{x}}
$$

</details>

### Ejercicio 7
Simplifica $\sqrt{18x^3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$18 = 9 \cdot 2 \to 3\sqrt{2}$.
$x^3 = x^2 \cdot x \to x\sqrt{x}$.

**Resultado:**
$$
\boxed{3x\sqrt{2x}}
$$

</details>

### Ejercicio 8
Simplifica $\sqrt[3]{54}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$54 = 27 \cdot 2 = 3^3 \cdot 2$.

**Resultado:**
$$
\boxed{3\sqrt[3]{2}}
$$

</details>

### Ejercicio 9
Simplifica $\sqrt{a^2 b^5}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a^2 \to a$.
$b^5 \to b^2\sqrt{b}$.

**Resultado:**
$$
\boxed{ab^2\sqrt{b}}
$$

</details>

### Ejercicio 10
Simplifica $\sqrt{98}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$98 = 49 \cdot 2 = 7^2 \cdot 2$.

**Resultado:**
$$
\boxed{7\sqrt{2}}
$$

</details>

---

## 🔑 Resumen

| Concepto | Regla |
|----------|-------|
| **Factorizar** | Descomponer el número en primos. |
| **Agrupar** | Formar grupos del tamaño del índice. |
| **Extraer** | Cada grupo sale como un solo elemento. |
| **Residuo** | Lo que no forma grupo se queda adentro. |

> Simplificar radicales es obligatorio para poder sumar y restar expresiones algebraicas más adelante.

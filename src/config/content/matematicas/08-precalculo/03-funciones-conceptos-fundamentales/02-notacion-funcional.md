---
title: "Notación Funcional"
---

# Notación Funcional

Cuando escribimos $f(x)$, no estamos multiplicando $f$ por $x$. Es una notación especial que nos dice cómo evaluar una función. Dominarla es esencial para todo el cálculo.

---

## 🎯 ¿Qué vas a aprender?

- El significado de $f(x)$ y cómo leerlo
- Evaluar funciones en valores numéricos
- Evaluar funciones en expresiones algebraicas
- Operaciones con notación funcional

---

## 📖 ¿Qué significa $f(x)$?

La notación $f(x)$ se lee "**f de x**" y representa:

- $f$: el nombre de la función
- $x$: la variable de entrada (argumento)
- $f(x)$: el valor de salida cuando la entrada es $x$

**Ejemplo:** Si $f(x) = 2x + 3$

Entonces $f(x)$ es la regla que dice: "toma $x$, multiplícalo por 2 y súmale 3".

### ⚠️ Cuidado con la confusión

$f(x)$ **no** es $f \cdot x$ (multiplicación).

Es una notación de "contención": lo que está dentro del paréntesis es lo que va a ser procesado por la función.

---

## 📖 Evaluación de funciones

**Evaluar** una función significa reemplazar la variable por un valor específico.

### Regla de sustitución

> Para calcular $f(a)$, reemplaza **cada** $x$ en la fórmula de $f(x)$ por $a$.

---

## ⚙️ Ejemplo 1: Evaluación numérica

Sea $f(x) = x^2 - 3x + 2$. Calcula:

**a) $f(4)$**

$$f(4) = (4)^2 - 3(4) + 2 = 16 - 12 + 2 = 6$$

**b) $f(-2)$**

$$f(-2) = (-2)^2 - 3(-2) + 2 = 4 + 6 + 2 = 12$$

**c) $f(0)$**

$$f(0) = (0)^2 - 3(0) + 2 = 0 - 0 + 2 = 2$$

---

## ⚙️ Ejemplo 2: Evaluación con fracciones

Sea $g(x) = \frac{x + 1}{x - 2}$. Calcula:

**a) $g(5)$**

$$g(5) = \frac{5 + 1}{5 - 2} = \frac{6}{3} = 2$$

**b) $g(-1)$**

$$g(-1) = \frac{-1 + 1}{-1 - 2} = \frac{0}{-3} = 0$$

**c) $g(2)$**

$$g(2) = \frac{2 + 1}{2 - 2} = \frac{3}{0} = \text{no definido}$$

El valor $x = 2$ **no está en el dominio** de $g$.

---

## 📖 Evaluación con expresiones algebraicas

Podemos evaluar una función en expresiones, no solo en números.

### ⚙️ Ejemplo 3: $f(a + h)$

Sea $f(x) = x^2 + 1$. Calcula $f(a + h)$.

Reemplazamos $x$ por $(a + h)$:

$$f(a + h) = (a + h)^2 + 1$$

Expandimos:

$$f(a + h) = a^2 + 2ah + h^2 + 1$$

---

### ⚙️ Ejemplo 4: Expresiones combinadas

Sea $f(x) = 3x - 5$. Calcula:

**a) $f(2x)$**

$$f(2x) = 3(2x) - 5 = 6x - 5$$

**b) $2f(x)$**

$$2f(x) = 2(3x - 5) = 6x - 10$$

**c) $f(x^2)$**

$$f(x^2) = 3(x^2) - 5 = 3x^2 - 5$$

**d) $[f(x)]^2$**

$$[f(x)]^2 = (3x - 5)^2 = 9x^2 - 30x + 25$$

### 💡 Nota importante

$f(2x) \neq 2f(x)$ y $f(x^2) \neq [f(x)]^2$ en general.

---

## 📖 El cociente de diferencias

Una expresión fundamental en cálculo es el **cociente de diferencias**:

$$
\frac{f(x + h) - f(x)}{h}
$$

Esta expresión mide la razón de cambio promedio de la función.

---

### ⚙️ Ejemplo 5: Calculando el cociente de diferencias

Sea $f(x) = x^2$. Calcula $\frac{f(x + h) - f(x)}{h}$.

**Paso 1:** Calculamos $f(x + h)$
$$f(x + h) = (x + h)^2 = x^2 + 2xh + h^2$$

**Paso 2:** Restamos $f(x)$
$$f(x + h) - f(x) = x^2 + 2xh + h^2 - x^2 = 2xh + h^2$$

**Paso 3:** Dividimos entre $h$
$$\frac{f(x + h) - f(x)}{h} = \frac{2xh + h^2}{h} = \frac{h(2x + h)}{h} = 2x + h$$

**Resultado:** $\frac{f(x+h) - f(x)}{h} = 2x + h$

---

### ⚙️ Ejemplo 6: Con función lineal

Sea $f(x) = 5x - 2$. Calcula el cociente de diferencias.

**Paso 1:** $f(x + h) = 5(x + h) - 2 = 5x + 5h - 2$

**Paso 2:** $f(x + h) - f(x) = (5x + 5h - 2) - (5x - 2) = 5h$

**Paso 3:** $\frac{f(x + h) - f(x)}{h} = \frac{5h}{h} = 5$

**Resultado:** El cociente de diferencias es $5$ (¡la pendiente de la recta!).

---

## 📖 Funciones definidas por partes

Algunas funciones tienen diferentes fórmulas para diferentes intervalos.

### ⚙️ Ejemplo 7: Evaluando funciones por partes

$$
g(x) = \begin{cases} x^2 & \text{si } x < 0 \\ 2x + 1 & \text{si } x \geq 0 \end{cases}
$$

**a) $g(-3)$**

Como $-3 < 0$, usamos la primera fórmula:
$$g(-3) = (-3)^2 = 9$$

**b) $g(0)$**

Como $0 \geq 0$, usamos la segunda fórmula:
$$g(0) = 2(0) + 1 = 1$$

**c) $g(4)$**

Como $4 \geq 0$:
$$g(4) = 2(4) + 1 = 9$$

---

## 📊 Resumen de notaciones

| Notación | Significado |
|----------|-------------|
| $f(x)$ | El valor de la función $f$ en $x$ |
| $f(a)$ | El valor específico cuando $x = a$ |
| $f(x + h)$ | Evaluar $f$ en la expresión $x + h$ |
| $f(x) + h$ | Sumar $h$ al resultado de $f(x)$ |
| $f(g(x))$ | Composición: primero $g$, luego $f$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Sea $f(x) = 2x^2 - x + 3$. Calcula:

a) $f(1)$
b) $f(-2)$
c) $f(0)$
d) $f(a)$

<details>
<summary>Ver soluciones</summary>

a) $f(1) = 2(1)^2 - 1 + 3 = 2 - 1 + 3 = 4$

b) $f(-2) = 2(-2)^2 - (-2) + 3 = 8 + 2 + 3 = 13$

c) $f(0) = 2(0)^2 - 0 + 3 = 3$

d) $f(a) = 2a^2 - a + 3$
</details>

---

**Ejercicio 2:** Sea $f(x) = \frac{1}{x + 2}$. Calcula y simplifica:

a) $f(3)$
b) $f(x + h)$
c) $f(x + h) - f(x)$

<details>
<summary>Ver soluciones</summary>

a) $f(3) = \frac{1}{3 + 2} = \frac{1}{5}$

b) $f(x + h) = \frac{1}{(x + h) + 2} = \frac{1}{x + h + 2}$

c) $f(x+h) - f(x) = \frac{1}{x + h + 2} - \frac{1}{x + 2}$

   $= \frac{(x + 2) - (x + h + 2)}{(x + h + 2)(x + 2)} = \frac{-h}{(x + h + 2)(x + 2)}$
</details>

---

**Ejercicio 3:** Sea $g(x) = \begin{cases} 3x + 1 & \text{si } x \leq 2 \\ x^2 - 3 & \text{si } x > 2 \end{cases}$

Evalúa: a) $g(-1)$, b) $g(2)$, c) $g(5)$

<details>
<summary>Ver soluciones</summary>

a) $-1 \leq 2$, entonces $g(-1) = 3(-1) + 1 = -2$

b) $2 \leq 2$, entonces $g(2) = 3(2) + 1 = 7$

c) $5 > 2$, entonces $g(5) = 5^2 - 3 = 22$
</details>

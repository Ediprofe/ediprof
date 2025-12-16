# Límites Laterales

Los límites laterales analizan el comportamiento de una función cuando nos acercamos a un punto desde un solo lado. Son esenciales para funciones definidas por partes y para detectar discontinuidades.

---

## 🎯 ¿Qué vas a aprender?

- Definición de límites laterales
- Cuándo usarlos
- Relación con el límite bilateral
- Aplicaciones en funciones por partes

---

## 📖 Definiciones

### Límite por la izquierda

$$
\lim_{x \to a^-} f(x) = L
$$

$x$ se acerca a $a$ desde valores **menores** ($x < a$).

### Límite por la derecha

$$
\lim_{x \to a^+} f(x) = L
$$

$x$ se acerca a $a$ desde valores **mayores** ($x > a$).

---

## 📖 Relación fundamental

$$
\lim_{x \to a} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L
$$

El límite bilateral existe si y solo si:
1. Ambos límites laterales existen
2. Ambos son iguales

---

## ⚙️ Ejemplo 1: Función definida por partes

$$f(x) = \begin{cases} x^2 + 1 & \text{si } x < 2 \\ 3x - 1 & \text{si } x \geq 2 \end{cases}$$

**Límite por la izquierda:**

$$
\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (x^2 + 1) = 4 + 1 = 5
$$

**Límite por la derecha:**

$$
\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} (3x - 1) = 6 - 1 = 5
$$

Como $5 = 5$:

$$
\lim_{x \to 2} f(x) = 5
$$

---

## ⚙️ Ejemplo 2: Límites laterales diferentes

$$g(x) = \begin{cases} x + 3 & \text{si } x < 1 \\ x^2 & \text{si } x \geq 1 \end{cases}$$

**Límite por la izquierda:**

$$
\lim_{x \to 1^-} g(x) = 1 + 3 = 4
$$

**Límite por la derecha:**

$$
\lim_{x \to 1^+} g(x) = 1^2 = 1
$$

Como $4 \neq 1$:

$$
\lim_{x \to 1} g(x) \text{ no existe}
$$

---

## ⚙️ Ejemplo 3: Valor absoluto

$$f(x) = \frac{|x|}{x}$$

Para $x > 0$: $f(x) = \frac{x}{x} = 1$

Para $x < 0$: $f(x) = \frac{-x}{x} = -1$

**Límites laterales en $x = 0$:**

$$
\lim_{x \to 0^+} \frac{|x|}{x} = 1
$$

$$
\lim_{x \to 0^-} \frac{|x|}{x} = -1
$$

El límite en $x = 0$ **no existe**.

---

## ⚙️ Ejemplo 4: Función con raíz

$$h(x) = \sqrt{4 - x^2}$$

**Dominio:** $-2 \leq x \leq 2$

En $x = 2$:
- Solo podemos acercarnos por la **izquierda**
- $\lim_{x \to 2^-} \sqrt{4 - x^2} = 0$

En $x = -2$:
- Solo podemos acercarnos por la **derecha**
- $\lim_{x \to -2^+} \sqrt{4 - x^2} = 0$

---

## 📖 Cuándo usar límites laterales

| Situación | ¿Límites laterales? |
|-----------|---------------------|
| Funciones definidas por partes | ✅ Siempre |
| Valor absoluto | ✅ En puntos críticos |
| Raíces con restricciones de dominio | ✅ En extremos |
| Funciones racionales con asíntotas | ✅ Para determinar signo |
| Funciones discontinuas | ✅ Para clasificar discontinuidad |

---

## ⚙️ Ejemplo 5: Asíntota vertical

$$f(x) = \frac{1}{x - 3}$$

En $x = 3$:

**Por la izquierda ($x < 3$):**
- $x - 3 < 0$ (negativo)
- $\frac{1}{x-3} \to -\infty$

$$
\lim_{x \to 3^-} \frac{1}{x - 3} = -\infty
$$

**Por la derecha ($x > 3$):**
- $x - 3 > 0$ (positivo)
- $\frac{1}{x-3} \to +\infty$

$$
\lim_{x \to 3^+} \frac{1}{x - 3} = +\infty
$$

---

## ⚙️ Ejemplo 6: Función escalón

La función mayor entero (piso):

$$\lfloor x \rfloor = \text{mayor entero} \leq x$$

En cualquier entero $n$:

$$\lim_{x \to n^-} \lfloor x \rfloor = n - 1$$
$$\lim_{x \to n^+} \lfloor x \rfloor = n$$

Los límites laterales difieren, por lo que el límite no existe en enteros.

---

## 📖 Clasificación de discontinuidades

Los límites laterales nos ayudan a clasificar discontinuidades:

| Tipo | Característica |
|------|----------------|
| **Removible** | Límites laterales iguales, pero $\neq f(a)$ |
| **De salto** | Límites laterales existen pero son diferentes |
| **Infinita** | Al menos un límite lateral es $\pm\infty$ |
| **Esencial** | Al menos un límite lateral no existe/oscila |

---

## ⚙️ Ejemplo 7: Clasificar discontinuidad

$$f(x) = \begin{cases} \frac{x^2 - 1}{x - 1} & \text{si } x \neq 1 \\ 5 & \text{si } x = 1 \end{cases}$$

**Límites laterales:**
Para $x \neq 1$: $f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1$

$$\lim_{x \to 1^-} f(x) = 2$$
$$\lim_{x \to 1^+} f(x) = 2$$

El límite es $2$, pero $f(1) = 5$.

**Tipo:** Discontinuidad **removible**.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula los límites laterales en $x = 0$:

$$f(x) = \frac{x}{|x|}$$

<details>
<summary>Ver solución</summary>

Para $x > 0$: $f(x) = \frac{x}{x} = 1$
Para $x < 0$: $f(x) = \frac{x}{-x} = -1$

$$\lim_{x \to 0^+} f(x) = 1$$
$$\lim_{x \to 0^-} f(x) = -1$$

El límite bilateral no existe.
</details>

---

**Ejercicio 2:** Determina si existe el límite:

$$g(x) = \begin{cases} 2x + 1 & \text{si } x \leq 3 \\ x^2 - 2 & \text{si } x > 3 \end{cases}$$

$$\lim_{x \to 3} g(x) = ?$$

<details>
<summary>Ver solución</summary>

$$\lim_{x \to 3^-} g(x) = 2(3) + 1 = 7$$
$$\lim_{x \to 3^+} g(x) = 9 - 2 = 7$$

Como ambos son iguales: $\lim_{x \to 3} g(x) = 7$
</details>

---

**Ejercicio 3:** Encuentra los límites laterales:

$$\lim_{x \to 2^+} \frac{x + 1}{x - 2}$$

<details>
<summary>Ver solución</summary>

Cuando $x \to 2^+$: $x > 2$, entonces $x - 2 > 0$ (pequeño positivo)

Numerador: $2 + 1 = 3$
Denominador: pequeño positivo $\to 0^+$

$$\lim_{x \to 2^+} \frac{x + 1}{x - 2} = \frac{3}{0^+} = +\infty$$
</details>

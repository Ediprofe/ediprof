# Concepto Intuitivo de Límite

¿Qué sucede con una función cuando nos acercamos a un punto sin llegar a él? Esta pregunta fundamental define el concepto de límite, la puerta de entrada al cálculo.

---

## 🎯 ¿Qué vas a aprender?

- La idea intuitiva de límite
- Qué significa "acercarse" a un valor
- Límites laterales
- Cuándo un límite existe y cuándo no

---

## 📖 La pregunta fundamental

Considera la función:

$$
f(x) = \frac{x^2 - 1}{x - 1}
$$

¿Qué vale $f(1)$?

$$
f(1) = \frac{1 - 1}{1 - 1} = \frac{0}{0} \quad \text{¡Indeterminado!}
$$

La función **no está definida** en $x = 1$.

**Pero podemos preguntar:** ¿Qué pasa con $f(x)$ cuando $x$ se **acerca** a 1?

---

## 📖 Acercándose al límite

Evaluemos $f(x) = \frac{x^2 - 1}{x - 1}$ para valores cercanos a 1:

### Acercándose por la izquierda ($x < 1$)

| $x$ | $f(x)$ |
|-----|--------|
| $0.9$ | $1.9$ |
| $0.99$ | $1.99$ |
| $0.999$ | $1.999$ |
| $0.9999$ | $1.9999$ |

### Acercándose por la derecha ($x > 1$)

| $x$ | $f(x)$ |
|-----|--------|
| $1.1$ | $2.1$ |
| $1.01$ | $2.01$ |
| $1.001$ | $2.001$ |
| $1.0001$ | $2.0001$ |

**Observación:** Cuando $x$ se acerca a 1, $f(x)$ se acerca a **2**.

---

## 📖 Simplificación algebraica

¿Por qué $f(x) \to 2$? Simplifiquemos:

$$
f(x) = \frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1)
$$

Para $x \neq 1$, la función es simplemente $f(x) = x + 1$.

Cuando $x \to 1$: $f(x) = x + 1 \to 1 + 1 = 2$

La gráfica es una línea recta $y = x + 1$ con un **hueco** en $(1, 2)$.

---

## 📖 Definición intuitiva de límite

$$
\lim_{x \to a} f(x) = L
$$

Se lee: "El límite de $f(x)$ cuando $x$ tiende a $a$ es igual a $L$".

**Significado:** A medida que $x$ se acerca (pero no llega) a $a$, los valores de $f(x)$ se acercan a $L$.

### Lo que importa

- El límite depende de lo que pasa **cerca** de $a$, no **en** $a$.
- La función no necesita estar definida en $a$ para que el límite exista.

---

## 📖 Límites laterales

### Límite por la izquierda

$$
\lim_{x \to a^-} f(x) = L_1
$$

$x$ se acerca a $a$ desde valores **menores** que $a$.

### Límite por la derecha

$$
\lim_{x \to a^+} f(x) = L_2
$$

$x$ se acerca a $a$ desde valores **mayores** que $a$.

### Condición de existencia

$$
\lim_{x \to a} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L
$$

El límite (bilateral) existe si y solo si ambos límites laterales existen y son iguales.

---

## ⚙️ Ejemplo 1: Límite que existe

$$
f(x) = \frac{x^2 - 4}{x - 2}
$$

Para $x \neq 2$: $f(x) = \frac{(x-2)(x+2)}{x-2} = x + 2$

$$
\lim_{x \to 2} f(x) = 2 + 2 = 4
$$

Aunque $f(2)$ no existe, el límite es $4$.

---

## ⚙️ Ejemplo 2: Límites laterales diferentes

$$g(x) = \begin{cases} x + 1 & \text{si } x < 2 \\ x^2 - 1 & \text{si } x \geq 2 \end{cases}$$

**Límite por la izquierda:**
$$\lim_{x \to 2^-} g(x) = \lim_{x \to 2^-} (x + 1) = 3$$

**Límite por la derecha:**
$$\lim_{x \to 2^+} g(x) = \lim_{x \to 2^+} (x^2 - 1) = 4 - 1 = 3$$

Como $3 = 3$: $\lim_{x \to 2} g(x) = 3$

---

## ⚙️ Ejemplo 3: Límite que no existe

$$h(x) = \begin{cases} 1 & \text{si } x < 0 \\ -1 & \text{si } x \geq 0 \end{cases}$$

**Límite por la izquierda:**
$$\lim_{x \to 0^-} h(x) = 1$$

**Límite por la derecha:**
$$\lim_{x \to 0^+} h(x) = -1$$

Como $1 \neq -1$: **El límite no existe**.

---

## 📊 Resumen

| Situación | ¿Existe el límite? |
|-----------|-------------------|
| Límites laterales iguales | ✅ Sí |
| Límites laterales diferentes | ❌ No |
| Función no definida en $a$, pero laterales iguales | ✅ Sí |
| Función "explota" cerca de $a$ | ❌ No (puede ser $\pm\infty$) |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa tablas para estimar:

$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$$

<details>
<summary>Ver solución</summary>

Simplificando: $\frac{x^2 - 9}{x - 3} = \frac{(x-3)(x+3)}{x-3} = x + 3$

$$\lim_{x \to 3} (x + 3) = 6$$
</details>

---

**Ejercicio 2:** Determina si existe el límite:

$$f(x) = \begin{cases} 2x & \text{si } x < 1 \\ x^2 + 1 & \text{si } x \geq 1 \end{cases}$$

$$\lim_{x \to 1} f(x) = ?$$

<details>
<summary>Ver solución</summary>

- $\lim_{x \to 1^-} f(x) = 2(1) = 2$
- $\lim_{x \to 1^+} f(x) = 1 + 1 = 2$

Como ambos son iguales: $\lim_{x \to 1} f(x) = 2$
</details>

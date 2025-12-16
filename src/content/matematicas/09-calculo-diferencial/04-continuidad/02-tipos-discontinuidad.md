# Tipos de Discontinuidad

No todas las discontinuidades son iguales. Clasificarlas nos ayuda a entender el comportamiento de las funciones y determinar si pueden "repararse".

---

## 🎯 ¿Qué vas a aprender?

- Los tres tipos principales de discontinuidad
- Cómo identificar cada tipo
- Discontinuidades removibles vs. esenciales
- Ejemplos visuales de cada caso

---

## 📖 Clasificación de discontinuidades

### Discontinuidad removible (evitable)

Se puede "reparar" redefiniendo la función en un solo punto.

**Características:**
- El límite $\lim_{x \to a} f(x) = L$ existe
- Pero $f(a) \neq L$ o $f(a)$ no existe

**Corrección:** Definir $f(a) = L$

---

### Discontinuidad de salto (de primera especie)

Los límites laterales existen pero son diferentes.

**Características:**
- $\lim_{x \to a^-} f(x) = L_1$ existe
- $\lim_{x \to a^+} f(x) = L_2$ existe
- $L_1 \neq L_2$

**El salto:** $|L_2 - L_1|$

---

### Discontinuidad infinita (de segunda especie)

Al menos un límite lateral es infinito.

**Características:**
- $\lim_{x \to a^+} f(x) = \pm\infty$ o $\lim_{x \to a^-} f(x) = \pm\infty$
- Hay una asíntota vertical en $x = a$

---

### Discontinuidad esencial (oscilante)

El límite no existe y no es infinito.

**Características:**
- La función oscila infinitamente cerca de $a$
- Ejemplo clásico: $\sin\left(\frac{1}{x}\right)$ en $x = 0$

---

## ⚙️ Ejemplo 1: Discontinuidad removible

$$f(x) = \frac{x^2 - 1}{x - 1}$$

En $x = 1$:

$$\lim_{x \to 1} \frac{(x-1)(x+1)}{x-1} = \lim_{x \to 1} (x+1) = 2$$

El límite es 2, pero $f(1)$ no existe.

**Tipo:** Removible

**Para hacerla continua:** Definir $f(1) = 2$

---

## ⚙️ Ejemplo 2: Discontinuidad de salto

$$g(x) = \begin{cases} x + 1 & \text{si } x < 2 \\ x^2 - 1 & \text{si } x \geq 2 \end{cases}$$

En $x = 2$:

$$\lim_{x \to 2^-} (x + 1) = 3$$
$$\lim_{x \to 2^+} (x^2 - 1) = 3$$

Espera... estos son iguales. ¡Esta es continua!

Cambiemos el ejemplo:

$$g(x) = \begin{cases} x + 1 & \text{si } x < 2 \\ 3x - 2 & \text{si } x \geq 2 \end{cases}$$

$$\lim_{x \to 2^-} (x + 1) = 3$$
$$\lim_{x \to 2^+} (3x - 2) = 4$$

**Tipo:** Salto de magnitud $|4 - 3| = 1$

---

## ⚙️ Ejemplo 3: Otro salto clásico

La función signo:

$$\text{sgn}(x) = \begin{cases} -1 & \text{si } x < 0 \\ 0 & \text{si } x = 0 \\ 1 & \text{si } x > 0 \end{cases}$$

En $x = 0$:

$$\lim_{x \to 0^-} \text{sgn}(x) = -1$$
$$\lim_{x \to 0^+} \text{sgn}(x) = 1$$

**Tipo:** Salto de magnitud 2

---

## ⚙️ Ejemplo 4: Discontinuidad infinita

$$h(x) = \frac{1}{x - 3}$$

En $x = 3$:

$$\lim_{x \to 3^+} \frac{1}{x-3} = +\infty$$
$$\lim_{x \to 3^-} \frac{1}{x-3} = -\infty$$

**Tipo:** Infinita (hay asíntota vertical)

---

## ⚙️ Ejemplo 5: Discontinuidad esencial

$$p(x) = \sin\left(\frac{1}{x}\right)$$

En $x = 0$:

Cuando $x \to 0$, el argumento $\frac{1}{x} \to \pm\infty$, y $\sin$ oscila entre $-1$ y $1$ infinitamente.

El límite no existe (ni finito ni infinito).

**Tipo:** Esencial (oscilante)

---

## 📊 Tabla resumen

| Tipo | Límites laterales | ¿Reparable? |
|------|-------------------|-------------|
| Removible | Iguales y finitos | ✅ Sí |
| De salto | Diferentes y finitos | ❌ No |
| Infinita | Al menos uno infinito | ❌ No |
| Esencial | No existen | ❌ No |

---

## 📖 Identificación por análisis

### Algoritmo para clasificar

1. Calcular $\lim_{x \to a^-} f(x)$ y $\lim_{x \to a^+} f(x)$

2. **Si ambos existen y son iguales ($= L$):**
   - Si $f(a) = L$ → Continua
   - Si $f(a) \neq L$ o no existe → **Removible**

3. **Si ambos existen y son diferentes:**
   - **De salto**

4. **Si al menos uno es $\pm\infty$:**
   - **Infinita**

5. **Si al menos uno no existe (oscila):**
   - **Esencial**

---

## ⚙️ Ejemplo 6: Clasificación completa

$$f(x) = \frac{|x|}{x}$$

En $x = 0$:

Para $x > 0$: $f(x) = \frac{x}{x} = 1$
Para $x < 0$: $f(x) = \frac{-x}{x} = -1$

$$\lim_{x \to 0^+} f(x) = 1$$
$$\lim_{x \to 0^-} f(x) = -1$$

Límites laterales finitos pero diferentes.

**Tipo:** De salto

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Clasifica la discontinuidad en $x = 0$:

a) $f(x) = \frac{\sin x}{x}$

b) $g(x) = \frac{1}{x^2}$

<details>
<summary>Ver soluciones</summary>

a) $\lim_{x \to 0} \frac{\sin x}{x} = 1$ existe, pero $f(0)$ no está definida.
   **Removible**

b) $\lim_{x \to 0} \frac{1}{x^2} = +\infty$ (por ambos lados)
   **Infinita**
</details>

---

**Ejercicio 2:** Clasifica:

$$h(x) = \begin{cases} x^2 & \text{si } x \leq 1 \\ 2x + 1 & \text{si } x > 1 \end{cases}$$ en $x = 1$

<details>
<summary>Ver solución</summary>

$\lim_{x \to 1^-} x^2 = 1$
$\lim_{x \to 1^+} (2x + 1) = 3$

Límites diferentes y finitos.

**De salto** (magnitud 2)
</details>

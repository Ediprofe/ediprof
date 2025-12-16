# Diferenciabilidad y Continuidad

¿Toda función continua es derivable? ¿Toda función derivable es continua? La relación entre estos conceptos es fundamental y tiene implicaciones importantes.

---

## 🎯 ¿Qué vas a aprender?

- La relación entre diferenciabilidad y continuidad
- Por qué derivabilidad implica continuidad
- Ejemplos de funciones continuas no derivables
- Puntos problemáticos para la derivabilidad

---

## 📖 El teorema fundamental

> **Teorema:** Si $f$ es derivable en $x = a$, entonces $f$ es continua en $x = a$.

$$\text{Derivable} \Rightarrow \text{Continua}$$

### ⚠️ El recíproco es FALSO

$$\text{Continua} \not\Rightarrow \text{Derivable}$$

Una función puede ser continua pero no derivable.

---

## 📖 Demostración del teorema

Si $f'(a)$ existe, queremos probar que $\lim_{x \to a} f(x) = f(a)$.

$$\lim_{x \to a} f(x) = \lim_{x \to a} \left[f(a) + \frac{f(x) - f(a)}{x - a} \cdot (x - a)\right]$$

$$= f(a) + \lim_{x \to a} \frac{f(x) - f(a)}{x - a} \cdot \lim_{x \to a}(x - a)$$

$$= f(a) + f'(a) \cdot 0 = f(a)$$

Por lo tanto, $f$ es continua en $a$. $\square$

---

## 📖 Contrarrecíproco

Si $f$ no es continua en $a$, entonces $f$ no es derivable en $a$.

$$\text{No continua} \Rightarrow \text{No derivable}$$

La continuidad es **necesaria** pero no **suficiente** para la derivabilidad.

---

## 📖 Tipos de puntos no derivables

### 1. Punto de discontinuidad

Si $f$ no es continua, no puede ser derivable.

### 2. Punto anguloso (pico)

La función es continua pero tiene "esquinas" donde los límites laterales de la derivada son diferentes.

### 3. Punto cúspide

Los límites laterales de la derivada son infinitos con signos opuestos.

### 4. Tangente vertical

La derivada tiende a $\pm\infty$ por ambos lados.

---

## ⚙️ Ejemplo 1: Valor absoluto (pico)

$$f(x) = |x|$$

**Continuidad en $x = 0$:** $\lim_{x \to 0} |x| = 0 = f(0)$ ✓

**Derivabilidad en $x = 0$:**

$$\lim_{h \to 0^+} \frac{|h| - 0}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1$$

$$\lim_{h \to 0^-} \frac{|h| - 0}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1$$

Los límites laterales son diferentes → **No derivable en $x = 0$**

---

## ⚙️ Ejemplo 2: Raíz cúbica (tangente vertical)

$$f(x) = \sqrt[3]{x} = x^{1/3}$$

**Continuidad en $x = 0$:** $\lim_{x \to 0} x^{1/3} = 0 = f(0)$ ✓

**Derivabilidad en $x = 0$:**

$$\lim_{h \to 0} \frac{h^{1/3} - 0}{h} = \lim_{h \to 0} \frac{1}{h^{2/3}} = +\infty$$

El límite es infinito → **No derivable en $x = 0$** (pero hay tangente vertical)

---

## ⚙️ Ejemplo 3: Función definida por partes

$$g(x) = \begin{cases} x^2 & \text{si } x \leq 1 \\ 2x - 1 & \text{si } x > 1 \end{cases}$$

**Continuidad en $x = 1$:**
- $\lim_{x \to 1^-} x^2 = 1$
- $\lim_{x \to 1^+} (2x - 1) = 1$
- $g(1) = 1$

Continua ✓

**Derivabilidad en $x = 1$:**
- Por la izquierda: $\lim_{x \to 1^-} 2x = 2$
- Por la derecha: $\lim_{x \to 1^+} 2 = 2$

Ambos iguales → **Derivable en $x = 1$** con $g'(1) = 2$

---

## ⚙️ Ejemplo 4: Por partes no derivable

$$h(x) = \begin{cases} x^2 & \text{si } x \leq 1 \\ x + 1 & \text{si } x > 1 \end{cases}$$

**Continuidad en $x = 1$:**
- $\lim_{x \to 1^-} x^2 = 1$
- $\lim_{x \to 1^+} (x + 1) = 2$

No continua → **No derivable**

---

## ⚙️ Ejemplo 5: Función continua no derivable en ningún punto

La **función de Weierstrass** es continua en todo $\mathbb{R}$ pero no es derivable en **ningún punto**.

$$W(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x)$$

donde $0 < a < 1$, $b$ es un entero impar positivo, y $ab > 1 + \frac{3\pi}{2}$.

Esta función "zigzaguea" infinitamente a todas las escalas.

---

## 📊 Resumen de relaciones

| Condición | Resultado |
|-----------|-----------|
| Derivable | → Continua |
| Continua | ↛ Derivable necesariamente |
| No continua | → No derivable |
| Derivada lateral existe y es finita por ambos lados (e igual) | → Derivable |
| Derivadas laterales diferentes | → No derivable (pico) |
| Derivada lateral infinita | → No derivable (cúspide o tangente vertical) |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Es $f(x) = |x - 2|$ derivable en $x = 2$?

<details>
<summary>Ver solución</summary>

$f$ es continua en $x = 2$ ($f(2) = 0$).

Derivada por la izquierda: $\lim_{h \to 0^-} \frac{|h|}{h} = -1$
Derivada por la derecha: $\lim_{h \to 0^+} \frac{|h|}{h} = 1$

Diferentes → **No derivable en $x = 2$** (pico)
</details>

---

**Ejercicio 2:** Determina si $f$ es derivable en $x = 0$:

$$f(x) = \begin{cases} x^2 \sin\left(\frac{1}{x}\right) & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases}$$

<details>
<summary>Ver solución</summary>

$$f'(0) = \lim_{h \to 0} \frac{h^2 \sin(1/h) - 0}{h} = \lim_{h \to 0} h \sin\left(\frac{1}{h}\right)$$

Como $|h \sin(1/h)| \leq |h| \to 0$, el límite es 0.

**Sí es derivable**, con $f'(0) = 0$.
</details>

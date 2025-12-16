# Límites y Formas Indeterminadas

No todas las indeterminaciones son iguales. Algunas esconden límites finitos, otras infinitos, y otras simplemente no existen. Aprenderemos a reconocerlas y resolverlas.

---

## 🎯 ¿Qué vas a aprender?

- Las siete formas indeterminadas
- Técnicas para resolver $\frac{0}{0}$
- Técnicas para resolver $\frac{\infty}{\infty}$
- Otras indeterminaciones y sus estrategias

---

## 📖 Las siete formas indeterminadas

| Forma | Tipo |
|-------|------|
| $\frac{0}{0}$ | Cociente |
| $\frac{\infty}{\infty}$ | Cociente |
| $0 \cdot \infty$ | Producto |
| $\infty - \infty$ | Diferencia |
| $0^0$ | Exponencial |
| $1^\infty$ | Exponencial |
| $\infty^0$ | Exponencial |

### ⚠️ ¿Por qué son indeterminadas?

No podemos saber el resultado sin más análisis. Por ejemplo:

$$\frac{x}{x} \to 1, \quad \frac{x^2}{x} \to \infty, \quad \frac{x}{x^2} \to 0$$

Todas son $\frac{0}{0}$ cuando $x \to 0$, pero dan resultados diferentes.

---

## 📖 Forma $\frac{0}{0}$

Esta es la más común. Técnicas:

1. **Factorización**
2. **Racionalización**
3. **Límites notables**
4. **Regla de L'Hôpital** (se verá después)

---

## ⚙️ Ejemplo 1: Factorización

$$\lim_{x \to 2} \frac{x^2 - 5x + 6}{x^2 - 4}$$

**Verificamos:** $\frac{0}{0}$ ✓

**Factorizamos:**
$$= \lim_{x \to 2} \frac{(x-2)(x-3)}{(x-2)(x+2)}$$

$$= \lim_{x \to 2} \frac{x-3}{x+2} = \frac{-1}{4}$$

---

## 📖 Forma $\frac{\infty}{\infty}$

Ocurre cuando $x \to \pm\infty$ en funciones racionales.

**Técnica:** Dividir numerador y denominador por la mayor potencia de $x$.

---

## ⚙️ Ejemplo 2: Dividir por mayor potencia

$$\lim_{x \to \infty} \frac{3x^2 + 2x - 1}{5x^2 - x + 4}$$

**Dividimos por $x^2$:**

$$= \lim_{x \to \infty} \frac{3 + \frac{2}{x} - \frac{1}{x^2}}{5 - \frac{1}{x} + \frac{4}{x^2}}$$

Cuando $x \to \infty$, los términos con $x$ en el denominador $\to 0$:

$$= \frac{3 + 0 - 0}{5 - 0 + 0} = \frac{3}{5}$$

---

## 📖 Regla para funciones racionales en $\pm\infty$

Sea $\frac{a_n x^n + \cdots}{b_m x^m + \cdots}$ donde $a_n, b_m \neq 0$:

| Relación de grados | Límite |
|--------------------|--------|
| $n < m$ | $0$ |
| $n = m$ | $\frac{a_n}{b_m}$ |
| $n > m$ | $\pm\infty$ |

---

## ⚙️ Ejemplo 3: Grado del numerador mayor

$$\lim_{x \to \infty} \frac{2x^3 - x}{x^2 + 1}$$

Grado 3 > Grado 2 → $\pm\infty$

Dividimos por $x^2$:
$$= \lim_{x \to \infty} \frac{2x - \frac{1}{x}}{1 + \frac{1}{x^2}} = \frac{\infty}{1} = +\infty$$

---

## 📖 Forma $0 \cdot \infty$

**Estrategia:** Convertir a forma $\frac{0}{0}$ o $\frac{\infty}{\infty}$.

$$f \cdot g = \frac{f}{1/g} \quad \text{si } g \to \infty$$

---

## ⚙️ Ejemplo 4: Producto infinito por cero

$$\lim_{x \to 0^+} x \cdot \ln x$$

Forma: $0 \cdot (-\infty)$

**Reescribimos:**
$$= \lim_{x \to 0^+} \frac{\ln x}{1/x} = \frac{-\infty}{\infty}$$

Usaremos L'Hôpital más adelante. El resultado es $0$.

---

## 📖 Forma $\infty - \infty$

**Estrategia:** Transformar algebraicamente (factorizar, racionalizar, etc.)

---

## ⚙️ Ejemplo 5: Diferencia de infinitos

$$\lim_{x \to \infty} (\sqrt{x^2 + x} - x)$$

Forma: $\infty - \infty$

**Racionalizamos:**
$$= \lim_{x \to \infty} \frac{(\sqrt{x^2 + x} - x)(\sqrt{x^2 + x} + x)}{\sqrt{x^2 + x} + x}$$

$$= \lim_{x \to \infty} \frac{(x^2 + x) - x^2}{\sqrt{x^2 + x} + x}$$

$$= \lim_{x \to \infty} \frac{x}{\sqrt{x^2 + x} + x}$$

Dividimos por $x$:
$$= \lim_{x \to \infty} \frac{1}{\sqrt{1 + \frac{1}{x}} + 1} = \frac{1}{1 + 1} = \frac{1}{2}$$

---

## 📖 Formas exponenciales indeterminadas

Para $f(x)^{g(x)}$:

**Técnica:** Usar logaritmo y la identidad $a^b = e^{b \ln a}$

$$\lim f^g = e^{\lim g \ln f}$$

---

## ⚙️ Ejemplo 6: Forma $1^\infty$

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$$

Forma: $1^\infty$

**Este es el límite que define $e$:**

$$= e$$

---

## 📊 Resumen de estrategias

| Forma indeterminada | Estrategia principal |
|---------------------|---------------------|
| $\frac{0}{0}$ | Factorizar, racionalizar, L'Hôpital |
| $\frac{\infty}{\infty}$ | Dividir por mayor potencia, L'Hôpital |
| $0 \cdot \infty$ | Convertir a cociente |
| $\infty - \infty$ | Racionalizar, simplificar |
| $0^0$, $1^\infty$, $\infty^0$ | Usar $e^{\ln(\cdot)}$ |

---

## 📖 Formas que NO son indeterminadas

| Expresión | Resultado |
|-----------|-----------|
| $\frac{c}{0}$ ($c \neq 0$) | $\pm\infty$ |
| $\frac{0}{c}$ ($c \neq 0$) | $0$ |
| $\frac{c}{\infty}$ | $0$ |
| $c \cdot \infty$ ($c > 0$) | $\infty$ |
| $\infty + \infty$ | $\infty$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica la forma indeterminada y calcula:

a) $\lim_{x \to 1} \frac{x^3 - 1}{x - 1}$

b) $\lim_{x \to \infty} \frac{4x^2 + 1}{2x^2 - 3x}$

<details>
<summary>Ver soluciones</summary>

a) Forma $\frac{0}{0}$. Factorizando: $\frac{(x-1)(x^2+x+1)}{x-1} = x^2 + x + 1 \to 3$

b) Forma $\frac{\infty}{\infty}$. Grados iguales: $\frac{4}{2} = 2$
</details>

---

**Ejercicio 2:** Calcula:

$$\lim_{x \to \infty} (\sqrt{x^2 + 4x} - x)$$

<details>
<summary>Ver solución</summary>

Racionalizando: $\frac{x^2 + 4x - x^2}{\sqrt{x^2 + 4x} + x} = \frac{4x}{\sqrt{x^2 + 4x} + x}$

Dividiendo por $x$: $\frac{4}{\sqrt{1 + 4/x} + 1} \to \frac{4}{2} = 2$
</details>

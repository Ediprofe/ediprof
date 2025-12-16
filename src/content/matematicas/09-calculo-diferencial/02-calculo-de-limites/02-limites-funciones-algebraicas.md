# Límites de Funciones Algebraicas

Las funciones algebraicas incluyen polinomios, raíces y cocientes. Aprenderemos técnicas específicas para calcular sus límites, especialmente cuando la sustitución directa no funciona.

---

## 🎯 ¿Qué vas a aprender?

- Límites de polinomios por sustitución directa
- Límites de funciones racionales
- Técnicas de factorización
- Racionalización para eliminar raíces

---

## 📖 Límites de polinomios

Para cualquier polinomio $P(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0$:

$$
\lim_{x \to a} P(x) = P(a)
$$

Basta **sustituir directamente**.

### ⚙️ Ejemplo 1

$$\lim_{x \to 3} (2x^3 - 5x^2 + x - 4)$$

$$= 2(27) - 5(9) + 3 - 4 = 54 - 45 + 3 - 4 = 8$$

---

## 📖 Límites de funciones racionales

Para $f(x) = \frac{P(x)}{Q(x)}$:

### Caso 1: $Q(a) \neq 0$

$$
\lim_{x \to a} \frac{P(x)}{Q(x)} = \frac{P(a)}{Q(a)}
$$

### Caso 2: $Q(a) = 0$ y $P(a) \neq 0$

El límite no existe (o es $\pm\infty$).

### Caso 3: $Q(a) = 0$ y $P(a) = 0$

Forma indeterminada $\frac{0}{0}$. Requiere factorización.

---

## ⚙️ Ejemplo 2: Sustitución directa

$$\lim_{x \to 2} \frac{x^2 + 3x - 1}{x + 5}$$

$$
= \frac{4 + 6 - 1}{2 + 5} = \frac{9}{7}
$$

---

## ⚙️ Ejemplo 3: Factorización

$$\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$$

**Sustitución directa:** $\frac{0}{0}$ (indeterminado)

**Factorizamos:**
$$= \lim_{x \to 3} \frac{(x-3)(x+3)}{x-3}$$

**Cancelamos** (válido porque $x \neq 3$):
$$= \lim_{x \to 3} (x + 3) = 6$$

---

## ⚙️ Ejemplo 4: Factorización más compleja

$$\lim_{x \to 2} \frac{x^3 - 8}{x^2 - 4}$$

**Sustitución directa:** $\frac{0}{0}$

**Factorizamos:**
- $x^3 - 8 = (x - 2)(x^2 + 2x + 4)$ (diferencia de cubos)
- $x^2 - 4 = (x - 2)(x + 2)$

$$
= \lim_{x \to 2} \frac{(x-2)(x^2 + 2x + 4)}{(x-2)(x+2)}
$$

$$
= \lim_{x \to 2} \frac{x^2 + 2x + 4}{x + 2} = \frac{4 + 4 + 4}{4} = \frac{12}{4} = 3
$$

---

## 📖 Técnica de racionalización

Se usa cuando hay **raíces** que causan indeterminación.

**Estrategia:** Multiplicar por el conjugado.

Si $\sqrt{a} - \sqrt{b}$, multiplicamos por $\frac{\sqrt{a} + \sqrt{b}}{\sqrt{a} + \sqrt{b}}$

---

## ⚙️ Ejemplo 5: Racionalización en el numerador

$$\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$$

**Sustitución directa:** $\frac{0}{0}$

**Multiplicamos por el conjugado:**

$$= \lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x} \cdot \frac{\sqrt{x + 4} + 2}{\sqrt{x + 4} + 2}$$

$$= \lim_{x \to 0} \frac{(x + 4) - 4}{x(\sqrt{x + 4} + 2)}$$

$$= \lim_{x \to 0} \frac{x}{x(\sqrt{x + 4} + 2)}$$

$$
= \lim_{x \to 0} \frac{1}{\sqrt{x + 4} + 2} = \frac{1}{2 + 2} = \frac{1}{4}
$$

---

## ⚙️ Ejemplo 6: Racionalización en el denominador

$$\lim_{x \to 4} \frac{x - 4}{\sqrt{x} - 2}$$

**Sustitución directa:** $\frac{0}{0}$

**Multiplicamos por el conjugado del denominador:**

$$= \lim_{x \to 4} \frac{(x - 4)(\sqrt{x} + 2)}{(\sqrt{x} - 2)(\sqrt{x} + 2)}$$

$$= \lim_{x \to 4} \frac{(x - 4)(\sqrt{x} + 2)}{x - 4}$$

$$
= \lim_{x \to 4} (\sqrt{x} + 2) = 2 + 2 = 4
$$

---

## ⚙️ Ejemplo 7: Diferencia de raíces

$$\lim_{x \to 0} \frac{\sqrt{1 + x} - \sqrt{1 - x}}{x}$$

**Sustitución directa:** $\frac{0}{0}$

**Multiplicamos por el conjugado:**

$$= \lim_{x \to 0} \frac{(\sqrt{1+x} - \sqrt{1-x})(\sqrt{1+x} + \sqrt{1-x})}{x(\sqrt{1+x} + \sqrt{1-x})}$$

$$= \lim_{x \to 0} \frac{(1+x) - (1-x)}{x(\sqrt{1+x} + \sqrt{1-x})}$$

$$= \lim_{x \to 0} \frac{2x}{x(\sqrt{1+x} + \sqrt{1-x})}$$

$$
= \lim_{x \to 0} \frac{2}{\sqrt{1+x} + \sqrt{1-x}} = \frac{2}{1 + 1} = 1
$$

---

## 📊 Resumen de técnicas

| Situación | Técnica |
|-----------|---------|
| Polinomio | Sustitución directa |
| Racional con $Q(a) \neq 0$ | Sustitución directa |
| $\frac{0}{0}$ con polinomios | Factorizar y cancelar |
| $\frac{0}{0}$ con raíces | Racionalizar |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\lim_{x \to -1} \frac{x^2 - 1}{x + 1}$

b) $\lim_{x \to 4} \frac{x^2 - 16}{x - 4}$

<details>
<summary>Ver soluciones</summary>

a) $\frac{(x-1)(x+1)}{x+1} = x - 1 \to -2$

b) $\frac{(x-4)(x+4)}{x-4} = x + 4 \to 8$
</details>

---

**Ejercicio 2:** Usa racionalización:

$$\lim_{x \to 9} \frac{x - 9}{\sqrt{x} - 3}$$

<details>
<summary>Ver solución</summary>

$$= \frac{(x-9)(\sqrt{x}+3)}{(\sqrt{x}-3)(\sqrt{x}+3)} = \frac{(x-9)(\sqrt{x}+3)}{x-9} = \sqrt{x}+3 \to 6$$
</details>

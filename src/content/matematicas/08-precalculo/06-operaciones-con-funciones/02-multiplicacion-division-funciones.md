# Multiplicación y División de Funciones

Además de sumar y restar, podemos multiplicar y dividir funciones. La división introduce restricciones adicionales en el dominio.

---

## 🎯 ¿Qué vas a aprender?

- Producto de funciones
- Cociente de funciones
- Restricciones de dominio
- Simplificación de expresiones

---

## 📖 Producto de funciones

$$
(f \cdot g)(x) = f(x) \cdot g(x)
$$

### Dominio del producto

$$
\text{Dom}(f \cdot g) = \text{Dom}(f) \cap \text{Dom}(g)
$$

---

## ⚙️ Ejemplo 1: Producto básico

Sean $f(x) = x + 2$ y $g(x) = x - 3$.

$$(f \cdot g)(x) = (x + 2)(x - 3) = x^2 - 3x + 2x - 6 = x^2 - x - 6$$

**Dominio:** $\mathbb{R}$

---

## ⚙️ Ejemplo 2: Producto con raíces

Sean $f(x) = \sqrt{x}$ y $g(x) = \sqrt{x - 1}$.

**Dominios:**
- $\text{Dom}(f) = [0, +\infty)$
- $\text{Dom}(g) = [1, +\infty)$

**Dominio del producto:** $[1, +\infty)$

$$(f \cdot g)(x) = \sqrt{x} \cdot \sqrt{x - 1} = \sqrt{x(x - 1)}$$

---

## 📖 Cociente de funciones

$$
\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}
$$

### Dominio del cociente

Además de la intersección de dominios, debemos excluir donde $g(x) = 0$:

$$
\text{Dom}\left(\frac{f}{g}\right) = \text{Dom}(f) \cap \text{Dom}(g) \cap \{x : g(x) \neq 0\}
$$

---

## ⚙️ Ejemplo 3: Cociente con exclusiones

Sean $f(x) = x^2 - 4$ y $g(x) = x - 2$.

$$\left(\frac{f}{g}\right)(x) = \frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x - 2}$$

**Simplificamos (si $x \neq 2$):**
$$\left(\frac{f}{g}\right)(x) = x + 2, \quad x \neq 2$$

**Dominio:** $\mathbb{R} - \{2\}$

Aunque la expresión simplificada es $x + 2$, el dominio **conserva** la restricción original.

---

## ⚙️ Ejemplo 4: Cociente con múltiples restricciones

Sean $f(x) = \sqrt{x}$ y $g(x) = x - 4$.

**Dominios:**
- $\text{Dom}(f) = [0, +\infty)$
- $\text{Dom}(g) = \mathbb{R}$

**Intersección:** $[0, +\infty)$

**Restricción adicional:** $g(x) \neq 0 \Rightarrow x \neq 4$

**Dominio de $\frac{f}{g}$:** $[0, 4) \cup (4, +\infty)$

$$\left(\frac{f}{g}\right)(x) = \frac{\sqrt{x}}{x - 4}$$

---

## ⚙️ Ejemplo 5: Evaluación

Sean $f(x) = 2x + 1$ y $g(x) = x^2$. Calcula:

**a) $(f \cdot g)(3)$**
$$f(3) \cdot g(3) = 7 \cdot 9 = 63$$

**b) $\left(\frac{f}{g}\right)(2)$**
$$\frac{f(2)}{g(2)} = \frac{5}{4}$$

**c) $\left(\frac{g}{f}\right)(-\frac{1}{2})$**
$$\frac{g(-\frac{1}{2})}{f(-\frac{1}{2})} = \frac{\frac{1}{4}}{0} = \text{no definido}$$

---

## 📖 Propiedades del producto

| Propiedad | Fórmula |
|-----------|---------|
| Conmutativa | $(f \cdot g)(x) = (g \cdot f)(x)$ |
| Asociativa | $((f \cdot g) \cdot h)(x) = (f \cdot (g \cdot h))(x)$ |
| Elemento neutro | $(f \cdot 1)(x) = f(x)$ donde $1(x) = 1$ |
| Elemento absorbente | $(f \cdot 0)(x) = 0$ |
| Distributiva | $(f \cdot (g + h))(x) = (f \cdot g + f \cdot h)(x)$ |

---

## ⚙️ Ejemplo 6: Aplicación

Un rectángulo tiene:
- Largo: $L(x) = 2x + 5$ metros
- Ancho: $A(x) = x - 1$ metros

**Área:**
$$
\text{Área}(x) = L(x) \cdot A(x) = (2x + 5)(x - 1) = 2x^2 + 3x - 5
$$

**Restricción física:** $A(x) > 0 \Rightarrow x > 1$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Sean $f(x) = x + 3$ y $g(x) = x^2 - 9$. Encuentra:

a) $(f \cdot g)(x)$
b) $\left(\frac{g}{f}\right)(x)$ y su dominio

<details>
<summary>Ver soluciones</summary>

a) $(f \cdot g)(x) = (x + 3)(x^2 - 9) = (x + 3)(x - 3)(x + 3) = (x + 3)^2(x - 3)$

b) $\left(\frac{g}{f}\right)(x) = \frac{x^2 - 9}{x + 3} = \frac{(x-3)(x+3)}{x+3} = x - 3$ para $x \neq -3$
   
   **Dominio:** $\mathbb{R} - \{-3\}$
</details>

---

**Ejercicio 2:** Sean $f(x) = \sqrt{x + 2}$ y $g(x) = \sqrt{3 - x}$.

a) Encuentra el dominio de $f \cdot g$
b) Calcula $(f \cdot g)(x)$

<details>
<summary>Ver soluciones</summary>

a) $\text{Dom}(f) = [-2, +\infty)$, $\text{Dom}(g) = (-\infty, 3]$
   
   **Dominio:** $[-2, 3]$

b) $(f \cdot g)(x) = \sqrt{x + 2} \cdot \sqrt{3 - x} = \sqrt{(x + 2)(3 - x)}$
</details>

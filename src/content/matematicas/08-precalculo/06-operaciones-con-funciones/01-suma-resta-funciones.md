# Suma y Resta de Funciones

Podemos combinar funciones para crear nuevas funciones. La suma y resta de funciones son las operaciones más directas y preservan muchas propiedades.

---

## 🎯 ¿Qué vas a aprender?

- Cómo sumar y restar funciones
- El dominio de la función resultante
- Aplicaciones prácticas
- Evaluación y simplificación

---

## 📖 Definición

Dadas dos funciones $f$ y $g$:

$$
(f + g)(x) = f(x) + g(x)
$$

$$
(f - g)(x) = f(x) - g(x)
$$

### Dominio de la suma/resta

El dominio de $f + g$ (o $f - g$) es la **intersección** de los dominios de $f$ y $g$:

$$
\text{Dom}(f \pm g) = \text{Dom}(f) \cap \text{Dom}(g)
$$

---

## ⚙️ Ejemplo 1: Suma básica

Sean $f(x) = 2x + 3$ y $g(x) = x^2 - 1$.

**(f + g)(x):**
$$
(f + g)(x) = (2x + 3) + (x^2 - 1) = x^2 + 2x + 2
$$

**(f - g)(x):**
$$
(f - g)(x) = (2x + 3) - (x^2 - 1) = -x^2 + 2x + 4
$$

**Dominio:** Ambas son polinomios → $\mathbb{R}$

---

## ⚙️ Ejemplo 2: Con dominios restringidos

Sean $f(x) = \sqrt{x}$ y $g(x) = \sqrt{4 - x}$.

**Dominios individuales:**
- $\text{Dom}(f) = [0, +\infty)$
- $\text{Dom}(g) = (-\infty, 4]$

**Dominio de $f + g$:**
$$
[0, +\infty) \cap (-\infty, 4] = [0, 4]
$$

**(f + g)(x):**
$$
(f + g)(x) = \sqrt{x} + \sqrt{4 - x} \quad \text{para } x \in [0, 4]
$$

---

## ⚙️ Ejemplo 3: Evaluación

Sean $f(x) = x^2 - 2x$ y $g(x) = 3x + 1$. Calcula:

**a) (f + g)(2)**
$$
f(2) + g(2) = (4 - 4) + (6 + 1) = 0 + 7 = 7
$$

**b) (f - g)(-1)**
$$
f(-1) - g(-1) = (1 + 2) - (-3 + 1) = 3 - (-2) = 5
$$

---

## 📖 Propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Conmutativa | $(f + g)(x) = (g + f)(x)$ |
| Asociativa | $((f + g) + h)(x) = (f + (g + h))(x)$ |
| Elemento neutro | $(f + 0)(x) = f(x)$ donde $0(x) = 0$ |
| Inverso aditivo | $(f + (-f))(x) = 0$ donde $(-f)(x) = -f(x)$ |

---

## ⚙️ Ejemplo 4: Aplicación práctica

Una empresa tiene:
- Costo fijo mensual: $C_f(x) = 5000$ (constante)
- Costo variable por unidad: $C_v(x) = 20x$

**Costo total:**
$$
C(x) = C_f(x) + C_v(x) = 5000 + 20x
$$

Si el ingreso por vender $x$ unidades es $I(x) = 50x$:

**Ganancia:**
$$
G(x) = I(x) - C(x) = 50x - (5000 + 20x) = 30x - 5000
$$

---

## 📖 Gráfica de la suma

La gráfica de $(f + g)(x)$ se obtiene sumando las ordenadas ($y$) de $f$ y $g$ para cada $x$.

### Proceso visual:
1. Para cada valor de $x$, encuentra $f(x)$ y $g(x)$
2. Suma los valores
3. Grafica el punto $(x, f(x) + g(x))$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Sean $f(x) = x^2 + 1$ y $g(x) = 2x - 3$. Encuentra y simplifica:

a) $(f + g)(x)$
b) $(f - g)(x)$
c) $(g - f)(x)$

<details>
<summary>Ver soluciones</summary>

a) $(f + g)(x) = x^2 + 1 + 2x - 3 = x^2 + 2x - 2$

b) $(f - g)(x) = x^2 + 1 - (2x - 3) = x^2 - 2x + 4$

c) $(g - f)(x) = 2x - 3 - (x^2 + 1) = -x^2 + 2x - 4$
</details>

---

**Ejercicio 2:** Sean $f(x) = \frac{1}{x}$ y $g(x) = \frac{1}{x - 2}$.

a) Encuentra el dominio de $f + g$
b) Calcula $(f + g)(x)$

<details>
<summary>Ver soluciones</summary>

a) $\text{Dom}(f) = \mathbb{R} - \{0\}$, $\text{Dom}(g) = \mathbb{R} - \{2\}$
   
   $\text{Dom}(f + g) = \mathbb{R} - \{0, 2\}$

b) $(f + g)(x) = \frac{1}{x} + \frac{1}{x-2} = \frac{(x-2) + x}{x(x-2)} = \frac{2x - 2}{x(x-2)} = \frac{2(x-1)}{x(x-2)}$
</details>

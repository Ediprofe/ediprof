# 🔄 Racionalización

En esta lección aprenderemos a racionalizar, es decir, a eliminar los radicales del denominador de una fracción.

---

## 📖 ¿Por qué racionalizar?

Por convención matemática, las expresiones se consideran simplificadas cuando **no hay radicales en el denominador**. Racionalizar facilita:

- Las operaciones posteriores
- La comparación de expresiones
- Los cálculos numéricos

---

## 📖 Caso 1: Denominador con un solo término

Para eliminar un radical simple del denominador, multiplicamos numerador y denominador por el mismo radical.

### Regla

$$
\frac{a}{\sqrt[n]{b}} = \frac{a \cdot \sqrt[n]{b^{n-1}}}{\sqrt[n]{b} \cdot \sqrt[n]{b^{n-1}}} = \frac{a\sqrt[n]{b^{n-1}}}{b}
$$

---

### Ejemplo 1

Racionalizar $\dfrac{5}{\sqrt{3}}$.

**Multiplicamos por $\dfrac{\sqrt{3}}{\sqrt{3}}$:**

$$
\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}
$$

$$
\boxed{\frac{5}{\sqrt{3}} = \frac{5\sqrt{3}}{3}}
$$

---

### Ejemplo 2

Racionalizar $\dfrac{12}{\sqrt{6}}$.

$$
\frac{12}{\sqrt{6}} \cdot \frac{\sqrt{6}}{\sqrt{6}} = \frac{12\sqrt{6}}{6} = 2\sqrt{6}
$$

$$
\boxed{\frac{12}{\sqrt{6}} = 2\sqrt{6}}
$$

---

### Ejemplo 3

Racionalizar $\dfrac{8}{2\sqrt{2}}$.

$$
\frac{8}{2\sqrt{2}} = \frac{4}{\sqrt{2}} \cdot \frac{\sqrt{2}}{\sqrt{2}} = \frac{4\sqrt{2}}{2} = 2\sqrt{2}
$$

$$
\boxed{\frac{8}{2\sqrt{2}} = 2\sqrt{2}}
$$

---

### Ejemplo 4

Racionalizar $\dfrac{6}{\sqrt[3]{2}}$.

Necesitamos $\sqrt[3]{2^3} = 2$ en el denominador, así que multiplicamos por $\sqrt[3]{2^2} = \sqrt[3]{4}$:

$$
\frac{6}{\sqrt[3]{2}} \cdot \frac{\sqrt[3]{4}}{\sqrt[3]{4}} = \frac{6\sqrt[3]{4}}{\sqrt[3]{8}} = \frac{6\sqrt[3]{4}}{2} = 3\sqrt[3]{4}
$$

$$
\boxed{\frac{6}{\sqrt[3]{2}} = 3\sqrt[3]{4}}
$$

---

### Ejemplo 5

Racionalizar $\dfrac{10}{\sqrt[3]{5}}$.

$$
\frac{10}{\sqrt[3]{5}} \cdot \frac{\sqrt[3]{25}}{\sqrt[3]{25}} = \frac{10\sqrt[3]{25}}{\sqrt[3]{125}} = \frac{10\sqrt[3]{25}}{5} = 2\sqrt[3]{25}
$$

$$
\boxed{\frac{10}{\sqrt[3]{5}} = 2\sqrt[3]{25}}
$$

---

## 📖 Caso 2: Denominador con suma o diferencia de radicales

Cuando el denominador tiene la forma $\sqrt{a} \pm \sqrt{b}$, multiplicamos por el **conjugado**.

### Conjugado

El conjugado de $\sqrt{a} + \sqrt{b}$ es $\sqrt{a} - \sqrt{b}$ (y viceversa).

### Propiedad

$$
(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = a - b
$$

Esto elimina los radicales porque es una diferencia de cuadrados.

---

### Ejemplo 6

Racionalizar $\dfrac{1}{\sqrt{5} + \sqrt{3}}$.

**Multiplicamos por el conjugado $\sqrt{5} - \sqrt{3}$:**

$$
\frac{1}{\sqrt{5} + \sqrt{3}} \cdot \frac{\sqrt{5} - \sqrt{3}}{\sqrt{5} - \sqrt{3}} = \frac{\sqrt{5} - \sqrt{3}}{5 - 3} = \frac{\sqrt{5} - \sqrt{3}}{2}
$$

$$
\boxed{\frac{1}{\sqrt{5} + \sqrt{3}} = \frac{\sqrt{5} - \sqrt{3}}{2}}
$$

---

### Ejemplo 7

Racionalizar $\dfrac{6}{\sqrt{7} - \sqrt{5}}$.

$$
\frac{6}{\sqrt{7} - \sqrt{5}} \cdot \frac{\sqrt{7} + \sqrt{5}}{\sqrt{7} + \sqrt{5}} = \frac{6(\sqrt{7} + \sqrt{5})}{7 - 5} = \frac{6(\sqrt{7} + \sqrt{5})}{2}
$$

$$
= 3(\sqrt{7} + \sqrt{5}) = 3\sqrt{7} + 3\sqrt{5}
$$

$$
\boxed{\frac{6}{\sqrt{7} - \sqrt{5}} = 3\sqrt{7} + 3\sqrt{5}}
$$

---

### Ejemplo 8

Racionalizar $\dfrac{\sqrt{3}}{\sqrt{3} + 1}$.

$$
\frac{\sqrt{3}}{\sqrt{3} + 1} \cdot \frac{\sqrt{3} - 1}{\sqrt{3} - 1} = \frac{\sqrt{3}(\sqrt{3} - 1)}{3 - 1} = \frac{3 - \sqrt{3}}{2}
$$

$$
\boxed{\frac{\sqrt{3}}{\sqrt{3} + 1} = \frac{3 - \sqrt{3}}{2}}
$$

---

### Ejemplo 9

Racionalizar $\dfrac{5}{2 + \sqrt{3}}$.

$$
\frac{5}{2 + \sqrt{3}} \cdot \frac{2 - \sqrt{3}}{2 - \sqrt{3}} = \frac{5(2 - \sqrt{3})}{4 - 3} = \frac{5(2 - \sqrt{3})}{1}
$$

$$
= 10 - 5\sqrt{3}
$$

$$
\boxed{\frac{5}{2 + \sqrt{3}} = 10 - 5\sqrt{3}}
$$

---

### Ejemplo 10

Racionalizar $\dfrac{\sqrt{2} + 1}{\sqrt{2} - 1}$.

$$
\frac{\sqrt{2} + 1}{\sqrt{2} - 1} \cdot \frac{\sqrt{2} + 1}{\sqrt{2} + 1} = \frac{(\sqrt{2} + 1)^2}{2 - 1}
$$

Expandimos el numerador:

$$
(\sqrt{2} + 1)^2 = 2 + 2\sqrt{2} + 1 = 3 + 2\sqrt{2}
$$

$$
= \frac{3 + 2\sqrt{2}}{1} = 3 + 2\sqrt{2}
$$

$$
\boxed{\frac{\sqrt{2} + 1}{\sqrt{2} - 1} = 3 + 2\sqrt{2}}
$$

---

## 📋 Resumen

| Tipo de denominador | Método |
|:--------------------|:-------|
| $\sqrt{a}$ | Multiplicar por $\dfrac{\sqrt{a}}{\sqrt{a}}$ |
| $\sqrt[3]{a}$ | Multiplicar por $\dfrac{\sqrt[3]{a^2}}{\sqrt[3]{a^2}}$ |
| $\sqrt{a} + \sqrt{b}$ | Multiplicar por el conjugado $\sqrt{a} - \sqrt{b}$ |
| $\sqrt{a} - \sqrt{b}$ | Multiplicar por el conjugado $\sqrt{a} + \sqrt{b}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Racionaliza $\dfrac{3}{\sqrt{5}}$.

<details>
<summary>Ver solución</summary>

$$
\frac{3}{\sqrt{5}} \cdot \frac{\sqrt{5}}{\sqrt{5}} = \frac{3\sqrt{5}}{5}
$$

</details>

---

**Ejercicio 2:** Racionaliza $\dfrac{10}{\sqrt{2}}$.

<details>
<summary>Ver solución</summary>

$$
\frac{10\sqrt{2}}{2} = 5\sqrt{2}
$$

</details>

---

**Ejercicio 3:** Racionaliza $\dfrac{4}{\sqrt[3]{3}}$.

<details>
<summary>Ver solución</summary>

$$
\frac{4\sqrt[3]{9}}{3}
$$

</details>

---

**Ejercicio 4:** Racionaliza $\dfrac{2}{\sqrt{6} + 2}$.

<details>
<summary>Ver solución</summary>

$$
\frac{2(\sqrt{6} - 2)}{6 - 4} = \frac{2(\sqrt{6} - 2)}{2} = \sqrt{6} - 2
$$

</details>

---

**Ejercicio 5:** Racionaliza $\dfrac{3}{\sqrt{5} - \sqrt{2}}$.

<details>
<summary>Ver solución</summary>

$$
\frac{3(\sqrt{5} + \sqrt{2})}{5 - 2} = \frac{3(\sqrt{5} + \sqrt{2})}{3} = \sqrt{5} + \sqrt{2}
$$

</details>

---

**Ejercicio 6:** Racionaliza $\dfrac{\sqrt{3} - 1}{\sqrt{3} + 1}$.

<details>
<summary>Ver solución</summary>

$$
\frac{(\sqrt{3} - 1)^2}{3 - 1} = \frac{3 - 2\sqrt{3} + 1}{2} = \frac{4 - 2\sqrt{3}}{2} = 2 - \sqrt{3}
$$

</details>

---

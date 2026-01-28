---
title: "Clasificación de Funciones"
---

# Clasificación de Funciones

Las funciones se pueden clasificar según cómo asignan valores. Entender estas clasificaciones es crucial para el estudio de funciones inversas y el análisis matemático avanzado.

---

## 🎯 ¿Qué vas a aprender?

- Funciones inyectivas (uno a uno)
- Funciones suprayectivas (sobre)
- Funciones biyectivas
- La prueba de la línea horizontal

---

## 📖 Función inyectiva (uno a uno)

> Una función es **inyectiva** si diferentes entradas siempre producen diferentes salidas.

**Definición formal:** $f$ es inyectiva si:
$$
f(a) = f(b) \quad \Rightarrow \quad a = b
$$

O equivalentemente:
$$
a \neq b \quad \Rightarrow \quad f(a) \neq f(b)
$$

### Interpretación

No hay dos valores de $x$ que den el mismo valor de $y$.

---

## 📖 Prueba de la línea horizontal

Para determinar si una función es inyectiva usando su gráfica:

> **Regla:** Toda línea horizontal corta la gráfica **a lo más una vez**.

Si alguna línea horizontal corta la gráfica en dos o más puntos, la función **no es inyectiva**.

---

## ⚙️ Ejemplo 1: Analizando inyectividad

**a) $f(x) = 2x + 3$**

Si $f(a) = f(b)$:
$$2a + 3 = 2b + 3$$
$$2a = 2b$$
$$a = b$$

**Es inyectiva** ✓

**b) $f(x) = x^2$**

Nota que $f(2) = 4 = f(-2)$, pero $2 \neq -2$.

**No es inyectiva** ✗

**c) $f(x) = x^3$**

Si $f(a) = f(b)$:
$$a^3 = b^3$$
$$a = b$$

**Es inyectiva** ✓

---

## 📖 Función suprayectiva (sobre)

> Una función $f: A \to B$ es **suprayectiva** si todo elemento del codominio $B$ es imagen de al menos un elemento del dominio $A$.

**Definición formal:** $f$ es suprayectiva si para todo $y \in B$, existe al menos un $x \in A$ tal que $f(x) = y$.

### Interpretación

El rango de la función **coincide** con el codominio.

---

## ⚙️ Ejemplo 2: Analizando suprayectividad

**a) $f: \mathbb{R} \to \mathbb{R}$ definida por $f(x) = 2x + 1$**

Dado cualquier $y \in \mathbb{R}$, ¿existe $x$ tal que $2x + 1 = y$?

$$x = \frac{y - 1}{2}$$

Siempre encontramos tal $x$.

**Es suprayectiva** ✓

**b) $f: \mathbb{R} \to \mathbb{R}$ definida por $f(x) = x^2$**

¿Todo $y \in \mathbb{R}$ es imagen de algún $x$?

Para $y = -1$, no existe $x$ real tal que $x^2 = -1$.

**No es suprayectiva** ✗

El rango es $[0, +\infty) \neq \mathbb{R}$.

---

## 📖 Función biyectiva

> Una función es **biyectiva** si es **inyectiva y suprayectiva** a la vez.

**Propiedades de funciones biyectivas:**
- Cada elemento del dominio se relaciona con un único elemento del codominio
- Cada elemento del codominio tiene exactamente un preimagen
- **Tienen inversa**

---

## ⚙️ Ejemplo 3: Verificando biyectividad

**$f: \mathbb{R} \to \mathbb{R}$ definida por $f(x) = 3x - 5$**

**¿Inyectiva?**
Si $3a - 5 = 3b - 5$, entonces $a = b$. ✓

**¿Suprayectiva?**
Dado $y$, resolvemos $3x - 5 = y$:
$$x = \frac{y + 5}{3}$$
Existe para todo $y \in \mathbb{R}$. ✓

**Es biyectiva** ✓

---

## 📊 Resumen de clasificaciones

| Tipo | Condición | En gráfica |
|------|-----------|------------|
| **Inyectiva** | Diferentes $x$ → diferentes $y$ | Línea horizontal corta a lo más una vez |
| **Suprayectiva** | Todo $y$ del codominio es imagen | Línea horizontal corta al menos una vez |
| **Biyectiva** | Ambas anteriores | Línea horizontal corta exactamente una vez |

---

## 📖 Importancia de la biyectividad

Una función tiene **inversa** si y solo si es **biyectiva**.

Si $f$ es biyectiva, existe $f^{-1}$ tal que:
- $f^{-1}(f(x)) = x$ para todo $x$ en el dominio de $f$
- $f(f^{-1}(y)) = y$ para todo $y$ en el rango de $f$

---

## ⚙️ Ejemplo 4: Restricción de dominio

$f(x) = x^2$ no es inyectiva en $\mathbb{R}$.

Pero si restringimos: $f: [0, +\infty) \to [0, +\infty)$

Ahora sí es inyectiva (la parábola "hacia la derecha") y suprayectiva (el codominio es el rango).

**Con esta restricción, es biyectiva** y tiene inversa: $f^{-1}(x) = \sqrt{x}$.

---

## 📖 Tabla de funciones comunes

| Función | ¿Inyectiva? | ¿Suprayectiva? (en $\mathbb{R}$) | ¿Biyectiva? |
|---------|-------------|----------------------------------|-------------|
| $f(x) = c$ | ❌ | ❌ | ❌ |
| $f(x) = x$ | ✅ | ✅ | ✅ |
| $f(x) = x^2$ | ❌ | ❌ | ❌ |
| $f(x) = x^3$ | ✅ | ✅ | ✅ |
| $f(x) = e^x$ | ✅ | ❌ (rango $(0,\infty)$) | ❌ |
| $f(x) = \|x\|$ | ❌ | ❌ | ❌ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Determina si las siguientes funciones son inyectivas:

a) $f(x) = 5x - 2$
b) $f(x) = x^2 + 1$
c) $f(x) = \sqrt{x}$ (con dominio $[0, +\infty)$)

<details>
<summary>Ver soluciones</summary>

a) **Sí.** Si $5a - 2 = 5b - 2$, entonces $a = b$.

b) **No.** $f(2) = 5 = f(-2)$ pero $2 \neq -2$.

c) **Sí.** La raíz cuadrada principal es inyectiva. Si $\sqrt{a} = \sqrt{b}$ (con $a, b \geq 0$), entonces $a = b$.
</details>

---

**Ejercicio 2:** Para cada función $f: \mathbb{R} \to \mathbb{R}$, clasifica como inyectiva, suprayectiva, biyectiva, o ninguna:

a) $f(x) = 2x^3$
b) $f(x) = x^2 - 4$
c) $f(x) = \frac{1}{x}$ (dominio $\mathbb{R} - \{0\}$, codominio $\mathbb{R} - \{0\}$)

<details>
<summary>Ver soluciones</summary>

a) Para $f(x) = 2x^3$:
   - Inyectiva: Sí (función cúbica estrictamente creciente)
   - Suprayectiva: Sí (para cualquier $y$, $x = \sqrt[3]{y/2}$ existe)
   - **Biyectiva** ✓

b) Para $f(x) = x^2 - 4$:
   - Inyectiva: No ($f(2) = f(-2) = 0$)
   - Suprayectiva: No (rango $[-4, +\infty) \neq \mathbb{R}$)
   - **Ninguna**

c) Para $f(x) = \frac{1}{x}$:
   - Inyectiva: Sí (si $\frac{1}{a} = \frac{1}{b}$, entonces $a = b$)
   - Suprayectiva: Sí (para cualquier $y \neq 0$, $x = \frac{1}{y}$ existe)
   - **Biyectiva** en $\mathbb{R} - \{0\} \to \mathbb{R} - \{0\}$ ✓
</details>

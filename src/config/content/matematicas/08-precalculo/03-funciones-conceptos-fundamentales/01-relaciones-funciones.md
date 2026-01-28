---
title: "Relaciones y Funciones"
---

# Relaciones y Funciones

Todo en matemáticas se trata de relacionar cantidades. Pero no toda relación es una función. ¿Cuál es la diferencia? Eso es exactamente lo que descubrirás aquí.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una relación entre conjuntos
- La definición formal de función
- Cómo distinguir una función de una relación
- La prueba de la línea vertical

---

## 📖 ¿Qué es una relación?

Una **relación** es un conjunto de pares ordenados $(x, y)$ que conecta elementos de un conjunto $A$ (dominio) con elementos de un conjunto $B$ (codominio).

**Ejemplo:** La relación "tiene como cuadrado a" entre $\{1, 2, 3\}$ y $\{1, 4, 9, 16\}$:

$$
R = \{(1, 1), (2, 4), (3, 9)\}
$$

Cada par $(x, y)$ indica que "$x$ está relacionado con $y$".

### Formas de representar una relación

1. **Diagrama de flechas (sagital)**
2. **Conjunto de pares ordenados**
3. **Tabla de valores**
4. **Gráfica en el plano cartesiano**

---

## 📖 ¿Qué es una función?

Una **función** es una relación especial donde **cada elemento del dominio** tiene **exactamente un** elemento asignado en el codominio.

> **Definición formal:** Una función $f$ de $A$ en $B$, escrita $f: A \to B$, es una regla que asigna a cada $x \in A$ un **único** elemento $y \in B$.

Escribimos: $y = f(x)$ o $f: x \mapsto y$

### La diferencia clave

| Relación | Función |
|----------|---------|
| Un $x$ puede tener varios $y$ | Cada $x$ tiene exactamente un $y$ |
| $(1, 2)$ y $(1, 5)$ pueden coexistir | $(1, 2)$ y $(1, 5)$ **no** pueden coexistir |

---

## ⚙️ Ejemplo 1: ¿Es función o no?

**a) $R_1 = \{(1, 3), (2, 5), (3, 7)\}$**

¿Cada $x$ tiene un único $y$?
- $1 \to 3$ ✓
- $2 \to 5$ ✓
- $3 \to 7$ ✓

**Sí es función** ✓

**b) $R_2 = \{(1, 2), (2, 4), (1, 5)\}$**

El valor $x = 1$ está asociado a dos valores: $2$ y $5$.

**No es función** ✗

**c) $R_3 = \{(1, 3), (2, 3), (4, 3)\}$**

¿Cada $x$ tiene un único $y$?
- $1 \to 3$ ✓
- $2 \to 3$ ✓
- $4 \to 3$ ✓

Aunque varios $x$ dan el mismo $y$, eso está permitido.

**Sí es función** ✓

---

## 📖 Prueba de la línea vertical

Para determinar si una gráfica representa una función:

> **Regla:** Traza líneas verticales a través de la gráfica. Si **alguna línea vertical corta la gráfica en más de un punto**, entonces **no es función**.

### ⚙️ Ejemplo 2: Aplicando la prueba

**a) Parábola $y = x^2$**

Toda línea vertical cruza la curva en exactamente un punto.

**Es función** ✓

**b) Círculo $x^2 + y^2 = 4$**

Una línea vertical en $x = 1$ cruza el círculo en dos puntos: $(1, \sqrt{3})$ y $(1, -\sqrt{3})$.

**No es función** ✗

**c) Línea vertical $x = 3$**

La línea vertical $x = 3$ coincide con la gráfica en infinitos puntos.

**No es función** ✗

---

## 📖 Tipos de relaciones según correspondencia

| Tipo | Descripción | ¿Es función? |
|------|-------------|--------------|
| Uno a uno | Cada $x$ con un solo $y$, cada $y$ con un solo $x$ | ✓ |
| Muchos a uno | Varios $x$ con el mismo $y$ | ✓ |
| Uno a muchos | Un $x$ con varios $y$ | ✗ |
| Muchos a muchos | Varios $x$ con varios $y$ | ✗ |

---

## ⚙️ Ejemplo 3: Clasificando relaciones

**a) $f(x) = 2x + 1$**

- Cada $x$ produce un único $y$: función ✓
- Diferentes $x$ dan diferentes $y$: uno a uno ✓

**b) $f(x) = x^2$**

- Cada $x$ produce un único $y$: función ✓
- Pero $f(2) = 4 = f(-2)$: muchos a uno ✓

**c) La relación "es padre de"**

Un padre puede tener varios hijos (un $x$ con varios $y$): uno a muchos ✗

**No es función**

---

## 📖 Dominio, codominio y rango

| Término | Definición |
|---------|------------|
| **Dominio** | Conjunto de todos los valores de entrada $x$ |
| **Codominio** | Conjunto donde pueden estar los valores de salida |
| **Rango (imagen)** | Conjunto de valores de salida que realmente se obtienen |

**Ejemplo:** $f(x) = x^2$ con dominio $\{-2, -1, 0, 1, 2\}$

- Dominio: $\{-2, -1, 0, 1, 2\}$
- Codominio: $\mathbb{R}$ (si así se define)
- Rango: $\{0, 1, 4\}$ (los valores que realmente salen)

---

## 📊 Resumen: ¿Es función?

Para verificar si una relación es función:

1. **En pares ordenados:** Revisa que ningún valor de $x$ se repita con diferentes $y$.
2. **En diagrama de flechas:** Cada elemento del dominio debe tener exactamente una flecha saliendo.
3. **En gráfica:** Aplica la prueba de la línea vertical.
4. **En ecuación:** Despeja $y$ y verifica que obtengas un único valor para cada $x$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Determina si las siguientes relaciones son funciones:

a) $\{(-1, 2), (0, 5), (1, 2), (2, 8)\}$
b) $\{(3, 4), (3, 5), (4, 6)\}$
c) $\{(a, 1), (b, 1), (c, 1)\}$

<details>
<summary>Ver soluciones</summary>

a) **Sí es función.** Cada $x$ tiene un único $y$.

b) **No es función.** El valor $x = 3$ tiene dos imágenes: $4$ y $5$.

c) **Sí es función.** Aunque todos dan el mismo $y$, cada $x$ tiene un único $y$.
</details>

---

**Ejercicio 2:** ¿Cuáles de las siguientes ecuaciones definen $y$ como función de $x$?

a) $y = 3x - 7$
b) $x^2 + y^2 = 25$
c) $y = \sqrt{x}$
d) $x = y^2$

<details>
<summary>Ver soluciones</summary>

a) **Sí.** Para cada $x$ hay exactamente un $y$.

b) **No.** Es un círculo; para $x = 3$, tenemos $y = \pm 4$.

c) **Sí.** La raíz cuadrada (principal) da un único valor no negativo.

d) **No.** Para $x = 4$, tenemos $y = 2$ o $y = -2$.
</details>

---

**Ejercicio 3:** Dada la función $f = \{(1, a), (2, b), (3, c), (4, a)\}$:

a) ¿Cuál es el dominio?
b) ¿Cuál es el rango?
c) ¿Es una función uno a uno?

<details>
<summary>Ver soluciones</summary>

a) Dominio: $\{1, 2, 3, 4\}$

b) Rango: $\{a, b, c\}$

c) **No es uno a uno** porque $f(1) = a = f(4)$. Es muchos a uno.
</details>

# 🔗 Introducción a los Sistemas de Ecuaciones

En esta lección introduciremos los sistemas de ecuaciones lineales y su interpretación gráfica.

---

## 📖 ¿Qué es un sistema de ecuaciones?

Un **sistema de ecuaciones** es un conjunto de dos o más ecuaciones que deben satisfacerse simultáneamente.

### Sistema de 2×2

Un sistema de dos ecuaciones con dos incógnitas:

$$
\begin{cases}
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
\end{cases}
$$

**Resolver** el sistema significa encontrar los valores de $x$ e $y$ que satisfacen **ambas** ecuaciones al mismo tiempo.

---

## 📖 Ejemplo de sistema

$$
\begin{cases}
x + y = 5 \\
2x - y = 4
\end{cases}
$$

Buscamos valores de $x$ e $y$ que cumplan las dos ecuaciones.

**Solución:** $x = 3$, $y = 2$

**Verificación:**
- Primera: $3 + 2 = 5$ ✓
- Segunda: $2(3) - 2 = 6 - 2 = 4$ ✓

---

## 📖 Interpretación gráfica

Cada ecuación lineal representa una **recta** en el plano. La solución del sistema es el **punto de intersección** de ambas rectas.

---

## 📖 Tipos de sistemas

### Sistema compatible determinado

Las rectas se **cruzan en un punto**. Hay **una única solución**.

$$
\begin{cases}
x + y = 4 \\
x - y = 2
\end{cases}
$$

Solución: $(3, 1)$

---

### Sistema compatible indeterminado

Las rectas **coinciden** (son la misma). Hay **infinitas soluciones**.

$$
\begin{cases}
x + y = 3 \\
2x + 2y = 6
\end{cases}
$$

La segunda ecuación es el doble de la primera.

---

### Sistema incompatible

Las rectas son **paralelas** (no se cruzan). **No hay solución**.

$$
\begin{cases}
x + y = 3 \\
x + y = 5
\end{cases}
$$

Las rectas tienen la misma pendiente pero diferente intercepto.

---

## 📖 Clasificación por relación de coeficientes

Para el sistema:
$$
\begin{cases}
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
\end{cases}
$$

| Condición | Tipo | Soluciones |
|:----------|:-----|:-----------|
| $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ | Compatible determinado | Una |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Compatible indeterminado | Infinitas |
| $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ | Incompatible | Ninguna |

---

### Ejemplo 1

Clasificar el sistema:
$$
\begin{cases}
2x + 3y = 6 \\
4x + 6y = 12
\end{cases}
$$

$$
\frac{2}{4} = \frac{3}{6} = \frac{6}{12} = \frac{1}{2}
$$

Las tres razones son iguales → **Compatible indeterminado** (infinitas soluciones).

---

### Ejemplo 2

Clasificar el sistema:
$$
\begin{cases}
x + 2y = 5 \\
3x + 4y = 11
\end{cases}
$$

$$
\frac{1}{3} \neq \frac{2}{4} = \frac{1}{2}
$$

Las razones son diferentes → **Compatible determinado** (una solución).

---

### Ejemplo 3

Clasificar el sistema:
$$
\begin{cases}
2x - y = 4 \\
4x - 2y = 3
\end{cases}
$$

$$
\frac{2}{4} = \frac{-1}{-2} = \frac{1}{2}, \quad \text{pero } \frac{4}{3} \neq \frac{1}{2}
$$

**Incompatible** (sin solución).

---

## 📖 Métodos de resolución

En las siguientes lecciones aprenderemos diferentes métodos:

1. **Sustitución**: Despejar una variable y sustituir
2. **Igualación**: Igualar las expresiones de una misma variable
3. **Reducción (eliminación)**: Sumar o restar ecuaciones
4. **Gráfico**: Dibujar las rectas y encontrar la intersección
5. **Cramer**: Usar determinantes
6. **Gauss-Jordan**: Usar matrices

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Es $(2, 3)$ solución de $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$?

<details>
<summary>Ver solución</summary>

$2 + 3 = 5$ ✓

$2(2) - 3 = 4 - 3 = 1$ ✓

Sí, es solución.

</details>

---

**Ejercicio 2:** Clasifica: $\begin{cases} 3x + 6y = 9 \\ x + 2y = 3 \end{cases}$

<details>
<summary>Ver solución</summary>

$\frac{3}{1} = \frac{6}{2} = \frac{9}{3} = 3$

Compatible indeterminado (infinitas soluciones).

</details>

---

**Ejercicio 3:** Clasifica: $\begin{cases} x - y = 2 \\ 2x - 2y = 5 \end{cases}$

<details>
<summary>Ver solución</summary>

$\frac{1}{2} = \frac{-1}{-2}$, pero $\frac{2}{5} \neq \frac{1}{2}$

Incompatible (sin solución).

</details>

---

**Ejercicio 4:** Clasifica: $\begin{cases} 2x + y = 7 \\ x - 3y = -4 \end{cases}$

<details>
<summary>Ver solución</summary>

$\frac{2}{1} = 2 \neq \frac{1}{-3}$

Compatible determinado (una solución).

</details>

---

**Ejercicio 5:** ¿Cuántas soluciones tiene un sistema de rectas paralelas?

<details>
<summary>Ver solución</summary>

Ninguna (sistema incompatible).

</details>

---

**Ejercicio 6:** ¿Qué representa geométricamente la solución de un sistema 2×2?

<details>
<summary>Ver solución</summary>

El punto de intersección de las dos rectas.

</details>

---

# 📈 Progresión Geométrica

En esta lección estudiaremos las progresiones geométricas.

---

## 📖 Definición

Una **progresión geométrica (PG)** es una sucesión donde cada término se obtiene multiplicando el anterior por una cantidad fija (llamada **razón común** $r$).

$$
a_n = a_1 \cdot r^{n-1}
$$

---

## 📖 Ejemplos

### Ejemplo 1

$2, 6, 18, 54, ...$

Razón: $r = \frac{6}{2} = 3$

Término general: $a_n = 2 \cdot 3^{n-1}$

---

### Ejemplo 2

Encontrar el término 6 de la PG $3, 6, 12, 24, ...$

$a_1 = 3$, $r = 2$

$$
a_6 = 3 \cdot 2^{5} = 3 \cdot 32 = 96
$$

$$
\boxed{a_6 = 96}
$$

---

### Ejemplo 3

Encontrar $a_5$ si $a_1 = 100$ y $r = 0.5$.

$$
a_5 = 100 \cdot (0.5)^4 = 100 \cdot 0.0625 = 6.25
$$

$$
\boxed{a_5 = 6.25}
$$

---

## 📖 Suma de una PG finita

$$
S_n = a_1 \cdot \frac{1 - r^n}{1 - r} \quad \text{(si } r \neq 1\text{)}
$$

### Ejemplo 4

Sumar $1 + 2 + 4 + 8 + 16$.

$a_1 = 1$, $r = 2$, $n = 5$

$$
S_5 = 1 \cdot \frac{1 - 32}{1 - 2} = \frac{-31}{-1} = 31
$$

$$
\boxed{S_5 = 31}
$$

---

## 📖 Suma de una PG infinita

Si $|r| < 1$, la suma infinita converge:

$$
S_\infty = \frac{a_1}{1 - r}
$$

### Ejemplo 5

Sumar $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ...$

$a_1 = 1$, $r = \frac{1}{2}$

$$
S_\infty = \frac{1}{1 - \frac{1}{2}} = \frac{1}{\frac{1}{2}} = 2
$$

$$
\boxed{S_\infty = 2}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra $a_4$ si $a_1 = 5$ y $r = 3$.

<details>
<summary>Ver solución</summary>

$a_4 = 5 \cdot 3^3 = 135$

</details>

---

**Ejercicio 2:** Calcula $S_4$ de $2, 6, 18, 54$.

<details>
<summary>Ver solución</summary>

$S_4 = 2 \cdot \frac{1 - 81}{1 - 3} = 2 \cdot 40 = 80$

</details>

---

**Ejercicio 3:** ¿Cuál es la razón de $8, 4, 2, 1, ...$?

<details>
<summary>Ver solución</summary>

$r = \frac{4}{8} = 0.5$

</details>

---

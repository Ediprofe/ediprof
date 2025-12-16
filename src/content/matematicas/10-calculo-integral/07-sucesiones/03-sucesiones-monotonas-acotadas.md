# Sucesiones Monótonas y Acotadas

Las sucesiones monótonas y acotadas tienen propiedades especiales de convergencia. Estos conceptos son fundamentales en análisis.

---

## 🎯 ¿Qué vas a aprender?

- Sucesiones monótonas
- Sucesiones acotadas
- Teorema de convergencia monótona
- Aplicaciones

---

## 📖 Sucesiones monótonas

**Creciente:** $a_{n+1} \geq a_n$ para todo $n$

**Estrictamente creciente:** $a_{n+1} > a_n$ para todo $n$

**Decreciente:** $a_{n+1} \leq a_n$ para todo $n$

**Estrictamente decreciente:** $a_{n+1} < a_n$ para todo $n$

---

## ⚙️ Ejemplo 1: Verificar monotonía

$$
a_n = \frac{n}{n+1}
$$

$$
a_{n+1} - a_n = \frac{n+1}{n+2} - \frac{n}{n+1}
$$

$$
= \frac{(n+1)^2 - n(n+2)}{(n+2)(n+1)} = \frac{1}{(n+2)(n+1)} > 0
$$

Es **estrictamente creciente**.

---

## ⚙️ Ejemplo 2: Usando razón

$$
a_n = \frac{2^n}{n!}
$$

$$
\frac{a_{n+1}}{a_n} = \frac{2^{n+1}/(n+1)!}{2^n/n!} = \frac{2}{n+1}
$$

Para $n \geq 2$: $\frac{2}{n+1} < 1$, así que es **decreciente** para $n \geq 2$.

---

## 📖 Sucesiones acotadas

**Acotada superiormente:** Existe $M$ tal que $a_n \leq M$ para todo $n$

**Acotada inferiormente:** Existe $m$ tal que $a_n \geq m$ para todo $n$

**Acotada:** Acotada superior e inferiormente

---

## 📖 Teorema de convergencia monótona

> Toda sucesión monótona y acotada converge.

- Creciente y acotada superiormente → converge a su supremo
- Decreciente y acotada inferiormente → converge a su ínfimo

---

## ⚙️ Ejemplo 3: Aplicación del teorema

$$
a_n = \frac{n}{n+1}
$$

- Creciente ✓ (ejemplo 1)
- Acotada: $0 < a_n < 1$ para todo $n$ ✓

Por el teorema, converge. El límite es el supremo = 1.

---

## ⚙️ Ejemplo 4: Sucesión recursiva

$$
a_1 = 2, \quad a_{n+1} = \frac{1}{2}(a_n + 3)
$$

**Paso 1:** Calcular primeros términos
$a_1 = 2$, $a_2 = 2.5$, $a_3 = 2.75$, $a_4 = 2.875$, ...

**Paso 2:** Mostrar que es creciente
Si $a_n < 3$, entonces $a_{n+1} = \frac{a_n + 3}{2} > a_n$ ✓

**Paso 3:** Mostrar que está acotada
Si $a_n < 3$, entonces $a_{n+1} = \frac{a_n + 3}{2} < \frac{3 + 3}{2} = 3$ ✓

**Paso 4:** Encontrar el límite
Si $L = \lim a_n$, entonces $L = \frac{L + 3}{2}$, así que $L = 3$.

---

## ⚙️ Ejemplo 5: Raíz cuadrada iterativa

$$
a_1 = 1, \quad a_{n+1} = \sqrt{2 + a_n}
$$

Términos: 1, $\sqrt{3}$, $\sqrt{2+\sqrt{3}}$, ...

**Límite:** Si $L = \lim a_n$:

$$
L = \sqrt{2 + L}
$$

$$
L^2 = 2 + L
$$

$$
L^2 - L - 2 = 0
$$

$$
(L-2)(L+1) = 0
$$

Como $a_n > 0$, $L = 2$.

---

## 📊 Resumen

| Tipo | Condición | Converge |
|------|-----------|----------|
| Creciente + acotada sup. | Sí | Siempre |
| Decreciente + acotada inf. | Sí | Siempre |
| Monótona no acotada | No | Nunca |
| Acotada no monótona | Depende | A veces |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Muestra que $a_n = \frac{n!}{n^n}$ es decreciente.

<details>
<summary>Ver solución</summary>

$$
\frac{a_{n+1}}{a_n} = \frac{(n+1)!/(n+1)^{n+1}}{n!/n^n}
$$

$$
= \frac{(n+1) \cdot n^n}{(n+1)^{n+1}} = \frac{n^n}{(n+1)^n} = \left(\frac{n}{n+1}\right)^n < 1
$$

Es decreciente.
</details>

---

**Ejercicio 2:** Si $a_1 = 1$ y $a_{n+1} = \sqrt{a_n + 2}$, encuentra el límite.

<details>
<summary>Ver solución</summary>

$L = \sqrt{L + 2}$ → $L^2 = L + 2$ → $L = 2$ (descartando $L = -1$)
</details>

# ✖️ Multiplicación de Números Complejos

En esta lección aprenderemos a multiplicar dos números complejos entre sí.

---

## 📖 Regla de multiplicación

Para multiplicar dos números complejos, usamos la propiedad distributiva y el hecho de que $i^2 = -1$:

$$
(a + bi)(c + di) = ac + adi + bci + bdi^2
$$

$$
= ac + adi + bci + bd(-1) = ac - bd + (ad + bc)i
$$

### Fórmula

$$
(a + bi)(c + di) = (ac - bd) + (ad + bc)i
$$

---

### Ejemplo 1

Calcular $(2 + 3i)(4 + 5i)$.

$$
(2 + 3i)(4 + 5i) = 2(4) + 2(5i) + 3i(4) + 3i(5i)
$$

$$
= 8 + 10i + 12i + 15i^2 = 8 + 22i + 15(-1)
$$

$$
= 8 + 22i - 15 = -7 + 22i
$$

$$
\boxed{(2 + 3i)(4 + 5i) = -7 + 22i}
$$

---

### Ejemplo 2

Calcular $(3 + 2i)(1 - 4i)$.

$$
= 3(1) + 3(-4i) + 2i(1) + 2i(-4i)
$$

$$
= 3 - 12i + 2i - 8i^2 = 3 - 10i - 8(-1)
$$

$$
= 3 - 10i + 8 = 11 - 10i
$$

$$
\boxed{(3 + 2i)(1 - 4i) = 11 - 10i}
$$

---

### Ejemplo 3

Calcular $(5 - 2i)(3 + i)$.

$$
= 15 + 5i - 6i - 2i^2 = 15 - i + 2 = 17 - i
$$

$$
\boxed{(5 - 2i)(3 + i) = 17 - i}
$$

---

### Ejemplo 4

Calcular $(4 + i)^2$.

$$
(4 + i)^2 = (4 + i)(4 + i) = 16 + 4i + 4i + i^2
$$

$$
= 16 + 8i - 1 = 15 + 8i
$$

$$
\boxed{(4 + i)^2 = 15 + 8i}
$$

---

### Ejemplo 5

Calcular $(2 - 3i)^2$.

$$
(2 - 3i)^2 = 4 - 12i + 9i^2 = 4 - 12i - 9 = -5 - 12i
$$

$$
\boxed{(2 - 3i)^2 = -5 - 12i}
$$

---

## 📖 Producto con su conjugado

El producto de un complejo con su conjugado siempre da un número **real positivo**:

$$
(a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2i^2 = a^2 + b^2
$$

---

### Ejemplo 6

Calcular $(3 + 4i)(3 - 4i)$.

$$
(3 + 4i)(3 - 4i) = 3^2 + 4^2 = 9 + 16 = 25
$$

$$
\boxed{(3 + 4i)(3 - 4i) = 25}
$$

---

### Ejemplo 7

Calcular $(5 + 2i)(5 - 2i)$.

$$
5^2 + 2^2 = 25 + 4 = 29
$$

$$
\boxed{(5 + 2i)(5 - 2i) = 29}
$$

---

### Ejemplo 8

Calcular $(1 + i)(1 - i)$.

$$
1^2 + 1^2 = 1 + 1 = 2
$$

$$
\boxed{(1 + i)(1 - i) = 2}
$$

---

## 📖 Propiedades

La multiplicación de complejos es:

- **Conmutativa:** $z_1 \cdot z_2 = z_2 \cdot z_1$
- **Asociativa:** $(z_1 \cdot z_2) \cdot z_3 = z_1 \cdot (z_2 \cdot z_3)$
- **Distributiva:** $z_1(z_2 + z_3) = z_1 z_2 + z_1 z_3$

---

### Ejemplo 9

Calcular $(1 + i)^3$.

$$
(1 + i)^3 = (1 + i)^2 \cdot (1 + i)
$$

Primero $(1 + i)^2 = 1 + 2i + i^2 = 1 + 2i - 1 = 2i$

$$
= 2i(1 + i) = 2i + 2i^2 = 2i - 2 = -2 + 2i
$$

$$
\boxed{(1 + i)^3 = -2 + 2i}
$$

---

### Ejemplo 10

Calcular $(2 + i)(3 - 2i)(1 + i)$.

Primero $(2 + i)(3 - 2i)$:

$$
= 6 - 4i + 3i - 2i^2 = 6 - i + 2 = 8 - i
$$

Ahora $(8 - i)(1 + i)$:

$$
= 8 + 8i - i - i^2 = 8 + 7i + 1 = 9 + 7i
$$

$$
\boxed{(2 + i)(3 - 2i)(1 + i) = 9 + 7i}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $(1 + 2i)(3 + 4i)$.

<details>
<summary>Ver solución</summary>

$$
3 + 4i + 6i + 8i^2 = 3 + 10i - 8 = -5 + 10i
$$

</details>

---

**Ejercicio 2:** Calcula $(4 - 3i)(2 + i)$.

<details>
<summary>Ver solución</summary>

$$
8 + 4i - 6i - 3i^2 = 8 - 2i + 3 = 11 - 2i
$$

</details>

---

**Ejercicio 3:** Calcula $(3 + 5i)^2$.

<details>
<summary>Ver solución</summary>

$$
9 + 30i + 25i^2 = 9 + 30i - 25 = -16 + 30i
$$

</details>

---

**Ejercicio 4:** Calcula $(2 + 7i)(2 - 7i)$.

<details>
<summary>Ver solución</summary>

$$
4 + 49 = 53
$$

</details>

---

**Ejercicio 5:** Calcula $(1 - i)^2$.

<details>
<summary>Ver solución</summary>

$$
1 - 2i + i^2 = 1 - 2i - 1 = -2i
$$

</details>

---

**Ejercicio 6:** Calcula $i(2 + 3i)$.

<details>
<summary>Ver solución</summary>

$$
2i + 3i^2 = 2i - 3 = -3 + 2i
$$

</details>

---

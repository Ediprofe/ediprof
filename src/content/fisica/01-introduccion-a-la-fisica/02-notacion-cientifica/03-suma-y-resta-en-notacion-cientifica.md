# Suma y resta en notación científica

> **🎯 ¿Qué vas a aprender?**
>
> - A sumar y restar números expresados en notación científica.
> - A igualar exponentes antes de operar.
> - A ajustar el resultado para mantener la forma estándar.

---

## ⚙️ Regla general

En notación científica, **no se pueden sumar o restar directamente** números si sus potencias de 10 son diferentes. Primero es necesario que ambos números tengan **el mismo exponente**.

**Para sumar o restar:**

1. **Igualar los exponentes** de 10 (ajustando uno de los números).
2. **Operar los números base** (sumar o restar).
3. **Ajustar el resultado final** para que el número base quede entre 1 y 9.
4. **Conservar el exponente común** (modificado si el ajuste lo requiere).

### Fórmulas

**Suma:**

$$
(a \times 10^n) + (b \times 10^n) = (a + b) \times 10^n
$$

**Resta:**

$$
(a \times 10^n) - (b \times 10^n) = (a - b) \times 10^n
$$

---

## ✏️ Ejemplo 1: Suma con exponentes distintos

Suma los siguientes números:

$$
(3.2 \times 10^5) + (4.8 \times 10^4)
$$

**Solución paso a paso:**

1. Los exponentes son diferentes ($5$ y $4$). Igualamos expresando ambos con $10^5$:

$$
4.8 \times 10^4 = 0.48 \times 10^5
$$

2. Sumamos los números base:

$$
3.2 \times 10^5 + 0.48 \times 10^5 = (3.2 + 0.48) \times 10^5 = 3.68 \times 10^5
$$

3. El número base $3.68$ ya está entre 1 y 9, así que el resultado final es:

$$
\boxed{3.68 \times 10^5}
$$

---

## ✏️ Ejemplo 2: Resta con números pequeños

Resta los siguientes números:

$$
(2.3 \times 10^{-3}) - (1.1 \times 10^{-2})
$$

**Solución paso a paso:**

1. Igualamos los exponentes. Expresamos ambos con $10^{-2}$:

$$
2.3 \times 10^{-3} = 0.23 \times 10^{-2}
$$

2. Restamos los números base:

$$
(0.23 - 1.1) \times 10^{-2} = -0.87 \times 10^{-2}
$$

3. Ajustamos el número base para que quede entre 1 y 9 (movemos el punto una posición a la derecha y reducimos el exponente en 1):

$$
-0.87 \times 10^{-2} = -8.7 \times 10^{-3}
$$

4. Resultado final:

$$
\boxed{-8.7 \times 10^{-3}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Calcula la siguiente suma:**

$$
(5.4 \times 10^6) + (2.3 \times 10^5)
$$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Igualamos exponentes:

$$
2.3 \times 10^5 = 0.23 \times 10^6
$$

Realizamos la suma:

$$
5.4 \times 10^6 + 0.23 \times 10^6 = 5.63 \times 10^6
$$

**Resultado:**

$$
\boxed{5.63 \times 10^6}
$$

</details>

---

### Ejercicio 2
**Calcula la siguiente resta:**

$$
(7.5 \times 10^4) - (3.2 \times 10^4)
$$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Los exponentes ya son iguales:

$$
(7.5 - 3.2) \times 10^4 = 4.3 \times 10^4
$$

**Resultado:**

$$
\boxed{4.3 \times 10^4}
$$

</details>

---

### Ejercicio 3
**Calcula:**

$$
(1.2 \times 10^{-5}) + (8.0 \times 10^{-6})
$$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Igualamos exponentes:

$$
8.0 \times 10^{-6} = 0.80 \times 10^{-5}
$$

Realizamos la suma:

$$
1.2 \times 10^{-5} + 0.80 \times 10^{-5} = 2.0 \times 10^{-5}
$$

**Resultado:**

$$
\boxed{2.0 \times 10^{-5}}
$$

</details>

---

## 🔑 Resumen

| Caso | Qué se hace | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| **Exponentes iguales** | Se suman o restan directamente | $(5.2 + 1.3) \times 10^4$ | $6.5 \times 10^4$ |
| **Exponentes distintos** | Se ajusta uno de los números | $(3.2 \times 10^5) + (4.8 \times 10^4)$ | $3.68 \times 10^5$ |
| **Resultado menor que 1** | Se ajusta exponente y base | $-0.87 \times 10^{-2}$ | $-8.7 \times 10^{-3}$ |

> **Recuerda:** Para sumar o restar en notación científica, **igualar los exponentes es esencial**. Luego, se realiza la operación con los números base y se ajusta el resultado para que el número base quede entre **1 y 9**.
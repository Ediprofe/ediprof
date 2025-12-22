# Multiplicación y división en notación científica

> **🎯 ¿Qué vas a aprender?**
>
> - A multiplicar números expresados en notación científica.
> - A dividir números expresados en notación científica.
> - A aplicar las reglas de suma y resta de exponentes.

---

## ⚙️ Regla general de multiplicación

La notación científica facilita las operaciones con números muy grandes o muy pequeños, ya que permite **trabajar por separado** con los números base y con las potencias de 10.

**Para multiplicar:**

1. **Multiplica los números base**.
2. **Suma los exponentes** de 10.
3. Ajusta el número base si es necesario para que quede entre 1 y 9.

$$
(a \times 10^n) \times (b \times 10^m) = (a \cdot b) \times 10^{n+m}
$$

---

## ✏️ Ejemplo 1: Multiplicación

Multiplica los siguientes números:

$$
(2.5 \times 10^{3}) \times (4.0 \times 10^{2})
$$

**Solución paso a paso:**

1. Multiplicamos los números base: $2.5 \times 4.0 = 10.0$

2. Sumamos los exponentes: $3 + 2 = 5$

3. El número base $10.0$ no está entre 1 y 9, así que movemos el punto una posición a la izquierda y aumentamos el exponente en 1:

$$
10.0 \times 10^{5} = 1.0 \times 10^{6}
$$

**Resultado final:**

$$
\boxed{1.0 \times 10^{6}}
$$

---

## ⚙️ Regla general de división

**Para dividir:**

1. **Divide los números base**.
2. **Resta los exponentes** del numerador y denominador.
3. Ajusta el número base para que quede entre 1 y 9.

$$
\frac{a \times 10^{n}}{b \times 10^{m}} = \left(\frac{a}{b}\right) \times 10^{n-m}
$$

---

## ✏️ Ejemplo 2: División

Divide los siguientes números:

$$
\frac{6.0 \times 10^{8}}{3.0 \times 10^{4}}
$$

**Solución paso a paso:**

1. Dividimos los números base: $6.0 \div 3.0 = 2.0$

2. Restamos los exponentes: $8 - 4 = 4$

3. El número base $2.0$ ya está entre 1 y 9, por lo tanto el resultado es:

$$
\boxed{2.0 \times 10^{4}}
$$

---

## ✏️ Ejemplo 3: Multiplicación con ajuste

Multiplica:

$$
(8.0 \times 10^{5}) \times (5.0 \times 10^{3})
$$

**Solución paso a paso:**

1. Multiplicamos los números base: $8.0 \times 5.0 = 40.0$

2. Sumamos los exponentes: $5 + 3 = 8$

3. El número base $40.0$ no está entre 1 y 9. Ajustamos:

$$
40.0 \times 10^{8} = 4.0 \times 10^{9}
$$

**Resultado final:**

$$
\boxed{4.0 \times 10^{9}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Calcula la siguiente multiplicación:**

$$
(3.0 \times 10^{4}) \times (2.0 \times 10^{5})
$$

<details>
<summary>Ver solución</summary>

1. Multiplicamos bases: $3.0 \times 2.0 = 6.0$
2. Sumamos exponentes: $4 + 5 = 9$

$$
6.0 \times 10^{9}
$$

</details>

---

### Ejercicio 2
**Calcula la siguiente división:**

$$
\frac{9.0 \times 10^{7}}{3.0 \times 10^{2}}
$$

<details>
<summary>Ver solución</summary>

1. Dividimos bases: $9.0 \div 3.0 = 3.0$
2. Restamos exponentes: $7 - 2 = 5$

$$
3.0 \times 10^{5}
$$

</details>

---

### Ejercicio 3
**Calcula:**

$$
(4.5 \times 10^{-3}) \times (2.0 \times 10^{6})
$$

<details>
<summary>Ver solución</summary>

1. Multiplicamos bases: $4.5 \times 2.0 = 9.0$
2. Sumamos exponentes: $-3 + 6 = 3$

$$
9.0 \times 10^{3}
$$

</details>

---

### Ejercicio 4
**Calcula:**

$$
\frac{2.4 \times 10^{-2}}{8.0 \times 10^{-5}}
$$

<details>
<summary>Ver solución</summary>

1. Dividimos bases: $2.4 \div 8.0 = 0.3$
2. Restamos exponentes: $-2 - (-5) = -2 + 5 = 3$

$$
0.3 \times 10^{3} = 3.0 \times 10^{2}
$$

</details>

---

## 🔑 Resumen

| Operación | Regla | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| **Multiplicación** | Multiplicar bases, **sumar** exponentes | $(2.5 \times 10^3)(4.0 \times 10^2)$ | $1.0 \times 10^6$ |
| **División** | Dividir bases, **restar** exponentes | $\frac{6.0 \times 10^8}{3.0 \times 10^4}$ | $2.0 \times 10^4$ |

> **Recuerda:** En la **multiplicación**, se **suman los exponentes** de 10. En la **división**, se **restan los exponentes**. En ambos casos, asegúrate de que el número base esté entre **1 y 9** antes de escribir el resultado final.

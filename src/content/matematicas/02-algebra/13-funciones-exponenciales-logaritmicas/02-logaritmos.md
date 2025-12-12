# 📉 Logaritmos

En esta lección estudiaremos los logaritmos como la operación inversa de la exponenciación.

---

## 📖 Definición

El **logaritmo** de un número es el exponente al cual hay que elevar la base para obtener ese número:

$$
\log_b(x) = y \quad \Leftrightarrow \quad b^y = x
$$

Se lee "logaritmo en base $b$ de $x$".

---

## 📖 Ejemplos de definición

### Ejemplo 1

Calcular $\log_2(8)$.

¿A qué exponente debo elevar $2$ para obtener $8$?

$$
2^3 = 8 \quad \Rightarrow \quad \log_2(8) = 3
$$

$$
\boxed{\log_2(8) = 3}
$$

---

### Ejemplo 2

Calcular $\log_3(27)$.

$$
3^3 = 27 \quad \Rightarrow \quad \log_3(27) = 3
$$

$$
\boxed{\log_3(27) = 3}
$$

---

### Ejemplo 3

Calcular $\log_{10}(1000)$.

$$
10^3 = 1000 \quad \Rightarrow \quad \log_{10}(1000) = 3
$$

$$
\boxed{\log_{10}(1000) = 3}
$$

---

### Ejemplo 4

Calcular $\log_5(1)$.

$$
5^0 = 1 \quad \Rightarrow \quad \log_5(1) = 0
$$

$$
\boxed{\log_5(1) = 0}
$$

---

## 📖 Tipos de logaritmos

| Notación | Base | Nombre |
|:--------:|:----:|:-------|
| $\log(x)$ | 10 | Logaritmo común |
| $\ln(x)$ | $e$ | Logaritmo natural |
| $\log_b(x)$ | $b$ | Logaritmo en base $b$ |

---

## 📖 Propiedades de los logaritmos

### Logaritmo de un producto

$$
\log_b(xy) = \log_b(x) + \log_b(y)
$$

### Logaritmo de un cociente

$$
\log_b\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y)
$$

### Logaritmo de una potencia

$$
\log_b(x^n) = n \cdot \log_b(x)
$$

---

### Ejemplo 5

Simplificar $\log_2(8 \cdot 4)$.

$$
\log_2(8) + \log_2(4) = 3 + 2 = 5
$$

Verificación: $\log_2(32) = 5$ ✓

---

### Ejemplo 6

Expandir $\log\left(\frac{x^2y}{z}\right)$.

$$
= \log(x^2) + \log(y) - \log(z) = 2\log(x) + \log(y) - \log(z)
$$

---

## 📖 Cambio de base

$$
\log_b(x) = \frac{\log_c(x)}{\log_c(b)} = \frac{\ln(x)}{\ln(b)}
$$

### Ejemplo 7

Calcular $\log_5(20)$ usando logaritmos decimales.

$$
\log_5(20) = \frac{\log(20)}{\log(5)} \approx \frac{1.301}{0.699} \approx 1.861
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $\log_4(16)$.

<details>
<summary>Ver solución</summary>

$4^2 = 16$ → $\log_4(16) = 2$

</details>

---

**Ejercicio 2:** Calcula $\log_2(32)$.

<details>
<summary>Ver solución</summary>

$2^5 = 32$ → $\log_2(32) = 5$

</details>

---

**Ejercicio 3:** Simplifica $\log(100) + \log(10)$.

<details>
<summary>Ver solución</summary>

$2 + 1 = 3$

</details>

---

**Ejercicio 4:** Expande $\ln(x^3y^2)$.

<details>
<summary>Ver solución</summary>

$3\ln(x) + 2\ln(y)$

</details>

---

# ⚡ Potencias de i

En esta lección estudiaremos el patrón cíclico que siguen las potencias de la unidad imaginaria $i$.

---

## 📖 Las primeras potencias de i

Calculemos las primeras potencias:

$$
i^1 = i
$$

$$
i^2 = -1 \quad \text{(por definición)}
$$

$$
i^3 = i^2 \cdot i = (-1) \cdot i = -i
$$

$$
i^4 = i^2 \cdot i^2 = (-1)(-1) = 1
$$

$$
i^5 = i^4 \cdot i = 1 \cdot i = i
$$

$$
i^6 = i^4 \cdot i^2 = 1 \cdot (-1) = -1
$$

---

## 📖 El patrón cíclico

Las potencias de $i$ forman un **ciclo de 4**:

| Residuo de dividir entre 4 | Potencia |
|:--------------------------:|:--------:|
| 1 | $i$ |
| 2 | $-1$ |
| 3 | $-i$ |
| 0 | $1$ |

### Regla

Para calcular $i^n$, dividimos $n$ entre $4$ y usamos el **residuo**:

- Si el residuo es 0: $i^n = 1$
- Si el residuo es 1: $i^n = i$
- Si el residuo es 2: $i^n = -1$
- Si el residuo es 3: $i^n = -i$

---

### Ejemplo 1

Calcular $i^{17}$.

$17 \div 4 = 4$ con residuo $1$

$$
i^{17} = i^1 = i
$$

$$
\boxed{i^{17} = i}
$$

---

### Ejemplo 2

Calcular $i^{24}$.

$24 \div 4 = 6$ con residuo $0$

$$
i^{24} = i^0 = 1
$$

$$
\boxed{i^{24} = 1}
$$

---

### Ejemplo 3

Calcular $i^{35}$.

$35 \div 4 = 8$ con residuo $3$

$$
i^{35} = i^3 = -i
$$

$$
\boxed{i^{35} = -i}
$$

---

### Ejemplo 4

Calcular $i^{102}$.

$102 \div 4 = 25$ con residuo $2$

$$
i^{102} = i^2 = -1
$$

$$
\boxed{i^{102} = -1}
$$

---

### Ejemplo 5

Calcular $i^{1000}$.

$1000 \div 4 = 250$ con residuo $0$

$$
i^{1000} = 1
$$

$$
\boxed{i^{1000} = 1}
$$

---

## 📖 Potencias negativas de i

Para potencias negativas, primero simplificamos:

$$
i^{-1} = \frac{1}{i} = \frac{1}{i} \cdot \frac{i}{i} = \frac{i}{i^2} = \frac{i}{-1} = -i
$$

$$
i^{-2} = \frac{1}{i^2} = \frac{1}{-1} = -1
$$

$$
i^{-3} = \frac{1}{i^3} = \frac{1}{-i} = \frac{1}{-i} \cdot \frac{-i}{-i} = \frac{-i}{i^2} = \frac{-i}{-1} = i
$$

$$
i^{-4} = \frac{1}{i^4} = \frac{1}{1} = 1
$$

---

### Ejemplo 6

Calcular $i^{-7}$.

$|-7| = 7$, $7 \div 4 = 1$ con residuo $3$, entonces $i^7 = -i$

$$
i^{-7} = \frac{1}{i^7} = \frac{1}{-i} = \frac{i}{-i^2} = \frac{i}{1} = i
$$

O usando el patrón para negativos (se invierte el signo de $i$):

$$
\boxed{i^{-7} = i}
$$

---

### Ejemplo 7

Calcular $i^{-10}$.

$10 \div 4 = 2$ con residuo $2$, entonces $i^{10} = -1$

$$
i^{-10} = \frac{1}{i^{10}} = \frac{1}{-1} = -1
$$

$$
\boxed{i^{-10} = -1}
$$

---

## 📖 Suma de potencias

### Ejemplo 8

Calcular $i^5 + i^6 + i^7 + i^8$.

$$
i^5 = i, \quad i^6 = -1, \quad i^7 = -i, \quad i^8 = 1
$$

$$
i + (-1) + (-i) + 1 = i - 1 - i + 1 = 0
$$

$$
\boxed{i^5 + i^6 + i^7 + i^8 = 0}
$$

> **Observación:** La suma de 4 potencias consecutivas de $i$ siempre es 0.

---

### Ejemplo 9

Calcular $i^{10} + i^{20} + i^{30}$.

$$
i^{10} = i^2 = -1
$$

$$
i^{20} = i^0 = 1
$$

$$
i^{30} = i^2 = -1
$$

$$
-1 + 1 + (-1) = -1
$$

$$
\boxed{i^{10} + i^{20} + i^{30} = -1}
$$

---

### Ejemplo 10

Calcular $i^{100} - i^{99}$.

$$
i^{100} = i^0 = 1
$$

$$
i^{99} = i^3 = -i
$$

$$
1 - (-i) = 1 + i
$$

$$
\boxed{i^{100} - i^{99} = 1 + i}
$$

---

## 📋 Resumen

| Potencia | Valor | Potencia | Valor |
|:--------:|:-----:|:--------:|:-----:|
| $i^1$ | $i$ | $i^5$ | $i$ |
| $i^2$ | $-1$ | $i^6$ | $-1$ |
| $i^3$ | $-i$ | $i^7$ | $-i$ |
| $i^4$ | $1$ | $i^8$ | $1$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $i^{15}$.

<details>
<summary>Ver solución</summary>

$15 \div 4 = 3$ residuo $3$ → $i^{15} = -i$

</details>

---

**Ejercicio 2:** Calcula $i^{48}$.

<details>
<summary>Ver solución</summary>

$48 \div 4 = 12$ residuo $0$ → $i^{48} = 1$

</details>

---

**Ejercicio 3:** Calcula $i^{73}$.

<details>
<summary>Ver solución</summary>

$73 \div 4 = 18$ residuo $1$ → $i^{73} = i$

</details>

---

**Ejercicio 4:** Calcula $i^{-5}$.

<details>
<summary>Ver solución</summary>

$i^5 = i$, entonces $i^{-5} = \frac{1}{i} = -i$

</details>

---

**Ejercicio 5:** Calcula $i^{21} + i^{22} + i^{23} + i^{24}$.

<details>
<summary>Ver solución</summary>

$i + (-1) + (-i) + 1 = 0$

</details>

---

**Ejercicio 6:** Calcula $i^{50} - i^{51}$.

<details>
<summary>Ver solución</summary>

$i^{50} = -1$, $i^{51} = i$

$-1 - i$

</details>

---

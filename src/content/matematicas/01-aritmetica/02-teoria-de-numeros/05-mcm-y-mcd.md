# 🔗 MCM y MCD

En este tema aprenderemos a calcular el Mínimo Común Múltiplo (MCM) y el Máximo Común Divisor (MCD).

---

## 📖 Máximo Común Divisor (MCD)

El **MCD** es el mayor número que divide exactamente a dos o más números.

### Método por factorización

1. Descomponer en factores primos
2. Tomar los factores **comunes** con el **menor** exponente

### Ejemplo 1

MCD de $12$ y $18$:

$$
12 = 2^2 \times 3
$$

$$
18 = 2 \times 3^2
$$

Factores comunes: $2^1$ y $3^1$

$$
\text{MCD}(12, 18) = 2 \times 3 = 6
$$

---

### Ejemplo 2

MCD de $24$ y $36$:

$$
24 = 2^3 \times 3
$$

$$
36 = 2^2 \times 3^2
$$

$$
\text{MCD}(24, 36) = 2^2 \times 3 = 12
$$

---

## 📖 Mínimo Común Múltiplo (MCM)

El **MCM** es el menor número que es múltiplo de dos o más números.

### Método por factorización

1. Descomponer en factores primos
2. Tomar **todos** los factores con el **mayor** exponente

### Ejemplo 1

MCM de $12$ y $18$:

$$
12 = 2^2 \times 3
$$

$$
18 = 2 \times 3^2
$$

Todos los factores con mayor exponente: $2^2$ y $3^2$

$$
\text{MCM}(12, 18) = 2^2 \times 3^2 = 4 \times 9 = 36
$$

---

### Ejemplo 2

MCM de $8$ y $12$:

$$
8 = 2^3
$$

$$
12 = 2^2 \times 3
$$

$$
\text{MCM}(8, 12) = 2^3 \times 3 = 24
$$

---

## 📖 Relación entre MCM y MCD

$$
\text{MCM}(a, b) \times \text{MCD}(a, b) = a \times b
$$

### Ejemplo

Para $12$ y $18$:

$$
36 \times 6 = 216 = 12 \times 18 \quad ✓
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula el MCD de $30$ y $45$.

**Ejercicio 2:** Calcula el MCM de $15$ y $20$.

**Ejercicio 3:** Calcula el MCD y MCM de $24$ y $60$.

**Ejercicio 4:** Si MCD$(a, 12) = 4$ y MCM$(a, 12) = 60$, ¿cuánto vale $a$?

---

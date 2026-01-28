---
title: "Variable Aleatoria y Valor Esperado"
---

# Variable Aleatoria y Valor Esperado

Hasta ahora hemos trabajado con eventos. Ahora damos el salto a **variables aleatorias**: números que asignamos a los resultados de un experimento. Esto abre la puerta a calcular promedios y medidas que describen comportamientos aleatorios.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una variable aleatoria
- Variables discretas vs continuas
- La función de probabilidad
- El valor esperado (esperanza matemática)
- Varianza y desviación estándar

---

## 📖 ¿Qué es una Variable Aleatoria?

> Una **variable aleatoria** (VA) es una función que asigna un **número** a cada resultado de un experimento aleatorio.

### 💡 Notación:

- Variables aleatorias: X, Y, Z (mayúsculas)
- Valores específicos: x, y, z (minúsculas)
- P(X = x) = probabilidad de que X tome el valor x

### ⚙️ Ejemplo: Lanzar 2 monedas

Experimento: Lanzar 2 monedas
Variable aleatoria X = "número de caras"

| Resultado | X |
|-----------|---|
| SS | 0 |
| SC | 1 |
| CS | 1 |
| CC | 2 |

X puede tomar valores 0, 1, o 2.

---

## 📖 Variables Discretas vs Continuas

| Tipo | Valores posibles | Ejemplos |
|------|------------------|----------|
| **Discreta** | Finitos o contables | Número de caras, goles, clientes |
| **Continua** | Infinitos en un intervalo | Peso, tiempo, temperatura |

En esta lección nos enfocamos en **discretas**.

---

## 📖 Función de Probabilidad

> La **función de probabilidad** $p(x) = P(X = x)$ asigna a cada valor posible de X su probabilidad.

### 💡 Propiedades:

1. $p(x) \geq 0$ para todo x
2. $\sum_{\text{todos los } x} p(x) = 1$

### ⚙️ Ejemplo: X = número de caras en 2 monedas

| x | P(X = x) |
|---|----------|
| 0 | 1/4 |
| 1 | 2/4 = 1/2 |
| 2 | 1/4 |
| **Total** | **1** |

---

## 📖 Valor Esperado (Esperanza)

> El **valor esperado** E(X) es el promedio ponderado de los valores de X, donde las ponderaciones son las probabilidades.

### 💡 Fórmula:

$$
E(X) = \sum_{x} x \cdot P(X = x) = \sum_{x} x \cdot p(x)
$$

### 💡 Interpretación:

El valor esperado es el valor "promedio" a largo plazo si repitiéramos el experimento muchas veces.

### ⚙️ Ejemplo: Número de caras en 2 monedas

$$
E(X) = 0 \cdot \frac{1}{4} + 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4}
$$
$$
= 0 + 0.5 + 0.5 = 1
$$

**Interpretación:** En promedio, obtendrás 1 cara al lanzar 2 monedas.

### ⚙️ Ejemplo: Dado de 6 caras

X = resultado del dado

$$
E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6}
$$
$$
= \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5
$$

---

## 📖 Varianza y Desviación Estándar

> La **varianza** mide qué tan dispersos están los valores respecto al valor esperado.

### 💡 Fórmula de varianza:

$$
Var(X) = E[(X - E(X))^2] = \sum_{x} (x - E(X))^2 \cdot p(x)
$$

### 💡 Fórmula alternativa (más fácil de calcular):

$$
Var(X) = E(X^2) - [E(X)]^2
$$

Donde $E(X^2) = \sum_{x} x^2 \cdot p(x)$

### 💡 Desviación estándar:

$$
\sigma_X = \sqrt{Var(X)}
$$

### ⚙️ Ejemplo: Dado de 6 caras

$E(X) = 3.5$

$E(X^2) = 1^2 \cdot \frac{1}{6} + 2^2 \cdot \frac{1}{6} + ... + 6^2 \cdot \frac{1}{6}$
$= \frac{1+4+9+16+25+36}{6} = \frac{91}{6} = 15.17$

$Var(X) = 15.17 - (3.5)^2 = 15.17 - 12.25 = 2.92$

$\sigma_X = \sqrt{2.92} \approx 1.71$

---

## 📖 Propiedades del Valor Esperado

### 💡 Linealidad:

$$
E(aX + b) = a \cdot E(X) + b
$$

### ⚙️ Ejemplo:

Si X es el resultado del dado y Y = 2X + 3:
$$
E(Y) = 2 \cdot E(X) + 3 = 2(3.5) + 3 = 10
$$

### 💡 Suma de variables:

$$
E(X + Y) = E(X) + E(Y)
$$

(Siempre, incluso si X e Y no son independientes)

---

## 📖 Propiedades de la Varianza

### 💡 Transformación lineal:

$$
Var(aX + b) = a^2 \cdot Var(X)
$$

(La constante b no afecta la dispersión)

### 💡 Suma de independientes:

$$
Var(X + Y) = Var(X) + Var(Y)
$$

(Solo si X e Y son independientes)

---

## 📖 Aplicación: Juegos de Azar

### ⚙️ Ejemplo: Juego con dado

Pagas $10 para jugar. Si sale 6, ganas $50. Si no, no ganas nada.

X = ganancia neta

| Resultado | X | P(X) |
|-----------|---|------|
| Sale 6 | 50 - 10 = 40 | 1/6 |
| No sale 6 | 0 - 10 = -10 | 5/6 |

$$
E(X) = 40 \cdot \frac{1}{6} + (-10) \cdot \frac{5}{6} = \frac{40 - 50}{6} = -\frac{10}{6} \approx -1.67
$$

**Interpretación:** En promedio, pierdes $1.67 por jugada. El juego no es justo (está a favor de la casa).

---

## 🔑 Resumen

| Concepto | Fórmula |
|----------|---------|
| **Valor esperado** | $E(X) = \sum x \cdot p(x)$ |
| **Varianza** | $Var(X) = E(X^2) - [E(X)]^2$ |
| **Desviación estándar** | $\sigma = \sqrt{Var(X)}$ |
| **Linealidad E** | $E(aX+b) = aE(X) + b$ |
| **Var de aX+b** | $Var(aX+b) = a^2 Var(X)$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
X tiene la siguiente distribución:

| x | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| P(X=x) | 0.1 | 0.3 | 0.4 | 0.2 |

Calcula E(X) y Var(X).

<details>
<summary>Ver solución</summary>

**E(X):**
$E(X) = 1(0.1) + 2(0.3) + 3(0.4) + 4(0.2)$
$= 0.1 + 0.6 + 1.2 + 0.8 = 2.7$

**E(X²):**
$E(X^2) = 1(0.1) + 4(0.3) + 9(0.4) + 16(0.2)$
$= 0.1 + 1.2 + 3.6 + 3.2 = 8.1$

**Var(X):**
$Var(X) = 8.1 - (2.7)^2 = 8.1 - 7.29 = 0.81$

**σ = √0.81 = 0.9**

</details>

### Ejercicio 2
En un sorteo, hay 1000 boletos. Un boleto cuesta $5. El premio es $1000.
¿Cuál es la ganancia esperada?

<details>
<summary>Ver solución</summary>

X = ganancia neta

| Resultado | X | P |
|-----------|---|---|
| Gana | 1000 - 5 = 995 | 1/1000 |
| Pierde | -5 | 999/1000 |

$E(X) = 995 \cdot \frac{1}{1000} + (-5) \cdot \frac{999}{1000}$
$= 0.995 - 4.995 = -4$

**Pérdida esperada: $4 por boleto**

(El organizador gana en promedio $4 por boleto vendido)

</details>

### Ejercicio 3
Si E(X) = 5 y Var(X) = 4, calcula E(3X - 2) y Var(3X - 2).

<details>
<summary>Ver solución</summary>

**E(3X - 2):**
$E(3X - 2) = 3 \cdot E(X) - 2 = 3(5) - 2 = 13$

**Var(3X - 2):**
$Var(3X - 2) = 3^2 \cdot Var(X) = 9(4) = 36$

(El -2 no afecta la varianza porque solo desplaza, no dispersa)

</details>

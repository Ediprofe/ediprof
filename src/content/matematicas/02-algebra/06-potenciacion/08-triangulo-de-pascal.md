# **Triángulo de Pascal**

En la lección anterior aprendimos a usar la fórmula de combinaciones $\binom{n}{k}$ para hallar los coeficientes del binomio. Pero seamos honestos: calcular factoriales una y otra vez es lento y aburrido.

Blaise Pascal popularizó una pirámide numérica mágica que nos regala todos esos coeficientes sin hacer ni una sola multiplicación.

---

## 🎯 ¿Qué vas a aprender?

- Cómo construir el Triángulo de Pascal desde cero sumando números.
- Cómo obtener los coeficientes de $(a+b)^n$ en segundos.
- Por qué la suma de cada fila es una potencia de 2.
- La simetría oculta en los números combinatorios.

---

## 🏗️ Construyendo la Pirámide

El triángulo se construye con una regla de oro: **"Cada número es la suma de los dos que tiene arriba"**.

Empezamos con un 1 en la cima. Los bordes siempre son 1.

### Paso a Paso:

**Fila 0:** (Solo el 1)
$$
1
$$

**Fila 1:** (Bordes 1)
$$
1 \quad 1
$$

**Fila 2:** (1+1=2 en el centro)
$$
1 \quad 2 \quad 1
$$

**Fila 3:** (1+2=3 y 2+1=3)
$$
1 \quad 3 \quad 3 \quad 1
$$

**Fila 4:** (1+3=4, 3+3=6, 3+1=4)
$$
1 \quad 4 \quad 6 \quad 4 \quad 1
$$

> 💡 **Dato:** Cada fila $n$ corresponde a los coeficientes de la potencia $(a+b)^n$.

---

## ⚡ Propiedades Asombrosas

### 1. Simetría de Espejo
Si cortas el triángulo por la mitad verticalmente, el lado izquierdo es idéntico al derecho.
Ejemplo Fila 4: $1, 4, 6, 4, 1$.
Esto significa que $\binom{n}{k} = \binom{n}{n-k}$.

### 2. La Suma de las Filas
¡Suma los números de cada fila y verás potencias de 2!

![Triángulo de pascal](https://cdn.ediprofe.com/img/matematicas/mwgi-triangulo-de-pascal.webp)

- Fila 0: $1 = 2^0$
- Fila 1: $1+1 = 2 = 2^1$
- Fila 2: $1+2+1 = 4 = 2^2$
- Fila 3: $1+3+3+1 = 8 = 2^3$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Construir la Fila 5

Queremos los coeficientes para $(a+b)^5$. Usamos la Fila 4 ($1, 4, 6, 4, 1$).

**Razonamiento:**
Sumamos los vecinos:
- $1$ (borde)
- $1+4 = 5$
- $4+6 = 10$
- $6+4 = 10$
- $4+1 = 5$
- $1$ (borde)

**Resultado:**

$$
\boxed{1, 5, 10, 10, 5, 1}
$$

---

### Ejemplo 2: Expansión rápida

Expande $(x + y)^3$ usando el triángulo.

**Razonamiento:**
Buscamos la Fila 3: $1, 3, 3, 1$.
Estos son los coeficientes directos.

$$
1x^3 + 3x^2y + 3xy^2 + 1y^3
$$

**Resultado:**

$$
\boxed{x^3 + 3x^2y + 3xy^2 + y^3}
$$

---

### Ejemplo 3: Coeficientes con resta

Expande $(2a - 1)^4$.

**Datos:**
- Fila 4: $1, 4, 6, 4, 1$.
- Signos: Alternados ($+, -, +, -, +$).
- Términos: $a=2a$, $b=1$.

**Razonamiento:**

$$
1(2a)^4 - 4(2a)^3(1) + 6(2a)^2(1)^2 - 4(2a)(1)^3 + 1(1)^4
$$

Calculamos potencias:

$$
16a^4 - 4(8a^3) + 6(4a^2) - 8a + 1
$$

$$
16a^4 - 32a^3 + 24a^2 - 8a + 1
$$

**Resultado:**

$$
\boxed{16a^4 - 32a^3 + 24a^2 - 8a + 1}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la Fila 6 del Triángulo de Pascal.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usamos la Fila 5 ($1, 5, 10, 10, 5, 1$).
Sumamos: $1+5=6$, $5+10=15$, $10+10=20$...

**Resultado:**
$$
\boxed{1, 6, 15, 20, 15, 6, 1}
$$

</details>

### Ejercicio 2
¿Cuál es la suma de los números de la Fila 6?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La suma es $2^n$. Aquí $n=6$.

$$
2^6 = 64
$$

**Resultado:**
$$
\boxed{64}
$$

</details>

### Ejercicio 3
Expande $(m + n)^5$ usando los coeficientes.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Fila 5: $1, 5, 10, 10, 5, 1$.

$$
m^5 + 5m^4n + 10m^3n^2 + 10m^2n^3 + 5mn^4 + n^5
$$

**Resultado:**
$$
\boxed{m^5 + 5m^4n + 10m^3n^2 + 10m^2n^3 + 5mn^4 + n^5}
$$

</details>

### Ejercicio 4
Encuentra el coeficiente del término $x^2y^2$ en $(x+y)^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En la Fila 4 ($1, 4, 6, 4, 1$), el término central corresponde a $x^2y^2$.

**Resultado:**
$$
\boxed{6}
$$

</details>

### Ejercicio 5
Expande $(x - 2)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Fila 3: $1, 3, 3, 1$. Signos alternados.

$$
x^3 - 3x^2(2) + 3x(2^2) - 2^3
$$

$$
x^3 - 6x^2 + 12x - 8
$$

**Resultado:**
$$
\boxed{x^3 - 6x^2 + 12x - 8}
$$

</details>

### Ejercicio 6
¿Cuántos números hay en la Fila 10?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La fila $n$ tiene $n+1$ números.

$$
10 + 1 = 11
$$

**Resultado:**
$$
\boxed{11}
$$

</details>

### Ejercicio 7
Calcula $\binom{7}{0} + \binom{7}{1} + \dots + \binom{7}{7}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la suma de toda la Fila 7.

$$
2^7 = 128
$$

**Resultado:**
$$
\boxed{128}
$$

</details>

### Ejercicio 8
Expande $(1 + x)^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Fila 4: $1, 4, 6, 4, 1$.

$$
1 + 4x + 6x^2 + 4x^3 + x^4
$$

**Resultado:**
$$
\boxed{1 + 4x + 6x^2 + 4x^3 + x^4}
$$

</details>

### Ejercicio 9
Si la suma de una fila es 256, ¿qué fila es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Buscamos $n$ tal que $2^n = 256$.

$$
2^8 = 256
$$

**Resultado:**
$$
\boxed{\text{Fila } 8}
$$

</details>

### Ejercicio 10
Expande $(a - b)^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Fila 2: $1, 2, 1$. Signos alternados.

$$
a^2 - 2ab + b^2
$$

**Resultado:**
$$
\boxed{a^2 - 2ab + b^2}
$$

</details>

---

## 🔑 Resumen


| Concepto | Descripción |
|----------|-------------|
| **Construcción** | Sumar los dos números de arriba. |
| **Fila $n$** | Coeficientes de $(a+b)^n$. |
| **Suma Fila** | Siempre es $2^n$. |
| **Simetría** | Se lee igual de izquierda a derecha. |

> Usa el triángulo de Pascal siempre que necesites expandir binomios rápidamente.

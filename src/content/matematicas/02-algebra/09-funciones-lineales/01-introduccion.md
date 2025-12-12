# 📈 Introducción a las Funciones Lineales

En esta lección introduciremos el concepto de función lineal, su importancia y aplicaciones en la vida cotidiana.

---

## 📖 ¿Por qué estudiar funciones lineales?

Las funciones lineales están en todas partes en nuestra vida cotidiana:

- **Salarios**: Si ganas $\$50$ por hora, tu ingreso depende linealmente de las horas trabajadas.
- **Distancia**: Si un auto viaja a velocidad constante de $80$ km/h, la distancia recorrida es proporcional al tiempo.
- **Costos**: El costo total de un taxi incluye una tarifa base más un costo por kilómetro.
- **Temperatura**: La conversión entre Celsius y Fahrenheit es una relación lineal.

---

## 📖 ¿Qué es una función?

Una **función** es una relación entre dos variables donde a cada valor de la variable independiente ($x$) le corresponde un único valor de la variable dependiente ($y$).

$$
y = f(x)
$$

Se lee "$y$ es igual a $f$ de $x$" o "$y$ es función de $x$".

---

## 📖 Función lineal: Definición

Una **función lineal** es aquella cuya gráfica es una **línea recta**. Tiene la forma:

$$
f(x) = mx + b
$$

o equivalentemente:

$$
y = mx + b
$$

donde:
- $m$ es la **pendiente** (indica la inclinación de la recta)
- $b$ es el **intercepto con el eje y** (punto donde la recta cruza el eje vertical)

---

## 📖 Ejemplos de funciones lineales

### Ejemplo 1: Salario por horas

Un trabajador gana $\$15$ por hora. Si trabaja $x$ horas, su salario es:

$$
f(x) = 15x
$$

Aquí $m = 15$ (gana $15 por hora) y $b = 0$ (no hay pago base).

| Horas ($x$) | Salario ($y$) |
|:-----------:|:-------------:|
| 0 | $\$0$ |
| 1 | $\$15$ |
| 5 | $\$75$ |
| 8 | $\$120$ |

---

### Ejemplo 2: Servicio de taxi

Un taxi cobra $\$3$ de tarifa base más $\$2$ por kilómetro. El costo de un viaje de $x$ kilómetros es:

$$
f(x) = 2x + 3
$$

Aquí $m = 2$ (costo por km) y $b = 3$ (tarifa base).

| Kilómetros ($x$) | Costo ($y$) |
|:----------------:|:-----------:|
| 0 | $\$3$ |
| 5 | $\$13$ |
| 10 | $\$23$ |

---

### Ejemplo 3: Temperatura

La conversión de Celsius a Fahrenheit es:

$$
F = \frac{9}{5}C + 32
$$

Aquí $m = \frac{9}{5} = 1.8$ y $b = 32$.

| Celsius | Fahrenheit |
|:-------:|:----------:|
| 0 | 32 |
| 20 | 68 |
| 100 | 212 |

---

## 📖 Elementos de una función lineal

### La pendiente (m)

La **pendiente** indica:
- **Cuánto cambia $y$** cuando $x$ aumenta en una unidad
- La **inclinación** de la recta

| Valor de $m$ | Tipo de recta |
|:------------:|:--------------|
| $m > 0$ | Recta ascendente (sube de izquierda a derecha) |
| $m < 0$ | Recta descendente (baja de izquierda a derecha) |
| $m = 0$ | Recta horizontal |

---

### El intercepto (b)

El **intercepto** $b$ es el valor de $y$ cuando $x = 0$. Es el punto donde la recta cruza el eje $y$.

| Valor de $b$ | Significado |
|:------------:|:------------|
| $b > 0$ | Cruza el eje $y$ arriba del origen |
| $b < 0$ | Cruza el eje $y$ abajo del origen |
| $b = 0$ | Pasa por el origen |

---

## 📖 Caso especial: Función constante

Cuando $m = 0$, la función se convierte en:

$$
f(x) = b
$$

Esta es una **función constante**. Sin importar el valor de $x$, $y$ siempre es igual a $b$.

### Ejemplo 4

$$
f(x) = 5
$$

Para cualquier valor de $x$, $f(x) = 5$. La gráfica es una línea horizontal que pasa por $y = 5$.

---

## 📖 Evaluando funciones lineales

Para evaluar una función, sustituimos el valor de $x$ en la expresión.

### Ejemplo 5

Si $f(x) = 3x - 2$, encontrar $f(4)$.

$$
f(4) = 3(4) - 2 = 12 - 2 = 10
$$

$$
\boxed{f(4) = 10}
$$

---

### Ejemplo 6

Si $f(x) = -2x + 7$, encontrar $f(-3)$.

$$
f(-3) = -2(-3) + 7 = 6 + 7 = 13
$$

$$
\boxed{f(-3) = 13}
$$

---

## 📋 Resumen

| Elemento | Símbolo | Significado |
|:---------|:-------:|:------------|
| Pendiente | $m$ | Inclinación de la recta |
| Intercepto | $b$ | Punto donde cruza el eje $y$ |
| Forma general | $y = mx + b$ | Ecuación de la recta |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Si $f(x) = 4x + 1$, calcula $f(3)$.

<details>
<summary>Ver solución</summary>

$$
f(3) = 4(3) + 1 = 13
$$

</details>

---

**Ejercicio 2:** Si $f(x) = -x + 5$, calcula $f(-2)$.

<details>
<summary>Ver solución</summary>

$$
f(-2) = -(-2) + 5 = 2 + 5 = 7
$$

</details>

---

**Ejercicio 3:** Identifica la pendiente y el intercepto de $f(x) = 2x - 3$.

<details>
<summary>Ver solución</summary>

$m = 2$ (pendiente), $b = -3$ (intercepto)

</details>

---

**Ejercicio 4:** Un plan de celular cobra $\$20$ fijos más $\$0.10$ por minuto. Escribe la función de costo.

<details>
<summary>Ver solución</summary>

$$
f(x) = 0.10x + 20
$$

</details>

---

**Ejercicio 5:** Si la pendiente es $0$, ¿qué tipo de recta es?

<details>
<summary>Ver solución</summary>

Es una recta horizontal (función constante).

</details>

---

**Ejercicio 6:** ¿La función $f(x) = 3x - 1$ es ascendente o descendente?

<details>
<summary>Ver solución</summary>

Ascendente, porque $m = 3 > 0$.

</details>

---

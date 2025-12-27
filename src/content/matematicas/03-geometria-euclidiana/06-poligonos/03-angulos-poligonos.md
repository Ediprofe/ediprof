# **Ángulos en Polígonos**

Cada vez que agregas un lado a un polígono, sus ángulos internos aumentan. Un triángulo suma $180^\circ$, un cuadrado $360^\circ$... ¿y uno de 20 lados? Vamos a descubrir el patrón perfecto que gobierna estas formas.

---

## 🎯 ¿Qué vas a aprender?

- Calcular la **suma** de los ángulos interiores de cualquier polígono.
- Calcular cuánto mide cada ángulo **individual** en un polígono regular.
- Entender por qué los ángulos exteriores siempre suman $360^\circ$ (la regla del giro completo).
- Hallar el número de lados sabiendo el valor de un ángulo.

---

## 📐 Suma de Ángulos Interiores

El secreto para entender cualquier polígono es dividirlo en triángulos.

1.  Elige un vértice.
2.  Traza todas las diagonales posibles desde ahí.
3.  El polígono queda dividido en **$n-2$ triángulos**.

Como cada triángulo suma $180^\circ$:

$$
S_{\text{int}} = 180^\circ \times (n-2)
$$

Donde $n$ es el número de lados.

### Tabla rápida:
- **Triángulo ($n=3$):** $180^\circ \times 1 = 180^\circ$
- **Cuadrilátero ($n=4$):** $180^\circ \times 2 = 360^\circ$
- **Pentágono ($n=5$):** $180^\circ \times 3 = 540^\circ$

---

## 📏 Ángulo Interior Individual

Si (y solo si) el polígono es **regular** (todos sus ángulos son iguales), podemos saber cuánto mide cada uno dividiendo la suma total entre el número de ángulos ($n$).

$$
\text{Ángulo interior} = \frac{180^\circ (n-2)}{n}
$$

---

## 🔄 Ángulos Exteriores (La regla mágica)

Imagina que caminas por el borde de un polígono. En cada vértice giras un poco para seguir el contorno. Al terminar de dar la vuelta completa y volver al inicio, ¿cuánto has girado en total? ¡Exactamente una vuelta completa!

> **Regla:** La suma de los ángulos exteriores de cualquier polígono convexo es **siempre $360^\circ$**. No importa si tiene 3 lados o 1000 lados.

$$
S_{\text{ext}} = 360^\circ
$$

### Ángulo Exterior Individual (Polígono Regular)
Como son todos iguales:

$$
\text{Ángulo exterior} = \frac{360^\circ}{n}
$$

> **Truco Pro:** Es mucho más fácil calcular el ángulo exterior primero ($360/n$) y luego hallar el interior usando que son suplementarios ($180 - \text{ext}$).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Suma de ángulos de un Dodecágono

Calcula la suma de los ángulos interiores de un polígono de 12 lados.

**Razonamiento:**
Usamos la fórmula $n=12$.
Triángulos formados: $12 - 2 = 10$.

$$
S = 180^\circ \times 10
$$

**Resultado:**
$$
\boxed{1800^\circ}
$$

### Ejemplo 2: Ángulo de un Octágono Regular

¿Cuánto mide cada ángulo interno de una señal de PARE?

**Método A (Fórmula directa):**
$$
\frac{180(8-2)}{8} = \frac{180 \times 6}{8} = \frac{1080}{8} = 135^\circ
$$

**Método B (Vía ángulo exterior - RECOMENDADO):**
Ángulo exterior = $360 / 8 = 45^\circ$.
Ángulo interior = $180 - 45 = 135^\circ$.

**Resultado:**
$$
\boxed{135^\circ}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la suma de los ángulos interiores de un heptágono ($n=7$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
S = 180(7-2) = 180(5)
$$

**Resultado:**
$$
\boxed{900^\circ}
$$

</details>

### Ejercicio 2
¿Cuánto mide cada ángulo exterior de un triángulo equilátero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\text{Ext} = \frac{360}{3}
$$

**Resultado:**
$$
\boxed{120^\circ}
$$

</details>

### Ejercicio 3
Si la suma de los ángulos interiores es $1080^\circ$, ¿cuántos lados tiene el polígono?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
180(n-2) = 1080
$$

$$
n-2 = \frac{1080}{180} = 6
$$

$$
n = 6+2
$$

**Resultado:**
$$
\boxed{8 \text{ lados (Octágono)}}
$$

</details>

### Ejercicio 4
Un polígono tiene un ángulo exterior de $36^\circ$. Si es regular, ¿cuántos lados tiene?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\frac{360}{n} = 36
$$

$$
n = \frac{360}{36}
$$

**Resultado:**
$$
\boxed{10 \text{ lados (Decágono)}}
$$

</details>

### Ejercicio 5
Calcula el ángulo interior de un hexágono regular.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\text{Ext} = \frac{360}{6} = 60^\circ
$$
$$
\text{Int} = 180 - 60 = 120^\circ
$$

**Resultado:**
$$
\boxed{120^\circ}
$$

</details>

### Ejercicio 6
Verdadero o Falso: La suma de los ángulos exteriores de un icoságono (20 lados) es mayor que la de un cuadrado.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. La suma exterior siempre es $360^\circ$ para cualquier polígono convexo.

**Resultado:**
$$
\boxed{\text{Falso, son iguales}}
$$

</details>

### Ejercicio 7
En un pentágono irregular, cuatro ángulos suman $400^\circ$. Halla el quinto ángulo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Total pentágono = $540^\circ$.

$$
x = 540 - 400
$$

**Resultado:**
$$
\boxed{140^\circ}
$$

</details>

### Ejercicio 8
¿Existe un polígono regular cuyo ángulo interior mida $100^\circ$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si Int = 100, entonces Ext = 80.
$n = 360 / 80 = 4.5$.
Como $n$ debe ser entero, no existe.

**Resultado:**
$$
\boxed{\text{No}}
$$

</details>

### Ejercicio 9
Calcula la suma de ángulos interiores de un polígono de 15 lados.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
180(15-2) = 180 \times 13
$$

**Resultado:**
$$
\boxed{2340^\circ}
$$

</details>

### Ejercicio 10
El ángulo interior de un polígono regular es 5 veces su ángulo exterior. Halla $n$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Int = $5x$, Ext = $x$.
Sabemos que Int + Ext = 180.
$5x + x = 180 \Rightarrow 6x = 180 \Rightarrow x = 30^\circ$.
Ext = 30.
$n = 360 / 30 = 12$.

**Resultado:**
$$
\boxed{12 \text{ lados}}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Notas |
| :--- | :--- | :--- |
| **Suma Interior** | $180(n-2)$ | Crece con $n$. |
| **Suma Exterior** | $360^\circ$ | Constante siempre. |
| **Ángulo Int.** (Regular) | $\frac{180(n-2)}{n}$ | $180 - \text{Ext}$. |
| **Ángulo Ext.** (Regular) | $\frac{360}{n}$ | La más fácil de usar. |

> Todo se reduce a triángulos ($180^\circ$) y giros completos ($360^\circ$).

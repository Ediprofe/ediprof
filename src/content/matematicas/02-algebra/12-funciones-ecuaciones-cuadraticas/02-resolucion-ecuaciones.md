# **Resolución de Ecuaciones Cuadráticas**

¿Recuerdas cuando $x$ valía solo una cosa? Bueno, en el mundo cuadrático, $x$ suele tener doble personalidad. Resolver una ecuación como $x^2 = 9$ significa encontrar *todos* los números que al cuadrado den 9 (¡3 y -3!). Aquí aprenderás las tres herramientas maestras: factorizar, completar el cuadrado y la famosa fórmula general.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa "raíz" o "cero" de una ecuación.
- Factorizar trinomios para encontrar soluciones rápidas.
- Usar la fórmula general "la vieja confiable".
- Saber cuántas soluciones tiene una ecuación con el discriminante.

---

## 🔍 ¿Qué estamos buscando?

Resolver $ax^2 + bx + c = 0$ es encontrar los valores de $x$ donde la parábola corta al eje horizontal (eje $X$).

- **Dos cortes:** La ecuación tiene 2 soluciones reales.
- **Un corte:** La ecuación tiene 1 solución real (el vértice toca el eje).
- **Cero cortes:** La parábola flota sobre (o bajo) el eje. No hay solución real.

---

## 🛠️ Método 1: Factorización

La herramienta más rápida. Si $A \cdot B = 0$, entonces obligatoriamente $A=0$ o $B=0$.

### Ejemplo 1: Trinomio Simple
Resolver $x^2 - 5x + 6 = 0$.

**Paso 1: Factorizar**
Buscamos dos números que multiplicados den 6 y sumados den -5.
¡Son -2 y -3!
$$
(x - 2)(x - 3) = 0
$$

**Paso 2: Igualar a cero**
- $x - 2 = 0 \implies x = 2$
- $x - 3 = 0 \implies x = 3$

**Resultado:**
$$
\boxed{x = 2, \quad x = 3}
$$

### Ejemplo 2: Diferencia de Cuadrados
Resolver $x^2 - 9 = 0$.

**Paso 1: Factorizar**
$$
(x - 3)(x + 3) = 0
$$

**Paso 2: Igualar**
- $x - 3 = 0 \implies x = 3$
- $x + 3 = 0 \implies x = -3$

**Resultado:**
$$
\boxed{x = 3, \quad x = -3}
$$

---

## 🧪 Método 2: Fórmula General

Cuando no se puede factorizar fácil, usamos la "fórmula del estudiante":

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Ejemplo 3: No factorizable
Resolver $2x^2 + 5x - 3 = 0$.

**Datos:** $a=2, b=5, c=-3$.

**Sustitución:**
$$
x = \frac{-5 \pm \sqrt{5^2 - 4(2)(-3)}}{2(2)}
$$
$$
x = \frac{-5 \pm \sqrt{25 + 24}}{4}
$$
$$
x = \frac{-5 \pm \sqrt{49}}{4} = \frac{-5 \pm 7}{4}
$$

**Dos caminos:**
1.  $x_1 = (-5 + 7)/4 = 2/4 = 0.5$
2.  $x_2 = (-5 - 7)/4 = -12/4 = -3$

**Resultado:**
$$
\boxed{x = 0.5, \quad x = -3}
$$

### Ejemplo 4: Raíces no exactas
Resolver $x^2 - 4x + 1 = 0$.

**Sustitución:**
$$
x = \frac{4 \pm \sqrt{16 - 4(1)(1)}}{2}
$$
$$
x = \frac{4 \pm \sqrt{12}}{2}
$$
Como $\sqrt{12} = \sqrt{4 \cdot 3} = 2\sqrt{3}$:
$$
x = \frac{4 \pm 2\sqrt{3}}{2} = 2 \pm \sqrt{3}
$$

**Resultado:**
$$
\boxed{x \approx 3.73, \quad x \approx 0.27}
$$

---

## 🔮 El Discriminante ($\Delta$)

Lo que está dentro de la raíz ($b^2 - 4ac$) nos dice el futuro:

- $\Delta > 0$: **Dos** soluciones reales.
- $\Delta = 0$: **Una** solución real (repetida).
- $\Delta < 0$: **Cero** soluciones reales (la raíz de un negativo no existe en los reales).

### Ejemplo 5: Solución Única
Resolver $x^2 - 6x + 9 = 0$.

$$
\Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0
$$
$$
x = \frac{6 \pm 0}{2} = 3
$$

**Resultado:**
$$
\boxed{x = 3}
$$

### Ejemplo 6: Sin Solución
Resolver $x^2 + x + 1 = 0$.

$$
\Delta = (1)^2 - 4(1)(1) = 1 - 4 = -3
$$
Como $\sqrt{-3}$ no es real:

**Resultado:**
$$
\boxed{\text{No tiene solución real}}
$$

---

## 🏛️ Método 3: Completar el Cuadrado

Transformamos el trinomio en un cuadrado perfecto $(x+k)^2$.

### Ejemplo 7
Resolver $x^2 + 6x + 5 = 0$.

1.  Mover el término $c$: $x^2 + 6x = -5$.
2.  Sumar $(b/2)^2$: $(6/2)^2 = 9$.
    $$
    x^2 + 6x + 9 = -5 + 9
    $$
3.  Factorizar:
    $$
    (x + 3)^2 = 4
    $$
4.  Sacar raíz:
    $$
    x + 3 = \pm 2
    $$
5.  Despejar:
    - $x = -3 + 2 = -1$
    - $x = -3 - 2 = -5$

**Resultado:**
$$
\boxed{x = -1, \quad x = -5}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve $x^2 - 7x + 12 = 0$ factorizando.

<details>
<summary>Ver solución</summary>

Dos números que multiplicados den 12 y sumados -7: -3 y -4.
$(x-3)(x-4)=0$.
**Resultado:** $\boxed{3, 4}$

</details>

---

### Ejercicio 2
Resuelve $3x^2 = 27$ despejando.

<details>
<summary>Ver solución</summary>

$x^2 = 9 \implies x = \pm 3$.
**Resultado:** $\boxed{3, -3}$

</details>

---

### Ejercicio 3
Calcula el discriminante de $x^2 - 2x + 10 = 0$.

<details>
<summary>Ver solución</summary>

$\Delta = (-2)^2 - 4(1)(10) = 4 - 40 = -36$.
**Resultado:** $\boxed{-36 \text{ (Sin solución)}}$

</details>

---

### Ejercicio 4
Resuelve $x^2 + 5x = 0$ factorizando $x$.

<details>
<summary>Ver solución</summary>

$x(x + 5) = 0$.
**Resultado:** $\boxed{0, -5}$

</details>

---

### Ejercicio 5
Resuelve $x^2 + 2x - 8 = 0$ con fórmula general.

<details>
<summary>Ver solución</summary>

$\frac{-2 \pm \sqrt{4+32}}{2} = \frac{-2 \pm 6}{2}$.
**Resultado:** $\boxed{2, -4}$

</details>

---

### Ejercicio 6
Resuelve $(x-2)^2 = 25$.

<details>
<summary>Ver solución</summary>

$x-2 = \pm 5$.
$x = 7$ o $x = -3$.
**Resultado:** $\boxed{7, -3}$

</details>

---

### Ejercicio 7
Encuentra las raíces de $2x^2 + 8x + 8 = 0$.

<details>
<summary>Ver solución</summary>

Simplifica entre 2: $x^2 + 4x + 4 = 0$.
$(x+2)^2 = 0$.
**Resultado:** $\boxed{-2}$

</details>

---

### Ejercicio 8
¿Cuántas soluciones tiene $5x^2 - 3x + 1 = 0$?

<details>
<summary>Ver solución</summary>

$\Delta = 9 - 20 = -11$.
**Resultado:** $\boxed{0}$

</details>

---

### Ejercicio 9
Resuelve $x^2 + 9 = 0$.

<details>
<summary>Ver solución</summary>

$x^2 = -9$. Raíz de negativo.
**Resultado:** $\boxed{\text{Sin Solución Real}}$

</details>

---

### Ejercicio 10
Resuelve $x^2 - x - 2 = 0$.

<details>
<summary>Ver solución</summary>

$(x-2)(x+1) = 0$.
**Resultado:** $\boxed{2, -1}$

</details>

---

## 🔑 Resumen

| Método | Cuándo usarlo |
|:--- |:--- |
| **Despeje Simple** | Si no hay término $bx$ (ej: $x^2=9$). |
| **Factorización** | Cuando los números son "bonitos" y enteros. |
| **Fórmula General** | Siempre funciona, pero es más lenta. |
| **Discriminante** | Solo quieres saber *cuántas* soluciones hay. |

> **Conclusión:** No todas las ecuaciones tienen solución, y algunas tienen dos. Aprender a leer el discriminante te evitará buscar soluciones fantasma.

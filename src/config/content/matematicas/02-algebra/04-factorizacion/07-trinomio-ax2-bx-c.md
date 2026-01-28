---
title: "Trinomio de la forma ax² + bx + c"
---

# **Trinomio de la forma ax² + bx + c**

En lecciones anteriores aprendimos a factorizar trinomios donde el coeficiente de $x^2$ es 1. Ahora veremos qué hacer cuando ese coeficiente es diferente de 1. Para resolver estos trinomios, existen tres métodos principales que nos permiten llegar al mismo resultado.

---

## 🎯 ¿Qué vas a aprender?

- A identificar trinomios con coeficiente principal distinto de 1.
- El **Método de Reducción** para convertir un trinomio difícil en uno simple de una vez.
- El **Método de Agrupación** para factorizar paso a paso mediante el producto AC.
- El **Método de Tanteo** para factorizar mediante inspección cruzada.
- A elegir el mejor método según tu preferencia y el problema.

---

## 🏗️ Método 1: Reducción a la forma simple

Este es un método muy potente que transforma de inmediato nuestro trinomio de la forma $ax^2 + bx + c$ ($a \neq 1$) en uno de la forma $x^2 + bx + c$ ($a = 1$) mediante un truco matemático. 

### Pasos del Método

Consiste en **multiplicar y dividir por el mismo coeficiente $a$** en un solo paso:

1.  Multiplicamos y dividimos todo el trinomio por $a$. Al multiplicar, el primer término queda como $(ax)^2$, el término central queda con el factor indicado $b(ax)$ y el último término se multiplica directamente $ac$.
2.  Factorizamos el trinomio de arriba buscando dos números que multipliquen $ac$ y sumen $b$.
3.  Simplificamos la fracción dividiendo para eliminar el denominador $a$.

---

### Ejemplo 1: El truco de multiplicar y dividir de una vez

Factoriza usando reducción: $6x^2 - 7x - 3$

**Datos:**
- $a = 6$, $b = -7$, $c = -3$

**Razonamiento:**

1. **Multiplicamos y dividimos por 6 directamente:**

$$
\frac{(6x)^2 - 7(6x) - 18}{6}
$$

2. **Factorizamos el trinomio de arriba:** Buscamos dos números que multipliquen **-18** y sumen **-7**. Estos son **-9** y **+2**.
   Escribimos los paréntesis usando $6x$ como nuestra variable:

$$
\frac{(6x - 9)(6x + 2)}{6}
$$

3. **Simplificamos:** Descomponemos el denominador $6$ en $3 \times 2$ para que divida exactamente a cada paréntesis:

$$
\frac{(6x - 9)}{3} \cdot \frac{(6x + 2)}{2} = (2x - 3)(3x + 1)
$$

**Resultado:** $\boxed{(2x - 3)(3x + 1)}$

---

## 🏗️ Método 2: Agrupación (Producto AC)

Este método es muy estructurado. Consiste en convertir el trinomio de 3 términos en un polinomio de 4 términos para poder aplicar factor común por agrupación.

### Pasos del Método

1. Multiplica el primer coeficiente ($a$) por el último ($c$) para obtener el **Producto AC**.
2. Busca dos números que **multiplicados** den el Producto AC y **sumados** den el término central $b$.
3. Reescribe el trinomio sustituyendo el término central por la suma de estos dos números.
4. Factoriza por agrupación sacando el factor común por parejas.

---

### Ejemplo 2: Agrupación paso a paso

Factoriza: $2x^2 + 7x + 3$

**Datos:**
- $a = 2$, $b = 7$, $c = 3$
- Producto AC = $2 \times 3 = 6$

**Razonamiento:**

1. Buscamos números que multipliquen 6 y sumen 7. Son **6** y **1**.

2. Abrimos el centro:

$$
2x^2 + 6x + x + 3
$$

3. Agrupamos por parejas:

$$
(2x^2 + 6x) + (x + 3)
$$

4. Sacamos factor común de cada grupo:

$$
2x(x + 3) + 1(x + 3)
$$

5. Como el bloque $(x + 3)$ se repite, lo extraemos:

**Resultado:** $\boxed{(x + 3)(2x + 1)}$

---

## 🏗️ Método 3: Tanteo (Inspección)

Este método consiste en probar combinaciones de factores de los términos extremos hasta que la suma cruzada coincida con el término central. Es muy rápido cuando los números son pequeños.

### Pasos del Método

1. Descompón el primer término ($ax^2$) en dos factores.
2. Descompón el último término ($c$) en dos factores.
3. Prueba combinaciones multiplicando en cruz.
4. Si la suma de estos productos cruzados es igual al término central, has encontrado los binomios correctos.

---

### Ejemplo 3: Tanteo básico

Factoriza: $2x^2 + 5x + 2$

**Razonamiento:**

1. Factores de $2x^2$: $(2x)$ y $(x)$.
2. Factores de $2$: $(1)$ y $(2)$.
3. Probamos la combinación:

$$
(2x + 1)(x + 2)
$$

4. Verificamos en cruz:

$$
2x \cdot 2 = 4x \quad \text{y} \quad x \cdot 1 = x
$$

5. Suma:

$$
4x + x = 5x
$$

¡Coincide con el centro!

**Resultado:** $\boxed{(2x + 1)(x + 2)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Factoriza: $2x^2 + 9x + 4$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 8, Suma = 9. Números: 8 y 1.

**Razonamiento:**

$$
2x^2 + 8x + x + 4 = 2x(x+4) + 1(x+4)
$$

**Resultado:** $\boxed{(x + 4)(2x + 1)}$

</details>

### Ejercicio 2
Factoriza: $3x^2 + 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** Multiplicamos y dividimos por 3. AC = 6, Suma = 7. Números: 6 y 1.

**Razonamiento:**

$$
\frac{(3x)^2 + 7(3x) + 6}{3} = \frac{(3x+6)(3x+1)}{3}
$$

Simplificando:

$$
(x+2)(3x+1)
$$

**Resultado:** $\boxed{(x + 2)(3x + 1)}$

</details>

### Ejercicio 3
Factoriza: $2x^2 + 11x + 5$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 10, Suma = 11. Números: 10 y 1.

**Razonamiento:**

$$
2x^2 + 10x + x + 5 = 2x(x+5) + 1(x+5)
$$

**Resultado:** $\boxed{(x + 5)(2x + 1)}$

</details>

### Ejercicio 4
Factoriza: $6x^2 - 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 12, Suma = -7. Números: -4 y -3.

**Razonamiento:**

$$
\frac{(6x-4)(6x-3)}{2 \times 3}
$$

Simplificando:

$$
(3x - 2)(2x - 1)
$$

**Resultado:** $\boxed{(3x - 2)(2x - 1)}$

</details>

### Ejercicio 5
Factoriza: $5x^2 + 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 10, Suma = 7. Números: 5 y 2.

**Razonamiento:**

$$
5x^2 + 5x + 2x + 2 = 5x(x+1) + 2(x+1)
$$

**Resultado:** $\boxed{(x + 1)(5x + 2)}$

</details>

### Ejercicio 6
Factoriza: $4x^2 - 15x - 4$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -16, Suma = -15. Números: -16 y 1.

**Razonamiento:**

$$
\frac{(4x-16)(4x+1)}{4}
$$

Simplificando:

$$
(x - 4)(4x + 1)
$$

**Resultado:** $\boxed{(x - 4)(4x + 1)}$

</details>

### Ejercicio 7
Factoriza: $3x^2 - 14x - 5$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -15, Suma = -14. Números: -15 y 1.

**Razonamiento:**

$$
3x^2 - 15x + x - 5 = 3x(x-5) + 1(x-5)
$$

**Resultado:** $\boxed{(x - 5)(3x + 1)}$

</details>

### Ejercicio 8
Factoriza: $2x^2 - 5x - 3$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -6, Suma = -5. Números: -6 y 1.

**Razonamiento:**

$$
\frac{(2x-6)(2x+1)}{2}
$$

Simplificando:

$$
(x - 3)(2x + 1)
$$

**Resultado:** $\boxed{(x - 3)(2x + 1)}$

</details>

### Ejercicio 9
Factoriza: $6x^2 + x - 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -12, Suma = 1. Números: 4 y -3.

**Razonamiento:**

$$
\frac{(6x+4)(6x-3)}{2 \cdot 3}
$$

Simplificando:

$$
(3x + 2)(2x - 1)
$$

**Resultado:** $\boxed{(3x + 2)(2x - 1)}$

</details>

### Ejercicio 10
Factoriza: $4x^2 + 18x + 8$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Primero sacamos factor común 2:

$$
2(2x^2 + 9x + 4)
$$

Luego factorizamos el trinomio interno (AC = 8, números 8 y 1):

$$
2[2x(x+4) + 1(x+4)] = 2(x+4)(2x+1)
$$

**Resultado:** $\boxed{2(2x + 1)(x + 4)}$

</details>

### Ejercicio 11
Factoriza usando Reducción: $3x^2 - 5x - 2$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Multiplicamos y dividimos por 3:

$$
\frac{(3x)^2 - 5(3x) - 6}{3}
$$

Buscamos factores de -6 que sumen -5: -6 y 1.

$$
\frac{(3x-6)(3x+1)}{3}
$$

Simplificando:

$$
(x - 2)(3x + 1)
$$

**Resultado:** $\boxed{(x - 2)(3x + 1)}$

</details>

### Ejercicio 12
Factoriza: $5x^2 + 13x - 6$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -30, Suma = 13. Números: 15 y -2.

**Razonamiento:**

$$
\frac{(5x+15)(5x-2)}{5}
$$

Simplificando:

$$
(x + 3)(5x - 2)
$$

**Resultado:** $\boxed{(x + 3)(5x - 2)}$

</details>

### Ejercicio 13
Factoriza: $6x^2 + 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 12, Suma = 7. Números: 4 y 3.

**Razonamiento:**

$$
\frac{(6x+4)(6x+3)}{2 \cdot 3}
$$

Simplificando:

$$
(3x + 2)(2x + 1)
$$

**Resultado:** $\boxed{(3x + 2)(2x + 1)}$

</details>

### Ejercicio 14
Factoriza: $2x^2 - 7x + 3$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 6, Suma = -7. Números: -6 y -1.

**Razonamiento:**

$$
\frac{(2x-6)(2x-1)}{2}
$$

Simplificando:

$$
(x - 3)(2x - 1)
$$

**Resultado:** $\boxed{(x - 3)(2x - 1)}$

</details>

### Ejercicio 15
Factoriza: $8x^2 - 14x + 3$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 24, Suma = -14. Números: -12 y -2.

**Razonamiento:**

$$
\frac{(8x-12)(8x-2)}{4 \cdot 2}
$$

Simplificando:

$$
(2x - 3)(4x - 1)
$$

**Resultado:** $\boxed{(2x - 3)(4x - 1)}$

</details>

---

## 🔑 Resumen

| Método | Cuándo usarlo | Ventaja |
| :--- | :--- | :--- |
| **Reducción** ($ax$) | Si buscas rapidez transformando a trinomio simple | Te permite usar lo que ya sabes del caso anterior |
| **Agrupación** ($AC$) | Cuando prefieres un camino lógico y seguro | Evitas confusiones con la división final |
| **Tanteo** | Cuando los coeficientes son pequeños | Ahorra mucho espacio y tiempo con práctica |

> Todos los métodos te llevarán a la expresión correcta. ¡Elige el que te resulte más natural y no olvides verificar siempre multiplicando tus binomios!

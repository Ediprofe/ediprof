---
title: "División de Fracciones Algebraicas"
---

# **División de Fracciones Algebraicas**

¿Sabías que dividir fracciones no requiere realmente una "división" tradicional? El secreto está en multiplicar, pero de una forma especial: **en cruz**. Es como tejer una trenza: el numerador de la primera se une con el denominador de la segunda, y viceversa. Este método directo te ahorrará pasos y confusiones.

---

## 🎯 ¿Qué vas a aprender?

- El método de la multiplicación en cruz (zig-zag).
- Por qué ya no necesitas "darle la vuelta" a nada.
- A simplificar divisiones complejas con polinomios.
- Cómo manejar enteros dentro de una división de fracciones.

---

## 🔍 El Método de la Multiplicación en Cruz

Para dividir dos fracciones, multiplicamos los términos en forma de **X** o zig-zag.

**La Regla de Oro:**

$$
\boxed{\frac{A}{B} \div \frac{C}{D} = \frac{A \cdot D}{B \cdot C}}
$$

**El proceso paso a paso:**
1.  **Flecha hacia arriba ($A \cdot D$):** Multiplica el numerador de la primera por el denominador de la segunda. El resultado va **ARRIBA**.
2.  **Flecha hacia abajo ($B \cdot C$):** Multiplica el denominador de la primera por el numerador de la segunda. El resultado va **ABAJO**.
3.  **Simplifica:** Una vez tienes la fracción resultante, factoriza y cancela términos repetidos.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: División de Monomios
Divide: $\dfrac{4x^2}{3y} \div \dfrac{2x}{9y^2}$

**Datos:**
- **Arriba (A):** $4x^2$
- **Abajo (B):** $3y$
- **Arriba (C):** $2x$
- **Abajo (D):** $9y^2$

**Razonamiento:**

1. **Multiplicamos cruzado:**
   - Numerador final: $4x^2 \cdot 9y^2$
   - Denominador final: $3y \cdot 2x$

$$
\frac{4x^2 \cdot 9y^2}{3y \cdot 2x}
$$

2. **Operamos los números y letras:**
   - Arriba: $36x^2y^2$
   - Abajo: $6xy$

$$
\frac{36x^2y^2}{6xy}
$$

3. **Simplificamos:**
   - $36 \div 6 = 6$
   - $x^2 \div x = x$
   - $y^2 \div y = y$

**Resultado:** $\boxed{6xy}$

---

### Ejemplo 2: Polinomios Simples
Divide: $\dfrac{2x+6}{5} \div \dfrac{x+3}{10}$

**Razonamiento:**

1. **Armamos la cruz** (dejado indicado para simplificar después):
   - Arriba: $(2x+6) \cdot 10$
   - Abajo: $5 \cdot (x+3)$

$$
\frac{10(2x+6)}{5(x+3)}
$$

2. **Factorizamos** lo que se pueda ($2x+6 = 2(x+3)$):

$$
\frac{10 \cdot 2(x+3)}{5(x+3)}
$$

3. **Cancelamos** y operamos:
   - Se va el paquete $(x+3)$.
   - Queda $\frac{20}{5}$

**Resultado:** $\boxed{4}$

---

### Ejemplo 3: Diferencia de Cuadrados
Divide: $\dfrac{x^2-16}{x+2} \div \dfrac{x-4}{x+2}$

**Datos:**
- $x^2-16$ es $(x+4)(x-4)$.

**Razonamiento:**

1. **Multiplicación en cruz:**

$$
\frac{(x^2-16) \cdot (x+2)}{(x+2) \cdot (x-4)}
$$

2. **Factorizamos el numerador:**

$$
\frac{(x+4)(x-4) \cdot (x+2)}{(x+2) \cdot (x-4)}
$$

3. **Cancelación masiva:**
   - El $(x-4)$ se va con el $(x-4)$.
   - El $(x+2)$ se va con el $(x+2)$.

4. Solo nos queda el factor sobreviviente.

**Resultado:** $\boxed{x+4}$

---

### Ejemplo 4: Trinomios
Divide: $\dfrac{x^2+5x+6}{x-3} \div \dfrac{x+2}{x-3}$

**Razonamiento:**

1. **Cruzamos:**
   - Numerador: $(x^2+5x+6) \cdot (x-3)$
   - Denominador: $(x-3) \cdot (x+2)$

$$
\frac{(x^2+5x+6)(x-3)}{(x-3)(x+2)}
$$

2. **Factorizamos** el trinomio $x^2+5x+6 \to (x+3)(x+2)$:

$$
\frac{(x+3)(x+2)(x-3)}{(x-3)(x+2)}
$$

3. **Simplificamos:**
   - Tachamos $(x+2)$ arriba y abajo.
   - Tachamos $(x-3)$ arriba y abajo.

**Resultado:** $\boxed{x+3}$

---

### Ejemplo 5: División de entero por fracción
Divide: $(x^2 - 9) \div \dfrac{x+3}{2}$

**Truco:** Ponle un 1 debajo al entero para verlo como fracción: $\frac{x^2-9}{1}$.

**Razonamiento:**

1. **Multiplicación en cruz:**
   - Arriba: $(x^2-9) \cdot 2$
   - Abajo: $1 \cdot (x+3)$

$$
\frac{2(x^2-9)}{x+3}
$$

2. **Factorizamos** la diferencia de cuadrados:

$$
\frac{2(x+3)(x-3)}{x+3}
$$

3. **Simplificamos:**
   - Se va el factor $(x+3)$.
   - Nos queda $2(x-3)$.

**Resultado:** $\boxed{2x-6}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Divide $\dfrac{10a^2}{3b} \div \dfrac{5a}{6b}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Cruzamos: $(10a^2 \cdot 6b)$ arriba, $(3b \cdot 5a)$ abajo.

$$
\frac{60a^2b}{15ab}
$$

Simplificamos: $60/15=4$, $a^2/a=a$, $b/b=1$.

**Resultado:** $\boxed{4a}$

</details>

### Ejercicio 2
Divide $\dfrac{3x}{y} \div 6x$.

<details>
<summary>Ver solución</summary>

**Datos:** $6x = \frac{6x}{1}$.
**Razonamiento:** 
Cruzamos: $3x \cdot 1$ arriba, $y \cdot 6x$ abajo.

$$
\frac{3x}{6xy}
$$

Simplificamos $3/6 = 1/2$ y las $x$.

**Resultado:** $\boxed{\frac{1}{2y}}$

</details>

### Ejercicio 3
Divide $\dfrac{x+5}{x-1} \div \dfrac{x+5}{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Cruzamos.

$$
\frac{(x+5) \cdot 2}{(x-1) \cdot (x+5)}
$$

Cancelamos $(x+5)$.

**Resultado:** $\boxed{\frac{2}{x-1}}$

</details>

### Ejercicio 4
Divide $\dfrac{x^2-1}{x} \div \dfrac{x+1}{x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Factorizamos $x^2-1 = (x+1)(x-1)$.
Cruzamos:

$$
\frac{(x+1)(x-1) \cdot x}{x \cdot (x+1)}
$$

Cancelamos $x$ y $(x+1)$.

**Resultado:** $\boxed{x-1}$

</details>

### Ejercicio 5
Divide $\dfrac{4x-8}{3} \div \dfrac{x-2}{6}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Cruzamos:

$$
\frac{6 \cdot 4(x-2)}{3 \cdot (x-2)}
$$

Cancelamos $(x-2)$. Queda $\frac{24}{3}$.

**Resultado:** $\boxed{8}$

</details>

### Ejercicio 6
Divide $\dfrac{x^2-2x+1}{x^2+x} \div \dfrac{x-1}{x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Factorizamos: $(x-1)^2$ y $x(x+1)$.
Cruzamos:

$$
\frac{(x-1)^2 \cdot x}{x(x+1) \cdot (x-1)}
$$

Cancelamos una $x$ y un $(x-1)$.

**Resultado:** $\boxed{\frac{x-1}{x+1}}$

</details>

### Ejercicio 7
Divide $\dfrac{a^2-b^2}{2} \div (a+b)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
$(a+b)$ tiene un 1 abajo.
Cruzamos:

$$
\frac{(a+b)(a-b) \cdot 1}{2 \cdot (a+b)}
$$

Cancelamos $(a+b)$.

**Resultado:** $\boxed{\frac{a-b}{2}}$

</details>

### Ejercicio 8
Divide $\dfrac{1}{x^2-9} \div \dfrac{1}{x-3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Cruzamos: $1 \cdot (x-3)$ arriba, $(x^2-9) \cdot 1$ abajo.

$$
\frac{x-3}{(x+3)(x-3)}
$$

**Resultado:** $\boxed{\frac{1}{x+3}}$

</details>

### Ejercicio 9
Divide $\dfrac{x^2+7x+12}{x} \div \dfrac{x+4}{2x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Cruzamos.

$$
\frac{(x+4)(x+3) \cdot 2x}{x \cdot (x+4)}
$$

Cancelamos $x$ y $(x+4)$. Queda $2(x+3)$.

**Resultado:** $\boxed{2x+6}$

</details>

### Ejercicio 10
Divide $\dfrac{x^3}{y^2} \div \dfrac{x^2}{y^3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Cruzamos: $x^3 \cdot y^3$ arriba, $y^2 \cdot x^2$ abajo.

$$
\frac{x^3y^3}{x^2y^2}
$$

Restamos exponentes: $3-2=1$.

**Resultado:** $\boxed{xy}$

</details>

---

## 🔑 Resumen

Para dividir fracciones algebraicas, usa la **multiplicación cruzada**:

| Paso | Acción |
| :--- | :--- |
| **1. Arriba** | Numerador 1 $\times$ Denominador 2 |
| **2. Abajo** | Denominador 1 $\times$ Numerador 2 |
| **3. Final** | Factorizar y simplificar |

> **Truco:** Dibuja una **X** gigante imaginaria entre las fracciones. Sigue las líneas y sabrás qué multiplicar con qué.

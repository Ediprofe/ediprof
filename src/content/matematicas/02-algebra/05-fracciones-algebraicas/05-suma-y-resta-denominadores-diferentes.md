# **Suma y Resta con Denominadores Diferentes**

¿Intentarías sumar directamente peras con manzanas? No, primero buscas una categoría común: "frutas". En las fracciones pasa lo mismo: no puedes sumar $\frac{1}{x} + \frac{1}{y}$ directamente. Primero necesitas encontrar un "lenguaje común" para ambos denominadores. Ese lenguaje es el Mínimo Común Múltiplo (MCM).

---

## 🎯 ¿Qué vas a aprender?

- El procedimiento estándar de 4 pasos para cualquier suma/resta.
- A calcular el denominador común (MCM) sin miedo.
- A "ajustar" los numeradores (el paso que todos olvidan).
- A sumar y simplificar fracciones complejas con polinomios.

---

## 🔍 El Método de los 4 Pasos

1.  **Hallar el MCM:** Factoriza los denominadores y encuentra el Mínimo Común Múltiplo.
2.  **Ajustar Numeradores:** Divide el MCM por cada denominador viejo y multiplica por el numerador.
    > *"Lo que le falta al denominador, se lo pones al numerador".*
3.  **Operar:** Suma o resta los resultados en el numerador (manteniendo el denominador MCM quieto).
4.  **Simplificar:** Factoriza el resultado final para ver si algo se cancela.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Denominadores monomios simples

Suma: $\dfrac{2}{3x} + \dfrac{5}{4x^2}$

**Datos:**
- Denominadores: $3x$ y $4x^2$.

**Razonamiento:**
1.  **MCM:** De 3 y 4 es 12. De $x$ y $x^2$ es $x^2$. $\to 12x^2$.
2.  **Ajuste:**
    *   Al primero ($3x$) le falta multiplicar por $4x$ para ser $12x^2$. $\to 2 \cdot (4x) = 8x$.
    *   Al segundo ($4x^2$) le falta multiplicar por $3$. $\to 5 \cdot 3 = 15$.
3.  **Suma:**
    $$\frac{8x + 15}{12x^2}$$

**Resultado:** $\boxed{\frac{8x + 15}{12x^2}}$

---

### Ejemplo 2: Denominadores binomios (distintos)

Resta: $\dfrac{3}{x+1} - \dfrac{2}{x-1}$

**Datos:**
- Denominadores primos entre sí: $(x+1)$ y $(x-1)$.

**Razonamiento:**
1.  **MCM:** $(x+1)(x-1)$.
2.  **Ajuste:** Multiplicamos cruzado (truco rápido para dos fracciones):
    *   $3 \cdot (x-1)$
    *   $-2 \cdot (x+1)$
3.  **Operación:**
    $$\frac{3(x-1) - 2(x+1)}{(x+1)(x-1)}$$
    $$= \frac{3x - 3 - 2x - 2}{(x+1)(x-1)}$$
    $$= \frac{x - 5}{(x+1)(x-1)}$$

**Resultado:** $\boxed{\frac{x - 5}{x^2 - 1}}$

---

### Ejemplo 3: Denominadores factorizables (Nivel intermedio)

Suma: $\dfrac{x}{x^2-9} + \dfrac{1}{x+3}$

**Datos:**
- $x+3$ es irreducible.
- $x^2-9$ es diferencia de cuadrados: $(x+3)(x-3)$.

**Razonamiento:**
1.  **MCM:** $(x+3)(x-3)$. *Nota: El primer denominador YA es el MCM, contiene a ambos.*
2.  **Ajuste:**
    *   Primera fracción (su denominador es el MCM): Se queda igual $\to x$.
    *   Segunda fracción ($x+3$): Le falta $(x-3)$. $\to 1 \cdot (x-3)$.
3.  **Suma:**
    $$\frac{x + (x-3)}{(x+3)(x-3)} = \frac{2x - 3}{x^2-9}$$

**Resultado:** $\boxed{\frac{2x - 3}{x^2 - 9}}$

---

### Ejemplo 4: Resta con signos y trinomios

Resta: $\dfrac{4}{x-2} - \dfrac{8}{x^2 - 4x + 4}$

**Datos:**
- $x^2 - 4x + 4 = (x-2)^2$.
- MCM de $(x-2)$ y $(x-2)^2$ es $(x-2)^2$.

**Razonamiento:**
1.  **Ajuste:**
    *   Al primero le falta un $(x-2)$. $\to 4(x-2) = 4x - 8$.
    *   El segundo está completo. $\to 8$.
2.  **Resta:**
    $$\frac{(4x - 8) - 8}{(x-2)^2} = \frac{4x - 16}{(x-2)^2}$$
3.  **Simplificación:**
    *   Num: $4(x-4)$.
    *   No se cancela nada con $(x-2)^2$.

**Resultado:** $\boxed{\frac{4(x-4)}{(x-2)^2}}$

---

### Ejemplo 5: Suma con simplificación final

Suma: $\dfrac{1}{x^2+x} + \dfrac{1}{x}$

**Datos:**
- $x^2+x = x(x+1)$.
- MCM: $x(x+1)$.

**Razonamiento:**
1.  **Ajuste:**
    *   1ra: Completa $\to 1$.
    *   2da: Le falta $(x+1) \to 1 \cdot (x+1)$.
2.  **Suma:**
    $$\frac{1 + x + 1}{x(x+1)} = \frac{x + 2}{x(x+1)}$$
    
**Resultado:** $\boxed{\frac{x+2}{x(x+1)}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\dfrac{1}{2x} + \dfrac{1}{3x}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM(2x, 3x) = 6x.
**Razonamiento:** $\frac{3 + 2}{6x}$.
**Resultado:** $\boxed{\frac{5}{6x}}$

</details>

### Ejercicio 2
Resta $\dfrac{5}{a} - \dfrac{2}{a^2}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $a^2$.
**Razonamiento:** $\frac{5a - 2}{a^2}$.
**Resultado:** $\boxed{\frac{5a - 2}{a^2}}$

</details>

### Ejercicio 3
Suma $\dfrac{2}{x+2} + \dfrac{3}{x-2}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $x^2-4$.
**Razonamiento:** $2(x-2) + 3(x+2) = 2x - 4 + 3x + 6 = 5x + 2$.
**Resultado:** $\boxed{\frac{5x+2}{x^2-4}}$

</details>

### Ejercicio 4
Calcula $\dfrac{x}{x-1} - \dfrac{1}{x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** $\frac{x(x) - 1(x-1)}{x(x-1)} = \frac{x^2 - x + 1}{x(x-1)}$.
**Resultado:** $\boxed{\frac{x^2-x+1}{x(x-1)}}$

</details>

### Ejercicio 5
Suma $\dfrac{4}{x-3} + \dfrac{5}{(x-3)^2}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $(x-3)^2$.
**Razonamiento:** $\frac{4(x-3) + 5}{(x-3)^2} = \frac{4x - 12 + 5}{(x-3)^2}$.
**Resultado:** $\boxed{\frac{4x-7}{(x-3)^2}}$

</details>

### Ejercicio 6
Calcula $\dfrac{3}{x^2-1} + \dfrac{1}{x-1}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $(x+1)(x-1)$.
**Razonamiento:** $\frac{3 + 1(x+1)}{x^2-1} = \frac{x+4}{x^2-1}$.
**Resultado:** $\boxed{\frac{x+4}{x^2-1}}$

</details>

### Ejercicio 7
Resta $\dfrac{2x}{x^2-9} - \dfrac{1}{x+3}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $(x+3)(x-3)$.
**Razonamiento:** $2x - 1(x-3) = 2x - x + 3 = x + 3$.
**Simplificación:** $\frac{x+3}{(x+3)(x-3)} = \frac{1}{x-3}$.
**Resultado:** $\boxed{\frac{1}{x-3}}$

</details>

### Ejercicio 8
Suma $\dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $abc$.
**Razonamiento:** $\frac{bc + ac + ab}{abc}$.
**Resultado:** $\boxed{\frac{ab+bc+ac}{abc}}$

</details>

### Ejercicio 9
Calcula $\dfrac{2}{x^2+3x} - \dfrac{1}{x}$.

<details>
<summary>Ver solución</summary>

**Datos:** $x(x+3)$. MCM = $x(x+3)$.
**Razonamiento:** $\frac{2 - 1(x+3)}{x(x+3)} = \frac{2 - x - 3}{x(x+3)} = \frac{-x - 1}{x(x+3)}$.
**Resultado:** $\boxed{\frac{-(x+1)}{x(x+3)}}$

</details>

### Ejercicio 10
Suma $\dfrac{x+1}{x-1} + \dfrac{x-1}{x+1}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** $\frac{(x+1)^2 + (x-1)^2}{x^2-1} = \frac{x^2+2x+1 + x^2-2x+1}{x^2-1} = \frac{2x^2+2}{x^2-1}$.
**Resultado:** $\boxed{\frac{2(x^2+1)}{x^2-1}}$

</details>

---

## 🔑 Resumen

| ¿Denominadores iguales? | Procedimiento |
| :--- | :--- |
| **SÍ** | Suma directa, denominador constante. |
| **NO** | Calcular MCM de denominadores $\to$ Ajustar numeradores $\to$ Sumar. |

> La clave del éxito no está en la suma, sino en sacar bien el **MCM** al principio.

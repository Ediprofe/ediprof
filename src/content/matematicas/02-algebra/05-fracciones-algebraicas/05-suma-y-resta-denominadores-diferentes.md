# **Suma y Resta con Denominadores Diferentes**

¿Intentarías sumar directamente peras con manzanas? No, primero buscas una categoría común: "frutas". En las fracciones pasa lo mismo: no puedes sumar $\frac{1}{x} + \frac{1}{y}$ directamente. Primero necesitas encontrar un denominador común. Para esto, tienes dos caminos principales: el método general del **MCM** y el método rápido de la **multiplicación en cruz**.

---

## 🎯 ¿Qué vas a aprender?

- El método de la multiplicación en cruz (ideal para dos fracciones).
- El método del Mínimo Común Múltiplo (MCM) para cualquier caso.
- 5 ejemplos detallados de cada método.
- Cuándo es mejor usar cada método.
- A simplificar el resultado final independientemente del método usado.

---

## 🛣️ Método 1: Multiplicación en Cruz (La "Carita Feliz")

Este método es directo y mecánico. Es perfecto cuando tienes **solo dos fracciones** y los denominadores son pequeños o no tienen factores comunes.

**La Fórmula:**

$$
\boxed{\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}}
$$

**El proceso:**
1.  **Multiplica los denominadores ($b \cdot d$)**: Este será tu nuevo denominador.
2.  **Multiplica en cruz ($a \cdot d$ y $b \cdot c$)**: Estos serán los términos de tu numerador.
3.  **Simplifica**: Al final, revisa si puedes factorizar y cancelar.

### ⚙️ Ejemplos con el Método en Cruz

#### Ejemplo 1: Denominadores simples
Suma: $\dfrac{3}{x} + \dfrac{2}{y}$

**Razonamiento:**
1. Denominador: $x \cdot y$.
2. Cruzado: $3y + 2x$.

**Resultado:** $\boxed{\frac{3y + 2x}{xy}}$

#### Ejemplo 2: Resta con números y letras
Resta: $\dfrac{5}{2a} - \dfrac{1}{3b}$

**Razonamiento:**
1. Denominador: $2a \cdot 3b = 6ab$.
2. Cruzado: $5(3b) - 1(2a) = 15b - 2a$.

**Resultado:** $\boxed{\frac{15b - 2a}{6ab}}$

#### Ejemplo 3: Binomios distintos
Suma: $\dfrac{2}{x+1} + \dfrac{3}{x-1}$

**Razonamiento:**
1. Denominador: $(x+1)(x-1) = x^2 - 1$.
2. Cruzado: $2(x-1) + 3(x+1)$.
3. Resolvemos arriba: $2x - 2 + 3x + 3 = 5x + 1$.

**Resultado:** $\boxed{\frac{5x + 1}{x^2 - 1}}$

#### Ejemplo 4: Suma con un entero
Suma: $x + \dfrac{2}{x-1}$

**Razonamiento:**
Imagina un 1 debajo de la x: $\frac{x}{1} + \frac{2}{x-1}$.
1. Denominador: $1 \cdot (x-1) = x-1$.
2. Cruzado: $x(x-1) + 2(1)$.
3. Operamos: $x^2 - x + 2$.

**Resultado:** $\boxed{\frac{x^2 - x + 2}{x - 1}}$

#### Ejemplo 5: Cruz con simplificación final
Resta: $\dfrac{x}{y} - \dfrac{x}{2y}$

**Razonamiento:**
Aunque tienen factor común $y$, usemos cruz para ver qué pasa.
1. Denominador: $y \cdot 2y = 2y^2$.
2. Cruzado: $x(2y) - x(y) = 2xy - xy = xy$.
3. Simplificamos final: $\frac{xy}{2y^2} = \frac{x}{2y}$.

**Resultado:** $\boxed{\frac{x}{2y}}$

---

## 🛣️ Método 2: El Mínimo Común Múltiplo

Este es el método general. Es obligatorio cuando tienes **tres o más fracciones** o cuando los denominadores son polinomios grandes que comparten factores.

**El proceso de 4 pasos:**
1.  **Hallar el MCM:** Factoriza los denominadores y encuentra el Mínimo Común Múltiplo.
2.  **Ajustar Numeradores:** Divide el MCM por cada denominador viejo y multiplica por su numerador.
    > *"Lo que le falta al denominador, se lo pones al numerador".*
3.  **Operar:** Suma o resta los numeradores.
4.  **Simplificar:** Factoriza el resultado final.

### ⚙️ Ejemplos con el Método MCM

#### Ejemplo 6: Denominadores monomios (comparten variable)
Suma: $\dfrac{3}{2x} + \dfrac{5}{4x^2}$

**Razonamiento:**
1. MCM de $2x$ y $4x^2$ es $4x^2$.
2. Ajuste:
   - 1ra: le falta $2x$ para llegar a $4x^2$. $\to 3(2x) = 6x$.
   - 2da: no le falta nada. $\to 5$.
3. Suma: $6x + 5$.

**Resultado:** $\boxed{\frac{6x + 5}{4x^2}}$

#### Ejemplo 7: Tres fracciones
Suma: $\dfrac{1}{x} + \dfrac{1}{2x} + \dfrac{1}{3x}$

**Razonamiento:**
1. MCM de $x, 2x, 3x$ es $6x$.
2. Ajuste:
   - 1ra: falta 6. $\to 6$.
   - 2da: falta 3. $\to 3$.
   - 3ra: falta 2. $\to 2$.
3. Suma: $6 + 3 + 2 = 11$.

**Resultado:** $\boxed{\frac{11}{6x}}$

#### Ejemplo 8: Denominador factorizable (Diferencia de cuadrados)
Suma: $\dfrac{2}{x^2-9} + \dfrac{1}{x+3}$

**Razonamiento:**
1. Factorizamos: $x^2-9 = (x+3)(x-3)$.
2. MCM: $(x+3)(x-3)$.
3. Ajuste:
   - 1ra: Completa. $\to 2$.
   - 2da: Le falta $(x-3)$. $\to 1(x-3)$.
4. Suma: $2 + x - 3 = x - 1$.

**Resultado:** $\boxed{\frac{x - 1}{x^2 - 9}}$

#### Ejemplo 9: Denominador trinomio cuadrado perfecto
Resta: $\dfrac{x}{x^2+2x+1} - \dfrac{1}{x+1}$

**Razonamiento:**
1. Factorizamos: $x^2+2x+1 = (x+1)^2$.
2. MCM: $(x+1)^2$.
3. Ajuste:
   - 1ra: Completa. $\to x$.
   - 2da: Le falta $(x+1)$. $\to 1(x+1)$.
4. Resta (cuidado con el signo):
   
$$
x - (x+1) = x - x - 1 = -1
$$

**Resultado:** $\boxed{\frac{-1}{(x+1)^2}}$

#### Ejemplo 10: Signos opuestos
Suma: $\dfrac{2}{x-3} + \dfrac{3}{3-x}$

**Razonamiento:**
1. Truco: $3-x = -(x-3)$.
2. MCM: $(x-3)$. Pero cambiamos el signo de la segunda fracción.
   
$$
\frac{2}{x-3} - \frac{3}{x-3}
$$

3. Como ahora tienen igual denominador: $2 - 3 = -1$.

**Resultado:** $\boxed{\frac{-1}{x-3}}$

---

## ⚡ ¿Cuál método elijo?

| Situación | Método Recomendado | Por qué |
| :--- | :--- | :--- |
| **2 fracciones simples** (ej: $\dfrac{1}{x} + \dfrac{2}{y}$) | **Cruz** | Es más rápido y directo. |
| **3 o más fracciones** | **MCM** | La cruz se vuelve un desastre con 3 fracciones. |
| **Polinomios con factores comunes** | **MCM** | La cruz genera expresiones gigantes que luego cuesta simplificar. |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1 (Método Cruz)
Calcula $\dfrac{a}{b} + \dfrac{c}{d}$ (Fórmula general).

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Aplicamos la definición de suma de fracciones heterogéneas.

$$
\frac{ad + bc}{bd}
$$

**Resultado:** $\boxed{\frac{ad+bc}{bd}}$

</details>

### Ejercicio 2 (Método Cruz)
Resta $\dfrac{5}{a} - \dfrac{2}{3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Multiplicamos en cruz. Denominador $3a$.

$$
\frac{5(3) - 2(a)}{3a} = \frac{15 - 2a}{3a}
$$

**Resultado:** $\boxed{\frac{15 - 2a}{3a}}$

</details>

### Ejercicio 3 (Método MCM)
Suma $\dfrac{1}{x} + \dfrac{1}{x^2}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM entre $x$ y $x^2$ es $x^2$.
**Razonamiento:** 
A la primera le falta una $x$.

$$
\frac{1(x) + 1}{x^2}
$$

**Resultado:** $\boxed{\frac{x+1}{x^2}}$

</details>

### Ejercicio 4 (Método Cruz)
Calcula $\dfrac{2}{x+2} + \dfrac{3}{x-2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{2(x-2) + 3(x+2)}{(x+2)(x-2)}
$$

$$
\frac{2x - 4 + 3x + 6}{x^2-4} = \frac{5x + 2}{x^2-4}
$$

**Resultado:** $\boxed{\frac{5x+2}{x^2-4}}$

</details>

### Ejercicio 5 (Método MCM)
Suma $\dfrac{4}{x-3} + \dfrac{5}{(x-3)^2}$.

<details>
<summary>Ver solución</summary>

**Datos:** El MCM es $(x-3)^2$ porque contiene al otro.
**Razonamiento:** 
Al primero le falta un $(x-3)$.

$$
\frac{4(x-3) + 5}{(x-3)^2} = \frac{4x - 12 + 5}{(x-3)^2}
$$

**Resultado:** $\boxed{\frac{4x-7}{(x-3)^2}}$

</details>

### Ejercicio 6 (Método Cruz)
Simplifica $\dfrac{x}{y} - \dfrac{x}{2y}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Denominador común $2y^2$ (si usamos cruz) o $2y$ (si usamos MCM). Usemos MCM que es más limpio.
MCM = $2y$. A la primera le falta un 2.

$$
\frac{2x - x}{2y} = \frac{x}{2y}
$$

**Resultado:** $\boxed{\frac{x}{2y}}$

</details>

### Ejercicio 7 (Suma de 3)
Suma $\dfrac{1}{2} + \dfrac{1}{x} + \dfrac{1}{x^2}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $2x^2$.
**Razonamiento:** 

$$
\frac{x^2(1) + 2x(1) + 2(1)}{2x^2}
$$

**Resultado:** $\boxed{\frac{x^2+2x+2}{2x^2}}$

</details>

### Ejercicio 8 (Polinomios)
Resta $\dfrac{2x}{x^2-1} - \dfrac{1}{x+1}$.

<details>
<summary>Ver solución</summary>

**Datos:** $x^2-1 = (x+1)(x-1)$. Este es el MCM.
**Razonamiento:** 
A la segunda fracción le falta $(x-1)$.

$$
\frac{2x - 1(x-1)}{x^2-1} = \frac{2x - x + 1}{x^2-1}
$$

**Resultado:** $\boxed{\frac{x+1}{x^2-1} = \frac{1}{x-1}}$

</details>

### Ejercicio 9 (Signos)
Calcula $\dfrac{3}{a-b} + \dfrac{2}{b-a}$.

<details>
<summary>Ver solución</summary>

**Truco:** $b-a = -(a-b)$.
**Razonamiento:** 
Cambiamos el signo de la segunda fracción para igualar denominadores.

$$
\frac{3}{a-b} - \frac{2}{a-b} = \frac{3-2}{a-b}
$$

**Resultado:** $\boxed{\frac{1}{a-b}}$

</details>

### Ejercicio 10 (Reto)
Suma $\dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c}$.

<details>
<summary>Ver solución</summary>

**Datos:** MCM = $abc$.
**Razonamiento:** 

$$
\frac{bc + ac + ab}{abc}
$$

**Resultado:** $\boxed{\frac{ab+bc+ac}{abc}}$

</details>

---

## 🔑 Resumen

| Método | Fórmula / Proceso | Cuándo usarlo |
| :--- | :--- | :--- |
| **Cruz** | $\frac{ad \pm bc}{bd}$ | Para 2 fracciones simples o binomios distintos. |
| **MCM** | Buscar el múltiplo común $\to$ Ajustar | Para 3+ fracciones o polinomios factorizables. |

> **Consejo:** Ante la duda, el **MCM** nunca falla. La cruz es rápida, pero peligrosa si no simplificas bien al final.

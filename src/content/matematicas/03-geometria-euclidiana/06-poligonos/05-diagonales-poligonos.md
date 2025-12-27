# **Diagonales de Polígonos**

Una diagonal es un "atajo". En lugar de caminar por los lados (el borde), la diagonal cruza por en medio del polígono. Es la línea que conecta a dos vértices que no son vecinos.

---

## 🎯 ¿Qué vas a aprender?

- Definir qué es una diagonal.
- Calcular cuántas diagonales salen de **un solo vértice**.
- Calcular el número **total** de diagonales de cualquier polígono ($D$).
- Entender la lógica detrás de la fórmula (para no tener que memorizarla).

---

## 📐 ¿Qué es una Diagonal?

> **Definición:** Es el segmento de recta que une dos vértices **no consecutivos**.

Si unes dos vértices consecutivos, eso es un **lado**, no una diagonal.

### Ejemplo
En un cuadrado $ABCD$:
-   De $A$ a $B$: Lado.
-   De $A$ a $C$: **Diagonal**.
-   De $A$ a $D$: Lado.

---

## 🔢 Diagonales desde UN Vértice ($d$)

Imagina que estás parado en un vértice de un polígono de $n$ lados y quieres lanzar cuerdas a los otros vértices.
¿A cuántos puedes lanzar?
-   No puedes lanzarte a ti mismo. ($-1$)
-   No puedes lanzar a tu vecino de la derecha (ya es un lado). ($-1$)
-   No puedes lanzar a tu vecino de la izquierda (ya es un lado). ($-1$)

En total, pierdes 3 vértices.

> **Fórmula:** El número de diagonales desde un solo vértice es:

$$
d = n - 3
$$

---

## 🔢 Diagonales Totales ($D$)

Si hay $n$ vértices, y de cada uno salen $n-3$ diagonales, podrías pensar que el total es $n(n-3)$.
**¡Pero cuidado!**
La diagonal que va de $A$ a $C$ es la misma que va de $C$ a $A$. Si simplemente multiplicamos, estaríamos contando cada cuerda dos veces (una por cada extremo).
Así que debemos dividir por 2.

> **Fórmula Maestra:** El número total de diagonales es:

$$
D = \frac{n(n - 3)}{2}
$$

### Tabla de Diagonales
-   **Triángulo ($n=3$):** $\frac{3(0)}{2} = 0$. (¡No tiene!)
-   **Cuadrilátero ($n=4$):** $\frac{4(1)}{2} = 2$.
-   **Pentágono ($n=5$):** $\frac{5(2)}{2} = 5$. (El único con $D = n$).
-   **Hexágono ($n=6$):** $\frac{6(3)}{2} = 9$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Diagonales de un Decágono

¿Cuántas diagonales tiene un polígono de 10 lados?

**Razonamiento:**
$n = 10$.
$n - 3 = 7$.

$$
D = \frac{10 \times 7}{2}
$$

$$
D = \frac{70}{2}
$$

**Resultado:**
$$
\boxed{35 \text{ diagonales}}
$$

### Ejemplo 2: Problema Inverso

¿Qué polígono tiene 9 diagonales?

**Razonamiento:**
$$
\frac{n(n-3)}{2} = 9
$$

$$
n(n-3) = 18
$$

Buscamos dos números que se lleven 3 de diferencia y multiplicados den 18.
Probamos: $6 \times 3 = 18$.
Entonces $n = 6$.

**Resultado:**
$$
\boxed{\text{Hexágono}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula las diagonales totales de un octágono ($n=8$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
D = \frac{8(8-3)}{2} = \frac{8 \times 5}{2} = \frac{40}{2}
$$

**Resultado:**
$$
\boxed{20}
$$

</details>

### Ejercicio 2
¿Cuántas diagonales salen de **un solo vértice** en un polígono de 20 lados?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
d = n - 3 = 20 - 3
$$

**Resultado:**
$$
\boxed{17}
$$

</details>

### Ejercicio 3
Calcula el número de diagonales de un triángulo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
D = \frac{3(0)}{2}
$$

**Resultado:**
$$
\boxed{0}
$$

</details>

### Ejercicio 4
Si un polígono tiene 54 diagonales, ¿cuántos lados tiene?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\frac{n(n-3)}{2} = 54 \Rightarrow n(n-3) = 108
$$
Buscamos factores de 108 con diferencia de 3.
$12 \times 9 = 108$.
$n = 12$.

**Resultado:**
$$
\boxed{12 \text{ lados (Dodecágono)}}
$$

</details>

### Ejercicio 5
Verdadero o Falso: Un pentágono tiene el mismo número de lados que de diagonales.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$n=5$.
$D = 5(2)/2 = 5$.
$5 = 5$.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 6
Calcula las diagonales de un icoságono ($n=20$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
D = \frac{20 \times 17}{2} = 10 \times 17
$$

**Resultado:**
$$
\boxed{170}
$$

</details>

### Ejercicio 7
¿Por qué dividimos entre 2 en la fórmula de las diagonales?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Porque si no, contaríamos cada diagonal dos veces (una de ida $A \to B$ y otra de vuelta $B \to A$).

**Resultado:**
$$
\boxed{\text{Para evitar contar doble}}
$$

</details>

### Ejercicio 8
¿Cuántas diagonales se pueden trazar desde un vértice en un cuadrilátero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$4 - 3 = 1$. (Solo una cruza, la otra es lado).

**Resultado:**
$$
\boxed{1}
$$

</details>

### Ejercicio 9
Un polígono tiene 170 diagonales. ¿Es un icoságono?
*(Pista: Ver ejercicio 6).*

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí, el cálculo coincide.

**Resultado:**
$$
\boxed{\text{Sí}}
$$

</details>

### Ejercicio 10
Si duplicamos el número de lados de un cuadrado ($n=4 \to n=8$), ¿se duplica el número de diagonales?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cuadrado ($n=4$): $D=2$.
Octágono ($n=8$): $D=20$.
De 2 a 20 se multiplicó por 10.
El crecimiento es cuadrático, no lineal.

**Resultado:**
$$
\boxed{\text{No, aumenta mucho más}}
$$

</details>

---

## 🔑 Resumen

| Fórmula | Uso |
| :--- | :--- |
| **$n - 3$** | Diagonales desde **UN** vértice. |
| **$\frac{n(n-3)}{2}$** | Diagonales **TOTALES**. |

> **Consejo:** Si olvidas la fórmula, prueba con un cuadrado ($n=4, D=2$) o un pentágono ($n=5, D=5$) para redescubrirla.

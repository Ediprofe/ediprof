# **Operaciones Combinadas sin Signos de Agrupación**

Imagina que entras a una cocina y ves ingredientes mezclados. Si metes todo a la licuadora sin pensar, te sale un desastre. En matemáticas pasa lo mismo: no puedes llegar y operar lo primero que veas. Hay un estricto orden de entrada, como en una fila VIP, llamado **Jerarquía de Operaciones**.

---

## 🎯 ¿Qué vas a aprender?

- El orden sagrado: PEMDAS (o PAPOMUDAS).
- Por qué $2 + 3 \times 4$ no es 20, sino 14.
- Cómo manejar potencias, raíces, multiplicaciones y sumas en una misma fiesta.
- La regla de "Izquierda a Derecha" cuando hay empates.

---

## La Pirámide de la Jerarquía

El orden para resolver es estricto. Si te lo saltas, el resultado muere.

1.  **Nivel Rey (P):** Paréntesis (Aquí no los veremos hoy).
2.  **Nivel Príncipe (E/R):** Potencias y Raíces ($x^2, \sqrt{x}$).
3.  **Nivel Caballero (M/D):** Multiplicación y División ($\times, \div$).
4.  **Nivel Peón (S/R):** Suma y Resta ($+, -$).

**¡Ojo!** Si tienes operaciones del mismo nivel (ej. suma y resta), se resuelven de **Izquierda a Derecha**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: El error clásico
$$ 2 + 3 \times 4 $$
-   Incorrecto: Sumar primero ($5 \times 4 = 20$).
-   **Correcto:** Multiplicar primero (Nivel Caballero gana a Peón).
$$ 2 + 12 = 14 $$
**Resultado:** $\boxed{14}$

#### Ejemplo 2: Potencia vs Multiplicación
$$ 5 \times 2^3 $$
-   Primero Potencia: $2^3 = 8$.
-   Queda: $5 \times 8$.
$$ 40 $$
**Resultado:** $\boxed{40}$

#### Ejemplo 3: El empate (Izquierda a Derecha)
$$ 20 \div 5 \times 2 $$
-   División y Multiplicación tienen el mismo rango.
-   Resolvemos la que aparezca primero a la izquierda: $20 \div 5 = 4$.
-   Queda: $4 \times 2$.
$$ 8 $$
**Resultado:** $\boxed{8}$
*(Si hicieras la multi primero, daría $20 \div 10 = 2$, ¡Error!)*.

#### Ejemplo 4: Mezcla completa
$$ 10 + 4^2 - \sqrt{9} \times 2 $$
1.  **Potencias/Raíces:**
    $4^2 = 16$.
    $\sqrt{9} = 3$.
    Queda: $10 + 16 - 3 \times 2$.
2.  **Multiplicación:**
    $3 \times 2 = 6$.
    Queda: $10 + 16 - 6$.
3.  **Suma/Resta (Izq a Der):**
    $10 + 16 = 26$.
    $26 - 6 = 20$.
**Resultado:** $\boxed{20}$

#### Ejemplo 5: División y Resta
$$ 30 - 10 \div 2 + 5 $$
1.  **División:** $10 \div 2 = 5$.
    Queda: $30 - 5 + 5$.
2.  **Suma/Resta (Izq a Der):**
    $30 - 5 = 25$.
    $25 + 5 = 30$.
**Resultado:** $\boxed{30}$

---

## Estrategia para Resolver

Subraya la operación que vas a hacer primero y reescribe todo lo demás abajo. Hazlo paso a paso, línea por línea.

### ⚙️ Ejemplos Paso a Paso

#### Ejemplo 6: Combinación de multiplicación y división
1.  División y Multiplicación. Empate. Empiezo por la izquierda ($8 \div 2$).
    $$ 6 + \mathbf{4} \times 3 $$
2.  Multiplicación ($4 \times 3$).
    $$ 6 + \mathbf{12} $$
3.  Suma.
    $$ 18 $$
**Resultado:** $\boxed{18}$

#### Ejemplo 7: Potencia con sumas y restas
1.  Potencia ($3^3$).
    $$ \mathbf{27} + 4 \times 5 - 10 $$
2.  Multiplicación ($4 \times 5$).
    $$ 27 + \mathbf{20} - 10 $$
3.  Suma (Izq a Der).
    $$ \mathbf{47} - 10 $$
4.  Resta.
    $$ 37 $$
**Resultado:** $\boxed{37}$

#### Ejemplo 8: Raíz con operaciones variadas
1.  Raíz.
    $$ \mathbf{5} \times 2 + 20 \div 4 $$
2.  Multiplicación ($5 \times 2$) y División ($20 \div 4$) están separadas por un más. Podemos hacerlas en la misma línea para ahorrar tiempo, pero con cuidado.
    $$ \mathbf{10} + \mathbf{5} $$
3.  Suma.
    $$ 15 $$
**Resultado:** $\boxed{15}$

#### Ejemplo 9: Resta con potencia y producto
1.  Potencia.
    $$ 100 - \mathbf{9} \times 10 $$
2.  Multiplicación.
    $$ 100 - \mathbf{90} $$
3.  Resta.
    $$ 10 $$
**Resultado:** $\boxed{10}$

#### Ejemplo 10: Cadena de operaciones iguales
1.  Multiplicación ($2 \times 2$).
    $$ 2 + 2 - \mathbf{4} \div 2 $$
2.  División ($4 \div 2$).
    $$ 2 + 2 - \mathbf{2} $$
3.  Suma ($2+2$).
    $$ \mathbf{4} - 2 $$
4.  Resta.
    $$ 2 $$
**Resultado:** $\boxed{2}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $5 + 5 \times 5$.

<details>
<summary>Ver solución</summary>

$5 \times 5 = 25$.
$5 + 25 = 30$.
**Resultado:** $\boxed{30}$

</details>

### Ejercicio 2
Calcula $16 - 8 \div 2$.

<details>
<summary>Ver solución</summary>

$8 \div 2 = 4$.
$16 - 4 = 12$.
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 3
Calcula $3 \times 4^2$.

<details>
<summary>Ver solución</summary>

$4^2 = 16$.
$3 \times 16 = 48$.
**Resultado:** $\boxed{48}$

</details>

### Ejercicio 4
Calcula $10 + 10 \times 0$.

<details>
<summary>Ver solución</summary>

$10 \times 0 = 0$.
$10 + 0 = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 5
Calcula $20 \div 4 \times 5$.

<details>
<summary>Ver solución</summary>

Izq a Der: $20 \div 4 = 5$.
$5 \times 5 = 25$.
**Resultado:** $\boxed{25}$

</details>

### Ejercicio 6
Calcula $7 \times 3 - 6 \div 2$.

<details>
<summary>Ver solución</summary>

$21 - 3 = 18$.
**Resultado:** $\boxed{18}$

</details>

### Ejercicio 7
Calcula $2^3 + \sqrt{16} \times 3$.

<details>
<summary>Ver solución</summary>

$8 + 4 \times 3$.
$8 + 12$.
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 8
Calcula $50 - 5^2 \times 2$.

<details>
<summary>Ver solución</summary>

$50 - 25 \times 2$.
$50 - 50$.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 9
Calcula $6 + 4 \div 2 + 1$.

<details>
<summary>Ver solución</summary>

$6 + 2 + 1 = 9$.
**Resultado:** $\boxed{9}$

</details>

### Ejercicio 10
Calcula $100 \div 10 \div 2$.

<details>
<summary>Ver solución</summary>

Izq a Der: $100 \div 10 = 10$.
$10 \div 2 = 5$.
**Resultado:** $\boxed{5}$

</details>

---

## 🔑 Resumen

| Nivel | Operaciones | Notas |
| :--- | :--- | :--- |
| **1** | Potencias y Raíces | Tienen superprioridad. |
| **2** | Multiplicación y División | Tienen prioridad media. |
| **3** | Suma y Resta | Esperan al final. |

> **Conclusión:** Ante la duda, respeta la pirámide y el sentido de lectura (izquierda a derecha). El orden de los factores AQUI sí altera el producto.

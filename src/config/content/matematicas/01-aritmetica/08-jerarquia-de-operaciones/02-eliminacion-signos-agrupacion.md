---
title: "Eliminación de Signos de Agrupación"
---

# **Eliminación de Signos de Agrupación**

Los paréntesis son como cajas de regalo dentro de otras cajas. Para llegar al regalo, tienes que abrir primero la caja más pequeña, luego la mediana y al final la grande. En matemáticas, estas cajas se llaman paréntesis (), corchetes [] y llaves {}.

---

## 🎯 ¿Qué vas a aprender?

- El orden de las cajas: De adentro hacia afuera.
- El portero: Qué hacer si hay un signo $(+)$ o $(-)$ antes del paréntesis.
- Cómo manejar paréntesis, corchetes y llaves en un solo problema.

---

## La Jerarquía de las Cajas

Aunque matemáticamente funcionan igual, visualmente solemos ordenarlos así para no confundirnos:
1.  **Paréntesis Cuadrados (Corchetes) $[\dots]$**
2.  **Llaves $\{\dots\}$**
3.  **Paréntesis Redondos $(\dots)$** $\leftarrow$ Se resuelven primero (los más internos).

**Regla de Oro:** Siempre resuelve lo que está más adentro primero.

---

## El Signo antes del Paréntesis

Antes de eliminar un paréntesis, mira quién está vigilando la entrada:

1.  **Signo Positivo $(+)$:** El portero buena onda. Deja salir a los números exactamente como son.
    -   $+(5 - 2) \rightarrow +5 - 2$
2.  **Signo Negativo $(-)$:** El portero estricto. Obliga a todos a cambiarse de ropa (de signo) al salir.
    -   $-(5 - 2) \rightarrow -5 + 2$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Paréntesis simple
$$ 10 + (3 - 5) $$
Opción A (Resolver adentro): $10 + (-2) = 8$.
Opción B (Eliminar paréntesis con signo +): $10 + 3 - 5 = 8$.
**Resultado:** $\boxed{8}$

#### Ejemplo 2: El signo menos traicionero
$$ 15 - (4 + 6) $$
¡Cuidado! El menos afecta a todo lo de adentro.
$15 - 4 - 6 = 5$.
(O resolver adentro: $15 - 10 = 5$).
**Resultado:** $\boxed{5}$

#### Ejemplo 3: Menos con Menos
$$ 20 - (5 - 8) $$
$20 - (-3)$. Menos por menos da más.
$20 + 3$.
**Resultado:** $\boxed{23}$

#### Ejemplo 4: Multiplicación invisible
$$ 3(4 + 2) $$
Si no hay signo entre el número y el paréntesis, es una **multiplicación**.
$3 \times 6 = 18$.
**Resultado:** $\boxed{18}$

#### Ejemplo 5: Dos paréntesis separados
$$ (5 + 2) - (3 - 4) $$
Resolvemos cada uno por separado.
$(7) - (-1)$.
$7 + 1 = 8$.
**Resultado:** $\boxed{8}$

---

## Cajas dentro de Cajas (Anidados)

Si ves $\{ [ ( ) ] \}$, ve directo al centro de la cebolla.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: Nivel medio
$$ 20 - [ 5 + (3 - 1) ] $$
1.  Paréntesis interno $(3-1)=2$.
    $$ 20 - [ 5 + 2 ] $$
2.  Corchete $[5+2]=7$.
    $$ 20 - 7 $$
3.  Resta.
    $$ 13 $$
**Resultado:** $\boxed{13}$

#### Ejemplo 7: Signos cambiados
$$ 10 - [ 6 - (4 + 1) ] $$
1.  Paréntesis $(4+1)=5$. Ojo con el menos de afuera.
    $$ 10 - [ 6 - 5 ] $$
2.  Corchete $[6-5]=1$.
    $$ 10 - 1 $$
**Resultado:** $\boxed{9}$

#### Ejemplo 8: Nivel Experto
$$ \{ 15 - [ 8 + (2 - 5) ] \} $$
1.  Paréntesis $(2-5)=-3$.
    $$ \{ 15 - [ 8 + (-3) ] \} $$
    $$ \{ 15 - [ 8 - 3 ] \} $$
2.  Corchete $[8-3]=5$.
    $$ \{ 15 - 5 \} $$
3.  Llave.
    $$ 10 $$
**Resultado:** $\boxed{10}$

#### Ejemplo 9: Doble anidación
$$ 2 + [ 3 - (5 + 1) ] - (8 - 4) $$
1.  Paréntesis: $(5+1)=6$ y $(8-4)=4$.
    $$ 2 + [ 3 - 6 ] - 4 $$
2.  Corchete: $[3-6]=-3$.
    $$ 2 + (-3) - 4 $$
3.  Todo fuera: $2 - 3 - 4$.
    $-1 - 4 = -5$.
**Resultado:** $\boxed{-5}$

#### Ejemplo 10: Multiplicación anidada
$$ 5 [ 2 + 3(4 - 2) ] $$
1.  Paréntesis $(4-2)=2$.
    $$ 5 [ 2 + 3(2) ] $$
2.  Multi dentro de corchete: $3 \times 2 = 6$.
    $$ 5 [ 2 + 6 ] $$
3.  Corchete $[2+6]=8$.
    $$ 5 [ 8 ] $$
4.  Multi final.
    $$ 40 $$
**Resultado:** $\boxed{40}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $12 + (5 - 2)$.

<details>
<summary>Ver solución</summary>

$12 + 3 = 15$.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 2
Calcula $15 - (8 + 2)$.

<details>
<summary>Ver solución</summary>

$15 - 10 = 5$.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 3
Calcula $4(5 - 2)$.

<details>
<summary>Ver solución</summary>

$4 \times 3 = 12$.
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 4
Calcula $10 + [ 5 - (3 - 1) ]$.

<details>
<summary>Ver solución</summary>

$[5 - 2] = 3$.
$10 + 3 = 13$.
**Resultado:** $\boxed{13}$

</details>

### Ejercicio 5
Calcula $20 - (5 - 10)$.

<details>
<summary>Ver solución</summary>

$20 - (-5) = 20 + 5$.
**Resultado:** $\boxed{25}$

</details>

### Ejercicio 6
Calcula $2 \{ 3 + 1 \}$.

<details>
<summary>Ver solución</summary>

$2 \times 4 = 8$.
**Resultado:** $\boxed{8}$

</details>

### Ejercicio 7
Calcula $- (3 + 4) - (1 - 2)$.

<details>
<summary>Ver solución</summary>

$-7 - (-1) = -7 + 1$.
**Resultado:** $\boxed{-6}$

</details>

### Ejercicio 8
Calcula $5 + [ 2(3) ]$.

<details>
<summary>Ver solución</summary>

$5 + 6 = 11$.
**Resultado:** $\boxed{11}$

</details>

### Ejercicio 9
Calcula $100 - [ 50 - (20 + 10) ]$.

<details>
<summary>Ver solución</summary>

$[50 - 30] = 20$.
$100 - 20 = 80$.
**Resultado:** $\boxed{80}$

</details>

### Ejercicio 10
Calcula $(5 + 5) \div (2 + 3)$.

<details>
<summary>Ver solución</summary>

$10 \div 5 = 2$.
**Resultado:** $\boxed{2}$

</details>

---

## 🔑 Resumen

| Situación | Acción | Ejemplo |
| :--- | :--- | :--- |
| **$+ ( \dots )$** | Quitas paréntesis, signos iguales. | $+(3-2) \to +3-2$ |
| **$- ( \dots )$** | Quitas paréntesis, inviertes signos. | $-(3-2) \to -3+2$ |
| **Anidados** | De adentro hacia afuera. | $\{ [ ( ) ] \}$ |

> **Conclusión:** Sé ordenado. No intentes quitar todos los paréntesis de golpe. Ve capa por capa, como pelando una cebolla, y no llorarás (tanto).

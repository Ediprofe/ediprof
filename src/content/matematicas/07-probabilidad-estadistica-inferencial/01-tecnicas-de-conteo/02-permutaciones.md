# Permutaciones

Las **permutaciones** son arreglos ordenados. Cuando el orden importa (primero, segundo, tercero...), estamos contando permutaciones.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las permutaciones y cuándo usarlas
- El concepto de factorial (n!)
- Permutaciones de n elementos
- Permutaciones parciales (tomar r de n)
- Permutaciones con elementos repetidos

---

## 📊 Fórmulas de Permutaciones

| Tipo | Fórmula | Cuándo usarla |
|------|---------|---------------|
| **Factorial** | $n! = n \times (n-1) \times ... \times 1$ | Base para otras fórmulas |
| **Permutación total** | $P_n = n!$ | Ordenar todos los n elementos |
| **Permutación parcial** | $P(n,r) = \frac{n!}{(n-r)!}$ | Elegir y ordenar r de n elementos |
| **Con repetición** | $\frac{n!}{n_1! \cdot n_2! \cdot ...}$ | Cuando hay elementos repetidos |

---

## 📖 El Factorial

> El **factorial** de un número n (escrito n!) es el producto de todos los enteros positivos desde 1 hasta n.

$$
n! = n \times (n-1) \times (n-2) \times ... \times 2 \times 1
$$

### 💡 Ejemplos:

| n | n! | Cálculo |
|---|-------|---------|
| 0 | 1 | Por definición |
| 1 | 1 | 1 |
| 2 | 2 | 2 × 1 |
| 3 | 6 | 3 × 2 × 1 |
| 4 | 24 | 4 × 3 × 2 × 1 |
| 5 | 120 | 5 × 4 × 3 × 2 × 1 |
| 6 | 720 | 6 × 5 × 4 × 3 × 2 × 1 |
| 10 | 3,628,800 | Crece muy rápido |

### 💡 Por qué 0! = 1:

Por convención matemática y para que las fórmulas funcionen correctamente.

---

## 📖 Permutaciones Totales

> Una **permutación** es un arreglo **ordenado** de todos los elementos de un conjunto.

### 💡 ¿De cuántas formas puedes ordenar n objetos diferentes?

$$
P_n = n!
$$

### ⚙️ Ejemplo 1: Ordenar 4 libros en un estante

¿De cuántas formas puedes ordenar 4 libros diferentes?

$$
P_4 = 4! = 4 \times 3 \times 2 \times 1 = 24 \text{ formas}
$$

### ⚙️ Ejemplo 2: Fila de 6 personas

¿De cuántas formas pueden formarse 6 personas en una fila?

$$
P_6 = 6! = 720 \text{ formas}
$$

---

## 📖 Permutaciones Parciales (Variaciones)

> ¿De cuántas formas puedes elegir **r elementos** de un conjunto de **n elementos** cuando el **orden importa**?

### 💡 Fórmula:

$$
P(n,r) = \frac{n!}{(n-r)!} = n \times (n-1) \times ... \times (n-r+1)
$$

### ⚙️ Ejemplo 1: Medallas en una carrera

En una carrera de 10 participantes, ¿de cuántas formas se pueden asignar las medallas de oro, plata y bronce?

$n = 10$ participantes, $r = 3$ medallas

$$
P(10,3) = \frac{10!}{(10-3)!} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720
$$

### ⚙️ Ejemplo 2: Directiva de un club

De 15 miembros, ¿de cuántas formas puedes elegir presidente, vicepresidente, secretario y tesorero?

$n = 15$, $r = 4$

$$
P(15,4) = 15 \times 14 \times 13 \times 12 = 32,760
$$

---

## 📖 Permutaciones con Repetición

> Cuando hay **elementos repetidos**, dividimos entre los factoriales de las repeticiones.

### 💡 Fórmula:

Si tenemos n elementos donde:
- $n_1$ son del tipo 1
- $n_2$ son del tipo 2
- y así sucesivamente...

$$
P = \frac{n!}{n_1! \cdot n_2! \cdot ... \cdot n_k!}
$$

### ⚙️ Ejemplo 1: Palabra MAMA

¿De cuántas formas diferentes puedes ordenar las letras de MAMA?

- Total de letras: 4
- M se repite 2 veces
- A se repite 2 veces

$$
P = \frac{4!}{2! \cdot 2!} = \frac{24}{2 \times 2} = \frac{24}{4} = 6
$$

### ⚙️ Ejemplo 2: Palabra ESTADÍSTICA

¿De cuántas formas diferentes puedes ordenar las letras de ESTADÍSTICA?

- Total de letras: 11
- E: 1, S: 2, T: 2, A: 2, D: 1, Í: 1, I: 1, C: 1

$$
P = \frac{11!}{1! \cdot 2! \cdot 2! \cdot 2! \cdot 1! \cdot 1! \cdot 1! \cdot 1!} = \frac{39,916,800}{8} = 4,989,600
$$

---

## 📖 Permutaciones Circulares

> Cuando los elementos se ordenan en **círculo** (sin principio ni fin), hay menos arreglos.

### 💡 Fórmula:

$$
P_{circular} = (n-1)!
$$

### ⚙️ Ejemplo: Mesa redonda

¿De cuántas formas pueden sentarse 6 personas alrededor de una mesa redonda?

$$
P_{circular} = (6-1)! = 5! = 120
$$

### 💡 ¿Por qué (n-1)!?

En un círculo, podemos "fijar" una persona y solo contar las formas de ordenar a las demás (ya que rotar todo el círculo da el mismo arreglo).

---

## 💡 ¿Cuándo es Permutación?

| Pregunta | Si la respuesta es SÍ... |
|----------|-------------------------|
| ¿El orden importa? | Es permutación |
| ¿"Primero" y "segundo" son diferentes? | Es permutación |
| ¿Las posiciones son distinguibles? | Es permutación |

### ⚙️ Ejemplos:

| Situación | ¿Orden importa? | Tipo |
|-----------|-----------------|------|
| Elegir presidente y vicepresidente | Sí | Permutación |
| Elegir un comité de 3 personas | No | Combinación |
| Formar palabra con letras | Sí | Permutación |
| Elegir 5 números de lotería | No | Combinación |

---

## 🔑 Resumen

| Concepto | Fórmula | Ejemplo |
|----------|---------|---------|
| **Factorial** | $n!$ | $5! = 120$ |
| **Permutación total** | $n!$ | Ordenar 5 libros = 120 |
| **Permutación parcial** | $\frac{n!}{(n-r)!}$ | 3 de 10 = 720 |
| **Con repetición** | $\frac{n!}{n_1! \cdot n_2!...}$ | MAMA = 6 |
| **Circular** | $(n-1)!$ | 6 en mesa = 120 |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula:
a) 7!
b) P(8,3)
c) Permutaciones de las letras de "LEER"

<details>
<summary>Ver solución</summary>

a) $7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5,040$

b) $P(8,3) = 8 \times 7 \times 6 = 336$

c) "LEER" tiene 4 letras: L(1), E(2), R(1)
$$P = \frac{4!}{1! \cdot 2! \cdot 1!} = \frac{24}{2} = 12$$

</details>

### Ejercicio 2
¿De cuántas formas pueden sentarse 8 personas en una fila para una foto?

<details>
<summary>Ver solución</summary>

Es una permutación total (orden importa en una foto):

$$P_8 = 8! = 40,320 \text{ formas}$$

</details>

### Ejercicio 3
De un grupo de 12 candidatos, ¿de cuántas formas se pueden elegir los 3 primeros lugares en una competencia?

<details>
<summary>Ver solución</summary>

El orden importa (1°, 2°, 3° son diferentes):

$$P(12,3) = 12 \times 11 \times 10 = 1,320 \text{ formas}$$

</details>

### Ejercicio 4
¿De cuántas formas diferentes pueden sentarse 5 personas alrededor de una mesa redonda?

<details>
<summary>Ver solución</summary>

Es una permutación circular:

$$P_{circular} = (5-1)! = 4! = 24 \text{ formas}$$

</details>

### Ejercicio 5
¿Cuántas "palabras" diferentes (con o sin sentido) puedes formar con las letras de MISSISSIPPI?

<details>
<summary>Ver solución</summary>

MISSISSIPPI tiene 11 letras:
- M: 1
- I: 4
- S: 4
- P: 2

$$P = \frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39,916,800}{1 \times 24 \times 24 \times 2} = \frac{39,916,800}{1,152} = 34,650$$

</details>

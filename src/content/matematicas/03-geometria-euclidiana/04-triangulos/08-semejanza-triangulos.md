# **Semejanza de Triángulos**

¿Alguna vez has hecho zoom en una foto en tu celular? La imagen se hace más grande, pero las personas y objetos no se deforman; mantienen su forma exacta. En geometría, esto se llama **semejanza**. Dos figuras son semejantes cuando son una "copia a escala" la una de la otra.

---

## 🎯 ¿Qué vas a aprender?

- Comprender qué significa que dos triángulos sean semejantes.
- Calcular la razón de semejanza ($k$) entre dos figuras.
- Aplicar los criterios de semejanza (AA, LLL, LAL).
- Resolver problemas hallando lados desconocidos usando proporciones.
- Relacionar las áreas de triángulos semejantes.

---

## 📐 Concepto de Semejanza

Dos triángulos son **semejantes** si tienen la misma forma, aunque tengan distinto tamaño.

Para que esto ocurra, deben cumplirse dos condiciones simultáneamente:
1.  Sus **ángulos correspondientes** son iguales.
2.  Sus **lados correspondientes** son proporcionales.

El símbolo de la semejanza es $\sim$.

$$
\triangle ABC \sim \triangle DEF
$$

### Razón de Semejanza ($k$)

Es el número por el que multiplicamos los lados del triángulo pequeño para obtener los del grande.

$$
\frac{DE}{AB} = \frac{EF}{BC} = \frac{DF}{AC} = k
$$

---

## 🔍 Criterios de Semejanza

Al igual que en la congruencia, existen "atajos" para saber si dos triángulos son semejantes sin medir todo.

### 1. Criterio AA (Ángulo-Ángulo)

Es el más usado. Si dos triángulos tienen **dos ángulos iguales**, entonces son semejantes. (El tercer ángulo obligatoriamente será igual porque suman 180°).

$$
\text{Si } \angle A = \angle D \text{ y } \angle B = \angle E \implies \triangle ABC \sim \triangle DEF
$$

### 2. Criterio LLL (Lados Proporcionales)

Si los tres lados de un triángulo son proporcionales a los tres lados del otro, son semejantes.

$$
\frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c} = k \implies \text{Semejantes}
$$

### 3. Criterio LAL (Lado-Ángulo-Lado)

Si tienen dos lados proporcionales y el ángulo **comprendido** entre ellos es igual, son semejantes.

$$
\frac{a'}{a} = \frac{c'}{c} \text{ y } \angle B = \angle B' \implies \text{Semejantes}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo de la razón de semejanza

Un triángulo tiene lados 3, 4 y 5. Otro triángulo tiene lados 9, 12 y 15. ¿Son semejantes? ¿Cuál es la razón?

**Datos:**
Lados $T_1$: 3, 4, 5.
Lados $T_2$: 9, 12, 15.

**Razonamiento:**
Calculamos el cociente entre lados correspondientes (mayor con mayor, menor con menor).

$$
\frac{9}{3} = 3
$$

$$
\frac{12}{4} = 3
$$

$$
\frac{15}{5} = 3
$$

Como todas las razones dan lo mismo ($3$), son semejantes por criterio **LLL**.

**Resultado:**
$$
\boxed{\text{Sí, son semejantes con } k = 3}
$$

### Ejemplo 2: Hallar un lado desconocido

Los triángulos $\triangle ABC$ y $\triangle DEF$ son semejantes.
En $\triangle ABC$, el lado $AB = 8$ cm.
En $\triangle DEF$, el lado correspondiente $DE = 4$ cm y el lado $EF = 6$ cm.
¿Cuánto mide el lado $BC$?

**Razonamiento:**
Primero hallamos la razón de semejanza del segundo al primero (o viceversa).
Usamos los lados correspondientes conocidos $AB$ y $DE$.

$$
k = \frac{AB}{DE} = \frac{8}{4} = 2
$$

Esto significa que el triángulo $ABC$ es el doble de grande que $DEF$.
Para hallar $BC$, multiplicamos su correspondiente $EF$ por la razón.

$$
BC = EF \cdot k
$$

$$
BC = 6 \cdot 2
$$

**Resultado:**
$$
\boxed{12 \text{ cm}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Determina si dos triángulos son semejantes si el primero tiene ángulos de 40° y 70°, y el segundo tiene ángulos de 70° y 80°.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Calculamos el tercer ángulo del primer triángulo:
$180^\circ - 40^\circ - 70^\circ = 70^\circ$.
Ángulos del primero: 40°, 70°, 70°.
Ángulos del segundo: 70°, 80°, y el tercero es $180^\circ-150^\circ=30^\circ$.

Los ángulos no coinciden.

**Resultado:**
$$
\boxed{\text{No son semejantes}}
$$

</details>

### Ejercicio 2
Si un mapa está a escala 1:1000, ¿qué significa esto en términos de semejanza?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El mapa y el terreno real son figuras semejantes.
La razón de semejanza es $k = 1000$ (si vamos del mapa a la realidad).
1 cm en el mapa equivale a 1000 cm en la realidad.

**Resultado:**
$$
\boxed{\text{Son figuras semejantes con razón } k=1000}
$$

</details>

### Ejercicio 3
Calcula la altura de un árbol si proyecta una sombra de 12 m, al mismo tiempo que un poste de 2 m de altura proyecta una sombra de 3 m.

<details>
<summary>Ver solución</summary>

**Datos:**
Triángulo Árbol: Altura $h$, Sombra 12.
Triángulo Poste: Altura 2, Sombra 3.
Los rayos del sol caen paralelos, formando triángulos semejantes (AA).

**Razonamiento:**
Establecemos la proporción:

$$
\frac{h}{2} = \frac{12}{3}
$$

$$
\frac{h}{2} = 4
$$

$$
h = 4 \cdot 2
$$

**Resultado:**
$$
\boxed{8 \text{ m}}
$$

</details>

### Ejercicio 4
En un triángulo, trazamos una línea paralela a la base. ¿El triángulo pequeño que se forma en la punta es semejante al triángulo grande original?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Al trazar una paralela, los ángulos correspondientes son iguales.
El ángulo superior es común.
Por criterio AA, los triángulos son semejantes. (Teorema fundamental de la semejanza).

**Resultado:**
$$
\boxed{\text{Sí, son semejantes}}
$$

</details>

### Ejercicio 5
Dos triángulos semejantes tienen una razón de semejanza $k=3$. Si el perímetro del pequeño es 15 cm, ¿cuál es el perímetro del grande?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La razón de los perímetros es igual a la razón de semejanza $k$.

$$
P_{grande} = P_{pequeño} \cdot k
$$

$$
P_{grande} = 15 \cdot 3
$$

**Resultado:**
$$
\boxed{45 \text{ cm}}
$$

</details>

### Ejercicio 6
Dos triángulos semejantes tienen una razón de semejanza $k=3$. Si el área del pequeño es $10 \text{ cm}^2$, ¿cuál es el área del grande?

<details>
<summary>Ver solución</summary>

**Datos:**
$k = 3$.
$A_1 = 10$.

**Razonamiento:**
La razón de las áreas es el **cuadrado** de la razón de semejanza ($k^2$).

$$
A_2 = A_1 \cdot k^2
$$

$$
A_2 = 10 \cdot 3^2
$$

$$
A_2 = 10 \cdot 9
$$

**Resultado:**
$$
\boxed{90 \text{ cm}^2}
$$

</details>

### Ejercicio 7
Halla $x$ si $\triangle ABC \sim \triangle DEF$.
Lados $ABC$: 4, 6, $x$.
Lados $DEF$: 2, 3, 5.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Vemos la relación entre los lados conocidos.
$4 \to 2$ (La mitad).
$6 \to 3$ (La mitad).
Pasar de $ABC$ a $DEF$ es dividir por 2 (o multiplicar por $0.5$).
Pasar de $DEF$ a $ABC$ es multiplicar por 2.

$$
x = 5 \cdot 2
$$

**Resultado:**
$$
\boxed{x = 10}
$$

</details>

### Ejercicio 8
¿Todos los triángulos equiláteros son semejantes entre sí?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Un triángulo equilátero tiene siempre sus tres ángulos internos de 60°.
Por el criterio AA (tienen los mismos ángulos), cualquier par de triángulos equiláteros será semejante.

**Resultado:**
$$
\boxed{\text{Sí, siempre}}
$$

</details>

### Ejercicio 9
¿Todos los triángulos rectángulos son semejantes entre sí?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Todos tienen un ángulo de 90°.
Pero los otros dos ángulos pueden variar (ej. 45-45 vs 30-60).
No cumplen necesariamente el criterio AA.

**Resultado:**
$$
\boxed{\text{No necesariamente}}
$$

</details>

### Ejercicio 10
Si la razón de semejanza entre dos triángulos es $k=1$, ¿cómo se llaman esos triángulos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $k=1$, significa que los lados miden lo mismo y no hay cambio de tamaño.
Son triángulos iguales en forma y tamaño.

**Resultado:**
$$
\boxed{\text{Congruentes}}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula / Regla | Nota Clave |
|----------|-----------------|------------|
| **Semejanza** | Misma forma, distinto tamaño | Ángulos iguales, lados proporcionales. |
| **Razón ($k$)** | $k = \frac{\text{Lado Grande}}{\text{Lado Pequeño}}$ | Factor de escala. |
| **Criterio AA** | $\angle A = \angle A', \angle B = \angle B'$ | El criterio más rápido. |
| **Áreas** | $\frac{A_2}{A_1} = k^2$ | El área crece al cuadrado de $k$. |

> La semejanza es la base de los mapas, los planos, la fotografía y el funcionamiento de nuestra propia visión al percibir distancias.

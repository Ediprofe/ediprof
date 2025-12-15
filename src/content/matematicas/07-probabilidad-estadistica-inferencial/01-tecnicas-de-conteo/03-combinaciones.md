# Combinaciones

¿Y si el orden **no** importa? Cuando solo queremos elegir elementos sin importar el orden, usamos **combinaciones**.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las combinaciones y cuándo usarlas
- La fórmula de combinaciones
- Diferencia entre permutaciones y combinaciones
- Propiedades de las combinaciones

---

## 📊 Fórmula de Combinaciones

$$
C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

Se lee "n elige r" o "combinación de n en r".

---

## 📖 ¿Qué son las Combinaciones?

> Una **combinación** es una selección de elementos donde el **orden no importa**.

### 💡 Clave:

- En **permutaciones**: {A, B, C} y {C, B, A} son **diferentes**
- En **combinaciones**: {A, B, C} y {C, B, A} son **iguales**

### ⚙️ Ejemplo comparativo:

**Pregunta 1:** ¿De cuántas formas puedes elegir presidente, vicepresidente y secretario de 5 personas?
→ **Permutación** (los cargos son diferentes)

**Pregunta 2:** ¿De cuántas formas puedes elegir un comité de 3 personas de 5?
→ **Combinación** (solo importa quiénes están en el comité)

---

## 📖 Fórmula de Combinaciones

### 💡 Derivación:

Las combinaciones son las permutaciones divididas entre las formas de ordenar cada grupo:

$$
C(n,r) = \frac{P(n,r)}{r!} = \frac{n!}{r!(n-r)!}
$$

### 💡 Notación:

$$
C(n,r) = C_n^r = \binom{n}{r} = _nC_r
$$

Todas estas notaciones significan "n elige r".

---

## 📖 Cálculo de Combinaciones

### ⚙️ Ejemplo 1: Elegir comité de 3 de 10 personas

$$
C(10,3) = \frac{10!}{3!(10-3)!} = \frac{10!}{3! \cdot 7!}
$$

Simplificando:
$$
= \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120
$$

### ⚙️ Ejemplo 2: Elegir 5 cartas de una baraja de 52

$$
C(52,5) = \frac{52!}{5! \cdot 47!} = \frac{52 \times 51 \times 50 \times 49 \times 48}{5 \times 4 \times 3 \times 2 \times 1}
$$
$$
= \frac{311,875,200}{120} = 2,598,960
$$

### ⚙️ Ejemplo 3: Elegir 2 de 6

$$
C(6,2) = \frac{6!}{2! \cdot 4!} = \frac{6 \times 5}{2 \times 1} = \frac{30}{2} = 15
$$

---

## 📖 Propiedades de las Combinaciones

### 💡 Propiedad 1: Simetría

$$
C(n,r) = C(n, n-r)
$$

**Ejemplo:** $C(10,3) = C(10,7) = 120$

**Razón:** Elegir 3 para incluir es lo mismo que elegir 7 para excluir.

### 💡 Propiedad 2: Casos extremos

$$
C(n,0) = C(n,n) = 1
$$

**Razón:** Solo hay una forma de elegir nada o todo.

### 💡 Propiedad 3: Elegir uno

$$
C(n,1) = n
$$

**Razón:** Elegir 1 de n tiene n opciones.

### 💡 Propiedad 4: Triángulo de Pascal

$$
C(n,r) = C(n-1, r-1) + C(n-1, r)
$$

---

## 📖 Permutación vs Combinación

| Aspecto | Permutación | Combinación |
|---------|-------------|-------------|
| ¿Orden importa? | ✅ Sí | ❌ No |
| Fórmula | $\frac{n!}{(n-r)!}$ | $\frac{n!}{r!(n-r)!}$ |
| Resultado | Mayor | Menor |
| Ejemplo | Primeros 3 lugares | Comité de 3 |

### ⚙️ Comparación numérica:

De 10 elementos, elegir 3:
- **Permutación:** $P(10,3) = 720$
- **Combinación:** $C(10,3) = 120$

La combinación es 6 veces menor porque cada grupo de 3 se puede ordenar de $3! = 6$ formas.

---

## 📖 Problemas con Múltiples Grupos

### ⚙️ Ejemplo: Comité mixto

De 8 hombres y 6 mujeres, ¿de cuántas formas puedes formar un comité de 5 con exactamente 3 hombres y 2 mujeres?

**Paso 1:** Elegir 3 hombres de 8
$$C(8,3) = \frac{8 \times 7 \times 6}{6} = 56$$

**Paso 2:** Elegir 2 mujeres de 6
$$C(6,2) = \frac{6 \times 5}{2} = 15$$

**Paso 3:** Multiplicar (ambas elecciones son consecutivas)
$$\text{Total} = 56 \times 15 = 840$$

### ⚙️ Ejemplo: Al menos uno de cada tipo

Del mismo grupo, ¿cuántos comités de 4 tienen **al menos** 1 hombre y 1 mujer?

**Estrategia:** Total - casos no deseados

**Total de comités de 4:**
$$C(14,4) = 1001$$

**Comités solo hombres:**
$$C(8,4) = 70$$

**Comités solo mujeres:**
$$C(6,4) = 15$$

**Comités mixtos:**
$$1001 - 70 - 15 = 916$$

---

## 💡 ¿Cuándo es Combinación?

| Pregunta | Si la respuesta es NO → Combinación |
|----------|-------------------------------------|
| ¿El orden importa? | Combinación |
| ¿Hay posiciones distinguibles? | Combinación |
| ¿Es lo mismo A-B-C que C-B-A? | Combinación |

---

## 🔑 Resumen

| Concepto | Fórmula |
|----------|---------|
| **Combinación** | $C(n,r) = \frac{n!}{r!(n-r)!}$ |
| **Simetría** | $C(n,r) = C(n, n-r)$ |
| **Casos base** | $C(n,0) = C(n,n) = 1$ |
| **Relación con P** | $C(n,r) = \frac{P(n,r)}{r!}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula:
a) C(8,3)
b) C(10,7)
c) C(5,5)

<details>
<summary>Ver solución</summary>

a) $C(8,3) = \frac{8 \times 7 \times 6}{6} = 56$

b) $C(10,7) = C(10,3) = \frac{10 \times 9 \times 8}{6} = 120$ (por simetría)

c) $C(5,5) = 1$ (solo hay una forma de elegir todos)

</details>

### Ejercicio 2
¿De cuántas formas puedes elegir 6 números de 49 para la lotería?

<details>
<summary>Ver solución</summary>

El orden no importa en la lotería:

$$C(49,6) = \frac{49!}{6! \cdot 43!} = \frac{49 \times 48 \times 47 \times 46 \times 45 \times 44}{720}$$
$$= 13,983,816$$

¡Casi 14 millones de combinaciones posibles!

</details>

### Ejercicio 3
De 10 estudiantes, ¿de cuántas formas puedes formar grupos de estudio de 4 personas?

<details>
<summary>Ver solución</summary>

El orden no importa (solo importa quiénes están en el grupo):

$$C(10,4) = \frac{10 \times 9 \times 8 \times 7}{24} = 210$$

</details>

### Ejercicio 4
Un examen tiene 10 preguntas y debes responder exactamente 7. ¿De cuántas formas puedes elegir qué preguntas responder?

<details>
<summary>Ver solución</summary>

$$C(10,7) = C(10,3) = \frac{10 \times 9 \times 8}{6} = 120$$

</details>

### Ejercicio 5
De 7 ingenieros y 5 médicos, ¿de cuántas formas puedes formar un equipo de 6 con exactamente 4 ingenieros?

<details>
<summary>Ver solución</summary>

Si hay 4 ingenieros, debe haber 2 médicos.

Elegir 4 de 7 ingenieros: $C(7,4) = 35$
Elegir 2 de 5 médicos: $C(5,2) = 10$

$$\text{Total} = 35 \times 10 = 350$$

</details>

# **Combinaciones**

Si ganas la lotería con los números "5, 12, 33", te da igual si salieron en ese orden o si salieron "33, 12, 5". Son los mismos números, es el mismo premio. Cuando el orden de los elementos **NO altera el resultado**, dejamos de hablar de Permutaciones y entramos al mundo de las **Combinaciones**.

---

## 🎯 ¿Qué vas a aprender?

- Calcular combinaciones ($nCr$).
- Entender por qué dividimos por $r!$ (eliminar el orden).
- Aprovechar la simetría ($10C3 = 10C7$).
- Resolver problemas de grupos mixtos (Hombres/Mujeres, Cartas, etc.).

---

## La Fórmula de la Combinación ($nCr$)

Para calcular combinaciones, primero calculamos como si el orden importara (Permutación) y luego dividimos por las formas de ordenar esos elementos, para eliminar la duplicidad.

$$ _nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!} $$

- $n$: Total de elementos disponibles.
- $r$: Cuántos vamos a elegir.

---

## Inducción: ¿Por qué es menor que la Permutación?

Imagina elegir 3 letras de {A, B, C, D}.
- **Permutación:** ABC, ACB, BAC, BCA, CAB, CBA... (Son 6 casos distintos).
- **Combinación:** {A, B, C}. (Es 1 solo caso).
Por eso la combinación siempre es un número menor.

---

## Tipos de Problemas

### 1. Selección Simple
Elegir un subgrupo donde todos son iguales en jerarquía.

#### ⚙️ Ejemplos Resueltos
1.  **Comité de Estudio:** De 10 alumnos, elegir 3 para un trabajo.
    $_10C_3 = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = 120$.
2.  **Juego de Cartas:** Mano de 5 cartas de una baraja de 52.
    $_52C_5 = 2,598,960$.
3.  **Helado:** Elegir 2 bolas de 10 sabores (en un vaso, sin importar cuál va abajo).
    $_10C_2 = 45$.
4.  **Examen:** Responder 3 preguntas de 5 opcionales.
    $_5C_3 = 10$.
5.  **Saludo:** 4 personas se saludan entre sí. ¿Cuántos apretones de mano?
    $_4C_2 = 6$.

### 2. Selección con Grupos Mixtos (Multiplicación de Combinaciones)
Elegir un poco de aquí y un poco de allá.

#### ⚙️ Ejemplos Resueltos
1.  **Comité Mixto:** 5 Hombres, 6 Mujeres. Armar grupo de 2 Hombres Y 2 Mujeres.
    $(_5C_2) \times (_6C_2) = 10 \times 15 = 150$.
2.  **Baraja:** 4 Ases, 48 Otras. Sacar 2 Ases Y 3 Otras.
    $(_4C_2) \times (_48C_3) = 6 \times 17,296 = 103,776$.
3.  **Frutas:** 3 Manzanas, 4 Peras. Elegir 1 de cada una.
    $(_3C_1) \times (_4C_1) = 3 \times 4 = 12$.
4.  **Equipo:** 3 Arqueros, 10 Jugadores. Elegir 1 Arquero Y 4 Jugadores.
    $(_3C_1) \times (_10C_4) = 3 \times 210 = 630$.
5.  **Bolsa de Canicas:** 5 Rojas, 3 Azules. Sacar 2 Rojas Y 1 Azul.
    $(_5C_2) \times (_3C_1) = 10 \times 3 = 30$.

### 3. Propiedad de Simetría
Elegir a quiénes **invitas** es lo mismo que elegir a quiénes **no invitas**.
$$ _nC_r = _nC_{n-r} $$

#### ⚙️ Ejemplos Resueltos
1.  **$_10C_8$:** Es difícil calcular $\frac{10!}{8!2!}$.
    Mejor calculo $_10C_2 = 45$. ¡Es igual!
2.  **$_50C_49$:** Elegir 49 de 50.
    Es lo mismo que $_50C_1 = 50$.
3.  **$_5C_5$:** Elegir todos.
    Es lo mismo que $_5C_0$ (Elegir ninguno). = 1.
4.  **$_100C_98$:**
    Es $_100C_2 = 4,950$.
5.  **$_7C_4$ vs $_7C_3$:**
    Son idénticos (35).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $_5C_2$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $\frac{5 \cdot 4}{2 \cdot 1} = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 2
Tienes 6 ingredientes para pizza. ¿Cuántas pizzas de 2 ingredientes puedes hacer?

<details>
<summary>Ver solución</summary>

**Cálculo:** $_6C_2 = 15$.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 3
Calcula $_8C_6$ usando la simetría.

<details>
<summary>Ver solución</summary>

**Simetría:** Es igual a $_8C_2$.
$\frac{8 \cdot 7}{2} = 28$.
**Resultado:** $\boxed{28}$

</details>

### Ejercicio 4
De 4 candidatos, ¿cuántas ternas (3) se pueden formar?

<details>
<summary>Ver solución</summary>

**Simetría:** Elegir 3 es dejar 1 por fuera. $_4C_1 = 4$.
**Resultado:** $\boxed{4}$

</details>

### Ejercicio 5
En una lotería de 45 números, aciertas 6. ¿Importa el orden?

<details>
<summary>Ver solución</summary>

**Concepto:** No importa.
**Resultado:** $\boxed{\text{Es Combinación}}$

</details>

### Ejercicio 6
Calcula $_7C_7$.

<details>
<summary>Ver solución</summary>

**Propiedad:** Solo hay 1 forma de elegir todo.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 7
Hay 5 puntos en un papel, no hay 3 alineados. ¿Cuántos triángulos puedes dibujar uniendo los puntos?

<details>
<summary>Ver solución</summary>

**Análisis:** Un triángulo necesita 3 puntos.
**Cálculo:** $_5C_3$. (Igual a $_5C_2$). $10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 8
Grupo de 10 personas. ¿Cuántos apretones de mano si todos se saludan?

<details>
<summary>Ver solución</summary>

**Cálculo:** $_10C_2 = \frac{10 \cdot 9}{2} = 45$.
**Resultado:** $\boxed{45}$

</details>

### Ejercicio 9
Elegir 3 vocales de las 5 existentes.

<details>
<summary>Ver solución</summary>

**Cálculo:** $_5C_3 = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 10
De 5 físicos y 4 químicos, formar comité de 2 físicos y 1 químico.

<details>
<summary>Ver solución</summary>

**Cálculo:** $(_5C_2) \times (_4C_1) = 10 \times 4 = 40$.
**Resultado:** $\boxed{40}$

</details>

---

## 🔑 Resumen

| Concepto | Permutación ($nPr$) | Combinación ($nCr$) |
|----------|---------------------|---------------------|
| **Orden** | ✅ Importa. | ❌ No importa. |
| **Clave** | Jerarquías, Posiciones. | Grupos, Subconjuntos. |
| **Valor** | Más grande. | Más pequeño. |

> **Conclusión:** Si preguntas "¿Quién es primero?", es Permutación. Si preguntas "¿Quiénes están en el equipo?", es Combinación.

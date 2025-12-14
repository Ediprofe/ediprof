# Semejanza de Triángulos

Dos triángulos son **semejantes** cuando tienen la misma forma, aunque no necesariamente el mismo tamaño. Es como una "copia a escala" de un triángulo.

---

## 📖 ¿Qué es la semejanza?

Dos triángulos son **semejantes** si:
- Sus **ángulos correspondientes son iguales**
- Sus **lados correspondientes son proporcionales**

> **Definición:** Dos triángulos son semejantes si uno es una ampliación o reducción del otro.

### Símbolo

$$
\triangle ABC \sim \triangle DEF
$$

Se lee: "El triángulo ABC es semejante al triángulo DEF"

---

## 📖 Diferencia entre congruencia y semejanza

| Característica | Congruencia | Semejanza |
|----------------|-------------|-----------|
| Forma | Igual | Igual |
| Tamaño | Igual | Puede ser diferente |
| Lados | Iguales | Proporcionales |
| Ángulos | Iguales | Iguales |
| Símbolo | $\cong$ | $\sim$ |

> **Nota:** Todo par de triángulos congruentes son también semejantes, pero no al revés.

---

## 📖 Razón de semejanza

La **razón de semejanza** ($k$) es el factor por el cual se multiplican los lados de un triángulo para obtener los lados del otro.

$$
k = \frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c}
$$

### Ejemplo

Si un triángulo tiene lados de 3, 4, 5 cm y otro tiene lados de 6, 8, 10 cm:

$$
k = \frac{6}{3} = \frac{8}{4} = \frac{10}{5} = 2
$$

La razón de semejanza es $k = 2$ (el segundo triángulo es el doble del primero).

---

## 📖 Criterios de semejanza

### Criterio AA (Ángulo-Ángulo)

Dos triángulos son semejantes si tienen **dos ángulos iguales**.

$$
\boxed{AA: \text{ Si } \angle A = \angle A' \text{ y } \angle B = \angle B' \Rightarrow \triangle ABC \sim \triangle A'B'C'}
$$

> **Nota:** Si dos ángulos son iguales, el tercero también lo es automáticamente (porque suman 180°).

### Ejemplo

Si un triángulo tiene ángulos de 30° y 60°, y otro tiene ángulos de 60° y 90°:
- Primer triángulo: 30°, 60°, 90°
- Segundo triángulo: 60°, 90°, 30°

Son semejantes por AA.

---

### Criterio LAL (Lado-Ángulo-Lado)

Dos triángulos son semejantes si tienen **un ángulo igual** y los **lados que lo forman son proporcionales**.

$$
\boxed{LAL: \text{ Si } \frac{a}{a'} = \frac{b}{b'} \text{ y } \angle C = \angle C' \Rightarrow \triangle ABC \sim \triangle A'B'C'}
$$

### Ejemplo

Triángulo 1: lados 3 y 4 con ángulo de 50° entre ellos
Triángulo 2: lados 6 y 8 con ángulo de 50° entre ellos

$$
\frac{6}{3} = \frac{8}{4} = 2
$$

Son semejantes por LAL (razón $k = 2$).

---

### Criterio LLL (Lado-Lado-Lado)

Dos triángulos son semejantes si sus **tres lados son proporcionales**.

$$
\boxed{LLL: \text{ Si } \frac{a}{a'} = \frac{b}{b'} = \frac{c}{c'} \Rightarrow \triangle ABC \sim \triangle A'B'C'}
$$

### Ejemplo

Triángulo 1: lados 2, 3, 4 cm
Triángulo 2: lados 4, 6, 8 cm

$$
\frac{4}{2} = \frac{6}{3} = \frac{8}{4} = 2
$$

Son semejantes por LLL.

---

## 📖 Propiedades de triángulos semejantes

### Relación de perímetros

Si $k$ es la razón de semejanza:

$$
\frac{\text{Perímetro}_2}{\text{Perímetro}_1} = k
$$

### Relación de áreas

$$
\frac{\text{Área}_2}{\text{Área}_1} = k^2
$$

### Ejemplo

Si $k = 3$:
- El perímetro se triplica
- El área se multiplica por $3^2 = 9$

---

## 📖 Ejemplo completo

**Problema:** Determinar si los triángulos son semejantes y calcular la razón de semejanza.

Triángulo ABC: lados 4, 6, 8 cm
Triángulo DEF: lados 6, 9, 12 cm

**Solución:**

Verificamos si los lados son proporcionales:

$$
\frac{6}{4} = 1.5, \quad \frac{9}{6} = 1.5, \quad \frac{12}{8} = 1.5
$$

Las tres razones son iguales, entonces:

$$
\triangle ABC \sim \triangle DEF \quad \text{con } k = 1.5
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: ¿Son semejantes?

Determina si los triángulos son semejantes:

1. Triángulo 1: lados 5, 10, 15 y Triángulo 2: lados 2, 4, 6
2. Triángulo 1: ángulos 40°, 60°, 80° y Triángulo 2: ángulos 40°, 80°, 60°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí**, son semejantes. $\frac{5}{2} = \frac{10}{4} = \frac{15}{6} = 2.5$
2. **Sí**, son semejantes. Tienen los mismos tres ángulos (AA).

</details>

---

### Ejercicio 2: Encontrar lado desconocido

Los triángulos ABC y DEF son semejantes con $k = 3$. Si $AB = 4$ cm, ¿cuánto mide $DE$?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
DE = AB \times k = 4 \times 3 = 12 \text{ cm}
$$

</details>

---

### Ejercicio 3: Relación de áreas

Dos triángulos semejantes tienen razón de semejanza $k = 2$. Si el área del triángulo pequeño es 10 cm², ¿cuál es el área del grande?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\text{Área}_2 = \text{Área}_1 \times k^2 = 10 \times 2^2 = 10 \times 4 = 40 \text{ cm}^2
$$

</details>

---

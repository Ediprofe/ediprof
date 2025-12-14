# Congruencia de Triángulos

Dos triángulos son **congruentes** cuando tienen la misma forma y el mismo tamaño. En esta lección estudiaremos qué significa la congruencia y los criterios para determinar si dos triángulos son congruentes.

---

## 📖 ¿Qué es la congruencia?

Dos figuras son **congruentes** cuando tienen exactamente la **misma forma** y el **mismo tamaño**.

> **Definición:** Dos triángulos son congruentes si sus tres lados y sus tres ángulos son respectivamente iguales.

### Símbolo

$$
\triangle ABC \cong \triangle DEF
$$

Se lee: "El triángulo ABC es congruente al triángulo DEF"

### ¿Qué significa "respectivamente iguales"?

Significa que los elementos correspondientes son iguales:
- Lado $AB$ = Lado $DE$
- Lado $BC$ = Lado $EF$
- Lado $CA$ = Lado $FD$
- $\angle A = \angle D$
- $\angle B = \angle E$
- $\angle C = \angle F$

---

## 📖 Los criterios de congruencia

No es necesario verificar los 6 elementos (3 lados + 3 ángulos) para saber si dos triángulos son congruentes. Existen **criterios** que permiten demostrarlo con menos información.

---

## 📖 Criterio LLL (Lado-Lado-Lado)

Dos triángulos son congruentes si sus **tres lados** son respectivamente iguales.

$$
\boxed{LLL: \text{ Si } a = a', b = b', c = c' \Rightarrow \triangle ABC \cong \triangle A'B'C'}
$$

### Ejemplo

Si el triángulo $ABC$ tiene lados de 3, 4 y 5 cm, y el triángulo $DEF$ también tiene lados de 3, 4 y 5 cm, entonces son congruentes por LLL.

---

## 📖 Criterio LAL (Lado-Ángulo-Lado)

Dos triángulos son congruentes si tienen **dos lados iguales** y el **ángulo comprendido** (entre esos lados) también es igual.

$$
\boxed{LAL: \text{ Si } a = a', \angle B = \angle B', c = c' \Rightarrow \triangle ABC \cong \triangle A'B'C'}
$$

### Importante

El ángulo debe ser el que está **entre** los dos lados considerados.

### Ejemplo

Si dos triángulos tienen:
- Un lado de 5 cm
- Un ángulo de 60° (entre los dos lados)
- Otro lado de 7 cm

Entonces son congruentes por LAL.

---

## 📖 Criterio ALA (Ángulo-Lado-Ángulo)

Dos triángulos son congruentes si tienen **un lado igual** y los **dos ángulos adyacentes** a ese lado también son iguales.

$$
\boxed{ALA: \text{ Si } \angle A = \angle A', c = c', \angle B = \angle B' \Rightarrow \triangle ABC \cong \triangle A'B'C'}
$$

### Ejemplo

Si dos triángulos tienen:
- Un ángulo de 40°
- Un lado de 8 cm (entre los dos ángulos)
- Un ángulo de 70°

Entonces son congruentes por ALA.

---

## 📖 Criterio LLA (Lado-Lado-Ángulo) - Caso especial

Este criterio solo funciona cuando el ángulo es el **opuesto al lado mayor**.

En la práctica, se usa más el caso especial para triángulos **rectángulos** (ver abajo).

---

## 📖 Criterio para triángulos rectángulos

Para triángulos rectángulos existe un criterio adicional:

### Criterio Hipotenusa-Cateto

Dos triángulos rectángulos son congruentes si tienen **la hipotenusa y un cateto** respectivamente iguales.

---

## 📖 Tabla resumen de criterios

| Criterio | Elementos iguales | Observación |
|----------|-------------------|-------------|
| LLL | 3 lados | El más básico |
| LAL | 2 lados + ángulo entre ellos | El ángulo debe estar "en medio" |
| ALA | 2 ángulos + lado entre ellos | El lado debe estar "en medio" |
| Hipotenusa-Cateto | Hipotenusa + 1 cateto | Solo para triángulos rectángulos |

---

## 📖 Ejemplo completo

**Problema:** Demostrar que los triángulos $ABC$ y $DEF$ son congruentes si:
- $AB = DE = 5$ cm
- $\angle B = \angle E = 50°$
- $BC = EF = 7$ cm

**Solución:**

Tenemos:
- Lado $AB = DE$ ✓
- Ángulo $\angle B = \angle E$ ✓ (el ángulo está entre los dos lados)
- Lado $BC = EF$ ✓

Por el criterio **LAL**, los triángulos son congruentes:

$$
\triangle ABC \cong \triangle DEF
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar el criterio

¿Qué criterio de congruencia se aplica en cada caso?

1. Ambos triángulos tienen lados de 6, 8 y 10 cm
2. Ambos tienen ángulos de 30° y 60° con un lado de 5 cm entre ellos
3. Ambos tienen lados de 4 y 7 cm con un ángulo de 90° entre ellos

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **LLL** (tres lados iguales)
2. **ALA** (dos ángulos y el lado entre ellos)
3. **LAL** (dos lados y el ángulo entre ellos)

</details>

---

### Ejercicio 2: ¿Son congruentes?

Determina si los triángulos son congruentes:

Triángulo 1: Lados de 5, 7, 9 cm
Triángulo 2: Lados de 5, 9, 7 cm

<details>
<summary><strong>Ver respuesta</strong></summary>

**Sí**, son congruentes por **LLL**.

Los lados son los mismos (5, 7, 9), solo están listados en diferente orden.

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Dos triángulos con los mismos tres ángulos son congruentes.
2. Si dos triángulos tienen un lado de 10 cm y ángulos de 60° y 50°, son congruentes.
3. Dos triángulos equiláteros con el mismo perímetro son congruentes.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Pueden tener la misma forma pero diferente tamaño (semejantes, no congruentes)
2. **Verdadero** - Por ALA (el tercer ángulo sería 70°, y el lado está "entre" los ángulos)
3. **Verdadero** - Si tienen el mismo perímetro, tienen los mismos lados (LLL)

</details>

---

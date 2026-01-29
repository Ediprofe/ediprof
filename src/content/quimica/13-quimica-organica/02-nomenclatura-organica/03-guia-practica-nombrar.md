# Guía Práctica para Nombrar Compuestos Orgánicos

> **¿Cómo nombrar cualquier compuesto orgánico paso a paso?** 🤔

Esta lección te da un **algoritmo práctico** que puedes seguir para nombrar cualquier molécula orgánica de manera sistemática.

## 🎯 ¿Qué vas a aprender?

- Un método paso a paso para nombrar compuestos
- Cómo manejar casos con múltiples grupos funcionales
- Trucos para evitar errores comunes

---

## 📋 Algoritmo de Nomenclatura

### Los 5 Pasos Fundamentales

```
┌─────────────────────────────────────────┐
│  PASO 1: Identificar grupo funcional   │
│          principal (sufijo)             │
├─────────────────────────────────────────┤
│  PASO 2: Encontrar cadena principal    │
│          (la más larga con el grupo)   │
├─────────────────────────────────────────┤
│  PASO 3: Numerar la cadena             │
│          (grupo funcional número bajo) │
├─────────────────────────────────────────┤
│  PASO 4: Identificar sustituyentes     │
│          (todo lo que cuelga)          │
├─────────────────────────────────────────┤
│  PASO 5: Construir el nombre           │
│          (alfabético + raíz + sufijo)  │
└─────────────────────────────────────────┘
```

---

## ⚙️ Paso 1: Identificar el Grupo Funcional Principal

### Jerarquía de prioridad

| Prioridad | Grupo | Fórmula | Sufijo |
|-----------|-------|---------|--------|
| 1 | Ácido carboxílico | -COOH | -oico |
| 2 | Éster | -COOR | -oato de R |
| 3 | Amida | -CONH₂ | -amida |
| 4 | Aldehído | -CHO | -al |
| 5 | Cetona | -CO- | -ona |
| 6 | Alcohol | -OH | -ol |
| 7 | Amina | -NH₂ | -amina |
| 8 | Alqueno | C=C | -eno |
| 9 | Alquino | C≡C | -ino |
| 10 | Alcano | C-C | -ano |

> 💡 **Truco:** "Los **A**cidos **E**logian **A**l **A**gua **C**on **A**zúcar **A**marilla **E**n **I**nvierno **A**zul"
> (Ácido, Éster, Amida, Aldehído, Cetona, Alcohol, Amina, Eno, Ino, Ano)

---

## ⚙️ Paso 2: Encontrar la Cadena Principal

### Criterios en orden

1. **Contiene el grupo funcional** de mayor jerarquía
2. **Mayor número de carbonos** continuos
3. **Mayor número de enlaces múltiples**
4. **Mayor número de sustituyentes** unidos

### Ejemplo

```
        OH
        |
CH₃—CH₂—CH—CH₂—CH₂—CH₃
        |
        CH₂—CH₂—CH₃
```

**Análisis:**
- Grupo funcional: -OH (alcohol) → debe estar en la cadena principal
- Opción A: horizontal = 6 carbonos con el -OH ✓
- Opción B: vertical = 3 carbonos sin considerar el -OH

**Cadena principal:** 6 carbonos → hex-

---

## ⚙️ Paso 3: Numerar la Cadena

### Reglas en orden de prioridad

1. El **grupo funcional principal** tiene el número más bajo
2. Si hay empate, los **enlaces múltiples** tienen número bajo
3. Si aún hay empate, los **sustituyentes** con número bajo

### Ejemplo

```
        OH
        |
CH₃—CH₂—CH—CH₂—CH₂—CH₃
 6   5   4   3   2   1     ← -OH en C4
 1   2   3   4   5   6     ← -OH en C3 ✓ (número menor)
```

Numeramos de derecha a izquierda para que el -OH esté en posición 3.

---

## ⚙️ Paso 4: Identificar Sustituyentes

### Tipos de sustituyentes

| Tipo | Ejemplos | Cómo nombrar |
|------|----------|--------------|
| **Alquilo** | CH₃-, C₂H₅- | metil, etil, propil... |
| **Halógeno** | F, Cl, Br, I | fluoro, cloro, bromo, yodo |
| **Hidroxi** | -OH (cuando no es principal) | hidroxi |
| **Amino** | -NH₂ (cuando no es principal) | amino |
| **Oxo** | =O (cuando no es principal) | oxo |

### Prefijos multiplicadores

| Cantidad | Prefijo |
|----------|---------|
| 2 | di- |
| 3 | tri- |
| 4 | tetra- |
| 5 | penta- |
| 6 | hexa- |

---

## ⚙️ Paso 5: Construir el Nombre

### Orden de escritura

$$
\boxed{\text{Sustituyentes (alfabético)} + \text{Raíz} + \text{Enlaces} + \text{Sufijo}}
$$

### Reglas de alfabetización

| Regla | Ejemplo |
|-------|---------|
| Se ordenan por la primera letra del sustituyente | cloro antes que metil |
| Los prefijos di, tri, tetra NO cuentan | dimetil va en la "m" |
| Los prefijos sec-, tert-, n- NO cuentan | tert-butil va en la "b" |
| Los prefijos iso, neo, ciclo SÍ cuentan | isopropil va en la "i" |

---

## ⚙️ Ejemplos Completos

### Ejemplo 1: Hidrocarburo con sustituyentes

```
    CH₃       CH₃
    |         |
CH₃—CH—CH₂—CH—CH₂—CH₃
```

**Paso 1:** No hay grupo funcional especial → alcano (-ano)

**Paso 2:** Cadena más larga = 6 carbonos → hex-

**Paso 3:** Numerar para menor conjunto:
```
    CH₃       CH₃
    |         |
CH₃—CH—CH₂—CH—CH₂—CH₃
 1   2   3   4   5   6    → sustituyentes en 2,4
 6   5   4   3   2   1    → sustituyentes en 3,5
```
Elegimos 2,4 porque 2 < 3.

**Paso 4:** Dos grupos metilo en 2 y 4 → 2,4-dimetil

**Paso 5:** 

$$
\boxed{\text{2,4-dimetilhexano}}
$$

---

### Ejemplo 2: Alcohol ramificado

```
        OH   CH₃
        |    |
CH₃—CH₂—CH—CH—CH₃
```

**Paso 1:** Grupo -OH → alcohol → sufijo -ol

**Paso 2:** Cadena con el -OH más larga = 5 carbonos → pent-

**Paso 3:** Numerar para -OH bajo:
```
        OH   CH₃
        |    |
CH₃—CH₂—CH—CH—CH₃
 1   2   3   4   5    → -OH en 3, metil en 4 ✓
 5   4   3   2   1    → -OH en 3, metil en 2
```
Ambos dan -OH en 3. Elegimos la primera porque el metil en 4 vs 2 da el menor número total (3+4=7 vs 3+2=5). En realidad, elegimos 1-2-3-4-5 para que el conjunto sea 3,4 vs 2,3.

**Paso 4:** Grupo metilo en posición 4 → 4-metil

**Paso 5:** 

$$
\boxed{\text{4-metilpentan-3-ol}}
$$

---

### Ejemplo 3: Compuesto con doble enlace y alcohol

```
CH₂=CH—CH₂—OH
```

**Paso 1:** Hay -OH (alcohol) y C=C (alqueno). El alcohol tiene prioridad → sufijo -ol

**Paso 2:** Cadena de 3 carbonos → prop-

**Paso 3:** Numerar para -OH bajo:
```
CH₂=CH—CH₂—OH
 3   2   1      → -OH en 1, doble en 2-3
 1   2   3      → -OH en 3, doble en 1-2
```
Elegimos la primera: -OH en posición 1.

**Paso 4:** No hay sustituyentes extra

**Paso 5:** Alqueno + alcohol = -en- + -ol

$$
\boxed{\text{prop-2-en-1-ol}}
$$

(Nombre común: alcohol alílico)

---

### Ejemplo 4: Ácido con sustituyente halogenado

```
         Cl
         |
CH₃—CH₂—CH—COOH
```

**Paso 1:** Grupo -COOH → ácido carboxílico → sufijo "ácido ...-oico"

**Paso 2:** Cadena con -COOH = 4 carbonos → but-

**Paso 3:** El -COOH **siempre es C1**:
```
         Cl
         |
CH₃—CH₂—CH—COOH
 4   3   2   1
```
Cl en posición 2.

**Paso 4:** Cloro en 2 → 2-cloro

**Paso 5:**

$$
\boxed{\text{ácido 2-clorobutanoico}}
$$

---

## 💡 Errores Comunes y Cómo Evitarlos

| Error | Correcto |
|-------|----------|
| ❌ Numerar al azar | ✅ Grupo funcional con número bajo |
| ❌ "2-metil-3-etilhexano" | ✅ "3-etil-2-metilhexano" (alfabético) |
| ❌ "dimetil" cuenta para orden | ✅ "di" no cuenta, va en la "m" |
| ❌ Olvidar la posición del grupo funcional | ✅ "butan-2-ol" no solo "butanol" |
| ❌ "hexano-2-ol" | ✅ "hexan-2-ol" (se elimina la "o" de ano) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Nombra el siguiente compuesto:

```
        Br
        |
CH₃—CH₂—C—CH₃
        |
        Br
```

<details>
<summary>Ver solución</summary>

**Paso 1:** No hay grupo funcional oxigenado → alcano

**Paso 2:** Cadena de 4 carbonos → but-

**Paso 3:** 
```
        Br
        |
CH₃—CH₂—C—CH₃
        |
        Br
 1   2   3   4    → Br en 3
 4   3   2   1    → Br en 2 ✓
```

**Paso 4:** Dos bromos en posición 2 → 2,2-dibromo

**Nombre:** **2,2-dibromobutano**

</details>

---

### Ejercicio 2
Nombra el siguiente compuesto:

```
    OH
    |
CH₃—CH—CH=CH₂
```

<details>
<summary>Ver solución</summary>

**Paso 1:** -OH (alcohol) tiene prioridad sobre C=C

**Paso 2:** Cadena de 4 carbonos → but-

**Paso 3:** 
```
    OH
    |
CH₃—CH—CH=CH₂
 4   3   2   1    → -OH en 3, doble en 1-2
 1   2   3   4    → -OH en 2, doble en 3-4
```
Elegimos -OH en posición 2 (menor).

**Paso 4:** Sin sustituyentes extra

**Nombre:** **but-3-en-2-ol**

</details>

---

### Ejercicio 3
Nombra el siguiente compuesto:

```
    O
    ‖
CH₃—C—CH₂—CH₂—CH₃
```

<details>
<summary>Ver solución</summary>

**Paso 1:** C=O en medio de cadena → cetona → sufijo -ona

**Paso 2:** Cadena de 5 carbonos → pent-

**Paso 3:** 
```
    O
    ‖
CH₃—C—CH₂—CH₂—CH₃
 1   2   3   4   5    → cetona en 2
 5   4   3   2   1    → cetona en 4
```
Elegimos cetona en posición 2.

**Nombre:** **pentan-2-ona**

</details>

---

### Ejercicio 4
Dado el nombre "3-etil-2-metilhexan-1-ol", dibuja la estructura.

<details>
<summary>Ver solución</summary>

**Decodificación:**
- hexan → 6 carbonos
- -1-ol → -OH en C1
- 2-metil → CH₃ en C2
- 3-etil → C₂H₅ en C3

**Estructura:**
```
                    C₂H₅
                    |
HO—CH₂—CH—CH—CH₂—CH₂—CH₃
       |
       CH₃
    1   2  3  4   5   6
```

</details>

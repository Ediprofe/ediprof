# Reglas IUPAC para Nomenclatura Orgánica

> **¿Por qué el mismo compuesto puede tener varios nombres?** 🤔

En química orgánica hay millones de compuestos. Para evitar confusiones, la **IUPAC** (Unión Internacional de Química Pura y Aplicada) creó un sistema de nomenclatura universal.

## 🎯 ¿Qué vas a aprender?

- Las reglas básicas para nombrar compuestos orgánicos
- Cómo identificar la cadena principal
- Cómo numerar y ubicar sustituyentes
- La estructura de un nombre IUPAC

---

## 📋 Resumen Rápido: Estructura del Nombre IUPAC

Un nombre IUPAC tiene **tres partes**:

$$
\boxed{\text{PREFIJO} + \text{RAÍZ} + \text{SUFIJO}}
$$

| Parte | Indica | Ejemplo |
|-------|--------|---------|
| **Prefijo** | Sustituyentes y su posición | 2-metil, 3-cloro |
| **Raíz** | Número de carbonos de la cadena principal | met, et, prop, but... |
| **Sufijo** | Grupo funcional principal | -ano, -eno, -ol, -al |

**Ejemplo:** 2-metilpropan-1-ol
- **2-metil** → hay un grupo metilo en el carbono 2
- **prop** → cadena de 3 carbonos
- **an** → enlaces simples
- **-1-ol** → grupo -OH en el carbono 1

---

## 📖 Paso 1: Identificar la Cadena Principal

### Regla fundamental

> La **cadena principal** es la cadena de carbonos **más larga** que contiene el **grupo funcional principal**.

### Criterios de selección (en orden de prioridad)

1. **Contiene el grupo funcional** de mayor jerarquía
2. **Mayor número de carbonos** continuos
3. **Mayor número de enlaces múltiples** (dobles y triples)
4. **Mayor número de sustituyentes**

### Ejemplo

```
        CH₃
        |
CH₃—CH₂—CH—CH₂—CH₂—CH₃
```

¿Cuál es la cadena principal?

**Opción A:** Línea horizontal = 6 carbonos ✓  
**Opción B:** Con la ramificación = 4 carbonos ✗

La cadena principal tiene **6 carbonos** → se usará la raíz "hex-"

---

## 📖 Paso 2: Numerar la Cadena

### Regla fundamental

> Numera los carbonos de la cadena principal para que el **grupo funcional tenga el número más bajo posible**.

### Si no hay grupo funcional (hidrocarburos)

Numera para que los **sustituyentes** tengan los números más bajos.

### Ejemplo

```
        CH₃
        |
CH₃—CH₂—CH—CH₂—CH₂—CH₃
 1    2   3   4   5   6    ← Numeración correcta: metilo en C3
 6    5   4   3   2   1    ← Numeración incorrecta: metilo en C4
```

El metilo en **posición 3** es mejor que en posición 4.

### Regla del menor conjunto

Si hay varios sustituyentes, compara las posiciones como conjuntos:

```
Opción A: sustituyentes en 2, 3, 5 → conjunto {2, 3, 5}
Opción B: sustituyentes en 2, 4, 5 → conjunto {2, 4, 5}
```

Se elige A porque 3 < 4 al comparar posición por posición.

---

## 📖 Paso 3: Identificar y Nombrar Sustituyentes

### ¿Qué es un sustituyente?

Un **sustituyente** es cualquier átomo o grupo unido a la cadena principal que no es hidrógeno.

### Sustituyentes tipo alquilo

Son fragmentos de hidrocarburos. Se nombran cambiando **-ano** por **-ilo** (o **-il** cuando se une):

| Fórmula | Nombre del alcano | Nombre del sustituyente |
|---------|-------------------|-------------------------|
| —CH₃ | Metano | Metilo (metil-) |
| —CH₂CH₃ | Etano | Etilo (etil-) |
| —CH₂CH₂CH₃ | Propano | Propilo (propil-) |
| —CH(CH₃)₂ | — | Isopropilo (isopropil-) |
| —CH₂CH₂CH₂CH₃ | Butano | Butilo (butil-) |
| —C(CH₃)₃ | — | *tert*-butilo (*t*-butil-) |

### Sustituyentes halógeno

| Átomo | Prefijo |
|-------|---------|
| F | fluoro- |
| Cl | cloro- |
| Br | bromo- |
| I | yodo- |

---

## 📖 Paso 4: Construir el Nombre

### Orden del nombre

1. **Sustituyentes en orden alfabético** (con su posición)
2. **Raíz** (número de carbonos)
3. **Sufijo** (grupo funcional)

### Reglas de escritura

| Regla | Ejemplo |
|-------|---------|
| Los números van separados por guiones | 2-metil |
| Múltiples números van separados por comas | 2,3-dimetil |
| Prefijos multiplicadores: di, tri, tetra | 2,2-dimetil |
| Los prefijos di, tri, tetra NO afectan orden alfabético | etil va antes de dimetil |
| Las letras *iso*, *neo*, *ciclo* SÍ afectan orden | isopropil va en la "i" |
| Las letras *sec*, *tert*, *n* NO afectan orden | *tert*-butil va en la "b" |

---

## ⚙️ Ejemplo Completo Paso a Paso

Nombrar el siguiente compuesto:

```
        CH₃   CH₃
        |     |
CH₃—CH—CH₂—CH—CH₂—CH₃
```

### Paso 1: Cadena principal
- Cadena más larga: 6 carbonos
- Raíz: **hex-**

### Paso 2: Numerar
```
        CH₃   CH₃
        |     |
CH₃—CH—CH₂—CH—CH₂—CH₃
 1   2   3   4   5   6
```
- Sustituyentes en 2 y 4
- Alternativa: 6, 5, 4, 3, 2, 1 → sustituyentes en 3 y 5
- Elegimos 2,4 porque 2 < 3

### Paso 3: Nombrar sustituyentes
- Posición 2: —CH₃ = metilo
- Posición 4: —CH₃ = metilo
- Son dos metilos = **dimetil**

### Paso 4: Construir el nombre

$$
\boxed{\text{2,4-dimetilhexano}}
$$

---

## 📊 Tabla de Raíces (Número de Carbonos)

| Carbonos | Raíz | Ejemplo |
|----------|------|---------|
| 1 | met- | metano |
| 2 | et- | etano |
| 3 | prop- | propano |
| 4 | but- | butano |
| 5 | pent- | pentano |
| 6 | hex- | hexano |
| 7 | hept- | heptano |
| 8 | oct- | octano |
| 9 | non- | nonano |
| 10 | dec- | decano |

---

## 💡 Tips para recordar

> **Truco para memorizar las raíces:**
> - 1-4: **M**ete **E**l **P**ié en la **B**oca (Met, Et, Prop, But)
> - 5-10: Penta (5 dedos), Hexa (6 como hexágono), Hepta, Octa (8 pulpos), Nona, Deca (década = 10)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica la cadena principal y nómbrala:

```
CH₃—CH₂—CH₂—CH₂—CH₃
```

<details>
<summary>Ver solución</summary>

- Cadena de 5 carbonos
- Sin sustituyentes
- Sin grupos funcionales especiales
- Nombre: **pentano**

</details>

---

### Ejercicio 2
Nombra el siguiente compuesto:

```
    CH₃
    |
CH₃—CH—CH₃
```

<details>
<summary>Ver solución</summary>

**Paso 1:** Cadena principal = 3 carbonos (prop-)

**Paso 2:** Numerar (da igual por dónde empieces, es simétrico)
```
    CH₃
    |
CH₃—CH—CH₃
 1   2   3
```

**Paso 3:** Sustituyente en posición 2 = metilo

**Nombre:** **2-metilpropano** (nombre IUPAC del isobutano)

</details>

---

### Ejercicio 3
Nombra el siguiente compuesto:

```
        Cl
        |
CH₃—CH₂—CH—CH₂—CH₃
```

<details>
<summary>Ver solución</summary>

**Paso 1:** Cadena principal = 5 carbonos (pent-)

**Paso 2:** Numerar para que el Cl tenga el número menor:
```
        Cl
        |
CH₃—CH₂—CH—CH₂—CH₃
 1   2   3   4   5
```
Cloro en posición 3.

**Paso 3:** Sustituyente = cloro

**Nombre:** **3-cloropentano**

</details>

---

### Ejercicio 4
Nombra el siguiente compuesto:

```
    CH₃       CH₃
    |         |
CH₃—C—CH₂—CH—CH₃
    |
    CH₃
```

<details>
<summary>Ver solución</summary>

**Paso 1:** Cadena principal = 5 carbonos (pent-)

**Paso 2:** Numerar:
```
    CH₃       CH₃
    |         |
CH₃—C—CH₂—CH—CH₃
    |
    CH₃
 1   2   3   4   5
```
Sustituyentes en 2, 2 y 4.

**Paso 3:** 
- Posición 2: dos metilos = 2,2-dimetil
- Posición 4: un metilo = 4-metil

**Nombre:** **2,2,4-trimetilpentano**

(Este es el componente principal de la gasolina, conocido comercialmente como "isooctano")

</details>

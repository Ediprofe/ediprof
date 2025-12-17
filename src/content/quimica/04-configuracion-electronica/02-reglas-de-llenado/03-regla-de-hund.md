# Regla de Hund

Cuando tienes varios orbitales del mismo subnivel (como los tres orbitales p), ¿cómo se distribuyen los electrones? La **Regla de Hund** dice que los electrones prefieren ocupar orbitales vacíos antes de aparearse en el mismo orbital.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la Regla de Hund
- Por qué los electrones prefieren ocupar orbitales vacíos
- Cómo aplicar la regla en diagramas de cajas
- El concepto de "máxima multiplicidad de spin"

---

## 📊 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Regla de Hund** | Los electrones llenan orbitales vacíos antes de aparearse |
| **Spines paralelos** | Los electrones en orbitales separados tienen el mismo spin |
| **Máxima multiplicidad** | Estado de menor energía |

---

## 📖 La Regla de Hund

> **"Los electrones llenan los orbitales degenerados (de igual energía) uno a la vez, con spines paralelos, antes de aparearse."**

### 💡 ¿Qué son orbitales degenerados?

Orbitales con la **misma energía**:
- Los 3 orbitales p (px, py, pz)
- Los 5 orbitales d
- Los 7 orbitales f

### 💡 Analogía: El autobús

Imagina un autobús con asientos dobles:
- Las personas prefieren sentarse **solas** primero
- Solo se sientan junto a alguien cuando no hay asientos vacíos

Los electrones hacen lo mismo con los orbitales.

---

## 📖 Aplicando la Regla de Hund

### 💡 Llenado correcto del subnivel p con 3 electrones:

```
    ✓ CORRECTO:
    ┌───┬───┬───┐
    │ ↑ │ ↑ │ ↑ │   ← Un electrón en cada orbital
    └───┴───┴───┘
    
    ✗ INCORRECTO:
    ┌───┬───┬───┐
    │ ↑↓│ ↑ │   │   ← Violación: se apareó antes de llenar
    └───┴───┴───┘
```

### 💡 Secuencia correcta de llenado para 2p:

```
    2p¹           2p²           2p³
   ┌───┬───┬───┐ ┌───┬───┬───┐ ┌───┬───┬───┐
   │ ↑ │   │   │ │ ↑ │ ↑ │   │ │ ↑ │ ↑ │ ↑ │
   └───┴───┴───┘ └───┴───┴───┘ └───┴───┴───┘
   
    2p⁴           2p⁵           2p⁶
   ┌───┬───┬───┐ ┌───┬───┬───┐ ┌───┬───┬───┐
   │ ↑↓│ ↑ │ ↑ │ │ ↑↓│ ↑↓│ ↑ │ │ ↑↓│ ↑↓│ ↑↓│
   └───┴───┴───┘ └───┴───┴───┘ └───┴───┴───┘
   
   Primero uno en cada orbital, luego se aparean
```

---

## 📖 ¿Por qué Funciona Así?

### 💡 Razón física:

Los electrones con **spines paralelos** (↑↑↑) se repelen menos que los electrones apareados (↑↓) porque:

1. Los electrones son cargas negativas que se repelen
2. Cuando están en orbitales separados, están más lejos
3. Spines paralelos hacen que se "eviten" mejor (regla cuántica)
4. Esto resulta en **menor energía** = más estable

### 💡 Máxima multiplicidad de spin:

La configuración más estable es aquella con el **mayor número de electrones desapareados** (spines paralelos).

---

## 📖 Ejemplos Completos

### ⚙️ Ejemplo 1: Carbono (C, Z = 6)

```
    1s      2s          2p
   ┌───┐   ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑ │ ↑ │   │  ← Aplicando Hund
   └───┘   └───┘   └───┴───┴───┘
     2       2          2
```

**Configuración:** $1s^2 \, 2s^2 \, 2p^2$

El carbono tiene **2 electrones desapareados**.

### ⚙️ Ejemplo 2: Nitrógeno (N, Z = 7)

```
    1s      2s          2p
   ┌───┐   ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑ │ ↑ │ ↑ │  ← Máxima multiplicidad
   └───┘   └───┘   └───┴───┴───┘
     2       2          3
```

**Configuración:** $1s^2 \, 2s^2 \, 2p^3$

El nitrógeno tiene **3 electrones desapareados**.

### ⚙️ Ejemplo 3: Oxígeno (O, Z = 8)

```
    1s      2s          2p
   ┌───┐   ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑↓│ ↑ │ ↑ │  ← Uno apareado, dos no
   └───┘   └───┘   └───┴───┴───┘
     2       2          4
```

**Configuración:** $1s^2 \, 2s^2 \, 2p^4$

El oxígeno tiene **2 electrones desapareados**.

### ⚙️ Ejemplo 4: Hierro (Fe, Z = 26)

```
    [Ar]    4s              3d
   (18)    ┌───┐   ┌───┬───┬───┬───┬───┐
           │ ↑↓│   │ ↑↓│ ↑ │ ↑ │ ↑ │ ↑ │
           └───┘   └───┴───┴───┴───┴───┘
             2              6
```

**Configuración:** $[Ar] \, 4s^2 \, 3d^6$

El hierro tiene **4 electrones desapareados** en 3d.

---

## 📖 Electrones Desapareados y Magnetismo

### 💡 ¿Por qué importa?

Los electrones desapareados determinan las propiedades magnéticas:

| Tipo | Electrones desapareados | Comportamiento |
|------|------------------------|----------------|
| **Diamagnético** | 0 | Repelido por imanes |
| **Paramagnético** | ≥ 1 | Atraído por imanes |

### ⚙️ Ejemplo:

- **Neón (Ne):** Todos apareados → diamagnético
- **Oxígeno (O):** 2 desapareados → paramagnético
- **Hierro (Fe):** 4 desapareados → fuertemente paramagnético

---

## 🔑 Resumen de las Tres Reglas

| Regla | Qué regula |
|-------|------------|
| **Aufbau** | Orden de llenado de subniveles |
| **Pauli** | Máximo 2 electrones por orbital |
| **Hund** | Llenar orbitales vacíos primero, spines paralelos |

### 💡 Aplicación combinada:

1. Seguir el orden de Aufbau (diagrama de flechas)
2. Máximo 2 electrones por orbital (Pauli)
3. En orbitales degenerados, uno en cada uno primero (Hund)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Dibuja el diagrama de cajas para el azufre (S, Z = 16) aplicando la Regla de Hund.

<details>
<summary>Ver solución</summary>

```
    1s      2s          2p         3s          3p
   ┌───┐   ┌───┐   ┌───┬───┬───┐  ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑↓│ ↑↓│ ↑↓│  │ ↑↓│   │ ↑↓│ ↑ │ ↑ │
   └───┘   └───┘   └───┴───┴───┘  └───┘   └───┴───┴───┘
     2       2          6           2          4
```

**Configuración:** $1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^4$

El azufre tiene **2 electrones desapareados**.

</details>

### Ejercicio 2
¿Cuál de las siguientes configuraciones de 2p³ es correcta según Hund?

a) ↑↓ | ↑ | 
b) ↑ | ↑ | ↑
c) ↑↓ | ↑↓ |

<details>
<summary>Ver solución</summary>

**b) ↑ | ↑ | ↑** es la correcta.

Según la Regla de Hund:
- Los electrones deben ocupar primero orbitales vacíos
- Deben tener spines paralelos

La opción (b) tiene un electrón en cada orbital con spines paralelos, que es la configuración de menor energía.

</details>

### Ejercicio 3
¿Cuántos electrones desapareados tiene el manganeso (Mn, Z = 25)?

<details>
<summary>Ver solución</summary>

Configuración del Mn: $[Ar] \, 4s^2 \, 3d^5$

Diagrama de 3d:
```
              3d
    ┌───┬───┬───┬───┬───┐
    │ ↑ │ ↑ │ ↑ │ ↑ │ ↑ │
    └───┴───┴───┴───┴───┘
```

El manganeso tiene **5 electrones desapareados**.

(Todos los orbitales 3d están semillenos, máxima multiplicidad)

</details>

### Ejercicio 4
¿Por qué el nitrógeno (N) es más estable que cabría esperar?

<details>
<summary>Ver solución</summary>

El nitrógeno tiene configuración: $1s^2 \, 2s^2 \, 2p^3$

```
          2p
    ┌───┬───┬───┐
    │ ↑ │ ↑ │ ↑ │   ← Subnivel semilleno
    └───┴───┴───┘
```

El subnivel 2p está **exactamente semilleno** (3 de 6 electrones).

- Cada orbital tiene exactamente 1 electrón
- Todos los spines son paralelos
- Esta configuración simétrica es **especialmente estable**

Por eso el nitrógeno tiene alta energía de ionización y baja reactividad comparada con O o C.

</details>

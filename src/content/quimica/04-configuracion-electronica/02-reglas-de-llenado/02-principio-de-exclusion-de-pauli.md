# Principio de Exclusión de Pauli

¿Por qué cada orbital solo puede tener 2 electrones? La respuesta está en el **Principio de Exclusión de Pauli**, una ley fundamental de la mecánica cuántica que establece límites estrictos a cómo los electrones pueden ocupar los orbitales.

---

## 🎯 ¿Qué vas a aprender?

- El Principio de Exclusión de Pauli
- El concepto de spin del electrón
- Por qué máximo 2 electrones por orbital
- Cómo afecta a la configuración electrónica

---

## 📊 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Principio de Pauli** | No hay dos electrones con todos sus números cuánticos iguales |
| **Consecuencia** | Máximo 2 electrones por orbital |
| **Spin** | Deben tener spines opuestos (↑↓) |

---

## 📖 El Principio de Exclusión de Pauli

> **"No pueden existir dos electrones en un átomo que tengan los cuatro números cuánticos iguales."**

### 💡 ¿Qué son los números cuánticos?

Cada electrón se describe con 4 números cuánticos:

| Número | Símbolo | Describe |
|--------|---------|----------|
| Principal | n | Nivel de energía (1, 2, 3...) |
| Angular | ℓ | Subnivel (0=s, 1=p, 2=d, 3=f) |
| Magnético | mℓ | Orbital específico |
| Spin | ms | Dirección del spin (+½ o -½) |

### 💡 ¿Por qué máximo 2 electrones por orbital?

Si dos electrones están en el mismo orbital:
- Tienen el mismo n
- Tienen el mismo ℓ
- Tienen el mismo mℓ

Para que sean diferentes, **deben tener diferente ms (spin)**:
- Un electrón: ms = +½ (↑)
- Otro electrón: ms = -½ (↓)

No puede haber un tercer electrón porque ya no hay valores de spin disponibles.

---

## 📖 El Spin del Electrón

> El **spin** es una propiedad intrínseca del electrón, como si "girara" sobre su propio eje.

### 💡 Solo hay dos valores posibles:

| Spin | Símbolo | Representación |
|------|---------|----------------|
| +½ | ms = +½ | ↑ (flecha arriba) |
| -½ | ms = -½ | ↓ (flecha abajo) |

### 💡 Analogía:

Imagina una moneda que solo puede caer en "cara" o "cruz". El electrón solo puede tener spin "arriba" o "abajo".

---

## 📖 Aplicación en Diagramas de Cajas

### 💡 Orbital vacío:
```
    ┌───┐
    │   │
    └───┘
```

### 💡 Orbital con 1 electrón:
```
    ┌───┐
    │ ↑ │   (electrón con spin +½)
    └───┘
```

### 💡 Orbital con 2 electrones:
```
    ┌───┐
    │↑↓ │   (electrones con spines opuestos)
    └───┘
```

### ❌ Configuración prohibida:
```
    ┌───┐
    │↑↑ │   ¡IMPOSIBLE! (viola Pauli)
    └───┘
```

### ❌ Más de 2 electrones:
```
    ┌───┐
    │↑↓↑│   ¡IMPOSIBLE! (viola Pauli)
    └───┘
```

---

## 📖 Ejemplos Aplicados

### ⚙️ Ejemplo 1: Helio (He, Z = 2)

Los 2 electrones van en el orbital 1s:

```
    1s
   ┌───┐
   │ ↑↓│   ← Ambos en 1s, spines opuestos
   └───┘
```

**Configuración:** $1s^2$ ✓

### ⚙️ Ejemplo 2: Litio (Li, Z = 3)

El tercer electrón NO puede ir en 1s (ya está lleno):

```
    1s      2s
   ┌───┐   ┌───┐
   │ ↑↓│   │ ↑ │   ← El 3er electrón va a 2s
   └───┘   └───┘
```

**Configuración:** $1s^2 \, 2s^1$ ✓

### ⚙️ Ejemplo 3: ¿Por qué el neón tiene 10 electrones así?

```
    1s      2s          2p
   ┌───┐   ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑↓│ ↑↓│ ↑↓│
   └───┘   └───┘   └───┴───┴───┘
     2       2          6
```

- 1s: 2 electrones (1 orbital × 2)
- 2s: 2 electrones (1 orbital × 2)
- 2p: 6 electrones (3 orbitales × 2)
- Total: 10 ✓

---

## 📖 Importancia del Principio de Pauli

### 💡 ¿Por qué es tan importante?

1. **Define la estructura electrónica:** Determina cuántos electrones caben en cada subnivel
2. **Explica la tabla periódica:** Los períodos terminan cuando se llenan los subniveles
3. **Explica las propiedades químicas:** La configuración electrónica determina la reactividad
4. **Explica la materia sólida:** Sin Pauli, toda la materia colapsaría

### 💡 Sin el principio de Pauli:

- Todos los electrones irían al orbital más bajo (1s)
- No habría química
- No habría diversidad de elementos
- ¡No existiríamos!

---

## 📖 Relación con los Otros Principios

| Principio | Regula |
|-----------|--------|
| **Aufbau** | Orden de llenado de subniveles |
| **Pauli** | Máximo 2 electrones por orbital |
| **Hund** | Cómo llenar orbitales degenerados |

Los tres principios trabajan juntos para determinar la configuración electrónica correcta.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Principio de Pauli** | No hay 2 electrones con los 4 números cuánticos iguales |
| **Spin** | Propiedad del electrón: +½ (↑) o -½ (↓) |
| **Límite por orbital** | Máximo 2 electrones con spines opuestos |
| **Representación** | ↑↓ en diagramas de cajas |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Por qué el subnivel 2p puede tener máximo 6 electrones?

<details>
<summary>Ver solución</summary>

El subnivel 2p tiene **3 orbitales** (px, py, pz).

Por el Principio de Pauli, cada orbital puede tener máximo 2 electrones.

Total: 3 orbitales × 2 electrones = **6 electrones**

```
              2p
    ┌───┬───┬───┐
    │ ↑↓│ ↑↓│ ↑↓│ = 6 electrones máximo
    └───┴───┴───┘
     px  py  pz
```

</details>

### Ejercicio 2
¿Cuál de las siguientes configuraciones viola el Principio de Pauli?

a) 1s² 2s² 2p⁶
b) 1s² 2s³
c) 1s² 2s² 2p⁵

<details>
<summary>Ver solución</summary>

**b) 1s² 2s³ viola el Principio de Pauli**

El subnivel 2s solo tiene 1 orbital, así que puede tener máximo 2 electrones.

- a) ✓ Válida
- b) ✗ Inválida (2s³ es imposible)
- c) ✓ Válida

</details>

### Ejercicio 3
¿Por qué dos electrones en el mismo orbital no pueden tener el mismo spin?

<details>
<summary>Ver solución</summary>

Si dos electrones en el mismo orbital tuvieran el mismo spin, tendrían los **4 números cuánticos iguales**:

| Número cuántico | Electrón 1 | Electrón 2 |
|-----------------|------------|------------|
| n | igual | igual |
| ℓ | igual | igual |
| mℓ | igual | igual |
| ms | igual | igual |

Esto viola el **Principio de Exclusión de Pauli**, que prohíbe que dos electrones tengan los 4 números cuánticos idénticos.

Al tener spines opuestos (+½ y -½), los electrones se diferencian en ms.

</details>

### Ejercicio 4
Dibuja el diagrama de cajas para el berilio (Be, Z = 4) respetando el Principio de Pauli.

<details>
<summary>Ver solución</summary>

El berilio tiene 4 electrones:

```
    1s      2s
   ┌───┐   ┌───┐
   │ ↑↓│   │ ↑↓│
   └───┘   └───┘
```

- 1s: 2 electrones con spines opuestos ✓
- 2s: 2 electrones con spines opuestos ✓
- Total: 4 electrones ✓

**Configuración:** $1s^2 \, 2s^2$

</details>

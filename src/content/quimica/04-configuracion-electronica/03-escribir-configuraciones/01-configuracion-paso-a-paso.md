# Configuración Electrónica Paso a Paso

Ya conoces las tres reglas (Aufbau, Pauli, Hund). Ahora vamos a escribir configuraciones electrónicas completas para diversos elementos, desde el hidrógeno hasta metales de transición como el hierro.

---

## 🎯 ¿Qué vas a aprender?

- El procedimiento sistemático para escribir configuraciones
- Ejemplos resueltos paso a paso
- Cómo verificar que la configuración es correcta
- Casos especiales y excepciones

---

## 📊 Las Tres Reglas Juntas

| Regla | Aplicación |
|-------|------------|
| **Aufbau** | Seguir el orden: 1s → 2s → 2p → 3s → 3p → 4s → 3d... |
| **Pauli** | Máximo 2 electrones por orbital |
| **Hund** | En orbitales degenerados, uno en cada uno primero |

---

## 📖 Procedimiento Paso a Paso

### 💡 Los 4 pasos:

1. **Determinar Z:** Busca el número atómico del elemento
2. **Seguir Aufbau:** Usa el diagrama de flechas para el orden
3. **Distribuir electrones:** Máximo según cada subnivel
4. **Verificar:** Suma de exponentes = Z

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Hidrógeno (H, Z = 1)

**Paso 1:** Z = 1 → 1 electrón

**Paso 2-3:** El primer subnivel es 1s (capacidad 2)
- Solo necesitamos 1 electrón

**Configuración:**
$$
1s^1
$$

**Verificación:** 1 = 1 ✓

---

### ⚙️ Ejemplo 2: Helio (He, Z = 2)

**Paso 1:** Z = 2 → 2 electrones

**Paso 2-3:** 1s puede contener 2 electrones
- Colocamos ambos

**Configuración:**
$$
1s^2
$$

**Verificación:** 2 = 2 ✓

---

### ⚙️ Ejemplo 3: Carbono (C, Z = 6)

**Paso 1:** Z = 6 → 6 electrones

**Paso 2-3:** Seguir orden de llenado

| Subnivel | Máximo | Usamos | Acumulado |
|----------|--------|--------|-----------|
| 1s | 2 | 2 | 2 |
| 2s | 2 | 2 | 4 |
| 2p | 6 | 2 | 6 ✓ |

**Configuración:**
$$
1s^2 \, 2s^2 \, 2p^2
$$

**Diagrama de cajas:**
```
    1s      2s          2p
   ┌───┐   ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑ │ ↑ │   │  (Regla de Hund)
   └───┘   └───┘   └───┴───┴───┘
```

**Verificación:** 2 + 2 + 2 = 6 ✓

---

### ⚙️ Ejemplo 4: Oxígeno (O, Z = 8)

**Paso 1:** Z = 8 → 8 electrones

**Paso 2-3:**

| Subnivel | Máximo | Usamos | Acumulado |
|----------|--------|--------|-----------|
| 1s | 2 | 2 | 2 |
| 2s | 2 | 2 | 4 |
| 2p | 6 | 4 | 8 ✓ |

**Configuración:**
$$
1s^2 \, 2s^2 \, 2p^4
$$

**Diagrama de cajas:**
```
    1s      2s          2p
   ┌───┐   ┌───┐   ┌───┬───┬───┐
   │ ↑↓│   │ ↑↓│   │ ↑↓│ ↑ │ ↑ │  (Hund: 3 solos, luego aparear)
   └───┘   └───┘   └───┴───┴───┘
```

**Verificación:** 2 + 2 + 4 = 8 ✓

---

### ⚙️ Ejemplo 5: Cloro (Cl, Z = 17)

**Paso 1:** Z = 17 → 17 electrones

**Paso 2-3:**

| Subnivel | Usamos | Acumulado |
|----------|--------|-----------|
| 1s | 2 | 2 |
| 2s | 2 | 4 |
| 2p | 6 | 10 |
| 3s | 2 | 12 |
| 3p | 5 | 17 ✓ |

**Configuración:**
$$
1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^5
$$

**Verificación:** 2 + 2 + 6 + 2 + 5 = 17 ✓

---

### ⚙️ Ejemplo 6: Calcio (Ca, Z = 20)

**Paso 1:** Z = 20 → 20 electrones

**Paso 2-3:**

| Subnivel | Usamos | Acumulado |
|----------|--------|-----------|
| 1s | 2 | 2 |
| 2s | 2 | 4 |
| 2p | 6 | 10 |
| 3s | 2 | 12 |
| 3p | 6 | 18 |
| 4s | 2 | 20 ✓ |

**Configuración:**
$$
1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6 \, 4s^2
$$

**Nota:** El 4s se llena antes que el 3d (Regla de Aufbau).

**Verificación:** 2 + 2 + 6 + 2 + 6 + 2 = 20 ✓

---

### ⚙️ Ejemplo 7: Hierro (Fe, Z = 26)

**Paso 1:** Z = 26 → 26 electrones

**Paso 2-3:**

| Subnivel | Usamos | Acumulado |
|----------|--------|-----------|
| 1s | 2 | 2 |
| 2s | 2 | 4 |
| 2p | 6 | 10 |
| 3s | 2 | 12 |
| 3p | 6 | 18 |
| 4s | 2 | 20 |
| 3d | 6 | 26 ✓ |

**Configuración:**
$$
1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6 \, 4s^2 \, 3d^6
$$

**Diagrama de cajas para 3d:**
```
              3d
    ┌───┬───┬───┬───┬───┐
    │ ↑↓│ ↑ │ ↑ │ ↑ │ ↑ │  (4 desapareados)
    └───┴───┴───┴───┴───┘
```

**Verificación:** 2+2+6+2+6+2+6 = 26 ✓

---

## 📖 Excepciones Importantes

### 💡 Cromo (Cr, Z = 24)

**Esperado:** [Ar] 4s² 3d⁴
**Real:** [Ar] 4s¹ 3d⁵

¿Por qué? El subnivel 3d **semilleno** (5 electrones) es especialmente estable.

### 💡 Cobre (Cu, Z = 29)

**Esperado:** [Ar] 4s² 3d⁹
**Real:** [Ar] 4s¹ 3d¹⁰

¿Por qué? El subnivel 3d **lleno** (10 electrones) es muy estable.

### 💡 Regla para excepciones:

Los subniveles **semillenos** (d⁵, f⁷) y **llenos** (d¹⁰, f¹⁴) son especialmente estables y pueden "robar" un electrón del 4s.

---

## 📖 Tabla de Referencia

| Elemento | Z | Configuración |
|----------|---|---------------|
| H | 1 | $1s^1$ |
| He | 2 | $1s^2$ |
| Li | 3 | $1s^2 \, 2s^1$ |
| C | 6 | $1s^2 \, 2s^2 \, 2p^2$ |
| N | 7 | $1s^2 \, 2s^2 \, 2p^3$ |
| O | 8 | $1s^2 \, 2s^2 \, 2p^4$ |
| Ne | 10 | $1s^2 \, 2s^2 \, 2p^6$ |
| Na | 11 | $1s^2 \, 2s^2 \, 2p^6 \, 3s^1$ |
| Cl | 17 | $1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^5$ |
| Ar | 18 | $1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6$ |
| Ca | 20 | $[Ar] \, 4s^2$ |
| Fe | 26 | $[Ar] \, 4s^2 \, 3d^6$ |

---

## 🔑 Resumen

| Paso | Acción |
|------|--------|
| 1 | Determinar Z (número de electrones) |
| 2 | Seguir orden de Aufbau |
| 3 | Aplicar Pauli (máx 2 por orbital) y Hund (paralelos primero) |
| 4 | Verificar: suma de exponentes = Z |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la configuración electrónica del fósforo (P, Z = 15).

<details>
<summary>Ver solución</summary>

| Subnivel | Usamos | Acumulado |
|----------|--------|-----------|
| 1s | 2 | 2 |
| 2s | 2 | 4 |
| 2p | 6 | 10 |
| 3s | 2 | 12 |
| 3p | 3 | 15 ✓ |

**Configuración:** $\boxed{1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^3}$

</details>

### Ejercicio 2
Escribe la configuración electrónica del zinc (Zn, Z = 30).

<details>
<summary>Ver solución</summary>

| Subnivel | Usamos | Acumulado |
|----------|--------|-----------|
| 1s-3p | 18 | 18 (= Ar) |
| 4s | 2 | 20 |
| 3d | 10 | 30 ✓ |

**Configuración:** $\boxed{1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6 \, 4s^2 \, 3d^{10}}$

O equivalente: $[Ar] \, 4s^2 \, 3d^{10}$

</details>

### Ejercicio 3
¿Por qué el cromo tiene configuración [Ar] 4s¹ 3d⁵ en lugar de [Ar] 4s² 3d⁴?

<details>
<summary>Ver solución</summary>

El cromo tiene esa configuración porque el subnivel **3d semilleno** (exactamente 5 electrones) es especialmente estable.

Esta estabilidad extra compensa el "costo" de mover un electrón del 4s al 3d:

**[Ar] 4s² 3d⁴:** 
- 3d tiene 4 electrones → no semilleno

**[Ar] 4s¹ 3d⁵:**
- 3d tiene 5 electrones → semilleno ✓
- El 4s tiene solo 1 electrón

La configuración semillena tiene menor energía total → es más estable.

</details>

### Ejercicio 4
Escribe la configuración de un átomo con 35 electrones e identifica el elemento.

<details>
<summary>Ver solución</summary>

Z = 35 → **Bromo (Br)**

| Subnivel | Usamos | Acumulado |
|----------|--------|-----------|
| [Ar] | 18 | 18 |
| 4s | 2 | 20 |
| 3d | 10 | 30 |
| 4p | 5 | 35 ✓ |

**Configuración:** $\boxed{[Ar] \, 4s^2 \, 3d^{10} \, 4p^5}$

El bromo está en el grupo 17 (halógenos) y período 4.

</details>

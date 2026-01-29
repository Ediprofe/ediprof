# Ejercicios Resueltos de Configuración Electrónica

En esta lección aplicaremos los principios aprendidos (Aufbau, Hund, Pauli) para escribir la configuración electrónica de varios elementos.

---

## 🎯 ¿Qué vas a aprender?

- Cómo escribir configuraciones electrónicas paso a paso
- Aplicar la regla de las diagonales
- Verificar que el total de electrones sea correcto

---

## 📖 Recordatorio: Orden de Llenado

$$
1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → ...
$$

### 💡 Capacidades:

| Subnivel | Electrones máximos |
|----------|-------------------|
| s | 2 |
| p | 6 |
| d | 10 |
| f | 14 |

---

## 📖 Ejercicio 1: Hidrógeno (H)

**Número atómico (Z) = 1**

### Solución:

| Paso | Acción |
|------|--------|
| 1 | Z = 1 → tenemos 1 electrón |
| 2 | Primer subnivel: 1s |
| 3 | Colocamos 1 electrón en 1s |

**Configuración:**
$$
\boxed{1s^1}
$$

---

## 📖 Ejercicio 2: Oxígeno (O)

**Número atómico (Z) = 8**

### Solución:

| Paso | Subnivel | Electrones | Acumulado |
|------|----------|------------|-----------|
| 1 | 1s | 2 | 2 |
| 2 | 2s | 2 | 4 |
| 3 | 2p | 4 | 8 ✓ |

**Configuración:**
$$
\boxed{1s^2 \, 2s^2 \, 2p^4}
$$

### 💡 Diagrama de cajas para 2p:

```
[↑↓] [↑] [↑]  ← 4 electrones en 2p
```

El oxígeno tiene **2 electrones desapareados**.

---

## 📖 Ejercicio 3: Aluminio (Al)

**Número atómico (Z) = 13**

### Solución:

| Paso | Subnivel | Electrones | Acumulado |
|------|----------|------------|-----------|
| 1 | 1s | 2 | 2 |
| 2 | 2s | 2 | 4 |
| 3 | 2p | 6 | 10 |
| 4 | 3s | 2 | 12 |
| 5 | 3p | 1 | 13 ✓ |

**Configuración:**
$$
\boxed{1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^1}
$$

---

## 📖 Ejercicio 4: Azufre (S)

**Número atómico (Z) = 16**

### Solución:

| Paso | Subnivel | Electrones | Acumulado |
|------|----------|------------|-----------|
| 1 | 1s | 2 | 2 |
| 2 | 2s | 2 | 4 |
| 3 | 2p | 6 | 10 |
| 4 | 3s | 2 | 12 |
| 5 | 3p | 4 | 16 ✓ |

**Configuración:**
$$
\boxed{1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^4}
$$

---

## 📖 Ejercicio 5: Hierro (Fe)

**Número atómico (Z) = 26**

### Solución:

| Paso | Subnivel | Electrones | Acumulado |
|------|----------|------------|-----------|
| 1 | 1s | 2 | 2 |
| 2 | 2s | 2 | 4 |
| 3 | 2p | 6 | 10 |
| 4 | 3s | 2 | 12 |
| 5 | 3p | 6 | 18 |
| 6 | 4s | 2 | 20 |
| 7 | 3d | 6 | 26 ✓ |

**Configuración:**
$$
\boxed{1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6 \, 4s^2 \, 3d^6}
$$

> Nota: El 4s se llena antes que el 3d, pero al escribir la configuración se ordena por nivel.

---

## 🔑 Resumen del Método

1. Identificar Z (número de electrones)
2. Seguir el orden de las diagonales
3. Llenar cada subnivel hasta su capacidad
4. Parar cuando el total = Z
5. Verificar la suma

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la configuración electrónica del carbono (C, Z=6).

<details>
<summary>Ver solución</summary>

$$
1s^2 \, 2s^2 \, 2p^2
$$

Comprobación: 2 + 2 + 2 = 6 ✓

</details>

### Ejercicio 2
Escribe la configuración electrónica del calcio (Ca, Z=20).

<details>
<summary>Ver solución</summary>

$$
1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6 \, 4s^2
$$

Comprobación: 2+2+6+2+6+2 = 20 ✓

</details>

### Ejercicio 3
Escribe la configuración electrónica del cobre (Cu, Z=29).

<details>
<summary>Ver solución</summary>

El cobre es una **excepción**:

$$
1s^2 \, 2s^2 \, 2p^6 \, 3s^2 \, 3p^6 \, 4s^1 \, 3d^{10}
$$

En lugar de 4s² 3d⁹, tiene 4s¹ 3d¹⁰ porque el subnivel d completo es más estable.

</details>

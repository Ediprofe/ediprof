---
title: "Ecuación de Estado del Gas Ideal"
---

# Ecuación de Estado del Gas Ideal

La **ecuación del gas ideal** (PV = nRT) es la ecuación más importante para describir el comportamiento de los gases. Relaciona las cuatro variables de estado en una sola expresión.

---

## 🎯 ¿Qué vas a aprender?

- La ecuación PV = nRT
- El significado y valores de la constante R
- Cómo resolver problemas con la ecuación
- Cuándo un gas se comporta idealmente

---

## 📊 La Ecuación

$$
\boxed{PV = nRT}
$$

| Variable | Significado | Unidades típicas |
|----------|-------------|------------------|
| P | Presión | atm, kPa, Pa |
| V | Volumen | L, m³ |
| n | Moles | mol |
| R | Constante | Depende de unidades |
| T | Temperatura | **K (siempre)** |

---

## 📖 La Constante R

### 💡 Valores según unidades:

| Valor de R | Unidades | Cuándo usar |
|------------|----------|-------------|
| **0.0821** | L·atm/(mol·K) | P en atm, V en L |
| 8.314 | J/(mol·K) | Unidades SI |
| 8.314 | kPa·L/(mol·K) | P en kPa, V en L |
| 62.36 | L·mmHg/(mol·K) | P en mmHg, V en L |

### 💡 El más usado:

$$
R = 0.0821 \frac{\text{L} \cdot \text{atm}}{\text{mol} \cdot \text{K}}
$$

---

## 📖 ¿Qué es un Gas Ideal?

Un **gas ideal** es un modelo teórico donde:

1. Las moléculas no tienen volumen propio
2. No hay fuerzas intermoleculares
3. Los choques son perfectamente elásticos

### 💡 ¿Cuándo un gas real se aproxima al ideal?

| Condición | Comportamiento ideal |
|-----------|---------------------|
| Alta temperatura | Sí ✓ |
| Baja presión | Sí ✓ |
| Baja temperatura | No ✗ |
| Alta presión | No ✗ |

---

## 📖 Formas Despejadas

### 💡 Para encontrar cada variable:

| Encontrar | Fórmula |
|-----------|---------|
| P | P = nRT/V |
| V | V = nRT/P |
| n | n = PV/RT |
| T | T = PV/nR |

---

## 📖 Ejemplo 1: Encontrar el Volumen

### Problema:
¿Qué volumen ocupa 2 mol de gas a 27°C y 1 atm?

### Solución:

**Datos:**
- n = 2 mol
- T = 27 + 273 = 300 K
- P = 1 atm
- R = 0.0821 L·atm/(mol·K)

**Cálculo:**
$$
V = \frac{nRT}{P} = \frac{2 \times 0.0821 \times 300}{1} = \boxed{49.3 \text{ L}}
$$

---

## 📖 Ejemplo 2: Encontrar la Presión

### Problema:
3 mol de O₂ ocupan 20 L a 127°C. ¿Cuál es la presión?

### Solución:

**Datos:**
- n = 3 mol, V = 20 L
- T = 127 + 273 = 400 K

**Cálculo:**
$$
P = \frac{nRT}{V} = \frac{3 \times 0.0821 \times 400}{20} = \boxed{4.93 \text{ atm}}
$$

---

## 📖 Ejemplo 3: Encontrar los Moles

### Problema:
Un gas a 2 atm y 300 K ocupa 12.3 L. ¿Cuántos moles hay?

### Solución:

$$
n = \frac{PV}{RT} = \frac{2 \times 12.3}{0.0821 \times 300} = \boxed{1.0 \text{ mol}}
$$

---

## 📖 Ejemplo 4: Masa Molar desde la Ecuación

### 💡 Combinando con n = m/M:

$$
PV = \frac{m}{M}RT
$$

Despejando la masa molar:

$$
M = \frac{mRT}{PV}
$$

### Ejemplo:

Si 1.60 g de gas ocupan 1 L a 27°C y 1.23 atm, ¿cuál es su masa molar?

$$
M = \frac{1.60 \times 0.0821 \times 300}{1.23 \times 1} = \boxed{32 \text{ g/mol}}
$$

Es oxígeno (O₂).

---

## 📖 Verificación de Unidades

### ⚠️ ¡Importante verificar!

$$
\frac{\text{mol} \times \frac{\text{L} \cdot \text{atm}}{\text{mol} \cdot \text{K}} \times \text{K}}{\text{atm}} = \text{L} \checkmark
$$

Las unidades deben ser **consistentes** con el valor de R que uses.

---

## 📖 Comparación con la Ley Combinada

| Ecuación | Cuándo usarla |
|----------|---------------|
| P₁V₁/T₁ = P₂V₂/T₂ | Dos estados del mismo gas |
| PV = nRT | Un estado, conociendo n |

---

## 🔑 Resumen

$$
\boxed{PV = nRT}
$$

| R | = 0.0821 L·atm/(mol·K) |
|---|------------------------|
| P | en atm |
| V | en L |
| T | en K (siempre) |
| n | en mol |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuál es el volumen de 1 mol de gas a CN (0°C, 1 atm)?

<details>
<summary>Ver solución</summary>

$$
V = \frac{1 \times 0.0821 \times 273}{1} = \boxed{22.4 \text{ L}}
$$

¡Este es el volumen molar estándar!

</details>

### Ejercicio 2
5 mol de gas a 2 atm y 300 K, ¿cuántos litros ocupan?

<details>
<summary>Ver solución</summary>

$$
V = \frac{5 \times 0.0821 \times 300}{2} = \boxed{61.6 \text{ L}}
$$

</details>

### Ejercicio 3
Un gas a 760 mmHg, 25°C ocupa 5 L. ¿Cuántos moles hay?

<details>
<summary>Ver solución</summary>

P = 760/760 = 1 atm, T = 298 K

$$
n = \frac{1 \times 5}{0.0821 \times 298} = \boxed{0.204 \text{ mol}}
$$

</details>

### Ejercicio 4
Si 4.4 g de CO₂ ocupan 2.24 L a 0°C, ¿cuál es la presión?

<details>
<summary>Ver solución</summary>

M(CO₂) = 44 g/mol → n = 4.4/44 = 0.1 mol

$$
P = \frac{0.1 \times 0.0821 \times 273}{2.24} = \boxed{1 \text{ atm}}
$$

</details>

### Ejercicio 5
¿Por qué los gases reales se desvían del comportamiento ideal a altas presiones?

<details>
<summary>Ver solución</summary>

A altas presiones:

1. Las moléculas están muy **juntas**
2. El volumen de las moléculas **ya no es despreciable**
3. Las **fuerzas intermoleculares** se hacen significativas
4. Los supuestos del gas ideal **no se cumplen**

Por eso se usan ecuaciones corregidas como la de Van der Waals:

$$
\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT
$$

Donde a y b corrigen las fuerzas intermoleculares y el volumen molecular.

</details>

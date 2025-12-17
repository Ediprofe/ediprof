# Ley de Dalton de las Presiones Parciales

La **Ley de Dalton** describe cómo se comportan las mezclas de gases. Cada gas en una mezcla ejerce su propia presión independientemente de los demás.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la presión parcial
- La Ley de Dalton de las presiones parciales
- Cómo calcular presiones en mezclas de gases
- Aplicaciones prácticas

---

## 📊 La Ley de Dalton

$$
\boxed{P_{\text{total}} = P_1 + P_2 + P_3 + \cdots}
$$

> La presión total de una mezcla de gases es igual a la **suma de las presiones parciales** de cada gas.

---

## 📖 ¿Qué es la Presión Parcial?

### 💡 Definición:

La **presión parcial** de un gas en una mezcla es la presión que ejercería ese gas si ocupara **solo él** todo el volumen a la misma temperatura.

### 💡 Visualización:

```
    Mezcla de 3 gases         Cada gas por separado
    en un recipiente          en el mismo volumen
    
    ┌─────────────────┐       ┌─────┐ ┌─────┐ ┌─────┐
    │  ●  ○  ▲  ●  ○  │       │  ●  │ │  ○  │ │  ▲  │
    │  ▲  ●  ○  ▲  ●  │  =    │  ●  │+│  ○  │+│  ▲  │
    │  ○  ▲  ●  ○  ▲  │       │  ●  │ │  ○  │ │  ▲  │
    └─────────────────┘       └─────┘ └─────┘ └─────┘
       P_total = 3 atm         P₁      P₂      P₃
                               1 atm  1.2 atm 0.8 atm
```

---

## 📖 Cálculo de Presión Parcial

### 💡 Usando la ecuación del gas ideal:

Para cada gas en la mezcla:

$$
P_i = \frac{n_i RT}{V}
$$

### 💡 Usando la fracción molar:

$$
P_i = X_i \times P_{\text{total}}
$$

Donde Xᵢ es la fracción molar (se verá en la siguiente lección).

---

## 📖 Ejemplo 1: Suma de Presiones

### Problema:
Una mezcla contiene O₂ (P = 0.2 atm), N₂ (P = 0.6 atm) y CO₂ (P = 0.1 atm). ¿Cuál es la presión total?

### Solución:

$$
P_{\text{total}} = P_{O_2} + P_{N_2} + P_{CO_2}
$$

$$
P_{\text{total}} = 0.2 + 0.6 + 0.1 = \boxed{0.9 \text{ atm}}
$$

---

## 📖 Ejemplo 2: Encontrar Presión Parcial

### Problema:
Una mezcla de gases a 2 atm contiene 3 mol de He y 1 mol de Ne. ¿Cuál es la presión parcial de cada gas?

### Solución:

**Paso 1:** Total de moles
$$
n_{\text{total}} = 3 + 1 = 4 \text{ mol}
$$

**Paso 2:** Fracción de cada gas
$$
X_{He} = \frac{3}{4} = 0.75 \quad X_{Ne} = \frac{1}{4} = 0.25
$$

**Paso 3:** Presiones parciales
$$
P_{He} = 0.75 \times 2 = \boxed{1.5 \text{ atm}}
$$

$$
P_{Ne} = 0.25 \times 2 = \boxed{0.5 \text{ atm}}
$$

---

## 📖 Ejemplo 3: Gas Recolectado sobre Agua

### 💡 Concepto importante:

Cuando se recolecta un gas sobre agua, el gas recogido está **mezclado con vapor de agua**.

$$
P_{\text{total}} = P_{\text{gas}} + P_{\text{vapor de agua}}
$$

Entonces:

$$
P_{\text{gas}} = P_{\text{total}} - P_{\text{vapor}}
$$

### Problema:
Se recolecta O₂ sobre agua a 25°C. La presión atmosférica es 760 mmHg y la presión de vapor del agua a 25°C es 24 mmHg. ¿Cuál es la presión del O₂ puro?

### Solución:

$$
P_{O_2} = 760 - 24 = \boxed{736 \text{ mmHg}}
$$

---

## 📖 Tabla de Presión de Vapor del Agua

| Temperatura (°C) | P vapor (mmHg) |
|------------------|----------------|
| 0 | 4.6 |
| 10 | 9.2 |
| 20 | 17.5 |
| 25 | 23.8 |
| 30 | 31.8 |
| 40 | 55.3 |
| 50 | 92.5 |
| 100 | 760.0 |

---

## 📖 Aplicaciones

### 💡 Composición del aire:

| Gas | % Volumen | P parcial (1 atm) |
|-----|-----------|-------------------|
| N₂ | 78.1% | 0.781 atm |
| O₂ | 20.9% | 0.209 atm |
| Ar | 0.9% | 0.009 atm |
| CO₂ | 0.04% | 0.0004 atm |

### 💡 Buceo:

A grandes profundidades, la P parcial de O₂ puede ser tóxica. Los buceadores usan mezclas especiales (nitrox, trimix).

### 💡 Respiración:

El intercambio de O₂ y CO₂ en los pulmones depende de las diferencias de presiones parciales.

---

## 🔑 Resumen

$$
P_{\text{total}} = \sum P_i = P_1 + P_2 + P_3 + \cdots
$$

$$
P_i = X_i \times P_{\text{total}} = \frac{n_i}{n_{\text{total}}} \times P_{\text{total}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Una mezcla tiene P(He) = 400 mmHg y P(Ar) = 300 mmHg. ¿Cuál es P total?

<details>
<summary>Ver solución</summary>

$$
P_{\text{total}} = 400 + 300 = \boxed{700 \text{ mmHg}}
$$

</details>

### Ejercicio 2
A P = 760 mmHg, el aire tiene 21% O₂. ¿Cuál es P(O₂)?

<details>
<summary>Ver solución</summary>

$$
P_{O_2} = 0.21 \times 760 = \boxed{159.6 \text{ mmHg}}
$$

</details>

### Ejercicio 3
Se recolecta H₂ sobre agua a 20°C (P_vapor = 17.5 mmHg). Si P_total = 750 mmHg, ¿cuál es P(H₂)?

<details>
<summary>Ver solución</summary>

$$
P_{H_2} = 750 - 17.5 = \boxed{732.5 \text{ mmHg}}
$$

</details>

### Ejercicio 4
Una mezcla de 2 mol de N₂ y 3 mol de O₂ tiene P_total = 5 atm. ¿Cuáles son las presiones parciales?

<details>
<summary>Ver solución</summary>

$$
X_{N_2} = \frac{2}{5} = 0.4 \quad X_{O_2} = \frac{3}{5} = 0.6
$$

$$
P_{N_2} = 0.4 \times 5 = \boxed{2 \text{ atm}}
$$

$$
P_{O_2} = 0.6 \times 5 = \boxed{3 \text{ atm}}
$$

</details>

### Ejercicio 5
¿Por qué la presión parcial de O₂ disminuye en la cima del Everest?

<details>
<summary>Ver solución</summary>

La P total atmosférica en el Everest es ≈ 0.3 atm (vs 1 atm a nivel del mar).

Aunque el **porcentaje** de O₂ sigue siendo ~21%, la **presión parcial** disminuye:

- A nivel del mar: P(O₂) = 0.21 × 1 = 0.21 atm
- En el Everest: P(O₂) = 0.21 × 0.3 = 0.063 atm

Con solo 1/3 de la presión de O₂, el cuerpo no puede absorber suficiente oxígeno. Por eso los escaladores necesitan oxígeno suplementario.

</details>

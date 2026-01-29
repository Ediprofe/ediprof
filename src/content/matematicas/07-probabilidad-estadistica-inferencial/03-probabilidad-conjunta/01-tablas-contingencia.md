# Probabilidad Conjunta y Tablas de Contingencia

Cuando analizamos **dos eventos** o **dos variables** juntos, necesitamos organizar las probabilidades de forma sistemática. Las **tablas de contingencia** son la herramienta perfecta para esto.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las probabilidades conjuntas
- Probabilidades marginales y condicionales en tablas
- Cómo construir e interpretar tablas de contingencia
- Relación entre las tres tipos de probabilidades

---

## 📖 Tipos de Probabilidades en Tablas

| Tipo | Símbolo | Descripción |
|------|---------|-------------|
| **Conjunta** | $P(A \cap B)$ | Probabilidad de ambos eventos |
| **Marginal** | $P(A)$ o $P(B)$ | Probabilidad de un solo evento (suma de una fila/columna) |
| **Condicional** | $P(B|A)$ | Probabilidad de B dado A |

---

## 📖 Ejemplo: Encuesta sobre Género y Preferencia

En una encuesta a 200 personas sobre su bebida favorita:

|  | Café | Té | Jugo | **Total** |
|--|------|-----|------|-----------|
| **Hombre** | 50 | 30 | 20 | **100** |
| **Mujer** | 40 | 35 | 25 | **100** |
| **Total** | **90** | **65** | **45** | **200** |

---

## 📖 Probabilidades Conjuntas

> La **probabilidad conjunta** es la probabilidad de que ocurran ambos eventos simultáneamente.

### 💡 Cálculo:

$$
P(A \cap B) = \frac{\text{frecuencia de ambos}}{\text{total}}
$$

### ⚙️ Ejemplos:

$$
P(\text{Hombre} \cap \text{Café}) = \frac{50}{200} = 0.25
$$

$$
P(\text{Mujer} \cap \text{Té}) = \frac{35}{200} = 0.175
$$

### 💡 Tabla de probabilidades conjuntas:

|  | Café | Té | Jugo | **Total** |
|--|------|-----|------|-----------|
| **Hombre** | 0.25 | 0.15 | 0.10 | **0.50** |
| **Mujer** | 0.20 | 0.175 | 0.125 | **0.50** |
| **Total** | **0.45** | **0.325** | **0.225** | **1.00** |

---

## 📖 Probabilidades Marginales

> La **probabilidad marginal** es la probabilidad de un solo evento, sin considerar el otro.

### 💡 Ubicación:

Están en los **márgenes** de la tabla (totales de filas y columnas).

### ⚙️ Ejemplos:

$$
P(\text{Hombre}) = \frac{100}{200} = 0.50
$$

$$
P(\text{Café}) = \frac{90}{200} = 0.45
$$

### 💡 Relación con conjuntas:

$$
P(A) = \sum_{\text{todos los } B} P(A \cap B)
$$

$$
P(\text{Hombre}) = P(H \cap C) + P(H \cap T) + P(H \cap J) = 0.25 + 0.15 + 0.10 = 0.50
$$

---

## 📖 Probabilidades Condicionales en Tablas

### 💡 Fórmula:

$$
P(B|A) = \frac{P(A \cap B)}{P(A)}
$$

### ⚙️ Ejemplo 1: P(Café | Hombre)

"Dado que es hombre, ¿cuál es la probabilidad de que prefiera café?"

$$
P(\text{Café} | \text{Hombre}) = \frac{P(\text{H} \cap \text{C})}{P(\text{H})} = \frac{0.25}{0.50} = 0.50
$$

O directamente de la tabla: $\frac{50}{100} = 0.50$

### ⚙️ Ejemplo 2: P(Mujer | Té)

"Dado que prefiere té, ¿cuál es la probabilidad de que sea mujer?"

$$
P(\text{Mujer} | \text{Té}) = \frac{P(\text{M} \cap \text{T})}{P(\text{T})} = \frac{0.175}{0.325} = 0.538
$$

O directamente: $\frac{35}{65} \approx 0.538$

---

## 📖 Independencia en Tablas de Contingencia

### 💡 Dos variables son independientes si:

$$
P(A \cap B) = P(A) \cdot P(B) \text{ para todas las combinaciones}
$$

### ⚙️ Verificación:

¿Son "Género" y "Bebida" independientes?

Si fueran independientes:
$$
P(\text{H} \cap \text{C}) = P(\text{H}) \cdot P(\text{C}) = 0.50 \times 0.45 = 0.225
$$

Pero el valor real es:
$$
P(\text{H} \cap \text{C}) = 0.25
$$

Como $0.25 \neq 0.225$, las variables **no son independientes**.

Los hombres prefieren café más de lo esperado si fueran independientes.

---

## 📖 Otro Ejemplo: Datos Médicos

Resultados de una prueba diagnóstica en 1000 personas:

|  | Enfermo | Sano | **Total** |
|--|---------|------|-----------|
| **Positivo** | 45 | 95 | **140** |
| **Negativo** | 5 | 855 | **860** |
| **Total** | **50** | **950** | **1000** |

### 💡 Probabilidades clave:

**Conjuntas:**
- P(Enfermo ∩ Positivo) = 45/1000 = 0.045
- P(Sano ∩ Positivo) = 95/1000 = 0.095 (falsos positivos)

**Marginales:**
- P(Enfermo) = 50/1000 = 0.05 (prevalencia)
- P(Positivo) = 140/1000 = 0.14

**Condicionales (características de la prueba):**
- P(Positivo | Enfermo) = 45/50 = 0.90 (sensibilidad)
- P(Negativo | Sano) = 855/950 = 0.90 (especificidad)

**Condicionales (utilidad clínica):**
- P(Enfermo | Positivo) = 45/140 = 0.32 (valor predictivo positivo)
- P(Sano | Negativo) = 855/860 = 0.99 (valor predictivo negativo)

---

## 🔑 Resumen

| Tipo | Ubicación en tabla | Fórmula |
|------|-------------------|---------|
| **Conjunta** | Celdas interiores | $\frac{\text{celda}}{\text{total}}$ |
| **Marginal** | Totales (márgenes) | Suma de fila o columna |
| **Condicional** | Calculada | $\frac{\text{conjunta}}{\text{marginal}}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Usa la tabla del ejemplo de bebidas:

|  | Café | Té | Jugo | Total |
|--|------|-----|------|-------|
| Hombre | 50 | 30 | 20 | 100 |
| Mujer | 40 | 35 | 25 | 100 |
| Total | 90 | 65 | 45 | 200 |

Calcula:
a) P(Mujer ∩ Jugo)
b) P(Té)
c) P(Hombre | Té)

<details>
<summary>Ver solución</summary>

a) P(Mujer ∩ Jugo) = 25/200 = 0.125

b) P(Té) = 65/200 = 0.325

c) P(Hombre | Té) = (Hombres que prefieren té) / (Total té) = 30/65 ≈ 0.462

</details>

### Ejercicio 2
En una universidad, 300 estudiantes fueron clasificados:

|  | Aprobó | Reprobó | Total |
|--|--------|---------|-------|
| Asistió a clases | 180 | 20 | 200 |
| No asistió | 50 | 50 | 100 |
| Total | 230 | 70 | 300 |

a) ¿Cuál es la probabilidad de aprobar si asistió?
b) ¿Cuál es la probabilidad de aprobar si no asistió?
c) ¿Son "asistencia" y "aprobar" independientes?

<details>
<summary>Ver solución</summary>

a) P(Aprobar | Asistió) = 180/200 = 0.90 = 90%

b) P(Aprobar | No asistió) = 50/100 = 0.50 = 50%

c) No son independientes porque P(Aprobar | Asistió) ≠ P(Aprobar)
   - P(Aprobar) = 230/300 = 0.767
   - P(Aprobar | Asistió) = 0.90 ≠ 0.767

La asistencia aumenta significativamente la probabilidad de aprobar.

</details>

### Ejercicio 3
¿Por qué se llaman "marginales" las probabilidades P(A) y P(B)?

<details>
<summary>Ver solución</summary>

Se llaman **marginales** porque aparecen en los **márgenes** (bordes) de la tabla de contingencia:

- Los totales de las filas están en el margen derecho
- Los totales de las columnas están en el margen inferior

Matemáticamente, son las **sumas** de las probabilidades conjuntas a lo largo de una dimensión, "marginalizando" (eliminando) la otra variable.

</details>

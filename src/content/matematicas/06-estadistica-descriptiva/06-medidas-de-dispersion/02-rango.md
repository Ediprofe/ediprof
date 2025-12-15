# El Rango

La medida de dispersión más simple es el **rango**: solo necesitas el valor más grande y el más pequeño. Es rápido, intuitivo, pero tiene sus limitaciones.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el rango y cómo calcularlo
- Sus ventajas y limitaciones
- Cuándo es útil y cuándo no

---

## 📖 Definición del Rango

> El **rango** es la diferencia entre el valor máximo y el valor mínimo de un conjunto de datos.

### 💡 Fórmula:

$$
R = X_{máx} - X_{mín}
$$

### ⚙️ Ejemplo 1: Notas de un examen

Notas: 5, 6, 7, 7, 8, 8, 9, 9, 10

- $X_{máx} = 10$
- $X_{mín} = 5$
- $R = 10 - 5 = 5$

**El rango es 5 puntos.**

### ⚙️ Ejemplo 2: Estaturas

Estaturas (cm): 155, 162, 168, 170, 175, 180, 185

- $X_{máx} = 185$ cm
- $X_{mín} = 155$ cm
- $R = 185 - 155 = 30$ cm

**El rango es 30 cm.**

---

## 📖 Interpretación del Rango

El rango nos dice cuánto **"espacio"** ocupan los datos en la escala de medición.

### ⚙️ Ejemplo comparativo

**Curso A:** Notas de 6, 7, 7, 8, 8, 9 → R = 9 - 6 = 3
**Curso B:** Notas de 3, 5, 7, 9, 11 → R = 11 - 3 = 8

| Curso | Rango | Interpretación |
|-------|-------|----------------|
| A | 3 | Notas más homogéneas |
| B | 8 | Notas más dispersas |

---

## 💡 Ventajas del Rango

| Ventaja | Descripción |
|---------|-------------|
| **Simplicidad** | Solo necesitas máximo y mínimo |
| **Rapidez** | Se calcula en segundos |
| **Intuitivo** | Fácil de entender y comunicar |
| **Primera aproximación** | Útil para una idea rápida de dispersión |

---

## ⚠️ Limitaciones del Rango

### Limitación 1: Solo usa dos valores

El rango **ignora** todos los valores intermedios.

### ⚙️ Ejemplo:

**Grupo A:** 0, 50, 50, 50, 50, 50, 100
**Grupo B:** 0, 10, 30, 50, 70, 90, 100

Ambos tienen $R = 100 - 0 = 100$, pero:
- Grupo A tiene la mayoría en 50 (menos disperso realmente)
- Grupo B tiene valores distribuidos (más disperso)

El rango no distingue esta diferencia.

### Limitación 2: Muy sensible a valores extremos

Un solo **outlier** puede alterar drásticamente el rango.

### ⚙️ Ejemplo:

**Datos originales:** 10, 12, 14, 16, 18 → R = 8
**Con outlier:** 10, 12, 14, 16, **100** → R = 90

¡El rango pasó de 8 a 90 por un solo valor!

### Limitación 3: No indica distribución interna

El rango no dice nada sobre cómo están distribuidos los datos dentro del intervalo.

---

## 📖 Rango para Datos Agrupados

Para datos en tablas de frecuencias:

$$
R = L_s^{última} - L_i^{primera}
$$

### ⚙️ Ejemplo:

| Intervalo | f |
|-----------|---|
| 10 - 19 | 5 |
| 20 - 29 | 12 |
| 30 - 39 | 18 |
| 40 - 49 | 10 |
| 50 - 59 | 5 |

$$
R = 59 - 10 = 49
$$

O usando límites reales: $R = 59.5 - 9.5 = 50$

---

## 📖 Cuándo Usar el Rango

| Situación | ¿Usar rango? | Razón |
|-----------|--------------|-------|
| Vista rápida inicial | ✅ Sí | Fácil y rápido |
| Datos sin outliers | ✅ Sí | Representativo |
| Análisis riguroso | ⚠️ Complementar | Usar junto con otras medidas |
| Hay valores extremos | ❌ Evitar solo | Muy distorsionado |
| Comparar grupos | ⚠️ Con cuidado | Si tienen outliers, no es justo |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Rango** | $R = X_{máx} - X_{mín}$ |
| **Ventaja** | Simple, rápido, intuitivo |
| **Limitación** | Solo usa dos valores, sensible a extremos |
| **Uso ideal** | Primera aproximación o cuando no hay outliers |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el rango de los siguientes conjuntos:

a) 15, 22, 18, 30, 25, 12, 28
b) 3.5, 4.2, 3.8, 4.0, 5.1, 3.6
c) -5, -2, 0, 3, 7, 10

<details>
<summary>Ver solución</summary>

a) **Datos: 15, 22, 18, 30, 25, 12, 28**
$X_{máx} = 30$, $X_{mín} = 12$
$R = 30 - 12 = 18$

b) **Datos: 3.5, 4.2, 3.8, 4.0, 5.1, 3.6**
$X_{máx} = 5.1$, $X_{mín} = 3.5$
$R = 5.1 - 3.5 = 1.6$

c) **Datos: -5, -2, 0, 3, 7, 10**
$X_{máx} = 10$, $X_{mín} = -5$
$R = 10 - (-5) = 10 + 5 = 15$

</details>

### Ejercicio 2
Los tiempos (en minutos) que tardaron 8 corredores en completar una carrera fueron:
25, 28, 27, 26, 29, 27, 28, 55

a) Calcula el rango
b) ¿Hay algún valor atípico?
c) ¿El rango representa bien la dispersión del grupo?

<details>
<summary>Ver solución</summary>

a) **Rango:**
$R = 55 - 25 = 30$ minutos

b) **Valor atípico:**
Sí, el 55 es un outlier. Los demás están entre 25-29, pero uno tardó 55 minutos (quizás tuvo un problema).

c) **¿Representa bien la dispersión?**
NO. El rango de 30 minutos sugiere mucha dispersión, pero 7 de 8 corredores tienen un rango de solo 4 minutos (25-29).

El rango está inflado por el outlier (55) y no representa la dispersión real del grupo típico.

</details>

### Ejercicio 3
¿Por qué el rango de las notas 5, 5, 5, 5, 10 es el mismo que el de 5, 6, 7, 8, 9, 10?

<details>
<summary>Ver solución</summary>

Ambos tienen **rango = 5** (10 - 5 = 5) porque el rango solo considera el máximo y el mínimo.

**Pero son muy diferentes:**
- Primer grupo: 4 de 5 valores son 5, solo uno es 10 (muy concentrado en 5)
- Segundo grupo: Valores distribuidos uniformemente (5,6,7,8,9,10)

**Esto ilustra la principal limitación del rango:** 
Ignora todos los valores intermedios y no refleja cómo están distribuidos los datos dentro del intervalo.

</details>

### Ejercicio 4
Una empresa mide las ventas diarias (en miles de pesos):

Semana 1: 50, 55, 52, 48, 53 → R = ?
Semana 2: 20, 45, 60, 80, 45 → R = ?

¿Qué semana tuvo ventas más consistentes?

<details>
<summary>Ver solución</summary>

**Semana 1:**
$R = 55 - 48 = 7$ (miles de pesos)

**Semana 2:**
$R = 80 - 20 = 60$ (miles de pesos)

**La Semana 1 tuvo ventas más consistentes** porque:
- Rango de solo 7 (todas las ventas entre 48-55)
- Semana 2 tiene rango de 60 (ventas muy variables, de 20 a 80)

</details>

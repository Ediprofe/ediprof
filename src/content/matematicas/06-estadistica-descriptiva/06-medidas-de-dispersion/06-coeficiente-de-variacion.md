# Coeficiente de Variación

¿Qué pasa si queremos comparar la dispersión de fenómenos completamente diferentes? Una desviación estándar de 10 puede ser mucha o poca, dependiendo de si hablamos de centímetros o millones de pesos. El **coeficiente de variación** resuelve este problema.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el coeficiente de variación y para qué sirve
- Cómo calcularlo e interpretarlo
- Cuándo usarlo (y cuándo no)
- Comparar la dispersión entre grupos diferentes

---

## 📖 El Problema: Comparar Dispersiones Diferentes

### ⚙️ Ejemplo:

- **Estaturas:** Media = 170 cm, $s = 10$ cm
- **Pesos:** Media = 70 kg, $s = 10$ kg

Ambos tienen $s = 10$, pero ¿tienen la misma dispersión relativa?

- 10 cm respecto a 170 cm es aproximadamente **6%**
- 10 kg respecto a 70 kg es aproximadamente **14%**

El peso tiene mayor variabilidad **relativa**, aunque la desviación estándar "absoluta" sea igual.

---

## 📖 Definición del Coeficiente de Variación

> El **coeficiente de variación** (CV) expresa la desviación estándar como **porcentaje** de la media.

### 💡 Fórmula:

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

### 💡 Características:
- Es **adimensional** (no tiene unidades)
- Permite comparar variables con diferentes escalas
- Se expresa como porcentaje

---

## 📖 Cálculo del Coeficiente de Variación

### ⚙️ Ejemplo 1: Estaturas vs Pesos

**Estaturas:**
- $\bar{x} = 170$ cm
- $s = 10$ cm
- $CV = \frac{10}{170} \times 100\% = 5.88\%$

**Pesos:**
- $\bar{x} = 70$ kg
- $s = 10$ kg
- $CV = \frac{10}{70} \times 100\% = 14.29\%$

**Conclusión:** Aunque ambos tienen $s = 10$, el peso tiene **mayor variabilidad relativa** (14.29% vs 5.88%).

### ⚙️ Ejemplo 2: Comparar dos grupos

**Grupo A - Salarios (empleados junior):**
- Media: $1,500,000
- Desviación estándar: $200,000
- $CV = \frac{200,000}{1,500,000} \times 100\% = 13.3\%$

**Grupo B - Salarios (ejecutivos):**
- Media: $8,000,000
- Desviación estándar: $600,000
- $CV = \frac{600,000}{8,000,000} \times 100\% = 7.5\%$

| Grupo | $s$ | CV | Conclusión |
|-------|-----|-----|------------|
| Junior | $200,000 | 13.3% | Mayor variabilidad relativa |
| Ejecutivos | $600,000 | 7.5% | Menor variabilidad relativa |

Aunque los ejecutivos tienen **mayor** desviación estándar ($600k vs $200k), tienen **menor** coeficiente de variación (7.5% vs 13.3%).

Los salarios de los junior son proporcionalmente más dispersos.

---

## 📖 Interpretación del CV

| Valor del CV | Interpretación |
|--------------|----------------|
| CV < 10% | Muy baja dispersión (datos homogéneos) |
| 10% ≤ CV < 20% | Dispersión moderada |
| 20% ≤ CV < 30% | Alta dispersión |
| CV ≥ 30% | Muy alta dispersión (datos heterogéneos) |

### 💡 Estas son guías generales, el contexto importa.

---

## ⚠️ Limitaciones del Coeficiente de Variación

### Limitación 1: No funciona si la media es cero o cercana a cero

Si $\bar{x} \approx 0$, el CV se vuelve muy grande o indefinido.

### ⚙️ Ejemplo problemático:

Temperaturas (°C): -5, 0, 2, 3, 5 → Media ≈ 1°C

CV sería muy grande, pero no porque haya mucha dispersión, sino porque la media está cerca de cero.

### Limitación 2: No funciona con datos negativos

Si la media es negativa, el CV pierde sentido.

### Limitación 3: Mejor para variables de razón

El CV es más significativo para variables que tienen un **cero absoluto** (peso, estatura, dinero) que para variables como temperatura Celsius.

---

## 📖 Aplicaciones Prácticas

| Campo | Uso del CV |
|-------|------------|
| **Control de calidad** | Comparar la precisión de diferentes máquinas |
| **Finanzas** | Medir el riesgo relativo de inversiones |
| **Ciencias** | Comparar variabilidad de mediciones en diferentes experimentos |
| **Economía** | Comparar desigualdad entre países de diferente tamaño |

### ⚙️ Ejemplo: Control de calidad

Dos máquinas producen tornillos de 10 mm:

| Máquina | Media | $s$ | CV |
|---------|-------|-----|-----|
| A | 10.0 mm | 0.2 mm | 2% |
| B | 10.0 mm | 0.5 mm | 5% |

**La máquina A es más precisa** (menor CV).

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Coeficiente de Variación** | $CV = \frac{s}{\bar{x}} \times 100\%$ |
| **Ventaja** | Permite comparar dispersiones de variables diferentes |
| **Interpretación** | Dispersión como % de la media |
| **Limitación** | No usar si la media es cero o negativa |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el CV para cada conjunto:

a) Media = 50, s = 10
b) Media = 200, s = 10
c) Media = 200, s = 40

<details>
<summary>Ver solución</summary>

a) $CV = \frac{10}{50} \times 100\% = 20\%$

b) $CV = \frac{10}{200} \times 100\% = 5\%$

c) $CV = \frac{40}{200} \times 100\% = 20\%$

**Comparación:**
- a y c tienen el mismo CV (20%) aunque diferentes medias y desviaciones
- b tiene menor CV (5%) aunque tiene la misma s que a

</details>

### Ejercicio 2
¿Cuál grupo tiene datos más homogéneos?

Grupo A: Media = 100, CV = 15%
Grupo B: Media = 500, CV = 8%

<details>
<summary>Ver solución</summary>

**El Grupo B tiene datos más homogéneos** porque su CV es menor (8% < 15%).

El CV nos dice que:
- En el Grupo A, los datos varían típicamente un 15% respecto a la media
- En el Grupo B, los datos varían típicamente un 8% respecto a la media

Aunque no conocemos las desviaciones estándar exactas, sabemos que el Grupo B es proporcionalmente menos disperso.

</details>

### Ejercicio 3
Las estaturas de hombres tienen media 175 cm y CV = 4%. Las de mujeres tienen media 162 cm y CV = 4%. ¿Qué grupo tiene mayor desviación estándar?

<details>
<summary>Ver solución</summary>

Despejando s de la fórmula del CV:

$s = CV \times \bar{x}$ (con CV en decimal)

**Hombres:**
$s = 0.04 \times 175 = 7$ cm

**Mujeres:**
$s = 0.04 \times 162 = 6.48$ cm

**Los hombres tienen mayor desviación estándar** (7 cm vs 6.48 cm), aunque ambos grupos tienen el mismo CV.

Esto tiene sentido: si la variabilidad relativa es igual, el grupo con mayor media tendrá mayor dispersión absoluta.

</details>

### Ejercicio 4
¿Por qué el CV no se debe usar para comparar temperaturas en Celsius?

<details>
<summary>Ver solución</summary>

El CV no es apropiado para temperaturas Celsius porque:

1. **El cero no es absoluto:** 0°C no significa "ausencia de temperatura", es solo el punto de congelación del agua.

2. **Puede dar resultados sin sentido:** Si la temperatura media es 5°C con s = 2°C, el CV sería 40%. Pero si cambiamos a Fahrenheit (media ≈ 41°F, s ≈ 3.6°F), el CV sería ~9%.

3. **Depende de la escala:** El mismo fenómeno daría CV diferentes según usemos Celsius, Fahrenheit o Kelvin.

4. **La media puede ser cercana a cero:** En temperaturas cerca de 0°C, el CV se dispara artificialmente.

**Alternativa:** Para temperaturas, es mejor usar solo la desviación estándar, o convertir a Kelvin (donde sí hay cero absoluto).

</details>

---
title: "La Distribución Normal"
---

# La Distribución Normal

La **distribución normal** (o gaussiana) es la más importante en estadística. Modela innumerables fenómenos naturales y es la base de la inferencia estadística.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la distribución normal y su famosa "campana"
- La distribución normal estándar (Z)
- Cómo estandarizar y usar tablas
- El Teorema del Límite Central

---

## 📖 Características de la Distribución Normal

### 💡 Forma:

- Curva simétrica en forma de **campana**
- El pico está en la media (μ)
- Se extiende infinitamente en ambas direcciones
- El área total bajo la curva = 1

### 💡 Parámetros:

$$
X \sim N(\mu, \sigma^2)
$$

- μ = media (centro de la campana)
- σ = desviación estándar (ancho de la campana)

---

## 📖 Propiedades de la Normal

| Propiedad | Descripción |
|-----------|-------------|
| **Simetría** | La curva es simétrica respecto a μ |
| **Media = Mediana = Moda** | Todas coinciden en μ |
| **Asíntotas** | La curva se acerca al eje pero nunca lo toca |
| **Puntos de inflexión** | Están en μ ± σ |

---

## 📖 La Regla Empírica (68-95-99.7)

Para cualquier distribución normal:

| Intervalo | % de datos |
|-----------|------------|
| μ ± 1σ | 68.27% |
| μ ± 2σ | 95.45% |
| μ ± 3σ | 99.73% |

### ⚙️ Ejemplo:

Estaturas de adultos: μ = 170 cm, σ = 8 cm

| Intervalo | Rango | % |
|-----------|-------|---|
| 170 ± 8 | 162-178 cm | 68% |
| 170 ± 16 | 154-186 cm | 95% |
| 170 ± 24 | 146-194 cm | 99.7% |

---

## 📖 La Distribución Normal Estándar (Z)

> La **normal estándar** es la normal con μ = 0 y σ = 1.

$$
Z \sim N(0, 1)
$$

### 💡 ¿Por qué es importante?

- Todas las normales se pueden convertir a estándar
- Hay tablas tabuladas para la estándar
- Simplifica cálculos

---

## 📖 Estandarización

### 💡 Fórmula para convertir X en Z:

$$
Z = \frac{X - \mu}{\sigma}
$$

### 💡 Interpretación de Z:

Z indica cuántas desviaciones estándar está X de la media.

- Z = 0 → X está en la media
- Z = 1 → X está 1σ arriba de la media
- Z = -2 → X está 2σ debajo de la media

### ⚙️ Ejemplo:

Si estaturas tienen μ = 170 cm, σ = 8 cm:

¿Cuál es el Z-score de alguien de 178 cm?

$$
Z = \frac{178 - 170}{8} = \frac{8}{8} = 1
$$

Esta persona está 1 desviación estándar arriba de la media.

---

## 📖 Uso de la Tabla Normal

### 💡 La tabla da P(Z ≤ z):

Para encontrar probabilidades:

1. Estandarizar el valor X a Z
2. Buscar en la tabla el valor correspondiente
3. Ajustar según la pregunta

### 💡 Valores comunes:

| Z | P(Z ≤ z) |
|---|----------|
| -2.0 | 0.0228 |
| -1.0 | 0.1587 |
| 0 | 0.5000 |
| 1.0 | 0.8413 |
| 2.0 | 0.9772 |
| 2.5 | 0.9938 |

---

## 📖 Ejemplos de Cálculo

### ⚙️ Ejemplo: Notas de examen

Las notas siguen N(70, 10²). ¿Qué proporción saca más de 85?

**Paso 1:** Estandarizar
$$
Z = \frac{85 - 70}{10} = 1.5
$$

**Paso 2:** Buscar P(Z ≤ 1.5) = 0.9332

**Paso 3:** Calcular P(Z > 1.5)
$$
P(X > 85) = 1 - 0.9332 = 0.0668 \approx 6.7\%
$$

### ⚙️ Ejemplo: Entre dos valores

¿Qué proporción saca entre 60 y 80?

$Z_1 = \frac{60-70}{10} = -1$, P(Z ≤ -1) = 0.1587

$Z_2 = \frac{80-70}{10} = 1$, P(Z ≤ 1) = 0.8413

$$
P(60 < X < 80) = 0.8413 - 0.1587 = 0.6826 \approx 68.3\%
$$

---

## 📖 Problemas Inversos: Encontrar X dado el Percentil

### ⚙️ Ejemplo:

¿Cuál es la nota mínima para estar en el top 10%?

**Paso 1:** El top 10% significa P(X > x) = 0.10, o P(X ≤ x) = 0.90

**Paso 2:** Buscar en tabla inversa: Z ≈ 1.28

**Paso 3:** Despejar X
$$
X = \mu + Z \cdot \sigma = 70 + 1.28 \times 10 = 82.8
$$

Necesitas sacar al menos 83 para estar en el top 10%.

---

## 📖 Teorema del Límite Central

> Si tomamos muestras de tamaño n de **cualquier** población con media μ y varianza σ², la distribución de las **medias muestrales** se aproxima a una normal cuando n es grande.

$$
\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)
$$

### 💡 Implicaciones:

1. Funciona para **cualquier** distribución original
2. Cuanto mayor n, mejor la aproximación
3. n ≥ 30 suele ser suficiente

---

## 🔑 Resumen

| Concepto | Fórmula/Valor |
|----------|---------------|
| **Estandarización** | $Z = \frac{X-\mu}{\sigma}$ |
| **Regla 68-95-99.7** | ±1σ, ±2σ, ±3σ |
| **Normal estándar** | $Z \sim N(0,1)$ |
| **TLC** | Medias muestrales → Normal |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
X ~ N(100, 15²). Calcula:
a) P(X < 115)
b) P(X > 85)
c) P(85 < X < 115)

<details>
<summary>Ver solución</summary>

a) $Z = \frac{115-100}{15} = 1$
   P(X < 115) = P(Z < 1) = **0.8413**

b) $Z = \frac{85-100}{15} = -1$
   P(X > 85) = P(Z > -1) = 1 - 0.1587 = **0.8413**

c) P(85 < X < 115) = P(-1 < Z < 1) = 0.8413 - 0.1587 = **0.6826**

(Esto confirma la regla 68%: ±1σ contiene ~68% de los datos)

</details>

### Ejercicio 2
El peso de bebés al nacer sigue N(3200g, 500²g). ¿Qué porcentaje pesa menos de 2500g?

<details>
<summary>Ver solución</summary>

$Z = \frac{2500 - 3200}{500} = \frac{-700}{500} = -1.4$

P(Z < -1.4) = 0.0808

**Aproximadamente 8% de los bebés pesa menos de 2500g** (bajo peso al nacer).

</details>

### Ejercicio 3
Si Z ~ N(0,1), ¿cuál es el valor de z tal que P(Z > z) = 0.05?

<details>
<summary>Ver solución</summary>

P(Z > z) = 0.05 significa P(Z ≤ z) = 0.95

Buscando en tabla: **z ≈ 1.645**

(Este es un valor crítico muy usado en pruebas de hipótesis)

</details>

### Ejercicio 4
El tiempo de servicio en un banco es N(5min, 1.5²min). Si hay 50 clientes, ¿cuál es la probabilidad de que el tiempo promedio de servicio sea mayor a 5.5 minutos?

<details>
<summary>Ver solución</summary>

Por el TLC, $\bar{X} \sim N(5, \frac{1.5^2}{50}) = N(5, 0.045)$

$\sigma_{\bar{X}} = \sqrt{0.045} = 0.212$

$Z = \frac{5.5 - 5}{0.212} = 2.36$

P(Z > 2.36) = 1 - 0.9909 = **0.0091**

Solo 0.9% de probabilidad de que el promedio supere 5.5 minutos.

</details>

# Desviación Media

El rango solo usa el máximo y el mínimo. ¿Y si quisiéramos usar **todos** los datos para medir la dispersión? La **desviación media** nos dice, en promedio, qué tan lejos están los datos de la media.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la desviación y cómo calcularla
- La fórmula de la desviación media
- Por qué usamos valores absolutos
- Limitaciones de esta medida

---

## 📖 ¿Qué es una Desviación?

> La **desviación** de un dato es la **distancia** entre ese dato y la media.

### 💡 Fórmula de desviación individual:

$$
d_i = x_i - \bar{x}
$$

### ⚙️ Ejemplo:

Datos: 2, 4, 6, 8, 10 → Media = 6

| Dato ($x_i$) | Desviación ($x_i - \bar{x}$) |
|--------------|------------------------------|
| 2 | 2 - 6 = **-4** |
| 4 | 4 - 6 = **-2** |
| 6 | 6 - 6 = **0** |
| 8 | 8 - 6 = **+2** |
| 10 | 10 - 6 = **+4** |

Las desviaciones negativas son datos **por debajo** de la media.
Las desviaciones positivas son datos **por encima** de la media.

---

## 📖 El Problema: Las Desviaciones Suman Cero

Si intentamos promediar las desviaciones directamente:

$$
\frac{(-4) + (-2) + 0 + 2 + 4}{5} = \frac{0}{5} = 0
$$

¡Siempre da cero! Los negativos cancelan a los positivos.

### 💡 Solución: Usar valores absolutos

El **valor absoluto** elimina el signo, dejando solo la magnitud de la distancia:

$$
|{-4}| = 4, \quad |{-2}| = 2, \quad |0| = 0, \quad |2| = 2, \quad |4| = 4
$$

---

## 📖 Definición de Desviación Media

> La **desviación media** (DM) es el promedio de los **valores absolutos** de las desviaciones respecto a la media.

### 💡 Fórmula:

$$
DM = \frac{\sum |x_i - \bar{x}|}{n}
$$

---

## 📖 Cálculo Paso a Paso

### ⚙️ Ejemplo: Notas de 6 estudiantes

Notas: 5, 6, 7, 8, 9, 9

**Paso 1:** Calcular la media
$$
\bar{x} = \frac{5+6+7+8+9+9}{6} = \frac{44}{6} = 7.33
$$

**Paso 2:** Calcular las desviaciones absolutas

| $x_i$ | $x_i - \bar{x}$ | $|x_i - \bar{x}|$ |
|-------|-----------------|-------------------|
| 5 | 5 - 7.33 = -2.33 | 2.33 |
| 6 | 6 - 7.33 = -1.33 | 1.33 |
| 7 | 7 - 7.33 = -0.33 | 0.33 |
| 8 | 8 - 7.33 = 0.67 | 0.67 |
| 9 | 9 - 7.33 = 1.67 | 1.67 |
| 9 | 9 - 7.33 = 1.67 | 1.67 |
| **Suma** | | **8.00** |

**Paso 3:** Calcular la desviación media
$$
DM = \frac{8.00}{6} = 1.33
$$

**Interpretación:** En promedio, las notas se desvían 1.33 puntos de la media.

---

## 📖 Desviación Media con Frecuencias

Para datos con tabla de frecuencias:

$$
DM = \frac{\sum f_i \cdot |x_i - \bar{x}|}{n}
$$

### ⚙️ Ejemplo:

| Valor ($x_i$) | $f_i$ | $f_i \cdot x_i$ |
|---------------|-------|-----------------|
| 3 | 2 | 6 |
| 4 | 5 | 20 |
| 5 | 8 | 40 |
| 6 | 3 | 18 |
| 7 | 2 | 14 |
| **Total** | **20** | **98** |

**Media:** $\bar{x} = \frac{98}{20} = 4.9$

| $x_i$ | $f_i$ | $|x_i - 4.9|$ | $f_i \cdot |x_i - 4.9|$ |
|-------|-------|---------------|--------------------------|
| 3 | 2 | 1.9 | 3.8 |
| 4 | 5 | 0.9 | 4.5 |
| 5 | 8 | 0.1 | 0.8 |
| 6 | 3 | 1.1 | 3.3 |
| 7 | 2 | 2.1 | 4.2 |
| **Total** | **20** | | **16.6** |

$$
DM = \frac{16.6}{20} = 0.83
$$

---

## 💡 Interpretación de la Desviación Media

| Valor de DM | Interpretación |
|-------------|----------------|
| DM = 0 | Todos los datos son iguales (sin dispersión) |
| DM pequeña | Datos agrupados cerca de la media |
| DM grande | Datos dispersos, alejados de la media |

### ⚙️ Ejemplo comparativo:

**Grupo A:** 48, 49, 50, 51, 52 → $\bar{x} = 50$, $DM = 1.2$
**Grupo B:** 30, 40, 50, 60, 70 → $\bar{x} = 50$, $DM = 12$

Ambos tienen la misma media (50), pero:
- Grupo A: Datos muy cercanos a la media (DM = 1.2)
- Grupo B: Datos muy alejados de la media (DM = 12)

---

## ⚠️ Limitaciones de la Desviación Media

| Limitación | Explicación |
|------------|-------------|
| **Uso del valor absoluto** | Matemáticamente incómodo para análisis avanzados |
| **Menos propiedades estadísticas** | No se usa en pruebas de hipótesis ni intervalos de confianza |
| **Poco usada en la práctica** | La desviación estándar es preferida |

### 💡 ¿Por qué entonces aprenderla?

1. **Paso conceptual:** Ayuda a entender la idea de "dispersión promedio"
2. **Base para la varianza:** La varianza usa una idea similar pero con cuadrados
3. **Interpretación intuitiva:** DM = 5 significa "en promedio, los datos están a 5 unidades de la media"

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Desviación** | Distancia de un dato a la media: $x_i - \bar{x}$ |
| **Desviación media** | Promedio de las distancias absolutas: $DM = \frac{\sum|x_i - \bar{x}|}{n}$ |
| **Interpretación** | "En promedio, los datos están a DM unidades de la media" |
| **Limitación** | Menos útil que la desviación estándar para análisis avanzados |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la desviación media de: 10, 12, 14, 16, 18

<details>
<summary>Ver solución</summary>

**Paso 1:** Media
$\bar{x} = \frac{10+12+14+16+18}{5} = \frac{70}{5} = 14$

**Paso 2:** Desviaciones absolutas

| $x_i$ | $|x_i - 14|$ |
|-------|-------------|
| 10 | 4 |
| 12 | 2 |
| 14 | 0 |
| 16 | 2 |
| 18 | 4 |
| **Suma** | **12** |

**Paso 3:** Desviación media
$DM = \frac{12}{5} = 2.4$

**Interpretación:** En promedio, los datos se desvían 2.4 unidades de la media.

</details>

### Ejercicio 2
Dos grupos tienen la misma media (100):

Grupo A: 98, 99, 100, 101, 102
Grupo B: 80, 90, 100, 110, 120

Calcula la DM de cada uno y compáralos.

<details>
<summary>Ver solución</summary>

**Grupo A:** Media = 100

| $x_i$ | $|x_i - 100|$ |
|-------|---------------|
| 98 | 2 |
| 99 | 1 |
| 100 | 0 |
| 101 | 1 |
| 102 | 2 |
| **Suma** | **6** |

$DM_A = \frac{6}{5} = 1.2$

**Grupo B:** Media = 100

| $x_i$ | $|x_i - 100|$ |
|-------|---------------|
| 80 | 20 |
| 90 | 10 |
| 100 | 0 |
| 110 | 10 |
| 120 | 20 |
| **Suma** | **60** |

$DM_B = \frac{60}{5} = 12$

**Comparación:**
- Grupo A: DM = 1.2 (muy homogéneo)
- Grupo B: DM = 12 (muy disperso)

El Grupo B tiene 10 veces más dispersión que el Grupo A, aunque ambos tienen la misma media.

</details>

### Ejercicio 3
¿Por qué no podemos simplemente promediar las desviaciones sin usar valor absoluto?

<details>
<summary>Ver solución</summary>

Porque **las desviaciones siempre suman cero**.

**Demostración:**
$\sum(x_i - \bar{x}) = \sum x_i - n\bar{x} = \sum x_i - n \cdot \frac{\sum x_i}{n} = \sum x_i - \sum x_i = 0$

**En palabras:**
- Los datos por debajo de la media tienen desviación negativa
- Los datos por encima de la media tienen desviación positiva
- Por definición de media, estas desviaciones se cancelan exactamente

**Ejemplo:**
Datos: 2, 4, 6 → Media = 4
Desviaciones: -2, 0, +2 → Suma = 0

Por eso usamos:
- **Valor absoluto:** $|x_i - \bar{x}|$ → Desviación media
- **Cuadrados:** $(x_i - \bar{x})^2$ → Varianza

Ambos métodos eliminan el problema de los signos opuestos.

</details>

### Ejercicio 4
Si la desviación media de un conjunto de datos es 0, ¿qué puedes concluir sobre esos datos?

<details>
<summary>Ver solución</summary>

Si $DM = 0$, entonces **todos los datos son iguales a la media**.

**Razonamiento:**
- $DM = \frac{\sum|x_i - \bar{x}|}{n} = 0$
- Para que la suma de valores absolutos sea 0, cada término debe ser 0
- $|x_i - \bar{x}| = 0$ para todo $i$
- Por lo tanto, $x_i = \bar{x}$ para todo $i$

**Ejemplo:**
Datos: 5, 5, 5, 5, 5 → Media = 5

Todas las desviaciones: $|5-5| = 0$

$DM = \frac{0+0+0+0+0}{5} = 0$

**Conclusión:** DM = 0 significa **dispersión nula**, todos los valores son idénticos.

</details>

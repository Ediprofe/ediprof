# Media Aritmética

El "promedio" que todos conocemos y usamos tiene un nombre técnico: **media aritmética**. Es la medida de tendencia central más utilizada, pero también la más malinterpretada.

Aprendamos a calcularla correctamente y a entender cuándo confiar en ella.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula y cálculo de la media
- Propiedades importantes de la media
- Cómo calcular la media con tablas de frecuencias
- La notación sumatoria (Σ)

---

## 📊 Fórmula de la Media

| Tipo de datos | Fórmula |
|---------------|---------|
| Datos simples | $\bar{x} = \frac{\sum x_i}{n}$ |
| Con frecuencias | $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$ |
| Datos agrupados | $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$ (usando marcas de clase) |

---

## 📖 Definición de la Media

> La **media aritmética** ($\bar{x}$) es la suma de todos los valores dividida entre la cantidad de valores.

### 💡 Fórmula básica:

$$
\bar{x} = \frac{x_1 + x_2 + x_3 + ... + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Donde:
- $\bar{x}$ = "x barra", la media
- $x_i$ = cada valor individual
- $n$ = cantidad total de valores
- $\Sigma$ = sumatoria (suma de todos)

---

## 📖 La Notación Sumatoria (Σ)

> El símbolo **Σ** (sigma mayúscula) significa "suma de todos".

### 💡 Cómo leerlo:

$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + x_3 + ... + x_n
$$

- El índice ($i$) va desde 1 hasta $n$
- Sumamos todos los valores $x_i$

### ⚙️ Ejemplo:

Si $x_1 = 3$, $x_2 = 5$, $x_3 = 7$, $x_4 = 9$:

$$
\sum_{i=1}^{4} x_i = 3 + 5 + 7 + 9 = 24
$$

---

## 📖 Cálculo de la Media: Datos Simples

### ⚙️ Ejemplo 1: Notas de 6 exámenes

Notas: 7.5, 8.0, 6.5, 9.0, 7.0, 8.5

**Paso 1:** Sumar todos los valores
$$
\sum x = 7.5 + 8.0 + 6.5 + 9.0 + 7.0 + 8.5 = 46.5
$$

**Paso 2:** Dividir entre la cantidad (n = 6)
$$
\bar{x} = \frac{46.5}{6} = 7.75
$$

**Interpretación:** El promedio de notas es 7.75

### ⚙️ Ejemplo 2: Edades de 5 amigos

Edades: 18, 20, 19, 21, 17

$$
\bar{x} = \frac{18 + 20 + 19 + 21 + 17}{5} = \frac{95}{5} = 19 \text{ años}
$$

---

## 📖 Cálculo de la Media: Con Tabla de Frecuencias

Cuando los datos vienen en una tabla de frecuencias, usamos:

$$
\bar{x} = \frac{\sum f_i \cdot x_i}{n} = \frac{\sum f_i \cdot x_i}{\sum f_i}
$$

### ⚙️ Ejemplo: Número de hermanos

| Hermanos ($x_i$) | Frecuencia ($f_i$) | $f_i \cdot x_i$ |
|------------------|-------------------|-----------------|
| 0 | 5 | $5 \times 0 = 0$ |
| 1 | 12 | $12 \times 1 = 12$ |
| 2 | 8 | $8 \times 2 = 16$ |
| 3 | 4 | $4 \times 3 = 12$ |
| 4 | 1 | $1 \times 4 = 4$ |
| **Total** | **30** | **44** |

$$
\bar{x} = \frac{\sum f_i \cdot x_i}{\sum f_i} = \frac{44}{30} = 1.47 \text{ hermanos}
$$

**Interpretación:** En promedio, los estudiantes tienen aproximadamente 1.5 hermanos.

---

## 📖 Cálculo de la Media: Datos Agrupados

Para datos agrupados en clases, usamos la **marca de clase** ($x_i$) como representante de cada intervalo:

### ⚙️ Ejemplo: Pesos de estudiantes

| Intervalo | Marca de Clase ($x_i$) | $f_i$ | $f_i \cdot x_i$ |
|-----------|----------------------|-------|-----------------|
| 52 - 58 | 55 | 7 | 385 |
| 59 - 65 | 62 | 8 | 496 |
| 66 - 72 | 69 | 9 | 621 |
| 73 - 79 | 76 | 8 | 608 |
| 80 - 86 | 83 | 4 | 332 |
| 87 - 93 | 90 | 4 | 360 |
| **Total** | | **40** | **2,802** |

$$
\bar{x} = \frac{2802}{40} = 70.05 \text{ kg}
$$

**Nota:** Este es un valor **aproximado** porque no conocemos los valores exactos dentro de cada clase.

---

## 📖 Propiedades de la Media

### 💡 Propiedad 1: La suma de las desviaciones es cero

Si restamos la media a cada valor, la suma de esas diferencias es cero:

$$
\sum (x_i - \bar{x}) = 0
$$

### ⚙️ Ejemplo:

Datos: 2, 4, 6 → Media = 4

| $x_i$ | $x_i - \bar{x}$ |
|-------|-----------------|
| 2 | 2 - 4 = -2 |
| 4 | 4 - 4 = 0 |
| 6 | 6 - 4 = +2 |
| **Suma** | **0** |

**Interpretación:** La media es el "punto de equilibrio" donde las desviaciones negativas y positivas se cancelan.

### 💡 Propiedad 2: Sensibilidad a valores extremos

La media cambia significativamente cuando hay valores extremos (outliers).

### ⚙️ Ejemplo:

**Sin outlier:** 10, 12, 11, 13, 14 → $\bar{x} = \frac{60}{5} = 12$

**Con outlier:** 10, 12, 11, 13, **100** → $\bar{x} = \frac{146}{5} = 29.2$

¡Un solo valor extremo (100) casi triplicó la media!

### 💡 Propiedad 3: Transformaciones lineales

Si multiplicamos todos los datos por una constante $a$ y sumamos $b$:

$$
\bar{x}_{nuevo} = a \cdot \bar{x} + b
$$

### ⚙️ Ejemplo: Conversión de temperatura

Si la media en Celsius es 20°C, ¿cuál es en Fahrenheit?

Fórmula: $F = 1.8 \cdot C + 32$

$$
\bar{x}_F = 1.8 \times 20 + 32 = 36 + 32 = 68°F
$$

---

## 📖 Media Poblacional vs Muestral

| Símbolo | Descripción | Fórmula |
|---------|-------------|---------|
| $\mu$ (mu) | Media poblacional (parámetro) | $\mu = \frac{\sum x_i}{N}$ |
| $\bar{x}$ (x barra) | Media muestral (estadístico) | $\bar{x} = \frac{\sum x_i}{n}$ |

- **N** = tamaño de la población
- **n** = tamaño de la muestra

Usamos $\bar{x}$ como **estimador** de $\mu$ cuando no podemos medir toda la población.

---

## 💡 Cuándo Usar (y No Usar) la Media

| ✅ Usar cuando... | ❌ Evitar cuando... |
|-------------------|---------------------|
| Datos simétricos | Hay valores extremos (outliers) |
| Se necesita un dato resumen | La distribución es muy sesgada |
| Datos cuantitativos | Datos cualitativos |
| Comparar grupos | El "centro" no es representativo |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Media ($\bar{x}$)** | Suma de valores / cantidad de valores |
| **Fórmula simple** | $\bar{x} = \frac{\sum x_i}{n}$ |
| **Con frecuencias** | $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$ |
| **Símbolo Σ** | Sumatoria (suma de todos) |
| **Debilidad** | Sensible a valores extremos |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la media de los siguientes datos:

a) 15, 18, 22, 19, 16
b) 3.5, 4.2, 3.8, 4.0, 4.5, 3.9

<details>
<summary>Ver solución</summary>

a) **Datos: 15, 18, 22, 19, 16**
$$\bar{x} = \frac{15 + 18 + 22 + 19 + 16}{5} = \frac{90}{5} = 18$$

b) **Datos: 3.5, 4.2, 3.8, 4.0, 4.5, 3.9**
$$\bar{x} = \frac{3.5 + 4.2 + 3.8 + 4.0 + 4.5 + 3.9}{6} = \frac{23.9}{6} = 3.98$$

</details>

### Ejercicio 2
Usa la siguiente tabla de frecuencias para calcular la media:

| Calificación | Frecuencia |
|--------------|------------|
| 5 | 3 |
| 6 | 7 |
| 7 | 12 |
| 8 | 8 |
| 9 | 4 |
| 10 | 2 |

<details>
<summary>Ver solución</summary>

| Calificación ($x_i$) | $f_i$ | $f_i \cdot x_i$ |
|---------------------|-------|-----------------|
| 5 | 3 | 15 |
| 6 | 7 | 42 |
| 7 | 12 | 84 |
| 8 | 8 | 64 |
| 9 | 4 | 36 |
| 10 | 2 | 20 |
| **Total** | **36** | **261** |

$$\bar{x} = \frac{261}{36} = 7.25$$

**La media de calificaciones es 7.25**

</details>

### Ejercicio 3
La media de 5 números es 12. Si agregamos el número 24, ¿cuál es la nueva media?

<details>
<summary>Ver solución</summary>

**Paso 1:** Encontrar la suma original
Si $\bar{x} = 12$ y $n = 5$:
$$\sum x = \bar{x} \times n = 12 \times 5 = 60$$

**Paso 2:** Agregar el nuevo número
$$\sum x_{nueva} = 60 + 24 = 84$$

**Paso 3:** Calcular la nueva media
$$\bar{x}_{nueva} = \frac{84}{6} = 14$$

**La nueva media es 14**

</details>

### Ejercicio 4
Si la media de los precios en dólares es $50, y el tipo de cambio es 1 dólar = 4,000 pesos, ¿cuál es la media en pesos?

<details>
<summary>Ver solución</summary>

Usamos la propiedad de transformación lineal.

La conversión es: $\text{pesos} = \text{dólares} \times 4000$

Esto es una transformación con $a = 4000$ y $b = 0$:

$$\bar{x}_{pesos} = 4000 \times \bar{x}_{dólares} = 4000 \times 50 = 200,000 \text{ pesos}$$

**La media en pesos es $200,000**

</details>

### Ejercicio 5
Demuestra que $\sum (x_i - \bar{x}) = 0$ para los datos: 3, 5, 7, 9, 11

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular la media
$$\bar{x} = \frac{3 + 5 + 7 + 9 + 11}{5} = \frac{35}{5} = 7$$

**Paso 2:** Calcular las desviaciones

| $x_i$ | $x_i - \bar{x}$ |
|-------|-----------------|
| 3 | 3 - 7 = -4 |
| 5 | 5 - 7 = -2 |
| 7 | 7 - 7 = 0 |
| 9 | 9 - 7 = +2 |
| 11 | 11 - 7 = +4 |

**Paso 3:** Sumar las desviaciones
$$\sum (x_i - \bar{x}) = -4 + (-2) + 0 + 2 + 4 = 0$$

**✓ Demostrado:** La suma de las desviaciones respecto a la media es cero.

</details>

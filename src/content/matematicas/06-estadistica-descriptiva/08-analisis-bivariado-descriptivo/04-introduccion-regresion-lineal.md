# Introducción a la Regresión Lineal

Ahora que sabemos medir la relación entre dos variables, queremos ir más allá: **predecir** una variable usando la otra. La **regresión lineal** nos permite encontrar la mejor línea recta que describe la relación entre X e Y.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la regresión lineal y para qué sirve
- El concepto de "mejor ajuste" (mínimos cuadrados)
- Cómo calcular la ecuación de la recta
- Cómo usar la recta para hacer predicciones

---

## 📖 ¿Qué es la Regresión Lineal?

> La **regresión lineal simple** busca la línea recta que **mejor representa** la relación entre una variable explicativa (X) y una variable respuesta (Y).

### 💡 Ecuación de la recta:

$$
\hat{y} = a + bx
$$

Donde:
- $\hat{y}$ = valor predicho de Y (se lee "y sombrero")
- $a$ = intercepto (valor de Y cuando X = 0)
- $b$ = pendiente (cuánto cambia Y por cada unidad de X)

---

## 📖 El Método de Mínimos Cuadrados

### 💡 Idea clave:

Queremos la recta que **minimice los errores** de predicción.

### ¿Qué es un error?

El error (o residuo) es la diferencia entre el valor real y el predicho:

$$
e_i = y_i - \hat{y}_i
$$

### ¿Por qué "cuadrados"?

Minimizamos la **suma de los cuadrados de los errores**:

$$
\text{Minimizar:} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Usamos cuadrados porque:
1. Evita que errores positivos y negativos se cancelen
2. Penaliza más los errores grandes
3. Tiene buenas propiedades matemáticas

---

## 📖 Fórmulas de los Coeficientes

### 💡 Pendiente (b):

$$
b = \frac{n\sum xy - (\sum x)(\sum y)}{n\sum x^2 - (\sum x)^2}
$$

### 💡 Intercepto (a):

$$
a = \bar{y} - b\bar{x}
$$

### 💡 Relación con la correlación:

$$
b = r \cdot \frac{s_y}{s_x}
$$

---

## 📖 Cálculo Paso a Paso

### ⚙️ Ejemplo: Horas de estudio vs Nota

Usemos los datos anteriores:

| x | y | x² | xy |
|---|---|----|----|
| 2 | 50 | 4 | 100 |
| 4 | 70 | 16 | 280 |
| 3 | 60 | 9 | 180 |
| 5 | 80 | 25 | 400 |
| 6 | 85 | 36 | 510 |
| **Σ=20** | **Σ=345** | **Σ=90** | **Σ=1470** |

$n = 5$, $\bar{x} = 4$, $\bar{y} = 69$

**Paso 1: Calcular la pendiente (b)**

$$
b = \frac{5(1470) - (20)(345)}{5(90) - (20)^2} = \frac{7350 - 6900}{450 - 400} = \frac{450}{50} = 9
$$

**Paso 2: Calcular el intercepto (a)**

$$
a = 69 - 9(4) = 69 - 36 = 33
$$

**Paso 3: Escribir la ecuación**

$$
\hat{y} = 33 + 9x
$$

---

## 📖 Interpretación de la Ecuación

### ⚙️ Nuestra ecuación: $\hat{y} = 33 + 9x$

**Pendiente (b = 9):**
Por cada hora adicional de estudio, la nota aumenta en promedio **9 puntos**.

**Intercepto (a = 33):**
Si un estudiante estudia 0 horas, la nota predicha sería 33.

### ⚠️ Cuidado con el intercepto:

A veces el intercepto no tiene sentido práctico:
- X = 0 puede estar fuera del rango de datos
- La relación podría no ser válida fuera del rango observado

---

## 📖 Haciendo Predicciones

### ⚙️ Ejemplo: ¿Qué nota esperamos si estudia 5 horas?

$$
\hat{y} = 33 + 9(5) = 33 + 45 = 78
$$

Predicción: **78 puntos**

### ⚙️ Ejemplo: ¿Y si estudia 8 horas?

$$
\hat{y} = 33 + 9(8) = 33 + 72 = 105
$$

### ⚠️ Cuidado con la extrapolación:

8 horas está **fuera del rango** de datos (2-6 horas). La predicción de 105 no es confiable y además es imposible (nota > 100).

### 💡 Regla de oro:

Solo predecir dentro del rango de datos observados (**interpolación**), no fuera de él (**extrapolación**).

---

## 📖 Residuos (Errores)

### Cálculo de residuos:

| x | y (real) | ŷ (predicho) | Residuo (y - ŷ) |
|---|----------|--------------|-----------------|
| 2 | 50 | 33 + 9(2) = 51 | -1 |
| 4 | 70 | 33 + 9(4) = 69 | 1 |
| 3 | 60 | 33 + 9(3) = 60 | 0 |
| 5 | 80 | 33 + 9(5) = 78 | 2 |
| 6 | 85 | 33 + 9(6) = 87 | -2 |

### 💡 Propiedades de los residuos:

- La suma de residuos es **cero** (o muy cercana)
- La recta pasa por el punto $(\bar{x}, \bar{y})$

---

## 📖 ¿Cuándo Usar Regresión Lineal?

| Condición | Verificación |
|-----------|--------------|
| Relación lineal | El diagrama de dispersión muestra tendencia recta |
| r moderado a fuerte | \|r\| > 0.3 aproximadamente |
| Sin patrones en residuos | Los residuos deben ser aleatorios |
| Sin outliers influyentes | No hay puntos que distorsionen la línea |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Regresión lineal** | Encontrar la recta que mejor ajusta los datos |
| **Ecuación** | $\hat{y} = a + bx$ |
| **Pendiente (b)** | Cambio en Y por cada unidad de X |
| **Intercepto (a)** | Valor de Y cuando X = 0 |
| **Mínimos cuadrados** | Minimiza la suma de errores al cuadrado |
| **Predicción** | Usar la ecuación para estimar Y dado X |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
La ecuación de regresión entre años de experiencia (X) y salario en miles (Y) es:

$$\hat{y} = 1200 + 80x$$

a) ¿Cuánto aumenta el salario por cada año adicional de experiencia?
b) ¿Cuál es el salario predicho para alguien con 5 años de experiencia?
c) ¿Qué significa el 1200 en esta ecuación?

<details>
<summary>Ver solución</summary>

a) **Aumento por año:** La pendiente es 80, así que el salario aumenta **$80,000** por cada año adicional de experiencia.

b) **Salario con 5 años:**
$\hat{y} = 1200 + 80(5) = 1200 + 400 = 1600$ (miles)
Salario predicho: **$1,600,000**

c) **Significado de 1200:**
Es el intercepto, el salario base predicho cuando X = 0 (sin experiencia).
Salario inicial: **$1,200,000**

</details>

### Ejercicio 2
¿Por qué es peligroso usar la ecuación del Ejercicio 1 para predecir el salario de alguien con 30 años de experiencia, si los datos tenían de 0 a 10 años?

<details>
<summary>Ver solución</summary>

Es peligroso porque:

1. **Extrapolación:** 30 años está muy fuera del rango observado (0-10).

2. **La relación podría cambiar:** El salario podría:
   - Tener una meseta (dejar de crecer tan rápido)
   - Incluso disminuir (trabajadores mayores a veces ganan menos)

3. **Predicción absurda:**
   $\hat{y} = 1200 + 80(30) = 1200 + 2400 = 3600$ (miles)
   Predice $3,600,000, que podría no ser realista.

4. **No hay datos que respalden:** No tenemos evidencia de qué pasa después de 10 años.

**Regla:** Solo predecir dentro del rango de los datos.

</details>

### Ejercicio 3
Si r = 0.9, $s_x = 2$ y $s_y = 10$, ¿cuál es la pendiente de la recta de regresión?

<details>
<summary>Ver solución</summary>

Usando la fórmula:

$$b = r \cdot \frac{s_y}{s_x} = 0.9 \times \frac{10}{2} = 0.9 \times 5 = 4.5$$

**La pendiente es 4.5**

Interpretación: Por cada unidad que aumenta X, Y aumenta en promedio 4.5 unidades.

</details>

### Ejercicio 4
En una regresión, todos los residuos son positivos. ¿Qué significa esto y qué está mal?

<details>
<summary>Ver solución</summary>

**¿Qué significa?**
Todos los valores reales (y) son mayores que los predichos (ŷ). La recta está **por debajo** de todos los puntos.

**¿Qué está mal?**
Esto **no debería ocurrir** si la recta se calculó correctamente con mínimos cuadrados, porque:
1. La suma de residuos debe ser cero
2. Si todos son positivos, la suma sería positiva (contradicción)

**Posibles causas:**
1. Error de cálculo en la ecuación
2. Error al calcular los residuos
3. Se usó una recta diferente a la de mínimos cuadrados

**Solución:** Verificar los cálculos de a y b.

</details>

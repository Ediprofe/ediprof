# La Varianza

La varianza es la medida de dispersión más importante en estadística. En lugar de usar valores absolutos (como la desviación media), usa **cuadrados** de las desviaciones. Esto la hace fundamental para la teoría estadística.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la varianza y por qué se usan cuadrados
- Diferencia entre varianza poblacional y muestral
- Cómo calcularla paso a paso
- Cómo interpretarla

---

## 📊 Fórmulas de la Varianza

| Tipo | Símbolo | Fórmula |
|------|---------|---------|
| **Poblacional** | $\sigma^2$ | $\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$ |
| **Muestral** | $s^2$ | $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$ |

---

## 📖 ¿Qué es la Varianza?

> La **varianza** es el promedio de los **cuadrados** de las desviaciones respecto a la media.

### 💡 ¿Por qué elevar al cuadrado?

1. **Elimina signos negativos:** Los cuadrados son siempre positivos
2. **Penaliza más los valores extremos:** Una desviación de 10 "pesa" 100, mientras que una de 2 solo pesa 4
3. **Propiedades matemáticas:** Los cuadrados son más fáciles de manipular algebraicamente
4. **Menos valores extremos:** Es la base para la desviación estándar y muchos métodos estadísticos

---

## 📖 Varianza Poblacional

Cuando tenemos **todos** los datos de la población:

$$
\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}
$$

Donde:
- $\sigma^2$ = varianza poblacional (sigma al cuadrado)
- $\mu$ = media poblacional
- $N$ = tamaño de la población

### ⚙️ Ejemplo: Notas de toda una clase (población)

Notas de los 5 estudiantes de un seminario: 6, 7, 8, 9, 10

**Paso 1:** Calcular la media poblacional
$$
\mu = \frac{6+7+8+9+10}{5} = \frac{40}{5} = 8
$$

**Paso 2:** Calcular las desviaciones al cuadrado

| $x_i$ | $x_i - \mu$ | $(x_i - \mu)^2$ |
|-------|-------------|-----------------|
| 6 | -2 | 4 |
| 7 | -1 | 1 |
| 8 | 0 | 0 |
| 9 | 1 | 1 |
| 10 | 2 | 4 |
| **Suma** | | **10** |

**Paso 3:** Calcular la varianza
$$
\sigma^2 = \frac{10}{5} = 2
$$

---

## 📖 Varianza Muestral

Cuando tenemos una **muestra** de la población:

$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
$$

### 💡 ¿Por qué dividir entre n-1?

Se divide entre $n-1$ (llamado **grados de libertad**) para obtener un **estimador insesgado** de la varianza poblacional.

**Razón intuitiva:** Al usar la media muestral en lugar de la poblacional, "perdemos" un grado de libertad. Si conocemos $\bar{x}$ y $n-1$ datos, el último dato queda determinado.

### ⚙️ Ejemplo: Muestra de estaturas

Estaturas (cm) de 6 estudiantes seleccionados: 160, 165, 170, 175, 180, 190

**Paso 1:** Calcular la media muestral
$$
\bar{x} = \frac{160+165+170+175+180+190}{6} = \frac{1040}{6} = 173.33
$$

**Paso 2:** Calcular las desviaciones al cuadrado

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|-------|-----------------|---------------------|
| 160 | -13.33 | 177.69 |
| 165 | -8.33 | 69.39 |
| 170 | -3.33 | 11.09 |
| 175 | 1.67 | 2.79 |
| 180 | 6.67 | 44.49 |
| 190 | 16.67 | 277.89 |
| **Suma** | | **583.33** |

**Paso 3:** Calcular la varianza muestral
$$
s^2 = \frac{583.33}{6-1} = \frac{583.33}{5} = 116.67 \text{ cm}^2
$$

---

## 📖 Fórmula Alternativa (Computacional)

Para calcular más rápido:

$$
s^2 = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n-1}
$$

Esta fórmula evita calcular la media primero y es útil para cálculos manuales.

---

## 📖 Varianza con Datos Agrupados

Para tablas de frecuencias:

$$
s^2 = \frac{\sum f_i (x_i - \bar{x})^2}{n-1}
$$

### ⚙️ Ejemplo:

| $x_i$ | $f_i$ | $f_i \cdot x_i$ | $(x_i-\bar{x})^2$ | $f_i(x_i-\bar{x})^2$ |
|-------|-------|-----------------|-------------------|----------------------|
| 2 | 3 | 6 | 9 | 27 |
| 3 | 5 | 15 | 4 | 20 |
| 4 | 8 | 32 | 1 | 8 |
| 5 | 4 | 20 | 0 | 0 |
| 6 | 5 | 30 | 1 | 5 |
| 7 | 3 | 21 | 4 | 12 |
| 8 | 2 | 16 | 9 | 18 |
| **Total** | **30** | **140** | | **90** |

Media: $\bar{x} = \frac{140}{30} = 4.67 \approx 5$ (usamos 5 para simplificar)

$$
s^2 = \frac{90}{30-1} = \frac{90}{29} = 3.10
$$

---

## ⚠️ El Problema de las Unidades

La varianza tiene unidades **al cuadrado**.

### ⚙️ Ejemplo:
- Si los datos están en cm, la varianza está en cm²
- Si los datos están en pesos, la varianza está en pesos²

**Problema:** ¿Qué significa "116.67 cm²" en términos de estatura?

**Solución:** Usar la **desviación estándar** (raíz de la varianza), que tiene las mismas unidades que los datos originales.

---

## 💡 Propiedades de la Varianza

### Propiedad 1: Siempre es positiva o cero

$$
\sigma^2 \geq 0
$$

Es cero solo si todos los datos son iguales.

### Propiedad 2: Transformación lineal

Si multiplicamos todos los datos por una constante $a$:

$$
\text{Var}(aX) = a^2 \cdot \text{Var}(X)
$$

Si sumamos una constante $b$:

$$
\text{Var}(X + b) = \text{Var}(X)
$$

Sumar una constante desplaza todos los datos pero no cambia su dispersión.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Varianza** | Promedio de las desviaciones al cuadrado |
| **Poblacional** ($\sigma^2$) | Dividir entre $N$ |
| **Muestral** ($s^2$) | Dividir entre $n-1$ |
| **Unidades** | Cuadrado de las unidades originales |
| **Interpretación** | Mayor varianza = mayor dispersión |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la varianza poblacional de: 4, 6, 8, 10, 12

<details>
<summary>Ver solución</summary>

**Paso 1:** Media
$\mu = \frac{4+6+8+10+12}{5} = \frac{40}{5} = 8$

**Paso 2:** Desviaciones al cuadrado

| $x_i$ | $(x_i - 8)^2$ |
|-------|---------------|
| 4 | 16 |
| 6 | 4 |
| 8 | 0 |
| 10 | 4 |
| 12 | 16 |
| **Suma** | **40** |

**Paso 3:** Varianza poblacional
$\sigma^2 = \frac{40}{5} = 8$

</details>

### Ejercicio 2
Usando los mismos datos del Ejercicio 1, calcula la varianza muestral.

<details>
<summary>Ver solución</summary>

La suma de desviaciones al cuadrado es la misma: 40

**Varianza muestral:**
$s^2 = \frac{40}{5-1} = \frac{40}{4} = 10$

**Comparación:**
- Varianza poblacional: 8
- Varianza muestral: 10

La muestral es mayor (divide entre n-1 en lugar de n).

</details>

### Ejercicio 3
¿Por qué la varianza de (10, 10, 10, 10, 10) es cero?

<details>
<summary>Ver solución</summary>

**Cálculo:**
- Media: $\mu = 10$
- Desviaciones: $10-10=0$ para todos
- Desviaciones al cuadrado: $0^2 = 0$ para todos
- Suma: 0
- Varianza: $\frac{0}{5} = 0$

**Razón conceptual:**
La varianza mide cuánto varían los datos respecto a la media. Si todos los datos son iguales, no hay variación alguna, por lo tanto la varianza es cero.

**Regla general:** $\sigma^2 = 0$ si y solo si todos los datos son idénticos.

</details>

### Ejercicio 4
Las edades de 5 personas son: 20, 25, 30, 35, 40

a) Calcula la varianza muestral
b) Si le sumamos 10 años a cada persona, ¿cambia la varianza?
c) Si multiplicamos cada edad por 2, ¿cómo cambia la varianza?

<details>
<summary>Ver solución</summary>

a) **Varianza muestral original:**
Media: $\bar{x} = \frac{150}{5} = 30$

| $x_i$ | $(x_i - 30)^2$ |
|-------|----------------|
| 20 | 100 |
| 25 | 25 |
| 30 | 0 |
| 35 | 25 |
| 40 | 100 |
| **Suma** | **250** |

$s^2 = \frac{250}{4} = 62.5$

b) **Sumando 10 a cada edad:** (30, 35, 40, 45, 50)
Nueva media: 40
Desviaciones: -10, -5, 0, +5, +10 (¡las mismas distancias!)
Nueva varianza: **62.5** (no cambia)

**Conclusión:** Sumar constante no afecta la varianza.

c) **Multiplicando por 2:** (40, 50, 60, 70, 80)
Nueva media: 60
Desviaciones: -20, -10, 0, +10, +20 (el doble que antes)
Nueva varianza: $2^2 \times 62.5 = 4 \times 62.5 = 250$

**Conclusión:** Multiplicar por $a$ multiplica la varianza por $a^2$.

</details>

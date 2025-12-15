# Medidas para Datos Agrupados

Cuando los datos vienen organizados en tablas de frecuencias (especialmente con clases), necesitamos adaptar nuestras fórmulas. Ya no tenemos los valores individuales, pero podemos **estimar** las medidas de tendencia central usando la información disponible.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular la media con datos agrupados
- Cómo estimar la mediana con interpolación
- Cómo identificar la clase modal y estimar la moda
- Por qué solo son estimaciones

---

## 📊 Resumen de Fórmulas

| Medida | Fórmula para Datos Agrupados |
|--------|------------------------------|
| **Media** | $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$ |
| **Mediana** | $Me = L_i + \left(\frac{\frac{n}{2} - F_{ant}}{f_{med}}\right) \cdot A$ |
| **Moda** | Clase con mayor frecuencia |

Donde $x_i$ = marca de clase

---

## 📖 Datos de Ejemplo

Usaremos la siguiente tabla a lo largo de la lección:

**Estaturas de 50 estudiantes (en cm)**

| Clase | Intervalo | $x_i$ (marca) | f | F |
|-------|-----------|---------------|---|---|
| 1 | 150 - 154 | 152 | 4 | 4 |
| 2 | 155 - 159 | 157 | 9 | 13 |
| 3 | 160 - 164 | 162 | 15 | 28 |
| 4 | 165 - 169 | 167 | 12 | 40 |
| 5 | 170 - 174 | 172 | 7 | 47 |
| 6 | 175 - 179 | 177 | 3 | 50 |
| **Total** | | | **50** | |

---

## 📖 Media para Datos Agrupados

### 💡 Idea clave:
No conocemos los valores exactos, así que usamos la **marca de clase** ($x_i$) como representante de todos los valores en ese intervalo.

### 💡 Fórmula:

$$
\bar{x} = \frac{\sum f_i \cdot x_i}{n}
$$

### ⚙️ Cálculo paso a paso:

| Intervalo | $x_i$ | $f_i$ | $f_i \cdot x_i$ |
|-----------|-------|-------|-----------------|
| 150-154 | 152 | 4 | 608 |
| 155-159 | 157 | 9 | 1,413 |
| 160-164 | 162 | 15 | 2,430 |
| 165-169 | 167 | 12 | 2,004 |
| 170-174 | 172 | 7 | 1,204 |
| 175-179 | 177 | 3 | 531 |
| **Total** | | **50** | **8,190** |

$$
\bar{x} = \frac{8,190}{50} = 163.8 \text{ cm}
$$

**Interpretación:** La estatura media estimada es aproximadamente 163.8 cm.

---

## 📖 Mediana para Datos Agrupados

### 💡 Proceso:

1. **Encontrar la posición de la mediana:** $\frac{n}{2}$
2. **Identificar la clase mediana:** Donde $F \geq \frac{n}{2}$
3. **Interpolar** para obtener un valor más preciso

### 💡 Fórmula de interpolación:

$$
Me = L_i + \left(\frac{\frac{n}{2} - F_{anterior}}{f_{mediana}}\right) \cdot A
$$

Donde:
- $L_i$ = límite inferior de la clase mediana
- $F_{anterior}$ = frecuencia acumulada ANTES de la clase mediana
- $f_{mediana}$ = frecuencia de la clase mediana
- $A$ = amplitud de clase

### ⚙️ Cálculo paso a paso:

**Paso 1:** Posición de la mediana
$$
\frac{n}{2} = \frac{50}{2} = 25
$$

**Paso 2:** Identificar la clase mediana
Buscamos el primer F ≥ 25:
- F = 4 para 150-154 ❌
- F = 13 para 155-159 ❌
- F = 28 para 160-164 ✅ ← Clase mediana

**Paso 3:** Identificar valores
- $L_i = 160$ (o 159.5 si usamos límites reales)
- $F_{anterior} = 13$ (frecuencia acumulada de la clase anterior)
- $f_{mediana} = 15$
- $A = 5$

**Paso 4:** Aplicar fórmula
$$
Me = 160 + \left(\frac{25 - 13}{15}\right) \cdot 5
$$
$$
Me = 160 + \left(\frac{12}{15}\right) \cdot 5 = 160 + 0.8 \cdot 5 = 160 + 4 = 164 \text{ cm}
$$

**Interpretación:** La estatura mediana estimada es 164 cm. El 50% de los estudiantes mide menos de 164 cm.

---

## 📖 Moda para Datos Agrupados

### 💡 Proceso simple:
Identificar la **clase modal** = la clase con mayor frecuencia.

En nuestro ejemplo:

| Intervalo | f |
|-----------|---|
| 150-154 | 4 |
| 155-159 | 9 |
| **160-164** | **15** ← Máxima |
| 165-169 | 12 |
| 170-174 | 7 |
| 175-179 | 3 |

**Clase modal: 160-164 cm**

### 💡 Estimación usando la marca de clase:

$$
Mo \approx x_i = \frac{160 + 164}{2} = 162 \text{ cm}
$$

### 💡 Fórmula de interpolación (más precisa):

$$
Mo = L_i + \left(\frac{d_1}{d_1 + d_2}\right) \cdot A
$$

Donde:
- $d_1$ = $f_{modal} - f_{anterior}$ = 15 - 9 = 6
- $d_2$ = $f_{modal} - f_{siguiente}$ = 15 - 12 = 3

$$
Mo = 160 + \left(\frac{6}{6 + 3}\right) \cdot 5 = 160 + \frac{6}{9} \cdot 5 = 160 + 3.33 = 163.3 \text{ cm}
$$

---

## 📊 Resumen de Resultados

Para los datos de estaturas:

| Medida | Valor Estimado |
|--------|----------------|
| **Media** | 163.8 cm |
| **Mediana** | 164.0 cm |
| **Moda** | 163.3 cm |

### 💡 ¿Qué indica esto?

Las tres medidas son muy similares (≈163-164 cm), lo que sugiere una distribución **aproximadamente simétrica**.

---

## ⚠️ Importante: Son Estimaciones

Cuando trabajamos con datos agrupados:

1. **Perdemos precisión:** No conocemos los valores exactos dentro de cada clase
2. **Asumimos uniformidad:** La marca de clase asume que los datos están uniformemente distribuidos en cada intervalo
3. **El resultado es aproximado:** Si tuviéramos los datos originales, los valores podrían diferir ligeramente

### 💡 ¿Por qué usar datos agrupados entonces?

- **Grandes volúmenes de datos:** Más fácil de manejar
- **Datos ya agrupados:** A veces solo tenemos la tabla
- **Visualización:** Histogramas requieren datos agrupados
- **Suficiente precisión:** Para muchos propósitos, la estimación es adecuada

---

## 🔑 Resumen

| Medida | Procedimiento |
|--------|---------------|
| **Media** | Usar marcas de clase: $\bar{x} = \frac{\sum f_i \cdot x_i}{n}$ |
| **Mediana** | Interpolar en la clase que contiene la posición $\frac{n}{2}$ |
| **Moda** | Clase con mayor frecuencia (o interpolar) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la media para los siguientes datos agrupados:

| Intervalo | f |
|-----------|---|
| 10 - 20 | 5 |
| 20 - 30 | 12 |
| 30 - 40 | 18 |
| 40 - 50 | 10 |
| 50 - 60 | 5 |

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular marcas de clase y productos

| Intervalo | $x_i$ | $f_i$ | $f_i \cdot x_i$ |
|-----------|-------|-------|-----------------|
| 10-20 | 15 | 5 | 75 |
| 20-30 | 25 | 12 | 300 |
| 30-40 | 35 | 18 | 630 |
| 40-50 | 45 | 10 | 450 |
| 50-60 | 55 | 5 | 275 |
| **Total** | | **50** | **1,730** |

**Paso 2:** Calcular la media
$$\bar{x} = \frac{1,730}{50} = 34.6$$

**La media estimada es 34.6**

</details>

### Ejercicio 2
Usando la tabla del Ejercicio 1, calcula la mediana.

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular frecuencias acumuladas

| Intervalo | f | F |
|-----------|---|---|
| 10-20 | 5 | 5 |
| 20-30 | 12 | 17 |
| 30-40 | 18 | 35 |
| 40-50 | 10 | 45 |
| 50-60 | 5 | 50 |

**Paso 2:** Posición de la mediana
$\frac{n}{2} = \frac{50}{2} = 25$

**Paso 3:** Identificar clase mediana
F = 17 para 20-30 ❌
F = 35 para 30-40 ✅ ← Clase mediana

**Paso 4:** Interpolar
- $L_i = 30$
- $F_{anterior} = 17$
- $f_{mediana} = 18$
- $A = 10$

$$Me = 30 + \left(\frac{25 - 17}{18}\right) \cdot 10 = 30 + \frac{8}{18} \cdot 10$$
$$Me = 30 + 0.444 \cdot 10 = 30 + 4.44 = 34.4$$

**La mediana estimada es 34.4**

</details>

### Ejercicio 3
Usando la tabla del Ejercicio 1:
a) ¿Cuál es la clase modal?
b) Estima la moda usando la marca de clase
c) Compara la media, mediana y moda. ¿Qué tipo de distribución sugiere?

<details>
<summary>Ver solución</summary>

a) **Clase modal:** 30-40 (frecuencia 18, la mayor)

b) **Moda estimada (marca de clase):**
$$Mo = \frac{30 + 40}{2} = 35$$

c) **Comparación:**
- Media ≈ 34.6
- Mediana ≈ 34.4
- Moda ≈ 35

**Las tres medidas son muy similares (34-35), lo que sugiere una distribución aproximadamente SIMÉTRICA.**

En una distribución simétrica: Media ≈ Mediana ≈ Moda ✓

</details>

### Ejercicio 4
¿Por qué la media calculada con datos agrupados es solo una "estimación" y no el valor exacto?

<details>
<summary>Ver solución</summary>

La media con datos agrupados es una estimación porque:

1. **Perdemos información:** Al agrupar, no sabemos los valores exactos dentro de cada clase.

2. **Usamos la marca de clase:** Asumimos que todos los valores de una clase son iguales al punto medio, pero esto no es necesariamente cierto.

3. **Ejemplo:** En la clase 30-40, podría haber valores como 31, 32, 38, 39 (asimétricos) o 34, 35, 36 (centrados). Usamos 35 para todos.

4. **El error depende de la distribución real:** Si los datos dentro de cada clase están centrados en la marca, la estimación es buena. Si están concentrados en un extremo, hay más error.

**Conclusión:** La estimación es útil y generalmente cercana al valor real, pero si necesitas exactitud total, debes trabajar con los datos originales no agrupados.

</details>

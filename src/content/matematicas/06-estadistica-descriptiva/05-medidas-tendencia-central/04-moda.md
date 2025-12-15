# La Moda

¿Cuál es la talla de zapato más vendida? ¿Cuál es el color de carro más popular? ¿Cuál es la nota más común en el examen? Estas preguntas se responden con la **moda**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la moda y cómo encontrarla
- Distribuciones unimodales, bimodales y multimodales
- Cómo encontrar la moda en tablas y datos agrupados
- Cuándo es más útil que la media o mediana

---

## 📊 Tipos de Distribuciones según la Moda

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Unimodal** | Una sola moda | Notas: 7, 8, **8**, 8, 9 → Moda = 8 |
| **Bimodal** | Dos modas | Tallas: S, **M**, L, **M**, **L**, XL → Modas = M y L |
| **Multimodal** | Tres o más modas | Poco común |
| **Amodal** | Sin moda (todos diferentes) | Edades: 15, 16, 17, 18, 19 → Sin moda |

---

## 📖 Definición de la Moda

> La **moda** (Mo) es el valor que aparece con **mayor frecuencia** en un conjunto de datos.

### 💡 Características:
- Es el valor **más repetido**
- Puede existir más de una moda
- Puede no existir (si todos los valores son diferentes)
- Funciona tanto para datos cuantitativos como cualitativos

---

## 📖 Encontrar la Moda: Datos Simples

### ⚙️ Ejemplo 1: Unimodal

Notas de 10 estudiantes: 7, 8, 6, 8, 9, 8, 7, 10, 8, 6

**Conteo:**
| Nota | Frecuencia |
|------|------------|
| 6 | 2 |
| 7 | 2 |
| **8** | **4** ← máximo |
| 9 | 1 |
| 10 | 1 |

**Moda = 8** (aparece 4 veces, más que cualquier otro)

### ⚙️ Ejemplo 2: Bimodal

Edades: 20, 22, 22, 25, 25, 25, 28, 28, 28, 30

**Conteo:**
| Edad | Frecuencia |
|------|------------|
| 20 | 1 |
| 22 | 2 |
| **25** | **3** |
| **28** | **3** |
| 30 | 1 |

**Modas = 25 y 28** (ambas con frecuencia 3)

### ⚙️ Ejemplo 3: Amodal

Datos: 1, 2, 3, 4, 5, 6, 7

Cada valor aparece exactamente 1 vez → **No hay moda**

---

## 📖 Moda para Datos Cualitativos

La moda es la **única** medida de tendencia central que funciona con datos cualitativos.

### ⚙️ Ejemplo: Colores favoritos

| Color | Votos |
|-------|-------|
| Azul | 15 |
| Rojo | 8 |
| **Verde** | **22** |
| Amarillo | 5 |

**Moda = Verde** (es el color con más votos)

❌ No podemos calcular la media de colores (¿qué es "azul + rojo ÷ 2"?)
❌ No podemos ordenar colores para encontrar la mediana
✅ Pero sí podemos encontrar el más frecuente

---

## 📖 Moda con Tabla de Frecuencias

Es muy fácil: busca la frecuencia más alta y el valor correspondiente.

### ⚙️ Ejemplo

| Número de hijos | Frecuencia |
|-----------------|------------|
| 0 | 5 |
| 1 | 12 |
| **2** | **18** ← máximo |
| 3 | 10 |
| 4 | 5 |

**Moda = 2 hijos** (frecuencia 18, la mayor)

---

## 📖 Moda con Datos Agrupados: Clase Modal

Para datos agrupados, identificamos la **clase modal** (la clase con mayor frecuencia).

### ⚙️ Ejemplo: Pesos de estudiantes

| Intervalo | Frecuencia |
|-----------|------------|
| 52 - 58 | 7 |
| 59 - 65 | 8 |
| **66 - 72** | **9** ← máximo |
| 73 - 79 | 8 |
| 80 - 86 | 4 |
| 87 - 93 | 4 |

**Clase modal = 66 - 72 kg**

### 💡 Estimación de la moda exacta

Podemos estimar un valor más preciso usando la **marca de clase**:

$$
\text{Moda} \approx \text{Marca de clase modal} = \frac{66 + 72}{2} = 69 \text{ kg}
$$

### 💡 Fórmula de interpolación (opcional)

Para mayor precisión:

$$
Mo = L_i + \left( \frac{d_1}{d_1 + d_2} \right) \times A
$$

Donde:
- $L_i$ = límite inferior de la clase modal
- $d_1$ = frecuencia modal - frecuencia clase anterior
- $d_2$ = frecuencia modal - frecuencia clase siguiente
- $A$ = amplitud de clase

---

## 📖 Interpretación Visual

En un histograma o polígono de frecuencias, la moda está en el **pico** (la barra más alta).

### Distribución unimodal:
```
      ▄█▄
    ▄█████▄
  ▄█████████▄
```
Un solo pico → una moda

### Distribución bimodal:
```
  ▄▄▄     ▄▄▄
 █████   █████
███████ ███████
```
Dos picos → dos modas

---

## 💡 ¿Cuándo Usar la Moda?

| Situación | ¿Usar moda? | Razón |
|-----------|-------------|-------|
| Datos cualitativos | ✅ Sí | Es la única opción |
| Buscar lo más popular/típico | ✅ Sí | Es exactamente lo que mide |
| Datos numéricos simétricos | ⚠️ Opcional | Media o mediana suelen ser mejores |
| Decisiones comerciales | ✅ Sí | ¿Qué talla producir más? |

### ⚙️ Ejemplo práctico: Taller de zapatos

Un taller necesita producir zapatos. ¿Qué talla producir más?

| Talla | Demanda |
|-------|---------|
| 36 | 50 |
| 37 | 80 |
| **38** | **150** |
| 39 | 100 |
| 40 | 70 |

**Moda = Talla 38** → Producir más zapatos de esta talla.

La media (38.something) no tiene sentido práctico porque no produces "talla 38.3".

---

## 📖 Relación Moda-Media-Mediana en Distribuciones Sesgadas

| Distribución | Orden de izq. a der. |
|--------------|---------------------|
| Sesgada a la derecha | Moda < Mediana < Media |
| Simétrica | Moda = Mediana = Media |
| Sesgada a la izquierda | Media < Mediana < Moda |

### 💡 Regla empírica (aproximación de Pearson):

$$
\text{Media} - \text{Moda} \approx 3 \times (\text{Media} - \text{Mediana})
$$

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Moda** | Valor que más se repite |
| **Unimodal** | Una sola moda |
| **Bimodal** | Dos modas |
| **Amodal** | Sin moda (todos diferentes) |
| **Uso principal** | Datos cualitativos o encontrar lo más común |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la moda de los siguientes conjuntos:

a) 5, 7, 8, 7, 9, 7, 6, 8, 7
b) 10, 20, 30, 40, 50
c) A, B, B, C, C, C, D, D
d) 2, 2, 3, 3, 4, 4

<details>
<summary>Ver solución</summary>

a) **Datos: 5, 7, 8, 7, 9, 7, 6, 8, 7**
Conteo: 5(1), 6(1), 7(4), 8(2), 9(1)
**Moda = 7** (unimodal)

b) **Datos: 10, 20, 30, 40, 50**
Cada valor aparece 1 vez
**Sin moda** (amodal)

c) **Datos: A, B, B, C, C, C, D, D**
Conteo: A(1), B(2), C(3), D(2)
**Moda = C** (unimodal)

d) **Datos: 2, 2, 3, 3, 4, 4**
Conteo: 2(2), 3(2), 4(2)
**Modas = 2, 3 y 4** (multimodal, las tres tienen la misma frecuencia)

</details>

### Ejercicio 2
En una encuesta sobre marca de celular favorita:

| Marca | Votos |
|-------|-------|
| Apple | 45 |
| Samsung | 52 |
| Xiaomi | 38 |
| Huawei | 25 |
| Otros | 40 |

a) ¿Cuál es la moda?
b) ¿Por qué no usamos media o mediana aquí?

<details>
<summary>Ver solución</summary>

a) **Moda = Samsung** (52 votos, la mayor frecuencia)

b) **No usamos media ni mediana porque:**
- Las marcas son datos **cualitativos** (nominales)
- No podemos sumar "Apple + Samsung" para calcular media
- No podemos ordenar marcas para encontrar mediana
- La moda es la **única** medida de tendencia central aplicable a datos nominales

</details>

### Ejercicio 3
La siguiente tabla muestra ventas de camisetas por talla:

| Talla | Frecuencia |
|-------|------------|
| XS | 15 |
| S | 42 |
| M | 68 |
| L | 55 |
| XL | 30 |
| XXL | 10 |

a) ¿Cuál es la moda?
b) Si la tienda solo puede destacar UNA talla en su vitrina, ¿cuál debería ser?

<details>
<summary>Ver solución</summary>

a) **Moda = M** (frecuencia 68, la mayor)

b) **Talla M** debería ir en la vitrina porque:
- Es la más demandada (moda)
- Maximiza las posibilidades de venta por exposición
- Representa al cliente "típico" de la tienda

</details>

### Ejercicio 4
Explica por qué una distribución bimodal podría indicar que los datos provienen de dos grupos diferentes.

<details>
<summary>Ver solución</summary>

Una distribución **bimodal** (dos picos) sugiere dos grupos porque:

**Cada grupo tiene su propio "centro":**
- Grupo 1 tiene su moda en el primer pico
- Grupo 2 tiene su moda en el segundo pico

**Ejemplo 1: Estaturas**
Si mezclamos hombres y mujeres:
- Pico 1: ~163 cm (moda de mujeres)
- Pico 2: ~175 cm (moda de hombres)

**Ejemplo 2: Tiempos de llegada**
Restaurante con dos turnos de comida:
- Pico 1: 12:30 pm (almuerzo)
- Pico 2: 7:30 pm (cena)

**Implicación:**
Cuando vemos un histograma bimodal, debemos preguntarnos:
"¿Hay dos poblaciones mezcladas que deberían analizarse por separado?"

</details>

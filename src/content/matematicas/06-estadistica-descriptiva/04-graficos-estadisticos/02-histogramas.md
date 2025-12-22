# Histogramas

¿Qué gráfico usamos cuando tenemos datos **continuos** como pesos, estaturas o tiempos? El diagrama de barras no funciona bien porque cada valor sería diferente.

La respuesta es el **histograma**: el gráfico más importante para datos cuantitativos continuos.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un histograma y cómo se diferencia del diagrama de barras
- Cómo construir un histograma paso a paso
- Cómo interpretar la forma de un histograma
- Identificar distribuciones simétricas y sesgadas

---

## 📊 Comparación: Histograma vs Diagrama de Barras

| Aspecto | Diagrama de Barras | Histograma |
|---------|-------------------|------------|
| **Datos** | Cualitativos o discretos | Cuantitativos continuos |
| **Barras** | Separadas | **Juntas** (sin espacio) |
| **Eje X** | Categorías | Intervalos numéricos |
| **Altura** | Frecuencia | Frecuencia |
| **Ancho** | Igual para todas | Igual para todas (amplitud de clase) |

---

## 📖 ¿Qué es un Histograma?

> Un **histograma** es un gráfico de barras **adyacentes** (pegadas) donde cada barra representa un intervalo de valores y su altura indica la frecuencia de ese intervalo.

### 💡 Características clave:
- Las barras están **pegadas** (sin espacio entre ellas)
- Cada barra representa una **clase** de la tabla de frecuencias
- La **altura** es la frecuencia de esa clase
- El **ancho** es la amplitud de clase (igual para todas)

---

## 📖 Construcción del Histograma

### ⚙️ Ejemplo: Pesos de 40 estudiantes

Usemos la tabla de frecuencias de la lección anterior:

| Clase | Intervalo | f |
|-------|-----------|---|
| 1 | 52 - 58 | 7 |
| 2 | 59 - 65 | 8 |
| 3 | 66 - 72 | 9 |
| 4 | 73 - 79 | 8 |
| 5 | 80 - 86 | 4 |
| 6 | 87 - 93 | 4 |

### Paso 1: Preparar los ejes

- **Eje X (horizontal):** Los intervalos de peso (52 a 93 kg)
- **Eje Y (vertical):** La frecuencia (0 a 10 o más)

### Paso 2: Dibujar las barras

Para cada clase:
1. La barra empieza en el límite inferior
2. La barra termina en el límite superior
3. La altura es igual a la frecuencia

| Barra | Desde | Hasta | Altura |
|-------|-------|-------|--------|
| 1 | 52 | 58 | 7 |
| 2 | 59 | 65 | 8 |
| 3 | 66 | 72 | 9 |
| 4 | 73 | 79 | 8 |
| 5 | 80 | 86 | 4 |
| 6 | 87 | 93 | 4 |

### Paso 3: Las barras deben estar pegadas

A diferencia del diagrama de barras, **no hay espacio** entre las barras del histograma. Esto refleja que los datos son continuos.

![Histograma de Pesos](/images/funciones/estadistica/histograma-pesos.svg)

---

## 📖 Interpretación del Histograma

Un histograma nos cuenta una historia sobre los datos. Miremos qué formas pueden tener:

### 💡 Distribución Simétrica (Campana)

![Distribución Simétrica](/images/funciones/estadistica/distribucion-simetrica.svg)

**Características:**
- Los datos se concentran en el centro
- La cola izquierda es igual a la derecha
- Media ≈ Mediana ≈ Moda
- **Ejemplo:** Estaturas de adultos, errores de medición

### 💡 Distribución Sesgada a la Derecha (Positiva)

![Distribución Sesgada a la Derecha](/images/funciones/estadistica/distribucion-sesgada-derecha.svg)

**Características:**
- La mayoría de los datos están a la izquierda
- Hay una "cola" larga hacia la derecha
- Media > Mediana > Moda
- **Ejemplo:** Ingresos (pocos ganan mucho), tiempos de espera

### 💡 Distribución Sesgada a la Izquierda (Negativa)

![Distribución Sesgada a la Izquierda](/images/funciones/estadistica/distribucion-sesgada-izquierda.svg)

**Características:**
- La mayoría de los datos están a la derecha
- Hay una "cola" larga hacia la izquierda
- Media < Mediana < Moda
- **Ejemplo:** Edad de jubilación, notas en un examen fácil

### 💡 Distribución Uniforme

![Distribución Uniforme](/images/funciones/estadistica/distribucion-uniforme.svg)

**Características:**
- Todas las barras tienen aproximadamente la misma altura
- Los datos están distribuidos equitativamente
- **Ejemplo:** Números de lotería, lanzamiento de dado justo

### 💡 Distribución Bimodal

![Distribución Bimodal](/images/funciones/estadistica/distribucion-bimodal.svg)

**Características:**
- Hay **dos picos** en el histograma
- Podría indicar dos grupos diferentes mezclados
- **Ejemplo:** Estaturas si mezclas hombres y mujeres, tiempos de llegada en hora pico

---

## 📖 ¿Por qué las Barras están Pegadas?

Esta es la diferencia **conceptual** más importante:

| Diagrama de Barras | Histograma |
|-------------------|------------|
| Las categorías son **independientes** | Los intervalos son **continuos** |
| "Bus" y "Metro" son diferentes | 52-58 kg y 59-65 kg son consecutivos |
| No hay nada "entre" las categorías | Entre 58 y 59 hay valores posibles |
| Separarlas tiene sentido | Separarlas sería incorrecto |

Las barras pegadas representan que los datos son **continuos**: un peso de 58.5 kg cae entre dos clases, no hay "vacío" entre ellas.

---

## 📖 El Histograma y el Área

> En un histograma, el **área** de cada barra es proporcional a la frecuencia de esa clase.

### 💡 Fórmula:

$$
\text{Área de la barra} = \text{Amplitud} \times \text{Altura} = A \times f
$$

Si todas las clases tienen la misma amplitud (lo más común), entonces la altura sola representa bien la frecuencia.

### ⚠️ Cuidado con clases de diferente amplitud

Si las clases tienen **amplitudes diferentes**, solo mirar la altura puede ser engañoso. En ese caso se usa la **densidad de frecuencia**:

$$
\text{Densidad} = \frac{f}{A}
$$

Esto ajusta la altura para que las áreas sean comparables.

---

## 💡 Lectura del Histograma: Preguntas que Podemos Responder

| Pregunta | Cómo responderla |
|----------|------------------|
| ¿Dónde se concentran los datos? | Buscar las barras más altas |
| ¿Hay valores extremos? | Mirar las colas (barras en los extremos) |
| ¿Los datos son simétricos? | Comparar forma izquierda vs derecha |
| ¿Cuántos datos hay en un rango? | Sumar las alturas de las barras en ese rango |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Histograma** | Gráfico de barras adyacentes para datos continuos |
| **Barras pegadas** | Reflejan la continuidad de los datos |
| **Altura de barras** | Representa la frecuencia de cada clase |
| **Forma del histograma** | Indica si la distribución es simétrica, sesgada, etc. |
| **Sesgo a la derecha** | Cola larga hacia valores altos |
| **Sesgo a la izquierda** | Cola larga hacia valores bajos |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Dada la siguiente tabla de frecuencias de tiempos de espera (en minutos):

| Intervalo | f |
|-----------|---|
| 0 - 4 | 8 |
| 5 - 9 | 15 |
| 10 - 14 | 12 |
| 15 - 19 | 5 |
| 20 - 24 | 3 |

a) ¿Cuál sería la forma probable del histograma?
b) ¿La distribución es simétrica o sesgada? ¿Hacia dónde?
c) ¿Dónde se concentra la mayoría de los datos?

<details>
<summary>Ver solución</summary>

a) **Forma probable:**
- La barra más alta es 5-9 (f=15)
- Las barras disminuyen hacia la derecha
- Forma: concentrada a la izquierda con cola a la derecha

b) **Distribución sesgada a la derecha (positiva)**
- La mayoría espera poco tiempo (5-9 min)
- Pocos esperan mucho (20-24 min)
- La cola larga está hacia los valores altos

c) **Concentración:**
- La mayoría de los datos están en 5-9 minutos
- El 58% espera menos de 10 minutos: (8+15)/43 = 53%
- Esperar más de 15 minutos es raro: solo 8 de 43 (19%)

</details>

### Ejercicio 2
¿Por qué las barras de un histograma deben estar pegadas pero las de un diagrama de barras deben estar separadas?

<details>
<summary>Ver solución</summary>

**Histograma (barras pegadas):**
- Representa datos **continuos**
- No hay "vacíos" entre los valores
- Un peso de 58.5 kg existe entre 52-58 y 59-65
- Las barras pegadas muestran que los intervalos son **consecutivos**

**Diagrama de barras (barras separadas):**
- Representa datos **categóricos** o discretos
- Las categorías son **independientes**
- No hay nada "entre" Bus y Metro
- Las barras separadas refuerzan que son **categorías distintas**

**Regla:** Si el eje X tiene valores que pueden ser cualquier número en un rango → Histograma (barras pegadas).

</details>

### Ejercicio 3
Un histograma de las notas de un examen tiene esta forma:

```
           ▄█
          ▄██
         ▄███
        ▄████
▄▄▄▄▄▄▄█████
```

a) ¿Cómo describirías esta distribución?
b) ¿Fue un examen fácil o difícil? ¿Por qué?
c) ¿La media sería mayor, menor o igual que la mediana?

<details>
<summary>Ver solución</summary>

a) **Distribución sesgada a la izquierda (negativa)**
- La mayoría de los datos están a la derecha (notas altas)
- Hay una cola larga hacia la izquierda (notas bajas)

b) **Fue un examen relativamente fácil**
- La mayoría de los estudiantes sacó notas altas
- Pocos estudiantes sacaron notas bajas
- La barra más alta está en el extremo derecho (notas altas)

c) **La media sería MENOR que la mediana**
- En distribuciones sesgadas a la izquierda:
- La cola de valores bajos "jala" la media hacia abajo
- La mediana está más a la derecha porque divide los datos en mitades
- Orden: Media < Mediana < Moda

</details>

### Ejercicio 4
Un investigador mezcló datos de estaturas de hombres y mujeres en un solo histograma y obtuvo una forma bimodal (dos picos). ¿Por qué ocurre esto?

<details>
<summary>Ver solución</summary>

La forma **bimodal** (dos picos) ocurre porque:

1. **Hay dos poblaciones mezcladas:** Hombres y mujeres tienen distribuciones de estatura diferentes.

2. **Cada grupo tiene su propia "moda":**
   - Mujeres: pico alrededor de 160-165 cm
   - Hombres: pico alrededor de 170-175 cm

3. **Al juntarlos:** Se ven los dos picos en el histograma

4. **Implicación:** Un histograma bimodal sugiere que los datos podrían provenir de **dos grupos diferentes** que deberían analizarse por separado.

**Solución:** Hacer histogramas separados para hombres y mujeres, o usar una variable de agrupación en el análisis.

</details>

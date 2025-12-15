# Introducción a los Promedios

Cuando alguien te pregunta *"¿Cómo te fue en el semestre?"*, probablemente respondes con tu promedio de notas. Pero ¿sabías que hay **más de una forma** de encontrar el "centro" de un conjunto de datos?

En esta lección exploraremos por qué buscamos el centro y qué opciones tenemos para calcularlo.

---

## 🎯 ¿Qué vas a aprender?

- Qué significan las "medidas de tendencia central"
- Por qué es útil resumir datos con un solo número
- Los tres principales "promedios": media, mediana y moda
- Cuándo usar cada uno

---

## 📊 Los Tres Promedios

| Medida | ¿Qué calcula? | Mejor para... |
|--------|---------------|---------------|
| **Media** | Suma total dividida entre cantidad | Datos sin valores extremos |
| **Mediana** | Valor que divide los datos en dos mitades | Datos con valores extremos |
| **Moda** | Valor que más se repite | Datos categóricos o encontrar lo "típico" |

---

## 📖 ¿Qué es el "Centro" de los Datos?

> Las **medidas de tendencia central** son valores que representan el **punto típico** o **central** de un conjunto de datos.

### 💡 ¿Por qué buscar el centro?

Imagina que tienes las notas de 100 estudiantes. ¿Cómo resumirías toda esa información en una sola frase?

- ❌ "Las notas fueron 7, 8, 6, 9, 7, 8, 5, 10, 6, 7, 8, 9, 7, 6, 8..." (nadie quiere escuchar 100 números)
- ✅ "El promedio fue 7.5" (un solo número que resume todo)

### 💡 El centro es un resumen

El valor central:
- Representa a todo el grupo
- Facilita comparaciones
- Simplifica la comunicación

---

## 📖 Las Tres Formas de Encontrar el Centro

### 🔹 Media (Promedio Aritmético)

> La **media** es la suma de todos los valores dividida entre la cantidad de valores.

**Fórmula:**
$$
\bar{x} = \frac{\text{suma de todos los valores}}{\text{cantidad de valores}} = \frac{\sum x}{n}
$$

**Ejemplo rápido:**
Notas: 7, 8, 6, 9, 10
$$
\bar{x} = \frac{7 + 8 + 6 + 9 + 10}{5} = \frac{40}{5} = 8
$$

### 🔹 Mediana

> La **mediana** es el valor que está **justo en el medio** cuando los datos están ordenados.

**Ejemplo rápido:**
Notas ordenadas: 6, 7, 8, 9, 10

El valor del medio es **8** (hay 2 valores a la izquierda y 2 a la derecha).

### 🔹 Moda

> La **moda** es el valor que **más se repite**.

**Ejemplo rápido:**
Notas: 7, 8, 7, 9, 7, 10, 8, 7

El 7 aparece 4 veces (más que cualquier otro). La moda es **7**.

---

## 💡 ¿Por qué Hay Tres Promedios?

Porque **no siempre funcionan igual**. Veamos un ejemplo dramático:

### ⚙️ Ejemplo: Ingresos de 5 personas

| Persona | Ingreso mensual |
|---------|-----------------|
| Ana | $1,500,000 |
| Luis | $1,800,000 |
| María | $2,000,000 |
| Carlos | $1,700,000 |
| Jeff (CEO) | $50,000,000 |

**Calculemos:**

**Media:**
$$
\bar{x} = \frac{1.5 + 1.8 + 2.0 + 1.7 + 50}{5} = \frac{57}{5} = 11.4 \text{ millones}
$$

**Mediana:**
Ordenando: 1.5, 1.7, 1.8, 2.0, 50.0
El valor del medio es **1.8 millones**

**Moda:**
Ningún valor se repite → No hay moda

### 💡 ¿Cuál es mejor?

- La **media** (11.4 millones) sugiere que el ingreso "típico" es altísimo. ❌ ¡Pero 4 de 5 personas ganan mucho menos!
- La **mediana** (1.8 millones) representa mejor al grupo típico. ✅

**Lección:** Un valor extremo (como el ingreso de Jeff) "jala" la media pero no afecta la mediana.

---

## 📖 ¿Cuándo Usar Cada Medida?

| Medida | Usar cuando... | No usar cuando... |
|--------|----------------|-------------------|
| **Media** | Los datos son simétricos, sin extremos | Hay valores extremos (outliers) |
| **Mediana** | Hay valores extremos o la distribución es sesgada | Los datos son simétricos (aunque funciona) |
| **Moda** | Quieres saber lo más frecuente o común | Los datos son todos diferentes |

### ⚙️ Ejemplos por contexto

| Contexto | Mejor medida | Razón |
|----------|--------------|-------|
| Notas de un examen | Media | Generalmente simétrico |
| Ingresos de un país | Mediana | Hay multimillonarios que distorsionan |
| Talla de ropa más vendida | Moda | Queremos la más común |
| Tiempo de espera | Mediana | Algunos esperan muuucho tiempo |
| Temperatura promedio | Media | Datos continuos sin extremos raros |

---

## 📖 Visualizando el Centro

En un histograma o gráfico:

### Distribución Simétrica
```
    ▄▄▄
  ▄█████▄
▄█████████▄
```
**Media ≈ Mediana ≈ Moda** (los tres coinciden en el centro)

### Distribución Sesgada a la Derecha
```
█▄
██▄
████▄▄▄
```
**Moda < Mediana < Media** (la media se va hacia la cola)

### Distribución Sesgada a la Izquierda
```
       ▄█
      ▄██
▄▄▄▄████
```
**Media < Mediana < Moda** (la media se va hacia la cola)

---

## 💡 Analogía: El Punto de Equilibrio

Imagina los datos como objetos en una balanza:

- La **media** es el punto donde la balanza se equilibra
- Si hay un objeto muy pesado en un extremo (valor extremo), el punto de equilibrio se mueve hacia allá
- La **mediana** es el punto que divide los objetos en dos grupos iguales (sin importar el peso)

---

## 🔑 Resumen

| Medida | Cálculo | Fortaleza | Debilidad |
|--------|---------|-----------|-----------|
| **Media** | $\frac{\sum x}{n}$ | Usa todos los datos | Sensible a extremos |
| **Mediana** | Valor central | Resistente a extremos | Ignora la magnitud |
| **Moda** | Más frecuente | Funciona con categóricas | Puede no existir |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Sin calcular, indica cuál medida (media, mediana o moda) sería más apropiada para:

a) El precio típico de las casas en un barrio donde hay una mansión de $5,000 millones
b) El color de carro más popular
c) El tiempo promedio que tarda un estudiante en resolver un ejercicio (todos tardan tiempos similares)

<details>
<summary>Ver solución</summary>

a) **Mediana** - La mansión de $5,000 millones es un valor extremo que distorsionaría la media

b) **Moda** - El color es una variable cualitativa; buscamos el más frecuente

c) **Media** - Si los tiempos son similares (sin extremos), la media representa bien al grupo

</details>

### Ejercicio 2
Las edades de 7 personas son: 22, 25, 23, 24, 25, 26, 85

a) Calcula la media
b) Calcula la mediana
c) ¿Cuál representa mejor al grupo? ¿Por qué?

<details>
<summary>Ver solución</summary>

a) **Media:**
$$\bar{x} = \frac{22 + 25 + 23 + 24 + 25 + 26 + 85}{7} = \frac{230}{7} = 32.9 \text{ años}$$

b) **Mediana:**
Ordenados: 22, 23, 24, **25**, 25, 26, 85
El valor del medio (posición 4) es **25 años**

c) **La mediana (25 años) representa mejor al grupo** porque:
- 6 de 7 personas tienen entre 22-26 años
- Una persona de 85 años es un valor extremo (outlier)
- La media (32.9 años) sugiere un grupo más viejo de lo que realmente es
- La mediana ignora el extremo y muestra la edad "típica"

</details>

### Ejercicio 3
En una distribución simétrica perfecta, ¿qué relación hay entre la media, la mediana y la moda?

<details>
<summary>Ver solución</summary>

En una distribución **simétrica perfecta**:

$$\text{Media} = \text{Mediana} = \text{Moda}$$

Las tres medidas **coinciden** en el mismo valor, que está exactamente en el centro de la distribución.

**Razón:**
- La simetría significa que hay igual "peso" a ambos lados del centro
- El punto de equilibrio (media), el punto medio (mediana) y el pico (moda) están todos en el mismo lugar

</details>

### Ejercicio 4
¿Por qué las noticias sobre ingresos suelen reportar la "mediana del ingreso" en lugar del "promedio del ingreso"?

<details>
<summary>Ver solución</summary>

Las noticias usan la **mediana** del ingreso porque:

1. **Distribución sesgada:** Los ingresos tienen una "cola" larga hacia valores altos (hay pocos multimillonarios, pero ganan muchísimo)

2. **Extremos distorsionantes:** Si un CEO gana 1000 veces más que el trabajador promedio, solo con él ya se eleva mucho la media

3. **La mediana es más representativa:** Indica cuánto gana la persona "típica" (la del medio)

4. **Ejemplo:** Si la media es $3,000,000 pero la mediana es $1,500,000, significa que:
   - La mitad de la población gana menos de $1,500,000
   - Los altos ingresos de pocos "jalan" la media hacia arriba
   - La mediana refleja mejor la realidad de la mayoría

</details>

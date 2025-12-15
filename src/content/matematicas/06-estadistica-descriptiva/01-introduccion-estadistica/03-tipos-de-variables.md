# Tipos de Variables

¿Sabías que no todas las variables son iguales? El color de ojos y la estatura son ambas "variables", pero **se tratan de forma muy diferente** en estadística.

Saber clasificar las variables es **fundamental** porque determina qué tipo de gráficos, tablas y cálculos puedes hacer con ellas.

---

## 🎯 ¿Qué vas a aprender?

- La diferencia entre variables cualitativas y cuantitativas
- Qué son las variables discretas y continuas
- Cómo clasificar cualquier variable correctamente

---

## 📊 Mapa de Clasificación

| Tipo Principal | Subtipo | Define | Ejemplo |
|----------------|---------|--------|---------|
| **Cualitativa** | Nominal | Categorías sin orden | Color de ojos |
| **Cualitativa** | Ordinal | Categorías con orden | Nivel educativo |
| **Cuantitativa** | Discreta | Números que se cuentan | Número de hijos |
| **Cuantitativa** | Continua | Números que se miden | Peso, estatura |

---

## 📖 Variables Cualitativas (Categóricas)

> Las **variables cualitativas** expresan **cualidades o categorías**, no números. También se llaman **categóricas**.

### 💡 Características:
- Sus valores son **categorías o etiquetas**
- No tiene sentido calcular promedios con ellas
- Se analizan contando **frecuencias** (cuántos hay en cada categoría)

---

### 📖 Cualitativas Nominales

> Las variables **nominales** son categorías **sin orden** natural entre ellas.

### ⚙️ Ejemplos:

| Variable | Posibles valores | ¿Hay orden? |
|----------|-----------------|-------------|
| Color de ojos | Café, negro, verde, azul | ❌ No (ningún color es "mayor" que otro) |
| Género | Masculino, femenino, otro | ❌ No |
| Tipo de sangre | A, B, AB, O | ❌ No |
| Estado civil | Soltero, casado, divorciado | ❌ No |
| País de nacimiento | Colombia, México, Perú... | ❌ No |

### 💡 Prueba rápida
Pregúntate: ¿Puedo decir que una categoría es "mayor" o "mejor" que otra de forma objetiva?
- Si la respuesta es **NO** → Nominal

---

### 📖 Cualitativas Ordinales

> Las variables **ordinales** son categorías **con un orden** natural entre ellas.

### ⚙️ Ejemplos:

| Variable | Posibles valores | ¿Hay orden? |
|----------|-----------------|-------------|
| Nivel educativo | Primaria < Secundaria < Universidad | ✅ Sí |
| Satisfacción | Muy malo < Malo < Regular < Bueno < Excelente | ✅ Sí |
| Talla de ropa | XS < S < M < L < XL | ✅ Sí |
| Grado escolar | 1° < 2° < 3° < ... < 11° | ✅ Sí |
| Nivel socioeconómico | Bajo < Medio < Alto | ✅ Sí |

### 💡 Prueba rápida
Pregúntate: ¿Puedo ordenar las categorías de menor a mayor (o peor a mejor)?
- Si la respuesta es **SÍ** → Ordinal

### ⚠️ Cuidado
Aunque las variables ordinales tienen orden, **no podemos medir la distancia** entre categorías.

Por ejemplo, la diferencia entre "Malo" y "Regular" no es necesariamente la misma que entre "Bueno" y "Excelente".

---

## 📖 Variables Cuantitativas (Numéricas)

> Las **variables cuantitativas** expresan **cantidades** mediante números. También se llaman **numéricas**.

### 💡 Características:
- Sus valores son **números**
- Tiene sentido calcular promedios, sumas, etc.
- Se pueden comparar matemáticamente (mayor, menor, diferencias)

---

### 📖 Cuantitativas Discretas

> Las variables **discretas** solo pueden tomar valores **enteros o contables**. Generalmente provienen de **contar**.

### ⚙️ Ejemplos:

| Variable | Posibles valores | ¿Por qué es discreta? |
|----------|-----------------|----------------------|
| Número de hijos | 0, 1, 2, 3, 4... | No puedes tener 2.5 hijos |
| Número de carros | 0, 1, 2, 3... | No puedes tener 1.7 carros |
| Goles en un partido | 0, 1, 2, 3... | No puedes anotar medio gol |
| Estudiantes en un salón | 25, 30, 35... | No hay "medio estudiante" |
| Número de materias reprobadas | 0, 1, 2, 3... | Son enteros |

### 💡 Palabra clave: **CONTAR**
Si la variable responde a "¿Cuántos hay?" y la respuesta siempre es un número entero → **Discreta**

---

### 📖 Cuantitativas Continuas

> Las variables **continuas** pueden tomar **cualquier valor** dentro de un intervalo, incluyendo decimales. Generalmente provienen de **medir**.

### ⚙️ Ejemplos:

| Variable | Posibles valores | ¿Por qué es continua? |
|----------|-----------------|----------------------|
| Estatura | 1.65 m, 1.734 m, 1.80 m... | Puede tomar cualquier valor |
| Peso | 65.3 kg, 70.125 kg... | Puede tener infinitos decimales |
| Temperatura | 36.5°C, 37.2°C... | Medición continua |
| Tiempo de carrera | 10.45 s, 10.456 s... | Depende de la precisión |
| Ingreso mensual | $1,500,000.50 | Puede tener centavos |

### 💡 Palabra clave: **MEDIR**
Si la variable responde a "¿Cuánto mide/pesa/dura?" y puede tener decimales → **Continua**

---

## 💡 El Truco Definitivo

Para clasificar cualquier variable, sigue este flujo:

```
¿Es un número que tiene sentido sumar/promediar?
│
├── NO → CUALITATIVA
│   └── ¿Tiene orden natural?
│       ├── NO → Nominal (color de ojos)
│       └── SÍ → Ordinal (nivel educativo)
│
└── SÍ → CUANTITATIVA
    └── ¿Puede tener decimales/se mide?
        ├── NO (se cuenta) → Discreta (número de hijos)
        └── SÍ (se mide) → Continua (estatura)
```

---

## ⚙️ Ejemplos de Clasificación Completa

### Ejemplo 1: Encuesta escolar

| Variable | Clasificación | Justificación |
|----------|--------------|---------------|
| Nombre del estudiante | Cualitativa nominal | Categoría sin orden |
| Género | Cualitativa nominal | Categoría sin orden |
| Grado | Cualitativa ordinal | Categorías ordenadas (1° < 2° < 3°...) |
| Número de hermanos | Cuantitativa discreta | Se cuenta (enteros) |
| Estatura | Cuantitativa continua | Se mide (puede tener decimales) |
| Nota promedio | Cuantitativa continua | Se mide (puede ser 8.5) |
| Satisfacción con el colegio | Cualitativa ordinal | Malo < Regular < Bueno < Excelente |

### Ejemplo 2: Datos médicos

| Variable | Clasificación | Justificación |
|----------|--------------|---------------|
| Tipo de sangre | Cualitativa nominal | A, B, AB, O sin orden |
| Peso | Cuantitativa continua | Se mide en kg |
| Número de consultas al año | Cuantitativa discreta | Se cuenta |
| Nivel de dolor (1-10) | *Debate* | Podría ser ordinal o discreta* |
| Diagnóstico | Cualitativa nominal | Categorías de enfermedades |

*El nivel de dolor del 1 al 10 es un caso especial: aunque usa números, realmente representa categorías ordenadas (ordinal). Sin embargo, muchos lo tratan como cuantitativa discreta para poder calcular promedios.

---

## 🔑 Resumen

| Tipo de Variable | Característica | Ejemplos |
|-----------------|----------------|----------|
| **Cualitativa Nominal** | Categorías sin orden | Color, género, país |
| **Cualitativa Ordinal** | Categorías con orden | Nivel educativo, satisfacción |
| **Cuantitativa Discreta** | Números enteros (contar) | Hijos, estudiantes, goles |
| **Cuantitativa Continua** | Números con decimales (medir) | Peso, estatura, tiempo |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica cada variable como **Cualitativa (Nominal u Ordinal)** o **Cuantitativa (Discreta o Continua)**:

a) Número de páginas de un libro
b) Color de un carro
c) Calificación de una película (1 a 5 estrellas)
d) Distancia recorrida en km
e) Número de idiomas que habla una persona

<details>
<summary>Ver solución</summary>

a) **Cuantitativa Discreta** - Se cuenta (200 páginas, no 200.5)

b) **Cualitativa Nominal** - Categorías sin orden (rojo, azul, negro...)

c) **Cualitativa Ordinal** - Categorías ordenadas (1★ < 2★ < 3★ < 4★ < 5★)

d) **Cuantitativa Continua** - Se mide (puede ser 5.3 km, 10.756 km...)

e) **Cuantitativa Discreta** - Se cuenta (1, 2, 3 idiomas... no 2.5)

</details>

### Ejercicio 2
Para cada situación, identifica la variable y clasifícala:

a) Una empresa registra el departamento donde trabajan sus empleados (Ventas, Marketing, Producción, etc.)

b) Un hospital mide la temperatura corporal de los pacientes al ingresar

c) Una escuela registra cuántos días faltó cada estudiante en el año

d) Una encuesta pide valorar un servicio como "Muy satisfecho", "Satisfecho", "Neutral", "Insatisfecho", "Muy insatisfecho"

<details>
<summary>Ver solución</summary>

a) **Variable:** Departamento de trabajo → **Cualitativa Nominal** (categorías sin orden)

b) **Variable:** Temperatura corporal → **Cuantitativa Continua** (se mide, puede ser 37.2°C)

c) **Variable:** Días de ausencia → **Cuantitativa Discreta** (se cuenta, son enteros)

d) **Variable:** Nivel de satisfacción → **Cualitativa Ordinal** (categorías con orden claro)

</details>

### Ejercicio 3
¿Por qué el número de teléfono, aunque está compuesto de números, NO es una variable cuantitativa?

<details>
<summary>Ver solución</summary>

Porque aunque los números de teléfono están formados por dígitos, **no representan cantidades**:

- No tiene sentido sumar dos números de teléfono
- No tiene sentido calcular el "promedio" de números de teléfono
- El número 3001234567 no es "mayor" en ningún sentido útil que 3009876543

Los números de teléfono son simplemente **etiquetas** o identificadores. Por lo tanto, son **cualitativas nominales**, igual que los nombres o los códigos de barras.

**Regla:** Si no tiene sentido hacer operaciones matemáticas con los números, entonces no es cuantitativa.

</details>

### Ejercicio 4
Un investigador quiere estudiar los hábitos de ejercicio. Diseña las siguientes preguntas:

1. ¿Cuántos días a la semana haces ejercicio?
2. ¿Cuál es tu deporte favorito?
3. ¿Cuánto tiempo (en minutos) dura cada sesión?
4. ¿Cómo calificas tu nivel de condición física? (Bajo, Medio, Alto)

Clasifica cada variable y explica qué tipo de análisis (gráficos, promedios, etc.) sería apropiado.

<details>
<summary>Ver solución</summary>

1. **Días a la semana:** Cuantitativa Discreta
   - **Análisis:** Calcular promedio, mediana, hacer histograma

2. **Deporte favorito:** Cualitativa Nominal
   - **Análisis:** Contar frecuencias, diagrama de barras o circular

3. **Tiempo en minutos:** Cuantitativa Continua
   - **Análisis:** Calcular promedio, desviación estándar, histograma

4. **Nivel de condición física:** Cualitativa Ordinal
   - **Análisis:** Contar frecuencias por categoría, diagrama de barras ordenado

</details>

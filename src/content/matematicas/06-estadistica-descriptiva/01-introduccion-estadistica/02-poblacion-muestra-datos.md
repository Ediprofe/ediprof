# Población, Muestra y Datos

Imagina que quieres saber cuántas horas al día usan el celular los jóvenes de tu país. ¿Tendrías que preguntarle a **cada uno de los millones de jóvenes**? ¡Imposible! 

Aquí es donde entran conceptos fundamentales que te permitirán estudiar grandes grupos sin necesidad de encuestar a todos.

---

## 🎯 ¿Qué vas a aprender?

- La diferencia entre población y muestra
- Qué son los datos y las variables
- Qué significan parámetro y estadístico
- Conceptos de experimento y observación

---

## 📊 Resumen Rápido

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Población** | Todos los individuos de interés | Todos los estudiantes de Colombia |
| **Muestra** | Subconjunto seleccionado de la población | 500 estudiantes encuestados |
| **Dato** | Valor registrado de una característica | "María tiene 16 años" |
| **Variable** | Característica que puede variar | Edad, estatura, color de ojos |
| **Parámetro** | Medida calculada sobre la población | Promedio de edad de TODOS los colombianos |
| **Estadístico** | Medida calculada sobre la muestra | Promedio de edad de los 500 encuestados |

---

## 📖 Población

> La **población** es el conjunto **completo** de todos los individuos, objetos o mediciones que queremos estudiar.

### 💡 Características de la población:
- Es el **grupo total** de interés
- Puede ser **finita** (se puede contar) o **infinita** (imposible de contar)
- Generalmente es muy grande o difícil de acceder

### ⚙️ Ejemplo 1: Población finita

**Pregunta:** ¿Cuál es la estatura promedio de los estudiantes de tu colegio?

- **Población:** Todos los estudiantes del colegio
- **Tamaño:** Si hay 800 estudiantes, la población tiene 800 elementos
- **Es finita:** Puedes contar exactamente cuántos son

### ⚙️ Ejemplo 2: Población infinita

**Pregunta:** ¿Cuánto dura una bombilla de cierta marca?

- **Población:** Todas las bombillas que la fábrica producirá (pasadas, presentes y futuras)
- **Es infinita:** No puedes saber cuántas producirán en el futuro

---

## 📖 Muestra

> La **muestra** es un **subconjunto** de la población, seleccionado para estudiarla.

### 💡 ¿Por qué usar muestras?
- **Economía:** Encuestar a todos es muy costoso
- **Tiempo:** Sería demasiado lento
- **Acceso:** A veces es imposible llegar a toda la población
- **Destrucción:** Algunas pruebas destruyen el objeto (como probar la duración de una bombilla)

### ⚙️ Ejemplo 1: Muestra de estudiantes

**Población:** Los 50,000 estudiantes universitarios de una ciudad

**Muestra:** 800 estudiantes seleccionados para una encuesta

**Pregunta:** ¿Cuántas horas estudian al día?

| Aspecto | Población | Muestra |
|---------|-----------|---------|
| Tamaño | 50,000 | 800 |
| ¿Se puede encuestar a todos? | Muy difícil | Sí |
| Resultado | Verdadero (pero desconocido) | Estimación del verdadero |

### ⚙️ Ejemplo 2: Control de calidad

Una fábrica produce 10,000 chocolates al día.

- **Población:** Los 10,000 chocolates del día
- **Muestra:** 50 chocolates seleccionados al azar para probar

¿Por qué no prueban todos? ¡Porque tendrían que comerse toda la producción! 🍫

---

## 📖 Dato

> Un **dato** es cada valor o información específica que registramos de un individuo.

### 💡 Ejemplos de datos:
- La edad de Juan: **17 años** ← Esto es un dato
- La nota de María en matemáticas: **8.5** ← Esto es un dato
- El color favorito de Pedro: **azul** ← Esto es un dato

### ⚙️ Ejemplo: Conjunto de datos

Si encuestamos a 5 estudiantes sobre su edad:

| Estudiante | Edad (dato) |
|------------|-------------|
| Ana | 15 |
| Luis | 16 |
| María | 15 |
| Carlos | 17 |
| Sofía | 16 |

Los **datos** son: 15, 16, 15, 17, 16

---

## 📖 Variable

> Una **variable** es la característica o propiedad que medimos u observamos, y que **puede tomar diferentes valores**.

### 💡 ¿Por qué se llama "variable"?
Porque su valor **varía** de un individuo a otro.

### ⚙️ Ejemplo de variables:

| Variable | Valores posibles |
|----------|-----------------|
| Edad | 15, 16, 17, 18... años |
| Estatura | 150, 165, 180... cm |
| Color de ojos | Café, negro, verde, azul |
| Nota del examen | 0 a 10 |
| Estado civil | Soltero, casado, divorciado |

### 💡 Relación dato-variable

- **Variable:** Edad
- **Datos:** 15, 16, 15, 17, 16

La variable es **qué** medimos; los datos son los **valores específicos** que obtenemos.

---

## 📖 Parámetro vs Estadístico

Esta es una distinción **crucial** en estadística:

| Concepto | Se calcula sobre... | Símbolo común | ¿Se conoce exactamente? |
|----------|--------------------|--------------|-----------------------|
| **Parámetro** | Toda la población | Letras griegas (μ, σ) | Generalmente NO |
| **Estadístico** | Solo la muestra | Letras latinas (x̄, s) | SÍ |

### ⚙️ Ejemplo concreto

**Situación:** Queremos conocer el ingreso promedio mensual de todos los trabajadores de un país.

- **Parámetro (μ):** El ingreso promedio **real** de TODOS los trabajadores → **Desconocido** (no podemos encuestar a todos)
- **Estadístico (x̄):** El ingreso promedio de los 2,000 trabajadores encuestados → **Conocido** (lo calculamos con la muestra)

El estadístico **estima** el parámetro.

### 💡 Analogía

Piensa en una olla de sopa:
- **Parámetro:** El sabor de TODA la olla
- **Estadístico:** El sabor de una cucharada que pruebas

Si mezclas bien la sopa, una cucharada es suficiente para saber cómo sabe toda la olla. ¡Eso es exactamente lo que hace la estadística inferencial!

---

## 📖 Experimento y Observación

Hay dos formas de obtener datos:

### Experimento

> Un **experimento** es cuando el investigador **interviene** y **controla** las condiciones para ver el efecto.

**Ejemplo:** Un laboratorio prueba un nuevo medicamento:
- Grupo A recibe el medicamento
- Grupo B recibe un placebo
- El investigador **controla** quién recibe qué

### Observación

> Una **observación** es cuando el investigador **solo registra** datos sin intervenir.

**Ejemplo:** Estudiar la relación entre horas de sueño y rendimiento académico:
- Se pregunta a los estudiantes cuánto duermen
- Se registran sus notas
- El investigador **no controla** cuánto duerme cada quien

| Tipo | ¿Hay intervención? | Ejemplo |
|------|-------------------|---------|
| Experimento | ✅ Sí | Probar efecto de un fertilizante en plantas |
| Observación | ❌ No | Registrar la cantidad de lluvia diaria |

---

## 🔑 Resumen

| Término | Definición rápida |
|---------|-------------------|
| **Población** | Grupo completo que queremos estudiar |
| **Muestra** | Subconjunto seleccionado de la población |
| **Dato** | Valor específico registrado |
| **Variable** | Característica que puede tomar diferentes valores |
| **Parámetro** | Medida calculada sobre toda la población |
| **Estadístico** | Medida calculada sobre la muestra |
| **Experimento** | Obtener datos con intervención del investigador |
| **Observación** | Obtener datos sin intervención |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica la **población** y la **muestra** en cada situación:

a) Para estudiar la opinión sobre el transporte público en una ciudad de 3 millones de habitantes, se encuestan 1,500 personas.

b) Un profesor quiere saber el tiempo promedio que sus 35 estudiantes dedican a la tarea. Pregunta a 10 de ellos.

<details>
<summary>Ver solución</summary>

a) 
- **Población:** Los 3 millones de habitantes de la ciudad
- **Muestra:** Las 1,500 personas encuestadas

b)
- **Población:** Los 35 estudiantes del profesor
- **Muestra:** Los 10 estudiantes a quienes preguntó

</details>

### Ejercicio 2
Clasifica cada característica como **variable** y da un ejemplo de **dato**:

a) El peso de los bebés al nacer
b) La marca de celular que tiene cada estudiante
c) El número de hermanos

<details>
<summary>Ver solución</summary>

a) **Variable:** Peso al nacer | **Dato posible:** 3.2 kg

b) **Variable:** Marca de celular | **Dato posible:** Samsung

c) **Variable:** Número de hermanos | **Dato posible:** 2

</details>

### Ejercicio 3
¿Cuál es la diferencia entre un **parámetro** y un **estadístico**? Explica con tus propias palabras.

<details>
<summary>Ver solución</summary>

- Un **parámetro** es una medida (como el promedio) calculada usando **toda la población**. Generalmente es desconocido porque no podemos acceder a toda la población.

- Un **estadístico** es una medida calculada usando **solo la muestra**. Es conocido porque tenemos los datos de la muestra.

El estadístico se usa para **estimar** el parámetro.

</details>

### Ejercicio 4
Indica si cada situación es un **experimento** o una **observación**:

a) Un médico asigna aleatoriamente a pacientes a dos tratamientos diferentes para comparar su efectividad.

b) Un investigador revisa los registros históricos de temperatura de una ciudad.

c) Un agrónomo divide un campo en parcelas y aplica diferentes cantidades de fertilizante a cada una.

d) Un sociólogo estudia la relación entre nivel educativo e ingresos usando datos del censo.

<details>
<summary>Ver solución</summary>

a) **Experimento** - El médico interviene asignando tratamientos

b) **Observación** - Solo revisa datos existentes, no interviene

c) **Experimento** - El agrónomo controla la cantidad de fertilizante

d) **Observación** - Usa datos existentes, no controla ninguna variable

</details>

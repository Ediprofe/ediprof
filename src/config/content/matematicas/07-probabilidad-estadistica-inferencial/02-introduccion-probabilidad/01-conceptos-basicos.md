---
title: "Conceptos Básicos de Probabilidad"
---

# Conceptos Básicos de Probabilidad

La probabilidad está en todas partes: desde el pronóstico del tiempo hasta los juegos de azar, desde los diagnósticos médicos hasta las decisiones de inversión. Empecemos por los conceptos fundamentales.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la probabilidad y qué mide
- Experimento aleatorio, espacio muestral y evento
- Las diferentes definiciones de probabilidad
- Propiedades básicas

---

## 📊 Terminología Esencial

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Experimento aleatorio** | Proceso con resultado incierto | Lanzar un dado |
| **Espacio muestral (S)** | Conjunto de todos los resultados posibles | {1, 2, 3, 4, 5, 6} |
| **Evento** | Subconjunto del espacio muestral | "Obtener par" = {2, 4, 6} |
| **Resultado** | Un elemento del espacio muestral | Obtener 5 |

---

## 📖 ¿Qué es la Probabilidad?

> La **probabilidad** de un evento es un número entre 0 y 1 que mide qué tan **posible** es que ocurra.

### 💡 Interpretación:

| Valor | Significado |
|-------|-------------|
| P = 0 | Imposible |
| P = 0.5 | Igual de probable que improbable |
| P = 1 | Seguro |
| 0 < P < 1 | Algún grado de posibilidad |

---

## 📖 Experimento Aleatorio

> Un **experimento aleatorio** es un proceso que:
> 1. Se puede repetir bajo las mismas condiciones
> 2. El resultado no se puede predecir con certeza
> 3. Se conocen todos los resultados posibles

### ⚙️ Ejemplos:

| Experimento | ¿Aleatorio? | Razón |
|-------------|-------------|-------|
| Lanzar moneda | ✅ Sí | No sabemos si será cara o sello |
| Soltar piedra | ❌ No | Siempre cae (es predecible) |
| Extraer carta de baraja | ✅ Sí | No sabemos cuál saldrá |
| Sumar 2 + 3 | ❌ No | Siempre es 5 |

---

## 📖 Espacio Muestral

> El **espacio muestral** (S o Ω) es el conjunto de **todos** los resultados posibles de un experimento aleatorio.

### ⚙️ Ejemplos:

| Experimento | Espacio Muestral |
|-------------|------------------|
| Lanzar moneda | S = {Cara, Sello} |
| Lanzar dado | S = {1, 2, 3, 4, 5, 6} |
| Lanzar 2 monedas | S = {CC, CS, SC, SS} |
| Bebé | S = {Niño, Niña} |

### 💡 Notación:

- |S| = número de elementos en S (cardinalidad)
- Para el dado: |S| = 6

---

## 📖 Eventos

> Un **evento** es cualquier subconjunto del espacio muestral.

### ⚙️ Ejemplo: Dado de 6 caras

- **S** = {1, 2, 3, 4, 5, 6}
- **Evento A:** "Obtener número par" = {2, 4, 6}
- **Evento B:** "Obtener número mayor que 4" = {5, 6}
- **Evento C:** "Obtener 7" = {} (evento imposible)
- **Evento S:** "Obtener cualquier número" = {1,2,3,4,5,6} (evento seguro)

### 💡 Tipos de eventos:

| Tipo | Descripción | Probabilidad |
|------|-------------|--------------|
| **Imposible** | Conjunto vacío {} | P = 0 |
| **Seguro** | Todo el espacio muestral S | P = 1 |
| **Elemental** | Un solo resultado | Depende |

---

## 📖 Definiciones de Probabilidad

### 💡 Definición Clásica (Laplace)

Si todos los resultados son **igualmente probables**:

$$
P(A) = \frac{\text{casos favorables a } A}{\text{casos totales}} = \frac{|A|}{|S|}
$$

### ⚙️ Ejemplo: Probabilidad de sacar par en un dado

- Casos favorables: {2, 4, 6} → 3 casos
- Casos totales: {1, 2, 3, 4, 5, 6} → 6 casos

$$
P(\text{par}) = \frac{3}{6} = \frac{1}{2} = 0.5 = 50\%
$$

### 💡 Definición Frecuentista

La probabilidad es el **límite** de la frecuencia relativa cuando el experimento se repite muchas veces:

$$
P(A) = \lim_{n \to \infty} \frac{f_A}{n}
$$

### ⚙️ Ejemplo:

Si lanzo una moneda 1000 veces y salen 512 caras:
$$
P(\text{cara}) \approx \frac{512}{1000} = 0.512
$$

### 💡 Definición Subjetiva

La probabilidad refleja el **grado de creencia** de un individuo sobre qué tan posible es un evento.

Ejemplo: "Creo que hay un 70% de probabilidad de que llueva mañana."

---

## 📖 Propiedades de la Probabilidad (Axiomas de Kolmogorov)

### 💡 Axioma 1: No negatividad

$$
P(A) \geq 0 \text{ para todo evento } A
$$

### 💡 Axioma 2: Normalización

$$
P(S) = 1
$$

### 💡 Axioma 3: Aditividad

Si A y B son **mutuamente excluyentes** (no pueden ocurrir juntos):

$$
P(A \cup B) = P(A) + P(B)
$$

---

## 📖 Consecuencias de los Axiomas

### 💡 Probabilidad del complemento:

$$
P(A') = 1 - P(A)
$$

Donde A' es "no ocurre A".

### ⚙️ Ejemplo:

Si P(llueve) = 0.3, entonces P(no llueve) = 1 - 0.3 = 0.7

### 💡 Probabilidad del evento imposible:

$$
P(\emptyset) = 0
$$

### 💡 Rango de probabilidad:

$$
0 \leq P(A) \leq 1
$$

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Experimento aleatorio** | Proceso con resultado incierto |
| **Espacio muestral (S)** | Todos los resultados posibles |
| **Evento** | Subconjunto de S |
| **Probabilidad** | Número entre 0 y 1 |
| **P (clásica)** | Favorables / Totales |
| **P (complemento)** | P(A') = 1 - P(A) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Define el espacio muestral para:
a) Lanzar una moneda 3 veces
b) Elegir un día de la semana al azar
c) Lanzar 2 dados y sumar los resultados

<details>
<summary>Ver solución</summary>

a) S = {CCC, CCS, CSC, CSS, SCC, SCS, SSC, SSS}
   (8 resultados)

b) S = {Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo}
   (7 resultados)

c) S = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
   (Las sumas posibles van de 2 a 12)

</details>

### Ejercicio 2
Se lanza un dado. Calcula:
a) P(obtener 5)
b) P(obtener número impar)
c) P(obtener número mayor que 6)

<details>
<summary>Ver solución</summary>

a) P(5) = 1/6 ≈ 0.167

b) Impares = {1, 3, 5}
   P(impar) = 3/6 = 1/2 = 0.5

c) Mayor que 6 = {} (imposible en dado normal)
   P(>6) = 0

</details>

### Ejercicio 3
Si P(A) = 0.7, ¿cuál es P(no ocurre A)?

<details>
<summary>Ver solución</summary>

P(A') = 1 - P(A) = 1 - 0.7 = **0.3**

</details>

### Ejercicio 4
¿Cuál es la probabilidad de sacar una carta de corazones de una baraja de 52 cartas?

<details>
<summary>Ver solución</summary>

- Cartas de corazones: 13
- Total de cartas: 52

$$P(\text{corazón}) = \frac{13}{52} = \frac{1}{4} = 0.25 = 25\%$$

</details>

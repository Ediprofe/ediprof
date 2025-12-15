# Percentiles

Los **percentiles** son la división más fina: 100 partes iguales. Son los que usas cuando el médico te dice "tu hijo está en el percentil 75 de estatura" o cuando un examen te ubica en cierto percentil.

---

## 🎯 ¿Qué vas a aprender?

- Qué son los percentiles
- Cómo calcularlos e interpretarlos
- Usos comunes en la vida real
- Relación con cuartiles y deciles

---

## 📊 Los 99 Percentiles

Los percentiles van del $P_1$ al $P_{99}$, dividiendo los datos en 100 partes iguales.

| Percentil | Porcentaje debajo | También conocido como |
|-----------|-------------------|----------------------|
| $P_{25}$ | 25% | Primer cuartil (Q1) |
| $P_{50}$ | 50% | Mediana (Q2) |
| $P_{75}$ | 75% | Tercer cuartil (Q3) |
| $P_{90}$ | 90% | Noveno decil (D9) |

---

## 📖 ¿Qué es un Percentil?

> El **percentil k** ($P_k$) es el valor por debajo del cual se encuentra el **k%** de los datos.

### ⚙️ Ejemplo:
Si tu puntaje en un examen es el $P_{85}$:
- **El 85%** de los estudiantes sacó **menos que tú**
- Solo el **15%** sacó **más que tú**

---

## 📖 Cálculo de Percentiles

### 💡 Fórmula de posición:

$$
\text{Posición de } P_k = \frac{k(n+1)}{100}
$$

### ⚙️ Ejemplo: 25 datos

Datos ordenados (tiempos en segundos):
12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 40

$n = 25$

**Percentil 20 ($P_{20}$):**
$$
\text{Pos} = \frac{20 \times 26}{100} = 5.2
$$
Entre posición 5 (18) y 6 (19):
$P_{20} = 18 + 0.2(19-18) = 18.2$

**Percentil 75 ($P_{75} = Q_3$):**
$$
\text{Pos} = \frac{75 \times 26}{100} = 19.5
$$
Entre posición 19 (32) y 20 (33):
$P_{75} = 32 + 0.5(33-32) = 32.5$

---

## 📖 Interpretación de Percentiles

### 💡 Regla de interpretación:

**"Estás en el percentil k"** significa:
- Superaste al k% de las personas
- Eres superado por el (100-k)% de las personas

### ⚙️ Ejemplos de lectura:

| Situación | Percentil | Interpretación |
|-----------|-----------|----------------|
| Examen de admisión | $P_{92}$ | Superaste al 92%; solo 8% mejor que tú |
| Peso de bebé | $P_{50}$ | Peso típico (mitad pesan más, mitad menos) |
| Ingresos | $P_{10}$ | Estás en el 10% con menores ingresos |
| Tiempo de maratón | $P_{80}$ | 80% terminó antes que tú (fuiste lento) |

---

## 📖 Percentiles en la Vida Real

### 💡 Medicina: Curvas de crecimiento

Los pediatras usan percentiles para evaluar el crecimiento:

| Percentil | Significado |
|-----------|-------------|
| < $P_3$ | Muy por debajo del promedio (posible problema) |
| $P_3$ - $P_{25}$ | Por debajo del promedio pero normal |
| $P_{25}$ - $P_{75}$ | Rango normal central |
| $P_{75}$ - $P_{97}$ | Por encima del promedio pero normal |
| > $P_{97}$ | Muy por encima (evaluar causas) |

### 💡 Educación: Pruebas estandarizadas

"Tu puntaje está en el percentil 85" significa que te fue mejor que al 85% de quienes tomaron el examen.

### 💡 Finanzas: Distribución de ingresos

Los economistas estudian la desigualdad usando percentiles:
- $P_{10}$ vs $P_{90}$ (ratio 90/10)
- Ingreso del $P_{99}$ (el 1% más rico)

---

## 📖 Percentiles en Datos Agrupados

Para tablas de frecuencias:

$$
P_k = L_i + \left(\frac{\frac{kn}{100} - F_{anterior}}{f_{P_k}}\right) \times A
$$

### ⚙️ Ejemplo: Encontrar $P_{60}$

| Intervalo | f | F |
|-----------|---|---|
| 10-20 | 5 | 5 |
| 20-30 | 15 | 20 |
| 30-40 | 25 | 45 |
| 40-50 | 30 | 75 |
| 50-60 | 20 | 95 |
| 60-70 | 5 | 100 |

$n = 100$, queremos $P_{60}$

**Paso 1:** Posición = $\frac{60 \times 100}{100} = 60$

**Paso 2:** Buscar en F: La posición 60 está en la clase 40-50 (F = 75 incluye posición 60)

**Paso 3:** Interpolar
- $L_i = 40$
- $F_{anterior} = 45$
- $f = 30$
- $A = 10$

$$
P_{60} = 40 + \left(\frac{60 - 45}{30}\right) \times 10 = 40 + \frac{15}{30} \times 10 = 40 + 5 = 45
$$

---

## 📖 Rango Percentílico

A veces queremos saber en qué percentil está un valor específico.

### 💡 Fórmula:

$$
\text{Rango percentílico de } x = \frac{\text{Número de datos menores que } x}{n} \times 100
$$

### ⚙️ Ejemplo:

En un examen con 50 estudiantes, María sacó 78 puntos. 35 estudiantes sacaron menos que ella.

$$
\text{Rango percentílico} = \frac{35}{50} \times 100 = 70
$$

María está en el **percentil 70**.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Percentil k** | Valor debajo del cual está el k% de datos |
| **$P_{50}$** | = Mediana |
| **$P_{25}$, $P_{75}$** | = Cuartiles Q1 y Q3 |
| **Posición** | $\frac{k(n+1)}{100}$ |
| **Uso principal** | Comparar posición relativa |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si estás en el percentil 95 en un examen de 200 estudiantes, ¿a cuántos superaste?

<details>
<summary>Ver solución</summary>

Estar en el $P_{95}$ significa que superaste al **95%** de los estudiantes.

$0.95 \times 200 = 190$ estudiantes

**Superaste a 190 estudiantes** (solo 10 sacaron más que tú).

</details>

### Ejercicio 2
Un bebé tiene una estatura en el $P_{30}$. ¿Esto es preocupante?

<details>
<summary>Ver solución</summary>

**No necesariamente es preocupante.**

$P_{30}$ significa que el 30% de los bebés de su edad son más bajos y el 70% son más altos.

- Está por debajo del promedio ($P_{50}$) pero dentro del rango normal
- Los percentiles entre $P_3$ y $P_{97}$ se consideran típicamente normales
- Lo importante es la **tendencia**: si el bebé siempre ha estado en $P_{30}$, es su crecimiento normal
- Solo se preocupa si hay caída brusca (ej: de $P_{50}$ a $P_{10}$)

</details>

### Ejercicio 3
¿Cuál es la relación entre $P_{25}$ y $Q_1$?

<details>
<summary>Ver solución</summary>

**Son el mismo valor.**

- $P_{25}$ = Percentil 25 = valor debajo del cual está el 25%
- $Q_1$ = Primer cuartil = valor que divide el primer 25%

Por definición: $P_{25} = Q_1$

De manera similar:
- $P_{50} = Q_2$ = Mediana
- $P_{75} = Q_3$

</details>

### Ejercicio 4
En un grupo de 40 datos, ¿en qué posición está $P_{85}$?

<details>
<summary>Ver solución</summary>

$$\text{Posición} = \frac{85 \times 41}{100} = \frac{3485}{100} = 34.85$$

$P_{85}$ está en la posición **34.85**, entre el dato 34 y el dato 35.

Se interpolaría: $P_{85} = x_{34} + 0.85(x_{35} - x_{34})$

</details>

### Ejercicio 5
En 80 datos ordenados, el dato en posición 60 tiene valor 125. ¿Aproximadamente qué percentil es 125?

<details>
<summary>Ver solución</summary>

Hay 59 datos menores que 125 (posiciones 1 a 59).

$$\text{Percentil} \approx \frac{59}{80} \times 100 = 73.75$$

El valor 125 está aproximadamente en el **percentil 74**.

(Esto es una aproximación; el cálculo exacto depende del método usado).

</details>

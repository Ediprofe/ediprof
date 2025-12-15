# Deciles

Los cuartiles dividen en 4 partes. ¿Y si quisiéramos una división más fina? Los **deciles** dividen los datos en **10 partes iguales**, dando una imagen más detallada de la distribución.

---

## 🎯 ¿Qué vas a aprender?

- Qué son los deciles y cuántos hay
- Cómo calcularlos
- Cómo interpretarlos
- Relación con cuartiles y percentiles

---

## 📊 Los Nueve Deciles

| Decil | Símbolo | Porcentaje debajo |
|-------|---------|-------------------|
| Primer decil | $D_1$ | 10% |
| Segundo decil | $D_2$ | 20% |
| Tercer decil | $D_3$ | 30% |
| Cuarto decil | $D_4$ | 40% |
| Quinto decil | $D_5$ | 50% (= mediana) |
| Sexto decil | $D_6$ | 60% |
| Séptimo decil | $D_7$ | 70% |
| Octavo decil | $D_8$ | 80% |
| Noveno decil | $D_9$ | 90% |

---

## 📖 ¿Qué son los Deciles?

> Los **deciles** son 9 valores que dividen un conjunto de datos ordenados en **10 partes iguales**, cada una con el 10% de los datos.

### 💡 Visualización:

```
[10%][10%][10%][10%][10%][10%][10%][10%][10%][10%]
    ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑
   D1   D2   D3   D4   D5   D6   D7   D8   D9
```

---

## 📖 Cálculo de Deciles

### 💡 Fórmula de posición:

$$
\text{Posición de } D_k = \frac{k(n+1)}{10}
$$

Donde:
- $k = 1, 2, ..., 9$
- $n$ = número de datos

### ⚙️ Ejemplo: 20 datos

Datos ordenados (puntajes de examen):
35, 42, 48, 52, 55, 58, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 93, 98

$n = 20$

**Decil 1 ($D_1$):**
$$
\text{Pos} = \frac{1 \times 21}{10} = 2.1
$$
Interpolamos entre posición 2 (42) y posición 3 (48):
$D_1 = 42 + 0.1(48-42) = 42 + 0.6 = 42.6$

**Decil 5 ($D_5$ = mediana):**
$$
\text{Pos} = \frac{5 \times 21}{10} = 10.5
$$
Entre posición 10 (70) y 11 (72):
$D_5 = 70 + 0.5(72-70) = 71$

**Decil 9 ($D_9$):**
$$
\text{Pos} = \frac{9 \times 21}{10} = 18.9
$$
Entre posición 18 (90) y 19 (93):
$D_9 = 90 + 0.9(93-90) = 90 + 2.7 = 92.7$

---

## 📖 Interpretación de Deciles

### ⚙️ Ejemplo: Ingresos mensuales

$D_1 = \$800,000$
$D_5 = \$1,500,000$
$D_9 = \$4,200,000$

| Decil | Interpretación |
|-------|----------------|
| $D_1$ | El 10% más pobre gana menos de $800,000 |
| $D_5$ | La mitad gana menos de $1,500,000 |
| $D_9$ | El 90% gana menos de $4,200,000 (solo 10% gana más) |

### 💡 Usos comunes:

- **"Estás en el decil 8"** → Superas al 80% de las personas
- **"Perteneces al primer decil"** → Estás en el 10% más bajo
- **"El decil 10"** → El 10% superior (los valores más altos)

---

## 📖 Relación con Cuartiles y Percentiles

| Medida | División | Cantidad de valores |
|--------|----------|---------------------|
| Cuartiles | 4 partes | 3 (Q1, Q2, Q3) |
| Deciles | 10 partes | 9 (D1 a D9) |
| Percentiles | 100 partes | 99 (P1 a P99) |

### 💡 Equivalencias:

| Decil | Equivale a |
|-------|------------|
| $D_1$ | Percentil 10 ($P_{10}$) |
| $D_2$ | Percentil 20 ($P_{20}$) |
| $D_5$ | Percentil 50 = Mediana = $Q_2$ |
| $D_{7.5}$ | Percentil 75 = $Q_3$ (conceptualmente) |
| $D_9$ | Percentil 90 ($P_{90}$) |

---

## 📖 Deciles en Datos Agrupados

Para tablas de frecuencias, se usa interpolación similar a la mediana:

$$
D_k = L_i + \left(\frac{\frac{kn}{10} - F_{anterior}}{f_{D_k}}\right) \times A
$$

Donde:
- $L_i$ = límite inferior de la clase del decil
- $F_{anterior}$ = frecuencia acumulada antes de esa clase
- $f_{D_k}$ = frecuencia de la clase del decil
- $A$ = amplitud de clase

---

## 💡 Aplicaciones Prácticas

| Campo | Uso de deciles |
|-------|----------------|
| **Educación** | "Tu puntaje está en el decil 9" (top 10%) |
| **Economía** | Distribución del ingreso por deciles |
| **Salud** | Percentiles de crecimiento infantil |
| **Recursos humanos** | Evaluaciones de desempeño |

### ⚙️ Ejemplo: Análisis de desigualdad

Los economistas usan los deciles para estudiar la desigualdad:

| Decil | % del ingreso total |
|-------|---------------------|
| 1 (más pobre) | 2% |
| 5 (medio) | 8% |
| 10 (más rico) | 35% |

Si el decil 10 tiene el 35% del ingreso total, hay alta desigualdad.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Deciles** | 9 valores que dividen datos en 10 partes iguales |
| **$D_k$** | El valor debajo del cual está el k×10% de datos |
| **$D_5$** | = Mediana |
| **Posición** | $\frac{k(n+1)}{10}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En un conjunto de 50 datos, ¿en qué posición está $D_3$?

<details>
<summary>Ver solución</summary>

$$\text{Posición de } D_3 = \frac{3 \times 51}{10} = \frac{153}{10} = 15.3$$

El tercer decil está en la posición **15.3** (entre los datos 15 y 16).

</details>

### Ejercicio 2
Si $D_7 = 85$ en las notas de un examen, ¿qué significa?

<details>
<summary>Ver solución</summary>

$D_7 = 85$ significa que:

- **El 70%** de los estudiantes sacó **menos de 85**
- **El 30%** de los estudiantes sacó **85 o más**

Si tu nota es 85, estás en el **30% superior** de la clase.

</details>

### Ejercicio 3
¿Cuál es la relación entre $D_5$ y la mediana?

<details>
<summary>Ver solución</summary>

**Son lo mismo.**

$D_5$ = Quinto decil = valor debajo del cual está el 50% de datos = **Mediana**

También es igual a:
- $Q_2$ (segundo cuartil)
- $P_{50}$ (percentil 50)

</details>

### Ejercicio 4
Los tiempos (en minutos) de 10 corredores fueron:
18, 20, 22, 24, 26, 28, 30, 32, 34, 36

Calcula $D_1$, $D_5$ y $D_9$.

<details>
<summary>Ver solución</summary>

n = 10

**$D_1$:**
$\text{Pos} = \frac{1 \times 11}{10} = 1.1$
$D_1 = 18 + 0.1(20-18) = 18 + 0.2 = 18.2$ min

**$D_5$:**
$\text{Pos} = \frac{5 \times 11}{10} = 5.5$
$D_5 = 26 + 0.5(28-26) = 26 + 1 = 27$ min

**$D_9$:**
$\text{Pos} = \frac{9 \times 11}{10} = 9.9$
$D_9 = 34 + 0.9(36-34) = 34 + 1.8 = 35.8$ min

**Resultado:**
- $D_1 = 18.2$ min (el 10% más rápido)
- $D_5 = 27$ min (mediana)
- $D_9 = 35.8$ min (el 10% más lento está por encima)

</details>

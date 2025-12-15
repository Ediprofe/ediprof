# Ojiva

¿Cómo respondemos preguntas como *"¿Cuántos estudiantes sacaron menos de 7?"* o *"¿En qué nota está el 50% inferior de la clase?"* de forma visual?

La **ojiva** (o polígono de frecuencias acumuladas) es el gráfico perfecto para esto.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una ojiva y para qué sirve
- Cómo construirla paso a paso
- Cómo leer percentiles y la mediana gráficamente
- La diferencia entre ojiva "menor que" y "mayor que"

---

## 📖 ¿Qué es una Ojiva?

> La **ojiva** es la representación gráfica de las **frecuencias acumuladas**. Muestra cuántos datos hay **hasta** cierto valor.

### 💡 Características:
- El eje X tiene los **límites superiores** de clase (o valores)
- El eje Y tiene la **frecuencia acumulada** (F, $F_r$ o $F\%$)
- Es una curva que **siempre sube** (o se mantiene)
- Forma de "S" estirada

---

## 📖 Construcción de la Ojiva

### ⚙️ Ejemplo: Pesos de 40 estudiantes

Usemos los datos de frecuencias acumuladas:

| Clase | Intervalo | Límite Superior | f | F | $F\%$ |
|-------|-----------|-----------------|---|---|-------|
| 0 | — | 51 | — | 0 | 0% |
| 1 | 52 - 58 | 58 | 7 | 7 | 17.5% |
| 2 | 59 - 65 | 65 | 8 | 15 | 37.5% |
| 3 | 66 - 72 | 72 | 9 | 24 | 60.0% |
| 4 | 73 - 79 | 79 | 8 | 32 | 80.0% |
| 5 | 80 - 86 | 86 | 4 | 36 | 90.0% |
| 6 | 87 - 93 | 93 | 4 | 40 | 100% |

### Paso 1: Identificar los puntos

Cada punto tiene coordenadas (Límite superior, F):

| Punto | Límite Superior | F |
|-------|-----------------|---|
| P0 | 51 | 0 |
| P1 | 58 | 7 |
| P2 | 65 | 15 |
| P3 | 72 | 24 |
| P4 | 79 | 32 |
| P5 | 86 | 36 |
| P6 | 93 | 40 |

### Paso 2: Graficar los puntos

- **Eje X:** Los límites superiores de clase
- **Eje Y:** La frecuencia acumulada

### Paso 3: Conectar los puntos

Unir los puntos con líneas rectas (o curvas suaves).

**Resultado:** Una curva que empieza en (51, 0) y termina en (93, 40).

---

## 📖 Usando la Ojiva para Responder Preguntas

### ⚙️ Ejemplo 1: ¿Cuántos estudiantes pesan menos de 70 kg?

**Método:**
1. Ubicar 70 en el eje X
2. Subir verticalmente hasta tocar la ojiva
3. Ir horizontalmente al eje Y
4. Leer el valor de F

**Resultado:** Aproximadamente 20-22 estudiantes pesan menos de 70 kg.

### ⚙️ Ejemplo 2: ¿Qué peso corresponde al 50% inferior?

Esta es la pregunta por la **mediana**.

**Método:**
1. Calcular el 50% de n: $0.50 \times 40 = 20$
2. Ubicar 20 en el eje Y
3. Ir horizontalmente hasta tocar la ojiva
4. Bajar verticalmente al eje X
5. Leer el valor del peso

**Resultado:** La mediana es aproximadamente 70-71 kg.

---

## 📖 Lectura de Percentiles

> El **percentil P** es el valor por debajo del cual se encuentra el P% de los datos.

### 💡 Cómo encontrar percentiles usando la ojiva:

| Para encontrar | Ubicar en eje Y | Leer en eje X |
|----------------|-----------------|---------------|
| Percentil 25 ($P_{25}$) | 25% de n | El valor de X |
| Mediana ($P_{50}$) | 50% de n | El valor de X |
| Percentil 75 ($P_{75}$) | 75% de n | El valor de X |
| Percentil 90 ($P_{90}$) | 90% de n | El valor de X |

### ⚙️ Ejemplo: Encontrar $P_{75}$ (Tercer Cuartil)

**Datos:** n = 40

1. Calcular: $0.75 \times 40 = 30$
2. Ubicar F = 30 en el eje Y
3. Ir horizontalmente a la ojiva
4. Bajar al eje X

**Resultado:** $P_{75} \approx 77$ kg

**Interpretación:** El 75% de los estudiantes pesa 77 kg o menos.

---

## 📖 Ojiva "Menor que" vs "Mayor que"

Hay dos tipos de ojivas:

### Ojiva "Menor que" (la más común)

- Usa **límites superiores** de clase
- Muestra cuántos datos son **menores o iguales** a X
- La curva **sube** de izquierda a derecha
- Empieza en 0, termina en n

### Ojiva "Mayor que"

- Usa **límites inferiores** de clase
- Muestra cuántos datos son **mayores o iguales** a X
- La curva **baja** de izquierda a derecha
- Empieza en n, termina en 0

### ⚙️ Ejemplo de ambas ojivas

Para los mismos datos de peso:

**Ojiva "Menor que":**
| Límite Superior | F (≤) |
|-----------------|-------|
| 58 | 7 |
| 65 | 15 |
| 72 | 24 |
| 79 | 32 |
| 86 | 36 |
| 93 | 40 |

**Ojiva "Mayor que":**
| Límite Inferior | F (≥) |
|-----------------|-------|
| 52 | 40 |
| 59 | 33 |
| 66 | 25 |
| 73 | 16 |
| 80 | 8 |
| 87 | 4 |

### 💡 ¿Dónde se cruzan?

Las dos ojivas se cruzan en la **mediana**, cuando:
- F (≤) = F (≥) = n/2

---

## 📖 Interpretación Visual de la Ojiva

### Forma típica

```
     _______________
    /               
   /                 
  /                  
 /                   
/
```

### ¿Qué indica la pendiente?

| Pendiente | Significa |
|-----------|-----------|
| **Muy empinada** | Muchos datos se concentran en ese rango |
| **Casi plana** | Pocos datos en ese rango |
| **Punto de inflexión** | Cambio en la densidad de datos |

---

## 💡 Usos Prácticos de la Ojiva

| Pregunta | Cómo usar la ojiva |
|----------|-------------------|
| ¿Cuántos ganaron menos de X? | Leer F desde X en eje Y |
| ¿Cuántos ganaron más de X? | Calcular n - F |
| ¿Cuál es la mediana? | Encontrar X donde F = n/2 |
| ¿Cuál es el percentil P? | Encontrar X donde F = P% × n |
| ¿En qué percentil está un valor X? | Leer F desde X, calcular F/n × 100 |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Ojiva** | Gráfico de frecuencias acumuladas |
| **Eje X** | Límites superiores de clase (ojiva "menor que") |
| **Eje Y** | Frecuencia acumulada (F, $F_r$ o $F\%$) |
| **Uso principal** | Encontrar percentiles y mediana visualmente |
| **Forma** | Curva que siempre sube (nunca baja) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
La siguiente tabla muestra las frecuencias acumuladas de puntajes en un examen:

| Puntaje (≤) | F |
|-------------|---|
| 40 | 5 |
| 50 | 15 |
| 60 | 35 |
| 70 | 55 |
| 80 | 70 |
| 90 | 78 |
| 100 | 80 |

a) ¿Cuántos estudiantes obtuvieron 60 puntos o menos?
b) ¿Cuántos obtuvieron más de 70 puntos?
c) ¿En qué puntaje aproximadamente está la mediana?

<details>
<summary>Ver solución</summary>

a) **60 puntos o menos:**
Directamente de la tabla: F = 35 estudiantes

b) **Más de 70 puntos:**
Total - estudiantes con 70 o menos = $80 - 55 = 25$ estudiantes

c) **Mediana (Percentil 50):**
50% de 80 = 40
Buscamos dónde F = 40
Está entre 60 (F=35) y 70 (F=55)
Por interpolación, la mediana está cerca de **62-63 puntos**

</details>

### Ejercicio 2
Usando la tabla del ejercicio anterior, encuentra:
a) El percentil 25 ($P_{25}$)
b) El percentil 75 ($P_{75}$)
c) El rango intercuartílico ($P_{75} - P_{25}$)

<details>
<summary>Ver solución</summary>

a) **Percentil 25:**
25% de 80 = 20
Buscamos dónde F = 20
Está entre 50 (F=15) y 60 (F=35)
$P_{25} \approx$ **52-53 puntos**

b) **Percentil 75:**
75% de 80 = 60
Buscamos dónde F = 60
Está entre 70 (F=55) y 80 (F=70)
$P_{75} \approx$ **73-74 puntos**

c) **Rango intercuartílico:**
$IQR = P_{75} - P_{25} = 73 - 52 = 21$ puntos

</details>

### Ejercicio 3
¿Por qué la ojiva "siempre sube" (nunca baja)?

<details>
<summary>Ver solución</summary>

La ojiva siempre sube porque representa la **frecuencia acumulada**, que es una **suma** de todas las frecuencias anteriores.

**Razones matemáticas:**
1. Las frecuencias son siempre ≥ 0 (no hay frecuencias negativas)
2. Cada punto de la ojiva = punto anterior + frecuencia nueva
3. Agregar un número ≥ 0 solo puede aumentar o mantener igual el total

**Analogía:** Es como llenar un vaso con agua. Cada clase agrega más agua (o la misma cantidad si f=0). El nivel nunca puede bajar por sí solo.

**Matemáticamente:**
$F_{i} = F_{i-1} + f_i$ donde $f_i \geq 0$

Por lo tanto, $F_i \geq F_{i-1}$ siempre.

</details>

### Ejercicio 4
Una empresa quiere saber qué ingreso mensual tiene el 10% de empleados mejor pagados. Si la ojiva muestra que el percentil 90 es de $5,200,000:

a) ¿Qué significa este valor?
b) ¿Cómo encontrarías el ingreso mínimo del 10% mejor pagado?

<details>
<summary>Ver solución</summary>

a) **Significado del $P_{90} = \$5,200,000$:**
- El 90% de los empleados gana $5,200,000 o menos
- Solo el 10% gana más de $5,200,000

b) **Ingreso mínimo del 10% mejor pagado:**
El $P_{90}$ es exactamente ese valor: **$5,200,000**

Cualquier empleado que gane más de $5,200,000 está en el 10% superior.

**Nota:** El 10% mejor pagado gana entre $5,200,000 y el máximo de la empresa.

</details>

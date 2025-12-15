# Frecuencia Acumulada

Hasta ahora hemos contado cuántas veces aparece cada valor. Pero a veces necesitamos responder preguntas como: *"¿Cuántos estudiantes sacaron 7 o menos?"* o *"¿Cuántos ganan menos de 2 millones de pesos?"*

Para esto necesitamos la **frecuencia acumulada**: ir sumando las frecuencias a medida que avanzamos.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la frecuencia acumulada absoluta y relativa
- Cómo calcularlas e interpretarlas
- Qué es una ojiva (curva de frecuencia acumulada)
- Cómo usar la acumulada para responder preguntas de "menor o igual que"

---

## 📊 Tipos de Frecuencia Acumulada

| Tipo | Símbolo | Qué indica |
|------|---------|------------|
| Acumulada Absoluta | $F$ | Cuántos datos hay **hasta** cierto valor |
| Acumulada Relativa | $F_r$ | Qué proporción hay **hasta** cierto valor |
| Acumulada Porcentual | $F\%$ | Qué porcentaje hay **hasta** cierto valor |

---

## 📖 Frecuencia Acumulada Absoluta

> La **frecuencia acumulada absoluta** ($F$) de un valor es la **suma** de todas las frecuencias de ese valor y los **anteriores**.

### 💡 Fórmula:

$$
F_i = f_1 + f_2 + ... + f_i = \sum_{j=1}^{i} f_j
$$

O más simple: vas sumando de arriba hacia abajo.

### ⚙️ Ejemplo: Notas de examen

| Nota | f | Frecuencia Acumulada (F) |
|------|---|--------------------------|
| 5 | 2 | 2 |
| 6 | 5 | 2 + 5 = 7 |
| 7 | 8 | 7 + 8 = 15 |
| 8 | 6 | 15 + 6 = 21 |
| 9 | 4 | 21 + 4 = 25 |
| 10 | 3 | 25 + 3 = **28** |
| **Total** | **28** | |

### 💡 ¿Cómo interpretar?

- $F = 7$ para nota 6 significa: **7 estudiantes** sacaron 6 o menos
- $F = 15$ para nota 7 significa: **15 estudiantes** sacaron 7 o menos
- $F = 28$ para nota 10 (última) siempre es igual a $n$ (el total)

### 💡 Propiedad:
La frecuencia acumulada de la **última categoría** siempre es igual a $n$.

---

## 📖 Frecuencia Acumulada Relativa

> La **frecuencia acumulada relativa** ($F_r$) es la proporción de datos que hay **hasta** cierto valor.

### 💡 Fórmula:

$$
F_r = \frac{F}{n}
$$

Donde:
- $F$ = frecuencia acumulada absoluta
- $n$ = total de datos

### ⚙️ Ejemplo continuado

Total de datos: $n = 28$

| Nota | f | F | $F_r = \frac{F}{28}$ | $F\%$ |
|------|---|---|---------------------|-------|
| 5 | 2 | 2 | 0.071 | 7.1% |
| 6 | 5 | 7 | 0.250 | 25.0% |
| 7 | 8 | 15 | 0.536 | 53.6% |
| 8 | 6 | 21 | 0.750 | 75.0% |
| 9 | 4 | 25 | 0.893 | 89.3% |
| 10 | 3 | 28 | 1.000 | 100% |

### 💡 ¿Cómo interpretar?

- $F_r = 0.25$ (25%) para nota 6: **25% de los estudiantes** sacaron 6 o menos
- $F_r = 0.536$ (53.6%) para nota 7: **Más de la mitad** sacó 7 o menos
- $F_r = 0.75$ (75%) para nota 8: **75%** sacó 8 o menos (o sea, 25% sacó más de 8)

---

## ⚙️ Ejemplo Completo: Datos Agrupados

Usemos los datos de peso de la lección anterior:

| Clase | Intervalo | f | F | $F_r$ | $F\%$ |
|-------|-----------|---|---|-------|-------|
| 1 | 52 - 58 | 7 | 7 | 0.175 | 17.5% |
| 2 | 59 - 65 | 8 | 15 | 0.375 | 37.5% |
| 3 | 66 - 72 | 9 | 24 | 0.600 | 60.0% |
| 4 | 73 - 79 | 8 | 32 | 0.800 | 80.0% |
| 5 | 80 - 86 | 4 | 36 | 0.900 | 90.0% |
| 6 | 87 - 93 | 4 | 40 | 1.000 | 100% |
| **Total** | | **40** | | | |

### 💡 Preguntas que podemos responder:

**"¿Cuántos estudiantes pesan 72 kg o menos?"**
- Miramos la clase que contiene 72: clase 3 (66-72)
- $F = 24$
- **Respuesta:** 24 estudiantes

**"¿Qué porcentaje pesa menos de 80 kg?"**
- Clase 4 termina en 79, así que buscamos $F\%$ de clase 4
- $F\% = 80\%$
- **Respuesta:** 80% de los estudiantes

**"¿Cuántos pesan MÁS de 79 kg?"**
- Total - los que pesan 79 o menos = $40 - 32 = 8$
- O bien: $100\% - 80\% = 20\%$ de 40 = 8
- **Respuesta:** 8 estudiantes

---

## 📖 Frecuencia Acumulada "Hacia Arriba" (Mayor o igual)

A veces queremos saber cuántos datos hay **por encima** de cierto valor.

> La **frecuencia acumulada descendente** indica cuántos datos son **mayores o iguales** a cierto valor.

### 💡 Cálculo:
$$F_{\geq} = n - F_{anterior}$$

### ⚙️ Ejemplo

| Nota | f | F (≤) | F (≥) |
|------|---|-------|-------|
| 5 | 2 | 2 | 28 |
| 6 | 5 | 7 | 26 |
| 7 | 8 | 15 | 21 |
| 8 | 6 | 21 | 13 |
| 9 | 4 | 25 | 7 |
| 10 | 3 | 28 | 3 |

**Interpretación:**
- $F_{\geq} = 21$ para nota 7: 21 estudiantes sacaron 7 o más
- $F_{\geq} = 7$ para nota 9: 7 estudiantes sacaron 9 o más

---

## 📖 La Ojiva (Polígono de Frecuencias Acumuladas)

> La **ojiva** es la representación gráfica de las frecuencias acumuladas. Muestra cómo se van acumulando los datos.

### 💡 Características de la ojiva:

- El eje X tiene los valores (o límites superiores de clase)
- El eje Y tiene la frecuencia acumulada (o $F\%$)
- Es una curva que **siempre sube** (o permanece igual, nunca baja)
- Termina en el total ($n$ o 100%)

### 💡 Usos de la ojiva:

- **Encontrar la mediana visualmente:** El valor donde $F\% = 50\%$
- **Encontrar percentiles:** El valor donde $F\% = P\%$
- **Comparar distribuciones:** Dos ojivas en el mismo gráfico

---

## 💡 Verificaciones Importantes

| Verificación | Debe cumplirse |
|--------------|----------------|
| Último valor de $F$ | Igual a $n$ |
| Último valor de $F_r$ | Igual a 1 |
| Último valor de $F\%$ | Igual a 100% |
| $F$ siempre... | Aumenta o se mantiene, nunca disminuye |

---

## 🔑 Resumen

| Concepto | Fórmula | Qué responde |
|----------|---------|--------------|
| **F (acumulada absoluta)** | Suma de todas las $f$ anteriores | ¿Cuántos hay hasta X? |
| **$F_r$ (acumulada relativa)** | $\frac{F}{n}$ | ¿Qué proporción hay hasta X? |
| **$F\%$ (acumulada %)** | $F_r \times 100$ | ¿Qué % hay hasta X? |
| **Ojiva** | Gráfico de $F$ vs valores | Visualizar la acumulación |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Una encuesta sobre horas de estudio diario dio estos resultados:

| Horas | f |
|-------|---|
| 0-1 | 5 |
| 2-3 | 12 |
| 4-5 | 18 |
| 6-7 | 10 |
| 8-9 | 5 |
| **Total** | **50** |

a) Calcula la frecuencia acumulada (F)
b) Calcula la frecuencia acumulada relativa ($F_r$) y porcentual ($F\%$)

<details>
<summary>Ver solución</summary>

| Horas | f | F | $F_r$ | $F\%$ |
|-------|---|---|-------|-------|
| 0-1 | 5 | 5 | 0.10 | 10% |
| 2-3 | 12 | 17 | 0.34 | 34% |
| 4-5 | 18 | 35 | 0.70 | 70% |
| 6-7 | 10 | 45 | 0.90 | 90% |
| 8-9 | 5 | 50 | 1.00 | 100% |

</details>

### Ejercicio 2
Usando la tabla del Ejercicio 1, responde:

a) ¿Cuántos estudiantes estudian 5 horas diarias o menos?
b) ¿Qué porcentaje estudia más de 5 horas?
c) ¿Cuántos estudian entre 4 y 7 horas (inclusive)?

<details>
<summary>Ver solución</summary>

a) **5 horas o menos:**
La clase 4-5 tiene límite superior 5, entonces $F = 35$
**Respuesta:** 35 estudiantes

b) **Más de 5 horas:**
$100\% - 70\% = 30\%$
**Respuesta:** 30% (o 15 estudiantes)

c) **Entre 4 y 7 horas:**
$F_{6-7} - F_{2-3} = 45 - 17 = 28$
**Respuesta:** 28 estudiantes

</details>

### Ejercicio 3
Las notas de 30 estudiantes son:

| Nota | f |
|------|---|
| 3 | 2 |
| 4 | 4 |
| 5 | 6 |
| 6 | 8 |
| 7 | 5 |
| 8 | 3 |
| 9 | 2 |

¿Cuántos estudiantes aprobaron si la nota mínima para aprobar es 6?

<details>
<summary>Ver solución</summary>

**Método 1:** Sumar las frecuencias de 6 o más:
$8 + 5 + 3 + 2 = 18$ estudiantes aprobaron

**Método 2:** Usar frecuencia acumulada
Primero calculamos $F$:

| Nota | f | F |
|------|---|---|
| 3 | 2 | 2 |
| 4 | 4 | 6 |
| 5 | 6 | 12 |
| 6 | 8 | 20 |
| 7 | 5 | 25 |
| 8 | 3 | 28 |
| 9 | 2 | 30 |

Los que NO aprobaron (nota < 6) = 12
Los que aprobaron = $30 - 12 = 18$

**Respuesta:** 18 estudiantes aprobaron

</details>

### Ejercicio 4
Explica con tus palabras por qué la frecuencia acumulada **nunca puede disminuir** a medida que avanzamos en la tabla.

<details>
<summary>Ver solución</summary>

La frecuencia acumulada nunca puede disminuir porque:

1. **Es una suma:** Cada valor de $F$ es la suma de todas las frecuencias anteriores más la actual.

2. **Las frecuencias son positivas o cero:** No puede haber frecuencias negativas (no puedes tener -3 personas con cierta característica).

3. **Sumar cero o más:** En cada paso sumamos $f_i \geq 0$, así que el total solo puede **aumentar o mantenerse igual**.

4. **Lógicamente:** Si 10 personas tienen nota 5 o menos, no puede haber menos de 10 con nota 6 o menos (porque los 10 anteriores siguen contando, más los nuevos).

**Analogía:** Es como llenar un vaso con agua. Puedes seguir agregando agua (aumentar) o no agregar nada (quedarse igual), pero el nivel nunca baja por sí solo.

</details>

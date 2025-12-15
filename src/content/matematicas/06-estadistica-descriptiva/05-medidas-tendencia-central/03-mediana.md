# La Mediana

¿Qué pasa cuando hay valores extremos que distorsionan el promedio? La **mediana** viene al rescate. Es la medida que resiste a los "outliers" y siempre nos da el valor que realmente está en el centro.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la mediana y cómo interpretarla
- Cómo calcularla para número par e impar de datos
- Cómo calcularla con tablas de frecuencias
- Por qué es "resistente" a valores extremos

---

## 📊 Fórmula de Posición de la Mediana

| Cantidad de datos | Posición de la mediana |
|-------------------|------------------------|
| **n impar** | Posición $\frac{n+1}{2}$ |
| **n par** | Promedio de posiciones $\frac{n}{2}$ y $\frac{n}{2}+1$ |

---

## 📖 Definición de la Mediana

> La **mediana** (Me o $\tilde{x}$) es el valor que divide a los datos ordenados en **dos mitades iguales**: 50% por debajo y 50% por encima.

### 💡 Requisito fundamental:
Para encontrar la mediana, los datos **deben estar ordenados** de menor a mayor (o viceversa).

---

## 📖 Cálculo de la Mediana: n Impar

Cuando hay un número **impar** de datos, la mediana es el valor que está exactamente en el medio.

### 💡 Fórmula de posición:

$$
\text{Posición} = \frac{n + 1}{2}
$$

### ⚙️ Ejemplo 1: 5 datos

Datos desordenados: 8, 3, 6, 9, 4

**Paso 1:** Ordenar → 3, 4, 6, 8, 9

**Paso 2:** Encontrar la posición
$$
\text{Posición} = \frac{5 + 1}{2} = 3
$$

**Paso 3:** La mediana es el valor en la posición 3

Posición: 1, 2, **3**, 4, 5
Valores: 3, 4, **6**, 8, 9

**Mediana = 6**

### ⚙️ Ejemplo 2: 7 datos

Datos ordenados: 12, 15, 18, 22, 25, 28, 30

$$
\text{Posición} = \frac{7 + 1}{2} = 4
$$

Posición: 1, 2, 3, **4**, 5, 6, 7
Valores: 12, 15, 18, **22**, 25, 28, 30

**Mediana = 22**

---

## 📖 Cálculo de la Mediana: n Par

Cuando hay un número **par** de datos, la mediana es el **promedio** de los dos valores centrales.

### 💡 Posiciones centrales:

$$
\text{Posición 1} = \frac{n}{2}, \quad \text{Posición 2} = \frac{n}{2} + 1
$$

### ⚙️ Ejemplo 1: 6 datos

Datos ordenados: 3, 5, 7, 9, 11, 13

$$
\text{Posición 1} = \frac{6}{2} = 3, \quad \text{Posición 2} = 3 + 1 = 4
$$

Los valores centrales son:
- Posición 3: valor 7
- Posición 4: valor 9

$$
\text{Mediana} = \frac{7 + 9}{2} = \frac{16}{2} = 8
$$

**Mediana = 8**

### ⚙️ Ejemplo 2: 8 datos

Datos ordenados: 10, 12, 15, 18, 20, 22, 25, 30

Posiciones centrales: $\frac{8}{2} = 4$ y $4 + 1 = 5$

Valores: posición 4 = 18, posición 5 = 20

$$
\text{Mediana} = \frac{18 + 20}{2} = 19
$$

**Mediana = 19**

---

## 📖 La Resistencia de la Mediana

> La mediana es **resistente** a valores extremos porque solo depende de la posición central, no de la magnitud de los valores.

### ⚙️ Ejemplo comparativo

**Datos originales:** 10, 20, 30, 40, 50

- Media: $\frac{150}{5} = 30$
- Mediana: 30 (posición 3)

**Cambiemos el último valor a 500:**

**Datos modificados:** 10, 20, 30, 40, **500**

- Media: $\frac{600}{5} = 120$ (¡cambió drásticamente!)
- Mediana: **30** (¡no cambió!)

### 💡 ¿Por qué ocurre esto?

La mediana solo "ve" qué valor está en el medio. No le importa si el último valor es 50 o 500, siempre y cuando el orden no cambie.

---

## 📖 Mediana con Tabla de Frecuencias

### ⚙️ Ejemplo: Número de mascotas

| Mascotas ($x_i$) | f | F (acumulada) |
|------------------|---|---------------|
| 0 | 8 | 8 |
| 1 | 15 | 23 |
| 2 | 12 | 35 |
| 3 | 5 | 40 |
| **Total** | **40** | |

**Paso 1:** Encontrar la posición de la mediana
$$
\text{Posición} = \frac{40 + 1}{2} = 20.5
$$

Buscamos el valor que contiene las posiciones 20 y 21.

**Paso 2:** Usar la frecuencia acumulada

- F = 8 para $x = 0$ → las posiciones 1-8 tienen valor 0
- F = 23 para $x = 1$ → las posiciones 9-23 tienen valor 1

La posición 20.5 cae en el rango de $x = 1$.

**Mediana = 1 mascota**

---

## 📖 Mediana con Datos Agrupados

Para datos agrupados en clases, usamos **interpolación lineal**:

### 💡 Fórmula:

$$
Me = L_i + \left( \frac{\frac{n}{2} - F_{anterior}}{f_{mediana}} \right) \times A
$$

Donde:
- $L_i$ = límite inferior de la clase mediana
- $n$ = total de datos
- $F_{anterior}$ = frecuencia acumulada antes de la clase mediana
- $f_{mediana}$ = frecuencia de la clase mediana
- $A$ = amplitud de clase

### ⚙️ Ejemplo: Pesos de 40 estudiantes

| Intervalo | f | F |
|-----------|---|---|
| 52 - 58 | 7 | 7 |
| 59 - 65 | 8 | 15 |
| 66 - 72 | 9 | 24 |
| 73 - 79 | 8 | 32 |
| 80 - 86 | 4 | 36 |
| 87 - 93 | 4 | 40 |

**Paso 1:** Encontrar $\frac{n}{2} = \frac{40}{2} = 20$

**Paso 2:** Identificar la clase mediana (donde cae la posición 20)
- F = 15 para clase 59-65
- F = 24 para clase 66-72

La posición 20 cae en la clase **66 - 72** (clase mediana).

**Paso 3:** Identificar los valores:
- $L_i = 66$ (o 65.5 si usamos límites reales)
- $F_{anterior} = 15$
- $f_{mediana} = 9$
- $A = 7$

**Paso 4:** Aplicar la fórmula:
$$
Me = 66 + \left( \frac{20 - 15}{9} \right) \times 7 = 66 + \left( \frac{5}{9} \right) \times 7
$$
$$
Me = 66 + 0.556 \times 7 = 66 + 3.89 = 69.89 \approx 70 \text{ kg}
$$

---

## 💡 Media vs Mediana

| Aspecto | Media | Mediana |
|---------|-------|---------|
| Sensible a extremos | ✅ Muy sensible | ❌ Resistente |
| Usa todos los valores | ✅ Sí | ❌ Solo la posición |
| Cálculo | Suma y divide | Ordena y busca el centro |
| Mejor para | Datos simétricos | Datos sesgados |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Mediana** | Valor central de los datos ordenados |
| **n impar** | Valor en posición $\frac{n+1}{2}$ |
| **n par** | Promedio de valores en posiciones $\frac{n}{2}$ y $\frac{n}{2}+1$ |
| **Resistencia** | No cambia con valores extremos |
| **Uso principal** | Datos con outliers o distribución sesgada |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la mediana de:

a) 12, 8, 15, 20, 5, 10, 18
b) 3, 7, 2, 9, 5, 4
c) 100, 200, 300, 400, 500, 10000

<details>
<summary>Ver solución</summary>

a) **Datos: 12, 8, 15, 20, 5, 10, 18** (n = 7, impar)
Ordenados: 5, 8, 10, **12**, 15, 18, 20
Posición: $\frac{7+1}{2} = 4$
**Mediana = 12**

b) **Datos: 3, 7, 2, 9, 5, 4** (n = 6, par)
Ordenados: 2, 3, **4, 5**, 7, 9
Posiciones centrales: 3 y 4 (valores 4 y 5)
**Mediana = $\frac{4+5}{2} = 4.5$**

c) **Datos: 100, 200, 300, 400, 500, 10000** (n = 6, par)
Ya ordenados: 100, 200, **300, 400**, 500, 10000
Posiciones centrales: 3 y 4 (valores 300 y 400)
**Mediana = $\frac{300+400}{2} = 350$**

Nota: El 10,000 es un outlier pero no afecta la mediana.

</details>

### Ejercicio 2
Los salarios mensuales (en miles de pesos) de 9 empleados son:
1,500 - 1,800 - 1,600 - 1,750 - 1,550 - 15,000 - 1,650 - 1,700 - 1,600

a) Calcula la media
b) Calcula la mediana
c) ¿Cuál representa mejor al grupo? ¿Por qué?

<details>
<summary>Ver solución</summary>

a) **Media:**
$$\bar{x} = \frac{1500 + 1800 + 1600 + 1750 + 1550 + 15000 + 1650 + 1700 + 1600}{9}$$
$$\bar{x} = \frac{28,150}{9} = 3,128$$

**Media = $3,128,000**

b) **Mediana:**
Ordenados: 1500, 1550, 1600, 1600, **1650**, 1700, 1750, 1800, 15000
Posición: $\frac{9+1}{2} = 5$

**Mediana = $1,650,000**

c) **La mediana representa mejor al grupo** porque:
- 8 de 9 empleados ganan entre $1,500,000 y $1,800,000
- Solo uno gana $15,000,000 (el gerente o dueño)
- La media de $3,128,000 es mayor que lo que ganan 8 de 9 personas
- La mediana de $1,650,000 refleja el salario "típico"

</details>

### Ejercicio 3
Usa la tabla para encontrar la mediana:

| Nota | Frecuencia |
|------|------------|
| 5 | 2 |
| 6 | 5 |
| 7 | 8 |
| 8 | 10 |
| 9 | 4 |
| 10 | 1 |

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular frecuencias acumuladas y total

| Nota | f | F |
|------|---|---|
| 5 | 2 | 2 |
| 6 | 5 | 7 |
| 7 | 8 | 15 |
| 8 | 10 | 25 |
| 9 | 4 | 29 |
| 10 | 1 | 30 |

Total n = 30 (par)

**Paso 2:** Posiciones de la mediana
Posiciones: $\frac{30}{2} = 15$ y $\frac{30}{2} + 1 = 16$

**Paso 3:** Buscar en F acumulada
- F = 7 para nota 6 (posiciones 1-7)
- F = 15 para nota 7 (posiciones 8-15)
- F = 25 para nota 8 (posiciones 16-25)

Posición 15 → nota 7
Posición 16 → nota 8

**Mediana = $\frac{7 + 8}{2} = 7.5$**

</details>

### Ejercicio 4
Si la mediana de un conjunto de datos es 50, y se agregan dos valores más: uno de 10 y otro de 90, ¿la nueva mediana será mayor, menor o igual a 50?

<details>
<summary>Ver solución</summary>

**La nueva mediana será igual a 50** (o muy cercana).

**Razón:**
- Se agregó un valor **por debajo** de la mediana (10)
- Se agregó un valor **por encima** de la mediana (90)
- Como se agregó uno de cada lado, el "centro" no se mueve

**Explicación geométrica:**
Imagina los datos en una recta:
```
---10---[valores]---50---[valores]---90---
```

El 10 empuja el centro hacia la derecha
El 90 empuja el centro hacia la izquierda
Los efectos se cancelan

**Nota:** Esto asume que los valores 10 y 90 están en lados opuestos de la mediana original. Si ambos estuvieran del mismo lado, la mediana sí cambiaría.

</details>

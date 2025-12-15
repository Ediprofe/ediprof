# Tabla de Frecuencias Agrupadas

¿Qué pasa si tienes 100 datos y cada uno es diferente? Una tabla con 100 filas no ayuda mucho. Para datos **continuos** o con **muchos valores diferentes**, necesitamos **agrupar** los datos en intervalos llamados **clases**.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo usar datos agrupados
- Cómo determinar el número de clases
- Calcular rango, amplitud, límites y marca de clase
- Construir una tabla de frecuencias agrupadas completa

---

## 📊 Estructura de una Tabla de Frecuencias Agrupadas

| Clase | Límite Inferior | Límite Superior | Marca de Clase ($x_i$) | f | $f_r$ | % |
|-------|-----------------|-----------------|----------------------|---|-------|---|
| 1 | $L_i$ | $L_s$ | $\frac{L_i + L_s}{2}$ | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... |
| **Total** | | | | n | 1 | 100% |

---

## 📖 ¿Cuándo Agrupar Datos?

| Situación | ¿Agrupar? |
|-----------|-----------|
| Variable continua (peso, estatura, tiempo) | ✅ Sí, siempre |
| Más de 15-20 valores diferentes | ✅ Sí |
| Variable discreta con pocos valores | ❌ No |
| Variable cualitativa | ❌ No |

### 💡 Ejemplo

**Datos de estatura de 50 personas (en cm):**
155, 162, 158, 170, 165, 172, 160, 168, 175, 163...

Cada persona tiene una estatura diferente. Si no agrupamos, tendríamos una tabla con 50 filas (¡una por cada valor único!). Agrupando en intervalos como 155-159, 160-164, 165-169... la información se vuelve manejable.

---

## 📖 Paso 1: Calcular el Rango

> El **rango** es la diferencia entre el valor máximo y el mínimo.

### 💡 Fórmula:

$$
R = X_{máx} - X_{mín}
$$

### ⚙️ Ejemplo

Datos de peso (en kg): mínimo = 52, máximo = 91

$$
R = 91 - 52 = 39 \text{ kg}
$$

El rango nos dice que los datos abarcan 39 kg.

---

## 📖 Paso 2: Determinar el Número de Clases

> El **número de clases** ($k$) es cuántos intervalos usaremos para agrupar los datos.

### 💡 Regla de Sturges (la más común):

$$
k = 1 + 3.322 \cdot \log_{10}(n)
$$

O la regla práctica:

$$
k \approx \sqrt{n}
$$

### ⚙️ Ejemplo

Si $n = 50$ datos:

**Método 1 (Sturges):**
$$
k = 1 + 3.322 \cdot \log_{10}(50) = 1 + 3.322 \cdot 1.699 = 1 + 5.64 \approx 7 \text{ clases}
$$

**Método 2 (Raíz):**
$$
k = \sqrt{50} = 7.07 \approx 7 \text{ clases}
$$

### 💡 Recomendaciones:
- Generalmente entre 5 y 15 clases
- Menos de 5: poca información
- Más de 15: demasiado detalle
- Redondear a un número entero

---

## 📖 Paso 3: Calcular la Amplitud de Clase

> La **amplitud** ($A$) es el ancho de cada intervalo.

### 💡 Fórmula:

$$
A = \frac{R}{k}
$$

### ⚙️ Ejemplo

Con $R = 39$ y $k = 7$:

$$
A = \frac{39}{7} = 5.57 \approx 6
$$

**Nota:** Se redondea hacia arriba para asegurar que todos los datos quepan.

---

## 📖 Paso 4: Establecer los Límites de Clase

Cada clase tiene:
- **Límite inferior** ($L_i$): el valor más bajo que entra en la clase
- **Límite superior** ($L_s$): el valor más alto que entra en la clase

### 💡 Procedimiento:

1. La primera clase comienza en el valor mínimo (o ligeramente antes)
2. Sumar la amplitud para obtener el límite inferior de la siguiente clase
3. Repetir hasta cubrir el valor máximo

### ⚙️ Ejemplo

Con mínimo = 52, amplitud = 6:

| Clase | Límite Inferior | Límite Superior |
|-------|-----------------|-----------------|
| 1 | 52 | 57 |
| 2 | 58 | 63 |
| 3 | 64 | 69 |
| 4 | 70 | 75 |
| 5 | 76 | 81 |
| 6 | 82 | 87 |
| 7 | 88 | 93 |

**Verificación:** El máximo (91) cae en la clase 7 (88-93) ✓

### ⚠️ Notación de intervalos

Hay dos formas comunes de escribir las clases:

**Forma 1: Límites exactos** (la que usamos arriba)
- 52-57 (incluye 52 y 57)

**Forma 2: Intervalos semi-abiertos** (común en estadística formal)
- [52, 58) significa: incluye 52, pero NO incluye 58
- Así no hay ambigüedad sobre dónde cae un valor

---

## 📖 Paso 5: Calcular la Marca de Clase

> La **marca de clase** ($x_i$) es el punto medio del intervalo. Representa a todos los datos de esa clase.

### 💡 Fórmula:

$$
x_i = \frac{L_i + L_s}{2}
$$

### ⚙️ Ejemplo

Para la clase 52-57:

$$
x_i = \frac{52 + 57}{2} = \frac{109}{2} = 54.5
$$

| Clase | $L_i$ | $L_s$ | Marca de Clase ($x_i$) |
|-------|-------|-------|------------------------|
| 1 | 52 | 57 | 54.5 |
| 2 | 58 | 63 | 60.5 |
| 3 | 64 | 69 | 66.5 |
| 4 | 70 | 75 | 72.5 |
| 5 | 76 | 81 | 78.5 |
| 6 | 82 | 87 | 84.5 |
| 7 | 88 | 93 | 90.5 |

---

## ⚙️ Ejemplo Completo: Pesos de 40 Estudiantes

**Datos (en kg):**
52, 58, 65, 71, 55, 63, 78, 82, 60, 67, 73, 55, 62, 69, 75, 80, 56, 64, 70, 77,
54, 61, 68, 74, 85, 57, 63, 70, 76, 88, 59, 66, 72, 79, 53, 62, 68, 75, 81, 91

**Paso 1: Valores extremos**
- $X_{mín} = 52$
- $X_{máx} = 91$
- $R = 91 - 52 = 39$

**Paso 2: Número de clases**
$$k = \sqrt{40} = 6.32 \approx 6 \text{ clases}$$

**Paso 3: Amplitud**
$$A = \frac{39}{6} = 6.5 \approx 7$$

**Paso 4: Construir la tabla**

| Clase | Intervalo | $x_i$ | Conteo | f | $f_r$ | % |
|-------|-----------|-------|--------|---|-------|---|
| 1 | 52 - 58 | 55 | ✓✓✓✓✓✓✓ | 7 | 0.175 | 17.5% |
| 2 | 59 - 65 | 62 | ✓✓✓✓✓✓✓✓ | 8 | 0.200 | 20.0% |
| 3 | 66 - 72 | 69 | ✓✓✓✓✓✓✓✓✓ | 9 | 0.225 | 22.5% |
| 4 | 73 - 79 | 76 | ✓✓✓✓✓✓✓✓ | 8 | 0.200 | 20.0% |
| 5 | 80 - 86 | 83 | ✓✓✓✓ | 4 | 0.100 | 10.0% |
| 6 | 87 - 93 | 90 | ✓✓✓✓ | 4 | 0.100 | 10.0% |
| **Total** | | | | **40** | **1.000** | **100%** |

**Interpretación:**
- La mayoría de los estudiantes pesa entre 59 y 79 kg (62.5%)
- Pocos pesan más de 80 kg (20%)
- La clase más frecuente es 66-72 kg

---

## 💡 Glosario de Términos

| Término | Símbolo | Definición |
|---------|---------|------------|
| Rango | $R$ | $X_{máx} - X_{mín}$ |
| Número de clases | $k$ | Cantidad de intervalos |
| Amplitud | $A$ | Ancho de cada intervalo: $\frac{R}{k}$ |
| Límite inferior | $L_i$ | Valor más bajo de la clase |
| Límite superior | $L_s$ | Valor más alto de la clase |
| Marca de clase | $x_i$ | Punto medio: $\frac{L_i + L_s}{2}$ |

---

## 🔑 Resumen del Proceso

1. **Calcular el rango:** $R = X_{máx} - X_{mín}$
2. **Decidir número de clases:** $k \approx \sqrt{n}$ o usar Sturges
3. **Calcular amplitud:** $A = \frac{R}{k}$ (redondear hacia arriba)
4. **Establecer límites:** Empezar en el mínimo, sumar amplitud
5. **Calcular marcas de clase:** $x_i = \frac{L_i + L_s}{2}$
6. **Contar frecuencias:** Clasificar cada dato en su intervalo
7. **Calcular frecuencias relativas y porcentajes**

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Dados los siguientes tiempos (en minutos) que 20 personas tardan en llegar al trabajo:

15, 22, 18, 35, 28, 42, 31, 25, 19, 38, 27, 33, 21, 45, 29, 36, 24, 40, 32, 17

a) Calcula el rango
b) Determina el número de clases apropiado
c) Calcula la amplitud

<details>
<summary>Ver solución</summary>

a) **Rango:**
- $X_{mín} = 15$
- $X_{máx} = 45$
- $R = 45 - 15 = 30$ minutos

b) **Número de clases:**
$k = \sqrt{20} = 4.47 \approx 5$ clases

c) **Amplitud:**
$A = \frac{30}{5} = 6$ minutos

Las clases serían:
- 15-20, 21-26, 27-32, 33-38, 39-44 (ajustando el último para incluir 45)
- O usar intervalos de 7: 15-21, 22-28, 29-35, 36-42, 43-49

</details>

### Ejercicio 2
Construye la tabla de frecuencias agrupadas completa para los datos del Ejercicio 1.

<details>
<summary>Ver solución</summary>

Usando amplitud = 7 para mayor comodidad:

| Clase | Intervalo | $x_i$ | f | $f_r$ | % |
|-------|-----------|-------|---|-------|---|
| 1 | 15 - 21 | 18 | 4 | 0.20 | 20% |
| 2 | 22 - 28 | 25 | 5 | 0.25 | 25% |
| 3 | 29 - 35 | 32 | 5 | 0.25 | 25% |
| 4 | 36 - 42 | 39 | 4 | 0.20 | 20% |
| 5 | 43 - 49 | 46 | 2 | 0.10 | 10% |
| **Total** | | | **20** | **1.00** | **100%** |

**Verificación de conteo:**
- 15-21: 15, 18, 19, 21 → 4 ✓
- 22-28: 22, 25, 27, 28, 24 → 5 ✓
- 29-35: 35, 31, 33, 29, 32 → 5 ✓
- 36-42: 42, 38, 36, 40 → 4 ✓
- 43-49: 45 → Espera, solo sale 1, revisando... 45 está en este intervalo. Los datos son 45 y... revisando, no hay otra. 

Hmm, 4+5+5+4+1 = 19, falta uno. Revisando 17: cae en 15-21. Recuento: 15, 18, 19, 21, 17 = 5.

**Tabla corregida:**

| Clase | Intervalo | $x_i$ | f | $f_r$ | % |
|-------|-----------|-------|---|-------|---|
| 1 | 15 - 21 | 18 | 5 | 0.25 | 25% |
| 2 | 22 - 28 | 25 | 5 | 0.25 | 25% |
| 3 | 29 - 35 | 32 | 5 | 0.25 | 25% |
| 4 | 36 - 42 | 39 | 4 | 0.20 | 20% |
| 5 | 43 - 49 | 46 | 1 | 0.05 | 5% |
| **Total** | | | **20** | **1.00** | **100%** |

</details>

### Ejercicio 3
Explica por qué la marca de clase es importante para calcular promedios en datos agrupados.

<details>
<summary>Ver solución</summary>

La **marca de clase** es importante porque:

1. **Perdemos los datos originales:** Al agrupar, ya no sabemos los valores exactos dentro de cada clase, solo cuántos hay.

2. **Necesitamos un valor representativo:** La marca de clase ($x_i$) representa a todos los datos del intervalo.

3. **Cálculo de la media:** Para calcular el promedio, multiplicamos cada marca de clase por su frecuencia:
   $$\bar{x} = \frac{\sum f_i \cdot x_i}{n}$$

4. **Es el punto medio:** Asumimos que los datos dentro de cada clase están distribuidos uniformemente alrededor del centro.

**Limitación:** El promedio calculado así es una **estimación**, no el valor exacto (que solo conoceríamos con los datos originales).

</details>

### Ejercicio 4
Un conjunto de datos tiene:
- Valor mínimo: 120
- Valor máximo: 200
- Número de datos: 64

Calcula: rango, número de clases (Sturges) y amplitud.

<details>
<summary>Ver solución</summary>

**Rango:**
$$R = 200 - 120 = 80$$

**Número de clases (Sturges):**
$$k = 1 + 3.322 \cdot \log_{10}(64)$$
$$k = 1 + 3.322 \cdot 1.806$$
$$k = 1 + 6.00 = 7 \text{ clases}$$

**Amplitud:**
$$A = \frac{80}{7} = 11.43 \approx 12$$

Usaríamos 7 clases con amplitud 12.

**Las clases serían:**
- 120-131, 132-143, 144-155, 156-167, 168-179, 180-191, 192-203

</details>

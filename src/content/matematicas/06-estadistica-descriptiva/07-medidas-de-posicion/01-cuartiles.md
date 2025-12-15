# Cuartiles

Ya conoces la mediana: el valor que divide los datos en dos mitades. Los **cuartiles** van más allá: dividen los datos en **cuatro partes iguales**, dándonos una imagen más completa de la distribución.

---

## 🎯 ¿Qué vas a aprender?

- Qué son los cuartiles Q1, Q2 y Q3
- Cómo calcularlos paso a paso
- Cómo interpretarlos
- El rango intercuartílico

---

## 📊 Los Tres Cuartiles

| Cuartil | Símbolo | División | Interpretación |
|---------|---------|----------|----------------|
| Primer cuartil | $Q_1$ | 25% abajo, 75% arriba | Valor que supera al 25% |
| Segundo cuartil | $Q_2$ | 50% abajo, 50% arriba | **Es la mediana** |
| Tercer cuartil | $Q_3$ | 75% abajo, 25% arriba | Valor que supera al 75% |

---

## 📖 ¿Qué son los Cuartiles?

> Los **cuartiles** son valores que dividen un conjunto de datos ordenados en **cuatro partes iguales**, cada una con el 25% de los datos.

### 💡 Visualización:

```
Datos ordenados:
[----25%----][----25%----][----25%----][----25%----]
             ↑            ↑            ↑
            Q1           Q2           Q3
          (P25)       (mediana)      (P75)
```

---

## 📖 Cálculo de Cuartiles: Método de Posición

### Paso 1: Ordenar los datos

Siempre de menor a mayor.

### Paso 2: Calcular las posiciones

$$
\text{Posición de } Q_k = \frac{k(n+1)}{4}
$$

Donde:
- $k = 1, 2, 3$ (para Q1, Q2, Q3)
- $n$ = número de datos

### ⚙️ Ejemplo: 11 datos

Datos ordenados: 12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 45

$n = 11$

**Posición de Q1:**
$$
\text{Pos}_{Q_1} = \frac{1 \times 12}{4} = 3
$$
Q1 = dato en posición 3 = **18**

**Posición de Q2 (mediana):**
$$
\text{Pos}_{Q_2} = \frac{2 \times 12}{4} = 6
$$
Q2 = dato en posición 6 = **25**

**Posición de Q3:**
$$
\text{Pos}_{Q_3} = \frac{3 \times 12}{4} = 9
$$
Q3 = dato en posición 9 = **35**

---

## 📖 Cuando la Posición No es Entera

### ⚙️ Ejemplo: 10 datos

Datos: 5, 8, 12, 15, 18, 22, 25, 30, 35, 40

$n = 10$

**Posición de Q1:**
$$
\text{Pos}_{Q_1} = \frac{1 \times 11}{4} = 2.75
$$

La posición 2.75 está entre el dato 2 (8) y el dato 3 (12).

**Interpolación:**
$$
Q_1 = 8 + 0.75 \times (12 - 8) = 8 + 3 = 11
$$

**Posición de Q3:**
$$
\text{Pos}_{Q_3} = \frac{3 \times 11}{4} = 8.25
$$

Entre dato 8 (30) y dato 9 (35):
$$
Q_3 = 30 + 0.25 \times (35 - 30) = 30 + 1.25 = 31.25
$$

---

## 📖 Método Alternativo (Más Simple)

Otra forma común de calcular cuartiles:

### Paso 1: Encontrar la mediana (Q2)

Divide los datos en dos mitades.

### Paso 2: Q1 = mediana de la mitad inferior

### Paso 3: Q3 = mediana de la mitad superior

### ⚙️ Ejemplo:

Datos: 2, 4, 6, 8, 10, 12, 14, 16 (n = 8)

**Q2 (mediana):** Entre 8 y 10 → $\frac{8+10}{2} = 9$

**Mitad inferior:** 2, 4, 6, 8
**Q1:** Mediana de (2, 4, 6, 8) = $\frac{4+6}{2} = 5$

**Mitad superior:** 10, 12, 14, 16
**Q3:** Mediana de (10, 12, 14, 16) = $\frac{12+14}{2} = 13$

**Resultado:** Q1 = 5, Q2 = 9, Q3 = 13

---

## 📖 Interpretación de los Cuartiles

### ⚙️ Ejemplo: Notas de un examen

Q1 = 55, Q2 = 70, Q3 = 82

| Cuartil | Interpretación |
|---------|----------------|
| Q1 = 55 | El 25% de los estudiantes sacó menos de 55 |
| Q2 = 70 | La mitad sacó menos de 70, la mitad más |
| Q3 = 82 | El 75% sacó menos de 82 (solo 25% superó 82) |

### 💡 Aplicaciones:
- **"Estás en el primer cuartil"** → Estás en el 25% más bajo
- **"Estás en el cuarto cuartil"** → Estás en el 25% más alto
- **"Tu puntaje supera a Q3"** → Estás por encima del 75%

---

## 📖 Rango Intercuartílico (IQR)

> El **rango intercuartílico** (IQR) es la diferencia entre Q3 y Q1. Contiene el **50% central** de los datos.

### 💡 Fórmula:

$$
IQR = Q_3 - Q_1
$$

### ⚙️ Ejemplo:

Si Q1 = 55 y Q3 = 82:
$$
IQR = 82 - 55 = 27
$$

### 💡 ¿Por qué es útil el IQR?

1. **Medida de dispersión resistente:** No se afecta por valores extremos
2. **Define el "centro":** El 50% central de los datos
3. **Detectar outliers:** Valores fuera de $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$ son atípicos

---

## 📖 Detección de Valores Atípicos (Outliers)

### 💡 Regla del 1.5 × IQR:

Un valor es **atípico** si:
- Es menor que $Q_1 - 1.5 \times IQR$ (atípico bajo)
- Es mayor que $Q_3 + 1.5 \times IQR$ (atípico alto)

### ⚙️ Ejemplo:

Q1 = 55, Q3 = 82, IQR = 27

**Límites:**
- Inferior: $55 - 1.5(27) = 55 - 40.5 = 14.5$
- Superior: $82 + 1.5(27) = 82 + 40.5 = 122.5$

Cualquier nota menor a 14.5 o mayor a 122.5 sería atípica.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Q1** | Primer cuartil (percentil 25) |
| **Q2** | Segundo cuartil = mediana (percentil 50) |
| **Q3** | Tercer cuartil (percentil 75) |
| **IQR** | $Q_3 - Q_1$ (rango del 50% central) |
| **Outlier** | Fuera de $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra Q1, Q2 y Q3 para: 3, 5, 7, 9, 11, 13, 15

<details>
<summary>Ver solución</summary>

n = 7 (impar), datos ya ordenados

**Q2 (mediana):** Posición 4 → **9**

**Mitad inferior:** 3, 5, 7
**Q1:** Mediana de (3, 5, 7) = **5**

**Mitad superior:** 11, 13, 15
**Q3:** Mediana de (11, 13, 15) = **13**

**Resultado:** Q1 = 5, Q2 = 9, Q3 = 13

</details>

### Ejercicio 2
Los puntajes de 12 estudiantes son:
45, 52, 58, 62, 65, 70, 75, 78, 82, 88, 92, 98

a) Calcula Q1, Q2 y Q3
b) Calcula el IQR
c) ¿Hay valores atípicos?

<details>
<summary>Ver solución</summary>

a) **Cuartiles:**

n = 12

**Q2:** Promedio de posiciones 6 y 7 = $\frac{70+75}{2} = 72.5$

**Mitad inferior:** 45, 52, 58, 62, 65, 70
**Q1:** Promedio de posiciones 3 y 4 = $\frac{58+62}{2} = 60$

**Mitad superior:** 75, 78, 82, 88, 92, 98
**Q3:** Promedio de posiciones 3 y 4 = $\frac{82+88}{2} = 85$

b) **IQR:**
$IQR = 85 - 60 = 25$

c) **Valores atípicos:**
- Límite inferior: $60 - 1.5(25) = 60 - 37.5 = 22.5$
- Límite superior: $85 + 1.5(25) = 85 + 37.5 = 122.5$

Rango válido: [22.5, 122.5]
Todos los valores están dentro → **No hay outliers**

</details>

### Ejercicio 3
Si Q1 = 100 y Q3 = 180, ¿el valor 250 es un outlier?

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular IQR
$IQR = 180 - 100 = 80$

**Paso 2:** Calcular límite superior
$Q_3 + 1.5 \times IQR = 180 + 1.5(80) = 180 + 120 = 300$

**Paso 3:** Comparar
250 < 300

**Conclusión:** 250 **NO** es un outlier (está dentro del límite).

</details>

### Ejercicio 4
¿Por qué decimos que el IQR es una medida "resistente" de dispersión?

<details>
<summary>Ver solución</summary>

El IQR es "resistente" porque:

1. **Solo usa Q1 y Q3:** Ignora los valores extremos (el 25% más bajo y el 25% más alto).

2. **No cambia con outliers:** Si el valor máximo pasa de 100 a 1000, el IQR no cambia (Q1 y Q3 permanecen igual).

3. **Representa el centro:** Mide la dispersión del 50% central de los datos.

**Comparación:**
- **Rango** (máx - mín): Cambia drásticamente con un solo outlier
- **Desviación estándar:** Se ve afectada por outliers
- **IQR:** Resistente a outliers

**Por eso el IQR se prefiere para datos con posibles valores extremos.**

</details>

# **Deciles**

Ya aprendiste a dividir un pastel en 4 partes (cuartiles). Ahora imagina que quieres hacer un "Top 10" de los mejores estudiantes, o analizar el 10% más pobre de un país. Necesitas una división más fina. Los **Deciles** son los cortes que dividen tus datos en **10 grupos iguales**, cada uno con el 10% de la información.

---

## 🎯 ¿Qué vas a aprender?

- Calcular los nueve deciles ($D_1$ a $D_9$) en datos simples y tablas.
- Entender la equivalencia entre Deciles, Cuartiles y Percentiles.
- Interpretar qué significa estar en el "último decil".
- Identificar su uso en clasificaciones económicas y académicas.

---

## La Decarquía de los Datos

Para tener 10 grupos, haces **9 cortes**:
- **$D_1$:** Deja atrás al 10% de los datos.
- **$D_5$:** Deja atrás al 50%. (¡Es la Mediana!).
- **$D_9$:** Deja atrás al 90%. (Solo el 10% "top" lo supera).

---

## Cálculo con Datos Simples

Ordena y busca la posición:
$$ Posición = \frac{k(n+1)}{10} $$
Donde $k$ va de 1 a 9.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: El Top 10% ($D_9$)
**Datos:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. ($n=10$).
**Objetivo:** Hallar el corte del 90%.
**Posición:** $9(11)/10 = 99/10 = 9.9$.
**Valor:** Entre el dato 9 (18) y el 10 (20).
**Interpolación:** $18 + 0.9(20-18) = 18 + 1.8 = 19.8$.
**Interpretación:** Solo el 10% de los datos supera 19.8.

#### Ejemplo 2: La Mediana ($D_5$)
**Posición:** $5(11)/10 = 55/10 = 5.5$.
**Valor:** Entre dato 5 (10) y 6 (12).
**Promedio:** 11.
**Confirmación:** La mediana de 0 a 20 es 11.

#### Ejemplo 3: El Fondo 20% ($D_2$)
**Datos:** 10, 20, 30, 40, 50. ($n=5$).
**Posición:** $2(6)/10 = 1.2$.
**Valor:** Entre 10 y 20.
**Interpolación:** $10 + 0.2(10) = 12$.

#### Ejemplo 4: Conjunto Pequeño vs Grande
- En $n=9$, la posición de $D_1$ es $1(10)/10 = 1$ (Exacta).
- En $n=100$, la posición de $D_1$ es $1(101)/10 = 10.1$ (Aprox dato 10).

#### Ejemplo 5: Equivalencia
Si calculas $Q_2$ (Mediana) y $D_5$, te dará exactamente el mismo número.

---

## Cálculo con Datos Agrupados (Frecuencias)

Usamos la fórmula maestra de posición:
$$ D_k = L_i + \left( \frac{\frac{kn}{10} - F_{ant}}{f_{D}} \right) \cdot A $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Ingresos de un País ($n=1,000,000$)
**Objetivo:** Hallar la línea de pobreza extrema (supongamos $D_1$).
**Posición:** $1(1M)/10 = 100,000$.
Buscamos en la tabla acumulada quién contiene a las primeras 100,000 personas.

#### Ejemplo 2: Notas de Admisión ($n=500$)
**Objetivo:** Aceptar solo al 20% superior.
**Estrategia:** Calcular $D_8$ (deja atrás al 80%).
**Posición:** $8(500)/10 = 400$.
El puntaje de corte será el valor del estudiante número 400 en el ranking ascendente.

#### Ejemplo 3: Análisis de Ventas
**Dato:** El $D_5$ es 50 unidades vendidas.
**Interpretación:** En el 50% de los días, vendemos menos de 50 unidades.

#### Ejemplo 4: Comparación
- **Decil 1:** Salario \$500.
- **Decil 10:** Salario \$50,000.
**Análisis:** La brecha es enorme (100 veces). Indica desigualdad.

#### Ejemplo 5: ¿En qué decil estoy?
Si ganas \$1500 y $D_3 = \$1400$ y $D_4 = \$1600$.
**Respuesta:** Estás en el 4º decil. (Superas el 30%, pero no llegas al 40%).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra $D_5$ de: 1, 3, 5, 7, 9.

<details>
<summary>Ver solución</summary>

**Concepto:** Es la mediana (5).
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 2
Si $n=49$, ¿cuál es la posición exacta de $D_2$?

<details>
<summary>Ver solución</summary>

**Cálculo:** $2(50)/10 = 10$.
**Posición:** $\boxed{10}$

</details>

### Ejercicio 3
Estás en el $Decil \ 9$ de altura. ¿Eres alto o bajo?

<details>
<summary>Ver solución</summary>

**Análisis:** Superas al 90%.
**Resultado:** $\boxed{\text{Muy alto}}$

</details>

### Ejercicio 4
Si $D_1 = 10$ y $D_9 = 100$, ¿qué opinas de la dispersión?

<details>
<summary>Ver solución</summary>

**Análisis:** El rango entre el 10% y el 90% es amplio (90 puntos).
**Resultado:** $\boxed{\text{Alta dispersión}}$

</details>

### Ejercicio 5
Calcula $D_1$ para: 10, 20, 30... hasta 100. ($n=10$).

<details>
<summary>Ver solución</summary>

**Posición:** $1(11)/10 = 1.1$.
**Valor:** $10 + 0.1(10) = 11$.
**Resultado:** $\boxed{11}$

</details>

### Ejercicio 6
Verdadero o Falso: $D_5$ es igual a la Media Aritmética.

<details>
<summary>Ver solución</summary>

**Teoría:** Falso. Es la Mediana.
**Resultado:** $\boxed{\text{Falso}}$

</details>

### Ejercicio 7
¿Qué decil usarías para definir el "60% de aprobación"?

<details>
<summary>Ver solución</summary>

**Necesidad:** Cortar el 40% inferior (reprobados) y dejar el 60% superior.
**Decil:** $D_4$.
**Resultado:** $\boxed{D_4}$

</details>

### Ejercicio 8
En una tabla, $F=25$ para la clase A y $n=100$. ¿Qué deciles ya pasaron?

<details>
<summary>Ver solución</summary>
25 es el 25% de 100.
Han pasado $D_1$ (10) y $D_2$ (20). Aún no llegamos a $D_3$ (30).
**Resultado:** $\boxed{D_1 \text{ y } D_2}$
</details>

### Ejercicio 9
Si duplicas todos los datos, ¿qué pasa con $D_1$?

<details>
<summary>Ver solución</summary>

**Análisis:** Todas las medidas de posición se duplican.
**Resultado:** $\boxed{\text{Se duplica}}$

</details>

### Ejercicio 10
Si un país elimina la pobreza y todos ganan lo mismo, ¿cuánto vale $D_1$ comparado con $D_9$?

<details>
<summary>Ver solución</summary>

**Análisis:** Si todos son iguales, $X_{min} = X_{max}$.
**Resultado:** $\boxed{\text{Son iguales}}$

</details>

---

## 🔑 Resumen

| Decil | % Inferior | Equivalente |
|-------|------------|-------------|
| **$D_1$** | 10% | Percentil 10. |
| **$D_5$** | 50% | $Q_2$, Mediana. |
| **$D_{10}$** | 100% | Máximo (teórico). |

> **Conclusión:** Los deciles son el estándar en economía y grandes estudios. Nos permiten ver los matices que los cuartiles (demasiado gruesos) esconden.

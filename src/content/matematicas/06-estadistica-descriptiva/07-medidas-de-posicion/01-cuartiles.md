# **Cuartiles**

Si cortas una pizza en cuatro partes iguales, tendrás cuatro pedazos del 25% cada uno. En estadística, **los cuartiles** son los tres cortes que dividen tus datos en cuatro grupos iguales. Son nuestra primera herramienta para entender no solo el centro, sino la **posición** de los datos.

---

## 🎯 ¿Qué vas a aprender?

- Calcular los tres cuartiles ($Q_1, Q_2, Q_3$) en datos simples.
- Entender que $Q_2$ es lo mismo que la **Mediana**.
- Interpretar qué significa estar en el "cuartil superior" o "inferior".
- Usar los cuartiles en tablas de frecuencia.

---

## El Concepto de los 4 Grupos

Para obtener 4 pedazos, necesitas hacer **3 cortes**.
1.  **$Q_1$ (Cuartil 1):** Deja el 25% de los datos por debajo.
2.  **$Q_2$ (Cuartil 2):** Deja el 50% de los datos por debajo. (¡Es la Mediana!).
3.  **$Q_3$ (Cuartil 3):** Deja el 75% de los datos por debajo.

---

## Cálculo con Datos Simples

Primero, **ordena** los datos. Luego busca la posición:
$$ Posición = \frac{k(n+1)}{4} $$
Donde $k$ es el número de cuartil (1, 2 o 3).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Datos Impares (El caso fácil)
**Datos:** 2, 4, 6, 8, 10, 12, 14. ($n=7$).
1.  **$Q_1$:** Pos = $1(8)/4 = 2$. Dato: **4**.
2.  **$Q_2$:** Pos = $2(8)/4 = 4$. Dato: **8**.
3.  **$Q_3$:** Pos = $3(8)/4 = 6$. Dato: **12**.
**Resultados:** $\boxed{4, 8, 12}$

#### Ejemplo 2: Datos Pares (Promedio)
**Datos:** 10, 20, 30, 40. ($n=4$).
1.  **$Q_1$:** Pos = $1(5)/4 = 1.25$. Promedio entre dato 1 y 2. $(10+20)/2 = 15$.
2.  **$Q_2$:** Pos = $2(5)/4 = 2.5$. Promedio entre 2 y 3. $(20+30)/2 = 25$.
3.  **$Q_3$:** Pos = $3(5)/4 = 3.75$. Promedio entre 3 y 4. $(30+40)/2 = 35$.
**Resultados:** $\boxed{15, 25, 35}$

#### Ejemplo 3: Interpolación estricta
Si quieres ser muy preciso con la posición 1.25 (del ejemplo anterior):
$10 + 0.25(20-10) = 10 + 2.5 = 12.5$.
(Generalmente el promedio simple basta en cursos introductorios, pero la interpolación es más exacta).

#### Ejemplo 4: Interpretación de Riqueza
Si estás en el **$Q_3$** de ingresos, significa que ganas más que el 75% de la gente. Solo el 25% ("el top") gana más que tú.

#### Ejemplo 5: Resistencia a Outliers
**Datos:** 1, 2, 3, 4, 1000.
$Q_1$ (aprox dato 1-2) = 1.5.
$Q_3$ (aprox dato 4-5) = Mayor, pero no explota como la media.
Los cuartiles son **resistentes** a valores extremos.

---

## Cálculo con Datos Agrupados

Usamos la misma lógica de la Mediana (interpolación), pero cambiamos $n/2$ por $kn/4$.

$$ Q_k = L_i + \left( \frac{\frac{kn}{4} - F_{ant}}{f_{Q}} \right) \cdot A $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Tabla de Notas ($n=40$)
**Posición $Q_1$:** $1(40)/4 = 10$. Buscamos en $F_i$.
Si el intervalo [0-2.0] tiene $F=5$ y [2.0-3.0] tiene $F=15$...
El $Q_1$ cae en la clase [2.0-3.0].

#### Ejemplo 2: Posición Exacta
Si la posición calculada es 10 y $F_{ant}$ es justo 10...
El cuartil es el límite superior de esa clase anterior.

#### Ejemplo 3: Salarios ($n=100$)
**$Q_3 = 3(100)/4 = 75$**.
Buscamos el dato 75 en las frecuencias acumuladas.

#### Ejemplo 4: Rango Intercuartílico (IQR)
Es la distancia entre $Q_3$ y $Q_1$.
Mide la dispersión del "centro" de los datos (la caja del medio).
$$IQR = Q_3 - Q_1$$

#### Ejemplo 5: Identificación de Outliers
Cualquier dato que esté muy lejos de los cuartiles (más de $1.5 \times IQR$) se considera sospechoso.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla los cuartiles de: 1, 1, 1, 1, 1.

<details>
<summary>Ver solución</summary>

**Lógica:** Todos son 1.
**Resultados:** $\boxed{1, 1, 1}$

</details>

### Ejercicio 2
Calcula $Q_2$ de: 1, 3, 5, 7, 9.

<details>
<summary>Ver solución</summary>

**Concepto:** Es la mediana.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 3
En una carrera, llegaste en el $Q_1$ de tiempos. ¿Fue bueno o malo?

<details>
<summary>Ver solución</summary>

**Análisis:** $Q_1$ en tiempo significa tiempos bajos (rápidos).
**Resultado:** $\boxed{\text{Bueno (eres rápido)}}$

</details>

### Ejercicio 4
Si $Q_1 = 20$ y $Q_3 = 30$, calcula el IQR.

<details>
<summary>Ver solución</summary>

**Resta:** $30 - 20 = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 5
Calcula $Q_1$ de: 10, 20, 30, 40.

<details>
<summary>Ver solución</summary>

**Posición:** $1.25$. Entre 10 y 20.
**Promedio:** 15.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 6
Verdadero o Falso: El $Q_2$ siempre es igual a la Media.

<details>
<summary>Ver solución</summary>

**Teoría:** Falso. Es igual a la Mediana. Solo en simetría perfecta coinciden con la media.
**Resultado:** $\boxed{\text{Falso}}$

</details>

### Ejercicio 7
Datos: 0, 10, 20, 30. ¿Qué porcentaje de datos es menor a 20?

<details>
<summary>Ver solución</summary>

**Observación:** 20 es el percentil 75 aprox ($Q_3$ fue 25). Bueno, técnicamente 20 es mayor que el 50% exacto.
**Cuartiles:** $Q_1=5, Q_2=15, Q_3=25$. 20 está entre $Q_2$ y $Q_3$.
**Resultado:** $\boxed{50\%}$ (Estrictamente, 0 y 10 son menores).

</details>

### Ejercicio 8
Posición de $Q_3$ si $n=100$.

<details>
<summary>Ver solución</summary>

**Fórmula:** $3(101)/4 = 303/4 = 75.75$.
**Resultado:** $\boxed{75.75}$

</details>

### Ejercicio 9
Si agregas un dato gigante al final, ¿cambia mucho $Q_1$?

<details>
<summary>Ver solución</summary>

**Análisis:** $Q_1$ mira el inicio de la lista. No se entera.
**Resultado:** $\boxed{\text{No cambia (o muy poco)}}$

</details>

### Ejercicio 10
¿Qué cuartil usarías para definir la "clase alta" en economía?

<details>
<summary>Ver solución</summary>

**Contexto:** Los más ricos están arriba.
**Resultado:** $\boxed{\text{Sobre Q3 (Top 25\%)}}$

</details>

---

## 🔑 Resumen

| Cuartil | Porcentaje Acumulado | Equivalente |
|---------|----------------------|-------------|
| **$Q_1$** | 25% | Percentil 25. |
| **$Q_2$** | 50% | La Mediana. |
| **$Q_3$** | 75% | Percentil 75. |

> **Conclusión:** Los cuartiles son los hitos de la carretera de tus datos. Te dicen si vas en el pelotón de atrás ($<Q_1$), en el medio (IQR), o en la fuga delantera ($>Q_3$).

# **Ojiva**

Si te pregunto "¿Cuántas personas pesan entre 60 y 70kg?", miras el histograma. Pero si te pregunto "¿Cuántas personas pesan **menos de** 70kg?", el histograma te obliga a sumar mentalmente. La **Ojiva** soluciona esto. Es una línea que siempre sube y te dice instantáneamente cuántos datos hay acumulados hasta cierto punto. Es la herramienta favorita para hallar medianas y percentiles visualmente.

---

## 🎯 ¿Qué vas a aprender?

- Trazar una Ojiva usando los límites superiores y las frecuencias acumuladas ($F_i$).
- Interpretar el gráfico para responder preguntas de tipo "menor que".
- Localizar gráficamente la mediana y otros percentiles (como el "Top 10%").
- Diferenciar la Ojiva del polígono de frecuencias.

---

## Construcción: Puntos de Acumulación

Para dibujar una Ojiva "Menor que", usamos:
1.  **Eje X:** Los límites superiores de cada intervalo.
2.  **Eje Y:** La frecuencia acumulada ($F_i$ o $H_i$).

La curva empieza en el suelo (frecuencia 0) en el límite inferior del primer intervalo y sube hasta el total de datos ($n$ o 100%).

### ⚙️ Ejemplos Resueltos: Hallando las Coordenadas

#### Ejemplo 1: Datos Básicos
**Intervalos:** [0-10), [10-20). Frecuencias acumuladas $F$: 5, 15.
**Puntos:**
- Inicio: (0, 0)
- Fin Int 1: (10, 5)
- Fin Int 2: (20, 15)

#### Ejemplo 2: Notas (0 a 5.0)
**Acumulado:** Hasta 3.0 van 10 alumnos. Hasta 4.0 van 25 alumnos. Hasta 5.0 van 30 alumnos.
**Puntos:**
- (3.0, 10)
- (4.0, 25)
- (5.0, 30)

#### Ejemplo 3: Tiempo de espera (minutos)
**Datos:** 20% espera < 5 min. 60% espera < 10 min. 100% espera < 15 min.
**Puntos (Eje Y = %):**
- (5, 20%)
- (10, 60%)
- (15, 100%)

#### Ejemplo 4: Estaturas
**Datos:** Intervalo [1.50 - 1.60] tiene $F=8$. [1.60-1.70] tiene $F=20$.
**Puntos:**
- (1.60, 8) <-- Usamos el límite superior
- (1.70, 20)

#### Ejemplo 5: Salarios acumulados
**Tabla:**
- Menos de 1M: 50 personas
- Menos de 2M: 150 personas
- Menos de 3M: 200 personas
**Puntos:**
- (1M, 50)
- (2M, 150)
- (3M, 200)

---

## Lectura de Posiciones: Mediana y Percentiles

La Ojiva es un mapa para encontrar posiciones.

### ⚙️ Ejemplos Resueltos: Interpretación Gráfica

#### Ejemplo 1: Hallar la Mediana
**Situación:** Tienes 100 datos. Quieres la mediana (dato #50).
**Método:**
1. Buscas 50 en el Eje Y.
2. Te mueves horizontalmente hasta chocar con la línea.
3. Bajas al Eje X. Ese valor es la mediana.

#### Ejemplo 2: Top 10%
**Situación:** Quieres saber qué nota saca el 10% mejor.
**Método:**
1. El 10% mejor está arriba, es decir, el percentil 90.
2. Buscas el 90% en el Eje Y.
3. Chocas con la curva y bajas. Esa es la nota mínima para estar en el top.

#### Ejemplo 3: ¿Cuántos pasaron?
**Situación:** La nota de aprobación es 60.
**Lectura:**
1. Buscas 60 en el Eje X (nota).
2. Subes hasta la curva y miras el Eje Y. Digamos que dice "80%".
3. Significa que el 80% sacó 60 o menos (Reprobó).
4. El 20% pasó.

#### Ejemplo 4: Primer Cuartil ($Q_1$)
**Situación:** Quieres el valor que deja por debajo al 25% de datos.
**Método:** Buscas el 25% en el Eje Y, chocas y bajas.

#### Ejemplo 5: Comparación de dos Ojivas
**Gráfico:** Ojiva A está siempre por encima de Ojiva B.
**Interpretación:** Significa que el grupo A acumula sus datos más rápido (valores más bajos). El grupo B tiene valores más altos en general.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En una ojiva de frecuencias acumuladas absolutas, el último punto tiene altura 50. ¿Cuánto vale $n$?

<details>
<summary>Ver solución</summary>

**Concepto:** La ojiva termina en el total de datos acumulados.
**Resultado:** $\boxed{50}$

</details>

### Ejercicio 2
Si la mediana es 15, ¿qué coordenada debe tener el punto en la ojiva (asumiendo eje Y relativo)?

<details>
<summary>Ver solución</summary>

**Concepto:** La mediana es el 50% ($0.5$).
**Coordenada:** $(15, 0.5)$
**Resultado:** $\boxed{(15, 0.5)}$

</details>

### Ejercicio 3
Para dibujar la ojiva del intervalo [10 - 20], ¿qué valor de X usas?

<details>
<summary>Ver solución</summary>

**Regla:** Ojiva "menor que" usa el límite superior.
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 4
Una ojiva muy vertical (casi parada) en un tramo indica...

<details>
<summary>Ver solución</summary>

**Interpretación:** Que la frecuencia acumulada subió muy rápido en poco espacio horizontal. Hay una gran concentración de datos ahí (mucha densidad).
**Resultado:** $\boxed{\text{Alta concentración de datos}}$

</details>

### Ejercicio 5
Si el punto (100, 20%) pertenece a la ojiva, ¿qué porcentaje de datos es mayor a 100?

<details>
<summary>Ver solución</summary>

**Cálculo:** La ojiva dice "menor o igual". Así que 20% son $\leq 100$. El resto son mayores.
$100\% - 20\% = 80\%$.
**Resultado:** $\boxed{80\%}$

</details>

### Ejercicio 6
Verdadero o Falso: La ojiva puede bajar si la frecuencia es baja.

<details>
<summary>Ver solución</summary>

**Lógica:** La frecuencia acumulada nunca disminuye (solo suma). Así que la ojiva nunca baja. Puede quedarse plana si $f=0$.
**Resultado:** $\boxed{\text{Falso}}$

</details>

### Ejercicio 7
¿Cómo hallas el Rango Intercuartílico ($IQR$) con una ojiva?

<details>
<summary>Ver solución</summary>

**Pasos:**
1. Hallas $Q_3$ (buscando el 75%).
2. Hallas $Q_1$ (buscando el 25%).
3. Restas sus valores en X.
**Resultado:** $\boxed{\text{Restando el valor de } X \text{ del 75\% y el 25\%}}$

</details>

### Ejercicio 8
Si tienes una ojiva de porcentajes, ¿en qué valor de Y terminas siempre?

<details>
<summary>Ver solución</summary>

**Concepto:** El total acumulado porcentual es 100%.
**Resultado:** $\boxed{100\%}$

</details>

### Ejercicio 9
Dibuja mentalmente: Intervalo 0-10 (f=0), 10-20 (f=100). ¿Cómo es la ojiva?

<details>
<summary>Ver solución</summary>

**Forma:** Plana de 0 a 10. Luego sube disparada hasta 100 en el tramo 10-20.
**Resultado:** $\boxed{\text{Plana y luego subida vertical}}$

</details>

### Ejercicio 10
¿Qué significa si dos ojivas se cruzan en el punto (X=50, Y=0.5)?

<details>
<summary>Ver solución</summary>

**Interpretación:** Ambas distribuciones tienen la misma mediana (50).
**Resultado:** $\boxed{\text{Tienen la misma mediana}}$

</details>

---

## 🔑 Resumen

| Gráfico | Eje X | Eje Y | Uso Principal |
|---------|-------|-------|---------------|
| **Ojiva** | Límites Superiores | Frec. Acumulada ($F_i, H_i$) | Mediana, Percentiles, Rangos. |
| **Polígono** | Marcas de clase | Frec. Simple ($f_i$) | Comparar formas y modas. |

> **Conclusión:** La Ojiva es el gráfico de "cuántos faltan". Es indispensable para responder preguntas de posición relativa sin hacer cálculos complejos.

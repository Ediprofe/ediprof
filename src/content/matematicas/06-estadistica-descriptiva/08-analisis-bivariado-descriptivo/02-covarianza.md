# **Covarianza**

Ya vimos en el Diagrama de Dispersión que las variables pueden "moverse juntas". Pero en estadística odiamos decir "parece que suben". Queremos un número. Un número que nos diga si la relación es positiva o negativa.

Para encontrarlo, usamos una lógica genial: **multiplicar distancias**.
- Si estoy lejos a la derecha ($+$) y muy arriba ($+$), el resultado es positivo ($+$).
- Si estoy lejos a la izquierda ($-$) y muy abajo ($-$), el resultado también es positivo ($+$). (¡Menos por menos da más!).

Así nace la **Covarianza**: el promedio de esos productos.

---

## 🎯 ¿Qué vas a aprender?

- Calcular la Covarianza ($S_{xy}$) paso a paso.
- Entender la lógica de los cuadrantes (signos).
- Interpretar el resultado Positivo, Negativo o Cero.
- Descubrir por qué este número es "inestable" (depende de las unidades).

---

## La Lógica Matemática

Imagina una cruz centrada en el promedio de los datos $(\bar{x}, \bar{y})$.
Esto crea 4 cuadrantes relativos.
- **Cuadrante Superior Derecho:** $X > \bar{x}, Y > \bar{y}$. ($+ \cdot + = +$).
- **Cuadrante Inferior Izquierdo:** $X < \bar{x}, Y < \bar{y}$. ($- \cdot - = +$).
- **Cuadrante Superior Izquierdo:** $X < \bar{x}, Y > \bar{y}$. ($- \cdot + = -$).
- **Cuadrante Inferior Derecho:** $X > \bar{x}, Y < \bar{y}$. ($+ \cdot - = -$).

$$ Cov(X,Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1} $$

Si la mayoría de puntos están en los cuadrantes positivos, la covarianza será positiva.

---

## Cálculo Paso a Paso

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Relación Positiva Perfecta
**Datos:** (1, 2), (2, 4), (3, 6).
- Medias: $\bar{x}=2, \bar{y}=4$.
1.  **Punto (1, 2):** $(1-2)(2-4) = (-1)(-2) = 2$.
2.  **Punto (2, 4):** $(2-2)(4-4) = (0)(0) = 0$.
3.  **Punto (3, 6):** $(3-2)(6-4) = (1)(2) = 2$.
- Suma: 4.
- $S_{xy} = 4 / (3-1) = 2$.
**Resultado:** $\boxed{2}$ (Positivo).

#### Ejemplo 2: Relación Negativa Perfecta
**Datos:** (1, 10), (2, 5), (3, 0).
- Medias: $\bar{x}=2, \bar{y}=5$.
1.  **Punto (1, 10):** $(-1)(5) = -5$.
2.  **Punto (2, 5):** $(0)(0) = 0$.
3.  **Punto (3, 0):** $(1)(-5) = -5$.
- Suma: -10.
- $S_{xy} = -10/2 = -5$.
**Resultado:** $\boxed{-5}$ (Negativo).

#### Ejemplo 3: Puntos Aleatorios (Sin relación)
**Datos:** (1, 5), (2, 2), (3, 5).
- Medias: $\bar{x}=2, \bar{y}=4$.
1.  **Punto 1:** $(-1)(1) = -1$.
2.  **Punto 2:** $(0)(-2) = 0$.
3.  **Punto 3:** $(1)(1) = 1$.
- Suma: 0.
- $S_{xy} = 0/2 = 0$.
**Resultado:** $\boxed{0}$ (Nula).

#### Ejemplo 4: El Problema de las Unidades (Metros)
**Datos:** (1m, 1m), (3m, 3m).
- Medias: 2m.
- $Cov = 2$.

#### Ejemplo 5: El Problema de las Unidades (Centímetros)
**Mismos Datos:** (100cm, 100cm), (300cm, 300cm).
- Medias: 200cm.
1.  **Punto 1:** $(-100)(-100) = 10,000$.
2.  **Punto 2:** $(100)(100) = 10,000$.
- $Avg = 10,000$.
**Resultado:** $\boxed{20,000}$
**Lección:** La covarianza "explotó" aunque la relación es la misma. Este es su gran defecto.

---

## Interpretación del Signo

1.  **$S_{xy} > 0$:** Las variables crecen juntas (Directa).
2.  **$S_{xy} < 0$:** Las variables se mueven opuestas (Inversa).
3.  **$S_{xy} \approx 0$:** No hay relación lineal clara.

### ⚙️ Ejemplos de Interpretación

#### Ejemplo 1: Salud vs Edad
$S_{xy} = -15$.
**Significado:** La salud tiende a bajar cuando la edad sube.

#### Ejemplo 2: Ventas vs Marketing
$S_{xy} = +5000$.
**Significado:** Moverse juntos. (Ojo: no dice qué tan fuerte es la unión, solo la dirección).

#### Ejemplo 3: Lluvia vs Ganancias
$S_{xy} = -20$.
**Contexto:** Quizás un negocio al aire libre. La lluvia "resta" dinero.

#### Ejemplo 4: Pasos vs Calorías
$S_{xy} = +400$.
**Significado:** Caminar más quema más. Positivo.

#### Ejemplo 5: Nube circular
$S_{xy} = 0.001$.
**Significado:** Prácticamente cero. Son independientes.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la covarianza de: (2, 4), (4, 8).

<details>
<summary>Ver solución</summary>

**Medias:** $\bar{x}=3, \bar{y}=6$.
1. $(2-3)(4-6) = (-1)(-2) = 2$.
2. $(4-3)(8-6) = (1)(2) = 2$.
Suma=4. Divisor($n-1$)=1.
**Resultado:** $\boxed{4}$

</details>

### Ejercicio 2
Si $Cov(X,Y) = -50$, ¿qué tipo de relación tienen?

<details>
<summary>Ver solución</summary>
**Signo:** Negativo.
**Resultado:** $\boxed{\text{Inversa (Negativa)}}$
</details>

### Ejercicio 3
Calcula la covarianza de: (1, 10), (3, 6).

<details>
<summary>Ver solución</summary>

**Medias:** $\bar{x}=2, \bar{y}=8$.
1. $(1-2)(10-8) = (-1)(2) = -2$.
2. $(3-2)(6-8) = (1)(-2) = -2$.
Suma=-4. Divisor=1.
**Resultado:** $\boxed{-4}$

</details>

### Ejercicio 4
Si multiplicas los datos por 10, ¿cambia la covarianza?

<details>
<summary>Ver solución</summary>

**Análisis:** Vimos en el ejemplo de cm/m que sí cambia drásticamente.
**Resultado:** $\boxed{\text{Sí, aumenta x100 (10*10)}}$

</details>

### Ejercicio 5
¿Puede la covarianza ser cero si hay una relación en forma de U ($Y=X^2$)?

<details>
<summary>Ver solución</summary>

**Teoría:** Sí. La parte negativa cancela a la positiva. La covarianza solo mide relaciones lineales.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 6
Calcula covarianza de: (5, 5), (5, 10), (5, 15).

<details>
<summary>Ver solución</summary>

**Análisis:** X no varía ($x-\bar{x}=0$ siempre).
**Cálculo:** $0 \cdot algo = 0$.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 7
Si $X$ representa "Horas de TV" y $Y$ "Calificaciones", esperas una covarianza:

<details>
<summary>Ver solución</summary>

**Lógica:** Más TV, menos estudio.
**Resultado:** $\boxed{\text{Negativa}}$

</details>

### Ejercicio 8
¿Cuál es la unidad de la covarianza si $X$ es Metros y $Y$ es Kilos?

<details>
<summary>Ver solución</summary>

**Operación:** Multiplicamos $X \cdot Y$.
**Resultado:** $\boxed{\text{Metros} \cdot \text{Kilos}}$

</details>

### Ejercicio 9
Si tienes 3 puntos alineados verticalmente, ¿cuánto es la covarianza?

<details>
<summary>Ver solución</summary>

**Análisis:** X es constante. No hay variación en X.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 10
Si sumas 100 a todos los valores de X, ¿cambia la covarianza?

<details>
<summary>Ver solución</summary>

**Análisis:**
- X cambia, pero $\bar{x}$ también cambia igual.
- $(x - \bar{x})$ se mantiene igual.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Significado |
|----------|---------|-------------|
| **Covarianza** | $\frac{\sum(x-\bar{x})(y-\bar{y})}{n-1}$ | Promedio de productos cruzados. |
| **Signo +** | Cuadrantes I y III. | Crecen juntas. |
| **Signo -** | Cuadrantes II y IV. | Crecen opuestas. |

> **Conclusión:** La Covarianza nos dio el signo (la dirección), pero su magnitud es un desastre porque depende de las unidades. Necesitamos una versión "estandarizada" que no cambie si medimos en centímetros o kilómetros. Esa versión es el **Coeficiente de Correlación**.

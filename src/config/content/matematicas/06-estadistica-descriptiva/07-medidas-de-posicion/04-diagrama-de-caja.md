---
title: "Diagrama de Caja (BoxPlot)"
---

# **Diagrama de Caja (BoxPlot)**

Imagina que eres un detective y necesitas ver **todo** lo importante de una escena del crimen en una sola foto: dónde está la acción principal, hasta dónde llega el desorden y si hay algo sospechoso fuera de lugar. En estadística, esa foto es el **Diagrama de Caja**. Te muestra el centro, la dispersión y los valores extraños (outliers) en un solo dibujo compacto.

---

## 🎯 ¿Qué vas a aprender?

- Construir un diagrama de caja a partir de una lista de datos.
- Identificar sus cinco componentes clave (Mínimo, $Q_1$, Mediana, $Q_3$, Máximo).
- Detectar outliers visual y matemáticamente.
- Comparar dos grupos con solo mirar sus gráficos.

---

## La Anatomía de la Caja

Un diagrama de caja se construye con los cuartiles y consta de:
1.  **La Caja:** Va de $Q_1$ a $Q_3$. Contiene el **50% central** de los datos.
2.  **La Línea:** Dentro de la caja, marca la **Mediana ($Q_2$)**.
3.  **Los Bigotes:** Se extienden desde la caja hasta los valores mínimo y máximo (que no sean outliers).
4.  **Los Puntos:** Valores atípicos (**Outliers**) que están demasiado lejos.

---

## Construcción Paso a Paso

Supongamos estos datos ordenados:
$$ 1, 2, 5, 6, 7, 8, 8, 10, 12, 15, 25 $$

### Paso 1: Los 5 Números Resumen
1.  **Mínimo:** 1
2.  **$Q_1$:** (Pos 3) $\to$ **5**
3.  **Mediana ($Q_2$):** (Pos 6) $\to$ **8**
4.  **$Q_3$:** (Pos 9) $\to$ **12**
5.  **Máximo:** 25

### Paso 2: Calcular el Rango Intercuartílico (IQR)
$$ IQR = Q_3 - Q_1 = 12 - 5 = 7 $$

### Paso 3: Barreras de Outliers
- **Límite Inferior:** $Q_1 - 1.5(IQR) = 5 - 1.5(7) = 5 - 10.5 = -5.5$.
- **Límite Superior:** $Q_3 + 1.5(IQR) = 12 + 10.5 = 22.5$.

### Paso 4: Identificar Outliers
¿Hay datos fuera de $[-5.5, 22.5]$?
Sí, el **25** es mayor que 22.5. Es un **Outlier**.

### Paso 5: Ajustar Bigotes
- **Bigote Izquierdo:** Hasta el dato mínimo dentro del límite (1).
- **Bigote Derecho:** Hasta el dato máximo dentro del límite (15). (No hasta el 22.5, ni hasta el 25).

### Resultado Visual
```
      (Bigote)   [   Caja   ]   (Bigote)      (Outlier)
      1 ------- 5 ----|---- 12 ------- 15         * 25
                      8
```

---

## Interpretación de Formas

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Simetría Perfecta
**Forma:** La línea de la mediana está justo en el centro de la caja. Los bigotes son igual de largos.
**Significado:** Datos en campana (Normales).

#### Ejemplo 2: Sesgo a la Derecha
**Forma:** La caja es corta a la izquierda y larga a la derecha. El bigote derecho es muy largo.
**Significado:** La mayoría está "pegada" a valores bajos, pero hay una cola larga de valores altos.

#### Ejemplo 3: Caja Pequeña vs Grande
**Comparación:** Caja A mide 2 cm. Caja B mide 10 cm.
**Significado:** Los datos del grupo A son mucho más homogéneos (compactos) que los de B.

#### Ejemplo 4: Mediana Desplazada
**Forma:** La línea está pegada a $Q_3$ (parte superior de la caja).
**Significado:** El 25% de los datos entre mediana y $Q_3$ están muy apretados. Hay alta densidad ahí.

#### Ejemplo 5: Comparación Lado a Lado
**Salarios Hombres vs Mujeres**
- La caja de Hombres está más arriba que la de Mujeres.
- La mediana de Hombres supera al $Q_3$ de Mujeres.
**Conclusión visual:** El hombre "promedio" gana más que el 75% de las mujeres. (Análisis visual potente).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el IQR si $Q_1=10$ y $Q_3=20$.

<details>
<summary>Ver solución</summary>

**Resta:** $20 - 10 = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 2
Si el límite superior es 100, y tienes un dato en 105, ¿cómo se dibuja?

<details>
<summary>Ver solución</summary>

**Regla:** Es outlier.
**Resultado:** $\boxed{\text{Como un punto externo}}$

</details>

### Ejercicio 3
En un diagrama, la caja va de 5 a 15. ¿Entre qué valores está el 50% central?

<details>
<summary>Ver solución</summary>

**Definición:** La caja ES el 50% central.
**Resultado:** $\boxed{5 \text{ y } 15}$

</details>

### Ejercicio 4
Si no hay outliers, ¿hasta dónde llegan los bigotes?

<details>
<summary>Ver solución</summary>

**Regla:** Hasta el Mínimo y Máximo reales.
**Resultado:** $\boxed{\text{Min y Max}}$

</details>

### Ejercicio 5
¿Qué porcentaje de datos queda fuera de la caja (sumando ambos lados)?

<details>
<summary>Ver solución</summary>

**Análisis:** Dentro hay 50%. Fuera queda el resto.
**Resultado:** $\boxed{50\%}$

</details>

### Ejercicio 6
Observas una caja muy aplastada (corta). ¿Qué indica sobre la dispersión?

<details>
<summary>Ver solución</summary>

**Interpretación:** Poca dispersión (Baja varianza).
**Resultado:** $\boxed{\text{Datos muy concentrados}}$

</details>

### Ejercicio 7
Si la mediana es 10 y $Q_1=2$, $Q_3=11$. ¿Hacia dónde es el sesgo?

<details>
<summary>Ver solución</summary>

**Distancias:**
- $Q_1$ a Mediana: $10-2=8$.
- Mediana a $Q_3$: $11-10=1$.
**Análisis:** La parte izquierda es mucho más larga.
**Resultado:** $\boxed{\text{Sesgo a la Izquierda}}$

</details>

### Ejercicio 8
¿El diagrama de caja muestra el promedio ($\bar{x}$)?

<details>
<summary>Ver solución</summary>

**Teoría:** No explícitamente (muestra mediana). A veces programas lo añaden con una "x" o punto extra.
**Resultado:** $\boxed{\text{No necesariamente}}$

</details>

### Ejercicio 9
Calcula el límite superior para outliers si $Q_3=50$ e $IQR=10$.

<details>
<summary>Ver solución</summary>

**Fórmula:** $50 + 1.5(10) = 50 + 15$.
**Resultado:** $\boxed{65}$

</details>

### Ejercicio 10
Tienes dos diagramas. El A está contenido totalmente dentro del rango del B. ¿Cuál tiene mayor dispersión?

<details>
<summary>Ver solución</summary>

**Visual:** B abarca más espacio.
**Resultado:** $\boxed{B}$

</details>

---

## 🔑 Resumen

| Elemento | Definición Gráfica | Significado Estadístico |
|----------|--------------------|-------------------------|
| **Caja** | Rectángulo central. | Rango Intercuartílico ($Q_3-Q_1$). |
| **Línea** | Corte dentro de la caja. | Mediana ($Q_2$). |
| **Bigote** | Línea externa. | Alcance de datos normales. |
| **Punto** | Fuera del bigote. | Outlier (Dato atípico). |

> **Conclusión:** El BoxPlot es el mejor amigo para comparar grupos. En un segundo te dice quién gana (posición), quién es más consistente (ancho de caja) y quién tiene "ovejas negras" (outliers).

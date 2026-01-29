# **Método Gráfico**

A veces una imagen vale más que mil cálculos. El método gráfico consiste en dibujar las dos rectas en el plano cartesiano y ver exactamente dónde se cruzan. Aunque es menos preciso que el álgebra pura, es excelente para entender qué está pasando realmente.

---

## 🎯 ¿Qué vas a aprender?

- Cómo transformar ecuaciones para poder graficarlas fácilmente.
- Hallar la solución visual (`intersección`) de un sistema.
- Identificar rectas paralelas o coincidentes visualmente.
- Las limitaciones de precisión de este método.

---

## 🎨 Pasos del Método Gráfico

Para resolver un sistema visualmente:

1.  **Despejar $y$:** Dejar ambas ecuaciones en la forma `y = mx + b`.
2.  **Graficar:** Dibujar cada recta usando la pendiente `m` y el intercepto `b`.
3.  **Localizar:** Encontrar el punto $(x, y)$ donde se cortan.
4.  **Verificar:** Probar ese punto en las ecuaciones originales.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Solución Entera

Resolver gráficamente:
$$
\left\{
\begin{array}{ll}
x + y = 4 \\
x - y = 2
\end{array}
\right.
$$

**Paso 1: Despejar $y$**
- Ecuación 1: $y = -x + 4$ (Empieza en 4, baja 1 por cada 1 a la derecha).
- Ecuación 2: $y = x - 2$ (Empieza en -2, sube 1 por cada 1 a la derecha).

**Paso 2: Graficar y buscar el cruce**
Al dibujar ambas líneas, vemos que se cruzan exactamente en:

**Resultado:**
$$
\boxed{x = 3, \quad y = 1}
$$

![Gráfica del sistema x+y=4, x-y=2](/images/matematicas/algebra/sistemas-ecuaciones/ejemplo1-sistema.svg)

---

### Ejemplo 2: Intersección en el Primer Cuadrante

Resolver:
$$
\left\{
\begin{array}{ll}
2x + y = 6 \\
x - y = 0
\end{array}
\right.
$$

**Paso 1: Despejar $y$**
- Ecuación 1: $y = -2x + 6$
- Ecuación 2: $y = x$ (Pasa por el origen).

**Paso 2: Análisis Visual**
La primera recta baja rápido desde 6. La segunda sube en diagonal perfecta. Se encuentran en:

**Resultado:**
$$
\boxed{x = 2, \quad y = 2}
$$

![Gráfica del sistema 2x+y=6, x-y=0](/images/matematicas/algebra/sistemas-ecuaciones/ejemplo2-sistema.svg)

---

### Ejemplo 3: Rectas Ya Despejadas

Resolver:
$$
\left\{
\begin{array}{ll}
y = 2x - 1 \\
y = -x + 5
\end{array}
\right.
$$

**Razonamiento:**
Ya están listas para graficar.
- Recta 1: Sube empinada ($m=2$).
- Recta 2: Baja suave ($m=-1$).

**Resultado:**
$$
\boxed{x = 2, \quad y = 3}
$$

![Gráfica del sistema y=2x-1, y=-x+5](/images/matematicas/algebra/sistemas-ecuaciones/ejemplo3-sistema.svg)

---

### Ejemplo 4: El Caso de las Paralelas

Resolver:
$$
\left\{
\begin{array}{ll}
y = 2x + 1 \\
y = 2x - 3
\end{array}
\right.
$$

**Razonamiento:**
Observamos que ambas tienen $m=2$.
- Recta 1: Sube con pendiente 2.
- Recta 2: También sube con pendiente 2, pero más abajo.

Como son rieles de tren, nunca se tocarán.

**Resultado:**
$$
\boxed{\text{Sin solución (Sistema Incompatible)}}
$$

![Gráfica de sistema incompatible](/images/matematicas/algebra/sistemas-ecuaciones/ejemplo4-incompatible.svg)

---

### Ejemplo 5: El Caso del Camuflaje

Resolver:
$$
\left\{
\begin{array}{ll}
x + y = 3 \\
2x + 2y = 6
\end{array}
\right.
$$

**Razonamiento:**
Si despejamos ambas:
- Ecuación 1: $y = -x + 3$
- Ecuación 2: $2y = -2x + 6 \implies y = -x + 3$

¡Son la misma ecuación! Al graficar, pintarás una línea encima de la otra.

**Resultado:**
$$
\boxed{\text{Infinitas soluciones}}
$$

![Gráfica de sistema indeterminado](/images/matematicas/algebra/sistemas-ecuaciones/ejemplo5-indeterminado.svg)

---

## ⚖️ Pros y Contras del Método

| Ventajas | Desventajas |
|:--- |:--- |
| **Visual:** Entiendes qué significa la solución. | **Impreciso:** Difícil ver si la respuesta es $2.1$ o $2.05$. |
| **Rápido:** Para verificar si hay solución. | **Lento:** Dibujar toma tiempo si no hay software. |
| **Intuitivo:** Detecta paralelas al instante. | **Limitado:** Solo práctico en 2D (2 incógnitas). |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En el sistema $\begin{cases} y = x \\ y = -x + 2 \end{cases}$, ¿dónde se cruzan?

<details>
<summary>Ver solución</summary>

Cruzan en $(1, 1)$. Si subes 1 y bajas 1 desde 2, llegas al mismo sitio.
**Resultado:** $\boxed{(1, 1)}$

</details>

---

### Ejercicio 2
Si graficas dos rectas y ves que son perfectamente verticales y distintas (ej. $x=2$ y $x=5$), ¿cuál es la solución?

<details>
<summary>Ver solución</summary>

Son paralelas verticales.
**Resultado:** $\boxed{\text{Sin solución}}$

</details>

---

### Ejercicio 3
¿Cuál es la pendiente de $y = 3x - 2$?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{m = 3}$

</details>

---

### Ejercicio 4
Si el punto de intersección es $(3, 0)$, ¿cuánto vale $y$?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{0}$

</details>

---

### Ejercicio 5
Grafica mentalmente: $y=2$ y $x=3$. ¿Dónde se cruzan?

<details>
<summary>Ver solución</summary>

Una es horizontal a altura 2, la otra vertical en 3.
**Resultado:** $\boxed{(3, 2)}$

</details>

---

### Ejercicio 6
Para graficar $2x + 3y = 6$ usando interceptos, si $x=0$, ¿cuánto vale $y$?

<details>
<summary>Ver solución</summary>

$3y = 6 \implies y = 2$
**Resultado:** $\boxed{2}$

</details>

---

### Ejercicio 7
¿Por qué el método gráfico no es bueno para resolver $\begin{cases} y = 100x \\ y = 100x + 0.1 \end{cases}$?

<details>
<summary>Ver solución</summary>

Porque las líneas estarían demasiado juntas para distinguirlas a ojo y requerirían una escala gigante.

</details>

---

### Ejercicio 8
Si las rectas se cruzan en el tercer cuadrante, ¿cómo son los signos de la solución?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{(-, -)}$

</details>

---

### Ejercicio 9
Transforma $x - y = 0$ a la forma pendiente-intercepto.

<details>
<summary>Ver solución</summary>

$-y = -x \implies y = x$
**Resultado:** $\boxed{y = x}$

</details>

---

### Ejercicio 10
Si obtienes las rectas $y = x + 1$ y $y = x + 2$, ¿qué concluyes?

<details>
<summary>Ver solución</summary>

Pendientes iguales ($m=1$) e interceptos distintos.
**Resultado:** $\boxed{\text{Incompatible (Sin solución)}}$

</details>

---

## 🔑 Resumen

| Paso | Acción |
|:--- |:--- |
| **1. Despejar** | Aislar $y$ en ambas ecuaciones. |
| **2. Graficar** | Dibujar las líneas (usando $m$ y $b$ o tabla). |
| **3. Mirar** | El punto de cruce es el tesoro. |

> **Conclusión:** El método gráfico es tu brújula. Quizás no te dé las coordenadas con 10 decimales, pero siempre te dirá hacia dónde está el norte (o si el norte existe).

# **Gráficas de Funciones Cuadráticas**

Ya sabemos resolver la ecuación, ahora vamos a *verla*. Graficar una parábola puede parecer arte, pero en realidad es seguir una receta. Con solo tres puntos clave (el vértice y los cortes con los ejes), puedes dibujar cualquier curva cuadrática sin necesidad de una computadora.

---

## 🎯 ¿Qué vas a aprender?

- Cómo dibujar una parábola perfecta usando puntos clave.
- Pasar de la forma estándar ($ax^2+bx+c$) a la forma vértice.
- Leer la gráfica: dónde sube, dónde baja y dónde alcanza su límite.
- Entender el eje de simetría (el espejo de la parábola).

---

## 🗺️ El Mapa del Tesoro

Para no dibujar "a ciegas", necesitamos encontrar los **4 Puntos Vitales** de la parábola. Si los tienes, el dibujo sale solo.

![El Mapa del Tesoro: Elementos Clave](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/grafica_mapa_tesoro.svg)

1.  **Orientación:** ¿Arriba o abajo? (Depende del signo de $a$).
2.  **Vértice ($V$):** El punto exacto donde da la vuelta.
3.  **Corte con Y:** Donde cruza el eje vertical (la altura inicial).
4.  **Raíces (Cortes con X):** Donde cruza el suelo (si es que lo hace).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Parábola Completa
Graficar $f(x) = x^2 - 4x + 3$.

**Paso 1: ¿Hacia dónde mira?**
$a = 1$. Como es positivo ($+$), abre hacia **arriba** (🙂).

**Paso 2: Encontrar el Vértice**
El vértice tiene dos coordenadas $(x, y)$.
- **Para la $x$:** Usamos la fórmula sagrada $x_v = \frac{-b}{2a}$.
  $$
  x_v = \frac{-(-4)}{2(1)} = \frac{4}{2} = 2
  $$
- **Para la $y$:** "Enchufamos" ese 2 en la ecuación original.
  $$
  y_v = (2)^2 - 4(2) + 3 = 4 - 8 + 3 = -1
  $$
📌 **Vértice:** $(2, -1)$.

**Paso 3: Cortes con los ejes**
- **Eje Y:** Es el valor de $c$. Aquí $c=3$. Punto $(0, 3)$.
- **Eje X:** Factorizamos $x^2 - 4x + 3 = 0$.
  $(x-3)(x-1)=0 \implies x=3, x=1$.

![Gráfica Ejemplo 1](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/grafica_ex1.svg)

---

### Ejemplo 2: Parábola Invertida
Graficar $f(x) = -x^2 + 2x + 3$.

**1. Orientación:**
$a = -1$. Negativo ($-$), abre hacia **abajo** (☹️).

**2. Vértice:**
- $x_v = \frac{-2}{2(-1)} = \frac{-2}{-2} = 1$.
- $y_v = -(1)^2 + 2(1) + 3 = -1 + 2 + 3 = 4$.
📌 **Vértice:** $(1, 4)$.

**3. Cortes:**
- **Corte Y:** $c=3$. Punto $(0, 3)$.
- **Cortes X:** $-x^2 + 2x + 3 = 0$. Multiplicamos por $-1$: $x^2 - 2x - 3 = 0$.
  $(x-3)(x+1) = 0 \implies x=3, x=-1$.

![Gráfica Ejemplo 2](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/grafica_ex2.svg)

---

### Ejemplo 3: Sin Raíces Reales
Graficar $f(x) = x^2 + 2x + 2$.

**1. Vértice:**
- $a=1, b=2$.
- $x_v = \frac{-2}{2(1)} = -1$.
- $y_v = (-1)^2 + 2(-1) + 2 = 1 - 2 + 2 = 1$.
📌 **Vértice:** $(-1, 1)$.

**2. Análisis Visual:**
El vértice está en altura $1$ (por encima del suelo) y la parábola abre hacia **arriba**.
¿Conclusión? ¡Nunca tocará el suelo! No tiene cortes con X.

**3. Puntos de Ayuda:**
- Corte Y: $(0, 2)$.
- Por simetría: Si del vértice $(-1, 1)$ damos un paso a la derecha y subimos a 2, entonces un paso a la izquierda $(-2)$ también subirá a 2. Punto $(-2, 2)$.

![Gráfica Ejemplo 3](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/grafica_ex3.svg)

---

### Ejemplo 4: Forma Vértice
Graficar $f(x) = 2(x-1)^2 - 3$.

A veces la ecuación viene "pre-cocinada" en la forma $a(x-h)^2 + k$.
¡Es la mejor forma! No hay que calcular nada.

- **Vértice:** $(h, k) = (1, -3)$. (Nota: al número dentro del paréntesis se le cambia el signo).
- **Orientación:** $a=2$ (Abre arriba y es estrecha).

**Puntos extra:**
Si $x=0 \implies y = 2(-1)^2 - 3 = 2(1) - 3 = -1$. Punto $(0, -1)$.
Su gemelo simétrico estará en $x=2$ con la misma altura $-1$.

![Gráfica Ejemplo 4](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/grafica_ex4.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el vértice de $y = x^2 - 6x + 5$.

<details>
<summary>Ver solución</summary>

$x_v = 3$, $y_v = -4$.
**Resultado:** $\boxed{(3, -4)}$

</details>

---

### Ejercicio 2
¿Dónde corta al eje Y la función $f(x) = -3x^2 + 7$?

<details>
<summary>Ver solución</summary>

En $x=0, y=7$.
**Resultado:** $\boxed{(0, 7)}$

</details>

---

### Ejercicio 3
¿Cuáles son las raíces de $y = x^2 - 9$?

<details>
<summary>Ver solución</summary>

$x^2=9$.
**Resultado:** $\boxed{3, -3}$

</details>

---

### Ejercicio 4
Escribe la ecuación del eje de simetría de $y = (x-2)^2 + 5$.

<details>
<summary>Ver solución</summary>

Pasa por el vértice $x=2$.
**Resultado:** $\boxed{x=2}$

</details>

---

### Ejercicio 5
Si el vértice es $(1, 3)$ y pasa por $(0, 4)$, encuentra el punto simétrico.

<details>
<summary>Ver solución</summary>

El simétrico de $x=0$ respecto a $x=1$ es $x=2$. La altura $y$ es la misma.
**Resultado:** $\boxed{(2, 4)}$

</details>

---

### Ejercicio 6
Convierte $y = x^2 + 4x + 4$ a forma vértice.

<details>
<summary>Ver solución</summary>

Es un trinomio cuadrado perfecto: $(x+2)^2$.
**Resultado:** $\boxed{y = (x+2)^2}$

</details>

---

### Ejercicio 7
¿Tiene máximo o mínimo la función $y = -5(x+1)^2 - 2$?

<details>
<summary>Ver solución</summary>

$a=-5$, abre abajo.
**Resultado:** $\boxed{\text{Máximo}}$

</details>

---

### Ejercicio 8
Encuentra el vértice de $y = -2x^2 + 8x$.

<details>
<summary>Ver solución</summary>

$x_v = -8/-4 = 2$.
$y_v = -2(4)+16 = 8$.
**Resultado:** $\boxed{(2, 8)}$

</details>

---

### Ejercicio 9
Determina si la parábola $y = x^2 + 10$ corta al eje X.

<details>
<summary>Ver solución</summary>

Vértice en $(0, 10)$, abre arriba. Nunca baja al eje X.
**Resultado:** $\boxed{\text{No}}$

</details>

---

### Ejercicio 10
Grafica mentalmente: vértice en $(0,0)$ y pasa por $(1,1)$. ¿Cuál es la función?

<details>
<summary>Ver solución</summary>

La parábola básica.
**Resultado:** $\boxed{y = x^2}$

</details>

---

## 🔑 Resumen

| Pista | Qué nos dice |
|:--- |:--- |
| **Vértice** | El punto de partida de la gráfica. |
| **Eje de Simetría** | La línea vertical $x = x_v$ actúa como un espejo. |
| **Raíces** | Los puntos sobre el suelo (eje X). |

> **Conclusión:** Dibujar una parábola no requiere talento artístico, solo saber encontrar sus puntos vitales. El vértice es la cabeza y los interceptos son los pies sobre la tierra.

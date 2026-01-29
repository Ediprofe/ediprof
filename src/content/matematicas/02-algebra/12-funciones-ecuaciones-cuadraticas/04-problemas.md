# **Problemas con Ecuaciones Cuadráticas**

La vida no siempre es lineal. A veces, para optimizar el espacio de tu sala, calcular la trayectoria de un lanzamiento o maximizar ganancias, necesitas pensar al cuadrado. Aquí aprenderás a traducir problemas reales al lenguaje de las parábolas.

---

## 🎯 ¿Qué vas a aprender?

- Cómo plantear ecuaciones cuadráticas a partir de texto.
- Resolver problemas de áreas de figuras geométricas.
- Calcular lanzamientos de proyectiles (física básica).
- Encontrar números mágicos a partir de sus sumas y productos.

---

## 🏗️ La Física del "Vértice" y las "Raíces"

- **Vértice ($V$):** El punto máximo o mínimo. En problemas, representa la "altura máxima", la "ganancia máxima" o el "costo mínimo".
- **Raíces ($x$):** Cuando $y=0$. En problemas, representa "cuándo cae al suelo", "cuándo se acaba el dinero" o las medidas físicas de un objeto.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Rectángulo Misterioso
El largo de una cancha es 4 metros más que su ancho. Su área total es de 96 m². ¿Cuánto mide de ancho?

![Problema del Rectángulo](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/problemas_ex1_rectangulo.svg)

**1. Definir variables:**
- Ancho: $x$
- Largo: $x + 4$

**2. Plantear ecuación (Área = base × altura):**
$$
x(x + 4) = 96
$$
$$
x^2 + 4x - 96 = 0
$$

**3. Resolver (Factorización):**
Buscamos dos números que multiplicados den -96 y sumados 4. Son 12 y -8.
$$
(x + 12)(x - 8) = 0
$$
- $x = -12$ (Descartado, ¡distancias no son negativas!)
- $x = 8$

**Resultado:**
$$
\boxed{\text{Ancho: } 8 \text{ m, Largo: } 12 \text{ m}}
$$

---

### Ejemplo 2: El Cohete de Juguete
Se lanza un cohete hacia arriba. Su altura $h$ (en metros) después de $t$ segundos es:
$$
h(t) = -5t^2 + 30t
$$
¿En qué momento alcanza su altura máxima y cuál es esa altura?

**Razonamiento:**
La "altura máxima" es el **vértice** de la parábola (que abre hacia abajo porque $a=-5$).

**1. Calcular tiempo ($x_v$):**
$$
t = \frac{-b}{2a} = \frac{-30}{2(-5)} = \frac{-30}{-10} = 3
$$
El cohete sube durante 3 segundos.

**2. Calcular altura ($y_v$):**
$$
h(3) = -5(3)^2 + 30(3) = -45 + 90 = 45
$$

**Resultado:**
$$
\boxed{\text{Alos 3 segundos, alcanza 45 metros}}
$$

![Trayectoria del Cohete](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/problemas_ex2_cohete.svg)

---

### Ejemplo 3: Números Consecutivos
El producto de dos números enteros positivos consecutivos es 156. ¿Cuáles son?

**1. Variables:**
- Primer número: $n$
- Segundo número: $n + 1$

**2. Ecuación:**
$$
n(n + 1) = 156
$$
$$
n^2 + n - 156 = 0
$$

**3. Resolver:**
Usamos fórmula general o tanteamos factores de 156 ($12 \times 13 = 156$).
$$
(n + 13)(n - 12) = 0
$$
- $n = -13$ (Descartado, piden positivos)
- $n = 12$

**Resultado:**
$$
\boxed{\text{Los números son 12 y 13}}
$$

---

### Ejemplo 4: El Marco de la Foto
Una foto mide $10 \times 15$ cm. Se le pone un marco de ancho constante $x$. Si el área total (foto + marco) es 266 cm², ¿cuánto mide el ancho del marco?

![Esquema del Marco](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/problemas_ex4_marco.svg)

**1. Dimensiones totales:**
- Nuevo largo: $15 + 2x$ (se suma $x$ a cada lado)
- Nuevo ancho: $10 + 2x$

**2. Ecuación:**
$$
(15 + 2x)(10 + 2x) = 266
$$
$$
150 + 30x + 20x + 4x^2 = 266
$$
$$
4x^2 + 50x + 150 - 266 = 0
$$
$$
4x^2 + 50x - 116 = 0
$$

**3. Simplificar (dividir por 2):**
$$
2x^2 + 25x - 58 = 0
$$

**4. Fórmula General:**
$$
x = \frac{-25 \pm \sqrt{625 - 4(2)(-58)}}{4}
$$
$$
x = \frac{-25 \pm \sqrt{625 + 464}}{4} = \frac{-25 \pm \sqrt{1089}}{4} = \frac{-25 \pm 33}{4}
$$
- $x = (-25 + 33)/4 = 8/4 = 2$
- $x = (-25-33)/4$ (Negativo, descartado)

**Resultado:**
$$
\boxed{\text{El marco mide 2 cm de ancho}}
$$

---

### Ejemplo 5: Caída Libre
Se deja caer una piedra desde un edificio de 80 m. Su altura es $h(t) = 80 - 5t^2$. ¿Cuándo toca el suelo?

**Razonamiento:**
"Tocar el suelo" significa altura cero ($h=0$).

**Ecuación:**
$$
80 - 5t^2 = 0
$$
$$
80 = 5t^2 \implies 16 = t^2
$$
$$
t = \pm 4
$$
El tiempo negativo no existe en este contexto.

**Resultado:**
$$
\boxed{\text{Toca el suelo a los 4 segundos}}
$$

![Gráfica Caída Libre](/images/matematicas/algebra/funciones-ecuaciones-cuadraticas/problemas_ex5_caida.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
El cuadrado de un número más el doble del mismo número es 24. ¿Cuál es?

<details>
<summary>Ver solución</summary>

$x^2 + 2x - 24 = 0 \implies (x+6)(x-4)=0$.
**Resultado:** $\boxed{4 \text{ o } -6}$

</details>

---

### Ejercicio 2
El área de un triángulo es 30 m². La base es 4 metros mayor que la altura. Halla la altura.

<details>
<summary>Ver solución</summary>

$h(h+4)/2 = 30 \implies h^2 + 4h - 60 = 0$.
$(h+10)(h-6)=0$. Descartamos negativo.
**Resultado:** $\boxed{6 \text{ m}}$

</details>

---

### Ejercicio 3
La suma de dos números es 20 y su producto es 96.

<details>
<summary>Ver solución</summary>

$x(20-x) = 96 \implies x^2 - 20x + 96 = 0$.
$(x-8)(x-12)=0$.
**Resultado:** $\boxed{8, 12}$

</details>

---

### Ejercicio 4
Un proyectil sigue $h(t) = -5t^2 + 40t$. ¿Cuándo vuelve al suelo?

<details>
<summary>Ver solución</summary>

$-5t(t-8) = 0$. $t=0$ (inicio) y $t=8$ (fin).
**Resultado:** $\boxed{8 \text{ s}}$

</details>

---

### Ejercicio 5
¿Cuál es la altura máxima del proyectil anterior?

<details>
<summary>Ver solución</summary>

Vértice en $t=4$. $h(4) = -5(16) + 160 = 80$.
**Resultado:** $\boxed{80 \text{ m}}$

</details>

---

### Ejercicio 6
Una piscina rectangular de $6 \times 8$ m tiene un borde de ancho $x$. Área total = 80.

<details>
<summary>Ver solución</summary>

$(6+2x)(8+2x) = 80$. Simplificando: $x^2 + 7x - 8 = 0$.
$(x+8)(x-1)=0$.
**Resultado:** $\boxed{1 \text{ m}}$

</details>

---

### Ejercicio 7
Halla un número tal que su cuadrado sea igual a 5 veces el número.

<details>
<summary>Ver solución</summary>

$x^2 = 5x \implies x(x-5) = 0$.
**Resultado:** $\boxed{0, 5}$

</details>

---

### Ejercicio 8
El triple del cuadrado de un número es 75.

<details>
<summary>Ver solución</summary>

$3x^2 = 75 \implies x^2 = 25$.
**Resultado:** $\boxed{5, -5}$

</details>

---

### Ejercicio 9
Una caja sin tapa se hace cortando esquinas de 4 cm de una lámina cuadrada. Si el volumen es 100 cm³, ¿lado original?

<details>
<summary>Ver solución</summary>

Base: $(x-8)$, Altura: 4.
$4(x-8)^2 = 100 \implies (x-8)^2 = 25$.
$x-8 = 5 \implies x = 13$.
**Resultado:** $\boxed{13 \text{ cm}}$

</details>

---

### Ejercicio 10
Dos trenes parten del mismo punto perpendicularmente. Después de una hora, están a 130 km de distancia. Uno va 70 km/h más rápido.

<details>
<summary>Ver solución</summary>

Pitágoras: $x^2 + (x+70)^2 = 130^2$.
$2x^2 + 140x + 4900 = 16900$.
$x^2 + 70x - 6000 = 0$.
$(x+120)(x-50)=0$.
Velocidades: 50 y 120.
**Resultado:** $\boxed{50 \text{ km/h}, 120 \text{ km/h}}$

</details>

---

## 🔑 Resumen

| Concepto Clave | En problemas significa... |
|:--- |:--- |
| **Raíces positivas** | Las respuestas físicas válidas (distancia, tiempo). |
| **Raíces negativas** | Generalmente se descartan (no hay tiempos negativos). |
| **Vértice** | El punto óptimo (máximo o mínimo). |

> **Conclusión:** Las ecuaciones cuadráticas son la matemática de la optimización y el movimiento. Si algo sube y baja, o tiene un área, probablemente hay una $x^2$ escondida.

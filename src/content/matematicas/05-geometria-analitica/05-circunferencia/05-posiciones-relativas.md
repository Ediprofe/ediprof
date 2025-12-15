# Posiciones Relativas entre Circunferencias y Rectas

¿Cómo puede una recta relacionarse con una circunferencia? Puede estar fuera, tocarla en un punto (tangente) o cortarla en dos puntos (secante). Estudiaremos estas posiciones y cómo determinarlas algebraicamente.

---

## 🎯 ¿Qué vas a aprender?

- Las tres posiciones relativas de una recta respecto a una circunferencia
- Cómo determinar la posición usando distancia
- Las posiciones relativas entre dos circunferencias

---

## 📖 Lo Esencial de Posiciones Relativas

### Recta y Circunferencia

| Posición | Condición (distancia $d$ del centro a la recta) |
|----------|------------------------------------------------|
| Exterior | $d > r$ |
| Tangente | $d = r$ |
| Secante | $d < r$ |

### Dos Circunferencias

| Posición | Condición ($d$ = distancia entre centros) |
|----------|-------------------------------------------|
| Externas | $d > r_1 + r_2$ |
| Tangentes externas | $d = r_1 + r_2$ |
| Secantes | $\|r_1 - r_2\| < d < r_1 + r_2$ |
| Tangentes internas | $d = \|r_1 - r_2\|$ |
| Una dentro de otra | $d < \|r_1 - r_2\|$ |
| Concéntricas | $d = 0$ |

---

## 📖 Recta y Circunferencia

Sea una circunferencia con centro $C$ y radio $r$, y una recta $\ell$.

La **distancia $d$** del centro a la recta determina la posición:

### Recta Exterior ($d > r$)

La recta no toca la circunferencia. No hay puntos de intersección.

### Recta Tangente ($d = r$)

La recta toca la circunferencia en exactamente **un punto**. Este punto se llama **punto de tangencia**.

### Recta Secante ($d < r$)

La recta corta la circunferencia en **dos puntos**.

---

## 📖 Ejemplos de Recta-Circunferencia

### ⚙️ Ejemplo 1: Determinar posición

Determina la posición de la recta $3x + 4y - 20 = 0$ respecto a la circunferencia $x^2 + y^2 = 9$.

**Datos:**
- Centro: $(0, 0)$
- Radio: $r = 3$
- Recta: $3x + 4y - 20 = 0$

**Distancia del centro a la recta:**
$$
d = \frac{|3(0) + 4(0) - 20|}{\sqrt{9 + 16}} = \frac{20}{5} = 4
$$

**Comparación:** $d = 4 > r = 3$

**Respuesta:** La recta es **exterior** a la circunferencia.

### ⚙️ Ejemplo 2: Recta tangente

Verifica que $y = x + \sqrt{2}$ es tangente a $x^2 + y^2 = 1$.

**Centro:** $(0, 0)$, **Radio:** $r = 1$

**Recta en forma general:** $x - y + \sqrt{2} = 0$

**Distancia:**
$$
d = \frac{|0 - 0 + \sqrt{2}|}{\sqrt{1 + 1}} = \frac{\sqrt{2}}{\sqrt{2}} = 1
$$

Como $d = r = 1$, la recta es **tangente**.

### ⚙️ Ejemplo 3: Recta secante

Determina la posición de $y = x$ respecto a $(x-3)^2 + (y-2)^2 = 25$.

**Centro:** $(3, 2)$, **Radio:** $r = 5$

**Recta:** $x - y = 0$

**Distancia:**
$$
d = \frac{|3 - 2 + 0|}{\sqrt{2}} = \frac{1}{\sqrt{2}} \approx 0.71
$$

Como $d \approx 0.71 < r = 5$, la recta es **secante**.

---

## 📖 Puntos de Intersección

Para encontrar los puntos de intersección entre una recta y una circunferencia:

1. Despeja una variable de la ecuación de la recta
2. Sustituye en la ecuación de la circunferencia
3. Resuelve la ecuación cuadrática resultante

### ⚙️ Ejemplo 4: Encontrar intersecciones

Encuentra los puntos de intersección de $y = x + 1$ con $x^2 + y^2 = 5$.

**Sustituyendo:**
$$
x^2 + (x + 1)^2 = 5
$$
$$
x^2 + x^2 + 2x + 1 = 5
$$
$$
2x^2 + 2x - 4 = 0
$$
$$
x^2 + x - 2 = 0
$$
$$
(x + 2)(x - 1) = 0
$$

$x = -2$ o $x = 1$

**Puntos:**
- $x = -2$: $y = -2 + 1 = -1$ → $(-2, -1)$
- $x = 1$: $y = 1 + 1 = 2$ → $(1, 2)$

---

## 📖 Dos Circunferencias

Sean dos circunferencias con centros $C_1$, $C_2$ y radios $r_1$, $r_2$.

La **distancia entre centros** $d = d(C_1, C_2)$ determina la posición.

### ⚙️ Ejemplo 5: Circunferencias externas

Circunferencia 1: Centro $(0, 0)$, radio $3$
Circunferencia 2: Centro $(10, 0)$, radio $4$

**Distancia:** $d = 10$

**Suma de radios:** $r_1 + r_2 = 7$

Como $d = 10 > 7$, son **externas** (no se tocan).

### ⚙️ Ejemplo 6: Tangentes externas

Circunferencia 1: Centro $(0, 0)$, radio $3$
Circunferencia 2: Centro $(8, 0)$, radio $5$

**Distancia:** $d = 8$

**Suma:** $r_1 + r_2 = 8$

Como $d = r_1 + r_2$, son **tangentes externas**.

### ⚙️ Ejemplo 7: Secantes

Circunferencia 1: Centro $(0, 0)$, radio $5$
Circunferencia 2: Centro $(4, 0)$, radio $3$

**Distancia:** $d = 4$

$|r_1 - r_2| = 2$ y $r_1 + r_2 = 8$

Como $2 < 4 < 8$, son **secantes** (se cortan en dos puntos).

---

## 🔑 Resumen

| Posición Recta-Circunferencia | Puntos de intersección |
|------------------------------|------------------------|
| Exterior | 0 |
| Tangente | 1 |
| Secante | 2 |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Determina la posición de $x + y = 10$ respecto a $x^2 + y^2 = 32$.

<details>
<summary>Ver solución</summary>

Centro: $(0, 0)$, Radio: $r = \sqrt{32} \approx 5.66$

Distancia: $d = \frac{|0 + 0 - 10|}{\sqrt{2}} = \frac{10}{\sqrt{2}} = 5\sqrt{2} \approx 7.07$

Como $d > r$, la recta es **exterior**.

</details>

### Ejercicio 2
¿La recta $4x - 3y = 0$ es tangente a $(x-4)^2 + (y-3)^2 = 25$?

<details>
<summary>Ver solución</summary>

Centro: $(4, 3)$, Radio: $r = 5$

Distancia: $d = \frac{|4(4) - 3(3) - 0|}{5} = \frac{|16 - 9|}{5} = \frac{7}{5} = 1.4$

Como $d = 1.4 < r = 5$, es **secante** (no tangente).

</details>

### Ejercicio 3
Encuentra los puntos de intersección de $y = 2$ con $x^2 + y^2 = 13$.

<details>
<summary>Ver solución</summary>

$x^2 + 4 = 13$
$x^2 = 9$
$x = \pm 3$

Puntos: $(3, 2)$ y $(-3, 2)$

</details>

### Ejercicio 4
Determina la posición entre las circunferencias con centros $(0, 0)$, $(5, 0)$ y radios $3$ y $4$.

<details>
<summary>Ver solución</summary>

$d = 5$
$r_1 + r_2 = 7$
$|r_1 - r_2| = 1$

Como $1 < 5 < 7$, son **secantes**.

</details>

### Ejercicio 5
¿Para qué valor de $k$ la recta $y = x + k$ es tangente a $x^2 + y^2 = 8$?

<details>
<summary>Ver solución</summary>

Recta: $x - y + k = 0$

Para ser tangente: $d = r$

$\frac{|k|}{\sqrt{2}} = \sqrt{8} = 2\sqrt{2}$

$|k| = 2\sqrt{2} \cdot \sqrt{2} = 4$

$k = 4$ o $k = -4$

</details>

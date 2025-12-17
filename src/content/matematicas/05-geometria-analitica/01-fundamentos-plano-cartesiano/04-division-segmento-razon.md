# División de un Segmento en una Razón Dada

El punto medio divide un segmento en dos partes **iguales**, pero ¿qué pasa si queremos dividirlo en partes **desiguales**? Por ejemplo, encontrar el punto que está a un tercio del camino, o a dos quintos. Para eso usamos la **división de un segmento en una razón dada**.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa dividir un segmento en una razón
- La fórmula de división del segmento
- Cómo aplicarla en diferentes casos

---

## 📖 Lo Esencial de División de Segmentos

| Concepto | Fórmula |
|----------|---------|
| Razón $r$ | $r = \dfrac{m}{n}$ donde $m + n$ = longitud total relativa |
| Punto $P$ que divide $\overline{AB}$ en razón $m:n$ | $P = \left(\dfrac{mx_2 + nx_1}{m + n}, \dfrac{my_2 + ny_1}{m + n}\right)$ |
| Caso especial: Punto medio | Cuando $m = n = 1$, $r = 1:1$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/division-segmento.svg" alt="División de un segmento en razón dada" style="width: 100%; height: auto;" />
</div>

---

## 📖 Concepto de Razón

Cuando decimos que un punto $P$ divide al segmento $\overline{AB}$ en la **razón $m:n$**, significa que:

$$
\frac{AP}{PB} = \frac{m}{n}
$$

Es decir, la distancia de $A$ a $P$ comparada con la distancia de $P$ a $B$ es como $m$ es a $n$.

### Ejemplos de razones:

| Razón | Significado |
|-------|-------------|
| $1:1$ | El punto está a la mitad (punto medio) |
| $1:2$ | El punto está a $\frac{1}{3}$ desde $A$ |
| $2:1$ | El punto está a $\frac{2}{3}$ desde $A$ |
| $3:2$ | El punto está a $\frac{3}{5}$ desde $A$ |

---

## 📖 Fórmula de División del Segmento

Dados los puntos $A(x_1, y_1)$ y $B(x_2, y_2)$, el punto $P(x, y)$ que divide al segmento $\overline{AB}$ en la razón $m:n$ es:

$$
P = \left(\frac{mx_2 + nx_1}{m + n}, \frac{my_2 + ny_1}{m + n}\right)
$$

> 💡 **Importante:** Los valores de $m$ y $n$ multiplican a las coordenadas del punto **contrario** (m multiplica a $x_2, y_2$ y n multiplica a $x_1, y_1$).

### ⚙️ Ejemplo 1: División en razón 1:2

Encuentra el punto $P$ que divide al segmento desde $A(1, 2)$ hasta $B(7, 8)$ en la razón $1:2$.

**Datos:**
- $A(1, 2)$ → $x_1 = 1$, $y_1 = 2$
- $B(7, 8)$ → $x_2 = 7$, $y_2 = 8$
- Razón: $m:n = 1:2$

**Aplicamos la fórmula:**

$$
x_P = \frac{1 \cdot 7 + 2 \cdot 1}{1 + 2} = \frac{7 + 2}{3} = \frac{9}{3} = 3
$$

$$
y_P = \frac{1 \cdot 8 + 2 \cdot 2}{1 + 2} = \frac{8 + 4}{3} = \frac{12}{3} = 4
$$

**Respuesta:** $P(3, 4)$

> Este punto está a $\frac{1}{3}$ del camino desde $A$ hacia $B$.

### ⚙️ Ejemplo 2: División en razón 2:3

Encuentra el punto que divide el segmento desde $A(-2, 1)$ hasta $B(8, 6)$ en la razón $2:3$.

**Datos:**
- $x_1 = -2$, $y_1 = 1$
- $x_2 = 8$, $y_2 = 6$
- $m:n = 2:3$

**Cálculo:**

$$
x_P = \frac{2 \cdot 8 + 3 \cdot (-2)}{2 + 3} = \frac{16 - 6}{5} = \frac{10}{5} = 2
$$

$$
y_P = \frac{2 \cdot 6 + 3 \cdot 1}{2 + 3} = \frac{12 + 3}{5} = \frac{15}{5} = 3
$$

**Respuesta:** $P(2, 3)$

---

## 📖 Verificación con el Punto Medio

Cuando $m = n = 1$, la razón es $1:1$ (el punto divide al segmento en partes iguales). Verifiquemos que la fórmula nos da el punto medio:

$$
P = \left(\frac{1 \cdot x_2 + 1 \cdot x_1}{1 + 1}, \frac{1 \cdot y_2 + 1 \cdot y_1}{1 + 1}\right) = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)
$$

¡Es exactamente la fórmula del punto medio! ✓

---

## 📖 División Externa

Los ejemplos anteriores son de **división interna** (el punto $P$ está **entre** $A$ y $B$).

En la **división externa**, el punto $P$ está **fuera** del segmento, en la prolongación de la recta $AB$.

Para la división externa, uno de los valores ($m$ o $n$) se considera **negativo**.

### ⚙️ Ejemplo 3: División externa

Encuentra el punto $P$ que divide externamente al segmento desde $A(2, 3)$ hasta $B(5, 9)$ en la razón $2:(-1)$ (o equivalentemente, en razón externa $2:1$).

**Datos:**
- $x_1 = 2$, $y_1 = 3$
- $x_2 = 5$, $y_2 = 9$
- $m = 2$, $n = -1$

**Cálculo:**

$$
x_P = \frac{2 \cdot 5 + (-1) \cdot 2}{2 + (-1)} = \frac{10 - 2}{1} = 8
$$

$$
y_P = \frac{2 \cdot 9 + (-1) \cdot 3}{2 + (-1)} = \frac{18 - 3}{1} = 15
$$

**Respuesta:** $P(8, 15)$ — Este punto está en la prolongación del segmento, más allá de $B$.

---

## 📖 Puntos de Trisección

Los **puntos de trisección** dividen un segmento en **tres partes iguales**.

Para encontrarlos, usamos las razones:
- Primer punto: razón $1:2$
- Segundo punto: razón $2:1$

### ⚙️ Ejemplo 4: Trisección de un segmento

Encuentra los puntos de trisección del segmento con extremos $A(0, 0)$ y $B(9, 12)$.

**Primer punto $T_1$ (razón 1:2):**

$$
x_{T_1} = \frac{1 \cdot 9 + 2 \cdot 0}{1 + 2} = \frac{9}{3} = 3
$$

$$
y_{T_1} = \frac{1 \cdot 12 + 2 \cdot 0}{1 + 2} = \frac{12}{3} = 4
$$

$T_1(3, 4)$

**Segundo punto $T_2$ (razón 2:1):**

$$
x_{T_2} = \frac{2 \cdot 9 + 1 \cdot 0}{2 + 1} = \frac{18}{3} = 6
$$

$$
y_{T_2} = \frac{2 \cdot 12 + 1 \cdot 0}{2 + 1} = \frac{24}{3} = 8
$$

$T_2(6, 8)$

**Respuesta:** Los puntos de trisección son $T_1(3, 4)$ y $T_2(6, 8)$.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| Razón $m:n$ | Indica cómo se divide el segmento |
| División interna | $P$ está entre $A$ y $B$; $m, n > 0$ |
| División externa | $P$ está fuera del segmento; un valor es negativo |
| Punto medio | Caso especial con razón $1:1$ |
| Puntos de trisección | Razones $1:2$ y $2:1$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el punto $P$ que divide el segmento de $A(2, 5)$ a $B(8, 11)$ en la razón $1:2$.

<details>
<summary>Ver solución</summary>

$$
x_P = \frac{1 \cdot 8 + 2 \cdot 2}{3} = \frac{8 + 4}{3} = \frac{12}{3} = 4
$$

$$
y_P = \frac{1 \cdot 11 + 2 \cdot 5}{3} = \frac{11 + 10}{3} = \frac{21}{3} = 7
$$

**Respuesta:** $P(4, 7)$

</details>

### Ejercicio 2
Encuentra el punto que divide el segmento desde $A(-4, 2)$ hasta $B(6, 7)$ en la razón $3:2$.

<details>
<summary>Ver solución</summary>

$$
x_P = \frac{3 \cdot 6 + 2 \cdot (-4)}{5} = \frac{18 - 8}{5} = \frac{10}{5} = 2
$$

$$
y_P = \frac{3 \cdot 7 + 2 \cdot 2}{5} = \frac{21 + 4}{5} = \frac{25}{5} = 5
$$

**Respuesta:** $P(2, 5)$

</details>

### Ejercicio 3
Encuentra los puntos de trisección del segmento con extremos $A(1, 2)$ y $B(7, 14)$.

<details>
<summary>Ver solución</summary>

**Primer punto (razón 1:2):**

$$
T_1 = \left(\frac{1 \cdot 7 + 2 \cdot 1}{3}, \frac{1 \cdot 14 + 2 \cdot 2}{3}\right) = \left(\frac{9}{3}, \frac{18}{3}\right) = (3, 6)
$$

**Segundo punto (razón 2:1):**

$$
T_2 = \left(\frac{2 \cdot 7 + 1 \cdot 1}{3}, \frac{2 \cdot 14 + 1 \cdot 2}{3}\right) = \left(\frac{15}{3}, \frac{30}{3}\right) = (5, 10)
$$

**Respuesta:** Los puntos de trisección son $T_1(3, 6)$ y $T_2(5, 10)$

</details>

### Ejercicio 4
Si el punto $P(5, 3)$ divide al segmento $\overline{AB}$ en razón $2:3$, y $A(1, -3)$, encuentra las coordenadas de $B$.

<details>
<summary>Ver solución</summary>

Usamos la fórmula y despejamos $B(x_2, y_2)$:

De $x_P = \frac{2x_2 + 3x_1}{5}$:

$$
5 = \frac{2x_2 + 3(1)}{5}
$$

$$
25 = 2x_2 + 3
$$

$$
x_2 = \frac{22}{2} = 11
$$

De $y_P = \frac{2y_2 + 3y_1}{5}$:

$$
3 = \frac{2y_2 + 3(-3)}{5}
$$

$$
15 = 2y_2 - 9
$$

$$
y_2 = \frac{24}{2} = 12
$$

**Respuesta:** $B(11, 12)$

</details>

### Ejercicio 5
¿En qué razón divide el punto $P(4, 5)$ al segmento desde $A(1, 2)$ hasta $B(10, 11)$?

<details>
<summary>Ver solución</summary>

Si $P$ divide a $\overline{AB}$ en razón $m:n$, entonces:

$$
4 = \frac{m \cdot 10 + n \cdot 1}{m + n}
$$

$$
4(m + n) = 10m + n
$$

$$
4m + 4n = 10m + n
$$

$$
3n = 6m
$$

$$
\frac{m}{n} = \frac{3}{6} = \frac{1}{2}
$$

**Respuesta:** La razón es $1:2$

</details>

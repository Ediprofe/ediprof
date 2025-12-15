# Familias de Circunferencias

Así como estudiamos familias de rectas, también existen **familias de circunferencias** que comparten ciertas propiedades. Estas familias son útiles para resolver problemas donde hay infinitas soluciones posibles.

---

## 🎯 ¿Qué vas a aprender?

- Familias de circunferencias con centro fijo
- Circunferencias concéntricas
- Haz de circunferencias (radical axis)

---

## 📖 Lo Esencial de Familias

| Familia | Característica | Parámetro |
|---------|---------------|-----------|
| Centro fijo | Mismo centro, radios variables | $r$ |
| Radio fijo | Diferentes centros, mismo radio | Centro |
| Concéntricas | Mismo centro | $r$ |
| Por un punto fijo | Pasan por un punto dado | Centro o radio |

---

## 📖 Circunferencias Concéntricas

Las **circunferencias concéntricas** tienen el mismo centro pero diferentes radios.

**Familia:** 
$$
(x - h)^2 + (y - k)^2 = r^2
$$

donde $(h, k)$ es fijo y $r$ varía.

### ⚙️ Ejemplo 1: Familia concéntrica

La familia de circunferencias con centro en $(2, 3)$:

$$
(x - 2)^2 + (y - 3)^2 = r^2
$$

Para $r = 1, 2, 3, ...$: círculos cada vez más grandes, todos con centro $(2, 3)$.

---

## 📖 Circunferencias por un Punto Fijo

Todas las circunferencias que pasan por un punto fijo $(a, b)$.

Si el centro es $(h, k)$, el radio debe satisfacer:

$$
r = \sqrt{(a - h)^2 + (b - k)^2}
$$

### ⚙️ Ejemplo 2: Circunferencias por el origen

La familia de circunferencias que pasan por el origen con centro en el eje X:

Centro: $(h, 0)$, pasa por $(0, 0)$, entonces $r = h$.

$$
(x - h)^2 + y^2 = h^2
$$

Expandiendo: $x^2 - 2hx + h^2 + y^2 = h^2$

$$
x^2 + y^2 - 2hx = 0
$$

donde $h$ es el parámetro.

---

## 📖 Circunferencias Tangentes a una Recta en un Punto

Las circunferencias tangentes a una recta en el punto $(a, b)$ tienen su centro sobre la recta perpendicular a la tangente que pasa por $(a, b)$.

### ⚙️ Ejemplo 3: Tangente al eje X

Circunferencias tangentes al eje X en el punto $(3, 0)$:

El centro está en la recta vertical $x = 3$: Centro = $(3, k)$

Como es tangente al eje X, $r = |k|$.

$$
(x - 3)^2 + (y - k)^2 = k^2
$$

donde $k \neq 0$ es el parámetro.

---

## 📖 Haz de Circunferencias

Dadas dos circunferencias:
- $C_1: x^2 + y^2 + D_1x + E_1y + F_1 = 0$
- $C_2: x^2 + y^2 + D_2x + E_2y + F_2 = 0$

El **haz de circunferencias** que pasan por sus puntos de intersección es:

$$
C_1 + \lambda C_2 = 0
$$

O más explícitamente:

$$
(x^2 + y^2 + D_1x + E_1y + F_1) + \lambda(x^2 + y^2 + D_2x + E_2y + F_2) = 0
$$

### ⚙️ Ejemplo 4: Haz de circunferencias

Las circunferencias $x^2 + y^2 - 4 = 0$ y $x^2 + y^2 - 2x - 2y = 0$ se intersectan.

**Haz:**
$$
(x^2 + y^2 - 4) + \lambda(x^2 + y^2 - 2x - 2y) = 0
$$

$$
(1 + \lambda)(x^2 + y^2) - 2\lambda x - 2\lambda y - 4 = 0
$$

Para $\lambda = -1$: obtenemos la **cuerda común** (eje radical).

---

## 📖 Eje Radical

El **eje radical** de dos circunferencias es el lugar geométrico de los puntos con igual potencia respecto a ambas circunferencias.

Para $C_1$ y $C_2$, el eje radical es:

$$
C_1 - C_2 = 0
$$

Esto da una **recta**.

### ⚙️ Ejemplo 5: Eje radical

Encuentra el eje radical de:
- $C_1: x^2 + y^2 - 4x - 6y + 9 = 0$
- $C_2: x^2 + y^2 - 2x - 4y + 1 = 0$

$$
C_1 - C_2 = (-4x + 2x) + (-6y + 4y) + (9 - 1) = 0
$$

$$
-2x - 2y + 8 = 0
$$

$$
x + y - 4 = 0
$$

---

## 📖 Circunferencias Ortogonales

Dos circunferencias son **ortogonales** si se cortan formando ángulos rectos.

**Condición:** Si $C_1$ tiene centro $O_1$, radio $r_1$ y $C_2$ tiene centro $O_2$, radio $r_2$:

$$
d^2 = r_1^2 + r_2^2
$$

donde $d$ es la distancia entre centros.

### ⚙️ Ejemplo 6: Verificar ortogonalidad

¿Son ortogonales $x^2 + y^2 = 4$ y $(x-2)^2 + y^2 = 4$?

- $C_1$: Centro $(0, 0)$, $r_1 = 2$
- $C_2$: Centro $(2, 0)$, $r_2 = 2$
- Distancia: $d = 2$

Verificamos: $d^2 = 4$, $r_1^2 + r_2^2 = 8$

Como $4 \neq 8$, **no son ortogonales**.

---

## 🔑 Resumen

| Familia | Ecuación |
|---------|----------|
| Concéntricas | $(x-h)^2 + (y-k)^2 = r^2$, $r$ variable |
| Haz por intersección | $C_1 + \lambda C_2 = 0$ |
| Eje radical | $C_1 - C_2 = 0$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la familia de circunferencias concéntricas con centro en $(-1, 4)$.

<details>
<summary>Ver solución</summary>

$$
(x + 1)^2 + (y - 4)^2 = r^2
$$

donde $r > 0$ es el parámetro.

</details>

### Ejercicio 2
De la familia de circunferencias que pasan por el origen y tienen centro en el eje Y, encuentra la que también pasa por $(0, 6)$.

<details>
<summary>Ver solución</summary>

Centro en $(0, k)$, pasa por el origen: $r = k$

$$
x^2 + (y - k)^2 = k^2
$$

Pasa por $(0, 6)$: $(6 - k)^2 = k^2$

$36 - 12k + k^2 = k^2$

$k = 3$

**Circunferencia:** $x^2 + (y - 3)^2 = 9$

</details>

### Ejercicio 3
Encuentra el eje radical de $x^2 + y^2 = 25$ y $x^2 + y^2 - 10x = 0$.

<details>
<summary>Ver solución</summary>

$C_1 - C_2$: $(x^2 + y^2 - 25) - (x^2 + y^2 - 10x) = 0$

$-25 + 10x = 0$

$x = 2.5$

</details>

### Ejercicio 4
Escribe el haz de circunferencias determinado por $x^2 + y^2 - 2 = 0$ y $x^2 + y^2 - 4x = 0$.

<details>
<summary>Ver solución</summary>

$(x^2 + y^2 - 2) + \lambda(x^2 + y^2 - 4x) = 0$

$(1 + \lambda)(x^2 + y^2) - 4\lambda x - 2 = 0$

</details>

### Ejercicio 5
¿Cuál es la condición para que dos circunferencias con centros $(0, 0)$ y $(5, 0)$ y radios $r_1$ y $r_2$ sean ortogonales?

<details>
<summary>Ver solución</summary>

Distancia entre centros: $d = 5$

Condición de ortogonalidad: $d^2 = r_1^2 + r_2^2$

$$
25 = r_1^2 + r_2^2
$$

</details>

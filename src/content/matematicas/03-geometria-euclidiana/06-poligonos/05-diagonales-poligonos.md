# Diagonales de Polígonos

Una **diagonal** es un segmento que une dos vértices no consecutivos de un polígono. El número de diagonales depende del número de lados.

---

## 📖 ¿Qué es una diagonal?

> **Definición:** Una diagonal es un segmento que une dos vértices de un polígono que **no son adyacentes** (no son consecutivos).

### Ejemplo

En un cuadrilátero $ABCD$:
- $\overline{AC}$ es diagonal (une vértices no consecutivos)
- $\overline{BD}$ es diagonal (une vértices no consecutivos)
- $\overline{AB}$ **no** es diagonal (es un lado)

---

## 📖 Fórmula del número de diagonales

El número de diagonales de un polígono de $n$ lados es:

$$
d = \frac{n(n-3)}{2}
$$

### ¿De dónde viene esta fórmula?

- Desde cada vértice se pueden trazar $(n-3)$ diagonales
- Hay $n$ vértices
- Cada diagonal se cuenta dos veces (una desde cada extremo)
- Por lo tanto: $d = \frac{n(n-3)}{2}$

---

## 📖 Tabla de diagonales

| Polígono | n | Diagonales |
|----------|---|------------|
| Triángulo | 3 | $\frac{3(0)}{2} = 0$ |
| Cuadrilátero | 4 | $\frac{4(1)}{2} = 2$ |
| Pentágono | 5 | $\frac{5(2)}{2} = 5$ |
| Hexágono | 6 | $\frac{6(3)}{2} = 9$ |
| Heptágono | 7 | $\frac{7(4)}{2} = 14$ |
| Octágono | 8 | $\frac{8(5)}{2} = 20$ |
| Decágono | 10 | $\frac{10(7)}{2} = 35$ |
| Dodecágono | 12 | $\frac{12(9)}{2} = 54$ |

---

## 📖 Propiedad: Diagonales desde un vértice

Desde un vértice cualquiera se pueden trazar exactamente $(n-3)$ diagonales.

### ¿Por qué $(n-3)$?

De los $n$ vértices:
- No se puede unir consigo mismo (1 vértice)
- No se puede unir con los vértices adyacentes (2 vértices)
- Quedan $n - 3$ vértices disponibles

### Ejemplos

| Polígono | n | Diagonales desde un vértice |
|----------|---|----------------------------|
| Cuadrilátero | 4 | $4 - 3 = 1$ |
| Pentágono | 5 | $5 - 3 = 2$ |
| Hexágono | 6 | $6 - 3 = 3$ |
| Octágono | 8 | $8 - 3 = 5$ |

---

## 📖 División en triángulos

Las diagonales trazadas desde **un solo vértice** dividen al polígono en $(n-2)$ triángulos.

### Ejemplo

Un hexágono (6 lados):
- Diagonales desde un vértice: 3
- Triángulos formados: $6 - 2 = 4$

Esta propiedad es la base de la fórmula para la suma de ángulos interiores.

---

## 📖 Todas las diagonales

Si trazamos **todas** las diagonales de un polígono convexo, el número de regiones internas puede ser muy grande.

Para un polígono convexo de $n$ lados, las diagonales pueden intersectarse en puntos internos, creando muchas regiones.

---

## 📖 Encontrar n conociendo las diagonales

Si conocemos el número de diagonales $d$, podemos encontrar $n$:

$$
d = \frac{n(n-3)}{2}
$$

$$
2d = n^2 - 3n
$$

$$
n^2 - 3n - 2d = 0
$$

Resolviendo con la fórmula cuadrática:

$$
n = \frac{3 + \sqrt{9 + 8d}}{2}
$$

### Ejemplo

Si $d = 20$:

$$
n = \frac{3 + \sqrt{9 + 160}}{2} = \frac{3 + \sqrt{169}}{2} = \frac{3 + 13}{2} = 8
$$

Es un **octágono**.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular diagonales

¿Cuántas diagonales tiene cada polígono?

1. Pentágono (5 lados)
2. Heptágono (7 lados)
3. Nonágono (9 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $d = \frac{5(5-3)}{2} = \frac{10}{2} = 5$
2. $d = \frac{7(7-3)}{2} = \frac{28}{2} = 14$
3. $d = \frac{9(9-3)}{2} = \frac{54}{2} = 27$

</details>

---

### Ejercicio 2: Diagonales desde un vértice

¿Cuántas diagonales se pueden trazar desde un vértice?

1. Hexágono
2. Decágono
3. Polígono de 15 lados

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $6 - 3 = 3$ diagonales
2. $10 - 3 = 7$ diagonales
3. $15 - 3 = 12$ diagonales

</details>

---

### Ejercicio 3: Encontrar el polígono

¿Cuántos lados tiene un polígono con...?

1. 9 diagonales
2. 35 diagonales
3. 44 diagonales

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{n(n-3)}{2} = 9 \Rightarrow n(n-3) = 18 \Rightarrow n = 6$ (hexágono)
2. $\frac{n(n-3)}{2} = 35 \Rightarrow n(n-3) = 70 \Rightarrow n = 10$ (decágono)
3. $\frac{n(n-3)}{2} = 44 \Rightarrow n(n-3) = 88 \Rightarrow n = 11$ (endecágono)

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Un triángulo tiene 0 diagonales.
2. Un cuadrilátero tiene 4 diagonales.
3. Desde cada vértice de un octágono se pueden trazar 5 diagonales.
4. Un pentágono tiene el mismo número de lados que de diagonales.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - No hay vértices no adyacentes
2. **Falso** - Tiene 2 diagonales
3. **Verdadero** - $8 - 3 = 5$
4. **Verdadero** - Tiene 5 lados y 5 diagonales

</details>

---

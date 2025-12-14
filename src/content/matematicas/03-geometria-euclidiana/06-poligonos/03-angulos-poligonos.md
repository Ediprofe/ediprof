# Ángulos en Polígonos

Los ángulos de un polígono siguen reglas matemáticas precisas. Conociendo el número de lados, podemos calcular la suma de los ángulos interiores y exteriores.

---

## 📖 Suma de ángulos interiores

> **Fórmula:** La suma de los ángulos interiores de un polígono de $n$ lados es:

$$
S = (n - 2) \times 180°
$$

### ¿Por qué funciona esta fórmula?

Desde un vértice podemos trazar diagonales que dividen el polígono en $(n-2)$ triángulos. Como cada triángulo tiene ángulos que suman 180°:

$$
\text{Suma total} = (n-2) \times 180°
$$

### Ejemplos

| Polígono | n | Suma de ángulos |
|----------|---|-----------------|
| Triángulo | 3 | $(3-2) \times 180° = 180°$ |
| Cuadrilátero | 4 | $(4-2) \times 180° = 360°$ |
| Pentágono | 5 | $(5-2) \times 180° = 540°$ |
| Hexágono | 6 | $(6-2) \times 180° = 720°$ |
| Octágono | 8 | $(8-2) \times 180° = 1080°$ |

---

## 📖 Ángulo interior de un polígono regular

En un polígono **regular**, todos los ángulos son iguales. Cada ángulo mide:

$$
\alpha = \frac{(n-2) \times 180°}{n}
$$

### Ejemplos

| Polígono regular | n | Ángulo interior |
|------------------|---|-----------------|
| Triángulo equilátero | 3 | $\frac{180°}{3} = 60°$ |
| Cuadrado | 4 | $\frac{360°}{4} = 90°$ |
| Pentágono | 5 | $\frac{540°}{5} = 108°$ |
| Hexágono | 6 | $\frac{720°}{6} = 120°$ |
| Octágono | 8 | $\frac{1080°}{8} = 135°$ |

---

## 📖 Suma de ángulos exteriores

> **Propiedad:** La suma de los ángulos exteriores de cualquier polígono convexo es siempre **360°**.

$$
\text{Suma de ángulos exteriores} = 360°
$$

Esta propiedad es válida para **todos** los polígonos convexos, sin importar el número de lados.

---

## 📖 Ángulo exterior de un polígono regular

En un polígono regular, cada ángulo exterior mide:

$$
\beta = \frac{360°}{n}
$$

### Ejemplos

| Polígono regular | n | Ángulo exterior |
|------------------|---|-----------------|
| Triángulo equilátero | 3 | $\frac{360°}{3} = 120°$ |
| Cuadrado | 4 | $\frac{360°}{4} = 90°$ |
| Pentágono | 5 | $\frac{360°}{5} = 72°$ |
| Hexágono | 6 | $\frac{360°}{6} = 60°$ |
| Octágono | 8 | $\frac{360°}{8} = 45°$ |

---

## 📖 Relación ángulo interior - exterior

El ángulo interior y el ángulo exterior en cada vértice son **suplementarios**:

$$
\alpha + \beta = 180°
$$

### Verificación

Para un hexágono regular:
- Ángulo interior: $120°$
- Ángulo exterior: $60°$
- Suma: $120° + 60° = 180°$ ✓

---

## 📖 Encontrar el número de lados

Si conocemos un ángulo, podemos encontrar $n$:

### Conociendo el ángulo interior

$$
n = \frac{360°}{180° - \alpha}
$$

### Conociendo el ángulo exterior

$$
n = \frac{360°}{\beta}
$$

### Ejemplo

Si el ángulo exterior de un polígono regular es $30°$:

$$
n = \frac{360°}{30°} = 12 \text{ lados (dodecágono)}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Suma de ángulos interiores

Calcula la suma de los ángulos interiores:

1. Pentágono (5 lados)
2. Heptágono (7 lados)
3. Decágono (10 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $(5-2) \times 180° = 3 \times 180° = 540°$
2. $(7-2) \times 180° = 5 \times 180° = 900°$
3. $(10-2) \times 180° = 8 \times 180° = 1440°$

</details>

---

### Ejercicio 2: Ángulo interior de polígono regular

Calcula el ángulo interior de:

1. Pentágono regular
2. Nonágono regular (9 lados)
3. Dodecágono regular (12 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{540°}{5} = 108°$
2. $\frac{(9-2) \times 180°}{9} = \frac{1260°}{9} = 140°$
3. $\frac{(12-2) \times 180°}{12} = \frac{1800°}{12} = 150°$

</details>

---

### Ejercicio 3: Ángulo exterior

Calcula el ángulo exterior de cada polígono regular:

1. Hexágono (6 lados)
2. Decágono (10 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{360°}{6} = 60°$
2. $\frac{360°}{10} = 36°$

</details>

---

### Ejercicio 4: Encontrar el número de lados

¿Cuántos lados tiene un polígono regular si...?

1. Su ángulo exterior es $40°$
2. Su ángulo interior es $156°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $n = \frac{360°}{40°} = 9$ lados (nonágono)
2. Ángulo exterior = $180° - 156° = 24°$, entonces $n = \frac{360°}{24°} = 15$ lados

</details>

---

### Ejercicio 5: Problema

Un polígono regular tiene ángulos interiores de $144°$. ¿Cuántos lados tiene y cuál es la suma de sus ángulos interiores?

<details>
<summary><strong>Ver respuesta</strong></summary>

Ángulo exterior = $180° - 144° = 36°$

$$
n = \frac{360°}{36°} = 10 \text{ lados (decágono)}
$$

Suma de ángulos = $(10-2) \times 180° = 1440°$

</details>

---

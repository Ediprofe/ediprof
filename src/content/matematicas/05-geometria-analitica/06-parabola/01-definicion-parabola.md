# Definición de la Parábola

La parábola es una de las **cónicas** más importantes. Aparece en la trayectoria de proyectiles, en antenas parabólicas, en los faros de automóviles y en muchas más aplicaciones. Estudiaremos su definición como lugar geométrico.

---

## 🎯 ¿Qué vas a aprender?

- La definición de parábola como lugar geométrico
- Sus elementos fundamentales
- La relación entre foco y directriz

---

## 📖 Lo Esencial de la Parábola

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/elementos-parabola.svg" alt="Elementos de la parábola" style="width: 100%; height: auto;" />
</div>

| Elemento | Símbolo | Descripción |
|----------|---------|-------------|
| Foco | $F$ | Punto fijo |
| Directriz | $\ell$ | Recta fija |
| Vértice | $V$ | Punto medio entre foco y directriz |
| Eje | — | Recta perpendicular a la directriz que pasa por el foco |
| Parámetro | $p$ | Distancia del vértice al foco (= del vértice a la directriz) |
| Lado recto | $LR = 4p$ | Cuerda que pasa por el foco, perpendicular al eje |

---

## 📖 Definición como Lugar Geométrico

> Una **parábola** es el lugar geométrico de todos los puntos del plano que están a **igual distancia** de un punto fijo (foco) y de una recta fija (directriz).

Matemáticamente, si $F$ es el foco y $\ell$ es la directriz:

$$
\text{Parábola} = \{P : d(P, F) = d(P, \ell)\}
$$

Esta propiedad se llama **propiedad focal** de la parábola.

---

## 📖 Elementos de la Parábola

### Foco (F)
El **foco** es el punto fijo que define la parábola junto con la directriz.

### Directriz (ℓ)
La **directriz** es la recta fija. Todos los puntos de la parábola equidistan del foco y de esta recta.

### Vértice (V)
El **vértice** es el punto de la parábola más cercano a la directriz. Está exactamente a la mitad entre el foco y la directriz.

### Eje de la parábola
El **eje** es la recta que pasa por el foco y es perpendicular a la directriz. Es también el eje de simetría de la parábola.

### Parámetro (p)
El **parámetro** es la distancia del vértice al foco (o del vértice a la directriz). Se denota $p$.

### Lado recto (LR)
El **lado recto** (o latus rectum) es la cuerda que pasa por el foco y es perpendicular al eje. Su longitud es $LR = 4p$.

---

## 📖 Construcción de la Ecuación

Sea una parábola con vértice en el origen y que abre hacia arriba:
- Foco: $F(0, p)$
- Directriz: $y = -p$

Para un punto $P(x, y)$ de la parábola:

**Distancia al foco:**
$$
d(P, F) = \sqrt{x^2 + (y - p)^2}
$$

**Distancia a la directriz:**
$$
d(P, \ell) = |y + p|
$$

Por la definición:
$$
\sqrt{x^2 + (y - p)^2} = |y + p|
$$

Elevando al cuadrado (para $y \geq -p$):
$$
x^2 + (y - p)^2 = (y + p)^2
$$

$$
x^2 + y^2 - 2py + p^2 = y^2 + 2py + p^2
$$

$$
x^2 = 4py
$$

Esta es la **ecuación canónica** de la parábola vertical con vértice en el origen que abre hacia arriba.

---

## 📖 Las Cuatro Orientaciones

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/cuatro-orientaciones-parabola.svg" alt="Las cuatro orientaciones de la parábola" style="width: 100%; height: auto;" />
</div>

Dependiendo de hacia dónde "abre" la parábola:

| Orientación | Ecuación | Foco | Directriz |
|-------------|----------|------|-----------|
| Arriba | $x^2 = 4py$ | $(0, p)$ | $y = -p$ |
| Abajo | $x^2 = -4py$ | $(0, -p)$ | $y = p$ |
| Derecha | $y^2 = 4px$ | $(p, 0)$ | $x = -p$ |
| Izquierda | $y^2 = -4px$ | $(-p, 0)$ | $x = p$ |

---

## 📖 Ejemplos Resueltos

### ⚙️ Ejemplo 1: Identificar elementos

De $x^2 = 12y$, encuentra el foco, la directriz y el lado recto.

**Comparamos con** $x^2 = 4py$:
$$
4p = 12 \Rightarrow p = 3
$$

- **Foco:** $(0, 3)$
- **Directriz:** $y = -3$
- **Lado recto:** $LR = 4(3) = 12$

### ⚙️ Ejemplo 2: Parábola horizontal

De $y^2 = 8x$, encuentra los elementos.

**Comparamos con** $y^2 = 4px$:
$$
4p = 8 \Rightarrow p = 2
$$

- **Foco:** $(2, 0)$
- **Directriz:** $x = -2$
- **Abre hacia:** la derecha

### ⚙️ Ejemplo 3: Signo negativo

De $y^2 = -16x$, encuentra los elementos.

**Comparamos con** $y^2 = -4px$:
$$
4p = 16 \Rightarrow p = 4
$$

- **Foco:** $(-4, 0)$
- **Directriz:** $x = 4$
- **Abre hacia:** la izquierda

---

## 📖 Aplicaciones de la Parábola

| Aplicación | Principio |
|------------|-----------|
| **Antenas parabólicas** | Los rayos paralelos se reflejan hacia el foco |
| **Faros de auto** | La luz desde el foco se refleja en rayos paralelos |
| **Puentes** | La forma parabólica distribuye el peso uniformemente |
| **Proyectiles** | La trayectoria bajo gravedad es parabólica |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| Definición | $d(P, F) = d(P, \ell)$ |
| Parámetro | $p$ = distancia vértice-foco |
| Lado recto | $LR = 4p$ |
| Eje | Línea de simetría |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el foco y la directriz de $x^2 = 20y$.

<details>
<summary>Ver solución</summary>

$4p = 20 \Rightarrow p = 5$

Foco: $(0, 5)$
Directriz: $y = -5$

</details>

### Ejercicio 2
Encuentra los elementos de $y^2 = -24x$.

<details>
<summary>Ver solución</summary>

$4p = 24 \Rightarrow p = 6$

Foco: $(-6, 0)$
Directriz: $x = 6$
Abre: hacia la izquierda

</details>

### Ejercicio 3
Escribe la ecuación de la parábola con vértice en el origen, eje vertical y foco en $(0, 4)$.

<details>
<summary>Ver solución</summary>

$p = 4$ (abre hacia arriba)

$x^2 = 4(4)y = 16y$

</details>

### Ejercicio 4
¿Cuál es el lado recto de $x^2 = 6y$?

<details>
<summary>Ver solución</summary>

$4p = 6 \Rightarrow p = 1.5$

$LR = 4p = 6$

</details>

### Ejercicio 5
Una parábola horizontal tiene directriz $x = 3$ y vértice en el origen. Encuentra su ecuación.

<details>
<summary>Ver solución</summary>

La directriz está a la derecha del vértice, así que la parábola abre hacia la izquierda.

$p = 3$

$y^2 = -4(3)x = -12x$

</details>

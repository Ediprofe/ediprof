# Ecuación General de la Recta

La recta es el lugar geométrico más simple y fundamental. En esta lección estudiaremos su forma más general: una ecuación que puede representar **cualquier** recta en el plano, incluyendo verticales y horizontales.

---

## 🎯 ¿Qué vas a aprender?

- La forma general de la ecuación de una recta
- Cómo identificar sus características
- Cómo convertir entre formas

---

## 📖 Lo Esencial de la Ecuación General

| Concepto | Expresión |
|----------|-----------|
| Ecuación general | $Ax + By + C = 0$ |
| Pendiente | $m = -\dfrac{A}{B}$ (si $B \neq 0$) |
| Intercepto Y | $b = -\dfrac{C}{B}$ (si $B \neq 0$) |
| Intercepto X | $a = -\dfrac{C}{A}$ (si $A \neq 0$) |
| Recta horizontal | $A = 0$: $By + C = 0$ |
| Recta vertical | $B = 0$: $Ax + C = 0$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/ecuacion-general.svg" alt="Ecuación general de la recta" style="width: 100%; height: auto;" />
</div>

---

## 📖 La Forma General

La **ecuación general** de una recta es:

$$
Ax + By + C = 0
$$

donde $A$, $B$ y $C$ son constantes reales, y **al menos uno** de $A$ o $B$ es diferente de cero.

> 💡 Esta forma es la más versátil porque puede representar **cualquier recta**, incluso las verticales (que no se pueden escribir en forma $y = mx + b$).

### Condiciones:
- Si $B \neq 0$: La recta no es vertical y tiene pendiente $m = -\frac{A}{B}$
- Si $B = 0$: La recta es vertical (ecuación $x = k$)
- Si $A = 0$: La recta es horizontal (ecuación $y = k$)

---

## 📖 Ejemplos de la Forma General

### ⚙️ Ejemplo 1: Identificar los coeficientes

Para la recta $3x - 2y + 6 = 0$, identifica $A$, $B$ y $C$.

**Respuesta:**
- $A = 3$
- $B = -2$
- $C = 6$

### ⚙️ Ejemplo 2: Calcular la pendiente desde la forma general

Encuentra la pendiente de $3x - 2y + 6 = 0$.

**Fórmula:** $m = -\frac{A}{B}$

$$
m = -\frac{3}{-2} = \frac{3}{2}
$$

**Respuesta:** La pendiente es $\frac{3}{2}$.

### ⚙️ Ejemplo 3: Encontrar los interceptos

Encuentra los interceptos de $2x + 4y - 8 = 0$.

**Intercepto Y** (cuando $x = 0$):
$$
4y - 8 = 0 \Rightarrow y = 2
$$
Intercepto: $(0, 2)$

**Intercepto X** (cuando $y = 0$):
$$
2x - 8 = 0 \Rightarrow x = 4
$$
Intercepto: $(4, 0)$

---

## 📖 Conversión de Formas

### De forma general a forma explícita

Para convertir $Ax + By + C = 0$ a $y = mx + b$:

1. Despeja $y$:
$$
By = -Ax - C
$$
$$
y = -\frac{A}{B}x - \frac{C}{B}
$$

Por lo tanto:
- Pendiente: $m = -\frac{A}{B}$
- Intercepto Y: $b = -\frac{C}{B}$

### ⚙️ Ejemplo 4: Convertir a forma explícita

Convierte $3x - 6y + 12 = 0$ a forma $y = mx + b$.

**Despejamos $y$:**
$$
-6y = -3x - 12
$$
$$
y = \frac{-3x - 12}{-6} = \frac{1}{2}x + 2
$$

**Respuesta:** $y = \frac{1}{2}x + 2$

### De forma explícita a forma general

Para convertir $y = mx + b$ a $Ax + By + C = 0$:

$$
y = mx + b
$$
$$
mx - y + b = 0
$$

### ⚙️ Ejemplo 5: Convertir a forma general

Convierte $y = -3x + 5$ a forma general.

$$
3x + y - 5 = 0
$$

**Respuesta:** $3x + y - 5 = 0$

---

## 📖 Casos Especiales

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/rectas-h-v.svg" alt="Rectas horizontales y verticales" style="width: 100%; height: auto;" />
</div>

### Recta horizontal

Una recta horizontal tiene ecuación $y = k$ o en forma general:

$$
0 \cdot x + 1 \cdot y - k = 0
$$

Es decir: $y - k = 0$

**Ejemplo:** $y = 3$ → $y - 3 = 0$ o $0x + y - 3 = 0$

### Recta vertical

Una recta vertical tiene ecuación $x = k$ o en forma general:

$$
1 \cdot x + 0 \cdot y - k = 0
$$

Es decir: $x - k = 0$

**Ejemplo:** $x = -2$ → $x + 2 = 0$ o $x + 0y + 2 = 0$

---

## 📖 Multiplicación por una Constante

Si multiplicamos toda la ecuación por una constante $k \neq 0$, obtenemos la **misma recta**:

$$
Ax + By + C = 0 \iff kAx + kBy + kC = 0
$$

### ⚙️ Ejemplo 6: Ecuaciones equivalentes

Las siguientes ecuaciones representan la misma recta:
- $2x + 4y - 6 = 0$
- $x + 2y - 3 = 0$ (dividida por 2)
- $4x + 8y - 12 = 0$ (multiplicada por 2)

---

## 🔑 Resumen

| Forma | Características |
|-------|----------------|
| General: $Ax + By + C = 0$ | Representa cualquier recta |
| Explícita: $y = mx + b$ | No incluye rectas verticales |
| Pendiente | $m = -\frac{A}{B}$ |
| Intercepto Y | $b = -\frac{C}{B}$ |
| Intercepto X | $a = -\frac{C}{A}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la pendiente y los interceptos de $4x - 2y + 8 = 0$.

<details>
<summary>Ver solución</summary>

**Pendiente:** $m = -\frac{4}{-2} = 2$

**Intercepto Y:** $b = -\frac{8}{-2} = 4$ → $(0, 4)$

**Intercepto X:** ($y = 0$) $4x + 8 = 0$ → $x = -2$ → $(-2, 0)$

</details>

### Ejercicio 2
Convierte $5x + 3y - 15 = 0$ a forma explícita.

<details>
<summary>Ver solución</summary>

$$
3y = -5x + 15
$$
$$
y = -\frac{5}{3}x + 5
$$

</details>

### Ejercicio 3
Escribe la ecuación $y = \frac{2}{3}x - 4$ en forma general con coeficientes enteros.

<details>
<summary>Ver solución</summary>

$$
y = \frac{2}{3}x - 4
$$
$$
3y = 2x - 12
$$
$$
2x - 3y - 12 = 0
$$

</details>

### Ejercicio 4
¿Cuál es la ecuación general de la recta horizontal que pasa por $(5, -3)$?

<details>
<summary>Ver solución</summary>

Una recta horizontal tiene $y = k$ constante.

Como pasa por $(5, -3)$, entonces $k = -3$.

**Forma explícita:** $y = -3$

**Forma general:** $y + 3 = 0$ o $0x + y + 3 = 0$

</details>

### Ejercicio 5
Verifica si el punto $(2, 3)$ pertenece a la recta $5x - 2y - 4 = 0$.

<details>
<summary>Ver solución</summary>

Sustituimos $(x, y) = (2, 3)$:

$$
5(2) - 2(3) - 4 = 10 - 6 - 4 = 0
$$

Como el resultado es 0, el punto **sí pertenece** a la recta.

</details>

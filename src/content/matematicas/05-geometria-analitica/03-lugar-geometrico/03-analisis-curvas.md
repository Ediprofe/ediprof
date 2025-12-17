# Análisis de Curvas

Cuando te dan una ecuación, ¿cómo la analizas sistemáticamente para entender qué curva representa? En esta lección aprenderás un método paso a paso para analizar cualquier curva en el plano cartesiano.

---

## 🎯 ¿Qué vas a aprender?

- Un método sistemático para analizar curvas
- Cómo identificar características clave
- Cómo determinar el tipo de curva

---

## 📖 Lo Esencial de Análisis de Curvas

| Paso | Pregunta a responder |
|------|---------------------|
| 1. Interceptos | ¿Dónde cruza los ejes? |
| 2. Simetría | ¿Es simétrica respecto a algún eje o al origen? |
| 3. Dominio/Rango | ¿Qué valores de $x$ y $y$ son válidos? |
| 4. Asíntotas | ¿Hay líneas a las que la curva se acerca pero nunca toca? |
| 5. Puntos clave | ¿Dónde están los máximos, mínimos, vértices? |
| 6. Comportamiento | ¿Qué pasa cuando $x \to \pm\infty$? |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/analisis-curva.svg" alt="Análisis de curva con interceptos y simetría" style="width: 100%; height: auto;" />
</div>

---

## 📖 Método de Análisis

### Paso 1: Interceptos

**Intercepto Y:** Sustituye $x = 0$ y resuelve para $y$.

**Interceptos X:** Sustituye $y = 0$ y resuelve para $x$.

### Paso 2: Simetrías

| Tipo | Procedimiento |
|------|---------------|
| Eje Y | Cambia $x$ por $-x$. Si la ecuación es igual, hay simetría |
| Eje X | Cambia $y$ por $-y$. Si la ecuación es igual, hay simetría |
| Origen | Cambia $x$ por $-x$ y $y$ por $-y$. Si es igual, hay simetría |

### Paso 3: Dominio y Rango

Identifica restricciones:
- No se puede dividir entre cero
- No se puede tomar raíz cuadrada de números negativos
- Considera las desigualdades implícitas

### Paso 4: Asíntotas

**Asíntota vertical:** Donde el denominador es cero.

**Asíntota horizontal:** El límite cuando $x \to \pm\infty$.

### Paso 5: Puntos especiales

- **Para parábolas:** El vértice
- **Para circunferencias:** El centro
- **Para elipses:** Los focos y vértices

### Paso 6: Comportamiento en el infinito

¿La curva sube, baja, o se estabiliza cuando $x$ se hace muy grande?

---

## 📖 Ejemplos de Análisis Completo

### ⚙️ Ejemplo 1: Análisis de una parábola

Analiza la curva $y = x^2 - 4x + 3$.

**Paso 1: Interceptos**

- Intercepto Y: $y = 0 - 0 + 3 = 3$ → $(0, 3)$
- Interceptos X: $x^2 - 4x + 3 = 0$ → $(x-1)(x-3) = 0$ → $(1, 0)$ y $(3, 0)$

**Paso 2: Simetría**

Cambiando $x$ por $-x$: $y = (-x)^2 - 4(-x) + 3 = x^2 + 4x + 3$

No es igual a la original, **no hay simetría respecto al eje Y**.

**Paso 3: Dominio y Rango**

- Dominio: Todos los reales
- Para el rango, encontramos el vértice.

**Paso 4: Vértice**

Completando el cuadrado:
$$
y = (x^2 - 4x + 4) + 3 - 4 = (x - 2)^2 - 1
$$

Vértice: $(2, -1)$

**Paso 5: Rango**

Como abre hacia arriba: $y \geq -1$

**Resultado:** Parábola con vértice en $(2, -1)$, interceptos en $(1, 0)$, $(3, 0)$ y $(0, 3)$.

### ⚙️ Ejemplo 2: Análisis de una hipérbola rectangular

Analiza la curva $y = \frac{1}{x}$.

**Paso 1: Interceptos**

- Intercepto Y: Cuando $x = 0$, la función no está definida. **No hay intercepto Y**.
- Intercepto X: Cuando $y = 0$, $\frac{1}{x} = 0$ no tiene solución. **No hay intercepto X**.

**Paso 2: Simetría**

Cambiando $x$ por $-x$ y $y$ por $-y$:
$$
-y = \frac{1}{-x} = -\frac{1}{x}
$$
$$
y = \frac{1}{x}
$$

**Hay simetría respecto al origen.**

**Paso 3: Dominio y Rango**

- Dominio: $x \neq 0$ (todos los reales excepto cero)
- Rango: $y \neq 0$ (todos los reales excepto cero)

**Paso 4: Asíntotas**

- Asíntota vertical: $x = 0$ (eje Y)
- Asíntota horizontal: $y = 0$ (eje X)

**Paso 5: Comportamiento**

- Cuando $x \to +\infty$: $y \to 0^+$
- Cuando $x \to 0^+$: $y \to +\infty$
- Cuando $x \to -\infty$: $y \to 0^-$
- Cuando $x \to 0^-$: $y \to -\infty$

**Resultado:** Hipérbola rectangular con dos ramas en los cuadrantes I y III.

### ⚙️ Ejemplo 3: Análisis de una circunferencia

Analiza la curva $x^2 + y^2 - 4x + 6y - 12 = 0$.

**Paso 1: Identificar la curva**

Completamos cuadrados:
$$
(x^2 - 4x + 4) + (y^2 + 6y + 9) = 12 + 4 + 9
$$
$$
(x - 2)^2 + (y + 3)^2 = 25
$$

Es una circunferencia con centro $(2, -3)$ y radio $5$.

**Paso 2: Interceptos**

- Intercepto Y ($x = 0$):
$$
4 + (y + 3)^2 = 25 \Rightarrow (y + 3)^2 = 21 \Rightarrow y = -3 \pm \sqrt{21}
$$

Interceptos: $(0, -3 + \sqrt{21})$ y $(0, -3 - \sqrt{21})$

- Intercepto X ($y = 0$):
$$
(x - 2)^2 + 9 = 25 \Rightarrow (x - 2)^2 = 16 \Rightarrow x = 2 \pm 4
$$

Interceptos: $(6, 0)$ y $(-2, 0)$

**Paso 3: Dominio y Rango**

- Dominio: $[2 - 5, 2 + 5] = [-3, 7]$
- Rango: $[-3 - 5, -3 + 5] = [-8, 2]$

**Resultado:** Circunferencia centrada en $(2, -3)$ con radio $5$.

---

## 📖 Tabla de Identificación de Curvas

| Característica de la ecuación | Tipo de curva |
|------------------------------|---------------|
| Grado 1 en $x$ y $y$ | Recta |
| $x^2 + y^2$ con coeficientes iguales | Circunferencia |
| $x^2$ y $y$ (o viceversa), grado 2 en una variable | Parábola |
| $x^2$ y $y^2$ con el mismo signo y coeficientes diferentes | Elipse |
| $x^2$ y $y^2$ con signos opuestos | Hipérbola |

---

## 🔑 Resumen

| Paso | Información obtenida |
|------|---------------------|
| Interceptos | Puntos de cruce con los ejes |
| Simetría | Comportamiento de reflexión |
| Dominio/Rango | Extensión de la curva |
| Asíntotas | Comportamiento límite |
| Puntos clave | Vértices, centros, focos |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Analiza la curva $y = x^2 + 2x - 3$: encuentra los interceptos y el vértice.

<details>
<summary>Ver solución</summary>

**Intercepto Y:** $y = 0 + 0 - 3 = -3$ → $(0, -3)$

**Interceptos X:** $x^2 + 2x - 3 = 0$ → $(x+3)(x-1) = 0$ → $(-3, 0)$ y $(1, 0)$

**Vértice:** $y = (x + 1)^2 - 4$ → Vértice: $(-1, -4)$

</details>

### Ejercicio 2
¿Qué tipo de curva es $4x^2 + 9y^2 = 36$?

<details>
<summary>Ver solución</summary>

Dividimos entre 36:
$$
\frac{x^2}{9} + \frac{y^2}{4} = 1
$$

Es una **elipse** con $a = 3$ y $b = 2$ (eje mayor horizontal).

</details>

### Ejercicio 3
Encuentra las asíntotas de $y = \frac{2x}{x - 1}$.

<details>
<summary>Ver solución</summary>

**Asíntota vertical:** Donde $x - 1 = 0$ → $x = 1$

**Asíntota horizontal:** Cuando $x \to \infty$:
$$
y = \frac{2x}{x-1} = \frac{2}{1 - \frac{1}{x}} \to 2
$$

Asíntota horizontal: $y = 2$

</details>

### Ejercicio 4
Analiza la simetría de $x^2 - y^2 = 4$.

<details>
<summary>Ver solución</summary>

**Simetría respecto al eje Y:** $(-x)^2 - y^2 = x^2 - y^2 = 4$ ✓

**Simetría respecto al eje X:** $x^2 - (-y)^2 = x^2 - y^2 = 4$ ✓

**Simetría respecto al origen:** $(-x)^2 - (-y)^2 = x^2 - y^2 = 4$ ✓

**Tiene las tres simetrías.**

Es una hipérbola con eje transversal horizontal.

</details>

### Ejercicio 5
Determina el dominio y rango de $y = \sqrt{9 - x^2}$.

<details>
<summary>Ver solución</summary>

Para que la raíz exista: $9 - x^2 \geq 0$ → $x^2 \leq 9$ → $-3 \leq x \leq 3$

**Dominio:** $[-3, 3]$

El valor mínimo de $\sqrt{9 - x^2}$ es $0$ (cuando $x = \pm 3$).
El valor máximo es $3$ (cuando $x = 0$).

**Rango:** $[0, 3]$

> Nota: Esta es la semicircunferencia superior de $x^2 + y^2 = 9$.

</details>

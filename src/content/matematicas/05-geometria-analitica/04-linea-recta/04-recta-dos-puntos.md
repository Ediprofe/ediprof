# Recta que Pasa por Dos Puntos

Si conoces dos puntos por donde pasa una recta, puedes determinar completamente su ecuación. Esta es una de las situaciones más comunes en geometría analítica.

---

## 🎯 ¿Qué vas a aprender?

- Cómo encontrar la ecuación de una recta dados dos puntos
- Diferentes métodos para resolver el problema
- Aplicaciones prácticas

---

## 📖 Lo Esencial de Recta por Dos Puntos

| Método | Fórmula |
|--------|---------|
| Primero calcular pendiente | $m = \dfrac{y_2 - y_1}{x_2 - x_1}$, luego usar punto-pendiente |
| Fórmula directa | $\dfrac{y - y_1}{y_2 - y_1} = \dfrac{x - x_1}{x_2 - x_1}$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/recta-dos-puntos.svg" alt="Recta por dos puntos" style="width: 100%; height: auto;" />
</div>

---

## 📖 Método 1: Pendiente + Punto-Pendiente

Este es el método más intuitivo:

1. **Calcular la pendiente** usando los dos puntos
2. **Usar punto-pendiente** con uno de los puntos

### ⚙️ Ejemplo 1: Método paso a paso

Encuentra la ecuación de la recta que pasa por $A(2, 3)$ y $B(5, 9)$.

**Paso 1:** Calcular la pendiente:
$$
m = \frac{9 - 3}{5 - 2} = \frac{6}{3} = 2
$$

**Paso 2:** Usar punto-pendiente con $A(2, 3)$:
$$
y - 3 = 2(x - 2)
$$
$$
y - 3 = 2x - 4
$$
$$
y = 2x - 1
$$

> 💡 Podríamos haber usado el punto $B(5, 9)$ y obtendríamos la misma ecuación.

### ⚙️ Ejemplo 2: Con coordenadas negativas

Encuentra la ecuación de la recta por $P(-3, 4)$ y $Q(1, -4)$.

**Paso 1:** Pendiente:
$$
m = \frac{-4 - 4}{1 - (-3)} = \frac{-8}{4} = -2
$$

**Paso 2:** Punto-pendiente:
$$
y - 4 = -2(x - (-3))
$$
$$
y - 4 = -2(x + 3)
$$
$$
y - 4 = -2x - 6
$$
$$
y = -2x - 2
$$

---

## 📖 Método 2: Fórmula Directa

También se puede usar la **fórmula simétrica**:

$$
\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}
$$

O en otra forma:

$$
\frac{y - y_1}{x - x_1} = \frac{y_2 - y_1}{x_2 - x_1}
$$

### ⚙️ Ejemplo 3: Usando la fórmula directa

Encuentra la ecuación de la recta por $(1, 2)$ y $(4, 8)$.

**Aplicamos la fórmula:**
$$
\frac{y - 2}{x - 1} = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2
$$

**Despejamos:**
$$
y - 2 = 2(x - 1)
$$
$$
y = 2x
$$

---

## 📖 Casos Especiales

### Recta horizontal (puntos con igual $y$)

Si $y_1 = y_2$, la recta es horizontal.

### ⚙️ Ejemplo 4: Recta horizontal

Encuentra la ecuación de la recta por $(2, 5)$ y $(7, 5)$.

Como $y_1 = y_2 = 5$, la recta es horizontal:
$$
y = 5
$$

### Recta vertical (puntos con igual $x$)

Si $x_1 = x_2$, la recta es vertical y la pendiente no está definida.

### ⚙️ Ejemplo 5: Recta vertical

Encuentra la ecuación de la recta por $(3, 1)$ y $(3, 8)$.

Como $x_1 = x_2 = 3$, la recta es vertical:
$$
x = 3
$$

---

## 📖 Conversión a Diferentes Formas

Una vez obtenida la ecuación, podemos convertirla a cualquier forma:

### ⚙️ Ejemplo 6: Todas las formas

Encuentra la ecuación de la recta por $(1, 4)$ y $(3, 10)$ en todas las formas.

**Pendiente:**
$$
m = \frac{10 - 4}{3 - 1} = \frac{6}{2} = 3
$$

**Forma punto-pendiente:**
$$
y - 4 = 3(x - 1)
$$

**Forma pendiente-ordenada:**
$$
y = 3x - 3 + 4 = 3x + 1
$$

**Forma general:**
$$
3x - y + 1 = 0
$$

---

## 📖 Verificación

Siempre es buena idea verificar que ambos puntos satisfacen la ecuación obtenida.

### ⚙️ Ejemplo 7: Verificación

Verificar que $y = 2x - 1$ pasa por $(2, 3)$ y $(5, 9)$.

**Para $(2, 3)$:**
$$
y = 2(2) - 1 = 4 - 1 = 3 ✓
$$

**Para $(5, 9)$:**
$$
y = 2(5) - 1 = 10 - 1 = 9 ✓
$$

---

## 📖 Aplicación: Interpolación Lineal

Un uso práctico de la recta por dos puntos es la **interpolación lineal**: estimar valores entre dos puntos conocidos.

### ⚙️ Ejemplo 8: Problema aplicado

A las 8:00 am la temperatura era 15°C y a las 12:00 pm era 23°C. Suponiendo crecimiento lineal, ¿cuál era la temperatura a las 10:00 am?

**Puntos:** $(8, 15)$ y $(12, 23)$

**Pendiente:**
$$
m = \frac{23 - 15}{12 - 8} = \frac{8}{4} = 2 \text{ °C/hora}
$$

**Ecuación:**
$$
T - 15 = 2(t - 8)
$$
$$
T = 2t - 16 + 15 = 2t - 1
$$

**A las 10:00 am ($t = 10$):**
$$
T = 2(10) - 1 = 19°C
$$

---

## 🔑 Resumen

| Paso | Acción |
|------|--------|
| 1 | Verificar si $x_1 = x_2$ (recta vertical) o $y_1 = y_2$ (recta horizontal) |
| 2 | Calcular $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| 3 | Usar punto-pendiente: $y - y_1 = m(x - x_1)$ |
| 4 | Simplificar a la forma deseada |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la ecuación de la recta por $(0, 3)$ y $(4, 7)$.

<details>
<summary>Ver solución</summary>

**Pendiente:**
$$
m = \frac{7 - 3}{4 - 0} = 1
$$

**Usando $(0, 3)$:**
$$
y - 3 = 1(x - 0)
$$
$$
y = x + 3
$$

</details>

### Ejercicio 2
Encuentra la ecuación de la recta por $(-2, 5)$ y $(4, -1)$.

<details>
<summary>Ver solución</summary>

**Pendiente:**
$$
m = \frac{-1 - 5}{4 - (-2)} = \frac{-6}{6} = -1
$$

**Ecuación:**
$$
y - 5 = -1(x + 2)
$$
$$
y = -x - 2 + 5
$$
$$
y = -x + 3
$$

</details>

### Ejercicio 3
Encuentra la ecuación de la recta por $(5, 2)$ y $(5, -7)$.

<details>
<summary>Ver solución</summary>

Como $x_1 = x_2 = 5$, es una recta **vertical**:

$$
x = 5
$$

</details>

### Ejercicio 4
La población de una ciudad era 50,000 en 2010 y 65,000 en 2020. Si el crecimiento es lineal, ¿cuál será la población en 2025?

<details>
<summary>Ver solución</summary>

**Puntos:** $(2010, 50000)$ y $(2020, 65000)$

**Pendiente:**
$$
m = \frac{65000 - 50000}{2020 - 2010} = \frac{15000}{10} = 1500 \text{ personas/año}
$$

**Ecuación:**
$$
P = 1500(t - 2010) + 50000
$$

**Para 2025:**
$$
P = 1500(2025 - 2010) + 50000 = 1500(15) + 50000 = 72500
$$

**Respuesta:** 72,500 habitantes

</details>

### Ejercicio 5
Escribe en forma general la ecuación de la recta por $(3, -2)$ y $(-1, 6)$.

<details>
<summary>Ver solución</summary>

**Pendiente:**
$$
m = \frac{6 - (-2)}{-1 - 3} = \frac{8}{-4} = -2
$$

**Ecuación:**
$$
y + 2 = -2(x - 3)
$$
$$
y + 2 = -2x + 6
$$
$$
2x + y - 4 = 0
$$

</details>

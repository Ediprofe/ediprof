# Función Valor Absoluto

Ya exploramos las propiedades del valor absoluto. Ahora estudiamos $f(x) = |x|$ como función, sus transformaciones y la familia de funciones lineales a trozos que genera.

---

## 🎯 ¿Qué vas a aprender?

- La gráfica característica en forma de V
- Transformaciones de la función valor absoluto
- Cómo graficar funciones de la forma $f(x) = a|x - h| + k$
- Aplicaciones del valor absoluto

---

## 📖 La función valor absoluto básica

$$
f(x) = |x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}
$$

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $[0, +\infty)$ |
| **Vértice** | $(0, 0)$ |
| **Paridad** | Par ($f(-x) = f(x)$) |
| **Simetría** | Eje Y |
| **Mínimo** | $0$ en $x = 0$ |

### Forma de la gráfica

La gráfica tiene forma de **V** con vértice en el origen:
- Rama izquierda: $y = -x$ (pendiente $-1$)
- Rama derecha: $y = x$ (pendiente $+1$)

---

## 📖 Forma general transformada

$$
f(x) = a|x - h| + k
$$

### Interpretación de parámetros

| Parámetro | Efecto |
|-----------|--------|
| **$(h, k)$** | Vértice de la V |
| **$a > 0$** | V abre hacia arriba |
| **$a < 0$** | V abre hacia abajo (forma de Λ) |
| **$\|a\| > 1$** | V más angosta |
| **$\|a\| < 1$** | V más ancha |

---

## ⚙️ Ejemplo 1: Identificar elementos

Para $f(x) = 2|x - 3| - 4$:

**Vértice:** $(3, -4)$

**Orientación:** $a = 2 > 0$ → abre hacia arriba

**Pendientes:** $\pm 2$ (más empinada que la básica)

**Dominio:** $\mathbb{R}$

**Rango:** $[-4, +\infty)$

---

## ⚙️ Ejemplo 2: Escribir por partes

Escribe $f(x) = |2x - 6|$ como función por partes.

**Paso 1:** Encontrar dónde el interior es cero
$$2x - 6 = 0 \Rightarrow x = 3$$

**Paso 2:** Determinar signos
- Si $x \geq 3$: $2x - 6 \geq 0$, entonces $|2x - 6| = 2x - 6$
- Si $x < 3$: $2x - 6 < 0$, entonces $|2x - 6| = -(2x - 6) = -2x + 6$

**Función por partes:**
$$
f(x) = \begin{cases} -2x + 6 & \text{si } x < 3 \\ 2x - 6 & \text{si } x \geq 3 \end{cases}
$$

---

## ⚙️ Ejemplo 3: Graficar paso a paso

Grafica $g(x) = -|x + 2| + 4$

**Paso 1:** Identificar el vértice
- $h = -2$, $k = 4$
- Vértice: $(-2, 4)$

**Paso 2:** Determinar orientación
- $a = -1 < 0$ → abre hacia abajo

**Paso 3:** Encontrar puntos adicionales
- Cuando $x = 0$: $g(0) = -|2| + 4 = 2$ → $(0, 2)$
- Cuando $x = -4$: $g(-4) = -|-2| + 4 = 2$ → $(-4, 2)$

**Paso 4:** Encontrar intersecciones con eje X
$$-|x + 2| + 4 = 0$$
$$|x + 2| = 4$$
$$x + 2 = 4 \text{ o } x + 2 = -4$$
$$x = 2 \text{ o } x = -6$$

**Intersecciones:** $(-6, 0)$ y $(2, 0)$

---

## 📖 Resolviendo ecuaciones gráficamente

La gráfica de $y = |x|$ nos ayuda a visualizar soluciones de ecuaciones con valor absoluto.

### $|x| = c$ (donde $c > 0$)

Es la intersección de $y = |x|$ con la recta horizontal $y = c$.

Hay **dos soluciones**: $x = c$ y $x = -c$.

### $|x| = c$ (donde $c < 0$)

No hay intersección (la V nunca está debajo del eje X).

**Sin solución.**

---

## 📖 Valor absoluto en modelado

El valor absoluto modela situaciones de **distancia** y **desviación**:

### Ejemplo: Error de medición

Si el peso ideal de un producto es 500 g y el error tolerado es 5 g:

$$|p - 500| \leq 5$$

Significa que el peso real $p$ debe estar entre 495 g y 505 g.

### Ejemplo: Temperatura

La temperatura $T$ debe mantenerse a distancia menor de 3°C de los 25°C:

$$|T - 25| < 3$$

Es decir, $22°C < T < 28°C$.

---

## ⚙️ Ejemplo 4: Suma de valores absolutos

Analiza $f(x) = |x| + |x - 2|$

**Puntos críticos:** $x = 0$ y $x = 2$

**Por partes:**
- Si $x < 0$: $f(x) = -x + (-(x-2)) = -x - x + 2 = -2x + 2$
- Si $0 \leq x < 2$: $f(x) = x + (-(x-2)) = x - x + 2 = 2$
- Si $x \geq 2$: $f(x) = x + (x-2) = 2x - 2$

**Observación:** La función es constante ($y = 2$) entre $x = 0$ y $x = 2$.

---

## 📊 Resumen de transformaciones

| Función | Vértice | Orientación | Pendientes |
|---------|---------|-------------|------------|
| $\|x\|$ | $(0, 0)$ | ↑ | $\pm 1$ |
| $\|x - 3\|$ | $(3, 0)$ | ↑ | $\pm 1$ |
| $\|x\| + 2$ | $(0, 2)$ | ↑ | $\pm 1$ |
| $2\|x\|$ | $(0, 0)$ | ↑ | $\pm 2$ |
| $-\|x\|$ | $(0, 0)$ | ↓ | $\pm 1$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Para cada función, identifica vértice, dominio y rango:

a) $f(x) = |x - 5|$
b) $g(x) = |x| - 3$
c) $h(x) = -2|x + 1| + 6$

<details>
<summary>Ver soluciones</summary>

a) Vértice: $(5, 0)$, Dominio: $\mathbb{R}$, Rango: $[0, +\infty)$

b) Vértice: $(0, -3)$, Dominio: $\mathbb{R}$, Rango: $[-3, +\infty)$

c) Vértice: $(-1, 6)$, Dominio: $\mathbb{R}$, Rango: $(-\infty, 6]$
</details>

---

**Ejercicio 2:** Escribe como función por partes:

$f(x) = |3x + 9|$

<details>
<summary>Ver solución</summary>

Punto crítico: $3x + 9 = 0 \Rightarrow x = -3$

$$
f(x) = \begin{cases} -(3x + 9) = -3x - 9 & \text{si } x < -3 \\ 3x + 9 & \text{si } x \geq -3 \end{cases}
$$
</details>

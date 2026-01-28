---
title: "Desplazamientos"
---

# Desplazamientos

Las transformaciones más intuitivas son los desplazamientos: mover una gráfica hacia arriba, abajo, izquierda o derecha sin cambiar su forma.

---

## 🎯 ¿Qué vas a aprender?

- Desplazamientos verticales
- Desplazamientos horizontales
- Cómo afectan la ecuación de la función
- Combinación de desplazamientos

---

## 📖 Desplazamiento vertical

Un **desplazamiento vertical** mueve la gráfica hacia arriba o hacia abajo.

### Regla

$$g(x) = f(x) + k$$

| Valor de $k$ | Efecto |
|--------------|--------|
| $k > 0$ | Sube $k$ unidades |
| $k < 0$ | Baja $\|k\|$ unidades |

### Interpretación

Sumamos $k$ a **cada valor de salida**. La entrada no cambia, solo el resultado.

---

## ⚙️ Ejemplo 1: Desplazamiento hacia arriba

Sea $f(x) = x^2$. Grafica $g(x) = x^2 + 3$.

**Transformación:** Cada punto $(x, y)$ de $f$ se convierte en $(x, y + 3)$.

**Puntos:**

| $f(x) = x^2$ | $g(x) = x^2 + 3$ |
|--------------|------------------|
| $(0, 0)$ | $(0, 3)$ |
| $(1, 1)$ | $(1, 4)$ |
| $(-2, 4)$ | $(-2, 7)$ |

**Vértice:** Se desplaza de $(0, 0)$ a $(0, 3)$.

---

## ⚙️ Ejemplo 2: Desplazamiento hacia abajo

Sea $f(x) = |x|$. Grafica $h(x) = |x| - 2$.

**Transformación:** Baja 2 unidades.

**Vértice:** De $(0, 0)$ a $(0, -2)$.

**Dominio:** No cambia → $\mathbb{R}$

**Rango:** Cambia de $[0, +\infty)$ a $[-2, +\infty)$

---

## 📖 Desplazamiento horizontal

Un **desplazamiento horizontal** mueve la gráfica hacia la izquierda o derecha.

### Regla

$$g(x) = f(x - h)$$

| Valor de $h$ | Efecto |
|--------------|--------|
| $h > 0$ | Se mueve $h$ unidades a la **derecha** |
| $h < 0$ | Se mueve $\|h\|$ unidades a la **izquierda** |

### ⚠️ ¡Cuidado con el signo!

El desplazamiento horizontal es **contraintuitivo**:
- $f(x - 3)$ desplaza a la **derecha**
- $f(x + 3)$ desplaza a la **izquierda**

### Interpretación

Cada valor de $y$ que antes ocurría en $x$, ahora ocurre en $x + h$.

---

## ⚙️ Ejemplo 3: Desplazamiento a la derecha

Sea $f(x) = \sqrt{x}$. Grafica $g(x) = \sqrt{x - 4}$.

**Transformación:** Desplaza 4 unidades a la derecha.

**Punto inicial:** De $(0, 0)$ a $(4, 0)$.

**Dominio:** De $[0, +\infty)$ a $[4, +\infty)$

**Rango:** No cambia → $[0, +\infty)$

---

## ⚙️ Ejemplo 4: Desplazamiento a la izquierda

Sea $f(x) = x^3$. Grafica $h(x) = (x + 2)^3$.

**Transformación:** Desplaza 2 unidades a la izquierda.

**Punto de inflexión:** De $(0, 0)$ a $(-2, 0)$.

**Dominio y Rango:** No cambian → ambos $\mathbb{R}$

---

## 📖 Combinación de desplazamientos

Podemos combinar ambos tipos de desplazamientos:

$$g(x) = f(x - h) + k$$

**Efecto:** Desplaza la gráfica:
- $h$ unidades horizontalmente (derecha si $h > 0$)
- $k$ unidades verticalmente (arriba si $k > 0$)

---

## ⚙️ Ejemplo 5: Desplazamiento combinado

Sea $f(x) = x^2$. Grafica $g(x) = (x - 3)^2 + 2$.

**Transformaciones:**
1. Desplaza 3 unidades a la derecha
2. Desplaza 2 unidades hacia arriba

**Vértice:** De $(0, 0)$ a $(3, 2)$.

**Eje de simetría:** De $x = 0$ a $x = 3$.

---

## ⚙️ Ejemplo 6: Identificar desplazamientos

Dada $g(x) = |x + 5| - 4$, identifica las transformaciones desde $f(x) = |x|$.

**Análisis:**
- $x + 5 = x - (-5)$ → desplazamiento 5 unidades a la **izquierda**
- $-4$ → desplazamiento 4 unidades hacia **abajo**

**Vértice:** $(-5, -4)$

---

## 📊 Resumen de desplazamientos

| Transformación | Ecuación | Efecto |
|----------------|----------|--------|
| Vertical arriba | $f(x) + k$ ($k > 0$) | Sube $k$ unidades |
| Vertical abajo | $f(x) - k$ ($k > 0$) | Baja $k$ unidades |
| Horizontal derecha | $f(x - h)$ ($h > 0$) | Derecha $h$ unidades |
| Horizontal izquierda | $f(x + h)$ ($h > 0$) | Izquierda $h$ unidades |

### 💡 Tip para recordar

- **Vertical:** El signo es directo ($+$ sube, $-$ baja)
- **Horizontal:** El signo es opuesto ($-h$ va a la derecha)

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Describe las transformaciones y el nuevo vértice/punto clave:

a) $g(x) = x^2 - 5$
b) $h(x) = (x + 1)^2$
c) $k(x) = (x - 2)^2 + 3$

<details>
<summary>Ver soluciones</summary>

a) Baja 5 unidades. Vértice: $(0, -5)$

b) Izquierda 1 unidad. Vértice: $(-1, 0)$

c) Derecha 2, arriba 3. Vértice: $(2, 3)$
</details>

---

**Ejercicio 2:** Escribe la ecuación de la función:

a) $f(x) = |x|$ desplazada 4 a la derecha y 1 hacia arriba
b) $f(x) = \sqrt{x}$ desplazada 2 a la izquierda y 3 hacia abajo

<details>
<summary>Ver soluciones</summary>

a) $g(x) = |x - 4| + 1$

b) $h(x) = \sqrt{x + 2} - 3$
</details>

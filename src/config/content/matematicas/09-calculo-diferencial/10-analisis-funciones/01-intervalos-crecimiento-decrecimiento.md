---
title: "Intervalos de Crecimiento y Decrecimiento"
---

# Intervalos de Crecimiento y Decrecimiento

La derivada nos dice en qué intervalos una función crece o decrece. Esta información es fundamental para entender el comportamiento de funciones.

---

## 🎯 ¿Qué vas a aprender?

- Criterio para crecimiento/decrecimiento
- Cómo encontrar los intervalos
- Relación con la gráfica de la función
- Aplicaciones prácticas

---

## 📖 Criterio de monotonía

Para una función diferenciable en un intervalo $(a, b)$:

| Condición | Comportamiento |
|-----------|----------------|
| $f'(x) > 0$ para todo $x$ en $(a, b)$ | $f$ es **creciente** en $(a, b)$ |
| $f'(x) < 0$ para todo $x$ en $(a, b)$ | $f$ es **decreciente** en $(a, b)$ |
| $f'(x) = 0$ para todo $x$ en $(a, b)$ | $f$ es **constante** en $(a, b)$ |

---

## 📖 Método para encontrar intervalos

1. **Derivar** $f(x)$
2. **Encontrar** dónde $f'(x) = 0$ o no existe (puntos críticos)
3. **Dividir** el dominio en intervalos usando los puntos críticos
4. **Evaluar** el signo de $f'(x)$ en cada intervalo
5. **Concluir** sobre crecimiento/decrecimiento

---

## ⚙️ Ejemplo 1: Polinomio cuadrático

Encuentra los intervalos de crecimiento/decrecimiento de $f(x) = x^2 - 4x + 3$.

**Paso 1:** $f'(x) = 2x - 4$

**Paso 2:** $f'(x) = 0 \Rightarrow x = 2$

**Paso 3:** Intervalos: $(-\infty, 2)$ y $(2, +\infty)$

**Paso 4:** 
- En $(-\infty, 2)$: prueba $x = 0$ → $f'(0) = -4 < 0$
- En $(2, +\infty)$: prueba $x = 3$ → $f'(3) = 2 > 0$

**Paso 5:**
- **Decreciente** en $(-\infty, 2)$
- **Creciente** en $(2, +\infty)$

---

## ⚙️ Ejemplo 2: Polinomio cúbico

$f(x) = x^3 - 3x^2 - 9x + 5$

**Derivada:**
$$f'(x) = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x-3)(x+1)$$

**Puntos críticos:** $x = -1, 3$

**Tabla de signos:**

| Intervalo | Signo de $f'(x)$ | Comportamiento |
|-----------|------------------|----------------|
| $(-\infty, -1)$ | $(-)(-) = +$ | Creciente |
| $(-1, 3)$ | $(+)(-) = -$ | Decreciente |
| $(3, +\infty)$ | $(+)(+) = +$ | Creciente |

---

## ⚙️ Ejemplo 3: Función racional

$f(x) = \frac{x}{x^2 + 1}$

**Derivada (cociente):**
$$f'(x) = \frac{(1)(x^2+1) - (x)(2x)}{(x^2+1)^2} = \frac{1 - x^2}{(x^2+1)^2}$$

**Puntos críticos:** $1 - x^2 = 0 \Rightarrow x = \pm 1$

**Tabla de signos:**

| Intervalo | Signo de $1 - x^2$ | Comportamiento |
|-----------|-------------------|----------------|
| $(-\infty, -1)$ | $-$ | Decreciente |
| $(-1, 1)$ | $+$ | Creciente |
| $(1, +\infty)$ | $-$ | Decreciente |

---

## ⚙️ Ejemplo 4: Con función trigonométrica

$f(x) = \sin x + \cos x$ en $[0, 2\pi]$

$$f'(x) = \cos x - \sin x = 0$$
$$\cos x = \sin x \Rightarrow \tan x = 1$$
$$x = \frac{\pi}{4}, \frac{5\pi}{4}$$

**Tabla de signos:**

| Intervalo | $f'(x)$ | Comportamiento |
|-----------|---------|----------------|
| $(0, \frac{\pi}{4})$ | $+$ | Creciente |
| $(\frac{\pi}{4}, \frac{5\pi}{4})$ | $-$ | Decreciente |
| $(\frac{5\pi}{4}, 2\pi)$ | $+$ | Creciente |

---

## 📖 Interpretación gráfica

| Signo de $f'$ | Gráfica |
|---------------|---------|
| $f' > 0$ | Sube de izquierda a derecha |
| $f' < 0$ | Baja de izquierda a derecha |
| $f' = 0$ | Tangente horizontal (posible extremo) |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra los intervalos de crecimiento/decrecimiento:

$$f(x) = x^3 - 12x + 1$$

<details>
<summary>Ver solución</summary>

$f'(x) = 3x^2 - 12 = 3(x^2 - 4) = 3(x-2)(x+2)$

Puntos críticos: $x = \pm 2$

- Creciente en $(-\infty, -2) \cup (2, +\infty)$
- Decreciente en $(-2, 2)$
</details>

---

**Ejercicio 2:** Analiza $f(x) = e^x - x$.

<details>
<summary>Ver solución</summary>

$f'(x) = e^x - 1 = 0 \Rightarrow x = 0$

- Para $x < 0$: $e^x < 1 \Rightarrow f' < 0$ (Decreciente)
- Para $x > 0$: $e^x > 1 \Rightarrow f' > 0$ (Creciente)
</details>

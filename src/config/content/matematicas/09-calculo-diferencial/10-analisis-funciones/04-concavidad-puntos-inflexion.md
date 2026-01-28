---
title: "Concavidad y Puntos de Inflexión"
---

# Concavidad y Puntos de Inflexión

La segunda derivada nos revela la "curvatura" de una función: si se curva hacia arriba o hacia abajo. Los puntos donde cambia la curvatura son los puntos de inflexión.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la concavidad
- Cómo determinar concavidad con $f''$
- Definición de punto de inflexión
- Cómo encontrar puntos de inflexión

---

## 📖 Concavidad

| Tipo | Descripción visual | Condición |
|------|-------------------|-----------|
| **Cóncava hacia arriba** (convexa) | La curva está por encima de sus tangentes | $f''(x) > 0$ |
| **Cóncava hacia abajo** | La curva está por debajo de sus tangentes | $f''(x) < 0$ |

---

## 📖 Criterio de concavidad

- Si $f''(x) > 0$ en un intervalo: $f$ es **cóncava hacia arriba** (⌣)
- Si $f''(x) < 0$ en un intervalo: $f$ es **cóncava hacia abajo** (⌢)

---

## 📖 Punto de inflexión

Un **punto de inflexión** es donde la función cambia de concavidad.

**Condiciones:**
1. La concavidad cambia en ese punto
2. El punto debe estar en la gráfica (función definida)

---

## 📖 Cómo encontrar puntos de inflexión

1. Calcular $f''(x)$
2. Encontrar dónde $f''(x) = 0$ o no existe
3. Verificar cambio de signo de $f''$ en esos puntos
4. Calcular las coordenadas $(c, f(c))$

---

## ⚙️ Ejemplo 1: Cúbica

$f(x) = x^3 - 3x^2 + 2$

$$
f'(x) = 3x^2 - 6x
$$

$$
f''(x) = 6x - 6 = 6(x - 1)
$$

**$f''(x) = 0$:** $x = 1$

**Signos de $f''$:**
- $x < 1$: $f'' < 0$ (cóncava abajo)
- $x > 1$: $f'' > 0$ (cóncava arriba)

**Punto de inflexión:** $(1, f(1)) = (1, 0)$

---

## ⚙️ Ejemplo 2: Cuártica

$f(x) = x^4 - 6x^2$

$$
f'(x) = 4x^3 - 12x
$$

$$
f''(x) = 12x^2 - 12 = 12(x^2 - 1) = 12(x-1)(x+1)
$$

**$f''(x) = 0$:** $x = -1, 1$

**Tabla de signos:**

| Intervalo | $f''(x)$ | Concavidad |
|-----------|----------|------------|
| $x < -1$ | $+$ | Arriba |
| $-1 < x < 1$ | $-$ | Abajo |
| $x > 1$ | $+$ | Arriba |

**Puntos de inflexión:**
- $(-1, f(-1)) = (-1, -5)$
- $(1, f(1)) = (1, -5)$

---

## ⚙️ Ejemplo 3: Sin punto de inflexión

$f(x) = x^4$

$$f''(x) = 12x^2$$

$f''(x) = 0$ solo en $x = 0$

Pero $f''(x) \geq 0$ para todo $x$ (no cambia de signo).

**No hay punto de inflexión** (siempre cóncava arriba).

---

## ⚙️ Ejemplo 4: Función exponencial

$f(x) = xe^x$

$$
f'(x) = e^x + xe^x = e^x(1 + x)
$$

$$
f''(x) = e^x(1+x) + e^x = e^x(2 + x)
$$

**$f''(x) = 0$:** $x = -2$

**Signos:**
- $x < -2$: $f'' < 0$
- $x > -2$: $f'' > 0$

**Punto de inflexión:** $(-2, -2e^{-2}) \approx (-2, -0.27)$

---

## ⚙️ Ejemplo 5: Trigonométrica

$f(x) = \sin x$ en $[0, 2\pi]$

$$f''(x) = -\sin x = 0$$
$$x = 0, \pi, 2\pi$$

**Signos:**
- $(0, \pi)$: $-\sin x < 0$ (cóncava abajo)
- $(\pi, 2\pi)$: $-\sin x > 0$ (cóncava arriba)

**Punto de inflexión:** $(\pi, 0)$

---

## 📖 Interpretación física

Si $s(t)$ es posición:
- $s''(t) = a(t)$ aceleración
- $s'' > 0$: acelerando
- $s'' < 0$: desacelerando
- Punto de inflexión: cambio en la aceleración

---

## 📊 Resumen visual

```
Cóncava arriba (f'' > 0):    Cóncava abajo (f'' < 0):
       ⌣                            ⌢
      / \                          \   /
     /   \                          \ /
```

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra intervalos de concavidad y puntos de inflexión:

$$
f(x) = x^3 + 3x^2 - 9x + 5
$$

<details>
<summary>Ver solución</summary>

$f''(x) = 6x + 6 = 0 \Rightarrow x = -1$

- $x < -1$: $f'' < 0$ (cóncava abajo)
- $x > -1$: $f'' > 0$ (cóncava arriba)

Punto de inflexión: $(-1, f(-1)) = (-1, 16)$
</details>

---

**Ejercicio 2:** Analiza la concavidad de $f(x) = \ln x$.

<details>
<summary>Ver solución</summary>

$f'(x) = \frac{1}{x}$

$f''(x) = -\frac{1}{x^2} < 0$ para todo $x > 0$

Siempre cóncava hacia abajo en su dominio. No hay puntos de inflexión.
</details>

---
title: "Inecuaciones Cuadráticas"
---

# Inecuaciones Cuadráticas

¿Qué pasa cuando la variable está elevada al cuadrado en una desigualdad? Las inecuaciones cuadráticas requieren un enfoque diferente: analizar el signo de una parábola.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una inecuación cuadrática
- El método de los puntos críticos
- Análisis de signos usando la parábola
- Resolver casos especiales

---

## 📖 ¿Qué es una inecuación cuadrática?

Una **inecuación cuadrática** es una desigualdad donde el mayor exponente de la variable es 2. Su forma estándar es:

$$
ax^2 + bx + c < 0 \quad \text{(o con } >, \leq, \geq \text{)}
$$

donde $a \neq 0$.

**Ejemplos:**
- $x^2 - 4 > 0$
- $2x^2 - 3x - 2 \leq 0$
- $-x^2 + 5x - 6 \geq 0$

---

## 📖 Método de los puntos críticos

El método consiste en encontrar las raíces del polinomio y analizar el signo en cada intervalo.

### Pasos:

1. **Igualar a cero** y factorizar (o usar fórmula general)
2. **Encontrar las raíces** (puntos críticos)
3. **Dividir la recta** en intervalos
4. **Evaluar el signo** en cada intervalo
5. **Seleccionar los intervalos** que satisfacen la desigualdad

---

## ⚙️ Ejemplo 1: Factorización directa

Resolver: $x^2 - 5x + 6 < 0$

**Paso 1:** Factorizamos
$$
x^2 - 5x + 6 = (x - 2)(x - 3)
$$

**Paso 2:** Encontramos las raíces
$$
x - 2 = 0 \Rightarrow x = 2 \quad \text{y} \quad x - 3 = 0 \Rightarrow x = 3
$$

**Paso 3:** Dividimos la recta en intervalos

```
←━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━→
          2         3
   I       II       III
```

**Paso 4:** Evaluamos el signo de $(x-2)(x-3)$ en cada intervalo

| Intervalo | Valor de prueba | $(x-2)$ | $(x-3)$ | Producto |
|-----------|-----------------|---------|---------|----------|
| $(-\infty, 2)$ | $x = 0$ | $(-)$ | $(-)$ | $(+)$ |
| $(2, 3)$ | $x = 2.5$ | $(+)$ | $(-)$ | $(-)$ |
| $(3, +\infty)$ | $x = 4$ | $(+)$ | $(+)$ | $(+)$ |

**Paso 5:** Necesitamos $< 0$, es decir, donde el producto es negativo.

**Solución:** $x \in (2, 3)$

---

## ⚙️ Ejemplo 2: Usando la parábola como guía

Resolver: $x^2 - 4 \geq 0$

**Paso 1:** Factorizamos (diferencia de cuadrados)
$$
x^2 - 4 = (x - 2)(x + 2)
$$

**Paso 2:** Raíces: $x = -2$ y $x = 2$

**Paso 3:** La parábola $y = x^2 - 4$ abre hacia arriba ($a = 1 > 0$).

Esto significa:
- **Negativa** entre las raíces
- **Positiva** fuera de las raíces

```
    ↗          ↗
     \        /
      \      /
       \    /
────────●──●────────
       -2  2
```

**Paso 4:** Necesitamos $\geq 0$ (positivo o cero).

**Solución:** $x \in (-\infty, -2] \cup [2, +\infty)$

Los corchetes incluyen las raíces porque la desigualdad es $\geq$.

---

## ⚙️ Ejemplo 3: Parábola que abre hacia abajo

Resolver: $-x^2 + 4x - 3 > 0$

**Paso 1:** Factorizamos (o usamos fórmula general)

Multiplicamos por $-1$ para facilitar:
$$
x^2 - 4x + 3 < 0
$$

Factorizamos:
$$
(x - 1)(x - 3) < 0
$$

**Paso 2:** Raíces: $x = 1$ y $x = 3$

**Paso 3:** La parábola $y = x^2 - 4x + 3$ abre hacia arriba, así que es negativa entre las raíces.

**Paso 4:** Necesitamos $< 0$.

**Solución:** $x \in (1, 3)$

---

## ⚙️ Ejemplo 4: Sin raíces reales

Resolver: $x^2 + x + 1 > 0$

**Paso 1:** Calculamos el discriminante
$$
\Delta = b^2 - 4ac = 1 - 4(1)(1) = -3 < 0
$$

No hay raíces reales.

**Paso 2:** La parábola $y = x^2 + x + 1$ tiene $a = 1 > 0$ (abre hacia arriba) y nunca toca el eje $x$.

Esto significa que la parábola está **siempre por encima** del eje $x$, es decir, siempre positiva.

**Solución:** $x \in \mathbb{R}$ (todos los números reales)

---

## ⚙️ Ejemplo 5: Usando la fórmula general

Resolver: $2x^2 - 7x + 3 \leq 0$

**Paso 1:** Fórmula general
$$
x = \frac{7 \pm \sqrt{49 - 24}}{4} = \frac{7 \pm \sqrt{25}}{4} = \frac{7 \pm 5}{4}
$$

$$
x_1 = \frac{7 - 5}{4} = \frac{1}{2} \quad \text{y} \quad x_2 = \frac{7 + 5}{4} = 3
$$

**Paso 2:** La parábola abre hacia arriba ($a = 2 > 0$), es negativa entre las raíces.

**Paso 3:** Necesitamos $\leq 0$.

**Solución:** $x \in \left[\frac{1}{2}, 3\right]$

---

## 📊 Resumen: Regla de la parábola

| Si $a > 0$ (abre ↑) | Si $a < 0$ (abre ↓) |
|---------------------|---------------------|
| Negativo **entre** raíces | Positivo **entre** raíces |
| Positivo **fuera** de raíces | Negativo **fuera** de raíces |

### 💡 Tip rápido

Para $ax^2 + bx + c$ con raíces $r_1 < r_2$:

| Desigualdad | Si $a > 0$ | Si $a < 0$ |
|-------------|------------|------------|
| $> 0$ | $(-\infty, r_1) \cup (r_2, +\infty)$ | $(r_1, r_2)$ |
| $< 0$ | $(r_1, r_2)$ | $(-\infty, r_1) \cup (r_2, +\infty)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve las siguientes inecuaciones:

a) $x^2 - 9 > 0$
b) $x^2 - 2x - 8 \leq 0$
c) $-x^2 + 6x - 5 \geq 0$

<details>
<summary>Ver soluciones</summary>

a) $(x-3)(x+3) > 0$. Raíces: $x = -3, 3$. Parábola ↑.
   
   **Solución:** $(-\infty, -3) \cup (3, +\infty)$

b) $(x-4)(x+2) \leq 0$. Raíces: $x = -2, 4$. Parábola ↑.
   
   **Solución:** $[-2, 4]$

c) Multiplicamos por $-1$: $x^2 - 6x + 5 \leq 0$, $(x-1)(x-5) \leq 0$
   
   **Solución:** $[1, 5]$
</details>

---

**Ejercicio 2:** Determina el conjunto solución:

a) $x^2 + 4 > 0$
b) $x^2 + 2x + 5 \leq 0$
c) $4x^2 - 4x + 1 \geq 0$

<details>
<summary>Ver soluciones</summary>

a) $\Delta = -16 < 0$, parábola ↑ siempre positiva.
   
   **Solución:** $\mathbb{R}$ (todos los reales)

b) $\Delta = 4 - 20 = -16 < 0$, parábola ↑ siempre positiva.
   
   **Solución:** $\emptyset$ (no hay solución)

c) $(2x - 1)^2 \geq 0$. Un cuadrado siempre es $\geq 0$.
   
   **Solución:** $\mathbb{R}$ (todos los reales)
</details>

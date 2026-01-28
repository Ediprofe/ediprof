---
title: "Gráficas con Valor Absoluto"
---

# Gráficas con Valor Absoluto

¿Cómo se ve la gráfica de una función con valor absoluto? Aprenderás a transformar cualquier gráfica aplicando el valor absoluto, creando esas características "V" y reflexiones.

---

## 🎯 ¿Qué vas a aprender?

- Graficar la función $y = |x|$ y sus transformaciones
- El efecto de $|f(x)|$ en una gráfica
- El efecto de $f(|x|)$ en una gráfica
- Técnicas de graficación por partes

---

## 📖 La función valor absoluto básica

La función $f(x) = |x|$ es la función valor absoluto más simple.

**Definición por partes:**
$$
f(x) = |x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}
$$

**Características:**
- **Dominio:** $\mathbb{R}$ (todos los reales)
- **Rango:** $[0, +\infty)$ (no negativos)
- **Vértice:** $(0, 0)$
- **Forma:** V invertida (abre hacia arriba)
- **Simetría:** Par (simétrica respecto al eje Y)

```
        ↗       ↗
         \     /
          \   /
           \ /
────────────●────────────
            0
```

---

## 📖 Transformaciones de $y = |x|$

Las transformaciones funcionan igual que con cualquier función.

| Transformación | Efecto |
|---------------|--------|
| $y = \|x\| + k$ | Traslación vertical: sube si $k > 0$ |
| $y = \|x - h\|$ | Traslación horizontal: derecha si $h > 0$ |
| $y = a\|x\|$ | Dilatación/compresión vertical |
| $y = -\|x\|$ | Reflexión respecto al eje X (V hacia abajo) |
| $y = \|x - h\| + k$ | Vértice en $(h, k)$ |

---

## ⚙️ Ejemplo 1: Traslaciones

Grafiquemos $y = |x - 2| + 3$

**Análisis:**
- Traslación 2 unidades a la derecha
- Traslación 3 unidades hacia arriba
- **Vértice:** $(2, 3)$

**Definición por partes:**
$$
y = \begin{cases} (x-2) + 3 = x + 1 & \text{si } x \geq 2 \\ -(x-2) + 3 = -x + 5 & \text{si } x < 2 \end{cases}
$$

**Puntos clave:**
- Vértice: $(2, 3)$
- Cuando $x = 0$: $y = |0-2|+3 = 5$ → punto $(0, 5)$
- Cuando $x = 4$: $y = |4-2|+3 = 5$ → punto $(4, 5)$

---

## ⚙️ Ejemplo 2: Reflexión

Grafiquemos $y = -|x| + 4$

**Análisis:**
- Reflexión respecto al eje X (la V apunta hacia abajo)
- Traslación 4 unidades hacia arriba
- **Vértice:** $(0, 4)$ (punto máximo)

**Definición por partes:**
$$
y = \begin{cases} -x + 4 & \text{si } x \geq 0 \\ x + 4 & \text{si } x < 0 \end{cases}
$$

La gráfica tiene forma de Λ (montaña).

---

## 📖 El efecto de $|f(x)|$ vs $f(|x|)$

### Caso 1: $y = |f(x)|$

Tomar el valor absoluto de **toda la función** $f(x)$:

> **Regla:** Las partes de la gráfica que están **debajo** del eje X se **reflejan hacia arriba**.

### Caso 2: $y = f(|x|)$

Tomar el valor absoluto de **la variable** $x$:

> **Regla:** La parte de la gráfica para $x \geq 0$ se **refleja** hacia la izquierda (simetría respecto al eje Y).

---

## ⚙️ Ejemplo 3: $y = |f(x)|$

Sea $f(x) = x - 2$. Grafiquemos $y = |x - 2|$.

**Gráfica original de $f(x) = x - 2$:**
- Es una línea recta con pendiente 1
- Cruza el eje X en $x = 2$

**Aplicamos $|f(x)|$:**
- La parte donde $f(x) < 0$ (es decir, $x < 2$) se refleja hacia arriba

```
Original:          Con valor absoluto:
     /                  ↗
    /                   /\
───●────               ●──●────
   2                   0  2
```

**Resultado:** Una V con vértice en $(2, 0)$.

---

## ⚙️ Ejemplo 4: $y = f(|x|)$

Sea $f(x) = x - 2$. Grafiquemos $y = |x| - 2$.

**Método:** Solo usamos $x \geq 0$ de la función original, luego reflejamos.

Para $x \geq 0$: $y = x - 2$ (línea con pendiente 1)
Para $x < 0$: $y = -x - 2$ (reflejo de lo anterior)

```
       /\
      /  \
─────●────●─────
    -2    2
```

**Resultado:** Una V con vértice en $(0, -2)$.

---

## ⚙️ Ejemplo 5: Función parabólica

Sea $f(x) = x^2 - 4$. Grafiquemos:

**a) $y = |x^2 - 4|$**

La parábola original corta el eje X en $x = -2$ y $x = 2$.

Entre estos puntos, $f(x) < 0$, así que esa parte se refleja hacia arriba.

```
Original:              Con |f(x)|:
\     /                 /\  /\
 \   /                 /  \/  \
──●─────●──           ●────────●
 -2    2              -2       2
```

**b) $y = (|x|)^2 - 4 = x^2 - 4$**

Como $(|x|)^2 = x^2$, obtenemos la misma parábola original.

---

## 📖 Graficación por partes

Cuando la expresión dentro del valor absoluto es más compleja, usamos el método por partes:

1. Encontrar dónde la expresión interior es cero
2. Determinar el signo en cada intervalo
3. Escribir la función por partes
4. Graficar cada parte

---

## ⚙️ Ejemplo 6: $y = |2x - 3| + |x + 1|$

**Paso 1:** Encontrar los puntos críticos
- $2x - 3 = 0 \Rightarrow x = \frac{3}{2}$
- $x + 1 = 0 \Rightarrow x = -1$

**Paso 2:** Dividir en intervalos: $(-\infty, -1)$, $(-1, \frac{3}{2})$, $(\frac{3}{2}, +\infty)$

**Paso 3:** Analizar signos y escribir por partes

| Intervalo | $2x - 3$ | $x + 1$ | $y$ |
|-----------|----------|---------|-----|
| $x < -1$ | $(-)$ | $(-)$ | $-(2x-3) + -(x+1) = -3x + 2$ |
| $-1 \leq x < \frac{3}{2}$ | $(-)$ | $(+)$ | $-(2x-3) + (x+1) = -x + 4$ |
| $x \geq \frac{3}{2}$ | $(+)$ | $(+)$ | $(2x-3) + (x+1) = 3x - 2$ |

**Paso 4:** Graficar cada segmento lineal

---

## 📊 Resumen visual

| Operación | Efecto gráfico |
|-----------|----------------|
| $\|f(x)\|$ | Refleja hacia arriba lo que está debajo del eje X |
| $f(\|x\|)$ | Elimina la parte para $x < 0$ y la reemplaza por el reflejo de $x > 0$ |
| $y = \|x - h\| + k$ | V con vértice en $(h, k)$ |
| $y = -\|x\|$ | V invertida (montaña) |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica el vértice y describe la gráfica:

a) $y = |x + 3|$
b) $y = |x - 1| - 2$
c) $y = -|x + 2| + 5$

<details>
<summary>Ver soluciones</summary>

a) Vértice: $(-3, 0)$. V abriendo hacia arriba.

b) Vértice: $(1, -2)$. V abriendo hacia arriba.

c) Vértice: $(-2, 5)$. V abriendo hacia abajo (montaña), punto máximo en el vértice.
</details>

---

**Ejercicio 2:** Escribe por partes:

a) $y = |3x - 6|$
b) $y = |x| + |x - 2|$

<details>
<summary>Ver soluciones</summary>

a) Punto crítico: $x = 2$
$$
y = \begin{cases} -(3x-6) = -3x + 6 & \text{si } x < 2 \\ 3x - 6 & \text{si } x \geq 2 \end{cases}
$$

b) Puntos críticos: $x = 0$ y $x = 2$
$$
y = \begin{cases} -x + -(x-2) = -2x + 2 & \text{si } x < 0 \\ x + -(x-2) = 2 & \text{si } 0 \leq x < 2 \\ x + (x-2) = 2x - 2 & \text{si } x \geq 2 \end{cases}
$$
</details>

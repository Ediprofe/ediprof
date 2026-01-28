---
title: "Estiramientos y Compresiones"
---

# Estiramientos y Compresiones

Al multiplicar por una constante, podemos estirar o comprimir una gráfica verticalmente u horizontalmente. Estas transformaciones cambian la "escala" de la función.

---

## 🎯 ¿Qué vas a aprender?

- Estiramientos y compresiones verticales
- Estiramientos y compresiones horizontales
- Diferenciar entre ambos tipos
- Efecto en la forma de la gráfica

---

## 📖 Estiramiento/compresión vertical

Multiplica las **salidas** por una constante.

### Regla

$$g(x) = a \cdot f(x)$$

| Valor de $\|a\|$ | Efecto |
|------------------|--------|
| $\|a\| > 1$ | **Estiramiento** vertical (gráfica más alta) |
| $0 < \|a\| < 1$ | **Compresión** vertical (gráfica más baja) |
| $a < 0$ | También hay reflexión en eje X |

### Interpretación

Cada valor $y$ se multiplica por $a$. Los puntos se alejan o acercan al eje X.

---

## ⚙️ Ejemplo 1: Estiramiento vertical

Sea $f(x) = x^2$. Compara $f(x)$, $2f(x)$ y $\frac{1}{2}f(x)$.

**Puntos para $x = 2$:**
- $f(2) = 4$
- $2f(2) = 8$ (estirada)
- $\frac{1}{2}f(2) = 2$ (comprimida)

**Efecto visual:**
- $2f(x) = 2x^2$: Parábola más angosta
- $\frac{1}{2}f(x) = \frac{1}{2}x^2$: Parábola más ancha

---

## 📖 Estiramiento/compresión horizontal

Multiplica el **argumento** por una constante.

### Regla

$$g(x) = f(b \cdot x)$$

| Valor de $\|b\|$ | Efecto |
|------------------|--------|
| $\|b\| > 1$ | **Compresión** horizontal (gráfica más angosta) |
| $0 < \|b\| < 1$ | **Estiramiento** horizontal (gráfica más ancha) |
| $b < 0$ | También hay reflexión en eje Y |

### ⚠️ ¡Cuidado! Es inverso

- Multiplicar por $b > 1$ **comprime** horizontalmente
- Multiplicar por $0 < b < 1$ **estira** horizontalmente

### Interpretación

El factor $\frac{1}{b}$ es el factor de escala horizontal.

---

## ⚙️ Ejemplo 2: Compresión horizontal

Sea $f(x) = |x|$. Compara $f(x)$ y $f(2x)$.

**Puntos:**

| $x$ | $f(x) = \|x\|$ | $f(2x) = \|2x\|$ |
|-----|---------------|-----------------|
| $0$ | $0$ | $0$ |
| $1$ | $1$ | $2$ |
| $2$ | $2$ | $4$ |

**Pero observa:** El valor $f(x) = 2$ ocurría en $x = 2$. Ahora $f(2x) = 2$ ocurre en $x = 1$.

La gráfica se **comprime horizontalmente** por factor $\frac{1}{2}$.

---

## ⚙️ Ejemplo 3: Estiramiento horizontal

Sea $f(x) = x^2$. Grafica $g(x) = f\left(\frac{x}{3}\right) = \left(\frac{x}{3}\right)^2$.

**Factor:** $b = \frac{1}{3}$, entonces la gráfica se **estira** horizontalmente por factor $3$.

**Puntos:**

| Original | Transformado |
|----------|--------------|
| $(1, 1)$ | $(3, 1)$ |
| $(2, 4)$ | $(6, 4)$ |

---

## 📖 Comparación visual

Para $f(x) = x^2$:

| Función | Tipo | Factor |
|---------|------|--------|
| $3x^2$ | Estiramiento vertical | $3$ |
| $\frac{1}{3}x^2$ | Compresión vertical | $\frac{1}{3}$ |
| $(3x)^2 = 9x^2$ | Compresión horizontal | $\frac{1}{3}$ |
| $\left(\frac{x}{3}\right)^2 = \frac{x^2}{9}$ | Estiramiento horizontal | $3$ |

### Nota importante

$(3x)^2 = 9x^2$ → Una compresión horizontal por $\frac{1}{3}$ es equivalente a un estiramiento vertical por $9$ para esta función.

---

## 📖 Forma general

La forma general que incluye todas las transformaciones es:

$$g(x) = a \cdot f(b(x - h)) + k$$

| Parámetro | Efecto |
|-----------|--------|
| $a$ | Estiramiento/compresión vertical y reflexión en X |
| $b$ | Estiramiento/compresión horizontal y reflexión en Y |
| $h$ | Desplazamiento horizontal |
| $k$ | Desplazamiento vertical |

---

## ⚙️ Ejemplo 4: Análisis completo

Describe las transformaciones de $g(x) = 3|2x - 4| + 1$ desde $f(x) = |x|$.

**Paso 1:** Reescribimos para identificar parámetros:
$$g(x) = 3|2(x - 2)| + 1$$

**Parámetros:**
- $a = 3$: Estiramiento vertical por 3
- $b = 2$: Compresión horizontal por $\frac{1}{2}$
- $h = 2$: Desplazamiento 2 a la derecha
- $k = 1$: Desplazamiento 1 hacia arriba

**Vértice:** $(2, 1)$

**Pendientes:** $\pm 3 \cdot 2 = \pm 6$

---

## 📊 Resumen de efectos

| Transformación | Ecuación | Efecto |
|----------------|----------|--------|
| Estiramiento vertical | $a \cdot f(x)$, $a > 1$ | Se aleja del eje X |
| Compresión vertical | $a \cdot f(x)$, $0 < a < 1$ | Se acerca al eje X |
| Compresión horizontal | $f(bx)$, $b > 1$ | Se acerca al eje Y |
| Estiramiento horizontal | $f(bx)$, $0 < b < 1$ | Se aleja del eje Y |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Describe la transformación:

a) $g(x) = 4\sqrt{x}$ desde $f(x) = \sqrt{x}$
b) $h(x) = \sqrt{4x}$ desde $f(x) = \sqrt{x}$
c) $k(x) = \frac{1}{3}x^2$ desde $f(x) = x^2$

<details>
<summary>Ver soluciones</summary>

a) Estiramiento vertical por factor 4

b) Compresión horizontal por factor $\frac{1}{4}$ (o estiramiento vertical por factor $2$, ya que $\sqrt{4x} = 2\sqrt{x}$)

c) Compresión vertical por factor $\frac{1}{3}$
</details>

---

**Ejercicio 2:** Si el punto $(2, 5)$ está en la gráfica de $f(x)$, ¿dónde está en la gráfica de...?

a) $3f(x)$
b) $f(2x)$
c) $f\left(\frac{x}{4}\right)$

<details>
<summary>Ver soluciones</summary>

a) $(2, 15)$ — la $y$ se multiplica por 3

b) $(1, 5)$ — la $x$ se divide por 2

c) $(8, 5)$ — la $x$ se multiplica por 4
</details>

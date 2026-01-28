---
title: "Reflexiones"
---

# Reflexiones

Las reflexiones crean imágenes espejo de las gráficas. Son fundamentales para entender simetría y para manipular funciones de manera precisa.

---

## 🎯 ¿Qué vas a aprender?

- Reflexión respecto al eje X
- Reflexión respecto al eje Y
- Reflexión respecto al origen
- Cómo afectan la paridad de funciones

---

## 📖 Reflexión respecto al eje X

Cambia el signo de todas las salidas.

### Regla

$$g(x) = -f(x)$$

### Efecto

Cada punto $(x, y)$ se transforma en $(x, -y)$.

La gráfica se "voltea" verticalmente.

---

## ⚙️ Ejemplo 1: Reflexión en eje X

Sea $f(x) = x^2$. Grafica $g(x) = -x^2$.

**Puntos:**

| $(x, f(x))$ | $(x, -f(x))$ |
|-------------|--------------|
| $(0, 0)$ | $(0, 0)$ |
| $(1, 1)$ | $(1, -1)$ |
| $(2, 4)$ | $(2, -4)$ |

**Efecto:** La parábola que abría hacia arriba ahora abre hacia abajo.

---

## 📖 Reflexión respecto al eje Y

Cambia el signo de todas las entradas.

### Regla

$$g(x) = f(-x)$$

### Efecto

Cada punto $(x, y)$ se transforma en $(-x, y)$.

La gráfica se "voltea" horizontalmente.

---

## ⚙️ Ejemplo 2: Reflexión en eje Y

Sea $f(x) = \sqrt{x}$. Grafica $g(x) = \sqrt{-x}$.

**Análisis:**
- Dominio original: $[0, +\infty)$
- Dominio de $g$: $-x \geq 0 \Rightarrow x \leq 0$ → $(-\infty, 0]$

**Puntos:**

| $(x, f(x))$ | $(-x, f(-x))$ |
|-------------|---------------|
| $(0, 0)$ | $(0, 0)$ |
| $(4, 2)$ | $(-4, 2)$ |
| $(9, 3)$ | $(-9, 3)$ |

**Efecto:** La raíz cuadrada ahora existe en el lado izquierdo.

---

## 📖 Reflexión respecto al origen

Combina ambas reflexiones.

### Regla

$$g(x) = -f(-x)$$

### Efecto

Cada punto $(x, y)$ se transforma en $(-x, -y)$.

Es una rotación de 180° alrededor del origen.

---

## ⚙️ Ejemplo 3: Reflexión en el origen

Sea $f(x) = x^3 + x$. Grafica $g(x) = -f(-x)$.

$$g(x) = -((-x)^3 + (-x)) = -(-x^3 - x) = x^3 + x$$

¡La función es igual! Esto significa que $f$ es **impar** (simétrica respecto al origen).

---

## ⚙️ Ejemplo 4: Función no simétrica

Sea $f(x) = 2^x$. Compara $f(x)$, $-f(x)$ y $f(-x)$.

**$f(x) = 2^x$:** Crece exponencialmente hacia la derecha.

**$-f(x) = -2^x$:** Reflexión en eje X (decrece por debajo del eje).

**$f(-x) = 2^{-x} = \frac{1}{2^x}$:** Reflexión en eje Y (decrece hacia la derecha).

---

## 📊 Resumen de reflexiones

| Transformación | Ecuación | Efecto en puntos |
|----------------|----------|------------------|
| Eje X | $-f(x)$ | $(x, y) \to (x, -y)$ |
| Eje Y | $f(-x)$ | $(x, y) \to (-x, y)$ |
| Origen | $-f(-x)$ | $(x, y) \to (-x, -y)$ |

---

## 📖 Relación con paridad

| Tipo de función | Condición | Simétrica respecto a |
|-----------------|-----------|---------------------|
| Par | $f(-x) = f(x)$ | Eje Y |
| Impar | $f(-x) = -f(x)$ | Origen |

### Interpretación

- Si $f(-x) = f(x)$, la reflexión en Y da la misma función.
- Si $f(-x) = -f(x)$, la reflexión en Y es igual a la reflexión en X.

---

## ⚙️ Ejemplo 5: Combinación de transformaciones

Dada $f(x) = x^2$, grafica $g(x) = -(x - 2)^2 + 3$.

**Transformaciones (en orden):**
1. Desplazamiento 2 a la derecha: $(x - 2)^2$
2. Reflexión en eje X: $-(x - 2)^2$
3. Desplazamiento 3 hacia arriba: $-(x - 2)^2 + 3$

**Vértice:** $(2, 3)$

**Orientación:** Abre hacia abajo (máximo en el vértice)

---

## 📖 Orden de las transformaciones

Cuando hay múltiples transformaciones, el orden importa:

**Transformaciones horizontales** (dentro del argumento):
1. Reflexión en eje Y
2. Estiramiento/compresión horizontal
3. Desplazamiento horizontal

**Transformaciones verticales** (fuera del argumento):
1. Estiramiento/compresión vertical
2. Reflexión en eje X
3. Desplazamiento vertical

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Describe la transformación:

a) $g(x) = -|x|$ partiendo de $f(x) = |x|$
b) $h(x) = \sqrt{-x}$ partiendo de $f(x) = \sqrt{x}$
c) $k(x) = -(-x)^3$ partiendo de $f(x) = x^3$

<details>
<summary>Ver soluciones</summary>

a) Reflexión respecto al eje X

b) Reflexión respecto al eje Y

c) $k(x) = -(-x^3) = x^3 = f(x)$. Es la misma función (porque $x^3$ es impar).
</details>

---

**Ejercicio 2:** Dada $f(x) = x^2 - 4$, escribe:

a) La función reflejada en el eje X
b) La función reflejada en el eje Y

<details>
<summary>Ver soluciones</summary>

a) $g(x) = -(x^2 - 4) = -x^2 + 4$

b) $h(x) = (-x)^2 - 4 = x^2 - 4$
   
   ¡Es igual! Porque $f$ es **par**.
</details>

---

**Ejercicio 3:** Dado el punto $(3, 5)$ en la gráfica de $f$, encuentra el punto correspondiente en:

a) $-f(x)$
b) $f(-x)$
c) $-f(-x)$

<details>
<summary>Ver soluciones</summary>

a) $(3, -5)$

b) $(-3, 5)$

c) $(-3, -5)$
</details>

# Rectas Paralelas y Perpendiculares

Dos rectas en el plano pueden tener relaciones especiales. Las **rectas paralelas** nunca se cruzan, mientras que las **rectas perpendiculares** se cruzan formando un ángulo de 90°. ¿Cómo identificamos estas relaciones usando las pendientes?

---

## 🎯 ¿Qué vas a aprender?

- La condición de paralelismo entre dos rectas
- La condición de perpendicularidad entre dos rectas
- Cómo aplicar estas condiciones para resolver problemas

---

## 📖 Lo Esencial de Paralelismo y Perpendicularidad

| Relación | Condición | En símbolos |
|----------|-----------|-------------|
| **Paralelas** | Pendientes iguales | $m_1 = m_2$ |
| **Perpendiculares** | Pendientes inversas y opuestas | $m_1 \cdot m_2 = -1$ |
| **Perpendiculares** (alternativa) | Una es inversa negativa de la otra | $m_2 = -\dfrac{1}{m_1}$ |

---

## 📖 Rectas Paralelas

> Dos rectas son **paralelas** si tienen la **misma pendiente**.

$$
\ell_1 \parallel \ell_2 \iff m_1 = m_2
$$

### ¿Por qué?

Si dos rectas tienen la misma pendiente, tienen la misma inclinación respecto al eje horizontal. Por lo tanto, "suben" o "bajan" al mismo ritmo y nunca se intersectan.

### ⚙️ Ejemplo 1: Verificar paralelismo

Determina si las rectas que pasan por $A(1, 2)$, $B(4, 8)$ y por $C(0, 1)$, $D(2, 5)$ son paralelas.

**Pendiente de la recta AB:**
$$
m_1 = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2
$$

**Pendiente de la recta CD:**
$$
m_2 = \frac{5 - 1}{2 - 0} = \frac{4}{2} = 2
$$

Como $m_1 = m_2 = 2$, las rectas **son paralelas**.

### ⚙️ Ejemplo 2: Encontrar pendiente de una paralela

Si una recta tiene ecuación $y = 3x + 5$, ¿cuál es la pendiente de cualquier recta paralela a ella?

**Análisis:** De la ecuación $y = 3x + 5$, la pendiente es $m = 3$.

Cualquier recta paralela debe tener la misma pendiente: $m = 3$.

---

## 📖 Rectas Perpendiculares

> Dos rectas son **perpendiculares** si el producto de sus pendientes es igual a $-1$.

$$
\ell_1 \perp \ell_2 \iff m_1 \cdot m_2 = -1
$$

O equivalentemente:

$$
m_2 = -\frac{1}{m_1}
$$

### ¿Por qué funciona esto?

Cuando dos rectas son perpendiculares, si una "sube" la otra "baja", pero con una proporción específica. Si la primera pendiente es $\frac{a}{b}$, la perpendicular tiene pendiente $-\frac{b}{a}$.

### ⚙️ Ejemplo 3: Verificar perpendicularidad

Verifica si las rectas con pendientes $m_1 = 3$ y $m_2 = -\frac{1}{3}$ son perpendiculares.

**Calculamos el producto:**
$$
m_1 \cdot m_2 = 3 \times \left(-\frac{1}{3}\right) = -1
$$

Como el producto es $-1$, las rectas **son perpendiculares**.

### ⚙️ Ejemplo 4: Encontrar pendiente perpendicular

Si una recta tiene pendiente $m = 4$, ¿cuál es la pendiente de una recta perpendicular?

$$
m_\perp = -\frac{1}{4}
$$

**Verificación:** $4 \times \left(-\frac{1}{4}\right) = -1$ ✓

### ⚙️ Ejemplo 5: Dados puntos

Las rectas pasan por $A(1, 3)$, $B(4, 6)$ y por $C(2, 0)$, $D(5, -3)$. ¿Son perpendiculares?

**Pendiente de AB:**
$$
m_1 = \frac{6 - 3}{4 - 1} = \frac{3}{3} = 1
$$

**Pendiente de CD:**
$$
m_2 = \frac{-3 - 0}{5 - 2} = \frac{-3}{3} = -1
$$

**Producto:**
$$
m_1 \cdot m_2 = 1 \times (-1) = -1
$$

Las rectas **son perpendiculares**.

---

## 📖 Casos Especiales

### Recta horizontal y vertical

- Una recta horizontal tiene $m = 0$
- Una recta vertical tiene $m$ indefinida

Estas dos rectas son **perpendiculares** entre sí, aunque no podemos verificarlo con la fórmula $m_1 \cdot m_2 = -1$ (porque una pendiente no existe).

### Rectas con la misma ecuación

Si dos rectas tienen exactamente la misma ecuación, son **la misma recta**, no solo paralelas.

---

## 📖 Tabla Resumen de Pendientes Perpendiculares

| Si $m_1 =$ | Entonces $m_\perp =$ |
|------------|---------------------|
| $2$ | $-\frac{1}{2}$ |
| $-3$ | $\frac{1}{3}$ |
| $\frac{2}{5}$ | $-\frac{5}{2}$ |
| $-\frac{3}{4}$ | $\frac{4}{3}$ |
| $1$ | $-1$ |
| $-1$ | $1$ |

> 💡 **Truco:** Para encontrar la pendiente perpendicular, invierte la fracción y cambia el signo.

---

## 🔑 Resumen

| Relación | Condición con pendientes |
|----------|-------------------------|
| Paralelas ($\parallel$) | $m_1 = m_2$ |
| Perpendiculares ($\perp$) | $m_1 \cdot m_2 = -1$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Determina si las rectas $y = 2x + 3$ y $y = 2x - 1$ son paralelas, perpendiculares o ninguna.

<details>
<summary>Ver solución</summary>

Ambas rectas tienen pendiente $m = 2$.

Como $m_1 = m_2$, las rectas son **paralelas**.

</details>

### Ejercicio 2
Determina si las rectas $y = 4x + 1$ y $y = -\frac{1}{4}x + 5$ son paralelas, perpendiculares o ninguna.

<details>
<summary>Ver solución</summary>

- $m_1 = 4$
- $m_2 = -\frac{1}{4}$

Producto: $m_1 \cdot m_2 = 4 \times \left(-\frac{1}{4}\right) = -1$

Las rectas son **perpendiculares**.

</details>

### Ejercicio 3
Encuentra la pendiente de una recta perpendicular a la que pasa por $A(2, 5)$ y $B(6, 1)$.

<details>
<summary>Ver solución</summary>

**Pendiente de AB:**
$$
m = \frac{1 - 5}{6 - 2} = \frac{-4}{4} = -1
$$

**Pendiente perpendicular:**
$$
m_\perp = -\frac{1}{-1} = 1
$$

**Respuesta:** $m_\perp = 1$

</details>

### Ejercicio 4
Si la recta $\ell_1$ pasa por $(0, 4)$ y $(3, 1)$, y la recta $\ell_2$ pasa por $(1, 2)$ y $(4, k)$. ¿Qué valor debe tener $k$ para que las rectas sean paralelas?

<details>
<summary>Ver solución</summary>

**Pendiente de $\ell_1$:**
$$
m_1 = \frac{1 - 4}{3 - 0} = \frac{-3}{3} = -1
$$

Para que sean paralelas, $m_2 = -1$:

$$
-1 = \frac{k - 2}{4 - 1} = \frac{k - 2}{3}
$$

$$
k - 2 = -3
$$

$$
k = -1
$$

**Respuesta:** $k = -1$

</details>

### Ejercicio 5
Dos rectas tienen pendientes $m_1 = a$ y $m_2 = a + 2$. Si las rectas son perpendiculares, encuentra el valor de $a$.

<details>
<summary>Ver solución</summary>

Para perpendiculares: $m_1 \cdot m_2 = -1$

$$
a(a + 2) = -1
$$

$$
a^2 + 2a + 1 = 0
$$

$$
(a + 1)^2 = 0
$$

$$
a = -1
$$

**Verificación:** $m_1 = -1$, $m_2 = -1 + 2 = 1$, producto = $-1$ ✓

**Respuesta:** $a = -1$

</details>

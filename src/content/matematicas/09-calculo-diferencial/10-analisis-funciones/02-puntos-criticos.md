# Puntos Críticos

Los puntos críticos son candidatos a extremos (máximos y mínimos). Son los puntos donde la función podría cambiar de comportamiento.

---

## 🎯 ¿Qué vas a aprender?

- Definición de punto crítico
- Cómo encontrar puntos críticos
- Clasificación de puntos críticos
- Puntos donde la derivada no existe

---

## 📖 Definición

Un **punto crítico** de $f$ es un valor $c$ en el dominio de $f$ donde:

$$
f'(c) = 0 \quad \text{o} \quad f'(c) \text{ no existe}
$$

---

## 📖 Importancia

Los puntos críticos son los únicos lugares donde pueden ocurrir **extremos relativos** (máximos o mínimos locales).

> **Teorema de Fermat:** Si $f$ tiene un extremo relativo en $c$ y $f$ es diferenciable en $c$, entonces $f'(c) = 0$.

---

## ⚙️ Ejemplo 1: Puntos donde $f' = 0$

$f(x) = x^3 - 3x^2 + 1$

$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$

$$f'(x) = 0 \Rightarrow x = 0 \text{ o } x = 2$$

**Puntos críticos:** $x = 0$ y $x = 2$

---

## ⚙️ Ejemplo 2: Derivada que no existe

$f(x) = |x|$

$$
f'(x) = \begin{cases} 1 & x > 0 \\ -1 & x < 0 \end{cases}
$$

$f'(0)$ no existe (límites laterales diferentes).

**Punto crítico:** $x = 0$

---

## ⚙️ Ejemplo 3: Raíz cúbica

$f(x) = x^{2/3}$

$$f'(x) = \frac{2}{3}x^{-1/3} = \frac{2}{3\sqrt[3]{x}}$$

$f'(0)$ no existe (división por cero).

**Punto crítico:** $x = 0$

---

## ⚙️ Ejemplo 4: Combinación

$f(x) = x^2 \sqrt[3]{x-1} = x^2(x-1)^{1/3}$

Usando regla del producto:
$$f'(x) = 2x(x-1)^{1/3} + x^2 \cdot \frac{1}{3}(x-1)^{-2/3}$$

$$= (x-1)^{-2/3}\left[2x(x-1) + \frac{x^2}{3}\right]$$

$$= \frac{6x(x-1) + x^2}{3(x-1)^{2/3}} = \frac{7x^2 - 6x}{3(x-1)^{2/3}}$$

**$f' = 0$:** $x(7x - 6) = 0 \Rightarrow x = 0, \frac{6}{7}$

**$f'$ no existe:** $x = 1$

**Puntos críticos:** $x = 0, \frac{6}{7}, 1$

---

## 📖 Clasificación de puntos críticos

No todo punto crítico es un extremo. Hay tres posibilidades:

| Tipo | Descripción |
|------|-------------|
| Máximo relativo | La función cambia de creciente a decreciente |
| Mínimo relativo | La función cambia de decreciente a creciente |
| No es extremo | La función no cambia de monotonía |

---

## ⚙️ Ejemplo 5: Punto crítico que no es extremo

$f(x) = x^3$

$$f'(x) = 3x^2 = 0 \Rightarrow x = 0$$

Pero $f'(x) \geq 0$ siempre, así que $f$ es creciente en todo su dominio.

$x = 0$ es punto crítico pero **no es extremo** (es un punto de inflexión).

---

## 📖 Proceso para encontrar puntos críticos

1. **Derivar** $f(x)$
2. **Resolver** $f'(x) = 0$
3. **Identificar** dónde $f'(x)$ no existe (pero $f(x)$ sí existe)
4. **Verificar** que cada valor esté en el dominio de $f$

---

## ⚙️ Ejemplo 6: Función racional

$f(x) = \frac{x^2}{x - 1}$

**Dominio:** $x \neq 1$

$$f'(x) = \frac{2x(x-1) - x^2}{(x-1)^2} = \frac{x^2 - 2x}{(x-1)^2} = \frac{x(x-2)}{(x-1)^2}$$

**$f' = 0$:** $x = 0, 2$

**$f'$ no existe en $x = 1$**, pero tampoco existe $f(1)$, así que $x = 1$ **no** es punto crítico.

**Puntos críticos:** $x = 0, 2$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra los puntos críticos:

a) $f(x) = x^4 - 4x^3$
b) $g(x) = \sqrt{x^2 - 4x}$

<details>
<summary>Ver soluciones</summary>

a) $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3) = 0$
   
   Puntos críticos: $x = 0, 3$

b) Dominio: $x \leq 0$ o $x \geq 4$
   
   $g'(x) = \frac{2x - 4}{2\sqrt{x^2-4x}} = \frac{x-2}{\sqrt{x^2-4x}}$
   
   $g' = 0$ cuando $x = 2$, pero $2 \notin$ dominio
   
   $g'$ no existe en $x = 0, 4$ (bordes del dominio)
   
   Puntos críticos: $x = 0, 4$
</details>

---

**Ejercicio 2:** Identifica todos los puntos críticos de $f(x) = |x^2 - 1|$.

<details>
<summary>Ver solución</summary>

$f(x) = |x^2 - 1| = \begin{cases} x^2 - 1 & |x| \geq 1 \\ 1 - x^2 & |x| < 1 \end{cases}$

$f'(x) = \begin{cases} 2x & |x| > 1 \\ -2x & |x| < 1 \end{cases}$

$f' = 0$: $x = 0$

$f'$ no existe: $x = \pm 1$ (cambio de fórmula)

Puntos críticos: $x = -1, 0, 1$
</details>

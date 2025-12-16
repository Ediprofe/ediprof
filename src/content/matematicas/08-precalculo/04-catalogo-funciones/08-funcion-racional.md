# Función Racional

Las funciones racionales son cocientes de polinomios. Introducen asíntotas, discontinuidades y comportamientos que serán fundamentales para el estudio de límites en cálculo.

---

## 🎯 ¿Qué vas a aprender?

- La forma general de una función racional
- Dominio y exclusiones
- Asíntotas verticales, horizontales y oblicuas
- Cómo graficar funciones racionales

---

## 📖 Definición

Una **función racional** es el cociente de dos polinomios:

$$
f(x) = \frac{P(x)}{Q(x)}
$$

donde $P(x)$ y $Q(x)$ son polinomios y $Q(x) \neq 0$.

### Ejemplos

- $f(x) = \frac{1}{x}$ (la más simple)
- $g(x) = \frac{x + 1}{x - 2}$
- $h(x) = \frac{x^2 - 4}{x^2 + 1}$

---

## 📖 Dominio

El dominio excluye los valores donde el denominador es cero.

**Pasos para encontrar el dominio:**
1. Igualar el denominador a cero
2. Resolver para $x$
3. Excluir esas raíces

### ⚙️ Ejemplo 1

Encuentra el dominio de $f(x) = \frac{3x + 1}{x^2 - 9}$

**Paso 1:** $x^2 - 9 = 0$

**Paso 2:** $x = \pm 3$

**Dominio:** $\mathbb{R} - \{-3, 3\}$ o $(-\infty, -3) \cup (-3, 3) \cup (3, +\infty)$

---

## 📖 La función $f(x) = \frac{1}{x}$

Esta es la función racional fundamental.

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R} - \{0\}$ |
| **Rango** | $\mathbb{R} - \{0\}$ |
| **Paridad** | Impar |
| **Asíntota vertical** | $x = 0$ |
| **Asíntota horizontal** | $y = 0$ |

### Comportamiento

- Cuando $x \to 0^+$: $f(x) \to +\infty$
- Cuando $x \to 0^-$: $f(x) \to -\infty$
- Cuando $x \to \pm\infty$: $f(x) \to 0$

---

## 📖 Asíntotas

### Asíntota vertical

Ocurre donde el **denominador es cero** (y el numerador no es cero).

$$x = a \text{ es asíntota vertical si } Q(a) = 0 \text{ y } P(a) \neq 0$$

### Asíntota horizontal

Depende de los grados de $P(x)$ y $Q(x)$:

| Grados | Asíntota horizontal |
|--------|---------------------|
| grado $P$ < grado $Q$ | $y = 0$ |
| grado $P$ = grado $Q$ | $y = \frac{\text{coef. principal de } P}{\text{coef. principal de } Q}$ |
| grado $P$ > grado $Q$ | No hay (puede haber asíntota oblicua) |

### Asíntota oblicua

Si grado $P$ = grado $Q$ + 1, hay una asíntota oblicua $y = mx + b$.

Se encuentra dividiendo $P(x) \div Q(x)$.

---

## ⚙️ Ejemplo 2: Análisis completo

Analiza $f(x) = \frac{2x + 1}{x - 3}$

**Dominio:** $x \neq 3$ → $\mathbb{R} - \{3\}$

**Asíntota vertical:** $x = 3$

**Asíntota horizontal:** Grados iguales (ambos 1)
$$y = \frac{2}{1} = 2$$

**Intercepto Y:** $f(0) = \frac{1}{-3} = -\frac{1}{3}$ → $(0, -\frac{1}{3})$

**Intercepto X:** $2x + 1 = 0 \Rightarrow x = -\frac{1}{2}$ → $(-\frac{1}{2}, 0)$

---

## ⚙️ Ejemplo 3: Sin asíntota horizontal

Analiza $g(x) = \frac{x^2 - 1}{x + 2}$

**Dominio:** $x \neq -2$

**Asíntota vertical:** $x = -2$

**Grados:** Numerador grado 2, denominador grado 1.
→ No hay asíntota horizontal.

**Asíntota oblicua:** Dividimos $\frac{x^2 - 1}{x + 2}$:

$$x^2 - 1 = (x + 2)(x - 2) + 3$$

Entonces: $g(x) = x - 2 + \frac{3}{x + 2}$

**Asíntota oblicua:** $y = x - 2$

---

## 📖 Huecos (discontinuidades removibles)

Si un factor se **cancela** entre numerador y denominador, hay un hueco en lugar de una asíntota.

### ⚙️ Ejemplo 4

$$h(x) = \frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x-2}$$

Si $x \neq 2$: $h(x) = x + 2$

En $x = 2$:
- La función no está definida
- Pero **no hay asíntota vertical**
- Hay un **hueco** en $(2, 4)$

---

## 📖 Pasos para graficar

1. **Dominio:** Encontrar restricciones
2. **Asíntotas verticales:** Denominador = 0
3. **Asíntota horizontal u oblicua:** Comparar grados
4. **Interceptos:** Con eje X (numerador = 0) y eje Y ($f(0)$)
5. **Signos:** Analizar en qué regiones es positiva/negativa
6. **Comportamiento cerca de asíntotas**

---

## ⚙️ Ejemplo 5: Graficar

Grafica $f(x) = \frac{x}{x^2 - 4} = \frac{x}{(x-2)(x+2)}$

**Dominio:** $x \neq \pm 2$

**Asíntotas verticales:** $x = -2$ y $x = 2$

**Asíntota horizontal:** Grado numerador (1) < grado denominador (2)
→ $y = 0$

**Interceptos:**
- Y: $f(0) = 0$ → $(0, 0)$
- X: $x = 0$ → $(0, 0)$

**Paridad:** Impar (simétrica respecto al origen)

---

## 📊 Resumen de asíntotas

| Tipo | Condición | Ecuación |
|------|-----------|----------|
| Vertical | $Q(a) = 0$, $P(a) \neq 0$ | $x = a$ |
| Horizontal | grado $P \leq$ grado $Q$ | $y = \frac{\text{coefs. principales o } 0}$ |
| Oblicua | grado $P$ = grado $Q$ + 1 | $y = mx + b$ (por división) |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra dominio y asíntotas:

a) $f(x) = \frac{5}{x + 4}$
b) $g(x) = \frac{3x - 2}{2x + 1}$
c) $h(x) = \frac{x^2 + 1}{x}$

<details>
<summary>Ver soluciones</summary>

a) Dominio: $\mathbb{R} - \{-4\}$
   
   AV: $x = -4$, AH: $y = 0$

b) Dominio: $\mathbb{R} - \{-\frac{1}{2}\}$
   
   AV: $x = -\frac{1}{2}$, AH: $y = \frac{3}{2}$

c) Dominio: $\mathbb{R} - \{0\}$
   
   AV: $x = 0$
   
   Asíntota oblicua: $h(x) = x + \frac{1}{x}$, entonces AO: $y = x$
</details>

---

**Ejercicio 2:** Simplifica y encuentra el hueco:

$$f(x) = \frac{x^2 - 9}{x - 3}$$

<details>
<summary>Ver solución</summary>

$$f(x) = \frac{(x-3)(x+3)}{x-3} = x + 3 \quad (x \neq 3)$$

Hueco en $x = 3$: el punto sería $(3, 6)$.
</details>

# Gráfica Completa de una Función

Combinar toda la información del cálculo diferencial nos permite trazar una gráfica precisa de cualquier función. Este proceso sistemático es la culminación del análisis de funciones.

---

## 🎯 ¿Qué vas a aprender?

- El método completo para graficar
- Qué información extraer
- Cómo organizar el análisis
- Un ejemplo paso a paso

---

## 📖 Elementos a analizar

| Elemento | Cómo encontrarlo |
|----------|------------------|
| **Dominio** | Restricciones de la expresión |
| **Interceptos** | $y$: $f(0)$; $x$: $f(x) = 0$ |
| **Simetría** | Par: $f(-x) = f(x)$; Impar: $f(-x) = -f(x)$ |
| **Asíntotas** | V: denominador = 0; H: límites en $\pm\infty$ |
| **Intervalos de crecimiento** | Signo de $f'$ |
| **Extremos** | Puntos críticos + criterios |
| **Concavidad** | Signo de $f''$ |
| **Puntos de inflexión** | Cambio de signo de $f''$ |

---

## 📖 Procedimiento sistemático

### Paso 1: Dominio y restricciones
### Paso 2: Interceptos con los ejes
### Paso 3: Simetría
### Paso 4: Comportamiento asintótico
### Paso 5: Primera derivada (crecimiento, extremos)
### Paso 6: Segunda derivada (concavidad, inflexiones)
### Paso 7: Tabla de valores adicionales si es necesario
### Paso 8: Trazar la gráfica

---

## ⚙️ Ejemplo completo

Grafica $f(x) = \frac{x^2}{x^2 - 1}$

---

### Paso 1: Dominio

$x^2 - 1 \neq 0 \Rightarrow x \neq \pm 1$

**Dominio:** $\mathbb{R} - \{-1, 1\}$

---

### Paso 2: Interceptos

**Intercepto Y:** $f(0) = 0$ → $(0, 0)$

**Intercepto X:** $\frac{x^2}{x^2-1} = 0 \Rightarrow x = 0$ → $(0, 0)$

---

### Paso 3: Simetría

$f(-x) = \frac{(-x)^2}{(-x)^2 - 1} = \frac{x^2}{x^2 - 1} = f(x)$

**Función par** (simétrica respecto al eje Y)

---

### Paso 4: Asíntotas

**Verticales:** $x = 1$ y $x = -1$

**Horizontal:** $\lim_{x \to \pm\infty} \frac{x^2}{x^2 - 1} = 1$ → $y = 1$

---

### Paso 5: Primera derivada

$$f'(x) = \frac{2x(x^2-1) - x^2(2x)}{(x^2-1)^2} = \frac{-2x}{(x^2-1)^2}$$

**Punto crítico:** $x = 0$

**Signo de $f'$:**
- $x < -1$: $f' > 0$ (creciente)
- $-1 < x < 0$: $f' > 0$ (creciente)
- $0 < x < 1$: $f' < 0$ (decreciente)
- $x > 1$: $f' < 0$ (decreciente)

**Máximo relativo** en $x = 0$: $f(0) = 0$

---

### Paso 6: Segunda derivada

$$f''(x) = \frac{d}{dx}\left[\frac{-2x}{(x^2-1)^2}\right]$$

Tras cálculos: $f''(x) = \frac{6x^2 + 2}{(x^2-1)^3}$

El numerador $6x^2 + 2 > 0$ siempre.

**Signo de $f''$:**
- $|x| < 1$: $(x^2-1)^3 < 0$ → $f'' < 0$ (cóncava abajo)
- $|x| > 1$: $(x^2-1)^3 > 0$ → $f'' > 0$ (cóncava arriba)

**No hay puntos de inflexión** (la concavidad cambia en las asíntotas).

---

### Paso 7: Tabla de valores

| $x$ | $f(x)$ |
|-----|--------|
| $-2$ | $\frac{4}{3}$ |
| $-0.5$ | $-\frac{1}{3}$ |
| $0$ | $0$ |
| $0.5$ | $-\frac{1}{3}$ |
| $2$ | $\frac{4}{3}$ |

---

### Paso 8: Características de la gráfica

- Pasa por el origen (máximo)
- Asíntotas verticales en $x = \pm 1$
- Asíntota horizontal $y = 1$
- Simétrica respecto al eje Y
- Cóncava abajo entre las asíntotas, arriba fuera

---

## 📊 Resumen del ejemplo

| Característica | Valor |
|----------------|-------|
| Dominio | $\mathbb{R} - \{-1, 1\}$ |
| Interceptos | $(0, 0)$ |
| Simetría | Par |
| A.V. | $x = -1$, $x = 1$ |
| A.H. | $y = 1$ |
| Máximo | $(0, 0)$ |
| Mínimo | Ninguno |
| Inflexiones | Ninguna |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Realiza el análisis completo de:

$$f(x) = \frac{x}{x^2 + 1}$$

<details>
<summary>Ver análisis</summary>

- **Dominio:** $\mathbb{R}$
- **Intercepto:** $(0, 0)$
- **Simetría:** Impar
- **A.H.:** $y = 0$
- **$f'(x) = \frac{1-x^2}{(x^2+1)^2}$**: críticos $x = \pm 1$
- Máximo: $(1, \frac{1}{2})$, Mínimo: $(-1, -\frac{1}{2})$
- Punto de inflexión: $(0, 0)$
</details>

---

**Ejercicio 2:** Grafica $f(x) = x^3 - 3x$.

<details>
<summary>Ver análisis</summary>

- **Dominio:** $\mathbb{R}$
- **Interceptos:** $(0,0)$, $(\pm\sqrt{3}, 0)$
- **Simetría:** Impar
- **$f'(x) = 3x^2 - 3$**: críticos $x = \pm 1$
- Máximo: $(-1, 2)$, Mínimo: $(1, -2)$
- **$f''(x) = 6x$**: inflexión en $(0, 0)$
</details>

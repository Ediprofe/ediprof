---
title: "Función Cúbica y Potencias"
---

# Función Cúbica y Potencias

Más allá de la parábola, las funciones de potencias superiores crean curvas fascinantes. Exploramos los patrones que emergen cuando $x$ se eleva a potencias mayores.

---

## 🎯 ¿Qué vas a aprender?

- La función cúbica y sus propiedades
- Funciones potencia $f(x) = x^n$
- Diferencias entre potencias pares e impares
- Comportamiento en los extremos

---

## 📖 La función cúbica básica

La función cúbica más simple es:

$$
f(x) = x^3
$$

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $\mathbb{R}$ |
| **Paridad** | Impar ($f(-x) = -f(x)$) |
| **Simetría** | Respecto al origen |
| **Inyectiva** | Sí |
| **Biyectiva** | Sí |
| **Punto de inflexión** | $(0, 0)$ |

### Forma de la gráfica

La gráfica tiene forma de "S" extendida:
- Crece lentamente cerca del origen
- Se acelera hacia los extremos
- Pasa por el origen
- Simétrica respecto al origen

---

## ⚙️ Ejemplo 1: Evaluar la función cúbica

$f(x) = x^3$

| $x$ | $f(x)$ |
|-----|--------|
| $-2$ | $-8$ |
| $-1$ | $-1$ |
| $0$ | $0$ |
| $1$ | $1$ |
| $2$ | $8$ |

---

## 📖 Función cúbica general

La forma general es:

$$
f(x) = ax^3 + bx^2 + cx + d \quad (a \neq 0)
$$

### Características

- Puede tener 1, 2 o 3 raíces reales
- Siempre tiene al menos una raíz real
- Puede tener 0, 1 o 2 puntos de inflexión
- El comportamiento final depende del signo de $a$

---

## ⚙️ Ejemplo 2: Analizar una cúbica

$f(x) = x^3 - 3x$

**Raíces:** $x^3 - 3x = 0 \Rightarrow x(x^2 - 3) = 0$

$x = 0$ o $x = \pm\sqrt{3}$

**Puntos críticos:** $f'(x) = 3x^2 - 3 = 0 \Rightarrow x = \pm 1$

- Máximo local en $x = -1$: $f(-1) = -1 + 3 = 2$
- Mínimo local en $x = 1$: $f(1) = 1 - 3 = -2$

---

## 📖 Funciones potencia $f(x) = x^n$

Las funciones potencia forman una familia importante.

### Potencias pares: $n = 2, 4, 6, \ldots$

$$f(x) = x^{2k}$$

| Propiedad | Valor |
|-----------|-------|
| Paridad | Par |
| Simetría | Eje Y |
| Rango | $[0, +\infty)$ |
| Mínimo | $0$ en $x = 0$ |

Mientras mayor sea $n$:
- Más plana cerca del origen
- Más empinada lejos del origen

### Potencias impares: $n = 1, 3, 5, \ldots$

$$f(x) = x^{2k+1}$$

| Propiedad | Valor |
|-----------|-------|
| Paridad | Impar |
| Simetría | Origen |
| Rango | $\mathbb{R}$ |
| Biyectiva | Sí |

---

## ⚙️ Ejemplo 3: Comparando potencias

Evaluamos en $x = 2$:

| Función | $f(2)$ |
|---------|--------|
| $x$ | $2$ |
| $x^2$ | $4$ |
| $x^3$ | $8$ |
| $x^4$ | $16$ |
| $x^5$ | $32$ |

Evaluamos en $x = 0.5$:

| Función | $f(0.5)$ |
|---------|----------|
| $x$ | $0.5$ |
| $x^2$ | $0.25$ |
| $x^3$ | $0.125$ |
| $x^4$ | $0.0625$ |
| $x^5$ | $0.03125$ |

Para $|x| > 1$: potencias mayores dan valores mayores.
Para $|x| < 1$: potencias mayores dan valores menores.

---

## 📖 Comportamiento asintótico

### Cuando $x \to +\infty$ o $x \to -\infty$

| Función | $x \to +\infty$ | $x \to -\infty$ |
|---------|-----------------|-----------------|
| $x^2$ | $+\infty$ | $+\infty$ |
| $x^3$ | $+\infty$ | $-\infty$ |
| $x^4$ | $+\infty$ | $+\infty$ |
| $x^5$ | $+\infty$ | $-\infty$ |

**Patrón:**
- Potencia **par**: mismo signo en ambos extremos
- Potencia **impar**: signos opuestos

---

## 📖 Funciones potencia con coeficiente

$$f(x) = ax^n$$

El coeficiente $a$ modifica:

| Si $a > 0$ | Si $a < 0$ |
|------------|------------|
| Conserva orientación | Refleja verticalmente |
| $|a| > 1$: estira | $|a| > 1$: estira (pero invertida) |
| $|a| < 1$: comprime | $|a| < 1$: comprime (pero invertida) |

---

## ⚙️ Ejemplo 4: Transformaciones

Compara:
- $f(x) = x^3$
- $g(x) = 2x^3$ (estirada)
- $h(x) = -x^3$ (reflejada)
- $k(x) = \frac{1}{2}x^3$ (comprimida)

En $x = 2$:
- $f(2) = 8$
- $g(2) = 16$
- $h(2) = -8$
- $k(2) = 4$

---

## 📊 Resumen comparativo

| Característica | Potencia par $(x^{2n})$ | Potencia impar $(x^{2n+1})$ |
|----------------|------------------------|----------------------------|
| Simetría | Eje Y | Origen |
| Rango | $[0, +\infty)$ | $\mathbb{R}$ |
| Inyectiva | No | Sí |
| Comportamiento en $\pm\infty$ | Igual signo | Signos opuestos |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Determina paridad, rango y comportamiento en infinito:

a) $f(x) = x^6$
b) $g(x) = -x^5$
c) $h(x) = 3x^4$

<details>
<summary>Ver soluciones</summary>

a) Par, rango $[0, +\infty)$, $\lim_{x \to \pm\infty} f(x) = +\infty$

b) Impar, rango $\mathbb{R}$, $\lim_{x \to +\infty} = -\infty$, $\lim_{x \to -\infty} = +\infty$

c) Par, rango $[0, +\infty)$, $\lim_{x \to \pm\infty} f(x) = +\infty$
</details>

---

**Ejercicio 2:** Ordena de menor a mayor cuando $x = 3$:

$x$, $x^2$, $x^3$, $\sqrt{x}$

<details>
<summary>Ver solución</summary>

- $\sqrt{3} \approx 1.73$
- $3 = 3$
- $3^2 = 9$
- $3^3 = 27$

**Orden:** $\sqrt{x} < x < x^2 < x^3$
</details>

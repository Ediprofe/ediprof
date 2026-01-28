---
title: "Función Cuadrática"
---

# Función Cuadrática

La parábola es una de las curvas más importantes en matemáticas. Describe el lanzamiento de proyectiles, forma puentes colgantes y aparece en innumerables aplicaciones.

---

## 🎯 ¿Qué vas a aprender?

- La forma estándar y la forma canónica
- Vértice, eje de simetría y orientación
- Intersecciones con los ejes
- Cómo graficar una parábola

---

## 📖 Forma general

La **función cuadrática** tiene la forma:

$$
f(x) = ax^2 + bx + c \quad \text{donde } a \neq 0
$$

### El coeficiente $a$ determina:

| Valor de $a$ | Efecto |
|--------------|--------|
| $a > 0$ | Parábola abre hacia **arriba** (tiene mínimo) |
| $a < 0$ | Parábola abre hacia **abajo** (tiene máximo) |
| $\|a\| > 1$ | Parábola más angosta |
| $\|a\| < 1$ | Parábola más ancha |

---

## 📖 Forma canónica (vértice)

La forma canónica permite identificar directamente el vértice:

$$
f(x) = a(x - h)^2 + k
$$

donde $(h, k)$ es el **vértice** de la parábola.

### Conversión de forma general a canónica

El vértice se calcula con:

$$
h = -\frac{b}{2a} \quad \text{y} \quad k = f(h) = c - \frac{b^2}{4a}
$$

---

## ⚙️ Ejemplo 1: Elementos de la parábola

Analiza $f(x) = 2x^2 - 8x + 6$

**Coeficientes:** $a = 2$, $b = -8$, $c = 6$

**Orientación:** $a = 2 > 0$ → abre hacia arriba

**Vértice:**
$$h = -\frac{-8}{2(2)} = \frac{8}{4} = 2$$
$$k = f(2) = 2(2)^2 - 8(2) + 6 = 8 - 16 + 6 = -2$$

**Vértice:** $(2, -2)$

**Eje de simetría:** $x = 2$

**Forma canónica:** $f(x) = 2(x - 2)^2 - 2$

---

## 📖 Intersecciones

### Con el eje Y

Se obtiene cuando $x = 0$:
$$f(0) = c$$

La intersección es el punto $(0, c)$.

### Con el eje X (raíces)

Se obtienen resolviendo $f(x) = 0$:
$$ax^2 + bx + c = 0$$

Usando la fórmula general:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

El **discriminante** $\Delta = b^2 - 4ac$ determina el número de raíces:

| Discriminante | Raíces reales | Intersecciones con eje X |
|---------------|---------------|--------------------------|
| $\Delta > 0$ | 2 distintas | 2 puntos |
| $\Delta = 0$ | 1 doble | 1 punto (vértice toca el eje) |
| $\Delta < 0$ | Ninguna | Ninguna |

---

## ⚙️ Ejemplo 2: Encontrar intersecciones

Para $f(x) = x^2 - 5x + 6$:

**Eje Y:** $f(0) = 6$ → punto $(0, 6)$

**Eje X:** Resolvemos $x^2 - 5x + 6 = 0$

Factorizamos: $(x - 2)(x - 3) = 0$

Raíces: $x = 2$ y $x = 3$

**Intersecciones con eje X:** $(2, 0)$ y $(3, 0)$

---

## ⚙️ Ejemplo 3: Completar el cuadrado

Escribe $f(x) = x^2 + 6x + 5$ en forma canónica.

**Paso 1:** Agrupamos y completamos el cuadrado
$$f(x) = (x^2 + 6x) + 5$$

Para completar: $\left(\frac{6}{2}\right)^2 = 9$

$$f(x) = (x^2 + 6x + 9) - 9 + 5$$
$$f(x) = (x + 3)^2 - 4$$

**Forma canónica:** $f(x) = (x + 3)^2 - 4$

**Vértice:** $(-3, -4)$

---

## 📖 Propiedades de la función cuadrática

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $[k, +\infty)$ si $a > 0$; $(-\infty, k]$ si $a < 0$ |
| **Paridad** | Par solo si $b = 0$ (eje de simetría en $x = 0$) |
| **Inyectiva** | No (a menos que se restrinja el dominio) |
| **Monotonía** | Decrece antes del vértice, crece después (si $a > 0$) |

---

## ⚙️ Ejemplo 4: Problema de optimización

Un comerciante vende $x$ artículos a un precio de $(50 - x)$ pesos cada uno. ¿Cuántos artículos debe vender para maximizar sus ingresos?

**Ingreso:** $I(x) = x(50 - x) = 50x - x^2 = -x^2 + 50x$

**Análisis:** $a = -1 < 0$ → parábola abre hacia abajo → tiene máximo

**Vértice:**
$$h = -\frac{50}{2(-1)} = 25$$

**Respuesta:** Debe vender 25 artículos.

**Ingreso máximo:** $I(25) = 25(50 - 25) = 25(25) = 625$ pesos.

---

## 📊 Pasos para graficar

1. Determinar orientación (signo de $a$)
2. Calcular el vértice $(h, k)$
3. Trazar el eje de simetría $x = h$
4. Encontrar intersección con eje Y: $(0, c)$
5. Encontrar intersecciones con eje X (si existen)
6. Usar simetría para encontrar puntos adicionales

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Para $f(x) = -x^2 + 4x - 3$, encuentra:

a) Orientación
b) Vértice
c) Intersecciones con los ejes

<details>
<summary>Ver soluciones</summary>

a) $a = -1 < 0$ → abre hacia **abajo**

b) $h = -\frac{4}{2(-1)} = 2$
   
   $k = f(2) = -(2)^2 + 4(2) - 3 = -4 + 8 - 3 = 1$
   
   **Vértice:** $(2, 1)$

c) **Eje Y:** $f(0) = -3$ → $(0, -3)$
   
   **Eje X:** $-x^2 + 4x - 3 = 0$ → $x^2 - 4x + 3 = 0$
   
   $(x-1)(x-3) = 0$ → $x = 1, 3$
   
   **Intersecciones:** $(1, 0)$ y $(3, 0)$
</details>

---

**Ejercicio 2:** Escribe en forma canónica:

a) $f(x) = x^2 - 4x + 7$
b) $g(x) = 2x^2 + 12x + 10$

<details>
<summary>Ver soluciones</summary>

a) $f(x) = (x^2 - 4x + 4) - 4 + 7 = (x - 2)^2 + 3$

b) $g(x) = 2(x^2 + 6x) + 10 = 2(x^2 + 6x + 9) - 18 + 10 = 2(x + 3)^2 - 8$
</details>

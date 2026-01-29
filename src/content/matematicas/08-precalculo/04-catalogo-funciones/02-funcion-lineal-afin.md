# Función Lineal y Afín

Las funciones lineales modelan relaciones proporcionales directas. Son la base para entender rectas, pendientes y tasas de cambio constantes.

---

## 🎯 ¿Qué vas a aprender?

- La diferencia entre función lineal y afín
- Pendiente e intercepto
- Formas de la ecuación de la recta
- Aplicaciones prácticas

---

## 📖 Función lineal

Una **función lineal** tiene la forma:

$$
f(x) = mx
$$

donde $m$ es la **pendiente**.

### Características

- Pasa por el origen $(0, 0)$
- La pendiente $m$ indica cuánto cambia $y$ por cada unidad de cambio en $x$
- Es una proporción directa: $y$ es proporcional a $x$

---

## 📖 Función afín

Una **función afín** tiene la forma:

$$
f(x) = mx + b
$$

donde:
- $m$ = **pendiente** (razón de cambio)
- $b$ = **ordenada al origen** (intercepto en Y)

### Nota terminológica

En muchos contextos, "función lineal" se usa informalmente para referirse también a la función afín. En rigor matemático:
- **Lineal:** $f(x) = mx$ (pasa por el origen)
- **Afín:** $f(x) = mx + b$ (puede no pasar por el origen)

---

## 📖 Interpretación de la pendiente

La pendiente $m$ se calcula como:

$$
m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\text{cambio vertical}}{\text{cambio horizontal}}
$$

| Valor de $m$ | Comportamiento de la recta |
|--------------|---------------------------|
| $m > 0$ | Creciente (sube hacia la derecha) |
| $m < 0$ | Decreciente (baja hacia la derecha) |
| $m = 0$ | Horizontal (función constante) |
| $m$ grande | Recta muy empinada |
| $m$ cercana a 0 | Recta casi horizontal |

---

## ⚙️ Ejemplo 1: Identificar pendiente e intercepto

Para $f(x) = -3x + 7$:

- Pendiente: $m = -3$ (la función es decreciente)
- Intercepto Y: $b = 7$ (cruza el eje Y en $(0, 7)$)

**Intercepto X:** Hacemos $f(x) = 0$:
$$-3x + 7 = 0 \Rightarrow x = \frac{7}{3}$$

Cruza el eje X en $\left(\frac{7}{3}, 0\right)$.

---

## ⚙️ Ejemplo 2: Graficar una función afín

Grafica $f(x) = 2x - 4$

**Método: dos puntos**

1. Intercepto Y: Cuando $x = 0$: $f(0) = -4$ → punto $(0, -4)$
2. Intercepto X: Cuando $f(x) = 0$: $2x - 4 = 0 \Rightarrow x = 2$ → punto $(2, 0)$

Conectamos los puntos con una línea recta.

**Pendiente:** $m = 2$ (por cada unidad que $x$ avanza, $y$ sube 2)

---

## ⚙️ Ejemplo 3: Encontrar la ecuación

Encuentra la ecuación de la recta que pasa por $(1, 5)$ y $(3, 11)$.

**Paso 1:** Calculamos la pendiente
$$m = \frac{11 - 5}{3 - 1} = \frac{6}{2} = 3$$

**Paso 2:** Usamos forma punto-pendiente
$$y - y_1 = m(x - x_1)$$
$$y - 5 = 3(x - 1)$$
$$y = 3x - 3 + 5$$
$$y = 3x + 2$$

**Ecuación:** $f(x) = 3x + 2$

---

## 📖 Formas de la ecuación lineal

| Forma | Ecuación | Información directa |
|-------|----------|---------------------|
| **Pendiente-intercepto** | $y = mx + b$ | Pendiente $m$, intercepto $b$ |
| **Punto-pendiente** | $y - y_1 = m(x - x_1)$ | Pendiente y un punto |
| **General** | $Ax + By + C = 0$ | Coeficientes |
| **Simétrica** | $\frac{x}{a} + \frac{y}{b} = 1$ | Interceptos $(a, 0)$ y $(0, b)$ |

---

## 📖 Propiedades de funciones afines

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $\mathbb{R}$ (si $m \neq 0$) |
| **Paridad** | Impar solo si $b = 0$ |
| **Inyectiva** | Sí (si $m \neq 0$) |
| **Tasa de cambio** | Constante (igual a $m$) |

---

## ⚙️ Ejemplo 4: Aplicación práctica

Un taxi cobra \$15 de banderazo más \$3 por kilómetro recorrido.

**a) Escribe la función del costo total:**
$$C(x) = 3x + 15$$

donde $x$ = kilómetros recorridos.

**b) ¿Cuánto cuesta un viaje de 8 km?**
$$C(8) = 3(8) + 15 = 24 + 15 = \$39$$

**c) Si el cliente paga \$45, ¿cuántos km recorrió?**
$$45 = 3x + 15$$
$$30 = 3x$$
$$x = 10 \text{ km}$$

---

## ⚙️ Ejemplo 5: Rectas paralelas y perpendiculares

**Paralelas:** Tienen la misma pendiente.
- $f(x) = 2x + 3$ y $g(x) = 2x - 1$ son paralelas.

**Perpendiculares:** Sus pendientes son recíprocos negativos ($m_1 \cdot m_2 = -1$).
- $f(x) = 3x + 1$ tiene pendiente $3$.
- Una recta perpendicular tiene pendiente $-\frac{1}{3}$.

---

## 📊 Resumen gráfico

| Tipo | Ejemplo | Gráfica |
|------|---------|---------|
| Creciente | $y = 2x + 1$ | Sube de izq. a der. |
| Decreciente | $y = -x + 4$ | Baja de izq. a der. |
| Horizontal | $y = 3$ | Línea horizontal |
| Vertical | $x = 2$ | No es función |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica la pendiente y el intercepto Y:

a) $f(x) = 5x - 2$
b) $g(x) = -\frac{1}{2}x + 4$
c) $h(x) = 7$

<details>
<summary>Ver soluciones</summary>

a) $m = 5$, $b = -2$

b) $m = -\frac{1}{2}$, $b = 4$

c) $m = 0$, $b = 7$ (función constante)
</details>

---

**Ejercicio 2:** Encuentra la ecuación de la recta que:

a) Pasa por $(2, 3)$ con pendiente $4$
b) Pasa por $(-1, 5)$ y $(3, -3)$

<details>
<summary>Ver soluciones</summary>

a) $y - 3 = 4(x - 2) \Rightarrow y = 4x - 5$

b) $m = \frac{-3 - 5}{3 - (-1)} = \frac{-8}{4} = -2$
   
   $y - 5 = -2(x + 1) \Rightarrow y = -2x + 3$
</details>

---

**Ejercicio 3:** ¿Son paralelas, perpendiculares, o ninguna?

a) $y = 3x + 1$ y $y = 3x - 4$
b) $y = 2x + 5$ y $y = -\frac{1}{2}x + 1$

<details>
<summary>Ver soluciones</summary>

a) **Paralelas** (misma pendiente: $m = 3$)

b) **Perpendiculares** ($2 \times (-\frac{1}{2}) = -1$)
</details>

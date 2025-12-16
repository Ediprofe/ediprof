# Derivación Implícita

No todas las funciones pueden escribirse explícitamente como $y = f(x)$. La derivación implícita nos permite encontrar $\frac{dy}{dx}$ cuando $y$ está definida implícitamente por una ecuación.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una función implícita
- Cómo derivar implícitamente
- Encontrar tangentes a curvas implícitas
- Derivadas de orden superior implícitas

---

## 📖 Funciones explícitas vs. implícitas

**Explícita:** $y = f(x)$ → $y$ aislada
- Ejemplo: $y = x^2 + 3x$

**Implícita:** $F(x, y) = 0$ → $y$ no aislada (o difícil de aislar)
- Ejemplo: $x^2 + y^2 = 25$ (círculo)
- Ejemplo: $x^3 + y^3 = 6xy$ (curva de Descartes)

---

## 📖 El método de derivación implícita

**Pasos:**
1. Derivar ambos lados respecto a $x$
2. Recordar que $\frac{d}{dx}[y] = \frac{dy}{dx} = y'$ (regla de la cadena)
3. Despejar $\frac{dy}{dx}$

---

## ⚙️ Ejemplo 1: Círculo

Encuentra $\frac{dy}{dx}$ para $x^2 + y^2 = 25$

**Derivamos ambos lados:**
$$\frac{d}{dx}[x^2] + \frac{d}{dx}[y^2] = \frac{d}{dx}[25]$$

$$2x + 2y \cdot \frac{dy}{dx} = 0$$

**Despejamos:**

$$
\frac{dy}{dx} = -\frac{2x}{2y} = -\frac{x}{y}
$$

---

## ⚙️ Ejemplo 2: Verificación

Para el mismo círculo, en el punto $(3, 4)$:

$$\frac{dy}{dx} = -\frac{3}{4}$$

La tangente tiene pendiente $-\frac{3}{4}$ y pasa por $(3, 4)$:

$$y - 4 = -\frac{3}{4}(x - 3)$$

$$y = -\frac{3}{4}x + \frac{25}{4}$$

---

## ⚙️ Ejemplo 3: Con productos

Encuentra $\frac{dy}{dx}$ para $xy = 1$

**Derivamos usando regla del producto:**
$$\frac{d}{dx}[xy] = \frac{d}{dx}[1]$$

$$
1 \cdot y + x \cdot \frac{dy}{dx} = 0
$$

$$
\frac{dy}{dx} = -\frac{y}{x}
$$

---

## ⚙️ Ejemplo 4: Expresión más compleja

Encuentra $\frac{dy}{dx}$ para $x^3 + y^3 = 6xy$

**Derivamos:**
$$3x^2 + 3y^2 \cdot y' = 6y + 6x \cdot y'$$

$$3y^2 y' - 6x y' = 6y - 3x^2$$

$$y'(3y^2 - 6x) = 6y - 3x^2$$

$$y' = \frac{6y - 3x^2}{3y^2 - 6x} = \frac{2y - x^2}{y^2 - 2x}$$

---

## ⚙️ Ejemplo 5: Con funciones trigonométricas

Encuentra $\frac{dy}{dx}$ para $\sin(xy) = x$

**Derivamos:**
$$\cos(xy) \cdot (1 \cdot y + x \cdot y') = 1$$

$$y\cos(xy) + xy'\cos(xy) = 1$$

$$y' = \frac{1 - y\cos(xy)}{x\cos(xy)}$$

---

## 📖 Segunda derivada implícita

Para encontrar $\frac{d^2y}{dx^2}$:
1. Deriva $\frac{dy}{dx}$ respecto a $x$
2. Sustituye $\frac{dy}{dx}$ por su expresión cuando aparezca

---

## ⚙️ Ejemplo 6: Segunda derivada

Para $x^2 + y^2 = 25$, sabemos que $y' = -\frac{x}{y}$

$$y'' = \frac{d}{dx}\left[-\frac{x}{y}\right]$$

$$= -\frac{1 \cdot y - x \cdot y'}{y^2}$$

$$= -\frac{y - x(-\frac{x}{y})}{y^2} = -\frac{y + \frac{x^2}{y}}{y^2}$$

$$= -\frac{\frac{y^2 + x^2}{y}}{y^2} = -\frac{y^2 + x^2}{y^3}$$

Como $x^2 + y^2 = 25$:

$$y'' = -\frac{25}{y^3}$$

---

## 📊 Resumen del método

| Expresión | Derivada respecto a $x$ |
|-----------|------------------------|
| $y$ | $y'$ |
| $y^n$ | $ny^{n-1} \cdot y'$ |
| $\sin y$ | $\cos y \cdot y'$ |
| $e^y$ | $e^y \cdot y'$ |
| $xy$ | $y + xy'$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra $\frac{dy}{dx}$:

a) $x^2 - y^2 = 16$ (hipérbola)
b) $x^2 + xy + y^2 = 7$

<details>
<summary>Ver soluciones</summary>

a) $2x - 2yy' = 0 \Rightarrow y' = \frac{x}{y}$

b) $2x + y + xy' + 2yy' = 0$
   
   $y'(x + 2y) = -2x - y$
   
   $y' = \frac{-2x - y}{x + 2y}$
</details>

---

**Ejercicio 2:** Encuentra la tangente a $x^2 + y^2 = 25$ en el punto $(4, 3)$.

<details>
<summary>Ver solución</summary>

$y' = -\frac{x}{y} = -\frac{4}{3}$

Tangente: $y - 3 = -\frac{4}{3}(x - 4)$

$y = -\frac{4}{3}x + \frac{25}{3}$
</details>

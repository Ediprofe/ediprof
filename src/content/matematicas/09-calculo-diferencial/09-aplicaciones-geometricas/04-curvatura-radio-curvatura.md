# Curvatura y Radio de Curvatura

La curvatura mide qué tan rápido cambia la dirección de una curva. Un círculo pequeño tiene alta curvatura; una recta tiene curvatura cero.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de curvatura
- Fórmulas para calcular la curvatura
- Radio de curvatura y círculo osculador
- Aplicaciones en física e ingeniería

---

## 📖 Concepto intuitivo

La **curvatura** $\kappa$ mide la tasa de cambio de la dirección de la tangente respecto a la longitud de arco.

- **Recta:** $\kappa = 0$ (no cambia de dirección)
- **Círculo de radio $r$:** $\kappa = \frac{1}{r}$ (constante)
- **Curva general:** $\kappa$ varía punto a punto

---

## 📖 Fórmula de curvatura

Para $y = f(x)$:

$$\boxed{\kappa = \frac{|y''|}{(1 + (y')^2)^{3/2}}}$$

---

## 📖 Radio de curvatura

El **radio de curvatura** es el recíproco de la curvatura:

$$R = \frac{1}{\kappa} = \frac{(1 + (y')^2)^{3/2}}{|y''|}$$

Es el radio del círculo que mejor aproxima la curva en ese punto.

---

## ⚙️ Ejemplo 1: Curvatura de un círculo

Para $y = \sqrt{r^2 - x^2}$ (semicírculo superior):

**Primera derivada:**
$$y' = \frac{-x}{\sqrt{r^2 - x^2}}$$

**Segunda derivada:**
$$y'' = \frac{-r^2}{(r^2 - x^2)^{3/2}}$$

**Curvatura:**
$$\kappa = \frac{\frac{r^2}{(r^2 - x^2)^{3/2}}}{\left(1 + \frac{x^2}{r^2 - x^2}\right)^{3/2}}$$

Simplificando: $\kappa = \frac{1}{r}$ (constante, como esperamos)

---

## ⚙️ Ejemplo 2: Parábola

Para $y = x^2$:

$$y' = 2x, \quad y'' = 2$$

$$\kappa = \frac{|2|}{(1 + 4x^2)^{3/2}} = \frac{2}{(1 + 4x^2)^{3/2}}$$

**En el vértice ($x = 0$):**
$$\kappa = \frac{2}{1} = 2$$
$$R = \frac{1}{2}$$

La curvatura es máxima en el vértice.

---

## ⚙️ Ejemplo 3: Función cúbica

Para $y = x^3$ en $x = 0$:

$$y' = 3x^2 \Rightarrow y'(0) = 0$$
$$y'' = 6x \Rightarrow y''(0) = 0$$

$$\kappa = \frac{0}{1} = 0$$

La curvatura es cero en el punto de inflexión.

---

## 📖 Círculo osculador

El **círculo osculador** (o círculo de curvatura) es el círculo que:
1. Pasa por el punto
2. Tiene la misma tangente que la curva
3. Tiene la misma curvatura que la curva

Su centro está en la dirección normal a distancia $R$ del punto.

---

## 📖 Centro de curvatura

El centro del círculo osculador está en:

$$\left(x - \frac{y'(1 + (y')^2)}{y''}, y + \frac{1 + (y')^2}{y''}\right)$$

---

## ⚙️ Ejemplo 4: Centro de curvatura

Para $y = x^2$ en $x = 1$ (punto $(1, 1)$):

$$y' = 2, \quad y'' = 2$$

$$x_c = 1 - \frac{2(1 + 4)}{2} = 1 - 5 = -4$$

$$y_c = 1 + \frac{1 + 4}{2} = 1 + \frac{5}{2} = \frac{7}{2}$$

Centro: $(-4, 3.5)$

Radio: $R = \frac{(1 + 4)^{3/2}}{2} = \frac{5\sqrt{5}}{2} \approx 5.59$

---

## 📖 Curvatura para paramétricas

Si $x = x(t)$, $y = y(t)$:

$$\kappa = \frac{|x'y'' - y'x''|}{(x'^2 + y'^2)^{3/2}}$$

---

## ⚙️ Ejemplo 5: Elipse

Para $x = a\cos t$, $y = b\sin t$:

$$x' = -a\sin t, \quad y' = b\cos t$$
$$x'' = -a\cos t, \quad y'' = -b\sin t$$

$$\kappa = \frac{|(-a\sin t)(-b\sin t) - (b\cos t)(-a\cos t)|}{(a^2\sin^2 t + b^2\cos^2 t)^{3/2}}$$

$$= \frac{ab\sin^2 t + ab\cos^2 t}{(a^2\sin^2 t + b^2\cos^2 t)^{3/2}}$$

$$= \frac{ab}{(a^2\sin^2 t + b^2\cos^2 t)^{3/2}}$$

---

## 📊 Resumen

| Cantidad | Fórmula |
|----------|---------|
| Curvatura $\kappa$ | $\frac{\|y''\|}{(1 + y'^2)^{3/2}}$ |
| Radio de curvatura $R$ | $\frac{1}{\kappa}$ |
| Curvatura del círculo | $\frac{1}{r}$ |
| Curvatura de la recta | $0$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula la curvatura de $y = e^x$ en $x = 0$.

<details>
<summary>Ver solución</summary>

$y' = e^0 = 1$, $y'' = e^0 = 1$

$\kappa = \frac{1}{(1 + 1)^{3/2}} = \frac{1}{2\sqrt{2}} = \frac{\sqrt{2}}{4}$
</details>

---

**Ejercicio 2:** Encuentra el radio de curvatura de $y = \sin x$ en $x = 0$.

<details>
<summary>Ver solución</summary>

$y'(0) = \cos 0 = 1$, $y''(0) = -\sin 0 = 0$

$\kappa = \frac{0}{(1 + 1)^{3/2}} = 0$

$R = \frac{1}{0} = \infty$ (la curva es casi recta ahí)
</details>

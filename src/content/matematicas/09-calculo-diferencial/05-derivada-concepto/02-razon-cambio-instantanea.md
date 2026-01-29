# Razón de Cambio Instantánea

¿Qué tan rápido está cambiando una función en un instante preciso? La razón de cambio instantánea responde esta pregunta tomando el límite cuando el intervalo se hace infinitesimalmente pequeño.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de cambio instantáneo
- Cómo pasar de promedio a instantáneo
- Interpretación física como velocidad instantánea
- Preparación para la definición de derivada

---

## 📖 Del promedio al instante

La razón de cambio promedio en $[a, a+h]$:

$$
\text{RCP} = \frac{f(a + h) - f(a)}{h}
$$

La **razón de cambio instantánea** en $x = a$ se obtiene cuando $h \to 0$:

$$
\text{RCI en } x = a = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
$$

---

## 📖 Interpretación física

### Velocidad instantánea

Si $s(t)$ es la posición en el tiempo $t$:

$$
v(t) = \lim_{h \to 0} \frac{s(t + h) - s(t)}{h}
$$

Es la velocidad en el instante exacto $t$.

### Analogía del velocímetro

- La velocidad **promedio** es la distancia total / tiempo total
- La velocidad **instantánea** es lo que marca el velocímetro en cada momento

---

## ⚙️ Ejemplo 1: Velocidad instantánea

La posición de un objeto está dada por $s(t) = t^2$ metros.

¿Cuál es la velocidad en $t = 3$ segundos?

$$v(3) = \lim_{h \to 0} \frac{s(3 + h) - s(3)}{h}$$

$$= \lim_{h \to 0} \frac{(3 + h)^2 - 9}{h}$$

$$= \lim_{h \to 0} \frac{9 + 6h + h^2 - 9}{h}$$

$$= \lim_{h \to 0} \frac{6h + h^2}{h}$$

$$= \lim_{h \to 0} (6 + h) = 6 \text{ m/s}$$

---

## ⚙️ Ejemplo 2: En cualquier punto

Para $s(t) = t^2$, encuentra la velocidad instantánea en cualquier tiempo $t$.

$$v(t) = \lim_{h \to 0} \frac{(t + h)^2 - t^2}{h}$$

$$= \lim_{h \to 0} \frac{t^2 + 2th + h^2 - t^2}{h}$$

$$= \lim_{h \to 0} \frac{2th + h^2}{h}$$

$$= \lim_{h \to 0} (2t + h) = 2t$$

**Resultado:** $v(t) = 2t$ m/s

Verificación: en $t = 3$, $v(3) = 6$ m/s ✓

---

## 📖 Interpretación geométrica

La razón de cambio instantánea es la **pendiente de la recta tangente** a la curva en el punto.

$$
m_{\text{tangente}} = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
$$

A medida que $h \to 0$:
- La recta **secante** se aproxima a la recta **tangente**
- La pendiente de la secante se aproxima a la pendiente de la tangente

---

## ⚙️ Ejemplo 3: Pendiente de tangente

Encuentra la pendiente de la tangente a $f(x) = x^3$ en $x = 2$.

$$m = \lim_{h \to 0} \frac{f(2 + h) - f(2)}{h}$$

$$= \lim_{h \to 0} \frac{(2 + h)^3 - 8}{h}$$

Expandimos $(2 + h)^3 = 8 + 12h + 6h^2 + h^3$:

$$= \lim_{h \to 0} \frac{8 + 12h + 6h^2 + h^3 - 8}{h}$$

$$= \lim_{h \to 0} \frac{12h + 6h^2 + h^3}{h}$$

$$= \lim_{h \to 0} (12 + 6h + h^2) = 12$$

La tangente en $x = 2$ tiene pendiente 12.

---

## ⚙️ Ejemplo 4: Con raíz cuadrada

Encuentra la RCI de $f(x) = \sqrt{x}$ en $x = 4$.

$$\lim_{h \to 0} \frac{\sqrt{4 + h} - \sqrt{4}}{h} = \lim_{h \to 0} \frac{\sqrt{4 + h} - 2}{h}$$

Racionalizamos:

$$= \lim_{h \to 0} \frac{(\sqrt{4 + h} - 2)(\sqrt{4 + h} + 2)}{h(\sqrt{4 + h} + 2)}$$

$$= \lim_{h \to 0} \frac{(4 + h) - 4}{h(\sqrt{4 + h} + 2)}$$

$$= \lim_{h \to 0} \frac{h}{h(\sqrt{4 + h} + 2)}$$

$$= \lim_{h \to 0} \frac{1}{\sqrt{4 + h} + 2} = \frac{1}{2 + 2} = \frac{1}{4}$$

---

## 📖 Notación alternativa

También se escribe con $\Delta x$ en lugar de $h$:

$$\lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$$

O usando otro punto $x$ que se acerca a $a$:

$$\lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

Todas son equivalentes.

---

## 📊 Comparación

| Concepto | Fórmula | Geometría |
|----------|---------|-----------|
| RCP (promedio) | $\frac{f(b) - f(a)}{b - a}$ | Pendiente secante |
| RCI (instantánea) | $\lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$ | Pendiente tangente |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la RCI de $f(x) = x^2 + 3x$ en $x = 1$.

<details>
<summary>Ver solución</summary>

$$\lim_{h \to 0} \frac{f(1+h) - f(1)}{h} = \lim_{h \to 0} \frac{(1+h)^2 + 3(1+h) - 4}{h}$$

$$= \lim_{h \to 0} \frac{1 + 2h + h^2 + 3 + 3h - 4}{h} = \lim_{h \to 0} \frac{5h + h^2}{h}$$

$$= \lim_{h \to 0} (5 + h) = 5$$
</details>

---

**Ejercicio 2:** La altura de una pelota lanzada verticalmente es $h(t) = 20t - 5t^2$ metros. Encuentra la velocidad en $t = 2$ s.

<details>
<summary>Ver solución</summary>

$$v(2) = \lim_{h \to 0} \frac{h(2+h) - h(2)}{h}$$

$h(2) = 40 - 20 = 20$
$h(2+k) = 20(2+k) - 5(2+k)^2 = 40 + 20k - 5(4 + 4k + k^2)$
$= 40 + 20k - 20 - 20k - 5k^2 = 20 - 5k^2$

$$v(2) = \lim_{k \to 0} \frac{20 - 5k^2 - 20}{k} = \lim_{k \to 0} \frac{-5k^2}{k} = 0$$

La velocidad es 0 (punto máximo de la trayectoria).
</details>

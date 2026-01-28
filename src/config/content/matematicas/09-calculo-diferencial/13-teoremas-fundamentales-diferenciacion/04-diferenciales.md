---
title: "Diferenciales"
---

# Diferenciales

El diferencial representa el cambio infinitesimal en una función. Es la base de la notación de Leibniz y tiene aplicaciones en aproximaciones y propagación de errores.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de diferencial
- Relación entre $dy$ y $\Delta y$
- Aproximaciones lineales
- Propagación de errores

---

## 📖 Definiciones

### Diferencial de $x$

$$dx = \Delta x$$

El diferencial de $x$ es simplemente un incremento arbitrario en $x$.

### Diferencial de $y$

$$dy = f'(x) \cdot dx$$

El diferencial de $y$ es el cambio en $y$ a lo largo de la **tangente**.

---

## 📖 Diferencial vs. Incremento

| Cantidad | Definición | En la gráfica |
|----------|-----------|---------------|
| $\Delta y = f(x + \Delta x) - f(x)$ | Cambio real en $y$ | Sobre la **curva** |
| $dy = f'(x) \cdot dx$ | Cambio aproximado | Sobre la **tangente** |

Para $dx$ pequeño: $\Delta y \approx dy$

---

## 📖 Aproximación lineal

$$f(x + dx) \approx f(x) + dy = f(x) + f'(x) \cdot dx$$

Esta es la **aproximación lineal** o **de primer orden**.

---

## ⚙️ Ejemplo 1: Calcular diferenciales

Para $y = x^3$, encuentra $dy$.

$$dy = 3x^2 \cdot dx$$

Si $x = 2$ y $dx = 0.1$:
$$dy = 3(4)(0.1) = 1.2$$

**Comparación con $\Delta y$:**
$$\Delta y = (2.1)^3 - 8 = 9.261 - 8 = 1.261$$

El diferencial aproxima bien el cambio real.

---

## ⚙️ Ejemplo 2: Aproximar un valor

Estimar $\sqrt{4.1}$ usando diferenciales.

Sea $f(x) = \sqrt{x}$, $x = 4$, $dx = 0.1$

$$dy = \frac{1}{2\sqrt{x}} \cdot dx = \frac{1}{4}(0.1) = 0.025$$

$$\sqrt{4.1} \approx \sqrt{4} + dy = 2 + 0.025 = 2.025$$

**Valor real:** $\sqrt{4.1} \approx 2.0248$ ✓

---

## ⚙️ Ejemplo 3: Aproximar función trigonométrica

Estimar $\sin(31°)$.

Sea $f(x) = \sin x$, $x = 30° = \frac{\pi}{6}$, $dx = 1° = \frac{\pi}{180}$

$$dy = \cos x \cdot dx = \cos\left(\frac{\pi}{6}\right) \cdot \frac{\pi}{180}$$

$$= \frac{\sqrt{3}}{2} \cdot \frac{\pi}{180} \approx 0.0151$$

$$\sin(31°) \approx \sin(30°) + 0.0151 = 0.5 + 0.0151 = 0.5151$$

**Valor real:** $\sin(31°) \approx 0.5150$ ✓

---

## 📖 Propagación de errores

Si una medición $x$ tiene error $dx$, el error en $f(x)$ es aproximadamente:

$$df = f'(x) \cdot dx$$

### Error relativo

$$\frac{df}{f} \approx \frac{f'(x) \cdot dx}{f(x)}$$

---

## ⚙️ Ejemplo 4: Error en área

El radio de un círculo se mide como $r = 10$ cm con error máximo de $0.1$ cm. Estima el error máximo en el área.

$$A = \pi r^2$$
$$dA = 2\pi r \cdot dr = 2\pi(10)(0.1) = 2\pi \approx 6.28 \text{ cm}^2$$

**Error relativo:**
$$\frac{dA}{A} = \frac{2\pi r \cdot dr}{\pi r^2} = \frac{2dr}{r} = \frac{2(0.1)}{10} = 0.02 = 2\%$$

---

## ⚙️ Ejemplo 5: Error en volumen

El lado de un cubo se mide como $s = 5$ cm con error de $\pm 0.02$ cm.

$$V = s^3$$
$$dV = 3s^2 \cdot ds = 3(25)(0.02) = 1.5 \text{ cm}^3$$

**Error relativo:**
$$\frac{dV}{V} = \frac{3ds}{s} = \frac{3(0.02)}{5} = 0.012 = 1.2\%$$

---

## 📖 Regla para errores relativos

Para $y = x^n$:
$$\frac{dy}{y} = n \cdot \frac{dx}{x}$$

El error relativo en $y$ es $n$ veces el error relativo en $x$.

---

## 📖 Tabla de diferenciales

| Función | Diferencial |
|---------|-------------|
| $y = x^n$ | $dy = nx^{n-1} dx$ |
| $y = e^x$ | $dy = e^x dx$ |
| $y = \ln x$ | $dy = \frac{dx}{x}$ |
| $y = \sin x$ | $dy = \cos x \, dx$ |
| $y = \cos x$ | $dy = -\sin x \, dx$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa diferenciales para aproximar $(2.03)^4$.

<details>
<summary>Ver solución</summary>

$f(x) = x^4$, $x = 2$, $dx = 0.03$

$dy = 4x^3 dx = 4(8)(0.03) = 0.96$

$(2.03)^4 \approx 16 + 0.96 = 16.96$

(Valor real: 17.0089...)
</details>

---

**Ejercicio 2:** El radio de una esfera se mide con 1% de error. Estima el error porcentual en el volumen.

<details>
<summary>Ver solución</summary>

$V = \frac{4}{3}\pi r^3$

$\frac{dV}{V} = 3 \frac{dr}{r} = 3(1\%) = 3\%$
</details>

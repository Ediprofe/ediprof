# Longitud de Arco

La integral nos permite calcular la longitud de curvas suaves en el plano.

---

## 🎯 ¿Qué vas a aprender?

- Fórmula de longitud de arco
- Longitud para $y = f(x)$
- Longitud para curvas paramétricas
- Ejemplos y aplicaciones

---

## 📖 Derivación de la fórmula

Un pequeño arco tiene longitud aproximada:

$$ds = \sqrt{(dx)^2 + (dy)^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

Integrando:

$$\boxed{L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx}$$

---

## ⚙️ Ejemplo 1: Recta (verificación)

Longitud de $y = 2x$ de $x = 0$ a $x = 3$:

$f'(x) = 2$

$$L = \int_0^3 \sqrt{1 + 4}\,dx = \sqrt{5} \cdot 3 = 3\sqrt{5}$$

**Verificación por Pitágoras:** $\sqrt{3^2 + 6^2} = \sqrt{45} = 3\sqrt{5}$ ✓

---

## ⚙️ Ejemplo 2: Parábola

Longitud de $y = x^2$ de $x = 0$ a $x = 1$:

$f'(x) = 2x$

$$L = \int_0^1 \sqrt{1 + 4x^2}\,dx$$

Por sustitución trigonométrica ($x = \frac{1}{2}\tan\theta$):

$$L = \frac{1}{2}[\sec\theta\tan\theta + \ln|\sec\theta + \tan\theta|]_{...}$$

$$\approx 1.479$$

---

## ⚙️ Ejemplo 3: Función que da integral simple

Longitud de $y = \frac{x^3}{3} + \frac{1}{4x}$ de $x = 1$ a $x = 2$:

$$f'(x) = x^2 - \frac{1}{4x^2}$$

$$1 + [f'(x)]^2 = 1 + x^4 - \frac{1}{2} + \frac{1}{16x^4} = x^4 + \frac{1}{2} + \frac{1}{16x^4}$$

$$= \left(x^2 + \frac{1}{4x^2}\right)^2$$

$$L = \int_1^2 \left(x^2 + \frac{1}{4x^2}\right)\,dx = \left[\frac{x^3}{3} - \frac{1}{4x}\right]_1^2$$

$$= \left(\frac{8}{3} - \frac{1}{8}\right) - \left(\frac{1}{3} - \frac{1}{4}\right) = \frac{59}{24}$$

---

## 📖 Longitud en forma paramétrica

Si $x = x(t)$, $y = y(t)$ para $t \in [\alpha, \beta]$:

$$L = \int_{\alpha}^{\beta} \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt$$

---

## ⚙️ Ejemplo 4: Círculo

Circunferencia de radio $r$:

$x = r\cos t$, $y = r\sin t$, $t \in [0, 2\pi]$

$$x'(t) = -r\sin t, \quad y'(t) = r\cos t$$

$$L = \int_0^{2\pi} \sqrt{r^2\sin^2 t + r^2\cos^2 t}\,dt = \int_0^{2\pi} r\,dt = 2\pi r$$ ✓

---

## ⚙️ Ejemplo 5: Cicloide

$x = t - \sin t$, $y = 1 - \cos t$, un arco ($t \in [0, 2\pi]$):

$$x' = 1 - \cos t, \quad y' = \sin t$$

$$[x']^2 + [y']^2 = (1-\cos t)^2 + \sin^2 t = 2(1 - \cos t) = 4\sin^2\frac{t}{2}$$

$$L = \int_0^{2\pi} 2\sin\frac{t}{2}\,dt = \left[-4\cos\frac{t}{2}\right]_0^{2\pi} = 4 + 4 = 8$$

---

## 📖 Longitud en coordenadas polares

Si $r = f(\theta)$:

$$L = \int_{\alpha}^{\beta} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$

---

## ⚙️ Ejemplo 6: Espiral

Espiral $r = \theta$ de $\theta = 0$ a $\theta = 2\pi$:

$$\frac{dr}{d\theta} = 1$$

$$L = \int_0^{2\pi} \sqrt{\theta^2 + 1}\,d\theta \approx 21.26$$

---

## 📊 Resumen de fórmulas

| Forma | Fórmula de longitud |
|-------|---------------------|
| $y = f(x)$ | $\int\sqrt{1 + (f')^2}\,dx$ |
| Paramétrica | $\int\sqrt{(x')^2 + (y')^2}\,dt$ |
| Polar | $\int\sqrt{r^2 + (r')^2}\,d\theta$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la longitud de $y = \ln(\cos x)$ de $x = 0$ a $x = \frac{\pi}{4}$.

<details>
<summary>Ver solución</summary>

$f'(x) = \frac{-\sin x}{\cos x} = -\tan x$

$L = \int_0^{\pi/4} \sqrt{1 + \tan^2 x}\,dx = \int_0^{\pi/4} \sec x\,dx$

$= [\ln|\sec x + \tan x|]_0^{\pi/4} = \ln(\sqrt{2} + 1)$
</details>

---

**Ejercicio 2:** Longitud de la cardioide $r = 1 + \cos\theta$.

<details>
<summary>Ver solución</summary>

$r' = -\sin\theta$

$L = \int_0^{2\pi}\sqrt{(1+\cos\theta)^2 + \sin^2\theta}\,d\theta$

$= \int_0^{2\pi}\sqrt{2 + 2\cos\theta}\,d\theta = 2\int_0^{2\pi}|\cos\frac{\theta}{2}|\,d\theta = 8$
</details>

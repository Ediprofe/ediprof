# Derivadas de Funciones Paramétricas

A veces las curvas se describen usando un parámetro: $x = f(t)$, $y = g(t)$. La derivación paramétrica nos permite encontrar la pendiente sin eliminar el parámetro.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las ecuaciones paramétricas
- Cómo calcular $\frac{dy}{dx}$ paramétricamente
- Segunda derivada paramétrica
- Tangentes a curvas paramétricas

---

## 📖 Ecuaciones paramétricas

Una curva se describe por:

$$
x = f(t), \quad y = g(t)
$$

donde $t$ es el **parámetro**.

**Ejemplos:**
- Círculo: $x = \cos t$, $y = \sin t$
- Cicloide: $x = t - \sin t$, $y = 1 - \cos t$
- Elipse: $x = a\cos t$, $y = b\sin t$

---

## 📖 Primera derivada

$$\boxed{\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}}$$

siempre que $\frac{dx}{dt} \neq 0$.

---

## ⚙️ Ejemplo 1: Círculo

$x = \cos t$, $y = \sin t$

$$\frac{dx}{dt} = -\sin t, \quad \frac{dy}{dt} = \cos t$$

$$\frac{dy}{dx} = \frac{\cos t}{-\sin t} = -\cot t$$

En $t = \frac{\pi}{4}$: $\frac{dy}{dx} = -\cot\frac{\pi}{4} = -1$

---

## ⚙️ Ejemplo 2: Parábola paramétrica

$x = t^2$, $y = t^3$

$$\frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2$$

$$\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$$

En $t = 2$: $\frac{dy}{dx} = 3$

---

## ⚙️ Ejemplo 3: Elipse

$x = 3\cos t$, $y = 2\sin t$

$$\frac{dx}{dt} = -3\sin t, \quad \frac{dy}{dt} = 2\cos t$$

$$\frac{dy}{dx} = \frac{2\cos t}{-3\sin t} = -\frac{2}{3}\cot t$$

---

## 📖 Segunda derivada

$$
\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}
$$

---

## ⚙️ Ejemplo 4: Segunda derivada

Para $x = t^2$, $y = t^3$, tenemos $\frac{dy}{dx} = \frac{3t}{2}$

$$\frac{d}{dt}\left(\frac{3t}{2}\right) = \frac{3}{2}$$

$$\frac{d^2y}{dx^2} = \frac{3/2}{2t} = \frac{3}{4t}$$

---

## ⚙️ Ejemplo 5: Cicloide

$x = t - \sin t$, $y = 1 - \cos t$

$$\frac{dx}{dt} = 1 - \cos t, \quad \frac{dy}{dt} = \sin t$$

$$\frac{dy}{dx} = \frac{\sin t}{1 - \cos t}$$

Usando identidades ($\sin t = 2\sin\frac{t}{2}\cos\frac{t}{2}$, $1 - \cos t = 2\sin^2\frac{t}{2}$):

$$= \frac{2\sin\frac{t}{2}\cos\frac{t}{2}}{2\sin^2\frac{t}{2}} = \cot\frac{t}{2}$$

---

## 📖 Tangentes horizontales y verticales

**Tangente horizontal:** $\frac{dy}{dx} = 0 \Rightarrow \frac{dy}{dt} = 0$ (con $\frac{dx}{dt} \neq 0$)

**Tangente vertical:** $\frac{dy}{dx}$ indefinida $\Rightarrow \frac{dx}{dt} = 0$ (con $\frac{dy}{dt} \neq 0$)

---

## ⚙️ Ejemplo 6: Encontrar tangentes especiales

Para $x = t^2 - 4$, $y = t^3 - 3t$

$$\frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2 - 3 = 3(t^2 - 1)$$

**Tangente horizontal:** $\frac{dy}{dt} = 0 \Rightarrow t = \pm 1$
- $t = 1$: $(x, y) = (-3, -2)$
- $t = -1$: $(x, y) = (-3, 2)$

**Tangente vertical:** $\frac{dx}{dt} = 0 \Rightarrow t = 0$
- $t = 0$: $(x, y) = (-4, 0)$

---

## ⚙️ Ejemplo 7: Ecuación de tangente

Para $x = t + 1$, $y = t^2 - 2t$, encuentra la tangente en $t = 3$.

**Punto:** $(4, 3)$

**Pendiente:**
$$\frac{dy}{dx} = \frac{2t - 2}{1} = 2t - 2$$

En $t = 3$: $\frac{dy}{dx} = 4$

**Tangente:** $y - 3 = 4(x - 4)$ → $y = 4x - 13$

---

## 📊 Resumen

| Derivada | Fórmula |
|----------|---------|
| Primera | $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ |
| Segunda | $\frac{d^2y}{dx^2} = \frac{d(y')/dt}{dx/dt}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra $\frac{dy}{dx}$ para:

$x = e^t$, $y = e^{2t}$

<details>
<summary>Ver solución</summary>

$\frac{dx}{dt} = e^t$, $\frac{dy}{dt} = 2e^{2t}$

$\frac{dy}{dx} = \frac{2e^{2t}}{e^t} = 2e^t$
</details>

---

**Ejercicio 2:** Encuentra los valores de $t$ donde hay tangente horizontal:

$x = t^3 - 3t$, $y = t^2 - 4$

<details>
<summary>Ver solución</summary>

$\frac{dy}{dt} = 2t = 0 \Rightarrow t = 0$

Punto: $(0, -4)$
</details>

# Ecuaciones Lineales de Primer Orden

Las ecuaciones lineales de primer orden tienen una fórmula de solución general usando el factor integrante.

---

## 🎯 ¿Qué vas a aprender?

- Forma estándar
- El factor integrante
- Fórmula de solución
- Aplicaciones

---

## 📖 Forma estándar

$$
\frac{dy}{dx} + P(x)y = Q(x)
$$

donde $P(x)$ y $Q(x)$ son funciones de $x$ solamente.

---

## 📖 El factor integrante

El **factor integrante** es:

$$
\mu(x) = e^{\int P(x)\,dx}
$$

Al multiplicar la ED por $\mu$, el lado izquierdo se convierte en $\frac{d}{dx}[\mu y]$.

---

## 📖 Fórmula de solución

$$
\boxed{y = \frac{1}{\mu(x)}\left[\int \mu(x)Q(x)\,dx + C\right]}
$$

donde $\mu(x) = e^{\int P(x)\,dx}$

---

## 📖 Método paso a paso

1. **Escribir** en forma estándar
2. **Identificar** $P(x)$ y $Q(x)$
3. **Calcular** $\mu = e^{\int P\,dx}$
4. **Multiplicar** por $\mu$: $\mu y' + \mu P y = \mu Q$
5. **Reconocer:** $(\mu y)' = \mu Q$
6. **Integrar:** $\mu y = \int \mu Q\,dx + C$
7. **Despejar** $y$

---

## ⚙️ Ejemplo 1: Básica

$$
y' + 2y = e^x
$$

$P = 2$, $Q = e^x$

$\mu = e^{\int 2\,dx} = e^{2x}$

$e^{2x}y' + 2e^{2x}y = e^{3x}$

$(e^{2x}y)' = e^{3x}$

$e^{2x}y = \frac{e^{3x}}{3} + C$

$$
y = \frac{e^x}{3} + Ce^{-2x}
$$

---

## ⚙️ Ejemplo 2: Con condición inicial

$$
y' - y = x, \quad y(0) = 1
$$

$P = -1$, $\mu = e^{-x}$

$(e^{-x}y)' = xe^{-x}$

$e^{-x}y = \int xe^{-x}\,dx = -xe^{-x} - e^{-x} + C$

$y = -x - 1 + Ce^x$

**Condición:** $1 = -1 + C \Rightarrow C = 2$

$$
y = -x - 1 + 2e^x
$$

---

## ⚙️ Ejemplo 3: Coeficiente variable

$$
y' + \frac{1}{x}y = x^2, \quad x > 0
$$

$P = \frac{1}{x}$, $\mu = e^{\ln x} = x$

$(xy)' = x^3$

$xy = \frac{x^4}{4} + C$

$$
y = \frac{x^3}{4} + \frac{C}{x}
$$

---

## ⚙️ Ejemplo 4: Circuito RL

Un circuito RL satisface:

$$
L\frac{dI}{dt} + RI = V(t)
$$

En forma estándar: $\frac{dI}{dt} + \frac{R}{L}I = \frac{V(t)}{L}$

$\mu = e^{Rt/L}$

Con $V$ constante e $I(0) = 0$:

$$
I = \frac{V}{R}(1 - e^{-Rt/L})
$$

---

## 📖 Ecuación de Bernoulli

$$
y' + P(x)y = Q(x)y^n
$$

Se reduce a lineal con $v = y^{1-n}$:

$$
v' + (1-n)P(x)v = (1-n)Q(x)
$$

---

## ⚙️ Ejemplo 5: Bernoulli

$$
y' + y = xy^2
$$

$n = 2$, $v = y^{-1}$, $v' = -y^{-2}y'$

$-v' + v = x$

$v' - v = -x$ (lineal en $v$)

$\mu = e^{-x}$, solución: $v = x + 1 + Ce^x$

$$
y = \frac{1}{x + 1 + Ce^x}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $y' + 3y = e^{2x}$.

<details>
<summary>Ver solución</summary>

$\mu = e^{3x}$

$(e^{3x}y)' = e^{5x}$

$e^{3x}y = \frac{e^{5x}}{5} + C$

$y = \frac{e^{2x}}{5} + Ce^{-3x}$
</details>

---

**Ejercicio 2:** Resuelve $xy' + y = x\cos x$, $y(\pi) = 0$.

<details>
<summary>Ver solución</summary>

$y' + \frac{1}{x}y = \cos x$

$\mu = x$

$(xy)' = x\cos x$

$xy = x\sin x + \cos x + C$

$y(\pi) = 0$: $0 = -1 + C$ → $C = 1$

$y = \sin x + \frac{\cos x + 1}{x}$
</details>

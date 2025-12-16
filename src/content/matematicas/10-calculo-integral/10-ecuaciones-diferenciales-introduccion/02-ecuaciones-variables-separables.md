# Ecuaciones de Variables Separables

Las ecuaciones de variables separables son las más simples de resolver: se separan las variables y se integra cada lado.

---

## 🎯 ¿Qué vas a aprender?

- Identificar ecuaciones separables
- El método de separación
- Resolver y verificar
- Aplicaciones

---

## 📖 Forma de una ecuación separable

Una ED es **separable** si se puede escribir como:

$$
\frac{dy}{dx} = f(x) \cdot g(y)
$$

o equivalentemente: $M(x) + N(y)y' = 0$

---

## 📖 Método de solución

1. Separar: $\frac{dy}{g(y)} = f(x)\,dx$
2. Integrar ambos lados: $\int \frac{dy}{g(y)} = \int f(x)\,dx$
3. Despejar $y$ si es posible
4. Aplicar condición inicial si la hay

---

## ⚙️ Ejemplo 1: Básica

$$
\frac{dy}{dx} = xy
$$

**Separar:**
$$
\frac{dy}{y} = x\,dx
$$

**Integrar:**
$$
\ln|y| = \frac{x^2}{2} + C
$$

**Despejar:**
$$
y = Ae^{x^2/2}
$$

donde $A = \pm e^C$

---

## ⚙️ Ejemplo 2: Con condición inicial

$$
\frac{dy}{dx} = \frac{x}{y}, \quad y(0) = 2
$$

**Separar:** $y\,dy = x\,dx$

**Integrar:** $\frac{y^2}{2} = \frac{x^2}{2} + C$

$y^2 = x^2 + 2C$

**Condición:** $4 = 0 + 2C \Rightarrow C = 2$

**Solución:** $y = \sqrt{x^2 + 4}$ (tomamos raíz positiva por $y(0) = 2 > 0$)

---

## ⚙️ Ejemplo 3: Exponencial

$$
y' = y(1-y)
$$

**Separar:** $\frac{dy}{y(1-y)} = dx$

**Fracciones parciales:** $\frac{1}{y(1-y)} = \frac{1}{y} + \frac{1}{1-y}$

**Integrar:** $\ln|y| - \ln|1-y| = x + C$

$\ln\left|\frac{y}{1-y}\right| = x + C$

$\frac{y}{1-y} = Ae^x$

**Despejar:** $y = \frac{Ae^x}{1 + Ae^x}$ (ecuación logística)

---

## ⚙️ Ejemplo 4: Trigonométrica

$$
\frac{dy}{dx} = \frac{\cos x}{e^y}
$$

**Separar:** $e^y\,dy = \cos x\,dx$

**Integrar:** $e^y = \sin x + C$

**Solución:** $y = \ln(\sin x + C)$

---

## 📖 Crecimiento y decaimiento

El modelo $\frac{dy}{dt} = ky$ tiene solución:

$$
y = y_0 e^{kt}
$$

- $k > 0$: crecimiento exponencial
- $k < 0$: decaimiento exponencial

---

## ⚙️ Ejemplo 5: Decaimiento radiactivo

$\frac{dN}{dt} = -\lambda N$, $N(0) = N_0$

**Solución:** $N = N_0 e^{-\lambda t}$

**Vida media:** $t_{1/2} = \frac{\ln 2}{\lambda}$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $\frac{dy}{dx} = \frac{x^2}{y}$, $y(0) = 1$.

<details>
<summary>Ver solución</summary>

$y\,dy = x^2\,dx$

$\frac{y^2}{2} = \frac{x^3}{3} + C$

$y(0) = 1$: $\frac{1}{2} = C$

$y = \sqrt{\frac{2x^3}{3} + 1}$
</details>

---

**Ejercicio 2:** Resuelve $y' = e^{x+y}$.

<details>
<summary>Ver solución</summary>

$y' = e^x \cdot e^y$

$e^{-y}\,dy = e^x\,dx$

$-e^{-y} = e^x + C$

$y = -\ln(-e^x - C)$
</details>

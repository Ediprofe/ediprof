# Ecuaciones Homogéneas

Las ecuaciones homogéneas se resuelven mediante una sustitución que las convierte en separables.

---

## 🎯 ¿Qué vas a aprender?

- Identificar ecuaciones homogéneas
- La sustitución $y = vx$
- Resolver paso a paso
- Ejemplos variados

---

## 📖 Funciones homogéneas

Una función $f(x, y)$ es **homogénea de grado $n$** si:

$$
f(tx, ty) = t^n f(x, y)
$$

---

## 📖 Ecuación diferencial homogénea

Una ED de primer orden es homogénea si puede escribirse:

$$
\frac{dy}{dx} = F\left(\frac{y}{x}\right)
$$

o si $M(x,y)\,dx + N(x,y)\,dy = 0$ donde $M$ y $N$ son homogéneas del mismo grado.

---

## 📖 Método de solución

1. **Sustituir:** $y = vx$ donde $v = \frac{y}{x}$
2. **Derivar:** $\frac{dy}{dx} = v + x\frac{dv}{dx}$
3. **Sustituir** en la ED
4. **Separar** variables $x$ y $v$
5. **Integrar**
6. **Revertir:** $v = \frac{y}{x}$

---

## ⚙️ Ejemplo 1: Básica

$$
\frac{dy}{dx} = \frac{x + y}{x}
$$

**Verificar homogeneidad:** $= 1 + \frac{y}{x} = F(y/x)$ ✓

**Sustituir:** $y = vx$, $y' = v + xv'$

$$v + xv' = 1 + v$$

$$xv' = 1$$

$$dv = \frac{dx}{x}$$

**Integrar:** $v = \ln|x| + C$

**Revertir:** $\frac{y}{x} = \ln|x| + C$

$$
y = x\ln|x| + Cx
$$

---

## ⚙️ Ejemplo 2: Forma M-N

$$
(x^2 + y^2)\,dx - 2xy\,dy = 0
$$

**Reescribir:** $\frac{dy}{dx} = \frac{x^2 + y^2}{2xy}$

**Sustituir:** $y = vx$

$$v + xv' = \frac{x^2 + v^2x^2}{2vx^2} = \frac{1 + v^2}{2v}$$

$$xv' = \frac{1 + v^2}{2v} - v = \frac{1 + v^2 - 2v^2}{2v} = \frac{1 - v^2}{2v}$$

$$\frac{2v\,dv}{1 - v^2} = \frac{dx}{x}$$

**Integrar:** $-\ln|1 - v^2| = \ln|x| + C$

$\frac{1}{|1-v^2|} = A|x|$

---

## ⚙️ Ejemplo 3: Con condición inicial

$$
\frac{dy}{dx} = \frac{y}{x} + \tan\frac{y}{x}, \quad y(1) = \frac{\pi}{4}
$$

$y = vx$: $v + xv' = v + \tan v$

$xv' = \tan v$

$\frac{dv}{\tan v} = \frac{dx}{x}$

$\int \cot v\,dv = \int \frac{dx}{x}$

$\ln|\sin v| = \ln|x| + C$

$\sin v = Ax$

**Condición:** $\sin\frac{\pi}{4} = A \cdot 1 \Rightarrow A = \frac{\sqrt{2}}{2}$

$\sin\frac{y}{x} = \frac{\sqrt{2}}{2}x$

---

## 📖 Identificación rápida

La ED $\frac{dy}{dx} = \frac{M(x,y)}{N(x,y)}$ es homogénea si al reemplazar $x \to tx$, $y \to ty$, las $t$ se cancelan.

---

## ⚙️ Ejemplo 4: Verificar

$\frac{dy}{dx} = \frac{xy + y^2}{x^2}$

Con $x \to tx$, $y \to ty$:

$\frac{(tx)(ty) + (ty)^2}{(tx)^2} = \frac{t^2(xy + y^2)}{t^2 x^2} = \frac{xy + y^2}{x^2}$ ✓

Es homogénea.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $(x + y)\,dx - x\,dy = 0$.

<details>
<summary>Ver solución</summary>

$\frac{dy}{dx} = \frac{x+y}{x} = 1 + \frac{y}{x}$

$y = vx$: $v + xv' = 1 + v$

$xv' = 1$ → $v = \ln|x| + C$

$y = x\ln|x| + Cx$
</details>

---

**Ejercicio 2:** Resuelve $x\,dy - y\,dx = \sqrt{x^2 + y^2}\,dx$.

<details>
<summary>Ver solución</summary>

$\frac{dy}{dx} = \frac{y + \sqrt{x^2+y^2}}{x} = \frac{y}{x} + \sqrt{1 + (y/x)^2}$

$y = vx$: $v + xv' = v + \sqrt{1+v^2}$

$\frac{dv}{\sqrt{1+v^2}} = \frac{dx}{x}$

$\sinh^{-1}(v) = \ln|x| + C$

$v = \sinh(\ln|x| + C)$
</details>

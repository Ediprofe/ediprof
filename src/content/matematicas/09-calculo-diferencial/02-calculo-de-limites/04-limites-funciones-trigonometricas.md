# Límites de Funciones Trigonométricas

Las funciones trigonométricas tienen límites especiales que aparecen constantemente en cálculo. El más importante es el límite fundamental del seno.

---

## 🎯 ¿Qué vas a aprender?

- El límite fundamental $\lim_{x \to 0} \frac{\sin x}{x}$
- Límites relacionados con seno y coseno
- Técnicas para límites trigonométricos
- Límites con tangente y otras funciones

---

## 📖 El límite fundamental

$$\boxed{\lim_{x \to 0} \frac{\sin x}{x} = 1}$$

Este es el límite más importante en trigonometría diferencial.

### ⚠️ Nota sobre unidades

Este límite solo vale cuando $x$ está en **radianes**.

### Demostración geométrica (idea)

Para $0 < x < \frac{\pi}{2}$:

$$\cos x < \frac{\sin x}{x} < 1$$

Cuando $x \to 0$, $\cos x \to 1$, por el teorema del encaje:

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

---

## 📖 Límites equivalentes

Del límite fundamental se derivan:

$$\lim_{x \to 0} \frac{x}{\sin x} = 1$$

$$\lim_{x \to 0} \frac{\tan x}{x} = 1$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$

---

## ⚙️ Ejemplo 1: Límite fundamental directo

$$\lim_{x \to 0} \frac{\sin 3x}{x}$$

**Técnica:** Hacer que argumento y denominador coincidan.

$$= \lim_{x \to 0} \frac{\sin 3x}{x} \cdot \frac{3}{3} = \lim_{x \to 0} 3 \cdot \frac{\sin 3x}{3x}$$

Sea $u = 3x$. Cuando $x \to 0$, $u \to 0$:

$$= 3 \cdot \lim_{u \to 0} \frac{\sin u}{u} = 3 \cdot 1 = 3$$

---

## ⚙️ Ejemplo 2: Cociente de senos

$$\lim_{x \to 0} \frac{\sin 5x}{\sin 2x}$$

**Reescribimos:**
$$= \lim_{x \to 0} \frac{\sin 5x}{5x} \cdot \frac{5x}{2x} \cdot \frac{2x}{\sin 2x}$$

$$= \lim_{x \to 0} \frac{\sin 5x}{5x} \cdot \frac{5}{2} \cdot \frac{2x}{\sin 2x}$$

$$= 1 \cdot \frac{5}{2} \cdot 1 = \frac{5}{2}$$

---

## ⚙️ Ejemplo 3: Con tangente

$$\lim_{x \to 0} \frac{\tan x}{x}$$

$$= \lim_{x \to 0} \frac{\sin x}{x \cos x} = \lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{1}{\cos x}$$

$$= 1 \cdot \frac{1}{1} = 1$$

---

## ⚙️ Ejemplo 4: Límite con $1 - \cos x$

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2}$$

**Usando identidad:** $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$

$$= \lim_{x \to 0} \frac{2\sin^2(x/2)}{x^2}$$

$$= \lim_{x \to 0} \frac{2\sin^2(x/2)}{4 \cdot (x/2)^2} = \frac{2}{4} \lim_{x \to 0} \left(\frac{\sin(x/2)}{x/2}\right)^2$$

$$= \frac{1}{2} \cdot 1^2 = \frac{1}{2}$$

---

## ⚙️ Ejemplo 5: Expresión más compleja

$$\lim_{x \to 0} \frac{\sin x - x}{x^3}$$

**Este es un límite más avanzado.** Usando series de Taylor:

$$\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$$

$$\sin x - x = -\frac{x^3}{6} + O(x^5)$$

$$\frac{\sin x - x}{x^3} = -\frac{1}{6} + O(x^2) \to -\frac{1}{6}$$

---

## 📖 Límites en otros puntos

### En $x = \frac{\pi}{2}$

$$\lim_{x \to \pi/2} \cos x = 0$$

$$\lim_{x \to \pi/2} \tan x = \text{no existe (laterales diferentes)}$$

### En $x = \pi$

$$\lim_{x \to \pi} \sin x = 0$$

$$\lim_{x \to \pi} \cos x = -1$$

---

## 📖 Tabla de límites trigonométricos fundamentales

| Límite | Valor |
|--------|-------|
| $\lim_{x \to 0} \frac{\sin x}{x}$ | $1$ |
| $\lim_{x \to 0} \frac{\tan x}{x}$ | $1$ |
| $\lim_{x \to 0} \frac{1 - \cos x}{x}$ | $0$ |
| $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | $\frac{1}{2}$ |
| $\lim_{x \to 0} \frac{\sin ax}{\sin bx}$ | $\frac{a}{b}$ |
| $\lim_{x \to 0} \frac{\arcsin x}{x}$ | $1$ |
| $\lim_{x \to 0} \frac{\arctan x}{x}$ | $1$ |

---

## ⚙️ Ejemplo 6: Con función inversa

$$\lim_{x \to 0} \frac{\arcsin x}{x}$$

Sea $y = \arcsin x$, entonces $x = \sin y$ y cuando $x \to 0$, $y \to 0$:

$$= \lim_{y \to 0} \frac{y}{\sin y} = 1$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\lim_{x \to 0} \frac{\sin 4x}{3x}$

b) $\lim_{x \to 0} \frac{\sin x \cdot \cos x}{x}$

<details>
<summary>Ver soluciones</summary>

a) $= \frac{4}{3} \cdot \lim_{x \to 0} \frac{\sin 4x}{4x} = \frac{4}{3}$

b) $= \lim_{x \to 0} \frac{\sin x}{x} \cdot \cos x = 1 \cdot 1 = 1$
</details>

---

**Ejercicio 2:** Calcula:

$$\lim_{x \to 0} \frac{\sin 2x}{\sin 5x}$$

<details>
<summary>Ver solución</summary>

$$= \frac{2x}{5x} \cdot \frac{\sin 2x}{2x} \cdot \frac{5x}{\sin 5x} = \frac{2}{5} \cdot 1 \cdot 1 = \frac{2}{5}$$
</details>

---

**Ejercicio 3:** Calcula:

$$\lim_{x \to 0} \frac{1 - \cos 2x}{x^2}$$

<details>
<summary>Ver solución</summary>

Usando $1 - \cos 2x = 2\sin^2 x$:

$$= \lim_{x \to 0} \frac{2\sin^2 x}{x^2} = 2 \cdot \left(\lim_{x \to 0} \frac{\sin x}{x}\right)^2 = 2 \cdot 1 = 2$$
</details>

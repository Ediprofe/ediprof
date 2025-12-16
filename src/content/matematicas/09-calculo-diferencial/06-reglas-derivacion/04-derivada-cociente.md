# Regla del Cociente

Derivar un cociente de funciones requiere su propia regla. Es un poco más compleja que la del producto, pero sigue un patrón memorable.

---

## 🎯 ¿Qué vas a aprender?

- La regla del cociente
- Patrones para recordarla
- Cuándo usar el cociente vs. otras técnicas
- Simplificación de resultados

---

## 📖 La regla del cociente

$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$$

O en notación corta:

$$\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$$

---

## 📖 Mnemotécnico

**"Bajo por derivada de arriba, menos arriba por derivada de bajo, sobre el cuadrado de abajo"**

O simplificado:
- $\frac{(\text{abajo})(\text{d-arriba}) - (\text{arriba})(\text{d-abajo})}{(\text{abajo})^2}$

---

## ⚙️ Ejemplo 1: Cociente simple

Deriva $f(x) = \frac{x^2}{x + 1}$

Sea: $\text{arriba} = x^2$, $\text{abajo} = x + 1$

$$f'(x) = \frac{(2x)(x + 1) - (x^2)(1)}{(x + 1)^2}$$

$$= \frac{2x^2 + 2x - x^2}{(x + 1)^2} = \frac{x^2 + 2x}{(x + 1)^2}$$

$$= \frac{x(x + 2)}{(x + 1)^2}$$

---

## ⚙️ Ejemplo 2: Derivar la tangente

Deriva $\tan x = \frac{\sin x}{\cos x}$

$$(\tan x)' = \frac{(\cos x)(\cos x) - (\sin x)(-\sin x)}{(\cos x)^2}$$

$$= \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}$$

$$= \sec^2 x$$

---

## ⚙️ Ejemplo 3: Función racional

Deriva $g(x) = \frac{3x - 1}{2x + 5}$

$$g'(x) = \frac{(3)(2x + 5) - (3x - 1)(2)}{(2x + 5)^2}$$

$$= \frac{6x + 15 - 6x + 2}{(2x + 5)^2}$$

$$= \frac{17}{(2x + 5)^2}$$

---

## ⚙️ Ejemplo 4: Con raíces

Deriva $h(x) = \frac{\sqrt{x}}{x + 1}$

$$h'(x) = \frac{\frac{1}{2\sqrt{x}}(x + 1) - \sqrt{x}(1)}{(x + 1)^2}$$

$$= \frac{\frac{x + 1}{2\sqrt{x}} - \sqrt{x}}{(x + 1)^2}$$

Multiplicando numerador y denominador del numerador por $2\sqrt{x}$:

$$= \frac{\frac{x + 1 - 2x}{2\sqrt{x}}}{(x + 1)^2} = \frac{1 - x}{2\sqrt{x}(x + 1)^2}$$

---

## ⚙️ Ejemplo 5: Derivar la cotangente

Deriva $\cot x = \frac{\cos x}{\sin x}$

$$(\cot x)' = \frac{(-\sin x)(\sin x) - (\cos x)(\cos x)}{(\sin x)^2}$$

$$= \frac{-\sin^2 x - \cos^2 x}{\sin^2 x} = \frac{-1}{\sin^2 x}$$

$$= -\csc^2 x$$

---

## 📖 Alternativa: Reescribir como producto

A veces es más fácil evitar la regla del cociente reescribiendo:

$$\frac{f}{g} = f \cdot g^{-1}$$

Y usando producto + regla de la cadena.

---

## ⚙️ Ejemplo 6: Como producto

Deriva $\frac{1}{x^2 + 1}$ de dos formas:

**Forma 1: Cociente**
$$= \frac{0 \cdot (x^2+1) - 1 \cdot 2x}{(x^2+1)^2} = \frac{-2x}{(x^2+1)^2}$$

**Forma 2: Potencia negativa**
$(x^2+1)^{-1}$
$$= -1 \cdot (x^2+1)^{-2} \cdot 2x = \frac{-2x}{(x^2+1)^2}$$

Mismo resultado ✓

---

## 📊 Derivadas de funciones trigonométricas (cocientes)

| Función | Derivada |
|---------|----------|
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x = \frac{1}{\cos x}$ | $\sec x \tan x$ |
| $\csc x = \frac{1}{\sin x}$ | $-\csc x \cot x$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $f(x) = \frac{x}{x - 1}$
b) $g(x) = \frac{x^2 + 1}{x^2 - 1}$

<details>
<summary>Ver soluciones</summary>

a) $f'(x) = \frac{(1)(x-1) - (x)(1)}{(x-1)^2} = \frac{-1}{(x-1)^2}$

b) $g'(x) = \frac{2x(x^2-1) - (x^2+1)(2x)}{(x^2-1)^2}$
   
   $= \frac{2x^3 - 2x - 2x^3 - 2x}{(x^2-1)^2} = \frac{-4x}{(x^2-1)^2}$
</details>

---

**Ejercicio 2:** Encuentra la tangente a $f(x) = \frac{x}{x + 2}$ en $x = 0$.

<details>
<summary>Ver solución</summary>

$f(0) = 0$ → $(0, 0)$

$f'(x) = \frac{(1)(x+2) - x(1)}{(x+2)^2} = \frac{2}{(x+2)^2}$

$f'(0) = \frac{2}{4} = \frac{1}{2}$

Tangente: $y = \frac{1}{2}x$
</details>

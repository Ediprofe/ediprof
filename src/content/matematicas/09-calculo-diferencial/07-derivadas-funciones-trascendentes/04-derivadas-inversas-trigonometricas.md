# Derivadas de Funciones Trigonométricas Inversas

Las funciones arco (arcseno, arccoseno, etc.) son las inversas de las trigonométricas. Sus derivadas son algebraicas, no trigonométricas, lo cual es notable.

---

## 🎯 ¿Qué vas a aprender?

- Derivadas de las seis funciones inversas
- Cómo se derivan usando derivación implícita
- Aplicación con la regla de la cadena

---

## 📖 Las seis derivadas

| Función | Derivada | Dominio |
|---------|----------|---------|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | $\|x\| < 1$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ | $\|x\| < 1$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ | $x \in \mathbb{R}$ |
| $\text{arccot } x$ | $-\frac{1}{1+x^2}$ | $x \in \mathbb{R}$ |
| $\text{arcsec } x$ | $\frac{1}{\|x\|\sqrt{x^2-1}}$ | $\|x\| > 1$ |
| $\text{arccsc } x$ | $-\frac{1}{\|x\|\sqrt{x^2-1}}$ | $\|x\| > 1$ |

---

## 📖 Demostración: $(\arcsin x)'$

Sea $y = \arcsin x$, entonces $\sin y = x$ con $y \in [-\frac{\pi}{2}, \frac{\pi}{2}]$

Derivando implícitamente:
$$\cos y \cdot \frac{dy}{dx} = 1$$

$$\frac{dy}{dx} = \frac{1}{\cos y}$$

Como $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$ (positivo en el rango):

$$\boxed{(\arcsin x)' = \frac{1}{\sqrt{1 - x^2}}}$$

---

## 📖 Demostración: $(\arctan x)'$

Sea $y = \arctan x$, entonces $\tan y = x$

Derivando implícitamente:
$$\sec^2 y \cdot \frac{dy}{dx} = 1$$

$$\frac{dy}{dx} = \frac{1}{\sec^2 y} = \cos^2 y$$

Usando $\sec^2 y = 1 + \tan^2 y = 1 + x^2$:

$$\boxed{(\arctan x)' = \frac{1}{1 + x^2}}$$

---

## 📖 Patrón notable

Las derivadas de $\arcsin$ y $\arccos$ solo difieren en el signo:

$$(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}$$

$$(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$$

Esto es porque $\arcsin x + \arccos x = \frac{\pi}{2}$ (constante).

---

## ⚙️ Ejemplo 1: Arcseno directo

$$\frac{d}{dx}[\arcsin x] = \frac{1}{\sqrt{1 - x^2}}$$

---

## ⚙️ Ejemplo 2: Arctangente directo

$$\frac{d}{dx}[\arctan x] = \frac{1}{1 + x^2}$$

---

## ⚙️ Ejemplo 3: Con regla de la cadena

Deriva $f(x) = \arcsin(2x)$

$$f'(x) = \frac{1}{\sqrt{1 - (2x)^2}} \cdot 2 = \frac{2}{\sqrt{1 - 4x^2}}$$

---

## ⚙️ Ejemplo 4: Arctangente compuesta

Deriva $g(x) = \arctan(x^2)$

$$g'(x) = \frac{1}{1 + (x^2)^2} \cdot 2x = \frac{2x}{1 + x^4}$$

---

## ⚙️ Ejemplo 5: Arccoseno

Deriva $h(x) = \arccos(\sqrt{x})$

$$h'(x) = -\frac{1}{\sqrt{1 - x}} \cdot \frac{1}{2\sqrt{x}}$$

$$= -\frac{1}{2\sqrt{x}\sqrt{1-x}} = -\frac{1}{2\sqrt{x(1-x)}}$$

---

## ⚙️ Ejemplo 6: Múltiplo

Deriva $f(x) = 3\arctan(5x)$

$$f'(x) = 3 \cdot \frac{1}{1 + 25x^2} \cdot 5 = \frac{15}{1 + 25x^2}$$

---

## ⚙️ Ejemplo 7: Con producto

Deriva $g(x) = x \arcsin x$

$$g'(x) = 1 \cdot \arcsin x + x \cdot \frac{1}{\sqrt{1-x^2}}$$

$$= \arcsin x + \frac{x}{\sqrt{1-x^2}}$$

---

## 📖 Integral inversa (anticipación)

Estas derivadas son importantes porque dan lugar a integrales:

$$\int \frac{1}{\sqrt{1-x^2}} dx = \arcsin x + C$$

$$\int \frac{1}{1+x^2} dx = \arctan x + C$$

---

## 📊 Resumen con cadena

| $f(u)$ | $\frac{d}{dx}[f(u)]$ |
|--------|----------------------|
| $\arcsin u$ | $\frac{u'}{\sqrt{1-u^2}}$ |
| $\arccos u$ | $-\frac{u'}{\sqrt{1-u^2}}$ |
| $\arctan u$ | $\frac{u'}{1+u^2}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $\arcsin(3x)$
b) $\arctan(x + 1)$
c) $\arccos(x^2)$

<details>
<summary>Ver soluciones</summary>

a) $\frac{3}{\sqrt{1 - 9x^2}}$

b) $\frac{1}{1 + (x+1)^2} = \frac{1}{x^2 + 2x + 2}$

c) $-\frac{2x}{\sqrt{1 - x^4}}$
</details>

---

**Ejercicio 2:** Deriva $f(x) = \arctan\left(\frac{1}{x}\right)$

<details>
<summary>Ver solución</summary>

$$f'(x) = \frac{1}{1 + \frac{1}{x^2}} \cdot \left(-\frac{1}{x^2}\right)$$

$$= \frac{-\frac{1}{x^2}}{\frac{x^2 + 1}{x^2}} = \frac{-1}{x^2 + 1}$$
</details>

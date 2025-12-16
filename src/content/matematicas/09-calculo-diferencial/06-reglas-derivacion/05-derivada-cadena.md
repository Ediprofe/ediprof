# Regla de la Cadena

La regla de la cadena es la herramienta más poderosa de diferenciación. Permite derivar funciones compuestas: funciones dentro de funciones.

---

## 🎯 ¿Qué vas a aprender?

- La regla de la cadena para composiciones
- Cómo identificar la función "exterior" e "interior"
- Aplicaciones múltiples de la cadena
- Notación de Leibniz para la cadena

---

## 📖 La regla de la cadena

Si $y = f(g(x))$, entonces:

$$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$$

**"Derivada de afuera evaluada en dentro, por derivada de dentro."**

En notación de Leibniz:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

donde $u = g(x)$.

---

## 📖 Cómo identificar las funciones

En $(x^2 + 1)^5$:

- **Función exterior:** $( \cdot )^5$ → "elevar a la 5"
- **Función interior:** $x^2 + 1$

En $\sin(3x)$:

- **Función exterior:** $\sin(\cdot)$
- **Función interior:** $3x$

En $e^{x^2}$:

- **Función exterior:** $e^{(\cdot)}$
- **Función interior:** $x^2$

---

## ⚙️ Ejemplo 1: Potencia de una función

Deriva $f(x) = (x^2 + 1)^5$

**Exterior:** $u^5$ → derivada: $5u^4$
**Interior:** $u = x^2 + 1$ → derivada: $2x$

$$f'(x) = 5(x^2 + 1)^4 \cdot 2x = 10x(x^2 + 1)^4$$

---

## ⚙️ Ejemplo 2: Seno de función

Deriva $g(x) = \sin(3x)$

**Exterior:** $\sin u$ → derivada: $\cos u$
**Interior:** $u = 3x$ → derivada: $3$

$$g'(x) = \cos(3x) \cdot 3 = 3\cos(3x)$$

---

## ⚙️ Ejemplo 3: Exponencial

Deriva $h(x) = e^{x^2}$

**Exterior:** $e^u$ → derivada: $e^u$
**Interior:** $u = x^2$ → derivada: $2x$

$$h'(x) = e^{x^2} \cdot 2x = 2xe^{x^2}$$

---

## ⚙️ Ejemplo 4: Raíz de función

Deriva $f(x) = \sqrt{x^3 + 2x}$

Reescribimos: $f(x) = (x^3 + 2x)^{1/2}$

$$f'(x) = \frac{1}{2}(x^3 + 2x)^{-1/2} \cdot (3x^2 + 2)$$

$$= \frac{3x^2 + 2}{2\sqrt{x^3 + 2x}}$$

---

## ⚙️ Ejemplo 5: Logaritmo de función

Deriva $g(x) = \ln(x^2 + 1)$

**Exterior:** $\ln u$ → derivada: $\frac{1}{u}$
**Interior:** $u = x^2 + 1$ → derivada: $2x$

$$g'(x) = \frac{1}{x^2 + 1} \cdot 2x = \frac{2x}{x^2 + 1}$$

---

## 📖 Regla de la cadena extendida

Para composiciones múltiples $f(g(h(x)))$:

$$\frac{d}{dx}[f(g(h(x)))] = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

---

## ⚙️ Ejemplo 6: Cadena doble

Deriva $f(x) = \sin^2(3x) = [\sin(3x)]^2$

**Capa 1:** $u^2$ → $2u$
**Capa 2:** $\sin v$ → $\cos v$
**Capa 3:** $3x$ → $3$

$$f'(x) = 2[\sin(3x)] \cdot \cos(3x) \cdot 3$$

$$= 6\sin(3x)\cos(3x) = 3\sin(6x)$$

(usando la identidad $2\sin\theta\cos\theta = \sin 2\theta$)

---

## ⚙️ Ejemplo 7: Con varias reglas

Deriva $h(x) = x^2 \cdot e^{3x}$

Usamos producto + cadena:

$$h'(x) = 2x \cdot e^{3x} + x^2 \cdot e^{3x} \cdot 3$$

$$= e^{3x}(2x + 3x^2) = xe^{3x}(2 + 3x)$$

---

## 📖 Regla de la potencia generalizada

$$\frac{d}{dx}[u^n] = nu^{n-1} \cdot u'$$

donde $u$ es una función de $x$.

---

## 📊 Derivadas con regla de la cadena

| Forma | Derivada |
|-------|----------|
| $[u(x)]^n$ | $nu^{n-1} \cdot u'$ |
| $e^{u(x)}$ | $e^u \cdot u'$ |
| $\ln[u(x)]$ | $\frac{u'}{u}$ |
| $\sin[u(x)]$ | $\cos u \cdot u'$ |
| $\cos[u(x)]$ | $-\sin u \cdot u'$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $(3x - 1)^7$
b) $\cos(x^2)$
c) $e^{-x}$

<details>
<summary>Ver soluciones</summary>

a) $7(3x-1)^6 \cdot 3 = 21(3x-1)^6$

b) $-\sin(x^2) \cdot 2x = -2x\sin(x^2)$

c) $e^{-x} \cdot (-1) = -e^{-x}$
</details>

---

**Ejercicio 2:** Deriva:

$$f(x) = \sqrt{1 + \sin x}$$

<details>
<summary>Ver solución</summary>

$$f(x) = (1 + \sin x)^{1/2}$$

$$f'(x) = \frac{1}{2}(1 + \sin x)^{-1/2} \cdot \cos x$$

$$= \frac{\cos x}{2\sqrt{1 + \sin x}}$$
</details>

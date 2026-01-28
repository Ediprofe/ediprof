---
title: "Derivación Logarítmica"
---

# Derivación Logarítmica

Algunas funciones son difíciles de derivar directamente, pero se simplifican tomando logaritmos primero. La derivación logarítmica es especialmente útil para productos, cocientes y potencias variables.

---

## 🎯 ¿Qué vas a aprender?

- La técnica de derivación logarítmica
- Cuándo es más útil usarla
- Derivada de $x^x$ y formas similares
- Simplificación de productos complicados

---

## 📖 El método

**Pasos:**
1. Tomar logaritmo natural de ambos lados: $\ln y = \ln f(x)$
2. Simplificar usando propiedades de logaritmos
3. Derivar implícitamente
4. Despejar $\frac{dy}{dx}$
5. Sustituir $y = f(x)$

---

## 📖 Cuándo usarla

- **Potencias variables:** $f(x)^{g(x)}$
- **Productos complicados:** $f \cdot g \cdot h \cdot \ldots$
- **Cocientes complicados:** $\frac{f \cdot g}{h \cdot k}$
- **Raíces de productos:** $\sqrt[n]{f \cdot g}$

---

## ⚙️ Ejemplo 1: La función $x^x$

Deriva $y = x^x$ para $x > 0$

**Paso 1:** $\ln y = \ln(x^x) = x \ln x$

**Paso 2:** Derivamos implícitamente:
$$\frac{1}{y} \cdot \frac{dy}{dx} = 1 \cdot \ln x + x \cdot \frac{1}{x}$$

$$\frac{1}{y} \cdot \frac{dy}{dx} = \ln x + 1$$

**Paso 3:** Despejamos:
$$\frac{dy}{dx} = y(\ln x + 1) = x^x(\ln x + 1)$$

$$\boxed{(x^x)' = x^x(\ln x + 1)}$$

---

## ⚙️ Ejemplo 2: Forma general $f(x)^{g(x)}$

Deriva $y = (\sin x)^x$

**Paso 1:** $\ln y = x \ln(\sin x)$

**Paso 2:** Derivamos:
$$\frac{y'}{y} = \ln(\sin x) + x \cdot \frac{\cos x}{\sin x}$$

$$\frac{y'}{y} = \ln(\sin x) + x\cot x$$

**Paso 3:**
$$y' = (\sin x)^x [\ln(\sin x) + x\cot x]$$

---

## ⚙️ Ejemplo 3: Producto largo

Deriva $y = (x+1)(x+2)(x+3)$

**Sin logaritmos:** Expandir y derivar → tedioso

**Con logaritmos:**
$$\ln y = \ln(x+1) + \ln(x+2) + \ln(x+3)$$

$$\frac{y'}{y} = \frac{1}{x+1} + \frac{1}{x+2} + \frac{1}{x+3}$$

$$y' = (x+1)(x+2)(x+3)\left[\frac{1}{x+1} + \frac{1}{x+2} + \frac{1}{x+3}\right]$$

---

## ⚙️ Ejemplo 4: Cociente complejo

Deriva $y = \frac{x^2 \sqrt{x+1}}{(x-1)^3}$

**Con logaritmos:**
$$\ln y = 2\ln x + \frac{1}{2}\ln(x+1) - 3\ln(x-1)$$

$$\frac{y'}{y} = \frac{2}{x} + \frac{1}{2(x+1)} - \frac{3}{x-1}$$

$$y' = \frac{x^2 \sqrt{x+1}}{(x-1)^3}\left[\frac{2}{x} + \frac{1}{2(x+1)} - \frac{3}{x-1}\right]$$

---

## ⚙️ Ejemplo 5: $x^{\sin x}$

Deriva $y = x^{\sin x}$

$$\ln y = \sin x \cdot \ln x$$

$$\frac{y'}{y} = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x}$$

$$y' = x^{\sin x}\left[\cos x \ln x + \frac{\sin x}{x}\right]$$

---

## ⚙️ Ejemplo 6: Raíz de producto

Deriva $y = \sqrt[3]{x(x+1)(x+2)}$

$$\ln y = \frac{1}{3}[\ln x + \ln(x+1) + \ln(x+2)]$$

$$\frac{y'}{y} = \frac{1}{3}\left[\frac{1}{x} + \frac{1}{x+1} + \frac{1}{x+2}\right]$$

$$y' = \frac{1}{3}\sqrt[3]{x(x+1)(x+2)}\left[\frac{1}{x} + \frac{1}{x+1} + \frac{1}{x+2}\right]$$

---

## 📖 Fórmula general para $f^g$

Para $y = [f(x)]^{g(x)}$ donde $f(x) > 0$:

$$y' = [f(x)]^{g(x)}\left[g'(x)\ln f(x) + g(x) \cdot \frac{f'(x)}{f(x)}\right]$$

---

## 📖 Casos especiales verificados

| Función | Usando la fórmula |
|---------|-------------------|
| $x^n$ (n constante) | $x^n \cdot \frac{n}{x} = nx^{n-1}$ ✓ |
| $a^x$ (a constante) | $a^x \cdot \ln a$ ✓ |
| $x^x$ | $x^x(\ln x + 1)$ ✓ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa derivación logarítmica:

$$y = x^{1/x}$$

<details>
<summary>Ver solución</summary>

$\ln y = \frac{1}{x} \ln x = \frac{\ln x}{x}$

$\frac{y'}{y} = \frac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}$

$y' = x^{1/x} \cdot \frac{1 - \ln x}{x^2}$
</details>

---

**Ejercicio 2:** Deriva:

$$y = \frac{(x-1)(x-2)}{(x+1)(x+2)}$$

<details>
<summary>Ver solución</summary>

$\ln y = \ln(x-1) + \ln(x-2) - \ln(x+1) - \ln(x+2)$

$\frac{y'}{y} = \frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x+1} - \frac{1}{x+2}$

$y' = \frac{(x-1)(x-2)}{(x+1)(x+2)}\left[\frac{1}{x-1} + \frac{1}{x-2} - \frac{1}{x+1} - \frac{1}{x+2}\right]$
</details>

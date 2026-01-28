---
title: "Derivada de Suma y Resta"
---

# Derivada de Suma y Resta

La derivación es una operación lineal: podemos derivar término a término. Esta propiedad hace que la derivación de polinomios sea directa y sistemática.

---

## 🎯 ¿Qué vas a aprender?

- Regla de la suma
- Regla de la resta
- Combinación con otras reglas
- Derivación de polinomios

---

## 📖 Regla de la suma

$$
\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
$$

**"La derivada de la suma es la suma de las derivadas."**

---

## 📖 Regla de la resta

$$
\frac{d}{dx}[f(x) - g(x)] = f'(x) - g'(x)
$$

**"La derivada de la diferencia es la diferencia de las derivadas."**

---

## 📖 Generalización

Para cualquier combinación lineal:

$$
\frac{d}{dx}[af(x) + bg(x)] = af'(x) + bg'(x)
$$

donde $a$ y $b$ son constantes.

---

## ⚙️ Ejemplo 1: Suma simple

Deriva $f(x) = x^3 + x^2$

$$f'(x) = \frac{d}{dx}[x^3] + \frac{d}{dx}[x^2]$$

$$= 3x^2 + 2x$$

---

## ⚙️ Ejemplo 2: Resta

Deriva $g(x) = x^5 - x^3$

$$g'(x) = 5x^4 - 3x^2$$

---

## ⚙️ Ejemplo 3: Polinomio completo

Deriva $h(x) = 3x^4 - 5x^3 + 2x^2 - 7x + 8$

$$h'(x) = 12x^3 - 15x^2 + 4x - 7$$

Cada término se deriva por separado usando la regla de la potencia.

---

## ⚙️ Ejemplo 4: Con raíces y fracciones

Deriva $f(x) = \sqrt{x} + \frac{1}{x}$

Reescribimos: $f(x) = x^{1/2} + x^{-1}$

$$f'(x) = \frac{1}{2}x^{-1/2} + (-1)x^{-2}$$

$$= \frac{1}{2\sqrt{x}} - \frac{1}{x^2}$$

---

## ⚙️ Ejemplo 5: Simplificar antes de derivar

Deriva $g(x) = \frac{x^3 + 2x^2}{x}$

Simplificamos primero:
$$g(x) = \frac{x^3}{x} + \frac{2x^2}{x} = x^2 + 2x$$

Ahora derivamos:
$$g'(x) = 2x + 2$$

---

## ⚙️ Ejemplo 6: Desarrollar antes de derivar

Deriva $h(x) = (x + 3)^2$

Expandimos primero:
$$h(x) = x^2 + 6x + 9$$

Derivamos:
$$h'(x) = 2x + 6$$

(También se puede usar la regla de la cadena, que veremos después.)

---

## 📖 Derivada de un polinomio general

Si $P(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$

Entonces:
$$P'(x) = na_nx^{n-1} + (n-1)a_{n-1}x^{n-2} + \cdots + a_1$$

El grado baja en uno y el término constante desaparece.

---

## ⚙️ Ejemplo 7: Evaluar derivada en un punto

Si $f(x) = x^3 - 4x^2 + 5x - 2$, encuentra $f'(2)$.

**Paso 1:** Derivar
$$f'(x) = 3x^2 - 8x + 5$$

**Paso 2:** Evaluar
$$f'(2) = 3(4) - 8(2) + 5 = 12 - 16 + 5 = 1$$

---

## ⚙️ Ejemplo 8: Ecuación de tangente

Encuentra la ecuación de la tangente a $f(x) = x^2 - 3x + 1$ en $x = 2$.

**Punto:** $f(2) = 4 - 6 + 1 = -1$ → $(2, -1)$

**Pendiente:** $f'(x) = 2x - 3$ → $f'(2) = 1$

**Tangente:**
$$y - (-1) = 1(x - 2)$$
$$y = x - 3$$

---

## 📊 Propiedades de linealidad

| Propiedad | Fórmula |
|-----------|---------|
| Suma | $(f + g)' = f' + g'$ |
| Resta | $(f - g)' = f' - g'$ |
| Múltiplo | $(cf)' = cf'$ |
| Combinación | $(af + bg)' = af' + bg'$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $f(x) = 4x^5 + 3x^3 - 2x + 7$
b) $g(x) = x^{-2} + x^{-1} + 1$
c) $h(x) = 2\sqrt{x} - 3x^{-1/2}$

<details>
<summary>Ver soluciones</summary>

a) $f'(x) = 20x^4 + 9x^2 - 2$

b) $g'(x) = -2x^{-3} - x^{-2} = -\frac{2}{x^3} - \frac{1}{x^2}$

c) $h'(x) = 2 \cdot \frac{1}{2}x^{-1/2} - 3 \cdot (-\frac{1}{2})x^{-3/2} = \frac{1}{\sqrt{x}} + \frac{3}{2x\sqrt{x}}$
</details>

---

**Ejercicio 2:** Simplifica y deriva:

$$
f(x) = \frac{x^4 - x^2 + x}{x}
$$

<details>
<summary>Ver solución</summary>

$$f(x) = x^3 - x + 1$$

$$f'(x) = 3x^2 - 1$$
</details>

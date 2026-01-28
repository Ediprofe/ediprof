---
title: "Regla del Producto"
---

# Regla del Producto

La derivada de un producto NO es el producto de las derivadas. La regla del producto nos dice cómo calcular correctamente $(fg)'$.

---

## 🎯 ¿Qué vas a aprender?

- La regla del producto
- Por qué $(fg)' \neq f' \cdot g'$
- Cómo aplicar la regla
- Extensión a productos de tres o más funciones

---

## 📖 La regla del producto

$$
\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)
$$

O en notación corta:

$$
(fg)' = f' g + f g'
$$

---

## 📖 Mnemotécnico

**"Primera derivada por segunda, más primera por segunda derivada"**

O: "Derivar una, dejar la otra, sumar."

---

## 📖 ¿Por qué no es $f' \cdot g'$?

Contraejemplo: Sea $f(x) = x$ y $g(x) = x$

- Producto: $fg = x^2$
- Derivada correcta: $(x^2)' = 2x$
- Si fuera $f' \cdot g' = 1 \cdot 1 = 1$ ← Incorrecto

Usando la regla del producto:
$$
(fg)' = 1 \cdot x + x \cdot 1 = 2x
$$ 

✓

---

## ⚙️ Ejemplo 1: Producto simple

Deriva $h(x) = x^2 \cdot e^x$

Sean $f = x^2$ y $g = e^x$

$$h'(x) = (2x)(e^x) + (x^2)(e^x)$$

$$= e^x(2x + x^2) = e^x \cdot x(2 + x)$$

---

## ⚙️ Ejemplo 2: Con polinomios

Deriva $f(x) = (3x + 1)(x^2 - 4)$

$$f'(x) = (3)(x^2 - 4) + (3x + 1)(2x)$$

$$= 3x^2 - 12 + 6x^2 + 2x$$

$$= 9x^2 + 2x - 12$$

**Verificación expandiendo primero:**
$$f(x) = 3x^3 - 12x + x^2 - 4 = 3x^3 + x^2 - 12x - 4$$
$$f'(x) = 9x^2 + 2x - 12$$ ✓

---

## ⚙️ Ejemplo 3: Con raíces

Deriva $g(x) = \sqrt{x} \cdot (x^2 + 1)$

$$g'(x) = \frac{1}{2\sqrt{x}}(x^2 + 1) + \sqrt{x}(2x)$$

$$= \frac{x^2 + 1}{2\sqrt{x}} + 2x\sqrt{x}$$

$$= \frac{x^2 + 1}{2\sqrt{x}} + 2x^{3/2}$$

Simplificando sobre un denominador común:
$$= \frac{x^2 + 1 + 4x^2}{2\sqrt{x}} = \frac{5x^2 + 1}{2\sqrt{x}}$$

---

## ⚙️ Ejemplo 4: Con tres factores

Deriva $h(x) = x \cdot \sin x \cdot \cos x$

La regla se extiende:
$$(fgh)' = f'gh + fg'h + fgh'$$

$$h'(x) = (1)(\sin x)(\cos x) + (x)(\cos x)(\cos x) + (x)(\sin x)(-\sin x)$$

$$= \sin x \cos x + x\cos^2 x - x\sin^2 x$$

$$= \sin x \cos x + x(\cos^2 x - \sin^2 x)$$

$$= \sin x \cos x + x\cos 2x$$

---

## 📖 Forma de Leibniz

En notación de Leibniz:

$$
\frac{d}{dx}[uv] = v\frac{du}{dx} + u\frac{dv}{dx}
$$

O simplemente: $d(uv) = v\,du + u\,dv$

---

## ⚙️ Ejemplo 5: Encontrar tangente

Encuentra la tangente a $f(x) = x \cdot \ln x$ en $x = 1$.

**Derivada:**
$$f'(x) = (1)(\ln x) + (x)\left(\frac{1}{x}\right) = \ln x + 1$$

**Pendiente en $x = 1$:**
$$f'(1) = \ln 1 + 1 = 0 + 1 = 1$$

**Punto:** $f(1) = 1 \cdot 0 = 0$ → $(1, 0)$

**Tangente:** $y - 0 = 1(x - 1)$ → $y = x - 1$

---

## 📊 Resumen

| Expresión | Derivada |
|-----------|----------|
| $fg$ | $f'g + fg'$ |
| $fgh$ | $f'gh + fg'h + fgh'$ |
| $cf \cdot g$ | $c(f'g + fg')$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $f(x) = x^3 \cdot 2^x$
b) $g(x) = (x^2 + 1)(x^3 - x)$

<details>
<summary>Ver soluciones</summary>

a) $f'(x) = 3x^2 \cdot 2^x + x^3 \cdot 2^x \ln 2 = 2^x(3x^2 + x^3 \ln 2)$

b) $g'(x) = 2x(x^3 - x) + (x^2 + 1)(3x^2 - 1)$
   
   $= 2x^4 - 2x^2 + 3x^4 - x^2 + 3x^2 - 1$
   
   $= 5x^4 - 1$
</details>

---

**Ejercicio 2:** Deriva $f(x) = (2x - 3)(x + 1)^2$ (pista: expande $(x+1)^2$ primero o usa producto de tres términos).

<details>
<summary>Ver solución</summary>

Opción 1: $(x+1)^2 = x^2 + 2x + 1$

$f(x) = (2x - 3)(x^2 + 2x + 1)$

$f'(x) = 2(x^2 + 2x + 1) + (2x - 3)(2x + 2)$

$= 2x^2 + 4x + 2 + 4x^2 + 4x - 6x - 6$

$= 6x^2 + 2x - 4$
</details>

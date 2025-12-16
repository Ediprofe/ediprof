# Derivadas Exponenciales

La función exponencial $e^x$ tiene una propiedad única: es su propia derivada. Esta propiedad hace que $e$ sea la base natural para el cálculo.

---

## 🎯 ¿Qué vas a aprender?

- Derivada de $e^x$ y por qué es especial
- Derivada de $a^x$ para cualquier base $a$
- Combinación con la regla de la cadena
- Aplicaciones

---

## 📖 La derivada más especial

$$
\boxed{\frac{d}{dx}[e^x] = e^x}
$$

**La función $e^x$ es su propia derivada.**

Esta propiedad define a $e \approx 2.71828...$

---

## 📖 Demostración (idea)

$$\frac{d}{dx}[e^x] = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h} = \lim_{h \to 0} \frac{e^x(e^h - 1)}{h}$$

$$= e^x \lim_{h \to 0} \frac{e^h - 1}{h}$$

El límite $\lim_{h \to 0} \frac{e^h - 1}{h} = 1$ (definición de $e$)

Por lo tanto: $\frac{d}{dx}[e^x] = e^x$

---

## 📖 Con la regla de la cadena

$$
\frac{d}{dx}[e^{u(x)}] = e^{u(x)} \cdot u'(x)
$$

La exponencial se mantiene y se multiplica por la derivada del exponente.

---

## ⚙️ Ejemplo 1: Exponencial simple

$$\frac{d}{dx}[e^x] = e^x$$

$$\frac{d}{dx}[5e^x] = 5e^x$$

$$\frac{d}{dx}[e^x + 3] = e^x$$

---

## ⚙️ Ejemplo 2: Con regla de la cadena

Deriva $f(x) = e^{3x}$

$$
f'(x) = e^{3x} \cdot 3 = 3e^{3x}
$$

---

## ⚙️ Ejemplo 3: Exponente cuadrático

Deriva $g(x) = e^{x^2}$

$$
g'(x) = e^{x^2} \cdot 2x = 2xe^{x^2}
$$

---

## ⚙️ Ejemplo 4: Exponente más complejo

Deriva $h(x) = e^{\sin x}$

$$
h'(x) = e^{\sin x} \cdot \cos x = \cos x \cdot e^{\sin x}
$$

---

## ⚙️ Ejemplo 5: Con otras reglas

Deriva $f(x) = x^2 e^x$

Usamos la regla del producto:

$$
f'(x) = 2x \cdot e^x + x^2 \cdot e^x = e^x(2x + x^2) = xe^x(2 + x)
$$

---

## 📖 Exponencial de base $a$

Para cualquier $a > 0$, $a \neq 1$:

$$
\boxed{\frac{d}{dx}[a^x] = a^x \ln a}
$$

**Nota:** Si $a = e$, entonces $\ln e = 1$ y recuperamos $\frac{d}{dx}[e^x] = e^x$.

---

## 📖 Demostración de $\frac{d}{dx}[a^x]$

Reescribimos $a^x = e^{x \ln a}$

$$
\frac{d}{dx}[a^x] = \frac{d}{dx}[e^{x \ln a}] = e^{x \ln a} \cdot \ln a = a^x \ln a
$$

---

## ⚙️ Ejemplo 6: Base 2

Deriva $f(x) = 2^x$

$$
f'(x) = 2^x \ln 2 \approx 0.693 \cdot 2^x
$$

---

## ⚙️ Ejemplo 7: Base 10

Deriva $g(x) = 10^x$

$$
g'(x) = 10^x \ln 10 \approx 2.303 \cdot 10^x
$$

---

## ⚙️ Ejemplo 8: Con cadena

Deriva $h(x) = 3^{2x}$

$$
h'(x) = 3^{2x} \cdot \ln 3 \cdot 2 = 2 \ln 3 \cdot 3^{2x}
$$

---

## 📖 Exponencial negativa

$$
\frac{d}{dx}[e^{-x}] = e^{-x} \cdot (-1) = -e^{-x}
$$

Útil en decaimiento exponencial.

---

## 📊 Resumen

| Función | Derivada |
|---------|----------|
| $e^x$ | $e^x$ |
| $e^{kx}$ | $ke^{kx}$ |
| $e^{u(x)}$ | $e^u \cdot u'$ |
| $a^x$ | $a^x \ln a$ |
| $a^{u(x)}$ | $a^u \cdot \ln a \cdot u'$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $e^{5x}$
b) $e^{-2x}$
c) $e^{x^3}$

<details>
<summary>Ver soluciones</summary>

a) $5e^{5x}$

b) $-2e^{-2x}$

c) $3x^2 e^{x^3}$
</details>

---

**Ejercicio 2:** Deriva:

$$
f(x) = \frac{e^x}{x}
$$

<details>
<summary>Ver solución</summary>

Usando la regla del cociente:

$$f'(x) = \frac{e^x \cdot x - e^x \cdot 1}{x^2} = \frac{e^x(x - 1)}{x^2}$$
</details>

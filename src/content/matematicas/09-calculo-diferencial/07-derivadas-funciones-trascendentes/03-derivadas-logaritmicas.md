# Derivadas Logarítmicas

Los logaritmos son las inversas de las exponenciales. Sus derivadas aparecen frecuentemente en problemas de tasas de cambio proporcionales.

---

## 🎯 ¿Qué vas a aprender?

- Derivada del logaritmo natural
- Derivada de logaritmo en cualquier base
- Aplicación con la regla de la cadena
- Patrones útiles

---

## 📖 Derivada del logaritmo natural

$$
\boxed{\frac{d}{dx}[\ln x] = \frac{1}{x}}
$$

Válida para $x > 0$.

---

## 📖 Demostración

Si $y = \ln x$, entonces $e^y = x$.

Derivando implícitamente: $e^y \frac{dy}{dx} = 1$

$$
\frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}
$$

---

## 📖 Con la regla de la cadena

$$
\frac{d}{dx}[\ln u] = \frac{1}{u} \cdot u' = \frac{u'}{u}
$$

"Derivada del argumento sobre el argumento."

---

## ⚙️ Ejemplo 1: Logaritmo simple

$$\frac{d}{dx}[\ln x] = \frac{1}{x}$$

$$\frac{d}{dx}[3\ln x] = \frac{3}{x}$$

---

## ⚙️ Ejemplo 2: Argumento lineal

Deriva $f(x) = \ln(3x)$

$$
f'(x) = \frac{1}{3x} \cdot 3 = \frac{3}{3x} = \frac{1}{x}
$$

**Interesante:** $\ln(3x) = \ln 3 + \ln x$, así que $(\ln 3 + \ln x)' = 0 + \frac{1}{x}$

---

## ⚙️ Ejemplo 3: Argumento cuadrático

Deriva $g(x) = \ln(x^2 + 1)$

$$
g'(x) = \frac{2x}{x^2 + 1}
$$

---

## ⚙️ Ejemplo 4: Con raíz

Deriva $h(x) = \ln(\sqrt{x}) = \ln(x^{1/2}) = \frac{1}{2}\ln x$

$$h'(x) = \frac{1}{2} \cdot \frac{1}{x} = \frac{1}{2x}$$

También por cadena: $\frac{1}{\sqrt{x}} \cdot \frac{1}{2\sqrt{x}} = \frac{1}{2x}$ ✓

---

## ⚙️ Ejemplo 5: Logaritmo de función trigonométrica

Deriva $f(x) = \ln(\sin x)$

$$
f'(x) = \frac{\cos x}{\sin x} = \cot x
$$

---

## 📖 Derivada de $\ln|x|$

$$
\frac{d}{dx}[\ln|x|] = \frac{1}{x}
$$

Válida para $x \neq 0$ (tanto positivo como negativo).

---

## 📖 Logaritmo de base $a$

$$
\log_a x = \frac{\ln x}{\ln a}
$$

Por lo tanto:

$$
\boxed{\frac{d}{dx}[\log_a x] = \frac{1}{x \ln a}}
$$

---

## ⚙️ Ejemplo 6: Logaritmo base 10

Deriva $f(x) = \log_{10} x$

$$
f'(x) = \frac{1}{x \ln 10} \approx \frac{0.434}{x}
$$

---

## ⚙️ Ejemplo 7: Logaritmo base 2

Deriva $g(x) = \log_2(x^2)$

$$
g'(x) = \frac{2x}{x^2 \ln 2} = \frac{2}{x \ln 2}
$$

También: $\log_2(x^2) = 2\log_2 x$, así que $g'(x) = \frac{2}{x \ln 2}$ ✓

---

## 📖 Patrón importante

$$
\frac{d}{dx}[\ln f(x)] = \frac{f'(x)}{f(x)}
$$

Este patrón es la base de la **derivación logarítmica**.

---

## ⚙️ Ejemplo 8: Producto con logaritmo

Deriva $h(x) = x \ln x$

$$
h'(x) = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1
$$

---

## 📊 Resumen

| Función | Derivada |
|---------|----------|
| $\ln x$ | $\frac{1}{x}$ |
| $\ln(ax)$ | $\frac{1}{x}$ |
| $\ln(u)$ | $\frac{u'}{u}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |
| $\log_a u$ | $\frac{u'}{u \ln a}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $\ln(5x)$
b) $\ln(x^3)$
c) $\ln(e^x)$

<details>
<summary>Ver soluciones</summary>

a) $\frac{5}{5x} = \frac{1}{x}$

b) $\frac{3x^2}{x^3} = \frac{3}{x}$ (o directamente: $3\ln x \to \frac{3}{x}$)

c) $\frac{e^x}{e^x} = 1$ (o directamente: $\ln(e^x) = x \to 1$)
</details>

---

**Ejercicio 2:** Deriva:

$$
f(x) = \frac{\ln x}{x}
$$

<details>
<summary>Ver solución</summary>

$$f'(x) = \frac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}$$
</details>

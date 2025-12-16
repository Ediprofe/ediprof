# Derivada de Constante y Regla de la Potencia

Las reglas de derivación nos permiten calcular derivadas sin usar la definición como límite cada vez. Comenzamos con las reglas más básicas: la constante y la potencia.

---

## 🎯 ¿Qué vas a aprender?

- Derivada de una constante
- Derivada de $x^n$ (regla de la potencia)
- Derivada de múltiplo constante
- Aplicaciones inmediatas

---

## 📖 Derivada de una constante

$$\frac{d}{dx}[c] = 0$$

La derivada de cualquier constante es cero.

**Interpretación:** Una constante no cambia, por lo tanto su razón de cambio es cero.

**Demostración:**
$$\lim_{h \to 0} \frac{c - c}{h} = \lim_{h \to 0} 0 = 0$$

---

## ⚙️ Ejemplos: Constantes

$$\frac{d}{dx}[5] = 0$$

$$\frac{d}{dx}[\pi] = 0$$

$$\frac{d}{dx}[-7] = 0$$

$$\frac{d}{dx}[e^2] = 0 \quad \text{(es un número fijo)}$$

---

## 📖 Regla de la potencia

$$\boxed{\frac{d}{dx}[x^n] = n \cdot x^{n-1}}$$

Esto funciona para **cualquier** $n$ real.

**Interpretación:** "Bajar el exponente y reducirlo en uno."

---

## ⚙️ Ejemplos: Potencias enteras positivas

$$\frac{d}{dx}[x] = \frac{d}{dx}[x^1] = 1 \cdot x^0 = 1$$

$$\frac{d}{dx}[x^2] = 2x^1 = 2x$$

$$\frac{d}{dx}[x^3] = 3x^2$$

$$\frac{d}{dx}[x^5] = 5x^4$$

$$\frac{d}{dx}[x^{100}] = 100x^{99}$$

---

## ⚙️ Ejemplos: Potencias negativas

$$\frac{d}{dx}[x^{-1}] = -1 \cdot x^{-2} = -\frac{1}{x^2}$$

$$\frac{d}{dx}\left[\frac{1}{x^2}\right] = \frac{d}{dx}[x^{-2}] = -2x^{-3} = -\frac{2}{x^3}$$

$$\frac{d}{dx}\left[\frac{1}{x^5}\right] = \frac{d}{dx}[x^{-5}] = -5x^{-6} = -\frac{5}{x^6}$$

---

## ⚙️ Ejemplos: Potencias fraccionarias (raíces)

$$\frac{d}{dx}[\sqrt{x}] = \frac{d}{dx}[x^{1/2}] = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$$

$$\frac{d}{dx}[\sqrt[3]{x}] = \frac{d}{dx}[x^{1/3}] = \frac{1}{3}x^{-2/3} = \frac{1}{3\sqrt[3]{x^2}}$$

$$\frac{d}{dx}[\sqrt[4]{x^3}] = \frac{d}{dx}[x^{3/4}] = \frac{3}{4}x^{-1/4} = \frac{3}{4\sqrt[4]{x}}$$

---

## 📖 Múltiplo constante

$$\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)$$

Las constantes "salen" de la derivada.

---

## ⚙️ Ejemplos: Múltiplo constante

$$\frac{d}{dx}[7x^3] = 7 \cdot 3x^2 = 21x^2$$

$$\frac{d}{dx}[4x^5] = 4 \cdot 5x^4 = 20x^4$$

$$\frac{d}{dx}\left[\frac{2}{x}\right] = 2 \cdot \frac{d}{dx}[x^{-1}] = 2(-1)x^{-2} = -\frac{2}{x^2}$$

$$\frac{d}{dx}[3\sqrt{x}] = 3 \cdot \frac{1}{2\sqrt{x}} = \frac{3}{2\sqrt{x}}$$

---

## 📊 Tabla resumen

| Función $f(x)$ | Derivada $f'(x)$ |
|----------------|------------------|
| $c$ | $0$ |
| $x$ | $1$ |
| $x^n$ | $nx^{n-1}$ |
| $cx^n$ | $cnx^{n-1}$ |
| $\frac{1}{x^n} = x^{-n}$ | $-nx^{-n-1}$ |
| $\sqrt{x} = x^{1/2}$ | $\frac{1}{2}x^{-1/2}$ |
| $\sqrt[n]{x} = x^{1/n}$ | $\frac{1}{n}x^{(1/n)-1}$ |

---

## ⚙️ Ejemplo completo

Deriva $f(x) = 4x^3 - 2x^2 + 5x - 7$

$$f'(x) = 4(3x^2) - 2(2x) + 5(1) - 0$$

$$f'(x) = 12x^2 - 4x + 5$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Deriva:

a) $f(x) = x^7$
b) $g(x) = 6x^4$
c) $h(x) = \frac{3}{x^2}$

<details>
<summary>Ver soluciones</summary>

a) $f'(x) = 7x^6$

b) $g'(x) = 24x^3$

c) $h(x) = 3x^{-2}$ → $h'(x) = -6x^{-3} = -\frac{6}{x^3}$
</details>

---

**Ejercicio 2:** Deriva:

$$f(x) = 5x^4 - 3x^2 + 2\sqrt{x} - \frac{1}{x}$$

<details>
<summary>Ver solución</summary>

$$f'(x) = 20x^3 - 6x + 2 \cdot \frac{1}{2}x^{-1/2} - (-1)x^{-2}$$

$$= 20x^3 - 6x + \frac{1}{\sqrt{x}} + \frac{1}{x^2}$$
</details>

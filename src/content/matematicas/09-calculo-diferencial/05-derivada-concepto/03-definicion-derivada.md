# Definición de Derivada

La derivada es el concepto central del cálculo diferencial. Formaliza la idea de razón de cambio instantánea y abre la puerta a innumerables aplicaciones.

---

## 🎯 ¿Qué vas a aprender?

- La definición formal de derivada
- Notaciones para la derivada
- Cómo calcular derivadas usando la definición
- Cuándo una función es derivable

---

## 📖 Definición formal

La **derivada de $f$ en $x = a$** se define como:

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
$$

siempre que este límite exista.

### Definición alternativa

$$
f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
$$

---

## 📖 La función derivada

La **función derivada** $f'(x)$ se define para todo $x$ donde el límite existe:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

$f'$ es una nueva función que da la pendiente de la tangente en cada punto.

---

## 📖 Notaciones

| Notación | Se lee |
|----------|--------|
| $f'(x)$ | "f prima de x" |
| $\frac{df}{dx}$ | "df sobre dx" o "derivada de f respecto a x" |
| $\frac{d}{dx}[f(x)]$ | "derivada de f(x) respecto a x" |
| $Df(x)$ | "D de f(x)" |
| $\dot{y}$ | "y punto" (usado en física) |

La notación $\frac{d}{dx}$ es de Leibniz y sugiere una "fracción" de cambios infinitesimales.

---

## ⚙️ Ejemplo 1: Derivada de $x^2$

Calculamos $f'(x)$ para $f(x) = x^2$ usando la definición:

$$f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h}$$

$$= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}$$

$$= \lim_{h \to 0} \frac{2xh + h^2}{h}$$

$$= \lim_{h \to 0} (2x + h) = 2x$$

$$
\boxed{f'(x) = 2x}
$$

---

## ⚙️ Ejemplo 2: Derivada de $x^3$

Para $f(x) = x^3$:

$$f'(x) = \lim_{h \to 0} \frac{(x + h)^3 - x^3}{h}$$

Usando $(x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$:

$$= \lim_{h \to 0} \frac{3x^2h + 3xh^2 + h^3}{h}$$

$$= \lim_{h \to 0} (3x^2 + 3xh + h^2) = 3x^2$$

$$
\boxed{f'(x) = 3x^2}
$$

---

## ⚙️ Ejemplo 3: Derivada de $\frac{1}{x}$

Para $f(x) = \frac{1}{x}$:

$$f'(x) = \lim_{h \to 0} \frac{\frac{1}{x+h} - \frac{1}{x}}{h}$$

$$= \lim_{h \to 0} \frac{\frac{x - (x+h)}{x(x+h)}}{h}$$

$$= \lim_{h \to 0} \frac{-h}{h \cdot x(x+h)}$$

$$= \lim_{h \to 0} \frac{-1}{x(x+h)} = \frac{-1}{x^2}$$

$$
\boxed{f'(x) = -\frac{1}{x^2}}
$$

---

## ⚙️ Ejemplo 4: Derivada de $\sqrt{x}$

Para $f(x) = \sqrt{x}$:

$$f'(x) = \lim_{h \to 0} \frac{\sqrt{x+h} - \sqrt{x}}{h}$$

Racionalizamos:

$$= \lim_{h \to 0} \frac{(\sqrt{x+h} - \sqrt{x})(\sqrt{x+h} + \sqrt{x})}{h(\sqrt{x+h} + \sqrt{x})}$$

$$= \lim_{h \to 0} \frac{(x+h) - x}{h(\sqrt{x+h} + \sqrt{x})}$$

$$= \lim_{h \to 0} \frac{h}{h(\sqrt{x+h} + \sqrt{x})}$$

$$= \lim_{h \to 0} \frac{1}{\sqrt{x+h} + \sqrt{x}} = \frac{1}{2\sqrt{x}}$$

$$
\boxed{f'(x) = \frac{1}{2\sqrt{x}}}
$$

---

## 📖 Derivabilidad

Una función es **derivable en $x = a$** si $f'(a)$ existe (el límite existe y es finito).

Una función es **derivable en un intervalo** si es derivable en cada punto del intervalo.

---

## 📖 Funciones no derivables

Una función puede no ser derivable si:

1. **No es continua** en el punto
2. **Tiene un "pico"** (punto anguloso)
3. **Tiene tangente vertical**

---

## ⚙️ Ejemplo 5: Pico en valor absoluto

$f(x) = |x|$ no es derivable en $x = 0$.

Por la izquierda: $\lim_{h \to 0^-} \frac{|h| - 0}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1$

Por la derecha: $\lim_{h \to 0^+} \frac{|h| - 0}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1$

Los límites laterales son diferentes → la derivada no existe en $x = 0$.

---

## 📊 Resumen de derivadas básicas

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $c$ (constante) | $0$ |
| $x$ | $1$ |
| $x^2$ | $2x$ |
| $x^3$ | $3x^2$ |
| $x^n$ | $nx^{n-1}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa la definición para calcular $f'(x)$ si $f(x) = 3x - 2$.

<details>
<summary>Ver solución</summary>

$$f'(x) = \lim_{h \to 0} \frac{3(x+h) - 2 - (3x - 2)}{h} = \lim_{h \to 0} \frac{3h}{h} = 3$$
</details>

---

**Ejercicio 2:** Usa la definición para calcular $f'(x)$ si $f(x) = x^2 + x$.

<details>
<summary>Ver solución</summary>

$$f'(x) = \lim_{h \to 0} \frac{(x+h)^2 + (x+h) - x^2 - x}{h}$$

$$= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 + x + h - x^2 - x}{h}$$

$$= \lim_{h \to 0} \frac{2xh + h^2 + h}{h} = \lim_{h \to 0} (2x + h + 1) = 2x + 1$$
</details>

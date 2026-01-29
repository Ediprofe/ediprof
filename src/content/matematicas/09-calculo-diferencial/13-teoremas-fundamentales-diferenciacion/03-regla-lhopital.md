# Regla de L'Hôpital

La Regla de L'Hôpital es una herramienta poderosa para calcular límites con formas indeterminadas. Transforma límites difíciles en límites más simples usando derivadas.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo aplicar la regla
- Forma $\frac{0}{0}$
- Forma $\frac{\infty}{\infty}$
- Otras formas indeterminadas

---

## 📖 Enunciado de la regla

> **Regla de L'Hôpital**
>
> Si $\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0$ (o ambos $\pm\infty$), y $\lim_{x \to a} \frac{f'(x)}{g'(x)}$ existe, entonces:
>
> $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

También vale para $x \to a^+$, $x \to a^-$, y $x \to \pm\infty$.

---

## 📖 Condiciones importantes

1. Debe ser forma indeterminada $\frac{0}{0}$ o $\frac{\infty}{\infty}$
2. Se derivan numerador y denominador **por separado** (NO es regla del cociente)
3. El límite del cociente de derivadas debe existir
4. Se puede aplicar repetidamente si es necesario

---

## ⚙️ Ejemplo 1: Forma $\frac{0}{0}$

$$\lim_{x \to 0} \frac{\sin x}{x}$$

**Verificar:** $\frac{0}{0}$ ✓

**Aplicar L'Hôpital:**
$$\lim_{x \to 0} \frac{\cos x}{1} = \frac{1}{1} = 1$$

---

## ⚙️ Ejemplo 2: Aplicar dos veces

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2}$$

**Primera aplicación:** $\frac{0}{0}$
$$\lim_{x \to 0} \frac{\sin x}{2x}$$

**Aún es $\frac{0}{0}$, segunda aplicación:**
$$\lim_{x \to 0} \frac{\cos x}{2} = \frac{1}{2}$$

---

## ⚙️ Ejemplo 3: Forma $\frac{\infty}{\infty}$

$$\lim_{x \to \infty} \frac{\ln x}{x}$$

**Verificar:** $\frac{\infty}{\infty}$ ✓

**L'Hôpital:**
$$\lim_{x \to \infty} \frac{1/x}{1} = \lim_{x \to \infty} \frac{1}{x} = 0$$

---

## ⚙️ Ejemplo 4: Exponencial vs polinomio

$$\lim_{x \to \infty} \frac{x^3}{e^x}$$

**$\frac{\infty}{\infty}$, aplicar 3 veces:**
$$\frac{3x^2}{e^x} \to \frac{6x}{e^x} \to \frac{6}{e^x} = 0$$

La exponencial crece más rápido que cualquier polinomio.

---

## 📖 Otras formas indeterminadas

Para formas que no son cocientes, convertir primero:

| Forma | Estrategia |
|-------|-----------|
| $0 \cdot \infty$ | Reescribir como $\frac{f}{1/g}$ |
| $\infty - \infty$ | Combinar en una fracción |
| $0^0$, $1^\infty$, $\infty^0$ | Usar $y = e^{\ln y}$ |

---

## ⚙️ Ejemplo 5: Forma $0 \cdot \infty$

$$\lim_{x \to 0^+} x \ln x$$

**Reescribir:**
$$\lim_{x \to 0^+} \frac{\ln x}{1/x} = \frac{-\infty}{\infty}$$

**L'Hôpital:**
$$\lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$$

---

## ⚙️ Ejemplo 6: Forma $\infty - \infty$

$$\lim_{x \to 0^+} \left(\frac{1}{x} - \frac{1}{\sin x}\right)$$

**Combinar:**
$$\lim_{x \to 0^+} \frac{\sin x - x}{x \sin x}$$

**$\frac{0}{0}$, L'Hôpital:**
$$\lim_{x \to 0^+} \frac{\cos x - 1}{\sin x + x\cos x}$$

**Aún $\frac{0}{0}$:**
$$\lim_{x \to 0^+} \frac{-\sin x}{\cos x + \cos x - x\sin x} = \frac{0}{2} = 0$$

---

## ⚙️ Ejemplo 7: Forma $1^\infty$

$$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$$

**Sea $y = \left(1 + \frac{1}{x}\right)^x$**

$$\ln y = x \ln\left(1 + \frac{1}{x}\right)$$

$$\lim_{x \to \infty} \ln y = \lim_{x \to \infty} \frac{\ln(1 + 1/x)}{1/x}$$

**$\frac{0}{0}$, L'Hôpital:**
$$\lim_{x \to \infty} \frac{\frac{-1/x^2}{1 + 1/x}}{-1/x^2} = \lim_{x \to \infty} \frac{1}{1 + 1/x} = 1$$

$$\ln y \to 1 \Rightarrow y \to e$$

---

## ⚠️ Errores comunes

1. **Aplicar cuando no es indeterminada:** $\frac{1}{0}$ NO es indeterminada
2. **Usar regla del cociente:** Se derivan por separado
3. **No verificar que el nuevo límite existe**
4. **Aplicar infinitamente:** A veces no ayuda

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

$$\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$$

<details>
<summary>Ver solución</summary>

$\frac{0}{0}$ → L'Hôpital: $\frac{e^x - 1}{2x}$

$\frac{0}{0}$ → L'Hôpital: $\frac{e^x}{2} = \frac{1}{2}$
</details>

---

**Ejercicio 2:** Calcula:

$$\lim_{x \to 0^+} x^x$$

<details>
<summary>Ver solución</summary>

$\ln y = x \ln x \to 0$ (del ejemplo 5)

$y \to e^0 = 1$
</details>

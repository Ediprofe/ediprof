---
title: "Asíntotas Verticales"
---

# Asíntotas Verticales

Las asíntotas verticales son líneas donde la función crece sin límite. Son el reflejo gráfico de los límites infinitos.

---

## 🎯 ¿Qué vas a aprender?

- Definición de asíntota vertical
- Cómo encontrar asíntotas verticales
- Comportamiento cerca de asíntotas
- Asíntotas de funciones comunes

---

## 📖 Definición

La recta $x = a$ es una **asíntota vertical** de $f(x)$ si al menos uno de los siguientes límites es $\pm\infty$:

$$
\lim_{x \to a^+} f(x) = \pm\infty \quad \text{o} \quad \lim_{x \to a^-} f(x) = \pm\infty
$$

La gráfica de la función se acerca a la recta pero nunca la toca (cerca de $a$).

---

## 📖 Cómo encontrar asíntotas verticales

### Para funciones racionales $\frac{P(x)}{Q(x)}$

1. Encontrar las raíces del denominador: $Q(x) = 0$
2. Verificar que el numerador **no** sea cero en esos puntos
3. Si $P(a) = 0$ también, simplificar y verificar de nuevo

### Para otras funciones

- **Logaritmos:** $\ln(g(x))$ tiene A.V. donde $g(x) = 0$
- **Tangente:** $\tan x$ tiene A.V. en $x = \frac{\pi}{2} + n\pi$
- **Raíces:** Pueden tener A.V. en extremos de dominio

---

## ⚙️ Ejemplo 1: Función racional simple

$$
f(x) = \frac{2}{x - 3}
$$

**Denominador = 0:** $x - 3 = 0 \Rightarrow x = 3$

**Numerador en $x = 3$:** $2 \neq 0$

**Asíntota vertical:** $x = 3$

**Comportamiento:**
$$
\lim_{x \to 3^+} \frac{2}{x-3} = \frac{2}{0^+} = +\infty
$$

$$
\lim_{x \to 3^-} \frac{2}{x-3} = \frac{2}{0^-} = -\infty
$$

---

## ⚙️ Ejemplo 2: Múltiples asíntotas

$$
g(x) = \frac{x}{x^2 - 4} = \frac{x}{(x-2)(x+2)}
$$

**Denominador = 0:** $x = 2$ y $x = -2$

**Numerador:** $2 \neq 0$ y $-2 \neq 0$

**Asíntotas verticales:** $x = 2$ y $x = -2$

---

## ⚙️ Ejemplo 3: Factor cancelable

$$
h(x) = \frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1}
$$

**Denominador = 0:** $x = 1$

**Simplificando:** $h(x) = x + 1$ para $x \neq 1$

**No hay asíntota vertical** en $x = 1$, hay un **hueco**.

$$
\lim_{x \to 1} h(x) = 2
$$

---

## ⚙️ Ejemplo 4: Con logaritmo

$$
f(x) = \ln(x - 2)
$$

**Argumento = 0:** $x - 2 = 0 \Rightarrow x = 2$

**Dominio:** $x > 2$

**Asíntota vertical:** $x = 2$

$$
\lim_{x \to 2^+} \ln(x - 2) = \ln(0^+) = -\infty
$$

---

## ⚙️ Ejemplo 5: Función tangente

$$
f(x) = \tan x = \frac{\sin x}{\cos x}
$$

**Denominador = 0:** $\cos x = 0 \Rightarrow x = \frac{\pi}{2} + n\pi$

**Asíntotas verticales:** $x = \pm\frac{\pi}{2}, \pm\frac{3\pi}{2}, \ldots$

---

## 📖 Comportamiento cerca de la asíntota

Una función puede acercarse a su asíntota de cuatro maneras:

| Por la izquierda | Por la derecha | Descripción |
|------------------|----------------|-------------|
| $+\infty$ | $+\infty$ | Ambos lados suben |
| $-\infty$ | $-\infty$ | Ambos lados bajan |
| $-\infty$ | $+\infty$ | Sube de izq. a der. |
| $+\infty$ | $-\infty$ | Baja de izq. a der. |

---

## ⚙️ Ejemplo 6: Análisis completo

$$
f(x) = \frac{x + 1}{(x - 2)^2}
$$

**Asíntota vertical:** $x = 2$

**Análisis:**
- Numerador en $x = 2$: $3 > 0$
- Denominador: $(x - 2)^2 > 0$ por ambos lados (cuadrado)

**Comportamiento:**
$$
\lim_{x \to 2^+} f(x) = \frac{3}{0^+} = +\infty
$$

$$
\lim_{x \to 2^-} f(x) = \frac{3}{0^+} = +\infty
$$

Ambos lados suben hacia $+\infty$.

---

## 📖 Criterio del exponente

Para $f(x) = \frac{g(x)}{(x-a)^n}$ donde $g(a) \neq 0$:

| $n$ | Comportamiento | Tipo de asíntota |
|-----|----------------|------------------|
| Par | Mismo signo ambos lados | Simétrica |
| Impar | Signos opuestos | Antisimétrica |

---

## 📊 Resumen

| Función | Asíntotas verticales |
|---------|---------------------|
| $\frac{1}{x-a}$ | $x = a$ |
| $\frac{1}{(x-a)(x-b)}$ | $x = a$, $x = b$ |
| $\ln(x-a)$ | $x = a$ |
| $\tan x$ | $x = \frac{\pi}{2} + n\pi$ |
| $\cot x$ | $x = n\pi$ |
| $\sec x$ | $x = \frac{\pi}{2} + n\pi$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra las asíntotas verticales:

a) $f(x) = \frac{x + 2}{x^2 - 9}$

b) $g(x) = \frac{x^2 - 4}{x - 2}$

<details>
<summary>Ver soluciones</summary>

a) $x^2 - 9 = 0 \Rightarrow x = \pm 3$
   
   Verificando: numerador no es cero en $\pm 3$
   
   **A.V.:** $x = 3$ y $x = -3$

b) $\frac{(x-2)(x+2)}{x-2} = x + 2$ para $x \neq 2$
   
   **No hay A.V.**, hay un hueco en $x = 2$
</details>

---

**Ejercicio 2:** Determina el comportamiento cerca de la asíntota:

$$
h(x) = \frac{5}{(x + 1)^3}
$$

<details>
<summary>Ver solución</summary>

A.V.: $x = -1$

Exponente impar → signos opuestos

$$
\lim_{x \to -1^+} = \frac{5}{0^+} = +\infty
$$

$$
\lim_{x \to -1^-} = \frac{5}{0^-} = -\infty
$$
</details>

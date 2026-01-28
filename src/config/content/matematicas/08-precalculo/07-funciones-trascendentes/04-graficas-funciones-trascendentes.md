---
title: "Gráficas de Funciones Trascendentes"
---

# Gráficas de Funciones Trascendentes

Las funciones exponenciales, logarítmicas y trigonométricas tienen gráficas características que debemos reconocer. Cada una tiene su forma distintiva y propiedades visuales únicas.

---

## 🎯 ¿Qué vas a aprender?

- Gráficas de funciones exponenciales y logarítmicas
- Gráficas de seno, coseno y tangente
- Transformaciones aplicadas
- Amplitud, período y fase

---

## 📖 Gráfica de $y = a^x$ (exponencial)

### Características para $a > 1$

- Pasa por $(0, 1)$
- Creciente de izquierda a derecha
- Asíntota horizontal: $y = 0$
- Rango: $(0, +\infty)$

### Características para $0 < a < 1$

- Pasa por $(0, 1)$
- Decreciente de izquierda a derecha
- Asíntota horizontal: $y = 0$
- Rango: $(0, +\infty)$

---

## 📖 Gráfica de $y = \log_a x$ (logarítmica)

### Características

- Pasa por $(1, 0)$
- Asíntota vertical: $x = 0$
- Dominio: $(0, +\infty)$
- Es la **reflexión** de $a^x$ respecto a $y = x$

| Base | Comportamiento |
|------|---------------|
| $a > 1$ | Creciente |
| $0 < a < 1$ | Decreciente |

---

## 📖 Gráficas de funciones trigonométricas

### $y = \sin x$

| Propiedad | Valor |
|-----------|-------|
| Período | $2\pi$ |
| Amplitud | $1$ |
| Máximo | $1$ (en $x = \frac{\pi}{2}$) |
| Mínimo | $-1$ (en $x = \frac{3\pi}{2}$) |
| Ceros | $x = n\pi$ ($n$ entero) |

**Forma:** Onda que empieza en el origen, sube hasta 1, baja hasta -1, y vuelve a 0.

### $y = \cos x$

| Propiedad | Valor |
|-----------|-------|
| Período | $2\pi$ |
| Amplitud | $1$ |
| Máximo | $1$ (en $x = 0$) |
| Mínimo | $-1$ (en $x = \pi$) |
| Ceros | $x = \frac{\pi}{2} + n\pi$ |

**Forma:** Igual que seno pero desplazado $\frac{\pi}{2}$ a la izquierda.

**Relación:** $\cos x = \sin\left(x + \frac{\pi}{2}\right)$

### $y = \tan x$

| Propiedad | Valor |
|-----------|-------|
| Período | $\pi$ |
| Amplitud | No definida (no acotada) |
| Asíntotas | $x = \frac{\pi}{2} + n\pi$ |
| Ceros | $x = n\pi$ |
| Rango | $\mathbb{R}$ |

**Forma:** Curvas en forma de S entre asíntotas verticales.

---

## 📖 Transformaciones de funciones sinusoidales

$$y = A \sin(B(x - C)) + D$$

| Parámetro | Nombre | Efecto |
|-----------|--------|--------|
| $A$ | Amplitud | $\|A\|$ = distancia del centro al máximo |
| $B$ | Frecuencia | Período $= \frac{2\pi}{\|B\|}$ |
| $C$ | Fase | Desplazamiento horizontal |
| $D$ | Desplazamiento vertical | Línea central |

---

## ⚙️ Ejemplo 1: Identificar parámetros

Analiza $y = 3\sin(2x - \pi) + 1$

**Paso 1:** Reescribimos en forma estándar
$$y = 3\sin\left(2\left(x - \frac{\pi}{2}\right)\right) + 1$$

**Parámetros:**
- Amplitud: $|A| = 3$
- Período: $\frac{2\pi}{|B|} = \frac{2\pi}{2} = \pi$
- Fase: $C = \frac{\pi}{2}$ (desplazamiento a la derecha)
- Desplazamiento vertical: $D = 1$

**Rango:** $[1 - 3, 1 + 3] = [-2, 4]$

---

## ⚙️ Ejemplo 2: Escribir la ecuación desde la gráfica

Una función sinusoidal tiene:
- Máximo en $y = 5$, mínimo en $y = -1$
- Período de $4\pi$
- Máximo en $x = 0$

**Paso 1:** Amplitud
$$A = \frac{\text{máx} - \text{mín}}{2} = \frac{5 - (-1)}{2} = 3$$

**Paso 2:** Desplazamiento vertical
$$D = \frac{\text{máx} + \text{mín}}{2} = \frac{5 + (-1)}{2} = 2$$

**Paso 3:** Frecuencia
$$\text{Período} = 4\pi \Rightarrow B = \frac{2\pi}{4\pi} = \frac{1}{2}$$

**Paso 4:** Fase
El máximo está en $x = 0$, lo cual corresponde al coseno.

**Ecuación:** $y = 3\cos\left(\frac{x}{2}\right) + 2$

---

## 📖 Comparación de gráficas

| Función | Dominio | Rango | Período |
|---------|---------|-------|---------|
| $e^x$ | $\mathbb{R}$ | $(0, +\infty)$ | — |
| $\ln x$ | $(0, +\infty)$ | $\mathbb{R}$ | — |
| $\sin x$ | $\mathbb{R}$ | $[-1, 1]$ | $2\pi$ |
| $\cos x$ | $\mathbb{R}$ | $[-1, 1]$ | $2\pi$ |
| $\tan x$ | $\mathbb{R} - \{\frac{\pi}{2} + n\pi\}$ | $\mathbb{R}$ | $\pi$ |

---

## ⚙️ Ejemplo 3: Transformación de exponencial

Grafica $y = -2^{x+1} + 3$

**Transformaciones desde $y = 2^x$:**
1. Desplazamiento 1 a la izquierda: $2^{x+1}$
2. Reflexión en eje X: $-2^{x+1}$
3. Desplazamiento 3 hacia arriba: $-2^{x+1} + 3$

**Asíntota horizontal:** $y = 3$

**Intercepto Y:** $y = -2^1 + 3 = 1$

**Comportamiento:** Decrece (por la reflexión) acercándose a $y = 3$ cuando $x \to -\infty$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Para $y = 4\cos(3x) - 2$, encuentra:

a) Amplitud
b) Período
c) Rango

<details>
<summary>Ver soluciones</summary>

a) Amplitud: $4$

b) Período: $\frac{2\pi}{3}$

c) Rango: $[-2 - 4, -2 + 4] = [-6, 2]$
</details>

---

**Ejercicio 2:** Identifica las asíntotas:

a) $y = \log(x - 3)$
b) $y = 2^x + 5$
c) $y = \tan(2x)$

<details>
<summary>Ver soluciones</summary>

a) Asíntota vertical: $x = 3$

b) Asíntota horizontal: $y = 5$

c) Asíntotas verticales: $x = \frac{\pi}{4} + \frac{n\pi}{2}$ (para todo entero $n$)
</details>

---

**Ejercicio 3:** Escribe la ecuación de una función seno con:
- Amplitud 2
- Período $\pi$
- Desplazamiento vertical 3

<details>
<summary>Ver solución</summary>

Período $= \frac{2\pi}{B} = \pi \Rightarrow B = 2$

$$y = 2\sin(2x) + 3$$
</details>

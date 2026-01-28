---
title: "Teorema del Valor Intermedio"
---

# Teorema del Valor Intermedio

El Teorema del Valor Intermedio (TVI) es uno de los resultados más poderosos sobre funciones continuas. Garantiza que una función continua "no puede saltar" sobre ningún valor.

---

## 🎯 ¿Qué vas a aprender?

- El enunciado del TVI
- Aplicaciones para encontrar raíces
- El método de bisección
- Demostraciones de existencia

---

## 📖 Enunciado del Teorema

> **Teorema del Valor Intermedio (TVI)**
>
> Si $f$ es continua en $[a, b]$ y $k$ es cualquier valor entre $f(a)$ y $f(b)$, entonces existe al menos un $c \in (a, b)$ tal que $f(c) = k$.

En símbolos:

$$
f \text{ continua en } [a, b], \quad f(a) < k < f(b) \quad \Rightarrow \quad \exists c \in (a, b): f(c) = k
$$

---

## 📖 Interpretación gráfica

Si trazas una gráfica continua desde el punto $(a, f(a))$ hasta $(b, f(b))$, la curva **debe cruzar** toda línea horizontal entre $f(a)$ y $f(b)$.

No puedes ir de un valor a otro sin pasar por los valores intermedios.

---

## 📖 Caso especial: Teorema de Bolzano

Si $f$ es continua en $[a, b]$ y $f(a)$ y $f(b)$ tienen **signos opuestos**:

$$
f(a) \cdot f(b) < 0
$$

Entonces existe al menos un $c \in (a, b)$ tal que $f(c) = 0$.

**La función tiene al menos una raíz en $(a, b)$.**

---

## ⚙️ Ejemplo 1: Existencia de raíz

Demuestra que $f(x) = x^3 - x - 1$ tiene una raíz en $[1, 2]$.

**Verificamos continuidad:** $f$ es un polinomio → continua en $\mathbb{R}$

**Evaluamos en los extremos:**
- $f(1) = 1 - 1 - 1 = -1 < 0$
- $f(2) = 8 - 2 - 1 = 5 > 0$

**Signos opuestos:** $f(1) \cdot f(2) = (-1)(5) < 0$

Por el Teorema de Bolzano, existe $c \in (1, 2)$ tal que $f(c) = 0$.

---

## ⚙️ Ejemplo 2: Encontrar una raíz

Demuestra que $\cos x = x$ tiene solución en $(0, 1)$.

Definimos $g(x) = \cos x - x$

**Evaluamos:**
- $g(0) = \cos(0) - 0 = 1 > 0$
- $g(1) = \cos(1) - 1 \approx 0.54 - 1 = -0.46 < 0$

Por el TVI, existe $c \in (0, 1)$ tal que $\cos c = c$.

---

## 📖 Método de bisección

El TVI nos da un algoritmo para aproximar raíces:

### Pasos

1. Encontrar $[a, b]$ donde $f(a) \cdot f(b) < 0$
2. Calcular el punto medio $m = \frac{a + b}{2}$
3. Evaluar $f(m)$
4. Si $f(m) = 0$ (o suficientemente pequeño), terminamos
5. Si $f(a) \cdot f(m) < 0$, la raíz está en $[a, m]$
6. Si $f(m) \cdot f(b) < 0$, la raíz está en $[m, b]$
7. Repetir con el nuevo intervalo

---

## ⚙️ Ejemplo 3: Método de bisección

Aproximar la raíz de $f(x) = x^3 - x - 1$ en $[1, 2]$.

**Iteración 1:**
- $m = 1.5$
- $f(1.5) = 3.375 - 1.5 - 1 = 0.875 > 0$
- $f(1) < 0$, $f(1.5) > 0$ → raíz en $[1, 1.5]$

**Iteración 2:**
- $m = 1.25$
- $f(1.25) = 1.953 - 1.25 - 1 = -0.297 < 0$
- $f(1.25) < 0$, $f(1.5) > 0$ → raíz en $[1.25, 1.5]$

**Iteración 3:**
- $m = 1.375$
- $f(1.375) \approx 0.224 > 0$
- Raíz en $[1.25, 1.375]$

Continuando: $c \approx 1.3247...$

---

## ⚙️ Ejemplo 4: Problema de existencia

Una persona pesa 50 kg a los 10 años y 70 kg a los 20 años. Demuestra que en algún momento pesó exactamente 60 kg.

**Modelamos:** Sea $P(t)$ el peso en función de la edad.

- $P(10) = 50$
- $P(20) = 70$
- $P$ es continua (el peso no cambia instantáneamente)
- $60$ está entre $50$ y $70$

Por el TVI, existe $c \in (10, 20)$ tal que $P(c) = 60$ kg.

---

## ⚙️ Ejemplo 5: Ecuación trascendente

Demuestra que $e^x + x = 2$ tiene exactamente una solución.

**Existencia:** Sea $f(x) = e^x + x - 2$
- $f(0) = 1 + 0 - 2 = -1 < 0$
- $f(1) = e + 1 - 2 \approx 1.72 > 0$

Por TVI, hay al menos una raíz en $(0, 1)$.

**Unicidad:** $f'(x) = e^x + 1 > 0$ siempre.

$f$ es estrictamente creciente → a lo más una raíz.

**Conclusión:** Exactamente una solución.

---

## 📖 Limitaciones del TVI

El TVI garantiza **existencia** pero no:
- **Unicidad:** Puede haber múltiples raíces
- **Ubicación exacta:** Solo sabemos que está en el intervalo
- **Cómo encontrarla:** Solo dice que existe

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa el TVI para demostrar que la ecuación tiene solución en el intervalo dado:

a) $x^5 - 3x + 1 = 0$ en $[0, 1]$

b) $\ln x = 2 - x$ en $[1, 2]$

<details>
<summary>Ver soluciones</summary>

a) $f(x) = x^5 - 3x + 1$
   - $f(0) = 1 > 0$
   - $f(1) = 1 - 3 + 1 = -1 < 0$
   
   Signos opuestos → hay raíz en $(0, 1)$

b) $g(x) = \ln x - 2 + x$
   - $g(1) = 0 - 2 + 1 = -1 < 0$
   - $g(2) = \ln 2 - 2 + 2 = \ln 2 \approx 0.69 > 0$
   
   Hay raíz en $(1, 2)$
</details>

---

**Ejercicio 2:** Demuestra que toda ecuación $x^n = c$ ($c > 0$, $n$ impar) tiene solución real.

<details>
<summary>Ver solución</summary>

Sea $f(x) = x^n - c$

- $f(0) = -c < 0$
- Para $x$ suficientemente grande: $f(x) = x^n - c > 0$

Por el TVI, existe $c^{1/n} > 0$.

Para $x < 0$: $f(x) \to -\infty$ cuando $x \to -\infty$ (n impar)

También hay raíz negativa cuando $c < 0$.
</details>

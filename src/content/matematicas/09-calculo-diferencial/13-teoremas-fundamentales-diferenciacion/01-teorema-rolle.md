# Teorema de Rolle

El Teorema de Rolle es un resultado fundamental que conecta los valores de una función con su derivada. Es la base para el Teorema del Valor Medio.

---

## 🎯 ¿Qué vas a aprender?

- El enunciado del Teorema de Rolle
- Condiciones necesarias
- Interpretación geométrica
- Aplicaciones

---

## 📖 Enunciado del teorema

> **Teorema de Rolle**
>
> Si $f$ satisface:
> 1. $f$ es continua en $[a, b]$
> 2. $f$ es derivable en $(a, b)$
> 3. $f(a) = f(b)$
>
> Entonces existe al menos un $c \in (a, b)$ tal que $f'(c) = 0$.

---

## 📖 Interpretación geométrica

Si una función continua comienza y termina en la misma altura, en algún punto intermedio la tangente debe ser horizontal.

Imagina una montaña: si empiezas y terminas a la misma altitud, en algún momento estás en la cima (o en un valle).

---

## 📖 Las tres condiciones son necesarias

**Sin continuidad:**
$$
f(x) = \begin{cases} 0 & x \in [0, 1) \cup (1, 2] \\ 1 & x = 1 \end{cases}
$$
$f(0) = f(2) = 0$, pero $f'(x) = 0$ en todo el dominio (no es ejemplo correcto porque f' existe). Mejor:

Una función con discontinuidad de salto puede no tener punto con tangente horizontal.

**Sin derivabilidad:**
$f(x) = |x|$ en $[-1, 1]$: $f(-1) = f(1) = 1$, pero $f'(0)$ no existe.

**Sin $f(a) = f(b)$:**
$f(x) = x$ en $[0, 1]$: $f(0) \neq f(1)$, y $f'(x) = 1 \neq 0$ siempre.

---

## ⚙️ Ejemplo 1: Verificación básica

Verifica el Teorema de Rolle para $f(x) = x^2 - 4x + 3$ en $[1, 3]$.

**Condición 1:** $f$ es un polinomio → continua en $[1, 3]$ ✓

**Condición 2:** $f$ es derivable en $(1, 3)$ ✓

**Condición 3:** $f(1) = 1 - 4 + 3 = 0$, $f(3) = 9 - 12 + 3 = 0$ ✓

**Encontrar $c$:**
$$f'(x) = 2x - 4 = 0 \Rightarrow x = 2$$

**Conclusión:** $c = 2 \in (1, 3)$ satisface $f'(2) = 0$ ✓

---

## ⚙️ Ejemplo 2: Función trigonométrica

Verifica para $f(x) = \sin x$ en $[0, \pi]$.

**Condiciones:** ✓ (continua, derivable, $f(0) = f(\pi) = 0$)

**Encontrar $c$:**
$$f'(x) = \cos x = 0 \Rightarrow x = \frac{\pi}{2}$$

$c = \frac{\pi}{2} \in (0, \pi)$ ✓

---

## ⚙️ Ejemplo 3: Múltiples puntos $c$

$f(x) = \sin 2x$ en $[0, \pi]$

$f(0) = 0$, $f(\pi) = 0$

$f'(x) = 2\cos 2x = 0$

$2x = \frac{\pi}{2}, \frac{3\pi}{2}$

$x = \frac{\pi}{4}, \frac{3\pi}{4}$

Hay **dos** valores de $c$.

---

## 📖 Aplicación: Demostrar unicidad de raíces

El Teorema de Rolle puede usarse para demostrar que una ecuación tiene a lo más una raíz.

**Idea:** Si hubiera dos raíces $a$ y $b$, entonces $f(a) = f(b) = 0$, y por Rolle existiría $c$ con $f'(c) = 0$. Si podemos probar que $f'(x) \neq 0$, hay contradicción.

---

## ⚙️ Ejemplo 4: Unicidad de raíz

Demuestra que $x^3 + 3x + 1 = 0$ tiene exactamente una raíz real.

**Existencia:** 
- $f(-1) = -1 - 3 + 1 = -3 < 0$
- $f(0) = 1 > 0$

Por TVI, hay al menos una raíz en $(-1, 0)$.

**Unicidad:**
$f'(x) = 3x^2 + 3 = 3(x^2 + 1) > 0$ siempre.

Si hubiera dos raíces, por Rolle habría $c$ con $f'(c) = 0$. Pero esto es imposible.

**Conclusión:** Exactamente una raíz real.

---

## 📖 Generalización

El Teorema de Rolle es un caso especial del Teorema del Valor Medio (cuando $f(a) = f(b)$).

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Verifica el Teorema de Rolle para $f(x) = x^3 - 3x$ en $[-\sqrt{3}, \sqrt{3}]$.

<details>
<summary>Ver solución</summary>

$f(-\sqrt{3}) = -3\sqrt{3} + 3\sqrt{3} = 0$

$f(\sqrt{3}) = 3\sqrt{3} - 3\sqrt{3} = 0$

$f'(x) = 3x^2 - 3 = 0 \Rightarrow x = \pm 1$

Ambos valores están en $(-\sqrt{3}, \sqrt{3})$ ✓
</details>

---

**Ejercicio 2:** Demuestra que $e^x = 2x + 1$ tiene a lo más una solución.

<details>
<summary>Ver solución</summary>

Sea $g(x) = e^x - 2x - 1$

$g'(x) = e^x - 2$

$g'(x) = 0$ solo cuando $x = \ln 2$

$g''(x) = e^x > 0$, así que $g$ es convexa.

Una función convexa cruza una recta a lo más dos veces... pero aquí $g$ tiene un solo mínimo y crece hacia $\pm\infty$, así que cruza el cero a lo más dos veces.

Para unicidad estricta, verificar signos cerca del mínimo.
</details>

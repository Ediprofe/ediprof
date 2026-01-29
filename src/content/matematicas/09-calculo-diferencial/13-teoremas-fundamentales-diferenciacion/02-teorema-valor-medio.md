# Teorema del Valor Medio

El Teorema del Valor Medio (TVM) generaliza el Teorema de Rolle y es uno de los resultados más importantes del cálculo diferencial.

---

## 🎯 ¿Qué vas a aprender?

- El enunciado del TVM
- Interpretación geométrica
- Consecuencias importantes
- Aplicaciones

---

## 📖 Enunciado del teorema

> **Teorema del Valor Medio (Lagrange)**
>
> Si $f$ es continua en $[a, b]$ y derivable en $(a, b)$, entonces existe $c \in (a, b)$ tal que:
>
> $$f'(c) = \frac{f(b) - f(a)}{b - a}$$

---

## 📖 Interpretación geométrica

La pendiente de la tangente en algún punto $c$ es igual a la pendiente de la secante que une los extremos.

En otras palabras: en algún momento, la velocidad instantánea iguala a la velocidad promedio.

---

## 📖 Relación con Rolle

Si $f(a) = f(b)$, entonces $\frac{f(b) - f(a)}{b - a} = 0$, y el TVM dice que existe $c$ con $f'(c) = 0$.

El Teorema de Rolle es un caso particular del TVM.

---

## ⚙️ Ejemplo 1: Verificación

Verifica el TVM para $f(x) = x^3 - x$ en $[0, 2]$.

**Condiciones:** Polinomio → continua y derivable ✓

**Pendiente de la secante:**
$$\frac{f(2) - f(0)}{2 - 0} = \frac{(8-2) - 0}{2} = \frac{6}{2} = 3$$

**Encontrar $c$:**
$$f'(x) = 3x^2 - 1 = 3$$
$$3x^2 = 4$$
$$x = \frac{2}{\sqrt{3}} \approx 1.15$$

Este valor está en $(0, 2)$ ✓

---

## ⚙️ Ejemplo 2: Aplicación física

Un auto viaja 200 km en 2 horas. Demuestra que en algún momento viajaba exactamente a 100 km/h.

**Modelamos:** $s(t)$ = posición, $s(0) = 0$, $s(2) = 200$

**Velocidad promedio:** $\frac{200 - 0}{2 - 0} = 100$ km/h

**Por el TVM:** Existe $c \in (0, 2)$ tal que $s'(c) = 100$ km/h ✓

---

## 📖 Consecuencias del TVM

### 1. Funciones con derivada cero

Si $f'(x) = 0$ para todo $x$ en un intervalo, entonces $f$ es constante.

**Demostración:** Para cualesquiera $a < b$, por TVM:
$$f(b) - f(a) = f'(c)(b - a) = 0$$
Entonces $f(b) = f(a)$.

### 2. Funciones con la misma derivada

Si $f'(x) = g'(x)$ para todo $x$, entonces $f(x) = g(x) + C$.

### 3. Cota para el crecimiento

Si $|f'(x)| \leq M$ para todo $x$ en $[a, b]$:
$$|f(b) - f(a)| \leq M|b - a|$$

---

## ⚙️ Ejemplo 3: Estimar valores

Si $f(2) = 5$ y $f'(x) \leq 3$ para todo $x$, estima el valor máximo de $f(4)$.

Por el TVM: $f(4) - f(2) = f'(c)(4 - 2)$ para algún $c \in (2, 4)$

Como $f'(c) \leq 3$:
$$f(4) - 5 \leq 3 \cdot 2 = 6$$
$$f(4) \leq 11$$

---

## ⚙️ Ejemplo 4: Desigualdad

Demuestra que $\sin x < x$ para todo $x > 0$.

Sea $f(x) = x - \sin x$.

$f(0) = 0$ y $f'(x) = 1 - \cos x \geq 0$

Por el TVM aplicado a $[0, x]$:
$$f(x) - f(0) = f'(c) \cdot x > 0$$ para $x > 0$ (ya que $f'(c) \geq 0$ y es estrictamente positivo excepto en puntos aislados)

Por lo tanto $f(x) > 0$, es decir, $x > \sin x$.

---

## 📖 Teorema del Valor Medio de Cauchy

Generalización cuando ambas funciones cambian:

Si $f$ y $g$ son continuas en $[a, b]$, derivables en $(a, b)$, y $g'(x) \neq 0$:

$$\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}$$

para algún $c \in (a, b)$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el valor de $c$ que satisface el TVM para $f(x) = \sqrt{x}$ en $[1, 4]$.

<details>
<summary>Ver solución</summary>

$\frac{f(4) - f(1)}{4 - 1} = \frac{2 - 1}{3} = \frac{1}{3}$

$f'(x) = \frac{1}{2\sqrt{x}} = \frac{1}{3}$

$\sqrt{x} = \frac{3}{2}$

$x = \frac{9}{4} = 2.25$

$c = 2.25 \in (1, 4)$ ✓
</details>

---

**Ejercicio 2:** Si $f''(x) > 0$ para todo $x$, demuestra que:

$$f\left(\frac{a+b}{2}\right) < \frac{f(a) + f(b)}{2}$$

(La función está por debajo de la secante)

<details>
<summary>Ver solución</summary>

Esto es la definición de función convexa. Se demuestra usando TVM dos veces: de $a$ al punto medio y del punto medio a $b$, mostrando que la pendiente aumenta.
</details>

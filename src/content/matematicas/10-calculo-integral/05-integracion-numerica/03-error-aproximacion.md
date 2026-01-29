# Error de Aproximación

Conocer el error de los métodos numéricos nos permite elegir el número de subdivisiones necesarias para alcanzar una precisión deseada.

---

## 🎯 ¿Qué vas a aprender?

- Cotas de error para cada método
- Cómo determinar $n$ para precisión deseada
- Comparación de eficiencia
- Ejemplos prácticos

---

## 📖 Cotas de error

### Método del punto medio

$$
|E_M| \leq \frac{(b-a)^3}{24n^2} \cdot M_2
$$

### Método del trapecio

$$
|E_T| \leq \frac{(b-a)^3}{12n^2} \cdot M_2
$$

### Regla de Simpson

$$
|E_S| \leq \frac{(b-a)^5}{180n^4} \cdot M_4
$$

donde $M_k = \max_{a \leq x \leq b} |f^{(k)}(x)|$

---

## 📖 Observaciones

- El error del trapecio es aproximadamente **el doble** del punto medio
- Simpson es mucho más preciso para el mismo $n$
- Para reducir el error a la mitad:
  - Trapecio: duplicar $n$ (cuádruple de trabajo)
  - Simpson: multiplicar $n$ por $\sqrt[4]{2} \approx 1.19$

---

## ⚙️ Ejemplo 1: Estimar error

Para $\int_0^1 e^x\,dx$ con método del trapecio y $n = 10$:

$f(x) = e^x$, $f''(x) = e^x$

$M_2 = \max_{[0,1]} e^x = e \approx 2.718$

$$
|E_T| \leq \frac{1^3}{12(10)^2} \cdot 2.718 = \frac{2.718}{1200} \approx 0.00226
$$

---

## ⚙️ Ejemplo 2: Determinar n necesario

¿Cuántos subintervalos usar para que el error del trapecio sea menor que $0.0001$ en $\int_1^2 \frac{1}{x}\,dx$?

$f(x) = \frac{1}{x}$, $f''(x) = \frac{2}{x^3}$

$M_2 = \max_{[1,2]} \frac{2}{x^3} = 2$ (en $x = 1$)

$$
\frac{(2-1)^3}{12n^2} \cdot 2 < 0.0001
$$

$$
\frac{1}{6n^2} < 0.0001
$$

$$
n^2 > \frac{1}{0.0006} \approx 1667
$$

$$
n > 41
$$

Se necesitan al menos **42 subintervalos**.

---

## ⚙️ Ejemplo 3: Simpson vs Trapecio

Para la misma integral con Simpson:

$f^{(4)}(x) = \frac{24}{x^5}$, $M_4 = 24$

$$
\frac{1^5}{180n^4} \cdot 24 < 0.0001
$$

$$
n^4 > \frac{24}{0.018} \approx 1333
$$

$$
n > 6
$$

¡Solo se necesitan **8 subintervalos** (par más cercano)!

---

## 📖 Eficiencia relativa

| Para error $10^{-6}$ | Trapecio | Simpson |
|---------------------|----------|---------|
| $n$ necesario | ~1000 | ~20 |
| Evaluaciones de $f$ | ~1000 | ~20 |

Simpson es dramáticamente más eficiente para funciones suaves.

---

## 📖 Extrapolación de Richardson

Si calculamos $T_{2n}$ y $T_n$, podemos mejorar la estimación:

$$
\text{Mejor} \approx T_{2n} + \frac{T_{2n} - T_n}{3}
$$

Este es el fundamento del método de Romberg.

---

## ⚙️ Ejemplo 4: Verificación numérica

Para $\int_0^1 x^2\,dx = \frac{1}{3}$:

| $n$ | $T_n$ | Error |
|-----|-------|-------|
| 4 | 0.34375 | 0.01042 |
| 8 | 0.33594 | 0.00260 |
| 16 | 0.33398 | 0.00065 |

El error se reduce aproximadamente por 4 al duplicar $n$ (como predice la teoría: $1/n^2$).

---

## 📖 Cuándo usar cada método

| Situación | Método recomendado |
|-----------|-------------------|
| $f$ suave, alta precisión | Simpson |
| $f$ con discontinuidades en derivadas | Trapecio adaptativo |
| Datos tabulados (sin fórmula) | Trapecio |
| Precisión extrema | Cuadratura de Gauss |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Cuántos intervalos necesita Simpson para calcular $\int_0^{\pi} \sin x\,dx$ con error menor que $10^{-8}$?

<details>
<summary>Ver solución</summary>

$f^{(4)}(x) = \sin x$, $M_4 = 1$

$$
\frac{\pi^5}{180n^4} < 10^{-8}
$$

$$
n^4 > \frac{\pi^5 \cdot 10^8}{180} \approx 1.7 \times 10^6
$$

$$
n > 36
$$

$n = 38$ (par más cercano)
</details>

---

**Ejercicio 2:** Si $T_4 = 0.7828$ y $T_8 = 0.7471$ para cierta integral, estima el valor usando extrapolación de Richardson.

<details>
<summary>Ver solución</summary>

$$
\text{Mejor} \approx T_8 + \frac{T_8 - T_4}{3} = 0.7471 + \frac{0.7471 - 0.7828}{3}
$$

$$
= 0.7471 - 0.0119 = 0.7352
$$
</details>

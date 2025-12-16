# Volúmenes por Capas Cilíndricas

El método de capas (o cascarones) usa cilindros concéntricos en lugar de discos. Es especialmente útil cuando el eje de rotación es paralelo al eje de la variable de integración.

---

## 🎯 ¿Qué vas a aprender?

- El método de capas cilíndricas
- Cuándo preferir capas sobre discos
- Revolución alrededor del eje y
- Ejes desplazados

---

## 📖 La idea

Imaginamos la región como capas cilíndricas concéntricas, como las capas de una cebolla.

Cada capa tiene:
- Radio: $r$
- Altura: $h$
- Espesor: $dx$
- Volumen: $2\pi r \cdot h \cdot dx$

---

## 📖 Fórmula (eje y)

Al rotar alrededor del eje y, integrando en x:

$$\boxed{V = 2\pi\int_a^b x \cdot f(x)\,dx}$$

- $x$ = radio de la capa
- $f(x)$ = altura de la capa

---

## ⚙️ Ejemplo 1: Básico

Rotar $y = x^2$ de $x = 0$ a $x = 2$ alrededor del eje y.

$$V = 2\pi\int_0^2 x \cdot x^2\,dx = 2\pi\int_0^2 x^3\,dx$$

$$= 2\pi\left[\frac{x^4}{4}\right]_0^2 = 2\pi \cdot 4 = 8\pi$$

---

## ⚙️ Ejemplo 2: Comparación con discos

Mismo problema por discos:

$x = \sqrt{y}$ de $y = 0$ a $y = 4$

$$V = \pi\int_0^4 y\,dy = \pi \cdot 8 = 8\pi$$ ✓

¡Mismo resultado!

---

## ⚙️ Ejemplo 3: Región entre curvas

Rotar la región entre $y = x$ y $y = x^2$ (de $x = 0$ a $x = 1$) alrededor del eje y.

$$V = 2\pi\int_0^1 x(x - x^2)\,dx = 2\pi\int_0^1 (x^2 - x^3)\,dx$$

$$= 2\pi\left[\frac{x^3}{3} - \frac{x^4}{4}\right]_0^1 = 2\pi\left(\frac{1}{3} - \frac{1}{4}\right) = \frac{\pi}{6}$$

---

## 📖 Fórmula (eje x)

Al rotar alrededor del eje x, integrando en y:

$$V = 2\pi\int_c^d y \cdot g(y)\,dy$$

---

## ⚙️ Ejemplo 4: Alrededor del eje x

Rotar $y = \sqrt{x}$ (de $y = 0$ a $y = 2$) alrededor del eje x.

$x = y^2$

$$V = 2\pi\int_0^2 y \cdot y^2\,dy = 2\pi\int_0^2 y^3\,dy$$

$$= 2\pi\left[\frac{y^4}{4}\right]_0^2 = 2\pi \cdot 4 = 8\pi$$

---

## 📖 Eje desplazado

Para rotar alrededor de $x = c$:

$$V = 2\pi\int_a^b |x - c| \cdot f(x)\,dx$$

El radio es la distancia al eje de rotación.

---

## ⚙️ Ejemplo 5: Alrededor de $x = -1$

Rotar $y = x^2$ de $x = 0$ a $x = 1$ alrededor de $x = -1$.

Radio = $x - (-1) = x + 1$

$$V = 2\pi\int_0^1 (x + 1) \cdot x^2\,dx = 2\pi\int_0^1 (x^3 + x^2)\,dx$$

$$= 2\pi\left[\frac{x^4}{4} + \frac{x^3}{3}\right]_0^1 = 2\pi\left(\frac{1}{4} + \frac{1}{3}\right) = \frac{7\pi}{6}$$

---

## 📖 ¿Cuándo usar capas?

| Situación | Método preferido |
|-----------|-----------------|
| Rotación eje x, función $y = f(x)$ | Discos (en x) |
| Rotación eje y, función $y = f(x)$ | Capas (en x) o Discos (en y) |
| Difícil despejar $x$ | Capas |
| Región con hueco | Arandelas o Capas |

---

## ⚙️ Ejemplo 6: Caso donde capas es mejor

Rotar la región bajo $y = \sin(x^2)$ de $x = 0$ a $x = \sqrt{\pi}$ alrededor del eje y.

Por capas:
$$V = 2\pi\int_0^{\sqrt{\pi}} x\sin(x^2)\,dx$$

$u = x^2$, $du = 2x\,dx$:
$$= \pi\int_0^{\pi} \sin u\,du = \pi[-\cos u]_0^{\pi} = \pi(1 + 1) = 2\pi$$

¡Por discos sería muy difícil!

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa capas para rotar $y = e^{-x^2}$ de $x = 0$ a $x = 1$ alrededor del eje y.

<details>
<summary>Ver solución</summary>

$V = 2\pi\int_0^1 xe^{-x^2}\,dx$

$u = -x^2$, $du = -2x\,dx$

$= -\pi[e^{-x^2}]_0^1 = \pi(1 - e^{-1})$
</details>

---

**Ejercicio 2:** Rotar la región entre $y = x$ y $y = x^2$ alrededor de $x = 2$.

<details>
<summary>Ver solución</summary>

Radio = $2 - x$

$V = 2\pi\int_0^1 (2-x)(x - x^2)\,dx$

$= 2\pi\int_0^1 (2x - 2x^2 - x^2 + x^3)\,dx$

$= 2\pi\int_0^1 (2x - 3x^2 + x^3)\,dx = \frac{\pi}{6}$
</details>

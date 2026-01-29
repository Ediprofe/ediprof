# Volúmenes por Discos

El método de discos calcula volúmenes de sólidos de revolución apilando discos circulares infinitesimalmente delgados.

---

## 🎯 ¿Qué vas a aprender?

- Sólidos de revolución
- El método de discos
- Revolución alrededor del eje x
- Revolución alrededor del eje y

---

## 📖 Sólido de revolución

Un **sólido de revolución** se forma al rotar una región del plano alrededor de un eje.

Ejemplos: esfera (semicírculo rotado), cono (triángulo rotado), cilindro (rectángulo rotado).

---

## 📖 Método de discos (eje x)

Al rotar $y = f(x)$ alrededor del eje x, cada "rebanada" es un disco de:
- Radio: $r = f(x)$
- Espesor: $dx$
- Volumen: $\pi r^2 \cdot dx = \pi[f(x)]^2\,dx$

$$
\boxed{V = \pi\int_a^b [f(x)]^2\,dx}
$$

---

## ⚙️ Ejemplo 1: Cono

Rotar $y = x$ (de $x = 0$ a $x = h$) alrededor del eje x.

$$
V = \pi\int_0^h x^2\,dx = \pi\left[\frac{x^3}{3}\right]_0^h = \frac{\pi h^3}{3}
$$

Para un cono con altura $h$ y radio $r$, usaríamos $y = \frac{r}{h}x$:

$$
V = \pi\int_0^h \left(\frac{r}{h}x\right)^2\,dx = \frac{\pi r^2}{h^2} \cdot \frac{h^3}{3} = \frac{\pi r^2 h}{3}
$$

---

## ⚙️ Ejemplo 2: Esfera

Rotar $y = \sqrt{r^2 - x^2}$ (semicírculo) de $-r$ a $r$:

$$
V = \pi\int_{-r}^{r} (r^2 - x^2)\,dx
$$

$$
= \pi\left[r^2x - \frac{x^3}{3}\right]_{-r}^{r}
$$

$$
= \pi\left[\left(r^3 - \frac{r^3}{3}\right) - \left(-r^3 + \frac{r^3}{3}\right)\right]
$$

$$
= \pi \cdot \frac{4r^3}{3} = \frac{4\pi r^3}{3}
$$

---

## ⚙️ Ejemplo 3: Paraboloide

Rotar $y = \sqrt{x}$ de $x = 0$ a $x = 4$ alrededor del eje x:

$$
V = \pi\int_0^4 (\sqrt{x})^2\,dx = \pi\int_0^4 x\,dx = \pi\left[\frac{x^2}{2}\right]_0^4 = 8\pi
$$

---

## 📖 Método de discos (eje y)

Si rotamos $x = g(y)$ alrededor del eje y:

$$
V = \pi\int_c^d [g(y)]^2\,dy
$$

---

## ⚙️ Ejemplo 4: Rotación alrededor de y

Rotar la región acotada por $y = x^2$ y $y = 4$ alrededor del eje y.

Despejamos: $x = \sqrt{y}$ (lado derecho)

$$
V = \pi\int_0^4 (\sqrt{y})^2\,dy = \pi\int_0^4 y\,dy = \pi\left[\frac{y^2}{2}\right]_0^4 = 8\pi
$$

---

## ⚙️ Ejemplo 5: Semicírculo alrededor de y

Rotar $x = \sqrt{4 - y^2}$ de $y = 0$ a $y = 2$ alrededor del eje y:

$$
V = \pi\int_0^2 (4 - y^2)\,dy = \pi\left[4y - \frac{y^3}{3}\right]_0^2
$$

$$
= \pi\left(8 - \frac{8}{3}\right) = \frac{16\pi}{3}
$$

(Esto es media esfera de radio 2)

---

## 📊 Resumen

| Eje de rotación | Fórmula |
|-----------------|---------|
| Eje x | $V = \pi\int_a^b [f(x)]^2\,dx$ |
| Eje y | $V = \pi\int_c^d [g(y)]^2\,dy$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el volumen del sólido obtenido al rotar $y = x^3$ de $x = 0$ a $x = 2$ alrededor del eje x.

<details>
<summary>Ver solución</summary>

$$
V = \pi\int_0^2 x^6\,dx = \pi\left[\frac{x^7}{7}\right]_0^2 = \frac{128\pi}{7}
$$
</details>

---

**Ejercicio 2:** Rotar $y = e^x$ de $x = 0$ a $x = 1$ alrededor del eje x.

<details>
<summary>Ver solución</summary>

$$
V = \pi\int_0^1 e^{2x}\,dx = \pi\left[\frac{e^{2x}}{2}\right]_0^1 = \frac{\pi(e^2 - 1)}{2}
$$
</details>

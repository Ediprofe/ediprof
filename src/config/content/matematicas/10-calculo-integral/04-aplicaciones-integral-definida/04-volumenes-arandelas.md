---
title: "Volúmenes por Arandelas"
---

# Volúmenes por Arandelas

El método de arandelas extiende el método de discos para regiones con un "hueco" en el centro.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo usar arandelas vs discos
- La fórmula de arandelas
- Revolución alrededor de ejes desplazados
- Ejemplos variados

---

## 📖 ¿Cuándo usar arandelas?

Usamos arandelas cuando hay un **hueco** en el sólido, es decir, cuando la región rotada no toca el eje de rotación.

---

## 📖 Fórmula de arandelas

Cada "rebanada" es una arandela (disco con hueco):

- Radio exterior: $R$
- Radio interior: $r$
- Área: $\pi R^2 - \pi r^2 = \pi(R^2 - r^2)$

$$
\boxed{V = \pi\int_a^b [R(x)^2 - r(x)^2]\,dx}
$$

---

## ⚙️ Ejemplo 1: Región entre dos curvas

Rotar la región entre $y = x^2$ y $y = x$ (de $x = 0$ a $x = 1$) alrededor del eje x.

- Radio exterior: $R = x$ (curva de arriba)
- Radio interior: $r = x^2$ (curva de abajo)

$$
V = \pi\int_0^1 [x^2 - x^4]\,dx = \pi\left[\frac{x^3}{3} - \frac{x^5}{5}\right]_0^1
$$

$$
= \pi\left(\frac{1}{3} - \frac{1}{5}\right) = \frac{2\pi}{15}
$$

---

## ⚙️ Ejemplo 2: Alrededor del eje y

Rotar la misma región ($y = x^2$ a $y = x$) alrededor del eje y.

Despejamos: $x = y$ y $x = \sqrt{y}$

- Radio exterior: $R = \sqrt{y}$
- Radio interior: $r = y$

$$
V = \pi\int_0^1 [y - y^2]\,dy = \pi\left[\frac{y^2}{2} - \frac{y^3}{3}\right]_0^1 = \frac{\pi}{6}
$$

---

## 📖 Eje desplazado: rotación sobre y = c

Si rotamos alrededor de la recta horizontal $y = c$:

$$
V = \pi\int_a^b [(f(x) - c)^2 - (g(x) - c)^2]\,dx
$$

donde $f$ está más lejos de $y = c$ que $g$.

---

## ⚙️ Ejemplo 3: Alrededor de y = -1

Rotar la región bajo $y = x^2$ de $x = 0$ a $x = 2$ alrededor de $y = -1$.

- Radio exterior: $R = x^2 - (-1) = x^2 + 1$
- Radio interior: $r = 0 - (-1) = 1$ (desde el eje x hasta $y = -1$)

$$
V = \pi\int_0^2 [(x^2+1)^2 - 1]\,dx
$$

$$
= \pi\int_0^2 [x^4 + 2x^2 + 1 - 1]\,dx = \pi\int_0^2 (x^4 + 2x^2)\,dx
$$

$$
= \pi\left[\frac{x^5}{5} + \frac{2x^3}{3}\right]_0^2 = \pi\left(\frac{32}{5} + \frac{16}{3}\right) = \frac{176\pi}{15}
$$

---

## 📖 Eje desplazado: rotación sobre x = c

Para rotar alrededor de $x = c$, integramos en $y$:

$$
V = \pi\int_c^d [(f(y) - c)^2 - (g(y) - c)^2]\,dy
$$

---

## ⚙️ Ejemplo 4: Alrededor de x = 4

Rotar $y = \sqrt{x}$ (de $x = 0$ a $x = 4$) alrededor de $x = 4$.

Convertimos: $y$ va de 0 a 2, $x = y^2$

- Radio exterior: $R = 4 - 0 = 4$
- Radio interior: $r = 4 - y^2$

$$
V = \pi\int_0^2 [16 - (4-y^2)^2]\,dy
$$

$$
= \pi\int_0^2 [16 - 16 + 8y^2 - y^4]\,dy
$$

$$
= \pi\int_0^2 (8y^2 - y^4)\,dy = \pi\left[\frac{8y^3}{3} - \frac{y^5}{5}\right]_0^2
$$

$$
= \pi\left(\frac{64}{3} - \frac{32}{5}\right) = \frac{224\pi}{15}
$$

---

## 📊 Resumen: Discos vs Arandelas

| Método | Uso | Fórmula |
|--------|-----|---------|
| Discos | Región toca el eje | $\pi\int R^2$ |
| Arandelas | Región con hueco | $\pi\int (R^2 - r^2)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Rotar la región entre $y = x$ y $y = x^2$ de $x = 0$ a $x = 1$ alrededor de $y = 2$.

<details>
<summary>Ver solución</summary>

$R = 2 - x^2$, $r = 2 - x$

$$
V = \pi\int_0^1 [(2-x^2)^2 - (2-x)^2]\,dx
$$

$$
= \pi\int_0^1 [4 - 4x^2 + x^4 - 4 + 4x - x^2]\,dx
$$

$$
= \pi\int_0^1 (x^4 - 5x^2 + 4x)\,dx = \frac{8\pi}{15}
$$
</details>

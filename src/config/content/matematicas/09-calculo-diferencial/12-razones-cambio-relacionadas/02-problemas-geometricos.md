---
title: "Problemas Geométricos de Razones Relacionadas"
---

# Problemas Geométricos de Razones Relacionadas

Los problemas geométricos involucran figuras cuyas dimensiones cambian: círculos, triángulos, rectángulos, conos, etc. Las fórmulas de área, perímetro y volumen conectan las variables.

---

## 🎯 ¿Qué vas a aprender?

- Razones relacionadas con áreas y perímetros
- Problemas con volúmenes cambiantes
- Triángulos semejantes en movimiento
- Ángulos que cambian

---

## ⚙️ Ejemplo 1: Círculo expandiéndose

El radio de un círculo aumenta a 3 cm/s. ¿A qué razón aumenta el área cuando el radio es 10 cm?

**Relación:** $A = \pi r^2$

**Derivando:**
$$\frac{dA}{dt} = 2\pi r \frac{dr}{dt}$$

**Sustituyendo:** $r = 10$, $\frac{dr}{dt} = 3$
$$\frac{dA}{dt} = 2\pi(10)(3) = 60\pi \approx 188.5 \text{ cm}^2/\text{s}$$

---

## ⚙️ Ejemplo 2: Rectángulo con lados cambiantes

Un rectángulo tiene largo $L$ y ancho $W$. El largo aumenta a 2 cm/s mientras el ancho disminuye a 1 cm/s. ¿Cómo cambia el área cuando $L = 12$ cm y $W = 5$ cm?

**Relación:** $A = LW$

**Derivando:**
$$\frac{dA}{dt} = \frac{dL}{dt} \cdot W + L \cdot \frac{dW}{dt}$$

**Sustituyendo:** $L = 12$, $W = 5$, $\frac{dL}{dt} = 2$, $\frac{dW}{dt} = -1$
$$\frac{dA}{dt} = (2)(5) + (12)(-1) = 10 - 12 = -2 \text{ cm}^2/\text{s}$$

**El área disminuye a 2 cm²/s.**

---

## ⚙️ Ejemplo 3: Esfera derritiéndose

Una bola de hielo esférica se derrite de modo que su área superficial disminuye a 2 cm²/min. ¿A qué razón disminuye el diámetro cuando el radio es 5 cm?

**Relaciones:** $S = 4\pi r^2$, $D = 2r$

**Derivando S:**
$$\frac{dS}{dt} = 8\pi r \frac{dr}{dt}$$

**Datos:** $\frac{dS}{dt} = -2$, $r = 5$
$$-2 = 8\pi(5)\frac{dr}{dt}$$
$$\frac{dr}{dt} = \frac{-2}{40\pi} = \frac{-1}{20\pi}$$

**Diámetro:**
$$\frac{dD}{dt} = 2\frac{dr}{dt} = \frac{-1}{10\pi} \approx -0.032 \text{ cm/min}$$

---

## ⚙️ Ejemplo 4: Triángulo isósceles

Los lados iguales de un triángulo isósceles miden 10 cm. El ángulo entre ellos aumenta a 2°/min. ¿A qué razón aumenta el área cuando el ángulo es 60°?

**Área del triángulo:**
$$A = \frac{1}{2}ab\sin\theta = \frac{1}{2}(10)(10)\sin\theta = 50\sin\theta$$

**Derivando:**
$$\frac{dA}{dt} = 50\cos\theta \cdot \frac{d\theta}{dt}$$

**Nota:** Convertir a radianes: $2°/\text{min} = \frac{\pi}{90}$ rad/min

**Sustituyendo:** $\theta = 60° = \frac{\pi}{3}$
$$\frac{dA}{dt} = 50\cos\left(\frac{\pi}{3}\right) \cdot \frac{\pi}{90} = 50 \cdot \frac{1}{2} \cdot \frac{\pi}{90}$$
$$= \frac{25\pi}{90} = \frac{5\pi}{18} \approx 0.87 \text{ cm}^2/\text{min}$$

---

## ⚙️ Ejemplo 5: Cono con agua escapando

Agua escapa de un tanque cónico (vértice abajo) a razón de 5 L/min. El tanque tiene radio 3 m y altura 6 m. ¿A qué razón baja el nivel cuando la profundidad es 2 m?

**Por semejanza:** $\frac{r}{h} = \frac{3}{6} = \frac{1}{2}$ → $r = \frac{h}{2}$

**Volumen:**
$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{h}{2}\right)^2 h = \frac{\pi h^3}{12}$$

**Derivando:**
$$\frac{dV}{dt} = \frac{\pi h^2}{4} \frac{dh}{dt}$$

**Datos:** $\frac{dV}{dt} = -5$ (escapa), $h = 2$
$$-5 = \frac{\pi(4)}{4}\frac{dh}{dt}$$
$$\frac{dh}{dt} = \frac{-5}{\pi} \approx -1.59 \text{ m/min}$$

---

## ⚙️ Ejemplo 6: Ángulo de elevación

Un cohete despega verticalmente a 100 m/s. Un observador está a 500 m de la plataforma. ¿A qué razón cambia el ángulo de elevación cuando el cohete está a 1000 m de altura?

**Relación:** $\tan\theta = \frac{h}{500}$

**Derivando:**
$$\sec^2\theta \cdot \frac{d\theta}{dt} = \frac{1}{500}\frac{dh}{dt}$$

**Cuando $h = 1000$:**
$\tan\theta = 2$, $\sec^2\theta = 1 + 4 = 5$

$$5 \cdot \frac{d\theta}{dt} = \frac{100}{500} = 0.2$$
$$\frac{d\theta}{dt} = 0.04 \text{ rad/s} \approx 2.29°/\text{s}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Un cuadrado crece de modo que su diagonal aumenta a 4 cm/s. ¿A qué razón aumenta el lado cuando mide 10 cm?

<details>
<summary>Ver solución</summary>

$d = s\sqrt{2}$ → $\frac{dd}{dt} = \sqrt{2}\frac{ds}{dt}$

$4 = \sqrt{2}\frac{ds}{dt}$

$\frac{ds}{dt} = \frac{4}{\sqrt{2}} = 2\sqrt{2} \approx 2.83$ cm/s
</details>

---

**Ejercicio 2:** Un cilindro tiene radio fijo de 5 cm. Si el volumen aumenta a 40π cm³/s, ¿a qué razón aumenta la altura?

<details>
<summary>Ver solución</summary>

$V = \pi r^2 h = 25\pi h$

$\frac{dV}{dt} = 25\pi \frac{dh}{dt}$

$40\pi = 25\pi \frac{dh}{dt}$

$\frac{dh}{dt} = \frac{8}{5} = 1.6$ cm/s
</details>

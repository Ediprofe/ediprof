---
title: "Introducción a Razones de Cambio Relacionadas"
---

# Introducción a Razones de Cambio Relacionadas

Cuando dos o más cantidades cambian con el tiempo y están relacionadas por una ecuación, sus razones de cambio también están relacionadas. Este tipo de problemas aparece frecuentemente en física e ingeniería.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de razones relacionadas
- Metodología para resolver problemas
- Cómo conectar derivadas respecto al tiempo
- Aplicaciones prácticas

---

## 📖 El concepto

Si dos cantidades $x$ y $y$ están relacionadas por una ecuación y ambas cambian con el tiempo $t$, entonces sus derivadas $\frac{dx}{dt}$ y $\frac{dy}{dt}$ también están relacionadas.

**Idea clave:** Derivar la ecuación respecto a $t$ y despejar la razón desconocida.

---

## 📖 Metodología

1. **Leer** el problema e identificar cantidades variables
2. **Dibujar** un diagrama (muy importante)
3. **Asignar** variables a las cantidades
4. **Escribir** una ecuación que relacione las variables
5. **Derivar** ambos lados respecto a $t$ (usando regla de la cadena)
6. **Sustituir** valores conocidos
7. **Resolver** para la razón desconocida

---

## ⚙️ Ejemplo 1: Escalera deslizante

Una escalera de 10 m está apoyada contra una pared. El pie de la escalera se desliza alejándose de la pared a 2 m/s. ¿Qué tan rápido baja la parte superior cuando el pie está a 6 m de la pared?

**Variables:**
- $x$ = distancia del pie a la pared
- $y$ = altura de la parte superior

**Relación:** $x^2 + y^2 = 100$ (Pitágoras)

**Derivando respecto a $t$:**
$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$$

**Datos:** $x = 6$, $\frac{dx}{dt} = 2$

Primero, hallamos $y$: $y = \sqrt{100 - 36} = 8$

**Sustituyendo:**
$$2(6)(2) + 2(8)\frac{dy}{dt} = 0$$
$$24 + 16\frac{dy}{dt} = 0$$
$$\frac{dy}{dt} = -\frac{24}{16} = -1.5 \text{ m/s}$$

**La parte superior baja a 1.5 m/s.**

---

## ⚙️ Ejemplo 2: Globo inflándose

Un globo esférico se infla de modo que su volumen aumenta a 100 cm³/s. ¿A qué razón aumenta el radio cuando el radio es 5 cm?

**Relación:** $V = \frac{4}{3}\pi r^3$

**Derivando respecto a $t$:**
$$\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$$

**Datos:** $\frac{dV}{dt} = 100$, $r = 5$

$$100 = 4\pi(25)\frac{dr}{dt}$$
$$\frac{dr}{dt} = \frac{100}{100\pi} = \frac{1}{\pi} \approx 0.318 \text{ cm/s}$$

---

## ⚙️ Ejemplo 3: Cono llenándose

Agua se vierte en un cono invertido (radio = altura) a razón de 10 m³/min. ¿A qué razón sube el nivel cuando la profundidad es 5 m?

**Relación:** Para un cono con $r = h$:
$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi h^3$$

**Derivando:**
$$\frac{dV}{dt} = \pi h^2 \frac{dh}{dt}$$

**Datos:** $\frac{dV}{dt} = 10$, $h = 5$

$$10 = \pi(25)\frac{dh}{dt}$$
$$\frac{dh}{dt} = \frac{10}{25\pi} = \frac{2}{5\pi} \approx 0.127 \text{ m/min}$$

---

## 📖 Errores comunes

1. **Sustituir valores antes de derivar** ❌
   → Los valores se sustituyen DESPUÉS de derivar

2. **Olvidar la regla de la cadena** ❌
   → $\frac{d}{dt}[x^2] = 2x\frac{dx}{dt}$, no simplemente $2x$

3. **Signos incorrectos** ❌
   → Positivo = aumenta, Negativo = disminuye

---

## ⚙️ Ejemplo 4: Sombra creciente

Una persona de 2 m de altura camina alejándose de un poste de luz de 8 m a velocidad de 1.5 m/s. ¿A qué razón crece su sombra?

**Por triángulos semejantes:**
$$\frac{8}{x + s} = \frac{2}{s}$$

donde $x$ = distancia de la persona al poste, $s$ = longitud de la sombra.

$$8s = 2(x + s)$$
$$8s = 2x + 2s$$
$$6s = 2x$$
$$s = \frac{x}{3}$$

**Derivando:**
$$\frac{ds}{dt} = \frac{1}{3}\frac{dx}{dt} = \frac{1}{3}(1.5) = 0.5 \text{ m/s}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Un avión vuela horizontalmente a 500 km/h a una altura de 2 km. ¿A qué razón cambia la distancia al observador cuando está a 3 km de distancia horizontal?

<details>
<summary>Ver solución</summary>

$d^2 = x^2 + 4$ (distancia al observador)

$2d\frac{dd}{dt} = 2x\frac{dx}{dt}$

Cuando $x = 3$: $d = \sqrt{9+4} = \sqrt{13}$

$\frac{dd}{dt} = \frac{x}{d}\frac{dx}{dt} = \frac{3}{\sqrt{13}}(500) \approx 416$ km/h
</details>

---

**Ejercicio 2:** Dos autos parten del mismo punto. Uno va al norte a 60 km/h, otro al este a 80 km/h. ¿A qué razón se separan después de 1 hora?

<details>
<summary>Ver solución</summary>

$d^2 = x^2 + y^2$

$2d\frac{dd}{dt} = 2x\frac{dx}{dt} + 2y\frac{dy}{dt}$

Después de 1 hora: $x = 80$, $y = 60$, $d = 100$

$\frac{dd}{dt} = \frac{80(80) + 60(60)}{100} = 100$ km/h
</details>

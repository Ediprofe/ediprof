# Razón de Cambio Promedio

La derivada mide cómo cambia una función. Antes de llegar a la derivada, entendemos la razón de cambio promedio: cuánto cambia una cantidad en promedio sobre un intervalo.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de razón de cambio
- Cálculo de la razón de cambio promedio
- Interpretación geométrica como pendiente de secante
- Conexión con la velocidad promedio

---

## 📖 ¿Qué es una razón de cambio?

Una **razón de cambio** mide cuánto cambia una cantidad con respecto a otra.

$$\text{Razón de cambio} = \frac{\text{Cambio en la salida}}{\text{Cambio en la entrada}} = \frac{\Delta y}{\Delta x}$$

---

## 📖 Razón de cambio promedio

La **razón de cambio promedio** de $f$ en el intervalo $[a, b]$ es:

$$\text{RCP} = \frac{f(b) - f(a)}{b - a} = \frac{\Delta f}{\Delta x}$$

Mide el cambio **promedio** de $f$ por cada unidad de cambio en $x$.

---

## ⚙️ Ejemplo 1: Distancia y velocidad

Un automóvil recorre una distancia $d(t)$ en metros, donde $t$ es el tiempo en segundos:

$$d(t) = t^2 + 3t$$

¿Cuál es la velocidad promedio entre $t = 2$ y $t = 5$ segundos?

**Cálculo:**
$$\text{Velocidad promedio} = \frac{d(5) - d(2)}{5 - 2}$$

$$d(5) = 25 + 15 = 40 \text{ m}$$
$$d(2) = 4 + 6 = 10 \text{ m}$$

$$\text{Velocidad promedio} = \frac{40 - 10}{3} = \frac{30}{3} = 10 \text{ m/s}$$

---

## 📖 Interpretación geométrica

La razón de cambio promedio es la **pendiente de la recta secante** que pasa por los puntos $(a, f(a))$ y $(b, f(b))$.

$$m_{\text{secante}} = \frac{f(b) - f(a)}{b - a}$$

---

## ⚙️ Ejemplo 2: Pendiente de secante

Para $f(x) = x^2$, encuentra la pendiente de la secante entre $x = 1$ y $x = 3$.

$$m = \frac{f(3) - f(1)}{3 - 1} = \frac{9 - 1}{2} = \frac{8}{2} = 4$$

La secante tiene pendiente 4.

---

## ⚙️ Ejemplo 3: Diferentes intervalos

Para $f(x) = x^3$, calcula la RCP en:

**a) $[0, 2]$:**
$$\frac{f(2) - f(0)}{2 - 0} = \frac{8 - 0}{2} = 4$$

**b) $[1, 2]$:**
$$\frac{f(2) - f(1)}{2 - 1} = \frac{8 - 1}{1} = 7$$

**c) $[1.5, 2]$:**
$$\frac{f(2) - f(1.5)}{2 - 1.5} = \frac{8 - 3.375}{0.5} = \frac{4.625}{0.5} = 9.25$$

Observa: A medida que el intervalo se acerca a $x = 2$, la RCP se acerca a un valor específico (que será la derivada).

---

## 📖 Notación con incrementos

Usando $h$ como el incremento:

$$\text{RCP} = \frac{f(a + h) - f(a)}{h}$$

donde $h = b - a$ es el "paso" o incremento.

---

## ⚙️ Ejemplo 4: Usando incrementos

Para $f(x) = 2x^2 - 1$ en $x = 3$ con incremento $h$:

$$\text{RCP} = \frac{f(3 + h) - f(3)}{h}$$

$$f(3 + h) = 2(3 + h)^2 - 1 = 2(9 + 6h + h^2) - 1 = 17 + 12h + 2h^2$$

$$f(3) = 18 - 1 = 17$$

$$\text{RCP} = \frac{17 + 12h + 2h^2 - 17}{h} = \frac{12h + 2h^2}{h} = 12 + 2h$$

Para diferentes valores de $h$:
- $h = 1$: RCP = 14
- $h = 0.1$: RCP = 12.2
- $h = 0.01$: RCP = 12.02

Cuando $h \to 0$, RCP $\to 12$ (esta será la derivada).

---

## 📖 Aplicaciones

| Contexto | Razón de cambio promedio |
|----------|-------------------------|
| Posición vs tiempo | Velocidad promedio |
| Velocidad vs tiempo | Aceleración promedio |
| Costo vs producción | Costo marginal promedio |
| Población vs tiempo | Tasa de crecimiento promedio |
| Temperatura vs posición | Gradiente promedio |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Para $f(x) = \sqrt{x}$, calcula la RCP en $[4, 9]$.

<details>
<summary>Ver solución</summary>

$$\text{RCP} = \frac{\sqrt{9} - \sqrt{4}}{9 - 4} = \frac{3 - 2}{5} = \frac{1}{5} = 0.2$$
</details>

---

**Ejercicio 2:** La temperatura en una ciudad durante un día está dada por $T(t) = -t^2 + 12t + 10$ (en °C), donde $t$ es la hora del día (0 a 12). Calcula el cambio de temperatura promedio entre las 8:00 y las 12:00.

<details>
<summary>Ver solución</summary>

$$T(12) = -144 + 144 + 10 = 10°C$$
$$T(8) = -64 + 96 + 10 = 42°C$$

$$\text{RCP} = \frac{10 - 42}{12 - 8} = \frac{-32}{4} = -8 \text{ °C/hora}$$

La temperatura baja en promedio 8°C por hora.
</details>

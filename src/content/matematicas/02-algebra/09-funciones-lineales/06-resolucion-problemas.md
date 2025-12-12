# 🧩 Resolución de Problemas con Funciones Lineales

En esta lección aplicaremos las funciones lineales a la resolución de problemas del mundo real.

---

## 📖 Pasos para resolver problemas

1. **Identificar** las variables (¿qué representa $x$? ¿qué representa $y$?)
2. **Escribir** la función lineal $y = mx + b$
3. **Usar** la función para responder las preguntas
4. **Interpretar** los resultados en contexto

---

## 📖 Problemas de costos

### Ejemplo 1

Un gimnasio cobra una inscripción de $\$50$ y una mensualidad de $\$30$. ¿Cuál es el costo total después de $x$ meses?

**Función:**
$$
C(x) = 30x + 50
$$

**a)** ¿Cuánto cuesta después de 6 meses?
$$
C(6) = 30(6) + 50 = 180 + 50 = \$230
$$

**b)** ¿Después de cuántos meses el costo será $\$290$?
$$
290 = 30x + 50 \quad \Rightarrow \quad 30x = 240 \quad \Rightarrow \quad x = 8 \text{ meses}
$$

$$
\boxed{C(x) = 30x + 50}
$$

---

### Ejemplo 2

Un fontanero cobra $\$40$ por visita más $\$25$ por hora de trabajo. Si trabaja $h$ horas, ¿cuál es el costo?

$$
C(h) = 25h + 40
$$

¿Cuánto cobra por un trabajo de 3 horas?
$$
C(3) = 25(3) + 40 = 75 + 40 = \$115
$$

$$
\boxed{C(3) = \$115}
$$

---

## 📖 Problemas de distancia

### Ejemplo 3

Un auto sale de una ciudad y viaja a $80$ km/h. ¿A qué distancia estará después de $t$ horas?

$$
d(t) = 80t
$$

**a)** ¿Distancia después de 2.5 horas?
$$
d(2.5) = 80(2.5) = 200 \text{ km}
$$

**b)** ¿Cuánto tiempo para recorrer 320 km?
$$
320 = 80t \quad \Rightarrow \quad t = 4 \text{ horas}
$$

$$
\boxed{d(t) = 80t}
$$

---

### Ejemplo 4

Un ciclista parte de un punto que está a 10 km del origen y avanza a 15 km/h.

$$
d(t) = 15t + 10
$$

¿A qué distancia del origen está después de 3 horas?
$$
d(3) = 15(3) + 10 = 55 \text{ km}
$$

$$
\boxed{d(3) = 55 \text{ km}}
$$

---

## 📖 Problemas de depreciación

### Ejemplo 5

Un auto nuevo vale $\$25,000$ y pierde $\$2,000$ de valor cada año. ¿Cuál es su valor después de $t$ años?

$$
V(t) = -2000t + 25000
$$

**a)** ¿Valor después de 4 años?
$$
V(4) = -2000(4) + 25000 = -8000 + 25000 = \$17,000
$$

**b)** ¿Cuándo valdrá $\$15,000$?
$$
15000 = -2000t + 25000 \quad \Rightarrow \quad t = 5 \text{ años}
$$

$$
\boxed{V(t) = -2000t + 25000}
$$

---

## 📖 Problemas de temperatura

### Ejemplo 6

La temperatura en una montaña disminuye $6°C$ por cada 1000 metros de altura. Si a nivel del suelo (0 m) la temperatura es $24°C$, ¿cuál es la temperatura a $h$ kilómetros de altura?

$$
T(h) = -6h + 24
$$

(donde $h$ está en kilómetros)

¿Temperatura a 3 km de altura?
$$
T(3) = -6(3) + 24 = -18 + 24 = 6°C
$$

$$
\boxed{T(3) = 6°C}
$$

---

## 📖 Problemas de producción

### Ejemplo 7

Una fábrica produce 150 unidades por día, teniendo ya 200 unidades en inventario. ¿Cuántas unidades habrá después de $d$ días?

$$
U(d) = 150d + 200
$$

¿Cuántas unidades habrá después de una semana (7 días)?
$$
U(7) = 150(7) + 200 = 1050 + 200 = 1250 \text{ unidades}
$$

$$
\boxed{U(7) = 1250}
$$

---

## 📖 Encontrando la ecuación a partir de datos

### Ejemplo 8

Un tanque de agua se está vaciando. Después de 2 horas tiene 80 litros y después de 5 horas tiene 50 litros. Encuentra la función.

**Paso 1:** Encontrar la pendiente
$$
m = \frac{50 - 80}{5 - 2} = \frac{-30}{3} = -10
$$

**Paso 2:** Usar un punto para encontrar $b$
$$
80 = -10(2) + b \quad \Rightarrow \quad b = 100
$$

**Función:**
$$
V(t) = -10t + 100
$$

¿Cuándo estará vacío?
$$
0 = -10t + 100 \quad \Rightarrow \quad t = 10 \text{ horas}
$$

$$
\boxed{V(t) = -10t + 100}
$$

---

### Ejemplo 9

Un negocio tuvo ventas de $\$1200$ en enero y $\$1800$ en abril (3 meses después). Encuentra la función de ventas.

$$
m = \frac{1800 - 1200}{3 - 0} = \frac{600}{3} = 200
$$

$$
V(t) = 200t + 1200
$$

¿Ventas proyectadas para diciembre (11 meses después de enero)?
$$
V(11) = 200(11) + 1200 = \$3400
$$

$$
\boxed{V(t) = 200t + 1200}
$$

---

### Ejemplo 10

El precio de un producto era $\$50$ hace 2 años y ahora es $\$80$. Si la tendencia continúa, ¿cuánto costará en 3 años más?

$t = 0$ corresponde a hace 2 años: $(0, 50)$
$t = 2$ corresponde a ahora: $(2, 80)$

$$
m = \frac{80 - 50}{2 - 0} = 15
$$

$$
P(t) = 15t + 50
$$

En 3 años más (5 años desde $t = 0$):
$$
P(5) = 15(5) + 50 = \$125
$$

$$
\boxed{P(5) = \$125}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Un taxi cobra $\$2.50$ por kilómetro más $\$5$ de banderazo. Escribe la función de costo y calcula el costo de un viaje de 12 km.

<details>
<summary>Ver solución</summary>

$C(x) = 2.50x + 5$

$C(12) = 30 + 5 = \$35$

</details>

---

**Ejercicio 2:** Una piscina tiene 5000 litros y se está llenando a razón de 200 litros/hora. ¿Cuántos litros tendrá en 8 horas?

<details>
<summary>Ver solución</summary>

$V(t) = 200t + 5000$

$V(8) = 1600 + 5000 = 6600$ litros

</details>

---

**Ejercicio 3:** Un teléfono nuevo cuesta $\$800$ y pierde $\$100$ de valor cada año. ¿Cuándo valdrá $\$300$?

<details>
<summary>Ver solución</summary>

$V(t) = -100t + 800$

$300 = -100t + 800$

$t = 5$ años

</details>

---

**Ejercicio 4:** La temperatura de un horno sube de $20°C$ a $220°C$ en 10 minutos. Encuentra la función y calcula la temperatura a los 6 minutos.

<details>
<summary>Ver solución</summary>

$m = \frac{220-20}{10} = 20$

$T(t) = 20t + 20$

$T(6) = 120 + 20 = 140°C$

</details>

---

# **Introducción a las Funciones Lineales**

¿Te has fijado que muchas cosas en la vida cambian de forma constante? Si caminas a la misma velocidad, entre más tiempo pase, más distancia recorres. Si trabajas por horas con un pago fijo, entre más horas, más ganas. Esa relación "pareja" y constante es lo que llamamos una función lineal.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una función y cómo se aplica en el mundo real.
- Cómo identificar una función lineal por su "ritmo" constante.
- Los elementos básicos: la variable independiente ($x$) y la dependiente ($y$).
- La diferencia fundamental entre una relación lineal y otros tipos de cambios.

---

## 📖 ¿Qué es una Función?

Imagina una máquina: tú le das una "entrada" (un número) y ella te devuelve una única "salida". En matemáticas, llamamos a la entrada **variable independiente ($x$)** y a la salida **variable dependiente ($y$)**.

Decimos que $y$ es una función de $x$ porque el valor de $y$ "depende" totalmente de lo que pongamos en $x$.

$$
y = f(x)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Salario por Hora

Un estudiante trabaja en una biblioteca y gana 15 pesos por cada hora.

**Razonamiento:**
- Si trabaja 1 hora, gana $15 \cdot 1 = 15$ pesos.
- Si trabaja 2 horas, gana $15 \cdot 2 = 30$ pesos.
- Si trabaja $x$ horas, gana $15 \cdot x$.

La relación es:

$$
f(x) = 15x
$$

Donde $x$ son las horas y $f(x)$ es el dinero total en pesos.

---

### Ejemplo 2: El Costo del Taxi

Un taxi cobra 3 pesos solo con subirte (banderazo) y luego 2 pesos por cada kilómetro recorrido.

**Razonamiento:**
- Al inicio (0 km): 3 pesos.
- Al recorrer 1 km: $3 + 2 = 5$ pesos.
- Al recorrer 2 km: $3 + 2(2) = 7$ pesos.
- Al recorrer $x$ km: $2x + 3$.

La función es:

$$
f(x) = 2x + 3
$$

---

### Ejemplo 3: El Tanque de Agua

Un tanque tiene 100 litros y se vacía a un ritmo de 5 litros por minuto.

**Razonamiento:**
- Inicio: 100 litros.
- 1 min: $100 - 5 = 95$ litros.
- $x$ min: $100 - 5x$.

La función es:

$$
f(x) = -5x + 100
$$

Observa que aquí el valor disminuye, por eso el número que acompaña a la $x$ es negativo.

---

### Ejemplo 4: Fotocopias en la Papelería

Sacar una fotocopia cuesta 0.20 pesos. ¿Cuánto pagas según la cantidad de hojas?

**Razonamiento:**
- Es un cambio constante: cada hoja suma 0.20 al precio final.
- Si sacas 10 fotocopias: $0.20 \cdot 10 = 2$ pesos.
- Si sacas $x$ fotocopias: $0.20 \cdot x$.

La función es:

$$
f(x) = 0.20x
$$

---

### Ejemplo 5: El Ahorro en tu Alcancía

Tienes 500 pesos ahorrados y decides meter 100 pesos cada mes de ahora en adelante.

**Razonamiento:**
- El valor inicial ($b$) es 500 pesos.
- El ritmo de crecimiento ($m$) es 100 pesos por mes.
- En 3 meses tendrás: $500 + 100(3) = 800$ pesos.
- En $x$ meses tendrás: $100x + 500$.

La función es:

$$
f(x) = 100x + 500
$$

---

### Ejemplo 6: Una Vela que se Consume

Prendes una vela que mide 20 cm de alto. Se desgasta 2 cm por cada hora que pasa.

**Razonamiento:**
- Inicia en 20 cm ($b = 20$).
- Disminuye 2 cm por hora ($m = -2$).
- A las 5 horas medirá: $20 - 2(5) = 10$ cm.
- A las $x$ horas medirá: $-2x + 20$.

La función es:

$$
f(x) = -2x + 20
$$

---

## 📈 La Forma General

Todas las funciones lineales siguen este patrón:

$$
y = mx + b
$$

Donde:
- **$m$ (Pendiente):** Es el ritmo de cambio (lo que aumenta o disminuye por cada unidad).
- **$b$ (Intercepto):** Es el valor inicial (donde empezamos cuando $x=0$).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si una fotocopia cuesta 0.10 pesos, escribe la función del costo total $y$ para $x$ fotocopias.

<details>
<summary>Ver solución</summary>

**Razonamiento:** El costo aumenta 0.10 por cada unidad.
**Resultado:** $\boxed{y = 0.10x}$

</details>

---

### Ejercicio 2
Un vendedor gana un sueldo base de 500 pesos más 50 pesos por cada venta realizada. Escribe su función de sueldo mensual.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Inicia en 500 ($b$) y suma 50 por cada venta ($m$).
**Resultado:** $\boxed{y = 50x + 500}$

</details>

---

### Ejercicio 3
Evalúa la función $f(x) = 4x - 2$ cuando $x = 3$.

<details>
<summary>Ver solución</summary>

$$
f(3) = 4(3) - 2
$$

$$
12 - 2 = 10
$$

**Resultado:** $\boxed{10}$

</details>

---

### Ejercicio 4
En la función $y = -3x + 10$, ¿cuál es el valor inicial (cuando $x=0$)?

<details>
<summary>Ver solución</summary>

**Razonamiento:** El valor inicial es el intercepto $b$.
**Resultado:** $\boxed{10}$

</details>

---

### Ejercicio 5
Un globo está a 200 metros de altura y baja 10 metros por segundo. Escribe la función de su altura $h(t)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Inicia en 200 y resta 10 por cada segundo $t$.
**Resultado:** $\boxed{h(t) = -10t + 200}$

</details>

---

### Ejercicio 6
Identifica la pendiente ($m$) en la función $f(x) = \frac{1}{2}x - 5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** La pendiente es el coeficiente que acompaña a la $x$.
**Resultado:** $\boxed{1/2}$

</details>

---

### Ejercicio 7
Si $y = 2x + 1$, ¿cuánto vale $y$ si $x = -2$?

<details>
<summary>Ver solución</summary>

$$
y = 2(-2) + 1
$$

$$
-4 + 1 = -3
$$

**Resultado:** $\boxed{-3}$

</details>

---

### Ejercicio 8
¿Cuál es la variable dependiente en la relación "Costo de gasolina según los galones comprados"?

<details>
<summary>Ver solución</summary>

**Razonamiento:** El costo total depende de cuánta gasolina compres.
**Resultado:** $\boxed{\text{El Costo}}$

</details>

---

### Ejercicio 9
Escribe la función para: "Un número $y$ es el triple de otro número $x$ aumentado en 4".

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{y = 3x + 4}$

</details>

---

### Ejercicio 10
Si $f(x) = 10$, ¿cuánto vale $f(5)$ e $f(100)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Es una función constante, la salida no depende de $x$.
**Resultado:** $\boxed{10 \text{ en ambos casos}}$

</details>

---

## 🔑 Resumen

| Concepto | Definición | Ejemplo |
|:--- |:--- |:--- |
| **Función** | Relación donde a cada $x$ le toca un solo $y$. | Entrada $\to$ Proceso $\to$ Salida |
| **Pendiente ($m$)** | El ritmo constante de aumento o descenso. | Gana 15 pesos por hora. |
| **Intercepto ($b$)** | El valor de $y$ cuando $x$ es cero. | Pago base del taxi: 3 pesos. |
| **Forma Lineal** | Ecuación que representa una línea recta. | $y = mx + b$ |

> **Conclusión:** Las funciones lineales describen procesos donde el cambio es siempre el mismo, permitiéndonos predecir resultados futuros con total exactitud.

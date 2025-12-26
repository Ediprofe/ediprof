# **Movimiento Parabólico**

Cuando un futbolista cobra un tiro libre o un tenista hace un globo, la pelota no viaja en línea recta. Sube y baja describiendo una curva perfecta: una parábola. Es el baile sincronizado entre avanzar y caer al mismo tiempo.

---

## 🎯 ¿Qué vas a aprender?

- Cómo descomponer un lanzamiento diagonal en dos movimientos simples.
- Por qué la velocidad horizontal nunca cambia (si ignoramos el aire).
- Cómo calcular dónde caerá un proyectil conociendo su ángulo y velocidad.
- El secreto del ángulo de 45 grados.

---

## 🏹 **Dos Movimientos en Uno**

El truco para entender este movimiento es dividirlo. Imagina que son dos películas reproduciéndose a la vez:

### 1. Película Horizontal (Eje X)
Es un **MRU**. No hay nada que frene ni empuje al objeto horizontalmente. Viaja a velocidad constante.

### 2. Película Vertical (Eje Y)
Es un **Lanzamiento Vertical (MRUA)**. La gravedad lo frena al subir y lo acelera al bajar.

> **Regla de Oro:** El tiempo es el mismo para ambos. Lo que tarda en subir y bajar (Y) es el tiempo que tiene para avanzar (X).

---

## 📐 **Las Fórmulas Descompuestas**

Primero, separamos la velocidad inicial ($v_o$) usando el ángulo ($\theta$):

$$
v_x = v_o \cdot \cos(\theta)
$$

$$
v_y = v_o \cdot \sin(\theta)
$$

Luego aplicamos las reglas de cada movimiento:

| Eje | Velocidad | Posición |
| :--- | :--- | :--- |
| **X (MRU)** | $v_x = \text{constante}$ | $x = v_x \cdot t$ |
| **Y (MRUA)** | $v_{yf} = v_y - g \cdot t$ | $y = v_y \cdot t - \frac{1}{2}g \cdot t^2$ |

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Tiro de Cañón**

Un cañón dispara a **$100\,\mathrm{m/s}$** con un ángulo de **$30^\circ$**. ¿Cuál es su alcance horizontal?

**Datos:**
- $v_o = 100\,\mathrm{m/s}$
- $\theta = 30^\circ$
- $\sin(30^\circ) = 0.5$
- $\cos(30^\circ) = 0.87$
- $g = 10\,\mathrm{m/s^2}$

**Paso 1: Descomponer Velocidad**

$$
v_x = 100 \cdot 0.87 = 87\,\mathrm{m/s}
$$

$$
v_y = 100 \cdot 0.5 = 50\,\mathrm{m/s}
$$

**Paso 2: Calcular Tiempo de Vuelo (usando Y)**
Sube con 50 m/s. La gravedad le quita 10 cada segundo. Tarda 5s en subir. Por lo tanto, el vuelo total es **10 segundos**.

$$
t_{total} = \frac{2 \cdot v_y}{g} = \frac{100}{10} = 10\,\mathrm{s}
$$

**Paso 3: Calcular Alcance (usando X)**
Viaja a 87 m/s durante 10 segundos.

$$
x = 87 \cdot 10
$$

**Resultado:**

$$
\boxed{870\,\mathrm{m}}
$$

---

### **Ejemplo 2: Saque de Voleibol**

Un jugador golpea el balón con una velocidad de **$14\,\mathrm{m/s}$** en un ángulo de **$45^\circ$**. ¿Qué altura máxima alcanza?

**Datos:**
- $v_o = 14\,\mathrm{m/s}$
- $\theta = 45^\circ$
- $\sin(45^\circ) \approx 0.70$
- $g = 10\,\mathrm{m/s^2}$

**Paso 1: Componente Vertical**
Solo la velocidad vertical importa para la altura.

$$
v_y = 14 \cdot 0.70 = 9.8\,\mathrm{m/s}
$$

**Paso 2: Calcular Altura**
En el punto más alto, la velocidad vertical se agota.

$$
h_{max} = \frac{v_y^2}{2g}
$$

**Cálculo:**

$$
h_{max} = \frac{(9.8)^2}{20} = \frac{96.04}{20}
$$

**Resultado:**

$$
\boxed{4.8\,\mathrm{m}}
$$

---

### **Ejemplo 3: Salto de Motocross**

Una moto salta una rampa a **$20\,\mathrm{m/s}$** con un ángulo de **$30^\circ$**. ¿Cuánto tiempo permanece en el aire antes de tocar el suelo?

**Datos:**
- $v_o = 20\,\mathrm{m/s}$
- $\theta = 30^\circ$ ($\sin(30^\circ) = 0.5$)

**Paso 1: Velocidad de Subida**
La gravedad lo frena. ¿Con qué velocidad sube?

$$
v_y = 20 \cdot 0.5 = 10\,\mathrm{m/s}
$$

**Paso 2: Calcular Tiempo**
La gravedad le quita $10\,\mathrm{m/s}$ cada segundo.
- Tarda 1 segundo en subir (hasta que $v_y=0$).
- Tarda lo mismo en bajar.

$$
t_{total} = \frac{2 \cdot v_y}{g} = \frac{20}{10}
$$

**Resultado:**

$$
\boxed{2\,\mathrm{s}}
$$

---

### **Ejemplo 4: Lanzamiento Horizontal (Avión de Rescate)**

Un avión vuela horizontalmente a **$50\,\mathrm{m/s}$** y deja caer un paquete desde una altura de **$80\,\mathrm{m}$**. ¿A qué distancia horizontal del punto de lanzamiento cae el paquete?

**Datos:**
- $v_x = 50\,\mathrm{m/s}$ (Horizontal pura)
- $v_{y0} = 0\,\mathrm{m/s}$ (Caída libre vertical)
- $h = 80\,\mathrm{m}$

**Paso 1: Calcular Tiempo de Caída**
Es una caída libre desde $80\,\mathrm{m}$.

$$
h = \frac{1}{2} g t^2 \rightarrow 80 = 5 t^2
$$

$$
t^2 = 16 \rightarrow t = 4\,\mathrm{s}
$$

**Paso 2: Calcular Distancia Horizontal**
Durante esos 4 segundos, el paquete avanzó hacia adelante.

$$
x = v_x \cdot t = 50 \cdot 4
$$

**Resultado:**

$$
\boxed{200\,\mathrm{m}}
$$

---

### **Ejemplo 5: El Golpe de Golf (Ángulo Máximo)**

Un golfista golpea la bola a **$40\,\mathrm{m/s}$** buscando la máxima distancia posible (usa $45^\circ$). ¿Cuán lejos llega?

**Datos:**
- $v_o = 40\,\mathrm{m/s}$
- $\theta = 45^\circ$ ($\sin 45^\circ \approx 0.707$)

**Paso 1: Componentes**
Al ser $45^\circ$, $v_x$ y $v_y$ valen lo mismo.

$$
v_x = v_y = 40 \cdot 0.707 = 28.28\,\mathrm{m/s}
$$

**Paso 2: Tiempo de Vuelo**
Sube con $28.28\,\mathrm{m/s}$. Tarda $2.8\,\mathrm{s}$ en subir y $2.8\,\mathrm{s}$ en bajar. Tiempo total $\approx 5.6\,\mathrm{s}$.

$$
t = \frac{2 \cdot 28.28}{10} = 5.656\,\mathrm{s}
$$

**Paso 3: Alcance**

$$
x = 28.28 \cdot 5.656
$$

**Resultado:**

$$
\boxed{160\,\mathrm{m}}
$$
(Redondeado)

---


## 📝 Ejercicios de Práctica

### Ejercicio 1
**Lanzas algo a $20\,\mathrm{m/s}$ con ángulo de $60^\circ$ ($\sin 60 = 0.87$). ¿Velocidad vertical inicial?**

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$v_y = 20 \cdot 0.87$$
**Resultado:**
$$\boxed{17.4\,\mathrm{m/s}}$$

</details>

### Ejercicio 2
**Con los datos anteriores ($\cos 60 = 0.5$), ¿velocidad horizontal?**

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$v_x = 20 \cdot 0.5$$
**Resultado:**
$$\boxed{10\,\mathrm{m/s}}$$

</details>

### Ejercicio 3
**Si $v_y = 30\,\mathrm{m/s}$, ¿cuánto tarda en llegar a la cima?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Gana/pierde 10 por segundo.
**Resultado:**
$$\boxed{3\,\mathrm{s}}$$

</details>

### Ejercicio 4
**Un proyectil vuela por 6 segundos. Su $v_x$ es $40\,\mathrm{m/s}$. ¿Alcance?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $x = v_x \cdot t$.
**Cálculo:**
$$x = 40 \cdot 6$$
**Resultado:**
$$\boxed{240\,\mathrm{m}}$$

</details>

### Ejercicio 5
**¿Qué ángulo logra el mayor alcance posible?**

<details>
<summary>Ver solución</summary>

**Respuesta:**
$$\boxed{45^\circ}$$
Es el equilibrio perfecto entre avanzar y subir.

</details>

### Ejercicio 6
**Disparas horizontalmente desde un acantilado a $10\,\mathrm{m/s}$. ¿Cuál es su $v_y$ inicial?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Al ser horizontal, no sube ni baja al inicio.
**Resultado:**
$$\boxed{0\,\mathrm{m/s}}$$

</details>

### Ejercicio 7
**Un balón es pateado. En el punto más alto, ¿su velocidad es cero?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. Su velocidad vertical es cero, pero **sigue avanzando horizontalmente** con $v_x$.
**Resultado:**
**No.**

</details>

### Ejercicio 8
**Calcula la altura máxima si $v_y = 20\,\mathrm{m/s}$.**

<details>
<summary>Ver solución</summary>

**Fórmula:** $h = v_y^2 / 2g$.
**Cálculo:**
$$h = \frac{20^2}{20} = \frac{400}{20}$$
**Resultado:**
$$\boxed{20\,\mathrm{m}}$$

</details>

### Ejercicio 9
**¿Dos proyectiles de distinta masa (sin aire) siguen la misma parábola si se lanzan igual?**

<details>
<summary>Ver solución</summary>

**Respuesta:**
**Sí.** La gravedad acelera a todos los objetos por igual.

</details>

### Ejercicio 10
**Si $v_x = 10\,\mathrm{m/s}$ y $v_y = 10\,\mathrm{m/s}$ en un instante, ¿a qué velocidad real va?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Pitágoras.
$$v = \sqrt{10^2 + 10^2} = \sqrt{200}$$
**Resultado:**
$$\boxed{14.1\,\mathrm{m/s}}$$

</details>

---

## 🔑 Resumen

![resumen-tiro-parabolico](https://cdn.ediprofe.com/img/fisica/tpbn-resumen-tiro-parabolico.webp)


| Componente | Ecuación Clave | Comportamiento |
|------------|----------------|----------------|
| **V. Horizontal** | $$v_x = v_o \cos\theta$$ | Nunca cambia. |
| **V. Vertical** | $$v_y = v_o \sin\theta$$ | Cambia con la gravedad (sube y baja). |
| **Alcance** | $$x = v_x \cdot t_{total}$$ | Depende del tiempo de vuelo. |
| **Tiempo** | $$t_{total} = \frac{2 v_y}{g}$$ | Determinado por la altura y gravedad. |

> Todo tiro parabólico es simplemente una caída libre que "se mueve hacia el lado".

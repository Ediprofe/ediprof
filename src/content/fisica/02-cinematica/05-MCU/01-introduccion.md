# 🎡 **Movimiento Circular Uniforme (MCU)**

¿Has visto la rueda de la fortuna girar? ¿O las manecillas de un reloj moviéndose? Estos son ejemplos perfectos del **Movimiento Circular Uniforme**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el Movimiento Circular Uniforme (MCU).
- La diferencia entre período ($T$) y frecuencia ($f$).
- Cómo se relacionan la velocidad angular ($\omega$) y la velocidad tangencial ($v$).
- Por qué existe aceleración (centrípeta) aunque la rapidez sea constante.

---

## 🔄 **¿Qué es el MCU?**

El **Movimiento Circular Uniforme (MCU)** es aquel donde un objeto se mueve en una **trayectoria circular** manteniendo una **rapidez constante**.

Aunque la rapidez (el valor numérico) no cambia, la **dirección** de la velocidad sí cambia constantemente instante a instante para seguir la curva. Por eso decimos que existe una aceleración especial llamada **aceleración centrípeta**.

### **Características Principales:**

| Característica | Descripción |
| :--- | :--- |
| **Trayectoria** | Un círculo perfecto. |
| **Rapidez** | Constante (siempre va a la misma marcha). |
| **Dirección** | Cambia continuamente (siempre tangente al círculo). |
| **Aceleración** | Apunta siempre hacia el centro (centrípeta). |

---

## 📐 **Conceptos Fundamentales**

Para entender el MCU, necesitamos definir nuevas variables que no usábamos en el movimiento rectilíneo.

### **1. Período ($T$)**
Es el **tiempo** que tarda el objeto en dar **una vuelta completa**.
* **Unidad:** Segundos ($s$).
* **Ejemplo:** La Tierra da una vuelta al Sol en 365 días.

### **2. Frecuencia ($f$)**
Es el **número de vueltas** que da el objeto en **un segundo**.
* **Unidad:** Hertz ($Hz$) o $s^{-1}$.
* **Relación con el período:** Son inversos.
  $$f = \frac{1}{T}$$

### **3. Velocidad Angular ($\omega$)**
Mide qué tan rápido **gira** el ángulo. Es el ángulo recorrido por unidad de tiempo.
* **Unidad:** Radianes por segundo ($rad/s$).
* **Fórmula:**
  $$\omega = \frac{2\pi}{T} = 2\pi f$$

### **4. Velocidad Tangencial ($v$)**
Es la velocidad "real" en metros por segundo. Representa la distancia recorrida en el borde del círculo.
* **Unidad:** Metros por segundo ($m/s$).
* **Fórmula:**
  $$v = \omega \cdot r$$
  *(Donde $r$ es el radio del círculo)*

---

## ⚡ **Aceleración Centrípeta**

Podría parecer extraño hablar de aceleración si la rapidez no cambia. Pero recuerda: **la velocidad es un vector** (tiene magnitud y dirección).

En el MCU:
1. La **magnitud** de la velocidad no cambia.
2. La **dirección** cambia todo el tiempo.

Ese cambio de dirección es causado por una fuerza (y por tanto una aceleración) que "jala" al objeto hacia el centro, evitando que salga disparado en línea recta.

$$a_c = \frac{v^2}{r} = \omega^2 \cdot r$$

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: La Rueda de Bicicleta**

Una rueda de radio $0.35\,\mathrm{m}$ da **2 vueltas por segundo**. Calcula su período y velocidad tangencial.

**1. Identificar datos:**
* $r = 0.35\,\mathrm{m}$
* $f = 2\,\mathrm{Hz}$ (2 vueltas/s)

**2. Calcular Período ($T$):**
$$T = \frac{1}{f} = \frac{1}{2} = 0.5\,\mathrm{s}$$

**3. Calcular Velocidad Angular ($\omega$):**
$$\omega = 2\pi f = 2\pi(2) = 4\pi \approx 12.57\,\mathrm{rad/s}$$

**4. Calcular Velocidad Tangencial ($v$):**
$$v = \omega \cdot r = 12.57 \cdot 0.35 \approx 4.4\,\mathrm{m/s}$$

> **Resultado:** La rueda gira a **4.4 m/s**.

---

### **Ejemplo 2: El Auto en la Curva**

Un auto toma una curva de radio $50\,\mathrm{m}$ a una velocidad de $20\,\mathrm{m/s}$ ($72\,\mathrm{km/h}$). ¿Cuál es su aceleración centrípeta?

**1. Datos:**
* $r = 50\,\mathrm{m}$
* $v = 20\,\mathrm{m/s}$

**2. Fórmula:**
$$a_c = \frac{v^2}{r}$$

**3. Cálculo:**
$$a_c = \frac{20^2}{50} = \frac{400}{50} = 8\,\mathrm{m/s^2}$$

> **Resultado:** La aceleración hacia el centro es de **$8\,\mathrm{m/s^2}$**.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1: El Ventilador**

Un ventilador gira a **120 RPM** (revoluciones por minuto). ¿Cuál es su frecuencia en Hz?

<details>
<summary>Ver solución</summary>

Convertimos minutos a segundos:
$$f = \frac{120\,\text{vueltas}}{60\,\text{segundos}} = 2\,\mathrm{Hz}$$

**Respuesta:** **2 Hz**.

</details>

---

### **Ejercicio 2: Velocidad Angular**

Un carrusel tarda **20 segundos** en dar una vuelta. ¿Cuál es su velocidad angular?

<details>
<summary>Ver solución</summary>

$$T = 20\,\mathrm{s}$$
$$\omega = \frac{2\pi}{T} = \frac{2\pi}{20} = \frac{\pi}{10} \approx 0.314\,\mathrm{rad/s}$$

**Respuesta:** **0.314 rad/s**.

</details>

---

### **Ejercicio 3: El CD**

Un punto en el borde de un CD ($r = 0.06\,\mathrm{m}$) gira con una velocidad tangencial de $3\,\mathrm{m/s}$. ¿Cuál es su velocidad angular?

<details>
<summary>Ver solución</summary>

Sabemos que $v = \omega \cdot r$, entonces despejamos $\omega$:
$$\omega = \frac{v}{r} = \frac{3}{0.06} = 50\,\mathrm{rad/s}$$

**Respuesta:** **50 rad/s**.

</details>

---

## 🔑 Resumen

| Concepto | Símbolo | Fórmula | Significado |
| :--- | :---: | :--- | :--- |
| **Período** | $T$ | $1/f$ | Tiempo de una vuelta. |
| **Frecuencia** | $f$ | $1/T$ | Vueltas por segundo. |
| **Vel. Angular** | $\omega$ | $2\pi f$ | Velocidad de giro (rad/s). |
| **Vel. Tangencial** | $v$ | $\omega \cdot r$ | Velocidad lineal (m/s). |
| **Acel. Centrípeta** | $a_c$ | $v^2/r$ | Aceleración hacia el centro. |

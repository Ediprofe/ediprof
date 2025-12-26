# 🎡 **Movimiento Circular Uniforme (MCU)**

Imagina que atas una piedra a una cuerda y empiezas a girarla sobre tu cabeza. Sientes la tensión en la cuerda, ¿verdad? Si soltaras la cuerda de repente, la piedra saldría disparada en línea recta.

Ese esfuerzo que haces para mantener la piedra girando es la clave para entender el **Movimiento Circular Uniforme (MCU)**.

---

## 🎯 **¿Qué vas a aprender?**

*   Por qué un objeto puede acelerar aunque su rapidez no cambie.
*   La diferencia entre qué tan rápido *giras* y qué tan rápido *te mueves*.
*   Cómo predecir el movimiento de cosas que giran (ruedas, planetas, ventiladores).

---

## 🔄 **El Concepto: Girar a ritmo constante**

El **MCU** es el movimiento de un objeto que viaja en círculos manteniendo siempre el mismo ritmo.

*   **Uniforme:** Significa que no se frena ni se acelera en su giro. Tarda siempre lo mismo en dar una vuelta.
*   **Circular:** Su camino es un círculo perfecto.

### **La Paradoja de la Aceleración**

Aquí viene lo interesante. En física, **Velocidad** y **Rapidez** no son lo mismo:

1.  **Rapidez:** Es solo el número (ej. $20\,\mathrm{km/h}$). En el MCU, **es constante**.
2.  **Velocidad:** Es el número + la **dirección**.

En un círculo, aunque vayas siempre a $20\,\mathrm{km/h}$, tu dirección cambia en cada instante (primero vas al norte, luego al oeste, luego al sur...).

> 💡 **Conclusión:** Como la **dirección** cambia, la **velocidad** cambia. Y si la velocidad cambia, **¡existe aceleración!**

Esta aceleración se llama **Centrípeta** (busca el centro) porque es la fuerza que "jala" al objeto hacia adentro para que no se escape en línea recta.

![MCU - Intro](/images/fisica/cinematica/mcu/mcu-intro.png)

---

## ⏱️ **Paso 1: El Ritmo del Giro (Período y Frecuencia)**

Para describir algo que gira, lo primero que preguntamos es: "¿Qué tan rápido da las vueltas?". Tenemos dos formas de medirlo:

### **1. El Período ($T$): "Tiempo por vuelta"**

Es el tiempo que tardas en completar **un ciclo completo**.

*   *Ejemplo:* La Tierra tarda 365 días en dar una vuelta al Sol. $T = 365\,\text{días}$.

**Fórmula:**

$$
T = \frac{\text{Tiempo total}}{\text{Número de vueltas}}
$$

### **2. La Frecuencia ($f$): "Vueltas por tiempo"**

Es al revés. Cuántas vueltas logras dar en **un segundo**.

*   *Ejemplo:* Un ventilador rápido da 10 vueltas en un segundo. $f = 10\,\mathrm{Hz}$.

**Fórmula:**

$$
f = \frac{\text{Número de vueltas}}{\text{Tiempo total}}
$$

> 🔄 **Son inversos:** Si tardas mucho en dar una vuelta (Período grande), das pocas vueltas por segundo (Frecuencia pequeña).

$$
T = \frac{1}{f} \quad \text{y} \quad f = \frac{1}{T}
$$

---

## 🏎️ **Paso 2: Las Dos Velocidades**

Imagina un carrusel. Tú te sientas en el borde (el caballo exterior) y tu amigo se sienta cerca del centro. Ambos completan una vuelta al mismo tiempo, pero tú recorres mucha más distancia que él.

### **1. Velocidad Angular ($\omega$): "¿Qué tan rápido giramos?"**

Mide el **ángulo** que barres por segundo.

*   En el carrusel, tú y tu amigo tienen la **misma** velocidad angular (ambos dan 1 vuelta en el mismo tiempo).
*   Se mide en **radianes por segundo ($rad/s$)**.

**Fórmula:** Una vuelta completa son $2\pi$ radianes.

$$
\omega = \frac{2\pi}{T} = 2\pi f
$$

### **2. Velocidad Tangencial ($v$): "¿Qué tan rápido nos movemos?"**

Mide los **metros** que recorres por segundo.

*   En el carrusel, tú vas **más rápido** que tu amigo porque estás más lejos del centro y tienes que recorrer un círculo más grande en el mismo tiempo.
*   Se mide en **metros por segundo ($m/s$)**.

**Fórmula:** Depende del radio ($r$).

$$
v = \omega \cdot r
$$

![Amigos en carrusel - MCU](/images/fisica/cinematica/mcu/carrusel-mcu.png)

---

## ⚙️ **Ejemplos de la Vida Real**

### **Ejemplo 1: La Rueda de Bicicleta**

Una rueda de radio $0.35\,\mathrm{m}$ gira rápidamente dando **2 vueltas cada segundo**. Queremos saber qué tan rápido se mueve un punto en el borde de la llanta.

![MCU - Rueda a 2 vueltas/s](/images/fisica/cinematica/mcu/rueda-2hz.png)

**Paso 1: Entender los datos**

*   Radio ($r$) = $0.35\,\mathrm{m}$.
*   Frecuencia ($f$) = $2\,\mathrm{Hz}$ (2 vueltas por segundo).

**Paso 2: Calcular la velocidad de giro ($\omega$)**

Cada vuelta son $2\pi$ radianes. Si da 2 vueltas:

$$
\omega = 2\pi \cdot 2 = 4\pi \approx 12.57\,\mathrm{rad/s}
$$

**Paso 3: Calcular la velocidad real ($v$)**

Ahora multiplicamos el giro por el radio:

$$
v = 12.57 \cdot 0.35 \approx 4.4\,\mathrm{m/s}
$$

> **Resultado:** El borde de la rueda viaja a **4.4 m/s** (unos 16 km/h).

---

### **Ejemplo 2: El Auto en la Curva**

Un auto entra a una rotonda de $50\,\mathrm{m}$ de radio a una velocidad de $20\,\mathrm{m/s}$. ¿Qué tan fuerte es la aceleración que siente hacia el centro?

![Auto en la curva](/images/fisica/cinematica/mcu/carro-en-mcu.png)

**Análisis:**

Aunque el velocímetro marque siempre 20, el auto está girando. Necesita una aceleración centrípeta ($a_c$) para no salirse de la curva.

**Fórmula:**

$$
a_c = \frac{v^2}{r}
$$

**Cálculo:**

$$
a_c = \frac{20^2}{50}
$$

$$
= \frac{400}{50}
$$

$$
= 8\,\mathrm{m/s^2}
$$

> **Interpretación:** Siente una aceleración lateral de $8\,\mathrm{m/s^2}$, casi tan fuerte como la gravedad ($9.8\,\mathrm{m/s^2}$). ¡Es una curva cerrada tomada a alta velocidad!

---

### **Ejemplo 3: La Tierra Orbitando**

La Tierra completa una vuelta al Sol en **365 días**. ¿Cuál es su período en segundos y su frecuencia?

**Datos:**
- 1 año = 365 días

**Paso 1: Convertir a segundos**

$$
T = 365 \times 24 \times 3600 = 31\,536\,000\,\mathrm{s}
$$

**Paso 2: Calcular frecuencia**

$$
f = \frac{1}{T} = \frac{1}{31\,536\,000}
$$

**Resultado:**

$$
\boxed{f \approx 3.17 \times 10^{-8}\,\mathrm{Hz}}
$$

(La Tierra da una vuelta cada 31 millones de segundos, ¡una frecuencia muy baja!).

---

### **Ejemplo 4: Período desde Velocidad Angular**

Un disco gira con velocidad angular de **$10\,\mathrm{rad/s}$**. ¿Cuánto tiempo tarda en dar una vuelta completa?

**Datos:**
- $\omega = 10\,\mathrm{rad/s}$

**Razonamiento:**
Una vuelta completa son $2\pi$ radianes. El período es el tiempo que tarda en barrer esos $2\pi$ radianes.

$$
T = \frac{2\pi}{\omega}
$$

**Cálculo:**

$$
T = \frac{6.28}{10}
$$

**Resultado:**

$$
\boxed{0.628\,\mathrm{s}}
$$

---

### **Ejemplo 5: Velocidad Tangencial en una Rueda Grande**

Una rueda de la fortuna tiene un radio de **$25\,\mathrm{m}$** y tarda **$40\,\mathrm{s}$** en dar una vuelta. ¿A qué velocidad viajan los pasajeros en el borde?

**Datos:**
- Radio ($r$) = $25\,\mathrm{m}$
- Período ($T$) = $40\,\mathrm{s}$

**Paso 1: Velocidad Angular**

$$
\omega = \frac{2\pi}{T} = \frac{6.28}{40} = 0.157\,\mathrm{rad/s}
$$

**Paso 2: Velocidad Tangencial**

$$
v = \omega \cdot r = 0.157 \times 25
$$

**Resultado:**

$$
\boxed{3.93\,\mathrm{m/s}}
$$

(Aproximadamente 14 km/h).

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1: El Ventilador**

Un ventilador gira a **120 RPM** (revoluciones por minuto). ¿Cuál es su frecuencia en Hz (vueltas por segundo)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Si da 120 vueltas en 60 segundos (1 minuto), ¿cuántas da en 1 segundo?

$$
f = \frac{120}{60} = 2\,\mathrm{Hz}
$$

**Respuesta:** $\boxed{2\,\mathrm{Hz}}$

</details>

---

### **Ejercicio 2: El Carrusel**

Un carrusel tarda **20 segundos** en dar una vuelta completa. ¿Cuál es su velocidad angular?

<details>
<summary>Ver solución</summary>

**Datos:** $T = 20\,\mathrm{s}$.

**Fórmula:**

$$
\omega = \frac{2\pi}{T}
$$

**Cálculo:**

$$
\omega = \frac{6.28}{20} \approx 0.314\,\mathrm{rad/s}
$$

**Respuesta:** $\boxed{0.314\,\mathrm{rad/s}}$

</details>

---

### **Ejercicio 3: Período de un Motor**

Un motor gira a **3600 RPM**. ¿Cuál es su período en segundos?

<details>
<summary>Ver solución</summary>

**Datos:** 3600 RPM = 60 vueltas/s (dividiendo entre 60).

**Razonamiento:** $f = 60\,\mathrm{Hz}$, entonces:

$$
T = \frac{1}{f} = \frac{1}{60}
$$

**Respuesta:** $\boxed{0.0167\,\mathrm{s}}$

</details>

---

### **Ejercicio 4: Velocidad Tangencial**

Una llanta de radio **$0.4\,\mathrm{m}$** gira a **$5\,\mathrm{rad/s}$**. ¿Cuál es la velocidad tangencial en su borde?

<details>
<summary>Ver solución</summary>

**Datos:** $r = 0.4\,\mathrm{m}$, $\omega = 5\,\mathrm{rad/s}$.

**Fórmula:**

$$
v = \omega \cdot r = 5 \times 0.4
$$

**Respuesta:** $\boxed{2\,\mathrm{m/s}}$

</details>

---

### **Ejercicio 5: Aceleración Centrípeta**

Un objeto gira en un círculo de radio **$2\,\mathrm{m}$** a **$4\,\mathrm{m/s}$**. ¿Cuál es su aceleración centrípeta?

<details>
<summary>Ver solución</summary>

**Datos:** $v = 4\,\mathrm{m/s}$, $r = 2\,\mathrm{m}$.

**Fórmula:**

$$
a_c = \frac{v^2}{r} = \frac{16}{2}
$$

**Respuesta:** $\boxed{8\,\mathrm{m/s^2}}$

</details>

---

### **Ejercicio 6: Frecuencia desde Período**

Si un trompo tarda **$0.5\,\mathrm{s}$** en dar una vuelta, ¿cuál es su frecuencia?

<details>
<summary>Ver solución</summary>

**Datos:** $T = 0.5\,\mathrm{s}$.

**Fórmula:**

$$
f = \frac{1}{T} = \frac{1}{0.5}
$$

**Respuesta:** $\boxed{2\,\mathrm{Hz}}$

</details>

---

### **Ejercicio 7: Radio desde Velocidades**

Un objeto tiene velocidad angular $\omega = 8\,\mathrm{rad/s}$ y velocidad tangencial $v = 24\,\mathrm{m/s}$. ¿Cuál es el radio del círculo?

<details>
<summary>Ver solución</summary>

**Datos:** $\omega = 8$, $v = 24$.

**Fórmula:** $v = \omega \cdot r \rightarrow r = v / \omega$.

$$
r = \frac{24}{8}
$$

**Respuesta:** $\boxed{3\,\mathrm{m}}$

</details>

---

### **Ejercicio 8: Comparación de Velocidades**

En un disco, el punto A está a $10\,\mathrm{cm}$ del centro y el punto B a $20\,\mathrm{cm}$. Si ambos dan la vuelta en el mismo tiempo, ¿cuál va más rápido (mayor velocidad tangencial)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ambos tienen la misma $\omega$ (mismo período), pero $v = \omega \cdot r$. El que tiene **mayor radio** va más rápido.

**Respuesta:** El punto **B** (a 20 cm del centro) va al doble de velocidad que A.

</details>

---

### **Ejercicio 9: Velocidad Angular desde Hz**

Un disco duro gira a **7200 RPM**. ¿Cuál es su velocidad angular en rad/s?

<details>
<summary>Ver solución</summary>

**Paso 1:** Convertir RPM a Hz.

$$
f = \frac{7200}{60} = 120\,\mathrm{Hz}
$$

**Paso 2:** Calcular $\omega$.

$$
\omega = 2\pi f = 6.28 \times 120
$$

**Respuesta:** $\boxed{753.6\,\mathrm{rad/s}}$

</details>

---

### **Ejercicio 10: La Lavadora**

El tambor de una lavadora tiene radio $0.25\,\mathrm{m}$ y gira a $800\,\mathrm{RPM}$ en el ciclo de centrifugado. ¿Cuál es la aceleración centrípeta de la ropa en el borde?

<details>
<summary>Ver solución</summary>

**Paso 1:** Frecuencia en Hz.

$$
f = \frac{800}{60} = 13.33\,\mathrm{Hz}
$$

**Paso 2:** Velocidad angular.

$$
\omega = 2\pi f = 6.28 \times 13.33 = 83.7\,\mathrm{rad/s}
$$

**Paso 3:** Velocidad tangencial.

$$
v = \omega \cdot r = 83.7 \times 0.25 = 20.9\,\mathrm{m/s}
$$

**Paso 4:** Aceleración centrípeta.

$$
a_c = \frac{v^2}{r} = \frac{(20.9)^2}{0.25} = \frac{437}{0.25}
$$

**Respuesta:** $\boxed{1748\,\mathrm{m/s^2}}$

(¡Unas 178 veces la gravedad! Por eso el agua sale de la ropa).

</details>

---

## 🔑 **Resumen**

![MCU-Resumen](/images/fisica/cinematica/mcu/mcu-resumen.png)

| Si quieres saber... | Usa esta variable | Fórmula Clave |
| :--- | :---: | :--- |
| ¿Cuánto tarda una vuelta? | **Período ($T$)** | $T = 1/f$ |
| ¿Cuántas vueltas por segundo? | **Frecuencia ($f$)** | $f = 1/T$ |
| ¿Qué tan rápido *gira*? | **Vel. Angular ($\omega$)** | $\omega = 2\pi f$ |
| ¿Qué tan rápido *avanza*? | **Vel. Tangencial ($v$)** | $v = \omega \cdot r$ |
| ¿Cuánto *jala* hacia el centro? | **Acel. Centrípeta ($a_c$)** | $a_c = v^2/r$ |

> El MCU combina lo mejor de dos mundos: la velocidad constante (rapidez fija) con la aceleración constante (cambio continuo de dirección).


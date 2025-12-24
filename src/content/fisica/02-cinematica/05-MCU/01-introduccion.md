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
*   **Fórmula:** 
$$
T = \frac{\text{Tiempo total}}{\text{Número de vueltas}}
$$

### **2. La Frecuencia ($f$): "Vueltas por tiempo"**
Es al revés. Cuántas vueltas logras dar en **un segundo**.
*   *Ejemplo:* Un ventilador rápido da 10 vueltas en un segundo. $f = 10\,\mathrm{Hz}$.
*   **Fórmula:** 
$$
f = \frac{\text{Número de vueltas}}{\text{Tiempo total}}
$$

> 🔄 **Son inversos:** Si tardas mucho en dar una vuelta (Período grande), das pocas vueltas por segundo (Frecuencia pequeña).
> $$T = \frac{1}{f} \quad \text{y} \quad f = \frac{1}{T}$$

---

## 🏎️ **Paso 2: Las Dos Velocidades**

Imagina un carrusel. Tú te sientas en el borde (el caballo exterior) y tu amigo se sienta cerca del centro. Ambos completan una vuelta al mismo tiempo, pero tú recorres mucha más distancia que él.

### **1. Velocidad Angular ($\omega$): "¿Qué tan rápido giramos?"**
Mide el **ángulo** que barres por segundo.
*   En el carrusel, tú y tu amigo tienen la **misma** velocidad angular (ambos dan 1 vuelta en el mismo tiempo).
*   Se mide en **radianes por segundo ($rad/s$)**.
*   **Fórmula:** Una vuelta completa son $2\pi$ radianes.
    $$
    \omega = \frac{2\pi}{T} = 2\pi f 
    $$

### **2. Velocidad Tangencial ($v$): "¿Qué tan rápido nos movemos?"**
Mide los **metros** que recorres por segundo.
*   En el carrusel, tú vas **más rápido** que tu amigo porque estás más lejos del centro y tienes que recorrer un círculo más grande en el mismo tiempo.
*   Se mide en **metros por segundo ($m/s$)**.
*   **Fórmula:** Depende del radio ($r$).
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
$$ \omega = 2\pi \cdot 2 = 4\pi \approx 12.57\,\mathrm{rad/s} $$

**Paso 3: Calcular la velocidad real ($v$)**
Ahora multiplicamos el giro por el radio:
$$ v = 12.57 \cdot 0.35 \approx 4.4\,\mathrm{m/s} $$

> **Resultado:** El borde de la rueda viaja a **4.4 m/s** (unos 16 km/h).

---

### **Ejemplo 2: El Auto en la Curva**

Un auto entra a una rotonda de $50\,\mathrm{m}$ de radio a una velocidad de $20\,\mathrm{m/s}$. ¿Qué tan fuerte es la aceleración que siente hacia el centro?

![Auto en la curva](/images/fisica/cinematica/mcu/carro-en-mcu.png)

**Análisis:**
Aunque el velocímetro marque siempre 20, el auto está girando. Necesita una aceleración centrípeta ($a_c$) para no salirse de la curva.

**Fórmula:**
$$ a_c = \frac{v^2}{r} $$

**Cálculo:**
$$ a_c = \frac{20^2}{50} = \frac{400}{50} = 8\,\mathrm{m/s^2} $$

> **Interpretación:** Siente una aceleración lateral de $8\,\mathrm{m/s^2}$, casi tan fuerte como la gravedad ($9.8\,\mathrm{m/s^2}$). ¡Es una curva cerrada tomada a alta velocidad!

---

## 📝 **Ponte a Prueba**

### **Ejercicio 1: El Ventilador**

Un ventilador gira a **120 RPM** (revoluciones por minuto). ¿Cuál es su frecuencia en Hz (vueltas por segundo)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si da 120 vueltas en 60 segundos (1 minuto), ¿cuántas da en 1 segundo?

$$ f = \frac{120}{60} = 2\,\mathrm{Hz} $$

**Respuesta:** **2 Hz**.

</details>

---

### **Ejercicio 2: El Carrusel**

Un carrusel tarda **20 segundos** en dar una vuelta completa. ¿Cuál es su velocidad angular?

<details>
<summary>Ver solución</summary>

**Datos:** $T = 20\,\mathrm{s}$.
**Fórmula:** $\omega = \frac{2\pi}{T}$

$$ \omega = \frac{6.28}{20} \approx 0.314\,\mathrm{rad/s} $$

**Respuesta:** **0.314 rad/s**.

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

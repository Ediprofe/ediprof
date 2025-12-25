# 🚀 **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)**

Hasta ahora habíamos estudiado movimientos donde la velocidad nunca cambiaba (MRU). Pero en la vida real, lo más común es que los objetos arranquen, frenen o aumenten su rapidez.

El **MRUA** es aquel movimiento en línea recta donde la **velocidad cambia** de manera uniforme.

---

## 🎯 ¿Qué vas a aprender?

- El concepto intuitivo y matemático de la aceleración.
- Qué significa realmente la unidad $m/s^2$.
- Las características clave que definen al MRUA.
- Cómo la gravedad es simplemente una aceleración natural.

---

## ⚡ **El Concepto de Aceleración**

La **Aceleración** nos dice **qué tan rápido cambia la velocidad** de un objeto.

* Si la velocidad se mantiene igual, la aceleración es **cero** ($a=0$).
* Si la velocidad aumenta o disminuye, existe una **aceleración** ($a \neq 0$).

### **¿Qué significa la unidad m/s²?**

La unidad de medida es **metros por segundo al cuadrado**. Aunque suena complejo, su significado es muy lógico si lo leemos así: **"Metros por segundo, cada segundo"**.

$$
a = \frac{\Delta v}{t} = \frac{\mathrm{m/s}}{\mathrm{s}} = \mathrm{m/s^2}
$$

> **La Regla de Oro:**
> Si un objeto tiene una aceleración de **$2\,\mathrm{m/s^2}$**, significa que su velocidad **aumenta en $2\,\mathrm{m/s}$ por cada segundo que pasa.**

![MRUA](/images/fisica/cinematica/mrua/mrua.png)

---

## ✨ **Características del MRUA**

1.  **Trayectoria Rectilínea:** El objeto se mueve siempre en línea recta.
2.  **Velocidad Variable:** La velocidad no es fija; cambia instante a instante.
3.  **Aceleración Constante:** El ritmo al que cambia la velocidad es siempre el mismo (no cambia de golpe).

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Análisis Detallado (Paso a Paso)**

Vamos a calcular la posición paso a paso para un móvil que parte del reposo ($v_0=0$) con una aceleración constante de $a = 2\,\mathrm{m/s^2}$ durante los primeros 3 segundos.

#### **1. Razonamiento por intervalos (Método Inductivo)**

En el **MRUA**, la velocidad cambia uniformemente, lo que hace que la distancia recorrida en cada segundo sea distinta.

* **Segundo 1 (de $t=0$ a $t=1$):**
    * La velocidad inicial es $0$ y la final es $2\,\mathrm{m/s}$ (aumentó $2$ unidades por la aceleración).
    * La velocidad promedio en este intervalo es $\frac{0+2}{2} = 1\,\mathrm{m/s}$.
    * En 1 segundo a $1\,\mathrm{m/s}$ promedio, recorre **1 metro**.
    * **Posición a $t=1$:** $0 + 1 = \boxed{1\,\mathrm{m}}$.

* **Segundo 2 (de $t=1$ a $t=2$):**
    * Empieza el segundo a $2\,\mathrm{m/s}$ y termina a $4\,\mathrm{m/s}$ (sumamos otros $2$ de aceleración).
    * La velocidad promedio en este intervalo es $\frac{2+4}{2} = 3\,\mathrm{m/s}$.
    * En este segundo recorre **3 metros**.
    * **Posición a $t=2$:** Posición anterior ($1$) + tramo nuevo ($3$) = $\boxed{4\,\mathrm{m}}$.

* **Segundo 3 (de $t=2$ a $t=3$):**
    * Empieza el segundo a $4\,\mathrm{m/s}$ y termina a $6\,\mathrm{m/s}$.
    * La velocidad promedio es $\frac{4+6}{2} = 5\,\mathrm{m/s}$.
    * En este segundo recorre **5 metros**.
    * **Posición a $t=3$:** Posición anterior ($4$) + tramo nuevo ($5$) = $\boxed{9\,\mathrm{m}}$.

---

#### **2. Comprobación con la Fórmula**

La fórmula de posición para objetos que parten del origen y del reposo ($v_0=0, x_0=0$) es:

$$
x = \frac{1}{2} a t^2
$$

Sustituimos $a = 2$:

* **Para $t=1$:** $x = 0.5 \cdot 2 \cdot (1)^2 = \boxed{1\,\mathrm{m}}$
* **Para $t=2$:** $x = 0.5 \cdot 2 \cdot (2)^2 = \boxed{4\,\mathrm{m}}$
* **Para $t=3$:** $x = 0.5 \cdot 2 \cdot (3)^2 = \boxed{9\,\mathrm{m}}$

---

#### **Resumen de Resultados**

| Tiempo ($t$) | Velocidad ($v$) | Razonamiento (Tramo) | Posición Final ($x$) |
| :--- | :--- | :--- | :--- |
| **0 s** | $0\,\mathrm{m/s}$ | Inicio | **0 m** |
| **1 s** | $2\,\mathrm{m/s}$ | Avanzó 1m | **1 m** |
| **2 s** | $4\,\mathrm{m/s}$ | Avanzó 3m más | **4 m** |
| **3 s** | $6\,\mathrm{m/s}$ | Avanzó 5m más | **9 m** |


![Mapa de movimiento MRUA](/images/fisica/cinematica/mrua/mapa-moviiento-mrua.png)

---

### **Ejemplo 2: Caída Libre (La Gravedad)**

Cuando dejas caer algo, su velocidad aumenta constantemente porque la Tierra lo atrae. A esa aceleración natural la llamamos **gravedad** ($g$).

En el mundo real, esta aceleración es de aproximadamente $9.8\,\mathrm{m/s^2}$. Sin embargo, para que puedas hacer los cálculos **mentalmente** y entender la lógica sin distraerte con decimales, en este ejemplo vamos a redondearla.

**Asumiremos:** $g \approx 10\,\mathrm{m/s^2}$.
*(Esto significa que cada segundo que pasa mientras cae, el objeto gana $10\,\mathrm{m/s}$ de velocidad).*

**El Reto:** Calcular cuánto ha caído la piedra en los primeros 3 segundos, **sin usar fórmulas de memoria**, solo usando la lógica inductiva.

#### **1. Razonamiento Lógico (Paso a Paso)**

La clave es entender que **Distancia = Velocidad Promedio $\times$ Tiempo**.

*   **Primer Segundo ($0 \to 1$s):**
    *   Velocidad: Pasa de $0$ a $10\,\mathrm{m/s}$.
    *   **Velocidad Promedio:** $5\,\mathrm{m/s}$ (la mitad de 10).
    *   Distancia recorrida: $5\,\mathrm{m/s} \times 1\,\mathrm{s} = \mathbf{5\,m}$.
    *   **Posición Total:** $\boxed{5\,\mathrm{m}}$.

*   **Segundo Segundo ($1 \to 2$s):**
    *   Velocidad: Pasa de $10$ a $20\,\mathrm{m/s}$.
    *   **Velocidad Promedio:** $15\,\mathrm{m/s}$ (punto medio entre 10 y 20).
    *   Distancia recorrida: $15\,\mathrm{m/s} \times 1\,\mathrm{s} = \mathbf{15\,m}$.
    *   **Posición Total:** $5 \text{ (acumulado)} + 15 \text{ (nuevo)} = \boxed{20\,\mathrm{m}}$.

*   **Tercer Segundo ($2 \to 3$s):**
    *   Velocidad: Pasa de $20$ a $30\,\mathrm{m/s}$.
    *   **Velocidad Promedio:** $25\,\mathrm{m/s}$.
    *   Distancia recorrida: $25\,\mathrm{m/s} \times 1\,\mathrm{s} = \mathbf{25\,m}$.
    *   **Posición Total:** $20 \text{ (acumulado)} + 25 \text{ (nuevo)} = \boxed{45\,\mathrm{m}}$.

#### **Resumen Visual del Movimiento**

| Tiempo ($t$) | Velocidad ($v$) | Velocidad Promedio (Tramo) | Distancia Recorrida (Tramo) | Posición Total ($y$) |
| :--- | :--- | :--- | :--- | :--- |
| **0 s** | $0\,\mathrm{m/s}$ | — | — | **0 m** |
| **1 s** | $10\,\mathrm{m/s}$ | $5\,\mathrm{m/s}$ | $5\,\mathrm{m}$ | **5 m** |
| **2 s** | $20\,\mathrm{m/s}$ | $15\,\mathrm{m/s}$ | $15\,\mathrm{m}$ | **20 m** |
| **3 s** | $30\,\mathrm{m/s}$ | $25\,\mathrm{m/s}$ | $25\,\mathrm{m}$ | **45 m** |

![Análisis - MRUA en caída libre](/images/fisica/cinematica/mrua/mrua-analisis-edificio.png)
---

#### **2. El "Secreto" de la Fórmula ($d = \frac{1}{2}at^2$)**

¿Por qué la fórmula es $\frac{1}{2}at^2$? ¡Míralo con los números del ejemplo anterior!

Si quieres calcular la distancia total a los **3 segundos** de un solo golpe:
1.  La velocidad final es $30\,\mathrm{m/s}$ (porque $v = a \cdot t = 10 \cdot 3$).
2.  La **Velocidad Promedio** de todo el viaje (desde que arrancó hasta el final) es **la mitad** de esa velocidad final: $15\,\mathrm{m/s}$.
3.  **Distancia** = Vel. Promedio $\times$ Tiempo Total = $15 \times 3 = \mathbf{45\,m}$.

**Matemáticamente es lo mismo:**
$$
\text{Distancia} = \underbrace{\left( \frac{a \cdot t}{2} \right)}_{\text{Vel. Promedio}} \cdot t = \frac{1}{2} a t^2
$$

Comprobemos con la fórmula clásica:
$$
d = \frac{1}{2} (10) (3)^2 = 5 \cdot 9 = \mathbf{45\,m}
$$

> **Conclusión:** La fórmula $\frac{1}{2}at^2$ no es magia. Simplemente calcula la **velocidad promedio** del trayecto ($\frac{1}{2}at$) y la multiplica por el tiempo.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1: Auto deportivo**

Un auto deportivo parte del reposo y acelera a $8\,\mathrm{m/s^2}$ durante $5$ segundos. ¿Cuál es su velocidad final?

<details>
<summary>Ver solución</summary>

**Datos:**
- $v_0 = 0\,\mathrm{m/s}$
- $a = 8\,\mathrm{m/s^2}$
- $t = 5\,\mathrm{s}$

**Cálculo:**
$$v = a \cdot t = 8 \times 5 = \boxed{40\,\mathrm{m/s}}$$

> El auto alcanza **40 m/s** (144 km/h).

</details>

---

### **Ejercicio 2: Bicicleta frenando**

Un ciclista viaja a $12\,\mathrm{m/s}$ y frena con una desaceleración de $3\,\mathrm{m/s^2}$. ¿Cuántos segundos tarda en detenerse?

<details>
<summary>Ver solución</summary>

**Análisis:** Cada segundo pierde 3 m/s.

- Inicio: 12 m/s
- 1s: 9 m/s
- 2s: 6 m/s
- 3s: 3 m/s
- 4s: 0 m/s

**Respuesta:** Tarda **4 segundos** en detenerse.

</details>

---

### **Ejercicio 3: Cohete despegando**

Un cohete modelo despega con una aceleración de $15\,\mathrm{m/s^2}$. ¿Qué velocidad tendrá después de 6 segundos?

<details>
<summary>Ver solución</summary>

$$v = a \cdot t = 15\,\mathrm{m/s^2} \times 6\,\mathrm{s} = \boxed{90\,\mathrm{m/s}}$$

> El cohete viajará a **90 m/s**.

</details>

---

### **Ejercicio 4: Lanzamiento vertical**

Una pelota se lanza hacia arriba con una velocidad inicial de $30\,\mathrm{m/s}$. Si la gravedad la desacelera a $10\,\mathrm{m/s^2}$ (aproximado), ¿cuántos segundos tarda en detenerse en el aire?

<details>
<summary>Ver solución</summary>

**Análisis:** Cada segundo pierde 10 m/s.

- Inicio: 30 m/s
- 1s: 20 m/s
- 2s: 10 m/s
- 3s: 0 m/s

**Respuesta:** Tarda **3 segundos** en alcanzar su punto más alto.

</details>

---

### **Ejercicio 5: Frenado de emergencia**

Un conductor pisa el freno y su auto desacelera a $8\,\mathrm{m/s^2}$ desde una velocidad inicial de $40\,\mathrm{m/s}$. ¿Cuánto tiempo tarda en detenerse completamente?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 40\,\mathrm{m/s}$, $a = -8\,\mathrm{m/s^2}$, $v_f = 0$ (se detiene).

**Análisis:** Cada segundo reduce su velocidad en 8 m/s.

- 0s: 40 m/s
- 1s: 32 m/s
- 2s: 24 m/s
- 3s: 16 m/s
- 4s: 8 m/s
- 5s: 0 m/s

**Respuesta:** Tarda **5 segundos** en detenerse.

</details>

---

### **Ejercicio 6: Aceleración de un tren**

Un tren parte del reposo y acelera uniformemente. Después de 12 segundos alcanza una velocidad de $60\,\mathrm{m/s}$. ¿Cuál es su aceleración?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0$ (parte del reposo), $v_f = 60\,\mathrm{m/s}$, $t = 12\,\mathrm{s}$.

**Cálculo:**
$$a = \frac{\Delta v}{t} = \frac{60 - 0}{12} = 5\,\mathrm{m/s^2}$$

**Respuesta:** La aceleración es de **5 m/s²**.

</details>

---

### **Ejercicio 7: Velocidad después de cierto tiempo**

Un ciclista comienza a pedalear con una aceleración de $2\,\mathrm{m/s^2}$. ¿Qué velocidad tiene después de 8 segundos?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0$, $a = 2\,\mathrm{m/s^2}$, $t = 8\,\mathrm{s}$.

**Cálculo:** Cada segundo aumenta 2 m/s.
$$v_f = 0 + 2(8) = 16\,\mathrm{m/s}$$

**Respuesta:** Alcanza una velocidad de **16 m/s**.

</details>

---

### **Ejercicio 8: Cambio de velocidad en caída libre**

Un objeto cae durante 5 segundos. Si partió del reposo y la gravedad es $g = 10\,\mathrm{m/s^2}$, ¿qué velocidad tiene al final?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0$, $a = g = 10\,\mathrm{m/s^2}$, $t = 5\,\mathrm{s}$.

**Cálculo:**
$$v_f = 0 + 10(5) = 50\,\mathrm{m/s}$$

**Respuesta:** Su velocidad final es de **50 m/s**.

</details>

---

### **Ejercicio 9: Análisis de gráfica de velocidad**

Una moto acelera uniformemente desde 0 a 25 m/s en 5 segundos. ¿Cuál es su aceleración?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0\,\mathrm{m/s}$, $v_f = 25\,\mathrm{m/s}$, $t = 5\,\mathrm{s}$.

**Cálculo:**
$$a = \frac{25 - 0}{5} = 5\,\mathrm{m/s^2}$$

**Respuesta:** Su aceleración es de **5 m/s²**.

</details>

---

### **Ejercicio 10: Comparación de aceleraciones**

Dos autos aceleran: Auto A de 0 a 30 m/s en 6 segundos, Auto B de 0 a 40 m/s en 8 segundos. ¿Cuál tiene mayor aceleración?

<details>
<summary>Ver solución</summary>

**Auto A:** $a_A = \frac{30}{6} = 5\,\mathrm{m/s^2}$

**Auto B:** $a_B = \frac{40}{8} = 5\,\mathrm{m/s^2}$

**Respuesta:** Ambos tienen la misma aceleración de **5 m/s²**, aunque B alcance mayor velocidad final.

</details>

---

## 🔑 Resumen

- **Aceleración ($a$):** Es el cambio de velocidad por unidad de tiempo.
- **Unidad ($m/s^2$):** Significa cuántos "metros por segundo" aumenta o disminuye la velocidad cada segundo.
- **Gravedad ($g$):** Es una aceleración constante de aprox. $9.8\,\mathrm{m/s^2}$ que atrae los objetos hacia la Tierra.
- **MRUA:** Movimiento Rectilíneo Uniformemente Acelerado (trayectoria recta, aceleración constante).

# 🍎 **Caída Libre**

## 🎯 **¿Qué vas a aprender?**

En esta lección aprenderás a:

*   **Comprender** que la caída libre es un movimiento con aceleración constante provocada por la gravedad.
*   **Relacionar** las fórmulas del MRUA con las de caída libre.
*   **Calcular** la velocidad, altura y tiempo de caída de objetos.
*   **Resolver** problemas prácticos aplicando los conceptos de gravedad.

---

## 🌍 **¿Qué es la Caída Libre?**

La **Caída Libre** es un movimiento donde un objeto cae **únicamente bajo la influencia de la gravedad**, sin ninguna otra fuerza que lo empuje o lo frene (idealmente, sin fricción del aire).

En la Tierra, la aceleración de la gravedad ($g$) es aproximadamente constante cerca de la superficie:

$$
g = 9.8\,\mathrm{m/s^2} \approx 10\,\mathrm{m/s^2}
$$

> 💡 **Significado:** Cada segundo que cae un objeto, su velocidad **aumenta en 10 m/s**.

| Tiempo de caída | Velocidad |
| :--- | :--- |
| $t = 0\,\mathrm{s}$ | $0\,\mathrm{m/s}$ |
| $t = 1\,\mathrm{s}$ | $10\,\mathrm{m/s}$ |
| $t = 2\,\mathrm{s}$ | $20\,\mathrm{m/s}$ |
| $t = 3\,\mathrm{s}$ | $30\,\mathrm{m/s}$ |

---

## 🔗 **Conexión con MRUA: Deducción de las Fórmulas**

La **caída libre** es simplemente un **MRUA** donde la aceleración es la **gravedad**.

### **Las fórmulas del MRUA se transforman así:**

1.  **Velocidad:**
    *   MRUA: $v_f = v_i + a \cdot t$
    *   Caída Libre: $v_f = v_i + g \cdot t$

2.  **Posición (Altura):**
    *   MRUA: $x_f = x_i + v_i \cdot t + \frac{1}{2} a \cdot t^2$
    *   Caída Libre: $h = v_i \cdot t + \frac{1}{2} g \cdot t^2$ (asumiendo altura inicial 0 o midiendo distancia recorrida)

3.  **Sin tiempo:**
    *   MRUA: $v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x$
    *   Caída Libre: $v_f^2 = v_i^2 + 2 \cdot g \cdot h$

### **Caso especial: Objeto que se suelta (parte del reposo)**

Si el objeto **se suelta** (no se lanza), entonces su velocidad inicial es cero ($v_i = 0$). Las fórmulas se simplifican:

| Fórmula General | Con $v_i = 0$ | Fórmula Simplificada |
| :--- | :--- | :--- |
| $v_f = v_i + g \cdot t$ | $v_f = 0 + g \cdot t$ | $$v_f = g \cdot t$$ |
| $h = v_i \cdot t + \frac{1}{2} g \cdot t^2$ | $h = 0 + \frac{1}{2} g \cdot t^2$ | $$h = \frac{1}{2} g \cdot t^2$$ |
| $v_f^2 = v_i^2 + 2gh$ | $v_f^2 = 0 + 2gh$ | $$v_f^2 = 2gh$$ |

> 💡 **Conclusión:** Las fórmulas de caída libre son las **mismas** del MRUA con $a = g$ y $v_i = 0$ (cuando se suelta).

---

## ⚙️ **Ejemplo 1 — Piedra soltada desde un puente**

Un estudiante suelta una piedra desde lo alto de un puente. La piedra cae libremente durante **3 segundos** antes de tocar el agua. ¿Con qué velocidad llegó al agua?

### 📝 **Solución Paso a Paso**

![Piedra soltada desde el puente](/images/fisica/cinematica/mrua/piedra-del-puente.png)

**Datos:**
*   $v_i = 0$ (se suelta)
*   $t = 3\,\mathrm{s}$
*   $g = 10\,\mathrm{m/s^2}$
*   **Incógnita:** $v_f = ?$

**Fórmula:**
$$v_f = v_i + g \cdot t$$

**Cálculo:**
$$v_f = 0 + 10 \cdot 3 = 30\,\mathrm{m/s}$$

> ✅ La piedra llega al agua a **30 m/s** (equivalente a 108 km/h).

---

## ⚙️ **Ejemplo 2 — Paracaidista saltando de un avión**

Un paracaidista salta desde un avión y cae en caída libre durante **4 segundos** antes de abrir el paracaídas. ¿Qué distancia recorrió?

### 📝 **Solución Paso a Paso**
![Paracaidista](/images/fisica/cinematica/mrua/paracaidista.png)

**Datos:**
*   $v_i = 0$
*   $t = 4\,\mathrm{s}$
*   $g = 10\,\mathrm{m/s^2}$
*   **Incógnita:** $h = ?$

**Fórmula:**
$$h = \frac{1}{2} g \cdot t^2$$

**Cálculo:**
$$h = \frac{1}{2} \cdot 10 \cdot (4)^2 = 5 \cdot 16 = 80\,\mathrm{m}$$

**¿Con qué velocidad llegó?**
$$v_f = g \cdot t = 10 \cdot 4 = 40\,\mathrm{m/s}$$

> ✅ El paracaidista cayó **80 metros** y alcanzó **144 km/h** antes de abrir el paracaídas.

---

## ⚙️ **Ejemplo 3 — Moneda desde un edificio**

Una moneda se deja caer desde un edificio de **45 metros** de altura. ¿Cuánto tiempo tarda en llegar al suelo?

### 📝 **Solución Paso a Paso**

![Moneda desde el edificio](/images/fisica/cinematica/mrua/moneda-cayendo.png)

**Datos:**
*   $v_i = 0$
*   $h = 45\,\mathrm{m}$
*   $g = 10\,\mathrm{m/s^2}$ (se aproxima)
*   **Incógnita:** $t = ?$

**Fórmula:**
$$h = \frac{1}{2} g \cdot t^2$$

**Despejamos $t$:**
$$t^2 = \frac{2h}{g} \Rightarrow t = \sqrt{\frac{2h}{g}}$$

**Cálculo:**
$$t = \sqrt{\frac{2 \cdot 45}{10}} = \sqrt{\frac{90}{10}} = \sqrt{9} = 3\,\mathrm{s}$$

> ✅ La moneda tarda **3 segundos** en llegar al suelo.

---

## 📝 **Ejercicios de Práctica**

Pon a prueba tus conocimientos con estos 10 ejercicios. Intenta resolverlos antes de mirar la solución.

### **Ejercicio 1: Altura desde el tiempo**
Un niño suelta una pelota desde una ventana. La pelota cae durante **2 segundos**. ¿A qué altura está la ventana?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 0$, $t = 2\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$

**Fórmula:** $h = \frac{1}{2} g \cdot t^2$

**Cálculo:**
$$h = \frac{1}{2} \cdot 10 \cdot (2)^2 = 5 \cdot 4 = 20\,\mathrm{m}$$

> La ventana está a **20 metros** de altura.

</details>

---

### **Ejercicio 2: Velocidad final**
Se deja caer una maceta desde una terraza y tarda **4 segundos** en llegar al suelo. ¿Con qué velocidad impacta el suelo?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 0$, $t = 4\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$

**Fórmula:** $v_f = g \cdot t$

**Cálculo:**
$$v_f = 10 \cdot 4 = 40\,\mathrm{m/s}$$

> La maceta impacta a **40 m/s**.

</details>

---

### **Ejercicio 3: Altura desde la velocidad**
¿Desde qué altura se debe dejar caer un objeto para que golpee el suelo con una velocidad de **50 m/s**?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 0$, $v_f = 50\,\mathrm{m/s}$, $g = 10\,\mathrm{m/s^2}$

**Fórmula:** $v_f^2 = v_i^2 + 2gh \Rightarrow v_f^2 = 2gh$

**Despeje:**
$$h = \frac{v_f^2}{2g}$$

**Cálculo:**
$$h = \frac{50^2}{2 \cdot 10} = \frac{2500}{20} = 125\,\mathrm{m}$$

> Se debe dejar caer desde **125 metros**.

</details>

---

### **Ejercicio 4: Tiempo de caída**
Una piedra se deja caer desde un puente de **80 metros** de altura. ¿Cuánto tiempo tarda en tocar el agua?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $h = 80\,\mathrm{m}$, $g = 10\,\mathrm{m/s^2}$, $v_i = 0$.
**Fórmula:** $h = \frac{1}{2}g t^2 \Rightarrow t = \sqrt{\frac{2h}{g}}$
**Cálculo:**
$$t = \sqrt{\frac{2(80)}{10}} = \sqrt{16} = 4\,\mathrm{s}$$

</details>

---

### **Ejercicio 5: Distancia por intervalos**
Un objeto cae libremente. ¿Qué distancia recorre **solo** durante el segundo segundo de su caída (entre $t=1$ y $t=2$)?

<details>
<summary><strong>Ver solución</strong></summary>

Calculamos la posición a $t=1$ y a $t=2$:
1. $h(1) = 5(1)^2 = 5\,\mathrm{m}$
2. $h(2) = 5(2)^2 = 20\,\mathrm{m}$
**Distancia recorrida:** $20 - 5 = 15\,\mathrm{m}$.

</details>

---

### **Ejercicio 6: Velocidad intermedia**
Se deja caer un balón desde un edificio muy alto. ¿Cuál es su velocidad después de **3.5 segundos**?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $t = 3.5\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$.
**Fórmula:** $v_f = g \cdot t$
**Cálculo:**
$$v_f = 10 \cdot 3.5 = 35\,\mathrm{m/s}$$

</details>

---

### **Ejercicio 7: Comparación de tiempos**
Un objeto A se deja caer desde 20m y un objeto B desde 80m. ¿Cuántas veces más tiempo tarda B en caer comparado con A?

<details>
<summary><strong>Ver solución</strong></summary>

**Tiempo A:** $t_A = \sqrt{2(20)/10} = \sqrt{4} = 2\,\mathrm{s}$
**Tiempo B:** $t_B = \sqrt{2(80)/10} = \sqrt{16} = 4\,\mathrm{s}$
**Comparación:** $4 / 2 = 2$.
El objeto B tarda el **doble** de tiempo.

</details>

---

### **Ejercicio 8: Tiempo para velocidad**
Si un objeto impacta el suelo a **60 m/s**, ¿cuánto tiempo estuvo cayendo?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_f = 60\,\mathrm{m/s}$, $g = 10\,\mathrm{m/s^2}$.
**Fórmula:** $v_f = g \cdot t \Rightarrow t = v_f / g$
**Cálculo:**
$$t = 60 / 10 = 6\,\mathrm{s}$$

</details>

---

### **Ejercicio 9: Altura pequeña**
Un gato salta (se deja caer) desde una rama y tarda **0.8 segundos** en aterrizar. ¿A qué altura estaba la rama?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $t = 0.8\,\mathrm{s}$.
**Fórmula:** $h = \frac{1}{2}g t^2 = 5 t^2$
**Cálculo:**
$$h = 5 \cdot (0.8)^2 = 5 \cdot 0.64 = 3.2\,\mathrm{m}$$

</details>

---

### **Ejercicio 10: Profundidad de un pozo**
Se deja caer una moneda en un pozo y se escucha el golpe **3 segundos** después. Despreciando el tiempo que tarda el sonido en subir, ¿qué profundidad tiene el pozo?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $t = 3\,\mathrm{s}$.
**Fórmula:** $h = 5 t^2$
**Cálculo:**
$$h = 5 \cdot (3)^2 = 5 \cdot 9 = 45\,\mathrm{m}$$

</details>

---

## 🎓 **Resumen**

![Resumen - Caída libre](/images/fisica/cinematica/mrua/resumen-caida-libre.png)

*   La **Caída Libre** es un MRUA donde la única aceleración es la gravedad ($g \approx 10\,\mathrm{m/s^2}$).
*   Todos los objetos caen con la misma aceleración, independientemente de su masa (sin aire).
*   Las fórmulas son las mismas del MRUA, sustituyendo $a$ por $g$ y $x$ por $h$.
*   Si el objeto **se suelta**, la velocidad inicial es cero ($v_i = 0$).
*   **Fórmulas Clave (partiendo del reposo):**
    *   $v_f = g \cdot t$
    *   $h = \frac{1}{2} g \cdot t^2$
    *   $v_f^2 = 2gh$

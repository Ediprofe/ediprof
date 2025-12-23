# 🚀 **Lanzamiento Vertical**

## 🎯 **¿Qué vas a aprender?**

En esta lección aprenderás a:

*   **Comprender** cómo actúa la gravedad cuando lanzamos un objeto hacia arriba.
*   **Analizar** las tres fases del movimiento: subida, punto más alto y bajada.
*   **Aplicar** correctamente la convención de signos para velocidad y gravedad.
*   **Calcular** la altura máxima y el tiempo de vuelo de un objeto lanzado verticalmente.

---

## 🎯 **¿Qué es el Lanzamiento Vertical?**

El **Lanzamiento Vertical** ocurre cuando lanzamos un objeto hacia arriba con una velocidad inicial. La gravedad **desacelera** el objeto hasta que se detiene momentáneamente en el punto más alto, y luego lo hace caer acelerándolo.

> 💡 **Idea clave:** La gravedad siempre apunta hacia abajo. Cuando el objeto sube, la gravedad lo frena. Cuando baja, lo acelera.

### **Dos fases del movimiento:**

| Fase | Descripción | ¿Qué pasa con la velocidad? |
| :--- | :--- | :--- |
| **Subida** | El objeto sube, la gravedad lo frena | Disminuye hasta llegar a 0 |
| **Punto más alto** | El objeto se detiene momentáneamente | $v = 0$ |
| **Bajada** | El objeto cae, la gravedad lo acelera | Aumenta (hacia abajo) |

---

## 🔗 **Conexión con MRUA: Deducción con Convención de Signos**

El lanzamiento vertical es un **MRUA** con aceleración constante (la gravedad). Para resolver problemas, es fundamental establecer una **convención de signos**.

### **Estableciendo la Convención de Signos**

| Dirección | Signo | Ejemplo |
| :--- | :--- | :--- |
| **Hacia arriba** | $+$ (positivo) | Velocidad inicial $v_i > 0$ |
| **Hacia abajo** | $-$ (negativo) | Gravedad $g = -10\,\mathrm{m/s^2}$ |

> 💡 **Por qué g es negativo:** La gravedad siempre apunta hacia abajo. Si definimos "arriba" como positivo, entonces la aceleración de la gravedad es **negativa**.

### **Paso 1: Fórmulas del MRUA**

| Fórmula MRUA | Nombre |
| :--- | :--- |
| $v_f = v_i + a \cdot t$ | Velocidad |
| $x_f = x_i + v_i \cdot t + \frac{1}{2} a \cdot t^2$ | Posición |
| $v_f^2 = v_i^2 + 2ax$ | Sin conocer el tiempo |

### **Paso 2: Aplicar a = −g (gravedad hacia abajo)**

Sustituimos $a$ por $-g$ en las fórmulas:

| Fórmula MRUA | Sustitución | Fórmula Lanzamiento Vertical |
| :--- | :--- | :--- |
| $v_f = v_i + a \cdot t$ | $a = -g$ | $$v_f = v_i - g \cdot t$$ |
| $x_f = x_i + v_i \cdot t + \frac{1}{2} a \cdot t^2$ | $a = -g$, $x = h$ | $$h = v_i \cdot t - \frac{1}{2} g \cdot t^2$$ |
| $v_f^2 = v_i^2 + 2ax$ | $a = -g$, $x = h$ | $$v_f^2 = v_i^2 - 2gh$$ |

> ⚠️ **Nota:** El signo **negativo** aparece porque la gravedad **se opone** al movimiento hacia arriba (desacelera el objeto).

### **Paso 3: Altura máxima (cuando v = 0)**

En el punto más alto, el objeto **se detiene** ($v_f = 0$) antes de caer.

De $v_f^2 = v_i^2 - 2gh$, cuando $v_f = 0$:

$$
0 = v_i^2 - 2gh_{\text{max}} \Rightarrow h_{\text{max}} = \frac{v_i^2}{2g}
$$

De $v_f = v_i - gt$, cuando $v_f = 0$:

$$
0 = v_i - gt_{\text{subida}} \Rightarrow t_{\text{subida}} = \frac{v_i}{g}
$$

---

## ⚙️ **Ejemplo 1 — Pelota lanzada hacia arriba**

Un jugador lanza una pelota verticalmente hacia arriba con velocidad inicial de **$20\,\mathrm{m/s}$**. ¿Cuánto tiempo tarda en alcanzar el punto más alto?

![Tiempo al punto más alto](/images/fisica/cinematica/mrua/tiempo-al-punto-mas-alto.png)

### 📝 **Solución Paso a Paso**

**Concepto clave:** En el punto más alto, la velocidad es **cero** (el objeto se detiene antes de caer).

**Datos:**
*   $v_i = 20\,\mathrm{m/s}$ (hacia arriba)
*   $v_f = 0$ (en el punto más alto)
*   $g = 10\,\mathrm{m/s^2}$

**Paso 1: Elegir la fórmula general**

Usamos la ecuación de velocidad del MRUA:
$$v_f = v_i - g \cdot t$$

**Paso 2: Sustituir los valores conocidos**

Como en el punto más alto $v_f = 0$:
$$0 = 20 - 10 \cdot t$$

**Paso 3: Simplificar y despejar**
$$10 \cdot t = 20$$
$$t = \frac{20}{10} = 2\,\mathrm{s}$$

> ✅ La pelota tarda **2 segundos** en llegar al punto más alto.

---

## ⚙️ **Ejemplo 2 — Altura máxima de un cohete de agua**

Un cohete de agua es lanzado hacia arriba con velocidad inicial de **$30\,\mathrm{m/s}$**. ¿Qué altura máxima alcanza?

![Lanzamiento de cohete](/images/fisica/cinematica/mrua/cohete-lanzamiento-vertical.png)

### 📝 **Solución Paso a Paso**

**Concepto clave:** Usamos la fórmula sin tiempo porque conocemos velocidades pero no sabemos cuánto tarda.

**Datos:**
*   $v_i = 30\,\mathrm{m/s}$ (velocidad inicial)
*   $v_f = 0$ (en altura máxima se detiene)
*   $g = 10\,\mathrm{m/s^2}$
*   $h = ?$ (lo que buscamos)

**Paso 1: Elegir la fórmula general**

Usamos la ecuación sin tiempo del MRUA:
$$v_f^2 = v_i^2 - 2gh$$

**Paso 2: Sustituir valores conocidos**

Como $v_f = 0$ en el punto más alto:
$$0^2 = 30^2 - 2(10)h$$
$$0 = 900 - 20h$$

**Paso 3: Despejar la altura**
$$20h = 900$$
$$h = \frac{900}{20} = 45\,\mathrm{m}$$

> ✅ El cohete alcanza una altura máxima de **45 metros**.

---

## ⚙️ **Ejemplo 3 — Tiempo de vuelo total**

Una piedra se lanza hacia arriba con velocidad de **$40\,\mathrm{m/s}$**. ¿Cuánto tiempo tarda en volver al punto de lanzamiento?

![Tiempo total de vuelo](/images/fisica/cinematica/mrua/lanzamiento-vertical-tiempo-de-vuelo.png)

### 📝 **Solución Paso a Paso**

**Concepto clave:** El tiempo total es el doble del tiempo de subida (por simetría: lo que sube tarda lo mismo en bajar).

**Datos:**
*   $v_i = 40\,\mathrm{m/s}$
*   $g = 10\,\mathrm{m/s^2}$

**Paso 1: Calcular tiempo de subida**

En el punto más alto, $v_f = 0$. Usamos:
$$v_f = v_i - g \cdot t_{\text{subida}}$$

Sustituimos:
$$0 = 40 - 10 \cdot t_{\text{subida}}$$

Despejamos:
$$t_{\text{subida}} = \frac{40}{10} = 4\,\mathrm{s}$$

**Paso 2: Calcular tiempo total**

Por simetría (sin fricción del aire):
$$t_{\text{total}} = 2 \times t_{\text{subida}} = 2 \times 4 = 8\,\mathrm{s}$$

> ✅ La piedra tarda **8 segundos** en volver a la mano del lanzador.

---

## 📝 **Ejercicios de Práctica**

Pon a prueba tus conocimientos con estos 10 ejercicios. Intenta resolverlos antes de mirar la solución.

### **Ejercicio 1: Altura Máxima**

Se lanza una flecha hacia arriba con una velocidad de **$50\,\mathrm{m/s}$**. ¿Qué altura máxima alcanza?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 50\,\mathrm{m/s}$, $g = 10\,\mathrm{m/s^2}$, $v_f = 0$ (en el punto más alto).

**Fórmula:** $v_f^2 = v_i^2 - 2gh \Rightarrow h_{\text{max}} = \frac{v_i^2}{2g}$

**Cálculo:**
$$h_{\text{max}} = \frac{50^2}{2 \cdot 10} = \frac{2500}{20} = 125\,\mathrm{m}$$

> La flecha alcanza **125 metros** de altura.

</details>

---

### **Ejercicio 2: Velocidad Inicial desde Tiempo Total**

Un balón es pateado verticalmente hacia arriba y tarda **6 segundos** en volver al suelo. ¿Con qué velocidad inicial fue lanzado?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $t_{\text{total}} = 6\,\mathrm{s}$.
Sabemos que $t_{\text{subida}} = \frac{t_{\text{total}}}{2} = 3\,\mathrm{s}$.

**Fórmula:** En el punto más alto, $v_f = 0$:
$$v_f = v_i - g \cdot t \Rightarrow 0 = v_i - 10(3)$$

**Despeje:**
$$v_i = 30\,\mathrm{m/s}$$

> El balón fue lanzado a **30 m/s**.

</details>

---

### **Ejercicio 3: Velocidad en un Instante**

¿Qué velocidad tendrá una piedra lanzada hacia arriba con $v_i = 40\,\mathrm{m/s}$ después de **5 segundos**?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 40\,\mathrm{m/s}$, $t = 5\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$.

**Fórmula:** $v_f = v_i - g \cdot t$

**Cálculo:**
$$v_f = 40 - 10(5) = 40 - 50 = -10\,\mathrm{m/s}$$

> La velocidad es **-10 m/s**. El signo negativo indica que la piedra ya pasó el punto más alto y está **cayendo** a 10 m/s.

</details>

---

### **Ejercicio 4: Tiempo al Punto Más Alto**

Un cohete de juguete se lanza verticalmente con $v_i = 60\,\mathrm{m/s}$. ¿Cuánto tiempo tarda en alcanzar el punto más alto?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 60\,\mathrm{m/s}$, $v_f = 0$, $g = 10\,\mathrm{m/s^2}$.

**Fórmula:** $v_f = v_i - g \cdot t$

**Sustituir:**
$$0 = 60 - 10t$$
$$t = \frac{60}{10} = 6\,\mathrm{s}$$

> Tarda **6 segundos** en alcanzar el punto más alto.

</details>

---

### **Ejercicio 5: Altura en un Instante**

Una pelota se lanza hacia arriba con $v_i = 25\,\mathrm{m/s}$. ¿A qué altura estará después de **2 segundos**?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 25\,\mathrm{m/s}$, $t = 2\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$.

**Fórmula:** $h = v_i \cdot t - \frac{1}{2}g \cdot t^2$

**Cálculo:**
$$h = 25(2) - \frac{1}{2}(10)(2^2)$$
$$h = 50 - 5(4) = 50 - 20 = 30\,\mathrm{m}$$

> A los 2 segundos estará a **30 metros** de altura.

</details>

---

### **Ejercicio 6: Velocidad de Regreso**

Si lanzas una moneda hacia arriba con $v_i = 15\,\mathrm{m/s}$, ¿con qué velocidad regresará a tu mano?

<details>
<summary><strong>Ver solución</strong></summary>

**Concepto:** Por simetría, la velocidad de regreso es igual a la velocidad inicial pero con **signo contrario**.

**Respuesta:** $v_f = -15\,\mathrm{m/s}$ (hacia abajo).

> Regresa a **15 m/s hacia abajo**.

</details>

---

### **Ejercicio 7: Tiempo de Vuelo Total**

Una roca se lanza verticalmente hacia arriba desde el suelo con $v_i = 35\,\mathrm{m/s}$. ¿Cuánto tiempo permanece en el aire antes de regresar al suelo?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 35\,\mathrm{m/s}$.

**Paso 1:** Tiempo de subida hasta $v_f = 0$:
$$t_{\text{subida}} = \frac{v_i}{g} = \frac{35}{10} = 3.5\,\mathrm{s}$$

**Paso 2:** Tiempo total (por simetría):
$$t_{\text{total}} = 2 \times 3.5 = 7\,\mathrm{s}$$

> Permanece **7 segundos** en el aire.

</details>

---

### **Ejercicio 8: Velocidad Inicial desde Altura**

Un proyectil alcanza una altura máxima de **20 metros**. ¿Con qué velocidad inicial fue lanzado?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $h_{\text{max}} = 20\,\mathrm{m}$, $g = 10\,\mathrm{m/s^2}$.

**Fórmula:** $h_{\text{max}} = \frac{v_i^2}{2g}$

**Despeje:**
$$v_i^2 = 2gh_{\text{max}} = 2(10)(20) = 400$$
$$v_i = \sqrt{400} = 20\,\mathrm{m/s}$$

> Fue lanzado a **20 m/s**.

</details>

---

### **Ejercicio 9: Comparación de Alturas**

Dos objetos se lanzan hacia arriba. El objeto A con $v_i = 20\,\mathrm{m/s}$ y el objeto B con $v_i = 40\,\mathrm{m/s}$. ¿Cuántas veces más alto sube B que A?

<details>
<summary><strong>Ver solución</strong></summary>

**Altura A:** $h_A = \frac{20^2}{2(10)} = \frac{400}{20} = 20\,\mathrm{m}$

**Altura B:** $h_B = \frac{40^2}{2(10)} = \frac{1600}{20} = 80\,\mathrm{m}$

**Comparación:** $\frac{h_B}{h_A} = \frac{80}{20} = 4$

> El objeto B sube **4 veces** más alto que A.

</details>

---

### **Ejercicio 10: Altura en Descenso**

Un objeto fue lanzado hacia arriba con $v_i = 30\,\mathrm{m/s}$. Si después de **4 segundos** está bajando, ¿a qué altura se encuentra en ese momento?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_i = 30\,\mathrm{m/s}$, $t = 4\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$.

**Fórmula:** $h = v_i \cdot t - \frac{1}{2}g \cdot t^2$

**Cálculo:**
$$h = 30(4) - \frac{1}{2}(10)(4^2)$$
$$h = 120 - 5(16) = 120 - 80 = 40\,\mathrm{m}$$

> A los 4 segundos está a **40 metros** de altura (en descenso).

</details>

---

## 🎓 **Resumen**

![Resumen: lanzamiento vertical](/images/fisica/cinematica/mrua/resumen-lanzamiento-vertical.png)

*   El **Lanzamiento Vertical** es un MRUA donde la gravedad actúa en contra del movimiento inicial.
*   **Convención de signos:**
    *   Hacia arriba: **Positivo (+)**
    *   Hacia abajo: **Negativo (-)** (Gravedad $g = -10\,\mathrm{m/s^2}$)
*   **Punto más alto:** La velocidad instantánea es **cero** ($v_f = 0$).
*   **Simetría:** El tiempo de subida es igual al tiempo de bajada (al mismo nivel). La velocidad de llegada es igual a la de partida pero con signo contrario.
*   **Fórmulas clave:**
    *   $v_f = v_i - g \cdot t$
    *   $h = v_i \cdot t - \frac{1}{2} g \cdot t^2$
    *   $h_{\text{max}} = \frac{v_i^2}{2g}$


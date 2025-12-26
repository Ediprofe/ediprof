# **Caída Libre**

Un martillo y una pluma, si no existiera el aire, caerían a la misma velocidad. Galileo lo sospechó, Newton lo explicó y un astronauta lo probó en la Luna. La **Caída Libre** es el ejemplo más puro de movimiento acelerado.

---

## 🎯 ¿Qué vas a aprender?

- Por qué en el vacío todos los objetos caen igual.
- El valor de la gravedad y cómo usarlo en cálculos.
- Fórmulas simplificadas para objetos que se "dejan caer".
- Calcular la profundidad de un precipicio con solo un reloj.

---

## 🌍 **¿Qué es la Caída Libre?**

Es un movimiento vertical donde **la única fuerza que actúa es la gravedad**. No hay motores, ni paracaídas, ni fricción del aire.

En la Tierra, esta atracción provoca una aceleración constante llamada **Gravedad ($g$)**.

$$
g \approx 9.8\,\mathrm{m/s^2} \approx 10\,\mathrm{m/s^2}
$$

> **Significado:** Cada segundo que cae, gana **$10\,\mathrm{m/s}$** de velocidad.

| Tiempo | Velocidad ($v = 10 \cdot t$) |
| :---: | :---: |
| 0 s | 0 m/s |
| 1 s | 10 m/s |
| 2 s | 20 m/s |
| 3 s | 30 m/s |

---

## 🔗 **Fórmulas Simplificadas**

La Caída Libre es un MRUA. Pero como casi siempre "soltamos" el objeto ($v_i = 0$), las fórmulas se vuelven diminutas:

### 1. Velocidad de Impacto
$$
v_f = g \cdot t
$$

### 2. Altura de Caída
$$
h = \frac{1}{2} g \cdot t^2
$$

### 3. Velocidad sin Tiempo
$$
v_f^2 = 2 \cdot g \cdot h
$$

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Dejando caer una piedra**

Desde un puente sueltas una piedra y tarda **3 segundos** en chocar con el agua. ¿A qué altura está el puente? (Usa $g = 10\,\mathrm{m/s^2}$).

![altura-de-la-piedra](https://cdn.ediprofe.com/img/fisica/89oh-altura-de-la-piedra.webp)


**Datos:**
- Tiempo ($t$) = $3\,\mathrm{s}$
- Gravedad ($g$) = $10\,\mathrm{m/s^2}$
- Altura ($h$) = ?

**Razonamiento:**
Usamos la fórmula de altura.

$$
h = \frac{1}{2} g \cdot t^2
$$

**Cálculo:**

$$
h = \frac{1}{2}(10) \cdot (3^2) = 5 \cdot 9
$$

**Resultado:**

$$
\boxed{45\,\mathrm{m}}
$$

---

### **Ejemplo 2: Velocidad de impacto**

¿Con qué velocidad golpea esa misma piedra el agua?

![piedra-del-puente](https://cdn.ediprofe.com/img/fisica/zj93-piedra-del-puente.webp)

**Datos:**
- Tiempo ($t$) = $3\,\mathrm{s}$

**Razonamiento:**
Cada segundo gana 10 m/s.

$$
v_f = g \cdot t
$$

**Cálculo:**

$$
v_f = 10 \cdot 3
$$

**Resultado:**

$$
\boxed{30\,\mathrm{m/s}}
$$
(¡Equivale a 108 km/h!)

---

### **Ejemplo 3: Tiempo de Caída desde una Altura Conocida**

Una moneda se deja caer desde un edificio de **$80\,\mathrm{m}$** de altura. ¿Cuánto tiempo tarda en llegar al suelo?

**Datos:**
- $h = 80\,\mathrm{m}$
- $g = 10\,\mathrm{m/s^2}$

**Razonamiento:**
Debemos despejar el tiempo de la fórmula de altura.

$$
h = \frac{1}{2} g \cdot t^2 \rightarrow t = \sqrt{\frac{2h}{g}}
$$

**Cálculo:**

$$
t = \sqrt{\frac{2(80)}{10}} = \sqrt{16}
$$

**Resultado:**

$$
\boxed{4\,\mathrm{s}}
$$

---

### **Ejemplo 4: Altura desde la Velocidad de Impacto**

Un objeto golpea el suelo a **$50\,\mathrm{m/s}$**. ¿Desde qué altura cayó?

**Datos:**
- $v_f = 50\,\mathrm{m/s}$
- $g = 10\,\mathrm{m/s^2}$

**Razonamiento:**
Usamos la fórmula sin tiempo y despejamos la altura.

$$
v_f^2 = 2gh \rightarrow h = \frac{v_f^2}{2g}
$$

**Cálculo:**

$$
h = \frac{50^2}{20} = \frac{2500}{20}
$$

**Resultado:**

$$
\boxed{125\,\mathrm{m}}
$$

---

### **Ejemplo 5: Distancia en el Tercer Segundo**

¿Qué distancia recorre un objeto en caída libre **SOLO durante el tercer segundo** (entre $t=2$ y $t=3$)?

**Datos:**
- $g = 10\,\mathrm{m/s^2}$

**Razonamiento:**
Calculamos la posición a $t=2$ y a $t=3$, luego restamos.

**Altura a $t=2$:**

$$
h_2 = \frac{1}{2}(10)(2^2) = 20\,\mathrm{m}
$$

**Altura a $t=3$:**

$$
h_3 = \frac{1}{2}(10)(3^2) = 45\,\mathrm{m}
$$

**Distancia en ese intervalo:**

$$
\Delta h = 45 - 20
$$

**Resultado:**

$$
\boxed{25\,\mathrm{m}}
$$

(Nota: en MRUA, la distancia recorrida **no es igual** cada segundo).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Sueltas una moneda desde un balcón y tarda 2 segundos en caer. ¿Altura del balcón? ($g=10$)**

<details>
<summary>Ver solución</summary>

**Datos:** $t=2, g=10$.
**Fórmula:** $h = 5 t^2$.
**Cálculo:**
$$h = 5(2^2) = 5(4)$$
**Resultado:**
$$\boxed{20\,\mathrm{m}}$$

</details>

### Ejercicio 2
**Un paracaidista cae libremente por 5 segundos antes de abrir el paracaídas. ¿Qué velocidad alcanza? ($g=10$)**

<details>
<summary>Ver solución</summary>

**Datos:** $t=5$.
**Fórmula:** $v_f = 10 t$.
**Cálculo:**
$$v_f = 10(5)$$
**Resultado:**
$$\boxed{50\,\mathrm{m/s}}$$

</details>

### Ejercicio 3
**¿Desde qué altura cayó un objeto si golpea el suelo a $40\,\mathrm{m/s}$? ($g=10$)**

<details>
<summary>Ver solución</summary>

**Datos:** $v_f=40$. Sin tiempo.
**Fórmula:** $v_f^2 = 2gh \rightarrow h = v_f^2 / 2g$.
**Cálculo:**
$$h = \frac{40^2}{20} = \frac{1600}{20}$$
**Resultado:**
$$\boxed{80\,\mathrm{m}}$$

</details>

### Ejercicio 4
**Una manzana cae de un árbol de 5 metros. ¿Cuánto tarda en llegar al suelo? ($g=10$)**

<details>
<summary>Ver solución</summary>

**Datos:** $h=5$.
**Fórmula:** $h = 5 t^2 \rightarrow t = \sqrt{h/5}$.
**Cálculo:**
$$t = \sqrt{5/5} = \sqrt{1}$$
**Resultado:**
$$\boxed{1\,\mathrm{s}}$$

</details>

### Ejercicio 5
**¿Qué distancia recorre un objeto en caída libre SOLAMENTE durante el primer segundo?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $h = 5(1^2)$.
**Resultado:**
$$\boxed{5\,\mathrm{m}}$$

</details>

### Ejercicio 6
**¿Qué profundidad tiene un pozo si dejas caer una piedra y escuchas el golpe a los 4 segundos? (Desprecia el sonido)**

<details>
<summary>Ver solución</summary>

**Datos:** $t=4$.
**Cálculo:**
$$h = 5(4^2) = 5(16)$$
**Resultado:**
$$\boxed{80\,\mathrm{m}}$$

</details>

### Ejercicio 7
**Si lanzas algo hacia abajo con velocidad inicial, ¿es caída libre?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Técnicamente el término "caída libre" implica que solo actúa la gravedad. Si lo lanzas, es un Tiro Vertical hacia abajo, que comparte las mismas reglas pero con $v_i \neq 0$.

</details>

### Ejercicio 8
**Un gato salta desde 1.25 metros. ¿Cuánto dura su vuelo?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $t = \sqrt{h/5}$.
**Cálculo:**
$$t = \sqrt{1.25 / 5} = \sqrt{0.25}$$
**Resultado:**
$$\boxed{0.5\,\mathrm{s}}$$

</details>

### Ejercicio 9
**¿Quién cae más rápido en el vacío: una bola de boliche o una pluma?**

<details>
<summary>Ver solución</summary>

**Respuesta:**
Ambos caen exactamente con la misma aceleración. Llegan al suelo juntos.

</details>

### Ejercicio 10
**Un objeto impacta a $20\,\mathrm{m/s}$. ¿Desde qué altura cayó?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $h = v_f^2 / 20$.
**Cálculo:**
$$h = \frac{20^2}{20} = \frac{400}{20}$$
**Resultado:**
$$\boxed{20\,\mathrm{m}}$$

</details>

---

## 🔑 Resumen
![resumen-caida-libre](https://cdn.ediprofe.com/img/fisica/w8j3-resumen-caida-libre.webp)


| Concepto | Descripción | Fórmula ($v_i=0$) |
|----------|-------------|-------------------|
| **Gravedad** | Aceleración constante de la Tierra. | $g \approx 10\,\mathrm{m/s^2}$ |
| **Velocidad** | Aumenta linealmente con el tiempo. | $$v_f = g \cdot t$$ |
| **Altura** | Aumenta al cuadrado con el tiempo. | $$h = \frac{1}{2}gt^2$$ |

> Recuerda: En ausencia de aire, no importa si es un elefante o una hormiga. **Todo cae al mismo ritmo**.

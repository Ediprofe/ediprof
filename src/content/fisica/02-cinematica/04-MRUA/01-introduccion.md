# **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)**

Hasta ahora estudiamos objetos con velocidad fija, como un tren en marcha crucero. Pero la realidad es más emocionante: los coches aceleran al arrancar, las manzanas caen ganando velocidad y los frenos nos detienen a tiempo.

El **MRUA** explica cómo cambia la velocidad paso a paso.

---

## 🎯 ¿Qué vas a aprender?

- Qué es realmente la aceleración y cómo se diferencia de la velocidad.
- Por qué la unidad de aceleración es "metros por segundo al cuadrado".
- Cómo predecir la velocidad futura de un objeto.
- Cómo la gravedad es simplemente una aceleración natural.

---

## ⚡ **El Concepto de Aceleración**

La **Aceleración** no es "ir rápido". Es **cambiar** de velocidad.

- Si pasas de $0$ a $100\,\mathrm{km/h}$, aceleraste.
- Si frenas ante un semáforo, desaceleraste (aceleración negativa).
- Si mantienes $100\,\mathrm{km/h}$ fijos, **tu aceleración es cero**.

> **Regla de Oro:** Aceleración = Cambio de Ritmo.

---

## 📏 **La Unidad Extraña: $m/s^2$**

La unidad **metros por segundo al cuadrado** ($m/s^2$) suele confundir, pero tiene un sentido muy lógico si la lees así:

**"Metros por segundo, cada segundo"**

Si tu aceleración es **$2\,\mathrm{m/s^2}$**, significa que:
- Cada segundo que pasa, tu velocidad aumenta en **$2\,\mathrm{m/s}$**.

![MRUA](/images/fisica/cinematica/mrua/mrua.png)

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Arrancando el Auto**

Un auto está quieto y acelera a **$3\,\mathrm{m/s^2}$** durante 4 segundos. ¿Qué tan rápido va al final?

**Datos:**
- Velocidad Inicial ($v_i$) = $0$
- Aceleración ($a$) = $3\,\mathrm{m/s^2}$
- Tiempo ($t$) = $4\,\mathrm{s}$

**Razonamiento Inductivo (Paso a Paso):**
- **Inicio:** $0\,\mathrm{m/s}$.
- **Segundo 1:** Gana 3. Va a $3\,\mathrm{m/s}$.
- **Segundo 2:** Gana otros 3. Va a $6\,\mathrm{m/s}$.
- **Segundo 3:** Gana otros 3. Va a $9\,\mathrm{m/s}$.
- **Segundo 4:** Gana otros 3. Va a $12\,\mathrm{m/s}$.

**Cálculo Directo:**

$$
v_f = 3 \times 4
$$

**Resultado:**

$$
\boxed{12\,\mathrm{m/s}}
$$

---

### **Ejemplo 2: La Gravedad**

La gravedad es una aceleración constante de aprox. **$10\,\mathrm{m/s^2}$** (redondeado para facilidad). Si dejas caer una piedra, ¿cuál es su velocidad a los 3 segundos?

**Datos:**
- $v_i = 0$
- $a = 10\,\mathrm{m/s^2}$
- $t = 3\,\mathrm{s}$

**Razonamiento:**
Cada segundo gana $10\,\mathrm{m/s}$. En 3 segundos habrá ganado 3 veces 10.

$$
v_f = 10 \times 3
$$

**Resultado:**

$$
\boxed{30\,\mathrm{m/s}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Un corredor parte del reposo y acelera a $2\,\mathrm{m/s^2}$ por 5 segundos. ¿Su velocidad final?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v_i = 0$
- $a = 2\,\mathrm{m/s^2}$
- $t = 5\,\mathrm{s}$

**Razonamiento:**
$v_f = \text{Aceleración} \times \text{Tiempo}$.

$$
v_f = 2 \times 5
$$

**Resultado:**

$$
\boxed{10\,\mathrm{m/s}}
$$

</details>

### Ejercicio 2
**Un auto viaja a $20\,\mathrm{m/s}$ y frena (desacelera) a $5\,\mathrm{m/s^2}$. ¿Cuánto tarda en detenerse?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v_i = 20\,\mathrm{m/s}$
- Pierde $5\,\mathrm{m/s}$ cada segundo.

**Razonamiento:**
Dividimos la velocidad que tiene entre lo que pierde por segundo.

$$
t = \frac{20}{5}
$$

**Resultado:**

$$
\boxed{4\,\mathrm{s}}
$$

</details>

### Ejercicio 3
**Si aceleras de $0$ a $30\,\mathrm{m/s}$ en 3 segundos, ¿cuál fue tu aceleración?**

<details>
<summary>Ver solución</summary>

**Datos:**
- Cambio velocidad = $30\,\mathrm{m/s}$
- Tiempo = $3\,\mathrm{s}$

**Razonamiento:**
$a = \text{Cambio} / \text{Tiempo}$.

$$
a = \frac{30}{3}
$$

**Resultado:**

$$
\boxed{10\,\mathrm{m/s^2}}
$$

</details>

### Ejercicio 4
**Una piedra cae durante 2 segundos ($g=10\,\mathrm{m/s^2}$). ¿A qué velocidad va?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $a = 10\,\mathrm{m/s^2}$
- $t = 2\,\mathrm{s}$

**Razonamiento:**
Velocidad = $10 \times 2$.

$$
v_f = 20\,\mathrm{m/s}
$$

**Resultado:**

$$
\boxed{20\,\mathrm{m/s}}
$$

</details>

### Ejercicio 5
**Un cohete acelera a $20\,\mathrm{m/s^2}$. ¿Qué velocidad tiene a los 2 segundos?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Gana 20 por segundo. En 2 segundos gana 40.

$$
v_f = 20 \times 2
$$

**Resultado:**

$$
\boxed{40\,\mathrm{m/s}}
$$

</details>

### Ejercicio 6
**Un tren va a $10\,\mathrm{m/s}$ y acelera a $1\,\mathrm{m/s^2}$ por 10 segundos. ¿Velocidad final?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v_i = 10\,\mathrm{m/s}$
- Gana $1\,\mathrm{m/s}$ cada segundo por 10s (Total ganado: 10).

**Razonamiento:**
$v_f = \text{Inicio} + \text{Ganancia}$.

$$
v_f = 10 + (1 \times 10)
$$

**Resultado:**

$$
\boxed{20\,\mathrm{m/s}}
$$

</details>

### Ejercicio 7
**¿Qué significa una aceleración de $0\,\mathrm{m/s^2}$?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Significa que la velocidad no cambia.

**Resultado:**
Es un **Movimiento Rectilíneo Uniforme (MRU)**.

</details>

### Ejercicio 8
**Un objeto pasa de $10\,\mathrm{m/s}$ a $20\,\mathrm{m/s}$ en 2 segundos. ¿Aceleración?**

<details>
<summary>Ver solución</summary>

**Datos:**
- Aumento = $10\,\mathrm{m/s}$ (de 10 a 20)
- Tiempo = $2\,\mathrm{s}$

**Razonamiento:**
$a = 10 / 2$.

$$
a = 5\,\mathrm{m/s^2}
$$

**Resultado:**

$$
\boxed{5\,\mathrm{m/s^2}}
$$

</details>

### Ejercicio 9
**¿Puede un objeto tener velocidad cero y aceleración distinta de cero?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí. Por ejemplo, cuando lanzas una pelota hacia arriba, en el punto más alto su velocidad es cero por un instante, pero la gravedad ($10\,\mathrm{m/s^2}$) sigue actuando para bajarla.

**Resultado:**
**Sí.**

</details>

### Ejercicio 10
**Un auto frena a $-4\,\mathrm{m/s^2}$. Si iba a $12\,\mathrm{m/s}$, ¿cuánto tarda en parar?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Pierde 4 cada segundo.

$$
t = \frac{12}{4}
$$

**Resultado:**

$$
\boxed{3\,\mathrm{s}}
$$

</details>

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **MRUA** | Movimiento con aceleración constante. |
| **Aceleración ($a$)** | Cambio de velocidad por segundo. |
| **$m/s^2$** | Unidad de aceleración (metros/segundo, cada segundo). |
| **Velocidad Cero** | No implica aceleración cero (ej. inicio de carrera o punto más alto de vuelo). |

> Recuerda: La velocidad te dice **dónde vas** y qué tan rápido. La aceleración te dice **cómo cambia** esa rapidez.

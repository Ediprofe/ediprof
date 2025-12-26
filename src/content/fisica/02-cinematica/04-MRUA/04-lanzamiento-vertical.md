# **Lanzamiento Vertical**

Si lanzas una pelota hacia arriba, primero sube rápido, luego se frena, se detiene un instante en el aire y finalmente cae acelerando. Es una batalla constante entre tu fuerza inicial y la gravedad de la Tierra.

---

## 🎯 ¿Qué vas a aprender?

- Cómo se comporta la velocidad cuando lanzas algo hacia arriba.
- Por qué la gravedad "resta" cuando subes y "suma" cuando bajas (dependiendo de la referencia).
- Cómo calcular cuánto tiempo tarda algo en volar y qué tan alto llega.
- La simetría perfecta: lo que tarda en subir, tarda en bajar.

---

## 🌎 **La Gravedad como Freno y Acelerador**

En el lanzamiento vertical, la gravedad ($g \approx 10\,\mathrm{m/s^2}$) siempre apunta hacia abajo.

1.  **Subida:** La gravedad está en contra del movimiento. La velocidad disminuye.
2.  **Cima:** Por un instante, la velocidad es **cero** ($0\,\mathrm{m/s}$).
3.  **Bajada:** La gravedad está a favor. La velocidad aumenta (hacia abajo).

> **Convención de Signos:**
> - Hacia arriba: **Positivo (+)**
> - Hacia abajo (Gravedad): **Negativo (-)**

---

## 📐 **Fórmulas Ajustadas**

Son las mismas del MRUA, pero con $a = -g$.

### 1. Velocidad en cualquier instante
$$
v_f = v_i - g \cdot t
$$

### 2. Altura en cualquier instante
$$
h = v_i \cdot t - \frac{1}{2} g \cdot t^2
$$

### 3. Altura Máxima ($v_f=0$)
$$
h_{max} = \frac{v_i^2}{2g}
$$

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Tiempo de Subida**

Lanzas una flecha hacia arriba a **$40\,\mathrm{m/s}$**. ¿Cuánto tarda en llegar al punto más alto? ($g=10\,\mathrm{m/s^2}$)

![flecha-hacia-arriba](https://cdn.ediprofe.com/img/fisica/8bj6-flecha-hacia-arriba.webp)


**Datos:**
- $v_i = 40\,\mathrm{m/s}$
- $v_f = 0$ (en la cima se detiene)
- $g = 10\,\mathrm{m/s^2}$

**Razonamiento:**
Cada segundo pierde 10 m/s de velocidad. Si tiene 40, tardará 4 segundos en quedarse en cero.

**Cálculo:**

$$
t = \frac{v_i}{g} = \frac{40}{10}
$$

**Resultado:**

$$
\boxed{4\,\mathrm{s}}
$$

---

### **Ejemplo 2: Altura Máxima**

¿Qué tan alto llega esa misma flecha?

**Datos:**
- $v_i = 40\,\mathrm{m/s}$
- $g = 10\,\mathrm{m/s^2}$

**Razonamiento:**
Usamos la fórmula de altura máxima.

$$
h_{max} = \frac{v_i^2}{2g}
$$

**Cálculo:**

$$
h_{max} = \frac{40^2}{2 \cdot 10} = \frac{1600}{20}
$$

**Resultado:**

$$
\boxed{80\,\mathrm{m}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Lanzas una pelota a $30\,\mathrm{m/s}$. ¿Cuánto tarda en llegar a la cima?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=30, g=10$.
**Razonamiento:**
Pierde 10 cada segundo.

$$
t = \frac{30}{10}
$$

**Resultado:**

$$
\boxed{3\,\mathrm{s}}
$$

</details>

### Ejercicio 2
**¿Qué velocidad tiene esa misma pelota a los 2 segundos?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=30, t=2$.
**Fórmula:** $v_f = 30 - 10(2)$.
**Cálculo:**
$$v_f = 30 - 20$$
**Resultado:**
$$\boxed{10\,\mathrm{m/s}}$$

</details>

### Ejercicio 3
**¿Qué altura alcanza un objeto lanzado a $20\,\mathrm{m/s}$?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $h_{max} = v_i^2 / 2g$.
**Cálculo:**
$$h = \frac{20^2}{20} = \frac{400}{20}$$
**Resultado:**
$$\boxed{20\,\mathrm{m}}$$

</details>

### Ejercicio 4
**Si lanzas algo a $50\,\mathrm{m/s}$, ¿cuánto tiempo total está en el aire (subir y bajar)?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tarda 5s en subir ($50/10$). Por simetría, tarda 5s en bajar.
**Resultado:**
$$\boxed{10\,\mathrm{s}}$$

</details>

### Ejercicio 5
**Un cohete de juguete alcanza $45\,\mathrm{m}$ de altura. ¿Con qué velocidad salió?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $v_i = \sqrt{2gh}$.
**Cálculo:**
$$v_i = \sqrt{2 \cdot 10 \cdot 45} = \sqrt{900}$$
**Resultado:**
$$\boxed{30\,\mathrm{m/s}}$$

</details>

### Ejercicio 6
**Lanzas una piedra hacia arriba a $10\,\mathrm{m/s}$. ¿A qué altura está tras 1 segundo?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $h = 10(1) - 5(1^2)$.
**Cálculo:**
$$h = 10 - 5$$
**Resultado:**
$$\boxed{5\,\mathrm{m}}$$
(Está en su altura máxima).

</details>

### Ejercicio 7
**¿Con qué velocidad regresa a tu mano un objeto lanzado a $25\,\mathrm{m/s}$?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Por conservación de energía y simetría, regresa con la misma rapidez.
**Resultado:**
$$\boxed{-25\,\mathrm{m/s}}$$
(Hacia abajo).

</details>

### Ejercicio 8
**Lanzas algo a $40\,\mathrm{m/s}$. ¿Cuál es su velocidad a los 5 segundos?**

<details>
<summary>Ver solución</summary>

**Fórmula:** $v_f = 40 - 10(5)$.
**Cálculo:**
$$v_f = 40 - 50$$
**Resultado:**
$$\boxed{-10\,\mathrm{m/s}}$$
(Está bajando a 10 m/s).

</details>

### Ejercicio 9
**¿Cuánto tiempo tarda en subir un objeto lanzado a $15\,\mathrm{m/s}$?**

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$t = \frac{15}{10}$$
**Resultado:**
$$\boxed{1.5\,\mathrm{s}}$$

</details>

### Ejercicio 10
**Un objeto es lanzado hacia arriba. En el punto más alto, ¿su aceleración es cero?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. Su velocidad es cero, pero la gravedad ($10\,\mathrm{m/s^2}$) sigue actuando para hacerlo bajar. Si la aceleración fuera cero, se quedaría flotando ahí para siempre.
**Resultado:**
**No.**

</details>

---

## 🔑 Resumen

![resumen-lanzamiento-vertical](https://cdn.ediprofe.com/img/fisica/w5ef-resumen-lanzamiento-vertical.webp)


| Variable | Comportamiento |
|----------|----------------|
| **Velocidad de Subida** | Positiva y disminuye. |
| **Velocidad en Cima** | Cero ($0\,\mathrm{m/s}$). |
| **Velocidad de Bajada** | Negativa y aumenta en magnitud. |
| **Aceleración** | Siempre $-10\,\mathrm{m/s^2}$ (hacia abajo). |
| **Tiempo** | Tiempo de subida = Tiempo de bajada. |

> Todo lo que sube, tiene que bajar (y tarda lo mismo en hacerlo).

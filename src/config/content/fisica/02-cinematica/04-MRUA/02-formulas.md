---
title: "Fórmulas del MRUA"
---

# **Fórmulas del MRUA**

Ya sabemos que en el MRUA la velocidad cambia. Ahora vamos a tener el poder de predecir el futuro: ¿dónde estará un objeto? ¿qué tan rápido irá? ¿cuánto tiempo le tomará? Para eso, usamos tres herramientas matemáticas fundamentales.

---

## 🎯 ¿Qué vas a aprender?

- Las 3 fórmulas maestras que gobiernan todo movimiento acelerado.
- Cuándo usar cada fórmula según los datos que tengas (la "Estrategia del Descarte").
- Cómo resolver problemas reales de autos, trenes y caída libre.

---

## 📐 **Las Tres Ecuaciones**

Imagina que tienes una caja de herramientas. Solo necesitas estas tres llaves para desmontar cualquier problema de cinemática:

### 1. Ecuación de Velocidad (Sin posición)

Nos dice qué tan rápido va algo después de cierto tiempo.

$$
v_f = v_i + a \cdot t
$$

- **$v_f$**: Velocidad Final
- **$v_i$**: Velocidad Inicial (0 si parte del reposo)
- **$a$**: Aceleración
- **$t$**: Tiempo

> **Úsala cuando:** No te pregunten ni te den la distancia.

### 2. Ecuación de Posición (El "Monstruo")

Nos dice dónde está el objeto. Es la más larga, pero la más completa.

$$
x_f = x_i + v_i \cdot t + \frac{1}{2} a \cdot t^2
$$

- **$x_f$**: Posición Final
- **$x_i$**: Posición Inicial
- **$t^2$**: ¡Ojo! Solo el tiempo va al cuadrado.

> **Úsala cuando:** Quieras saber la distancia o posición y conozcas el tiempo.

### 3. Ecuación Atemporal (Sin tiempo)

Nos relaciona distancias con velocidades, sin importar el reloj.

$$
v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x
$$

- **$\Delta x$**: Distancia recorrida ($x_f - x_i$)

> **Úsala cuando:** El problema **no mencione el tiempo** por ningún lado.

---

## ⚙️ **Estrategia para Resolver Problemas**

1.  **Lista tus datos:** Escribe qué tienes ($v_i, a, t...$).
2.  **Identifica qué falta:** ¿Qué te piden?
3.  **Elige la fórmula:** Busca la ecuación que tenga lo que te piden y lo que tienes.

---

## ⚙️ **Ejemplo Resuelto: Despegue de Avión**

Un avión parte del reposo y acelera a **$3\,\mathrm{m/s^2}$**. Necesita alcanzar **$60\,\mathrm{m/s}$** para despegar. ¿Qué distancia de pista necesita?

![despegue-del-avion](https://cdn.ediprofe.com/img/fisica/rh5n-despegue-del-avion.webp)


**Datos:**
- $v_i = 0$ (reposo)
- $a = 3\,\mathrm{m/s^2}$
- $v_f = 60\,\mathrm{m/s}$
- **Incógnita:** Distancia ($\Delta x$)
- **No tenemos:** Tiempo ($t$)

**Razonamiento:**
Como no tenemos el tiempo, usamos la **Ecuación 3 (Atemporal)**.

$$
v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x
$$

Despejamos $\Delta x$:

$$
\Delta x = \frac{v_f^2 - v_i^2}{2 \cdot a}
$$

**Cálculo:**

$$
\Delta x = \frac{60^2 - 0}{2 \cdot 3} = \frac{3600}{6}
$$

**Resultado:**

$$
\boxed{600\,\mathrm{m}}
$$

Necesita 600 metros de pista.

---

### **Ejemplo 2: Cálculo de Velocidad Final**

Un ciclista parte del reposo y acelera a **$2\,\mathrm{m/s^2}$** durante **6 segundos**. ¿Qué velocidad alcanza?

**Datos:**
- $v_i = 0$
- $a = 2\,\mathrm{m/s^2}$
- $t = 6\,\mathrm{s}$

**Razonamiento:**
No nos piden distancia. Usamos la **Ecuación 1 (Velocidad)**.

$$
v_f = v_i + a \cdot t
$$

**Cálculo:**

$$
v_f = 0 + 2 \times 6
$$

**Resultado:**

$$
\boxed{12\,\mathrm{m/s}}
$$

---

### **Ejemplo 3: Cálculo de Distancia**

Un tren viaja a **$15\,\mathrm{m/s}$** y acelera a **$1\,\mathrm{m/s^2}$** durante **10 segundos**. ¿Qué distancia recorre en ese tiempo?

**Datos:**
- $v_i = 15\,\mathrm{m/s}$
- $a = 1\,\mathrm{m/s^2}$
- $t = 10\,\mathrm{s}$

**Razonamiento:**
Necesitamos distancia y tenemos tiempo. Usamos la **Ecuación 2 (Posición)**.

$$
\Delta x = v_i \cdot t + \frac{1}{2} a \cdot t^2
$$

**Cálculo:**

$$
\Delta x = 15 \cdot 10 + \frac{1}{2}(1)(10^2)
$$

$$
\Delta x = 150 + 50
$$

**Resultado:**

$$
\boxed{200\,\mathrm{m}}
$$

---

### **Ejemplo 4: Desaceleración (Frenado)**

Un auto viaja a **$25\,\mathrm{m/s}$** y frena hasta detenerse en **$62.5\,\mathrm{m}$**. ¿Cuál fue su desaceleración?

**Datos:**
- $v_i = 25\,\mathrm{m/s}$
- $v_f = 0$ (se detiene)
- $\Delta x = 62.5\,\mathrm{m}$
- **No tenemos tiempo**

**Razonamiento:**
Sin tiempo. Usamos **Ecuación 3** y despejamos $a$.

$$
v_f^2 = v_i^2 + 2a\Delta x \rightarrow a = \frac{v_f^2 - v_i^2}{2\Delta x}
$$

**Cálculo:**

$$
a = \frac{0 - 25^2}{2 \cdot 62.5} = \frac{-625}{125}
$$

**Resultado:**

$$
\boxed{-5\,\mathrm{m/s^2}}
$$

(Negativo porque frena).

---

### **Ejemplo 5: Calculando el Tiempo**

Un cohete acelera a **$5\,\mathrm{m/s^2}$** desde el reposo hasta alcanzar **$40\,\mathrm{m/s}$**. ¿Cuánto tiempo tardó?

**Datos:**
- $v_i = 0$
- $v_f = 40\,\mathrm{m/s}$
- $a = 5\,\mathrm{m/s^2}$

**Razonamiento:**
Despejamos el tiempo de la Ecuación 1.

$$
v_f = v_i + a \cdot t \rightarrow t = \frac{v_f - v_i}{a}
$$

**Cálculo:**

$$
t = \frac{40 - 0}{5}
$$

**Resultado:**

$$
\boxed{8\,\mathrm{s}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Un auto acelera de 0 a $20\,\mathrm{m/s}$ en 5 segundos. ¿Cuál es su aceleración?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=0, v_f=20, t=5$.
**Fórmula 1:**
$$a = \frac{20 - 0}{5}$$
**Resultado:**
$$\boxed{4\,\mathrm{m/s^2}}$$

</details>

### Ejercicio 2
**Un tren viaja a $10\,\mathrm{m/s}$ y acelera a $2\,\mathrm{m/s^2}$ durante 10 segundos. ¿Qué distancia recorre?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=10, a=2, t=10$.
**Fórmula 2 (Posición):**
$$\Delta x = (10 \cdot 10) + \frac{1}{2}(2 \cdot 10^2)$$
$$\Delta x = 100 + 100$$
**Resultado:**
$$\boxed{200\,\mathrm{m}}$$

</details>

### Ejercicio 3
**Una piedra cae del reposo y golpea el suelo a $30\,\mathrm{m/s}$. Si $g=10\,\mathrm{m/s^2}$, ¿desde qué altura cayó?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=0, v_f=30, a=10$. Sin tiempo.
**Fórmula 3 (Atemporal):**
$$\Delta x = \frac{30^2 - 0}{2 \cdot 10} = \frac{900}{20}$$
**Resultado:**
$$\boxed{45\,\mathrm{m}}$$

</details>

### Ejercicio 4
**Un ciclista frena con $a = -2\,\mathrm{m/s^2}$. Si iba a $10\,\mathrm{m/s}$, ¿cuánto recorre antes de parar?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=10, v_f=0, a=-2$.
**Fórmula 3:**
$$\Delta x = \frac{0^2 - 10^2}{2(-2)} = \frac{-100}{-4}$$
**Resultado:**
$$\boxed{25\,\mathrm{m}}$$

</details>

### Ejercicio 5
**Un cohete parte del reposo y sube 100m en 4 segundos. ¿Cuál fue su aceleración?**

<details>
<summary>Ver solución</summary>

**Datos:** $\Delta x=100, t=4, v_i=0$.
**Fórmula 2:** $\Delta x = \frac{1}{2} a t^2 \rightarrow a = \frac{2 \Delta x}{t^2}$
$$a = \frac{200}{16}$$
**Resultado:**
$$\boxed{12.5\,\mathrm{m/s^2}}$$

</details>

### Ejercicio 6
**¿Qué velocidad alcanza el cohete del ejercicio anterior a los 4 segundos?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=0, a=12.5, t=4$.
**Fórmula 1:**
$$v_f = 0 + (12.5 \cdot 4)$$
**Resultado:**
$$\boxed{50\,\mathrm{m/s}}$$

</details>

### Ejercicio 7
**Un bus acelera a $1\,\mathrm{m/s^2}$. Si recorre 50m partiendo del reposo, ¿qué velocidad final tiene?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=0, a=1, \Delta x=50$. Sin tiempo.
**Fórmula 3:**
$$v_f^2 = 0 + 2(1)(50) = 100$$
$$v_f = \sqrt{100}$$
**Resultado:**
$$\boxed{10\,\mathrm{m/s}}$$

</details>

### Ejercicio 8
**Un objeto cae por 3 segundos ($g=10$). ¿Qué distancia recorre?**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=0, t=3, a=10$.
**Fórmula 2:**
$$\Delta x = \frac{1}{2}(10)(3^2) = 5(9)$$
**Resultado:**
$$\boxed{45\,\mathrm{m}}$$

</details>

### Ejercicio 9
**Un auto a $30\,\mathrm{m/s}$ ve un obstáculo y frena en 3 segundos ($v_f=0$). ¿Cuál fue su desaceleración?**

<details>
<summary>Ver solución</summary>

**Fórmula 1:**
$$a = \frac{0 - 30}{3}$$
**Resultado:**
$$\boxed{-10\,\mathrm{m/s^2}}$$

</details>

### Ejercicio 10
**Si lanzas una pelota hacia arriba a $20\,\mathrm{m/s}$, ¿cuánto sube hasta detenerse? ($g=-10\,\mathrm{m/s^2}$)**

<details>
<summary>Ver solución</summary>

**Datos:** $v_i=20, v_f=0, a=-10$.
**Fórmula 3:**
$$\Delta x = \frac{0^2 - 20^2}{2(-10)} = \frac{-400}{-20}$$
**Resultado:**
$$\boxed{20\,\mathrm{m}}$$

</details>

---

## 🔑 Resumen

![Fórmulas-MRUA](https://cdn.ediprofe.com/img/fisica/8m24-formulas-mrua.webp)

| Ecuación | Variable faltante | Fórmula |
|----------|-------------------|---------|
| **Velocidad** | Distancia | $$v_f = v_i + a \cdot t$$ |
| **Posición** | Velocidad Final | $$x_f = x_i + v_i t + \frac{1}{2} a t^2$$ |
| **Atemporal** | Tiempo | $$v_f^2 = v_i^2 + 2 a \Delta x$$ |

> Domina estas tres y dominarás el movimiento del universo.

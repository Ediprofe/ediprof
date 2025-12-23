# 🏀 **Movimiento Parabólico**

## 🎯 **¿Qué vas a aprender?**

En esta lección aprenderás a:

*   **Entender** el movimiento parabólico como la suma de dos movimientos independientes (horizontal y vertical).
*   **Descomponer** vectores de velocidad usando funciones trigonométricas.
*   **Calcular** variables clave como altura máxima, tiempo de vuelo y alcance horizontal.
*   **Resolver** problemas prácticos de proyectiles en deportes y situaciones cotidianas.

---

## 🎯 **¿Qué es el Movimiento Parabólico?**

El **Movimiento Parabólico** (también llamado *Tiro Oblicuo*) ocurre cuando un objeto es lanzado con un ángulo respecto al suelo, describiendo una trayectoria curva en forma de parábola.

La clave para entenderlo es que son **dos movimientos independientes que ocurren al mismo tiempo**:

| Dirección | Tipo de movimiento | ¿Por qué? |
| :--- | :--- | :--- |
| **Horizontal (x)** | **MRU** (velocidad constante) | No hay fuerza horizontal (despreciando el aire) |
| **Vertical (y)** | **Caída libre** (MRUA) | La gravedad actúa hacia abajo |

> 💡 **Principio de independencia:** Lo que pasa en $x$ no afecta a $y$, y viceversa. El tiempo es la única variable que comparten.

---

## 🔗 **Conexión con MRU y MRUA: Deducción de las Fórmulas**

El movimiento parabólico **no es un movimiento nuevo**, es simplemente la **combinación** de dos movimientos que ya conocemos.

### **Paso 1: Descomponer la velocidad inicial**

Al lanzar con ángulo $\theta$, usamos **trigonometría** para descomponer la velocidad inicial $v_0$:

$$
v_x = v_0 \cdot \cos\theta \qquad v_y = v_0 \cdot \sin\theta
$$

### **Paso 2: Aplicar MRU en la dirección horizontal**

No hay aceleración horizontal ($a_x = 0$), por lo tanto la velocidad horizontal es constante.

| Fórmula MRU | Resultado |
| :--- | :--- |
| $x = v \cdot t$ | $$x = (v_0 \cos\theta) \cdot t$$ |
| $v_x = \text{constante}$ | $$v_x = v_0 \cos\theta$$ |

### **Paso 3: Aplicar MRUA (caída libre) en la dirección vertical**

La gravedad actúa hacia abajo ($a_y = -g$).

| Fórmula MRUA | Con $a = -g$ | Fórmula para y |
| :--- | :--- | :--- |
| $v_f = v_i + at$ | $v_{yf} = v_{yi} - gt$ | $$v_{yf} = v_0\sin\theta - gt$$ |
| $y = v_i t + \frac{1}{2}at^2$ | $y = v_{yi}t - \frac{1}{2}gt^2$ | $$y = (v_0\sin\theta)t - \frac{1}{2}gt^2$$ |

### **Paso 4: Deducir fórmulas especiales**

**Altura máxima** (cuando $v_y = 0$):

$$
h_{\max} = \frac{(v_0\sin\theta)^2}{2g}
$$

**Tiempo de vuelo** (sube + baja):

$$
t_{total} = \frac{2v_0\sin\theta}{g}
$$

**Alcance horizontal máximo** (distancia en x al volver al suelo):

$$
x_{\max} = \frac{v_0^2 \sin(2\theta)}{g}
$$

---

## ⚙️ **Ejemplo 1 — Tiro libre de fútbol**

Un jugador patea un balón con velocidad de **$20\,\mathrm{m/s}$** a un ángulo de **$30°$**. Calcular las componentes de velocidad, el tiempo de vuelo y el alcance.

![Tiro parabólico - Ejemplo 1](/images/fisica/cinematica/mrua/tiro-parabolico-ejemplo1.png)

### 📝 **Solución Paso a Paso**

**Concepto clave:** Dividimos el problema en dos: movimiento horizontal (MRU) y vertical (caída libre).

**Datos:**
*   $v_0 = 20\,\mathrm{m/s}$
*   $\theta = 30°$
*   $g = 10\,\mathrm{m/s^2}$
*   $\cos(30°) \approx 0.866$ y $\sin(30°) = 0.5$

**Paso 1: Descomponer la velocidad inicial en sus componentes**

Usamos trigonometría:
$$v_x = v_0 \cdot \cos(30°) = 20 \times 0.866 = 17.3\,\mathrm{m/s}$$
$$v_y = v_0 \cdot \sin(30°) = 20 \times 0.5 = 10\,\mathrm{m/s}$$

**Paso 2: Calcular el tiempo de vuelo (solo depende de $v_y$)**

El tiempo de subida es:
$$t_{\text{subida}} = \frac{v_y}{g} = \frac{10}{10} = 1\,\mathrm{s}$$

El tiempo total (por simetría):
$$t_{\text{total}} = 2 \times 1 = 2\,\mathrm{s}$$

**Paso 3: Calcular el alcance horizontal (MRU en x)**

Como en x no hay aceleración, usamos:
$$x = v_x \cdot t_{\text{total}} = 17.3 \times 2 = 34.6\,\mathrm{m}$$

> ✅ El balón vuela durante **2 segundos** y alcanza **34.6 metros** de distancia horizontal.

---

## ⚙️ **Ejemplo 2 — Cañón de confeti**

Un cañón de confeti dispara a **$30°$** con velocidad de **$25\,\mathrm{m/s}$**. ¿Qué altura máxima alcanza?

![Tiro parabólico - Ejemplo 2](/images/fisica/cinematica/mrua/tiro-parabolico-ejemplo2.png)

### 📝 **Solución Paso a Paso**

**Concepto clave:** La altura máxima solo depende de la componente vertical de la velocidad. Es como un lanzamiento vertical puro.

**Datos:**
*   $v_0 = 25\,\mathrm{m/s}$
*   $\theta = 30°$
*   $g = 10\,\mathrm{m/s^2}$
*   $\sin(30°) = 0.5$

**Paso 1: Extraer la componente vertical**

Solo nos importa $v_y$ porque solo eso afecta a la altura:
$$v_y = v_0 \cdot \sin(30°) = 25 \times 0.5 = 12.5\,\mathrm{m/s}$$

**Paso 2: Aplicar la fórmula de altura máxima**

Esta es la misma fórmula que en lanzamiento vertical, pero con $v_y$ en lugar de $v_0$:
$$h_{\text{max}} = \frac{v_y^2}{2g}$$

**Paso 3: Sustituir y calcular**

$$h_{\text{max}} = \frac{(12.5)^2}{2 \times 10} = \frac{156.25}{20} = 7.8\,\mathrm{m}$$

> ✅ El confeti alcanza una altura máxima de **7.8 metros**.

---

## ⚙️ **Ejemplo 3 — Baloncesto: Tiro al aro**

Un jugador lanza un balón con **$v_0 = 15\,\mathrm{m/s}$** a **$45°$**. ¿A qué distancia horizontal cae el balón?

![Tiro parabólico - Ejemplo 3](/images/fisica/cinematica/mrua/tiro-parabolico-ejemplo3.png)

### 📝 **Solución Paso a Paso**

**Concepto clave:** El ángulo de $45°$ es especial porque hace que $v_x = v_y$, maximizando el alcance horizontal.

**Datos:**
*   $v_0 = 15\,\mathrm{m/s}$
*   $\theta = 45°$
*   $g = 10\,\mathrm{m/s^2}$
*   $\sin(45°) = \cos(45°) \approx 0.707$

**Paso 1: Descomponer en componentes**

Con $45°$, ambas componentes son iguales:
$$v_x = v_y = 15 \times 0.707 = 10.6\,\mathrm{m/s}$$

**Paso 2: Calcular tiempo de vuelo**

De la componente vertical:
$$t_{\text{total}} = \frac{2v_y}{g} = \frac{2 \times 10.6}{10} = 2.12\,\mathrm{s}$$

**Paso 3: Calcular alcance (MRU en x)**

Como en x no hay aceleración:
$$x = v_x \cdot t_{\text{total}} = 10.6 \times 2.12 = 22.5\,\mathrm{m}$$

> ✅ El balón cae a **22.5 metros** del punto de lanzamiento.

> 💡 **Dato curioso:** Con $\theta = 45°$ se obtiene el **alcance máximo** posible para una misma velocidad inicial.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1**

Un proyectil es lanzado con una velocidad de **$40\,\mathrm{m/s}$** y un ángulo de **$30°$**. ¿Cuál es su velocidad horizontal ($v_x$)?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 40\,\mathrm{m/s}$, $\theta = 30°$.

**Fórmula:** $v_x = v_0 \cdot \cos\theta$

**Cálculo:**
$$v_x = 40 \cdot \cos(30°) = 40 \cdot 0.866 = 34.64\,\mathrm{m/s}$$

> La velocidad horizontal es **34.64 m/s** y se mantiene constante.

</details>

### **Ejercicio 2**

Se dispara una bala de cañón con $v_0 = 100\,\mathrm{m/s}$ a un ángulo de $53°$ ($\sin 53° \approx 0.8$). ¿Cuánto tiempo tarda en llegar al punto más alto?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 100\,\mathrm{m/s}$, $\theta = 53°$, $g=10\,\mathrm{m/s^2}$.

**1. Velocidad vertical inicial:**
$$v_{yi} = 100 \cdot 0.8 = 80\,\mathrm{m/s}$$

**2. Tiempo de subida:**
$$t_{\text{subida}} = \frac{v_{yi}}{g} = \frac{80}{10} = 8\,\mathrm{s}$$

> Tarda **8 segundos** en subir.

</details>

### **Ejercicio 3**

¿Cuál es el alcance horizontal de una piedra lanzada a $20\,\mathrm{m/s}$ con un ángulo de $45°$?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 20\,\mathrm{m/s}$, $\theta = 45°$, $g=10\,\mathrm{m/s^2}$.
Sabemos que $\sin(2\theta) = \sin(90°) = 1$.

**Fórmula de alcance:**
$$x = \frac{v_0^2 \sin(2\theta)}{g}$$

**Cálculo:**
$$x = \frac{20^2 \cdot 1}{10} = \frac{400}{10} = 40\,\mathrm{m}$$

> El alcance es de **40 metros**.

</details>

---

### **Ejercicio 4: Velocidad Vertical**

Un proyectil se dispara a $30\,\mathrm{m/s}$ con un ángulo de $60°$. ¿Cuál es su velocidad vertical inicial? ($\sin 60° \approx 0.866$)

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 30\,\mathrm{m/s}$, $\theta = 60°$.

**Fórmula:** $v_y = v_0 \cdot \sin\theta$

**Cálculo:**
$$v_y = 30 \times 0.866 = 25.98 \approx 26\,\mathrm{m/s}$$

> La velocidad vertical inicial es aproximadamente **26 m/s**.

</details>

---

### **Ejercicio 5: Tiempo de Vuelo en Ángulo de 30°**

Se lanza un objeto con $v_0 = 40\,\mathrm{m/s}$ a un ángulo de $30°$. ¿Cuánto tiempo permanece en el aire?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 40\,\mathrm{m/s}$, $\theta = 30°$, $\sin 30° = 0.5$.

**Paso 1:** Calcular velocidad vertical:
$$v_y = 40 \times 0.5 = 20\,\mathrm{m/s}$$

**Paso 2:** Tiempo total de vuelo:
$$t_{\text{total}} = \frac{2v_y}{g} = \frac{2(20)}{10} = 4\,\mathrm{s}$$

> El objeto permanece **4 segundos** en el aire.

</details>

---

### **Ejercicio 6: Comparación de Ángulos**

¿Cuál ángulo produce mayor alcance: $30°$ o $60°$ si ambos se disparan con la misma velocidad inicial?

<details>
<summary><strong>Ver solución</strong></summary>

**Concepto:** El alcance depende de $\sin(2\theta)$.

Para $30°$: $\sin(60°) = 0.866$
Para $60°$: $\sin(120°) = 0.866$

**Respuesta:** Ambos ángulos producen el **mismo alcance** porque $\sin(2 \times 30°) = \sin(2 \times 60°)$.

> **Dato importante:** Los ángulos complementarios (30° y 60°) producen el mismo alcance.

</details>

---

### **Ejercicio 7: Altura Máxima en Tiro Vertical**

¿Cuál es la altura máxima de un proyectil lanzado a $50\,\mathrm{m/s}$ y $60°$? ($\sin 60° \approx 0.866$)

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 50\,\mathrm{m/s}$, $\theta = 60°$, $g = 10\,\mathrm{m/s^2}$.

**Paso 1:** Velocidad vertical:
$$v_y = 50 \times 0.866 = 43.3\,\mathrm{m/s}$$

**Paso 2:** Altura máxima:
$$h_{\text{max}} = \frac{v_y^2}{2g} = \frac{(43.3)^2}{20} = \frac{1874.89}{20} \approx 93.7\,\mathrm{m}$$

> La altura máxima es aproximadamente **93.7 metros**.

</details>

---

### **Ejercicio 8: Velocidad Horizontal Constante**

En un tiro parabólico con $v_0 = 35\,\mathrm{m/s}$ y $\theta = 40°$, ¿cuál es la velocidad horizontal durante todo el vuelo? ($\cos 40° \approx 0.766$)

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 35\,\mathrm{m/s}$, $\theta = 40°$.

**Fórmula:** $v_x = v_0 \cdot \cos\theta$

**Cálculo:**
$$v_x = 35 \times 0.766 = 26.81\,\mathrm{m/s}$$

**Concepto:** La velocidad horizontal es constante (no hay fricción).

> La velocidad horizontal es **26.81 m/s** durante todo el vuelo.

</details>

---

### **Ejercicio 9: Alcance en Tiro a Ángulo Pequeño**

¿Cuál es el alcance de un proyectil lanzado a $25\,\mathrm{m/s}$ y $15°$? (Usa la fórmula de alcance)

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 25\,\mathrm{m/s}$, $\theta = 15°$, $\sin(30°) = 0.5$.

**Fórmula:**
$$x = \frac{v_0^2 \sin(2\theta)}{g}$$

**Cálculo:**
$$x = \frac{25^2 \times 0.5}{10} = \frac{625 \times 0.5}{10} = \frac{312.5}{10} = 31.25\,\mathrm{m}$$

> El alcance es aproximadamente **31.25 metros**.

</details>

---

### **Ejercicio 10: Análisis de Trayectoria**

Un objeto se lanza a $v_0 = 20\,\mathrm{m/s}$ con $\theta = 45°$. ¿Cuál es su alcance máximo?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 20\,\mathrm{m/s}$, $\theta = 45°$, $\sin(90°) = 1$.

**Fórmula:**
$$x_{\text{max}} = \frac{v_0^2 \sin(2\theta)}{g} = \frac{v_0^2 \sin(90°)}{g} = \frac{v_0^2}{g}$$

**Cálculo:**
$$x_{\text{max}} = \frac{20^2}{10} = \frac{400}{10} = 40\,\mathrm{m}$$

> El alcance máximo es **40 metros** (alcance óptimo con $45°$).

</details>

---

## 🎓 **Resumen**

![Resumen - Tiro parabólco](/images/fisica/cinematica/mrua/resumen-tiro-parabolico.png)

*   El **Movimiento Parabólico** combina **MRU** en horizontal y **Caída Libre** en vertical.
*   Las componentes son independientes:
    *   $x$ depende de $v_x = v_0 \cos\theta$ (constante).
    *   $y$ depende de $v_y = v_0 \sin\theta - gt$ (variable).
*   El **tiempo de vuelo** depende únicamente de la componente vertical de la velocidad.
*   El **alcance máximo** se logra con un ángulo de **45°**.
*   **Fórmulas Clave:**
    *   $x = (v_0 \cos\theta) \cdot t$
    *   $y = (v_0 \sin\theta) \cdot t - \frac{1}{2} g \cdot t^2$


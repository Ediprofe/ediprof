# 📐 **Fórmulas del MRUA: De dónde salen y cómo usarlas**

En física, las fórmulas no son "magia"; son consecuencias lógicas de las definiciones básicas. A continuación, vamos a deducir las tres ecuaciones fundamentales del **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)** paso a paso.

---

## 🎯 ¿Qué vas a aprender?

- De dónde sale la ecuación de la velocidad final.
- Cómo se deduce la ecuación cuadrática de la posición.
- La "Tercera Ecuación" para cuando no conoces el tiempo.
- Una guía clara para elegir la fórmula correcta en cada problema.

---

## 1️⃣ **Primera Ecuación: Calculando la Velocidad Final**

Esta fórmula nace directamente de la definición de **Aceleración**. Sabemos que la aceleración es el cambio de velocidad en el tiempo.

**Paso 1: Escribimos la definición**
$$
a = \frac{\text{Cambio de velocidad}}{\text{Tiempo}} = \frac{v_f - v_i}{t}
$$

**Paso 2: Despejamos la Velocidad Final ($v_f$)**
Pasamos el tiempo ($t$) a multiplicar al otro lado:
$$
a \cdot t = v_f - v_i
$$

Ahora pasamos la velocidad inicial ($v_i$) a sumar:

**✅ FÓRMULA DE VELOCIDAD:**
$$
v_f = v_i + a \cdot t
$$

> **Uso:** Ideal cuando conoces el tiempo y la aceleración, y quieres saber qué tan rápido vas al final.

---

## 2️⃣ **Segunda Ecuación: Calculando la Posición**

Esta fórmula permite hallar dónde está el objeto en cualquier instante. Nace del concepto de **Velocidad Promedio**.

**Paso 1: Definimos el Desplazamiento usando el promedio**
Si la aceleración es constante, la velocidad promedio es justo la mitad entre la inicial y la final. El desplazamiento es esa velocidad promedio por el tiempo.
$$
\Delta x = \left( \frac{v_i + v_f}{2} \right) \cdot t
$$

**Paso 2: Sustitución y Simplificación**
Reemplazamos $v_f$ por $(v_i + a \cdot t)$ y operamos:
$$
\Delta x = v_i \cdot t + \frac{1}{2}a \cdot t^2
$$

**✅ FÓRMULA DE POSICIÓN:**
$$
x_f = x_i + v_i \cdot t + \frac{1}{2}a \cdot t^2
$$

> **Uso:** La ecuación reina. Te dice dónde estás ($x_f$) en cualquier instante $t$.

---

## 3️⃣ **Tercera Ecuación: Eliminando el Tiempo**

A veces tenemos problemas donde conocemos las velocidades y el desplazamiento, pero **no sabemos el tiempo**. Para estos casos, fusionamos las ecuaciones anteriores para eliminar la variable $t$.

**✅ FÓRMULA SIN TIEMPO:**
$$
v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x
$$

> **Uso:** Fundamental cuando el problema **no menciona el tiempo**.

---

## 📝 **Ejercicios de Práctica**

Pon a prueba tus conocimientos con estos 10 ejercicios. Intenta resolverlos antes de mirar la solución.

### **Ejercicio 1: Velocidad Final**
Un ciclista parte del reposo ($v_i = 0$) y acelera a razón de $2\,\mathrm{m/s^2}$ durante 5 segundos. ¿Cuál es su velocidad final?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0$, $a = 2\,\mathrm{m/s^2}$, $t = 5\,\mathrm{s}$.
**Fórmula:** $v_f = v_i + a \cdot t$
**Cálculo:**
$$v_f = 0 + (2)(5) = 10\,\mathrm{m/s}$$

</details>

---

### **Ejercicio 2: Desplazamiento**
Un auto viaja a $10\,\mathrm{m/s}$ y acelera a $3\,\mathrm{m/s^2}$ durante 4 segundos. ¿Cuál es su desplazamiento en ese tiempo?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 10\,\mathrm{m/s}$, $a = 3\,\mathrm{m/s^2}$, $t = 4\,\mathrm{s}$.
**Fórmula:** $\Delta x = v_i \cdot t + \frac{1}{2}a \cdot t^2$
**Cálculo:**
$$\Delta x = (10)(4) + \frac{1}{2}(3)(4^2)$$
$$\Delta x = 40 + 0.5(3)(16) = 40 + 24 = 64\,\mathrm{m}$$

</details>

---

### **Ejercicio 3: Sin Tiempo**
Una moto acelera de $5\,\mathrm{m/s}$ a $15\,\mathrm{m/s}$ con un desplazamiento de 50 metros. ¿Cuál fue su aceleración?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 5\,\mathrm{m/s}$, $v_f = 15\,\mathrm{m/s}$, $\Delta x = 50\,\mathrm{m}$.
**Fórmula:** $v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x$
**Despeje:** $a = \frac{v_f^2 - v_i^2}{2\Delta x}$
**Cálculo:**
$$a = \frac{15^2 - 5^2}{2(50)} = \frac{225 - 25}{100} = \frac{200}{100} = 2\,\mathrm{m/s^2}$$

</details>

---

### **Ejercicio 4: Tiempo de Frenado**
Un camión viaja a $20\,\mathrm{m/s}$ y frena con una desaceleración de $4\,\mathrm{m/s^2}$ hasta detenerse. ¿Cuánto tiempo tarda?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 20\,\mathrm{m/s}$, $v_f = 0$, $a = -4\,\mathrm{m/s^2}$.
**Fórmula:** $v_f = v_i + a \cdot t \rightarrow t = \frac{v_f - v_i}{a}$
**Cálculo:**
$$t = \frac{0 - 20}{-4} = \frac{-20}{-4} = 5\,\mathrm{s}$$

</details>

---

### **Ejercicio 5: Velocidad Inicial**
Un objeto alcanza una velocidad de $30\,\mathrm{m/s}$ después de acelerar a $4\,\mathrm{m/s^2}$ durante 6 segundos. ¿Cuál era su velocidad inicial?

<details>
<summary>Ver solución</summary>

**Datos:** $v_f = 30\,\mathrm{m/s}$, $a = 4\,\mathrm{m/s^2}$, $t = 6\,\mathrm{s}$.
**Fórmula:** $v_f = v_i + a \cdot t \rightarrow v_i = v_f - a \cdot t$
**Cálculo:**
$$v_i = 30 - (4)(6) = 30 - 24 = 6\,\mathrm{m/s}$$

</details>

---

### **Ejercicio 6: Caída Libre (Posición)**
Se deja caer una pelota desde un edificio. ¿Qué distancia habrá recorrido a los 3 segundos? (Usa $g = 9.8\,\mathrm{m/s^2}$)

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0$ (se deja caer), $a = g = 9.8\,\mathrm{m/s^2}$, $t = 3\,\mathrm{s}$.
**Fórmula:** $\Delta y = v_i \cdot t + \frac{1}{2}g \cdot t^2$
**Cálculo:**
$$\Delta y = 0 + \frac{1}{2}(9.8)(3^2) = 4.9(9) = 44.1\,\mathrm{m}$$

</details>

---

### **Ejercicio 7: Desplazamiento de Frenado**
Un coche va a $30\,\mathrm{m/s}$ y frena uniformemente hasta detenerse en 10 segundos. ¿Cuál fue su desplazamiento mientras frenaba?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 30\,\mathrm{m/s}$, $v_f = 0$, $t = 10\,\mathrm{s}$.
**Nota:** Primero hallamos $a$, o usamos la fórmula de velocidad promedio.
**Método Vel. Promedio:** $\Delta x = \frac{v_i + v_f}{2} \cdot t$
**Cálculo:**
$$\Delta x = \frac{30 + 0}{2} \cdot 10 = 15 \cdot 10 = 150\,\mathrm{m}$$

</details>

---

### **Ejercicio 8: Aceleración en Rampa**
Un bloque se desliza por una rampa partiendo del reposo y recorre 18 metros en 3 segundos. ¿Cuál es su aceleración?

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 0$, $\Delta x = 18\,\mathrm{m}$, $t = 3\,\mathrm{s}$.
**Fórmula:** $\Delta x = v_i \cdot t + \frac{1}{2}a \cdot t^2 \rightarrow \Delta x = \frac{1}{2}a \cdot t^2$
**Despeje:** $a = \frac{2 \cdot \Delta x}{t^2}$
**Cálculo:**
$$a = \frac{2(18)}{3^2} = \frac{36}{9} = 4\,\mathrm{m/s^2}$$

</details>

---

### **Ejercicio 9: Velocidad de Impacto**
Se lanza una piedra hacia abajo con una velocidad inicial de $5\,\mathrm{m/s}$ desde una altura de 20 metros. ¿Con qué velocidad golpea el suelo? ($g = 9.8\,\mathrm{m/s^2}$)

<details>
<summary>Ver solución</summary>

**Datos:** $v_i = 5\,\mathrm{m/s}$, $\Delta y = 20\,\mathrm{m}$, $a = 9.8\,\mathrm{m/s^2}$.
**Fórmula:** $v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta y$
**Cálculo:**
$$v_f^2 = 5^2 + 2(9.8)(20) = 25 + 392 = 417$$
$$v_f = \sqrt{417} \approx 20.42\,\mathrm{m/s}$$

</details>

---

### **Ejercicio 10: Encuentro (Conceptual)**
Dos autos parten del reposo. El auto A acelera a $2\,\mathrm{m/s^2}$ y el auto B a $4\,\mathrm{m/s^2}$. Después de 5 segundos, ¿cuánto mayor es el desplazamiento del auto B respecto al auto A?

<details>
<summary>Ver solución</summary>

**Auto A:** $\Delta x_A = \frac{1}{2}(2)(5^2) = 25\,\mathrm{m}$
**Auto B:** $\Delta x_B = \frac{1}{2}(4)(5^2) = 50\,\mathrm{m}$
**Diferencia:** $50 - 25 = 25\,\mathrm{m}$
El auto B recorrió 25 metros más.

</details>

---

## 🔑 Resumen

Aquí tienes la guía definitiva para resolver cualquier problema de MRUA. Identifica qué variable te falta y elige la ecuación correcta.

### 1. Las 5 Variables del Movimiento
Todo problema de MRUA involucra 5 variables. Normalmente conoces 3 y buscas 1.
- $v_i$: Velocidad Inicial
- $v_f$: Velocidad Final
- $a$: Aceleración
- $t$: Tiempo
- $\Delta x$: Desplazamiento

### 2. Tabla de Selección de Fórmulas

| **Si el problema NO menciona...** | **Usa esta fórmula** |
| :--- | :--- |
| **Desplazamiento ($\Delta x$)** | $$v_f = v_i + a \cdot t$$ |
| **Velocidad Final ($v_f$)** | $$\Delta x = v_i \cdot t + \frac{1}{2}a \cdot t^2$$ |
| **Tiempo ($t$)** | $$v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x$$ |
| **Aceleración ($a$)** | $$\Delta x = \left( \frac{v_i + v_f}{2} \right) \cdot t$$ |

### 3. Tips
- **Reposo:** Si dice "parte del reposo", entonces $v_i = 0$.
- **Frenado:** Si dice "se detiene", entonces $v_f = 0$.
- **Signos:** Si frena, la aceleración es **negativa** (opuesta a la velocidad).
- **Caída Libre:** La aceleración es $g \approx 9.8\,\mathrm{m/s^2}$ (hacia abajo).

### 4. Resumen visual

![formulas-mrua](https://cdn.ediprofe.com/img/fisica/8m24-formulas-mrua.webp)

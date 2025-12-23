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

A veces tenemos problemas donde conocemos las velocidades y distancias, pero **no sabemos el tiempo**. Para estos casos, fusionamos las ecuaciones anteriores para eliminar la variable $t$.

**✅ FÓRMULA SIN TIEMPO:**
$$
v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x
$$

> **Uso:** Fundamental cuando el problema **no menciona el tiempo**.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1: Aplicando la 1ª Ecuación**
Un bus acelera a $2\,\mathrm{m/s^2}$ desde el reposo durante 10 segundos. ¿Qué velocidad alcanza?

<details>
<summary>Ver solución</summary>

$$v_f = 0 + (2)(10) = 20\,\mathrm{m/s}$$

</details>

---

### **Ejercicio 2: Aplicando la 2ª Ecuación**
Una piedra cae desde un puente (velocidad inicial cero). Después de 3 segundos, ¿qué distancia ha recorrido? ($g = 9.8\,\mathrm{m/s^2}$)

<details>
<summary>Ver solución</summary>

$$x = 0 + \frac{1}{2}(9.8)(3^2) = 4.9 \times 9 = 44.1\,\mathrm{m}$$

</details>

---

### **Ejercicio 3: Aplicando la 3ª Ecuación**
Un auto frena con aceleración $-5\,\mathrm{m/s^2}$ hasta detenerse en una distancia de 40 metros. ¿A qué velocidad venía? ($v_f = 0$)

<details>
<summary>Ver solución</summary>

$$0^2 = v_i^2 + 2(-5)(40)$$
$$0 = v_i^2 - 400$$
$$v_i^2 = 400 \rightarrow v_i = 20\,\mathrm{m/s}$$

</details>

---

## 🔑 Resumen

Usa esta tabla para saber qué fórmula elegir según los datos que tengas:

| **¿Qué quieres hallar?** | **¿Qué datos tienes?** | **Fórmula a usar** |
| :--- | :--- | :--- |
| **Velocidad Final ($v_f$)** | Tiempo y Aceleración | $$v_f = v_i + a \cdot t$$ |
| **Posición Final ($x_f$)** | Tiempo y Aceleración | $$x_f = x_i + v_i \cdot t + \frac{1}{2}a \cdot t^2$$ |
| **Velocidad o Posición** | **NO** tienes el tiempo | $$v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x$$ |

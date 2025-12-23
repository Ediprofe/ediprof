# 📐 **Fórmulas del Movimiento Rectilíneo Uniforme (MRU)**

El MRU se rige por una relación matemática simple pero poderosa entre tres variables: posición, velocidad y tiempo. Dominar estas fórmulas es el primer paso para resolver problemas de cinemática.

---

## 🎯 ¿Qué vas a aprender?

- Las tres fórmulas fundamentales del MRU.
- La diferencia entre desplazamiento ($x$) y cambio de posición ($\Delta x$).
- Cómo resolver problemas paso a paso identificando los datos.
- Cómo aplicar estas fórmulas en situaciones reales (trenes, atletas, sonido).

---

## 🧮 **Las Fórmulas Maestras**

Para describir matemáticamente el movimiento, usaremos la letra **$x$** para representar el **Desplazamiento** o **Posición**.

### **1. El Caso Simple (Partiendo de Cero)**

Imaginemos la situación más común: encendemos el cronómetro justo cuando el objeto arranca desde el punto de inicio ($0$).

| Magnitud | Fórmula | ¿Cuándo usarla? |
| :--- | :--- | :--- |
| **Desplazamiento** | $$x = v \cdot t$$ | Cuando buscas qué distancia recorrió. |
| **Velocidad** | $$v = \frac{x}{t}$$ | Cuando buscas qué tan rápido iba. |
| **Tiempo** | $$t = \frac{x}{v}$$ | Cuando buscas cuánto tardó. |

> **Nota:** Estas fórmulas asumen que el objeto parte desde el origen ($x_i = 0$).

---

### **2. El Caso General (Con Posición Inicial)**

En la realidad, no siempre empezamos a contar desde cero. A veces el objeto ya se encuentra en una **Posición Inicial ($x_i$)** y termina en una **Posición Final ($x_f$)**.

El desplazamiento real es la diferencia: $\Delta x = x_f - x_i$.

La ecuación de posición evoluciona a:

$$
x_f = x_i + v \cdot t
$$

**Donde:**
* $x_f$: **Posición Final** (Ubicación de llegada).
* $x_i$: **Posición Inicial** (Ubicación de partida).
* $v \cdot t$: **Desplazamiento** (Lo que recorrió).

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Hallar la Velocidad**

Un atleta corre un desplazamiento de $100\,\mathrm{m}$ partiendo desde la línea de salida. Si tarda $10\,\mathrm{s}$ en llegar a la meta, ¿cuál fue su velocidad?

**1. Identifica los datos:**
* $x = 100\,\mathrm{m}$
* $t = 10\,\mathrm{s}$
* $v = ?$

**2. Selecciona la fórmula:**
$$
v = \frac{x}{t}
$$

**3. Sustituye y calcula:**
$$v = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = 10\,\mathrm{m/s}$$

> **Respuesta:** El atleta corrió a **$10\,\mathrm{m/s}$**.

---

### **Ejemplo 2: Hallar el Desplazamiento**

El sonido viaja a una velocidad constante de $340\,\mathrm{m/s}$. Si un trueno se escucha $3\,\mathrm{s}$ después del relámpago, ¿a qué distancia cayó?

**1. Identifica los datos:**
* $v = 340\,\mathrm{m/s}$
* $t = 3\,\mathrm{s}$
* $x = ?$

**2. Selecciona la fórmula:**
$$
x = v \cdot t
$$

**3. Sustituye y calcula:**
$$x = 340\,\mathrm{m/s} \times 3\,\mathrm{s} = 1020\,\mathrm{m}$$

> **Respuesta:** El rayo cayó a **$1020$ metros** (aprox. 1 km).

---

### **Ejemplo 3: Posición Final (Caso General)**

Un ciclista se encuentra en el **Kilómetro 10**. Continúa pedaleando a **$20\,\mathrm{km/h}$** durante **2 horas**. ¿En qué kilómetro estará?

**1. Identifica los datos:**
* $x_i = 10\,\mathrm{km}$ (Posición inicial)
* $v = 20\,\mathrm{km/h}$
* $t = 2\,\mathrm{h}$
* $x_f = ?$

**2. Selecciona la fórmula:**
$$
x_f = x_i + v \cdot t
$$

**3. Sustituye y calcula:**
$$x_f = 10 + (20 \times 2) = 10 + 40 = 50\,\mathrm{km}$$

> **Respuesta:** El ciclista terminará en el **kilómetro 50**.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1: El Tren Viajero**

Un tren sale de una ciudad en el **km 200** y viaja hacia otra en el **km 500** a una velocidad de **$100\,\mathrm{km/h}$**. ¿Cuánto tiempo tardará en llegar?

<details>
<summary>Ver solución</summary>

**1. Calcular desplazamiento:**
$$\Delta x = 500 - 200 = 300\,\mathrm{km}$$

**2. Calcular tiempo:**
$$t = \frac{\Delta x}{v} = \frac{300\,\mathrm{km}}{100\,\mathrm{km/h}} = 3\,\mathrm{h}$$

**Respuesta:** Tardará **3 horas**.

</details>

---

### **Ejercicio 2: Encuentro de Autos**

Dos autos parten simultáneamente en sentidos contrarios:
- Auto A desde Medellín (km 0) a **$80\,\mathrm{km/h}$**.
- Auto B desde Bogotá (km 420) a **$60\,\mathrm{km/h}$**.

¿En cuánto tiempo se encuentran?

<details>
<summary>Ver solución</summary>

Al ir en sentidos contrarios, las velocidades se suman:
$$v_{relativa} = 80 + 60 = 140\,\mathrm{km/h}$$

$$t = \frac{\text{Distancia}}{v_{relativa}} = \frac{420}{140} = 3\,\mathrm{h}$$

**Respuesta:** Se encuentran en **3 horas**.

</details>

---

### **Ejercicio 3: Vuelo Comercial**

Un avión viaja a **$800\,\mathrm{km/h}$**. Si su destino está a **$650\,\mathrm{km}$**, ¿cuántos minutos dura el vuelo?

<details>
<summary>Ver solución</summary>

$$t = \frac{650}{800} = 0.8125\,\mathrm{h}$$

Convertimos a minutos multiplicando por 60:
$$0.8125 \times 60 = 48.75\,\mathrm{min}$$

**Respuesta:** Aprox. **49 minutos**.

</details>

---

## 🔑 Resumen

- **Velocidad ($v$):** Es la relación entre espacio y tiempo ($v = x/t$).
- **Desplazamiento ($x$):** Es el producto de velocidad por tiempo ($x = v \cdot t$).
- **Posición Final ($x_f$):** Si no partes de cero, debes sumar la posición inicial ($x_f = x_i + v \cdot t$).
- **Unidades:** Siempre verifica que las unidades coincidan (km con horas, metros con segundos).

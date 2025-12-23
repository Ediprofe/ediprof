# 🚗 **MRU: Introducción**

El **Movimiento Rectilíneo Uniforme (MRU)** es el modelo de movimiento más sencillo de la física. Antes de aprender fórmulas complejas, vamos a entender qué significa realmente que algo se mueva "uniformemente".

---

## 🎯 ¿Qué vas a aprender?

- Qué significa que un movimiento sea Rectilíneo y Uniforme.
- La relación entre distancia y tiempo en el MRU.
- Cómo interpretar el gráfico de Posición vs. Tiempo.
- A calcular velocidades simples mentalmente.

---

## 📖 **¿Qué es el MRU?**

Un objeto está en MRU cuando cumple **dos condiciones fundamentales**:

1.  **Trayectoria Rectilínea:** Se mueve en línea recta (no cambia de dirección).
2.  **Velocidad Constante:** Mantiene su rapidez y dirección inalterables (no acelera ni frena).

![MRU](/public/images/fisica/cinematica/mru/mru.png)

> 💡 **Dato Clave:** Si la velocidad es constante, significa que la **aceleración es cero** ($a = 0$).

---

## 🧠 **La Idea Clave: Distancias Iguales en Tiempos Iguales**

Imagina un tren que viaja a **60 km/h** de manera constante. Esto significa literalmente:

- En la **1ª hora** recorre **60 km**.
- En la **2ª hora** recorre otros **60 km**.
- En la **3ª hora** recorre otros **60 km** más.


![Tren MRU](/public/images/fisica/cinematica/mru/tren-mru.png)

¿Ves el patrón? **Siempre avanza la misma distancia en cada unidad de tiempo.**

> 💡 Esta es la esencia del MRU: **el objeto avanza distancias iguales en tiempos iguales.**

---

## ⚙️ **Ejemplo 1 — El Robot Constante**

Un robot se mueve con una velocidad constante de **$4\,\mathrm{m/s}$**.

### **¿Qué significa esto?**
Significa que **por cada segundo que pasa**, el robot avanza exactamente **4 metros**.

![Robot en MRU](/public/images/fisica/cinematica/mru/robot-camina.png) 

Veamos su avance paso a paso:

| Tiempo ($t$) | Avance en ese segundo | Posición acumulada ($x$) |
| :---: | :---: | :---: |
| $0\,\mathrm{s}$ | — | $0\,\mathrm{m}$ (Inicio) |
| $1\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $4\,\mathrm{m}$ |
| $2\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $8\,\mathrm{m}$ |
| $3\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $12\,\mathrm{m}$ |

### **Cálculo intuitivo**
Si avanza $4$ metros cada segundo, en $3$ segundos habrá avanzado:
$$
4 + 4 + 4 = 12\,\mathrm{m}
$$

O multiplicando:
$$
\text{Posición} = 4\,\mathrm{m/s} \times 3\,\mathrm{s} = 12\,\mathrm{m}
$$

Esto nos lleva a la fórmula básica:
$$
x = v \cdot t
$$

---

## 📊 **Visualización: El Gráfico Posición vs Tiempo**

Si graficamos los datos del robot anterior (tiempo en el eje horizontal, posición en el vertical), obtenemos esto:

<div class="image-card">
  <img src="/images/fisica/cinematica/mru/mru-posicion-tiempo.svg" alt="Gráfico Posición vs Tiempo MRU" />
</div>

### **¿Qué nos dice este gráfico?**

1.  **Es una línea recta:** Esto es la "firma" del MRU. Si no es recta, la velocidad no es constante.
2.  **Sube uniformemente:** Indica que el objeto avanza sin frenar ni acelerar.
3.  **La inclinación (pendiente):** Representa la velocidad. Una línea más inclinada significaría una mayor velocidad (más metros en menos tiempo).

---

## ⚙️ **Ejemplo 2 — Calculando la Velocidad**

Un corredor recorre **$20\,\mathrm{m}$** en **$4\,\mathrm{s}$** manteniendo un ritmo constante. ¿Cuál es su velocidad?

![Corredor recorre 20m en 4s](/public/images/fisica/cinematica/mru/20m-en-4s.png)

### **Análisis paso a paso**

Queremos saber cuántos metros avanza **en 1 segundo**.

- En 4 segundos recorre 20 metros.
- Repartimos los 20 metros equitativamente en los 4 segundos:

$$
v = \frac{20\,\mathrm{m}}{4\,\mathrm{s}} = 5\,\mathrm{m/s}
$$

> ✅ **Respuesta:** Su velocidad es de **$5\,\mathrm{m/s}$**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Un auto viaja con velocidad constante de $15\,\mathrm{m/s}$. ¿Qué distancia recorre en 6 segundos?**

<details>
<summary>Ver solución</summary>

**$90\,\mathrm{m}$**

Usamos la lógica de "distancia = velocidad × tiempo":
$$x = 15\,\mathrm{m/s} \times 6\,\mathrm{s} = 90\,\mathrm{m}$$

</details>

---

### Ejercicio 2
**Un ciclista recorre 100 metros en 10 segundos con velocidad constante. ¿Cuál es su velocidad?**

<details>
<summary>Ver solución</summary>

**$10\,\mathrm{m/s}$**

Dividimos la distancia total entre el tiempo total:
$$v = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = 10\,\mathrm{m/s}$$

</details>

---

### Ejercicio 3
**Verdadero o Falso: En un Movimiento Rectilíneo Uniforme, la aceleración es positiva.**

<details>
<summary>Ver solución</summary>

**Falso.**

En el MRU la velocidad no cambia, por lo tanto, la aceleración es **cero**.

</details>

---

## 🔑 Resumen

- **MRU** significa **M**ovimiento **R**ectilíneo **U**niforme.
- **Uniforme** quiere decir que la **velocidad es constante** (no cambia).
- Como la velocidad no cambia, la **aceleración es cero ($a=0$)**.
- En el MRU se recorren **distancias iguales en tiempos iguales**.
- El gráfico de **Posición vs. Tiempo** es siempre una **línea recta**.

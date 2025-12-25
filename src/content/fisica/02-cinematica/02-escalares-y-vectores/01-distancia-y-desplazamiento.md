# 📏 Distancia vs. Desplazamiento

Aunque en la vida diaria usamos estas palabras indistintamente, en física representan conceptos totalmente distintos. Es fundamental diferenciar entre "cuánto me moví" y "dónde terminé".

---

## 🎯 ¿Qué vas a aprender?

- La diferencia entre distancia (escalar) y desplazamiento (vectorial).
- Cómo calcular ambos en 1D y 2D.
- Por qué la distancia nunca puede ser menor que la magnitud del desplazamiento.

---

## 👣 Distancia

Es una magnitud **escalar** que mide la **longitud total del camino recorrido**.

* **Significado:** Es la suma de todos los pasos dados, sin importar la dirección.
* **Signo:** Siempre es positiva (+). Nunca resta.
* **Fórmula:** Suma de los valores absolutos de cada tramo.

$$
d = |d_1| + |d_2| + |d_3| + \dots
$$

---

## 📍 Desplazamiento

Es una magnitud **vectorial** que mide el **cambio de posición** desde el punto de inicio hasta el punto final.

* **Significado:** Es la línea recta que une el inicio con el final.
* **Signo:** Puede ser positivo, negativo o cero.
* **Fórmula:** Posición final menos posición inicial.

$$
\Delta x = x_f - x_i
$$

---

## ⚙️ Ejemplo 1 — El Tenista

Un tenista comienza en la línea de fondo ($x=0$ m), corre hasta la red ubicada a 12 m, y luego retrocede hasta la línea de saque, ubicada a 6 m.

![Movimiento del Tenista](/images/fisica/cinematica/escalares-y-vectores/tenista.svg)

### ✅ Solución

**Distancia:** Suma de todos los tramos recorridos.

$$d = 12 + 6 = 18\ \text{m}$$

**Desplazamiento:** Posición final menos posición inicial.

$$\Delta x = 6 - 0 = +6\ \text{m}$$

---

## ⚙️ Ejemplo 2 — El Ascensor

El ascensor sube de 0 m a 20 m, luego baja hasta -4 m.

![alt text](/images/fisica/cinematica/escalares-y-vectores/ascensor.png)

### ✅ Solución

**Distancia:**

$$d = 20 + 24 = 44\ \text{m}$$

**Desplazamiento:**

$$\Delta x = -4 - 0 = -4\ \text{m}$$

---

## ⚙️ Ejemplo 3 — Vuelta a la Manzana

Una persona recorre una pista circular de 400 m y termina en el mismo punto.

![Vuelta a la Manzana](/images/fisica/cinematica/escalares-y-vectores/vuelta-manzana.svg)

### ✅ Solución

**Distancia:**

$$d = 400\ \text{m}$$

**Desplazamiento:**

$$\Delta x = 0$$ (regresó al punto de partida)

---

## ⚙️ Ejemplo 4 — Caminata en Dos Dimensiones

Camina 30 m al norte y luego 40 m al este.

![Caminata en 2D](/images/fisica/cinematica/escalares-y-vectores/caminata-2d.svg)

### ✅ Solución

**Distancia:**

$$d = 30 + 40 = 70\ \text{m}$$

**Desplazamiento (Pitágoras):**

$$\Delta x = \sqrt{30^2 + 40^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50\ \text{m}$$

> 💡 **Observa:** La distancia recorrida (70 m) es **mayor** que el desplazamiento (50 m). El desplazamiento es siempre la **ruta más corta**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Caminas 10 metros al norte y luego 5 metros al sur. Calcula:**
a) La distancia total recorrida.
b) El desplazamiento desde el punto de inicio.

<details>
<summary>Ver solución</summary>

a) **Distancia:** $d = 10 + 5 = 15\,\mathrm{m}$.
b) **Desplazamiento:** $\Delta x = 10 - 5 = +5\,\mathrm{m}$ (hacia el norte).

</details>

---

### Ejercicio 2
**¿Puede la distancia ser negativa? ¿Y el desplazamiento?**

<details>
<summary>Ver solución</summary>

- La **distancia** NUNCA es negativa, ya que suma longitudes recorridas.
- El **desplazamiento** SÍ puede ser negativo, indicando que el movimiento fue en sentido contrario al eje positivo.

</details>

---

### Ejercicio 3
**Un corredor recorre media vuelta en una pista circular de radio 50 m. Calcula:**
a) La distancia recorrida (la longitud del arco).
b) La magnitud del desplazamiento (línea recta inicio-fin).

<details>
<summary>Ver solución</summary>

a) **Distancia:** La mitad del perímetro del círculo.
$$d = \frac{2\pi r}{2} = \pi(50) \approx 157\,\mathrm{m}$$

b) **Desplazamiento:** El diámetro del círculo.
$$|\Delta x| = 2r = 2(50) = 100\,\mathrm{m}$$

</details>

---

### Ejercicio 4
**Una partícula se mueve en el eje X: inicia en $x_i = 5$ m, va hasta $x = 12$ m y finalmente se detiene en $x_f = 2$ m.**
a) Calcula la distancia total recorrida.
b) Calcula el desplazamiento total.

<details>
<summary>Ver solución</summary>

a) **Distancia:**
- Tramo 1 (5 a 12): $|12 - 5| = 7\,\mathrm{m}$
- Tramo 2 (12 a 2): $|2 - 12| = |-10| = 10\,\mathrm{m}$
- Total: $d = 7 + 10 = 17\,\mathrm{m}$

b) **Desplazamiento:**
$$\Delta x = x_f - x_i = 2 - 5 = -3\,\mathrm{m}$$

</details>

---

### Ejercicio 5
**Un barco navega 8 km al Norte y luego 6 km al Oeste. Calcula:**
a) La distancia total recorrida.
b) La magnitud del desplazamiento resultante.

<details>
<summary>Ver solución</summary>

a) **Distancia:**
$$d = 8 + 6 = 14\,\mathrm{km}$$

b) **Desplazamiento:** Hipotenusa del triángulo rectángulo.
$$|\Delta x| = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10\,\mathrm{km}$$

</details>

---

## 🔑 Resumen

- **Distancia ($d$):** Magnitud escalar. Suma de todo el camino recorrido. Siempre positiva.
- **Desplazamiento ($\Delta x$):** Magnitud vectorial. Cambio de posición ($x_f - x_i$). Puede ser positivo, negativo o cero.
- La distancia siempre es mayor o igual que la magnitud del desplazamiento ($d \geq |\Delta x|$).

![alt text](/images/fisica/cinematica/escalares-y-vectores/distancia-y-desplazamiento.png)

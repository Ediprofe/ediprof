# 📍 **Posición y Marco de Referencia**

La **posición** ($x$) es la ubicación de un objeto en el espacio. Sin embargo, para describir dónde está algo, siempre necesitamos un punto de comparación.

Este punto de comparación se llama **Marco de Referencia** u **Origen** ($x=0$).

---

## 🎯 ¿Qué vas a aprender?

- Qué es un marco de referencia y por qué es necesario.
- Cómo describir la posición en 1D y 2D.
- Cómo cambia la posición al cambiar el origen del sistema de coordenadas.

---

## 📐 **¿Qué es un Marco de Referencia?**

El movimiento es **relativo**. Para describir la posición de una partícula, necesitamos un sistema desde donde observar y medir. Un marco de referencia consta de tres elementos esenciales:

1.  **Origen de coordenadas:** El punto $(0,0)$ desde donde se mide la posición.
2.  **Sistema de ejes:** Generalmente ejes cartesianos ($x, y, z$) para dar dirección.
3.  **Reloj:** Para medir el tiempo ($t$).

El siguiente diagrama muestra un marco de referencia con una partícula ubicada en la posición $(x, y)$:

![Posición en 2D](/images/fisica/cinematica/introduccion/posicion-2d.svg)

> 💡 **Nota:** Observa cómo las coordenadas $(x, y)$ se miden respecto al origen O.

---

## 📐 **El origen puede estar en cualquier punto**

El origen del marco de referencia **no tiene que estar en un lugar "especial"**. Podemos elegirlo donde sea más conveniente. Observa cómo la **misma partícula** tiene coordenadas diferentes según dónde coloquemos el origen:

![Marcos de referencia](/images/fisica/cinematica/introduccion/marcos-referencia.svg)

> 💡 **Nota:** Una misma posición tiene **coordenadas diferentes** según el marco de referencia elegido (O₁ o O₂).


---

## 📏 **Posiciones Positivas y Negativas**

* Si el objeto está en el sentido positivo del eje (generalmente a la derecha), su posición es **positiva** ($+$).
* Si el objeto está en el sentido negativo (generalmente a la izquierda), su posición es **negativa** ($-$).

![alt text](/public/images/fisica/cinematica/posicion-positiva-y-negativa.png)

> **Regla de oro:** La posición física de un objeto **no es fija**; cambia si cambiamos el lugar desde donde lo miramos (el origen).


---

## ⚙️ **Ejemplo 1 — Los Salones del Colegio**

En un pasillo recto se encuentran tres lugares clave distribuidos en el siguiente orden: la **Rectoría**, el **Salón A** y el **Salón B**.

Las distancias son las siguientes:
* De la Rectoría al Salón A hay **20 metros**.
* Del Salón A al Salón B hay **10 metros**.

$$
\text{[Rectoría]} \xrightarrow{20\,\mathrm{m}} \text{[Salón A]} \xrightarrow{10\,\mathrm{m}} \text{[Salón B]}
$$

**Determine la posición ($x$) de cada uno de los tres lugares (Rectoría, Salón A y Salón B) respecto a los siguientes marcos de referencia:**

1.  **Origen en la Rectoría.**
2.  **Origen en el Salón A.**
3.  **Origen en el Salón B.**

### **✅ Solución**

**1. Marco de Referencia: Origen en la Rectoría ($x=0$)**
Ubicamos el cero en el extremo izquierdo. Todo lo demás queda a la derecha (positivo).

![Rectoría como origen](/images/fisica/cinematica/introduccion/posicion-1d-rectoria.svg)

* **Posición Rectoría:** $x = 0\,\mathrm{m}$
* **Posición Salón A:** $x_A = +20\,\mathrm{m}$
* **Posición Salón B:** $x_B = +30\,\mathrm{m}$

**2. Marco de Referencia: Origen en el Salón A ($x=0$)**
Ubicamos el cero en el medio.

![Salón A como origen](/images/fisica/cinematica/introduccion/posicion-1d-salon-a.svg)

* **Posición Salón A:** $x = 0\,\mathrm{m}$
* **Posición Salón B:** $x_B = +10\,\mathrm{m}$
* **Posición Rectoría:** $x_R = -20\,\mathrm{m}$

**3. Marco de Referencia: Origen en el Salón B ($x=0$)**
Ubicamos el cero en el extremo derecho. Todo lo demás queda a la izquierda (negativo).

![Salón B como origen](/images/fisica/cinematica/introduccion/posicion-1d-salon-b.svg)

* **Posición Salón B:** $x = 0\,\mathrm{m}$
* **Posición Salón A:** $x_A = -10\,\mathrm{m}$
* **Posición Rectoría:** $x_R = -30\,\mathrm{m}$

---

## ⚙️ **Ejemplo 2 — La Carrera de Atletismo**

Tres atletas están calentando en una pista recta: **Atleta 1**, **Atleta 2** y **Atleta 3**. Su distribución es la siguiente:

* El **Atleta 2** está situado en el centro.
* El **Atleta 1** se encuentra **15 metros a la izquierda** del Atleta 2.
* El **Atleta 3** se encuentra **15 metros a la derecha** del Atleta 2.

$$
\text{[Atleta 1]} \xleftarrow{15\,\mathrm{m}} \text{[Atleta 2]} \xrightarrow{15\,\mathrm{m}} \text{[Atleta 3]}
$$

**Calcule la posición ($x$) de los tres atletas para los siguientes casos:**

1.  El entrenador pone el origen en la posición del **Atleta 2**.
2.  El entrenador pone el origen en la posición del **Atleta 1**.

### **✅ Solución**

**1. Marco de Referencia: Origen en el Atleta 2 ($x=0$)**
El observador está en el centro.

![Atleta 2 como origen](/images/fisica/cinematica/introduccion/atletas-origen-2.svg)

* **Posición Atleta 2:** $x = 0\,\mathrm{m}$
* **Posición Atleta 3:** $x_3 = +15\,\mathrm{m}$
* **Posición Atleta 1:** $x_1 = -15\,\mathrm{m}$

**2. Marco de Referencia: Origen en el Atleta 1 ($x=0$)**
El observador está en el extremo izquierdo. Todos los demás están a su derecha (positivos).

![Atleta 1 como origen](/images/fisica/cinematica/introduccion/atletas-origen-1.svg)

* **Posición Atleta 1:** $x = 0\,\mathrm{m}$
* **Posición Atleta 2:** $x_2 = +15\,\mathrm{m}$
* **Posición Atleta 3:** $x_3 = +30\,\mathrm{m}$

---

> 💡 **Conclusión:**
> Un mismo objeto puede tener posiciones diferentes (ej: $x = 30\,\mathrm{m}$ o $x = -20\,\mathrm{m}$) dependiendo de **dónde pongas el cero ($0$)**, aunque la distancia física entre los objetos nunca cambió.

---

## ⚙️ **Ejemplo 3 — Posición en el Plano (2D)**

Un dron sobrevuela un parque. En un sistema de coordenadas donde el **kiosko** está en el origen $(0,0)$, el dron se encuentra en la posición $(4, 3)$ metros.

![Posición del Dron](/images/fisica/cinematica/introduccion/dron-posicion.svg)

**Pregunta:** ¿Cuál es la distancia del dron al kiosko?

### ✅ Solución

Usamos el teorema de Pitágoras:

$$
d = \sqrt{x^2 + y^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\,\mathrm{m}
$$

---

## ⚙️ **Ejemplo 4 — Cambio de origen en el plano (2D)**

Tres amigos están en una plaza:
- **Ana** está en el origen $(0, 0)$
- **Beto** está en $(3, 4)$
- **Carlos** está en $(6, 0)$

![Origen en Ana](/images/fisica/cinematica/introduccion/plaza-ana.svg)

**Pregunta:** Si ahora **Carlos** es el nuevo origen, ¿cuáles son las posiciones de Ana y Beto?

### ✅ Solución

Restamos las coordenadas de Carlos a cada punto:

**Nuevo origen: Carlos en $(6, 0)$**

* **Posición de Ana:** 
  $$\vec{r}_A = (0 - 6, 0 - 0) = (-6, 0)$$
  
* **Posición de Beto:**
  $$\vec{r}_B = (3 - 6, 4 - 0) = (-3, 4)$$

* **Posición de Carlos:**
  $$\vec{r}_C = (0, 0) \quad \text{(es el nuevo origen)}$$

![Origen en Carlos](/images/fisica/cinematica/introduccion/plaza-carlos.svg)

> 💡 **Observa:** ¡Las posiciones cambiaron completamente al cambiar el origen! Ana ahora está a la **izquierda** de Carlos (coordenada x negativa).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Si te mueves 5 metros hacia la derecha desde el origen, y luego 2 metros hacia la izquierda. ¿Cuál es tu posición final?**

<details>
<summary>Ver solución</summary>

**$x = +3\,\mathrm{m}$.**
$x = 5 - 2 = 3$. Quedas a 3 metros a la derecha del origen.

</details>

---

### Ejercicio 2
**Un pájaro está en la posición $(2, 5)$ respecto a un árbol. Si cambiamos el origen al mismo pájaro, ¿cuál es la posición del árbol?**

<details>
<summary>Ver solución</summary>

**$(-2, -5)$.**
Si el pájaro es el origen $(0,0)$, el árbol está en la posición opuesta. Matemáticamente: $\vec{r}_{árbol} = \vec{0} - (2, 5) = (-2, -5)$.

</details>

---

### Ejercicio 3
**Un ascensor comienza en el piso 2. Sube 4 pisos y luego baja 3 pisos. Si definimos el piso 0 como el origen ($y=0$), ¿cuál es su posición final?**

<details>
<summary>Ver solución</summary>

**$y = +3$ (Piso 3).**
Posición inicial: $y_0 = 2$.
Desplazamiento 1: $+4$.
Desplazamiento 2: $-3$.
Posición final: $y = 2 + 4 - 3 = 3$.

</details>

---

### Ejercicio 4
**Un barco se encuentra en las coordenadas $(-3, 4)$ km respecto a un faro. ¿A qué distancia del faro se encuentra el barco?**

<details>
<summary>Ver solución</summary>

**$5\,\mathrm{km}$.**
Usamos el teorema de Pitágoras:
$$d = \sqrt{(-3)^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\,\mathrm{km}$$

</details>

---

### Ejercicio 5
**Dos coches viajan por una carretera recta. El coche A está en la posición $x_A = 100\,\mathrm{m}$ y el coche B está en $x_B = 150\,\mathrm{m}$. Si el conductor del coche A decide que él es el nuevo origen ($x'_A = 0$), ¿cuál es la nueva posición del coche B?**

<details>
<summary>Ver solución</summary>

**$x'_B = +50\,\mathrm{m}$.**
La posición relativa se calcula restando la posición del nuevo origen:
$x'_B = x_B - x_A = 150 - 100 = 50\,\mathrm{m}$.
Esto significa que el coche B está 50 metros delante del coche A.

</details>

---

## 🔑 Resumen

- La **Posición ($x$)** indica la ubicación de un objeto respecto a un punto de referencia.
- Un **Marco de Referencia** necesita un **Origen ($0$)**, **Ejes** y un **Reloj**.
- El movimiento es **relativo**: las coordenadas de un objeto cambian si movemos el origen, aunque el objeto no se mueva.
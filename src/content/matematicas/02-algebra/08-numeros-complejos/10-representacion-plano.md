# **Representación en el Plano Complejo**

Si los números reales viven en una recta (la recta numérica), ¿dónde viven los números complejos? Necesitan más espacio. Viven en un **plano**. Imagina un mapa de coordenadas: el eje horizontal es para la parte real y el vertical para la parte imaginaria.

---

## 🎯 ¿Qué vas a aprender?

- Cómo dibujar números complejos en el **Plano de Argand**.
- Dónde colocar los reales puros y los imaginarios puros.
- Cómo identificar el cuadrante de un número complejo.
- La interpretación geométrica de sumar complejos (el "Método del Paralelogramo").

---

<div style="width: 100%; box-sizing: border-box;">

![El Plano de Argand](/images/geometria/analitica/argand-vacio.svg)

</div>

---

## 📍 El Plano de Argand

Es idéntico al plano cartesiano que ya conoces, solo cambiamos los nombres:

- **Eje horizontal:** Eje Real (Re).
- **Eje vertical:** Eje Imaginario (Im).

Para graficar un número complejo:

$$
z = a + bi
$$

Simplemente buscamos el punto:

$$
(a, b)
$$

---

## ⚙️ Ejemplos Resueltos

<div style="width: 100%; box-sizing: border-box;">

![Números Complejos en los Cuadrantes](/images/geometria/analitica/argand-cuadrantes.svg)

</div>

### Ejemplo 1: Primer Cuadrante

Grafica:

$$
z = 3 + 2i
$$

**Razonamiento:**

1. Identificamos la Parte Real:

$$
a = 3
$$

2. Identificamos la Parte Imaginaria:

$$
b = 2
$$

3. El punto en el plano es:

$$
(3, 2)
$$

---

### Ejemplo 2: Segundo Cuadrante

Grafica:

$$
z = -4 + i
$$

**Razonamiento:**

1. Parte Real:

$$
a = -4
$$

2. Parte Imaginaria:

$$
b = 1
$$

3. El punto es:

$$
(-4, 1)
$$

---

### Ejemplo 3: Tercer Cuadrante

Grafica:

$$
z = -2 - 3i
$$

**Razonamiento:**

1. Parte Real:

$$
a = -2
$$

2. Parte Imaginaria:

$$
b = -3
$$

3. El punto es:

$$
(-2, -3)
$$

---

### Ejemplo 4: Cuarto Cuadrante

Grafica:

$$
z = 5 - 4i
$$

**Razonamiento:**

1. Parte Real:

$$
a = 5
$$

2. Parte Imaginaria:

$$
b = -4
$$

3. El punto es:

$$
(5, -4)
$$

---

### Ejemplo 5: Ejes (Casos Especiales)

<div style="width: 100%; box-sizing: border-box;">

![Reales e Imaginarios Puros](/images/geometria/analitica/argand-ejes.svg)

</div>

- **Real Puro:**

$$
z = 6
$$

Va en el punto:

$$
(6, 0)
$$

- **Imaginario Puro:**

$$
z = -3i
$$

Va en el punto:

$$
(0, -3)
$$

---

## 📐 Suma Gráfica (Vectores)

Podemos ver los números complejos como **flechas** (vectores) que salen del origen $(0,0)$.
Para sumarlos gráficamente, usamos la **Ley del Paralelogramo**:

Si sumas:

$$
z_1 + z_2
$$

Colocas la cola de la flecha de $z_2$ en la punta de la flecha de $z_1$. El punto final es la suma.

<div style="width: 100%; box-sizing: border-box;">

![Suma Gráfica de Complejos](/images/geometria/analitica/argand-suma.svg)

</div>

### Ejemplo 6: Suma Visual

Suma visualmente:

$$
z_1 = 3 + i
$$

$$
z_2 = 1 + 2i
$$

1. Dibuja la flecha al punto:

$$
(3, 1)
$$

2. Desde ahí, desplázate 1 unidad a la derecha y 2 unidades arriba.
3. Llegas al punto final:

$$
(4, 3)
$$

Efectivamente:

$$
(3+1) + (1+2)i = 4 + 3i
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Determina las coordenadas $(x, y)$ para:

$$
z = 2 + 5i
$$

<details>
<summary>Ver solución</summary>

$$
(2, 5)
$$

</details>

---

### Ejercicio 2
Determina las coordenadas para:

$$
z = -3 + 4i
$$

<details>
<summary>Ver solución</summary>

$$
(-3, 4)
$$

</details>

---

### Ejercicio 3
¿En qué cuadrante está el número?

$$
z = -1 - i
$$

<details>
<summary>Ver solución</summary>

Cuadrante III (porque tanto la parte real como la imaginaria son negativas).

</details>

---

### Ejercicio 4
¿En qué cuadrante está el número?

$$
z = 7 - 2i
$$

<details>
<summary>Ver solución</summary>

Cuadrante IV (parte real positiva, parte imaginaria negativa).

</details>

---

### Ejercicio 5
¿Sobre qué eje está el siguiente número?

$$
z = 10i
$$

<details>
<summary>Ver solución</summary>

Eje Imaginario (Vertical).

</details>

---

### Ejercicio 6
Determina el punto para el opuesto de:

$$
z = 2 + 2i
$$

<details>
<summary>Ver solución</summary>

1. El opuesto es:

$$
-z = -2 - 2i
$$

2. El punto es:

$$
(-2, -2)
$$

</details>

---

### Ejercicio 7
Determina el punto para el conjugado de:

$$
z = -3 + i
$$

<details>
<summary>Ver solución</summary>

1. El conjugado es:

$$
\bar{z} = -3 - i
$$

2. El punto es:

$$
(-3, -1)
$$

</details>

---

### Ejercicio 8
Si sumas gráficamente $(2,0)$ y $(0,3)$, ¿dónde terminas?

<details>
<summary>Ver solución</summary>

En el punto:

$$
(2, 3)
$$

Que representa a:

$$
2 + 3i
$$

</details>

---

### Ejercicio 9
Describe la posición de:

$$
z = -5
$$

<details>
<summary>Ver solución</summary>

Sobre el eje real negativo, punto:

$$
(-5, 0)
$$

</details>

---

### Ejercicio 10
¿Qué punto representa el origen?

<details>
<summary>Ver solución</summary>

$$
(0, 0)
$$

O también:

$$
0 + 0i
$$

</details>

---

## 🔑 Resumen

| Cuadrante | Signos (Re, Im) | Ejemplo |
|:--- |:---: |:--- |
| **I** | $(+, +)$ | $1 + i$ |
| **II** | $(-, +)$ | $-1 + i$ |
| **III** | $(-, -)$ | $-1 - i$ |
| **IV** | $(+, -)$ | $1 - i$ |

> **Conclusión:** El plano complejo es una herramienta visual que nos permite tratar a los números complejos como puntos o vectores bidimensionales, facilitando operaciones como la suma y la resta.

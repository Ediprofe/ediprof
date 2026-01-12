# **Definición de Triángulo**

Si miras a tu alrededor, verás triángulos en puentes, grúas y techos de casas. ¿Te has preguntado por qué es la figura favorita de los ingenieros y arquitectos? No es casualidad: el triángulo es la única figura que no se deforma cuando aplicas fuerza sobre ella. En esta lección, entenderás qué hace tan especial a esta figura de tres lados.

---

## 🎯 ¿Qué vas a aprender?

*   La definición exacta de triángulo y por qué sus vértices no pueden estar alineados.
*   Cómo identificar y nombrar correctamente sus elementos: vértices, lados y ángulos.
*   La relación entre vértices y sus lados opuestos.
*   Por qué el triángulo es la figura más rígida de todas.
*   La regla de oro para saber si tres líneas pueden formar un triángulo (Desigualdad Triangular).

---

## 📐 ¿Qué es un triángulo?

Un triángulo es la figura geométrica más simple que podemos cerrar. Se forma al unir tres puntos que **no están en línea recta**.

> **Definición:** Un triángulo es la unión de tres segmentos determinados por tres puntos no colineales.

![definition](/images/geometria/triangulos/definition.svg)

### ¿Por qué "no colineales"?

Imagina tres puntos en una misma línea recta. Si intentas unirlos, solo obtienes... una línea recta más larga. Para que exista una figura "abierta" y con área interior, necesitamos que al menos un punto se salga de la fila.

![collinear-vs-non](/images/geometria/triangulos/collinear-vs-non.svg)

---

## 🧩 Elementos del Triángulo

Todo triángulo, grande o pequeño, tiene tres componentes fundamentales. Vamos a desglosarlos usando un triángulo estándar llamado $\triangle ABC$.

### 1. Vértices
Son los puntos de las esquinas. Se nombran siempre con **letras mayúsculas**.
*   Ejemplo: $A$, $B$, $C$.

### 2. Lados
Son los segmentos que unen los vértices. Tenemos dos formas de nombrarlos:
*   **Por sus extremos:** Usando las dos letras mayúsculas de los vértices (ej. $\overline{AB}$).
*   **Por su nombre corto:** Usando la **letra minúscula** del vértice que tienen en frente (opuesto).
    *   Lado $a$ está frente al vértice $A$.
    *   Lado $b$ está frente al vértice $B$.
    *   Lado $c$ está frente al vértice $C$.

### 3. Ángulos Interiores
Es la abertura formada por dos lados en cada vértice.
*   Ejemplo: $\angle A$, $\angle B$, $\angle C$.
*   También se pueden nombrar con tres letras, dejando el vértice en el medio: $\angle BAC$ (es lo mismo que $\angle A$).

### Tabla Resumen

| Elemento | Cantidad | Notación |
| :--- | :---: | :--- |
| **Vértices** | 3 | $A$, $B$, $C$ |
| **Lados** | 3 | $\overline{AB}, \overline{BC}, \overline{CA}$  o  $a, b, c$ |
| **Ángulos** | 3 | $\angle A, \angle B, \angle C$ |

![elements](/images/geometria/triangulos/elements.svg)

---

## 🏗️ Propiedad Fundamental: La Rigidez

Toma cuatro palitos y únelos con chinches para formar un cuadrado. Si lo empujas suavemente, se deformará y se convertirá en un rombo. ¡No es rígido!

Ahora haz lo mismo con tres palitos para formar un triángulo. Empújalo. **No se deforma**.

> **Propiedad de Rigidez:** El triángulo es la única figura que no cambia de forma cuando se aplica fuerza en sus vértices (siempre que sus lados no se rompan ni se estiren).

Por esto las torres eléctricas y las bicicletas están llenas de triángulos.

![rigides-de-triangulos](https://cdn.ediprofe.com/img/matematicas/vqr6-rigides-de-triangulos.webp)


---

## 📏 Propiedad de Existencia (Desigualdad Triangular)

No puedes tomar tres palitos de cualquier tamaño y esperar que formen un triángulo. Por ejemplo, si tienes dos lados muy cortos y uno muy largo, los cortos no alcanzarán a tocarse y cerrar la figura.

Para que exista un triángulo, **la suma de dos lados cualquiera debe ser siempre mayor que el tercer lado**.

**Matemáticamente:**

$$
a + b > c
$$

$$
a + c > b
$$

$$
b + c > a
$$

Si alguna de estas sumas falla, el triángulo es imposible.

![desigualdad-triangular](https://cdn.ediprofe.com/img/matematicas/rpng-desigualdad-triangular.webp)


---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Identificación de Lados Opuestos

Dado el triángulo $\triangle PQR$, identifica qué lado se opone a cada ángulo.

**Razonamiento:**
El lado opuesto es aquel que "no toca" al vértice del ángulo. O dicho de otra forma, es el lado formado por las otras dos letras.

1.  Para el ángulo $\angle P$, el lado opuesto conecta $Q$ y $R$.
2.  Para el ángulo $\angle Q$, el lado opuesto conecta $P$ y $R$.
3.  Para el ángulo $\angle R$, el lado opuesto conecta $P$ y $Q$.

![ex1-opposite-sides](/images/geometria/triangulos/ex1-opposite-sides.svg)

**Resultado:**
$$
\text{Opuesto a } P \rightarrow \overline{QR} \text{ (o lado } p)
$$

$$
\text{Opuesto a } Q \rightarrow \overline{PR} \text{ (o lado } q)
$$

$$
\text{Opuesto a } R \rightarrow \overline{PQ} \text{ (o lado } r)
$$

---

### Ejemplo 2: Verificando la Existencia

¿Es posible construir un torneo con lados que midan $3\,\text{cm}$, $4\,\text{cm}$ y $8\,\text{cm}$?

**Datos:**
*   $a = 3$
*   $b = 4$
*   $c = 8$

**Razonamiento:**
Probamos la Desigualdad Triangular. Sumamos los dos más pequeños y vemos si superan al mayor.

$$
3 + 4 = 7
$$

¿Es $7$ mayor que el tercer lado ($8$)?
No, $7 < 8$.

**Conclusión:**
Los lados de 3 y 4 cm son demasiado cortos. Incluso puestos en línea recta solo suman 7 cm, por lo que nunca podrían encontrarse para cerrar un triángulo sobre una base de 8 cm.

![ex2-existence-fail](/images/geometria/triangulos/ex2-existence-fail.svg)

**Resultado:**
$\boxed{\text{No es posible}}$

---

### Ejemplo 3: El Lado Faltante

Tienes dos lados de un triángulo que miden $5$ y $7$. El tercer lado debe ser un número entero. ¿Cuál es la **mínima** longitud que podría tener el tercer lado?

**Datos:**
*   Lado 1 = $5$
*   Lado 2 = $7$
*   Lado 3 = $x$

**Razonamiento:**
La suma de los lados pequeños debe superar al grande.
Si $x$ fuera el lado más pequeño, entonces $x + 5$ debe ser mayor que $7$.

$$
x + 5 > 7
$$

$$
x > 7 - 5
$$

$$
x > 2
$$

El número debe ser mayor que 2. Como buscamos el entero mínimo...

**Resultado:**
$\boxed{3}$

![ex3-missing-side](/images/geometria/triangulos/ex3-missing-side.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En un triángulo $\triangle XYZ$, ¿cuál es el lado opuesto al vértice $Y$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El lado opuesto al vértice $Y$ es el segmento que une los otros dos vértices, $X$ y $Z$. También se puede denotar con la letra minúscula del vértice.

**Resultado:**
$\boxed{\overline{XZ} \text{ o lado } y}$

</details>

---

### Ejercicio 2
Determina si es posible formar un triángulo con lados de $6\,\text{m}$, $7\,\text{m}$ y $15\,\text{m}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sumamos los dos lados menores:
$$
6 + 7 = 13
$$

Comparamos con el lado mayor ($15$):
$$
13 < 15
$$

Como la suma no supera al lado mayor, no pueden cerrarse.

**Resultado:**
$\boxed{\text{No es posible}}$

</details>

---

### Ejercicio 3
Nombra los tres ángulos del triángulo formado por los vértices $D$, $E$ y $F$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Los ángulos se nombran con el vértice en el centro o simplemente con la letra del vértice.

**Resultado:**
$\boxed{\angle D, \angle E, \angle F \text{ o } \angle EDF, \angle DEF, \angle EFD}$

</details>

---

### Ejercicio 4
En el triángulo $\triangle MNO$, el lado $n$ mide 10 y el lado $o$ mide 10. ¿Cómo se llama el lado que une los vértices $N$ y $O$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El lado que une $N$ y $O$ es el que está opuesto al vértice faltante, que es $M$.

**Resultado:**
$\boxed{\text{lado } m \text{ o } \overline{NO}}$

</details>

---

### Ejercicio 5
Calcula si se puede formar un triángulo con lados $5, 5, 5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sumamos dos lados cualquiera: $5 + 5 = 10$.
Comparamos con el tercero: $10 > 5$.
Sí es posible (es un triángulo equilátero).

**Resultado:**
$\boxed{\text{Sí es posible}}$

</details>

---

### Ejercicio 6
Si dos lados de un triángulo miden $3\,\text{cm}$ y $4\,\text{cm}$, ¿cuál es la longitud máxima **entera** posible para el tercer lado?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El tercer lado ($x$) debe ser menor que la suma de los otros dos.
$$x < 3 + 4$$
$$x < 7$$
El entero menor que 7 es 6.

**Resultado:**
$\boxed{6\,\text{cm}}$

</details>

---

### Ejercicio 7
¿Por qué tres puntos alineados no forman un triángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Porque al unirlos se forma un único segmento de recta, no una figura cerrada con área y tres ángulos.

**Resultado:**
$\boxed{\text{Porque son colineales}}$

</details>

---

### Ejercicio 8
En la notación $\triangle GHI$, ¿qué vértice está entre el lado $g$ y el lado $h$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El lado $g$ es opuesto a $G$ (conecta $H$ e $I$).
El lado $h$ es opuesto a $H$ (conecta $G$ e $I$).
Ambos lados se encuentran en el vértice $I$.

**Resultado:**
$\boxed{\text{Vértice } I}$

</details>

---

### Ejercicio 9
Dibuja (mentalmente) un triángulo. Si cortas una esquina, ¿cuántos vértices tendrá la figura resultante?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si cortas una esquina de un triángulo (traspasando una línea recta), eliminas 1 vértice pero creas 2 nuevos. De 3 pasas a 4. Se vuelve un cuadrilátero.

**Resultado:**
$\boxed{4}$

</details>

---

### Ejercicio 10
Menciona un objeto de tu casa que tenga forma triangular para asegurar rigidez.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ejemplos comunes: Percha (gancho) de ropa, escuadra, soporte de repisa, escalera de tijera abierta.

**Resultado:**
$\boxed{\text{Percha / Escuadra}}$

</details>

---

## 🔑 Resumen

| Concepto | Descripción |
| :--- | :--- |
| **Triángulo** | Polígono de 3 lados cerrado. Rigidez total. |
| **Vértices** | Puntos de unión ($A, B, C$). |
| **Lados** | Segmentos que unen vértices ($a, b, c$). |
| **Desigualdad Triangular** | `Lado1 + Lado2 > Lado3`. Condición vital para existir. |

# **Construcción de la Elipse**

Dibujar una elipse perfecta es posible sin computadoras, usando solo cuerdas y estacas. Este método, conocido como "del jardinero", se usa en la vida real para trazar canteros ovalados o mesas de diseño.

---

## 🎯 ¿Qué vas a aprender?

- Cómo dibujar una elipse usando dos puntos fijos (focos).
- Por qué la suma de distancias siempre es constante ($2a$).
- Cómo deducir la ecuación matemática a partir del dibujo.

---

## 🏗️ El Método del Jardinero

Este método aprovecha la definición pura: $d(P, F_1) + d(P, F_2) = \text{Constante}$.

**Pasos:**
1.  Clava dos estacas en el suelo (Focos $F_1$ y $F_2$).
2.  Toma una cuerda que mida más que la distancia entre las estacas. (Longitud de cuerda = $2a$).
3.  Ata los extremos de la cuerda a las estacas.
4.  Con un lápiz, tensa la cuerda y muévete alrededor. ¡La curva que aparece es una elipse!

---

## 📐 Deducción de la Ecuación

Imagina que centramos nuestra elipse en el plano cartesiano $(0,0)$.
*   Focos en $(-c, 0)$ y $(c, 0)$.
*   Longitud de la cuerda: $2a$.

Para cualquier punto $P(x, y)$ en la curva:

$$
\sqrt{(x - (-c))^2 + (y - 0)^2} + \sqrt{(x - c)^2 + (y - 0)^2} = 2a
$$

Si tienes paciencia y elevas al cuadrado dos veces para eliminar las raíces, llegas a la famosa ecuación:

$$
\frac{x^2}{a^2} + \frac{x^2}{a^2 - c^2} = 1
$$

Y como el triángulo sagrado dice que $a^2 - c^2 = b^2$, obtenemos:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Datos del Jardinero
Usamos una cuerda de 10 metros y clavamos estacas a 6 metros de distancia entre sí.
1.  **Cuerda ($2a$):** 10 $\Rightarrow a = 5$.
2.  **Distancia focal ($2c$):** 6 $\Rightarrow c = 3$.
3.  **Ancho de la elipse ($2b$):**
    $$ b = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = 4 $$
    La elipse tendrá 8 metros de ancho ($2b$).

### Ejemplo 2: Construcción Inversa
Queremos una elipse de 20m de largo y 12m de ancho. ¿Dónde ponemos las estacas?
1.  $2a = 20 \Rightarrow a = 10$.
2.  $2b = 12 \Rightarrow b = 6$.
3.  **Posición de focos ($c$):**
    $$ c = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8 $$
    Debemos poner las estacas a 8 metros del centro (16 metros entre ellas).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si la cuerda mide 26 y los focos están a 10 de distancia ($2c=10$). Halla $b$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=13, c=5$.
$b = \sqrt{169 - 25} = 12$.

**Respuesta:** $\boxed{12}$
</details>

---

### Ejercicio 2
¿Qué pasa si la cuerda mide lo mismo que la distancia entre focos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2a = 2c$. No puedes formar un triángulo. Solo trazas una línea recta entre los focos.

**Respuesta:** **Es un segmento de recta**
</details>

---

### Ejercicio 3
Si usas una cuerda de 10m y los focos coinciden ($c=0$), ¿qué dibujas?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=5, c=0$. Es un círculo de radio 5.

**Respuesta:** **Un círculo**
</details>

---

### Ejercicio 4
En el método del jardinero, ¿qué representa la longitud de la cuerda?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la suma de distancias constante.

**Respuesta:** **El Eje Mayor (2a)**
</details>

---

### Ejercicio 5
Calcula $c$ si quieres una elipse con eje mayor 10 y eje menor 8.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=5, b=4$.
$c = \sqrt{25-16} = 3$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 6
Si fijas las estacas en $(-4,0)$ y $(4,0)$, ¿dónde está el centro?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Punto medio.

**Respuesta:** $\boxed{(0,0)}$
</details>

---

### Ejercicio 7
¿Qué herramienta de dibujo técnico puede trazar elipses?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Aparte de la cuerda, existen compases, plantillas y elipsógrafos.

**Respuesta:** **Elipsógrafo o Plantilla**
</details>

---

### Ejercicio 8
Si $a=15$ y $c=9$, ¿cuánto mide la elipse en su parte más ancha (eje menor)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$b = \sqrt{225 - 81} = \sqrt{144} = 12$.
Ancho total $2b = 24$.

**Respuesta:** $\boxed{24}$
</details>

---

### Ejercicio 9
Escribe la ecuación para el caso anterior ($a=15, b=12$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2/225 + y^2/144 = 1$.

**Respuesta:** $\boxed{\frac{x^2}{225} + \frac{y^2}{144} = 1}$
</details>

---

### Ejercicio 10
Deduce: ¿Por qué $a$ siempre es mayor que $c$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Por desigualdad triangular. La suma de dos lados (cuerda $2a$) debe ser mayor que el tercer lado (distancia $2c$).

**Respuesta:** **Desigualdad triangular**
</details>

---

## 🔑 Resumen

| Concepto | Representación Física | Matemáticas |
| :--- | :--- | :--- |
| **Focos** | Las estacas | $(\pm c, 0)$ |
| **Eje Mayor ($2a$)** | La cuerda | Constante de la definición |
| **Dibujo** | Tensar y girar | Lugar geométrico |

> **Conclusión:** La elipse no es una fórmula abstracta; es una figura mecánica que surge naturalmente al restringir el movimiento con una cuerda atada a dos puntos.

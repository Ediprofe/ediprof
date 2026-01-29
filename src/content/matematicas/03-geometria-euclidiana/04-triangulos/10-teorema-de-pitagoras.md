# **Teorema de Pitágoras**

Si las matemáticas tuvieran celebridades, el Teorema de Pitágoras sería la estrella más famosa. Es esa ecuación que todo el mundo recuerda: la suma de los cuadrados de los lados cortos es igual al cuadrado del lado largo. Pero más allá de la fama, es la herramienta fundamental para calcular distancias en diagonal, desde la construcción de pirámides hasta el desarrollo de videojuegos modernos.

---

## 🎯 ¿Qué vas a aprender?

- Identificar quién es quién: Hipotenusa vs. Catetos.
- Aplicar la fórmula $a^2 + b^2 = c^2$ para solucionar problemas.
- Calcular la hipotenusa (el lado largo) sumando áreas.
- Calcular un cateto (el lado corto) restando áreas.
- Reconocer ternas pitagóricas para calcular mentalmente.

---

## 📐 Identificando los Lados

El teorema **SOLO** funciona en triángulos rectángulos (los que tienen una esquina perfecta de 90° o forma de "L").

1.  **Hipotenusa ($c$):**
    - Es el lado más largo.
    - Está siempre **frente** al ángulo recto.
    - Es como la rampa o el tobogán del triángulo.

2.  **Catetos ($a$ y $b$):**
    - Son los dos lados más cortos.
    - Son los que forman el ángulo recto (la "L").

![Identificando Lados](/images/content/matematicas/geometria/triangulos/pythagoras_sides.svg)

---

---

## 🔑 La Fórmula Clave

El área del cuadrado construido sobre la hipotenusa es igual a la suma de las áreas de los cuadrados construidos sobre los catetos.

$$
c^2 = a^2 + b^2
$$

![Fórmula Sagrada](/images/content/matematicas/geometria/triangulos/pythagoras_squares.svg)


### ¿Cómo usarla?

Todo depende de qué lado te falte.

**Caso 1: Buscas la Hipotenusa ($c$)**
Como buscas el lado más grande, **SUMAS**.

$$
c = \sqrt{a^2 + b^2}
$$

**Caso 2: Buscas un Cateto ($a$ o $b$)**
Como buscas un lado más pequeño, tienes que **RESTAR** a la hipotenusa.

$$
a = \sqrt{c^2 - b^2}
$$

$$
b = \sqrt{c^2 - a^2}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Hallando la Hipotenusa

Tienes un triángulo con catetos de 3 cm y 4 cm. ¿Cuánto mide su diagonal (hipotenusa)?

![Hallar Hipotenusa](/images/content/matematicas/geometria/triangulos/pythagoras_ex1.svg)


**Datos:**
$a = 3$
$b = 4$
$c = ?$

**Razonamiento:**
Usamos la fórmula de suma.

$$
c = \sqrt{3^2 + 4^2}
$$

$$
c = \sqrt{9 + 16}
$$

$$
c = \sqrt{25}
$$

**Resultado:**
$$
\boxed{5 \text{ cm}}
$$

---

### Ejemplo 2: Hallando un Cateto

Una escalera de 10 m (hipotenusa) está apoyada en una pared. Si la base está a 6 m de la pared, ¿a qué altura llega?

![Problema Escalera](/images/content/matematicas/geometria/triangulos/pythagoras_ladder.svg)


**Datos:**
$c = 10$ (Escalera/Hipotenusa)
$b = 6$ (Base/Cateto)
$a = ?$ (Altura/Cateto)

**Razonamiento:**
Como buscamos un cateto, usamos la resta.

$$
a = \sqrt{10^2 - 6^2}
$$

$$
a = \sqrt{100 - 36}
$$

$$
a = \sqrt{64}
$$

**Resultado:**
$$
\boxed{8 \text{ m}}
$$

---

### Ejemplo 3: La Diagonal de televisión

Una pantalla de 50 pulgadas (diagonal) tiene un ancho de 40 pulgadas. ¿Cuál es su altura?

![Diagonal TV](/images/content/matematicas/geometria/triangulos/pythagoras_tv.svg)


**Razonamiento:**
La diagonal es la hipotenusa. El ancho es un cateto. Buscamos el otro cateto.

$$
h = \sqrt{50^2 - 40^2}
$$

$$
h = \sqrt{2500 - 1600}
$$

$$
h = \sqrt{900}
$$

**Resultado:**
$$
\boxed{30 \text{ pulgadas}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la hipotenusa de un triángulo rectángulo cuyos catetos miden 5 cm y 12 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
c = \sqrt{5^2 + 12^2}
$$

$$
c = \sqrt{25 + 144}
$$

$$
c = \sqrt{169}
$$

**Resultado:**
$$
\boxed{13 \text{ cm}}
$$

</details>

### Ejercicio 2
Si la hipotenusa mide 15 cm y uno de los catetos mide 9 cm, ¿cuánto mide el otro cateto?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usamos resta.

$$
b = \sqrt{15^2 - 9^2}
$$

$$
b = \sqrt{225 - 81}
$$

$$
b = \sqrt{144}
$$

**Resultado:**
$$
\boxed{12 \text{ cm}}
$$

</details>

### Ejercicio 3
¿Es posible formar un triángulo rectángulo con lados de 2, 3 y 4 metros? (Verifícalo).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Comprobamos si $2^2 + 3^2 = 4^2$.

$$
4 + 9 = 13
$$

$$
4^2 = 16
$$

$$
13 \neq 16
$$

**Resultado:**
$$
\boxed{\text{No es rectángulo}}
$$

</details>

### Ejercicio 4
Calcula la diagonal de un cuadrado cuyo lado mide 1 metro.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
d = \sqrt{1^2 + 1^2}
$$

$$
d = \sqrt{1 + 1}
$$

$$
d = \sqrt{2}
$$

**Resultado:**
$$
\boxed{\approx 1.41 \text{ m}}
$$

</details>

### Ejercicio 5
Un barco navega 8 km al Norte y luego 6 km al Este. ¿A qué distancia en línea recta se encuentra del puerto de salida?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
d = \sqrt{8^2 + 6^2}
$$

$$
d = \sqrt{64 + 36}
$$

$$
d = \sqrt{100}
$$

**Resultado:**
$$
\boxed{10 \text{ km}}
$$

</details>

### Ejercicio 6
Calcula la altura de un triángulo equilátero de lado 2 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La altura divide la base en dos (1 cm y 1 cm).
Se forma un triángulo rectángulo con hipotenusa 2 y cateto base 1.

$$
h = \sqrt{2^2 - 1^2}
$$

$$
h = \sqrt{4 - 1}
$$

**Resultado:**
$$
\boxed{\sqrt{3} \approx 1.73 \text{ cm}}
$$

</details>

### Ejercicio 7
Si la hipotenusa de un triángulo rectángulo es $\sqrt{10}$ y un cateto es 1, halla el otro cateto.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
x = \sqrt{(\sqrt{10})^2 - 1^2}
$$

$$
x = \sqrt{10 - 1}
$$

$$
x = \sqrt{9}
$$

**Resultado:**
$$
\boxed{3}
$$

</details>

### Ejercicio 8
¿Cuál es la longitud de la hipotenusa en un triángulo con catetos iguales de 5 cm?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
c = \sqrt{5^2 + 5^2}
$$

$$
c = \sqrt{25 + 25}
$$

$$
c = \sqrt{50} = \sqrt{25 \cdot 2}
$$

**Resultado:**
$$
\boxed{5\sqrt{2} \text{ cm}}
$$

</details>

### Ejercicio 9
Comprueba si los números (8, 15, 17) forman una terna pitagórica.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
8^2 + 15^2 = 64 + 225 = 289
$$

$$
17^2 = 289
$$

**Resultado:**
$$
\boxed{\text{Sí, lo son}}
$$

</details>

### Ejercicio 10
Una puerta rectangular mide 2 metros de alto y 1 metro de ancho. ¿Pasará un tablero de madera de 2.20 metros de diámetro por la diagonal?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Calculamos la diagonal de la puerta.

$$
D = \sqrt{2^2 + 1^2}
$$

$$
D = \sqrt{4 + 1} = \sqrt{5}
$$

$$
D \approx 2.236 \text{ m}
$$

Como $2.236 > 2.20$, el tablero pasa.

**Resultado:**
$$
\boxed{\text{Sí pasa}}
$$

</details>

---

## 🔑 Resumen

![teorema-de-pitagoras](https://cdn.ediprofe.com/img/matematicas/aigt-teorema-de-pitagoras.webp)


| Concepto | Fórmula | Cuándo usar |
|----------|---------|-------------|
| **Hallar Hipotenusa** | $c = \sqrt{a^2+b^2}$ | Cuando conoces los dos lados cortos. |
| **Hallar Cateto** | $a = \sqrt{c^2-b^2}$ | Cuando conoces la diagonal y un lado corto. |
| **Recíproco** | $a^2+b^2=c^2$ | Para verificar si una esquina es recta (90°). |

> Recuerda: La hipotenusa es egoísta, quiere todo el espacio, por eso **suma**. Los catetos son modestos, si buscas uno, tienes que **restar**.


# **Progresiones Aritméticas**

Imagina una escalera. Cada escalón sube exactamente la misma altura que el anterior. Si el primer escalón está a 10 cm del suelo y cada uno sube 15 cm, ¿a qué altura estarás en el escalón 100? No necesitas subir uno por uno para saberlo; la matemática tiene un atajo llamado "progresión aritmética".

---

## 🎯 ¿Qué vas a aprender?

- **Identificar patrones:** Reconocer secuencias que suman lo mismo siempre.
- **Término General:** Encontrar cualquier valor de la lista sin escribirla toda.
- **Suma de Términos:** El truco de Gauss para sumar cientos de números en segundos.
- **Aplicaciones Reales:** Resolver problemas de ahorros, construcciones y tiempo.

---

## 👣 El Concepto: Paso Constante 

Una progresión aritmética es una sucesión de números donde la diferencia entre un término y el anterior es siempre la misma. A este valor constante lo llamamos **diferencia común** ($$d$$).

### Ejemplo Inductivo
Mira esta secuencia:

$$
3, 7, 11, 15, 19, \dots
$$

Analicemos los saltos:
1. Del 3 al 7 hay:
$$
+4
$$
2. Del 7 al 11 hay:
$$
+4
$$
3. Del 11 al 15 hay:
$$
+4
$$

Como el salto es siempre $$+4$$, decimos que es una progresión aritmética con $$d = 4$$.

---

## 📈 ¿Puntos o Líneas? (Discreto vs Continuo)

Es común confundir una progresión aritmética con una **función lineal** (como una línea recta en un mapa). Sin embargo, hay una diferencia crucial:

1. **La Función Lineal es continua:** Cubre todos los números, como $$1.5$$ o $$\pi$$. Puedes dibujar una línea sin levantar el lápiz.
2. **La Progresión es discreta:** Solo existen los términos en posiciones enteras ($$n=1, n=2, n=3\dots$$). No existe el término "1.5".

![Progresión discreta vs continua](/images/matematicas/algebra/progresiones/progresion_discreta_vs_continua.svg)

**Por qué importa:** 
Cuando graficamos una progresión, representamos **puntos aislados** en el plano. Aunque esos puntos estén perfectamente alineados, la "línea" entre ellos no forma parte de la secuencia; es solo una guía visual para mostrar la tendencia.

---

## 🔍 Encontrando el Término General

Si queremos el término número 100, no vamos a sumar 4 cien veces. Busquemos la lógica detrás de los saltos:

- **Término 1 ($$a_1$$):**
$$
3
$$
- **Término 2 ($$a_2$$):**
$$
3 + 4
$$
- **Término 3 ($$a_3$$):**
$$
3 + 4 + 4 = 3 + 2(4)
$$
- **Término 4 ($$a_4$$):**
$$
3 + 4 + 4 + 4 = 3 + 3(4)
$$

**La Lógica:** Para llegar al término $$n$$, siempre damos un salto menos que la posición. Por ejemplo, para el 4º término, damos 3 saltos. Por eso la fórmula usa $$(n-1)$$:

$$
a_n = a_1 + (n-1)d
$$

**Redondeando la idea:**
Esta fórmula es tu "máquina del tiempo". No importa qué tan lejos esté el número, solo necesitas saber dónde empezaste ($$a_1$$) y de cuánto es el salto ($$d$$).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar un término lejano
En la secuencia $$5, 8, 11, 14, \dots$$, encuentra el término número 20 ($$a_{20}$$).

**1. Identificamos los datos:**
- Primer término ($$a_1$$):
$$
5
$$
- Diferencia ($$d$$):
$$
8 - 5 = 3
$$
- Posición buscada ($$n$$):
$$
20
$$

**2. Aplicamos la fórmula:**
$$
a_{20} = 5 + (20 - 1)(3)
$$
$$
a_{20} = 5 + (19)(3)
$$
$$
a_{20} = 5 + 57 = 62
$$

**Resultado:**
$$
\boxed{62}
$$

---

### Ejemplo 2: Hacia atrás (Diferencia negativa)
Encuentra el término 15 de: $$100, 95, 90, 85, \dots$$

**1. Datos:**
- $$a_1 = 100$$
- $$d = 95 - 100 = -5$$

**2. Cálculo:**
$$
a_{15} = 100 + (14)(-5)
$$
$$
a_{15} = 100 - 70 = 30
$$

**Resultado:**
$$
\boxed{30}
$$

---

### Ejemplo 3: ¿Cuántos términos hay?
Si una secuencia empieza en 4, va de 3 en 3, y termina en 40. ¿Cuántos números tiene?

**Planteamiento:**
Sabemos que el último término ($a_n$) es 40.
$$
40 = 4 + (n-1)(3)
$$

**Despejamos $n$:**
$$
40 - 4 = (n-1)(3)
$$
$$
36 = 3(n-1)
$$
$$
\frac{36}{3} = n - 1
$$
$$
12 = n - 1 \implies n = 13
$$

**Resultado:**
$$
\boxed{\text{Hay 13 términos}}
$$

---

## ➕ La Suma de Gauss

Cuenta la leyenda que al niño Carl Friedrich Gauss le pidieron sumar del 1 al 100 para mantenerlo ocupado. Él en segundos dio la respuesta. ¿Cómo? Notó que si sumaba el primero con el último, el segundo con el penúltimo, etc., ¡siempre daba lo mismo!

- $$1 + 100 = 101$$
- $$2 + 99 = 101$$
- $$3 + 98 = 101$$

Como hay 100 números, se forman 50 parejas de 101.

**Fórmula General:**
$$
S_n = \frac{n}{2}(a_1 + a_n)
$$

**Redondeando la idea:**
Sumar una progresión es como sacar el promedio entre el primero y el último ($$\frac{a_1 + a_n}{2}$$) y multiplicarlo por cuántos números hay ($$n$$).

### Ejemplo 4: Suma rápida
Suma los primeros 20 números de la secuencia: $$2, 6, 10, 14, \dots$$

**1. Encontrar el último término ($$a_{20}$$):**
$$
a_{20} = 2 + 19(4) = 78
$$

**2. Aplicar la suma:**
$$
S_{20} = \frac{20}{2}(2 + 78)
$$
$$
S_{20} = 10(80) = 800
$$

**Resultado:**
$$
\boxed{800}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el 10º término de $$4, 9, 14, 19 \dots$$.

<details>
<summary>Ver solución</summary>

**Datos:**
- $$a_1 = 4$$
- $$d = 5$$

**Cálculo:**
$$
a_{10} = 4 + 9(5)
$$
$$
a_{10} = 4 + 45 = 49
$$

**Resultado:** 
$$
\boxed{49}
$$

</details>

---

### Ejercicio 2
Calcula la diferencia común de $$15, 12, 9, 6 \dots$$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
d = 12 - 15 = -3
$$

**Resultado:** 
$$
\boxed{-3}
$$

</details>

---

### Ejercicio 3
Halla el término general ($$a_n$$) de $$5, 7, 9 \dots$$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
a_n = 5 + (n-1)2
$$
$$
a_n = 5 + 2n - 2
$$
$$
a_n = 2n + 3
$$

**Resultado:** 
$$
\boxed{a_n = 2n + 3}
$$

</details>

---

### Ejercicio 4
Encuentra la suma de los primeros 10 términos de $$1, 2, 3 \dots$$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
a_{10} = 10
$$
$$
S_{10} = \frac{10}{2}(1 + 10)
$$
$$
S_{10} = 5(11) = 55
$$

**Resultado:** 
$$
\boxed{55}
$$

</details>

---

### Ejercicio 5
Si $$a_1 = 2$$ y $$a_5 = 14$$, halla $$d$$.

<details>
<summary>Ver solución</summary>

**Planteamiento:**
$$
a_5 = a_1 + 4d
$$
$$
14 = 2 + 4d
$$
$$
12 = 4d \implies d = 3
$$

**Resultado:** 
$$
\boxed{3}
$$

</details>

---

### Ejercicio 6
 ¿Cuál es el término 100 de los números pares ($$2, 4, 6\dots$$)?

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
a_{100} = 2 + 99(2)
$$
$$
a_{100} = 2 + 198 = 200
$$

**Resultado:** 
$$
\boxed{200}
$$

</details>

---

### Ejercicio 7
Suma: $$10 + 20 + 30 + \dots + 100$$.

<details>
<summary>Ver solución</summary>

**Datos:**
- $$n = 10$$ (del 10 al 100 de 10 en 10 hay 10 términos)
- $$a_1 = 10$$
- $$a_{10} = 100$$

**Cálculo:**
$$
S_{10} = \frac{10}{2}(10 + 100)
$$
$$
S_{10} = 5(110) = 550
$$

**Resultado:** 
$$
\boxed{550}
$$

</details>

---

### Ejercicio 8
Una persona ahorra 500 pesos la primera semana, 600 la segunda, 700 la tercera. ¿Cuánto ahorra en la semana 10?

<details>
<summary>Ver solución</summary>

**Datos:**
- $$a_1 = 500$$
- $$d = 100$$

**Cálculo:**
$$
a_{10} = 500 + 9(100)
$$
$$
a_{10} = 500 + 900 = 1400
$$

**Resultado:** 
$$
\boxed{1400 \text{ pesos}}
$$

</details>

---

### Ejercicio 9
¿Cuántos números impares hay entre 1 y 99 (incluyéndolos)?

<details>
<summary>Ver solución</summary>

**Planteamiento:**
$$
99 = 1 + (n-1)2
$$
$$
98 = 2(n-1)
$$
$$
49 = n-1 \implies n = 50
$$

**Resultado:** 
$$
\boxed{50}
$$

</details>

---

### Ejercicio 10
Inserta 3 medios aritméticos entre 2 y 14.

<details>
<summary>Ver solución</summary>

**Planteamiento:**
En total hay 5 términos ($$2, \_, \_, \_, 14$$).
$$
14 = 2 + 4d
$$
$$
12 = 4d \implies d = 3
$$

**Resultado:** 
$$
\boxed{5, 8, 11}
$$

</details>

---

## 🔑 Resumen


| Concepto | Fórmula | Notas |
| :--- | :--- | :--- |
| **Diferencia ($d$)** | $$d = a_{n} - a_{n-1}$$ | El "paso" constante de la secuencia. |
| **Término General** | $$a_n = a_1 + (n-1)d$$ | Útil para encontrar cualquier valor. |
| **Suma de Términos** | $$S_n = \frac{n}{2}(a_1 + a_n)$$ | El método de Gauss para sumar rápido. |

![progresion-aritmetica](https://cdn.ediprofe.com/img/matematicas/3k9m-progresion-aritmetica.webp)

> **Conclusión:** Las progresiones aritméticas son la base de los crecimientos lineales. Si entiendes que cada paso es igual al anterior, tienes el control de toda la secuencia, sin importar qué tan larga sea.

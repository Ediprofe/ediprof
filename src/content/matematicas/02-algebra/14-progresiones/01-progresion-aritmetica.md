# **Progresiones Aritméticas**

Imagina una escalera. Cada escalón sube exactamente la misma altura que el anterior. Si el primer escalón está a 10 cm del suelo y cada uno sube 15 cm, ¿a qué altura estarás en el escalón 100? No necesitas subir uno por uno para saberlo; la matemática tiene un atajo llamado "progresión aritmética".

---

## 🎯 ¿Qué vas a aprender?

- Identificar patrones numéricos lineales (que suman lo mismo siempre).
- La fórmula para encontrar cualquier término sin escribir toda la lista.
- Cómo sumó Gauss los números del 1 al 100 en segundos (suma de términos).
- Resolver problemas de ahorros y secuencias.

---

## 🪜 El Patrón de la Escalera

Una progresión aritmética es una fila de números donde la diferencia entre uno y el siguiente es siempre constante. A esa diferencia la llamamos **diferencia común** ($d$).

### Ejemplo Inductivo
Mira esta secuencia:
$$
3, 7, 11, 15, 19, \dots
$$

1.  Del 3 al 7 hay +4.
2.  Del 7 al 11 hay +4.
3.  Del 11 al 15 hay +4.

¡Es una progresión aritmética con $d=4$!

---

## 🔍 Encontrando el Término General

Si queremos el término número 100, no vamos a sumar 4 cien veces. Busquemos la lógica.

- **Término 1 ($a_1$):** $3$
- **Término 2 ($a_2$):** $3 + 4$
- **Término 3 ($a_3$):** $3 + 4 + 4 = 3 + 2(4)$
- **Término 4 ($a_4$):** $3 + 4 + 4 + 4 = 3 + 3(4)$

**La Regla:** Para llegar al término $n$, damos $(n-1)$ saltos.

$$
a_n = a_1 + (n-1)d
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar un término lejano
En la secuencia $5, 8, 11, 14, \dots$, encuentra el término número 20 ($a_{20}$).

**Datos:**
- Primer término ($a_1$): 5
- Diferencia ($d$): $8 - 5 = 3$
- Posición buscada ($n$): 20

**Cálculo:**
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
Encuentra el término 15 de: $100, 95, 90, 85, \dots$

**Datos:**
- $a_1 = 100$
- $d = 95 - 100 = -5$ (¡Cuidado con el signo!)

**Cálculo:**
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

Cuenta la leyenda que al niño Carl Friedrich Gauss le pidieron sumar del 1 al 100 para mantenerlo ocupado. Él notó algo curioso:
- $1 + 100 = 101$
- $2 + 99 = 101$
- $3 + 98 = 101$

¡Parejas de igual valor!
La fórmula para sumar $n$ términos es:

$$
S_n = \frac{n}{2}(a_1 + a_n)
$$

### Ejemplo 4: Suma rápida
Suma los primeros 20 números de la secuencia: $2, 6, 10, 14, \dots$

**1. Encontrar el último término ($a_{20}$):**
$$
a_{20} = 2 + 19(4) = 2 + 76 = 78
$$

**2. Aplicar la suma:**
Promedio del primero y el último, multiplicado por la cantidad.
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
Encuentra el 10º término de $4, 9, 14, 19 \dots$.

<details>
<summary>Ver solución</summary>

$a_1 = 4$, $d=5$.
$a_{10} = 4 + 9(5) = 4 + 45$.
**Resultado:** $\boxed{49}$

</details>

---

### Ejercicio 2
Calcula la diferencia común de $15, 12, 9, 6 \dots$.

<details>
<summary>Ver solución</summary>

$12 - 15 = -3$.
**Resultado:** $\boxed{-3}$

</details>

---

### Ejercicio 3
Halla el término general ($a_n$) de $5, 7, 9 \dots$.

<details>
<summary>Ver solución</summary>

$a_n = 5 + (n-1)2 = 5 + 2n - 2$.
**Resultado:** $\boxed{2n + 3}$

</details>

---

### Ejercicio 4
Encuentra la suma de los primeros 10 términos de $1, 2, 3 \dots$.

<details>
<summary>Ver solución</summary>

$a_{10} = 10$.
$S_{10} = \frac{10}{2}(1 + 10) = 5(11)$.
**Resultado:** $\boxed{55}$

</details>

---

### Ejercicio 5
Si $a_1 = 2$ y $a_5 = 14$, halla $d$.

<details>
<summary>Ver solución</summary>

4 saltos nos llevan de 2 a 14.
$2 + 4d = 14 \implies 4d = 12$.
**Resultado:** $\boxed{d = 3}$

</details>

---

### Ejercicio 6
 ¿Cuál es el término 100 de los números pares ($2, 4, 6\dots$)?

<details>
<summary>Ver solución</summary>

$a_{100} = 2 + 99(2) = 2 + 198$.
**Resultado:** $\boxed{200}$

</details>

---

### Ejercicio 7
Suma: $10 + 20 + 30 + \dots + 100$.

<details>
<summary>Ver solución</summary>

Hay 10 términos.
$S = \frac{10}{2}(10 + 100) = 5(110)$.
**Resultado:** $\boxed{550}$

</details>

---

### Ejercicio 8
Una persona ahorra 500 pesos la primera semana, 600 la segunda, 700 la tercera. ¿Cuánto ahorra en la semana 10?

<details>
<summary>Ver solución</summary>

$a_1 = 500, d = 100$.
$a_{10} = 500 + 9(100)$.
**Resultado:** $\boxed{1400 \text{ pesos}}$

</details>

---

### Ejercicio 9
¿Cuántos números impares hay entre 1 y 99 (incluyéndolos)?

<details>
<summary>Ver solución</summary>

$1, 3, \dots, 99$.
$99 = 1 + (n-1)2 \implies 98 = 2(n-1) \implies 49 = n-1$.
**Resultado:** $\boxed{50}$

</details>

---

### Ejercicio 10
Inserta 3 medios aritméticos entre 2 y 14 (es decir, completa $2, \_, \_, \_, 14$).

<details>
<summary>Ver solución</summary>

Hay 5 términos en total. $a_5 = 14$.
$2 + 4d = 14 \implies 4d = 12 \implies d=3$.
$2+3=5, 5+3=8, 8+3=11$.
**Resultado:** $\boxed{5, 8, 11}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Notas |
|:--- |:--- |:--- |
| **Término General** | $a_n = a_1 + (n-1)d$ | Para encontrar un valor específico. |
| **Suma** | $S_n = \frac{n}{2}(a_1 + a_n)$ | Para sumar toda la lista rápido. |
| **Diferencia** | $d = a_2 - a_1$ | Lo que crece o decrece. |

> **Conclusión:** Las progresiones aritméticas son simplemente "contar de tanto en tanto". Si entiendes que multiplicar es sumar repetidamente, ya entiendes las progresiones.

# **Perímetro y Área de Polígonos Regulares**

Cuando un polígono tiene todos sus lados y ángulos iguales, se llama regular. Su simetría hace que calcular su área sea mucho más fácil, usando un elemento clave llamado **apotema**.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el perímetro multiplicando el número de lados por la longitud de uno.
- Entender qué es la **apotema** (del centro a la mitad del lado).
- Aplicar la fórmula general de área: $\frac{P \cdot a}{2}$.
- Resolver problemas de pentágonos, hexágonos y octógonos.

---

## 📏 Perímetro ($P$)

Como todos los lados son iguales, solo necesitas multiplicar.

$$
P = n \times l
$$

*   $n$: Número de lados.
*   $l$: Longitud de cada lado.

### Ejemplos
*   Pentágono ($n=5$) de lado 3: $P = 5 \times 3 = 15$.
*   Hexágono ($n=6$) de lado 2: $P = 6 \times 2 = 12$.

---

## 📐 Área ($A$)

El área de cualquier polígono regular se calcula con su perímetro y su apotema.

$$
A = \frac{P \times a}{2}
$$

**¿Qué es la apotema ($a$)?**
Es la distancia desde el **centro** del polígono hasta el **punto medio** de cualquiera de sus lados. Funciona como la "altura" de los triángulos que forman el polígono.

### ¿Por qué funciona la fórmula?
Si divides el polígono en $n$ triángulos iguales, cada uno tiene base $l$ y altura $a$.
Área triángulo = $\frac{l \cdot a}{2}$.
Área total = $n \times \frac{l \cdot a}{2} = \frac{(n \cdot l) \cdot a}{2} = \frac{P \cdot a}{2}$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Pentágono Regular

Lado = 6 cm, Apotema = 4 cm.

**Razonamiento:**
1.  Calculamos Perímetro: $P = 5 \times 6 = 30 \text{ cm}$.
2.  Calculamos Área:

$$
A = \frac{30 \times 4}{2} = \frac{120}{2}
$$

**Resultado:**
$$
\boxed{60 \text{ cm}^2}
$$

### Ejemplo 2: Hexágono Regular

Lado = 4 m, Apotema = 3.5 m.

**Razonamiento:**
1.  Perímetro ($n=6$): $P = 6 \times 4 = 24 \text{ m}$.
2.  Área:

$$
A = \frac{24 \times 3.5}{2} = \frac{84}{2}
$$

**Resultado:**
$$
\boxed{42 \text{ m}^2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Perímetro de un octógono regular de lado 5 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$n=8$.
$P = 8 \times 5$.

**Resultado:**
$$
\boxed{40 \text{ cm}}
$$

</details>

### Ejercicio 2
Área de un pentágono con perímetro 20 y apotema 3.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{20 \cdot 3}{2} = \frac{60}{2}$.

**Resultado:**
$$
\boxed{30}
$$

</details>

### Ejercicio 3
Calcula el área de un hexágono regular de lado 10 y apotema 8.7.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$P = 6 \times 10 = 60$.
$A = \frac{60 \cdot 8.7}{2}$.

**Resultado:**
$$
\boxed{261}
$$

</details>

### Ejercicio 4
Si el área es 100 y el perímetro 40, ¿cuánto mide la apotema?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$100 = \frac{40 \cdot a}{2} \Rightarrow 100 = 20a \Rightarrow a=5$.

**Resultado:**
$$
\boxed{5}
$$

</details>

### Ejercicio 5
Decágono regular ($n=10$) de lado 2. Perímetro:

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$10 \times 2$.

**Resultado:**
$$
\boxed{20}
$$

</details>

### Ejercicio 6
Verdadero o Falso: La apotema es lo mismo que el radio del polígono.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. El radio va al vértice; la apotema va al centro del lado (es más corta).

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 7
Un cuadrado es un polígono regular ($n=4$). Si lado=4, apotema=2. Comprueba la fórmula.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$P = 16$.
$A = \frac{16 \cdot 2}{2} = 16$.
Coincide con $l^2 = 4^2 = 16$.

**Resultado:**
$$
\boxed{16}
$$

</details>

### Ejercicio 8
Perímetro de un heptágono ($n=7$) de lado 3.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$7 \times 3$.

**Resultado:**
$$
\boxed{21}
$$

</details>

### Ejercicio 9
Si el lado se duplica, ¿qué pasa con el perímetro?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Se duplica}
$$

</details>

### Ejercicio 10
Área de un triángulo equilátero ($n=3$) con lado 10 y apotema 2.9 (aprox).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$P = 30$.
$A = \frac{30 \cdot 2.9}{2} = \frac{87}{2}$.

**Resultado:**
$$
\boxed{43.5}
$$

</details>

---

## 🔑 Resumen

| Figura | Fórmula General |
| :--- | :--- |
| **Polígono Regular** | $\frac{P \cdot a}{2}$ |

> No confundas **Apotema** (al lado) con **Radio** (al vértice). La apotema es la que necesitas para el área.

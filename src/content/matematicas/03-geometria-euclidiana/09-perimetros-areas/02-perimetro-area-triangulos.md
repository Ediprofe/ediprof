# **Perímetro y Área de Triángulos**

El triángulo es la figura más estable en la construcción y la más básica en geometría. Si sabes calcular su área, puedes calcular el área de cualquier polígono dividiéndolo en triángulos.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el perímetro sumando los tres lados.
- Aplicar la fórmula clásica del área: $\text{Base} \times \text{Altura} / 2$.
- Calcular el área de un triángulo rectángulo usando sus catetos.
- Usar la fórmula de Herón cuando solo conoces los lados.

---

## 📏 Perímetro ($P$)

Es simplemente la suma de las longitudes de sus tres lados.

$$
P = a + b + c
$$

### Ejemplo
Un triángulo con lados 3 cm, 4 cm y 5 cm.
$$
P = 3 + 4 + 5 = 12 \text{ cm}
$$

---

## 📐 Área ($A$)

### 1. Fórmula General (Base y Altura)
Es la mitad del área de un rectángulo que tuviera la misma base y altura.

$$
A = \frac{\text{base} \times \text{altura}}{2} = \frac{b \cdot h}{2}
$$

> **Nota:** La altura ($h$) es siempre la línea perpendicular (90°) desde un vértice hasta el lado opuesto (base).

### 2. Triángulo Rectángulo
Aquí es muy fácil: los catetos funcionan como base y altura.

$$
A = \frac{\text{cateto}_1 \times \text{cateto}_2}{2}
$$

### 3. Fórmula de Herón (Solo Lados)
Si no te dan la altura, pero tienes los tres lados ($a, b, c$), primero calculas el **semiperímetro** ($s$):

$$
s = \frac{a + b + c}{2}
$$

Y luego aplicas la fórmula mágica:

$$
A = \sqrt{s(s-a)(s-b)(s-c)}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Fórmula Básica

Calcula el área de un triángulo con base $b=10$ cm y altura $h=5$ cm.

**Razonamiento:**
Aplicamos la fórmula $bh/2$.

$$
A = \frac{10 \cdot 5}{2} = \frac{50}{2}
$$

**Resultado:**
$$
\boxed{25 \text{ cm}^2}
$$

### Ejemplo 2: Triángulo Rectángulo

Calcula el área de un triángulo rectángulo con catetos de 3 m y 4 m.

**Razonamiento:**
Los catetos son perpendiculares, así que uno es base y el otro altura.

$$
A = \frac{3 \cdot 4}{2} = \frac{12}{2}
$$

**Resultado:**
$$
\boxed{6 \text{ m}^2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el perímetro de un triángulo equilátero de lado 6 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$P = 6+6+6$.

**Resultado:**
$$
\boxed{18 \text{ cm}}
$$

</details>

### Ejercicio 2
Calcula el área si $b=8$ y $h=3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{8 \cdot 3}{2} = \frac{24}{2}$.

**Resultado:**
$$
\boxed{12}
$$

</details>

### Ejercicio 3
Perímetro de un triángulo isósceles con lados iguales de 10 cm y base 5 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$10+10+5$.

**Resultado:**
$$
\boxed{25 \text{ cm}}
$$

</details>

### Ejercicio 4
Si el área es 20 y la base es 10, ¿cuánto mide la altura?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$20 = (10 \cdot h)/2 \Rightarrow 40 = 10h \Rightarrow h=4$.

**Resultado:**
$$
\boxed{4}
$$

</details>

### Ejercicio 5
Calcula el área usando Herón: Lados 3, 4, 5.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$s = (3+4+5)/2 = 6$.
$A = \sqrt{6(6-3)(6-4)(6-5)} = \sqrt{6 \cdot 3 \cdot 2 \cdot 1} = \sqrt{36}$.

**Resultado:**
$$
\boxed{6}
$$

</details>

### Ejercicio 6
Verdadero o Falso: La altura siempre divide a la base en dos partes iguales.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. Solo ocurre en triángulos isósceles o equiláteros.

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 7
Calcula el área de un triángulo rectángulo isósceles con catetos de 2 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2 \cdot 2}{2}$.

**Resultado:**
$$
\boxed{2 \text{ cm}^2}
$$

</details>

### Ejercicio 8
¿Cuál es la altura de un triángulo equilátero de lado 2? (Usa Pitágoras).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Divide en dos. Hipotenusa=2, base=1.
$h = \sqrt{2^2 - 1^2} = \sqrt{3}$.

**Resultado:**
$$
\boxed{\sqrt{3}}
$$

</details>

### Ejercicio 9
Si duplicas la base y mantienes la altura, ¿qué pasa con el área?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2b \cdot h}{2} = 2(\frac{bh}{2})$.

**Resultado:**
$$
\boxed{\text{Se duplica}}
$$

</details>

### Ejercicio 10
Triángulo con perímetro 12 y lados 3, 4, 5. ¿Es rectángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$3^2 + 4^2 = 9+16=25=5^2$. Sí, cumple Pitágoras.

**Resultado:**
$$
\boxed{\text{Sí}}
$$

</details>

---

## 🔑 Resumen

| Figura | Fórmula de Área ($A$) |
| :--- | :--- |
| **General** | $\frac{b \cdot h}{2}$ |
| **Rectángulo** | $\frac{\text{cateto} \cdot \text{cateto}}{2}$ |
| **Herón** (Lados) | $\sqrt{s(s-a)(s-b)(s-c)}$ |

> La base puede ser cualquier lado, pero la altura debe ser perpendicular a ESE lado.

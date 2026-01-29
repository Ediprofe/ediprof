# **Cono**

Un cono es como una pirámide, pero con una base circular. Es el cuerpo geométrico de los helados, los gorros de fiesta y los conos de tráfico.

---

## 🎯 ¿Qué vas a aprender?

- Calcular la **Generatriz** usando el Teorema de Pitágoras.
- Calcular el **Área Lateral** (el envoltorio del cono) y el **Área Total**.
- Calcular el **Volumen** ($V = \pi r^2 h / 3$).
- Entender la relación de "un tercio" con el cilindro.

---

## 🍦 Elementos del Cono

1.  **Base:** Un círculo de radio $r$.
2.  **Altura ($h$):** Distancia perpendicular desde el centro de la base hasta la punta.
3.  **Generatriz ($g$):** Es la hipotenusa del triángulo formado por la altura y el radio. Es la distancia por el borde desde la base hasta la punta.
4.  **Vértice (Cúspide):** El punto más alto.

---

## 📏 Fórmulas Fundamentales

### 1. Generatriz ($g$)
Usamos Pitágoras.

$$
g^2 = h^2 + r^2 \Rightarrow g = \sqrt{h^2 + r^2}
$$

### 2. Volumen ($V$)
Es la tercera parte de un cilindro con la misma base y altura.

$$
V = \frac{\pi r^2 h}{3}
$$

### 3. Área Lateral ($A_L$)
Es el área de la superficie curva.

$$
A_L = \pi \cdot r \cdot g
$$

### 4. Área Total ($A_T$)
Área lateral más el área de la base.

$$
A_T = \pi r g + \pi r^2 = \pi r (g+r)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo de Generatriz

Un cono tiene radio 3 cm y altura 4 cm.

**Razonamiento:**
Pitágoras: $g^2 = 3^2 + 4^2 = 9 + 16 = 25$.
$g = \sqrt{25}$.

**Resultado:**
$$
\boxed{5 \text{ cm}}
$$

### Ejemplo 2: Volumen y Área

Del cono anterior ($r=3, h=4, g=5$).

**Razonamiento:**
*   **Volumen:** $\frac{\pi(3^2)(4)}{3} = \frac{36\pi}{3} = 12\pi$.
*   **Área Lateral:** $\pi(3)(5) = 15\pi$.
*   **Área Total:** $15\pi + \pi(3^2) = 15\pi + 9\pi = 24\pi$.

**Resultado:**
$$
\boxed{V = 12\pi \text{ cm}^3, A_T = 24\pi \text{ cm}^2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Volumen de un cono con $r=2$ m y $h=3$ m.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$V = \frac{\pi(4)(3)}{3} = 4\pi$.

**Resultado:**
$$
\boxed{4\pi \approx 12.57 \text{ m}^3}
$$

</details>

### Ejercicio 2
Calcula la generatriz si $r=5$ y $h=12$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$g = \sqrt{25 + 144} = \sqrt{169}$.

**Resultado:**
$$
\boxed{13}
$$

</details>

### Ejercicio 3
Área lateral de un cono con $r=6$ y $g=10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A_L = \pi(6)(10)$.

**Resultado:**
$$
\boxed{60\pi}
$$

</details>

### Ejercicio 4
Si el volumen es $30\pi$ y el área de la base es $9\pi$, halla la altura.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A_b = 9\pi \Rightarrow r=3$.
$30\pi = \frac{9\pi \cdot h}{3} \Rightarrow 30\pi = 3\pi h \Rightarrow h=10$.

**Resultado:**
$$
\boxed{10}
$$

</details>

### Ejercicio 5
Calcula el Área Total si $r=4$ y $g=6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A_T = \pi(4)(6) + \pi(4^2) = 24\pi + 16\pi$.

**Resultado:**
$$
\boxed{40\pi}
$$

</details>

### Ejercicio 6
Un cono tiene altura igual a su radio ($h=r$). Si $r=3$, calcula $V$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$V = \frac{\pi(9)(3)}{3} = 9\pi$.

**Resultado:**
$$
\boxed{9\pi}
$$

</details>

### Ejercicio 7
Si duplicas la altura de un cono, ¿qué pasa con el volumen?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$V' = \frac{\pi r^2 (2h)}{3} = 2V$.

**Resultado:**
$$
\boxed{Se duplica}
$$

</details>

### Ejercicio 8
Área lateral de un cono equilátero (el corte es un triángulo equilátero, $g = 2r$). Si $r=5$, calcula $A_L$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$g = 10$.
$A_L = \pi(5)(10)$.

**Resultado:**
$$
\boxed{50\pi}
$$

</details>

### Ejercicio 9
Diferencia de volumen entre un cilindro y un cono de igual base ($r=3$) y altura ($h=10$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cilindro: $90\pi$.
Cono: $30\pi$.
Diferencia: $60\pi$.

**Resultado:**
$$
\boxed{60\pi}
$$

</details>

### Ejercicio 10
Cantidad de papel para un gorro de fiesta ($r=10, h=24$). (Sin base).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Necesitamos $g$. $\sqrt{100+576} = \sqrt{676} = 26$.
Área Lateral = $\pi(10)(26)$.

**Resultado:**
$$
\boxed{260\pi \approx 816.8 \text{ cm}^2}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula |
| :--- | :--- |
| **Volumen** | $\frac{\pi r^2 h}{3}$ |
| **Generatriz ($g$)** | $\sqrt{h^2+r^2}$ |
| **Área Lateral** | $\pi r g$ |

> **Truco:** Siempre dibuja el triángulo rectángulo interno formado por $h$, $r$ y $g$. Ahí está la clave.

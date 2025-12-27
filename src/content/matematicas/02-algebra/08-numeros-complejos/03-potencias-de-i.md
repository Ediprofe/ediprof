# **Potencias de i**

Imagina un reloj que solo tiene 4 horas. Cada vez que multiplicas por $i$, la aguja avanza una hora. Después de 4 veces, vuelves al principio. Este comportamiento cíclico hace que calcular potencias enormes (como $i^{2000}$) sea increíblemente fácil si conoces el secreto del número 4.

---

## 🎯 ¿Qué vas a aprender?

- El ciclo de 4 pasos de las potencias de $i$.
- Cómo calcular cualquier potencia positiva ($i^n$).
- Cómo calcular potencias negativas ($i^{-n}$).
- Patrones interesantes en sumas de potencias consecutivas.

---

## 🔄 El Ciclo de 4 Pasos

Empecemos multiplicando $i$ por sí mismo varias veces:

1. **Uno:** $i^1 = i$
2. **Dos:** $i^2 = -1$ (Por definición)
3. **Tres:** $i^3 = i^2 \cdot i = (-1) \cdot i = -i$
4. **Cuatro:** $i^4 = i^2 \cdot i^2 = (-1)(-1) = 1$

¡Si seguimos, se repite!
- $i^5 = i^4 \cdot i = 1 \cdot i = i$ (Igual a $i^1$)
- $i^6 = i^4 \cdot i^2 = 1 \cdot (-1) = -1$ (Igual a $i^2$)

### **La Tabla Maestra**

Todo depende del residuo (lo que sobra) al dividir el exponente entre 4:

| Residuo | Valor Equivalente | Resultado Final |
|:---:|:---:|:---:|
| **1** | $i^1$ | $i$ |
| **2** | $i^2$ | $-1$ |
| **3** | $i^3$ | $-i$ |
| **0** | $i^4$ | $1$ |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Exponente Grande

Calcula $i^{53}$.

**Razonamiento:**
Dividimos 53 entre 4.
$53 = 13 \times 4 + 1$.
El residuo es **1**.

**Cálculo:**

$$
i^{53} = i^1 = i
$$

**Resultado:**

$$
\boxed{i}
$$

---

### Ejemplo 2: Exponente Exacto

Calcula $i^{100}$.

**Razonamiento:**
100 es múltiplo de 4 ($25 \times 4$). El residuo es **0**.

**Cálculo:**

$$
i^{100} = i^0 = i^4 = 1
$$

**Resultado:**

$$
\boxed{1}
$$

---

### Ejemplo 3: Potencia Negativa

Calcula $i^{-3}$.

**Razonamiento:**
Recordemos que $x^{-n} = 1/x^n$.

$$
i^{-3} = \frac{1}{i^3}
$$

Sustituimos $i^3 = -i$.

$$
\frac{1}{-i}
$$

Para eliminar la $i$ del denominador, multiplicamos por $i/i$:

$$
\frac{1 \cdot i}{-i \cdot i} = \frac{i}{-i^2} = \frac{i}{-(-1)} = \frac{i}{1} = i
$$

**Resultado:**

$$
\boxed{i}
$$

---

### Ejemplo 4: Suma de Potencias

Calcula $i^{10} + i^{12}$.

**Paso 1: Simplificar cada una**
- $10 \div 4 \rightarrow$ Residuo 2. Así que $i^{10} = i^2 = -1$.
- $12 \div 4 \rightarrow$ Residuo 0. Así que $i^{12} = i^4 = 1$.

**Paso 2: Sumar**

$$
-1 + 1
$$

**Resultado:**

$$
\boxed{0}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $i^{22}$.

<details>
<summary>Ver solución</summary>

$22 \div 4$ da residuo 2.

$$
i^{22} = i^2 = -1
$$

**Resultado:**

$$
\boxed{-1}
$$

</details>

---

### Ejercicio 2
Calcula $i^{33}$.

<details>
<summary>Ver solución</summary>

$33 \div 4$ da residuo 1.

$$
i^{33} = i^1 = i
$$

**Resultado:**

$$
\boxed{i}
$$

</details>

---

### Ejercicio 3
Calcula $i^{103}$.

<details>
<summary>Ver solución</summary>

$103 \div 4$ da residuo 3.

$$
i^{103} = i^3 = -i
$$

**Resultado:**

$$
\boxed{-i}
$$

</details>

---

### Ejercicio 4
Calcula $i^{80}$.

<details>
<summary>Ver solución</summary>

80 es múltiplo exacto de 4 (residuo 0).

$$
i^{80} = 1
$$

**Resultado:**

$$
\boxed{1}
$$

</details>

---

### Ejercicio 5
Simplifica $i^{4n + 3}$ (donde $n$ es entero).

<details>
<summary>Ver solución</summary>

$i^{4n} \cdot i^3 = (i^4)^n \cdot i^3 = 1^n \cdot (-i) = -i$.

**Resultado:**

$$
\boxed{-i}
$$

</details>

---

### Ejercicio 6
Calcula $i^{-1}$.

<details>
<summary>Ver solución</summary>

$$
\frac{1}{i} = \frac{i}{i^2} = \frac{i}{-1} = -i
$$

**Resultado:**

$$
\boxed{-i}
$$

</details>

---

### Ejercicio 7
Calcula $i^6 \cdot i^7$.

<details>
<summary>Ver solución</summary>

Propiedad de potencias: $i^{6+7} = i^{13}$.
$13 \div 4$ da residuo 1.

**Resultado:**

$$
\boxed{i}
$$

</details>

---

### Ejercicio 8
Calcula $(2i)^3$.

<details>
<summary>Ver solución</summary>

$$
2^3 \cdot i^3 = 8 \cdot (-i) = -8i
$$

**Resultado:**

$$
\boxed{-8i}
$$

</details>

---

### Ejercicio 9
Simplifica $i^{2023}$.

<details>
<summary>Ver solución</summary>

$2023 \div 4$. Observamos los últimos dos dígitos (23).
$23 \div 4$ da residuo 3.

$$
i^{2023} = i^3 = -i
$$

**Resultado:**

$$
\boxed{-i}
$$

</details>

---

### Ejercicio 10
Suma: $i + i^2 + i^3 + i^4$.

<details>
<summary>Ver solución</summary>

$$
i + (-1) + (-i) + 1 = 0
$$

**Resultado:**

$$
\boxed{0}
$$

</details>

---

## 🔑 Resumen

| Potencia Clave | Valor | Truco de Memoria |
|:--- |:--- |:--- |
| $i^0$ o $i^4$ | **1** | Vuelta completa |
| $i^1$ | **i** | Una hora |
| $i^2$ | **-1** | Media vuelta (*el más importante*) |
| $i^3$ | **-i** | Tres cuartos |

> **Conclusión:** Cualquier potencia de $i$, por gigante que sea, siempre será uno de estos cuatro resultados: $1, i, -1, -i$.

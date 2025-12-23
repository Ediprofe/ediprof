# Multiplicación de vectores

La **multiplicación de un vector por un escalar** permite cambiar el tamaño o el sentido de un vector sin alterar su dirección.

---

## 🎯 ¿Qué vas a aprender?

- A multiplicar un vector por un número (escalar)
- Cómo cambia la magnitud y el sentido según el valor del escalar
- A aplicar la multiplicación por componentes
- Aplicaciones prácticas en física

---

## 🔢 **¿Qué significa multiplicar por un escalar?**

Cuando un vector se multiplica por un **número real** (escalar), se obtiene otro vector en la **misma dirección**, pero con **magnitud diferente**.

Si $\vec{A}$ es un vector y $k$ es un escalar:

$$
\vec{B} = k\vec{A}
$$

El nuevo vector $\vec{B}$:
- Tiene la **misma dirección** que $\vec{A}$
- Su **magnitud** es $|k| \times |\vec{A}|$
- Su **sentido** depende del signo de $k$

---

## 📊 **Casos según el valor de k**

| Valor de $k$ | Efecto sobre el vector |
| :--- | :--- |
| $k > 1$ | Más largo, mismo sentido |
| $k = 1$ | Sin cambio (idéntico) |
| $0 < k < 1$ | Más corto, mismo sentido |
| $k = 0$ | Vector nulo (desaparece) |
| $k = -1$ | Misma magnitud, sentido opuesto |
| $k < -1$ | Más largo, sentido opuesto |
| $-1 < k < 0$ | Más corto, sentido opuesto |

### Visualización:

![alt text](/public/images/fisica/vectores/vector-por-escalar.png)

> 💡 Observa cómo el vector **2A⃗** es el doble de largo, **0.5A⃗** es la mitad, y **-A⃗** tiene sentido opuesto.

---

## ✏️ **Ejemplo: Escalar de velocidad**

Supón que $\vec{A}$ representa una velocidad de $4\,\mathrm{m/s}$ hacia el este:

| Operación | Resultado |
| :--- | :--- |
| $2\vec{A}$ | $8\,\mathrm{m/s}$ hacia el este |
| $\frac{1}{2}\vec{A}$ | $2\,\mathrm{m/s}$ hacia el este |
| $-\vec{A}$ | $4\,\mathrm{m/s}$ hacia el **oeste** |
| $-2\vec{A}$ | $8\,\mathrm{m/s}$ hacia el **oeste** |

> 💡 **Observa:** El escalar negativo **invierte el sentido** del vector.

---

## 🧮 **Multiplicación por componentes**

Si el vector está expresado en componentes:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

Entonces:

$$
k\vec{A} = (kA_x)\,\hat{i} + (kA_y)\,\hat{j}
$$

> 💡 **Regla simple:** Cada componente se multiplica por $k$.

### Ejemplo:

$$
\vec{A} = 3\,\hat{i} + 2\,\hat{j}, \quad k = 2
$$

$$
2\vec{A} = 2(3)\,\hat{i} + 2(2)\,\hat{j} = 6\,\hat{i} + 4\,\hat{j}
$$

### Otro ejemplo con negativo:

$$
\vec{B} = 4\,\hat{i} - 6\,\hat{j}, \quad k = -1
$$

$$
-\vec{B} = (-1)(4)\,\hat{i} + (-1)(-6)\,\hat{j} = -4\,\hat{i} + 6\,\hat{j}
$$

---

## 📐 **Propiedades de la multiplicación por escalar**

| Propiedad | Expresión |
| :--- | :--- |
| **Asociativa** | $k(m\vec{A}) = (km)\vec{A}$ |
| **Distributiva en escalares** | $(k + m)\vec{A} = k\vec{A} + m\vec{A}$ |
| **Distributiva en vectores** | $k(\vec{A} + \vec{B}) = k\vec{A} + k\vec{B}$ |
| **Identidad** | $1 \cdot \vec{A} = \vec{A}$ |
| **Anulación** | $0 \cdot \vec{A} = \vec{0}$ |

---

## ⚡ **Aplicaciones en física**

La multiplicación por escalar aparece en muchas fórmulas físicas:

### Segunda Ley de Newton

$$
\vec{F} = m\vec{a}
$$

La masa $m$ (escalar) multiplica a la aceleración $\vec{a}$ (vector) para dar la fuerza $\vec{F}$ (vector).

> Si duplicas la masa, duplicas la fuerza (para la misma aceleración).

### Velocidad en MRU

$$
\vec{v} = \frac{\vec{d}}{t}
$$

Equivale a multiplicar el desplazamiento por $\frac{1}{t}$.

### Momento lineal

$$
\vec{p} = m\vec{v}
$$

La masa (escalar) multiplica a la velocidad (vector).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Si $\vec{A} = 5\,\hat{i} + 3\,\hat{j}$, calcula $3\vec{A}$.**

<details>
<summary>Ver solución</summary>

$$
3\vec{A} = 3(5\,\hat{i} + 3\,\hat{j}) = 15\,\hat{i} + 9\,\hat{j}
$$

</details>

---

### Ejercicio 2
**Si $\vec{B} = 8\,\hat{i} - 4\,\hat{j}$, calcula $-\vec{B}$ y $0.5\vec{B}$.**

<details>
<summary>Ver solución</summary>

$$
-\vec{B} = -8\,\hat{i} + 4\,\hat{j}
$$

$$
0.5\vec{B} = 4\,\hat{i} - 2\,\hat{j}
$$

</details>

---

### Ejercicio 3
**Un vector de velocidad es $\vec{v} = 6\,\mathrm{m/s}$ hacia el este. Describe $-2\vec{v}$.**

<details>
<summary>Ver solución</summary>

$$
-2\vec{v} = 12\,\mathrm{m/s} \text{ hacia el oeste}
$$

El factor $-2$:
- Duplica la magnitud: $2 \times 6 = 12\,\mathrm{m/s}$
- Invierte el sentido: de este a oeste

</details>

---

### Ejercicio 4
**Demuestra que $2(\vec{A} + \vec{B}) = 2\vec{A} + 2\vec{B}$ usando $\vec{A} = 1\,\hat{i} + 2\,\hat{j}$ y $\vec{B} = 3\,\hat{i} + 4\,\hat{j}$.**

<details>
<summary>Ver solución</summary>

**Lado izquierdo:**

$$
\vec{A} + \vec{B} = 4\,\hat{i} + 6\,\hat{j}
$$

$$
2(\vec{A} + \vec{B}) = 8\,\hat{i} + 12\,\hat{j}
$$

**Lado derecho:**

$$
2\vec{A} = 2\,\hat{i} + 4\,\hat{j}
$$

$$
2\vec{B} = 6\,\hat{i} + 8\,\hat{j}
$$

$$
2\vec{A} + 2\vec{B} = 8\,\hat{i} + 12\,\hat{j}
$$

✅ Ambos lados son iguales. Se cumple la propiedad distributiva.

</details>

---

## 🔑 Resumen

| Operación | Resultado |
| :--- | :--- |
| $k > 1$ | Vector más largo, mismo sentido |
| $0 < k < 1$ | Vector más corto, mismo sentido |
| $k = -1$ | Misma magnitud, sentido opuesto |
| $k < 0$ | Cambia magnitud y sentido |

| Fórmula | Descripción |
| :--- | :--- |
| $k\vec{A} = (kA_x)\,\hat{i} + (kA_y)\,\hat{j}$ | Multiplicación por componentes |
| $\vert k\vec{A}\vert = \vert k\vert \cdot \vert\vec{A}\vert$ | Magnitud del producto |

> **Recuerda:** Multiplicar un vector por un escalar cambia su **magnitud** (según $|k|$) y posiblemente su **sentido** (si $k < 0$), pero **nunca cambia su dirección**.

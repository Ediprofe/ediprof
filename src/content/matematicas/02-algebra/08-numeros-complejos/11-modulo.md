# **Módulo de un Número Complejo**

El módulo es simplemente una forma elegante de preguntar: "¿Qué tan lejos está este número del cero?". Geométricamente, es la longitud de la flecha que representa al número complejo. Como siempre formamos un triángulo rectángulo con los ejes, ¡Pitágoras viene al rescate!

---

## 🎯 ¿Qué vas a aprender?

- Qué representa el módulo ($|z|$) gráficamente.
- Qué representa el módulo ($|z|$) gráficamente.
- Cómo calcular el módulo usando el **Teorema de Pitágoras**.
- La relación entre módulo, número y conjugado.
- Propiedades clave (siempre es positivo).

---

<div style="width: 100%; box-sizing: border-box;">

![Concepto de Módulo](/images/geometria/analitica/modulo-concepto.svg)

</div>

---

## 📏 La Fórmula del Módulo

Para un número complejo $z = a + bi$, el módulo se denota $|z|$ y se calcula como:

$$
|z| = \sqrt{a^2 + b^2}
$$

> **Nota:** Tomamos $a$ y $b$ (los números reales). **No incluyas la $i$ dentro de la raíz.**

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Módulo Estándar

Calcula el módulo de:

$$
z = 3 + 4i
$$

**Razonamiento:**

1. Identificamos componentes:

$$
a = 3
$$

$$
b = 4
$$

2. Usamos Pitágoras:

$$
|z| = \sqrt{3^2 + 4^2}
$$

$$
|z| = \sqrt{9 + 16}
$$

$$
|z| = \sqrt{25}
$$

**Resultado:**

$$
\boxed{5}
$$

---

### Ejemplo 2: Módulo con Negativos

<div style="width: 100%; box-sizing: border-box;">

![Módulo con Coordenadas Negativas](/images/geometria/analitica/modulo-negativo.svg)

</div>

Calcula el módulo de:

$$
|5 - 12i|
$$

**Razonamiento:**

1. Identificamos componentes:

$$
a = 5
$$

$$
b = -12
$$

2. Al elevar al cuadrado, el negativo desaparece:

$$
(-12)^2 = 144
$$

3. Calculamos la raíz:

$$
\sqrt{5^2 + (-12)^2}
$$

$$
\sqrt{25 + 144} = \sqrt{169}
$$

**Resultado:**

$$
\boxed{13}
$$

---

### Ejemplo 3: Módulo de Imaginario Puro

<div style="width: 100%; box-sizing: border-box;">

![Módulo Imaginario Puro](/images/geometria/analitica/modulo-ejes.svg)

</div>

Calcula:

$$
|-3i|
$$

**Razonamiento:**

Es el punto $(0, -3)$. La distancia al cero es simplemente 3. Usando la fórmula:

$$
a = 0
$$

$$
b = -3
$$

$$
\sqrt{0^2 + (-3)^2} = \sqrt{9}
$$

**Resultado:**

$$
\boxed{3}
$$

---

### Ejemplo 4: Módulo con Raíces

<div style="width: 100%; box-sizing: border-box;">

![Módulo con Radicales](/images/geometria/analitica/modulo-raiz.svg)

</div>

Calcula:

$$
|1 + i|
$$

**Razonamiento:**

$$
a = 1
$$

$$
b = 1
$$

$$
\sqrt{1^2 + 1^2} = \sqrt{1 + 1}
$$

**Resultado:**

$$
\boxed{\sqrt{2}}
$$

---

## 💎 Propiedad Importante

Multiplicar un número por su conjugado nos da el módulo al cuadrado:

$$
z \cdot \bar{z} = |z|^2
$$

### Ejemplo 5: Verificación

Para $z = 3 + 4i$, ya vimos que $|z| = 5$, por lo que:

$$
|z|^2 = 25
$$

Veamos el producto con el conjugado:

$$
(3 + 4i)(3 - 4i) = 3^2 + 4^2
$$

$$
9 + 16 = 25
$$

¡Coinciden!

---

## 📝 Ejercicios de Práctica

### Ejemplo 1
Calcula:

$$
|6 + 8i|
$$

<details>
<summary>Ver solución</summary>

$$
\sqrt{6^2 + 8^2}
$$

$$
\sqrt{36 + 64} = \sqrt{100}
$$

**Resultado:**

$$
\boxed{10}
$$

</details>

---

### Ejemplo 2
Calcula:

$$
|-2 + 5i|
$$

<details>
<summary>Ver solución</summary>

$$
\sqrt{(-2)^2 + 5^2}
$$

$$
\sqrt{4 + 25} = \sqrt{29}
$$

**Resultado:**

$$
\boxed{\sqrt{29}}
$$

</details>

---

### Ejemplo 3
Calcula:

$$
|4i|
$$

<details>
<summary>Ver solución</summary>

Distancia directa es 4 unidades sobre el eje imaginario.

**Resultado:**

$$
\boxed{4}
$$

</details>

---

### Ejemplo 4
Calcula:

$$
|-7|
$$

<details>
<summary>Ver solución</summary>

Distancia directa (valor absoluto) es 7 unidades sobre el eje real.

**Resultado:**

$$
\boxed{7}
$$

</details>

---

### Ejemplo 5
Calcula:

$$
|3 - 3i|
$$

<details>
<summary>Ver solución</summary>

$$
\sqrt{3^2 + (-3)^2}
$$

$$
\sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2}
$$

**Resultado:**

$$
\boxed{3\sqrt{2}}
$$

</details>

---

### Ejemplo 6
Calcula:

$$
|1 - \sqrt{3}i|
$$

<details>
<summary>Ver solución</summary>

$$
\sqrt{1^2 + (-\sqrt{3})^2}
$$

$$
\sqrt{1 + 3} = \sqrt{4}
$$

**Resultado:**

$$
\boxed{2}
$$

</details>

---

### Ejemplo 7
Calcula el módulo de:

$$
z = \frac{3}{5} + \frac{4}{5}i
$$

<details>
<summary>Ver solución</summary>

$$
\sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2}
$$

$$
\sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}}
$$

**Resultado:**

$$
\boxed{1}
$$

</details>

---

### Ejemplo 8
Si $|z| = 3$, ¿cuánto vale $|z|^2$?

<details>
<summary>Ver solución</summary>

$$
3^2 = 9
$$

</details>

---

### Ejemplo 9
Calcula:

$$
|2i - 2|
$$

<details>
<summary>Ver solución</summary>

Ordenado es $-2 + 2i$.

$$
\sqrt{(-2)^2 + 2^2}
$$

$$
\sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}
$$

**Resultado:**

$$
\boxed{2\sqrt{2}}
$$

</details>

---

### Ejemplo 10
¿Es posible que el módulo sea negativo?

<details>
<summary>Ver solución</summary>

**No.** Es una distancia geométrica, por lo tanto siempre es:

$$
|z| \geq 0
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Significado |
|:--- |:--- |:--- |
| **Módulo** | $|z| = \sqrt{a^2+b^2}$ | Longitud del vector $z$. |
| **Propiedad** | $|z| \geq 0$ | Siempre es positivo o cero. |
| **Relación** | $|z|^2 = z \cdot \bar{z}$ | Conecta módulo y conjugado. |

> **Conclusión:** El módulo ignora los signos negativos y la $i$; solo le importa la magnitud pura de las componentes.

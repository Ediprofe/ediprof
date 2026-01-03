# **Conjugado de un Número Complejo**

El conjugado es como el "gemelo espejo" de un número complejo. Es una herramienta matemática extremadamente útil, especialmente para dividir complejos y calcular módulos. Gráficamente, es el reflejo del número sobre el eje horizontal.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el conjugado ($\bar{z}$) y cómo encontrarlo.
- La interpretación geométrica (espejo).
- Propiedades clave (suma y producto).
- Por qué $(a+bi)(a-bi)$ siempre es real.

---

<div style="width: 100%; box-sizing: border-box;">

![Simetría del Conjugado](/images/geometria/analitica/conjugado-simetria.svg)

</div>

---

## 🔄 Definición de Conjugado

Para obtener el conjugado de un número complejo, simplemente **cambiamos el signo de la parte imaginaria**.

Si $z = a + bi$, entonces su conjugado $\bar{z}$ es:

$$
\bar{z} = a - bi
$$

> **Nota:** La parte real se queda igual. Solo cambia el signo de la $i$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Conjugado Estándar

Halla el conjugado de:

$$
z = 3 + 4i
$$

**Razonamiento:**
Cambiamos el signo de la parte imaginaria ($+4i$ por $-4i$).

**Resultado:**

$$
\bar{z} = 3 - 4i
$$

---

### Ejemplo 2: Conjugado con Negativos

<div style="width: 100%; box-sizing: border-box;">

![Conjugado en otros Cuadrantes](/images/geometria/analitica/conjugado-cuadrante.svg)

</div>

Halla $\bar{z}$ si:

$$
z = -4 + 3i
$$

**Razonamiento:**
Cambiamos $+3i$ por $-3i$. La parte real ($-4$) no se toca.

**Resultado:**

$$
\bar{z} = -4 - 3i
$$

---

### Ejemplo 3: Conjugado de parte Real Negativa

Halla $\bar{z}$ si:

$$
z = -1 + 7i
$$

**Razonamiento:**
Solo miramos la parte imaginaria ($+7i$). Cambia a $-7i$. El $-1$ se queda igual.

**Resultado:**

$$
\bar{z} = -1 - 7i
$$

---

### Ejemplo 4: Conjugado de Real Puro

<div style="width: 100%; box-sizing: border-box;">

![Conjugado de un Real Puro](/images/geometria/analitica/conjugado-real.svg)

</div>

Halla $\bar{z}$ si:

$$
z = 5
$$

**Razonamiento:**
Como no tiene parte imaginaria ($0i$), el signo no afecta nada. El reflejo de un punto sobre el eje real es el mismo punto.

**Resultado:**

$$
\bar{z} = 5
$$

---

### Ejemplo 5: Conjugado de Imaginario Puro

<div style="width: 100%; box-sizing: border-box;">

![Conjugado de un Imaginario Puro](/images/geometria/analitica/conjugado-imaginario.svg)

</div>

Halla $\bar{z}$ si:

$$
z = 4i
$$

**Razonamiento:**
Cambiamos $+4i$ por $-4i$.

**Resultado:**

$$
\bar{z} = -4i
$$

---

## 💎 Propiedades Mágicas

### 1. El Producto es Real
Al multiplicar un número por su conjugado, los términos imaginarios se cancelan y obtenemos una suma de cuadrados.

$$
z \cdot \bar{z} = (a+bi)(a-bi) = a^2 + b^2
$$

### 2. La Suma es Real
Al sumar un número con su conjugado, la parte imaginaria se anula.

$$
z + \bar{z} = (a+bi) + (a-bi) = 2a
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla $\bar{z}$ para:

$$
z = 5 + 2i
$$

<details>
<summary>Ver solución</summary>

$$
\bar{z} = 5 - 2i
$$

</details>

---

### Ejercicio 2
Halla $\bar{z}$ para:

$$
z = 4 - 6i
$$

<details>
<summary>Ver solución</summary>

$$
\bar{z} = 4 + 6i
$$

</details>

---

### Ejercicio 3
Halla el conjugado de:

$$
z = -7 - i
$$

<details>
<summary>Ver solución</summary>

$$
\bar{z} = -7 + i
$$

</details>

---

### Ejercicio 4
Halla el conjugado de:

$$
z = 10i
$$

<details>
<summary>Ver solución</summary>

$$
\bar{z} = -10i
$$

</details>

---

### Ejercicio 5
Calcula $z + \bar{z}$ si:

$$
z = 3 + 2i
$$

<details>
<summary>Ver solución</summary>

$$
(3+2i) + (3-2i) = 6
$$

</details>

---

### Ejercicio 6
Calcula $z - \bar{z}$ si:

$$
z = 4 + 5i
$$

<details>
<summary>Ver solución</summary>

$$
(4+5i) - (4-5i) = 10i
$$

</details>

---

### Ejercicio 7
Calcula $z \cdot \bar{z}$ si:

$$
z = 1 + 2i
$$

<details>
<summary>Ver solución</summary>

$$
1^2 + 2^2 = 5
$$

</details>

---

### Ejercicio 8
¿Cuál es el conjugado de $\pi$?

<details>
<summary>Ver solución</summary>

$$
\pi
$$

(Es un número real).

</details>

---

### Ejercicio 9
Si $\bar{z} = 2 + 3i$, ¿cuál era $z$?

<details>
<summary>Ver solución</summary>

$$
z = 2 - 3i
$$

</details>

---

### Ejercicio 10
Verifica que $\overline{(\bar{z})} = z$.

<details>
<summary>Ver solución</summary>

Al conjugar dos veces, cambiamos el signo dos veces, volviendo al estado original.

$$
a + bi \xrightarrow{\text{conj}} a - bi \xrightarrow{\text{conj}} a + bi
$$

</details>

---

## 🔑 Resumen

| Número ($z$) | Conjugado ($\bar{z}$) | Patrón |
|:--- |:--- |:--- |
| $a + bi$ | $a - bi$ | Cambia signo Im |
| $a - bi$ | $a + bi$ | Cambia signo Im |
| $a$ (Real) | $a$ | Igual |
| $bi$ (Imag) | $-bi$ | Opuesto |

> **Conclusión:** El conjugado es la herramienta clave para eliminar raíces imaginarias de denominadores (división) y para calcular distancias (módulos).

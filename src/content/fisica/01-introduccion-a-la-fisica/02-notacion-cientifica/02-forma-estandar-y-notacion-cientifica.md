# Forma estándar y notación científica

> **🎯 ¿Qué vas a aprender?**
>
> - A convertir números de forma estándar a notación científica.
> - A expresar cantidades muy grandes o muy pequeñas de manera simplificada.
> - A realizar la conversión inversa: de notación científica a su forma decimal original.

## 🧮 Conversión entre forma estándar y notación científica

En esta sección aprenderás a **convertir un número común (forma estándar)** en **notación científica**, y también cómo **volver** de la notación científica a la **forma decimal original**.

---

### 🔹 1. De forma estándar a notación científica

Para convertir un número común en notación científica:

1. Coloca el punto decimal de modo que quede **una sola cifra distinta de cero antes del punto**.
2. Cuenta **cuántos lugares se movió el punto**:
   - Si se movió **a la izquierda**, el exponente de 10 es **positivo**.
   - Si se movió **a la derecha**, el exponente de 10 es **negativo**.
3. Escribe el número en la forma:

$$
a \times 10^n
$$

---

#### ✏️ Ejemplo 1: número grande

Convierte $4\,500\,000$ a notación científica.

**Solución paso a paso:**

1. Mueve el punto decimal después del primer dígito no nulo: $4.5$
2. Contamos los lugares movidos: **6 lugares a la izquierda**.
3. El exponente será positivo: $n = +6$.

$$
4\,500\,000 = 4.5 \times 10^6
$$

---

#### ✏️ Ejemplo 2: número pequeño

Convierte $0.00037$ a notación científica.

**Solución paso a paso:**

1. Mueve el punto decimal hasta después del primer dígito no nulo: $3.7$
2. Se movió **4 lugares a la derecha**, por lo tanto el exponente será negativo: $n = -4$.

$$
0.00037 = 3.7 \times 10^{-4}
$$

---

### 🔹 2. De notación científica a forma estándar

Para convertir un número expresado como $a \times 10^n$ a su forma decimal:

1. Si el exponente $n$ es **positivo**, mueve el punto decimal **a la derecha** $n$ lugares.
2. Si el exponente $n$ es **negativo**, mueve el punto decimal **a la izquierda** $n$ lugares.
3. Completa con ceros si es necesario.

---

#### ✏️ Ejemplo 3: exponente positivo

Convierte $3.25 \times 10^4$ a forma estándar.

**Solución paso a paso:**

1. El exponente $n=4$ indica que se mueve el punto **4 lugares a la derecha**.
2. Desplazamos el punto: $3.25 \to 32\,500$

$$
3.25 \times 10^4 = 32\,500
$$

---

#### ✏️ Ejemplo 4: exponente negativo

Convierte $6.5 \times 10^{-3}$ a forma estándar.

**Solución paso a paso:**

1. El exponente $n=-3$ indica que se mueve el punto **3 lugares a la izquierda**.
2. Colocamos el punto: $6.5 \to 0.0065$

$$
6.5 \times 10^{-3} = 0.0065
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Expresa los siguientes números en notación científica:**

a) $72\,000\,000$

b) $0.000045$

c) $930\,000\,000\,000$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

a) 

$$
7.2 \times 10^7
$$

b) 

$$
4.5 \times 10^{-5}
$$

c) 

$$
9.3 \times 10^{11}
$$

</details>

---

### Ejercicio 2
**Convierte los siguientes números de notación científica a forma estándar:**

a) $5.1 \times 10^5$

b) $2.8 \times 10^{-6}$

c) $9.07 \times 10^3$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

a) 

$$
510\,000
$$

b) 

$$
0.0000028
$$

c) 

$$
9\,070
$$

</details>

---

### Ejercicio 3
**La distancia de la Tierra a Marte es aproximadamente 225 000 000 km. Exprésala en notación científica.**

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
225\,000\,000\,\mathrm{km} = 2.25 \times 10^8\,\mathrm{km}
$$

Se movió el punto 8 lugares a la izquierda, por lo tanto $n = 8$.

</details>

---

### Ejercicio 4
**El diámetro de un átomo de hidrógeno es aproximadamente $1.2 \times 10^{-10}$ m. Expresa este valor en forma estándar.**

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
1.2 \times 10^{-10}\,\mathrm{m} = 0.00000000012\,\mathrm{m}
$$

El exponente $-10$ indica que el punto se mueve 10 lugares a la izquierda.

</details>

---

## 🔑 Resumen

La notación científica permite expresar cualquier número como el producto de un número base entre **1 y 9** multiplicado por una potencia de 10.

| Conversión | Movimiento del punto decimal | Ejemplo |
| :--- | :--- | :--- |
| **Grande → Notación** | A la izquierda ($n$ es $+$) | $4\,500\,000 = 4.5 \times 10^6$ |
| **Pequeño → Notación** | A la derecha ($n$ es $-$) | $0.00037 = 3.7 \times 10^{-4}$ |
| **Notación → Estándar** | $n$ positivo: a la derecha | $3.25 \times 10^4 = 32\,500$ |
| **Notación → Estándar** | $n$ negativo: a la izquierda | $6.5 \times 10^{-3} = 0.0065$ |

> **Recuerda:** Un exponente positivo indica un número grande (como miles o millones), mientras que un exponente negativo indica un número pequeño (decimales menores a 1).

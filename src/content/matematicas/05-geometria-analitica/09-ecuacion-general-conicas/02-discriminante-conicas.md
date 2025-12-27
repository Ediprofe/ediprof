# **El Discriminante de las Cónicas**

Cuando la ecuación tiene ese molesto término $Bxy$, la cónica está inclinada y la regla simple de los signos $(A, C)$ ya no funciona. Necesitamos una herramienta más potente: **El Discriminante** ($\Delta$). Es la prueba de ADN definitiva para cualquier cónica.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula sagrada: $B^2 - 4AC$.
- Cómo clasificar CUALQUIER cónica, esté rotada o no.
- Aplicar la fórmula en 5 casos diferentes.

---

## 🔍 Concepto 1: El Cálculo del Discriminante

El indicador $\Delta$ (Delta) se calcula usando solo los coeficientes cuadráticos de la ecuación general $Ax^2 + Bxy + Cy^2 + \dots = 0$.

$$ \Delta = B^2 - 4AC $$

*   *Nota: Se parece al de la fórmula cuadrática, pero aquí define la **forma** de la curva.*

Practiquemos el cálculo en **5 ejemplos**:

### Ejemplo 1.1
$$ x^2 + 2xy + y^2 - 4 = 0 $$
*   $A=1, B=2, C=1$.
*   $\Delta = (2)^2 - 4(1)(1) = 4 - 4 = 0$.

### Ejemplo 1.2
$$ 2x^2 - 3xy + 2y^2 - 5x = 0 $$
*   $A=2, B=-3, C=2$.
*   $\Delta = (-3)^2 - 4(2)(2) = 9 - 16 = -7$.

### Ejemplo 1.3
$$ xy - 16 = 0 $$
*   $A=0, C=0$. (No hay cuadrados puros).
*   $B=1$.
*   $\Delta = (1)^2 - 4(0)(0) = 1 - 0 = 1$.

### Ejemplo 1.4
$$ 3x^2 + 4y^2 - 12 = 0 $$
*   $A=3, B=0, C=4$.
*   $\Delta = 0^2 - 4(3)(4) = -48$.

### Ejemplo 1.5
$$ x^2 - xy - 6y^2 = 0 $$
*   $A=1, B=-1, C=-6$.
*   $\Delta = (-1)^2 - 4(1)(-6) = 1 + 24 = 25$.

---

## 🔍 Concepto 2: La Tabla de Clasificación

El signo de $\Delta$ nos dice qué curva es.

| Valor de $\Delta$ | Cónica | Mnemotecnia |
| :--- | :--- | :--- |
| **Negativo ($<0$)** | **Elipse** (o Círculo) | "Elipse" es cerrado, negativo es "menos". |
| **Cero ($=0$)** | **Parábola** | "Par" es igual, cero es neutro. |
| **Positivo ($>0$)** | **Hipérbola** | "Híper" es más, positivo es "más". |

Veamos **5 ejemplos de clasificación**:

### Ejemplo 2.1: Elipse Rotada
Ecuación: $2x^2 - xy + 2y^2 - 2 = 0$.
1.  Calculamos: $\Delta = (-1)^2 - 4(2)(2) = 1 - 16 = -15$.
2.  Como $-15 < 0$, es una **Elipse**.

### Ejemplo 2.2: Parábola Rotada
Ecuación: $x^2 + 2xy + y^2 + x - y = 0$.
1.  Calculamos: $\Delta = (2)^2 - 4(1)(1) = 4 - 4 = 0$.
2.  Como $\Delta = 0$, es una **Parábola**.

### Ejemplo 2.3: Hipérbola Estándar
Ecuación: $4x^2 - 9y^2 - 36 = 0$.
1.  Datos: $A=4, B=0, C=-9$.
2.  Calculamos: $\Delta = 0^2 - 4(4)(-9) = 0 + 144 = +144$.
3.  Positivo $\to$ **Hipérbola**.

### Ejemplo 2.4: Hipérbola Rectangular
Ecuación: $2xy + 5 = 0$.
1.  Datos: $A=0, B=2, C=0$.
2.  Calculamos: $\Delta = 2^2 - 0 = 4$.
3.  Positivo $\to$ **Hipérbola**.

### Ejemplo 2.5: Círculo
Ecuación: $x^2 + y^2 - 25 = 0$.
1.  Datos: $A=1, B=0, C=1$.
2.  Calculamos: $\Delta = 0^2 - 4(1)(1) = -4$.
3.  Negativo $\to$ Elipse.
    *   *Caso especial:* Como $A=C$ y $B=0$, es específicamente una **Circunferencia**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Discriminante de $x^2 + y^2 = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\Delta = 0 - 4(1)(1) = -4$.

**Respuesta:** $\boxed{-4}$
</details>

---

### Ejercicio 2
Clasifica $x^2 - 4xy + 4y^2 + x = 0$.

<details>
<summary>Ver solución</summary>
**Razonamiento:**
$\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0$. Parábola.

**Respuesta:** **Parábola**
</details>

---

### Ejercicio 3
Clasifica $3x^2 + 2xy - y^2 = 0$.

<details>
<summary>Ver solución</summary>
**Razonamiento:**
$\Delta = 2^2 - 4(3)(-1) = 4 + 12 = 16 > 0$. Hipérbola.

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 4
Si $B^2 = 4AC$, ¿qué cónica es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Entonces $B^2 - 4AC = 0$. Parábola.

**Respuesta:** **Parábola**
</details>

---

### Ejercicio 5
Calcula $\Delta$ para $5x^2 + 2y^2 = 10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\Delta = 0 - 4(5)(2) = -40$.

**Respuesta:** $\boxed{-40}$
</details>

---

### Ejercicio 6
Clasifica $x^2 + xy + y^2 - 3 = 0$.

<details>
<summary>Ver solución</summary>
**Razonamiento:**
$\Delta = 1^2 - 4(1)(1) = -3$. Elipse.

**Respuesta:** **Elipse**
</details>

---

### Ejercicio 7
¿Puede un discriminante positivo ser una elipse?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, positivo siempre es Hipérbola.

**Respuesta:** **No**
</details>

---

### Ejercicio 8
Discriminante de $y = x^2$ (Parábola vertical).

<details>
<summary>Ver solución</summary>
$x^2 - y = 0$. $A=1, B=0, C=0$. $\Delta = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 9
Si $\Delta = -100$, ¿qué es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Negativo $\to$ Elipse.

**Respuesta:** **Elipse**
</details>

---

### Ejercicio 10
Discriminante de $xy = -1$.

<details>
<summary>Ver solución</summary>
$A=0, B=1, C=0$. $\Delta = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

## 🔑 Resumen

| Conclusión | Signo $\Delta$ |
| :--- | :--- |
| **Elipse** | Menos $(-)$ |
| **Parábola** | Cero $(0)$ |
| **Hipérbola** | Más $(+)$ |

> **Conclusión:** El discriminante no miente. Incluso si la cónica está girada y deformada, este número revela su verdadera identidad geométrica.

---
title: "Forma General de las Cónicas"
---

# **Forma General de las Cónicas**

Hasta ahora hemos visto ecuaciones "bonitas" y ordenadas como $(x-h)^2 + (y-k)^2 = r^2$. Pero en el mundo real, las ecuaciones vienen "desordenadas" y expandidas. Esta es la llamada **Ecuación General de Segundo Grado**.

---

## 🎯 ¿Qué vas a aprender?

- La estructura de la ecuación general: $Ax^2 + Bxy + Cy^2 + \dots = 0$.
- Cómo identificar los coeficientes $A, B, C, D, E, F$.
- Cómo clasificar la cónica rápidamente mirando solo a $A$ y $C$ (cuando $B=0$).

---

## 🧱 La Ecuación General Completa

Cualquier curva cónica (Círculo, Elipse, Parábola, Hipérbola) puede escribirse de esta forma:

$$ Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 $$

*   **$A, C$:** Coeficientes de los términos cuadráticos ($x^2, y^2$).
*   **$B$:** Coeficiente del término rectangular ($xy$). *Si existe, la cónica está rotada/inclinada.*
*   **$D, E$:** Coeficientes lineales ($x, y$). Mueven el centro.
*   **$F$:** Término independiente.

---

## 🔍 Concepto 1: Identificando Coeficientes

Para clasificar, primero debes saber quién es quién. Mira estos **5 ejemplos**:

### Ejemplo 1.1
$$ 4x^2 + 9y^2 - 36 = 0 $$
*   $A = 4$ (acompaña a $x^2$).
*   $C = 9$ (acompaña a $y^2$).
*   $B = 0$ (no hay $xy$).
*   $F = -36$.

### Ejemplo 2.2
$$ x^2 - 4x + 6y - 12 = 0 $$
*   $A = 1$.
*   $C = 0$ (no hay $y^2$).
*   $D = -4, E = 6, F = -12$.

### Ejemplo 3.3
$$ 2xy + 3 = 0 $$
*   $A = 0, C = 0$.
*   $B = 2$ (hay término $xy$).
*   $F = 3$.

### Ejemplo 4.4
$$ x^2 + y^2 + 2x + 2y + 1 = 0 $$
*   $A = 1, C = 1$.
*   $B = 0$.

### Ejemplo 5.5
$$ -3x^2 + 5y^2 = 10 $$
Primero igualamos a cero: $-3x^2 + 5y^2 - 10 = 0$.
*   $A = -3$.
*   $C = 5$.
*   $F = -10$.

---

## 🔍 Concepto 2: Clasificación Rápida (Sin Rotación)

Si **$B = 0$** (la cónica no está inclinada), podemos saber qué es solo mirando los signos y valores de **$A$** y **$C$**.

| Condición ($A$ y $C$) | Cónica |
| :--- | :--- |
| **$A = C$** | Circunferencia |
| **$A \cdot C > 0$** (Mismo signo, distintos) | Elipse |
| **$A \cdot C < 0$** (Signos opuestos) | Hipérbola |
| **$A \cdot C = 0$** (Uno es cero) | Parábola |

Analicemos **5 casos prácticos**:

### Ejemplo 2.1
$$ 3x^2 + 3y^2 - 12x = 0 $$
*   $A = 3, C = 3$.
*   Como $A = C$, es una **Circunferencia**.

### Ejemplo 2.2
$$ 5x^2 - 4y^2 + 20 = 0 $$
*   $A = 5, C = -4$.
*   Signos opuestos ($+,-$). Es una **Hipérbola**.

### Ejemplo 2.3
$$ 2x^2 + y = 0 $$
*   $A = 2, C = 0$.
*   Uno es cero. Es una **Parábola**.

### Ejemplo 2.4
$$ 9x^2 + 4y^2 = 36 $$
*   IGuala a cero: $9x^2 + 4y^2 - 36 = 0$.
*   $A = 9, C = 4$.
*   Mismo signo ($+$), pero distintos. Es una **Elipse**.

### Ejemplo 2.5
$$ -2x^2 - 5y^2 + 10 = 0 $$
*   $A = -2, C = -5$.
*   Mismo signo (ambos negativos), distintos valores. Es una **Elipse**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Coeficientes de $x^2 - 2xy + y^2 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A=1, B=-2, C=1$.

**Respuesta:** $\boxed{A=1, B=-2, C=1}$
</details>

---

### Ejercicio 2
Clasifica $x^2 + y^2 - 4 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A=1, C=1$. Iguales.

**Respuesta:** **Circunferencia**
</details>

---

### Ejercicio 3
Clasifica $x^2 - y^2 = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
A=1, C=-1. Signos opuestos.

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 4
Clasifica $y^2 = 8x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
A=0, C=1. Falta una cuadrada.

**Respuesta:** **Parábola**
</details>

---

### Ejercicio 5
Coeficiente B en $3x^2 + 5y^2 = 10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No hay término mezclado xy.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 6
Clasifica $2x^2 + 4y^2 = 0$ (geométricamente).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Suma de positivos igual a cero. Solo un punto (Elipse degenerada).

**Respuesta:** **Punto (0,0)**
</details>

---

### Ejercicio 7
Clasifica $-3x^2 + 3y^2 - 6 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
A=-3, C=3. Signos opuestos.

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 8
¿Qué es $xy = 1$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tiene B diferente de cero. Hipérbola Rotada.

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 9
Si A y C son negativos iguales, ¿qué es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ej: $-x^2 - y^2 + 4 = 0 \Rightarrow x^2 + y^2 = 4$. Círculo.

**Respuesta:** **Circunferencia**
</details>

---

### Ejercicio 10
Valor de F en $x^2 = 4y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 - 4y = 0$. No hay constante sola.

**Respuesta:** $\boxed{0}$
</details>

---

## 🔑 Resumen

| Tipo | Condición Clave ($B=0$) |
| :--- | :--- |
| **Circunferencia** | $A = C$ |
| **Elipse** | $A, C$ igual signo |
| **Hipérbola** | $A, C$ distinto signo |
| **Parábola** | $A=0$ o $C=0$ |

> **Conclusión:** Si la ecuación no tiene $xy$, la clasificación es cuestión de segundos. Solo mira a los "gigantes" ($x^2$ y $y^2$).

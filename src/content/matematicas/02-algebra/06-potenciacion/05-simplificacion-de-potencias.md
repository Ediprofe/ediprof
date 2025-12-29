# **Simplificación de Potencias**

## 🎯 ¿Qué vas a aprender?

- Una estrategia de 4 pasos para atacar cualquier problema.
- A combinar múltiples propiedades sin confundirte.
- Cómo manejar signos, coeficientes y variables al mismo tiempo.
- A dejar siempre la respuesta "limpia" (sin exponentes negativos).

---

## 🔍 Resumen de propiedades

Ten esta tabla a mano.

| Nombre | Regla |
| :--- | :--- |
| **Producto** | $a^m \cdot a^n = a^{m+n}$ |
| **Cociente** | $\frac{a^m}{a^n} = a^{m-n}$ |
| **Potencia de Potencia** | $(a^m)^n = a^{m \cdot n}$ |
| **Potencia de Producto** | $(ab)^n = a^n b^n$ |
| **Exponente Negativo** | $a^{-n} = \frac{1}{a^n}$ |
| **Exponente Cero** | $a^0 = 1$ |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Combo Básico

Simplifica $(2x^3y^2)^3 \cdot (3x^2y)^2$.

**Datos:**
- Dos paréntesis elevados a potencias.

**Razonamiento:**

1. **Quitar paréntesis (Distribuir):**

Para el primero:

$$
(2x^3y^2)^3 = 2^3 \cdot (x^3)^3 \cdot (y^2)^3
$$

$$
= 8x^9y^6
$$

Para el segundo:

$$
(3x^2y)^2 = 3^2 \cdot (x^2)^2 \cdot y^2
$$

$$
= 9x^4y^2
$$

2. **Juntar (Multiplicar):**

Números:

$$
8 \cdot 9 = 72
$$

Variable x:

$$
x^9 \cdot x^4 = x^{13}
$$

Variable y:

$$
y^6 \cdot y^2 = y^8
$$

3. **Resultado:**

$$
72x^{13}y^8
$$

**Resultado:** $\boxed{72x^{13}y^8}$

---

### Ejemplo 2: División y Resta

Simplifica $\dfrac{15a^5b^{-2}}{3a^2b^3}$.

**Datos:**
- Coeficientes 15 y 3.
- Variables $a$ y $b$ (con negativos).

**Razonamiento:**

1. **Números:**

$$
\frac{15}{3} = 5
$$

2. **Variables (Resta):**

Para $a$:

$$
5 - 2 = 3 \to a^3
$$

Para $b$:

$$
-2 - 3 = -5 \to b^{-5}
$$

3. **Limpiar negativos:**

$$
5a^3b^{-5} = \frac{5a^3}{b^5}
$$

**Resultado:** $\boxed{\frac{5a^3}{b^5}}$

---

### Ejemplo 3: La "Torre" de Fracciones

Simplifica $\left( \dfrac{2x^3}{y^2} \right)^4 \cdot \left( \dfrac{y}{x^2} \right)^3$.

**Datos:**
- Dos fracciones elevadas a potencias.

**Razonamiento:**

1. **Distribuir exponentes:**

Primera fracción:

$$
\frac{2^4 x^{12}}{y^8} = \frac{16x^{12}}{y^8}
$$

Segunda fracción:

$$
\frac{y^3}{x^6}
$$

2. **Multiplicar fracciones (lineal):**

$$
\frac{16x^{12}y^3}{y^8x^6}
$$

3. **Simplificar (Resta):**

Para $x$:

$$
12 - 6 = 6 \text{ (arriba)}
$$

Para $y$:

$$
3 - 8 = -5 \text{ (o sea, 5 abajo)}
$$

4. **Respuesta:**

$$
\frac{16x^6}{y^5}
$$

**Resultado:** $\boxed{\frac{16x^6}{y^5}}$

---

### Ejemplo 4: Exponente Negativo Externo

Simplifica $\left( \dfrac{3a^{-2}}{b^3} \right)^{-2}$.

**Datos:**
- Exponente de afuera es -2.

**Razonamiento:**

1. **Truco del Volantín:** Invertimos la fracción y hacemos positivo el exponente de afuera.

$$
\left( \frac{b^3}{3a^{-2}} \right)^2
$$

2. **Distribuir el 2:**

$$
\frac{b^6}{3^2 a^{-4}} = \frac{b^6}{9a^{-4}}
$$

3. **Subir el negativo:** El $a^{-4}$ de abajo sube como $a^4$.

$$
\frac{b^6a^4}{9}
$$

**Resultado:** $\boxed{\frac{a^4b^6}{9}}$

---

### Ejemplo 5: Todo contra todos

Simplifica $\dfrac{(x^2y)^3 \cdot (x^{-1}y^2)^{-2}}{x^4y^{-1}}$.

**Datos:**
- Numerador complejo, denominador simple.

**Razonamiento:**

1. **Numerador - Primera parte:**

$$
(x^2y)^3 = x^6y^3
$$

2. **Numerador - Segunda parte:**

$$
(x^{-1}y^2)^{-2} = x^{(-1)(-2)}y^{(2)(-2)} = x^2y^{-4}
$$

3. **Multiplicamos todo el numerador:**

$$
x^6y^3 \cdot x^2y^{-4} = x^8y^{-1}
$$

4. **División:**

$$
\frac{x^8y^{-1}}{x^4y^{-1}}
$$

5. **Simplificar:**

Para $x$:

$$
8 - 4 = 4
$$

Para $y$:

$$
-1 - (-1) = -1 + 1 = 0
$$

(Los $y$ se cancelan)

**Resultado:** $\boxed{x^4}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $(2x^2)^3 \cdot x^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
8x^6 \cdot x^4 = 8x^{10}
$$

**Resultado:** $\boxed{8x^{10}}$

</details>

### Ejercicio 2
Simplifica $\dfrac{x^5y^2}{x^3y^5}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
x^{5-3} y^{2-5} = x^2 y^{-3}
$$

$$
= \frac{x^2}{y^3}
$$

**Resultado:** $\boxed{\frac{x^2}{y^3}}$

</details>

### Ejercicio 3
Simplifica $(3a^{-1})^2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
3^2 a^{-2} = 9a^{-2}
$$

$$
= \frac{9}{a^2}
$$

**Resultado:** $\boxed{\frac{9}{a^2}}$

</details>

### Ejercicio 4
Simplifica $\left( \dfrac{x}{2} \right)^{-3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\left(\frac{2}{x}\right)^3 = \frac{8}{x^3}
$$

**Resultado:** $\boxed{\frac{8}{x^3}}$

</details>

### Ejercicio 5
Simplifica $\dfrac{(ab)^3}{a^2b}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{a^3b^3}{a^2b} = a^{3-2}b^{3-1} = ab^2
$$

**Resultado:** $\boxed{ab^2}$

</details>

### Ejercicio 6
Simplifica $(x^0 y^2)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
x^0 = 1
$$

$$
(1 \cdot y^2)^3 = (y^2)^3 = y^6
$$

**Resultado:** $\boxed{y^6}$

</details>

### Ejercicio 7
Simplifica $\dfrac{10x^5}{2x^{-2}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{10}{2} x^{5-(-2)} = 5x^7
$$

**Resultado:** $\boxed{5x^7}$

</details>

### Ejercicio 8
Simplifica $\left( \dfrac{a^2}{b^3} \right)^2 \cdot \left( \dfrac{b}{a} \right)^3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{a^4}{b^6} \cdot \frac{b^3}{a^3}
$$

$$
= \frac{a^4b^3}{a^3b^6}
$$

$$
= \frac{a}{b^3}
$$

**Resultado:** $\boxed{\frac{a}{b^3}}$

</details>

### Ejercicio 9
Simplifica $\dfrac{x^{-2} \cdot x^5}{x^3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Numerador:

$$
x^{-2 + 5} = x^3
$$

División:

$$
\frac{x^3}{x^3} = 1
$$

**Resultado:** $\boxed{1}$

</details>

### Ejercicio 10
Simplifica $(2x)^2 + (3x)^2$ (¡Cuidado, es suma!).

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
4x^2 + 9x^2
$$

Son términos semejantes.

$$
= 13x^2
$$

**Resultado:** $\boxed{13x^2}$

</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1.** | **Paréntesis fuera:** Aplica potencia de potencia. |
| **2.** | **Agrupar:** Multiplica lo de arriba con lo de arriba. |
| **3.** | **Dividir:** Resta los exponentes de abajo. |
| **4.** | **Limpiar:** Manda los exponentes negativos al otro piso. |

> Al final, una expresión simplificada no debe tener paréntesis, ni bases repetidas, ni exponentes negativos.

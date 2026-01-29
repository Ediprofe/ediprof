# **Cubo de un Binomio**


## 🎯 ¿Qué vas a aprender?

- A entender el significado de elevar un binomio a la potencia 3.
- La regla de los "triples productos" para el cubo de una suma.
- El patrón de signos alternados para el cubo de una resta.
- A aplicar la fórmula paso a paso sin perderse en los cálculos.

---

## 🧊 El Cubo de una Suma

Cuando multiplicamos $(a + b)$ por sí mismo tres veces, obtenemos una expresión de cuatro términos. El patrón es muy ordenado: el exponente de la primera letra va bajando ($3, 2, 1, 0$) mientras que el de la segunda letra va subiendo.

### **Ejemplo: Paso a paso con números**

Calcula: $(x + 2)^3$

**Razonamiento:**
1.  **Cubo del primero:** $x^3$.
2.  **Triple del primero al cuadrado por el segundo:** $3 \cdot (x^2) \cdot (2) = 6x^2$.
3.  **Triple del primero por el segundo al cuadrado:** $3 \cdot (x) \cdot (2^2) = 3 \cdot x \cdot 4 = 12x$.
4.  **Cubo del segundo:** $2^3 = 8$.

**Resultado:** $\boxed{x^3 + 6x^2 + 12x + 8}$

### **La Regla General (Suma)**

$$
\boxed{(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3}
$$

---

## 📉 El Cubo de una Resta

Para la resta, la fórmula es idéntica en valores, pero los signos se alternan empezando por el primero positivo: $(+), (-), (+), (-)$.

### **Ejemplo: El caso negativo**

Calcula: $(m - 1)^3$

**Razonamiento:**
1.  Primero al cubo: $m^3$.
2.  Triple del 1ero cuadrado por el 2do: $3 \cdot m^2 \cdot 1 = 3m^2$ (negativo).
3.  Triple del 1ero por el 2do cuadrado: $3 \cdot m \cdot 1^2 = 3m$ (positivo).
4.  Segundo al cubo: $1^3 = 1$ (negativo).

**Resultado:** $\boxed{m^3 - 3m^2 + 3m - 1}$

### **La Regla General (Resta)**

$$
\boxed{(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Con coeficientes mayores

Desarrolla: $(2x + 3)^3$

**Datos:**
- $a = 2x$
- $b = 3$

**Razonamiento:**
1. $(2x)^3 = 8x^3$
2. $3 \cdot (2x)^2 \cdot 3 = 3 \cdot 4x^2 \cdot 3 = 36x^2$
3. $3 \cdot (2x) \cdot 3^2 = 3 \cdot 2x \cdot 9 = 54x$
4. $3^3 = 27$

**Resultado:** $\boxed{8x^3 + 36x^2 + 54x + 27}$

---

### Ejemplo 2: Variables combinadas

Calcula: $(a - 2b)^3$

**Datos:**
- $a = a$
- $b = 2b$

**Razonamiento:**
1. $a^3 = a^3$
2. $3 \cdot a^2 \cdot (2b) = 6a^2b$ (negativo)
3. $3 \cdot a \cdot (2b)^2 = 3 \cdot a \cdot 4b^2 = 12ab^2$ (positivo)
4. $(2b)^3 = 8b^3$ (negativo)

**Resultado:** $\boxed{a^3 - 6a^2b + 12ab^2 - 8b^3}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve: $(x + 1)^3$

<details>
<summary>Ver solución</summary>

**Datos:** $a = x, b = 1$.
**Razonamiento:** $x^3 + 3(x^2)(1) + 3(x)(1^2) + 1^3$.
**Resultado:** $\boxed{x^3 + 3x^2 + 3x + 1}$

</details>


### Ejercicio 2
Desarrolla: $(a - 2)^3$

<details>
<summary>Ver solución</summary>

**Datos:** Cubo de una resta.
**Razonamiento:** $a^3 - 3(a^2)(2) + 3(a)(2^2) - 2^3 = a^3 - 6a^2 + 12a - 8$.
**Resultado:** $\boxed{a^3 - 6a^2 + 12a - 8}$

</details>


### Ejercicio 3
Calcula: $(2y + 1)^3$

<details>
<summary>Ver solución</summary>

**Datos:** Primer término con coeficiente $2$.
**Razonamiento:** $(2y)^3 + 3(2y)^2(1) + 3(2y)(1^2) + 1^3 = 8y^3 + 12y^2 + 6y + 1$.
**Resultado:** $\boxed{8y^3 + 12y^2 + 6y + 1}$

</details>


### Ejercicio 4
Resuelve: $(x - 5)^3$

<details>
<summary>Ver solución</summary>

**Datos:** Los signos se alternan $+,-,+,-$.
**Razonamiento:** $x^3 - 3(x^2)(5) + 3(x)(5^2) - 5^3 = x^3 - 15x^2 + 75x - 125$.
**Resultado:** $\boxed{x^3 - 15x^2 + 75x - 125}$

</details>


### Ejercicio 5
Desarrolla: $(3x + 2)^3$

<details>
<summary>Ver solución</summary>

**Datos:** Coeficiente $3$ y número $2$.
**Razonamiento:** $(3x)^3 + 3(3x)^2(2) + 3(3x)(2^2) + 2^3 = 27x^3 + 54x^2 + 36x + 8$.
**Resultado:** $\boxed{27x^3 + 54x^2 + 36x + 8}$

</details>


### Ejercicio 6
Calcula: $(4a - 1)^3$

<details>
<summary>Ver solución</summary>

**Datos:** $a = 4a, b = 1$.
**Razonamiento:** $(4a)^3 - 3(4a)^2(1) + 3(4a)(1^2) - 1^3 = 64a^3 - 48a^2 + 12a - 1$.
**Resultado:** $\boxed{64a^3 - 48a^2 + 12a - 1}$

</details>


### Ejercicio 7
Resuelve: $(x^2 + 2)^3$

<details>
<summary>Ver solución</summary>

**Datos:** El primer término tiene exponente.
**Razonamiento:** $(x^2)^3 + 3(x^2)^2(2) + 3(x^2)(2^2) + 2^3 = x^6 + 6x^4 + 12x^2 + 8$.
**Resultado:** $\boxed{x^6 + 6x^4 + 12x^2 + 8}$

</details>


### Ejercicio 8
Desarrolla: $(x + \frac{1}{2})^3$

<details>
<summary>Ver solución</summary>

**Datos:** Fracción como segundo término.
**Razonamiento:** $x^3 + 3(x^2)(\frac{1}{2}) + 3(x)(\frac{1}{4}) + \frac{1}{8}$.
**Resultado:** $\boxed{x^3 + \frac{3}{2}x^2 + \frac{3}{4}x + \frac{1}{8}}$

</details>


### Ejercicio 9
Simplifica: $(x + 1)^3 - x^3$

<details>
<summary>Ver solución</summary>

**Datos:** Desarrollo y resta de términos.
**Razonamiento:** $(x^3 + 3x^2 + 3x + 1) - x^3 = 3x^2 + 3x + 1$.
**Resultado:** $\boxed{3x^2 + 3x + 1}$

</details>


### Ejercicio 10
Calcula el volumen de un cubo de arista $(x + 3)$.

<details>
<summary>Ver solución</summary>

**Datos:** $V = \text{Arista}^3$.
**Razonamiento:** $(x + 3)^3 = x^3 + 3(x^2)(3) + 3(x)(3^2) + 3^3 = x^3 + 9x^2 + 27x + 27$.
**Resultado:** $\boxed{x^3 + 9x^2 + 27x + 27}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula / Descripción |
|----------|-----------------------|
| **Cubo de un Binomio** | Expresión elevada a la potencia 3. Tiene **4 términos**. |
| **Cubo Suma** | $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ |
| **Cubo Resta** | $(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$ |
| **Los Triples** | Los términos centrales siempre llevan el coeficiente **3**. |

> Elevar al cubo requiere orden. Recuerda la secuencia de exponentes del primer término: $3, 2, 1, 0$. Si sigues este ritmo, nunca olvidarás un término.

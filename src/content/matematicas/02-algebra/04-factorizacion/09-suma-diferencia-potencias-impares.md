# ⚡ Suma y Diferencia de Potencias Impares Iguales

En esta lección aprenderemos a factorizar expresiones de la forma $a^n + b^n$ y $a^n - b^n$ cuando $n$ es un número impar.

---

## 📖 Generalización de cubos a potencias impares

La suma y diferencia de cubos son casos particulares de una fórmula más general que aplica a **cualquier potencia impar**.

---

## 📖 Diferencia de potencias iguales

Para cualquier exponente natural $n$:

$$
a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + a^{n-3}b^2 + ... + ab^{n-2} + b^{n-1})
$$

Esta fórmula funciona para **cualquier valor de $n$** (par o impar).

### Casos particulares

| $n$ | Fórmula |
|:---:|:--------|
| $2$ | $a^2 - b^2 = (a - b)(a + b)$ |
| $3$ | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |
| $4$ | $a^4 - b^4 = (a - b)(a^3 + a^2b + ab^2 + b^3)$ |
| $5$ | $a^5 - b^5 = (a - b)(a^4 + a^3b + a^2b^2 + ab^3 + b^4)$ |

---

## 📖 Suma de potencias impares iguales

Para **$n$ impar**:

$$
a^n + b^n = (a + b)(a^{n-1} - a^{n-2}b + a^{n-3}b^2 - ... - ab^{n-2} + b^{n-1})
$$

> ⚠️ **Importante:** La suma de potencias **pares** (como $a^4 + b^4$) **no se factoriza** con esta fórmula.

### Casos particulares

| $n$ | Fórmula |
|:---:|:--------|
| $3$ | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| $5$ | $a^5 + b^5 = (a + b)(a^4 - a^3b + a^2b^2 - ab^3 + b^4)$ |
| $7$ | $a^7 + b^7 = (a + b)(a^6 - a^5b + a^4b^2 - a^3b^3 + a^2b^4 - ab^5 + b^6)$ |

---

## 📖 Patrón del segundo factor

### Para $a^n - b^n$

El segundo factor tiene:
- **$n$ términos**
- Los exponentes de $a$ bajan de $n-1$ a $0$
- Los exponentes de $b$ suben de $0$ a $n-1$
- **Todos los signos son positivos** ($+$)

### Para $a^n + b^n$ (n impar)

El segundo factor tiene:
- **$n$ términos**
- Los exponentes varían igual que arriba
- **Los signos alternan** ($+$, $-$, $+$, $-$, ...)
- Empieza con $+$ y termina con $+$

---

## 📖 Ejemplos de diferencia de potencias impares

### Ejemplo 1

Factoriza: $x^5 - 32$

**Identificamos:**
- $x^5 = (x)^5$
- $32 = 2^5$

$$
x^5 - 32 = (x - 2)(x^4 + x^3 \cdot 2 + x^2 \cdot 2^2 + x \cdot 2^3 + 2^4)
$$

$$
= (x - 2)(x^4 + 2x^3 + 4x^2 + 8x + 16)
$$

$$
\boxed{(x - 2)(x^4 + 2x^3 + 4x^2 + 8x + 16)}
$$

### Ejemplo 2

Factoriza: $a^5 - 1$

$$
a^5 - 1 = (a - 1)(a^4 + a^3 + a^2 + a + 1)
$$

$$
\boxed{(a - 1)(a^4 + a^3 + a^2 + a + 1)}
$$

### Ejemplo 3

Factoriza: $x^7 - y^7$

$$
x^7 - y^7 = (x - y)(x^6 + x^5y + x^4y^2 + x^3y^3 + x^2y^4 + xy^5 + y^6)
$$

$$
\boxed{(x - y)(x^6 + x^5y + x^4y^2 + x^3y^3 + x^2y^4 + xy^5 + y^6)}
$$

### Ejemplo 4

Factoriza: $32m^5 - 243$

- $32m^5 = (2m)^5$
- $243 = 3^5$

$$
32m^5 - 243 = (2m - 3)((2m)^4 + (2m)^3(3) + (2m)^2(3)^2 + (2m)(3)^3 + 3^4)
$$

$$
= (2m - 3)(16m^4 + 24m^3 + 36m^2 + 54m + 81)
$$

$$
\boxed{(2m - 3)(16m^4 + 24m^3 + 36m^2 + 54m + 81)}
$$

---

## 📖 Ejemplos de suma de potencias impares

### Ejemplo 5

Factoriza: $x^5 + 32$

**Identificamos:**
- $x^5 = (x)^5$
- $32 = 2^5$

$$
x^5 + 32 = (x + 2)(x^4 - x^3 \cdot 2 + x^2 \cdot 2^2 - x \cdot 2^3 + 2^4)
$$

$$
= (x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)
$$

$$
\boxed{(x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)}
$$

### Ejemplo 6

Factoriza: $a^5 + 1$

$$
a^5 + 1 = (a + 1)(a^4 - a^3 + a^2 - a + 1)
$$

$$
\boxed{(a + 1)(a^4 - a^3 + a^2 - a + 1)}
$$

### Ejemplo 7

Factoriza: $x^7 + y^7$

$$
x^7 + y^7 = (x + y)(x^6 - x^5y + x^4y^2 - x^3y^3 + x^2y^4 - xy^5 + y^6)
$$

$$
\boxed{(x + y)(x^6 - x^5y + x^4y^2 - x^3y^3 + x^2y^4 - xy^5 + y^6)}
$$

### Ejemplo 8

Factoriza: $32a^5 + 243b^5$

- $32a^5 = (2a)^5$
- $243b^5 = (3b)^5$

$$
= (2a + 3b)(16a^4 - 24a^3b + 36a^2b^2 - 54ab^3 + 81b^4)
$$

$$
\boxed{(2a + 3b)(16a^4 - 24a^3b + 36a^2b^2 - 54ab^3 + 81b^4)}
$$

---

## 📖 Diferencia de potencias pares

La diferencia de potencias pares se puede factorizar de forma iterada.

### Ejemplo 9

Factoriza: $x^4 - 16$

**Método 1:** Usando la fórmula general

$$
x^4 - 16 = (x - 2)(x^3 + 2x^2 + 4x + 8)
$$

**Método 2:** Diferencia de cuadrados (preferible)

$$
x^4 - 16 = (x^2)^2 - 4^2 = (x^2 + 4)(x^2 - 4)
$$

$$
= (x^2 + 4)(x + 2)(x - 2)
$$

$$
\boxed{(x^2 + 4)(x + 2)(x - 2)}
$$

### Ejemplo 10

Factoriza: $x^6 - 64$

**Usando diferencia de cuadrados:**

$$
x^6 - 64 = (x^3)^2 - 8^2 = (x^3 + 8)(x^3 - 8)
$$

Cada factor es suma/diferencia de cubos:

$$
= (x + 2)(x^2 - 2x + 4)(x - 2)(x^2 + 2x + 4)
$$

$$
\boxed{(x + 2)(x - 2)(x^2 - 2x + 4)(x^2 + 2x + 4)}
$$

---

## 📖 Suma de potencias pares

> ⚠️ La suma de potencias **pares** como $a^4 + b^4$ **no se factoriza** directamente con coeficientes racionales.

Por ejemplo, $x^4 + 16$ no puede factorizarse como producto de polinomios con coeficientes enteros.

**Excepción especial:** Algunas sumas de potencias pares pueden factorizarse añadiendo y restando un término (completar cuadrados), pero esto está fuera del alcance de esta lección.

---

## 📖 Con factor común

### Ejemplo 11

Factoriza: $2x^5 + 64$

**Paso 1:** Factor común $2$:

$$
2x^5 + 64 = 2(x^5 + 32)
$$

**Paso 2:** Suma de quintas potencias:

$$
= 2(x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)
$$

$$
\boxed{2(x + 2)(x^4 - 2x^3 + 4x^2 - 8x + 16)}
$$

### Ejemplo 12

Factoriza: $3a^7 - 3b^7$

**Paso 1:** Factor común $3$:

$$
3a^7 - 3b^7 = 3(a^7 - b^7)
$$

**Paso 2:**

$$
= 3(a - b)(a^6 + a^5b + a^4b^2 + a^3b^3 + a^2b^4 + ab^5 + b^6)
$$

$$
\boxed{3(a - b)(a^6 + a^5b + a^4b^2 + a^3b^3 + a^2b^4 + ab^5 + b^6)}
$$

---

## 📖 Resumen

| Expresión | Factorización | Condición |
|:----------|:--------------|:----------|
| $a^n - b^n$ | $(a - b)(\text{términos positivos})$ | Para todo $n$ |
| $a^n + b^n$ | $(a + b)(\text{signos alternados})$ | Solo $n$ impar |

---

## 📝 Ejercicios de práctica

### Diferencia de potencias impares

**Ejercicio 1:** $x^5 - 1$

**Ejercicio 2:** $a^5 - 243$

**Ejercicio 3:** $32x^5 - 1$

---

### Suma de potencias impares

**Ejercicio 4:** $x^5 + 1$

**Ejercicio 5:** $a^5 + 32$

**Ejercicio 6:** $243m^5 + 32n^5$

---

### Potencias pares

**Ejercicio 7:** $x^6 - 1$

**Ejercicio 8:** $a^8 - 256$

---

### Con factor común

**Ejercicio 9:** $2x^5 - 2$

**Ejercicio 10:** $5a^7 + 5$

---

## ✅ Soluciones

### Diferencia de potencias impares

**Ejercicio 1:**
$$
x^5 - 1 = (x - 1)(x^4 + x^3 + x^2 + x + 1)
$$

**Ejercicio 2:** ($243 = 3^5$)
$$
a^5 - 243 = (a - 3)(a^4 + 3a^3 + 9a^2 + 27a + 81)
$$

**Ejercicio 3:** ($32 = 2^5$)
$$
32x^5 - 1 = (2x - 1)(16x^4 + 8x^3 + 4x^2 + 2x + 1)
$$

### Suma de potencias impares

**Ejercicio 4:**
$$
x^5 + 1 = (x + 1)(x^4 - x^3 + x^2 - x + 1)
$$

**Ejercicio 5:**
$$
a^5 + 32 = (a + 2)(a^4 - 2a^3 + 4a^2 - 8a + 16)
$$

**Ejercicio 6:** ($243 = 3^5$, $32 = 2^5$)
$$
243m^5 + 32n^5 = (3m + 2n)(81m^4 - 54m^3n + 36m^2n^2 - 24mn^3 + 16n^4)
$$

### Potencias pares

**Ejercicio 7:**
$$
x^6 - 1 = (x^3 + 1)(x^3 - 1) = (x + 1)(x^2 - x + 1)(x - 1)(x^2 + x + 1)
$$

**Ejercicio 8:** ($256 = 4^4 = 2^8$)
$$
a^8 - 256 = (a^4 + 16)(a^4 - 16) = (a^4 + 16)(a^2 + 4)(a + 2)(a - 2)
$$

### Con factor común

**Ejercicio 9:**
$$
2x^5 - 2 = 2(x^5 - 1) = 2(x - 1)(x^4 + x^3 + x^2 + x + 1)
$$

**Ejercicio 10:**
$$
5a^7 + 5 = 5(a^7 + 1) = 5(a + 1)(a^6 - a^5 + a^4 - a^3 + a^2 - a + 1)
$$

---

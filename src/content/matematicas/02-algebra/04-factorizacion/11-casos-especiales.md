# 🌟 Casos Especiales de Factorización

En esta lección final estudiaremos casos especiales de factorización que combinan varios métodos o presentan formas particulares.

---

## 📖 Estrategia general de factorización

Antes de ver los casos especiales, repasemos el orden recomendado para factorizar cualquier expresión:

### Orden de factorización

1. **¿Hay factor común?** — Siempre es el primer paso
2. **¿Cuántos términos tiene?**
   - **2 términos:** Diferencia de cuadrados, suma/diferencia de cubos
   - **3 términos:** TCP, trinomio $x^2 + bx + c$ o $ax^2 + bx + c$
   - **4+ términos:** Agrupación
3. **¿Se puede factorizar más?** — Revisa cada factor

---

## 📖 Caso 1: Factor común seguido de otro caso

### Ejemplo 1

Factoriza: $3x^3 - 12x$

**Paso 1:** Factor común $3x$:

$$
3x^3 - 12x = 3x(x^2 - 4)
$$

**Paso 2:** Diferencia de cuadrados:

$$
= 3x(x + 2)(x - 2)
$$

$$
\boxed{3x(x + 2)(x - 2)}
$$

### Ejemplo 2

Factoriza: $2x^4 - 32$

**Paso 1:** Factor común $2$:

$$
2x^4 - 32 = 2(x^4 - 16)
$$

**Paso 2:** $x^4 - 16 = (x^2)^2 - 4^2$ → diferencia de cuadrados:

$$
= 2(x^2 + 4)(x^2 - 4)
$$

**Paso 3:** $x^2 - 4$ → diferencia de cuadrados:

$$
= 2(x^2 + 4)(x + 2)(x - 2)
$$

$$
\boxed{2(x^2 + 4)(x + 2)(x - 2)}
$$

---

## 📖 Caso 2: Diferencia de cuadrados con binomios

### Ejemplo 3

Factoriza: $(x + 1)^2 - 9$

Reconocemos: $a = (x + 1)$, $b = 3$

$$
(x + 1)^2 - 9 = [(x + 1) + 3][(x + 1) - 3]
$$

$$
= (x + 4)(x - 2)
$$

$$
\boxed{(x + 4)(x - 2)}
$$

### Ejemplo 4

Factoriza: $(2x - 3)^2 - (x + 1)^2$

Diferencia de cuadrados con $a = (2x - 3)$ y $b = (x + 1)$:

$$
= [(2x - 3) + (x + 1)][(2x - 3) - (x + 1)]
$$

$$
= (2x - 3 + x + 1)(2x - 3 - x - 1)
$$

$$
= (3x - 2)(x - 4)
$$

$$
\boxed{(3x - 2)(x - 4)}
$$

### Ejemplo 5

Factoriza: $4(a + b)^2 - 9(a - b)^2$

$$
= [2(a + b)]^2 - [3(a - b)]^2
$$

$$
= [2(a + b) + 3(a - b)][2(a + b) - 3(a - b)]
$$

$$
= (2a + 2b + 3a - 3b)(2a + 2b - 3a + 3b)
$$

$$
= (5a - b)(-a + 5b)
$$

$$
\boxed{(5a - b)(5b - a)}
$$

---

## 📖 Caso 3: TCP con binomios

### Ejemplo 6

Factoriza: $(x + 2)^2 + 6(x + 2) + 9$

Sea $u = (x + 2)$:

$$
u^2 + 6u + 9 = (u + 3)^2
$$

Sustituyendo de vuelta:

$$
= [(x + 2) + 3]^2 = (x + 5)^2
$$

$$
\boxed{(x + 5)^2}
$$

### Ejemplo 7

Factoriza: $(a - 1)^2 - 4(a - 1) + 4$

Sea $u = (a - 1)$:

$$
u^2 - 4u + 4 = (u - 2)^2
$$

$$
= [(a - 1) - 2]^2 = (a - 3)^2
$$

$$
\boxed{(a - 3)^2}
$$

---

## 📖 Caso 4: Trinomios con binomios

### Ejemplo 8

Factoriza: $(x + 1)^2 + 5(x + 1) + 6$

Sea $u = (x + 1)$:

$$
u^2 + 5u + 6 = (u + 2)(u + 3)
$$

Sustituyendo:

$$
= [(x + 1) + 2][(x + 1) + 3] = (x + 3)(x + 4)
$$

$$
\boxed{(x + 3)(x + 4)}
$$

### Ejemplo 9

Factoriza: $(2x - 1)^2 - (2x - 1) - 6$

Sea $u = (2x - 1)$:

$$
u^2 - u - 6 = (u - 3)(u + 2)
$$

$$
= [(2x - 1) - 3][(2x - 1) + 2]
$$

$$
= (2x - 4)(2x + 1) = 2(x - 2)(2x + 1)
$$

$$
\boxed{2(x - 2)(2x + 1)}
$$

---

## 📖 Caso 5: Suma de cuadrados (casos especiales)

Aunque $a^2 + b^2$ generalmente no se factoriza, hay casos donde sí es posible.

### Ejemplo 10: Añadiendo y restando un término

Factoriza: $x^4 + 4$

**Truco:** Añadimos y restamos $4x^2$:

$$
x^4 + 4 = x^4 + 4x^2 + 4 - 4x^2
$$

$$
= (x^2 + 2)^2 - (2x)^2
$$

$$
= [(x^2 + 2) + 2x][(x^2 + 2) - 2x]
$$

$$
= (x^2 + 2x + 2)(x^2 - 2x + 2)
$$

$$
\boxed{(x^2 + 2x + 2)(x^2 - 2x + 2)}
$$

### Ejemplo 11

Factoriza: $a^4 + 4b^4$

$$
= a^4 + 4a^2b^2 + 4b^4 - 4a^2b^2
$$

$$
= (a^2 + 2b^2)^2 - (2ab)^2
$$

$$
= (a^2 + 2ab + 2b^2)(a^2 - 2ab + 2b^2)
$$

$$
\boxed{(a^2 + 2ab + 2b^2)(a^2 - 2ab + 2b^2)}
$$

---

## 📖 Caso 6: Agrupación creativa

### Ejemplo 12

Factoriza: $x^2 + 2xy + y^2 - z^2$

**Reconocemos TCP:** $x^2 + 2xy + y^2 = (x + y)^2$

$$
= (x + y)^2 - z^2
$$

**Diferencia de cuadrados:**

$$
= [(x + y) + z][(x + y) - z]
$$

$$
= (x + y + z)(x + y - z)
$$

$$
\boxed{(x + y + z)(x + y - z)}
$$

### Ejemplo 13

Factoriza: $a^2 - 4ab + 4b^2 - 9c^2$

$$
= (a - 2b)^2 - (3c)^2
$$

$$
= (a - 2b + 3c)(a - 2b - 3c)
$$

$$
\boxed{(a - 2b + 3c)(a - 2b - 3c)}
$$

### Ejemplo 14

Factoriza: $x^2 - y^2 + x - y$

**Agrupamos:**

$$
= (x^2 - y^2) + (x - y)
$$

$$
= (x + y)(x - y) + 1(x - y)
$$

$$
= (x - y)(x + y + 1)
$$

$$
\boxed{(x - y)(x + y + 1)}
$$

---

## 📖 Caso 7: Expresiones cíclicas

### Ejemplo 15

Factoriza: $a^2(b - c) + b^2(c - a) + c^2(a - b)$

Expandimos y agrupamos:

$$
= a^2b - a^2c + b^2c - ab^2 + ac^2 - bc^2
$$

Agrupamos de forma conveniente:

$$
= a^2b - ab^2 + b^2c - bc^2 + ac^2 - a^2c
$$

$$
= ab(a - b) + bc(b - c) + c(a + c)(a - c)... 
$$

**Forma factorizada (resultado conocido):**

$$
= -(a - b)(b - c)(c - a)
$$

$$
\boxed{-(a - b)(b - c)(c - a)}
$$

---

## 📖 Caso 8: Factorización iterada

### Ejemplo 16

Factoriza completamente: $x^8 - 1$

**Paso 1:** Diferencia de cuadrados:

$$
x^8 - 1 = (x^4 + 1)(x^4 - 1)
$$

**Paso 2:** $x^4 - 1$ → diferencia de cuadrados:

$$
= (x^4 + 1)(x^2 + 1)(x^2 - 1)
$$

**Paso 3:** $x^2 - 1$ → diferencia de cuadrados:

$$
= (x^4 + 1)(x^2 + 1)(x + 1)(x - 1)
$$

$$
\boxed{(x^4 + 1)(x^2 + 1)(x + 1)(x - 1)}
$$

### Ejemplo 17

Factoriza completamente: $x^6 - y^6$

**Opción 1:** Como diferencia de cuadrados:

$$
x^6 - y^6 = (x^3)^2 - (y^3)^2 = (x^3 + y^3)(x^3 - y^3)
$$

Luego aplicamos suma y diferencia de cubos:

$$
= (x + y)(x^2 - xy + y^2)(x - y)(x^2 + xy + y^2)
$$

$$
\boxed{(x + y)(x - y)(x^2 - xy + y^2)(x^2 + xy + y^2)}
$$

---

## 📖 Resumen de casos especiales

| Caso | Forma | Técnica |
|:----:|:------|:--------|
| 1 | Factor común + otro | Secuencial |
| 2 | $(A)^2 - (B)^2$ | Diferencia de cuadrados con expresiones |
| 3 | $(u)^2 \pm 2(u) + 1$ | TCP con sustitución |
| 4 | $(u)^2 + b(u) + c$ | Trinomio con sustitución |
| 5 | $a^4 + 4b^4$ | Añadir/restar término |
| 6 | TCP $- z^2$ | Agrupar y diferencia |
| 7 | Expresiones simétricas | Patrones conocidos |
| 8 | Potencias altas | Factorización iterada |

---

## 📝 Ejercicios de práctica

### Factor común + otro caso

**Ejercicio 1:** $5x^3 - 20x$

**Ejercicio 2:** $3a^4 - 48$

---

### Diferencia de cuadrados con binomios

**Ejercicio 3:** $(x + 3)^2 - 16$

**Ejercicio 4:** $(3x - 1)^2 - (2x + 1)^2$

---

### Trinomios con sustitución

**Ejercicio 5:** $(x - 2)^2 + 7(x - 2) + 12$

**Ejercicio 6:** $(a + 1)^2 - 2(a + 1) - 15$

---

### Agrupación creativa

**Ejercicio 7:** $x^2 - 6x + 9 - 4y^2$

**Ejercicio 8:** $a^2 - b^2 + a + b$

---

### Factorización iterada

**Ejercicio 9:** $x^4 - 81$

**Ejercicio 10:** $a^6 - 64$

---

## ✅ Soluciones

### Factor común + otro caso

**Ejercicio 1:**
$$
5x^3 - 20x = 5x(x^2 - 4) = 5x(x + 2)(x - 2)
$$

**Ejercicio 2:**
$$
3a^4 - 48 = 3(a^4 - 16) = 3(a^2 + 4)(a + 2)(a - 2)
$$

### Diferencia de cuadrados con binomios

**Ejercicio 3:**
$$
(x + 3)^2 - 16 = (x + 3 + 4)(x + 3 - 4) = (x + 7)(x - 1)
$$

**Ejercicio 4:**
$$
= (3x - 1 + 2x + 1)(3x - 1 - 2x - 1) = (5x)(x - 2) = 5x(x - 2)
$$

### Trinomios con sustitución

**Ejercicio 5:** Sea $u = (x - 2)$:
$$
u^2 + 7u + 12 = (u + 3)(u + 4) = (x + 1)(x + 2)
$$

**Ejercicio 6:** Sea $u = (a + 1)$:
$$
u^2 - 2u - 15 = (u - 5)(u + 3) = (a - 4)(a + 4)
$$

### Agrupación creativa

**Ejercicio 7:**
$$
(x - 3)^2 - (2y)^2 = (x - 3 + 2y)(x - 3 - 2y)
$$

**Ejercicio 8:**
$$
(a + b)(a - b) + (a + b) = (a + b)(a - b + 1)
$$

### Factorización iterada

**Ejercicio 9:**
$$
x^4 - 81 = (x^2 + 9)(x^2 - 9) = (x^2 + 9)(x + 3)(x - 3)
$$

**Ejercicio 10:**
$$
a^6 - 64 = (a^3 + 8)(a^3 - 8) = (a + 2)(a^2 - 2a + 4)(a - 2)(a^2 + 2a + 4)
$$

---

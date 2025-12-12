# ✂️ Simplificación de Radicales

En esta lección aprenderemos a simplificar radicales extrayendo factores del radicando que sean potencias perfectas.

---

## 📖 ¿Qué significa simplificar un radical?

**Simplificar un radical** significa expresarlo en su forma más simple, extrayendo del radical todos los factores posibles.

Un radical está simplificado cuando:
1. El radicando no tiene factores que sean potencias del índice
2. El índice y el exponente no tienen factores comunes
3. No hay radicales en el denominador (se verá en racionalización)

---

## 📖 Método de simplificación

Para simplificar $\sqrt[n]{a^m}$:

1. **Dividir** el exponente $m$ entre el índice $n$
2. **Cociente**: sale fuera del radical
3. **Residuo**: queda dentro del radical

$$
\sqrt[n]{a^m} = a^{\frac{m}{n}} = a^{q} \cdot \sqrt[n]{a^r}
$$

donde $m = n \cdot q + r$ (división euclidiana)

---

## 📖 Ejemplos con raíces cuadradas

### Ejemplo 1

Simplificar $\sqrt{18}$.

**Paso 1:** Descomponemos en factores primos:

$$
18 = 2 \times 9 = 2 \times 3^2
$$

**Paso 2:** Extraemos las potencias perfectas:

$$
\sqrt{18} = \sqrt{9 \times 2} = \sqrt{9} \cdot \sqrt{2} = 3\sqrt{2}
$$

$$
\boxed{\sqrt{18} = 3\sqrt{2}}
$$

---

### Ejemplo 2

Simplificar $\sqrt{72}$.

$$
72 = 36 \times 2 = 6^2 \times 2
$$

$$
\sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}
$$

$$
\boxed{\sqrt{72} = 6\sqrt{2}}
$$

---

### Ejemplo 3

Simplificar $\sqrt{200}$.

$$
200 = 100 \times 2 = 10^2 \times 2
$$

$$
\sqrt{200} = \sqrt{100 \times 2} = 10\sqrt{2}
$$

$$
\boxed{\sqrt{200} = 10\sqrt{2}}
$$

---

### Ejemplo 4

Simplificar $\sqrt{x^5}$.

$$
\sqrt{x^5} = \sqrt{x^4 \cdot x} = \sqrt{x^4} \cdot \sqrt{x} = x^2\sqrt{x}
$$

$$
\boxed{\sqrt{x^5} = x^2\sqrt{x}}
$$

---

### Ejemplo 5

Simplificar $\sqrt{50a^3b^4}$.

$$
\sqrt{50a^3b^4} = \sqrt{25 \cdot 2 \cdot a^2 \cdot a \cdot b^4}
$$

$$
= \sqrt{25} \cdot \sqrt{a^2} \cdot \sqrt{b^4} \cdot \sqrt{2a} = 5ab^2\sqrt{2a}
$$

$$
\boxed{\sqrt{50a^3b^4} = 5ab^2\sqrt{2a}}
$$

---

## 📖 Ejemplos con raíces cúbicas

### Ejemplo 6

Simplificar $\sqrt[3]{54}$.

$$
54 = 27 \times 2 = 3^3 \times 2
$$

$$
\sqrt[3]{54} = \sqrt[3]{27 \times 2} = 3\sqrt[3]{2}
$$

$$
\boxed{\sqrt[3]{54} = 3\sqrt[3]{2}}
$$

---

### Ejemplo 7

Simplificar $\sqrt[3]{128}$.

$$
128 = 64 \times 2 = 4^3 \times 2
$$

$$
\sqrt[3]{128} = \sqrt[3]{64 \times 2} = 4\sqrt[3]{2}
$$

$$
\boxed{\sqrt[3]{128} = 4\sqrt[3]{2}}
$$

---

### Ejemplo 8

Simplificar $\sqrt[3]{x^7}$.

$$
\sqrt[3]{x^7} = \sqrt[3]{x^6 \cdot x} = \sqrt[3]{x^6} \cdot \sqrt[3]{x} = x^2\sqrt[3]{x}
$$

$$
\boxed{\sqrt[3]{x^7} = x^2\sqrt[3]{x}}
$$

---

### Ejemplo 9

Simplificar $\sqrt[3]{40a^5b^8}$.

$$
40 = 8 \times 5 = 2^3 \times 5
$$

$$
\sqrt[3]{40a^5b^8} = \sqrt[3]{8 \times 5 \times a^3 \times a^2 \times b^6 \times b^2}
$$

$$
= 2ab^2\sqrt[3]{5a^2b^2}
$$

$$
\boxed{\sqrt[3]{40a^5b^8} = 2ab^2\sqrt[3]{5a^2b^2}}
$$

---

## 📖 Ejemplos con otros índices

### Ejemplo 10

Simplificar $\sqrt[4]{48}$.

$$
48 = 16 \times 3 = 2^4 \times 3
$$

$$
\sqrt[4]{48} = \sqrt[4]{16 \times 3} = 2\sqrt[4]{3}
$$

$$
\boxed{\sqrt[4]{48} = 2\sqrt[4]{3}}
$$

---

### Ejemplo 11

Simplificar $\sqrt[4]{x^{10}y^7}$.

Para $x$: $10 = 4 \times 2 + 2$, entonces sale $x^2$ y queda $x^2$

Para $y$: $7 = 4 \times 1 + 3$, entonces sale $y^1$ y queda $y^3$

$$
\sqrt[4]{x^{10}y^7} = x^2y\sqrt[4]{x^2y^3}
$$

$$
\boxed{\sqrt[4]{x^{10}y^7} = x^2y\sqrt[4]{x^2y^3}}
$$

---

### Ejemplo 12

Simplificar $\sqrt[5]{64a^8}$.

$$
64 = 32 \times 2 = 2^5 \times 2
$$

Para $a$: $8 = 5 \times 1 + 3$

$$
\sqrt[5]{64a^8} = \sqrt[5]{32 \times 2 \times a^5 \times a^3} = 2a\sqrt[5]{2a^3}
$$

$$
\boxed{\sqrt[5]{64a^8} = 2a\sqrt[5]{2a^3}}
$$

---

## 📋 Resumen del proceso

| Paso | Descripción |
|:----:|:------------|
| 1 | Factorizar el radicando |
| 2 | Identificar potencias del índice |
| 3 | Extraer las raíces exactas |
| 4 | Dejar el resto bajo el radical |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Simplifica $\sqrt{45}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{45} = \sqrt{9 \times 5} = 3\sqrt{5}
$$

</details>

---

**Ejercicio 2:** Simplifica $\sqrt{98}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{98} = \sqrt{49 \times 2} = 7\sqrt{2}
$$

</details>

---

**Ejercicio 3:** Simplifica $\sqrt{x^7y^4}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{x^7y^4} = x^3y^2\sqrt{x}
$$

</details>

---

**Ejercicio 4:** Simplifica $\sqrt[3]{250}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt[3]{250} = \sqrt[3]{125 \times 2} = 5\sqrt[3]{2}
$$

</details>

---

**Ejercicio 5:** Simplifica $\sqrt[3]{a^{11}b^5}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt[3]{a^{11}b^5} = a^3b\sqrt[3]{a^2b^2}
$$

</details>

---

**Ejercicio 6:** Simplifica $\sqrt[4]{80x^9}$.

<details>
<summary>Ver solución</summary>

$$
80 = 16 \times 5, \quad x^9 = x^8 \cdot x
$$

$$
\sqrt[4]{80x^9} = 2x^2\sqrt[4]{5x}
$$

</details>

---

# ✖️ Multiplicación de Radicales

En esta lección aprenderemos a multiplicar radicales, tanto con el mismo índice como con índices diferentes.

---

## 📖 Multiplicación de radicales con el mismo índice

Cuando los radicales tienen el **mismo índice**, se multiplican los radicandos:

$$
\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}
$$

---

### Ejemplo 1

Calcular $\sqrt{3} \cdot \sqrt{5}$.

$$
\sqrt{3} \cdot \sqrt{5} = \sqrt{3 \times 5} = \sqrt{15}
$$

$$
\boxed{\sqrt{3} \cdot \sqrt{5} = \sqrt{15}}
$$

---

### Ejemplo 2

Calcular $\sqrt{6} \cdot \sqrt{6}$.

$$
\sqrt{6} \cdot \sqrt{6} = \sqrt{36} = 6
$$

$$
\boxed{\sqrt{6} \cdot \sqrt{6} = 6}
$$

---

### Ejemplo 3

Calcular $\sqrt[3]{4} \cdot \sqrt[3]{2}$.

$$
\sqrt[3]{4} \cdot \sqrt[3]{2} = \sqrt[3]{8} = 2
$$

$$
\boxed{\sqrt[3]{4} \cdot \sqrt[3]{2} = 2}
$$

---

### Ejemplo 4

Calcular $2\sqrt{3} \cdot 5\sqrt{7}$.

$$
2\sqrt{3} \cdot 5\sqrt{7} = (2 \times 5)(\sqrt{3} \cdot \sqrt{7}) = 10\sqrt{21}
$$

$$
\boxed{2\sqrt{3} \cdot 5\sqrt{7} = 10\sqrt{21}}
$$

---

### Ejemplo 5

Calcular $3\sqrt{8} \cdot 2\sqrt{2}$.

$$
3\sqrt{8} \cdot 2\sqrt{2} = 6\sqrt{16} = 6 \times 4 = 24
$$

$$
\boxed{3\sqrt{8} \cdot 2\sqrt{2} = 24}
$$

---

## 📖 Multiplicación con variables

### Ejemplo 6

Simplificar $\sqrt{2x} \cdot \sqrt{8x}$.

$$
\sqrt{2x} \cdot \sqrt{8x} = \sqrt{16x^2} = 4x
$$

(Asumiendo $x \geq 0$)

$$
\boxed{\sqrt{2x} \cdot \sqrt{8x} = 4x}
$$

---

### Ejemplo 7

Simplificar $\sqrt{x^3} \cdot \sqrt{x^5}$.

$$
\sqrt{x^3} \cdot \sqrt{x^5} = \sqrt{x^8} = x^4
$$

$$
\boxed{\sqrt{x^3} \cdot \sqrt{x^5} = x^4}
$$

---

## 📖 Multiplicación de radicales con diferentes índices

Para multiplicar radicales con **índices diferentes**, primero los convertimos al **mismo índice** usando el MCM de los índices.

$$
\sqrt[n]{a} \cdot \sqrt[m]{b} = \sqrt[\text{MCM}(n,m)]{a^{m/d} \cdot b^{n/d}}
$$

donde $d = \text{MCD}(n, m)$

---

### Ejemplo 8

Calcular $\sqrt{2} \cdot \sqrt[3]{4}$.

**Paso 1:** El MCM de 2 y 3 es 6.

**Paso 2:** Convertimos a índice 6:

$$
\sqrt{2} = \sqrt[6]{2^3} = \sqrt[6]{8}
$$

$$
\sqrt[3]{4} = \sqrt[6]{4^2} = \sqrt[6]{16}
$$

**Paso 3:** Multiplicamos:

$$
\sqrt[6]{8} \cdot \sqrt[6]{16} = \sqrt[6]{128}
$$

$$
\boxed{\sqrt{2} \cdot \sqrt[3]{4} = \sqrt[6]{128}}
$$

---

### Ejemplo 9

Calcular $\sqrt{3} \cdot \sqrt[4]{9}$.

**Paso 1:** El MCM de 2 y 4 es 4.

**Paso 2:** Convertimos:

$$
\sqrt{3} = \sqrt[4]{3^2} = \sqrt[4]{9}
$$

$$
\sqrt[4]{9} = \sqrt[4]{9}
$$

**Paso 3:** Multiplicamos:

$$
\sqrt[4]{9} \cdot \sqrt[4]{9} = \sqrt[4]{81} = 3
$$

$$
\boxed{\sqrt{3} \cdot \sqrt[4]{9} = 3}
$$

---

## 📖 Productos con sumas (distributiva)

### Ejemplo 10

Desarrollar $\sqrt{2}(\sqrt{3} + \sqrt{5})$.

Aplicamos la propiedad distributiva:

$$
\sqrt{2}(\sqrt{3} + \sqrt{5}) = \sqrt{2} \cdot \sqrt{3} + \sqrt{2} \cdot \sqrt{5}
$$

$$
= \sqrt{6} + \sqrt{10}
$$

$$
\boxed{\sqrt{2}(\sqrt{3} + \sqrt{5}) = \sqrt{6} + \sqrt{10}}
$$

---

### Ejemplo 11

Desarrollar $(\sqrt{3} + \sqrt{2})(\sqrt{3} - \sqrt{2})$.

Este es un producto de suma por diferencia (diferencia de cuadrados):

$$
(\sqrt{3} + \sqrt{2})(\sqrt{3} - \sqrt{2}) = (\sqrt{3})^2 - (\sqrt{2})^2 = 3 - 2 = 1
$$

$$
\boxed{(\sqrt{3} + \sqrt{2})(\sqrt{3} - \sqrt{2}) = 1}
$$

---

### Ejemplo 12

Desarrollar $(\sqrt{5} + 2)^2$.

Usamos el cuadrado de un binomio:

$$
(\sqrt{5} + 2)^2 = (\sqrt{5})^2 + 2(\sqrt{5})(2) + 2^2
$$

$$
= 5 + 4\sqrt{5} + 4 = 9 + 4\sqrt{5}
$$

$$
\boxed{(\sqrt{5} + 2)^2 = 9 + 4\sqrt{5}}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $\sqrt{5} \cdot \sqrt{7}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{5 \cdot 7} = \sqrt{35}
$$

</details>

---

**Ejercicio 2:** Calcula $3\sqrt{2} \cdot 4\sqrt{5}$.

<details>
<summary>Ver solución</summary>

$$
12\sqrt{10}
$$

</details>

---

**Ejercicio 3:** Simplifica $\sqrt{12} \cdot \sqrt{3}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{36} = 6
$$

</details>

---

**Ejercicio 4:** Desarrolla $\sqrt{3}(\sqrt{6} - \sqrt{2})$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{18} - \sqrt{6} = 3\sqrt{2} - \sqrt{6}
$$

</details>

---

**Ejercicio 5:** Desarrolla $(\sqrt{7} + 1)(\sqrt{7} - 1)$.

<details>
<summary>Ver solución</summary>

$$
(\sqrt{7})^2 - 1^2 = 7 - 1 = 6
$$

</details>

---

**Ejercicio 6:** Desarrolla $(2\sqrt{3} - 1)^2$.

<details>
<summary>Ver solución</summary>

$$
(2\sqrt{3})^2 - 2(2\sqrt{3})(1) + 1 = 12 - 4\sqrt{3} + 1 = 13 - 4\sqrt{3}
$$

</details>

---

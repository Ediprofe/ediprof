---
title: "Propiedades de los Logaritmos"
---

# **Propiedades de los Logaritmos**

Si los logaritmos son "exponentes disfrazados", las propiedades de los logaritmos son las mismas que las de las potencias, pero traducidas al lenguaje logarítmico. Estas reglas te permiten descomponer logaritmos complicados en piezas simples, o fusionar varios logaritmos en uno solo.

---

## 🎯 ¿Qué vas a aprender?

- Convertir multiplicaciones en sumas de logaritmos.
- Convertir divisiones en restas de logaritmos.
- Bajar exponentes como coeficientes.
- Cambiar de base cuando sea necesario.

---

## 1. Logaritmo de un Producto

Si tienes el logaritmo de una multiplicación, puedes separarlo en una suma.

$$ \log_b(A \times B) = \log_b A + \log_b B $$

**Intuición:** Multiplicar números es como sumar sus exponentes. Los logaritmos "leen" esos exponentes.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Producto simple
$$ \log_2(4 \times 8) $$
Separamos:
$$ \log_2 4 + \log_2 8 = 2 + 3 = \boxed{5} $$
(Verificación: $4 \times 8 = 32$, y $\log_2 32 = 5$).

#### Ejemplo 2: Base 10
$$ \log(100 \times 1000) $$
$$ \log 100 + \log 1000 = 2 + 3 = \boxed{5} $$

#### Ejemplo 3: Tres factores
$$ \log_3(3 \times 9 \times 27) $$
$$ \log_3 3 + \log_3 9 + \log_3 27 = 1 + 2 + 3 = \boxed{6} $$

#### Ejemplo 4: Variables
$$ \log(xy) = \log x + \log y $$

#### Ejemplo 5: Fusionar suma en producto
$$ \log_5 25 + \log_5 5 $$
Fusionamos:
$$ \log_5(25 \times 5) = \log_5 125 = \boxed{3} $$

---

## 2. Logaritmo de un Cociente

Si tienes el logaritmo de una división, puedes separarlo en una resta.

$$ \log_b\left(\frac{A}{B}\right) = \log_b A - \log_b B $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: División simple
$$ \log_2\left(\frac{32}{4}\right) $$
Separamos:
$$ \log_2 32 - \log_2 4 = 5 - 2 = \boxed{3} $$

#### Ejemplo 7: Base 10
$$ \log\left(\frac{10000}{100}\right) $$
$$ \log 10000 - \log 100 = 4 - 2 = \boxed{2} $$

#### Ejemplo 8: Variables
$$ \log\left(\frac{x}{y}\right) = \log x - \log y $$

#### Ejemplo 9: Fusionar resta en cociente
$$ \log_3 81 - \log_3 9 $$
$$ \log_3\left(\frac{81}{9}\right) = \log_3 9 = \boxed{2} $$

#### Ejemplo 10: Inverso
$$ \log_5\left(\frac{1}{25}\right) $$
$$ \log_5 1 - \log_5 25 = 0 - 2 = \boxed{-2} $$

---

## 3. Logaritmo de una Potencia

Si el argumento está elevado a una potencia, el exponente "baja" como multiplicador.

$$ \log_b(A^n) = n \cdot \log_b A $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 11: Potencia simple
$$ \log_2(8^3) $$
Bajamos el 3:
$$ 3 \cdot \log_2 8 = 3 \cdot 3 = \boxed{9} $$

#### Ejemplo 12: Cuadrado
$$ \log(100^2) $$
$$ 2 \cdot \log 100 = 2 \cdot 2 = \boxed{4} $$

#### Ejemplo 13: Raíz como potencia fraccionaria
$$ \log_3(\sqrt{9}) = \log_3(9^{1/2}) $$
$$ \frac{1}{2} \cdot \log_3 9 = \frac{1}{2} \cdot 2 = \boxed{1} $$

#### Ejemplo 14: Exponente negativo
$$ \log_5(25^{-1}) $$
$$ -1 \cdot \log_5 25 = -1 \cdot 2 = \boxed{-2} $$

#### Ejemplo 15: Variables
$$ \log(x^5) = 5 \log x $$

---

## 4. Cambio de Base

A veces necesitas calcular un logaritmo en una base que tu calculadora no tiene. La fórmula de cambio de base te salva.

$$ \log_b A = \frac{\log_c A}{\log_c b} $$

(Usualmente $c = 10$ o $c = e$).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 16: Cambio a base 10
$$ \log_2 8 $$
Usando base 10:
$$ \frac{\log 8}{\log 2} = \frac{0.903}{0.301} \approx \boxed{3} $$

#### Ejemplo 17: Cambio a base natural
$$ \log_5 25 $$
$$ \frac{\ln 25}{\ln 5} = \frac{3.219}{1.609} \approx \boxed{2} $$

#### Ejemplo 18: Verificación
$$ \log_3 27 = \frac{\log 27}{\log 3} = \frac{1.431}{0.477} = \boxed{3} $$

#### Ejemplo 19: Base arbitraria
$$ \log_4 16 = \frac{\log_2 16}{\log_2 4} = \frac{4}{2} = \boxed{2} $$

#### Ejemplo 20: Simplificación
$$ \frac{\log_b x}{\log_b y} = \log_y x $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Expande $\log_2(16 \times 32)$.

<details>
<summary>Ver solución</summary>

$\log_2 16 + \log_2 32 = 4 + 5$.
**Resultado:** $\boxed{9}$

</details>

### Ejercicio 2
Simplifica $\log_3 81 - \log_3 9$.

<details>
<summary>Ver solución</summary>

$\log_3(81/9) = \log_3 9$.
**Resultado:** $\boxed{2}$

</details>

### Ejercicio 3
Calcula $\log_5(125^2)$.

<details>
<summary>Ver solución</summary>

$2 \cdot \log_5 125 = 2 \cdot 3$.
**Resultado:** $\boxed{6}$

</details>

### Ejercicio 4
Fusiona $\log 10 + \log 100$.

<details>
<summary>Ver solución</summary>

$\log(10 \times 100) = \log 1000$.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 5
Calcula $\log_2(\sqrt{16})$.

<details>
<summary>Ver solución</summary>

$\log_2(16^{1/2}) = \frac{1}{2} \cdot 4$.
**Resultado:** $\boxed{2}$

</details>

### Ejercicio 6
Simplifica $2\log_3 9$.

<details>
<summary>Ver solución</summary>

$\log_3(9^2) = \log_3 81$.
**Resultado:** $\boxed{4}$

</details>

### Ejercicio 7
Expande $\log(x^3 y^2)$.

<details>
<summary>Ver solución</summary>

$3\log x + 2\log y$.
**Resultado:** $\boxed{3\log x + 2\log y}$

</details>

### Ejercicio 8
Calcula $\log_4 64$ usando cambio de base a base 2.

<details>
<summary>Ver solución</summary>

$\frac{\log_2 64}{\log_2 4} = \frac{6}{2}$.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 9
Simplifica $\log_5 1 - \log_5 25$.

<details>
<summary>Ver solución</summary>

$0 - 2$.
**Resultado:** $\boxed{-2}$

</details>

### Ejercicio 10
Calcula $\log_3(27^{-1})$.

<details>
<summary>Ver solución</summary>

$-1 \cdot \log_3 27 = -1 \cdot 3$.
**Resultado:** $\boxed{-3}$

</details>

---

## 🔑 Resumen

| Propiedad | Fórmula |
| :--- | :--- |
| **Producto** | $\log(AB) = \log A + \log B$ |
| **Cociente** | $\log(A/B) = \log A - \log B$ |
| **Potencia** | $\log(A^n) = n \log A$ |
| **Cambio de Base** | $\log_b A = \frac{\log A}{\log b}$ |

> **Conclusión:** Las propiedades de los logaritmos son herramientas algebraicas para descomponer expresiones complejas. Domínalas y podrás resolver ecuaciones logarítmicas como un profesional.

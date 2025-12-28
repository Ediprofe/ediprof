# **Logaritmos: Conceptos Básicos**

El nombre asusta, pero la idea es ridículamente simple. Un logaritmo no es más que **un exponente buscando su base**. Es la pregunta: "¿Cuántas veces tengo que multiplicar este número pequeño para llegar al grande?". Si entiendes las potencias, ya entiendes los logaritmos.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un logaritmo (spoiler: es un exponente).
- Cómo leer $\log_2 8$ sin entrar en pánico.
- Por qué el logaritmo de 1 siempre es 0.
- Los logaritmos famosos: El Común (base 10) y el Natural (base $e$).

---

## ¿Qué es un Logaritmo?

Es la operación inversa a la potenciación, pero enfocada en buscar el **exponente**.

Si $2^3 = 8$, entonces el logaritmo en base 2 de 8 es 3.
Traducido al español: "¿A qué potencia elevo el 2 para que me de 8? Respuesta: A la 3".

$$ \log_{\text{Base}}(\text{Resultado}) = \text{Exponente} \iff \text{Base}^{\text{Exponente}} = \text{Resultado} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Logaritmo en base 2
Pregunta: "¿2 elevado a qué da 8?".
$2 \times 2 \times 2 = 8$ (3 veces).
$$ \log_2 8 = \boxed{3} $$

#### Ejemplo 2: Logaritmo en base 3
Pregunta: "¿3 elevado a qué da 9?".
$3^2 = 9$.
$$ \log_3 9 = \boxed{2} $$

#### Ejemplo 3: Logaritmo en base 5
$5^1 = 5$.
$5^2 = 25$.
$5^3 = 125$.
$$ \log_5 125 = \boxed{3} $$

#### Ejemplo 4: Logaritmo en base 10
¿Cuántos 10 necesito para llegar a 1000? Tres.
$$ \log_{10} 1000 = \boxed{3} $$

#### Ejemplo 5: Logaritmo en base 4
$4 \times 4 = 16$.
$$ \log_4 16 = \boxed{2} $$

---

## Propiedades Fundamentales

Hay dos casos obvios que debes saber de memoria para no perder tiempo.

1.  **Logaritmo de 1:** ¿A qué elevo cualquier número (5, 100, 1000) para que me de 1? ¡A la cero!
    $$ \log_b(1) = 0 $$
2.  **Logaritmo de la Base:** ¿A qué elevo 5 para que me de 5? ¡A la uno!
    $$ \log_b(b) = 1 $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: Logaritmo de la unidad
La base es 25. El objetivo es 1. Exponente: 0.
$$ \boxed{0} $$

#### Ejemplo 7: Logaritmo de la propia base
La base es 7. El objetivo es 7. Exponente: 1.
$$ \boxed{1} $$

#### Ejemplo 8: Identidad logarítmica
Si la base y el argumento son iguales, da 1.
$$ \boxed{1} $$

#### Ejemplo 9: Otro logaritmo de uno
$$ \boxed{0} $$

#### Ejemplo 10: Logaritmo de una potencia de la base
Pregunta: "¿A qué elevo 3 para obtener $3^5$?". ¡Pues a la 5!
$$ \boxed{5} $$

---

## Los Logaritmos Famosos

Si ves un logaritmo sin numerito abajo (sin base), o uno que dice "ln", son los VIPs del mundo matemático.

1.  **Logaritmo Común ($\log$):** Base 10. Es el estándar de nuestra calculadora científica.
    $$ \log(x) \quad \text{significa} \quad \log_{10}(x) $$
2.  **Logaritmo Natural ($\ln$):** Base $e$ (Euler $\approx 2.718$). Es el lenguaje de la naturaleza y el crecimiento.
    $$ \ln(x) \quad \text{significa} \quad \log_{e}(x) $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 11: Logaritmo común de cien
Base invisible es 10. $10^2 = 100$.
$$ \boxed{2} $$

#### Ejemplo 12: Logaritmo común de diez mil
Cuenta los ceros del 10,000. Son 4.
$$ \boxed{4} $$

#### Ejemplo 13: Logaritmo natural de e
Base $e$. Argumento $e$. Son iguales.
$$ \boxed{1} $$

#### Ejemplo 14: Logaritmo natural de uno
Logaritmo de 1 siempre es 0, no importa la base.
$$ \boxed{0} $$

#### Ejemplo 15: Logaritmo de un decimal
$0.1 = \frac{1}{10} = 10^{-1}$.
$$ \boxed{-1} $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\log_2 32$.

<details>
<summary>Ver solución</summary>

$2^5 = 32$.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 2
Calcula $\log_3 27$.

<details>
<summary>Ver solución</summary>

$3^3 = 27$.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 3
Calcula $\log 1000$.

<details>
<summary>Ver solución</summary>

Base 10.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 4
Calcula $\log_5 1$.

<details>
<summary>Ver solución</summary>

Siempre es 0.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 5
Calcula $\log_6 6$.

<details>
<summary>Ver solución</summary>

Base igual al número.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 6
Calcula $\log_2 64$.

<details>
<summary>Ver solución</summary>

$2^6 = 64$.
**Resultado:** $\boxed{6}$

</details>

### Ejercicio 7
Calcula $\ln(e^3)$.

<details>
<summary>Ver solución</summary>

El exponente de $e$.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 8
Calcula $\log_{10} 0.01$.

<details>
<summary>Ver solución</summary>

$1/100 = 10^{-2}$.
**Resultado:** $\boxed{-2}$

</details>

### Ejercicio 9
Si $\log_x 9 = 2$, ¿quién es $x$?

<details>
<summary>Ver solución</summary>

$x^2 = 9$.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 10
Si $\log_2 x = 4$, ¿quién es $x$?

<details>
<summary>Ver solución</summary>

$2^4 = x$.
**Resultado:** $\boxed{16}$

</details>

---

## 🔑 Resumen

| Notación | Significado | Ejemplo |
| :--- | :--- | :--- |
| $\log_b a = c$ | $b^c = a$ | $\log_2 8 = 3 \iff 2^3 = 8$ |
| $\log x$ | Base 10 | $\log 100 = 2$ |
| $\ln x$ | Base $e$ | $\ln e = 1$ |
| $\log 1$ | 0 | $\ln 1 = 0$ |

> **Conclusión:** No dejes que la palabra "logaritmo" te intimide. Solo te están preguntando por el exponente.

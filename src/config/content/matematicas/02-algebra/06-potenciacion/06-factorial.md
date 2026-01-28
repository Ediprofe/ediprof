---
title: "Factorial de un Número"
---

# **Factorial de un Número**

Imagina que tienes 3 libros favoritos y quieres ordenarlos en una repisa. ¿De cuántas formas distintas puedes hacerlo? Al intentar contar todas las combinaciones posibles, descubres una operación matemática fundamental para el conteo y la probabilidad.

Esa operación que multiplica números en escalera descendente se llama **Factorial**.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa el símbolo $!$ en matemáticas.
- Cómo calcular factoriales de números pequeños y grandes.
- Por qué el factorial de cero es 1 ($0! = 1$).
- Cómo simplificar divisiones de factoriales sin usar calculadora.

---

## 📚 El Concepto: Ordenando cosas

Vamos a resolver el problema de los libros de forma inductiva.

### 1. Con 1 libro
Solo hay **1** forma de ponerlo.

$$
1 = 1
$$

### 2. Con 2 libros (A y B)
Puedes poner A-B o B-A. Son **2** formas.

$$
2 \times 1 = 2
$$

### 3. Con 3 libros (A, B y C)
Para la primera posición tienes 3 opciones. Para la segunda te quedan 2. Para la última solo 1.

$$
3 \times 2 \times 1 = 6
$$

### 4. Con 4 libros
Siguiendo la lógica:

$$
4 \times 3 \times 2 \times 1 = 24
$$

A este patrón de multiplicar un número por todos sus anteriores hasta llegar al 1 lo llamamos **Factorial** y se escribe con un signo de exclamación ($n!$).

---

## 📝 Definición Formal

El factorial de un número entero positivo $n$ es el producto de todos los enteros positivos desde $n$ hasta $1$.

**Fórmula:**

$$
n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1
$$

### Casos Especiales Importantes

Hay dos valores que debes memorizar por convención matemática (para que las fórmulas funcionen):

**Factorial de 1:**

$$
1! = 1
$$

**Factorial de 0:**

$$
0! = 1
$$

> 💡 **Nota:** ¡No es cero! Si fuera cero, muchas fórmulas de probabilidad se romperían.

---

## ⚡ Propiedad Clave: La Recursividad

Observa esto con atención. Calculemos $5!$:

$$
5! = 5 \times \underbrace{4 \times 3 \times 2 \times 1}_{Esto es 4!}
$$

Entonces podemos escribir:

$$
5! = 5 \times 4!
$$

**Regla General:**
Cualquier factorial se puede escribir como el número multiplicado por el factorial del anterior.

$$
n! = n \times (n-1)!
$$

Esta propiedad es **el truco secreto** para simplificar fracciones.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo directo

Calcula el valor de $6!$.

**Razonamiento:**
Multiplicamos desde el 6 bajando hasta el 1.

$$
6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1
$$

$$
6! = 720
$$

**Resultado:**

$$
\boxed{720}
$$

---

### Ejemplo 2: Simplificación de fracciones (El truco)

Simplifica la expresión $\frac{8!}{6!}$.

**Razonamiento:**
No calcules $8!$ (40,320) y luego dividas. Usa la propiedad recursiva.
Desarrolla el $8!$ solo hasta llegar al $6!$ para poder cancelar.

$$
\frac{8!}{6!} = \frac{8 \times 7 \times 6!}{6!}
$$

Cancelamos $6!$ arriba y abajo:

$$
= 8 \times 7
$$

$$
= 56
$$

**Resultado:**

$$
\boxed{56}
$$

---

### Ejemplo 3: Simplificación con variables

Simplifica la expresión $\frac{n!}{(n-1)!}$.

**Razonamiento:**
Aplicamos la misma lógica. El de arriba ($n$) es mayor que el de abajo ($n-1$). Desarrollamos el de arriba.

$$
\frac{n \times (n-1)!}{(n-1)!}
$$

Cancelamos $(n-1)!$:

$$
= n
$$

**Resultado:**

$$
\boxed{n}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el valor de $4!$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
4! = 4 \times 3 \times 2 \times 1
$$

$$
= 24
$$

**Resultado:**
$$
\boxed{24}
$$

</details>

### Ejercicio 2
Calcula el valor de $\frac{5!}{3!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{5 \times 4 \times 3!}{3!}
$$

$$
= 5 \times 4
$$

**Resultado:**
$$
\boxed{20}
$$

</details>

### Ejercicio 3
Calcula $3! + 0!$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Recordamos que $3! = 6$ y $0! = 1$.

$$
6 + 1
$$

**Resultado:**
$$
\boxed{7}
$$

</details>

### Ejercicio 4
Simplifica $\frac{10!}{8!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{10 \times 9 \times 8!}{8!}
$$

$$
= 10 \times 9
$$

**Resultado:**
$$
\boxed{90}
$$

</details>

### Ejercicio 5
Simplifica $\frac{12!}{10! \cdot 2!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{12 \times 11 \times 10!}{10! \times (2 \times 1)}
$$

$$
= \frac{12 \times 11}{2}
$$

$$
= \frac{132}{2}
$$

**Resultado:**
$$
\boxed{66}
$$

</details>

### Ejercicio 6
Simplifica la expresión $\frac{(n+2)!}{(n+1)!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Desarrollamos el mayor ($n+2$) hasta llegar al menor ($n+1$).

$$
\frac{(n+2) \times (n+1)!}{(n+1)!}
$$

$$
= n+2
$$

**Resultado:**
$$
\boxed{n+2}
$$

</details>

### Ejercicio 7
Calcula $\frac{7! - 6!}{5!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Podemos separar la fracción o factorizar.
Opción 1 (separar):

$$
\frac{7!}{5!} - \frac{6!}{5!}
$$

$$
= (7 \times 6) - 6
$$

$$
= 42 - 6
$$

**Resultado:**
$$
\boxed{36}
$$

</details>

### Ejercicio 8
Simplifica $\frac{n!}{(n-2)!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Desarrollamos $n!$ dos pasos hasta llegar a $(n-2)!$.

$$
\frac{n \times (n-1) \times (n-2)!}{(n-2)!}
$$

$$
= n(n-1)
$$

$$
= n^2 - n
$$

**Resultado:**
$$
\boxed{n(n-1)}
$$

</details>

### Ejercicio 9
Si $(x+1)! = 6$, halla el valor de $x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sabemos que $3! = 6$.
Por tanto:

$$
x + 1 = 3
$$

$$
x = 2
$$

**Resultado:**
$$
\boxed{2}
$$

</details>

### Ejercicio 10
Calcula $\frac{100!}{99!}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{100 \times 99!}{99!}
$$

$$
= 100
$$

**Resultado:**
$$
\boxed{100}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula / Valor |
|----------|-----------------|
| **Definición** | $n! = n \times (n-1) \times \dots \times 1$ |
| **Cero Factorial** | $0! = 1$ |
| **Propiedad Recursiva** | $n! = n \times (n-1)!$ |
| **Simplificación** | Desarrollar el mayor hasta alcanzar el menor |

> El factorial es la base para contar combinaciones y entender el Binomio de Newton. Recuerda siempre simplificar antes de multiplicar números gigantes.

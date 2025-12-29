# Cuadrado de un Binomio


## 🎯 ¿Qué vas a aprender?

- A identificar qué es un producto notable y por qué ahorra tiempo.
- La regla de oro para calcular el cuadrado de una suma.
- El truco para el cuadrado de una resta sin fallar en los signos.
- A visualizar gráficamente por qué la fórmula funciona.

---

## 🏗️ ¿Qué es un Producto Notable?

En álgebra, multiplicar polinomios puede ser un proceso largo y tedioso. Sin embargo, existen ciertas multiplicaciones que aparecen tan seguido que sus resultados siguen un patrón fijo.

A estos patrones los llamamos **productos notables**. Son como "atajos" matemáticos que nos permiten escribir el resultado directamente, ahorrándonos mucho tiempo y evitando errores de cálculo.

---

## 🟦 El Cuadrado de una Suma

Para elevar al cuadrado cualquier suma, aplicamos la siguiente regla:

| Identidad | Fórmula | Resultado |
|-----------|---------|-----------|
| **Cuadrado de una Suma** | $(a + b)^2$ | $a^2 + 2ab + b^2$ |

![Representación geométrica del cuadrado de una suma](/images/matematicas/algebra/productos-notables/cuadrado-suma-teoria.svg)

> **Regla de oro:** El cuadrado de la suma es igual al primer término al cuadrado, más el doble del producto del primero por el segundo, más el segundo término al cuadrado.

---

### **¿Por qué funciona? (La explicación geométrica)**

Imagina que tienes un cuadrado de lado $a$ y decides ampliarlo agregándole una distancia $b$. El nuevo lado será $(a+b)$, y el área total del cuadrado resultante será $(a+b)^2$.

Si observamos la imagen de arriba, vemos que el área total se compone de cuatro piezas:
1.  Un cuadrado grande de área $a^2$.
2.  Un cuadrado pequeño de área $b^2$.
3.  Dos rectángulos iguales, cada uno con área $ab$.

Al sumar todas estas piezas, obtenemos la fórmula: $a^2 + ab + ab + b^2 = a^2 + 2ab + b^2$.

### **Ejemplo: Ampliando el área**

Calcula el desarrollo de: $(x + 3)^2$

![Ejemplo visual del cuadrado de una suma con x y 3](/images/matematicas/algebra/productos-notables/cuadrado-suma-ejemplo.svg)

**Razonamiento:**
1.  Elevamos el **primer término** ($x$) al cuadrado: $x^2$.
2.  Calculamos el **doble del producto** de ambos ($2 \cdot x \cdot 3$): $6x$.
3.  Elevamos el **segundo término** ($3$) al cuadrado: $3^2 = 9$.
4.  Sumamos todas las piezas resultantes.

**Resultado:** $\boxed{x^2 + 6x + 9}$


---

## 🟥 El Cuadrado de una Resta

Cuando restamos en el binomio, la regla cambia ligeramente en el signo del término central:

| Identidad | Fórmula | Resultado |
|-----------|---------|-----------|
| **Cuadrado de una Resta** | $(a - b)^2$ | $a^2 - 2ab + b^2$ |

![Representación geométrica del cuadrado de una resta](/images/matematicas/algebra/productos-notables/cuadrado-resta-teoria.svg)

> **Regla de oro:** El cuadrado de la resta es igual al primer término al cuadrado, **menos** el doble del producto del primero por el segundo, **más** el segundo término al cuadrado.

---

### **¿Por qué funciona? (La explicación geométrica)**

Si tenemos un cuadrado grande de lado $a$, su área total es $a^2$. Si queremos encontrar el área de un cuadrado más pequeño de lado $(a-b)$, debemos "recortar" tiras del cuadrado original.

Como se ve en la imagen:
1. Empezamos con el área total $a^2$.
2. Restamos dos rectángulos de área $ab$.
3. Al hacer esto, hemos restado el cuadradito de la esquina ($b^2$) **dos veces**.
4. Por eso, debemos sumar $b^2$ una vez para compensar.

Esto nos da: $a^2 - 2ab + b^2$.

---

### **Ejemplo: El Caso de la Diferencia**

Calcula el desarrollo de:

$$
(x - 2)^2
$$

![Ejemplo visual del cuadrado de una resta con x y 2](/images/matematicas/algebra/productos-notables/cuadrado-resta-ejemplo.svg)

**Razonamiento:**

1. Cuadrado del **primero**:
$$
(x)^2 = x^2
$$

2. **Doble** del primero por el segundo:
$$
2 \cdot (x) \cdot (2) = 4x
$$
Como es una resta, este término será negativo ($-4x$).

3. Cuadrado del **segundo**:
$$
(2)^2 = 4
$$
(siempre positivo).

**Resultado:**

$$
\boxed{x^2 - 4x + 4}
$$

⚠️ **Cuidado:** Un error muy común es pensar que $(a-b)^2 = a^2 - b^2$. ¡Nunca te olvides del término central $-2ab$!

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Con dos variables

Calcula:

$$
(3x + 2y)^2
$$

**Datos:**
- Primer término: $3x$
- Segundo término: $2y$

**Razonamiento:**

1. Cuadrado del primero:
$$
(3x)^2 = 9x^2
$$

2. Doble del primero por el segundo:
$$
2 \cdot (3x) \cdot (2y) = 12xy
$$

3. Cuadrado del segundo:
$$
(2y)^2 = 4y^2
$$

**Resultado:**

$$
\boxed{9x^2 + 12xy + 4y^2}
$$

---

### Ejemplo 2: Con fracciones

Desarrolla:

$$
\left(x - \frac{1}{2}\right)^2
$$

**Datos:**
- Primer término: $x$
- Segundo término: $\frac{1}{2}$

**Razonamiento:**

1. Cuadrado del primero:
$$
x^2
$$

2. Doble del primero por el segundo:
$$
2 \cdot x \cdot \frac{1}{2} = 1x
$$
(negativo debido a la resta).

3. Cuadrado del segundo:
$$
\left(\frac{1}{2}\right)^2 = \frac{1}{4}
$$

**Resultado:**

$$
\boxed{x^2 - x + \frac{1}{4}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el resultado de: $(x + 4)^2$

<details>
<summary>Ver solución</summary>

**Datos:** $a = x$, $b = 4$.

**Razonamiento:** Aplicamos $(a+b)^2 = a^2 + 2ab + b^2$:

$$
x^2 + 2(x)(4) + 4^2
$$

**Resultado:** 

$$
\boxed{x^2 + 8x + 16}
$$

</details>

### Ejercicio 2
Desarrolla: $(a - 6)^2$

<details>
<summary>Ver solución</summary>

**Datos:** $a = a$, $b = 6$.

**Razonamiento:** Aplicamos el cuadrado de la resta:

$$
a^2 - 2(a)(6) + 6^2
$$

**Resultado:**

$$
\boxed{a^2 - 12a + 36}
$$

</details>

### Ejercicio 3
Resuelve: $(5x + 1)^2$

<details>
<summary>Ver solución</summary>

**Datos:** Primer término $5x$, segundo constante $1$.

**Razonamiento:** 

$$
(5x)^2 + 2(5x)(1) + 1^2
$$

**Resultado:**

$$
\boxed{25x^2 + 10x + 1}
$$

</details>

### Ejercicio 4
Calcula: $(3m - 2n)^2$

<details>
<summary>Ver solución</summary>

**Datos:** Términos $3m$ y $2n$.

**Razonamiento:**

$$
(3m)^2 - 2(3m)(2n) + (2n)^2
$$

**Resultado:**

$$
\boxed{9m^2 - 12mn + 4n^2}
$$

</details>

### Ejercicio 5
Desarrolla: $(x^2 + 3)^2$

<details>
<summary>Ver solución</summary>

**Datos:** El primer término ya tiene exponente ($x^2$).

**Razonamiento:**

$$
(x^2)^2 + 2(x^2)(3) + 3^2
$$

Aplicamos potencia de potencia:

**Resultado:**

$$
\boxed{x^4 + 6x^2 + 9}
$$

</details>

### Ejercicio 6
Resuelve: $(x - \frac{1}{3})^2$

<details>
<summary>Ver solución</summary>

**Datos:** Segundo término una fracción.

**Razonamiento:**

$$
x^2 - 2(x)\left(\frac{1}{3}\right) + \left(\frac{1}{3}\right)^2
$$

**Resultado:**

$$
\boxed{x^2 - \frac{2}{3}x + \frac{1}{9}}
$$

</details>

### Ejercicio 7
Calcula: $(10 + 2a)^2$

<details>
<summary>Ver solución</summary>

**Datos:** $a = 10, b = 2a$.

**Razonamiento:**

$$
10^2 + 2(10)(2a) + (2a)^2
$$

**Resultado:**

$$
\boxed{100 + 40a + 4a^2}
$$

</details>

### Ejercicio 8
Desarrolla: $(4xy - 1)^2$

<details>
<summary>Ver solución</summary>

**Datos:** Término compuesto $4xy$.

**Razonamiento:**

$$
(4xy)^2 - 2(4xy)(1) + 1^2
$$

**Resultado:**

$$
\boxed{16x^2y^2 - 8xy + 1}
$$

</details>

### Ejercicio 9
Calcula el área de un cuadrado de lado $(x + 7)$.

<details>
<summary>Ver solución</summary>

**Datos:** Lado $L = x + 7$.

**Razonamiento:** El área es $L^2$. Por tanto:

$$
(x+7)^2 = x^2 + 14x + 49
$$

**Resultado:**

$$
\boxed{x^2 + 14x + 49}
$$

</details>

### Ejercicio 10
Simplifica la expresión: $(x + 2)^2 - x^2$

<details>
<summary>Ver solución</summary>

**Datos:** Resta de polinomios.

**Razonamiento:** Desarrollamos el cuadrado:

$$
x^2 + 4x + 4
$$

Luego restamos $x^2$. Los términos $x^2$ se eliminan.

**Resultado:**

$$
\boxed{4x + 4}
$$

</details>

---

## 🔑 Resumen

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **Producto Notable** | Multiplicación con patrón fijo que se resuelve por regla. | $(a+b)^2$ |
| **Cuadrado Suma** | $(a+b)^2 = a^2 + 2ab + b^2$ | $(x+3)^2 = x^2+6x+9$ |
| **Cuadrado Resta** | $(a-b)^2 = a^2 - 2ab + b^2$ | $(x-3)^2 = x^2-6x+9$ |
| **Error Fatal** | Decir que $(a+b)^2 = a^2 + b^2$. | ¡Falta el $2ab$! |

> Dominar estos patrones es la clave para simplificar el álgebra y resolver ecuaciones complejas con rapidez y precisión.

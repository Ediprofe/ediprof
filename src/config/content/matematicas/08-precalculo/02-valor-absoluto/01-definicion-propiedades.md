---
title: "Definición y Propiedades del Valor Absoluto"
---

# Definición y Propiedades del Valor Absoluto

El valor absoluto es una de las herramientas más útiles del precálculo. Aparece en distancias, errores de medición, y es fundamental para entender límites en cálculo.

---

## 🎯 ¿Qué vas a aprender?

- La definición formal del valor absoluto
- Interpretación geométrica como distancia
- Propiedades algebraicas fundamentales
- Cómo simplificar expresiones con valor absoluto

---

## 📖 Definición del valor absoluto

El **valor absoluto** de un número real $x$, denotado $|x|$, se define por partes:

$$
|x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}
$$

### 💡 ¿Por qué $-x$ cuando $x$ es negativo?

Si $x = -5$, entonces $-x = -(-5) = 5$, que es positivo.

El valor absoluto siempre "quita el signo negativo".

---

## 📖 Interpretación geométrica

El valor absoluto de $x$ representa la **distancia** de $x$ al origen (cero) en la recta numérica.

```
        |−5| = 5           |3| = 3
←━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━→
    -5          0              3

    ←━━━━ 5 ━━━━→              ←━ 3 ━→
```

### Distancia entre dos puntos

La distancia entre $a$ y $b$ en la recta numérica es:

$$
d(a, b) = |a - b| = |b - a|
$$

**Ejemplo:** La distancia entre $-3$ y $5$ es:
$$
|-3 - 5| = |-8| = 8 \quad \text{o equivalentemente} \quad |5 - (-3)| = |8| = 8
$$

---

## 📊 Propiedades del valor absoluto

| Propiedad | Fórmula | Ejemplo |
|-----------|---------|---------|
| No negatividad | $\|x\| \geq 0$ | $\|-7\| = 7 \geq 0$ |
| Identidad positiva | $\|x\| = 0 \Leftrightarrow x = 0$ | $\|0\| = 0$ |
| Simetría | $\|-x\| = \|x\|$ | $\|-4\| = \|4\| = 4$ |
| Producto | $\|xy\| = \|x\| \cdot \|y\|$ | $\|(-3)(2)\| = \|-3\| \cdot \|2\| = 6$ |
| Cociente | $\left\|\frac{x}{y}\right\| = \frac{\|x\|}{\|y\|}$ (si $y \neq 0$) | $\left\|\frac{-8}{2}\right\| = \frac{8}{2} = 4$ |
| Desigualdad triangular | $\|x + y\| \leq \|x\| + \|y\|$ | $\|3 + (-5)\| = 2 \leq 3 + 5 = 8$ |

---

## 📖 Propiedad del cuadrado

Una propiedad muy útil es la relación con el cuadrado:

$$
|x|^2 = x^2 \quad \text{y} \quad |x| = \sqrt{x^2}
$$

**Ejemplo:** $|-4|^2 = 16 = (-4)^2$ ✓

Esta propiedad nos permite eliminar valores absolutos cuando trabajamos con cuadrados.

---

## ⚙️ Ejemplo 1: Evaluar valores absolutos

Calcula el valor de cada expresión:

a) $|5 - 9|$
b) $|3 - \pi|$ (sabiendo que $\pi \approx 3.14$)
c) $|x - 2|$ cuando $x = -1$

**Soluciones:**

a) $|5 - 9| = |-4| = 4$

b) Como $3 < \pi$, entonces $3 - \pi < 0$:
   $$|3 - \pi| = -(3 - \pi) = \pi - 3$$

c) $|-1 - 2| = |-3| = 3$

---

## ⚙️ Ejemplo 2: Simplificar con propiedades

Simplifica las siguientes expresiones:

a) $|(-3)^4|$
b) $\frac{|12|}{|-4|}$
c) $|x^2 + 1|$

**Soluciones:**

a) $|(-3)^4| = |81| = 81$

   También podemos usar la propiedad del producto:
   $|(-3)^4| = |-3|^4 = 3^4 = 81$

b) $\frac{|12|}{|-4|} = \frac{12}{4} = 3$

c) Como $x^2 \geq 0$, entonces $x^2 + 1 \geq 1 > 0$ siempre.
   
   Por lo tanto: $|x^2 + 1| = x^2 + 1$

---

## ⚙️ Ejemplo 3: Desigualdad triangular

Verifica la desigualdad triangular para $x = 4$ y $y = -7$:

$$|x + y| \leq |x| + |y|$$

**Solución:**

- $|x + y| = |4 + (-7)| = |-3| = 3$
- $|x| + |y| = |4| + |-7| = 4 + 7 = 11$

Verificamos: $3 \leq 11$ ✓

---

## ⚙️ Ejemplo 4: Simplificar $|x - a|$ según el valor de $x$

Expresar $|x - 3|$ sin valor absoluto si:

a) $x = 5$
b) $x = 1$
c) $x \geq 3$
d) $x < 3$

**Soluciones:**

a) $|5 - 3| = |2| = 2$

b) $|1 - 3| = |-2| = 2$

c) Si $x \geq 3$, entonces $x - 3 \geq 0$:
   $$|x - 3| = x - 3$$

d) Si $x < 3$, entonces $x - 3 < 0$:
   $$|x - 3| = -(x - 3) = 3 - x$$

---

## 📖 Casos particulares importantes

### Caso 1: $|x - a|$ representa distancia

$|x - a|$ es la distancia entre $x$ y el punto $a$.

- $|x - 5| = 3$ significa que $x$ está a distancia 3 de 5, es decir, $x = 2$ o $x = 8$.

### Caso 2: $|x| = x$ cuando $x \geq 0$

Si sabemos que una expresión es siempre no negativa, podemos quitar el valor absoluto directamente.

**Ejemplo:** $|x^2| = x^2$ porque $x^2 \geq 0$ siempre.

### Caso 3: $|f(x)| = |g(x)|$ implica casos

Si $|A| = |B|$, entonces $A = B$ o $A = -B$.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Evalúa:

a) $|-12| + |7|$
b) $|(-2)^3|$
c) $|4 - 10| - |10 - 4|$

<details>
<summary>Ver soluciones</summary>

a) $12 + 7 = 19$

b) $|(-2)^3| = |-8| = 8$

c) $|-6| - |6| = 6 - 6 = 0$
</details>

---

**Ejercicio 2:** Simplifica sin valor absoluto:

a) $|x|$ si $x = -8$
b) $|2x - 6|$ si $x > 3$
c) $|x + 4|$ si $x < -4$

<details>
<summary>Ver soluciones</summary>

a) $|-8| = 8$

b) Si $x > 3$, entonces $2x > 6$, así que $2x - 6 > 0$:
   $|2x - 6| = 2x - 6$

c) Si $x < -4$, entonces $x + 4 < 0$:
   $|x + 4| = -(x + 4) = -x - 4$
</details>

---

**Ejercicio 3:** Encuentra todos los valores de $x$ que satisfacen:

a) $|x| = 7$
b) $|x - 4| = 5$
c) $|2x + 1| = 9$

<details>
<summary>Ver soluciones</summary>

a) $x = 7$ o $x = -7$

b) $x - 4 = 5$ o $x - 4 = -5$
   
   $x = 9$ o $x = -1$

c) $2x + 1 = 9$ o $2x + 1 = -9$
   
   $x = 4$ o $x = -5$
</details>
